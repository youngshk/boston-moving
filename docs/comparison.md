# 비교표 (2026-06-13 갱신)

> 모든 숫자는 조사 시점 최신 리스팅 기준이며 base rent입니다. `n/p` = 공식 미공개(not published), `n/d` = 확인 불가(not determinable). 시작가(from)는 변동요금(dynamic) 범위의 하한일 수 있습니다.
>
> **2026-06-06 → 06-13 한 주간 변동은 각 행 끝 화살표/메모 참고.** 직전 회차(06-06) 수치는 git 히스토리로 보존됩니다.

!!! success "🔓 06-13 공식 라이브 재검증 (Playwright)"
    이번 회차는 **Cloudflare로 막혔던 공식 사이트를 헤드리스 브라우저(Playwright)로 직접 렌더링**하고, SightMap·Knock·RentCafe **유닛 단위 JSON API까지 가로채** 검증했습니다. 그 결과 일부 aggregator 수치가 **부정확**했음이 드러났습니다 — 특히 **Cambridge Park는 스튜디오가 실제로 가용 0이고 1BR도 $3,699부터**(aggregator의 $3,140/$3,276은 stale). **(공식✓)** 표기 = 이번에 공식 라이브로 확인. Hanover·Tempo·The Brook는 공식 페이지가 가격을 위젯 밖으로 노출하지 않아 aggregator 값 유지.

## 스튜디오 · 1베드 가격 / 크기

| 단지 | Tier | Alewife 도보 | 스튜디오 월세 | 스튜디오 크기 | 1BR 월세 | 1BR 크기 | 비고 (공식✓ = 06-13 라이브) |
|---|---|---|---|---|---|---|---|
| Cambridge Park | 1 | 2-3분 | **가용 없음** (공식✓) | (~698 sf) | **$3,699+** (727sf, 8월~) (공식✓) | 727 sf | ⚠️ aggregator $3,140/$3,276은 stale, **공식엔 스튜디오 0개** |
| Urbane at Alewife | 1 | 2-4분 | ~$2,969–3,099 | 517–556 sf | ~$3,007+ | 634–754 sf | 1BR 즉시입주 $3,007 신규 |
| Luxe at Alewife | 1 | 3-6분 | **$3,003+** (공식✓) | 576–636 sf | **$3,010/$3,325+** (공식✓) | 732–896 sf | 1개월 무료+$99 공식✓ |
| Hanover Alewife | 1 | 4-6분 | ~$2,780+ | ~574 sf | ~$3,092+ | 711–805 sf | 공식 위젯 가격 미노출, Zumper 기준 |
| Vox on Two | 2 | ~8분 | 가용 없음 (공식✓) | (620 sf) | **$3,048+** (공식✓) | 840–857 sf | 12세대 가용, 전부 1BR↑ |
| Tempo Cambridge | 2 | ~8–10분 | ~$2,635–2,725 | 502–515 sf | ~$2,956–3,166 | 626–837 sf | 공식 미렌더, ApartmentList 기준 |
| Atmark Cambridge | 2 | ~10–12분 | ~$2,575–2,717 | 569–588 sf | **$2,817+** (공식✓, 즉시) | 725–740 sf | 1개월 무료 공식✓ |
| The Brook | 2 | ~10–12분 | 없음 | — | $2,925–3,300 | 671–983 sf | #506 신규 추가 |
| The Laurent | 3 | ~10분 | **$2,370–2,626** (공식✓) | 451–525 sf | **$2,767+** (공식✓) | 583–838 sf | 전 스튜디오 ↓ $157–168, $1,000 off |
| 603 Concord | 3 | ~10–13분 | **$3,000** (7/2, 공식✓) | 401 sf | **$3,100** (7/5, 공식✓) | 813 sf | "전화 문의 특가" |
| 605 Concord | 3 | ~10–15분 | **$2,850 (6/19 확정, 공식✓)** | 512 sf | 문의(Micro 575/1BR 719) | 575–719 sf | 입주일 6/19로 확정 |
| Park87 | 3 | ~10–12분 | 없음 | — | **1BR Plus $3,100** (6/15, 공식✓) | 787 sf | 기본 1BR 가용 없음 |
| Park77 | 3 | ~10–15분 | 가용 없음 (공식✓) | 444 sf | 가용 없음 (공식✓) | 741 sf | 스튜디오·1BR 모두 공실 0 |
| The Royal Belmont | 4 | ~15–20분 | 가용 없음 (공식✓) | 596 sf | **$2,870–3,190** (공식✓) | 632–1,062 sf | 1BR 13세대(752sf ~$2,875×다수) |
| Walden Park *(Porter)* | 4 | ~25–30분 | **$2,490+** (공식✓) | 539 sf | **$2,860+** (공식✓) | 625–760 sf | 스튜디오3·1BR6 가용 |
| Chester Street *(Porter/Davis)* | 4 | ~30분+ | **$2,200–2,400** (공식✓) | 380 sf | 가용 없음 (공식✓) | — | 스튜디오 6세대, 최저가 |

