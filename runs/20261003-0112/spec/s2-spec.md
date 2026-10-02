# S2 설계 — run 20261003-0112

대상 화면: 15 (랜딩) · 학교 기본값: input.json (이 화면에는 학교명을 표시하지 않는다)
변경 사유: 2026-10-03 화면 15 랜딩 추가 — 로그인 전 첫 화면(PRD §7 15, story-service 결정 사항 "랜딩", rules.json screens_required 15, auth.landing_screen = 15).
기준 설계: runs/20261002-2019 화면 1(로그인)·14(회원가입). 수정하지 않고, 같은 nav-pill 표현(로그인 전 = 워드마크만)과 버튼 톤을 따른다.
근거: docs/PRD.md §6·§7 15, docs/story-service.md(N1·N2, 결정 사항 "랜딩"·"모바일 하단 탭바"), docs/design.md(Signature Components — Landing: landing-hero·feature-card·landing-cta, button-primary, button-outline, badge-low-stock, nav-pill), harness/rules.json(screens_required 15, tab_bar, colors, auth), research/s1-adopt.md
색·폰트·모서리·간격은 docs/design.md와 harness/rules.json을 따른다. 허용 색 밖의 값은 쓰지 않는다. 그림자는 쓰지 않는다.
- 핑크 #d6246a는 "재고 부족 알림" 카드 안의 예시 badge-low-stock 안에서만 쓴다. 연핑크 #fbe9f0는 쓰지 않는다.
- 하늘색 #2b9fe0는 feature-card 아이콘에만 쓴다. 옅은 하늘색 #e6f4fc는 쓰지 않는다. 하늘색은 글자색으로 쓰지 않고, button-primary·badge-low-stock 안에는 쓰지 않는다.
로그인 전 화면이라 역할 구분이 없고, 역할별 노출 표의 컴포넌트를 하나도 담지 않는다. 하단 탭바는 모바일·데스크탑 모두 두지 않는다(로그인 후 화면 2~13 전용).
학교를 고르는 입력·학교명 표시는 두지 않는다(학교는 회원가입 화면 14에서만 고른다, N1). 외부 서비스 연결 값 입력·외부 서비스 설정·AI 엔진 선택 UI를 두지 않는다(N2).

