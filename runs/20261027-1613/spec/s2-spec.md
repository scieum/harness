# S2 설계 — run 20261027-1613

대상 화면: 13 (홈) · 14 (회원가입) · 15 (랜딩) · 18 (관리, 모바일 전용) · 19 (개인정보 처리방침, 새 화면) + 상태 화면 14-consent + 둘러보기 18 · 학교: 샘플고등학교 (input.json) · 키스크린: 14-consent-mobile, 19-mobile, 19-desktop, 18-mobile
변경 사유: 개발 세션 요청 10 (2026-10-27, rules.json 1.31) — ① 회원가입 '개인정보 수집·이용 동의' › 펼침 = privacy-consent-detail 항목 목록(수집 목적 → 수집 항목 → 보유 기간 → 처리 위탁·국외 이전 → 동의 거부 권리 → 보호책임자) + 마지막 줄 privacy-link "개인정보 처리방침 전문 보기 ↗"(상태 화면 14-consent). 필수 체크 방식은 그대로 ② 새 화면 19 개인정보 처리방침 /privacy — 로그인 없이 열림, 로그인 전 틀(데스크톱 web-header · 모바일 nav-pill, tab-bar·app-sidebar 없음), privacy-doc · privacy-toc · privacy-table · web-footer ③ web-footer 저작권 글 뒤 footer-links "개인정보 처리방침"(굵게 600, ink) · "사용 가이드"(text-muted) — 화면 15·19 ④ guide-link "사용 가이드 ↗"(새 탭) = 데스크톱 app-sidebar 아래(13-desktop), 모바일 관리 탭 맨 아래 넷째 묶음 "도움말"(18-mobile · 18-guest-mobile). 모든 역할·둘러보기.
근거: docs/PRD.md §7(13 · 14 · 15 · 18 · 19, "회원가입 개인정보 동의 (2026-10-27)", "사용 가이드 (2026-10-27)"), docs/story-service.md, docs/design.md "Privacy consent"·"Privacy policy"·"Usage guide link"·"Manage tab"·"Pre-login desktop"(web-footer · footer-links)·"Desktop shell"·`tab-bar`·`nav-pill`·"Guest mode", harness/rules.json 1.31(privacy_consent, privacy_page, guide, footer, desktop_shell.guide_link · pre_login(screens 1·14·15·19, desktop_required 19), manage.guide, screens_required 13·14·15·18·19, variants 14.consent, frames.mobile_only_screens [18], roles R1~R8, guest.manage · hidden_components, never.N1·N2), research/s1-adopt.md.
기준 설계(틀): input.json base — 새 Figma 파일 B4bHJR70riJS4cmXPT4ETs(노드 ID 이전 파일과 같음). 13·15 = run 20261027-1224 S4-screens-v26(2015:2) — 13-mobile 2015:3, 13-desktop 2015:326, 15-mobile 2015:267, 15-desktop 2015:996(설계 = runs/20261027-1224/spec/s2-spec.md 화면 13·15). 14 = run 20261011-0813 승인 S4 페이지 593:2(설계 = runs/20261011-0813/spec/s2-spec.md 화면 14·14-error). 18 = run 20261013-1938 승인 S4-screens-v24 716:2(설계 = runs/20261013-1938/spec/s2-spec.md 화면 18·둘러보기 18). 13-mobile은 그대로, 13-desktop은 사이드바 guide-link만 더한다. 14는 terms-agree 줄을 이름 붙여 두고 펼침 상태(14-consent)를 새로 그린다. 15는 footer-links만 더한다. 18은 넷째 묶음 "도움말"만 더한다. 19는 새로 설계한다.

색·폰트·모서리·간격은 docs/design.md와 harness/rules.json을 따른다. 허용 색 밖의 값은 쓰지 않는다. 그림자는 쓰지 않는다(segmented-control-active 예외). 떠 있는 버튼(FAB)은 두지 않는다.
- 핑크 #d6246a·연핑크 #fbe9f0는 badge-low-stock, reorder-alert-card 안에서만 쓴다(이번 대상: 13 재고 부족 배지·재주문 알림, 15 조각 안 배지). privacy-consent-detail·privacy-link·privacy-doc·privacy-toc·privacy-table·footer-links·guide-link에는 핑크를 쓰지 않는다 — 정보이지 결정 신호가 아니다.
- 하늘색 #2b9fe0·옅은 하늘색 #e6f4fc는 선택·현재 위치·아이콘·체크에만 쓴다. 글자색 금지(그 위 글자 #141414). privacy-link·footer-links·privacy-toc 링크는 하늘색이 아니라 #141414(밑줄) 또는 #707070 글자다. guide-link는 현재 표시가 없으므로 #e6f4fc 채움을 쓰지 않는다.
- 모서리: 허용값 0 · 16 · 24 · 9999만. design.md "rounded.md"는 24, "rounded.sm"은 16으로 읽는다.
학교 선택은 회원가입(화면 14)에만 있다 — 시/도 → 지역(시/군/구) → 학교급 → 학교(N1-d). 화면 13·18에는 학교 선택·전환을 두지 않고 현재 학교명 "샘플고등학교"를 모바일은 nav-pill 안, 데스크톱은 app-sidebar 맨 위에 표시한다. 시약·센서·기록·홈 요약·관리 요약은 샘플고등학교 것만이다(N1). 화면 14·15·19는 로그인 전이라 현재 학교명을 표시하지 않는다(14는 학교를 고르는 중). 처리방침·동의 문구에도 특정 학교명을 쓰지 않는다. 둘러보기 18은 "데모 학교"만 쓴다.
외부 서비스 연결 값(학교 목록·AI 서류 읽기·MSDS 요약)은 서버에서만 다룬다. 어떤 화면에도 연결 값 입력 칸·외부 서비스 설정·AI 엔진 선택 UI·관련 문구를 두지 않는다(N2). 처리방침의 위탁 업체 이름(Supabase · Vercel · Google Gemini)은 "하는 일 · 위치"만 적고 연결 값·설정 이야기는 쓰지 않는다.
괄호 안 역할 표시가 없는 구성 요소는 그 화면에 들어오는 모든 역할에게 보인다. guide-link는 학생·교사·admin·둘러보기 모두 같다(rules.json guide). reorder-alert-card·sensor-alert-tile·feature-intro-popup은 교사·admin만. manage-list '입고·주문' 묶음은 교사·admin, '학교' 묶음은 admin만, '재고'·'도움말' 묶음은 모든 역할.

