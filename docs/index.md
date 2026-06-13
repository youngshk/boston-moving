# Alewife 역 인근 아파트 시장조사

캠브리지 **Alewife** 역(Red Line 종점) 도보권을 중심으로, 스튜디오·1베드 위주의 렌탈 시장을 정리했습니다. Alewife 바로 인근부터 Fresh Pond / Cambridge Highlands, 그리고 바로 인접한 East Belmont(Acorn Park)까지 포함합니다.

📍 단지 위치는 **[지도](map.md)**, 소득제한 유닛은 **[어포더블](affordable.md)** 페이지에서 한눈에 볼 수 있습니다.

!!! warning "데이터 기준 / 주의"
    - **조사 기준일: 2026-06-13** (직전 회차 2026-06-06 대비 갱신). 렌탈 가격과 프로모션은 거의 매주 바뀝니다. 아래 숫자는 "조사 시점의 최신 리스팅" 기준이며, **계약 전 반드시 리싱 오피스에 전화로 재확인**하세요.
    - 가격은 대부분 base rent 기준입니다. 일부 단지(Urbane 등)는 필수 부대비용을 포함한 "total monthly price"로 표기합니다.
    - 06-13 회차에서 **Cloudflare로 막혔던 공식 사이트를 헤드리스 브라우저(Playwright)로 우회해 공식 라이브 데이터를 직접 확인**했습니다(**(공식✓)** 표기). 단 가격 위젯 밖 항목(주차비 등)은 여전히 미공개("n/p")이며, Hanover·Tempo·The Brook는 가격이 위젯에 안 떠 aggregator 값을 유지했습니다. 출처를 각 항목에 표기했습니다.
    - 프로모션은 공식 사이트 배너 기준을 우선했고, aggregator(Apartments.com 등)에만 있는 내용은 "미확인"으로 표시했습니다.

## 한눈에 보기 (핵심 요약)

| 구분 | 단지 |
|---|---|
| **Alewife에 가장 가까움** | Cambridge Park (도보 2-3분, 길 건너), Urbane (2-4분), Luxe (3-6분), Hanover (4-6분) |
| **가장 저렴한 스튜디오** | Chester St (~$2,200, 단 Davis Sq), **The Laurent (~$2,370, 06-13 인하)**, Walden Park (~$2,490, 공식✓), Atmark (~$2,575) |
| **가장 저렴한 1BR** | The Laurent (~$2,767), Atmark (~$2,817, 공식✓), Walden Park (~$2,860, 공식✓), Royal Belmont (~$2,870, 공식✓) |
| **가장 좋은 사인업 보너스(공식 확인)** | The Royal Belmont (1개월 무료, 6/21 마감 임박), The Laurent ($1,000 off), **Luxe (1개월 무료+$99)**, **Atmark (1개월 무료)** |
| **어포더블(소득제한) 유닛** | The Laurent(~100세대) 등 다수 신축 — 신청은 케임브리지 시 CDD 풀 경유 → [어포더블](affordable.md) |
| **유틸리티 포함 혜택** | Cambridge Park(난방+쓰레기), 603·605·Park77(난방+온수), Walden Park(가스·물·난방·인터넷·케이블 등) |
| **주차비 공개된 곳** | Cambridge Park $100-150, The Laurent $250, The Brook $250, 603 Concord 차고$195/노상$155, Walden Park $175, Chester St $125 |
| **거주자 평점 최고 (라이브 Google)** | Hanover (4.8·519건, 신뢰도 최상), Vox on Two (4.7·150건), The Laurent (4.6·135건) |
| **평판 주의 / 부정 평** | Luxe·Tempo (3.6), Atmark (3.8, 택배도난), Royal Belmont (4.0이나 방음 혹평) / The Brook·605 Concord는 리뷰 1-2건뿐이라 평점 무의미 |

