# S2 설계 — run 20261029-1556

대상 화면: 13 (홈) · 14 (회원가입) · 18 (관리, 모바일 전용) · 20 (게시판, 새 화면) + 상태 화면 14-consent · 20-detail · 20-new · 20-empty · 20-student · 학교: 샘플고등학교 (input.json) · 키스크린: 20-mobile, 20-detail-desktop, 14-consent-mobile
변경 사유: 개발 세션 요청 11 (2026-10-29, rules.json 1.32) — ① 새 화면 20 게시판 /board · /board/{id} · /board/new — 로그인한 모든 사용자(학생 포함), 전체 학교 공용(N1 예외, 글쓴이 = 학교명 + "선생님"). board-tabs FAQ · 오류 문의 · 개선 제안, faq-item, board-post-row · board-status-badge(접수 / 답변 완료, 무채색), board-write(교사·admin만), board-detail · board-answer "운영자 답변", board-post-menu(본인, 답변 뒤 수정 불가), board-form · board-privacy-note. 상태 20-detail · 20-new · 20-empty · 20-student ② 진입 board-link "게시판" = 13-desktop(그리고 20-desktop) 사이드바 guide-link 바로 위, 18-mobile "도움말" 묶음 guide-link 위 ③ 화면 14 약관 셋째 필수 줄 age-confirm "만 14세 이상입니다 (필수)"("모두 동의"에 포함, › 펼침 한 줄), 개인정보 동의 거부 문구 "동의하지 않을 수 있지만, 동의하지 않으면 가입할 수 없어요", 학교 목록 고등학교에 시·도 온라인학교(neis.json "충북온라인학교").
근거: docs/PRD.md §7(13 · 14 · 18 · 20, "회원가입 만 14세 확인 (2026-10-29)", "온라인학교 (2026-10-29)"), docs/story-service.md(N1 예외, "게시판 (화면 20)", "만 14세 확인 (화면 14)"), docs/design.md "Board" · "Privacy consent" · "Usage guide link" · "Manage tab" · "Desktop shell" · `tab-bar` · `nav-pill`, harness/rules.json 1.32(board, screens_required 13·14·18·20, variants 14.consent · 20.detail·new·empty·student, roles R1~R8(R5에 board-write · board-form · board-post-menu), desktop_shell.board_link · guide_link · desktop_required 13·20, manage.guide · manage.back, privacy_consent.age_confirm · copy.refuse, neis.online_schools, never.N1.board_exception · N2), runs/20261029-1556/neis.json, research/s1-adopt.md.
기준 설계(틀): input.json base — Figma 파일 B4bHJR70riJS4cmXPT4ETs, run 20261027-1613 승인 S4-screens-v27(2036:2). 13-mobile 2036:3 그대로, 13-desktop 2036:119 사이드바에 board-link만 더함. 14-mobile 2036:275 · 14-desktop 2036:395 · 14-consent-mobile 2036:565 · 14-consent-desktop 2036:716 = terms-agree에 age-confirm 줄 더함 + 동의 거부 문구만 바꿈. 18-mobile 2036:1268 = "도움말" 묶음에 board-link만 더함. 설계 = runs/20261027-1613/spec/s2-spec.md 화면 13 · 14 · 14-consent · 18. 20은 새로 설계한다 — 데스크톱 틀 = 13-desktop 사이드바(board-link 현재), 모바일 틀 = 관리 아래 화면(nav-pill → "‹ 관리", tab-bar 활성 "관리").

색·폰트·모서리·간격은 docs/design.md와 harness/rules.json을 따른다. 허용 색 밖의 값은 쓰지 않는다. 그림자는 쓰지 않는다(segmented-control-active 예외). 떠 있는 버튼(FAB)은 두지 않는다.
- 핑크 #d6246a·연핑크 #fbe9f0는 badge-low-stock, reorder-alert-card 안에서만 쓴다(이번 대상: 13 재고 부족 배지·재주문 알림만). 게시판 전체(board-*, faq-item), age-confirm, board-privacy-note에는 핑크를 쓰지 않는다 — 정보이지 결정 신호가 아니다. "접수" 상태도 무채색이다.
- 하늘색 #2b9fe0·옅은 하늘색 #e6f4fc는 선택·현재 위치·아이콘·체크에만 쓴다. 글자색 금지(그 위 글자 #141414). board-status-badge · faq-item · board-answer · board-privacy-note에는 하늘색을 쓰지 않는다. board-link는 화면 20에서만 현재 표시(#e6f4fc 채움 + #2b9fe0 아이콘).
- 모서리: 허용값 0 · 16 · 24 · 9999만. design.md "rounded.md"는 24, "rounded.sm"은 16으로 읽는다.
학교 선택은 회원가입(화면 14)에만 있다 — 시/도 → 지역(시/군/구) → 학교급 → 학교(N1-d). 화면 13 · 18 · 20에는 학교 선택·전환을 두지 않고 현재 학교명 "샘플고등학교"를 모바일은 nav-pill 안, 데스크톱은 app-sidebar 맨 위에 표시한다. 시약·센서·기록·홈 요약·관리 요약은 샘플고등학교 것만이다(N1). 화면 14는 로그인 전이라 현재 학교명을 표시하지 않는다(학교를 고르는 중).
N1 예외(화면 20만): 게시판 글은 모든 학교가 함께 본다. 글쓴이 표시는 늘 "{학교명} 선생님"(예: "충북고등학교 선생님") — 사람 이름·이메일·역할은 쓰지 않는다(admin 글도 같음). 화면 20에도 시약·재고·사용 기록은 나오지 않는다. 다른 학교 이름은 화면 20 글쓴이 줄에만 나오고 화면 13 · 18에는 쓰지 않는다.
외부 서비스 연결 값(학교 목록·AI 서류 읽기·MSDS 요약)은 서버에서만 다룬다. 어떤 화면에도 연결 값 입력 칸·외부 서비스 설정·AI 엔진 선택 UI·관련 문구를 두지 않는다(N2). 게시판 운영자는 서버 환경변수의 운영자 이메일 1명으로 정해지며 화면·DB에서 지정하지 않는다 — 운영자 지정 UI·운영자 화면(답변 입력 · FAQ 작성 · 글 숨기기)은 그리지 않는다(범위 밖).
괄호 안 역할 표시가 없는 구성 요소는 그 화면에 들어오는 모든 역할에게 보인다. board-link는 로그인한 학생·교사·admin 모두 같다(둘러보기 없음). board-write · board-form · board-post-menu는 교사·admin만(학생 R5 = 0). board-post-menu는 그중에서도 글쓴이 본인 글에서만. reorder-alert-card · sensor-alert-tile · feature-intro-popup은 교사·admin만. manage-list "입고·주문" 묶음은 교사·admin, "학교" 묶음은 admin만, "재고" · "도움말" 묶음은 모든 역할.