## 보너스 · 주차 · 세탁기 · 유틸 · 무브인

| 단지 | 사인업 보너스 (2026-06-13) | 주차비 | In-unit 세탁/건조 | 유틸 포함 | 빠른 무브인 |
|---|---|---|---|---|---|
| Cambridge Park | 없음 | $100–150/월 | 예 (전 세대) | **난방·쓰레기** | 즉시(스튜디오 1세대) |
| Urbane at Alewife | 공식 "없음" / aggregator "2주 무료" *(상충·미확인)* | 차고 있음, n/p | 예 | 없음(서브미터) | 1BR 즉시(A06 #425), 스튜디오 6/20~ |
| Luxe at Alewife | **1개월 무료 + 보증금 $99** *(공식 RentCafe 확인)* | 있음, n/p | 예 | 없음 | 스튜디오 6/16~, 1BR 즉시(A19) |
| Hanover Alewife | 스튜디오 "최대 4주+1주 무료" / 1BR "$500"(공식) · Zumper "2주"(상충) | 차고(+필수 fee 일부 포함), n/p | 예 | 없음 | 문의 |
| Vox on Two | 없음 | 있음, n/p | 예 (full-size) | 없음 | 1BR 즉시(#330) |
| Tempo Cambridge | 없음 (3BR만 $1,000 off) | 차고/커버드, n/p | 예 (포함) | 없음 | 1BR 즉시(A7.1C #2305) |
| Atmark Cambridge | **1개월 무료** *(공식 RentCafe 확인, 혼선 해소)* | 차고+EV, n/p | 예 (front-load) | 없음 | 스튜디오 6/20~, 1BR 즉시 |
| The Brook | 공식 없음 / aggregator "노브로커피·1개월 무료" *(미확인)* | $250/월 차고 | 예 | n/p | 1BR 9/1 |
| The Laurent | **"투어 후 24시간 내 신청 시 $1,000 off"** (공식) | 예약 $250/월 | 예 (full-size) | n/p | 즉시~ (다수 공실) |
| 603 Concord | **"한정 특가 — 전화 문의"** (공식, 06-06 "No offers"에서 변경) | 차고 $195 / 노상 $155 | 예 (전 세대) | **난방·온수** | 스튜디오 7/2, 1BR 7/5 |
| 605 Concord | 명시 오퍼 없음 "전화 문의"(2BR 프로모 사라짐) | n/p (Alewife 무료 셔틀) | 예 | **난방·온수** | 스튜디오 6/19~6/30 |
| Park87 | "2BR 1개월 무료" + **"1BR 2주 무료"**(정황·상충) | 차고+노상, n/p | 예 (전 세대) | n/p | 1BR Plus 6/15 |
| Park77 | 공식 라이브에 스튜디오 프로모 미노출(aggregator엔 잔존) | 지하 차고+무료 EV, n/p | 예 | **난방·온수** | 공실 없음(문의) |
| The Royal Belmont | **"6/21/26까지 입주 시 1개월 무료"** (공식, 유지) | 차고, n/p | 예 (stackable) | n/p | 1BR 다수 (Norbert 10세대) |
| Walden Park *(Porter)* | 없음(보증금 특가 만료) | $175/월(추정) | 미확인 | **가스·물·난방·쓰레기·하수·케이블·인터넷** | 문의 |
| Chester Street *(Porter/Davis)* | **"1개월 무료 — 전 공실 대상"**(aggregator, 문구 확대) | $125/월 (세대당 1대) | 아니오 (공용 세탁실) | 난방·물 | 스튜디오 즉시~11월 |

!!! note "사인업 보너스 \"공식 / 미확인\"의 의미"
    **(공식)** = 단지 공식 사이트(또는 공식 RentCafe 피드) 배너에서 직접 확인. **(미확인)** = aggregator(Apartments.com 등)에만 있어 전화 확인 필요. 이번 회차에서 **Luxe·Atmark는 "미확인→공식 확인"으로 격상**되었고, **603 Concord는 새 "한정 특가"가 등장**했습니다.

!!! tip "어포더블(소득제한) 유닛은 별도"
    위는 모두 **시장가** 유닛 기준입니다. 같은 건물의 어포더블(소득제한) 유닛은 가격·신청 경로가 전혀 다릅니다 → **[어포더블 (소득제한)](affordable.md)** 페이지 참고.

## 거주자 평점 & 평판 (라이브 Google Maps)

> 아래 별점·리뷰 수는 **2026-06-06 Google Maps 직접 추출값**입니다(이번 06-13 회차에서는 가격·프로모션 위주로 갱신했고, 평점은 한 주 새 유의미하게 바뀌지 않으므로 직전 라이브 값을 유지). **리뷰 수가 적을수록(특히 한 자릿수) 평점 1개가 평균을 크게 흔드므로** 숫자를 그대로 신뢰하기 어렵습니다.

| 단지 | Google 평점 (리뷰수) | Google 리뷰 | 한 줄 평 |
|---|---|---|---|
| Hanover Alewife | **4.8 (519)** | [리뷰 보기](https://www.google.com/maps/search/Hanover+Alewife+130+Cambridgepark+Dr+Cambridge+MA) | 평점·리뷰량 모두 최상위. **가장 신뢰할 만함** |
| Vox on Two | **4.7 (150)** | [리뷰 보기](https://www.google.com/maps/search/Vox+on+Two+223+Concord+Turnpike+Cambridge+MA) | Tier 2 최고. 청결·스태프 호평 (단 층간소음) |
| The Laurent | **4.6 (135)** | [리뷰 보기](https://www.google.com/maps/search/The+Laurent+55+Wheeler+St+Cambridge+MA) | 리뷰량 많고 평점 높음. 수리 호평 / 택배도난·방음 |
| Urbane at Alewife | 4.5 (162) | [리뷰 보기](https://www.google.com/maps/search/Urbane+at+Alewife+50+Cambridgepark+Dr+Cambridge+MA) | 모던·스태프 호평 / 층간소음·엘베고장·택배도난 |
| Cambridge Park | 4.5 (274) | [리뷰 보기](https://www.google.com/maps/search/Cambridge+Park+Apartments+30+Cambridge+Park+Dr+Cambridge+MA) | 관리·위치 호평 / 건물 노후(2001) |
| Walden Park | 4.4 (118) | [리뷰 보기](https://www.google.com/maps/search/Walden+Park+Apartments+205+Walden+St+Cambridge+MA) | 스태프·커뮤니티 호평 / (과거)해충·소음 |
| The Royal Belmont | 4.0 (130) | [리뷰 보기](https://www.google.com/maps/search/The+Royal+Belmont+375+Acorn+Park+Dr+Belmont+MA) | 빠른 수리 / 방음 최악 평. (ApartmentRatings는 2.9) |
| Park77 | 3.9 (16) | [리뷰 보기](https://www.google.com/maps/search/Park77+Apartments+77+New+St+Cambridge+MA) | 청결·스태프 호평 / 배송·층간소음 |
| Atmark Cambridge | 3.8 (221) | [리뷰 보기](https://www.google.com/maps/search/Atmark+Cambridge+80+Fawcett+St+Cambridge+MA) | 위치 좋음 / 택배도난·관리전환 불만 |
| Park87 | 3.8 (6) ⚠️ | [리뷰 보기](https://www.google.com/maps/search/Park87+Apartments+87+New+St+Cambridge+MA) | 표본 작음. 위치 좋음 / 창호·방음 부실 |
| 603 Concord | 3.7 (6) ⚠️ | [리뷰 보기](https://www.google.com/maps/search/603+Concord+Apartments+Cambridge+MA) | 표본 매우 작음. 빠른 수리 / 게스트주차 |
| Luxe at Alewife | 3.6 (82) | [리뷰 보기](https://www.google.com/maps/search/Luxe+at+Alewife+80+Cambridgepark+Dr+Cambridge+MA) | **이 그룹 최저권.** 어메니티 / 화재경보·마감·벽 |
| Tempo Cambridge | 3.6 (115) | [리뷰 보기](https://www.google.com/maps/search/Tempo+Cambridge+203+Concord+Turnpike+Cambridge+MA) | 관리 호평/빌드품질·주차 비판 갈림 |
| 605 Concord | 1.5 (2) ⚠️ | [리뷰 보기](https://www.google.com/maps/search/605+Concord+at+Fresh+Pond+Cambridge+MA) | 신축(2025), 리뷰 2건뿐 — **평점 무의미** |
| The Brook | 1.0 (1) ⚠️ | [리뷰 보기](https://www.google.com/maps/search/The+Brook+Luxury+Apartments+95+Fawcett+St+Cambridge+MA) | 리뷰 1건뿐 — **평점 무의미** (별도 텍스트 리뷰는 부정적) |
| Chester Street | Google 등록 없음 | — | 검색 시 매칭되는 Google 플레이스 없음 (미평가) |

⚠️ = 리뷰 수가 한 자릿수~극소라 평점 신뢰 불가.

!!! warning "리뷰 데이터 주의"
    - **리뷰 수가 적은 곳(The Brook 1건, 605 Concord 2건, 603·Park87 6건)은 평점이 사실상 의미 없습니다.** 텍스트 리뷰 내용(상세 페이지)을 보세요.
    - **Chester Street**는 Google Maps에 매칭되는 플레이스가 없습니다(검색 시 뜨는 4.4는 Allston의 무관한 광고 매물이니 사용 금지).
    - **공통적으로 가장 많은 불만은 "층간/벽간 방음"과 "택배 도난"** — 거의 모든 단지에서 반복됩니다.