!!! tip "06-13 한 주간 핵심 변동"
    - **The Laurent 가격 약세** — 전 스튜디오 시작가 약 $157–168 인하, 1BR도 하향. 지금 협상 여지 큼.
    - **프로모션 격상** — Luxe·Atmark가 "미확인→공식 1개월 무료"로 확정. 603 Concord에 한정 특가 신규.
    - **Royal Belmont 1개월 무료 6/21 마감 임박**(8일 후).

!!! success "🔓 공식 라이브 재검증 완료 (Playwright)"
    Cloudflare로 막혔던 공식 사이트를 헤드리스 브라우저로 직접 렌더링하고 SightMap·Knock·RentCafe **유닛 단위 JSON API까지 확인**했습니다. 주요 정정:
    
    - **⚠️ Cambridge Park** — aggregator의 "스튜디오 ~$3,140 / 1BR $3,276"은 **부정확**. 공식엔 **스튜디오 가용 0, 1BR은 727sf $3,699부터**.
    - **Atmark 1BR $2,817부터**, **Walden Park 스튜디오 $2,490 / 1BR $2,860부터** (공식이 aggregator보다 저렴).
    - **Royal Belmont·Chester St** 전 유닛 호수·가격·입주일 확보. **605 Concord 스튜디오 입주일 6/19 확정**.

자세한 비교는 **[비교표](comparison.md)**, 위치는 **[지도](map.md)**, 소득제한은 **[어포더블](affordable.md)**, 프로모션·리퍼럴·시즌성은 **[사인업 보너스 & 시즌성](promotions.md)** 참고.

## 거리(Tier)별 분류

이 조사는 Alewife 역까지의 도보 거리 기준으로 4개 티어로 나눴습니다.

- **Tier 1 — Cambridgepark Dr 클러스터 (도보 2-6분):** Urbane, Luxe, Hanover, Cambridge Park. 역에서 가장 가깝고 가장 새 건물들. 가격대는 중상위.
- **Tier 2 — Concord Tpke / Fawcett St (도보 8-12분):** Vox on Two, Tempo, Atmark, The Brook. 가성비/세대수 많은 단지들.
- **Tier 3 — Cambridge Highlands / Fresh Pond (도보 10-15분):** The Laurent, 603 Concord, 605 Concord, Park87, Park77. 일부는 난방·온수 포함.
- **Tier 4 — Belmont / Porter (참고용):** The Royal Belmont(East Belmont, Rt-2 건너), Walden Park·Chester St(실제로는 Porter/Davis Square — Alewife와는 거리가 있음).

## 결론 (의사결정 가이드)

- **역과의 거리 최우선 + 유틸 포함** → **Cambridge Park** (길 건너, 난방·쓰레기 포함, 주차 $100-150). 단, 소형 유닛도 비싼 편이고 현재 프로모션 없음.
- **새 건물 + 공식 보너스** → **Luxe**(1개월 무료+보증금 $99, **06-13 공식 확인**) 또는 **Atmark**(1개월 무료, **공식 확인**). Urbane은 2주 무료가 공식엔 안 떠서(aggregator만) 전화 확인 권장.
- **가격 최우선** → **The Laurent**(스튜디오 ~$2,370부터로 06-13 인하 + $1,000 off, 공실 많아 협상 유리), Tier 2의 **Tempo / Atmark**, 또는 (Davis Sq 감수 시) **Chester St ~$2,200**.
- **확실한 1개월 무료를 지금 받고 싶다** → **The Royal Belmont**(6/21/26 입주 마감 임박) 또는 **The Laurent**($1,000 off, 24시간 내 신청), **Luxe·Atmark**(1개월 무료). 단 Royal Belmont는 East Belmont라 셔틀 의존.
- **어포더블(소득제한) 자격이 될 수도** → 연소득이 1인 ~$96k / 2인 ~$110k 이하라면 케임브리지 인클루저너리 대상일 수 있음. 시장가와 **병행 등록** 권장 → [어포더블](affordable.md).
