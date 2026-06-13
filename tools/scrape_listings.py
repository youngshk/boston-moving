#!/usr/bin/env python3
"""
Alewife 시장조사용 공식 사이트 스크래퍼 (Playwright)

다수 단지 공식 사이트가 Cloudflare/JS 위젯 뒤에 있어 일반 fetch(403/빈 HTML)로는 가격을
못 읽는다. 진짜 헤드리스 브라우저(Chromium)로 렌더링하면 Cloudflare managed-challenge를
통과하고, 동시에 SightMap/Knock/RentCafe 위젯이 호출하는 유닛 단위 JSON API 응답까지
가로채 저장한다.

사용법:
    pip install playwright && playwright install chromium
    python tools/scrape_listings.py            # 전체 스크랩 → out/ 에 .txt(본문) + .json(API)
    python tools/scrape_listings.py --parse     # 저장된 out/*.json 에서 유닛 표 출력

산출물(out/<slug>.txt, out/<slug>.json)을 읽어 docs/ 의 가격·공실·프로모션을 갱신한다.
가격은 변동요금이라 자주 바뀌므로, 갱신 시 조사 기준일을 docs 상단에 함께 기록할 것.
"""
import argparse
import json
import os
import re
from playwright.sync_api import sync_playwright

OUT = os.path.join(os.path.dirname(__file__), "out")
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")

# (slug, primary_url, [fallback_urls])
TARGETS = [
    ("cambridge_park", "https://www.livecambridgepark.com/floorplans", ["https://www.livecambridgepark.com/availability"]),
    ("urbane", "https://urbaneatalewife.com/floorplans/", ["https://urbaneatalewife.com/availability/"]),
    ("luxe", "https://www.luxealewife.com/floorplans", []),
    ("hanover", "https://www.hanoveralewife.com/cambridge/hanover-alewife/floor-plans", []),
    ("windsor_cp", "https://www.rentcafe.com/apartments/ma/cambridge/windsor-at-cambridge-park/default.aspx", []),
    ("fuse", "https://www.fusecambridge.com/floorplans", ["https://www.fusecambridge.com/"]),
    ("vox", "https://www.rentcafe.com/apartments/ma/cambridge/vox-on-two/default.aspx", []),
    ("tempo", "https://www.tempocambridge.com/floorplans", ["https://www.tempocambridge.com/availability"]),
    ("atmark", "https://liveatmark.com/floorplans/", []),
    ("the_brook", "https://thebrookcambridge.com/availability", []),
    ("laurent", "https://www.livethelaurent.com/floor-plans/", []),
    ("603concord", "https://www.603concord.com/floorplans", []),
    ("605concord", "https://www.605concord.com/floorplans", []),
    ("park87", "https://www.park87.com/floorplans", []),
    ("park77", "https://www.park77aptscambridge.com/floorplans", []),
    ("royal_belmont", "https://www.harborgroupmanagement.com/apartments/ma/belmont/the-royal-belmont/floor-plans", []),
    ("walden_park", "https://www.equityapartments.com/boston/porter-square/walden-park-apartments", []),
    ("chester_st", "https://chesterstreetapartments.com/floor-plans/", ["https://chesterstreetapartments.com/"]),
]

# JSON API 응답 중 가격/유닛 관련만 저장하기 위한 URL 키워드
KW = ("availab", "floorplan", "floor-plan", "rent", "unit", "pricing", "sightmap", "rates", "knockrentals")


def _settle(page, url):
    r = page.goto(url, wait_until="domcontentloaded", timeout=45000)
    page.wait_for_timeout(5000)  # Cloudflare challenge + 위젯 로딩
    try:
        for _ in range(4):
            page.mouse.wheel(0, 2200)
            page.wait_for_timeout(900)
    except Exception:
        pass
    page.wait_for_timeout(2500)
    return (r.status if r else None), page.inner_text("body")


def scrape():
    os.makedirs(OUT, exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, args=["--disable-blink-features=AutomationControlled"])
        for slug, url, fbs in TARGETS:
            bucket = []
            ctx = browser.new_context(user_agent=UA, locale="en-US", viewport={"width": 1400, "height": 1000})
            page = ctx.new_page()

            def on_resp(resp, b=bucket):
                try:
                    ct = (resp.headers or {}).get("content-type", "")
                    if "json" in ct and any(k in resp.url.lower() for k in KW):
                        b.append({"url": resp.url, "body": resp.text()[:1_000_000]})
                except Exception:
                    pass

            page.on("response", on_resp)
            status, body = None, ""
            for cand in [url] + fbs:
                try:
                    status, body = _settle(page, cand)
                    if status and status < 400 and len(body) > 1500:
                        url = cand
                        break
                except Exception as e:
                    print(f"  {slug} {cand} -> {e}")
            with open(f"{OUT}/{slug}.txt", "w") as f:
                f.write(f"URL: {url}\nSTATUS: {status}\n\n{body}")
            if bucket:
                with open(f"{OUT}/{slug}.json", "w") as f:
                    json.dump(bucket, f)
            prices = len(set(re.findall(r"\$[0-9],[0-9]{3}", body)))
            print(f"{slug:14} status={status} bodylen={len(body):6} prices={prices:2} jsonAPI={len(bucket)}")
            ctx.close()
        browser.close()


def parse():
    """저장된 JSON 에서 Knock units_data / SightMap units 를 표로 출력."""
    for fn in sorted(os.listdir(OUT)):
        if not fn.endswith(".json"):
            continue
        slug = fn[:-5]
        data = json.load(open(f"{OUT}/{fn}"))
        for d in data:
            u = d["url"]
            try:
                j = json.loads(d["body"])
            except Exception:
                continue
            # Knock
            if u.endswith("/units") and "units_data" in j:
                ud = j["units_data"]
                lay = {l["id"]: l for l in ud.get("layouts", [])}
                print(f"\n### {slug} (Knock, {len(ud.get('units', []))} units)")
                for unit in sorted(ud.get("units", []), key=lambda x: (x.get("bedrooms", 9), x.get("price") or 0)):
                    L = lay.get(unit.get("layoutId"), {})
                    print(f"  {unit.get('bedrooms')}BR {str(L.get('name'))[:10]:10} {L.get('area')}sf "
                          f"#{unit.get('name')} ${unit.get('price')} avail={unit.get('availableOn')}")
            # SightMap
            if "/sightmaps/" in u and isinstance(j.get("data"), dict) and j["data"].get("units"):
                dd = j["data"]
                fps = {f["id"]: f for f in dd.get("floor_plans", [])}
                print(f"\n### {slug} (SightMap, {len(dd['units'])} available units)")
                for unit in dd["units"]:
                    fp = fps.get(unit["floor_plan_id"], {})
                    print(f"  {fp.get('bedroom_count')}BR #{unit.get('display_unit_number')} "
                          f"{unit.get('display_area')} ${unit.get('price')} avail={unit.get('display_available_on')}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--parse", action="store_true", help="저장된 out/*.json 파싱만 수행")
    args = ap.parse_args()
    if args.parse:
        parse()
    else:
        scrape()
