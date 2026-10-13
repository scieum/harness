# S2 설계 — run 20261013-1938

대상 화면: 2 (시약 목록) · 10 (사용 기록 내역) · 13 (홈) · 17 (센서) · 18 (관리, 새 화면·모바일 전용) + 상태 화면 2-wipe · 10-record-wipe + 둘러보기 18 · 학교: 샘플고등학교 (input.json) · 키스크린: 18-mobile, 2-wipe-mobile, 10-record-wipe-desktop
변경 사유: 개발 세션 요청 9 (2026-10-13, rules.json 1.29) — ① 모바일 하단 탭 '시약' → '관리'(격자 아이콘), 탭 4개 = 홈 · 관리 · QR 스캔 · 기록 ② 화면 18 관리 = 모바일 전용, manage-list 묶음 3개(재고 · 입고·주문 · 학교) + 행마다 요약 caption ③ 관리 아래 화면(이번 대상 2·17) 모바일 머리 왼쪽 manage-back "‹ 관리", 탭 '관리' 활성 ④ ☰(mobile-menu-button·mobile-menu-sheet)와 inventory-switch "시약 | 센서" 없앰 — 2·13·17 어디에도 두지 않는다(13-menu 상태 없음) ⑤ 시약 전체 삭제(2-wipe)·기록 삭제(10-record-wipe) = admin만, 페이지 머리 ⋯(page-more-menu) → 학교명 입력(school-name-confirm) 후 실행 ⑥ 둘러보기 18-guest = 시약 · 센서 두 줄, 데모 학교.
근거: docs/PRD.md §7, docs/story-service.md 결정 사항 2026-10-13(관리 탭·전체 삭제), docs/design.md "Manage tab"·"Wipe — all reagents · records"·`tab-bar`·`nav-pill`("Mobile menu … removed 2026-10-13")·"Sensors"(Entry)·"Desktop shell"·"Guest mode", harness/rules.json 1.29(manage, wipe, tab_bar.labels·sensor_entry·quick_action_note, mobile_menu.removed, frames.mobile_only_screens [18], variants 2.wipe·10.record-wipe, screens_required 18, roles R1~R8(R5·R8에 page-more-menu·reagent-wipe·record-wipe), guest.manage·hidden_components, never.N1·N2), research/s1-adopt.md.
기준 설계(틀): input.json base — 화면 2·10 = runs/20261011-0813 승인 S4(설계 = runs/20261011-0813/spec/s2-spec.md 화면 2·10), 화면 13 = runs/20261012-0939 승인 S4 v22(설계 = runs/20261012-0939/spec/s2-spec.md 화면 13), 화면 17 = S4-screens-v23 696:2(설계 = runs/20261012-1155/spec/s2-spec.md 화면 17). 승인본 구성은 그대로 두고 요청 9 결정분만 바꾼다. 화면 18은 새로 설계한다(admin 기준, 요약은 예시 값).

색·폰트·모서리·간격은 docs/design.md와 harness/rules.json을 따른다. 허용 색 밖의 값(딤 반투명 검정 등)은 쓰지 않는다. 그림자는 쓰지 않는다(segmented-control-active 예외). 떠 있는 버튼(FAB)은 두지 않는다.
- 핑크 #d6246a·연핑크 #fbe9f0는 badge-low-stock, reorder-alert-card 안에서만 쓴다(이번 대상 기준: 화면 2·13 재고 부족 배지, 13 재주문 알림). 관리 목록 요약 숫자("재고 부족 3"·"고장 1"), 전체 삭제·기록 삭제의 위험 표시·모달·시트·미리보기 줄에는 핑크·빨강을 쓰지 않는다.
- 위험 표시는 무채색: 제목 앞 #141414 외곽선 경고 아이콘(삼각형 !) 하나. 되돌릴 수 없는 실행 버튼("전체 삭제"·"기록 N건 삭제")은 검정 button-primary(#141414 채움, #ffffff 글자) — 시약·센서 삭제와 같다. 꺼진 button-primary = #e0e0e0 채움 + #707070 글자(17-type 승인본과 같음).
- 하늘색 #2b9fe0·옅은 하늘색 #e6f4fc는 선택·현재 위치·아이콘·체크에만 쓴다. 글자색 금지(그 위 글자 #141414). badge-low-stock·reorder-alert-card·button-primary 안에는 쓰지 않는다. manage-row 아이콘·숫자에는 쓰지 않는다(아이콘 #141414).
학교 선택은 회원가입(화면 14)에만 있다. 화면 2·10·13·17·18과 상태 화면 2-wipe·10-record-wipe에는 학교 선택·전환을 두지 않고 현재 학교명 "샘플고등학교"를 모바일은 nav-pill 안, 데스크톱은 app-sidebar 맨 위에 표시한다. 2-wipe·10-record-wipe는 school-name-confirm 안내 caption·입력 칸 placeholder에도 같은 학교명이 나온다. 시약·센서·기록·홈·관리 요약과 삭제 범위는 모두 샘플고등학교 것만이다(N1). 둘러보기 18은 "데모 학교"만 쓴다.
외부 서비스 연결 값은 서버에서만 다룬다. 어떤 화면에도 연결 값 입력 칸·외부 서비스 설정·AI 엔진 선택 UI·관련 문구를 두지 않는다(N2). 관리 탭에도 그런 항목을 두지 않는다.
괄호 안 역할 표시가 없는 구성 요소는 그 화면에 들어오는 모든 역할에게 보인다. page-more-menu·reagent-wipe·record-wipe·school-name-confirm은 admin만(교사·학생·둘러보기 0 — R5·R8). list-select-toggle·msds-bulk-banner·sensor-add·sensor-doc-add·sensor-alert-tile·reorder-alert-card는 교사·admin만. manage-list의 '입고·주문' 묶음은 교사·admin, '학교' 묶음은 admin만 보이고, manage-row·manage-back은 모든 역할에 있다.

