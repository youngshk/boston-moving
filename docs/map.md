# 지도

Alewife 역 인근 16개 단지를 지도에 표시했습니다. **마커 색은 Tier(역까지 거리 그룹)** 기준입니다. 마커를 클릭하면 단지명·가격·프로모션 요약이 뜹니다.

<div id="alewife-map" style="height: 600px; border-radius: 8px; margin: 1rem 0; z-index: 0;"></div>

<div style="font-size: 0.85rem; line-height: 1.8;">
<strong>범례</strong> &nbsp;
<span style="color:#d32f2f;">●</span> Alewife 역 &nbsp;
<span style="color:#1565c0;">●</span> Tier 1 (도보 2–6분) &nbsp;
<span style="color:#2e7d32;">●</span> Tier 2 (도보 8–12분) &nbsp;
<span style="color:#ef6c00;">●</span> Tier 3 (도보 10–15분) &nbsp;
<span style="color:#6a1b9a;">●</span> Tier 4 (Belmont/Porter, 참고)
</div>

!!! tip "지도 사용법"
    - 마커 클릭 → 단지명·현재 스튜디오/1BR 시작가·프로모션 팝업
    - 스크롤로 확대/축소, 드래그로 이동
    - Tier 4(보라색)는 Alewife에서 다소 떨어져 있어 지도를 줄이면 동쪽(Porter/Davis)에 보입니다.
    - 가격은 **2026-06-13** 조사 시점 시작가 기준이며 변동됩니다. 상세는 [비교표](comparison.md)·단지 상세 참고.

<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" integrity="sha256-p4NxAoJBhIIN+hmNHrzRCf9tD/miZyoHS5obTRR9BMY=" crossorigin="" />
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js" integrity="sha256-20nQCchB9co0qIjJZRGuk2/Z9VM+kNiyxNV1lvTlZBo=" crossorigin=""></script>

<script>
(function () {
  function initAlewifeMap() {
    var el = document.getElementById('alewife-map');
    if (!el || typeof L === 'undefined') return;
    if (el._leaflet_id) return; // already initialized

    var tierColors = {
      station: '#d32f2f',
      1: '#1565c0',
      2: '#2e7d32',
      3: '#ef6c00',
      4: '#6a1b9a'
    };

    var places = [
      {n:'Alewife 역 (Red Line 종점)', lat:42.39600, lng:-71.14128, t:'station', d:'MBTA Red Line 종점 · 버스 환승 · 차고'},
      {n:'Cambridge Park', lat:42.39401, lng:-71.14311, t:1, d:'스튜디오 가용없음 · 1BR $3,699~(727sf, 공식) · 프로모 없음 · 난방·쓰레기 포함'},
      {n:'Urbane at Alewife', lat:42.39409, lng:-71.14384, t:1, d:'스튜디오 ~$2,969 · 1BR ~$3,007 · 2주 무료(미확인)'},
      {n:'Luxe at Alewife', lat:42.39300, lng:-71.14189, t:1, d:'스튜디오 ~$3,003 · 1BR ~$3,325 · 1개월 무료+$99(공식)'},
      {n:'Hanover Alewife', lat:42.39361, lng:-71.14479, t:1, d:'스튜디오 ~$2,780 · 1BR ~$3,092 · 최대 4주+1주(공식) · 평점 4.8'},
      {n:'Vox on Two', lat:42.40001, lng:-71.15112, t:2, d:'스튜디오 공실없음 · 1BR ~$3,048 · 프로모 없음 · 평점 4.7'},
      {n:'Tempo Cambridge', lat:42.40012, lng:-71.15043, t:2, d:'스튜디오 ~$2,635 · 1BR ~$2,956 · 프로모 없음'},
      {n:'Atmark Cambridge', lat:42.39123, lng:-71.14562, t:2, d:'스튜디오 ~$2,575 · 1BR $2,817~(공식) · 1개월 무료(공식)'},
      {n:'The Brook', lat:42.39313, lng:-71.14692, t:2, d:'스튜디오 없음 · 1BR ~$2,925 · 입주 9/1~ · 프로모 미확인'},
      {n:'The Laurent', lat:42.39129, lng:-71.14478, t:3, d:'스튜디오 ~$2,370 · 1BR ~$2,767 · $1,000 off(공식) · 어포더블 100세대 · 평점 4.6'},
      {n:'603 Concord', lat:42.38912, lng:-71.14443, t:3, d:'스튜디오 $3,000 · 1BR $3,100 · 한정 특가(문의) · 난방·온수 포함'},
      {n:'605 Concord', lat:42.38926, lng:-71.14489, t:3, d:'스튜디오 $2,850 · 1BR 문의 · 신축(2025) · 난방·온수 포함 · 무료 셔틀'},
      {n:'Park87', lat:42.38980, lng:-71.13948, t:3, d:'스튜디오 없음 · 1BR Plus ~$3,100 · 1BR 2주 무료(정황)'},
      {n:'Park77', lat:42.38930, lng:-71.14005, t:3, d:'스튜디오/1BR 가격 비공개 · 난방·온수 포함'},
      {n:'The Royal Belmont', lat:42.39921, lng:-71.15447, t:4, d:'(Belmont) 스튜디오 없음 · 1BR ~$2,870 · 1개월 무료(6/21/26 마감)'},
      {n:'Walden Park', lat:42.38709, lng:-71.12967, t:4, d:'(Porter) 스튜디오 $2,490~ · 1BR $2,860~(공식) · 유틸 다수 포함'},
      {n:'Chester Street', lat:42.39360, lng:-71.12481, t:4, d:'(Porter/Davis) 스튜디오 ~$2,200(최저가) · 1BR 공실없음 · 1개월 무료(전 공실)'}
    ];

    var map = L.map('alewife-map').setView([42.3935, -71.1410], 14);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      maxZoom: 19,
      attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    var bounds = [];
    places.forEach(function (p) {
      var isStation = p.t === 'station';
      var marker = L.circleMarker([p.lat, p.lng], {
        radius: isStation ? 11 : 8,
        color: '#fff',
        weight: 2,
        fillColor: tierColors[p.t],
        fillOpacity: 0.95
      }).addTo(map);
      var gmaps = 'https://www.google.com/maps/search/' + encodeURIComponent(p.n + ' Cambridge MA');
      marker.bindPopup(
        '<strong>' + p.n + '</strong><br>' + p.d +
        '<br><a href="' + gmaps + '" target="_blank" rel="noopener">Google 지도에서 보기 ↗</a>'
      );
      if (!isStation) {
        marker.bindTooltip(p.n, {permanent: false, direction: 'top'});
      }
      bounds.push([p.lat, p.lng]);
    });

    map.fitBounds(bounds, {padding: [40, 40]});
  }

  // Run now, and re-run on Material's instant navigation
  if (document.readyState !== 'loading') {
    initAlewifeMap();
  } else {
    document.addEventListener('DOMContentLoaded', initAlewifeMap);
  }
  if (typeof document$ !== 'undefined' && document$.subscribe) {
    document$.subscribe(initAlewifeMap);
  }
})();
</script>
