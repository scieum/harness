# S1 채택 항목 — run 20261003-0112

구조·흐름·배치만 가져온다. 색·폰트·모서리는 docs/design.md를 따른다.
화면 15(랜딩)는 탭바 없음. 캐러셀·소셜 로그인 버튼·일러스트 대형 배너는 가져오지 않는다 (한 장짜리 정적 랜딩).

## 화면 15
| # | ui_url | 가져올 것 |
|---|---|---|
| 1 | https://uibowl.io/name/%EB%9E%AD%ED%94%8C%EB%A6%AD%EC%8A%A4?patterns=%EC%98%A8%EB%B3%B4%EB%94%A9&imgId=cmswzxy9v0003l404lllro7wu | 소개 문구 위계(작은 리드 1줄 → 굵은 핵심 한 줄) → 기능 목록 → 하단 CTA 순서, CTA는 채움 버튼(회원가입) 1개 + 그 아래 텍스트형 보조(로그인)로 강조 차이를 둠 |
| 2 | https://uibowl.io/name/%ED%8E%98%EC%9D%B4%EC%9B%8C%ED%81%AC?patterns=%EC%98%A8%EB%B3%B4%EB%94%A9&patternName=%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85%20%EC%A0%84 | 업무형 가치 제안 2줄 헤드라인을 상단 중앙에 두고, 하단 고정 영역에 전폭 버튼을 세로로 쌓되 주 버튼은 채움·보조 버튼은 외곽선으로 구분 |
| 3 | https://uibowl.io/name/CES%202026?patterns=%EC%98%A8%EB%B3%B4%EB%94%A9&imgId=cmk5qewa10003jy04k4wwtudg | 제목 → 서비스 설명 짧은 본문 → 전폭 주 버튼 → 바로 아래 텍스트 버튼의 2단 CTA 배치 (로그인 전 웰컴의 최소 구성) |
| 4 | https://uibowl.io/name/%EC%B1%84%EB%B9%84?patterns=%EC%83%81%EC%84%B8%EC%A0%95%EB%B3%B4%20%28PDP%29&patternName=%EC%84%9C%EB%B9%84%EC%8A%A4%20%EC%86%8C%EA%B0%9C | 기능 카드 세로 목록안: 전폭 카드를 세로로 쌓고 카드 안은 기능명 제목 → 1~2줄 설명 순서 (학교별 분리·NEIS 학교 선택·QR 스캔·재고 부족 알림 4장), 일러스트·각주는 빼고 아이콘 1개로 축소 |
| 5 | https://uibowl.io/name/%ED%8E%98%EC%9D%B4%EC%9B%8C%ED%81%AC?patterns=%EC%98%A8%EB%B3%B4%EB%94%A9&patternName=%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85%20%ED%9B%84 | 기능 카드 2열 그리드안: 4개 기능을 2x2 카드로 배치해 한 화면에 스크롤 없이 담고, 그리드 위에 제목 + 설명 1줄, 그리드 아래 하단 고정 CTA |
