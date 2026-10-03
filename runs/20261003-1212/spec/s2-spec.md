# S2 설계 — run 20261003-1212

대상 화면: 15 (랜딩) · 둘러보기 화면: 13, 2, 3 (input.json guest_screens) · 키스크린: 15-mobile, 13-guest-mobile, 2-guest-mobile
변경 사유: 2026-10-03 사용자 결정 — 비회원 둘러보기. 랜딩(15)의 "둘러보기"로 들어가 데모 학교(읽기 전용) 데이터로 홈(13)·시약 목록(2)·시약 상세(3)를 본다. 쓰기 동작은 잠그고, 상단 띠에서 가입을 유도한다(PRD §7 둘러보기 줄, story-service 결정 사항 "둘러보기", rules.json guest).
기준 설계(수정하지 않음): 화면 15 = runs/20261003-0112, 홈 13 = runs/20261002-1416, 화면 2·3(탭바 버전) = runs/20261002-1441. 같은 컴포넌트 이름과 톤을 따른다. 둘러보기 화면은 원래 화면의 학생 역할 구성(쓰기·관리 진입이 가장 적은 구성)을 바탕으로 숨김·잠금을 적용했다.
근거: docs/PRD.md §6·§7(15, 둘러보기), docs/story-service.md(N1·N2, 결정 사항 "둘러보기"·"랜딩"·"모바일 하단 탭바"), docs/design.md(Signature Components — Landing: landing-hero·feature-card·landing-cta·guest-entry, Guest mode: guest-banner·guest-lock, tab-bar), harness/rules.json(screens_required 15, guest, tab_bar, colors), research/s1-adopt.md
색·폰트·모서리·간격은 docs/design.md와 harness/rules.json을 따른다. 허용 색 밖의 값은 쓰지 않는다. 그림자는 쓰지 않는다(segmented-control-active 예외).
- 핑크 #d6246a는 badge-low-stock 안에서만 쓴다. 연핑크 #fbe9f0는 쓰지 않는다. 둘러보기의 잠금 안내(guest-lock, ex-toast)에는 핑크를 쓰지 않는다(결정이 필요한 신호가 아니다).
- 하늘색 #2b9fe0(아이콘·인디케이터)과 옅은 하늘색 #e6f4fc(guest-banner 바탕·선택 바탕)는 선택·강조에만 쓴다. 글자색으로 쓰지 않고(하늘색 위 글자는 #141414), badge-low-stock·button-primary 안에는 쓰지 않는다.
학교 선택은 회원가입(화면 14)에만 있다. 화면 15에는 학교명·학교 선택이 없다. 둘러보기 화면에는 학교 선택이 없고, 학교명은 데모 학교 "데모 학교" 1종만 표시한다. 실제 학교명·다른 학교 데이터는 둘러보기에 섞지 않는다(N1).
외부 서비스 연결 값은 서버에서만 다룬다. 어떤 화면에도 연결 값 입력·외부 서비스 설정·AI 엔진 선택 UI를 두지 않는다(N2).
둘러보기 공통(13·2·3):
- 숨김(rules.json guest.hidden_components): stock-intake, reagent-register, manual-upload, user-manage, cabinet-edit, vendor-register, vendor-link, reorder-alert-card, school-select-sido, school-select-region, school-select-school. 이 이름의 컴포넌트와 그 진입 버튼은 둘러보기 프레임에 하나도 두지 않는다.
- 모바일(390×844) 위→아래: nav-pill → guest-banner(전폭, 스크롤해도 nav-pill 아래 고정) → 원래 화면 본문 → 하단 tab-bar(y 780~844). 본문 스크롤 영역은 tab-bar 위쪽 선에서 끝나고 마지막 요소 아래 16 여백.
- 데스크탑(1440×900): tab-bar 없음. nav-pill 섹션 링크 "홈"·"시약 목록"·"QR 스캔"·"사용 기록 내역" 중 뒤 두 개는 링크 오른쪽에 guest-lock 아이콘. 재주문 알림·입고·사용자 관리·판매처 설정 링크는 두지 않는다. guest-banner는 nav-pill 아래 콘텐츠 폭 전체.
- 잠금 동작: guest-lock이 붙은 항목을 누르면 화면 이동 없이 ex-toast "가입하면 쓸 수 있어요"가 뜬다. 가입 진입은 guest-banner의 "가입하기"(→ 화면 14) 하나로 통일한다.
- 데모 학교 예시 데이터(13·2·3 공통): 전체 시약 24종, 재고 부족 2종 — 염산 · 1병, 에탄올 · 200mL. 그 밖 시약 수산화나트륨 · 500g, 황산구리(II) · 250g, 아세톤 · 1L, 질산칼륨 · 300g. 시약장 1개(칸 8개 중 지정 7 · 미지정 1). 최근 사용 기록 3줄: 염산 · 학생 A · 20mL · 오늘 10:20 / 에탄올 · 교사 B · 50mL · 어제 14:05 / 황산구리(II) · 학생 C · 5g · 10월 1일.

