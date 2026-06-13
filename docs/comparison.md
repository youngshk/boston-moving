# 비교표 (2026-06-13 갱신)

> 모든 숫자는 조사 시점 최신 리스팅 기준이며 base rent입니다. `n/p` = 공식 미공개(not published), `n/d` = 확인 불가(not determinable). 시작가(from)는 변동요금(dynamic) 범위의 하한일 수 있습니다.
>
> **2026-06-06 → 06-13 한 주간 변동은 각 행 끝 화살표/메모 참고.** 직전 회차(06-06) 수치는 git 히스토리로 보존됩니다.

!!! success "🔓 06-13 공식 라이브 재검증 (Playwright)"
    이번 회차는 **Cloudflare로 막혔던 공식 사이트를 헤드리스 브라우저(Playwright)로 직접 렌더링**하고, SightMap·Knock·RentCafe **유닛 단위 JSON API까지 가로채** 검증했습니다. 그 결과 일부 aggregator 수치가 **부정확**했음이 드러났습니다 — 특히 **Cambridge Park는 스튜디오가 실제로 가용 0이고 1BR도 $3,699부터**(aggregator의 $3,140/$3,276은 stale). **(공식✓)** 표기 = 이번에 공식 라이브로 확인. Hanover·Tempo·The Brook는 공식 페이지가 가격을 위젯 밖으로 노출하지 않아 aggregator 값 유지.

## 실측 도보 거리 (Alewife 역까지)

!!! warning "Tier ≠ 거리 순서 — 동네 클러스터로 묶은 것 (경계가 모호함)"
    Tier는 **거리 띠가 아니라 동네 묶음**입니다(Tier 2 = Concord Tpke·**Fawcett St**, Tier 3 = Cambridge Highlands·**Fresh Pond**). 이 묶음은 원래 "거리 이름" 기준이라 경계에서 어긋납니다:

    - **Atmark(Tier 2, 80 Fawcett St)와 The Laurent(Tier 3, 55 Wheeler St)는 사실상 같은 블록 — 직선 69m, 도보 3분 거리의 바로 옆 단지**입니다. 그런데 Tier가 갈린 건, Fawcett St는 원래 The Brook과 함께 "Concord Tpke/Fawcett 묶음(T2)"으로, Wheeler St·Concord Ave는 "Fresh Pond 묶음(T3)"으로 분류했기 때문입니다. **거리·환경상으론 둘을 같은 그룹으로 보는 게 맞습니다.**
    - 실제 거리도 역전됩니다 — **Atmark(T2) ~19분이 The Laurent(T3) ~16분·603/605/Park77·87(~14분)보다 멉니다.** The Brook(T2)도 ~20분.
    
    → **거리만 본다면 아래 표(실측 순)를, 동네 환경은 Atmark·The Brook을 Wheeler/Concord Ave(Fresh Pond) 쪽과 함께** 보세요.

아래는 각 단지 정문 좌표에서 **Alewife 역까지 실제 보행 네트워크 경로**를 측정한 값입니다(OpenStreetMap 기반 보행 라우팅, OSRM foot). 보행 속도 ~5km/h 가정. **Google 도보 길찾기 링크**로 직접 대조할 수 있습니다.