모바일 공통(승인본 + 요청 9): tab-bar는 화면 아래 가장자리 y 780~844(폭 390, 높이 64, rounded 0, #ffffff + 위쪽 1px #f0f0f0 선, 그림자 없음)에 붙고 tab-item 4개 "홈" · "관리" · "QR 스캔" · "기록"을 같은 폭으로 채운다(모든 역할 같음). "관리" 아이콘 = 네 칸 격자. 활성 = #2b9fe0 아이콘 + #141414 라벨, 비활성 = #707070 아이콘·라벨. "QR 스캔"은 화면 12 전까지 회색 — 아이콘·라벨 #adadad + 아이콘 아래 caption "준비 중"(#adadad), 누르면 ex-toast "준비 중이에요". 활성 탭: 2·17·18 = "관리", 10 = "기록", 13 = "홈". 하단 고정 바·시트는 tab-bar 위쪽 선 위에 붙는다(딤 없음, 1px #e0e0e0 테두리, 위쪽 rounded 24, 오른쪽 위 × 닫기).
- mobile-menu-button(☰)·mobile-menu-sheet·inventory-switch는 어느 프레임에도 그리지 않는다. 계정·로그아웃은 nav-pill 학교명 옆 ▾(nav-account-menu). 센서는 관리 탭(화면 18) '센서' 행으로 들어간다.
- nav-pill 두 가지: ① 탭 첫 화면(13 홈 · 18 관리 · 10 기록) = 왼쪽 "Lab_Stock" 워드마크(10은 + 제목 "사용 기록 내역") → 오른쪽 학교명 + nav-account-menu ▾. ② 관리 아래 화면(2 · 17 및 그 상태) = 맨 왼쪽 manage-back "‹ 관리"(워드마크 자리) → 오른쪽 학교명 + nav-account-menu ▾. 화면 제목은 nav-pill 아래 페이지 머리 줄.
데스크톱 공통(1440×900, rules.json desktop_shell, 요청 9로 바뀌지 않음): nav-pill·tab-bar·manage-back·manage-list 없음.
- app-sidebar: 왼쪽 고정 열 폭 240, 높이 전체, rounded 0, #f3f3f3 채움, 오른쪽 1px #f0f0f0 선. 맨 위 "Lab_Stock" 워드마크 + 학교명 "샘플고등학교"(title #141414, 전환 없음) → sidebar-item 묶음 → 맨 아래 "{이름} · {역할}"(body-sm) + nav-account-menu ▾.
- sidebar-item: 아이콘 + body 라벨, 높이 44, rounded 0. 현재 항목 = #e6f4fc 채움 + #2b9fe0 아이콘, 라벨 #141414. 메뉴(desktop_shell.menu): 학생 6개(홈·시약·센서·기록·시약장·QR 찾기) / 교사 9개(+ 입고·실험 매뉴얼·재주문 알림) / admin 11개(+ 사용자·판매처). "QR 찾기"는 비활성 — 아이콘·라벨 #adadad + caption "준비 중"(#adadad).
- 본문 = 사이드바 오른쪽, 페이지 여백 32. 페이지 머리 = 왼쪽 제목(heading-2) + 개수(caption #707070), 오른쪽 검색·필터·선택·보조·주 버튼, 맨 오른쪽 끝 (admin) page-more-menu ⋯. data-table = ex-data-table-cell 머리행(caption #707070)·본문(body-sm), rounded 16 컨테이너 + 1px #f0f0f0 테두리, 선택 행 #e6f4fc. detail-drawer = 오른쪽 폭 480, 높이 전체, #ffffff, 왼쪽 1px #f0f0f0 선, 딤 없음, 오른쪽 위 × 닫기.
- 겹침: ex-modal-card는 확인에만(가운데 폭 440, rounded 24, 1px #e0e0e0, 그림자·딤 없음). 모바일 고르기 시트는 데스크톱에서 드롭다운·팝오버. ex-toast는 모바일 tab-bar 바로 위 / 데스크톱 오른쪽 아래.
- page-more-menu 공통 모양: ⋯ 아이콘 버튼(#141414, 채움 없음, 44×44, rounded 9999). 누르면 버튼 바로 아래 붙는 작은 메뉴(reagent-more-menu 모양: #ffffff, rounded 24, 1px #f0f0f0, 여백 8, 그림자 없음) 1항목(왼쪽 #141414 경고 아이콘 + body #141414, 높이 44). 누른 동안 버튼 뒤 #e6f4fc 원. 지울 것이 0건이면 항목 #adadad + 아래 caption "지울 시약이 없어요" / "지울 기록이 없어요". 선택 모드와 섞지 않는다(선택 모드 중에는 숨김).
- school-name-confirm 공통 모양: 위 caption #707070 "확인을 위해 학교 이름 '샘플고등학교'를 입력하세요" → text-input(#f0f0f0, rounded 16, placeholder "샘플고등학교" #adadad, 포커스 링 2px #141414). 입력이 학교명과 정확히 같을 때만 실행 버튼이 켜진다. 다르면 칸 아래 body-sm #707070 "학교 이름이 달라요". 붙여 넣기 허용.
예시 데이터(공통): 오늘 = 2026-10-13. 샘플고등학교 시약 42종, 재고 부족 3종(염산 · 50 mL, 에탄올 · 200 mL, 질산은 · 5 g), MSDS 없는 시약 4종, 시약장 2개(칸 16개 중 지정 14 · 미지정 2), 재주문 알림 3건, 사용자 학생 3 · 교사 1 · admin 1, 판매처 4곳. 센서 7개(runs/20261012-1155 예시 그대로 — 고장 1 운동 센서, 점검 필요 1 무선 pH 센서). 기본 프레임 역할 = 교사 "김OO · 교사"(승인본과 같음), 화면 18·2-wipe·10-record-wipe = admin "정OO · admin".

## 화면 2
시약 목록. 학생·교사·admin 모두. 승인본(runs/20261011-0813 화면 2) 그대로(필터 적용 없음, 이름순, "전체", 42종) + 요청 9: ① 모바일 inventory-switch 없앰 ② 모바일 nav-pill 맨 왼쪽 manage-back "‹ 관리"(워드마크 자리), 탭 '관리' 활성 ③ 페이지 머리 맨 오른쪽 (admin) page-more-menu ⋯ → "시약 전체 삭제"(상태 화면 2-wipe). 이 프레임은 교사 기준이라 ⋯는 그리지 않는다. 행 끝 삭제 버튼은 여전히 없다.
모바일 활성 탭: "관리". 위→아래: nav-pill(‹ 관리 + 학교명 ▾) → (교사·admin) msds-bulk-banner → 페이지 머리 줄(왼쪽 heading-4 "시약 42종" + 오른쪽 (교사·admin) list-select-toggle "선택" · (admin) page-more-menu ⋯) → segmented-control → 검색 줄(text-input + list-filter-button) → (필터 적용 시) filter-chip-row → reagent-row 목록 → tab-bar. 좌우 여백 16.
데스크톱 배치: app-sidebar("시약" 현재) | 본문 = 페이지 머리(왼쪽 "시약" + "42종" + 요약 줄 / 오른쪽 검색 text-input 폭 320 + list-filter-button + (교사·admin) list-select-toggle + (admin) page-more-menu ⋯) → (교사·admin) msds-bulk-banner → 툴바(segmented-control 왼쪽, filter-chip-row 오른쪽) → data-table → 페이지 번호 "1 2 3".
### 구성 요소
- app-sidebar: 데스크톱 전용. 공통 규격, 워드마크 + 학교명 "샘플고등학교" + 역할별 메뉴 + 이름·역할·nav-account-menu
- sidebar-item: 데스크톱 전용. 학생 6개 / 교사 9개 / admin 11개("센서" 포함, "QR 찾기" 비활성 '준비 중'). 현재 = "시약"(#e6f4fc 채움 + #2b9fe0 아이콘, 라벨 #141414)
- nav-pill: 모바일 전용. 관리 아래 화면 머리 — 맨 왼쪽 manage-back "‹ 관리" + 오른쪽 현재 학교명 "샘플고등학교" + nav-account-menu ▾. 워드마크·☰ 없음. 학교 전환 없음
- manage-back: 모바일 전용. nav-pill 맨 왼쪽 link "‹ 관리"(‹ 아이콘 + body #141414, 누름 영역 44 이상) → 화면 18. 데스크톱에는 두지 않는다. 하늘색: ‹ 아이콘 #2b9fe0
- nav-account-menu: 모바일 = 학교명 옆 ▾, 데스크톱 = app-sidebar 맨 아래. "로그아웃" 1개. 하늘색 없음
- msds-bulk-banner: 모바일 = nav-pill 아래 전폭 띠(rounded 0, #e6f4fc, 여백 12·16) "MSDS 없는 시약 4종" + button-pill-soft "한 번에 찾기", 데스크톱 = 페이지 머리 아래 본문 폭 띠(rounded 16). 승인본 그대로. 하늘색: 띠 채움 #e6f4fc (교사·admin만)
- list-select-toggle: 선택 모드 진입. 모바일 = 페이지 머리 줄 오른쪽 button-pill-soft "선택", 데스크톱 = list-filter-button 오른쪽 button-outline "선택". 승인본 그대로. 핑크 없음 (교사·admin만)
- page-more-menu: 페이지 머리 맨 오른쪽 ⋯(공통 모양, 모바일·데스크톱 같은 자리). 메뉴 항목 = reagent-wipe "시약 전체 삭제". 이 프레임(교사)에는 그리지 않는다 — admin 프레임은 상태 화면 2-wipe. 하늘색: 누른 동안 버튼 뒤 #e6f4fc 원 (admin만)
- segmented-control: "전체 / 재고 부족", 한 번에 하나. 데스크톱 = 툴바 왼쪽
- segmented-control-active: 선택 옵션 "전체" 흰 pill. 하늘색: 1px #2b9fe0 테두리(글자 #141414)
- text-input: 검색 "시약명 검색"(#f0f0f0, rounded 16, 포커스 링 2px #141414). 하늘색: 검색 아이콘 #2b9fe0
- list-filter-button: 검색 오른쪽 button-pill-soft "필터"(왼쪽 필터 아이콘, 높이 44 이상). 적용 개수 pill은 적용 없음이라 숨김. 하늘색: 필터 아이콘 #2b9fe0
- list-filter-sheet: 필터 패널(이 프레임에서는 닫힘, 승인본 2-filter 모양)
- filter-chip-row: 필터 적용 시에만(이 프레임 숨김)
- data-table: 데스크톱 전용 시약 표(승인본 그대로). 열 = 시약명(정렬, 활성 ↑ #2b9fe0) · 보관 분류 · 보관 위치 · 재고 · 상태(badge-low-stock) · 최근 입고일 · MSDS. 한 페이지 20행, 페이지 번호 "1 2 3". 행을 누르면 화면 3 드로어
- reagent-row: 모바일 전용. 시약명(title) + 재고량·단위(body) + 입고일(caption #707070), #f3f3f3, rounded 16, 행 사이 12. 누르면 화면 3(머리는 지금처럼 ‹ 뒤로). 하늘색: › 아이콘 #2b9fe0
- badge-low-stock: 재고 부족 3종 "재고 부족"(#d6246a 채움, #ffffff label, rounded 9999). 모바일 = 시약명 옆, 데스크톱 = 상태 열. 하늘색 없음
- button-pill-soft: 모바일 list-select-toggle "선택", msds-bulk-banner "한 번에 찾기"
- button-outline: 데스크톱 list-select-toggle "선택" (교사·admin만)
- ex-empty-state-card: 검색 결과 0건 "찾는 시약이 없어요"(이 프레임 숨김). 하늘색: 안내 아이콘 #2b9fe0
- ex-toast: 'QR 스캔' 탭·'QR 찾기' 메뉴를 누르면 "준비 중이에요"(이 프레임에는 그리지 않음). 핑크 없음
- tab-bar: 모바일 전용 하단 탭바 1개(공통 규격). 데스크톱에는 두지 않는다. 하늘색: 활성 tab-item 아이콘 #2b9fe0만
- tab-item: "홈" · "관리" · "QR 스캔" · "기록" 4개. 활성 = "관리"(격자 아이콘). "QR 스캔" 회색 '준비 중', "홈"·"기록" #707070
### 반영한 레퍼런스
- https://uibowl.io/website/%EB%8B%B9%EA%B7%BC%20%EB%B9%84%EC%A6%88%EB%8B%88%EC%8A%A4?patterns=%EC%83%81%EC%84%B8%EC%A0%95%EB%B3%B4%20%28PDP%29&imgId=cmso6dgem00ualf04cqgg6fh8
- https://uibowl.io/name/%EC%BD%94%EC%9B%A8%EC%9D%B4%20IoCare%2B?patterns=%EC%84%A4%EC%A0%95&patternName=%EB%A9%A4%EB%B2%84%20%EA%B4%80%EB%A6%AC

## 상태 화면 2-wipe
시약 전체 삭제 확인(프레임 2-wipe-mobile · 2-wipe-desktop, 키스크린 2-wipe-mobile). admin만(교사·학생·둘러보기에는 ⋯ 자체가 없다). 흐름: 페이지 머리 ⋯(page-more-menu) → 메뉴 "시약 전체 삭제"(reagent-wipe) → 확인 ex-modal-card → 학교명을 정확히 입력하면 "전체 삭제"가 켜짐 → 누르면 ex-toast "시약 42종을 삭제했어요" → 빈 목록(ex-empty-state-card). "닫기"·× = 모달만 닫힘. 되돌리기 없음. 사용·입고 기록은 남는다(화면 10에 '삭제된 시약'). 핑크·빨강 없음.
예시 상태: admin 정OO, 화면 2(42종, "전체", 이름순)에서 ⋯ → "시약 전체 삭제"를 고른 직후. 메뉴는 닫히고 ⋯ 버튼만 누른 상태(#e6f4fc 원)로 남은 채 모달이 열림. 학교명 칸은 비어 있음(placeholder "샘플고등학교") → "전체 삭제" 꺼짐. 뒤 화면 2 목록은 그대로 보인다(딤 없음).
모바일 활성 탭: "관리". 위→아래: nav-pill(‹ 관리 + 학교명 ▾) → msds-bulk-banner → 페이지 머리 줄("시약 42종" + "선택" + ⋯ 누른 상태) → segmented-control → 검색 줄 → reagent-row 목록(윗부분) → ex-modal-card = tab-bar 위 시트(전폭, 위쪽 rounded 24) → tab-bar.
데스크톱 배치: app-sidebar("시약" 현재, admin 11개) | 화면 2 본문 그대로(페이지 머리 맨 오른쪽 ⋯ 누른 상태 → msds-bulk-banner → 툴바 → data-table) 위 가운데 ex-modal-card 폭 440.
### 구성 요소
- app-sidebar: 데스크톱 전용. 공통 규격, 학교명 "샘플고등학교" + admin 메뉴 + "정OO · admin" + nav-account-menu (admin만)
- sidebar-item: 데스크톱 전용. admin 11개. 현재 = "시약", "QR 찾기" 비활성 '준비 중' (admin만)
- nav-pill: 모바일 전용. manage-back "‹ 관리" + 현재 학교명 "샘플고등학교" + nav-account-menu ▾. ☰·inventory-switch 없음 (admin만)
- manage-back: 모바일 전용. nav-pill 맨 왼쪽 "‹ 관리"(모달 뒤 그대로). 하늘색: ‹ 아이콘 #2b9fe0 (admin만)
- nav-account-menu: 닫힌 ▾ (admin만)
- msds-bulk-banner: 모달 뒤 화면 2 띠 그대로. 하늘색: 띠 채움 #e6f4fc (admin만)
- list-select-toggle: 모달 뒤 페이지 머리 "선택"(모바일 button-pill-soft / 데스크톱 button-outline) 그대로 (admin만)
- page-more-menu: 페이지 머리 맨 오른쪽 ⋯(공통 모양). 방금 눌러 버튼 뒤 #e6f4fc 원, 메뉴는 닫힘. 하늘색: 누른 상태 원 #e6f4fc (admin만)
- segmented-control: 모달 뒤 "전체 / 재고 부족" (admin만)
- segmented-control-active: "전체" 흰 pill. 하늘색: 1px #2b9fe0 테두리 (admin만)
- text-input: 모달 뒤 검색 "시약명 검색", 모달 안 school-name-confirm 입력 칸 (admin만)
- list-filter-button: 모달 뒤 "필터" (admin만)
- data-table: 데스크톱 전용. 모달 뒤 시약 표(42종 중 첫 페이지) (admin만)
- reagent-row: 모바일 전용. 모달 뒤 시약 행(시트에 가려지지 않은 윗부분만) (admin만)
- badge-low-stock: 모달 뒤 재고 부족 행 배지 그대로(#d6246a 채움, #ffffff label) (admin만)
- ex-modal-card: 시약 전체 삭제 확인 1개(#ffffff, 1px #e0e0e0 테두리, 여백 24, 그림자·딤 없음, 오른쪽 위 × 닫기 누름 영역 44 이상). 모바일 = tab-bar 위 시트(전폭, 위쪽 rounded 24), 데스크톱 = 가운데 폭 440, rounded 24. 위→아래: reagent-wipe 머리(경고 아이콘 + 제목) → body #141414 "목록·시약장·홈·재주문 알림에서 사라지고 되돌릴 수 없어요." → body #141414 "사용·입고 기록은 남아요." → (위 간격 24) school-name-confirm → 버튼 줄(위 간격 24, 1:1, 사이 8): 왼쪽 button-outline "닫기" + 오른쪽 button-primary "전체 삭제". '취소'가 두 번 서지 않게 왼쪽은 "닫기". 핑크·빨강·하늘색 없음 (admin만)
- reagent-wipe: 시약 전체 삭제 흐름의 머리(메뉴 항목 "시약 전체 삭제"가 연 모달의 제목 묶음). 모달 맨 위 한 줄: #141414 외곽선 경고 아이콘(삼각형 !, 24) + heading-3 #141414 "시약 42종을 모두 삭제할까요?". 메뉴 항목 모양은 page-more-menu 공통(이 프레임에서 메뉴는 닫힘). 핑크·빨강 없음 (admin만)
- school-name-confirm: 모달 안 학교명 확인(공통 모양). caption #707070 "확인을 위해 학교 이름 '샘플고등학교'를 입력하세요" → text-input 빈 값(placeholder "샘플고등학교" #adadad, 포커스 링 2px #141414). 아직 입력 전이라 "학교 이름이 달라요" 줄 없음 (admin만)
- button-outline: 모달 "닫기"(#ffffff, 1px #e0e0e0, 라벨 #141414, rounded 9999, 높이 44 이상) (admin만)
- button-primary: 모달 "전체 삭제" — 이 프레임 = 꺼짐(#e0e0e0 채움 + #707070 글자, rounded 9999, 높이 44 이상). 학교명이 맞으면 검정(#141414 채움, #ffffff 글자). 하늘색 없음 (admin만)
- ex-toast: 실행 뒤 "시약 42종을 삭제했어요"(이 프레임에는 그리지 않음) → 빈 목록 ex-empty-state-card. 하늘색: 완료 체크 아이콘 #2b9fe0 (admin만)
- tab-bar: 모바일 전용 하단 탭바 1개(공통 규격). 시트는 이 바 위쪽 선 위에 붙는다. 데스크톱에는 두지 않는다 (admin만)
- tab-item: 4개 "홈" · "관리" · "QR 스캔" · "기록". 활성 = "관리", "QR 스캔" 회색 '준비 중' (admin만)
### 반영한 레퍼런스
- https://uibowl.io/name/%EC%99%93%EC%84%AD?patterns=%EC%B7%A8%EC%86%8C%ED%95%98%EA%B8%B0&imgId=cmqt89aob001pjl044nphhj04
- https://uibowl.io/name/%EB%8B%A4%EA%B8%80%EB%A1%9C?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&patternName=%EC%9C%A0%ED%8A%9C%EB%B8%8C%20%EB%A7%81%ED%81%AC%20%EC%97%85%EB%A1%9C%EB%93%9C
- https://uibowl.io/name/%EC%85%94%ED%81%B4?patterns=%EC%B7%A8%EC%86%8C%ED%95%98%EA%B8%B0&imgId=cmrt4shpb0007l104b7hb2rnd

## 화면 10
사용 기록 내역. 학생·교사·admin 모두. 샘플고등학교 기록만. 승인본(runs/20261011-0813 화면 10) 그대로 — 사용일로 묶고 최신순, class-label, class-filter, deleted-reagent-tag, record-add — + 요청 9: ① 모바일 탭 라벨 '시약' → '관리'(이 화면 활성은 "기록" 그대로) ② 페이지 머리 맨 오른쪽 (admin) page-more-menu ⋯ → "기록 삭제"(상태 화면 10-record-wipe). 이 프레임은 교사 기준이라 ⋯는 그리지 않는다. 화면 10은 관리 아래가 아니라 manage-back 없음.
예시 상태(승인본 그대로): "전체", 기간 "최근 1개월", 반 "전체". 6건 — ① "10월 10일": 에탄올 · 페놀프탈레인 용액 · 수산화나트륨(교사 김OO · 14:05 · 1학년 2반 · 통합과학) ② "10월 8일": 염산(학생 이OO · 2학년 1반) / 과망가니즈산 칼륨(삭제된 시약 · 교사 박OO · 수업 없음) ③ "10월 7일": 질산은 · 통합과학 + "10월 8일에 기록". 데스크톱은 첫 행(에탄올) detail-drawer가 열린 상태.
모바일 활성 탭: "기록". 위→아래: nav-pill → 페이지 머리 줄(왼쪽 heading-4 "사용 기록 6건" + 오른쪽 record-add · (admin) page-more-menu ⋯) → segmented-control + 기간 선택 → 검색 → class-filter 줄 → 사용일 그룹 목록 → tab-bar.
데스크톱 배치: app-sidebar("기록" 현재) | 본문 = 페이지 머리(왼쪽 "기록" + "6건" / 오른쪽 검색 + record-add + (admin) page-more-menu ⋯) → 툴바(segmented-control "전체 / 내 기록" + 기간 드롭다운 + class-filter) → data-table(사용일 묶음 머리 행 + 기록 행, 열 "수업") → 페이지 번호 + 오른쪽 detail-drawer(기록 상세).
### 구성 요소
- app-sidebar: 데스크톱 전용. 공통 규격, 학교명 "샘플고등학교" + 역할별 메뉴 + nav-account-menu
- sidebar-item: 데스크톱 전용. 학생 6개 / 교사 9개 / admin 11개. 현재 = "기록", "QR 찾기" 비활성 '준비 중'
- nav-pill: 모바일 전용. "Lab_Stock" 워드마크 + 제목 "사용 기록 내역" + 현재 학교명 "샘플고등학교" + nav-account-menu ▾. ☰ 없음
- nav-account-menu: 모바일 = 학교명 옆 ▾, 데스크톱 = app-sidebar 맨 아래. "로그아웃" 1개. 하늘색 없음
- record-add: 페이지 머리 오른쪽 button-primary "기록 추가"(#141414 채움, #ffffff 글자, rounded 9999, 왼쪽 + 아이콘). 모바일 = 머리 줄 높이 44 작은 pill, 데스크톱 = 검색 text-input 오른쪽(사이 8). 누르면 빈 화면 4. 떠 있는 버튼·그림자 없음. 모든 역할. 하늘색 없음
- page-more-menu: 페이지 머리 맨 오른쪽 record-add 오른쪽(사이 8) ⋯(공통 모양, 모바일·데스크톱 같은 자리). 메뉴 항목 = record-wipe "기록 삭제". 이 프레임(교사)에는 그리지 않는다 — admin 프레임은 상태 화면 10-record-wipe (admin만)
- segmented-control: "전체 / 내 기록", 한 번에 하나. 데스크톱 = 툴바 왼쪽
- segmented-control-active: 선택 "전체" 흰 pill. 하늘색: 1px #2b9fe0 테두리(글자 #141414)
- text-input: 기간 선택 상자("최근 1개월" ▾)와 "시약명 검색"(#f0f0f0, rounded 16, 포커스 링 2px #141414). 하늘색: 검색·▾ 아이콘 #2b9fe0
- class-filter: 반 필터 button-pill-soft "반: 전체 ▾"(높이 44 이상). 모바일 = 검색 아래 줄 왼쪽, 데스크톱 = 툴바 기간 드롭다운 오른쪽. 이 프레임은 "전체"·닫힘. 하늘색: ▾ 아이콘 #2b9fe0
- class-label: 기록 행의 수업 표기 "{학년}학년 {반}반 · {수업명}", 있는 것만. 모바일 = 행 보조줄 아래 caption #707070, 데스크톱 = data-table 열 "수업"(없으면 "—" #adadad) + 드로어 "수업 | 값". 핑크·하늘색 없음
- deleted-reagent-tag: 과망가니즈산 칼륨 시약명 오른쪽 pill "삭제된 시약"(#f3f3f3 채움, label #141414), 시약명 #707070, 시약 상세 링크·› 없음. 시약 전체 삭제로 지운 시약도 같다. 핑크·하늘색 없음
- data-table: 데스크톱 전용. 열 = 사용일(정렬, 활성 ↓ #2b9fe0) · 시약명 · 수업 · 사용자 · 사용량 · 기록 시각. 사용일 묶음 머리 행. 선택 행(에탄올) #e6f4fc
- ex-data-table-cell: 모바일 기록 목록 — 사용일 그룹 헤더(caption #707070) 아래 행 = 시약명(title) + 보조줄 body-sm #707070 "교사 김OO · 14:05" + class-label + 오른쪽 사용량. 데스크톱 data-table 셀 chrome. 하늘색: 누른 행 #e6f4fc, 그룹 헤더 왼쪽 #2b9fe0 인디케이터
- detail-drawer: 데스크톱 전용 기록 상세(승인본 그대로). heading-3 "에탄올" + "50 mL" → "항목 | 값" 사용자 · 사용일 · 수업 · 메모 → msds-entry → 아래 고정 button-outline "닫기"
- ex-modal-card: 모바일 전용 기록 상세 시트(tab-bar 위, × 닫기). 이 프레임에서는 닫힘
- msds-entry: 상세 안 button-pill-soft "MSDS 보기 ›" → 화면 16. 학생·교사·admin 모두. 하늘색: › 아이콘 #2b9fe0
- button-pill-soft: class-filter 버튼, msds-entry 버튼
- button-outline: 상세 "닫기"
- ex-empty-state-card: 결과 0건 "아직 사용 기록이 없어요" + "기간이나 반을 바꿔 보세요"(이 프레임 숨김). 핑크 없음
- ex-toast: 기록 추가 뒤 "3개 시약 사용을 기록했어요", 'QR 스캔' 탭 "준비 중이에요"(이 프레임에는 그리지 않음)
- tab-bar: 모바일 전용 하단 탭바 1개(공통 규격). 데스크톱에는 두지 않는다. 하늘색: 활성 tab-item 아이콘 #2b9fe0만
- tab-item: "홈" · "관리" · "QR 스캔" · "기록" 4개. 활성 = "기록", "QR 스캔" 회색 '준비 중', "홈"·"관리" #707070
### 반영한 레퍼런스
- https://uibowl.io/name/%EC%91%A5%EC%91%A5%EC%B0%B0%EC%B9%B5?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&patternName=%EC%9D%BC%EA%B8%B0%2F%EC%88%98%EC%9C%A0%ED%85%80%20%ED%83%AD%20-%20%EC%88%98%EC%9C%A0%ED%85%80%20-%20%EB%82%B4%EC%97%AD%EC%82%AD%EC%A0%9C

## 상태 화면 10-record-wipe
기록 삭제(프레임 10-record-wipe-mobile · 10-record-wipe-desktop, 키스크린 10-record-wipe-desktop). admin만. 흐름: 페이지 머리 ⋯(page-more-menu) → 메뉴 "기록 삭제"(record-wipe) → 모바일 바텀시트 / 데스크톱 detail-drawer(짧은 폼), × 닫기 → 기간 고르기(record-wipe-range) → 지울 건수 미리보기(wipe-preview) → 학교명 확인(school-name-confirm) → "기록 N건 삭제" → ex-toast "기록 30건을 삭제했어요", 목록·홈 숫자·재주문 알림 바로 반영. 지금 재고 수량은 바뀌지 않는다. 0건이면 미리보기 "이 기간에 지울 기록이 없어요" + 버튼 꺼짐. 핑크·빨강 없음.
예시 상태: admin 정OO, 화면 10에서 ⋯ → "기록 삭제"를 고른 직후 입력을 마친 상태 — 범위 "이 날짜 이전", 날짜 "2026-09-01"(그날 기록은 남음) → 미리보기 "사용 기록 24건 · 입고 기록 6건을 지워요" → 학교명 "샘플고등학교" 정확히 입력 → button-primary "기록 30건 삭제" 켜짐(검정). 뒤 화면 10 목록은 그대로(딤 없음), 데스크톱은 기록 상세 드로어 대신 이 드로어가 열림(표 선택 행 없음).
모바일 활성 탭: "기록". 위→아래: nav-pill → 페이지 머리 줄("사용 기록 6건" + record-add + ⋯ 누른 상태) → 뒤 목록 윗부분 → ex-modal-card = tab-bar 위 높은 바텀시트(머리 record-wipe + × → record-wipe-range → wipe-preview → school-name-confirm → 시트 맨 아래 고정 button-primary 전폭, 안에서 스크롤) → tab-bar.
데스크톱 배치: app-sidebar("기록" 현재, admin 11개) | 본문 = 화면 10 그대로(페이지 머리 + 툴바 + data-table, 페이지 머리 ⋯ 누른 상태 — 드로어 아래) + 오른쪽 detail-drawer 480 = 기록 삭제 폼(위→아래 record-wipe 머리 → record-wipe-range → wipe-preview → school-name-confirm, 아래 고정 줄 button-primary 전폭).
### 구성 요소
- app-sidebar: 데스크톱 전용. 공통 규격, 학교명 "샘플고등학교" + admin 메뉴 + "정OO · admin" + nav-account-menu (admin만)
- sidebar-item: 데스크톱 전용. admin 11개. 현재 = "기록", "QR 찾기" 비활성 '준비 중' (admin만)
- nav-pill: 모바일 전용. "Lab_Stock" 워드마크 + 제목 "사용 기록 내역" + 현재 학교명 "샘플고등학교" + nav-account-menu ▾ (admin만)
- nav-account-menu: 닫힌 ▾ (admin만)
- record-add: 시트·드로어 뒤 페이지 머리 "기록 추가" 그대로 (admin만)
- page-more-menu: 페이지 머리 맨 오른쪽 ⋯(공통 모양). 방금 눌러 버튼 뒤 #e6f4fc 원, 메뉴는 닫힘(데스크톱은 드로어에 가려짐). 하늘색: 누른 상태 원 #e6f4fc (admin만)
- segmented-control: 뒤 화면 "전체 / 내 기록", 그리고 record-wipe-range 안 "전체 | 이 날짜 이전"(#f3f3f3 트랙, rounded 9999) (admin만)
- segmented-control-active: 뒤 화면 "전체", record-wipe-range "이 날짜 이전" 흰 pill. 하늘색: 1px #2b9fe0 테두리(글자 #141414) (admin만)
- text-input: 뒤 화면 기간 상자·검색, record-wipe-range 날짜 칸, school-name-confirm 입력 칸(#f0f0f0, rounded 16, 포커스 링 2px #141414) (admin만)
- class-filter: 뒤 화면 "반: 전체 ▾" 그대로 (admin만)
- class-label: 뒤 화면 기록 행 수업 표기 그대로 (admin만)
- data-table: 데스크톱 전용. 드로어 뒤 화면 10 기록 표(선택 행 없음) (admin만)
- ex-data-table-cell: 모바일 시트 뒤 기록 행, 데스크톱 표 셀 chrome (admin만)
- ex-modal-card: 모바일 전용 기록 삭제 바텀시트 1개(#ffffff, 위쪽 rounded 24·아래 0, 1px #e0e0e0, 딤·그림자 없음, 여백 16·24, 오른쪽 위 × 닫기 누름 영역 44 이상, tab-bar 위쪽 선 위에 붙고 nav-pill 아래까지 높게). 안 순서 = record-wipe → record-wipe-range → wipe-preview → school-name-confirm → 맨 아래 고정 button-primary. 핑크·빨강 없음 (admin만)
- detail-drawer: 데스크톱 전용 기록 삭제 폼 드로어 1개(폭 480, 높이 900, #ffffff, 왼쪽 1px #f0f0f0 선, 여백 24, 오른쪽 위 × 닫기). 안 순서는 모바일 시트와 같고 아래 고정 줄(위 1px #f0f0f0) button-primary 전폭 (admin만)
- record-wipe: 기록 삭제 흐름의 머리(메뉴 항목 "기록 삭제"가 연 시트·드로어의 제목 묶음). #141414 외곽선 경고 아이콘(삼각형 !, 24) + heading-3 #141414 "기록 삭제". 메뉴 항목 모양은 page-more-menu 공통(이 프레임에서 메뉴는 닫힘). 핑크·빨강 없음 (admin만)
- record-wipe-range: 지울 기간 묶음. 라벨 body #141414 "지울 기간" → segmented-control "전체 | 이 날짜 이전"(기본·예시 "이 날짜 이전") → 날짜 text-input "2026-09-01"(오늘 이후 못 고름, 오른쪽 달력 아이콘) → caption #707070 "이 날짜 기록은 남아요". "전체"를 고르면 날짜 칸이 숨는다. 하늘색: 선택 칸 테두리, 달력 아이콘 (admin만)
- wipe-preview: 미리보기 줄 1개(#f3f3f3, rounded 16, 여백 12·16): body #141414 "사용 기록 24건 · 입고 기록 6건을 지워요" + 아래 body-sm #707070 "지금 재고 수량은 그대로예요. 수업 정보도 함께 지워져요." 0건이면 body #141414 "이 기간에 지울 기록이 없어요" 한 줄 + 실행 버튼 꺼짐. 핑크·하늘색 없음 (admin만)
- school-name-confirm: 학교명 확인(공통 모양). caption #707070 "확인을 위해 학교 이름 '샘플고등학교'를 입력하세요" → text-input 값 "샘플고등학교"(#141414, 정확히 일치 — "학교 이름이 달라요" 줄 없음) (admin만)
- button-primary: "기록 30건 삭제"(검정 — #141414 채움, #ffffff 글자, rounded 9999, 높이 44 이상, 건수 = 사용 + 입고). 학교명이 다르거나 0건이면 꺼짐(#e0e0e0 채움 + #707070 글자). 모바일 = 시트 맨 아래 전폭, 데스크톱 = 드로어 아래 고정 줄 전폭. 뒤 화면 record-add도 button-primary. 하늘색 없음 (admin만)
- ex-toast: 실행 뒤 "기록 30건을 삭제했어요"(이 프레임에는 그리지 않음). 하늘색: 완료 체크 아이콘 #2b9fe0 (admin만)
- tab-bar: 모바일 전용 하단 탭바 1개(공통 규격). 시트는 이 바 위쪽 선 위에 붙는다. 데스크톱에는 두지 않는다 (admin만)
- tab-item: 4개 "홈" · "관리" · "QR 스캔" · "기록". 활성 = "기록", "QR 스캔" 회색 '준비 중' (admin만)
### 반영한 레퍼런스
- https://uibowl.io/website/%EB%A6%AC%EB%94%94?patterns=%EB%82%B4%EC%97%AD&imgId=cmuq7e6jd000wjs046c714kre
- https://uibowl.io/website/%EC%82%AC%EB%B0%A9%EB%84%B7?patterns=%ED%8E%B8%EC%A7%91%C2%B7%EC%88%98%EC%A0%95%ED%95%98%EA%B8%B0&imgId=cmu4rqsym001rl504326axccl
- https://uibowl.io/website/%EC%9C%84%EC%8B%9C%EC%BC%93?patterns=%ED%95%84%ED%84%B0&imgId=cmunb6fr3003ul2040dnbgwff
- https://uibowl.io/name/%EC%91%A5%EC%91%A5%EC%B0%B0%EC%B9%B5?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&patternName=%EC%9D%BC%EA%B8%B0%2F%EC%88%98%EC%9C%A0%ED%85%80%20%ED%83%AD%20-%20%EC%88%98%EC%9C%A0%ED%85%80%20-%20%EB%82%B4%EC%97%AD%EC%82%AD%EC%A0%9C
- https://uibowl.io/website/%EB%8B%B9%EA%B7%BC%20%EB%B9%84%EC%A6%88%EB%8B%88%EC%8A%A4?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&imgId=cmso6f8zf000rl704l4qn0f5w

## 화면 13
홈. 로그인 후 첫 화면, 학생·교사·admin 모두. 승인본(runs/20261012-0939 S4 v22 화면 13) 그대로 — quick-action · home-summary · (교사·admin) reorder-alert-card · (교사·admin) sensor-alert-tile · 최근 사용 기록 — + 요청 9: ① 모바일 nav-pill에서 mobile-menu-button ☰ 없앰(13-menu 상태 없음) → 머리 = 워드마크 + 학교명 ▾ 얇은 한 줄 ② 탭 라벨 '시약' → '관리'. quick-action은 그대로(관리 화면이 생겨도 바뀌지 않음). home-summary·reorder-alert-card의 "… N건 ›" 연결은 그대로 관리 아래 화면(2·6)으로 간다.
예시 상태: 교사 김OO. 전체 시약 42종, 재고 부족 3종, MSDS 없는 시약 4종, 시약장 2개(칸 16개 중 지정 14 · 미지정 2), 재주문 알림 3건, 최근 사용 기록 3줄, 센서 고장 1 · 점검 필요 1.
모바일 활성 탭: "홈". 위→아래: nav-pill(워드마크 + 학교명 ▾) → quick-action(교사 3칸 2+1) → home-summary ① 재고 요약(맨 아래 sensor-alert-tile 줄) → reorder-alert-card → home-summary ② 시약장 요약 → 최근 사용 기록 카드 → tab-bar.
데스크톱 배치: app-sidebar("홈" 현재) | 본문 = 페이지 머리(왼쪽 heading-2 "샘플고등학교" + "오늘 10월 13일 · 전체 시약 42종" / 오른쪽 quick-action 버튼 줄) → 숫자 타일 줄 "지금 처리할 것"(교사·admin = 재고 부족 3 · 재주문 알림 3 · MSDS 없는 시약 4 · 고장·점검 필요 센서 2 / 학생 = 재고 부족 3) → 3열 위젯 격자(최근 사용 기록 data-table 2칸 폭 · 재고 부족 · 시약장 요약).
### 구성 요소
- app-sidebar: 데스크톱 전용. 공통 규격, 학교명 "샘플고등학교" + 역할별 메뉴 + nav-account-menu
- sidebar-item: 데스크톱 전용. 학생 6개 / 교사 9개 / admin 11개. 현재 = "홈", "QR 찾기" 비활성 '준비 중'
- nav-pill: 모바일 전용. "Lab_Stock" 워드마크 + 현재 학교명 "샘플고등학교" + nav-account-menu ▾. ☰(mobile-menu-button) 없음, 학교 선택·전환 없음
- nav-account-menu: 모바일 = 학교명 옆 ▾, 데스크톱 = app-sidebar 맨 아래. "로그아웃" 1개. 하늘색 없음
- quick-action: 역할별 작업 바로가기(승인본 그대로). 모바일 = 교사 3칸 "사용 기록 입력" · "입고"(stock-intake 진입) · "시약장 설정", admin 3칸 "입고" · "사용자 관리"(user-manage 진입) · "시약장 설정", 2+1. 학생 2칸 "사용 기록 입력" · "시약장 보기". 데스크톱 = 페이지 머리 오른쪽 버튼 줄. 하늘색: 모바일 아이콘 #2b9fe0 + 바탕 #e6f4fc
- home-summary: 모바일 = 요약 카드 2장(#ffffff, 1px #f0f0f0, rounded 24, 여백 24) ① 재고 요약 "재고 부족 3개" + 부족 시약 칩 + "전체 시약 42종"(+ 교사·admin 카드 맨 아래 sensor-alert-tile 줄) ② 시약장 요약(막대 + "칸 16개 중 지정 14 · 미지정 2"). 데스크톱 = 숫자 타일 "재고 부족 3" · (교사·admin) "MSDS 없는 시약 4" + 위젯 "재고 부족"·"시약장 요약". 하늘색: 막대 지정 구간, › 아이콘
- sensor-alert-tile: 고장·점검 필요 센서 2. 0개면 그리지 않는다. 모바일 = home-summary ① 카드 맨 아래 한 줄(센서 아이콘 #141414 + body "고장·점검 필요 센서 2" + ›, → 화면 17 상태 필터), 데스크톱 = "지금 처리할 것" 4번째 숫자 타일. 무채색. 하늘색: › 아이콘만 (교사·admin만)
- badge-low-stock: 재고 요약 개수 배지 "3", reorder-alert-card 안 "재고 부족"(#d6246a 채움, #ffffff label). 하늘색 없음
- reorder-alert-card: "재주문 알림" 카드(#f3f3f3, rounded 24). 모바일 = heading-4 "재주문 알림" + badge-low-stock + "3건 ›" + "필요량보다 적은 시약이 3종 있어요", 데스크톱 = 숫자 타일 줄의 타일 1개. 판매처 연결 버튼 없음. 하늘색 없음 (교사·admin만)
- data-table: 데스크톱 전용 "최근 사용 기록" 위젯(2칸 폭). 열 = 사용일 · 시약명 · 사용자 · 사용량, 3행, 머리 오른쪽 "전체 보기 ›"
- reagent-row: 모바일 최근 사용 기록 카드 안 3줄. 누르면 화면 10. 하늘색: 누른 행 #e6f4fc
- button-pill-soft: 모바일 "더 보기 ›", reorder-alert-card "3건 ›"(교사·admin만), 데스크톱 위젯 "전체 보기 ›"
- button-outline: 데스크톱 quick-action 버튼 줄 보조 버튼
- button-primary: 데스크톱 quick-action 버튼 줄 마지막 버튼(교사·admin "입고", 학생 "사용 기록 입력"). 하늘색 없음
- ex-empty-state-card: 시약장 0개 / 최근 사용 기록 0건 안내(이 프레임 숨김)
- ex-toast: 권한 없는 주소로 들어왔을 때 한 번(13-no-access 승인본), 'QR 스캔' 탭·'QR 찾기' 메뉴 "준비 중이에요". 이 프레임에는 그리지 않는다
- tab-bar: 모바일 전용 하단 탭바 1개(공통 규격). 데스크톱에는 두지 않는다. 하늘색: 활성 tab-item 아이콘 #2b9fe0만
- tab-item: "홈" · "관리" · "QR 스캔" · "기록" 4개. 활성 = "홈", "QR 스캔" 회색 '준비 중', "관리"(격자 아이콘)·"기록" #707070. 역할별 작업은 tab-item으로 두지 않는다
### 반영한 레퍼런스
- https://uibowl.io/name/%ED%8E%98%EC%9D%B4%EC%9B%8C%ED%81%AC?patterns=%EB%A9%94%EC%9D%B8&imgId=cmtzo55qv002rl7047rsl7n07
- https://uibowl.io/name/%ED%8E%98%EC%9D%B4%ED%9E%88%EC%96%B4?patterns=%EB%A9%94%EC%9D%B8&imgId=cmnfmxnhh0003l8045z9h1r15
- https://uibowl.io/name/%ED%97%A4%EC%9D%B4%EC%98%81%20%EC%BA%A0%ED%8D%BC%EC%8A%A4?patterns=%EB%A9%94%EC%9D%B8&imgId=cmmbj8sqh0004lh048k4kbkqd
- https://uibowl.io/name/Kia?patterns=%EB%A9%94%EC%9D%B8&imgId=cmpur0a3g000dl504qp9o8f4s

## 화면 17
센서. 무선 센서·현미경 보유 관리만 — 측정값·대여 없음. 학생·교사·admin 모두(학생은 보기만). 샘플고등학교 센서만(N1). 승인본(S4-screens-v23 696:2, 설계 runs/20261012-1155 화면 17) 그대로 + 요청 9: ① 모바일 inventory-switch "시약 | 센서" 없앰(그 아래 segmented-control도 함께 없어짐) ② 모바일 nav-pill ☰ 없앰 → 맨 왼쪽 manage-back "‹ 관리" ③ 탭 라벨 '시약' → '관리', 활성 = "관리". 검색·목록·하단 동작·행 카드 구조는 그대로(머리만 교체).
예시 상태(17-mobile · 17-desktop): 센서 7개, 필터 없음, 이름순. 교사 기준, 드로어·등록 시트·필터 시트 닫힘.
모바일 활성 탭: "관리". 위→아래: nav-pill(‹ 관리 + 학교명 ▾) → 페이지 머리 줄(왼쪽 heading-4 "센서 7개" + 오른쪽 (교사·admin) list-select-toggle "선택" · sensor-add "등록") → 검색 줄(text-input + list-filter-button) → sensor-list(sensor-row 카드 7장, 사이 12) → tab-bar. 좌우 여백 16.
데스크톱 배치: app-sidebar("센서" 현재) | 본문 = 페이지 머리(왼쪽 heading-2 "센서" + caption "7개" / 오른쪽 검색 text-input 폭 320 + list-filter-button + (교사·admin) list-select-toggle + (교사·admin) sensor-doc-add "서류로 등록" + (교사·admin) sensor-add "센서 등록", 사이 8) → sensor-list = data-table(열 이름 · 종류 · 회사 · 모델 · 수량 · 보관 위치 · 상태, 7행) → 행을 누르면 오른쪽 detail-drawer. 승인본 그대로.
### 구성 요소
- app-sidebar: 데스크톱 전용. 공통 규격, 워드마크 + 학교명 "샘플고등학교" + 역할별 메뉴 + 이름·역할·nav-account-menu
- sidebar-item: 데스크톱 전용. 학생 6개 / 교사 9개 / admin 11개. 현재 = "센서"("시약" 바로 아래), "QR 찾기" 비활성 '준비 중'
- nav-pill: 모바일 전용. 관리 아래 화면 머리 — 맨 왼쪽 manage-back "‹ 관리" + 오른쪽 현재 학교명 "샘플고등학교" + nav-account-menu ▾. 워드마크·☰·inventory-switch 없음. 학교 전환 없음
- manage-back: 모바일 전용. nav-pill 맨 왼쪽 link "‹ 관리"(‹ 아이콘 + body #141414, 누름 영역 44 이상) → 화면 18. 화면 2와 같은 머리. 데스크톱에는 두지 않는다. 하늘색: ‹ 아이콘 #2b9fe0
- nav-account-menu: 모바일 = 학교명 옆 ▾, 데스크톱 = app-sidebar 맨 아래. "로그아웃" 1개. 하늘색 없음
- sensor-list: 센서 목록 1개. 머리 "센서 7개". 모바일 = sensor-row 카드 세로 쌓기(사이 12). 데스크톱 = data-table. 이름순 기본. 검색은 이름·모델
- sensor-row: 센서 1개(승인본 그대로). 모바일 = 카드(#f3f3f3, rounded 16, 여백 16): 1줄 이름(title #141414) + 오른쪽 위 sensor-status-badge / 2줄 caption #707070 "온도 · 파스코 · PS-3201" / 3줄 body-sm #141414 "3개 · 과학실 뒤 선반"(시약장 칸이면 cabinet-number 원 + "1번 시약장 · 좌 1단"). 데스크톱 = data-table 한 행. 하늘색: 모바일 › 아이콘 #2b9fe0, 누른 행 #e6f4fc
- sensor-status-badge: 상태 배지(무채색). 고장 = #141414 채움 pill + #ffffff label, 점검 필요 = #f3f3f3 pill(카드 위에서는 #ffffff 채움 + 1px #e0e0e0 테두리) + #141414 label, 정상 = 채움 없이 #707070 "정상". 예시 = 운동 센서 고장 · 무선 pH 센서 점검 필요 · 나머지 정상. 핑크·하늘색 없음
- cabinet-number: 무선 pH 센서 보관 위치 앞 작은 원 "1"(#ffffff, 1px #e0e0e0, label #141414)
- data-table: 데스크톱 전용. sensor-list 표 — 열 = 이름(정렬, 활성 ↑ #2b9fe0) · 종류 · 회사 · 모델 · 수량(정렬) · 보관 위치 · 상태(정렬). 7행. 선택 행 #e6f4fc. rounded 16 컨테이너, 1px #f0f0f0
- ex-data-table-cell: data-table 머리행(caption #707070)·셀(body-sm) chrome, 행 구분 1px #f0f0f0
- text-input: 검색 "센서 이름·모델 검색"(#f0f0f0, rounded 16, 포커스 링 2px #141414). 하늘색: 검색 아이콘 #2b9fe0
- list-filter-button: 검색 오른쪽 button-pill-soft "필터"(필터 아이콘, 높이 44 이상). 적용 개수 pill은 이 프레임 숨김. 하늘색: 필터 아이콘 #2b9fe0
- list-filter-sheet: 센서 필터(이 프레임 닫힘 — 연 모양은 승인본 17-filter: 종류 sensor-type-group 4줄 접힘 → 회사 → 상태 → "초기화" / "{N}개 보기")
- list-select-toggle: 선택 모드 진입. 모바일 = 머리 줄 button-pill-soft "선택"(sensor-add 왼쪽, 사이 8), 데스크톱 = list-filter-button 오른쪽 button-outline "선택". 핑크 없음 (교사·admin만)
- sensor-doc-add: 서류로 등록 진입. 데스크톱 = 페이지 머리 sensor-add 바로 왼쪽 button-outline "서류로 등록"(왼쪽 서류 아이콘 #141414). 모바일 = sensor-add "등록" 시트의 첫 줄 "서류로 등록" + caption #707070 "품의서·영수증을 AI가 읽어요"(이 프레임에서는 시트 닫힘). 하늘색 없음 (교사·admin만)
- sensor-add: 센서 등록 진입. 데스크톱 = 페이지 머리 맨 오른쪽 button-primary "센서 등록" → detail-drawer sensor-form. 모바일 = 머리 줄 맨 오른쪽 button-pill-soft "등록"(왼쪽 + 아이콘, 높이 44) → 작은 바텀시트 2줄 "서류로 등록" / "직접 입력". 이 프레임에서는 시트 닫힘. 하늘색 없음 (교사·admin만)
- detail-drawer: 데스크톱 전용. 센서 상세·등록·수정 자리(이 프레임 닫힘). 폭 480, #ffffff, 왼쪽 1px #f0f0f0 선, × 닫기
- button-pill-soft: 모바일 list-select-toggle "선택"·sensor-add "등록"(교사·admin만), list-filter-button "필터"
- button-outline: 데스크톱 list-select-toggle "선택"·sensor-doc-add "서류로 등록" (교사·admin만)
- button-primary: 데스크톱 sensor-add "센서 등록"(#141414 채움, #ffffff 글자, rounded 9999, 높이 44 이상). 하늘색 없음 (교사·admin만)
- ex-empty-state-card: 검색·필터 결과 0건 "조건에 맞는 센서가 없어요" + button-outline "필터 지우기"(이 프레임 숨김). 핑크 없음
- ex-toast: 서류로 등록 뒤 "센서 3개를 등록했어요", 'QR 스캔' 탭 "준비 중이에요"(이 프레임에는 그리지 않음)
- tab-bar: 모바일 전용 하단 탭바 1개(공통 규격). 데스크톱에는 두지 않는다. 하늘색: 활성 tab-item 아이콘 #2b9fe0만
- tab-item: "홈" · "관리" · "QR 스캔" · "기록" 4개. 활성 = "관리"(센서는 관리 아래 화면), "QR 스캔" 회색 '준비 중'
### 반영한 레퍼런스
- https://uibowl.io/website/%EB%8B%B9%EA%B7%BC%20%EB%B9%84%EC%A6%88%EB%8B%88%EC%8A%A4?patterns=%EC%83%81%EC%84%B8%EC%A0%95%EB%B3%B4%20%28PDP%29&imgId=cmso6dgem00ualf04cqgg6fh8
- https://uibowl.io/name/%ED%8E%98%EC%9D%B4%EC%9B%8C%ED%81%AC?patterns=%EB%A9%94%EB%89%B4&patternName=%EA%B0%84%ED%8E%B8%EB%A9%94%EB%89%B4%20-%20%EA%B1%B0%EB%9E%98%EC%B2%98
- https://uibowl.io/name/Kia?patterns=%EB%82%B4%EC%97%AD&imgId=cmpuohezz0015k104h5xybl51
- https://uibowl.io/name/%ED%8E%98%EC%9D%B4%ED%9E%88%EC%96%B4?patterns=%EB%A9%94%EC%9D%B8&imgId=cmnfmxdij001fl204l8u0mu8b

## 화면 18
관리(새 화면, 모바일 전용, 키스크린 18-mobile). 하단 탭 '관리'의 첫 화면 — 홈과 분리된 탭 화면이라 되돌아가기 없음. 학생·교사·admin 모두 들어오고 역할에 따라 묶음 자체가 숨는다: 재고(시약 · 센서 · 시약장) = 모든 역할, 입고·주문(입고 · 실험 매뉴얼 · 재주문 알림) = 교사·admin, 학교(사용자 · 판매처) = admin. 행을 누르면 그 화면으로(시약 → 2, 센서 → 17, 시약장 → 11, 입고 → 7, 실험 매뉴얼 → 5, 재주문 알림 → 6, 사용자 → 8, 판매처 → 9 — 모두 머리 "‹ 관리", 탭 '관리' 활성). 홈·기록·QR 스캔은 각자 탭이라 목록에 없다. 전체 삭제·기록 삭제 진입은 이 화면에 두지 않는다(화면 2·10 머리 ⋯).
예시 상태: admin 정OO, 묶음 3개·행 8개 모두 보임. 요약 caption(예시 값, 샘플고등학교 기준): 시약 "시약 42종 · 재고 부족 3" · 센서 "센서 7개 · 고장 1" · 시약장 "시약장 2개" · 입고 (요약 없음 — 이름만) · 실험 매뉴얼 (요약 없음 — 이름만) · 재주문 알림 "알림 3건" · 사용자 "학생 3 · 교사 1 · admin 1" · 판매처 "4곳".
모바일 활성 탭: "관리". 위→아래: nav-pill(워드마크 + 학교명 ▾) → 페이지 제목 heading-2 "관리"(좌우 여백 16, 위 24) → manage-list(묶음 "재고" 제목 → 행 3 → 1px #f0f0f0 선 → 묶음 "입고·주문" 제목 → 행 3 → 1px #f0f0f0 선 → 묶음 "학교" 제목 → 행 2, 넘치면 안에서 스크롤) → tab-bar.
데스크톱 배치: 모바일 전용 — 데스크톱은 app-sidebar
### 구성 요소
- nav-pill: 모바일 전용. 탭 첫 화면 머리 — "Lab_Stock" 워드마크 + 현재 학교명 "샘플고등학교" + nav-account-menu ▾. ☰·manage-back 없음. 학교 선택·전환 없음
- nav-account-menu: 학교명 옆 ▾. "로그아웃" 1개(계정 동작은 여기에만). 하늘색 없음
- manage-list: 관리 목록 1개. 페이지 제목 heading-2 #141414 "관리" 아래, 묶음 3개 세로. 묶음 = 제목 caption #707070(좌우 여백 16, 위 24·아래 8) + manage-row들. 묶음 사이 1px #f0f0f0 선(전폭). ① "재고" — 시약 · 센서 · 시약장(모든 역할) ② "입고·주문" — 입고 · 실험 매뉴얼 · 재주문 알림(교사·admin, 학생은 묶음째 숨김) ③ "학교" — 사용자 · 판매처(admin, 교사·학생은 묶음째 숨김). 배경 #ffffff. 핑크·하늘색 없음
- manage-row: 행 1개(예시 8개). 높이 56, 전폭, 사각(rounded 0), #ffffff, 좌우 여백 16, 행 사이 선 없음(묶음 사이만). 왼쪽 아이콘 24 #141414 → 사이 12 → 이름 title #141414 + 바로 아래 요약 caption #707070(요약 없는 항목은 이름만, 세로 가운데) → 오른쪽 끝 › #707070. 숫자는 무채색 글자만 — "재고 부족 3"·"고장 1"도 #707070 글자, 핑크·하늘색 배지 없음. 누른 행만 잠깐 #f3f3f3. 줄 전체가 누름 영역(44 이상). 아이콘: 시약 = 시약병, 센서 = 센서, 시약장 = 수납장, 입고 = 상자, 실험 매뉴얼 = 문서, 재주문 알림 = 종, 사용자 = 사람 둘, 판매처 = 가게
- ex-toast: 'QR 스캔' 탭을 누르면 "준비 중이에요"(이 프레임에는 그리지 않음)
- tab-bar: 모바일 전용 하단 탭바 1개(공통 규격). 하늘색: 활성 tab-item 아이콘 #2b9fe0만
- tab-item: "홈" · "관리" · "QR 스캔" · "기록" 4개. 활성 = "관리"(격자 아이콘 #2b9fe0, 라벨 #141414), "QR 스캔" 회색 '준비 중', "홈"·"기록" #707070
### 반영한 레퍼런스
- https://uibowl.io/website/%EC%82%AC%EB%B0%A9%EB%84%B7?patterns=%EB%A9%94%EB%89%B4&imgId=cmu4rpvqh000cjy04yej53zvj
- https://uibowl.io/name/%ED%8E%98%EC%9D%B4%ED%9E%88%EC%96%B4?patterns=%EB%A9%94%EC%9D%B8&imgId=cmnfmxdij001fl204l8u0mu8b
- https://uibowl.io/name/%ED%8E%98%EC%9D%B4%EC%9B%8C%ED%81%AC?patterns=%EB%A9%94%EC%9D%B8&imgId=cmtzo55qv002rl7047rsl7n07
- https://uibowl.io/website/%EC%9E%94%EB%94%94?patterns=%EB%8C%80%EC%8B%9C%EB%B3%B4%EB%93%9C&imgId=cmpz4uprc0003ie04h1ia0clk

## 둘러보기 화면 18
둘러보기 관리(프레임 18-guest-mobile만 — 모바일 전용 화면이라 desktop 없음). 데모 학교 읽기 전용. 학교명은 "데모 학교" 1종만(샘플고등학교 등 실제 학교명 없음). manage-list = "재고" 묶음에 시약 · 센서 두 줄만(요약 = 데모 값), 시약장 행과 "입고·주문"·"학교" 묶음은 숨김. 시약 → 둘러보기 2, 센서 → 둘러보기 17. 탭 '관리' 활성, QR 스캔·기록 tab-item에 guest-lock(2). 잠긴 탭을 누르면 ex-toast "가입하면 쓸 수 있어요". 이 화면에는 쓰기 동작이 없어 탭 밖 잠금은 없다.
예시 상태: 둘러보기 사용자, 시약 "시약 24종 · 재고 부족 2", 센서 "센서 5개 · 고장 1".
모바일 위→아래: nav-pill(워드마크 + "데모 학교") → guest-banner → 페이지 제목 heading-2 "관리" → manage-list(묶음 "재고" 제목 → 행 2) → tab-bar.
### 구성 요소
- nav-pill: 모바일 전용. "Lab_Stock" 워드마크 + 학교명 "데모 학교". nav-account-menu 없음(로그인 전). ☰·manage-back 없음
- guest-banner: nav-pill 아래 전폭 띠 1개(#e6f4fc 채움, rounded 0, 여백 12·16): body-sm #141414 "둘러보는 중 — 가입하면 우리 학교 데이터로 시작해요" + 끝에 작은 button-primary "가입하기"(→ 화면 14). 하늘색: 띠 채움 #e6f4fc
- button-primary: guest-banner 안 "가입하기"(#141414 채움, #ffffff 글자, rounded 9999, 높이 44 이상). 하늘색 없음
- manage-list: "재고" 묶음 1개만(제목 caption #707070 "재고") — 화면 18과 같은 모양. "입고·주문"·"학교" 묶음 없음
- manage-row: 2개 — 시약(시약병 아이콘 #141414 + "시약" + caption "시약 24종 · 재고 부족 2" + ›) · 센서(센서 아이콘 + "센서" + caption "센서 5개 · 고장 1" + ›). 시약장 행 숨김. 높이 56, 사각, #ffffff, 숫자 무채색. 핑크·하늘색 없음
- guest-lock: tab-bar 안 2개 — "QR 스캔"·"기록" tab-item 아이콘 오른쪽 위 작은 자물쇠(#707070). 탭 밖 잠금 없음
- ex-toast: 잠긴 탭을 누르면 "가입하면 쓸 수 있어요"(이 프레임에는 그리지 않음). 핑크 없음
- tab-bar: 모바일 전용 하단 탭바 1개(공통 규격)
- tab-item: "홈" · "관리" · "QR 스캔" · "기록" 4개. 활성 = "관리", "QR 스캔"·"기록" = guest-lock(아이콘·라벨 #707070)
숨김(둘러보기 0개, rules.json guest.hidden_components): page-more-menu · reagent-wipe · record-wipe · school-name-confirm · user-manage · stock-intake · reagent-register · manual-upload · vendor-register · vendor-link · reorder-alert-card · cabinet-edit · sensor-add · sensor-doc-add 등 — manage-row 시약장·입고·실험 매뉴얼·재주문 알림·사용자·판매처 행도 그리지 않는다.
### 반영한 레퍼런스
- https://uibowl.io/website/%EC%9E%94%EB%94%94?patterns=%EB%8C%80%EC%8B%9C%EB%B3%B4%EB%93%9C&imgId=cmpz4uprc0003ie04h1ia0clk
- https://uibowl.io/website/%EC%82%AC%EB%B0%A9%EB%84%B7?patterns=%EB%A9%94%EB%89%B4&imgId=cmu4rpvqh000cjy04yej53zvj

## 역할별 노출
앱 전체(로그인 후 화면) 기준 개수. runs/20261012-1155 승인 표를 기준으로 이번 변경을 반영했다. 같은 화면의 상태 화면·모바일·데스크톱에 다시 나오는 같은 컴포넌트는 그 화면 1개로 센다(예: 화면 2의 page-more-menu는 2·2-wipe, 모바일·데스크톱에 나와도 1).
이번 변경(admin만 — 학생 R5·교사 R8 = 0):
- page-more-menu = 화면 2 1 + 화면 10 1 → admin 2. reagent-wipe = 화면 2(2-wipe) 1 → admin 1. record-wipe = 화면 10(10-record-wipe) 1 → admin 1.
- manage-row·manage-list·manage-back은 모든 역할에 있고(묶음 노출만 역할별) rules.json roles 대상이 아니어서 표에 넣지 않는다. 관리 탭의 "입고"·"사용자"·"판매처"·"재주문 알림"·"실험 매뉴얼" 행은 화면 이동 링크이고 stock-intake·user-manage·vendor-register·reorder-alert-card·manual-upload 컴포넌트가 아니다 — 해당 행 개수는 바뀌지 않는다.
- school-name-confirm·record-wipe-range·wipe-preview는 admin만 여는 모달·시트 안이라 학생·교사 노출 0이며 rules.json roles 대상이 아니어서 표에 넣지 않는다.
- mobile-menu-button·mobile-menu-sheet·inventory-switch는 없앴다(roles 대상 아님, 개수 영향 없음).
- 둘러보기(18-guest)는 R 규칙 대상이 아니어서 표에 넣지 않는다.
msds-entry = 화면 3 1 + 화면 10 상세 1(학생·교사·admin 모두 2, R4). 나머지 행은 runs/20261012-1155 값 그대로.

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