## 화면 15
랜딩. 앱을 처음 연 사람이 서비스가 무엇인지 보고 회원가입(화면 14)·로그인(화면 1)으로 가거나, 가입 없이 둘러보기(데모 학교 홈)로 간다. 캐러셀·소셜 로그인·대형 일러스트는 두지 않는 한 장짜리 정적 화면. runs/20261003-0112 설계를 그대로 두고 landing-cta 아래에 guest-entry만 더했다.
기능 카드 배치: 모바일 = 전폭 세로 목록(390 폭에서 2열이면 한 줄 설명이 꺾이므로 "제목 → 한 줄" 위계를 지킨다, design.md "grids collapse to one column").
CTA 위계(레퍼런스 2·4): 채움 "회원가입" → 외곽선 "로그인" → 가장 약한 위계의 "둘러보기" 3단.
모바일(390×844) 위→아래: nav-pill → landing-hero → feature-card 4장 세로 목록(카드 사이 12) → landing-cta + guest-entry(화면 하단 고정 영역, button-primary 위·button-outline 아래 세로 쌓기, 그 아래 guest-entry). 좌우 여백 16, hero와 카드 목록 사이 32. 카드가 길면 본문만 스크롤되고 하단 고정 영역은 그대로 있다. 하단 탭바 없음.
데스크탑(1440×900): nav-pill(가운데 떠 있는 바) → 가운데 정렬 landing-hero → feature-card 4장 한 줄 4열 그리드(카드 사이 24, 콘텐츠 폭 가운데 정렬) → 그 아래 가운데 landing-cta(button-primary "회원가입"과 button-outline "로그인"을 나란히) → 바로 아래 가운데 guest-entry. 섹션 사이 48. 하단 탭바 없음. 좁아지면 4열 → 2열 → 1열로 열 단위로 접힌다.
### 구성 요소
- nav-pill: "Lab_Stock" 워드마크만 표시(#f3f3f3 바, rounded 9999, 그림자 없음). 로그인 전이라 섹션 링크·학교명·CTA는 없다. 하늘색 없음
- landing-hero: 위→아래로 작은 리드 "Lab_Stock"(body, #707070) → 한 줄 소개 "과학실 시약, 학교별로 한눈에 관리해요"(heading-1, #141414) → 가벼운 부제 "시약 재고·사용 기록·MSDS를 QR로 연결하고, 재고가 부족하면 판매처까지 이어 줘요"(body-lg, #707070). 모노크롬, 학교명 없음. 모바일 왼쪽 정렬, 데스크탑 가운데 정렬. 하늘색 없음
- feature-card: 기능 카드 4장(#f3f3f3 채움, 테두리 없음, rounded 24, 안쪽 여백 24). 카드 안은 위→아래 아이콘(24, #2b9fe0) → 제목(heading-4, #141414) → 한 줄 설명(body, #707070). ① "학교별 분리" — "우리 학교 시약·재고·사용 기록만 보여요. 다른 학교와 섞이지 않아요" (아이콘: 건물) ② "NEIS 학교 선택" — "회원가입 때 시/도 → 지역 → 학교 순서로 우리 학교를 골라요" (아이콘: 위치 핀) ③ "QR 스캔" — "시약장 QR을 찍으면 시약 정보와 MSDS가 바로 열려요" (아이콘: QR) ④ "재고 부족 알림" — "필요한 양보다 적으면 알려 주고 판매처로 연결해요" (아이콘: 종) + 제목 오른쪽에 예시 badge-low-stock 1개. 하늘색: 각 카드 아이콘만 #2b9fe0(글자는 #141414·#707070)
- badge-low-stock: "재고 부족 알림" 카드 제목 옆 예시 배지 1개. #d6246a 채움, 라벨 "재고 부족"(label, #ffffff), rounded 9999. 핑크는 이 배지 안에서만. 하늘색 없음
- landing-cta: 하단 행동 영역. button-primary "회원가입"(→ 화면 14)과 button-outline "로그인"(→ 화면 1). 모바일은 화면 하단 고정 #ffffff 영역(위 1px #f0f0f0 선, 안쪽 여백 16)에 전폭 버튼 2개를 세로로 쌓고(사이 8), 그 아래 8 간격으로 guest-entry가 같은 고정 영역 안에 이어진다. 데스크탑은 가운데에 두 버튼을 나란히(사이 12) 둔다. 하늘색 없음
- button-primary: landing-cta 안 "회원가입"(#141414 채움, #ffffff 글자 link, rounded 9999, 높이 44 이상). 누르면 화면 14 회원가입. 하늘색 없음
- button-outline: landing-cta 안 "로그인"(#ffffff 채움, 1px #e0e0e0 테두리, #141414 글자 link, rounded 9999, 높이 44 이상). 누르면 화면 1 로그인. 하늘색 없음
- guest-entry: landing-cta 바로 아래 세 번째, 가장 조용한 행동. button-pill-soft "둘러보기" 1개(→ 둘러보기 화면 13, 데모 학교 홈). 모바일은 landing-cta 고정 영역 안 맨 아래 가운데, 데스크탑은 landing-cta 아래 12 간격 가운데. 위에 보조 문구는 두지 않는다. 하늘색: 라벨 오른쪽 › 아이콘 #2b9fe0(라벨 글자는 #141414)
- button-pill-soft: guest-entry 안 "둘러보기 ›"(#f3f3f3 채움, 테두리 없음, 라벨 #141414 link, rounded 9999, 높이 44 이상, 버튼 폭은 라벨에 맞춤 — 전폭 아님으로 회원가입·로그인보다 약한 위계). 하늘색: › 아이콘만
### 반영한 레퍼런스
- https://uibowl.io/name/%EB%9E%AD%ED%94%8C%EB%A6%AD%EC%8A%A4?patterns=%EC%98%A8%EB%B3%B4%EB%94%A9&imgId=cmswzxy9v0003l404lllro7wu
- https://uibowl.io/name/CES%202026?patterns=%EC%98%A8%EB%B3%B4%EB%94%A9&imgId=cmk5qewa10003jy04k4wwtudg
- https://uibowl.io/name/%EC%B1%84%EB%B9%84?patterns=%EC%83%81%EC%84%B8%EC%A0%95%EB%B3%B4%20%28PDP%29&patternName=%EC%84%9C%EB%B9%84%EC%8A%A4%20%EC%86%8C%EA%B0%9C
- https://uibowl.io/name/%EB%83%89%EC%9E%A5%EA%B3%A0%ED%84%B8%EA%B8%B0?patterns=%EC%98%A8%EB%B3%B4%EB%94%A9&imgId=cmohwstxe001vl204icjh4dc7
- https://uibowl.io/name/G%20car?patterns=%EC%98%A8%EB%B3%B4%EB%94%A9&imgId=cmo85ethb000fjs04bga7173h

## 둘러보기 화면 13
데모 학교 홈. 랜딩의 guest-entry로 들어온다. 구조는 runs/20261002-1416 학생 홈과 같고(레퍼런스 4: 화면 구조를 로그인 홈과 동일하게), 요약 숫자는 데모 학교 값으로 그대로 보여준다. 재주문 알림 카드(reorder-alert-card)와 입고·사용자 관리 바로가기는 숨긴다.
모바일 위→아래: nav-pill → guest-banner → quick-action 2칸 한 줄 → home-summary ① 재고 요약 카드 → home-summary ② 시약장 요약 카드 → 최근 사용 기록 카드. 화면 하단 tab-bar 고정. 카드 사이 24, 좌우 여백 16. 첫 화면(스크롤 전)은 nav-pill · guest-banner · quick-action · 재고 요약 카드까지 보인다.
데스크탑: tab-bar 없음. nav-pill → guest-banner → 2열. 왼쪽 열 = quick-action 2칸 + home-summary(재고 요약 → 시약장 요약), 오른쪽 열 = 최근 사용 기록 카드.
### 구성 요소
- nav-pill: "Lab_Stock" 워드마크 + 학교명 "데모 학교" 텍스트. 학교 선택·전환 컨트롤 없음. 모바일 = 워드마크·학교명만 있는 얇은 헤더. 데스크탑 = 공통 규칙의 섹션 링크("QR 스캔"·"사용 기록 내역"에 guest-lock). 하늘색: 데스크탑 현재 섹션 링크("홈") 아래 #2b9fe0 밑줄 인디케이터(글자는 #141414)
- guest-banner: nav-pill 바로 아래 전폭 띠 1개. #e6f4fc 채움, rounded 0, 안쪽 여백 위아래 8 · 좌우 16. 왼쪽 문구 "둘러보는 중 — 가입하면 우리 학교 데이터로 시작해요"(body-sm, #141414, 두 줄까지 줄바꿈), 오른쪽 끝 button-primary "가입하기". 띠 안 하늘색은 바탕뿐(글자·버튼에는 쓰지 않음)
- button-primary: guest-banner 안 "가입하기"(#141414 채움, #ffffff 글자 link, rounded 9999, 높이 44 이상, 폭은 라벨에 맞춤). 누르면 화면 14 회원가입. 하늘색 없음
- quick-action: 바로가기 2칸 한 줄(같은 폭 2열, 칸 사이 12). 칸 = #f3f3f3 채움, rounded 16, 안쪽 여백 16, 왼쪽 원형 아이콘 바탕(#e6f4fc, rounded 9999) 안 #2b9fe0 아이콘 + 오른쪽 label(link, #141414). 학생 홈과 같은 2칸 "사용 기록 입력" · "시약장 보기". 둘 다 오른쪽 끝에 guest-lock(사용 기록 입력 = 쓰기 동작, 시약장 보기 = 화면 11이 둘러보기 범위 밖). 입고·사용자 관리 칸은 두지 않는다. 하늘색: 아이콘 #2b9fe0 + 아이콘 바탕 #e6f4fc
- guest-lock: #707070 작은 자물쇠 아이콘(16). 이 화면에 4곳 — quick-action "사용 기록 입력"·"시약장 보기" 칸 오른쪽 끝, 최근 사용 기록 카드 "더 보기" 버튼 라벨 앞, tab-bar 안 "QR 스캔"·"기록" tab-item 아이콘 오른쪽 위. 잠긴 항목은 보이되 누르면 ex-toast만 뜬다. 핑크·하늘색 없음
- home-summary: 요약 카드 2장(#ffffff, 1px #f0f0f0 테두리, rounded 24, 안쪽 여백 24). ① 재고 요약 카드: heading-4 "재고 부족 2개"(#141414) + 오른쪽 badge-low-stock "2" → 부족 시약 칩 가로 줄(칩 = #f3f3f3 채움, rounded 9999, label #141414 "염산 · 1병" / "에탄올 · 200mL", 누르면 둘러보기 화면 3 시약 상세) → 보조 1행 "전체 시약"(caption #707070) + "24종"(title). ② 시약장 요약 카드: heading-4 "시약장 요약"(둘러보기에서는 화면 11로 가지 않으므로 › 없음) → 큰 숫자 display "1개" → 상태별 구간 막대 1줄(지정 칸 #2b9fe0 구간 + 미지정 칸 #e0e0e0 구간, rounded 9999) → body-sm(#707070) "칸 8개 중 지정 7 · 미지정 1". 하늘색: 시약장 막대 지정 구간. 핑크는 badge-low-stock 안에서만
- badge-low-stock: 재고 요약 카드 제목 옆 개수 배지 "2"(#d6246a 채움, #ffffff label, rounded 9999). 데모 데이터의 재고 부족 표시는 로그인 화면과 같이 핑크 그대로. 하늘색 없음
- reagent-row: 최근 사용 기록 카드 안 3줄(데모 데이터). 카드 = #ffffff, 1px #f0f0f0 테두리, rounded 24, 제목 heading-4 "최근 사용 기록". 행 = 시약명(title) + "학생 A · 20mL"(body) + 시각 caption(#707070), #f3f3f3 채움, rounded 16, 행 사이 12. 둘러보기에서는 행을 눌러도 이동하지 않는다(화면 10이 범위 밖, 화살표 없음). 재고 부족 배지는 이 행에 두지 않는다. 하늘색 없음
- button-pill-soft: 최근 사용 기록 카드 하단 "더 보기"(#f3f3f3 채움, 라벨 #141414, rounded 9999, 높이 44 이상) + 라벨 앞 guest-lock. 누르면 ex-toast("기록" 탭과 같은 잠금). 하늘색 없음
- ex-toast: 잠긴 항목을 누르면 tab-bar 위(모바일) · 화면 아래 가운데(데스크탑)에 2초간 뜬다. #141414 채움, 왼쪽 guest-lock 모양 자물쇠 아이콘 #ffffff + 문구 "가입하면 쓸 수 있어요"(body-sm, #ffffff), rounded 16, 안쪽 여백 12·16, 그림자 없음. 핑크 금지, 하늘색 없음
- tab-bar: 모바일 전용 하단 탭바 1개. 전폭 사각형 바(x 0, 폭 390, 높이 64, y 780~844, rounded 0). #ffffff 채움 + 위쪽에만 1px #f0f0f0 선, 그림자 없음, floating pill 아님. 안쪽 위아래 여백 8, 좌우 0. tab-item 4개를 같은 폭으로 채운다. 데스크탑 프레임에는 두지 않는다. 하늘색: 활성 tab-item 아이콘만
- tab-item: tab-bar 안 4개, 왼쪽부터 "홈"(둘러보기 화면 13) · "시약"(둘러보기 화면 2) · "QR 스캔" · "기록". 같은 폭(390 ÷ 4) 사각형 누름 영역(rounded 0, 채움 없음), 높이 48, 아이콘 위 + label(12/600) 아래, 사이 4. "QR 스캔"·"기록"은 아이콘 오른쪽 위에 guest-lock(탭 안 잠금 2개), 누르면 화면 이동 없이 ex-toast. 이 화면의 활성 = "홈": #2b9fe0 아이콘 + 라벨 #141414. 비활성("시약"·"QR 스캔"·"기록"): 아이콘·라벨 #707070
### 반영한 레퍼런스
- https://uibowl.io/name/%EB%A7%88%EC%9D%B4%ED%98%84%EB%8C%80?patterns=%EB%A9%94%EC%9D%B8&patternName=%ED%99%88%ED%99%94%EB%A9%B4%20%28%EB%A1%9C%EA%B7%B8%EC%9D%B8%20%EC%A0%84%29
- https://uibowl.io/name/%ED%95%B4%ED%94%BC%EB%AC%B8%EB%8D%B0%EC%9D%B4?patterns=%EB%A9%94%EC%9D%B8&patternName=%EB%A1%9C%EA%B7%B8%EC%9D%B8%20%EC%A0%84
- https://uibowl.io/name/%EB%AF%B8%EB%9E%98%EC%97%90%EC%85%8B%EC%A6%9D%EA%B6%8C%20M-STOCK?patterns=%EB%A9%94%EC%9D%B8&patternName=%ED%99%88%20-%20%EC%9E%90%EC%82%B0%20-%20%EB%A1%9C%EA%B7%B8%EC%9D%B8%20%EC%A0%84
- https://uibowl.io/name/%ED%95%9C%ED%8C%A8%EC%8A%A4?patterns=%EB%A9%94%EC%9D%B8&patternName=%EB%A1%9C%EA%B7%B8%EC%9D%B8%20%EC%A0%84
- https://uibowl.io/name/Kia?patterns=%EB%A7%88%EC%9D%B4%ED%8E%98%EC%9D%B4%EC%A7%80&patternName=%EB%B9%84%EB%A1%9C%EA%B7%B8%EC%9D%B8-%EB%8B%A4%ED%81%AC%EB%AA%A8%EB%93%9C

## 둘러보기 화면 2
데모 학교 시약 목록. 구조는 runs/20261002-1441 화면 2(학생)와 같다. 목록·필터·검색은 모두 쓸 수 있고(읽기), 이 화면에는 원래 쓰기 진입이 없어 본문 잠금은 없다. 재주문 알림 링크는 두지 않는다.
모바일 위→아래: nav-pill → guest-banner → segmented-control → text-input 검색 → reagent-row 목록 → 하단 tab-bar. 활성 탭 "시약".
데스크탑: nav-pill → guest-banner → 필터·검색 → 목록(가운데 단일 열). tab-bar 없음.
### 구성 요소
- nav-pill: "Lab_Stock" 워드마크 + 학교명 "데모 학교" 텍스트. 모바일은 워드마크·학교명만. 데스크탑은 공통 규칙의 섹션 링크("QR 스캔"·"사용 기록 내역"에 guest-lock, 재주문 알림 링크 없음). 학교 전환 없음. 하늘색: 데스크탑 현재 섹션 링크("시약 목록") 아래 #2b9fe0 밑줄 인디케이터(글자는 #141414)
- guest-banner: nav-pill 바로 아래 전폭 띠 1개. 둘러보기 화면 13과 같은 위치·문구·모양(#e6f4fc 채움, rounded 0, "둘러보는 중 — 가입하면 우리 학교 데이터로 시작해요" body-sm #141414 + 오른쪽 button-primary "가입하기")
- button-primary: guest-banner 안 "가입하기"(#141414 채움, #ffffff 글자, rounded 9999, 높이 44 이상) → 화면 14. 하늘색 없음
- segmented-control: 리스트 위 필터 "전체 / 재고 부족" 두 옵션, 한 번에 하나. 예시 상태 = "전체" 선택
- segmented-control-active: 선택된 옵션의 흰 pill. 하늘색: 1px #2b9fe0 테두리(글자는 #141414)
- text-input: 시약명 검색 바, 플레이스홀더 "시약명 검색". 하늘색: 왼쪽 검색 아이콘 #2b9fe0. 포커스 링 #141414
- reagent-row: 데모 학교 시약 6줄 — 염산 · 1병, 에탄올 · 200mL, 수산화나트륨 · 500g, 황산구리(II) · 250g, 아세톤 · 1L, 질산칼륨 · 300g. 행 = 시약명(title) + 2행 재고량·단위·입고일(caption). 행을 누르면 둘러보기 화면 3. 행 사이 12. 하늘색: 오른쪽 이동 화살표 #2b9fe0, 누른 행 배경 #e6f4fc. 재고 부족 행의 배지 안에는 하늘색 없음
- badge-low-stock: 재고 부족 2행(염산 · 1병, 에탄올 · 200mL)의 시약명 옆 "재고 부족"(#d6246a 채움, #ffffff label, rounded 9999). 하늘색 없음
- ex-empty-state-card: 검색 결과 0건일 때 "찾는 시약이 없어요". 가입·등록 버튼은 두지 않는다(시약 등록 진입 숨김). 하늘색: 안내 아이콘 #2b9fe0
- guest-lock: #707070 자물쇠 아이콘. tab-bar 안 "QR 스캔"·"기록" tab-item에 2개, 데스크탑 nav-pill "QR 스캔"·"사용 기록 내역" 링크 옆. 누르면 ex-toast. 핑크·하늘색 없음
- ex-toast: 잠긴 탭을 누르면 tab-bar 위에 "가입하면 쓸 수 있어요". 둘러보기 화면 13과 같은 모양(#141414 채움, #ffffff 자물쇠 아이콘·문구, rounded 16, 그림자 없음). 핑크 금지
- tab-bar: 모바일 전용 하단 탭바 1개(둘러보기 화면 13과 같음: 전폭 사각형, y 780~844, rounded 0, #ffffff + 위 1px #f0f0f0, 그림자 없음). 리스트 스크롤 영역은 tab-bar 위쪽 선에서 끝난다. 데스크탑 없음. 하늘색: 활성 tab-item 아이콘만
- tab-item: 4개 "홈"(둘러보기 화면 13) · "시약"(둘러보기 화면 2) · "QR 스캔"(guest-lock) · "기록"(guest-lock). 같은 폭, 높이 48, rounded 0. 이 화면의 활성 = "시약": #2b9fe0 아이콘 + 라벨 #141414. 비활성 3개: 아이콘·라벨 #707070
### 반영한 레퍼런스
- https://uibowl.io/name/%EC%95%84%ED%8C%8C%ED%8A%B8%EC%95%84%EC%9D%B4?patterns=%EB%A7%88%EC%9D%B4%ED%8E%98%EC%9D%B4%EC%A7%80&patternName=%EB%B9%84%EB%A1%9C%EA%B7%B8%EC%9D%B8%ED%96%88%EC%9D%84%20%EA%B2%BD%EC%9A%B0
- https://uibowl.io/name/%EC%8F%98%EC%B9%B4?patterns=%EB%A9%94%EC%9D%B8&patternName=%EB%A1%9C%EA%B7%B8%EC%9D%B8%20%EC%A0%84
- https://uibowl.io/name/%EC%BD%94%EC%98%A4%EB%A1%B1%EB%AA%B0?patterns=%EB%B6%81%EB%A7%88%ED%81%AC%C2%B7%EC%9C%84%EC%8B%9C%EB%A6%AC%EC%8A%A4%ED%8A%B8&patternName=%EB%A1%9C%EA%B7%B8%EC%9D%B8%20%EC%A0%84
- https://uibowl.io/name/%EC%BD%94%EC%98%A4%EB%A1%B1%EB%AA%B0?patterns=%EC%9E%A5%EB%B0%94%EA%B5%AC%EB%8B%88&imgId=cms36dumn0007l7041q8folw3

## 둘러보기 화면 3
데모 학교 시약 상세(예시: 염산). 구조는 runs/20261002-1441 화면 3(학생)과 같다. 정보·사용 기록 표·MSDS 열람은 그대로 쓸 수 있고, 하단 "사용 기록" 버튼만 잠근다. 교사·admin용 "입고" 버튼은 숨긴다.
모바일 위→아래: nav-pill → guest-banner → reagent-detail-card → segmented-control → 표 → msds-entry → 하단 고정 "사용 기록" 버튼(tab-bar 바로 위, 버튼 아래 끝과 tab-bar 위쪽 선 사이 16) → tab-bar. 활성 탭 "시약".
데스크탑: nav-pill → guest-banner → 왼쪽 reagent-detail-card·표, 오른쪽 msds-entry, 하단 "사용 기록" 버튼. tab-bar 없음.
### 구성 요소
- nav-pill: 뒤로가기(둘러보기 화면 2) + 제목 "시약 상세" + 학교명 "데모 학교" 텍스트. 학교 전환 없음. 하늘색: 뒤로가기 아이콘 #2b9fe0
- guest-banner: nav-pill 바로 아래 전폭 띠 1개. 둘러보기 화면 13과 같은 위치·문구·모양(#e6f4fc 채움, rounded 0, "둘러보는 중 — 가입하면 우리 학교 데이터로 시작해요" body-sm #141414 + 오른쪽 button-primary "가입하기")
- button-primary: ① guest-banner 안 "가입하기"(#141414 채움, #ffffff 글자, rounded 9999, 높이 44 이상) → 화면 14. ② 하단 고정 전폭 "사용 기록" — 둘러보기에서는 비활성 모양(#f0f0f0 채움, 라벨 #707070, rounded 9999, 높이 44 이상) + 라벨 앞 guest-lock. 누르면 화면 4로 가지 않고 ex-toast. 하늘색 없음
- reagent-detail-card: 상단 요약. 시약명 "염산"(title), 현재 재고량 "1"(display) + "병", 입고일 라벨-값(caption 라벨, 예: "2026-09-01"). 하늘색 없음
- badge-low-stock: reagent-detail-card 안 시약명 옆 "재고 부족"(#d6246a 채움, #ffffff label, rounded 9999). 하늘색 없음
- segmented-control: "정보 / 사용 기록" 두 탭, 활성 하나. 예시 상태 = "정보"
- segmented-control-active: 활성 탭 흰 pill. 하늘색: 활성 탭 아래 #2b9fe0 인디케이터(글자는 #141414)
- ex-data-table-cell: "정보" 탭 = 시약 속성 라벨-값 표(종류 "산", 입고일, 보관 위치 "시약장 1 · 2단"), "사용 기록" 탭 = 날짜·사용자·사용량 3열 표(데모: 오늘 · 학생 A · 20mL, 9월 24일 · 교사 B · 30mL). 읽기 전용. 하늘색: 가장 최근 사용 기록 행 배경 #e6f4fc
- msds-entry: msds-qr-tile(MSDS QR 1:1, 독립 블록 중앙, 아래 설명 "QR로 MSDS 열기") + button-pill-soft "MSDS 보기 ↗". 둘러보기에서도 잠그지 않고 그대로 열린다. 하늘색: "MSDS 보기 ↗" 바깥 화살표 아이콘 #2b9fe0(라벨 #141414). QR 이미지는 흑백
- guest-lock: #707070 자물쇠 아이콘. 하단 "사용 기록" 버튼 라벨 앞 1개(쓰기 동작 잠금), tab-bar 안 "QR 스캔"·"기록" tab-item에 2개, 데스크탑 nav-pill "QR 스캔"·"사용 기록 내역" 링크 옆. 핑크·하늘색 없음
- ex-toast: 잠긴 "사용 기록" 버튼·잠긴 탭을 누르면 tab-bar 위에 "가입하면 쓸 수 있어요". 둘러보기 화면 13과 같은 모양(#141414 채움, #ffffff 자물쇠 아이콘·문구, rounded 16, 그림자 없음). 핑크 금지
- tab-bar: 모바일 전용 하단 탭바 1개(둘러보기 화면 13과 같음: 전폭 사각형, y 780~844, rounded 0, #ffffff + 위 1px #f0f0f0, 그림자 없음). 하단 고정 "사용 기록" 버튼은 이 바 위에 쌓는다. 데스크탑 없음. 하늘색: 활성 tab-item 아이콘만
- tab-item: 4개 "홈"(둘러보기 화면 13) · "시약"(둘러보기 화면 2) · "QR 스캔"(guest-lock) · "기록"(guest-lock). 같은 폭, 높이 48, rounded 0. 이 화면의 활성 = "시약": #2b9fe0 아이콘 + 라벨 #141414. 비활성 3개: 아이콘·라벨 #707070
### 반영한 레퍼런스
- https://uibowl.io/name/%EC%B1%84%EB%B9%84?patterns=%EB%A9%94%EC%9D%B8&imgId=cmoi0a0cw000kjv049hmrvovp
- https://uibowl.io/name/%ED%95%B4%ED%94%BC%EB%AC%B8%EB%8D%B0%EC%9D%B4?patterns=%EC%98%A8%EB%B3%B4%EB%94%A9&imgId=cmtwleyy0002ijr04dxtnh7zj
- https://uibowl.io/name/%ED%8F%AC%EC%8A%A4%ED%85%94%EB%9F%AC?patterns=%EB%A1%9C%EA%B7%B8%EC%9D%B8%C2%B7%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85&imgId=cmr9wx3ii000bl804c5z1vixq
- https://uibowl.io/name/%EC%BB%AC%EB%A6%AC?patterns=%EC%83%81%EC%84%B8%EC%A0%95%EB%B3%B4%20%28PDP%29&imgId=cmfyzh8s9000xkw04nno3avlo

## 역할별 노출
앱 전체 기준 개수. runs/20261002-2019 표를 그대로 옮겼다. 화면 15는 로그인 전 화면이라 표의 컴포넌트를 담지 않고, 둘러보기 화면은 역할이 없는 비회원 화면이라 표에 넣지 않는다(게스트는 R 규칙 대상 아님). 숫자는 바뀌지 않는다.

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
