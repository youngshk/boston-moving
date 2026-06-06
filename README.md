# Alewife 아파트 시장조사

캠브리지 **Alewife** 역(Red Line) 인근 스튜디오·1베드 렌탈 시장조사. 2026-06-06 기준 데이터를 MkDocs(Material 테마)로 정리해 GitHub Pages로 퍼블리시합니다.

## 로컬 미리보기

```bash
pip install -r requirements.txt
mkdocs serve
# http://127.0.0.1:8000
```

## 빌드

```bash
mkdocs build   # site/ 디렉터리에 정적 사이트 생성
```

## 배포

`main` 브랜치에 푸시하면 GitHub Actions(`.github/workflows/deploy.yml`)가 `mkdocs gh-deploy`로 `gh-pages` 브랜치에 배포합니다. 저장소 Settings → Pages에서 Source를 `gh-pages` 브랜치로 설정하세요.

## 구조

```
mkdocs.yml          # 사이트 설정 / 네비게이션
docs/
  index.md          # 개요 · 요약 · 의사결정 가이드
  comparison.md     # 전체 비교표
  promotions.md     # 사인업 보너스 & 시즌성
  tier1.md          # Alewife 도보 2-6분
  tier2.md          # Concord Tpke / Fawcett St
  tier3.md          # Cambridge Highlands / Fresh Pond
  tier4.md          # Belmont / Porter (참고)
```

## 주의

가격·프로모션은 거의 매주 바뀝니다. 모든 수치는 조사 시점 최신 리스팅 기준이며 계약 전 리싱 오피스 확인이 필요합니다. 출처와 신뢰도는 각 페이지에 표기되어 있습니다.