모바일 공통(승인본 그대로): 로그인 후 화면(13 · 18 · 20)의 tab-bar는 화면 아래 가장자리 y 780~844(폭 390, 높이 64, rounded 0, #ffffff + 위쪽 1px #f0f0f0 선, 그림자 없음), tab-item 4개 "홈" · "관리" · "QR 스캔" · "기록" 같은 폭. "관리" 아이콘 = 네 칸 격자. 활성 = #2b9fe0 아이콘 + #141414 라벨, 비활성 = #707070. "QR 스캔"은 회색 — 아이콘·라벨 #adadad + 아이콘 아래 caption "준비 중"(#adadad). 활성: 13 = "홈", 18 · 20(모든 상태) = "관리". 로그인 전 화면(14)에는 tab-bar가 없다.
- nav-pill: 로그인 후(13 · 18 · 20) = 왼쪽 "Lab_Stock" 워드마크 → 오른쪽 학교명 "샘플고등학교" + nav-account-menu ▾. 로그인 전(14) = 뒤로가기 + 워드마크 + 제목 "회원가입", 학교명·nav-account-menu 없음.
- 20 모바일 머리(nav-pill 아래 한 줄, 높이 44): 목록(20 · 20-empty · 20-student) = 왼쪽 manage-back "‹ 관리"(link #141414), 글 보기·글쓰기(20-detail · 20-new) = 왼쪽 "‹ 게시판"(link #141414, 누르면 /board). 그 아래 페이지 제목.
데스크톱 공통(1440×900):
- 로그인 후(13 · 20): app-sidebar = 왼쪽 고정 열 폭 240, 높이 전체, rounded 0, #f3f3f3 채움, 오른쪽 1px #f0f0f0 선. 위→아래: "Lab_Stock" 워드마크 + 학교명 "샘플고등학교"(title #141414, 전환 없음) → sidebar-item 묶음(학생 6 / 교사 9 / admin 11, "QR 찾기" 비활성 "준비 중") → 남는 세로 공간 → 1px #f0f0f0 구분선(사이드바 폭 전체) → (새) board-link "게시판" → guide-link "사용 가이드 ↗" → 맨 아래 "{이름} · {역할}"(body-sm) + nav-account-menu ▾. nav-pill·tab-bar 없음.
- 로그인 전(14): web-header = 전폭 상단 바(높이 64, rounded 0, #ffffff + 아래 1px #f0f0f0), 왼쪽 "Lab_Stock" 워드마크(→ 15), 오른쪽 button-outline "로그인"만. nav-pill·app-sidebar·tab-bar 없음.
- board-link 공통 모양(데스크톱): sidebar-item과 같은 행 — 아이콘(말풍선, 20) + body "게시판", 높이 44, rounded 0, 좌우 여백 sidebar-item과 같음. 보통 = 아이콘·라벨 #141414, 채움 없음. 화면 20(모든 상태) = 현재 표시(#e6f4fc 채움 + #2b9fe0 아이콘, 라벨 #141414). 노드 이름은 board-link(sidebar-item으로 세지 않음). 누르면 /board. 핑크 없음.
- guide-link 공통 모양(승인본 그대로): 아이콘(펼친 책, 20, #707070) + body #707070 "사용 가이드" + 오른쪽 ↗(#707070). 높이 44, 새 탭. 현재 표시 없음.
예시 데이터(13 · 18, 승인본 그대로): 오늘 = 2026-10-27 기준 승인본 값 유지. 샘플고등학교 시약 42종, 재고 부족 3종(염산 · 50 mL, 에탄올 · 200 mL, 질산은 · 5 g), MSDS 없는 시약 4종, 시약장 2개, 재주문 알림 3건, 사용자 학생 3 · 교사 1 · admin 1, 판매처 4곳, 센서 7개(고장 1 · 점검 필요 1). 13 기본 프레임 = 교사 "김OO · 교사", 18-mobile = admin "정OO · admin".
게시판 예시 데이터(화면 20, 오늘 = 2026-10-29):
- FAQ(rules.json board.faq_examples 6개, 이 순서): ① "온라인학교는 회원가입에서 어디에 있나요?" — "학교급에서 '고등학교'를 고르면 시·도 온라인학교(예: 충북온라인학교)가 함께 나와요." ② "만 14세 미만 학생도 가입할 수 있나요?" — "아니요. 만 14세 미만은 보호자 동의가 필요해서 Lab_Stock에 가입할 수 없어요." ③ "우리 학교가 학교 목록에 없어요" — "학교 목록은 NEIS 학교 정보를 그대로 써요. 시/도·지역·학교급을 다시 확인해 주세요." ④ "다른 학교 선생님이 우리 학교 재고를 볼 수 있나요?" — "아니요. 시약·재고·사용 기록은 학교별로 나뉘어 있어요. 게시판 글만 모든 학교가 함께 봐요." ⑤ "재주문 알림 기준은 어떻게 정하나요?" — "시약 상세에서 직접 입력하거나, 비워 두면 최근 사용량으로 자동 계산해요." ⑥ "학생도 사용 기록을 남길 수 있나요?" — "네. 학생·교사 모두 사용 기록을 입력할 수 있어요."
- 오류 문의 글 4개(최신 순): ① "사용 기록 저장 뒤 홈 숫자가 늦게 바뀌어요" · 샘플고등학교 선생님 · 10월 28일 · 답변 완료(교사 김OO 본인 글 — 20-detail) ② "서류로 입고에서 두 장짜리 PDF가 한 장만 읽혀요" · 충북고등학교 선생님 · 10월 27일 · 접수 ③ "시약장 칸 이름이 잘려 보여요" · 청주여자고등학교 선생님 · 10월 25일 · 답변 완료 ④ "모바일에서 필터 시트가 닫히지 않아요" · 세광고등학교 선생님 · 10월 24일 · 접수
- 개선 제안 글 0개(20-empty).
- 20-detail 본문: "여러 시약을 한 번에 저장하면 홈의 재고 부족 숫자가 새로고침해야 바뀌어요. 모바일 크롬에서 봤어요." / 운영자 답변(10월 29일): "알려 주셔서 고마워요. 저장하면 홈 숫자가 바로 바뀌도록 고쳤어요. 같은 일이 또 생기면 다시 남겨 주세요."
처리방침·동의 문구(rules.json privacy_consent.copy — 14-consent):
- 수집 목적: "회원 확인, 학교별 시약·센서 관리, 사용·입고 기록에 이름 표시, 초대·안내 메일"
- 수집 항목: "(필수) 이름, 개인 이메일, 비밀번호(암호화 저장), 학교(NEIS 학교 정보), 역할 · 자동 수집: 접속 기록"
- 보유 기간: "탈퇴할 때까지 (탈퇴·학교 계정 삭제 시 바로 파기)"
- 처리 위탁·국외 이전: "Supabase(DB·로그인, 서울) · Vercel(호스팅, 서울) · Google Gemini(AI 서류 읽기, 국외 — 올린 파일은 읽기에만 쓰고 저장하지 않음)"
- 동의 거부 권리(바뀜): "동의하지 않을 수 있지만, 동의하지 않으면 가입할 수 없어요"
- 보호책임자: "{운영자 이름} · {이메일}"(시안은 자리 표시 그대로)
- 만 14세 펼침 한 줄(rules.json privacy_consent.age_confirm.detail): "만 14세 미만은 보호자 동의가 필요해서 Lab_Stock에 가입할 수 없어요."

## 화면 13
홈. 로그인 후 첫 화면, 학생·교사·admin 모두. 승인본(S4-screens-v27 13-mobile 2036:3 · 13-desktop 2036:119) 그대로 — quick-action · home-summary · (교사·admin) reorder-alert-card · (교사·admin) sensor-alert-tile · 최근 사용 기록. 이번 변경은 13-desktop app-sidebar 아래쪽, guide-link 바로 위에 board-link "게시판" 한 줄을 더하는 것뿐이다(desktop_shell.board_link · desktop_required 13). 13-mobile은 바꾸지 않는다(모바일 게시판 진입은 화면 18 "도움말").
예시 상태: 교사 김OO(승인본 그대로). feature-intro-popup은 이 기본 프레임에 그리지 않는다.
모바일 활성 탭: "홈". 위→아래(그대로): nav-pill(워드마크 + 학교명 ▾) → quick-action(교사 3칸 2+1) → home-summary ① 재고 요약(맨 아래 sensor-alert-tile 줄) → reorder-alert-card → home-summary ② 시약장 요약 → 최근 사용 기록 카드 → tab-bar.
데스크톱 배치: app-sidebar("홈" 현재, 교사 9개 → 남는 공간 → 구분선 → board-link "게시판" → guide-link "사용 가이드 ↗" → 이름·역할 칸) | 본문 = 페이지 머리(heading-2 "샘플고등학교" + 날짜·전체 시약 줄 / 오른쪽 quick-action 버튼 줄) → "지금 처리할 것" 숫자 타일 줄 → 3열 위젯 격자(최근 사용 기록 data-table 2칸 폭 · 재고 부족 · 시약장 요약). 본문은 승인본 그대로.
### 구성 요소
- app-sidebar: 데스크톱 전용. 공통 규격, 워드마크 + 학교명 "샘플고등학교" + 역할별 메뉴 + 구분선 + (새) board-link + guide-link + 이름·역할·nav-account-menu. board-link · guide-link 두 줄은 이름·역할 칸 바로 위에 붙고, 메뉴 묶음과의 사이는 남는 세로 공간
- sidebar-item: 데스크톱 전용. 학생 6개 / 교사 9개 / admin 11개. 현재 = "홈", "QR 찾기" 비활성 "준비 중". board-link · guide-link는 sidebar-item으로 세지 않는다
- board-link: 데스크톱 전용. 1px #f0f0f0 구분선 바로 아래, guide-link 바로 위 한 줄(공통 모양: 말풍선 아이콘 #141414 + body #141414 "게시판", 높이 44, rounded 0). 이 화면에서는 현재 표시 없음(채움 없음). 누르면 화면 20 /board. 학생·교사·admin 모두 같은 자리. 13-mobile에는 두지 않는다. 핑크 없음
- guide-link: 데스크톱 전용. board-link 바로 아래, 이름·역할 칸 바로 위(공통 모양, 승인본 그대로). 현재 표시 없음, 새 탭. 13-mobile에는 두지 않는다
- nav-pill: 모바일 전용. "Lab_Stock" 워드마크 + 현재 학교명 "샘플고등학교" + nav-account-menu ▾. ☰ 없음, 학교 선택·전환 없음
- nav-account-menu: 모바일 = 학교명 옆 ▾, 데스크톱 = app-sidebar 맨 아래. "로그아웃" 1개. 하늘색 없음
- quick-action: 역할별 작업 바로가기(승인본 그대로). 모바일 = 교사 3칸 "사용 기록 입력" · "입고"(stock-intake 진입) · "시약장 설정", admin 3칸 "입고" · "사용자 관리"(user-manage 진입) · "시약장 설정", 2+1. 학생 2칸. 데스크톱 = 페이지 머리 오른쪽 버튼 줄. 하늘색: 모바일 아이콘 #2b9fe0 + 바탕 #e6f4fc
- home-summary: 모바일 = 요약 카드 2장(재고 요약 · 시약장 요약), 데스크톱 = 숫자 타일 + 위젯 "재고 부족" · "시약장 요약"(승인본 그대로). 하늘색: 막대 지정 구간, › 아이콘
- sensor-alert-tile: 고장·점검 필요 센서 2(승인본 그대로). 무채색. 하늘색: › 아이콘만 (교사·admin만)
- badge-low-stock: 재고 요약 개수 배지 "3", reorder-alert-card 안 "재고 부족"(#d6246a 채움, #ffffff label). 하늘색 없음
- reorder-alert-card: "재주문 알림" 카드(승인본 그대로). 하늘색 없음 (교사·admin만)
- data-table: 데스크톱 전용 "최근 사용 기록" 위젯(2칸 폭, 승인본 그대로)
- reagent-row: 모바일 최근 사용 기록 카드 안 3줄(승인본 그대로). 하늘색: 누른 행 #e6f4fc
- button-pill-soft: 모바일 "더 보기 ›", reorder-alert-card "3건 ›"(교사·admin만), 데스크톱 위젯 "전체 보기 ›"
- button-outline: 데스크톱 quick-action 버튼 줄 보조 버튼
- button-primary: 데스크톱 quick-action 버튼 줄 마지막 버튼(교사·admin "입고", 학생 "사용 기록 입력"). 하늘색 없음
- feature-intro-popup: 신기능 소개 팝업 자리(이 프레임에는 그리지 않음 — 승인된 13-feature-intro 그대로) (교사·admin만)
- ex-empty-state-card: 시약장 0개 / 최근 사용 기록 0건 안내(이 프레임 숨김)
- ex-toast: 권한 없는 주소 안내(13-no-access), "QR 스캔" · "QR 찾기" "준비 중이에요". 이 프레임에는 그리지 않는다
- tab-bar: 모바일 전용 하단 탭바 1개(공통 규격). 데스크톱에는 두지 않는다. 하늘색: 활성 tab-item 아이콘 #2b9fe0만
- tab-item: "홈" · "관리" · "QR 스캔" · "기록" 4개. 활성 = "홈", "QR 스캔" 회색 "준비 중"
### 반영한 레퍼런스
- https://uibowl.io/website/Npay%20%EC%A6%9D%EA%B6%8C?patterns=%EA%B3%A0%EA%B0%9D%EC%84%BC%ED%84%B0%C2%B7FAQ&imgId=cmvg2hf390003jh061i12flxl
- https://uibowl.io/website/KRDS?patterns=%EB%AC%B8%EC%9D%98%ED%95%98%EA%B8%B0&imgId=cmnqqy3l80004i90485kh3whj
- https://uibowl.io/website/%EB%A0%88%EB%B7%B0%20(REVU)?patterns=%EB%82%B4%EC%97%AD&imgId=cmvepnf0c000sl606tagx4sv7

## 화면 14
회원가입. 학교(시/도 → 지역 → 학교급 → 학교)와 계정(이름·개인 이메일·비밀번호)을 받는다. 승인본(14-mobile 2036:275 · 14-desktop 2036:395) 그대로. 이번 변경: ① terms-agree 마지막(셋째 약관) 줄로 age-confirm "만 14세 이상입니다 (필수)"를 더한다 — 다른 약관 줄과 같은 체크 행 구조(왼쪽 원형 체크 + 라벨 + 오른쪽 끝 ›), "모두 동의"가 셋 다 체크, 필수 체크 방식 그대로. › 를 누르면 그 줄 바로 아래에 한 줄 설명 상자가 펼쳐지고 › 가 ⌄ 로 바뀐다(이 프레임은 닫힘) ② 학교급 "고등학교" 목록에 시·도 온라인학교가 함께 나온다(neis.json 충청북도 청주시 = "충북온라인학교" 포함 39개, 이름에 "고등학교"가 없어도 고등학교 목록). 로그인 전이라 현재 학교명은 표시하지 않는다.
예시 상태(승인본 그대로, neis.json): 시/도 "충청북도" 선택됨 → 지역 "청주시" 선택됨 → 학교급 아직 고르지 않음 → 학교 칸 비활성 "학교급을 먼저 골라 주세요". 계정 칸 비어 있음, 약관 4줄 모두 미동의(펼침 모두 닫힘), 진행 막대 2칸. 오류 요약 없음.
모바일(390×844) 위→아래: nav-pill → ex-auth-form-card(제목 → 학교 블록[안내 박스 → 진행 막대 → 시/도 → 지역 → 학교급 → 학교] → 계정 블록[이름 → 개인 이메일 → 비밀번호 → 비밀번호 확인] → terms-agree[모두 동의 → 선 → 서비스 이용약관 → 개인정보 수집·이용 › → 만 14세 이상 ›]) → 카드 아래 로그인 줄 → 하단 고정 영역(signup-error-summary 자리 + "가입하기"). 하단 탭바 없음. 약관 줄이 하나 늘어 카드가 44 길어진다(스크롤, 고정 영역은 그대로).
데스크톱 배치: web-header(오른쪽 button-outline "로그인"만) | 아래 반 나눔 — 왼쪽 폼 열 폭 440("1 학교 선택"[안내 박스 → 진행 막대 → 시/도 → 지역 → 학교급 → 학교] → 구분선 → "2 계정"[이름 → 개인 이메일 → 비밀번호 → 비밀번호 확인 → terms-agree 4줄 → signup-error-summary 자리 → 전폭 "가입하기"] → "로그인 ›") / 오른쪽 #f3f3f3 서비스 소개 패널(feature-card 4개). 승인본 그대로(약관 한 줄만 늘어남).
### 구성 요소
- web-header: 데스크톱 전용. 로그인 전 공통 규격. 왼쪽 "Lab_Stock" 워드마크(→ 화면 15), 오른쪽 button-outline "로그인"(→ 화면 1)만. 하늘색 없음
- nav-pill: 모바일 전용. 뒤로가기(화면 1) + "Lab_Stock" 워드마크 + 제목 "회원가입". 학교명·nav-account-menu 없음. 하늘색: 뒤로가기 아이콘 #2b9fe0
- ex-auth-form-card: 가입 폼(승인본 그대로). 모바일 = 카드(#ffffff, 1px #f0f0f0, rounded 24, 여백 24), 데스크톱 = 왼쪽 폼 열 번호 섹션 "1 학교 선택" → "2 계정". 학교 블록 안내 박스(#e6f4fc, rounded 16) "고른 학교의 시약·기록만 보여요. 가입한 뒤에는 바꿀 수 없어요" → 4단계 진행 막대(예시 2칸 #2b9fe0) → 학교 4칸 → 계정 4칸 → terms-agree. 하늘색: 안내 박스, 진행 막대, 동의 체크 원
- school-select-sido: 첫 번째 칸 "시/도"(▾ 선택 상자, #f0f0f0, rounded 16). 목록 = neis.json 시/도 17개. 예시 값 "충청북도"(선택됨). 하늘색: 선택된 칸 #e6f4fc + #2b9fe0 체크(글자 #141414)
- school-select-region: 두 번째 칸 "지역(시/군/구)". 시/도 전 비활성. 예시 값 "청주시"(선택됨). 하늘색: 선택된 칸 #e6f4fc + #2b9fe0 체크
- school-select-kind: 세 번째 칸 "학교급" — segmented-control 3칸 "초등학교 · 중학교 · 고등학교". 기본값 없음(예시 = 3칸 #707070, 흰 pill 없음). "고등학교"에는 시·도 온라인학교도 들어 있다. 하늘색: 선택 칸 테두리만
- school-select-school: 네 번째 칸 "학교". 학교급 전 비활성 — #f0f0f0 + "학교급을 먼저 골라 주세요"(#adadad) + ▾ #adadad. 고등학교를 고르면 목록 = neis.json school_list 39개(가나다 순, "충북온라인학교"가 "충북예술고등학교"와 "충북외국어고등학교" 사이에 같은 행 모양으로 — 따로 표시·묶음 없음). 하늘색: 목록 선택 행 #e6f4fc + 체크 #2b9fe0
- segmented-control: school-select-kind 트랙(#f3f3f3, rounded 9999)
- segmented-control-active: 학교급을 고른 뒤 흰 pill(이 프레임 없음). 하늘색: 1px #2b9fe0 테두리
- text-input: 계정 4칸 "이름" · "개인 이메일"(플레이스홀더 "name@example.com") · "비밀번호" · "비밀번호 확인". #f0f0f0, rounded 16, 포커스 링 2px #141414
- terms-agree: 약관 동의 묶음, 4줄(줄 높이 44 이상): ① "모두 동의"(title #141414, 원형 체크 — 아래 셋을 모두 체크) → 1px #f0f0f0 선 → ② "서비스 이용약관 동의 (필수)"(body #141414, 원형 체크) ③ "개인정보 수집·이용 동의 (필수)"(body #141414, 원형 체크) + 오른쪽 끝 펼침 아이콘 ›(#707070, 누름 영역 44×44) ④ age-confirm(아래). 체크 안 함 = #ffffff + 1px #adadad 원, 체크 = #2b9fe0 채움 + 흰 체크. 아이콘 ›만 누르면 펼침, 줄 나머지를 누르면 체크. 이 프레임은 모두 미동의·닫힘. 하늘색: 체크 원 채움만
- age-confirm: terms-agree 넷째 줄(셋째 약관) 1개 — 다른 약관 줄과 같은 행 구조: 왼쪽 원형 체크(같은 규격) + body #141414 "만 14세 이상입니다 (필수)" + 오른쪽 끝 ›(#707070, 누름 영역 44×44). 줄 높이 44 이상, 위 줄과 간격 같음. "모두 동의"에 포함. › 를 누르면 그 줄 바로 아래(위 간격 8) #f3f3f3 상자(rounded 24, 여백 16, 테두리 없음)에 한 줄 body-sm #141414 "만 14세 미만은 보호자 동의가 필요해서 Lab_Stock에 가입할 수 없어요." + › 가 ⌄ 로(이 프레임은 닫힘 — 상자 그리지 않음). 체크하지 않고 "가입하기" = signup-error-summary "약관에 동의해 주세요". 핑크·하늘색 글자 없음
- privacy-consent-detail: "개인정보 수집·이용 동의" 펼침 상자 자리(이 프레임에서는 닫힘 — 그리지 않는다. 연 모양은 상태 화면 14-consent)
- signup-error-summary: 오류 요약 한 줄 자리 — "가입하기" 바로 위. 이 프레임에서는 숨김(14-error 승인본). 핑크 없음
- button-primary: 전폭 "가입하기"(#141414 채움, #ffffff 글자, rounded 9999, 높이 44 이상). 늘 누를 수 있음. 모바일 = 하단 고정, 데스크톱 = 섹션 2 맨 아래. 하늘색 없음
- button-outline: 데스크톱 web-header "로그인" → 화면 1
- button-pill-soft: 폼 아래 "이미 계정이 있으신가요?" + "로그인 ›" → 화면 1. 하늘색: › 아이콘 #2b9fe0
- feature-card: 데스크톱 전용. 오른쪽 서비스 소개 패널 4개 목록(승인본 그대로). 하늘색: 아이콘만
### 반영한 레퍼런스
- https://uibowl.io/name/%EC%84%9D%EA%B0%80%EB%A8%B8%EB%8B%88?patterns=%EC%95%BD%EA%B4%80%EB%8F%99%EC%9D%98&imgId=cmvfy6yjy0039l706526nm0qq
- https://uibowl.io/name/%EC%95%B3%ED%94%8C%EB%A6%AC?patterns=%EC%95%BD%EA%B4%80%EB%8F%99%EC%9D%98&imgId=cmtpoktbe003gkz04h7vfsb8a
- https://uibowl.io/name/%EB%AF%B8%EC%86%8C?patterns=%EC%95%BD%EA%B4%80%EB%8F%99%EC%9D%98&imgId=cmqt6jy3n00mvjp04xw22obmk

## 상태 화면 14-consent
개인정보 동의 펼친 모습(프레임 14-consent-mobile · 14-consent-desktop, 키스크린 14-consent-mobile). 로그인 전, 역할 없음. 승인본(2036:565 · 2036:716) 그대로 두고 ① 개인정보 상자 "동의 거부 권리" 문구를 "동의하지 않을 수 있지만, 동의하지 않으면 가입할 수 없어요"로 바꾸고 ② 상자 아래에 age-confirm 줄(닫힘)을 더한다. 흐름(그대로): "개인정보 수집·이용 동의 (필수)" 줄의 › 를 누름 → 그 줄 바로 아래 privacy-consent-detail 상자가 다 펼쳐지고 › 는 ⌄ → 상자 마지막 줄 privacy-link를 누르면 화면 19가 새 탭으로(가입 입력 유지). 상자 안 스크롤 없음. 펼친다고 체크되지 않는다. 핑크 없음.
예시 상태(neis.json): 시/도 "충청북도" → 지역 "청주시" → 학교급 "고등학교" → 학교 "청주고등학교" 모두 선택(진행 막대 4칸), 이름 "김OO" · 개인 이메일 "kim@example.com" · 비밀번호 · 비밀번호 확인 일치. 약관: "서비스 이용약관 동의 (필수)" 체크됨, "개인정보 수집·이용 동의 (필수)" 미체크 + 펼침, age-confirm "만 14세 이상입니다 (필수)" 미체크·닫힘, "모두 동의" 미체크. 화면은 약관 동의 묶음으로 스크롤된 상태.
모바일 위→아래(보이는 부분): nav-pill → (스크롤 위로 지나간 학교·계정 블록) → terms-agree[모두 동의 → 선 → 서비스 이용약관(체크) → 개인정보 수집·이용(⌄) → privacy-consent-detail 상자(항목 6개 → privacy-link) → age-confirm 줄(›)] → 카드 아래 로그인 줄(화면 밖일 수 있음) → 하단 고정 영역(signup-error-summary 자리 + "가입하기"). 상자 전체와 그 아래 age-confirm 줄이 고정 영역 위에 보이게 스크롤 위치를 잡는다(필요하면 "모두 동의" 줄은 위로 지나가도 된다). 하단 탭바 없음.
데스크톱 배치: web-header("로그인"만) | 왼쪽 폼 열 440 = 섹션 2 아래쪽(비밀번호 확인 → terms-agree[… 개인정보 줄 → 펼친 privacy-consent-detail(폼 열 전폭) → age-confirm 줄] → signup-error-summary 자리 → "가입하기")이 보이게 스크롤 / 오른쪽 #f3f3f3 서비스 소개 패널(feature-card 4개, 그대로). 하단 탭바 없음.
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
- terms-agree: 4줄 — "모두 동의" 미체크 / "서비스 이용약관 동의 (필수)" 체크(#2b9fe0 채움 원 + 흰 체크) / "개인정보 수집·이용 동의 (필수)" 미체크(#ffffff + 1px #adadad 원) + 오른쪽 끝 ⌄(#707070, 펼친 상태) / age-confirm 미체크 + ›. 펼친 줄 배경은 바뀌지 않는다. 하늘색: 체크 원 채움만
- age-confirm: "만 14세 이상입니다 (필수)" 줄 1개 — privacy-consent-detail 상자 바로 아래(위 간격 8), 화면 14와 같은 행 구조(원형 체크 #ffffff + 1px #adadad, body #141414, 오른쪽 끝 › #707070). 닫힘 상태(한 줄 설명 상자 없음). 핑크 없음
- privacy-consent-detail: 펼친 상자 1개(승인본 그대로) — 개인정보 줄 바로 아래(위 간격 8), 줄 글자 시작선에 맞춰 들여 붙임. #f3f3f3 채움, rounded 24, 테두리 없음, 여백 16, 안에서 스크롤 없음. 항목 목록 6개(항목 사이 12): 위 작은 제목 caption #707070 + 아래 본문 body-sm #141414. 순서·문구 = 공통 처리방침·동의 문구 ① "수집 목적" ② "수집 항목" ③ "보유 기간" ④ "처리 위탁·국외 이전" ⑤ "동의 거부 권리" — (바뀜) "동의하지 않을 수 있지만, 동의하지 않으면 가입할 수 없어요" ⑥ "보호책임자". 마지막 항목 아래(간격 16) privacy-link. 핑크·하늘색 없음
- privacy-link: 상자 마지막 줄 텍스트 링크 1개 "개인정보 처리방침 전문 보기 ↗"(link 15/600, #141414, 밑줄 #141414, 누름 영역 높이 44 이상). 새 탭으로 화면 19(가입 입력 유지). 하늘색 아님. 핑크 없음
- signup-error-summary: "가입하기" 바로 위 자리(이 프레임 숨김). 핑크 없음
- button-primary: 전폭 "가입하기"(#141414 채움, #ffffff 글자, rounded 9999, 높이 44 이상). 모바일 = 하단 고정 영역(#ffffff, 위 1px #f0f0f0, 여백 12·16), 데스크톱 = 섹션 2 맨 아래. 하늘색 없음
- button-outline: 데스크톱 web-header "로그인"
- button-pill-soft: 폼 아래 "로그인 ›"(모바일은 화면 밖일 수 있음). 하늘색: › 아이콘 #2b9fe0
- feature-card: 데스크톱 전용. 오른쪽 서비스 소개 패널 4개(그대로). 하늘색: 아이콘만
### 반영한 레퍼런스
- https://uibowl.io/name/%EC%84%9D%EA%B0%80%EB%A8%B8%EB%8B%88?patterns=%EC%95%BD%EA%B4%80%EB%8F%99%EC%9D%98&imgId=cmvfy6yjy0039l706526nm0qq
- https://uibowl.io/name/%EC%95%B3%ED%94%8C%EB%A6%AC?patterns=%EC%95%BD%EA%B4%80%EB%8F%99%EC%9D%98&imgId=cmtpoktbe003gkz04h7vfsb8a
- https://uibowl.io/name/%EB%AF%B8%EC%86%8C?patterns=%EC%95%BD%EA%B4%80%EB%8F%99%EC%9D%98&imgId=cmqt6jy3n00mvjp04xw22obmk

## 화면 18
관리(모바일 전용). 하단 탭 "관리"의 첫 화면. 승인본(S4-screens-v27 18-mobile 2036:1268) 그대로 — 묶음 4개(재고 · 입고·주문 · 학교 · 도움말) + 요약 줄 — 에서 "도움말" 묶음 맨 위, guide-link 바로 위에 board-link "게시판" 한 줄을 더한다(rules.json manage.guide). board-link = manage-row 모양(아이콘 + 이름 + 요약 caption + ›). 학생·교사·admin 모두 같은 자리(둘러보기는 board-link 없음 — 이번 run 대상 아님). 전체 삭제·기록 삭제 진입은 여기 두지 않는다(화면 2 · 10 머리 ⋯).
예시 상태: admin 정OO, 묶음 4개 · 행 8개 + board-link · guide-link 모두 보임. 요약 caption(승인본 그대로): 시약 "시약 42종 · 재고 부족 3" · 센서 "센서 7개 · 고장 1" · 시약장 "시약장 2개" · 입고 (이름만) · 실험 매뉴얼 (이름만) · 재주문 알림 "알림 3건" · 사용자 "학생 3 · 교사 1 · admin 1" · 판매처 "4곳" · (새) 게시판 "답변 완료 1" · 사용 가이드 (이름만).
모바일 활성 탭: "관리". 위→아래: nav-pill(워드마크 + 학교명 ▾) → 페이지 제목 heading-2 "관리" → manage-list(묶음 "재고" 제목 → 행 3 → 선 → "입고·주문" 제목 → 행 3 → 선 → "학교" 제목 → 행 2 → 선 → "도움말" 제목 → board-link → guide-link) → tab-bar. 줄이 하나 늘어 admin 목록이 tab-bar 위(y 780)까지 다 들어가도록 묶음 제목 여백을 위 12 → 8, 아래 8 → 4로 줄인다(행 높이 56 그대로; 목표 = nav-pill y 8~56, 제목 "관리" y 64~96, 목록 y 104부터, guide-link 아래 끝 ≤ y 780). 그래도 넘치면 목록 안에서 스크롤하되 이 프레임에서는 guide-link 줄까지 tab-bar 위에 다 보이게 한다.
데스크톱 배치: 모바일 전용 — 데스크톱은 app-sidebar
### 구성 요소
- nav-pill: 모바일 전용. 탭 첫 화면 머리 — "Lab_Stock" 워드마크 + 현재 학교명 "샘플고등학교" + nav-account-menu ▾. ☰·manage-back 없음. 학교 선택·전환 없음
- nav-account-menu: 학교명 옆 ▾. "로그아웃" 1개. 하늘색 없음
- manage-list: 관리 목록 1개. 페이지 제목 heading-2 #141414 "관리" 아래 묶음 4개 세로. 묶음 = 제목 caption #707070(좌우 여백 16, 위 8 · 아래 4) + 줄들. 묶음 사이 1px #f0f0f0 선(전폭). ① "재고" — 시약 · 센서 · 시약장(모든 역할) ② "입고·주문" — 입고 · 실험 매뉴얼 · 재주문 알림(교사·admin, 학생은 묶음째 숨김) ③ "학교" — 사용자 · 판매처(admin, 교사·학생은 묶음째 숨김) ④ "도움말" — (새) board-link → guide-link(모든 역할, 늘 맨 아래). 배경 #ffffff. 핑크·하늘색 없음
- manage-row: 행 8개(승인본 그대로). 높이 56, 전폭, rounded 0, #ffffff, 좌우 여백 16. 왼쪽 아이콘 24 #141414 → 사이 12 → 이름 title #141414 + 아래 요약 caption #707070(요약 없으면 이름만) → 오른쪽 끝 › #707070. 숫자는 무채색 글자만. 누른 행만 잠깐 #f3f3f3
- board-link: "도움말" 묶음 첫 줄 1개 — manage-row와 같은 모양(높이 56, 전폭, rounded 0, #ffffff, 좌우 여백 16, 말풍선 아이콘 24 #141414 → 사이 12 → 이름 title #141414 "게시판" + 아래 요약 caption #707070 "답변 완료 1" → 오른쪽 끝 › #707070). 누르면 화면 20 /board(같은 탭, tab-bar 활성 "관리" 유지). 노드 이름은 board-link(manage-row로 세지 않음). 요약 숫자는 무채색 글자만. 학생·교사·admin 모두 같음. 핑크·하늘색 없음
- guide-link: "도움말" 묶음 둘째 줄 1개(승인본 그대로) — manage-row 모양, 이름 "사용 가이드"(요약 없음) + 오른쪽 끝 ↗ #707070, 새 탭. 노드 이름 guide-link. 핑크·하늘색 없음
- ex-toast: "QR 스캔" 탭을 누르면 "준비 중이에요"(이 프레임에는 그리지 않음)
- tab-bar: 모바일 전용 하단 탭바 1개(공통 규격). 하늘색: 활성 tab-item 아이콘 #2b9fe0만
- tab-item: "홈" · "관리" · "QR 스캔" · "기록" 4개. 활성 = "관리"(격자 아이콘 #2b9fe0, 라벨 #141414), "QR 스캔" 회색 "준비 중", "홈" · "기록" #707070
### 반영한 레퍼런스
- https://uibowl.io/name/%EC%B0%A8%EB%9E%80?patterns=%EB%A7%88%EC%9D%B4%ED%8E%98%EC%9D%B4%EC%A7%80&imgId=cmtwj2vr0000njr04c0puv2kw
- https://uibowl.io/name/%EB%B9%BC%EA%B8%B0?patterns=%EB%A7%88%EC%9D%B4%ED%8E%98%EC%9D%B4%EC%A7%80&imgId=cmsu39z4z00eajv04guutwvzj
- https://uibowl.io/name/%EB%B3%B4%EB%A7%B5?patterns=%EB%A7%88%EC%9D%B4%ED%8E%98%EC%9D%B4%EC%A7%80&imgId=cmr2zi6fs0006l104cnmb2duz

## 화면 20
게시판 목록(새 화면, 주소 /board, 키스크린 20-mobile). 로그인한 모든 사용자(학생 포함), 전체 학교 공용 — N1 예외(게시판 글만 학교를 넘어 보인다). 둘러보기 없음. 진입 = 데스크톱 사이드바 board-link · 모바일 관리 탭(18) "도움말"의 board-link. 이 기본 프레임 = 교사 김OO, board-tabs "FAQ"(기본 탭) 선택, FAQ 6개 중 ① "온라인학교는 회원가입에서 어디에 있나요?" 하나가 펼쳐진 모습. FAQ 작성은 운영자만이라 FAQ 탭에도 board-write는 페이지 머리에 그대로 있다(누르면 board-form, 분류는 오류 문의 · 개선 제안만). 다른 상태: 20-detail(글 보기) · 20-new(글쓰기) · 20-empty(개선 제안 0건) · 20-student(학생 · 오류 문의 탭).
모바일(390×844) 활성 탭: "관리". 위→아래: nav-pill(워드마크 + 학교명 "샘플고등학교" ▾) → 머리 줄 manage-back "‹ 관리" → 페이지 머리(heading-2 "게시판" 왼쪽 / 오른쪽 board-write "글쓰기" 높이 44 알약) → board-tabs(전폭, 좌우 여백 16) → faq-item 6줄(① 펼침: 질문 줄 → 답 상자, ②~⑥ 닫힘) → tab-bar. 목록이 넘치면 페이지가 스크롤되고 tab-bar는 고정. 하단 고정 버튼·FAB 없음.
데스크톱 배치: app-sidebar(교사 9개, board-link "게시판" 현재 → guide-link → 이름·역할) | 본문(x 240~1440, 여백 32) = 페이지 머리(heading-2 "게시판" 왼쪽 / 오른쪽 board-write button-primary "글쓰기") → 아래 16 board-tabs(왼쪽 정렬, 폭 360) → 아래 24 faq-item 목록(본문 전폭, ① 펼침). data-table·detail-drawer 없음(FAQ는 아코디언 목록).
### 구성 요소
- app-sidebar: 데스크톱 전용. 공통 규격 — 워드마크 + 학교명 "샘플고등학교" + 교사 메뉴 9개 + 구분선 + board-link(현재) + guide-link + "김OO · 교사" + nav-account-menu
- sidebar-item: 데스크톱 전용. 학생 6 / 교사 9 / admin 11. 이 화면에서는 현재 sidebar-item 없음(현재 = board-link). "QR 찾기" 비활성 "준비 중"
- board-link: 데스크톱 전용. 공통 모양, 현재 표시 — #e6f4fc 채움 + 말풍선 아이콘 #2b9fe0 + 라벨 #141414 "게시판"(sidebar-item 현재와 같은 방식). guide-link 바로 위. 하늘색: 채움·아이콘만
- guide-link: 데스크톱 전용. board-link 바로 아래(공통 모양, 현재 표시 없음, 새 탭)
- nav-pill: 모바일 전용. "Lab_Stock" 워드마크 + 현재 학교명 "샘플고등학교" + nav-account-menu ▾. 학교 선택·전환 없음
- nav-account-menu: 모바일 = 학교명 옆 ▾, 데스크톱 = app-sidebar 맨 아래. "로그아웃" 1개
- manage-back: 모바일 전용. nav-pill 아래 머리 줄 왼쪽 "‹ 관리"(link #141414, 누름 영역 44) → 화면 18. 데스크톱에는 두지 않는다. 하늘색 없음
- board-tabs: 분류 탭 1개 — segmented-control 3칸 "FAQ" · "오류 문의" · "개선 제안"(FAQ 맨 앞 고정, 같은 폭). 선택 = "FAQ". 모바일 = 전폭, 데스크톱 = 폭 360. 탭을 바꾸면 아래 목록만 바뀐다(주소 /board 유지). 하늘색: 선택 칸 1px #2b9fe0 테두리만(글자 #141414)
- segmented-control: board-tabs 트랙(#f3f3f3, rounded 9999), 비선택 라벨 #707070
- segmented-control-active: "FAQ" 흰 pill(#ffffff, 라벨 #141414). 하늘색: 1px #2b9fe0 테두리
- faq-item: FAQ 아코디언 줄 6개(rules.json board.faq_examples 순서·문구). 줄 = 질문 title #141414 한 줄(넘치면 줄바꿈) + 오른쪽 끝 ›(#707070, 펼치면 ⌄), 높이 56 이상, 좌우 여백 16(데스크톱 0), 줄 사이 1px #f0f0f0 선, 줄 전체가 누름 영역. 펼친 ① = 질문 바로 아래(간격 8) #f3f3f3 상자(rounded 24, 여백 16, 테두리 없음)에 답 body-sm #141414 "학교급에서 '고등학교'를 고르면 시·도 온라인학교(예: 충북온라인학교)가 함께 나와요.", 상자 아래 16 뒤 다음 줄. 글쓴이·날짜·상태 배지 없음. 핑크·하늘색 없음
- board-write: "글쓰기" 버튼 1개(button-primary 모양 — #141414 채움, #ffffff 글자, rounded 9999, 높이 44, 노드 이름 board-write). 페이지 머리 오른쪽(모바일 = heading-2 "게시판"과 같은 줄 오른쪽 작은 알약). 누르면 /board/new(20-new). 하늘색 없음 (교사·admin만 — 학생 화면에는 0)
- tab-bar: 모바일 전용 하단 탭바 1개(공통 규격). 데스크톱에는 두지 않는다
- tab-item: "홈" · "관리" · "QR 스캔" · "기록" 4개. 활성 = "관리", "QR 스캔" 회색 "준비 중"
### 반영한 레퍼런스
- https://uibowl.io/name/%EC%98%A4%EC%9D%BC%EB%82%98%EC%9A%B0?patterns=%EB%AC%B8%EC%9D%98%ED%95%98%EA%B8%B0&imgId=cmtpnvv5p001ajo04pqnetzma
- https://uibowl.io/name/%EC%A0%A0%EB%94%94?patterns=%EA%B3%A0%EA%B0%9D%EC%84%BC%ED%84%B0%C2%B7FAQ&imgId=cmradcdot0027k204q9o4qkmx
- https://uibowl.io/website/KRDS?patterns=%EB%AC%B8%EC%9D%98%ED%95%98%EA%B8%B0&imgId=cmnqqy3l80004i90485kh3whj

## 상태 화면 20-detail
글 보기(주소 /board/{id}, 프레임 20-detail-mobile · 20-detail-desktop, 키스크린 20-detail-desktop). 교사 김OO가 자기 오류 문의 글 "사용 기록 저장 뒤 홈 숫자가 늦게 바뀌어요"(답변 완료)를 연 모습. 순서 = 분류 → 제목 → 글쓴이·날짜 줄 + 상태 배지 → 본문 → 아래에 board-answer "운영자 답변" 상자. 본인 글이라 board-post-menu ⋯ 가 보이고, 이 프레임에서는 ⋯ 메뉴를 연 모습으로 그린다 — "수정" 비활성 + 이유 "답변이 달린 글은 고칠 수 없어요", "삭제"(누르면 ex-modal-card 확인, 이 프레임에는 그리지 않음). 운영자 답변 입력 칸·운영자 기능은 그리지 않는다(범위 밖).
모바일 활성 탭: "관리". 위→아래: nav-pill → 머리 줄(왼쪽 "‹ 게시판" link #141414 / 오른쪽 board-post-menu ⋯ 아이콘 버튼 44×44, 그 아래 연 메뉴) → board-detail(분류 → 제목 → 글쓴이·날짜 + 배지 → 본문) → 아래 24 board-answer → tab-bar. 다른 사람 글이면 ⋯ 없음.
데스크톱 배치: app-sidebar(교사 9개, board-link 현재) | 본문 720(x 240~960, 여백 32) = 게시판 목록 그대로(페이지 머리 "게시판" + board-write → board-tabs "오류 문의" 선택 → board-post-row 4개, 연 글 ① 행 #e6f4fc) | 오른쪽 detail-drawer 480(x 960~1440) = 머리(× 왼쪽 board-post-menu ⋯ + 연 메뉴, 오른쪽 위 ×) → board-detail → 아래 24 board-answer. 드로어를 닫으면 목록, 주소는 /board/{id}.
### 구성 요소
- app-sidebar: 데스크톱 전용. 화면 20과 같음(교사, board-link 현재)
- sidebar-item: 데스크톱 전용. 교사 9개, 현재 없음
- board-link: 데스크톱 전용. 현재 표시(#e6f4fc 채움 + #2b9fe0 아이콘). 하늘색: 채움·아이콘만
- guide-link: 데스크톱 전용. board-link 바로 아래(공통 모양)
- nav-pill: 모바일 전용. 워드마크 + "샘플고등학교" + nav-account-menu ▾
- nav-account-menu: 모바일 = 학교명 옆 ▾, 데스크톱 = app-sidebar 맨 아래. "로그아웃" 1개
- board-write: 데스크톱 전용(드로어 왼쪽 목록 페이지 머리 오른쪽, 화면 20과 같은 "글쓰기"). 모바일 글 보기 화면에는 두지 않는다 (교사·admin만)
- board-tabs: 데스크톱 전용(목록 위). segmented-control 3칸, 선택 = "오류 문의"
- segmented-control: board-tabs 트랙(#f3f3f3, rounded 9999)
- segmented-control-active: "오류 문의" 흰 pill. 하늘색: 1px #2b9fe0 테두리
- board-post-row: 데스크톱 전용(드로어 왼쪽 목록) 4개 — 오류 문의 예시 글 ①~④. 모양은 상태 화면 20-student와 같음. 연 글 ① 행 = #e6f4fc 채움(글자 #141414). 하늘색: 선택 행 채움만
- board-status-badge: 목록 행마다 1개(데스크톱) + board-detail 안 1개 "답변 완료"(#141414 채움 + #ffffff label 12, rounded 9999, 높이 24, 좌우 여백 8). "접수" = #f3f3f3 채움 + #707070 label. 핑크·하늘색 없음
- detail-drawer: 데스크톱 전용. 오른쪽 480, 높이 전체, #ffffff + 왼쪽 1px #f0f0f0, rounded 0, 여백 24. 오른쪽 위 ×(누르면 목록), 그 왼쪽 board-post-menu ⋯. 가운데 모달 아님
- board-detail: 글 1개. 위→아래: 분류 caption #707070 "오류 문의" → 아래 4 제목 heading-2 #141414 "사용 기록 저장 뒤 홈 숫자가 늦게 바뀌어요"(줄바꿈 허용) → 아래 8 한 줄 = 글쓴이·날짜 caption #707070 "샘플고등학교 선생님 · 10월 28일" + 오른쪽 board-status-badge "답변 완료" → 아래 16 1px #f0f0f0 선 → 아래 16 본문 body #141414 "여러 시약을 한 번에 저장하면 홈의 재고 부족 숫자가 새로고침해야 바뀌어요. 모바일 크롬에서 봤어요." 모바일 = 좌우 여백 16. 글쓴이에 사람 이름·이메일 없음. 핑크·하늘색 없음
- board-answer: 운영자 답변 상자 1개 — board-detail 본문 아래 24, #f3f3f3 채움, rounded 24, 테두리 없음, 여백 16. 머리 한 줄 = caption #707070 "운영자 답변" · "10월 29일" → 아래 8 본문 body-sm #141414 "알려 주셔서 고마워요. 저장하면 홈 숫자가 바로 바뀌도록 고쳤어요. 같은 일이 또 생기면 다시 남겨 주세요." 답변 입력 칸·운영자 이름 없음. 핑크·하늘색 없음
- board-post-menu: 본인 글 ⋯ 아이콘 버튼 1개(#141414 아이콘, 누름 영역 44×44) + 연 작은 메뉴(#ffffff, rounded 24, 1px #f0f0f0 테두리, 여백 8, 그림자 없음 — reagent-more-menu와 같은 모양). 항목 2개(줄 높이 44): ① "수정" 비활성 — 글자 #adadad + 아래 caption #707070 "답변이 달린 글은 고칠 수 없어요" ② "삭제" — body #141414(누르면 ex-modal-card 확인). 위치: 모바일 = 머리 줄 오른쪽, 데스크톱 = detail-drawer 머리 × 왼쪽. 핑크·하늘색 없음 (교사·admin 중 글쓴이 본인만)
- ex-modal-card: "삭제"를 누르면 여는 확인 모달 자리(이 프레임에는 그리지 않음). 확인 버튼은 검정 button-primary, 핑크 없음
- tab-bar: 모바일 전용 하단 탭바 1개(공통 규격)
- tab-item: 4개. 활성 = "관리", "QR 스캔" 회색 "준비 중"
### 반영한 레퍼런스
- https://uibowl.io/name/%EC%8F%98%EC%B9%B4?patterns=%EB%AC%B8%EC%9D%98%ED%95%98%EA%B8%B0&imgId=cmogjptrp02kpl104qg664v7v
- https://uibowl.io/name/%EC%98%A4%EC%9D%BC%EB%82%98%EC%9A%B0?patterns=%EB%AC%B8%EC%9D%98%ED%95%98%EA%B8%B0&imgId=cmtpnvv5p001ajo04pqnetzma
- https://uibowl.io/website/KRDS?patterns=%EB%AC%B8%EC%9D%98%ED%95%98%EA%B8%B0&imgId=cmnqqy3l80004i90485kh3whj

## 상태 화면 20-new
글쓰기(주소 /board/new, 프레임 20-new-mobile · 20-new-desktop). 교사 김OO가 board-write를 누른 뒤. 순서 = 분류 선택 → 제목 → board-privacy-note → 본문 → "등록". 안내 문구는 입력 칸 사이 한 줄. 예시 상태: 분류 "오류 문의" 선택, 제목 "QR 인쇄 미리보기가 비어 보여요" 입력됨, 본문 비어 있음(플레이스홀더). 등록 뒤 = 글 보기(/board/{id}, 상태 "접수"), 이 프레임에는 그리지 않는다.
모바일 활성 탭: "관리". 위→아래: nav-pill → 머리 줄 "‹ 게시판" → 페이지 제목 heading-2 "글쓰기" → board-form(분류 → 제목 → board-privacy-note → 본문 → 전폭 "등록") → tab-bar. 키보드·하단 고정 영역 없음.
데스크톱 배치: app-sidebar(교사 9개, board-link 현재) | 본문 = 가운데 폼 열 폭 640(본문 영역 x 240~1440 가운데) — 머리 줄 "‹ 게시판"(link) → heading-2 "글쓰기" → board-form("라벨 | 입력" 행이 아닌 위 라벨 · 아래 입력 세로 흐름, 항목 사이 24) → 폼 맨 아래 오른쪽 정렬 "등록". 페이지(드로어 아님 — 본문이 길어질 수 있는 입력, 주소 /board/new).
### 구성 요소
- app-sidebar: 데스크톱 전용. 화면 20과 같음(교사, board-link 현재)
- sidebar-item: 데스크톱 전용. 교사 9개, 현재 없음
- board-link: 데스크톱 전용. 현재 표시(#e6f4fc 채움 + #2b9fe0 아이콘)
- guide-link: 데스크톱 전용. board-link 바로 아래(공통 모양)
- nav-pill: 모바일 전용. 워드마크 + "샘플고등학교" + nav-account-menu ▾
- nav-account-menu: 모바일 = 학교명 옆 ▾, 데스크톱 = app-sidebar 맨 아래. "로그아웃" 1개
- board-form: 글쓰기 폼 1개 (교사·admin만). 위→아래(항목 사이 모바일 16 · 데스크톱 24, 라벨 caption #707070 위 · 입력 아래 간격 4): ① "분류" — segmented-control 2칸 "오류 문의" · "개선 제안"(FAQ 없음), 예시 "오류 문의" 선택 ② "제목" — text-input 한 줄, 값 "QR 인쇄 미리보기가 비어 보여요" ③ board-privacy-note 한 줄 ④ "본문" — text-input 여러 줄(높이 모바일 200 · 데스크톱 240, 위 정렬), 플레이스홀더 "어떤 화면에서 어떤 일이 있었는지 적어 주세요"(#adadad) ⑤ button-primary "등록". 글쓴이는 자동 "샘플고등학교 선생님"(입력 칸 없음). 핑크 없음
- segmented-control: 분류 트랙(#f3f3f3, rounded 9999), 비선택 라벨 #707070
- segmented-control-active: "오류 문의" 흰 pill. 하늘색: 1px #2b9fe0 테두리
- text-input: 제목 · 본문 2칸(#f0f0f0 채움, 테두리 없음, rounded 16, 여백 8·16). 포커스 = 2px #141414 링(이 프레임은 제목 칸 포커스 없음)
- board-privacy-note: 제목 칸과 본문 칸 사이 안내 한 줄 1개 — 정보 아이콘(원 안 i, 16, #707070) + 사이 8 + body-sm #141414 "학생 이름·연락처 같은 개인정보는 쓰지 마세요". 채움·테두리 없음. 핑크·하늘색 없음
- button-primary: board-form 맨 아래 "등록"(#141414 채움, #ffffff 글자, rounded 9999, 높이 44 이상). 모바일 = 전폭, 데스크톱 = 폼 열 오른쪽 끝(폭 120). 하늘색 없음
- tab-bar: 모바일 전용 하단 탭바 1개(공통 규격)
- tab-item: 4개. 활성 = "관리", "QR 스캔" 회색 "준비 중"
### 반영한 레퍼런스
- https://uibowl.io/name/%ED%95%B4%ED%94%BC%EB%AC%B8%EB%8D%B0%EC%9D%B4?patterns=%EB%AC%B8%EC%9D%98%ED%95%98%EA%B8%B0&imgId=cmtwleq9n0044l704bgq32c1l
- https://uibowl.io/name/%EC%98%A4%EC%9D%BC%EB%82%98%EC%9A%B0?patterns=%EB%AC%B8%EC%9D%98%ED%95%98%EA%B8%B0&imgId=cmtpnvv5p001ajo04pqnetzma

## 상태 화면 20-empty
고른 분류에 글이 0개(프레임 20-empty-mobile · 20-empty-desktop). 교사 김OO, board-tabs "개선 제안" 선택, 개선 제안 글 0개. board-tabs는 그대로 두고 그 아래 ex-empty-state-card 한 장 + board-write 진입.
모바일 활성 탭: "관리". 위→아래: nav-pill → 머리 줄 manage-back "‹ 관리" → 페이지 머리(heading-2 "게시판" / 오른쪽 board-write "글쓰기") → board-tabs("개선 제안" 선택) → 아래 24 ex-empty-state-card(카드 안 board-write) → tab-bar.
데스크톱 배치: app-sidebar(교사 9개, board-link 현재) | 본문 = 페이지 머리("게시판" + 오른쪽 board-write) → board-tabs(폭 360, "개선 제안" 선택) → 아래 24 ex-empty-state-card(본문 전폭, 가운데 정렬 내용).
### 구성 요소
- app-sidebar: 데스크톱 전용. 화면 20과 같음(교사, board-link 현재)
- sidebar-item: 데스크톱 전용. 교사 9개, 현재 없음
- board-link: 데스크톱 전용. 현재 표시(#e6f4fc 채움 + #2b9fe0 아이콘)
- guide-link: 데스크톱 전용. board-link 바로 아래(공통 모양)
- nav-pill: 모바일 전용. 워드마크 + "샘플고등학교" + nav-account-menu ▾
- nav-account-menu: 모바일 = 학교명 옆 ▾, 데스크톱 = app-sidebar 맨 아래. "로그아웃" 1개
- manage-back: 모바일 전용. "‹ 관리"(link #141414) → 화면 18
- board-tabs: segmented-control 3칸 "FAQ" · "오류 문의" · "개선 제안", 선택 = "개선 제안". 빈 상태여도 그대로 보인다
- segmented-control: board-tabs 트랙(#f3f3f3, rounded 9999)
- segmented-control-active: "개선 제안" 흰 pill. 하늘색: 1px #2b9fe0 테두리
- ex-empty-state-card: 빈 상태 카드 1장(#f3f3f3 채움, rounded 24, 여백 24, 테두리 없음, 내용 가운데 정렬). 말풍선 아이콘(32, #707070) → 아래 12 title #141414 "아직 올라온 글이 없어요" → 아래 4 body-sm #707070 "Lab_Stock을 쓰며 바라는 점을 남겨 주세요" → 아래 16 board-write. 핑크·하늘색 없음
- board-write: "글쓰기" 2곳 — 페이지 머리 오른쪽(화면 20과 같음) + ex-empty-state-card 안(가운데, 같은 button-primary 모양, 높이 44). 둘 다 /board/new (교사·admin만 — 학생 빈 상태는 글만)
- tab-bar: 모바일 전용 하단 탭바 1개(공통 규격)
- tab-item: 4개. 활성 = "관리", "QR 스캔" 회색 "준비 중"
### 반영한 레퍼런스
- https://uibowl.io/name/%EB%9D%BC%EC%9D%B4%ED%94%84%EC%BA%90%EC%B9%98?patterns=%EB%AC%B8%EC%9D%98%ED%95%98%EA%B8%B0&imgId=cmqzb48yx003yju04rnwhv1yb
- https://uibowl.io/name/%EC%98%A4%EC%9D%BC%EB%82%98%EC%9A%B0?patterns=%EB%AC%B8%EC%9D%98%ED%95%98%EA%B8%B0&imgId=cmtpnvv5p001ajo04pqnetzma

## 상태 화면 20-student
학생이 본 게시판(프레임 20-student-mobile · 20-student-desktop). 학생 "이OO · 학생", board-tabs "오류 문의" 선택, 오류 문의 글 4개(다른 학교 글 포함 — N1 예외). 학생은 읽기만: board-write · board-form · board-post-menu = 0(R5). 행을 누르면 글 보기(⋯ 없음, 답변은 보임).
모바일 활성 탭: "관리". 위→아래: nav-pill → 머리 줄 manage-back "‹ 관리" → 페이지 머리(heading-2 "게시판"만, 오른쪽 버튼 없음) → board-tabs("오류 문의" 선택) → board-post-row 4개 → tab-bar.
데스크톱 배치: app-sidebar(학생 6개 "홈 · 시약 · 센서 · 기록 · 시약장 · QR 찾기", board-link 현재 → guide-link → "이OO · 학생") | 본문 = 페이지 머리(heading-2 "게시판"만) → board-tabs(폭 360) → 아래 16 board-post-row 4개 목록(본문 전폭, rounded 16 컨테이너 + 1px #f0f0f0 테두리, 행 구분 1px #f0f0f0). data-table 열 머리 없음(행 목록).
### 구성 요소
- app-sidebar: 데스크톱 전용. 공통 규격 — 워드마크 + "샘플고등학교" + 학생 메뉴 6개 + 구분선 + board-link(현재) + guide-link + "이OO · 학생" + nav-account-menu
- sidebar-item: 데스크톱 전용. 학생 6개, 현재 없음, "QR 찾기" 비활성 "준비 중"
- board-link: 데스크톱 전용. 현재 표시(#e6f4fc 채움 + #2b9fe0 아이콘). 학생도 같음
- guide-link: 데스크톱 전용. board-link 바로 아래(공통 모양)
- nav-pill: 모바일 전용. 워드마크 + "샘플고등학교" + nav-account-menu ▾
- nav-account-menu: 모바일 = 학교명 옆 ▾, 데스크톱 = app-sidebar 맨 아래. "로그아웃" 1개
- manage-back: 모바일 전용. "‹ 관리"(link #141414) → 화면 18
- board-tabs: segmented-control 3칸, 선택 = "오류 문의"
- segmented-control: board-tabs 트랙(#f3f3f3, rounded 9999)
- segmented-control-active: "오류 문의" 흰 pill. 하늘색: 1px #2b9fe0 테두리
- board-post-row: 글 행 4개(예시 오류 문의 ①~④, 최신 순). 행 = 위 줄 분류 caption #707070 "오류 문의" · 제목 title #141414(한 줄, 넘치면 …) / 아래 줄(간격 4) 글쓴이·날짜 caption #707070 "{학교명} 선생님 · {날짜}" + 행 오른쪽(세로 가운데) board-status-badge. 높이 64(56 이상), 좌우 여백 16, rounded 0, #ffffff, 행 사이 1px #f0f0f0 선. 누른 행만 잠깐 #f3f3f3. 예시: ① "사용 기록 저장 뒤 홈 숫자가 늦게 바뀌어요" · "샘플고등학교 선생님 · 10월 28일" · 답변 완료 ② "서류로 입고에서 두 장짜리 PDF가 한 장만 읽혀요" · "충북고등학교 선생님 · 10월 27일" · 접수 ③ "시약장 칸 이름이 잘려 보여요" · "청주여자고등학교 선생님 · 10월 25일" · 답변 완료 ④ "모바일에서 필터 시트가 닫히지 않아요" · "세광고등학교 선생님 · 10월 24일" · 접수. 사람 이름·이메일 없음. 핑크·하늘색 없음
- board-status-badge: 행마다 1개(4개). "접수" = #f3f3f3 채움 + #707070 label 12 / "답변 완료" = #141414 채움 + #ffffff label 12. rounded 9999, 높이 24, 좌우 여백 8. 무채색만 — 핑크·하늘색 없음
- tab-bar: 모바일 전용 하단 탭바 1개(공통 규격)
- tab-item: 4개. 활성 = "관리", "QR 스캔" 회색 "준비 중"
숨김(학생 0개, R5): board-write(페이지 머리·빈 상태 카드 모두) · board-form · board-post-menu. 그 밖 교사·admin 전용 컴포넌트도 이 화면에 없다.
### 반영한 레퍼런스
- https://uibowl.io/name/%EC%98%A4%EC%9D%BC%EB%82%98%EC%9A%B0?patterns=%EB%AC%B8%EC%9D%98%ED%95%98%EA%B8%B0&imgId=cmtpnvv5p001ajo04pqnetzma
- https://uibowl.io/website/KRDS?patterns=%EB%AC%B8%EC%9D%98%ED%95%98%EA%B8%B0&imgId=cmnqqy3l80004i90485kh3whj

## 역할별 노출
앱 전체(로그인 후 화면) 기준 개수. 직전 승인본 runs/20261027-1613 표를 그대로 옮기고 게시판 행을 더했다. 같은 화면의 상태 화면·모바일·데스크톱에 다시 나오는 같은 컴포넌트는 그 화면 1개로 센다.
- (새) 화면 20: board-write · board-form · board-post-menu = 교사·admin 1, 학생 0(R5 — 20-student에 없음, 학생에게는 글쓰기·내 글 메뉴 진입점이 없다). board-tabs · faq-item · board-post-row · board-status-badge · board-detail · board-answer = 학생·교사·admin 모두 1(읽기는 모든 역할).
- board-link(13 · 20 데스크톱 사이드바, 18 도움말)와 guide-link는 로그인한 모든 역할에게 같고 rules.json roles 대상이 아니어서 표에 넣지 않는다.
- terms-agree · age-confirm · privacy-consent-detail · privacy-link(화면 14)는 로그인 전 화면이라 역할 개수에 넣지 않는다.
- 화면 18의 관리 행(입고·사용자·판매처·재주문 알림·실험 매뉴얼)은 화면 이동 링크이고 stock-intake · user-manage · vendor-register · reorder-alert-card · manual-upload 컴포넌트가 아니다 — 개수 변화 없음. page-more-menu · reagent-wipe · record-wipe는 admin만(학생 R5 · 교사 R8 = 0) 그대로이며 화면 18에는 두지 않는다.
msds-entry = 화면 3 1 + 화면 10 상세 1(학생·교사·admin 모두 2, R4). 나머지 행은 runs/20261027-1613 값 그대로.

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
| board-write | 0 | 1 | 1 |
| board-form | 0 | 1 | 1 |
| board-post-menu | 0 | 1 | 1 |
| board-tabs | 1 | 1 | 1 |
| faq-item | 1 | 1 | 1 |
| board-post-row | 1 | 1 | 1 |
| board-status-badge | 1 | 1 | 1 |
| board-detail | 1 | 1 | 1 |
| board-answer | 1 | 1 | 1 |