## 화면 15
랜딩. 앱을 처음 연 사람이 서비스가 무엇인지 보고 회원가입(화면 14) 또는 로그인(화면 1)으로 간다. 캐러셀·소셜 로그인·대형 일러스트는 두지 않는 한 장짜리 정적 화면.
기능 카드 배치 결정: 모바일 = 세로 목록(레퍼런스 4). 이유: 390 폭에서 2열이면 카드 안 글자 폭이 약 120px로 줄어 한 줄 설명이 2~3줄로 꺾이므로, 전폭 카드를 세로로 쌓아 "제목 → 한 줄" 위계를 지킨다(design.md "grids collapse to one column").
모바일(390×844) 위→아래: nav-pill → landing-hero → feature-card 4장 세로 목록(카드 사이 12) → landing-cta(화면 하단 고정, button-primary 위·button-outline 아래 세로 쌓기, 레퍼런스 2). 좌우 여백 16, hero와 카드 목록 사이 32. 카드가 길면 본문만 스크롤되고 landing-cta는 하단에 고정된다. 하단 탭바 없음.
데스크탑(1440×900): nav-pill(가운데 떠 있는 바) → 가운데 정렬 landing-hero → feature-card 4장을 한 줄 4열 그리드(카드 사이 24, 콘텐츠 폭 가운데 정렬, 레퍼런스 5의 "제목·설명 아래 카드 묶음 → 아래 CTA" 순서) → 그 아래 가운데 landing-cta(button-primary "회원가입"과 button-outline "로그인"을 나란히). 섹션 사이 48. 하단 탭바 없음. 좁아지면 4열 → 2열 → 1열로 열 단위로 접힌다.
### 구성 요소
- nav-pill: "Lab_Stock" 워드마크만 표시(#f3f3f3 바, rounded 9999, 그림자 없음). 로그인 전이라 섹션 링크·학교명·CTA는 없다. 하늘색 없음
- landing-hero: 위→아래로 작은 리드 "Lab_Stock"(body, #707070) → 한 줄 소개 "과학실 시약, 학교별로 한눈에 관리해요"(heading-1, #141414) → 가벼운 부제 "시약 재고·사용 기록·MSDS를 QR로 연결하고, 재고가 부족하면 판매처까지 이어 줘요"(body-lg, #707070). 모노크롬, 학교명 없음. 모바일 왼쪽 정렬, 데스크탑 가운데 정렬. 하늘색 없음
- feature-card: 기능 카드 4장(#f3f3f3 채움, 테두리 없음, rounded 24, 안쪽 여백 24). 카드 안은 위→아래 아이콘(24, #2b9fe0) → 제목(heading-4, #141414) → 한 줄 설명(body, #707070). ① "학교별 분리" — "우리 학교 시약·재고·사용 기록만 보여요. 다른 학교와 섞이지 않아요" (아이콘: 건물) ② "NEIS 학교 선택" — "회원가입 때 시/도 → 지역 → 학교 순서로 우리 학교를 골라요" (아이콘: 위치 핀) ③ "QR 스캔" — "시약장 QR을 찍으면 시약 정보와 MSDS가 바로 열려요" (아이콘: QR) ④ "재고 부족 알림" — "필요한 양보다 적으면 알려 주고 판매처로 연결해요" (아이콘: 종) + 제목 오른쪽에 예시 badge-low-stock 1개. 하늘색: 각 카드 아이콘만 #2b9fe0(글자는 #141414·#707070)
- badge-low-stock: "재고 부족 알림" 카드 제목 옆 예시 배지 1개. #d6246a 채움, 라벨 "재고 부족"(label, #ffffff), rounded 9999. 핑크는 이 배지 안에서만. 하늘색 없음
- landing-cta: 하단 행동 영역. button-primary "회원가입"(→ 화면 14)과 button-outline "로그인"(→ 화면 1). 모바일은 화면 하단 고정 #ffffff 영역(위 1px #f0f0f0 선, 안쪽 여백 16)에 전폭 버튼 2개를 세로로 쌓고(사이 8), 데스크탑은 가운데에 두 버튼을 나란히(사이 12) 둔다. 하늘색 없음
- button-primary: landing-cta 안 "회원가입"(#141414 채움, #ffffff 글자 link, rounded 9999, 높이 44 이상). 누르면 화면 14 회원가입. 하늘색 없음
- button-outline: landing-cta 안 "로그인"(#ffffff 채움, 1px #e0e0e0 테두리, #141414 글자 link, rounded 9999, 높이 44 이상). 누르면 화면 1 로그인. 하늘색 없음
### 반영한 레퍼런스
- https://uibowl.io/name/%EB%9E%AD%ED%94%8C%EB%A6%AD%EC%8A%A4?patterns=%EC%98%A8%EB%B3%B4%EB%94%A9&imgId=cmswzxy9v0003l404lllro7wu
- https://uibowl.io/name/%ED%8E%98%EC%9D%B4%EC%9B%8C%ED%81%AC?patterns=%EC%98%A8%EB%B3%B4%EB%94%A9&patternName=%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85%20%EC%A0%84
- https://uibowl.io/name/CES%202026?patterns=%EC%98%A8%EB%B3%B4%EB%94%A9&imgId=cmk5qewa10003jy04k4wwtudg
- https://uibowl.io/name/%EC%B1%84%EB%B9%84?patterns=%EC%83%81%EC%84%B8%EC%A0%95%EB%B3%B4%20%28PDP%29&patternName=%EC%84%9C%EB%B9%84%EC%8A%A4%20%EC%86%8C%EA%B0%9C
- https://uibowl.io/name/%ED%8E%98%EC%9D%B4%EC%9B%8C%ED%81%AC?patterns=%EC%98%A8%EB%B3%B4%EB%94%A9&patternName=%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85%20%ED%9B%84

## 역할별 노출
앱 전체 기준 개수. runs/20261002-2019 표를 그대로 옮겼다. 화면 15는 로그인 전 화면이라 표의 컴포넌트를 하나도 담지 않으므로 숫자가 바뀌지 않는다.

| 컴포넌트 | 학생 | 교사 | admin |
|---|---|---|---|
| manual-upload | 0 | 2 | 2 |
| reorder-alert-card | 0 | 2 | 2 |
| vendor-link | 0 | 1 | 1 |
| vendor-register | 0 | 0 | 2 |
| msds-entry | 3 | 3 | 3 |
| stock-intake | 0 | 2 | 2 |
| reagent-register | 0 | 1 | 1 |
| user-manage | 0 | 0 | 2 |
| cabinet-edit | 0 | 2 | 2 |