| 순위 | 단지 | Tier | 실측 도보거리 | 도보 시간 | Google 도보 |
|---|---|---|---|---|---|
| 1 | Luxe at Alewife | 1 | 397m (0.25mi) | ~5분 | [길찾기](https://www.google.com/maps/dir/?api=1&origin=42.39300,-71.14189&destination=42.39600,-71.14128&travelmode=walking) |
| 2 | Cambridge Park | 1 | 426m (0.26mi) | ~6분 | [길찾기](https://www.google.com/maps/dir/?api=1&origin=42.39401,-71.14311&destination=42.39600,-71.14128&travelmode=walking) |
| 3 | Urbane at Alewife | 1 | 492m (0.31mi) | ~7분 | [길찾기](https://www.google.com/maps/dir/?api=1&origin=42.39409,-71.14384&destination=42.39600,-71.14128&travelmode=walking) |
| 4 | Hanover Alewife | 1 | 563m (0.35mi) | ~8분 | [길찾기](https://www.google.com/maps/dir/?api=1&origin=42.39361,-71.14479&destination=42.39600,-71.14128&travelmode=walking) |
| 5 | Fuse Cambridge | 1 | 708m (0.44mi) | ~9분 | [길찾기](https://www.google.com/maps/dir/?api=1&origin=42.39544,-71.14757&destination=42.39600,-71.14128&travelmode=walking) |
| 6 | Windsor at Cambridge Park | 1 | 712m (0.44mi) | ~10분 | [길찾기](https://www.google.com/maps/dir/?api=1&origin=42.39450,-71.14772&destination=42.39600,-71.14128&travelmode=walking) |
| 7 | Tempo Cambridge | 2 | 1,017m (0.63mi) | ~14분 | [길찾기](https://www.google.com/maps/dir/?api=1&origin=42.40012,-71.15043&destination=42.39600,-71.14128&travelmode=walking) |
| 8 | Park77 | 3 | 1,022m (0.63mi) | ~14분 | [길찾기](https://www.google.com/maps/dir/?api=1&origin=42.38930,-71.14005&destination=42.39600,-71.14128&travelmode=walking) |
| 9 | Park87 | 3 | 1,053m (0.65mi) | ~14분 | [길찾기](https://www.google.com/maps/dir/?api=1&origin=42.38980,-71.13948&destination=42.39600,-71.14128&travelmode=walking) |
| 10 | Vox on Two | 2 | 1,062m (0.66mi) | ~14분 | [길찾기](https://www.google.com/maps/dir/?api=1&origin=42.40001,-71.15112&destination=42.39600,-71.14128&travelmode=walking) |
| 11 | 605 Concord | 3 | 1,065m (0.66mi) | ~14분 | [길찾기](https://www.google.com/maps/dir/?api=1&origin=42.38926,-71.14489&destination=42.39600,-71.14128&travelmode=walking) |
| 12 | 603 Concord | 3 | 1,069m (0.66mi) | ~14분 | [길찾기](https://www.google.com/maps/dir/?api=1&origin=42.38912,-71.14443&destination=42.39600,-71.14128&travelmode=walking) |
| 13 | The Laurent | 3 | 1,188m (0.74mi) | ~16분 | [길찾기](https://www.google.com/maps/dir/?api=1&origin=42.39129,-71.14478&destination=42.39600,-71.14128&travelmode=walking) |
| 14 | Atmark Cambridge | 2 | 1,399m (0.87mi) | ~19분 | [길찾기](https://www.google.com/maps/dir/?api=1&origin=42.39123,-71.14562&destination=42.39600,-71.14128&travelmode=walking) |
| 15 | The Royal Belmont | 4 | 1,409m (0.87mi) | ~19분 | [길찾기](https://www.google.com/maps/dir/?api=1&origin=42.39921,-71.15447&destination=42.39600,-71.14128&travelmode=walking) |
| 16 | The Brook | 2 | 1,495m (0.93mi) | ~20분 | [길찾기](https://www.google.com/maps/dir/?api=1&origin=42.39313,-71.14692&destination=42.39600,-71.14128&travelmode=walking) |
| 17 | Chester Street | 4 | 1,603m (1.00mi) | ~21분 | [길찾기](https://www.google.com/maps/dir/?api=1&origin=42.39360,-71.12481&destination=42.39600,-71.14128&travelmode=walking) |
| 18 | Walden Park | 4 | 1,836m (1.14mi) | ~24분 | [길찾기](https://www.google.com/maps/dir/?api=1&origin=42.38709,-71.12967&destination=42.39600,-71.14128&travelmode=walking) |

!!! note "측정 방법·오차"
    - 출발점은 각 단지 정문 좌표, 도착점은 Alewife 역 노드(42.39600, -71.14128). **건물 입구·역 출입구(차고/버스웨이/플랫폼)를 어디로 잡느냐에 따라 ±1–2분** 차이가 납니다.
    - OSM 보행 네트워크 기준이라 **Google과 보통 1–2분 내로 일치**하지만, 정확한 비교는 위 "Google 도보" 링크로 직접 확인하세요. 신호 대기·실제 걸음 속도는 미반영.
    - 기존 본문의 "도보 N분"은 동네 단위 추정치였고, 이 표가 **실측 기준**입니다.

## 스튜디오 · 1베드 가격 / 크기

| 단지 | Tier | Alewife 도보 | 스튜디오 월세 | 스튜디오 크기 | 1BR 월세 | 1BR 크기 | 비고 (공식✓ = 06-13 라이브) |
|---|---|---|---|---|---|---|---|
| Cambridge Park | 1 | ~6분 | **가용 없음** (공식✓) | (~698 sf) | **$3,699+** (727sf, 8월~) (공식✓) | 727 sf | ⚠️ aggregator $3,140/$3,276은 stale, **공식엔 스튜디오 0개** |
| Urbane at Alewife | 1 | ~7분 | ~$2,969–3,099 | 517–556 sf | ~$3,007+ | 634–754 sf | 1BR 즉시입주 $3,007 신규 |
| Luxe at Alewife | 1 | ~5분 | **$3,003+** (공식✓) | 576–636 sf | **$3,010/$3,325+** (공식✓) | 732–896 sf | 1개월 무료+$99 공식✓ |
| Hanover Alewife | 1 | ~8분 | ~$2,780+ | ~574 sf | ~$3,092+ | 711–805 sf | 공식 위젯 가격 미노출, Zumper 기준 |
| Windsor at Cambridge Park | 1 | ~10분 | 가용 없음 (공식✓) | (n/p) | **$3,053+** (공식✓) | 725–906 sf | 2014년, 398세대 |
| Fuse Cambridge | 1 | ~9분 | **$3,034+** (공식✓) | 531–552 sf | **$3,583+** (공식✓) | 704–749 sf | Bozzuto, LEED Silver |
| Vox on Two | 2 | ~14분 | 가용 없음 (공식✓) | (620 sf) | **$3,048+** (공식✓) | 840–857 sf | 12세대 가용, 전부 1BR↑ |
| Tempo Cambridge | 2 | ~14분 | ~$2,635–2,725 | 502–515 sf | ~$2,956–3,166 | 626–837 sf | 공식 미렌더, ApartmentList 기준 |
| Atmark Cambridge | 2 | **~19분** | ~$2,575–2,717 | 569–588 sf | **$2,817+** (공식✓, 즉시) | 725–740 sf | 1개월 무료 공식✓ |
| The Brook | 2 | **~20분** | 없음 | — | $2,925–3,300 | 671–983 sf | #506 신규 추가 |
| The Laurent | 3 | ~16분 | **$2,370–2,626** (공식✓) | 451–525 sf | **$2,767+** (공식✓) | 583–838 sf | 전 스튜디오 ↓ $157–168, $1,000 off |
| 603 Concord | 3 | ~14분 | **$3,000** (7/2, 공식✓) | 401 sf | **$3,100** (7/5, 공식✓) | 813 sf | "전화 문의 특가" |
| 605 Concord | 3 | ~14분 | **$2,850 (6/19 확정, 공식✓)** | 512 sf | 문의(Micro 575/1BR 719) | 575–719 sf | 입주일 6/19로 확정 |
| Park87 | 3 | ~14분 | 없음 | — | **1BR Plus $3,100** (6/15, 공식✓) | 787 sf | 기본 1BR 가용 없음 |
| Park77 | 3 | ~14분 | 가용 없음 (공식✓) | 444 sf | 가용 없음 (공식✓) | 741 sf | 스튜디오·1BR 모두 공실 0 |
| The Royal Belmont | 4 | ~19분 | 가용 없음 (공식✓) | 596 sf | **$2,870–3,190** (공식✓) | 632–1,062 sf | 1BR 13세대(752sf ~$2,875×다수) |
| Walden Park *(Porter)* | 4 | ~24분 | **$2,490+** (공식✓) | 539 sf | **$2,860+** (공식✓) | 625–760 sf | 스튜디오3·1BR6 가용 |
| Chester Street *(Porter/Davis)* | 4 | ~21분 | **$2,200–2,400** (공식✓) | 380 sf | 가용 없음 (공식✓) | — | 스튜디오 6세대, 최저가 |

## 보너스 · 주차 · 세탁기 · 유틸 · 무브인

| 단지 | 사인업 보너스 (2026-06-13) | 주차비 | In-unit 세탁/건조 | 유틸 포함 | 빠른 무브인 |
|---|---|---|---|---|---|
| Cambridge Park | 없음 | $100–150/월 | 예 (전 세대) | **난방·쓰레기** | 즉시(스튜디오 1세대) |
| Urbane at Alewife | 공식 "없음" / aggregator "2주 무료" *(상충·미확인)* | 차고 있음, n/p | 예 | 없음(서브미터) | 1BR 즉시(A06 #425), 스튜디오 6/20~ |
| Luxe at Alewife | **1개월 무료 + 보증금 $99** *(공식 RentCafe 확인)* | 있음, n/p | 예 | 없음 | 스튜디오 6/16~, 1BR 즉시(A19) |
| Hanover Alewife | 스튜디오 "최대 4주+1주 무료" / 1BR "$500"(공식) · Zumper "2주"(상충) | 차고(+필수 fee 일부 포함), n/p | 예 | 없음 | 문의 |
| Windsor at Cambridge Park | 없음 (공식✓) | 온사이트, n/p | 예 | 없음 | 1BR 즉시~ |
| Fuse Cambridge | 없음 (공식✓) | n/p | 예 | 없음 | 스튜디오 7/22~, 1BR 즉시 |
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
| Windsor at Cambridge Park | ~4.4 (검색) † | [리뷰 보기](https://www.google.com/maps/search/Windsor+at+Cambridge+Park+160+Cambridgepark+Dr+Cambridge+MA) | 2014년 건물. 풀·어메니티 호평 (ApartmentRatings 4.2·69건) |
| Fuse Cambridge | 미추출 † | [리뷰 보기](https://www.google.com/maps/search/Fuse+Cambridge+165+Cambridgepark+Dr+Cambridge+MA) | Bozzuto·LEED. 리뷰 다수(ApartmentRatings 52건) |
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

⚠️ = 리뷰 수가 한 자릿수~극소라 평점 신뢰 불가. † = 06-13 신규 추가 단지로, 평점은 검색 기준이며 **라이브 Google 추출은 다음 패스에서 보강** 예정.

!!! warning "리뷰 데이터 주의"
    - **리뷰 수가 적은 곳(The Brook 1건, 605 Concord 2건, 603·Park87 6건)은 평점이 사실상 의미 없습니다.** 텍스트 리뷰 내용(상세 페이지)을 보세요.
    - **Chester Street**는 Google Maps에 매칭되는 플레이스가 없습니다(검색 시 뜨는 4.4는 Allston의 무관한 광고 매물이니 사용 금지).
    - **공통적으로 가장 많은 불만은 "층간/벽간 방음"과 "택배 도난"** — 거의 모든 단지에서 반복됩니다.
