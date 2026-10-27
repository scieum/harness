# S2 설계 — run 20261027-1224

대상 화면: 13 (홈) + 상태 화면 13-feature-intro · 15 (랜딩) · 상태 화면은 13-feature-intro 하나 · 둘러보기 없음(input.json guest_screens 없음) · 학교: 샘플고등학교 (input.json) · 키스크린: 13-feature-intro-mobile, 13-feature-intro-desktop, 15-desktop
변경 사유: 2026-10-27 사용자 요청 (rules.json 1.30) — ① 신기능 소개 팝업 feature-intro-popup(첫 대상 = AI 입고, 화면 7 "서류로 입고"). 교사·admin이 홈(13)에 들어올 때 한 번, 모바일 = 바텀시트(✕ 없음) / 데스크톱 = 가운데 모달(폭 560 안팎, 오른쪽 위 ✕ = 닫기). 순서 = 꼬리표 "새 기능" → 제목 → 화면 7 그림 → 3단계 → 전폭 button-primary "AI 입고 써 보기" → feature-intro-dismiss "일주일 동안 보지 않기" · "닫기". 상태 프레임 13-feature-intro-mobile · desktop(교사 홈 위 팝업). ② 랜딩 15-desktop 히어로 왼쪽 글 묶음(꼬리표~특징 캡션) 전체를 오른쪽 product-shot 회색 패널의 세로 가운데로(±8px, landing_hero_align). 글 묶음 안 간격은 그대로, 15-mobile은 바꾸지 않는다.
근거: docs/PRD.md §7(13 홈 · 15 랜딩 · "신기능 소개 팝업 (2026-10-27, 교사·admin)"), docs/story-service.md 결정 사항 "신기능 소개 팝업·랜딩 글 위치 (화면 13·15, 2026-10-27 추가)", docs/design.md "Feature intro popup"·"Pre-login desktop" Screen 15 히어로 문단("vertically centered on the right panel, ±8px")·"Desktop shell"·`tab-bar`·`nav-pill`·"Landing", harness/rules.json 1.30(feature_intro, landing_hero_align, variants 13.feature-intro, screens_required 13·15, desktop_shell.pre_login.desktop_required 15, roles R1~R8(R5에 feature-intro-popup), guest.hidden_components(feature-intro-popup), never.N1·N2), research/s1-adopt.md, refs/uibowl-feature-intro-popup-20261027.md.
기준 설계(틀): input.json base — 화면 13 = run 20261013-1938 승인 S4(S4-screens-v24 716:2, 13-mobile 716:531 · 13-desktop 716:1936, 설계 = runs/20261013-1938/spec/s2-spec.md 화면 13), 화면 15 = run 20261012-0939 승인 S4(S4-screens-v22 655:2, 설계 = runs/20261012-0939/spec/s2-spec.md 화면 15). 새 Figma 파일 B4bHJR70riJS4cmXPT4ETs(노드 ID 같음). 13 기본 프레임은 그대로 두고 13-feature-intro는 그 교사 홈 위에 팝업만 얹는다. 15-mobile은 그대로, 15-desktop은 히어로 글 묶음 세로 위치만 바꾼다.

