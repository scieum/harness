# S2 설계 — run 20261008-1233

대상 화면: 1 (로그인) · 14 (회원가입) · 15 (랜딩) · 상태 화면 14-no-school · 둘러보기 화면 13 · 2 · 3 · 16 (input.json guest_screens) · 키스크린: 15-desktop, 14-desktop, 2-guest-desktop
학교: 화면 1·14·15는 로그인 전이라 현재 학교명을 표시하지 않는다. 둘러보기 화면은 "데모 학교" 1종만 표시한다(input.json school_name "샘플고등학교"는 이번 대상 화면 어디에도 나오지 않는다).
변경 사유: 2026-10-08 사용자 결정 "데스크톱 2차" — 로그인 전 desktop(1·14·15)은 nav-pill 대신 전폭 web-header, 1·14는 왼쪽 폼 / 오른쪽 소개 패널 반 나눔(14는 번호 섹션 "1 학교 선택" → "2 계정"), 15는 웹 랜딩. 둘러보기 desktop은 로그인 후와 같은 app-sidebar("데모 학교", 홈·시약 + 잠긴 기록·QR 찾기 2, 관리 메뉴 숨김) + 본문 위 guest-banner. 둘러보기 16(MSDS 요약, 읽기 전용)을 새로 더한다.
근거: docs/design.md "Pre-login desktop (screens 1·14·15)"·"Desktop shell"·"Guest mode"·"Landing"·"School level"·"MSDS summary", docs/story-service.md 결정 사항("학교 선택"·"랜딩"·"둘러보기"·"MSDS 요약"), harness/rules.json(desktop_shell.pre_login, guest.desktop·sidebar_locks·hidden_components, screens_required 14·15, variants 14 no-school, never.N1 school_select_levels, msds_summary, roles R1~R7, colors), research/s1-adopt.md, neis.json(화면 14 목록 값).
모바일 기준 설계(수정하지 않고 옮김): 화면 1 = runs/20261002-2019, 화면 14·14-no-school = runs/20261007-1305, 화면 15 = runs/20261003-1212, 둘러보기 = runs/20261003-1212 둘러보기 섹션의 숨김·잠금 방식을 최신 일반 화면(runs/20261008-0936 화면 13·2·3·16, 학생 구성)에 입힌 것. 모바일에서 바뀌는 것은 하나뿐 — 화면 15 feature-card ② 설명을 학교급이 들어간 4단계("시/도 → 지역 → 학교급 → 학교")로 맞춘다(story-service "학교 선택" 2026-10-07).
색·폰트·모서리·간격은 docs/design.md와 harness/rules.json을 따른다. 허용 색 밖의 값은 쓰지 않는다. 그림자는 쓰지 않는다(segmented-control-active 예외).
- 핑크 #d6246a·연핑크 #fbe9f0는 badge-low-stock 안에서만 쓴다(화면 15 예시 배지, 둘러보기 재고 부족 표시). 1·14·14-no-school·잠금 안내·학교 0개 안내에는 쓰지 않는다.
- 하늘색 #2b9fe0·옅은 하늘색 #e6f4fc는 선택·현재 위치·진행·아이콘·안내 띠에만 쓴다. 글자색 금지(그 위 글자 #141414), badge-low-stock·button-primary 안에는 쓰지 않는다.
- 빨강 #ff0000은 둘러보기 16 ghs-pictogram 마름모 테두리 안에서만 쓴다.
학교 선택은 회원가입(화면 14)에만 있다. 화면 1·15·둘러보기 화면에는 학교 선택·학교 관련 입력이 없다. 학교 목록은 서버가 불러온 NEIS 값을 보여 줄 뿐이고, 고른 학교는 계정에 저장되어 로그인 후 그 학교 데이터만 보인다(N1).
외부 서비스 연결 값(NEIS 학교 목록·MSDS 요약)은 서버에서만 다룬다. 어떤 화면에도 연결 값 입력 칸·외부 서비스 설정·AI 엔진 선택 UI·관련 문구를 두지 않는다(N2).
1·14·15는 로그인 전 화면이라 역할 구분이 없고, 둘러보기는 역할이 없는 비회원 화면이다. 이번 대상 화면은 역할별 노출 표의 숫자를 바꾸지 않는다.