모바일 공통(승인본 그대로): 로그인 후 화면(13·18)의 tab-bar는 화면 아래 가장자리 y 780~844(폭 390, 높이 64, rounded 0, #ffffff + 위쪽 1px #f0f0f0 선, 그림자 없음), tab-item 4개 "홈" · "관리" · "QR 스캔" · "기록" 같은 폭. "관리" 아이콘 = 네 칸 격자. 활성 = #2b9fe0 아이콘 + #141414 라벨, 비활성 = #707070. "QR 스캔"은 회색 — 아이콘·라벨 #adadad + 아이콘 아래 caption "준비 중"(#adadad). 활성: 13 = "홈", 18 = "관리". 로그인 전 화면(14·15·19)에는 tab-bar가 없다.
- nav-pill: 로그인 후 탭 첫 화면(13·18) = 왼쪽 "Lab_Stock" 워드마크 → 오른쪽 학교명 "샘플고등학교" + nav-account-menu ▾. 로그인 전(14·15·19) = 워드마크(14는 뒤로가기 + 제목 "회원가입"), 학교명·nav-account-menu 없음.
데스크톱 공통(1440×900):
- 로그인 후(13): app-sidebar = 왼쪽 고정 열 폭 240, 높이 전체, rounded 0, #f3f3f3 채움, 오른쪽 1px #f0f0f0 선. 위→아래: "Lab_Stock" 워드마크 + 학교명 "샘플고등학교"(title #141414, 전환 없음) → sidebar-item 묶음(학생 6 / 교사 9 / admin 11, "QR 찾기" 비활성 '준비 중') → (새) 1px #f0f0f0 구분선 → guide-link "사용 가이드 ↗" 한 줄 → 맨 아래 "{이름} · {역할}"(body-sm) + nav-account-menu ▾. nav-pill·tab-bar 없음.
- 로그인 전(14·15·19): web-header = 전폭 상단 바(높이 64, rounded 0, #ffffff + 아래 1px #f0f0f0), 왼쪽 "Lab_Stock" 워드마크(→ 15), 오른쪽 button-outline "로그인" + button-primary "회원가입"(지금 페이지의 버튼은 뺀다). nav-pill·app-sidebar·tab-bar 없음.
- web-footer 공통(15·19): 위 1px #f0f0f0 선, 가운데 정렬. 데스크톱 = 한 줄 "© 2026 사이음(sci_eum). 과학의 사이, 사람을 잇다." (caption #707070) + " · " + footer-links. 모바일 = 두 줄(위 저작권 / 아래 footer-links), 열 없음.
- footer-links 공통 모양: "개인정보 처리방침"(caption 12, #141414, 굵기 600 — 쉽게 찾게) · "사용 가이드"(caption 12, #707070, 굵기 400). 사이 " · "(#707070). 밑줄·하늘색·핑크 없음. "개인정보 처리방침" → 화면 19, "사용 가이드" → 정적 가이드 새 탭.
- guide-link 공통 모양: 아이콘(물음표 원 또는 펼친 책, 20, #707070) + body #707070 "사용 가이드" + 오른쪽 ↗(#707070). 높이 44, 누르면 정적 가이드(public/guide)를 새 탭으로. ↗ = 새 탭("원문 MSDS 보기 ↗"와 같은 뜻). sidebar-item이 아니고 현재 표시(#e6f4fc 채움·#2b9fe0 아이콘)가 생기지 않는다.
예시 데이터(13·18, 승인본 그대로): 오늘 = 2026-10-27. 샘플고등학교 시약 42종, 재고 부족 3종(염산 · 50 mL, 에탄올 · 200 mL, 질산은 · 5 g), MSDS 없는 시약 4종, 시약장 2개(칸 16개 중 지정 14 · 미지정 2), 재주문 알림 3건, 사용자 학생 3 · 교사 1 · admin 1, 판매처 4곳, 센서 7개(고장 1 · 점검 필요 1). 13 기본 프레임 = 교사 "김OO · 교사", 18-mobile = admin "정OO · admin".
처리방침·동의 문구(rules.json privacy_consent.copy — 14-consent와 19가 같은 값):
- 수집 목적: "회원 확인, 학교별 시약·센서 관리, 사용·입고 기록에 이름 표시, 초대·안내 메일"
- 수집 항목: "(필수) 이름, 개인 이메일, 비밀번호(암호화 저장), 학교(NEIS 학교 정보), 역할 · 자동 수집: 접속 기록"
- 보유 기간: "탈퇴할 때까지 (탈퇴·학교 계정 삭제 시 바로 파기)"
- 처리 위탁·국외 이전: "Supabase(DB·로그인, 서울) · Vercel(호스팅, 서울) · Google Gemini(AI 서류 읽기, 국외 — 올린 파일은 읽기에만 쓰고 저장하지 않음)"
- 동의 거부 권리: "동의하지 않을 수 있어요. 다만 동의하지 않으면 가입할 수 없어요"
- 보호책임자: "{운영자 이름} · {이메일}"(시안은 자리 표시 그대로, 실제 값은 개발 쪽)

## 화면 13
홈. 로그인 후 첫 화면, 학생·교사·admin 모두. 승인본(S4-screens-v26 13-mobile 2015:3 · 13-desktop 2015:326) 그대로 — quick-action · home-summary · (교사·admin) reorder-alert-card · (교사·admin) sensor-alert-tile · 최근 사용 기록. 이번 변경은 13-desktop app-sidebar 아래에 guide-link 한 줄을 더하는 것뿐이다. 13-mobile은 바꾸지 않는다(모바일 가이드 진입은 화면 18 '도움말').
예시 상태: 교사 김OO(승인본 그대로). feature-intro-popup은 이 기본 프레임에 그리지 않는다.
모바일 활성 탭: "홈". 위→아래(그대로): nav-pill(워드마크 + 학교명 ▾) → quick-action(교사 3칸 2+1) → home-summary ① 재고 요약(맨 아래 sensor-alert-tile 줄) → reorder-alert-card → home-summary ② 시약장 요약 → 최근 사용 기록 카드 → tab-bar.
데스크톱 배치: app-sidebar("홈" 현재, 교사 9개 아래 구분선 + guide-link "사용 가이드 ↗" → 이름·역할 칸) | 본문 = 페이지 머리(heading-2 "샘플고등학교" + 날짜·전체 시약 줄 / 오른쪽 quick-action 버튼 줄) → "지금 처리할 것" 숫자 타일 줄 → 3열 위젯 격자(최근 사용 기록 data-table 2칸 폭 · 재고 부족 · 시약장 요약). 본문은 승인본 그대로.
### 구성 요소
- app-sidebar: 데스크톱 전용. 공통 규격, 워드마크 + 학교명 "샘플고등학교" + 역할별 메뉴 + (새) 구분선·guide-link + 이름·역할·nav-account-menu. 메뉴 묶음과 guide-link 사이는 남는 세로 공간(guide-link는 이름·역할 칸 바로 위에 붙는다)
- sidebar-item: 데스크톱 전용. 학생 6개 / 교사 9개 / admin 11개. 현재 = "홈", "QR 찾기" 비활성 '준비 중'. guide-link는 sidebar-item으로 세지 않는다
- guide-link: 데스크톱 전용. app-sidebar 맨 아래 이름·역할 칸 바로 위, 위에 1px #f0f0f0 구분선(사이드바 폭 전체), 그 아래 한 줄(공통 모양: 아이콘 #707070 + body #707070 "사용 가이드" + ↗, 높이 44, 좌우 여백 sidebar-item과 같음, rounded 0). 현재 표시 없음, 새 탭. 학생·교사·admin 모두 같은 자리. 13-mobile에는 두지 않는다. 핑크·하늘색 없음
- nav-pill: 모바일 전용. "Lab_Stock" 워드마크 + 현재 학교명 "샘플고등학교" + nav-account-menu ▾. ☰ 없음, 학교 선택·전환 없음
- nav-account-menu: 모바일 = 학교명 옆 ▾, 데스크톱 = app-sidebar 맨 아래. "로그아웃" 1개. 하늘색 없음
- quick-action: 역할별 작업 바로가기(승인본 그대로). 모바일 = 교사 3칸 "사용 기록 입력" · "입고"(stock-intake 진입) · "시약장 설정", admin 3칸 "입고" · "사용자 관리"(user-manage 진입) · "시약장 설정", 2+1. 학생 2칸. 데스크톱 = 페이지 머리 오른쪽 버튼 줄. 하늘색: 모바일 아이콘 #2b9fe0 + 바탕 #e6f4fc
- home-summary: 모바일 = 요약 카드 2장(재고 요약 · 시약장 요약), 데스크톱 = 숫자 타일 + 위젯 "재고 부족"·"시약장 요약"(승인본 그대로). 하늘색: 막대 지정 구간, › 아이콘
- sensor-alert-tile: 고장·점검 필요 센서 2(승인본 그대로). 무채색. 하늘색: › 아이콘만 (교사·admin만)
- badge-low-stock: 재고 요약 개수 배지 "3", reorder-alert-card 안 "재고 부족"(#d6246a 채움, #ffffff label). 하늘색 없음
- reorder-alert-card: "재주문 알림" 카드(승인본 그대로). 하늘색 없음 (교사·admin만)
- data-table: 데스크톱 전용 "최근 사용 기록" 위젯(2칸 폭, 승인본 그대로)
- reagent-row: 모바일 최근 사용 기록 카드 안 3줄(승인본 그대로). 하늘색: 누른 행 #e6f4fc
- button-pill-soft: 모바일 "더 보기 ›", reorder-alert-card "3건 ›"(교사·admin만), 데스크톱 위젯 "전체 보기 ›"
- button-outline: 데스크톱 quick-action 버튼 줄 보조 버튼
- button-primary: 데스크톱 quick-action 버튼 줄 마지막 버튼(교사·admin "입고", 학생 "사용 기록 입력"). 하늘색 없음
- feature-intro-popup: 신기능 소개 팝업 자리(이 프레임에는 그리지 않음 — 승인된 13-feature-intro 그대로). 교사·admin이 홈에 들어올 때만 (교사·admin만)
- ex-empty-state-card: 시약장 0개 / 최근 사용 기록 0건 안내(이 프레임 숨김)
- ex-toast: 권한 없는 주소 안내(13-no-access), 'QR 스캔'·'QR 찾기' "준비 중이에요". 이 프레임에는 그리지 않는다
- tab-bar: 모바일 전용 하단 탭바 1개(공통 규격). 데스크톱에는 두지 않는다. 하늘색: 활성 tab-item 아이콘 #2b9fe0만
- tab-item: "홈" · "관리" · "QR 스캔" · "기록" 4개. 활성 = "홈", "QR 스캔" 회색 '준비 중'
### 반영한 레퍼런스
- https://uibowl.io/website/%ED%94%BC%EC%B2%98%EB%A7%81?patterns=AI&imgId=cmuz1dsag000ll304xjrioyls
- https://uibowl.io/website/%ED%9E%89%EC%8A%A4%ED%95%84%EB%93%9C%20(Higgsfield)?patterns=%EB%A7%88%EC%9D%B4%ED%8E%98%EC%9D%B4%EC%A7%80&imgId=cmtrw3r7g003aib04cnmeic4y
- https://uibowl.io/website/Npay%20%EC%A6%9D%EA%B6%8C?patterns=%EA%B3%A0%EA%B0%9D%EC%84%BC%ED%84%B0%C2%B7FAQ&imgId=cmvg2hf390003jh061i12flxl

## 화면 14
회원가입. 학교(시/도 → 지역 → 학교급 → 학교)와 계정(이름·개인 이메일·비밀번호)을 받는다. 승인본(run 20261011-0813 S4 593:2, 14-mobile · 14-desktop) 그대로. 이번 변경: 약관 동의 묶음을 terms-agree로 이름 붙이고(줄 구성·필수 체크 그대로), "개인정보 수집·이용 동의 (필수)" 줄 오른쪽 끝에 펼침 아이콘 ›를 둔다. ›를 누르면 그 줄 바로 아래에 privacy-consent-detail이 펼쳐진다(상태 화면 14-consent). 이 기본 프레임은 닫힌 상태. 로그인 전이라 현재 학교명은 표시하지 않는다.
예시 상태(승인본 그대로, neis.json): 시/도 "충청북도" 선택됨 → 지역 "청주시" 선택됨 → 학교급 아직 고르지 않음 → 학교 칸 비활성 "학교급을 먼저 골라 주세요". 계정 칸 비어 있음, 약관 모두 미동의(펼침 닫힘), 진행 막대 2칸. 오류 요약 없음.
모바일(390×844) 위→아래: nav-pill → ex-auth-form-card(제목 → 학교 블록[안내 박스 → 진행 막대 → 시/도 → 지역 → 학교급 → 학교] → 계정 블록[이름 → 개인 이메일 → 비밀번호 → 비밀번호 확인] → terms-agree) → 카드 아래 로그인 줄 → 하단 고정 영역(signup-error-summary 자리 + "가입하기"). 하단 탭바 없음.
데스크톱 배치: web-header(오른쪽 button-outline "로그인"만) | 아래 반 나눔 — 왼쪽 폼 열 폭 440("1 학교 선택"[안내 박스 → 진행 막대 → 시/도 → 지역 → 학교급 → 학교] → 구분선 → "2 계정"[이름 → 개인 이메일 → 비밀번호 → 비밀번호 확인 → terms-agree → signup-error-summary 자리 → 전폭 "가입하기"] → "로그인 ›") / 오른쪽 #f3f3f3 서비스 소개 패널(feature-card 4개). 승인본 그대로.
### 구성 요소
- web-header: 데스크톱 전용. 로그인 전 공통 규격. 왼쪽 "Lab_Stock" 워드마크(→ 화면 15), 오른쪽 button-outline "로그인"(→ 화면 1)만. 하늘색 없음
- nav-pill: 모바일 전용. 뒤로가기(화면 1) + "Lab_Stock" 워드마크 + 제목 "회원가입". 학교명·nav-account-menu 없음. 하늘색: 뒤로가기 아이콘 #2b9fe0
- ex-auth-form-card: 가입 폼(승인본 그대로). 모바일 = 카드(#ffffff, 1px #f0f0f0, rounded 24, 여백 24), 데스크톱 = 왼쪽 폼 열 번호 섹션 "1 학교 선택" → "2 계정". 학교 블록 안내 박스(#e6f4fc, rounded 16) "고른 학교의 시약·기록만 보여요. 가입한 뒤에는 바꿀 수 없어요" → 4단계 진행 막대(예시 2칸 #2b9fe0) → 학교 4칸 → 계정 4칸 → terms-agree. 하늘색: 안내 박스, 진행 막대, 동의 체크 원, › 아이콘
- school-select-sido: 첫 번째 칸 "시/도"(▾ 선택 상자, #f0f0f0, rounded 16). 목록 = neis.json 시/도 17개. 예시 값 "충청북도"(선택됨). 하늘색: 선택된 칸 #e6f4fc + #2b9fe0 체크(글자 #141414)
- school-select-region: 두 번째 칸 "지역(시/군/구)". 시/도 전 비활성. 예시 값 "청주시"(선택됨). 하늘색: 선택된 칸 #e6f4fc + #2b9fe0 체크
- school-select-kind: 세 번째 칸 "학교급" — segmented-control 3칸 "초등학교 · 중학교 · 고등학교". 기본값 없음(예시 = 3칸 #707070, 흰 pill 없음). 하늘색: 선택 칸 테두리만
- school-select-school: 네 번째 칸 "학교". 학교급 전 비활성 — #f0f0f0 + "학교급을 먼저 골라 주세요"(#adadad) + ▾ #adadad. 하늘색: 목록 선택 행 #e6f4fc + 체크 #2b9fe0
- segmented-control: school-select-kind 트랙(#f3f3f3, rounded 9999)
- segmented-control-active: 학교급을 고른 뒤 흰 pill(이 프레임 없음). 하늘색: 1px #2b9fe0 테두리
- text-input: 계정 4칸 "이름" · "개인 이메일"(플레이스홀더 "name@example.com") · "비밀번호" · "비밀번호 확인". #f0f0f0, rounded 16, 포커스 링 2px #141414
- terms-agree: 약관 동의 묶음(줄 구성 그대로, 필수 체크 유지). 3줄, 줄 높이 44 이상: ① "모두 동의"(title #141414, 원형 체크) → 1px #f0f0f0 선 → ② "서비스 이용약관 동의 (필수)"(body #141414, 원형 체크) ③ "개인정보 수집·이용 동의 (필수)"(body #141414, 원형 체크) + 줄 오른쪽 끝 펼침 아이콘 ›(#707070, 누름 영역 44×44 — 아이콘만 누르면 펼침, 줄 나머지를 누르면 체크). 체크 안 함 = #ffffff + 1px #adadad 원, 체크 = #2b9fe0 채움 + 흰 체크. 이 프레임은 모두 미동의·닫힘. 하늘색: 체크 원 채움만
- privacy-consent-detail: "개인정보 수집·이용 동의" 펼침 상자 자리(이 프레임에서는 닫힘 — 그리지 않는다. 연 모양은 상태 화면 14-consent)
- signup-error-summary: 오류 요약 한 줄 자리 — "가입하기" 바로 위. 이 프레임에서는 숨김(14-error 승인본). 핑크 없음
- button-primary: 전폭 "가입하기"(#141414 채움, #ffffff 글자, rounded 9999, 높이 44 이상). 늘 누를 수 있음. 모바일 = 하단 고정, 데스크톱 = 섹션 2 맨 아래. 하늘색 없음
- button-outline: 데스크톱 web-header "로그인" → 화면 1
- button-pill-soft: 폼 아래 "이미 계정이 있으신가요?" + "로그인 ›" → 화면 1. 하늘색: › 아이콘 #2b9fe0
- feature-card: 데스크톱 전용. 오른쪽 서비스 소개 패널 4개 목록(승인본 그대로). 하늘색: 아이콘만
### 반영한 레퍼런스
- https://uibowl.io/name/%EB%AF%B8%EB%8B%88%EC%8A%A4%ED%83%81?patterns=%EC%95%BD%EA%B4%80%EB%8F%99%EC%9D%98&imgId=cmty2llwu002pl704p152k9w2

## 상태 화면 14-consent
개인정보 동의 펼친 모습(프레임 14-consent-mobile · 14-consent-desktop, 키스크린 14-consent-mobile). 로그인 전, 역할 없음. 흐름: terms-agree "개인정보 수집·이용 동의 (필수)" 줄의 ›를 누름 → 그 줄 바로 아래 privacy-consent-detail 상자가 다 펼쳐지고 › 는 ⌄로 바뀜 → 상자 마지막 줄 privacy-link를 누르면 화면 19가 새 탭으로 열림(가입 입력은 그대로 유지). ⌄를 다시 누르면 접힘. 상자 안 스크롤 없음 — 상자가 다 펼쳐지고 페이지가 스크롤된다. 하단 고정 "가입하기"는 그대로. 체크 방식은 바뀌지 않는다(펼친다고 체크되지 않음). 핑크 없음.
예시 상태(neis.json): 시/도 "충청북도" → 지역 "청주시" → 학교급 "고등학교" → 학교 "청주고등학교" 모두 선택(진행 막대 4칸), 이름 "김OO" · 개인 이메일 "kim@example.com" · 비밀번호 · 비밀번호 확인 일치. 약관: "서비스 이용약관 동의 (필수)" 체크됨, "개인정보 수집·이용 동의 (필수)" 아직 미체크 + 펼침, "모두 동의" 미체크. 화면은 약관 동의 묶음으로 스크롤된 상태(학교·계정 블록은 위로 지나가 보이지 않지만 폼 안에 그대로 있다).
모바일 위→아래(보이는 부분): nav-pill → (스크롤 위로 지나간 학교·계정 블록) → terms-agree 3줄 → 개인정보 줄 바로 아래 privacy-consent-detail 상자(항목 6개 → privacy-link) → 카드 아래 로그인 줄(화면 밖일 수 있음) → 하단 고정 영역(signup-error-summary 자리 + "가입하기"). 상자 전체(마지막 privacy-link까지)가 고정 영역 위에 보이게 스크롤 위치를 잡는다. 하단 탭바 없음.
데스크톱 배치: web-header("로그인"만) | 왼쪽 폼 열 440 = 섹션 2 아래쪽(비밀번호 확인 → terms-agree → 펼친 privacy-consent-detail(폼 열 전폭) → signup-error-summary 자리 → "가입하기")이 보이게 스크롤 / 오른쪽 #f3f3f3 서비스 소개 패널(feature-card 4개, 그대로). 하단 탭바 없음.
### 구성 요소
- web-header: 데스크톱 전용. 화면 14와 같음 — 왼쪽 워드마크, 오른쪽 button-outline "로그인"만. 하늘색 없음
- nav-pill: 모바일 전용. 화면 14와 같음 — 뒤로가기 + "Lab_Stock" + "회원가입". 학교명 없음
- ex-auth-form-card: 화면 14와 같은 가입 폼, 진행 막대 4칸 채움. 스크롤 위치만 약관 묶음. 하늘색: 안내 박스, 진행 막대, 체크 원
- school-select-sido: "시/도" 값 "충청북도"(선택됨, 스크롤 위쪽 — 프레임 안 폼 위쪽에 그대로 둔다)
- school-select-region: "지역(시/군/구)" 값 "청주시"(선택됨)
- school-select-kind: segmented-control "초등학교 · 중학교 · 고등학교", "고등학교" 선택됨(흰 pill + 1px #2b9fe0 테두리)
- school-select-school: "학교" 값 "청주고등학교"(선택됨)
- segmented-control: 학교급 트랙(#f3f3f3, rounded 9999)
- segmented-control-active: "고등학교" 흰 pill. 하늘색: 1px #2b9fe0 테두리
- text-input: 계정 4칸 채움(오류 없음)
- terms-agree: 3줄 그대로 — "모두 동의" 미체크 / "서비스 이용약관 동의 (필수)" 체크(#2b9fe0 채움 원 + 흰 체크) / "개인정보 수집·이용 동의 (필수)" 미체크(#ffffff + 1px #adadad 원) + 오른쪽 끝 아이콘 ⌄(#707070, 펼친 상태). 펼친 줄 자체의 배경은 바뀌지 않는다. 하늘색: 체크 원 채움만
- privacy-consent-detail: 펼친 상자 1개 — 개인정보 줄 바로 아래(위 간격 8), 왼쪽은 줄 글자 시작선에 맞춰 들여 붙여 어느 동의의 세부인지 보이게. #f3f3f3 채움, rounded 24, 테두리 없음, 여백 16, 안에서 스크롤 없음. 표가 아닌 항목 목록 6개(항목 사이 12): 항목마다 위 작은 제목 caption #707070 + 아래 본문 body-sm #141414(줄바꿈 허용). 순서·문구 = 공통 처리방침·동의 문구 ① "수집 목적" ② "수집 항목" ③ "보유 기간" ④ "처리 위탁·국외 이전" ⑤ "동의 거부 권리" ⑥ "보호책임자". 마지막 항목 아래(간격 16) privacy-link. 핑크·하늘색 없음
- privacy-link: 상자 마지막 줄 텍스트 링크 1개 "개인정보 처리방침 전문 보기 ↗"(link 15/600, #141414, 밑줄 #141414, 버튼 아님, 누름 영역 높이 44 이상). 누르면 화면 19를 새 탭으로(가입 입력 유지). 하늘색 아님 — ink 밑줄. 핑크 없음
- signup-error-summary: "가입하기" 바로 위 자리(이 프레임 숨김 — 아직 누르지 않음). 핑크 없음
- button-primary: 전폭 "가입하기"(#141414 채움, #ffffff 글자, rounded 9999, 높이 44 이상). 모바일 = 하단 고정 영역(#ffffff, 위 1px #f0f0f0, 여백 12·16), 데스크톱 = 섹션 2 맨 아래. 하늘색 없음
- button-outline: 데스크톱 web-header "로그인"
- button-pill-soft: 폼 아래 "로그인 ›"(모바일은 화면 밖일 수 있음). 하늘색: › 아이콘 #2b9fe0
- feature-card: 데스크톱 전용. 오른쪽 서비스 소개 패널 4개(그대로). 하늘색: 아이콘만
### 반영한 레퍼런스
- https://uibowl.io/name/%EB%AF%B8%EB%8B%88%EC%8A%A4%ED%83%81?patterns=%EC%95%BD%EA%B4%80%EB%8F%99%EC%9D%98&imgId=cmty2llwu002pl704p152k9w2
- https://uibowl.io/name/%ED%94%8C%EB%A6%AC%ED%86%A0?patterns=%EC%95%BD%EA%B4%80%EB%8F%99%EC%9D%98&imgId=cmvisjbbi0044k108s5hbqpkk
- https://uibowl.io/name/iM%EB%B1%85%ED%81%AC?patterns=%EB%A1%9C%EA%B7%B8%EC%9D%B8%C2%B7%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85&imgId=cmp0ugm9t002yky04s0u5cd5l
- https://uibowl.io/name/%EB%A7%88%EC%9D%B4%ED%98%84%EB%8C%80?patterns=%EB%A1%9C%EA%B7%B8%EC%9D%B8%C2%B7%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85&imgId=cmojm0g540005jp04b2jrd3g6
- https://uibowl.io/name/%EC%84%B8%EC%9D%B4%EB%B8%8C%20(SAVE)?patterns=%EC%95%BD%EA%B4%80%EB%8F%99%EC%9D%98&imgId=cmuo3ak1j004bjp04fzibrcm5

## 화면 15
랜딩. 로그인 전 첫 화면. 바탕 = run 20261027-1224 승인 S4-screens-v26 15-mobile 2015:267 · 15-desktop 2015:996 그대로(히어로 세로 가운데 포함). 이번 변경: web-footer 저작권 글 뒤에 footer-links "개인정보 처리방침" · "사용 가이드"를 더한다(PRD "랜딩 footer에서 링크"). 다른 섹션·위치·문구·프레임 높이(15-desktop 1440 × 5498)는 바꾸지 않는다. 학교명·학교 선택·tab-bar·app-sidebar 없음. 워드마크는 상단 바에만 1번.
CTA 위계(그대로): 채움 "회원가입" → 외곽선 "로그인" → 가장 약한 "둘러보기". footer-links는 그보다 더 약한 caption 링크 2개로 본문 흐름을 방해하지 않는다.
모바일(390×844) 위→아래: nav-pill(워드마크만) → landing-hero → feature-card 4장 → (새, 스크롤 끝) web-footer 두 줄(저작권 / footer-links) → 하단 고정 영역(landing-cta 버튼 2개 세로 + guest-entry). web-footer는 feature-card ④ 아래 간격 48, 고정 영역에 가려지지 않게 그 높이만큼 아래 여백을 둔 스크롤 끝 위치 — 844 첫 화면에서는 고정 영역 아래로 잘려 보이지 않아도 된다(프레임 안 노드로는 둔다). 하단 탭바 없음.
데스크톱 배치: 1440 × 5498 세로 긴 프레임 한 장(그대로), web-header | 가운데 콘텐츠 폭 1200 — 히어로 2열 → landing-tabs → 문제 공감 feature-card 3 → landing-section 4 → step-flow 5단계 → 대상 탭 → 안심 2×2 → cta-band → web-footer 한 줄(저작권 + " · " + footer-links, 가운데 정렬).
### 구성 요소
- web-header: 데스크톱 전용(그대로). 왼쪽 "Lab_Stock" 워드마크, 오른쪽 button-outline "로그인" + button-primary "회원가입". 하늘색 없음
- nav-pill: 모바일 전용(그대로). "Lab_Stock" 워드마크만. 학교명 없음
- landing-hero: 히어로 글 묶음(그대로 — 데스크톱은 product-shot 회색 패널 세로 가운데 ±8px). 워드마크 없음, 모노크롬, 학교명 없음
- product-shot: 데스크톱 전용(그대로). 핑크는 조각 안 badge-low-stock 안에서만
- shot-sidebar: 데스크톱 전용. product-shot · 대상 탭 교사 조각 안 승인 화면 사이드바 이름(app-sidebar로 세지 않음, 그대로). 조각 안 guide-link는 새로 넣지 않는다
- landing-cta: 모바일 = 하단 고정 전폭 버튼 2개 세로 "회원가입" · "로그인", 데스크톱 = 히어로 글 묶음 안 "회원가입하고 시작하기" · "로그인"(그대로)
- button-primary: landing-cta · web-header · cta-band "회원가입"(#141414 채움, #ffffff 글자, rounded 9999, 높이 44 이상, cta-band 안에서는 반전). 하늘색 없음
- button-outline: landing-cta · web-header "로그인", cta-band "둘러보기". 하늘색 없음
- guest-entry: button-pill-soft "둘러보기 ›" 1개(→ 둘러보기 13, 그대로). 하늘색: › 아이콘 #2b9fe0
- button-pill-soft: guest-entry "둘러보기 ›"
- landing-tabs: 데스크톱 전용(그대로). 활성 밑줄 2px #2b9fe0
- feature-card: 모바일 = 기능 카드 4장(그대로), 데스크톱 = 문제 공감 3장(그대로). 하늘색: 아이콘만
- badge-low-stock: 모바일 feature-card ④ 예시 배지, 데스크톱 조각 안 재고 부족 표시(그대로)
- data-table: 데스크톱 전용. product-shot 겹친 카드, landing-section 조각 안 승인 표(그대로)
- landing-section: 데스크톱 전용 4개(그대로)
- step-flow: 데스크톱 전용(그대로). #141414 반전 띠
- segmented-control: 데스크톱 전용. 대상 탭 "교사 · 학생 · 관리자"(그대로)
- segmented-control-active: "교사" 흰 pill. 하늘색: 1px #2b9fe0 테두리
- cta-band: 데스크톱 전용(그대로)
- web-footer: 페이지 맨 끝 바닥글 1개. 위 1px #f0f0f0 선, 위아래 여백 24, 가운데 정렬. 데스크톱 = 한 줄 caption #707070 "© 2026 사이음(sci_eum). 과학의 사이, 사람을 잇다." + " · " + footer-links(같은 줄). 모바일 = 두 줄(위 저작권 / 아래 footer-links, 줄 사이 4). 열 없음. 핑크·하늘색 없음
- footer-links: web-footer 안 저작권 글 바로 뒤 링크 2개(공통 모양) — "개인정보 처리방침"(caption #141414 굵기 600) → 화면 19 · "사용 가이드"(caption #707070) → 정적 가이드 새 탭. 사이 " · ". 누름 영역 높이 44(글자는 caption 그대로). 밑줄·하늘색·핑크 없음
### 반영한 레퍼런스
- https://uibowl.io/website/%EC%B9%B4%EC%B9%B4%EC%98%A4%ED%8E%98%EC%9D%B4%EC%A7%80?patterns=%EC%9D%B8%EC%A6%9D%ED%95%98%EA%B8%B0&imgId=cmtfgnm2b001xju044gyoj0mz
- https://uibowl.io/website/%EB%94%94%EB%A7%A8%EB%93%9C?patterns=%EB%A7%88%EC%9D%B4%ED%8E%98%EC%9D%B4%EC%A7%80&imgId=cmti7w8im000ykz040a1ads80
- https://uibowl.io/website/%EB%A6%AC%EB%B8%94?patterns=%EB%A1%9C%EA%B7%B8%EC%9D%B8%C2%B7%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85&imgId=cmuc27ubo000cl804kuclzweh

## 화면 18
관리(모바일 전용, 키스크린 18-mobile). 하단 탭 '관리'의 첫 화면. 승인본(S4-screens-v24 716:2 18-mobile) 그대로 — 묶음 3개(재고 · 입고·주문 · 학교) + 요약 줄 — 에 맨 아래 넷째 묶음 "도움말"을 더한다(rules.json manage.guide). "도움말" 묶음 = guide-link 한 줄 "사용 가이드"(manage-row 모양, 오른쪽 끝 › 대신 ↗). 학생·교사·admin 모두 같은 자리(학생은 재고 → 도움말, 교사는 재고 → 입고·주문 → 도움말, admin은 넷 다). 전체 삭제·기록 삭제 진입은 여기 두지 않는다(화면 2·10 머리 ⋯).
예시 상태: admin 정OO, 묶음 4개·행 8개 + guide-link 1줄 모두 보임. 요약 caption(승인본 그대로): 시약 "시약 42종 · 재고 부족 3" · 센서 "센서 7개 · 고장 1" · 시약장 "시약장 2개" · 입고 (이름만) · 실험 매뉴얼 (이름만) · 재주문 알림 "알림 3건" · 사용자 "학생 3 · 교사 1 · admin 1" · 판매처 "4곳". guide-link는 요약 없음(이름만).
모바일 활성 탭: "관리". 위→아래: nav-pill(워드마크 + 학교명 ▾) → 페이지 제목 heading-2 "관리" → manage-list(묶음 "재고" 제목 → 행 3 → 선 → "입고·주문" 제목 → 행 3 → 선 → "학교" 제목 → 행 2 → 선 → "도움말" 제목 → guide-link 1줄) → tab-bar. admin 4묶음이 tab-bar 위(y 780)까지 다 보이도록 묶음 제목 위 여백을 24 → 12로 줄인다(제목 아래 8, 행 높이 56 그대로). 넘치면 목록 안에서 스크롤하되 키스크린에서는 guide-link 줄이 tab-bar 위에 보여야 한다.
데스크톱 배치: 모바일 전용 — 데스크톱은 app-sidebar
### 구성 요소
- nav-pill: 모바일 전용. 탭 첫 화면 머리 — "Lab_Stock" 워드마크 + 현재 학교명 "샘플고등학교" + nav-account-menu ▾. ☰·manage-back 없음. 학교 선택·전환 없음
- nav-account-menu: 학교명 옆 ▾. "로그아웃" 1개. 하늘색 없음
- manage-list: 관리 목록 1개. 페이지 제목 heading-2 #141414 "관리" 아래 묶음 4개 세로. 묶음 = 제목 caption #707070(좌우 여백 16, 위 12·아래 8) + 줄들. 묶음 사이 1px #f0f0f0 선(전폭). ① "재고" — 시약 · 센서 · 시약장(모든 역할) ② "입고·주문" — 입고 · 실험 매뉴얼 · 재주문 알림(교사·admin, 학생은 묶음째 숨김) ③ "학교" — 사용자 · 판매처(admin, 교사·학생은 묶음째 숨김) ④ (새) "도움말" — guide-link 1줄(모든 역할, 늘 맨 아래). 배경 #ffffff. 핑크·하늘색 없음
- manage-row: 행 8개(승인본 그대로). 높이 56, 전폭, rounded 0, #ffffff, 좌우 여백 16. 왼쪽 아이콘 24 #141414 → 사이 12 → 이름 title #141414 + 아래 요약 caption #707070(요약 없으면 이름만) → 오른쪽 끝 › #707070. 숫자는 무채색 글자만. 누른 행만 잠깐 #f3f3f3
- guide-link: "도움말" 묶음 안 한 줄 1개 — manage-row와 같은 모양(높이 56, 전폭, rounded 0, #ffffff, 좌우 여백 16, 아이콘 24 #141414(물음표 원 또는 펼친 책) → 사이 12 → 이름 title #141414 "사용 가이드", 요약 없음) + 오른쪽 끝 › 대신 ↗ #707070. 누르면 정적 가이드를 새 탭으로. 노드 이름은 guide-link(manage-row로 세지 않음). 누른 동안만 #f3f3f3. 모든 역할 같음. 핑크·하늘색 없음
- ex-toast: 'QR 스캔' 탭을 누르면 "준비 중이에요"(이 프레임에는 그리지 않음)
- tab-bar: 모바일 전용 하단 탭바 1개(공통 규격). 하늘색: 활성 tab-item 아이콘 #2b9fe0만
- tab-item: "홈" · "관리" · "QR 스캔" · "기록" 4개. 활성 = "관리"(격자 아이콘 #2b9fe0, 라벨 #141414), "QR 스캔" 회색 '준비 중', "홈"·"기록" #707070
### 반영한 레퍼런스
- https://uibowl.io/name/%EC%97%90%EC%9D%B4%EB%B8%94%EB%A6%AC?patterns=%EB%A7%88%EC%9D%B4%ED%8E%98%EC%9D%B4%EC%A7%80&imgId=qb6brliqfji7q5h65lsvu2r7
- https://uibowl.io/name/%ED%8E%98%EC%9D%B4%ED%9E%88%EC%96%B4?patterns=%EC%84%A4%EC%A0%95&imgId=cmnfn0a7v0003jt04b35hxklt
- https://uibowl.io/name/%ED%81%AC%EB%AA%BD?patterns=%EB%A7%88%EC%9D%B4%ED%8E%98%EC%9D%B4%EC%A7%80&imgId=cmopqffvu000fjl04q4jpxiog
- https://uibowl.io/name/Keepin?patterns=%EC%84%A4%EC%A0%95&imgId=cm0lpx4rh001ul80cz8hgnetu

## 둘러보기 화면 18
둘러보기 관리(프레임 18-guest-mobile만 — 모바일 전용 화면이라 desktop 없음). 데모 학교 읽기 전용. 승인본(716:2 18-guest-mobile) 그대로 — "재고" 묶음에 시약 · 센서 두 줄만, 시약장 행과 "입고·주문"·"학교" 묶음 숨김 — 에 "도움말" 묶음(guide-link 1줄)을 맨 아래 같은 자리에 더한다(guide는 둘러보기에도 보임, guest.hidden_components에 없음). 학교명은 "데모 학교" 1종만. 탭 '관리' 활성, QR 스캔·기록 tab-item에 guest-lock(2). 잠긴 탭을 누르면 ex-toast "가입하면 쓸 수 있어요". guide-link는 잠그지 않는다(읽기용 안내, 쓰기 동작 아님).
예시 상태: 둘러보기 사용자, 시약 "시약 24종 · 재고 부족 2", 센서 "센서 5개 · 고장 1", 도움말 "사용 가이드".
모바일 위→아래: nav-pill(워드마크 + "데모 학교") → guest-banner → 페이지 제목 heading-2 "관리" → manage-list(묶음 "재고" 제목 → 행 2 → 1px #f0f0f0 선 → 묶음 "도움말" 제목 → guide-link 1줄) → tab-bar.
### 구성 요소
- nav-pill: 모바일 전용. "Lab_Stock" 워드마크 + 학교명 "데모 학교". nav-account-menu 없음. ☰·manage-back 없음
- guest-banner: nav-pill 아래 전폭 띠 1개(#e6f4fc 채움, rounded 0, 여백 12·16): body-sm #141414 "둘러보는 중 — 가입하면 우리 학교 데이터로 시작해요" + 끝에 작은 button-primary "가입하기"(→ 화면 14). 하늘색: 띠 채움 #e6f4fc
- button-primary: guest-banner 안 "가입하기"(#141414 채움, #ffffff 글자, rounded 9999, 높이 44 이상). 하늘색 없음
- manage-list: 묶음 2개 — "재고"(시약 · 센서) + "도움말"(guide-link). 화면 18과 같은 모양, 묶음 사이 1px #f0f0f0 선. "입고·주문"·"학교" 묶음 없음
- manage-row: 2개 — 시약(시약병 아이콘 #141414 + "시약" + caption "시약 24종 · 재고 부족 2" + ›) · 센서(센서 아이콘 + "센서" + caption "센서 5개 · 고장 1" + ›). 시약장 행 숨김. 높이 56, 사각, #ffffff, 숫자 무채색
- guide-link: "도움말" 묶음 한 줄 1개 — 화면 18과 같은 모양("사용 가이드" + 오른쪽 ↗ #707070), 새 탭. 잠금 없음. 핑크·하늘색 없음
- guest-lock: tab-bar 안 2개 — "QR 스캔"·"기록" tab-item 아이콘 오른쪽 위 작은 자물쇠(#707070). 탭 밖 잠금 없음
- ex-toast: 잠긴 탭을 누르면 "가입하면 쓸 수 있어요"(이 프레임에는 그리지 않음). 핑크 없음
- tab-bar: 모바일 전용 하단 탭바 1개(공통 규격)
- tab-item: "홈" · "관리" · "QR 스캔" · "기록" 4개. 활성 = "관리", "QR 스캔"·"기록" = guest-lock(아이콘·라벨 #707070)
숨김(둘러보기 0개, rules.json guest.hidden_components): page-more-menu · reagent-wipe · record-wipe · school-name-confirm · user-manage · stock-intake · reagent-register · manual-upload · vendor-register · vendor-link · reorder-alert-card · cabinet-edit · sensor-add · sensor-doc-add · feature-intro-popup 등 — manage-row 시약장·입고·실험 매뉴얼·재주문 알림·사용자·판매처 행도 그리지 않는다.
### 반영한 레퍼런스
- https://uibowl.io/name/%EC%A0%9C%ED%8E%98%ED%86%A0?patterns=%EC%84%A4%EC%A0%95&imgId=cmulc9f7c001fl2049rgd1hj4
- https://uibowl.io/name/%EC%97%90%EC%9D%B4%EB%B8%94%EB%A6%AC?patterns=%EB%A7%88%EC%9D%B4%ED%8E%98%EC%9D%B4%EC%A7%80&imgId=qb6brliqfji7q5h65lsvu2r7

## 화면 19
개인정보 처리방침(새 화면, 주소 /privacy, 키스크린 19-mobile · 19-desktop). 로그인 없이 열린다 — 랜딩·처리방침 footer-links, 회원가입 privacy-link(새 탭)에서 들어온다. 로그인 전 틀: 데스크톱 web-header + 가운데 읽기 단(최대 720) + web-footer, 모바일 nav-pill(로그인 전) + 같은 단 + web-footer. tab-bar·app-sidebar 없음. 학교명·학교 선택 없음. 읽기 전용 문서라 입력 칸·동의 버튼 없음.
문서 내용(privacy-doc, rules.json privacy_page.doc + 공통 처리방침·동의 문구): 제목 "개인정보 처리방침" → "시행일 2026-10-27" → privacy-toc → 번호 절 7개:
1 수집 목적 — 공통 문구 "수집 목적"
2 수집 항목 — 공통 문구 "수집 항목"
3 보유·파기 — "탈퇴할 때까지 보관해요. 탈퇴하거나 학교 계정을 삭제하면 바로 파기해요."
4 처리 위탁·국외 이전 — 한 줄 "서비스 운영을 위해 아래 업체에 처리를 맡겨요." + privacy-table 3행(Supabase · DB·로그인 · 서울 / Vercel · 호스팅 · 서울 / Google Gemini · AI 서류 읽기(올린 파일은 읽기에만 쓰고 저장하지 않음) · 국외) + 표 아래 caption #707070 자리 줄 "국외 이전 세부(국가 · 이전받는 자 · 항목 · 시기)는 확정 후 적어요"(rules.json privacy_page.note — 시안은 자리만)
5 이용자 권리 — "언제든 내 개인정보의 열람·정정·삭제·처리정지를 요청할 수 있어요. 보호책임자 이메일로 요청해 주세요."
6 보호책임자 — "{운영자 이름} · {이메일}"
7 시행일 — "이 방침은 2026-10-27부터 적용해요."
모바일(390×844) 위→아래: nav-pill(워드마크만) → 읽기 단(좌우 여백 16): privacy-doc 머리(제목 heading-2 → 시행일 caption) → privacy-toc 상자 → 절 1~7(절 사이 24, 4절 안 privacy-table = 업체 카드 3장) → web-footer 두 줄(저작권 / footer-links). 하단 탭바·하단 고정 버튼 없음. 844 프레임은 첫 화면(제목 → 시행일 → 목차 → 1절 이후 일부)을 보여 주고, 나머지 절·privacy-table·web-footer는 같은 프레임 안 아래로 이어져 잘린다(노드는 순서대로 모두 둔다).
데스크톱 배치: web-header(로그인 전, 오른쪽 "로그인" + "회원가입") | 가운데 읽기 단 폭 720(x 360~1080), 위 여백 24 — privacy-doc(제목 → 시행일 → privacy-toc 상자(2열 번호 목록 4+3) → 절 1~7, 절 사이 12, 4절 privacy-table = data-table) → web-footer 한 줄(저작권 + " · " + footer-links). 1440×900 안에 web-footer까지 들어오게 간격을 맞춘다(절 본문은 대부분 한 줄, 수집 항목만 두 줄).
### 구성 요소
- web-header: 데스크톱 전용. 로그인 전 공통 규격(전폭 1440, 높이 64, rounded 0, #ffffff + 아래 1px #f0f0f0). 왼쪽 "Lab_Stock" 워드마크(→ 15), 오른쪽 button-outline "로그인" + button-primary "회원가입"(사이 8). 하늘색 없음
- nav-pill: 모바일 전용. 로그인 전 — "Lab_Stock" 워드마크만(#f3f3f3, rounded 9999, → 15). 학교명·nav-account-menu·뒤로가기 없음(새 탭으로 열리는 문서). 데스크톱에는 두지 않는다
- privacy-doc: 처리방침 본문 1개(읽기 단 전체). 머리 = 제목 heading-2 #141414 "개인정보 처리방침" → 아래 4 caption #707070 "시행일 2026-10-27" → 아래 16 privacy-toc → 아래 24 번호 절 7개. 절 = 소제목 title #141414 "1 수집 목적"(번호 포함) + 아래 4 본문 body #141414(필요하면 글머리표 짧은 줄로 끊음, 줄바꿈 허용). 절 사이 모바일 24 / 데스크톱 12. 문구는 위 "문서 내용" 그대로. 링크·강조 색 없음, 핑크·하늘색 없음
- privacy-toc: 목차 상자 1개(#f3f3f3 채움, rounded 24, 여백 16, 테두리 없음). 위 caption #707070 "목차" → 번호 붙은 조항 링크 7개 "1 수집 목적" · "2 수집 항목" · "3 보유·파기" · "4 처리 위탁·국외 이전" · "5 이용자 권리" · "6 보호책임자" · "7 시행일"(body-sm #141414, 줄 높이 20, 누름 영역 높이 44 이상 — 누르면 그 절로 이동). 모바일 = 세로 목록 한 열(줄 사이 4), 데스크톱 = 2열(왼쪽 1~4 · 오른쪽 5~7). 현재 표시 없음. 하늘색 글자 없음, 핑크 없음
- privacy-table: 4절 위탁 표 1개(소제목·안내 줄 바로 아래, 간격 8). 데스크톱 = data-table(아래). 모바일 = 업체마다 카드 1장 세로 3장(#f3f3f3, rounded 16, 여백 12·16, 카드 사이 8): 업체명 title #141414 → 하는 일 body-sm #141414 → 위치 caption #707070("서울" / "국외"), 좁은 폭에서 줄바꿈 허용. 표 아래 국외 이전 자리 줄 caption #707070. 핑크·하늘색 없음
- data-table: 데스크톱 전용. privacy-table 안 표 — ex-data-table-cell 머리행(caption #707070) "업체 · 하는 일 · 위치" + 본문 3행(body-sm #141414, 행 높이 40, 셀 안 줄바꿈 허용), rounded 16 컨테이너 + 1px #f0f0f0 테두리, 행 구분 1px #f0f0f0. 정렬·선택·hover 없음(읽기 전용)
- button-primary: 데스크톱 web-header "회원가입"(#141414 채움, #ffffff 글자, rounded 9999, 높이 44 이상). 하늘색 없음
- button-outline: 데스크톱 web-header "로그인"(#ffffff, 1px #e0e0e0, 라벨 #141414, rounded 9999, 높이 44 이상)
- web-footer: 본문 끝 뒤 바닥글 1개(공통 모양, 위 간격 48). 데스크톱 = 한 줄(저작권 + " · " + footer-links), 모바일 = 두 줄(저작권 / footer-links). 핑크·하늘색 없음
- footer-links: web-footer 안 링크 2개(공통 모양) — "개인정보 처리방침"(caption #141414 굵기 600, 지금 페이지라 누르면 맨 위로) · "사용 가이드"(caption #707070, 새 탭). 밑줄·하늘색·핑크 없음
### 반영한 레퍼런스
- https://uibowl.io/name/%EB%82%98%EB%A7%8C%EC%9D%98%EB%8B%A5%ED%84%B0?patterns=%EC%95%BD%EA%B4%80%EB%8F%99%EC%9D%98&imgId=cm74d146z006dii0conp0ldug
- https://uibowl.io/name/%EA%B5%AC%EA%B8%80%20%EC%A0%9C%EB%AF%B8%EB%82%98%EC%9D%B4%20(Google%20Gemini)?patterns=%EA%B3%B5%EC%A7%80%EC%82%AC%ED%95%AD&imgId=cmto3us98001ol4044rol8igk
- https://uibowl.io/name/%EB%B9%BC%EA%B8%B0?patterns=%EA%B3%B5%EC%A7%80%EC%82%AC%ED%95%AD&imgId=cmsu3827y000gji04vsqgeimy
- https://uibowl.io/name/%EB%B0%B0%EB%8B%AC%EC%9D%98%EB%AF%BC%EC%A1%B1?patterns=%EA%B3%B5%EC%A7%80%EC%82%AC%ED%95%AD&imgId=cmni7hqmb0015jg04xstayb73
- https://uibowl.io/website/%EB%A6%AC%EB%94%94?patterns=%EA%B3%A0%EA%B0%9D%EC%84%BC%ED%84%B0%C2%B7FAQ&imgId=cmuq7edsw0017kz04purwnq87

## 역할별 노출
앱 전체(로그인 후 화면) 기준 개수. 직전 승인본 runs/20261027-1224 표를 그대로 옮겼다. 같은 화면의 상태 화면·모바일·데스크톱에 다시 나오는 같은 컴포넌트는 그 화면 1개로 센다.
이번 변경은 역할 개수를 바꾸지 않는다:
- guide-link(13-desktop 사이드바 · 18 도움말)는 학생·교사·admin·둘러보기 모두 같고 rules.json roles 대상이 아니어서 표에 넣지 않는다. 화면 18 "도움말" 묶음도 모든 역할에 보인다.
- terms-agree · privacy-consent-detail · privacy-link(화면 14) · privacy-doc · privacy-toc · privacy-table(화면 19) · web-footer · footer-links(화면 15·19)는 로그인 전 화면이라 역할 개수에 넣지 않는다.
- 둘러보기(18-guest)는 R 규칙 대상이 아니어서 표에 넣지 않는다.
- 화면 18의 관리 행(입고·사용자·판매처·재주문 알림·실험 매뉴얼)은 화면 이동 링크이고 stock-intake·user-manage·vendor-register·reorder-alert-card·manual-upload 컴포넌트가 아니다 — 개수 변화 없음. page-more-menu·reagent-wipe·record-wipe는 admin만(학생 R5·교사 R8 = 0) 그대로이며 화면 18에는 두지 않는다.
msds-entry = 화면 3 1 + 화면 10 상세 1(학생·교사·admin 모두 2, R4). 나머지 행은 runs/20261027-1224 값 그대로.

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
| doc-upload | 0 | 2 | 2 |
| msds-search | 0 | 2 | 2 |
| msds-bulk-banner | 0 | 1 | 1 |
| reagent-more-menu | 0 | 1 | 1 |
| reagent-delete | 0 | 1 | 1 |
| list-select-toggle | 0 | 2 | 2 |
| select-checkbox | 0 | 2 | 2 |
| bulk-action-bar | 0 | 2 | 2 |
| sensor-add | 0 | 1 | 1 |
| sensor-edit | 0 | 1 | 1 |
| sensor-delete | 0 | 1 | 1 |
| sensor-alert-tile | 0 | 1 | 1 |
| sensor-doc-add | 0 | 1 | 1 |
| invite-more-menu | 0 | 0 | 1 |
| invite-cancel | 0 | 0 | 1 |
| page-more-menu | 0 | 0 | 2 |
| reagent-wipe | 0 | 0 | 1 |
| record-wipe | 0 | 0 | 1 |
| feature-intro-popup | 0 | 1 | 1 |
| feature-intro-dismiss | 0 | 1 | 1 |