색·폰트·모서리·간격은 docs/design.md와 harness/rules.json을 따른다. 허용 색 밖의 값(반투명 검정 등)은 쓰지 않는다. 반투명 회색은 badge-overlay 안에서만. 그림자는 쓰지 않는다(segmented-control-active 예외) — 팝업에도 그림자 없음(feature_intro.style). 떠 있는 버튼(FAB)은 두지 않는다.
- 핑크 #d6246a·연핑크 #fbe9f0는 badge-low-stock, reorder-alert-card 안에서만 쓴다(이번 대상: 13 재고 부족 배지·재주문 알림 카드, 15 조각 안 배지). feature-intro-popup·feature-intro-dismiss·팝업 안 그림 조각에는 핑크를 쓰지 않는다 — 정보이지 경고가 아니다.
- 하늘색 #2b9fe0·옅은 하늘색 #e6f4fc는 선택·현재 위치·아이콘·진행 표시에만 쓴다. 글자색 금지(그 위 글자 #141414). badge-low-stock·reorder-alert-card·button-primary 안에는 쓰지 않는다. 팝업 안에서는 그림 조각 속 승인 화면의 원래 하늘색(진행 줄·선택 표시)만 남고, 팝업 자체 꼬리표·단계 번호·dismiss에는 쓰지 않는다.
- 모서리: 허용값 0 · 16 · 24 · 9999만. design.md·rules.json의 "rounded.lg"는 radius 표에 없는 이름이라 큰 모서리 24로 읽는다(시트 위쪽 모서리 24, 모달 24, 그림 패널 16).
- 배경 딤(feature_intro.mobile "배경 딤"): 허용 색에 반투명 검정이 없으므로(rgba는 badge-overlay 전용) 시안에서는 뒤 홈 위에 반투명 레이어를 그리지 않는다. 시트·모달은 1px #e0e0e0 테두리로 뒤 화면과 구분한다(승인된 시트·모달과 같은 방식). 실제 딤은 개발 쪽에서 처리한다.
학교 선택은 회원가입(화면 14)에만 있다. 화면 13과 상태 화면 13-feature-intro에는 학교 선택·전환을 두지 않고 현재 학교명 "샘플고등학교"를 모바일은 nav-pill 안, 데스크톱은 app-sidebar 맨 위(그리고 홈 페이지 머리 제목)에 표시한다. 팝업 그림 조각에 학교명이 보이면 "샘플고등학교"만 쓴다(다른 학교명 0, N1). 시약·기록·요약은 샘플고등학교 것만이다. 화면 15는 로그인 전이라 학교명을 표시하지 않는다.
외부 서비스 연결 값(서류 AI 읽기)은 서버에서만 다룬다. 팝업·랜딩 어디에도 연결 값 입력 칸·외부 서비스 설정·AI 엔진 선택 UI·관련 문구를 두지 않는다(N2). 팝업 문구는 "AI가 읽어요" 수준의 기능 설명만.
괄호 안 역할 표시가 없는 구성 요소는 그 화면에 들어오는 모든 역할에게 보인다. feature-intro-popup·feature-intro-dismiss는 교사·admin만(학생 0 — R5, 둘러보기 숨김 — guest.hidden_components). reorder-alert-card·sensor-alert-tile은 교사·admin만.