로그인 전 desktop 공통(1440×900, rules.json desktop_shell.pre_login): nav-pill·app-sidebar·tab-bar 없음.
- web-header: 전폭 상단 바(x 0, 폭 1440, 높이 64, rounded 0), #ffffff 채움 + 아래쪽 1px #f0f0f0 선, 그림자 없음, 좌우 여백 32. 왼쪽 "Lab_Stock" 워드마크(link #141414, → 화면 15), 오른쪽 button-outline "로그인"(→ 화면 1) + button-primary "회원가입"(→ 화면 14), 사이 8. 지금 화면 자기 버튼은 뺀다(화면 1 = "회원가입"만, 화면 14 = "로그인"만, 화면 15 = 둘 다). 하늘색 없음.
- 1·14 반 나눔: web-header 아래(y 64~900) 왼쪽 절반 폭 720 = 폼 영역(#ffffff, 가운데 단일 열 폭 440, 위 여백 64), 오른쪽 절반 폭 720 = 서비스 소개 패널(#f3f3f3 채움, rounded 0, 여백 64): 맨 위 heading-2 "과학실 시약, 학교별로 한눈에 관리해요" + body-lg(#707070) 한 줄 → feature-card 4개 세로 목록(사이 12). 폼이 길면 왼쪽 열만 스크롤되고 오른쪽 패널은 고정.
- 모바일은 승인본 그대로 nav-pill을 유지한다(web-header는 desktop 전용).

둘러보기 공통(13·2·3·16):
- 숨김(rules.json guest.hidden_components): stock-intake, reagent-register, manual-upload, user-manage, cabinet-edit, vendor-register, vendor-link, reorder-alert-card, school-select-sido, school-select-region, school-select-school, threshold-edit, location-edit, slot-assign, qr-print, cabinet-add, doc-upload, msds-search, msds-bulk-banner, location-suggest. 이 이름의 컴포넌트와 그 진입 버튼은 둘러보기 프레임(모바일·데스크톱)에 하나도 두지 않는다.
- 모바일(390×844) 위→아래: nav-pill(워드마크 또는 ‹ + 제목 + "데모 학교", nav-account-menu 없음) → guest-banner(전폭, nav-pill 아래 고정) → 최신 일반 화면 본문(학생 구성) → 하단 tab-bar(y 780~844, 폭 390, rounded 0, #ffffff + 위쪽 1px #f0f0f0 선). tab-item 4개 "홈"·"시약"·"QR 스캔"·"기록" 중 "QR 스캔"·"기록"에 guest-lock(탭 안 잠금 2).
- 데스크톱(1440×900): nav-pill·tab-bar 없음. app-sidebar(왼쪽 폭 240, 높이 전체, rounded 0, #f3f3f3 + 오른쪽 1px #f0f0f0 선): 맨 위 "Lab_Stock" 워드마크 + 학교명 "데모 학교"(title #141414, 전환 없음) → sidebar-item 4개 "홈"(→ 둘러보기 13) · "시약"(→ 둘러보기 2) · "기록"(guest-lock) · "QR 찾기"(guest-lock) — 사이드바 안 잠금은 이 2개뿐. "시약장"과 "관리"·"학교 설정" 묶음(입고·실험 매뉴얼·재주문 알림·사용자·판매처)은 두지 않는다. 맨 아래 이름·역할·nav-account-menu 대신 body-sm(#707070) "둘러보는 중" + button-outline "로그인"(→ 화면 1). 본문 = 사이드바 오른쪽 폭 1200: 맨 위 guest-banner(본문 폭 전체, rounded 0, 페이지 이동·드로어 열림과 관계없이 같은 자리 고정, 아래 내용을 밀어 내림 — 겹치지 않음) → 페이지 여백 32 안 화면 내용. detail-drawer는 guest-banner 아래부터 열린다.
- 잠금 동작: guest-lock이 붙은 항목을 누르면 화면 이동 없이 ex-toast "가입하면 쓸 수 있어요"(모바일 tab-bar 위, 데스크톱 오른쪽 아래). 가입 진입은 guest-banner "가입하기"(→ 화면 14) 하나로 통일한다.
- 데모 학교 예시 데이터(13·2·3·16 공통): 오늘 = 2026-10-07. 전체 시약 24종, 재고 부족 2종 — 염산 · 1병, 에탄올 · 200 mL. 그 밖 시약 수산화나트륨 · 500 g, 황산구리(II) · 250 g, 아세톤 · 1 L, 질산칼륨 · 300 g. 시약장 1개(1번 시약장, 칸 8개 중 지정 7 · 미지정 1). 최근 사용 기록 3줄: 염산 · 학생 A · 20 mL · 오늘 10:20 / 에탄올 · 교사 B · 50 mL · 어제 14:05 / 황산구리(II) · 학생 C · 5 g · 10월 1일.

## 화면 1
로그인. 개인 이메일 + 비밀번호만 받는다. 학교 관련 입력·표시, 아이디 찾기·소셜 로그인·자동 로그인은 두지 않는다. 모바일 = runs/20261002-2019 화면 1 그대로.
모바일(390×844) 위→아래: nav-pill → ex-auth-form-card(제목 → 이메일 → 비밀번호 → 로그인 버튼 → 비밀번호 찾기 링크) → 카드 아래 "아직 회원이 아니신가요?" + "회원가입 ›". 좌우 여백 16, 블록 사이 24. 하단 탭바 없음.
데스크톱 배치: web-header(오른쪽 button-primary "회원가입"만) | 아래 반 나눔 — 왼쪽 폼 열 폭 440(heading-1 "로그인" + body-lg "개인 이메일로 로그인하세요" → 이메일 → 비밀번호 → 전폭 "로그인" → 가운데 "비밀번호 찾기" → 맨 아래 "아직 회원이 아니신가요? 회원가입 ›") / 오른쪽 #f3f3f3 서비스 소개 패널(한 줄 소개 + feature-card 4개 목록). 하단 탭바 없음.
### 구성 요소
- web-header: 데스크톱 전용. 로그인 전 공통 규격(높이 64, rounded 0, #ffffff + 아래 1px #f0f0f0). 왼쪽 "Lab_Stock" 워드마크(→ 화면 15), 오른쪽 button-primary "회원가입"(→ 화면 14)만 — 지금 화면인 "로그인" 버튼은 뺀다. 하늘색 없음
- nav-pill: 모바일 전용. "Lab_Stock" 워드마크만 표시. 로그인 전이라 섹션 링크·학교명·CTA·nav-account-menu 없음. 데스크톱에는 두지 않는다. 하늘색 없음
- ex-auth-form-card: 로그인 폼. 모바일 = 카드(#ffffff, 1px #f0f0f0 테두리, rounded 24, 안쪽 여백 24) 안 제목 "로그인"(heading-3) + 보조 문구 "개인 이메일로 로그인하세요"(body-lg) → text-input 2개(라벨 위·입력 아래, 사이 12) → button-primary "로그인" → 버튼 바로 아래 가운데 "비밀번호 찾기" 밑줄 텍스트 링크(body-sm #707070, 누름 영역 44 이상). 데스크톱 = 카드 테두리 없이 왼쪽 폼 열(폭 440) 안에 같은 순서, 제목은 heading-1 "로그인". 학교 관련 필드·문구 없음. 하늘색 없음
- text-input: 라벨 "개인 이메일"(플레이스홀더 "name@example.com" #adadad), 라벨 "비밀번호"(가림 입력, 오른쪽 보기 토글 눈 아이콘 #707070). #f0f0f0 채움, 테두리 없음, rounded 16, 포커스 링 2px #141414. 하늘색 없음
- button-primary: 폼 안 전폭 "로그인"(#141414 채움, #ffffff 글자 link, rounded 9999, 높이 44 이상). 두 칸이 모두 채워지기 전 비활성(예시 상태 = 비활성). 데스크톱은 web-header 오른쪽 "회원가입"(폭은 라벨에 맞춤)도 같은 모양. 하늘색 없음
- button-pill-soft: 폼 아래 한 줄 "아직 회원이 아니신가요?"(body-sm #707070) 옆 "회원가입 ›"(#f3f3f3 채움, 라벨 #141414, rounded 9999, 높이 44 이상) → 화면 14. 모바일 = 카드 아래, 데스크톱 = 왼쪽 폼 열 맨 아래. 하늘색: › 아이콘 #2b9fe0(라벨 #141414)
- feature-card: 데스크톱 전용. 오른쪽 서비스 소개 패널(#f3f3f3) 안 4개 세로 목록(사이 12). 패널 바탕과 구분되도록 카드 = #ffffff 채움, 테두리 없음, rounded 24, 안쪽 여백 24, 왼쪽 아이콘(24, #2b9fe0) + 오른쪽 제목(heading-4 #141414) · 한 줄 설명(body #707070). 내용은 화면 15 feature-card 4개와 같음(① 학교별 분리 ② NEIS 학교 선택 ③ QR 스캔 ④ 재고 부족 알림). 이 패널에서는 badge-low-stock을 두지 않는다(로그인 화면에 핑크 없음). 하늘색: 아이콘만
### 반영한 레퍼런스
- https://uibowl.io/website/%EB%AE%A4%EC%A6%88%EB%B0%94%EC%9D%B4%20Museby?patterns=%EB%A1%9C%EA%B7%B8%EC%9D%B8%C2%B7%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85&imgId=cmttba7s2000okz04vi1241gp
- https://uibowl.io/website/%EC%9E%94%EB%94%94?patterns=%EB%A1%9C%EA%B7%B8%EC%9D%B8%C2%B7%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85&imgId=cmpz4v0pv00b7ld04afw5a58j
- https://uibowl.io/website/%EC%9C%A0%EA%B4%91%EA%B8%B0?patterns=%EB%A1%9C%EA%B7%B8%EC%9D%B8%C2%B7%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85&imgId=cmtb2zqla000kjr04j48pf8ll
- https://uibowl.io/website/%EB%A7%88%EC%9D%B4%ED%81%AC%EB%A1%9C%EC%86%8C%ED%94%84%ED%8A%B8%20%ED%81%B4%EB%9E%98%EB%A6%AC%ED%8B%B0%20(Microsoft%20Clarity)?patterns=%EB%9E%9C%EB%94%A9%ED%8E%98%EC%9D%B4%EC%A7%80&imgId=cmt180ji1000dkz04ef56j21k

## 화면 14
회원가입. 화면 1 "회원가입 ›", 화면 15·web-header "회원가입", guest-banner "가입하기"로 들어온다. 학교(시/도 → 지역 → 학교급 → 학교)와 계정 정보(이름·개인 이메일·비밀번호)를 받는다. 모바일 = runs/20261007-1305 화면 14 그대로. 현재 학교명은 표시하지 않는다(학교를 고르는 중).
예시 상태(14-mobile · 14-desktop, neis.json): 시/도 "충청북도" 선택됨 → 지역 "청주시" 선택됨 → 학교급 아직 고르지 않음(3칸 모두 #707070 라벨, 흰 pill 없음) → 학교 칸 비활성 "학교급을 먼저 골라 주세요". 계정 칸 비어 있음, 약관 모두 미동의, 가입 버튼 비활성. 진행 막대 2칸 채움.
모바일(390×844) 위→아래: nav-pill → ex-auth-form-card(제목 → 학교 블록[안내 박스 → 진행 막대 → 시/도 → 지역 → 학교급 → 학교] → 계정 블록[이름 → 개인 이메일 → 비밀번호 → 비밀번호 확인] → 약관 동의) → 카드 아래 로그인 줄 → 하단 고정 "가입하기". 좌우 여백 16, 칸 사이 12, 블록 사이 24. 하단 탭바 없음.
데스크톱 배치: web-header(오른쪽 button-outline "로그인"만) | 아래 반 나눔 — 왼쪽 폼 열 폭 440(heading-1 "회원가입" + body-lg 한 줄 → 번호 섹션 "1 학교 선택"[안내 박스 → 진행 막대 → 시/도 → 지역 → 학교급 → 학교] → 1px #f0f0f0 구분선 → "2 계정"[이름 → 개인 이메일 → 비밀번호 → 비밀번호 확인 → 약관 동의 → 전폭 "가입하기"] → 맨 아래 "이미 계정이 있으신가요? 로그인 ›", 왼쪽 열만 스크롤) / 오른쪽 #f3f3f3 서비스 소개 패널(한 줄 소개 + feature-card 4개 목록, 고정). 시/도·지역·학교 목록은 바텀시트 대신 그 칸 바로 아래 붙는 드롭다운. 하단 탭바 없음.
### 구성 요소
- web-header: 데스크톱 전용. 로그인 전 공통 규격(높이 64, rounded 0, #ffffff + 아래 1px #f0f0f0). 왼쪽 "Lab_Stock" 워드마크(→ 화면 15), 오른쪽 button-outline "로그인"(→ 화면 1)만 — 지금 화면인 "회원가입" 버튼은 뺀다. 하늘색 없음
- nav-pill: 모바일 전용. 뒤로가기(화면 1) + "Lab_Stock" 워드마크 + 제목 "회원가입". 학교명·nav-account-menu 없음. 데스크톱에는 두지 않는다. 하늘색: 뒤로가기 아이콘 #2b9fe0
- ex-auth-form-card: 가입 폼. 모바일 = 카드(#ffffff, 1px #f0f0f0 테두리, rounded 24, 안쪽 여백 24), 제목 "회원가입"(heading-3) + 보조 문구 "우리 학교를 고르고 계정을 만드세요"(body-lg). 데스크톱 = 카드 테두리 없이 왼쪽 폼 열(폭 440), 제목 heading-1 "회원가입", 블록 소제목을 번호 섹션 머리로 바꿈: heading-4 "1 학교 선택"(번호 "1"은 같은 줄 앞, #141414) → 섹션 사이 1px #f0f0f0 구분선(위아래 여백 24) → heading-4 "2 계정". ① 학교 블록(데스크톱 = 섹션 1): 안내 박스 1개(#e6f4fc 채움, rounded 16, 여백 16, 왼쪽 정보 아이콘 #2b9fe0 + body-sm #141414 "고른 학교의 시약·기록만 보여요. 가입한 뒤에는 바꿀 수 없어요") → 4단계 진행 막대(시/도 → 지역 → 학교급 → 학교 중 채운 단계만 #2b9fe0, 나머지 #e0e0e0, rounded 9999, 예시 = 2칸 채움) → 시/도·지역·학교급·학교 4칸을 이 순서로 세로로 쌓음. ② 계정 블록(데스크톱 = 섹션 2): text-input 4개(라벨 위·입력 아래, 라벨 옆 caption "필수" #707070). ③ 약관 동의(계정 블록 안 마지막): "모두 동의" 한 줄(body) → 1px #f0f0f0 구분선 → 필수 약관 2줄 "서비스 이용약관 동의 (필수)", "개인정보 수집·이용 동의 (필수)"(body-sm), 각 줄 오른쪽 › 전문 보기, 왼쪽 원형 체크(rounded 9999, 누름 영역 44 이상: 미동의 = 1px #e0e0e0 원, 동의 = #2b9fe0 채움 원 + #ffffff 체크). 예시 = 모두 미동의. 하늘색: 안내 박스, 진행 막대 채운 구간, 동의 체크 원, 약관 › 아이콘(글자는 모두 #141414)
- school-select-sido: 학교 블록 첫 번째 칸 "시/도"(▾ 선택 상자, #f0f0f0, rounded 16). 누르면 목록(neis.json sido_list, 17개) — 모바일 = 바텀시트(제목 "시/도 선택" + 오른쪽 위 × 닫기, 1px #e0e0e0 테두리, 위쪽 rounded 24, 딤 없음), 데스크톱 = 칸 바로 아래 붙는 드롭다운(#ffffff, 1px #e0e0e0, rounded 24, 칸과 같은 폭, 목록이 길면 안쪽 스크롤). 예시 값 "충청북도"(선택됨). 시/도를 바꾸면 지역·학교급·학교가 비워진다. 하늘색: 선택된 칸 = #e6f4fc 바탕 + 오른쪽 #2b9fe0 체크 아이콘(값 글자 #141414), 목록 현재 선택 행 #e6f4fc + 체크 #2b9fe0
- school-select-region: 두 번째 칸 "지역(시/군/구)". 시/도를 고르기 전 비활성(#f0f0f0 바탕, 글자 #adadad). 목록 = 고른 시/도의 지역(neis.json region_list, 11개; 모바일 바텀시트 "지역 선택" + ×, 데스크톱 칸 아래 드롭다운). 예시 값 "청주시"(선택됨). 지역을 바꾸면 학교가 비워진다(학교급 유지). 하늘색: 선택된 칸 #e6f4fc + #2b9fe0 체크(글자 #141414), 목록 현재 선택 행 #e6f4fc + 체크 #2b9fe0
- school-select-kind: 세 번째 칸 "학교급"(caption "필수") — segmented-control 3칸 "초등학교 · 중학교 · 고등학교"(neis.json kind_list, #f3f3f3 트랙, rounded 9999, 같은 폭 pill 누름 영역 44 이상). 기본값 없음: 고르기 전 흰 pill(segmented-control-active) 없음, 3칸 라벨 #707070. 지역을 고르기 전 트랙 전체 비활성(라벨 #adadad). 고르면 그 칸이 흰 pill(segmented-control-active, 1px #2b9fe0 테두리, 라벨 #141414)로 떠오르고 학교 칸이 켜진다. 학교급을 바꾸면 학교가 비워진다. 예시 = 지역은 골랐고 학교급은 아직(3칸 #707070, 선택 가능). 특수학교·각종학교 칸 없음. 하늘색: 선택 칸 테두리 #2b9fe0만
- school-select-school: 네 번째 칸 "학교". 학교급을 고르기 전 비활성 — #f0f0f0 바탕 + 칸 안 플레이스홀더 "학교급을 먼저 골라 주세요"(#adadad) + 오른쪽 ▾ #adadad(예시 상태). 학교급을 고르면 플레이스홀더 "학교 선택"(#adadad) + ▾ #707070로 켜지고, 누르면 목록(모바일 바텀시트 "학교 선택" + ×, 데스크톱 칸 아래 드롭다운; 둘 다 위쪽 학교 이름 검색 text-input) = 고른 지역·학교급의 학교(neis.json school_list, 고등학교 38개). 행 = 학교명(title) + 주소 보조줄(caption #707070). 고르면 #e6f4fc 바탕 + #2b9fe0 체크(글자 #141414). 학교 0개면 상태 화면 14-no-school. 하늘색: 목록 현재 선택 행 #e6f4fc + 체크 #2b9fe0
- segmented-control: school-select-kind 트랙(#f3f3f3, rounded 9999). 고르지 않은 칸 라벨 #707070
- segmented-control-active: 학교급을 고른 뒤의 흰 pill(#ffffff, 그림자 허용 예외, 1px #2b9fe0 테두리, 라벨 #141414). 예시 상태에서는 없음
- text-input: 계정 블록 4개 "이름", "개인 이메일"(플레이스홀더 "name@example.com"), "비밀번호"(가림, 보기 토글 눈 아이콘 #707070), "비밀번호 확인"(가림). #f0f0f0 채움, 테두리 없음, rounded 16, 포커스 링 2px #141414. "비밀번호 확인" 아래 일치 여부 한 줄(caption): 일치 = #2b9fe0 체크 아이콘 + "비밀번호가 일치해요"(#141414), 불일치 = "비밀번호가 일치하지 않아요"(#141414), 비어 있으면 숨김. 학교 목록 검색 칸도 같은 모양. 하늘색: 일치 체크 아이콘만
- button-primary: 전폭 "가입하기"(#141414 채움, #ffffff 글자 link, rounded 9999, 높이 44 이상). 학교 4칸·계정 4칸·필수 약관 2개가 모두 채워지고 비밀번호가 일치하기 전 비활성(예시 = 비활성). 누르면 계정에 고른 학교를 저장하고 화면 13(홈)으로. 모바일 = 화면 하단 고정, 데스크톱 = 섹션 2 맨 아래(폼 열 폭). 하늘색 없음
- button-outline: 데스크톱 web-header 오른쪽 "로그인"(#ffffff, 1px #e0e0e0 테두리, 라벨 #141414, rounded 9999, 높이 44 이상) → 화면 1. 하늘색 없음
- button-pill-soft: 폼 아래 한 줄 "이미 계정이 있으신가요?"(body-sm #707070) 옆 "로그인 ›"(#f3f3f3 채움, 라벨 #141414, rounded 9999, 높이 44 이상) → 화면 1. 모바일 = 카드 아래, 데스크톱 = 왼쪽 폼 열 맨 아래. 하늘색: › 아이콘 #2b9fe0
- feature-card: 데스크톱 전용. 오른쪽 서비스 소개 패널 안 4개 세로 목록 — 화면 1과 같은 모양·내용(#ffffff 카드, rounded 24, 아이콘 #2b9fe0 + 제목 + 한 줄, badge-low-stock 없음). 두 화면의 반 나눔 틀을 맞춘다. 하늘색: 아이콘만
### 반영한 레퍼런스
- https://uibowl.io/website/%EC%9C%A0%EA%B4%91%EA%B8%B0?patterns=%EB%A1%9C%EA%B7%B8%EC%9D%B8%C2%B7%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85&imgId=cmtb2zqla000kjr04j48pf8ll
- https://uibowl.io/website/%EB%AE%A4%EC%A6%88%EB%B0%94%EC%9D%B4%20Museby?patterns=%EB%A1%9C%EA%B7%B8%EC%9D%B8%C2%B7%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85&imgId=cmttba7s2000okz04vi1241gp
- https://uibowl.io/website/%EC%9E%94%EB%94%94?patterns=%EB%A1%9C%EA%B7%B8%EC%9D%B8%C2%B7%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85&imgId=cmpz4v0pv00b7ld04afw5a58j

## 상태 화면 14-no-school
화면 14에서 학교급까지 골랐는데 그 지역에 그 학교급 학교가 0개인 상태. 학교 칸 자리를 그대로 두고 그 안에 안내 한 줄만 넣는다(레퍼런스: 목록 자리에 빈 상태 2줄). 모바일 = runs/20261007-1305 상태 화면 14-no-school 그대로.
예시 상태(14-no-school-mobile · 14-no-school-desktop): 시/도 "충청북도" → 지역 "청주시" → 학교급 "고등학교" 선택됨(segmented-control-active) → 학교 칸 자리에 무채색 안내 "이 지역에 고등학교가 없어요 — 지역을 다시 골라 주세요". 진행 막대 3칸 채움. 계정 칸 비어 있음, 가입 버튼 비활성. (neis.json 예시 값을 쓴 시안용 상태 — 실제 0개 여부와 무관하게 0개일 때의 모양.)
데스크톱 배치: 화면 14와 같음 — web-header("로그인"만) | 왼쪽 폼 열 번호 섹션 "1 학교 선택" → "2 계정" / 오른쪽 서비스 소개 패널. 섹션 1의 학교 칸 자리만 바뀐다. 하단 탭바 없음.
### 구성 요소
- web-header: 데스크톱 전용. 화면 14와 같음 — 왼쪽 워드마크, 오른쪽 button-outline "로그인"만. 하늘색 없음
- nav-pill: 모바일 전용. 화면 14와 같음 — 뒤로가기(화면 1) + "Lab_Stock" 워드마크 + 제목 "회원가입". 학교명 없음. 하늘색: 뒤로가기 아이콘 #2b9fe0
- ex-auth-form-card: 화면 14와 같은 가입 폼(데스크톱은 번호 섹션 "1 학교 선택" → 구분선 → "2 계정"). 학교 블록 안내 박스 → 4단계 진행 막대(예시 = 3칸 채움) → 시/도 → 지역 → 학교급 → 학교 자리. 계정 블록·약관 동의는 비어 있음·미동의. 하늘색: 안내 박스, 진행 막대 채운 구간, 약관 › 아이콘
- school-select-sido: "시/도" 값 "충청북도"(선택됨, #e6f4fc 바탕 + #2b9fe0 체크, 글자 #141414)
- school-select-region: "지역(시/군/구)" 값 "청주시"(선택됨, #e6f4fc 바탕 + #2b9fe0 체크, 글자 #141414). 안내 문구가 가리키는 다시 고를 칸
- school-select-kind: segmented-control 3칸 "초등학교 · 중학교 · 고등학교", "고등학교" 선택됨(segmented-control-active). 다른 학교급을 고르면 학교 칸이 다시 계산된다. 하늘색: 선택 칸 테두리 #2b9fe0(글자 #141414)
- school-select-school: 학교 칸 자리 그대로(같은 높이·폭, rounded 16, #f3f3f3 채움, 테두리 없음) 안에 ▾·선택 상자 대신 무채색 안내 한 줄 — #707070 정보 아이콘 + body-sm #141414 "이 지역에 고등학교가 없어요 — 지역을 다시 골라 주세요"({학교급} = 고른 학교급 이름). 누를 수 없음(목록이 열리지 않음). 핑크 없음, 하늘색 없음
- segmented-control: 학교급 트랙(#f3f3f3, rounded 9999). 고르지 않은 칸 라벨 #707070
- segmented-control-active: 선택된 학교급 "고등학교" 흰 pill(#ffffff, 그림자 허용 예외). 하늘색: 1px #2b9fe0 테두리(글자 #141414)
- text-input: 계정 블록 4칸(화면 14와 같음, 비어 있음)
- button-primary: 전폭 "가입하기" 비활성(학교 미선택). 하늘색 없음
- button-outline: 데스크톱 web-header "로그인" → 화면 1. 하늘색 없음
- button-pill-soft: 폼 아래 "이미 계정이 있으신가요?" + "로그인 ›" → 화면 1. 하늘색: › 아이콘 #2b9fe0
- feature-card: 데스크톱 전용. 오른쪽 서비스 소개 패널 4개 목록(화면 14와 같음). 하늘색: 아이콘만
### 반영한 레퍼런스
- https://uibowl.io/website/%EB%A6%AC%EB%94%94?patterns=%EB%82%B4%EC%97%AD&imgId=cmuq7e6jd000wjs046c714kre
- https://uibowl.io/website/%EC%9C%A0%EA%B4%91%EA%B8%B0?patterns=%EB%A1%9C%EA%B7%B8%EC%9D%B8%C2%B7%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85&imgId=cmtb2zqla000kjr04j48pf8ll

## 화면 15
랜딩. 앱을 처음 연 사람이 서비스가 무엇인지 보고 회원가입(화면 14)·로그인(화면 1)으로 가거나, 가입 없이 둘러보기(둘러보기 화면 13)로 간다. 캐러셀·소셜 로그인·대형 일러스트는 두지 않는다. 학교명·학교 선택·탭바 없음. 모바일 = runs/20261003-1212 화면 15 그대로(feature-card ② 설명만 학교급 4단계로).
CTA 위계: 채움 "회원가입" → 외곽선 "로그인" → 가장 약한 "둘러보기" 3단.
모바일(390×844) 위→아래: nav-pill → landing-hero → feature-card 4장 세로 목록(사이 12) → 하단 고정 영역(landing-cta 전폭 버튼 2개 세로 + 그 아래 guest-entry). 좌우 여백 16, hero와 카드 목록 사이 32. 하단 탭바 없음.
데스크톱 배치: web-header(오른쪽 "로그인" + "회원가입" 둘 다) | 웹 랜딩 본문(콘텐츠 폭 1200 가운데, 좌우 여백 120) — 위 64 여백 뒤 히어로 줄 2열: 왼쪽 landing-hero(왼쪽 정렬, 폭 680) / 오른쪽 그 옆 landing-cta(버튼 2개 나란히) + 그 아래 guest-entry(세로 묶음, 히어로 제목 줄과 아래 끝 맞춤) → 48 여백 → feature-card 4장 한 줄 4열(같은 폭, 사이 24). 하단 탭바 없음. 좁아지면 4열 → 2열 → 1열.
### 구성 요소
- web-header: 데스크톱 전용. 로그인 전 공통 규격(높이 64, rounded 0, #ffffff + 아래 1px #f0f0f0). 왼쪽 "Lab_Stock" 워드마크, 오른쪽 button-outline "로그인"(→ 화면 1) + button-primary "회원가입"(→ 화면 14), 사이 8. 하늘색 없음
- nav-pill: 모바일 전용. "Lab_Stock" 워드마크만 표시(#f3f3f3 바, rounded 9999, 그림자 없음). 섹션 링크·학교명·CTA 없음. 데스크톱에는 두지 않는다. 하늘색 없음
- landing-hero: 위→아래 작은 리드 "Lab_Stock"(body #707070) → 한 줄 소개 "과학실 시약, 학교별로 한눈에 관리해요"(heading-1 #141414) → 가벼운 부제 "시약 재고·사용 기록·MSDS를 QR로 연결하고, 재고가 부족하면 판매처까지 이어 줘요"(body-lg #707070). 모노크롬, 학교명 없음. 모바일·데스크톱 모두 왼쪽 정렬(데스크톱은 히어로 줄 왼쪽 열). 하늘색 없음
- feature-card: 기능 카드 4장(#f3f3f3 채움, 테두리 없음, rounded 24, 안쪽 여백 24). 위→아래 아이콘(24, #2b9fe0) → 제목(heading-4 #141414) → 한 줄 설명(body #707070). ① "학교별 분리" — "우리 학교 시약·재고·사용 기록만 보여요. 다른 학교와 섞이지 않아요"(건물) ② "NEIS 학교 선택" — "회원가입 때 시/도 → 지역 → 학교급 → 학교 순서로 우리 학교를 골라요"(위치 핀) ③ "QR 스캔" — "시약장 QR을 찍으면 시약 정보와 MSDS가 바로 열려요"(QR) ④ "재고 부족 알림" — "필요한 양보다 적으면 알려 주고 판매처로 연결해요"(종) + 제목 오른쪽 예시 badge-low-stock 1개. 모바일 = 전폭 세로 목록, 데스크톱 = 한 줄 4열. 하늘색: 아이콘만
- badge-low-stock: "재고 부족 알림" 카드 제목 옆 예시 배지 1개(#d6246a 채움, label "재고 부족" #ffffff, rounded 9999). 핑크는 이 배지 안에서만. 하늘색 없음
- landing-cta: 행동 영역. button-primary "회원가입"(→ 화면 14) + button-outline "로그인"(→ 화면 1). 모바일 = 화면 하단 고정 #ffffff 영역(위 1px #f0f0f0 선, 안쪽 여백 16)에 전폭 버튼 2개 세로(사이 8), 그 아래 8 간격 guest-entry. 데스크톱 = 히어로 줄 오른쪽 열(landing-hero 옆)에 두 버튼 나란히(사이 12, 각 폭은 라벨에 맞춤 + 좌우 여백 24). 하늘색 없음
- button-primary: landing-cta "회원가입", 데스크톱 web-header "회원가입"(#141414 채움, #ffffff 글자 link, rounded 9999, 높이 44 이상). 하늘색 없음
- button-outline: landing-cta "로그인", 데스크톱 web-header "로그인"(#ffffff, 1px #e0e0e0 테두리, #141414 글자 link, rounded 9999, 높이 44 이상). 하늘색 없음
- guest-entry: landing-cta 바로 아래 세 번째, 가장 조용한 행동 — button-pill-soft "둘러보기 ›" 1개(→ 둘러보기 화면 13, 데모 학교 홈). 모바일 = 하단 고정 영역 맨 아래 가운데, 데스크톱 = landing-cta 아래 12 간격 왼쪽 맞춤. 위 보조 문구 없음. 하늘색: › 아이콘 #2b9fe0
- button-pill-soft: guest-entry 안 "둘러보기 ›"(#f3f3f3 채움, 테두리 없음, 라벨 #141414 link, rounded 9999, 높이 44 이상, 폭은 라벨에 맞춤 — 회원가입·로그인보다 약한 위계). 하늘색: › 아이콘만
### 반영한 레퍼런스
- https://uibowl.io/website/%EB%A7%88%EC%9D%B4%ED%81%AC%EB%A1%9C%EC%86%8C%ED%94%84%ED%8A%B8%20%ED%81%B4%EB%9E%98%EB%A6%AC%ED%8B%B0%20(Microsoft%20Clarity)?patterns=%EB%9E%9C%EB%94%A9%ED%8E%98%EC%9D%B4%EC%A7%80&imgId=cmt180ji1000dkz04ef56j21k
- https://uibowl.io/website/%EB%A6%AC%EC%8A%A4%EB%8B%9D%EB%A7%88%EC%9D%B8%EB%93%9C?patterns=%EB%9E%9C%EB%94%A9%ED%8E%98%EC%9D%B4%EC%A7%80&imgId=cmsssa2md000vl404rq691ip5

## 둘러보기 화면 13
데모 학교 홈. 랜딩 guest-entry로 들어온다. 구조는 최신 학생 홈(runs/20261008-0936 화면 13)과 같고 요약 숫자는 데모 학교 값. reorder-alert-card·입고·사용자 관리 진입은 숨긴다. 사용 기록 입력·시약장 보기는 잠금(쓰기 동작 / 화면 11이 둘러보기 범위 밖).
모바일 위→아래: nav-pill → guest-banner → quick-action 2칸 한 줄 → home-summary ① 재고 요약 → home-summary ② 시약장 요약 → 최근 사용 기록 카드 → tab-bar(활성 "홈"). 카드 사이 24, 좌우 여백 16.
데스크톱 배치: app-sidebar("데모 학교", "홈" 현재) | 본문 = guest-banner → 페이지 머리(왼쪽 heading-2 "데모 학교" + body-sm #707070 "오늘 10월 7일 · 전체 시약 24종" / 오른쪽 quick-action 버튼 줄: button-outline "시약장 보기" + button-primary "사용 기록 입력", 둘 다 guest-lock) → 숫자 타일 줄 "지금 처리할 것"(학생 구성 = "재고 부족 2" 타일 1개) → 3열 위젯 격자(최근 사용 기록 data-table 2칸 폭 · 재고 부족 · 시약장 요약).
### 구성 요소
- app-sidebar: 데스크톱 전용. 둘러보기 공통 규격 — 맨 위 "Lab_Stock" + "데모 학교", 가운데 sidebar-item 4개, 맨 아래 "둘러보는 중" + button-outline "로그인". 사이드바 안 guest-lock 2개(기록·QR 찾기)
- sidebar-item: 데스크톱 전용. 4개 "홈"(현재: #e6f4fc 채움 + #2b9fe0 아이콘, 라벨 #141414) · "시약"(→ 둘러보기 2) · "기록"(라벨 오른쪽 guest-lock) · "QR 찾기"(라벨 오른쪽 guest-lock). 높이 44, rounded 0. 비활성 아이콘 #707070 · 라벨 #141414. 시약장·관리 메뉴 없음
- nav-pill: 모바일 전용. "Lab_Stock" 워드마크 + 학교명 "데모 학교". 학교 선택·전환·nav-account-menu 없음. 데스크톱에는 두지 않는다
- guest-banner: 전폭 띠 1개. #e6f4fc 채움, rounded 0, 안쪽 여백 위아래 8 · 좌우 16(데스크톱 좌우 32). 왼쪽 정보 아이콘 #2b9fe0 + 문구 "둘러보는 중 — 가입하면 우리 학교 데이터로 시작해요"(body-sm #141414), 오른쪽 끝 button-primary "가입하기". 모바일 = nav-pill 바로 아래, 데스크톱 = 사이드바 오른쪽 본문 맨 위 폭 1200. 띠 안 하늘색은 바탕·아이콘뿐
- button-primary: ① guest-banner "가입하기"(#141414 채움, #ffffff 글자 link, rounded 9999, 높이 44 이상, 폭은 라벨에 맞춤) → 화면 14. ② 데스크톱 페이지 머리 "사용 기록 입력" — 둘러보기에서는 비활성 모양(#f0f0f0 채움, 라벨 #707070) + 라벨 앞 guest-lock, 누르면 ex-toast. 하늘색 없음
- button-outline: 데스크톱 페이지 머리 "시약장 보기"(라벨 앞 guest-lock, 누르면 ex-toast), app-sidebar 맨 아래 "로그인"(→ 화면 1). #ffffff, 1px #e0e0e0, 라벨 #141414, rounded 9999, 높이 44 이상
- quick-action: 모바일 = 바로가기 2칸 한 줄(같은 폭, 사이 12). 칸 = #f3f3f3, rounded 16, 여백 16, 위 원형 아이콘 바탕(#e6f4fc, rounded 9999) 안 #2b9fe0 아이콘 + 아래 label #141414. "사용 기록 입력" · "시약장 보기", 둘 다 오른쪽 위 guest-lock. 데스크톱 = 페이지 머리 오른쪽 버튼 줄(button-outline "시약장 보기" + button-primary "사용 기록 입력", 둘 다 잠금). 입고·사용자 관리·시약장 설정 칸 없음. 하늘색: 아이콘 #2b9fe0 + 바탕 #e6f4fc
- home-summary: 모바일 = 요약 카드 2장(#ffffff, 1px #f0f0f0, rounded 24, 여백 24). ① 재고 요약: heading-4 "재고 부족 2개" + badge-low-stock "2" → 부족 시약 칩 줄(#f3f3f3, rounded 9999, label #141414 "염산 · 1병" / "에탄올 · 200 mL", → 둘러보기 3) → caption "전체 시약"(#707070) + "24종"(title). ② 시약장 요약: heading-4 "시약장 요약"(› 없음, 화면 11로 가지 않음) → display "1개" → 구간 막대(지정 #2b9fe0 + 미지정 #e0e0e0, rounded 9999) → body-sm #707070 "칸 8개 중 지정 7 · 미지정 1". 데스크톱 = ⓐ 숫자 타일 "재고 부족 2"(#ffffff, 1px #f0f0f0, rounded 24, 여백 24, caption 이름 + display 숫자 + badge-low-stock, → 둘러보기 2 재고 부족) ⓑ 위젯 "재고 부족"(칩 2개 + "전체 보기 ›" → 둘러보기 2) ⓒ 위젯 "시약장 요약"(같은 막대·문구, "전체 보기" 없음). 하늘색: 막대 지정 구간, › 아이콘. 핑크는 badge-low-stock 안에서만
- badge-low-stock: 재고 요약 개수 배지 "2", 데스크톱 "재고 부족 2" 타일 숫자 옆(#d6246a 채움, #ffffff label, rounded 9999). 하늘색 없음
- data-table: 데스크톱 전용 "최근 사용 기록" 위젯(2칸 폭, rounded 16 컨테이너, 1px #f0f0f0). 열 = 사용일 · 시약명 · 사용자 · 사용량, 3행(데모 데이터). 머리 오른쪽 "전체 보기"는 라벨 앞 guest-lock(화면 10이 범위 밖, 누르면 ex-toast). 행을 눌러도 이동하지 않는다(hover 없음)
- ex-data-table-cell: 데스크톱 data-table 머리행(caption #707070)·셀(body-sm), 행 구분 1px #f0f0f0
- reagent-row: 모바일 최근 사용 기록 카드(#ffffff, 1px #f0f0f0, rounded 24, heading-4 "최근 사용 기록") 안 3줄 = 시약명(title) + "학생 A · 20 mL"(body) + 시각 caption(#707070), #f3f3f3, rounded 16, 사이 12. 눌러도 이동 없음(화살표 없음). 하늘색 없음
- button-pill-soft: 모바일 최근 사용 기록 카드 "더 보기"(라벨 앞 guest-lock, 누르면 ex-toast), 데스크톱 위젯 머리 "전체 보기 ›"(재고 부족 위젯) · "전체 보기"(최근 사용 기록, guest-lock). #f3f3f3, 라벨 #141414, rounded 9999, 높이 44 이상. 하늘색: › 아이콘만
- guest-lock: #707070 작은 자물쇠 아이콘(16). 모바일 = quick-action 2칸, "더 보기", tab-bar "QR 스캔"·"기록" tab-item(탭 안 2). 데스크톱 = app-sidebar "기록"·"QR 찾기"(사이드바 안 2), 페이지 머리 "시약장 보기"·"사용 기록 입력", 최근 사용 기록 위젯 "전체 보기". 핑크·하늘색 없음
- ex-toast: 잠긴 항목을 누르면 2초간 "가입하면 쓸 수 있어요"(#141414 채움, 왼쪽 #ffffff 자물쇠 아이콘 + body-sm #ffffff, rounded 16, 여백 12·16, 그림자 없음). 모바일 tab-bar 위, 데스크톱 오른쪽 아래. 핑크 금지
- tab-bar: 모바일 전용 하단 탭바 1개(둘러보기 공통 규격). 데스크톱에는 두지 않는다. 하늘색: 활성 tab-item 아이콘만
- tab-item: 4개 "홈"(둘러보기 13) · "시약"(둘러보기 2) · "QR 스캔"(guest-lock) · "기록"(guest-lock). 같은 폭, 높이 48, rounded 0. 활성 = "홈"(#2b9fe0 아이콘 + 라벨 #141414), 비활성 아이콘·라벨 #707070
### 반영한 레퍼런스
- https://uibowl.io/website/%EB%AF%B9%EC%8A%A4%ED%8C%A8%EB%84%90%20(mixpanel)?patterns=%EB%B6%81%EB%A7%88%ED%81%AC%C2%B7%EC%9C%84%EC%8B%9C%EB%A6%AC%EC%8A%A4%ED%8A%B8&imgId=cmuxmlodo0003js04xhbgfj5d
- https://uibowl.io/website/%EB%A6%AC%EC%8A%A4%EB%8B%9D%EB%A7%88%EC%9D%B8%EB%93%9C?patterns=%EB%9E%9C%EB%94%A9%ED%8E%98%EC%9D%B4%EC%A7%80&imgId=cmsssa2md000vl404rq691ip5
- https://uibowl.io/website/%EC%82%AC%EB%B0%A9%EB%84%B7?patterns=%EB%A9%94%EC%9D%B8&imgId=cmu4rq7ga000pjm04hw12bpue
- https://uibowl.io/website/%EB%8B%B9%EA%B7%BC%20%EB%B9%84%EC%A6%88%EB%8B%88%EC%8A%A4?patterns=%EB%8C%80%EC%8B%9C%EB%B3%B4%EB%93%9C&imgId=cmso68mja000el704vilcy6lq

## 둘러보기 화면 2
데모 학교 시약 목록. 구조는 최신 학생 시약 목록(runs/20261008-0936 화면 2)과 같다. 목록·검색·segmented-control·필터·정렬은 모두 쓸 수 있다(읽기, list_filter.roles "둘러보기 동일"). msds-bulk-banner와 등록 진입은 숨긴다. 본문 쓰기 진입이 없어 본문 잠금은 없다.
예시 상태: "전체", 이름순, 필터 적용 없음, 24종.
모바일 위→아래: nav-pill → guest-banner → segmented-control → 검색 줄(text-input + list-filter-button) → reagent-row 목록 → tab-bar(활성 "시약").
데스크톱 배치: app-sidebar("데모 학교", "시약" 현재) | 본문 = guest-banner → 페이지 머리(왼쪽 "시약" + "24종", 아래 body-sm #707070 "재고 부족 2" / 오른쪽 검색 text-input 폭 320 + list-filter-button) → 툴바(segmented-control 왼쪽) → data-table → 표 아래 가운데 페이지 번호 "1 2".
### 구성 요소
- app-sidebar: 데스크톱 전용. 둘러보기 공통 규격 — "데모 학교", sidebar-item 4개, 맨 아래 "둘러보는 중" + button-outline "로그인". 사이드바 안 guest-lock 2개
- sidebar-item: 데스크톱 전용. 4개 "홈" · "시약"(현재: #e6f4fc 채움 + #2b9fe0 아이콘, 라벨 #141414) · "기록"(guest-lock) · "QR 찾기"(guest-lock). 시약장·관리 메뉴 없음
- nav-pill: 모바일 전용. "Lab_Stock" 워드마크 + 학교명 "데모 학교". 전환·nav-account-menu 없음. 데스크톱에는 두지 않는다
- guest-banner: 둘러보기 13과 같은 위치·문구·모양(#e6f4fc, rounded 0, 정보 아이콘 #2b9fe0 + "둘러보는 중 — 가입하면 우리 학교 데이터로 시작해요" body-sm #141414 + 오른쪽 button-primary "가입하기"). 데스크톱은 본문 맨 위에서 표를 밀어 내림
- button-primary: guest-banner "가입하기"(#141414 채움, #ffffff 글자, rounded 9999, 높이 44 이상) → 화면 14. 필터 패널 "{N}종 보기"도 같은 모양. 하늘색 없음
- button-outline: app-sidebar 맨 아래 "로그인"(→ 화면 1), 필터 패널 "초기화". #ffffff, 1px #e0e0e0, 라벨 #141414, rounded 9999
- segmented-control: "전체 / 재고 부족", 한 번에 하나. 데스크톱 = 표 위 툴바 왼쪽. 예시 = "전체"
- segmented-control-active: 선택 옵션 흰 pill("전체"). 하늘색: 1px #2b9fe0 테두리(글자 #141414)
- text-input: 검색 "시약명 검색"(#f0f0f0, rounded 16, 포커스 링 2px #141414). 모바일 = 검색 줄 왼쪽(list-filter-button 자리만큼 줄어든 폭, 사이 8), 데스크톱 = 페이지 머리 오른쪽 폭 320. 하늘색: 검색 아이콘 #2b9fe0
- list-filter-button: 검색 text-input 오른쪽 button-pill-soft "필터"(#f3f3f3, 왼쪽 필터 아이콘, 라벨 #141414, rounded 9999, 높이 44 이상). 모바일 = list-filter-sheet 바텀시트, 데스크톱 = 버튼 아래 드롭다운 패널. 적용 개수 pill은 적용 없음이라 숨김. 하늘색: 필터 아이콘 #2b9fe0
- list-filter-sheet: 필터 패널(이 프레임에서는 닫힘). 최신 일반 화면 2와 같은 순서(정렬 → 보관 분류 storage-class-chip + "분류 없음" → 보관 위치 → "MSDS 없는 시약만" → "초기화" + "{N}종 보기"). "MSDS 없는 시약만"을 켜도 둘러보기에는 MSDS 일괄 찾기 띠가 나오지 않는다
- data-table: 데스크톱 전용 시약 표. 열 = 시약명(정렬, 활성 — 이름순 ↑ #2b9fe0) · 보관 분류 · 보관 위치(cabinet-number 원 + "1번 시약장 · 좌 1단", 없으면 "칸 없음" #707070) · 재고(정렬) · 상태(badge-low-stock) · 최근 입고일(정렬) · MSDS(있음 / "없음" #707070). 한 페이지 20행, 24종 → 페이지 번호 "1 2"(현재 "1" #e6f4fc 원 + #141414 숫자). 행 hover #f3f3f3, 행을 누르면 둘러보기 3(이 표 옆에 detail-drawer, 그 행 #e6f4fc). 결과 0건이면 표 머리를 남기고 표 안 ex-empty-state-card
- ex-data-table-cell: data-table 머리행(caption #707070)·셀(body-sm)
- cabinet-number: 보관 위치 값 앞 작은 원(#ffffff, 1px #e0e0e0, rounded 9999) 안 "1"(label #141414). 핑크·하늘색 글자 없음
- reagent-row: 모바일 전용. 데모 학교 시약 6줄 — 염산 · 1병, 에탄올 · 200 mL, 수산화나트륨 · 500 g, 황산구리(II) · 250 g, 아세톤 · 1 L, 질산칼륨 · 300 g(이름순으로 정렬해 보여 줌). 행 = 시약명(title) + 재고량·단위(body) + 입고일(caption #707070), #f3f3f3, rounded 16, 사이 12. 누르면 둘러보기 3. 하늘색: › 아이콘 #2b9fe0, 누른 행 #e6f4fc
- badge-low-stock: 재고 부족 2행(염산, 에탄올) "재고 부족"(#d6246a 채움, #ffffff label, rounded 9999). 모바일 = 시약명 옆, 데스크톱 = data-table 상태 열. 하늘색 없음
- ex-empty-state-card: 검색 결과 0건 "찾는 시약이 없어요". 등록 버튼 없음(시약 등록 진입 숨김). 데스크톱은 data-table 안. 하늘색: 안내 아이콘 #2b9fe0
- guest-lock: #707070 자물쇠 아이콘. 모바일 = tab-bar "QR 스캔"·"기록" tab-item(탭 안 2), 데스크톱 = app-sidebar "기록"·"QR 찾기"(사이드바 안 2). 핑크·하늘색 없음
- ex-toast: 잠긴 탭·메뉴를 누르면 "가입하면 쓸 수 있어요"(둘러보기 13과 같은 모양). 모바일 tab-bar 위, 데스크톱 오른쪽 아래. 핑크 금지
- tab-bar: 모바일 전용 하단 탭바 1개(둘러보기 공통 규격). 목록 스크롤 영역은 tab-bar 위쪽 선에서 끝난다. 데스크톱에는 두지 않는다. 하늘색: 활성 tab-item 아이콘만
- tab-item: 4개 "홈" · "시약" · "QR 스캔"(guest-lock) · "기록"(guest-lock). 활성 = "시약"(#2b9fe0 아이콘 + 라벨 #141414), 비활성 #707070
### 반영한 레퍼런스
- https://uibowl.io/website/%EC%B1%84%EB%84%90%ED%86%A1?patterns=%EB%AA%A9%EB%A1%9D%20%28PLP%29&imgId=cmudq4ko40041jx04pjl68ftt
- https://uibowl.io/website/%EB%A6%AC%EC%BA%90%EC%B9%98?patterns=%EA%B2%80%EC%83%89&imgId=cmihk0pui000pl804eqhg1j1k
- https://uibowl.io/website/%EB%AF%B9%EC%8A%A4%ED%8C%A8%EB%84%90%20(mixpanel)?patterns=%EB%A6%AC%EB%B7%B0%EC%93%B0%EA%B8%B0&imgId=cmuxmm2c10009jn04qhjm9sf4
- https://uibowl.io/website/%EB%A6%AC%EC%8A%A4%EB%8B%9D%EB%A7%88%EC%9D%B8%EB%93%9C?patterns=%EA%B2%80%EC%83%89&imgId=cmsss8y490003jv04xvtyntbp

## 둘러보기 화면 3
데모 학교 시약 상세(예시: 염산). 구조는 최신 학생 시약 상세(runs/20261008-0936 화면 3)와 같다. 정보·보관 위치·재주문 기준·사용 기록 표·MSDS 열람은 그대로 보이고(읽기), "사용 기록" 버튼만 잠근다. location-edit·threshold-edit·msds-search·"입고"는 숨긴다.
예시 상태: 염산, 재고 1병, 재주문 기준 자동 2병(사용 기록 근거) + 재고 부족, 보관 위치 1번 시약장 · 좌 1단, 보관 분류 "산", 입고일 2026-09-01, MSDS 있음. "정보" 탭.
모바일 위→아래: nav-pill → guest-banner → reagent-detail-card(시약명·재고 → reagent-location → reorder-threshold) → segmented-control "정보 / 사용 기록" → 표 → msds-entry → 하단 고정 "사용 기록"(잠금, tab-bar 위 간격 16) → tab-bar(활성 "시약").
데스크톱 배치: app-sidebar("데모 학교", "시약" 현재) | 본문 = guest-banner → 둘러보기 2 시약 목록(data-table, "염산" 행 #e6f4fc 선택) + 오른쪽 detail-drawer 480(guest-banner 아래부터, 본문을 밀어내는 배치). 드로어 = × 닫기 → "염산" + 상태 칩 → segmented-control → "항목 | 값" 행(현재 재고 · 입고일 · 보관 위치 · 재주문 기준) → msds-entry → 아래 고정 동작 줄("사용 기록" 잠금).
### 구성 요소
- app-sidebar: 데스크톱 전용. 둘러보기 공통 규격 — "데모 학교", sidebar-item 4개, 맨 아래 "둘러보는 중" + button-outline "로그인". 사이드바 안 guest-lock 2개
- sidebar-item: 데스크톱 전용. 4개 "홈" · "시약"(현재) · "기록"(guest-lock) · "QR 찾기"(guest-lock). 시약장·관리 메뉴 없음
- nav-pill: 모바일 전용. 뒤로가기(둘러보기 2) + 제목 "시약 상세" + 학교명 "데모 학교". 전환·nav-account-menu 없음. 하늘색: 뒤로가기 아이콘 #2b9fe0
- guest-banner: 둘러보기 13과 같은 위치·문구·모양. 데스크톱은 드로어가 열려도 본문 맨 위에 그대로 유지
- data-table: 데스크톱 전용. 드로어 옆 둘러보기 2 시약 표(열·정렬·페이지 번호 같음), 선택 행 "염산" #e6f4fc. 다른 행을 누르면 드로어 내용이 그 시약으로 바뀐다
- ex-data-table-cell: 데스크톱 data-table 머리행·셀, 그리고 "정보" 탭 = 시약 속성 라벨-값 표, "사용 기록" 탭 = 날짜·사용자·사용량 3열 표(데모: 오늘 · 학생 A · 20 mL, 9월 24일 · 교사 B · 30 mL). 읽기 전용. 하늘색: 가장 최근 사용 기록 행 #e6f4fc
- detail-drawer: 데스크톱 전용. 오른쪽 폭 480, guest-banner 아래부터 프레임 아래 끝까지, #ffffff, 왼쪽 1px #f0f0f0 선, 안쪽 여백 24, 딤 없음, 오른쪽 위 × 닫기(누름 영역 44 이상). 위→아래: heading-3 "염산" → 상태 칩 줄(badge-low-stock "재고 부족" + storage-class-chip "산") → segmented-control "정보 / 사용 기록" → "항목 | 값" 2열 행(사이 1px #f0f0f0): 현재 재고 "1병"(display) · 입고일 "2026-09-01" · reagent-location 행 · reorder-threshold 행 → msds-entry → 아래 고정 동작 줄(위 1px #f0f0f0): button-primary "사용 기록" 잠금 모양 + guest-lock. "입고" 버튼 없음. 하늘색: × 아이콘 #2b9fe0
- reagent-detail-card: 모바일 = 상단 요약 카드(#ffffff, 1px #f0f0f0, rounded 24, 여백 24): 시약명 "염산"(title) + badge-low-stock, 현재 재고 display "1" + "병", 입고일 caption, 아래 reagent-location 줄·reorder-threshold 줄. 데스크톱 = 카드 테두리 없이 detail-drawer "항목 | 값" 행으로 같은 내용. 하늘색 없음
- badge-low-stock: 재고 1병 < 재주문 기준 2병이라 "재고 부족"(#d6246a 채움, #ffffff label). 모바일 = 시약명 옆, 데스크톱 = 드로어 상태 칩 줄. 하늘색 없음
- storage-class-chip: 데스크톱 드로어 상태 칩 줄 보관 분류 "산"(보기 전용, #f3f3f3, label #141414, rounded 9999). 하늘색·핑크 없음
- reagent-location: 한 줄. caption "보관 위치"(#707070) + 값 cabinet-number "1" + "1번 시약장 · 좌 1단"(body #141414). 보기만 — "위치 바꾸기" 없음
- cabinet-number: reagent-location 값 앞 작은 원(#ffffff, 1px #e0e0e0, rounded 9999) 안 "1"(label #141414)
- reorder-threshold: reagent-location 아래 한 줄. caption "재주문 기준"(#707070) + 값 "2병"(body #141414) + auto-threshold-badge "자동", 줄 아래 caption(#707070) "최근 사용량으로 계산했어요". 보기만 — 연필(고치기) 없음
- auto-threshold-badge: reorder-threshold 값 옆 pill "자동"(#f3f3f3 채움, rounded 9999, label #141414). 핑크·하늘색 없음
- segmented-control: "정보 / 사용 기록" 두 탭, 예시 = "정보". 모바일 = 요약 아래, 데스크톱 = 드로어 상태 칩 아래
- segmented-control-active: 활성 탭 흰 pill. 하늘색: 활성 탭 아래 #2b9fe0 인디케이터(글자 #141414)
- msds-entry: MSDS 블록 — msds-qr-tile + button-pill-soft "MSDS 보기 ›"(→ 둘러보기 16: 모바일 MSDS 전용 화면, 데스크톱은 같은 detail-drawer가 MSDS 요약으로 바뀜). 둘러보기에서도 잠그지 않는다. 하늘색: › 아이콘 #2b9fe0
- msds-qr-tile: msds-entry 안 QR 타일(#ffffff, 1px #f0f0f0, rounded 24, QR 1:1 rounded 0 흑백, 아래 라벨 "QR로 MSDS 열기")
- button-pill-soft: msds-entry "MSDS 보기 ›"(#f3f3f3, 라벨 #141414, rounded 9999, 높이 44 이상). 하늘색: › 아이콘만
- button-primary: ① guest-banner "가입하기" → 화면 14. ② "사용 기록" — 둘러보기에서는 비활성 모양(#f0f0f0 채움, 라벨 #707070, rounded 9999, 높이 44 이상) + 라벨 앞 guest-lock, 누르면 화면 4로 가지 않고 ex-toast. 모바일 = 하단 고정 전폭, 데스크톱 = 드로어 아래 고정 줄 전폭. 하늘색 없음
- button-outline: app-sidebar 맨 아래 "로그인"(→ 화면 1). #ffffff, 1px #e0e0e0, 라벨 #141414, rounded 9999
- guest-lock: #707070 자물쇠 아이콘. "사용 기록" 버튼 라벨 앞 1개(쓰기 잠금, 탭바·사이드바 밖), 모바일 tab-bar "QR 스캔"·"기록"(탭 안 2), 데스크톱 app-sidebar "기록"·"QR 찾기"(사이드바 안 2). 핑크·하늘색 없음
- ex-toast: 잠긴 "사용 기록"·탭·메뉴를 누르면 "가입하면 쓸 수 있어요"(둘러보기 13과 같은 모양). 모바일 tab-bar 위, 데스크톱 오른쪽 아래. 핑크 금지
- tab-bar: 모바일 전용 하단 탭바 1개(둘러보기 공통 규격). "사용 기록" 버튼은 이 바 위에 쌓는다. 데스크톱에는 두지 않는다
- tab-item: 4개 "홈" · "시약" · "QR 스캔"(guest-lock) · "기록"(guest-lock). 활성 = "시약", 비활성 #707070
### 반영한 레퍼런스
- https://uibowl.io/website/%EB%A6%AC%EC%BA%90%EC%B9%98?patterns=%EB%82%B4%EC%97%AD&imgId=cmihk1yub0005li04jv0iyqbi
- https://uibowl.io/website/%EB%AF%B9%EC%8A%A4%ED%8C%A8%EB%84%90%20(mixpanel)?patterns=%EB%A6%AC%EB%B7%B0%EC%93%B0%EA%B8%B0&imgId=cmuxmm2c10009jn04qhjm9sf4
- https://uibowl.io/website/%EC%B1%84%EB%84%90%ED%86%A1?patterns=AI&imgId=cmudq46a2002ul4041tszo60n
- https://uibowl.io/website/%EC%B1%84%EB%84%90%ED%86%A1?patterns=%EB%A9%94%EC%9D%B8&imgId=cmudq3ztp000cl704tva1cnep

## 둘러보기 화면 16
데모 학교 MSDS 요약(새 둘러보기 화면). 둘러보기 3 msds-entry "MSDS 보기 ›"로 들어온다. 구조는 최신 화면 16(runs/20261008-0936)과 같고 내용만 데모 학교 시약(염산)으로 바꾼다. 읽기 전용 — 이 화면에는 원래 쓰기 동작이 없어 본문 잠금은 없다. 요약은 물질안전보건자료(한국산업안전보건공단) 내용을 서버에서 가져와 보여 준다(연결 값은 서버에서만, N2).
예시 상태(16-guest-mobile · 16-guest-desktop): 염산(데모 학교 시약, 보관 분류 산). 신호어 "위험". 그림문자 2개 — 부식성 · 자극성. 항목 요약 —
2. 유해·위험성: 금속을 부식시킬 수 있어요 / 피부에 심한 화상과 눈 손상을 일으켜요 / 호흡기를 자극할 수 있어요
4. 응급조치 요령: 눈에 들어가면 물로 15분 이상 씻고 의사의 진료를 받아요 / 피부에 묻으면 오염된 옷을 벗고 물로 씻어요 / 들이마셨으면 신선한 공기가 있는 곳으로 옮겨요
7. 취급 및 저장방법: 염기·금속과 떨어뜨려 보관해요 / 환기가 잘 되는 서늘한 곳에 둬요 / 용기를 꼭 닫아 둬요
8. 노출방지 및 개인보호구: 보안경·내화학 장갑·실험복을 착용해요 / 증기가 나면 후드 안에서 다뤄요 / 작업 뒤 손을 씻어요
모바일 위→아래: nav-pill(‹ + "MSDS · 염산" + "데모 학교") → guest-banner → 출처 줄 → msds-summary(신호어 → 그림문자 줄 → 항목 2·4·7·8 카드) → msds-original-link(맨 아래 전폭) → tab-bar(활성 "시약"). 좌우 여백 16, 블록 사이 24.
데스크톱 배치: app-sidebar("데모 학교", "시약" 현재) | 본문 = guest-banner → 둘러보기 2 시약 목록(data-table, "염산" 행 #e6f4fc 선택) + 오른쪽 detail-drawer 480(guest-banner 아래부터): "‹ 시약 상세" + × 닫기 → heading-3 "MSDS · 염산" + 출처 줄 → 항목 바로가기 줄(2 · 4 · 7 · 8) → msds-summary → 드로어 아래 고정 msds-original-link.
### 구성 요소
- app-sidebar: 데스크톱 전용. 둘러보기 공통 규격 — "데모 학교", sidebar-item 4개, 맨 아래 "둘러보는 중" + button-outline "로그인". 사이드바 안 guest-lock 2개
- sidebar-item: 데스크톱 전용. 4개 "홈" · "시약"(현재: #e6f4fc 채움 + #2b9fe0 아이콘, 라벨 #141414) · "기록"(guest-lock) · "QR 찾기"(guest-lock). 시약장·관리 메뉴 없음
- nav-pill: 모바일 전용 헤더. 뒤로가기 ‹(둘러보기 3) + heading-3 "MSDS · 염산" + 학교명 "데모 학교"(caption). 전환·nav-account-menu 없음. 그 아래(guest-banner 다음) 출처 줄 caption(#707070) "물질안전보건자료 · 한국산업안전보건공단". 하늘색: 뒤로가기 아이콘 #2b9fe0
- guest-banner: 둘러보기 13과 같은 위치·문구·모양(#e6f4fc, rounded 0, 정보 아이콘 #2b9fe0 + "둘러보는 중 — 가입하면 우리 학교 데이터로 시작해요" body-sm #141414 + 오른쪽 button-primary "가입하기"). 데스크톱은 드로어가 열려도 본문 맨 위 같은 자리. 샘플 내용임을 알리는 띠 역할
- button-primary: guest-banner "가입하기"(#141414 채움, #ffffff 글자, rounded 9999, 높이 44 이상) → 화면 14. 하늘색 없음
- data-table: 데스크톱 전용. 드로어 옆 둘러보기 2 시약 표(열·정렬·페이지 번호 같음), 선택 행 "염산" #e6f4fc
- ex-data-table-cell: 데스크톱 data-table 머리행(caption #707070)·셀(body-sm)
- detail-drawer: 데스크톱 전용. 폭 480, guest-banner 아래부터 프레임 아래 끝까지, #ffffff, 왼쪽 1px #f0f0f0 선, 여백 24, 딤 없음. 위→아래: 조용한 텍스트 동작 "‹ 시약 상세"(link #141414, → 둘러보기 3 드로어) + 오른쪽 위 × 닫기 → heading-3 "MSDS · 염산" → 출처 줄 caption(#707070) "물질안전보건자료 · 한국산업안전보건공단" → 항목 바로가기 줄(조용한 텍스트 동작 "2. 유해·위험성" · "4. 응급조치" · "7. 취급·저장" · "8. 보호구", 현재 항목 아래 #2b9fe0 밑줄, 글자 #141414) → msds-summary(드로어 안 스크롤) → 아래 고정 줄(위 1px #f0f0f0 선) msds-original-link. 하늘색: × 아이콘, 바로가기 밑줄
- msds-summary: 요약 본문. ① 신호어 pill "위험"(#141414 채움, #ffffff label, rounded 9999) — 핑크·빨강 없음 → ② 그림문자 줄: ghs-pictogram 2개 가로(사이 16) → ③ 항목 카드 4장(#ffffff, 1px #f0f0f0 테두리, rounded 24, 여백 24, 사이 12): 제목 title "2. 유해·위험성" · "4. 응급조치 요령" · "7. 취급 및 저장방법" · "8. 노출방지 및 개인보호구" + 요약 3줄(body #141414, 줄마다 글머리) + 조용한 텍스트 동작 "더 보기"(link #141414, 누름 영역 44 이상, 펼치기는 읽기 동작이라 잠그지 않음). 내용 없는 항목 = body #707070 "내용이 없어요". 모바일·데스크톱 같은 순서. 하늘색: "더 보기" 옆 ▾ 아이콘 #2b9fe0
- ghs-pictogram: GHS 그림문자 1개 = 흰 바탕(#ffffff) 마름모(정사각형 45° 회전, 한 변 56) + 표준 빨강 #ff0000 테두리(두께 4) + 검정(#141414) 그림 + 아래 caption #141414 이름. 예시 2개 "부식성"(손·금속 부식) · "자극성"(느낌표). #ff0000은 이 컴포넌트 안에서만
- msds-original-link: 맨 아래 전폭 button-outline "원문 MSDS 보기 ↗"(#ffffff, 1px #e0e0e0, 라벨 #141414, rounded 9999, 높이 44 이상) — 공단 MSDS 페이지를 새 창으로 연다(바깥 열람이라 잠그지 않음). 모바일 = 항목 카드 아래(tab-bar 위 간격 16), 데스크톱 = detail-drawer 아래 고정 줄. 하늘색: ↗ 아이콘 #2b9fe0
- button-outline: msds-original-link 버튼 모양, app-sidebar 맨 아래 "로그인"(→ 화면 1)
- guest-lock: #707070 자물쇠 아이콘. 모바일 = tab-bar "QR 스캔"·"기록" tab-item(탭 안 2), 데스크톱 = app-sidebar "기록"·"QR 찾기"(사이드바 안 2). 핑크·하늘색 없음
- ex-toast: 잠긴 탭·메뉴를 누르면 "가입하면 쓸 수 있어요"(둘러보기 13과 같은 모양). 모바일 tab-bar 위, 데스크톱 오른쪽 아래. 핑크 금지
- tab-bar: 모바일 전용 하단 탭바 1개(둘러보기 공통 규격). 데스크톱에는 두지 않는다. 하늘색: 활성 tab-item 아이콘만
- tab-item: 4개 "홈" · "시약" · "QR 스캔"(guest-lock) · "기록"(guest-lock). 활성 = "시약", 비활성 #707070
### 반영한 레퍼런스
- https://uibowl.io/website/%EB%A7%88%ED%94%8C?patterns=%EC%83%81%EC%84%B8%EC%A0%95%EB%B3%B4%20%28PDP%29&imgId=cmnnx4cuq02ikju04zkbrvx39
- https://uibowl.io/website/%EB%A6%AC%EC%BA%90%EC%B9%98?patterns=%EB%82%B4%EC%97%AD&imgId=cmihk1yub0005li04jv0iyqbi
- https://uibowl.io/website/%EB%AF%B9%EC%8A%A4%ED%8C%A8%EB%84%90%20(mixpanel)?patterns=%EB%B6%81%EB%A7%88%ED%81%AC%C2%B7%EC%9C%84%EC%8B%9C%EB%A6%AC%EC%8A%A4%ED%8A%B8&imgId=cmuxmlodo0003js04xhbgfj5d

## 역할별 노출
앱 전체(로그인 후 화면) 기준 개수. runs/20261008-0936 표를 그대로 옮겼다. 화면 1·14·15는 로그인 전 화면이라 표의 컴포넌트를 하나도 담지 않고, 둘러보기 화면은 역할이 없는 비회원 화면이라 표에 넣지 않는다(게스트는 R 규칙 대상 아님). 숫자는 바뀌지 않는다. msds-entry = 화면 3 1 + 화면 10 상세 1(학생·교사·admin 모두 2, R4).

| 컴포넌트 | 학생 | 교사 | admin |
|---|---|---|---|
| manual-upload | 0 | 2 | 2 |
| reorder-alert-card | 0 | 2 | 2 |
| vendor-link | 0 | 1 | 1 |
| vendor-register | 0 | 0 | 2 |
| msds-entry | 2 | 2 | 2 |
| stock-intake | 0 | 2 | 2 |
| reagent-register | 0 | 1 | 1 |
| user-manage | 0 | 0 | 2 |
| cabinet-edit | 0 | 3 | 3 |
| cabinet-add | 0 | 1 | 1 |
| slot-assign | 0 | 1 | 1 |
| location-edit | 0 | 1 | 1 |
| qr-print | 0 | 1 | 1 |
| threshold-edit | 0 | 1 | 1 |
| doc-upload | 0 | 1 | 1 |
| msds-search | 0 | 2 | 2 |
| msds-bulk-banner | 0 | 1 | 1 |