모바일 공통(승인본 그대로): tab-bar는 화면 아래 가장자리 y 780~844(폭 390, 높이 64, rounded 0, #ffffff + 위쪽 1px #f0f0f0 선, 그림자 없음)에 붙고 tab-item 4개 "홈" · "관리" · "QR 스캔" · "기록"을 같은 폭으로 채운다. "관리" 아이콘 = 네 칸 격자. 활성 = #2b9fe0 아이콘 + #141414 라벨, 비활성 = #707070. "QR 스캔"은 회색 — 아이콘·라벨 #adadad + 아이콘 아래 caption "준비 중"(#adadad), 누르면 ex-toast "준비 중이에요". 13 활성 = "홈". 시트는 tab-bar 위쪽 선 위에 붙는다(1px #e0e0e0 테두리, 위쪽 rounded 24).
- nav-pill(탭 첫 화면 머리) = 왼쪽 "Lab_Stock" 워드마크 → 오른쪽 학교명 "샘플고등학교" + nav-account-menu ▾. ☰·inventory-switch 없음.
데스크톱 공통(1440×900, rules.json desktop_shell): nav-pill·tab-bar 없음.
- app-sidebar: 왼쪽 고정 열 폭 240, 높이 전체, rounded 0, #f3f3f3 채움, 오른쪽 1px #f0f0f0 선. 맨 위 "Lab_Stock" 워드마크 + 학교명 "샘플고등학교"(title #141414, 전환 없음) → sidebar-item 묶음 → 맨 아래 "{이름} · {역할}"(body-sm) + nav-account-menu ▾.
- sidebar-item: 아이콘 + body 라벨, 높이 44, rounded 0. 현재 항목 = #e6f4fc 채움 + #2b9fe0 아이콘, 라벨 #141414. 메뉴: 학생 6개(홈·시약·센서·기록·시약장·QR 찾기) / 교사 9개(+ 입고·실험 매뉴얼·재주문 알림) / admin 11개(+ 사용자·판매처). "QR 찾기" 비활성 — #adadad + caption "준비 중".
- 본문 = 사이드바 오른쪽, 페이지 여백 32. 겹침: ex-modal-card 계열은 가운데(rounded 24, 1px #e0e0e0, 그림자 없음). ex-toast는 데스크톱 오른쪽 아래.
예시 데이터(승인본 그대로): 교사 김OO. 샘플고등학교 전체 시약 42종, 재고 부족 3종(염산 · 50 mL, 에탄올 · 200 mL, 질산은 · 5 g), MSDS 없는 시약 4종, 시약장 2개(칸 16개 중 지정 14 · 미지정 2), 재주문 알림 3건, 최근 사용 기록 3줄, 센서 고장 1 · 점검 필요 1. 13-feature-intro 뒤 홈은 13 승인 프레임과 같은 데이터·날짜.

## 화면 13
홈. 로그인 후 첫 화면, 학생·교사·admin 모두. 승인본(S4-screens-v24 13-mobile 716:531 · 13-desktop 716:1936) 그대로 — quick-action · home-summary · (교사·admin) reorder-alert-card · (교사·admin) sensor-alert-tile · 최근 사용 기록. 이번 변경은 이 기본 프레임을 바꾸지 않는다. 교사·admin이 홈에 들어오면 그 위에 feature-intro-popup이 한 번 뜬다(상태 화면 13-feature-intro) — 기본 프레임 13-mobile·13-desktop에는 팝업을 그리지 않는다.
예시 상태: 교사 김OO(승인본 그대로).
모바일 활성 탭: "홈". 위→아래: nav-pill(워드마크 + 학교명 ▾) → quick-action(교사 3칸 2+1) → home-summary ① 재고 요약(맨 아래 sensor-alert-tile 줄) → reorder-alert-card → home-summary ② 시약장 요약 → 최근 사용 기록 카드 → tab-bar.
데스크톱 배치: app-sidebar("홈" 현재) | 본문 = 페이지 머리(왼쪽 heading-2 "샘플고등학교" + 날짜·전체 시약 줄 / 오른쪽 quick-action 버튼 줄) → 숫자 타일 줄 "지금 처리할 것"(교사·admin = 재고 부족 3 · 재주문 알림 3 · MSDS 없는 시약 4 · 고장·점검 필요 센서 2 / 학생 = 재고 부족 3) → 3열 위젯 격자(최근 사용 기록 data-table 2칸 폭 · 재고 부족 · 시약장 요약). 승인본 그대로.
### 구성 요소
- app-sidebar: 데스크톱 전용. 공통 규격, 워드마크 + 학교명 "샘플고등학교" + 역할별 메뉴 + 이름·역할·nav-account-menu
- sidebar-item: 데스크톱 전용. 학생 6개 / 교사 9개 / admin 11개. 현재 = "홈", "QR 찾기" 비활성 '준비 중'
- nav-pill: 모바일 전용. "Lab_Stock" 워드마크 + 현재 학교명 "샘플고등학교" + nav-account-menu ▾. ☰ 없음, 학교 선택·전환 없음
- nav-account-menu: 모바일 = 학교명 옆 ▾, 데스크톱 = app-sidebar 맨 아래. "로그아웃" 1개. 하늘색 없음
- quick-action: 역할별 작업 바로가기(승인본 그대로). 모바일 = 교사 3칸 "사용 기록 입력" · "입고"(stock-intake 진입) · "시약장 설정", admin 3칸 "입고" · "사용자 관리"(user-manage 진입) · "시약장 설정", 2+1. 학생 2칸 "사용 기록 입력" · "시약장 보기". 데스크톱 = 페이지 머리 오른쪽 버튼 줄. 하늘색: 모바일 아이콘 #2b9fe0 + 바탕 #e6f4fc
- home-summary: 모바일 = 요약 카드 2장(#ffffff, 1px #f0f0f0, rounded 24, 여백 24) ① 재고 요약 "재고 부족 3개" + 부족 시약 칩 + "전체 시약 42종"(+ 교사·admin 카드 맨 아래 sensor-alert-tile 줄) ② 시약장 요약(막대 + "칸 16개 중 지정 14 · 미지정 2"). 데스크톱 = 숫자 타일 "재고 부족 3" · (교사·admin) "MSDS 없는 시약 4" + 위젯 "재고 부족"·"시약장 요약". 하늘색: 막대 지정 구간, › 아이콘
- sensor-alert-tile: 고장·점검 필요 센서 2. 모바일 = home-summary ① 카드 맨 아래 한 줄, 데스크톱 = "지금 처리할 것" 4번째 숫자 타일. 무채색. 하늘색: › 아이콘만 (교사·admin만)
- badge-low-stock: 재고 요약 개수 배지 "3", reorder-alert-card 안 "재고 부족"(#d6246a 채움, #ffffff label). 하늘색 없음
- reorder-alert-card: "재주문 알림" 카드(#f3f3f3, rounded 24). 모바일 = heading-4 "재주문 알림" + badge-low-stock + "3건 ›" + "필요량보다 적은 시약이 3종 있어요", 데스크톱 = 숫자 타일 줄의 타일 1개. 판매처 연결 버튼 없음. 하늘색 없음 (교사·admin만)
- data-table: 데스크톱 전용 "최근 사용 기록" 위젯(2칸 폭). 열 = 사용일 · 시약명 · 사용자 · 사용량, 3행, 머리 오른쪽 "전체 보기 ›"
- reagent-row: 모바일 최근 사용 기록 카드 안 3줄. 누르면 화면 10. 하늘색: 누른 행 #e6f4fc
- button-pill-soft: 모바일 "더 보기 ›", reorder-alert-card "3건 ›"(교사·admin만), 데스크톱 위젯 "전체 보기 ›"
- button-outline: 데스크톱 quick-action 버튼 줄 보조 버튼
- button-primary: 데스크톱 quick-action 버튼 줄 마지막 버튼(교사·admin "입고", 학생 "사용 기록 입력"). 하늘색 없음
- feature-intro-popup: 신기능 소개 팝업 자리(이 프레임에는 그리지 않음 — 연 모양은 상태 화면 13-feature-intro). 교사·admin이 홈에 들어올 때만, 한 번에 하나 (교사·admin만)
- ex-empty-state-card: 시약장 0개 / 최근 사용 기록 0건 안내(이 프레임 숨김)
- ex-toast: 권한 없는 주소로 들어왔을 때 한 번(13-no-access 승인본), 'QR 스캔' 탭·'QR 찾기' 메뉴 "준비 중이에요". 이 프레임에는 그리지 않는다
- tab-bar: 모바일 전용 하단 탭바 1개(공통 규격). 데스크톱에는 두지 않는다. 하늘색: 활성 tab-item 아이콘 #2b9fe0만
- tab-item: "홈" · "관리" · "QR 스캔" · "기록" 4개. 활성 = "홈", "QR 스캔" 회색 '준비 중', "관리"(격자 아이콘)·"기록" #707070
### 반영한 레퍼런스
- https://uibowl.io/name/%EB%AA%A8%EB%91%90%EC%9D%98%EC%A3%BC%EC%B0%A8%EC%9E%A5?patterns=%EC%8B%A0%EC%B2%AD%ED%95%98%EA%B8%B0&imgId=cmcld2g1u000fk107yclukc50
- https://uibowl.io/website/%EC%82%AC%EB%B0%A9%EB%84%B7?patterns=AI&imgId=cmu4rq2t60005l60421mauau0

## 상태 화면 13-feature-intro
신기능 소개 팝업(프레임 13-feature-intro-mobile · 13-feature-intro-desktop, 둘 다 키스크린). 교사 기준(교사·admin만 — 학생·둘러보기에는 뜨지 않는다). 흐름: 홈(13) 진입 → 팝업 하나. 주 버튼 "AI 입고 써 보기" = 화면 7 서류로 입고(intake-mode "서류로 입고")로 이동 + 이 기능 팝업은 다시 안 뜸 · "일주일 동안 보지 않기" = 7일 숨김 · "닫기"(데스크톱은 ✕도) = 이번 접속에서만 숨김. 동작 저장은 개발 쪽(브라우저 저장). 핑크·그림자 없음.
예시 상태: 교사 김OO가 홈에 막 들어온 직후. 뒤 화면 = 13 승인 프레임(교사 홈) 그대로 — 데이터·날짜 같음, 뒤 화면 요소는 위치·내용을 바꾸지 않는다.
모바일 활성 탭: "홈". 위→아래: nav-pill(워드마크 + 학교명 ▾) → 뒤 교사 홈 윗부분(quick-action · home-summary ① 일부 — 시트에 가려지지 않은 만큼) → feature-intro-popup = tab-bar 위쪽 선 위에 붙은 바텀시트(전폭 390, 위쪽 rounded 24·아래 0, ✕ 없음, 안 순서: 꼬리표 → 제목 → 그림 → 단계 3줄 → 전폭 button-primary → feature-intro-dismiss 한 줄) → tab-bar.
데스크톱 배치: app-sidebar("홈" 현재, 교사 9개) | 교사 홈 본문 그대로(페이지 머리 + "지금 처리할 것" 타일 줄 + 위젯 격자) 위 화면 가운데 feature-intro-popup 모달 폭 560(rounded 24, 오른쪽 위 ✕, 안 순서는 모바일과 같음 — 위 그림 / 아래 글 한 열).
### 구성 요소
- app-sidebar: 데스크톱 전용. 공통 규격, 학교명 "샘플고등학교" + 교사 메뉴 9개 + "김OO · 교사" + nav-account-menu. 모달 뒤 그대로 (교사·admin만)
- sidebar-item: 데스크톱 전용. 교사 9개. 현재 = "홈", "QR 찾기" 비활성 '준비 중' (교사·admin만)
- nav-pill: 모바일 전용. "Lab_Stock" 워드마크 + 현재 학교명 "샘플고등학교" + nav-account-menu ▾. 시트 위 그대로 보임 (교사·admin만)
- nav-account-menu: 닫힌 ▾ (교사·admin만)
- quick-action: 뒤 교사 홈 그대로 — 모바일 3칸 "사용 기록 입력" · "입고" · "시약장 설정"(2+1), 데스크톱 페이지 머리 버튼 줄. 하늘색: 모바일 아이콘 #2b9fe0 + 바탕 #e6f4fc (교사·admin만)
- home-summary: 뒤 교사 홈 요약 그대로(모바일은 시트에 가려지지 않은 윗부분만, 데스크톱 숫자 타일 + 위젯). 하늘색: 막대 지정 구간, › 아이콘 (교사·admin만)
- sensor-alert-tile: 뒤 홈 그대로(모바일 = 시트에 가려지면 그리지 않아도 됨, 데스크톱 = 4번째 숫자 타일 "고장·점검 필요 센서 2"). 무채색 (교사·admin만)
- badge-low-stock: 뒤 홈 재고 요약 배지 "3"·재주문 알림 "재고 부족"(#d6246a 채움, #ffffff label) 그대로. 팝업 안에는 없음 (교사·admin만)
- reorder-alert-card: 뒤 홈 그대로(모바일 = 시트에 가려진 만큼 생략, 데스크톱 = 숫자 타일 1개). 하늘색 없음 (교사·admin만)
- data-table: 데스크톱 전용. 모달 뒤 "최근 사용 기록" 위젯 그대로 (교사·admin만)
- button-outline: 데스크톱 뒤 quick-action 보조 버튼 그대로 (교사·admin만)
- feature-intro-popup: 신기능 소개 팝업 1개(#ffffff 채움, 1px #e0e0e0 테두리, 그림자 없음, 여백 24, 요소 사이 16 — 그림 위아래 24). 모바일 = tab-bar 위쪽 선 위에 붙은 바텀시트(전폭 390, 위쪽 rounded 24·아래 0, ✕ 없음, 뒤 홈 윗부분이 보이게 nav-pill 아래까지 덮지 않는다). 데스크톱 = 화면(1440×900) 가운데 모달 폭 560(ex-modal-card 계열보다 넓게, rounded 24), 오른쪽 위 ✕ 아이콘 버튼(#141414, 채움 없음, 누름 영역 44 이상, rounded 9999) = 닫기. 안 위→아래: ① 꼬리표 "새 기능"(#f3f3f3 채움 pill, rounded 9999, caption #141414, 여백 4·12) ② 제목 heading-3 #141414 "거래명세서만 올리면 AI가 입고 목록을 채워요"(모바일 2줄, 데스크톱 1~2줄, 왼쪽 정렬) ③ 그림 = #f3f3f3 패널(rounded 16, 전폭, 안 여백 16) 안에 승인된 화면 7 조각 — 왼쪽(모바일은 위) doc-upload 카드 일부("품의서·영수증·거래명세서를 올려 주세요") → 화살표(#707070) → 오른쪽(모바일은 아래) 7-doc-review 확인 표 2~3행(품명·규격·수량 + reagent-link 줄). 실제 승인 프레임의 축소 조각이며 사이드바·학교명이 들어가지 않게 자른다(들어가면 "샘플고등학교"만). 조각 안 핑크 없음 ④ 단계 3줄(세로, 줄 사이 8): 줄마다 번호 원(지름 24, #ffffff + 1px #e0e0e0, label #141414 "1"·"2"·"3") + body #141414 — "명세서·납품서 사진이나 PDF를 올려요" / "AI가 시약 이름·규격·수량을 읽어요" / "확인하고 한 번에 입고해요" ⑤ 전폭 button-primary "AI 입고 써 보기" ⑥ feature-intro-dismiss 한 줄. 핑크·하늘색(팝업 자체 요소) 없음 (교사·admin만)
- feature-intro-dismiss: 팝업 맨 아래 한 줄(button-primary 아래 간격 8): 왼쪽 텍스트 버튼 "일주일 동안 보지 않기" · 오른쪽 텍스트 버튼 "닫기". 둘 다 채움·테두리 없음, body-sm #707070(주 버튼보다 약하게), 누름 영역 높이 44 이상. 모바일·데스크톱 같은 줄. 데스크톱은 ✕도 "닫기"와 같은 동작. 하늘색·핑크 없음 (교사·admin만)
- button-primary: 팝업 "AI 입고 써 보기"(#141414 채움, #ffffff 글자, rounded 9999, 높이 48, 팝업 안 전폭) → 화면 7 서류로 입고. 데스크톱 뒤 quick-action 마지막 버튼 "입고" 그대로. 하늘색 없음 (교사·admin만)
- tab-bar: 모바일 전용 하단 탭바 1개(공통 규격). 바텀시트는 이 바 위쪽 선 위에 붙고 탭바는 그대로 보인다. 데스크톱에는 두지 않는다 (교사·admin만)
- tab-item: 4개 "홈" · "관리" · "QR 스캔" · "기록". 활성 = "홈", "QR 스캔" 회색 '준비 중' (교사·admin만)
### 반영한 레퍼런스
- https://uibowl.io/name/%EB%AA%A8%EB%91%90%EC%9D%98%EC%A3%BC%EC%B0%A8%EC%9E%A5?patterns=%EC%8B%A0%EC%B2%AD%ED%95%98%EA%B8%B0&imgId=cmcld2g1u000fk107yclukc50
- https://uibowl.io/name/%EB%8D%B0%EC%9D%BC%EB%A6%AC%EC%83%B7?patterns=%EC%95%BD%EA%B4%80%EB%8F%99%EC%9D%98&imgId=cm90v7lis001bk10dcwvwu420
- https://uibowl.io/name/%ED%8C%A8%EC%8A%A4%EC%98%A4%EB%8D%94?patterns=%EC%8B%A0%EC%B2%AD%ED%95%98%EA%B8%B0&imgId=cmsph1e6f00ccjp04i4cje3i8
- https://uibowl.io/name/LG%20ThinQ?patterns=AI&imgId=cmf2a9pjn000tjl04eyw47yvv
- https://uibowl.io/website/%EC%82%AC%EB%B0%A9%EB%84%B7?patterns=AI&imgId=cmu4rq2t60005l60421mauau0

## 화면 15
랜딩. 로그인 전 첫 화면. 바탕 = run 20261012-0939 승인 S4(S4-screens-v22 655:2) 15-mobile · 15-desktop. 15-mobile은 그대로(한 줄 흐름이라 landing_hero_align 해당 없음). 15-desktop은 히어로 글 묶음의 세로 위치만 바꾼다(rules.json landing_hero_align): 왼쪽 글 묶음 = 꼬리표 → 2줄 헤드라인 "우리 학교 시약장, / 한 화면에서 관리해요"(48 Bold 700) → body-lg 부제 2줄 → landing-cta → guest-entry → 특징 캡션 "학교별 데이터 분리 · NEIS 학교 검색 · QR로 시약 찾기"를 한 덩어리(landing-hero)로 묶고, 그 덩어리의 세로 가운데 y = 오른쪽 product-shot 회색 패널(#f3f3f3, rounded 24)의 세로 가운데 y(허용 ±8px). 기준은 회색 패널 범위다(겹친 흰 카드가 패널 밖으로 나가도 그 부분은 기준에 넣지 않는다). 글 묶음 안 순서·간격·글자·폭과 가로 위치, product-shot·web-header·히어로 아래 섹션은 모두 그대로. 학교명·학교 선택·tab-bar·app-sidebar 없음. 워드마크는 상단 바에만 1번.
CTA 위계(그대로): 채움 "회원가입" → 외곽선 "로그인" → 가장 약한 "둘러보기" 3단. 페이지 끝 cta-band에서 한 번 더(데스크톱).
모바일(390×844) 위→아래(그대로): nav-pill(워드마크만) → landing-hero(꼬리표 "과학실 시약·센서 관리" → 강조 헤드라인 2줄 → 부제) → feature-card 4장 → 하단 고정 영역(landing-cta 버튼 2개 세로 + guest-entry). 하단 탭바 없음.
데스크톱 배치: 1440 × 5498 세로 긴 프레임 한 장(높이 그대로), web-header(위) | 가운데 콘텐츠 폭 1200 — 히어로 2열(왼쪽 landing-hero 글 묶음 = product-shot 회색 패널 세로 가운데 · 오른쪽 product-shot) → landing-tabs → 문제 공감 feature-card 3 → landing-section 4 → step-flow 5단계 → 대상 탭 → 안심 2×2 → cta-band → web-footer 한 줄.
### 구성 요소
- web-header: 데스크톱 전용. 로그인 전 공통 규격(전폭 1440, 높이 64, rounded 0, #ffffff + 아래 1px #f0f0f0). 왼쪽 "Lab_Stock" 워드마크(페이지의 유일한 워드마크), 오른쪽 button-outline "로그인" + button-primary "회원가입". 그대로. 하늘색 없음
- nav-pill: 모바일 전용(그대로). "Lab_Stock" 워드마크만(#f3f3f3, rounded 9999). 학교명 없음(로그인 전). 데스크톱에는 두지 않는다
- landing-hero: 히어로 글 묶음 1개. 안에 "Lab_Stock" 워드마크 없음. 모바일 = 그대로(꼬리표 caption #707070 "과학실 시약·센서 관리" → 헤드라인 2줄 → body-lg 부제). 데스크톱 = 꼬리표 → 2줄 헤드라인 48 Bold 700 → body-lg 부제 → landing-cta → guest-entry → 특징 캡션(caption #707070)을 세로 auto-layout 한 덩어리로 묶고(안 간격 승인본 그대로), 덩어리 전체를 product-shot 회색 패널 세로 가운데에 맞춘다(덩어리 중심 y − 패널 중심 y = −8 ~ +8). 가로 위치·폭 그대로. 모노크롬, 학교명 없음
- product-shot: 데스크톱 전용(그대로). 히어로 오른쪽 #f3f3f3 패널(rounded 24) + 브라우저 틀 안 승인 홈(13-desktop) 실제 크기 조각 + 왼쪽 아래 겹친 흰 카드(data-table 몇 행), hairline으로 겹침, 그림자 없음. 위치·크기 바꾸지 않음 — 글 묶음 세로 가운데의 기준. 핑크는 조각 안 badge-low-stock 안에서만
- shot-sidebar: 데스크톱 전용. product-shot · 대상 탭 교사 조각 안 승인 화면 사이드바 이름(app-sidebar로 세지 않음, 그대로)
- landing-cta: 모바일 = 하단 고정 전폭 버튼 2개 세로 "회원가입" · "로그인", 데스크톱 = 히어로 글 묶음 안 "회원가입하고 시작하기" · "로그인"(글 묶음과 함께 이동, 그대로)
- button-primary: landing-cta · web-header · cta-band "회원가입"(#141414 채움, #ffffff 글자, rounded 9999, 높이 44 이상. #141414 띠 안 cta-band에서는 반전). 하늘색 없음
- button-outline: landing-cta · web-header "로그인", cta-band "둘러보기". 하늘색 없음
- guest-entry: button-pill-soft "둘러보기 ›" 1개(→ 둘러보기 13, 데스크톱은 글 묶음과 함께 이동). 하늘색: › 아이콘 #2b9fe0
- button-pill-soft: guest-entry "둘러보기 ›"
- landing-tabs: 데스크톱 전용(그대로). 접는 선 탭 줄, 활성 밑줄 2px #2b9fe0
- feature-card: 모바일 = 기능 카드 4장(그대로, ④에 예시 badge-low-stock), 데스크톱 = 문제 공감 3장(그대로). 하늘색: 아이콘만
- badge-low-stock: 모바일 feature-card ④ 예시 배지, 데스크톱 조각 안 재고 부족 표시(그대로)
- data-table: 데스크톱 전용. product-shot 겹친 카드, landing-section 조각 안 승인 표(그대로)
- landing-section: 데스크톱 전용 4개(그대로 — 사용 기록 조각 = 4-desktop)
- step-flow: 데스크톱 전용(그대로). #141414 반전 띠, 5단계
- segmented-control: 데스크톱 전용. 대상 탭 "교사 · 학생 · 관리자"(그대로)
- segmented-control-active: "교사" 흰 pill. 하늘색: 1px #2b9fe0 테두리
- cta-band: 데스크톱 전용(그대로)
- web-footer: 데스크톱 전용(그대로). caption #707070 "© 2026 사이음(sci_eum). 과학의 사이, 사람을 잇다."
### 반영한 레퍼런스
- https://uibowl.io/website/%EB%A7%88%EC%9D%B4%ED%81%AC%EB%A1%9C%EC%86%8C%ED%94%84%ED%8A%B8%20%ED%81%B4%EB%9E%98%EB%A6%AC%ED%8B%B0%20(Microsoft%20Clarity)?patterns=%EB%9E%9C%EB%94%A9%ED%8E%98%EC%9D%B4%EC%A7%80&imgId=cmt180ji1000dkz04ef56j21k
- https://uibowl.io/website/%EC%84%BC%EC%84%9C%ED%83%80%EC%9B%8C?patterns=%EB%9E%9C%EB%94%A9%ED%8E%98%EC%9D%B4%EC%A7%80&imgId=cmtfd83b80003l804cq6f05lo
- https://uibowl.io/website/braintrust?patterns=%EB%9E%9C%EB%94%A9%ED%8E%98%EC%9D%B4%EC%A7%80&imgId=cm5vzhejt003pla0cs5ayo0x7
- https://uibowl.io/website/%EB%8B%B9%EA%B7%BC%20%EB%B9%84%EC%A6%88%EB%8B%88%EC%8A%A4?patterns=%EB%9E%9C%EB%94%A9%ED%8E%98%EC%9D%B4%EC%A7%80&imgId=cmso68wbc000clf04biyhswza
- https://uibowl.io/website/KRDS?patterns=%EB%9E%9C%EB%94%A9%ED%8E%98%EC%9D%B4%EC%A7%80&imgId=cmnqqvr26000kl50444y648go

## 역할별 노출
앱 전체(로그인 후 화면) 기준 개수. 직전 승인본 runs/20261014-0806 표를 그대로 옮기고 이번 변경을 더했다. 같은 화면의 상태 화면·모바일·데스크톱에 다시 나오는 같은 컴포넌트는 그 화면 1개로 센다(예: 화면 13의 feature-intro-popup은 13·13-feature-intro, 모바일·데스크톱에 나와도 1).
이번 변경(교사·admin만 — 학생 R5 = 0, 둘러보기 숨김):
- feature-intro-popup = 화면 13(13-feature-intro) 1 → 교사 1 · admin 1, 학생 0.
- feature-intro-dismiss = 화면 13(13-feature-intro) 1 → 교사 1 · admin 1, 학생 0(팝업 안에만 있음).
- 팝업 주 버튼 "AI 입고 써 보기"는 화면 7로 가는 이동 버튼이고 stock-intake·doc-upload 컴포넌트가 아니다(그림 조각도 축소 이미지라 컴포넌트로 세지 않는다) — stock-intake·doc-upload 개수는 바뀌지 않는다.
- 화면 15는 로그인 전이라 역할 개수에 넣지 않는다. 둘러보기(13-guest)는 R 규칙 대상이 아니어서 표에 넣지 않는다 — 둘러보기 홈에는 feature-intro-popup을 그리지 않는다(guest.hidden_components).
나머지 행은 runs/20261014-0806 값 그대로.

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
