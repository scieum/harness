# S2 설계 — run 20261008-0936

대상 화면: 2·3·4·5·6·7·8·9·10·11·12·13·16 · 상태 화면 없음 · 학교: 샘플고등학교 (input.json)
변경 사유: ① 2026-10-08 사용자 결정 A — 데스크톱을 넓힌 휴대폰이 아닌 웹앱으로 재구성(왼쪽 app-sidebar · data-table · 오른쪽 detail-drawer, 무거운 작업은 페이지). ② 요청 5-1 — 새 화면 16 MSDS 요약. ③ 요청 5-2 — 개발 기준 맞춤(재주문 카드 문구, 사용자 관리 머리 인원 줄, 판매처 행 이름+연락처, 자동 기준 캡션 두 문구).
근거: docs/design.md "Desktop shell"·"MSDS summary"·reorder-alert-card·ex-modal-card, docs/story-service.md 결정 사항 2026-10-08 두 행("MSDS 요약"·"개발 기준 맞춤"), harness/rules.json(roles R1~R7, screens_required, desktop_shell, msds_summary, reorder.auto·card_text, app_exceptions, tab_bar, colors), research/s1-adopt.md.
모바일 기준 설계(수정하지 않고 옮김): 화면 2·4·10 = runs/20261007-0744, 화면 3·7 = runs/20261007-0002, 화면 5·6·8·9 = runs/20261007-0848, 화면 11·12·13 = runs/20261006-1223. 모바일은 승인본 그대로 두고 아래 세 가지만 바꾼다 — 6 카드 문구·자동 캡션, 8 머리 인원 줄, 9 판매처 행(이름 + 연락처). msds-entry "MSDS 보기"는 바깥 링크 대신 화면 16을 연다(rules.json msds_summary.entry)라서 ↗ 대신 › 로 표기한다. 화면 16은 새로 설계한다.
색·폰트·모서리·간격은 docs/design.md와 harness/rules.json을 따른다. 허용 색 밖의 값(딤 반투명 검정 등)은 쓰지 않는다. 반투명 회색은 badge-overlay 안에서만. 그림자는 쓰지 않는다(segmented-control-active 예외).
- 핑크 #d6246a·연핑크 #fbe9f0는 badge-low-stock, reorder-alert-card, mix-warning 안에서만 쓴다.
- 하늘색 #2b9fe0·옅은 하늘색 #e6f4fc는 선택·현재 위치·진행·아이콘·안내 띠에만 쓴다. 글자색 금지(그 위 글자 #141414), badge-low-stock·reorder-alert-card·button-primary·mix-warning 안에는 쓰지 않는다. app-sidebar 현재 sidebar-item과 data-table 선택 행·정렬 화살표(활성)는 하늘색 규칙대로.
- 빨강 #ff0000은 화면 16 ghs-pictogram 마름모 테두리 안에서만 쓴다(GHS 표준). 신호어 pill에는 핑크·빨강을 쓰지 않는다.
- auto-threshold-badge "자동" = #f3f3f3 회색 pill + #141414 글자, 캡션은 근거에 따라 두 문구 중 하나: 사용 기록 근거 "최근 사용량으로 계산했어요" / 사용 기록 없음 "마지막 입고량의 20%로 계산했어요". 핑크·하늘색 없음.
학교 선택은 회원가입(화면 14)에만 있다. 대상 화면 모두 학교 선택·전환이 없고 현재 학교명 "샘플고등학교"를 모바일은 nav-pill 안, 데스크톱은 app-sidebar 맨 위에 표시한다. 시약·기록·사용자·판매처·시약장·MSDS 연결은 모두 샘플고등학교 것만 보인다(N1).
외부 서비스 연결 값(AI 읽기·MSDS 조회·요약)은 서버에서만 다룬다. 어떤 화면에도 연결 값 입력 칸·외부 서비스 설정·AI 엔진 선택 UI·관련 문구를 두지 않는다(N2).
괄호 안 역할 표시가 없는 구성 요소는 그 화면에 들어오는 모든 역할에게 보인다. 화면 5·6·7 = 교사·admin만, 화면 8·9 = admin만 들어온다.

모바일 공통(승인본 그대로): tab-bar는 화면 아래 가장자리 y 780~844(폭 390, 높이 64, rounded 0, #ffffff + 위쪽 1px #f0f0f0 선, 그림자 없음)에 붙고 tab-item 4개("홈"·"시약"·"QR 스캔"·"기록")를 같은 폭으로 채운다. 하단 고정 버튼은 tab-bar 바로 위(간격 16). 시트는 tab-bar 위쪽 선 위에 붙는다(딤 없음, 1px #e0e0e0 테두리, 위쪽 rounded 24, 오른쪽 위 × 닫기). 모바일 nav-pill = 얇은 헤더(뒤로가기 또는 워드마크 + 제목 + 학교명 + nav-account-menu ▾).

데스크톱 공통(1440×900, rules.json desktop_shell): nav-pill·tab-bar 없음.
- app-sidebar: 왼쪽 고정 열 폭 240, 높이 전체, rounded 0, #f3f3f3 채움, 오른쪽 1px #f0f0f0 선. 맨 위 "Lab_Stock" 워드마크 + 학교명 "샘플고등학교"(title #141414, 전환 없음) → 가운데 sidebar-item 묶음 → 맨 아래 "{이름} · {역할}"(body-sm) + nav-account-menu ▾.
- sidebar-item: 아이콘 + body 라벨, 높이 44, 사각형(rounded 0). 현재 항목 = #e6f4fc 채움 + #2b9fe0 아이콘, 라벨 #141414. 비활성 아이콘·라벨 #707070 아이콘 / #141414 라벨. 역할별 메뉴(rules.json desktop_shell.menu) — 묶음 제목 caption #707070:
  - 학생 5개: 홈 · 시약 · 기록 · 시약장 · QR 찾기
  - 교사 8개: 홈 · 시약 · 기록 · 시약장 · QR 찾기 / "관리" 입고 · 실험 매뉴얼 · 재주문 알림
  - admin 10개: 교사 8개 + "학교 설정" 사용자 · 판매처
  - 연결: 홈→13, 시약→2, 기록→10, 시약장→11, QR 찾기→12, 입고→7, 실험 매뉴얼→5, 재주문 알림→6, 사용자→8, 판매처→9. 화면 3·4·16은 "시약"이 현재 항목.
- nav-account-menu: app-sidebar 맨 아래 이름·역할 옆 작은 ▾ → 위로 열리는 #ffffff 작은 메뉴(rounded 24, 1px #f0f0f0 테두리)에 "로그아웃" 1개. 프레임에는 닫힌 상태.
- 본문 = 사이드바 오른쪽 전체, 페이지 여백 32. 페이지 머리 = 왼쪽 제목(heading-2) + 개수(caption #707070), 오른쪽 검색·필터·주 버튼.
- data-table: ex-data-table-cell 머리행(caption #707070)·본문(body-sm) + rounded 16 컨테이너, 1px #f0f0f0 테두리. 정렬 가능한 열 머리(화살표 #707070, 활성 #2b9fe0), 행 hover #f3f3f3, 선택 행 #e6f4fc. 상태(badge-low-stock)는 자기 열. 길면 표 아래 가운데 페이지 번호.
- detail-drawer: 오른쪽 폭 480, 높이 전체, #ffffff, 왼쪽 1px #f0f0f0 선, 딤 없음(뒤 표가 그대로 보이고 선택 행만 강조), 오른쪽 위 × 닫기. 순서 = 제목 → 상태 칩 → "항목 | 값" 2열 행 → 아래 고정 동작 줄. 가운데 모달로 열지 않는다.
- 무거운 작업(5·7·11) = 본문 페이지. 가운데 단일 열 폭 640, "라벨 | 입력" 행 사이 1px #f0f0f0 선, 주 동작은 본문 하단 고정 바(#ffffff, 위 1px #f0f0f0 선, 오른쪽 정렬).
- 겹침: ex-modal-card는 확인·한 칸 입력에만. 모바일 고르기 시트(필터·MSDS 후보·위치·판매처·날짜·칸)는 데스크톱에서 그 컨트롤에 붙은 드롭다운·팝오버(#ffffff, 1px #e0e0e0, rounded 24). ex-toast는 오른쪽 아래.
예시 데이터(공통): 오늘 = 2026-10-07. 샘플고등학교 시약 42종, 재고 부족 3종(염산 · 50 mL, 에탄올 · 200 mL, 질산은 · 5 g), MSDS 없는 시약 4종, 시약장 2개(1번 시약장 · 2번 시약장). 데스크톱 프레임 기준 역할 = 화면 8·9는 admin "정OO · admin", 나머지는 교사 "김OO · 교사".

## 화면 2
시약 목록. 학생·교사·admin 모두. 모바일 = runs/20261007-0744 화면 2 그대로(필터 적용 없음, 이름순, "전체", 42종).
모바일 활성 탭: "시약". 위→아래: nav-pill → (교사·admin) msds-bulk-banner → segmented-control → 검색 줄(text-input + list-filter-button) → (필터 적용 시) filter-chip-row → reagent-row 목록 → tab-bar.
데스크톱 배치: app-sidebar("시약" 현재) | 본문 = 페이지 머리(왼쪽 "시약" + "42종", 그 아래 body-sm #707070 요약 "재고 부족 3 · MSDS 없음 4"(학생은 "재고 부족 3"만) / 오른쪽 검색 text-input 폭 320 + list-filter-button) → (교사·admin) msds-bulk-banner → 툴바(segmented-control 왼쪽, filter-chip-row 오른쪽) → data-table → 표 아래 가운데 페이지 번호 "1 2 3".
### 구성 요소
- app-sidebar: 데스크톱 전용. 공통 규격, 워드마크 + 학교명 "샘플고등학교" + 역할별 메뉴 + 이름·역할·nav-account-menu
- sidebar-item: 데스크톱 전용. 학생 5개(홈·시약·기록·시약장·QR 찾기) / 교사 8개(+ 입고·실험 매뉴얼·재주문 알림) / admin 10개(+ 사용자·판매처). 현재 = "시약"(#e6f4fc 채움 + #2b9fe0 아이콘, 라벨 #141414)
- nav-pill: 모바일 전용. "Lab_Stock" 워드마크 + 현재 학교명 "샘플고등학교" + 학교명 옆 nav-account-menu ▾. 학교 전환 없음. 데스크톱에는 두지 않는다
- nav-account-menu: 모바일 = 학교명 옆 ▾, 데스크톱 = app-sidebar 맨 아래 이름 옆 ▾. 메뉴 항목 "로그아웃" 1개. 하늘색 없음
- msds-bulk-banner: 모바일 = nav-pill 바로 아래·segmented-control 위 한 줄 전폭 띠(x 0, 폭 390, rounded 0, #e6f4fc 채움, 안쪽 여백 12·16). 왼쪽 body-sm #141414 "MSDS 없는 시약 4종", 오른쪽 button-pill-soft "한 번에 찾기"(높이 44 이상). 데스크톱 = 페이지 머리 아래 본문 폭 띠(rounded 16, 같은 내용). 누르면 상태 화면 2-msds-bulk(데스크톱은 띠 버튼에 붙은 팝오버의 msds-candidates). 0종이면 숨김. 하늘색: 띠 채움 #e6f4fc (교사·admin만)
- button-pill-soft: msds-bulk-banner 안 "한 번에 찾기"(#f3f3f3 채움, 라벨 #141414, rounded 9999). 하늘색 없음 (교사·admin만)
- segmented-control: "전체 / 재고 부족", 한 번에 하나. 필터와 따로 동작하고 둘 다 결과에 적용. 데스크톱 = 표 위 툴바 왼쪽
- segmented-control-active: 선택 옵션 흰 pill("전체"). 하늘색: 1px #2b9fe0 테두리(글자 #141414)
- text-input: 검색 "시약명 검색"(#f0f0f0, rounded 16, 포커스 링 2px #141414). 모바일 = 검색 줄 왼쪽(오른쪽 list-filter-button 자리만큼 줄어든 폭, 사이 8), 데스크톱 = 페이지 머리 오른쪽 폭 320. 하늘색: 검색 아이콘 #2b9fe0
- list-filter-button: 검색 text-input 오른쪽 button-pill-soft "필터"(#f3f3f3, 왼쪽 필터 아이콘, 라벨 #141414, rounded 9999, 높이 44 이상). 모바일은 list-filter-sheet 바텀시트, 데스크톱은 버튼 바로 아래 드롭다운 패널. 적용되면 개수 pill(#e6f4fc 채움 + 1px #2b9fe0 테두리, label #141414). 이 프레임은 적용 없음이라 숨김. 하늘색: 필터 아이콘 #2b9fe0
- list-filter-sheet: 필터 패널(이 프레임에서는 닫힘). 모바일 = tab-bar 위 바텀시트, 데스크톱 = list-filter-button 아래 드롭다운 패널(폭 400, 오른쪽 끝을 버튼에 맞춤, rounded 24, 1px #e0e0e0). 순서 = 정렬 → 보관 분류 storage-class-chip + "분류 없음" → 보관 위치(시약장 → 칸, "칸 없음만") → "MSDS 없는 시약만" → button-outline "초기화" + button-primary "{N}종 보기". 모양은 상태 화면 2-filter 승인본
- filter-chip-row: 필터가 하나 이상 적용됐을 때만 목록 위 한 줄(적용 칩 #f3f3f3 pill + × / "모두 지우기" / 결과 수 caption "12종"). 데스크톱 = 툴바 segmented-control 오른쪽. 이 프레임에서는 숨김
- data-table: 데스크톱 전용 시약 표. 열 = 시약명(정렬, 활성 — 이름순 ↑ #2b9fe0) · 보관 분류 · 보관 위치(cabinet-number 원 + "1번 시약장 · 우 1단", 없으면 "칸 없음" #707070) · 재고(정렬) · 상태(badge-low-stock) · 최근 입고일(정렬) · MSDS(있음 / "없음" #707070). 한 페이지 20행, 42종 → 페이지 번호 "1 2 3"(현재 "1" #e6f4fc 원 + #141414 숫자). 행을 누르면 화면 3(이 표 위에 detail-drawer, 그 행 #e6f4fc). 필터 결과 0건이면 표 머리를 남기고 표 안에 ex-empty-state-card
- reagent-row: 모바일 전용. 시약명(title) + 재고량·단위(body) + 입고일(caption #707070), #f3f3f3, rounded 16, 행 사이 12. 누르면 화면 3. 기본 정렬 이름순. 하늘색: › 아이콘 #2b9fe0, 누른 행 배경 #e6f4fc
- badge-low-stock: 재고 부족 시약 "재고 부족"(#d6246a 채움, #ffffff label, rounded 9999). 모바일 = 시약명 옆, 데스크톱 = data-table 상태 열. 하늘색 없음
- ex-empty-state-card: 검색만으로 결과 0건 "찾는 시약이 없어요"(필터 적용 0건은 2-filter-empty). 데스크톱은 data-table 안. 하늘색: 안내 아이콘 #2b9fe0
- tab-bar: 모바일 전용 하단 탭바 1개(공통 규격). 데스크톱에는 두지 않는다. 하늘색: 활성 tab-item 아이콘 #2b9fe0만
- tab-item: "홈" · "시약" · "QR 스캔" · "기록" 4개, 사각형(rounded 0), 높이 48. 활성 = "시약"(#2b9fe0 아이콘 + 라벨 #141414), 비활성 3개 #707070
### 반영한 레퍼런스
- https://uibowl.io/name/%EB%B3%BC%ED%8A%B8%EC%97%85?patterns=%ED%95%84%ED%84%B0&imgId=cmojep21l001hjs04hvksxikk
- https://uibowl.io/name/%EC%B9%B4%EC%B9%B4%EC%98%A4%EA%B3%A8%ED%94%84%EC%98%88%EC%95%BD?patterns=%ED%95%84%ED%84%B0&imgId=cmtwlv9y9002eky04rfw0ikms
- https://uibowl.io/website/%EB%A6%AC%EC%BA%90%EC%B9%98?patterns=%EA%B2%80%EC%83%89&imgId=cmihk0pui000pl804eqhg1j1k
- https://uibowl.io/website/%EB%BF%8C%EB%A6%AC%EC%98%A4?patterns=%EB%82%B4%EC%97%AD&imgId=cmu1vvu9l000vjv04jiybtxr8
- https://uibowl.io/website/%EC%82%AC%EB%B0%A9%EB%84%B7?patterns=%ED%8E%B8%EC%A7%91%C2%B7%EC%88%98%EC%A0%95%ED%95%98%EA%B8%B0&imgId=cmu4rqsym001rl504326axccl

## 화면 3
시약 상세. 학생·교사·admin 모두. 교사·admin은 location-edit·threshold-edit, 학생은 보기만. 모바일 = runs/20261007-0002 화면 3 그대로(과산화수소, 재고 2병, 재주문 기준 자동 3병 + 재고 부족, 보관 위치 1번 시약장 · 우 1단, MSDS 있음). 바뀐 것: 자동 기준 캡션을 근거별 두 문구로, "MSDS 보기"가 화면 16을 연다.
모바일 활성 탭: "시약". 위→아래: nav-pill → reagent-detail-card(시약명·재고 → reagent-location → reorder-threshold) → segmented-control "정보 / 사용 기록" → 표 → msds-entry → 하단 고정 "사용 기록"(+ 교사·admin "입고") → tab-bar.
데스크톱 배치: app-sidebar("시약" 현재) | 본문 = 화면 2 시약 목록(data-table, "과산화수소" 행 #e6f4fc 선택) 그대로 + 오른쪽 detail-drawer 480(딤 없음, 왼쪽 목록 머리·검색은 그대로 보임). 드로어 = × 닫기 → 시약명 + 상태 칩 → segmented-control → "항목 | 값" 행(현재 재고·입고일·보관 위치·재주문 기준) → msds-entry → 아래 고정 동작 줄.
### 구성 요소
- app-sidebar: 데스크톱 전용. 공통 규격, 학교명 "샘플고등학교" + 역할별 메뉴 + nav-account-menu
- sidebar-item: 데스크톱 전용. 학생 5개 / 교사 8개 / admin 10개(공통 메뉴). 현재 = "시약"
- nav-pill: 모바일 전용. 뒤로가기(화면 2) + 제목 "시약 상세" + 현재 학교명 "샘플고등학교" + nav-account-menu ▾. 학교 전환 없음. 하늘색: 뒤로가기 아이콘 #2b9fe0
- nav-account-menu: 모바일 = 학교명 옆 ▾, 데스크톱 = app-sidebar 맨 아래. 메뉴 항목 "로그아웃" 1개. 하늘색 없음
- data-table: 데스크톱 전용. 드로어 뒤 화면 2 시약 표(열·정렬·페이지 번호 화면 2와 같음), 선택 행 "과산화수소" #e6f4fc. 다른 행을 누르면 드로어 내용이 그 시약으로 바뀐다
- detail-drawer: 데스크톱 전용. 오른쪽 폭 480, 높이 900, #ffffff, 왼쪽 1px #f0f0f0 선, 안쪽 여백 24, 오른쪽 위 × 닫기(누름 영역 44 이상). 위→아래: 시약명 heading-3 "과산화수소" → 상태 칩 줄(badge-low-stock "재고 부족" + storage-class-chip "산화제" 보기 전용) → segmented-control "정보 / 사용 기록" → "항목 | 값" 2열 행(사이 1px #f0f0f0 선): 현재 재고 "2병"(display) · 입고일 · reagent-location 행 · reorder-threshold 행 → msds-entry → 아래 고정 동작 줄(위 1px #f0f0f0 선): button-primary "사용 기록"(→ 화면 4, 드로어 안 폼으로 바뀜) + (교사·admin) button-outline "입고". 하늘색: × 아이콘 #2b9fe0
- reagent-detail-card: 모바일 = 상단 요약 카드(#ffffff, 1px #f0f0f0 테두리, rounded 24, 여백 24): 시약명(title) + badge-low-stock, 현재 재고 display "2" + 단위 "병", 입고일 caption, 그 아래 reagent-location 줄·reorder-threshold 줄. 데스크톱 = 카드 테두리 없이 detail-drawer 안 "항목 | 값" 행으로 같은 내용. 하늘색 없음
- badge-low-stock: 재고 2병 < 재주문 기준 3병이라 "재고 부족"(#d6246a 채움, #ffffff label). 자동 기준이어도 같은 규칙. 모바일 = 시약명 옆, 데스크톱 = 드로어 상태 칩 줄. 하늘색 없음
- storage-class-chip: 데스크톱 드로어 상태 칩 줄의 보관 분류 "산화제"(보기 전용, #f3f3f3 채움, label #141414, rounded 9999). 하늘색·핑크 없음
- reagent-location: 한 줄. caption "보관 위치"(#707070) + 값 "cabinet-number(1) 1번 시약장 · 우 1단"(body #141414). 칸이 없으면 "칸 없음"(#707070). 교사·admin은 줄 오른쪽에 location-edit. 학생은 값만
- cabinet-number: reagent-location 값 앞 작은 원(#ffffff, 1px #e0e0e0, rounded 9999) 안 숫자 "1"(label #141414). 핑크·하늘색 글자 없음
- location-edit: reagent-location 줄 오른쪽 button-pill-soft "위치 바꾸기"(#f3f3f3, 라벨 #141414, rounded 9999, 높이 44 이상). 모바일 = 상태 화면 3-location 바텀시트, 데스크톱 = 버튼에 붙은 팝오버(폭 400, 드로어 왼쪽으로 펼침)의 location-picker(추천 칸 suggest-badge 처음 선택) (교사·admin만)
- reorder-threshold: reagent-location 아래 한 줄. caption "재주문 기준"(#707070) + 값 "3병"(body #141414) + 값 오른쪽 auto-threshold-badge "자동", 줄 아래 caption(#707070) 근거 한 줄 — 이 시약은 사용 기록이 있어 "최근 사용량으로 계산했어요"(사용 기록이 없으면 "마지막 입고량의 20%로 계산했어요"). 값이 없고 자동 계산도 못 하면 "아직 없어요"(#707070). 화면 5 AI 추출 값과 같은 칸. 학생은 값·배지·캡션만
- auto-threshold-badge: reorder-threshold 값 옆 작은 pill "자동"(#f3f3f3 채움, rounded 9999, label #141414). 직접 입력·매뉴얼 추출 값이면 배지·캡션 없음. 핑크·하늘색 없음. 모든 역할
- threshold-edit: reorder-threshold 값 오른쪽 연필 아이콘(누름 영역 44 이상). 누르면 값 자리가 숫자 text-input(값 "3" + suffix "병")과 줄 아래 button-primary "저장"으로 바뀐다(데스크톱도 드로어 안 그 자리). 저장하면 직접 입력 값이 되어 "자동" 배지·캡션이 사라진다. 빈 값·음수는 #141414 body-sm "1 이상 입력하세요"(핑크 금지). 하늘색: 연필 아이콘 #2b9fe0 (교사·admin만)
- text-input: threshold-edit 편집 상태 숫자 입력(#f0f0f0, 테두리 없음, rounded 16, 포커스 링 2px #141414, suffix #707070) (교사·admin만)
- segmented-control: "정보 / 사용 기록" 두 탭. 모바일 = 요약 아래, 데스크톱 = 드로어 상태 칩 아래
- segmented-control-active: 활성 탭 흰 pill. 하늘색: 활성 탭 아래 #2b9fe0 인디케이터(글자 #141414)
- ex-data-table-cell: "정보" 탭 = 시약 속성 라벨-값 표, "사용 기록" 탭 = 날짜·사용자·사용량 3열 표. 하늘색: 가장 최근 사용 기록 행 배경 #e6f4fc
- msds-entry: MSDS 블록. MSDS가 있으면 msds-qr-tile + button-pill-soft "MSDS 보기 ›"(→ 화면 16: 모바일은 MSDS 전용 화면, 데스크톱은 같은 detail-drawer가 MSDS 요약으로 바뀜). 학생·교사·admin 모두 1개. MSDS가 없으면 QR 자리에 caption(#707070) "MSDS가 아직 없어요" + 교사·admin에게만 msds-search(상태 화면 3-msds, 데스크톱은 버튼에 붙은 팝오버). 하늘색: › 아이콘 #2b9fe0
- msds-qr-tile: msds-entry 안 QR 타일(#ffffff, 1px #f0f0f0, rounded 24, QR 1:1 rounded 0, 아래 라벨 "QR로 MSDS 열기")
- msds-search: MSDS 없는 시약일 때 msds-entry 안 button-pill-soft "MSDS 찾기". 예시 시약(과산화수소)은 MSDS가 있어 이 프레임에는 그리지 않는다. 하늘색: 검색 아이콘 #2b9fe0 (교사·admin만)
- button-primary: 하단 고정 "사용 기록"(→ 화면 4, 모든 역할), threshold-edit "저장"(교사·admin). #141414 채움, #ffffff 글자, rounded 9999, 높이 44 이상. 데스크톱 = 드로어 아래 고정 동작 줄. 하늘색 없음
- button-outline: "사용 기록" 옆 "입고"(→ 화면 7) (교사·admin만)
- ex-toast: "재주문 기준을 3병으로 바꿨어요" / "보관 위치를 바꿨어요". 모바일 tab-bar 위, 데스크톱 오른쪽 아래. 하늘색: 완료 체크 아이콘 #2b9fe0 (교사·admin만)
- tab-bar: 모바일 전용 하단 탭바 1개(공통 규격). 데스크톱에는 두지 않는다. 하늘색: 활성 tab-item 아이콘 #2b9fe0만
- tab-item: "홈" · "시약" · "QR 스캔" · "기록" 4개. 활성 = "시약", 비활성 3개 #707070
### 반영한 레퍼런스
- https://uibowl.io/name/Bitget?patterns=%EC%9D%B8%EC%A6%9D%ED%95%98%EA%B8%B0&imgId=cmukqaul5002ll60430j2ykk1
- https://uibowl.io/name/%ED%86%A0%EC%8A%A4%EC%A6%9D%EA%B6%8C?patterns=%EC%BB%A4%EB%AE%A4%EB%8B%88%ED%8B%B0&imgId=cmsb4ub9l0009jo042gue22tj
- https://uibowl.io/website/%EB%A6%AC%EC%BA%90%EC%B9%98?patterns=%EB%82%B4%EC%97%AD&imgId=cmihk1yub0005li04jv0iyqbi
- https://uibowl.io/website/%EB%A6%AC%EC%BA%90%EC%B9%98?patterns=%EB%82%B4%EC%97%AD&imgId=cmihk1ytc0003li04whm7bprz
- https://uibowl.io/website/%EC%B1%84%EB%84%90%ED%86%A1?patterns=AI&imgId=cmudq46a2002ul4041tszo60n

## 화면 4
사용 기록 입력. 학생·교사·admin 모두(화면 3 "사용 기록", 홈 quick-action "사용 기록 입력"). 모바일 = runs/20261007-0744 화면 4 그대로(에탄올, 현재 재고 1,200 mL, 사용량 50 mL, 사용일 오늘 "2026-10-07", past-date-note 숨김).
모바일 활성 탭: "기록". 위→아래: nav-pill → reagent-detail-card → 폼(사용량 → 사용일 → 사용자 → 메모) → 하단 전폭 "사용 기록 저장" → tab-bar.
데스크톱 배치: app-sidebar("시약" 현재) | 본문 = 시약 목록 data-table("에탄올" 행 선택) + 오른쪽 detail-drawer가 사용 기록 폼으로 바뀐 상태(맨 위 "‹ 시약 상세" 되돌아가기 → 제목 "사용 기록 · 에탄올" → "라벨 | 입력" 행 사용량 · 사용일 · 사용자 · 메모 → 아래 고정 "사용 기록 저장"). 저장 후 오른쪽 아래 ex-toast, 화면 이동 없이 드로어는 시약 상세로 돌아감.
### 구성 요소
- app-sidebar: 데스크톱 전용. 공통 규격, 학교명 "샘플고등학교" + 역할별 메뉴 + nav-account-menu
- sidebar-item: 데스크톱 전용. 학생 5개 / 교사 8개 / admin 10개(공통 메뉴). 현재 = "시약"
- nav-pill: 모바일 전용. 뒤로가기(화면 3) + 제목 "사용 기록" + 현재 학교명 "샘플고등학교" + nav-account-menu ▾. 하늘색: 뒤로가기 아이콘 #2b9fe0
- nav-account-menu: 모바일 = 학교명 옆 ▾, 데스크톱 = app-sidebar 맨 아래. "로그아웃" 1개. 하늘색 없음
- data-table: 데스크톱 전용. 드로어 뒤 화면 2 시약 표, 선택 행 "에탄올" #e6f4fc
- detail-drawer: 데스크톱 전용. 폭 480, 높이 900, #ffffff, 왼쪽 1px #f0f0f0 선, 여백 24, × 닫기. 위→아래: 조용한 텍스트 동작 "‹ 시약 상세"(link #141414, 누름 영역 44 이상) → heading-3 "사용 기록" + caption(#707070) "에탄올 · 현재 1,200 mL" → "라벨 | 입력" 행(사이 1px #f0f0f0 선): 사용량 · 사용일(usage-date) · 사용자 · 메모 → 아래 고정 button-primary "사용 기록 저장"
- reagent-detail-card: 모바일 = 폼 위 요약(#ffffff, 1px #f0f0f0 테두리, rounded 24, 여백 24) 시약명 "에탄올"(title) + 현재 재고 "1,200 mL"(body). 데스크톱 = 드로어 제목 아래 caption 한 줄로 대신. 재고 부족 배지 없음. 하늘색 없음
- text-input: "사용량"(필수) 숫자 + 단위 칩(병·mL·g, 선택 "mL"), "사용자"(필수, 로그인한 사용자 기본값), "메모". 필수 라벨 옆 caption "필수"(#707070). #f0f0f0, rounded 16, 포커스 링 2px #141414. 모바일 = 라벨 위·입력 아래 세로, 데스크톱 = 라벨 왼쪽 | 입력 오른쪽. 하늘색: 단위 칩 선택 #e6f4fc + 1px #2b9fe0 테두리(글자 #141414)
- usage-date: 사용량 바로 아래 "사용일"(필수) 날짜 칸(text-input 모양, #f0f0f0, rounded 16, 값 "2026-10-07", 오른쪽 달력 아이콘) — 화면 7 입고일과 같은 모양. 모바일 = 누르면 날짜 고르기 시트(tab-bar 위, × 닫기, 하단 "완료"), 데스크톱 = 칸 아래 붙는 달력 팝오버(누르면 바로 반영). 오늘 이후 흐림(#adadad, 누름 없음). 오늘이 아니면 past-date-note(상태 화면 4-past-date). 하늘색: 달력 아이콘 #2b9fe0, 선택 날짜 원 #e6f4fc + 1px #2b9fe0 테두리(숫자 #141414)
- button-primary: "사용 기록 저장"(#141414 채움, #ffffff 글자, rounded 9999, 높이 44 이상). 모바일 = 하단 전폭 tab-bar 바로 위, 데스크톱 = 드로어 아래 고정 줄 전폭. 사용량·사용일·사용자가 비면 비활성. 모바일 날짜 시트 "완료"도 같은 모양. 하늘색 없음
- ex-toast: 저장 직후 "사용 기록을 저장했어요". 모바일 = tab-bar 위, 이후 화면 3 "사용 기록" 탭으로. 데스크톱 = 오른쪽 아래(✓ + "기록했어요" + 시약명 한 줄), 드로어는 시약 상세로. 하늘색: 완료 체크 아이콘 #2b9fe0
- tab-bar: 모바일 전용 하단 탭바 1개(공통 규격). 저장 버튼은 이 바 위. 데스크톱에는 두지 않는다. 하늘색: 활성 tab-item 아이콘 #2b9fe0만
- tab-item: "홈" · "시약" · "QR 스캔" · "기록" 4개. 활성 = "기록"(#2b9fe0 아이콘 + 라벨 #141414), 비활성 3개 #707070
### 반영한 레퍼런스
- https://uibowl.io/name/%EB%83%89%EC%9E%A5%EA%B3%A0%ED%84%B8%EA%B8%B0?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&imgId=cmohwpkck001bl2044p9wk6ef
- https://uibowl.io/name/%ED%82%A4%ED%94%BC%EB%9F%BD?patterns=%EB%A9%94%EC%9D%B8&imgId=cmow8tk98000el704gib8a8ij
- https://uibowl.io/website/%EB%A6%AC%EC%BA%90%EC%B9%98?patterns=%EB%82%B4%EC%97%AD&imgId=cmihk1yub0005li04jv0iyqbi
- https://uibowl.io/website/%EB%A6%AC%EC%BA%90%EC%B9%98?patterns=%EB%82%B4%EC%97%AD&imgId=cmihk42lp000jjp0436gwgn7n
- https://uibowl.io/website/%EB%A6%AC%EB%94%94?patterns=%EB%82%B4%EC%97%AD&imgId=cmuq7e6jd000wjs046c714kre

## 화면 5
실험 매뉴얼 → AI 추출 결과 확인. 교사·admin만(학생 노출 0). 모바일 = runs/20261007-0848 화면 5 그대로. 흐름: 1단계 업로드(파일 + 조 수, 조 수 처음 빈 값) → "AI 추출" → 2단계 추출 결과 확인 → "확인 후 저장".
예시 상태(5-mobile · 5-desktop): 2단계. 접힌 manual-upload("산·염기 중화 실험.pdf", 조 수 4) 아래 extraction-table 행 4개 —
① 염산 · 1조 20 · mL → 80 mL / 우리 학교 시약 "염산" · 삭제 · "기존 기준 100 · 바뀌어요"
② 수산화나트륨 · 1조 5 · g → 20 g / "수산화나트륨" · 삭제 · "기존 기준 20 · 그대로 둬요"
③ 페놀프탈레인 용액 · 1조 2 · mL → 8 mL / "페놀프탈레인 용액" · 삭제 · "기존 기준 없음 · 새로 정해요"
④ 증류수 · 1조 150 · mL → 600 mL / "증류수" · 삭제 · "기존 기준 500 · 바뀌어요" + 무채색 안내 줄 "2개 행을 합쳤어요"
모바일 활성 탭: "기록". 위→아래: nav-pill → 접힌 manual-upload → extraction-table(행 카드) → 하단 버튼 줄("다시 추출" + "확인 후 저장") → tab-bar.
데스크톱 배치: app-sidebar("실험 매뉴얼" 현재) | 본문 페이지 = 페이지 머리 "실험 매뉴얼" → 가운데 단일 열 폭 640: 접힌 manual-upload 한 줄 → extraction-table 열 표(시약명 · 1조 사용량 · 단위 · 1반 1회 필요량, 행마다 아래 줄) → 본문 하단 고정 바(button-outline "다시 추출" + button-primary "확인 후 저장" 오른쪽 정렬).
### 구성 요소
- app-sidebar: 데스크톱 전용. 공통 규격, 학교명 "샘플고등학교" + 메뉴 + nav-account-menu (교사·admin만)
- sidebar-item: 데스크톱 전용. 교사 8개(홈·시약·기록·시약장·QR 찾기 / 입고·실험 매뉴얼·재주문 알림) / admin 10개(+ 사용자·판매처). 현재 = "실험 매뉴얼". 학생에게는 이 화면이 없다 (교사·admin만)
- nav-pill: 모바일 전용. 뒤로가기(화면 6) + 제목 "실험 매뉴얼" + 현재 학교명 "샘플고등학교" + nav-account-menu ▾. 하늘색: 뒤로가기 아이콘 #2b9fe0 (교사·admin만)
- nav-account-menu: 모바일 = 학교명 옆 ▾, 데스크톱 = app-sidebar 맨 아래. "로그아웃" 1개. 하늘색 없음 (교사·admin만)
- manual-upload: 1단계 업로드 영역. 처음 상태 = body-lg "실험 매뉴얼을 올리면 시약별 사용량을 찾아드려요" + 업로드/미리보기 타일(rounded 16, 비율 유지) + "조 수" text-input(빈 값, 플레이스홀더 "예: 4") + button-primary "AI 추출"(파일·조 수가 비면 비활성). 추출 중 = 타일 안 진행 막대 + "사용량을 찾고 있어요". 2단계(예시) = 한 줄 높이로 접혀 파일 타일(작은 미리보기 + badge-overlay) 오른쪽에 "조 수 4"(고치면 필요량 다시 계산). 데스크톱 = 640 열 맨 위 같은 한 줄. 하늘색: 업로드 아이콘 #2b9fe0, 진행 막대 #2b9fe0(트랙 #e6f4fc) (교사·admin만)
- badge-overlay: 미리보기 위 파일 이름 태그 "산·염기 중화 실험.pdf"(rgba(115,115,115,0.56), #ffffff label, rounded 9999). 하늘색 없음 (교사·admin만)
- text-input: "조 수"(숫자, 기본 빈 값), 추출 행 "1조 사용량"(숫자), 단위 선택 상자(값 "mL" ▾, 목록 병 · mL · g — 데스크톱은 드롭다운), "우리 학교 시약" 선택 상자. #f0f0f0, 테두리 없음, rounded 16, 포커스 링 2px #141414. 하늘색: ▾ 아이콘 #2b9fe0 (교사·admin만)
- extraction-table: 2단계 추출 결과 확인. heading-3 "추출 결과 확인" + body-sm(#707070) "확인한 뒤 저장해야 반영돼요". 행 1줄 = 시약명(title) · 1조 사용량 + 단위 · 1반 1회 필요량(자동 계산) / 2줄(위 간격 8) = "우리 학교 시약" 선택 상자(샘플고등학교 시약만) → 조용한 텍스트 동작 "삭제"(link #141414, 확인 없음) → 줄 끝 body-sm(#707070) "기존 기준 {N} · 그대로 둬요 / 바뀌어요"(기준 없으면 "기존 기준 없음 · 새로 정해요"). 같은 시약이 여러 번 나오면 한 행으로 합치고 caption(#707070) "2개 행을 합쳤어요". 모바일 = 행마다 #f3f3f3 카드(rounded 16, 여백 16), 데스크톱 = rounded 16 표 컨테이너 안 ex-data-table-cell 행(폭 640). 하늘색: 고친 사용량 칸 배경 #e6f4fc (교사·admin만)
- ex-data-table-cell: 데스크톱 extraction-table 머리행(caption #707070 "시약명 · 1조 사용량 · 단위 · 1반 1회 필요량")과 본문 셀(body-sm), 행 구분 1px #f0f0f0 선 (교사·admin만)
- button-outline: 2단계 "다시 추출"(#ffffff, 1px #e0e0e0, 라벨 #141414, rounded 9999, 높이 44 이상). 모바일 = tab-bar 위 버튼 줄 왼쪽(비율 1:2), 데스크톱 = 하단 고정 바 "확인 후 저장" 왼쪽 (교사·admin만)
- button-primary: 1단계 "AI 추출", 2단계 "확인 후 저장"(#141414 채움, #ffffff 글자, rounded 9999, 높이 44 이상). 저장하면 각 행 필요량이 연결된 시약의 재주문 기준(화면 3 reorder-threshold와 같은 칸)에 들어간다. 연결 안 된 행이 있으면 비활성. 데스크톱 = 본문 하단 고정 바 오른쪽 끝. 하늘색 없음 (교사·admin만)
- ex-toast: 저장 직후 "재주문 기준을 저장했어요", 이후 화면 6. 모바일 tab-bar 위, 데스크톱 오른쪽 아래. 하늘색: 완료 체크 아이콘 #2b9fe0 (교사·admin만)
- tab-bar: 모바일 전용 하단 탭바 1개(공통 규격). 데스크톱에는 두지 않는다. 하늘색: 활성 tab-item 아이콘 #2b9fe0만 (교사·admin만)
- tab-item: "홈" · "시약" · "QR 스캔" · "기록" 4개. 활성 = "기록", 비활성 3개 #707070 (교사·admin만)
### 반영한 레퍼런스
- https://uibowl.io/name/%ED%8E%98%EC%9D%B4%ED%9E%88%EC%96%B4?patterns=%EC%B4%AC%EC%98%81%ED%95%98%EA%B8%B0&imgId=cmnfmykft001zl204e2svm4y5
- https://uibowl.io/name/%EA%B3%A8%ED%94%84%EC%A1%B4?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&imgId=cmunkfw4m0069jq041c3fhn4u
- https://uibowl.io/website/%EB%8B%B9%EA%B7%BC%20%EB%B9%84%EC%A6%88%EB%8B%88%EC%8A%A4?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&imgId=cmso6flkw000zl7046s1sne8f
- https://uibowl.io/website/%EC%82%AC%EB%B0%A9%EB%84%B7?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&imgId=cmu4rq8hn000zl604l8itbfr2
- https://uibowl.io/website/%EB%A6%AC%EC%BA%90%EC%B9%98?patterns=%EB%82%B4%EC%97%AD&imgId=cmihk42ii000bjp04pdf72v47

## 화면 6
재주문 알림. 교사·admin만(학생 노출 0). 모바일 = runs/20261007-0848 화면 6 구성 그대로, 카드 문구만 요청 5-2(rules.json reorder.card_text·reorder.auto)대로 바꾼다.
예시 상태(6-mobile · 6-desktop): 알림 3건.
① 염산 — "재주문 기준 100 mL"(매뉴얼 추출 값, 배지 없음) · "현재 재고 50 mL" · "10월 7일 알림". 판매처 "확인" 뒤 상태 — vendor-link 아래 새 창 안내 줄이 보인다.
② 에탄올 — "재주문 기준 800 mL" + auto-threshold-badge "자동" + 캡션 "최근 사용량으로 계산했어요" · "현재 재고 200 mL" · "10월 7일 알림".
③ 질산은 — "재주문 기준 10 g" + auto-threshold-badge "자동" + 캡션 "마지막 입고량의 20%로 계산했어요"(사용 기록 없음, 마지막 입고 50 g) · "현재 재고 5 g" · "10월 6일 알림".
모바일 활성 탭: "시약". 위→아래: nav-pill → 재주문 기준 안내 박스(manual-upload 진입) → reorder-alert-card 목록 → (admin) "판매처 등록" → tab-bar.
데스크톱 배치: app-sidebar("재주문 알림" 현재) | 본문 페이지 = 페이지 머리(왼쪽 "재주문 알림" + "3건" / 오른쪽 (admin) vendor-register "판매처 등록") → 가운데 단일 열 폭 640: 안내 박스 → reorder-alert-card 세로 목록(사이 12). 판매처 고르기는 vendor-link에 붙은 팝오버.
### 구성 요소
- app-sidebar: 데스크톱 전용. 공통 규격, 학교명 "샘플고등학교" + 메뉴 + nav-account-menu (교사·admin만)
- sidebar-item: 데스크톱 전용. 교사 8개 / admin 10개(공통 메뉴). 현재 = "재주문 알림". 학생에게는 이 화면이 없다 (교사·admin만)
- nav-pill: 모바일 전용. "Lab_Stock" 워드마크 + 제목 "재주문 알림" + 현재 학교명 "샘플고등학교" + nav-account-menu ▾. 학교 전환 없음 (교사·admin만)
- nav-account-menu: 모바일 = 학교명 옆 ▾, 데스크톱 = app-sidebar 맨 아래. "로그아웃" 1개. 하늘색 없음 (교사·admin만)
- manual-upload: 목록 위 재주문 기준 안내 박스(#e6f4fc 채움, rounded 16, 글자 #141414, "필요량 = 1반 1회 실험량 × 조 수 · 기준이 없는 시약은 최근 사용량(사용 기록이 없으면 마지막 입고량의 20%)으로 계산해요") 끝의 button-pill-soft "실험 매뉴얼 올리기" → 화면 5. 하늘색: 박스 채움 #e6f4fc, 정보 아이콘 #2b9fe0 (교사·admin만)
- reorder-alert-card: 알림 1건 카드(#f3f3f3, 테두리 없음, rounded 24, 여백 24). 왼쪽 위 badge-low-stock "재고 부족" → 시약명(heading-4) → body "재주문 기준 {N}{단위}"(자동 값이면 숫자 바로 오른쪽 auto-threshold-badge "자동" + 그 줄 아래 caption #707070 근거 한 줄: 사용 기록 근거 "최근 사용량으로 계산했어요" / 사용 기록 없음 "마지막 입고량의 20%로 계산했어요") → body "현재 재고 {M}{단위}" → caption(#707070) "{M}월 {D}일 알림"(예 "10월 7일 알림") → 카드 하단 오른쪽 vendor-link. 판매처 "확인" 뒤 vendor-link 바로 아래(간격 8) 무채색 안내 줄: #707070 바깥 링크 아이콘 + body-sm(#707070) "사이트를 새 창으로 열었어요. 열리지 않았다면" + button-pill-soft "직접 열기". 데스크톱도 같은 카드(폭 640). 카드 안 하늘색 없음 (교사·admin만)
- badge-low-stock: reorder-alert-card 안 "재고 부족"(#d6246a 채움, #ffffff label, rounded 9999). 하늘색 없음 (교사·admin만)
- auto-threshold-badge: 자동 기준 카드(에탄올·질산은) 기준 숫자 오른쪽 pill "자동"(#f3f3f3 채움 + 카드 바탕과 구분되도록 1px #e0e0e0 테두리, label #141414, rounded 9999). 매뉴얼 추출·직접 입력 기준(염산)에는 없다. 핑크·하늘색 없음 (교사·admin만)
- vendor-link: reorder-alert-card 하단 오른쪽 button-primary "판매처 연결"(#141414 채움, #ffffff 글자, rounded 9999, 높이 44 이상). 누르면 판매처 고르기 — 모바일 = ex-modal-card 시트, 데스크톱 = 버튼에 붙은 팝오버. 하늘색 없음 (교사·admin만)
- ex-modal-card: 판매처 고르기(모바일 tab-bar 위 시트, 데스크톱은 같은 내용을 vendor-link 팝오버로, 1px #e0e0e0 테두리, 그림자·딤 없음). 제목 heading-3 "판매처 고르기" + 시약명 caption → 판매처 행 목록(샘플고등학교 판매처 먼저, 그다음 공통 목록) → button-outline "취소" + button-primary "확인". "확인"을 누르면 닫히고 판매처 사이트가 새 창으로 열리며 카드에 새 창 안내 줄이 나타난다. 하늘색: 선택 행 배경 #e6f4fc + 왼쪽 #2b9fe0 선택 표시 (교사·admin만)
- button-pill-soft: 안내 박스 "실험 매뉴얼 올리기", 카드 새 창 안내 줄 "직접 열기"(카드 위라 1px #e0e0e0 테두리, 라벨 #141414, rounded 9999). 하늘색 없음 (교사·admin만)
- button-outline: 판매처 고르기 "취소", (admin) "판매처 등록" (교사·admin만)
- vendor-register: button-outline "판매처 등록" → 화면 9. 모바일 = 알림 목록 아래, 데스크톱 = 페이지 머리 오른쪽 (admin만, 교사 화면에는 없음)
- ex-empty-state-card: 알림 0건 "재고가 부족한 시약이 없어요". 하늘색: 안내 아이콘 #2b9fe0 (교사·admin만)
- tab-bar: 모바일 전용 하단 탭바 1개(공통 규격). 데스크톱에는 두지 않는다. 하늘색: 활성 tab-item 아이콘 #2b9fe0만 (교사·admin만)
- tab-item: "홈" · "시약" · "QR 스캔" · "기록" 4개. 활성 = "시약", 비활성 3개 #707070 (교사·admin만)
### 반영한 레퍼런스
- https://uibowl.io/name/%ED%8F%B4%EC%84%BC%ED%8A%B8?patterns=%ED%98%9C%ED%83%9D&imgId=cmpuvbnmd002xla04lzx58y7e
- https://uibowl.io/name/%ED%86%A0%EC%8A%A4?patterns=%EC%83%81%EC%84%B8%EC%A0%95%EB%B3%B4%20%28PDP%29&imgId=cmrtwe8la005jl204biikq9ad
- https://uibowl.io/website/%EC%9C%84%EC%8B%9C%EC%BC%93?patterns=%EC%95%8C%EB%A6%BC&imgId=cmunb6cq20050l204dynrrpgm
- https://uibowl.io/website/%EC%82%AC%EB%B0%A9%EB%84%B7?patterns=%EC%95%8C%EB%A6%BC&imgId=cmu4rqjcr004pjq04qsvv4bon

## 화면 7
입고·시약 등록. 교사·admin만(홈 quick-action "입고", 화면 3 "입고", 데스크톱 sidebar-item "입고"). 모바일 = runs/20261007-0002 화면 7 그대로 — intake-mode 기본 "서류로 입고", 아직 파일 없는 첫 상태. 이후 흐름은 승인된 상태 화면 7-doc-upload → 7-doc-review → 7-suggest, 실패 7-doc-fail, MSDS 7-msds.
모바일 활성 탭: "시약". 위→아래: nav-pill → intake-mode → doc-upload → tab-bar.
데스크톱 배치: app-sidebar("입고" 현재) | 본문 페이지 = 페이지 머리 "입고" → 가운데 단일 열 폭 640: intake-mode → doc-upload 카드 → 본문 하단 고정 바(button-primary "AI로 읽기" 오른쪽, 파일 없으면 비활성). "직접 입력"은 같은 640 열의 "라벨 | 입력" 행 폼.
### 구성 요소
- app-sidebar: 데스크톱 전용. 공통 규격, 학교명 "샘플고등학교" + 메뉴 + nav-account-menu (교사·admin만)
- sidebar-item: 데스크톱 전용. 교사 8개 / admin 10개(공통 메뉴). 현재 = "입고". 학생에게는 이 화면이 없다 (교사·admin만)
- nav-pill: 모바일 전용. "Lab_Stock" 워드마크 + 제목 "입고·시약 등록" + 현재 학교명 "샘플고등학교" + nav-account-menu ▾ (교사·admin만)
- nav-account-menu: 모바일 = 학교명 옆 ▾, 데스크톱 = app-sidebar 맨 아래. "로그아웃" 1개 (교사·admin만)
- intake-mode: 맨 위 segmented-control 두 옵션 "직접 입력 / 서류로 입고", 한 번에 하나. 기본·이 프레임 = "서류로 입고". 데스크톱 = 640 열 맨 위 (교사·admin만)
- segmented-control: intake-mode 트랙(#f3f3f3, rounded 9999), "직접 입력" 모드 안 "기존 시약 입고 / 새 시약 등록" 토글 (교사·admin만)
- segmented-control-active: 선택 옵션 흰 pill. 하늘색: 1px #2b9fe0 테두리(글자 #141414) (교사·admin만)
- doc-upload: 올리기 카드 1개(ex-empty-state-card 모양, #ffffff, 1px #e0e0e0 테두리, rounded 24, 여백 24). 가운데 업로드 아이콘 → heading-4 "품의서·영수증·거래명세서를 올려 주세요" → caption(#707070) "PDF·JPG·PNG, 4MB까지" → button-pill-soft "촬영하기" · "파일 선택"(데스크톱은 "파일 선택" + 카드 안 끌어다 놓기 안내 caption "여기에 끌어다 놓아도 돼요") → button-primary "AI로 읽기"(모바일 = 카드 하단 전폭, 데스크톱 = 본문 하단 고정 바). 형식·크기 오류 = #141414 아이콘 + body-sm "PDF·JPG·PNG 4MB까지만 올릴 수 있어요"(핑크 금지). 하늘색: 업로드 아이콘 #2b9fe0 (교사·admin만)
- button-pill-soft: doc-upload "촬영하기"(모바일) · "파일 선택"(#f3f3f3, 라벨 #141414, rounded 9999). 하늘색: 왼쪽 아이콘 #2b9fe0 (교사·admin만)
- button-primary: "AI로 읽기"(#141414 채움, #ffffff 글자, rounded 9999, 높이 44 이상, 파일 없으면 비활성), 직접 입력의 "입고"·"시약 등록". 하늘색 없음 (교사·admin만)
- stock-intake: "직접 입력" 모드 "기존 시약 입고" 갈래 — 기존 구성 그대로(검색 → 선택 → 수량 → 입고일 → "입고"). 데스크톱 = 640 열 "라벨 | 입력" 행. 이 프레임에는 그리지 않는다 (교사·admin만)
- reagent-register: "직접 입력" 모드 "새 시약 등록" 갈래 — 기존 폼(시약명·종류·재고량·입고일) + MSDS 칸 옆 msds-search. 이 프레임에는 그리지 않는다 (교사·admin만)
- msds-search: reagent-register MSDS 칸 옆·서류 new-reagent-fields 안 button-pill-soft "MSDS 찾기"(모바일 msds-candidates 시트, 데스크톱 버튼에 붙은 팝오버). 이 프레임에는 그리지 않는다 (교사·admin만)
- text-input: 직접 입력 모드 검색·수량·입고일·폼 입력(#f0f0f0, rounded 16, 포커스 링 2px #141414). 이 프레임에는 그리지 않는다 (교사·admin만)
- ex-toast: 입고 저장 직후 "입고를 기록했어요". 모바일 tab-bar 위, 데스크톱 오른쪽 아래 (교사·admin만)
- tab-bar: 모바일 전용 하단 탭바 1개(공통 규격). 데스크톱에는 두지 않는다. 하늘색: 활성 tab-item 아이콘 #2b9fe0만 (교사·admin만)
- tab-item: "홈" · "시약" · "QR 스캔" · "기록" 4개. 활성 = "시약", 비활성 3개 #707070 (교사·admin만)
### 반영한 레퍼런스
- https://uibowl.io/name/%ED%8E%98%EC%9D%B4%EC%9B%8C%ED%81%AC?patterns=%EC%B4%AC%EC%98%81%ED%95%98%EA%B8%B0
- https://uibowl.io/website/%EC%82%AC%EB%B0%A9%EB%84%B7?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&imgId=cmu4rq8hn000zl604l8itbfr2
- https://uibowl.io/website/%EB%8B%B9%EA%B7%BC%20%EB%B9%84%EC%A6%88%EB%8B%88%EC%8A%A4?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&imgId=cmso6flkw000zl7046s1sne8f
- https://uibowl.io/website/%EC%9C%84%EC%8B%9C%EC%BC%93?patterns=%EA%B3%84%EC%A2%8C&imgId=cmunb5pib0007l204n4d6jnbv

## 화면 8
사용자 관리. admin만(학생·교사 노출 0). 모바일 = runs/20261007-0848 화면 8 그대로 + 요청 5-2: 머리에 역할별 인원 줄(rules.json app_exceptions.user-count-line), 초대 = 이메일 + 역할(학생·교사), 이름 칸 없음.
예시 상태(8-mobile · 8-desktop): 멤버 5명(학생 3 · 교사 1 · admin 1) · 초대 대기 2건, 학생 "박OO" 삭제 확인이 열린 상태. 뒤 목록은 그대로 보인다.
모바일 활성 탭: "홈". 위→아래: nav-pill → user-manage(헤더 "샘플고등학교 사용자 5명" + "초대" → 인원 줄 "학생 3 · 교사 1 · admin 1" → 이름 검색 → 멤버 → 초대 대기 → 유의사항) → tab-bar. 삭제 확인 시트는 tab-bar 위.
데스크톱 배치: app-sidebar("사용자" 현재) | 본문 페이지 = 페이지 머리(왼쪽 "사용자" + "5명", 그 아래 인원 줄 / 오른쪽 인라인 초대 폼: 이메일 text-input + 역할 segmented-control "학생 / 교사" + button-primary "초대") → 툴바(이름 검색) → 멤버 data-table → "초대 대기 (2)" data-table → 유의사항. 삭제 확인 = 가운데 ex-modal-card(확인이라 모달).
### 구성 요소
- app-sidebar: 데스크톱 전용. 공통 규격, 학교명 "샘플고등학교" + 메뉴 + "정OO · admin" + nav-account-menu (admin만)
- sidebar-item: 데스크톱 전용. admin 10개(홈·시약·기록·시약장·QR 찾기 / 입고·실험 매뉴얼·재주문 알림 / 사용자·판매처). 현재 = "사용자". 학생·교사에게는 이 화면이 없다 (admin만)
- nav-pill: 모바일 전용. "Lab_Stock" 워드마크 + 제목 "사용자 관리" + 현재 학교명 "샘플고등학교" + nav-account-menu ▾ (admin만)
- nav-account-menu: 모바일 = 학교명 옆 ▾, 데스크톱 = app-sidebar 맨 아래. "로그아웃" 1개. 하늘색 없음 (admin만)
- user-manage: 본문 블록 1개. 모바일 = 헤더 한 줄 heading-3 "샘플고등학교 사용자 5명" + 오른쪽 button-primary "초대" → 바로 아래 역할별 인원 줄 body-sm(#707070) "학생 3 · 교사 1 · admin 1" → text-input 이름 검색 → "멤버"(heading-4): 행 = 이름(title) + 본인 "나" pill + 보조줄 역할(body-sm #707070) + › (역할 변경 시트) → "초대 대기 (2)"(heading-4): 행 = 이메일 + 초대일 caption + 역할 + 상태 "대기" → 유의사항 body-sm(#707070) "같은 학교(샘플고등학교) 계정만 초대할 수 있어요". 데스크톱 = 페이지 머리(제목·인원 줄·인라인 초대 폼) + 멤버 data-table + 초대 대기 data-table + 유의사항. 하늘색: 로그인한 admin 본인 행 배경 #e6f4fc (admin만)
- data-table: 데스크톱 전용. ① 멤버 표 열 = 이름(정렬) · 이메일 · 역할(정렬) · 가입일(정렬) · 행 끝 ⋮(역할 바꾸기 · 사용자 삭제 — 본인·마지막 admin 행은 삭제 없음). ② 초대 대기 표 열 = 이메일 · 역할 · 초대일 · 상태 "대기". 역할 바꾸기 = ⋮에 붙은 팝오버 라디오 "학생 / 교사 / admin" + "변경". 선택 행(박OO) #e6f4fc (admin만)
- text-input: 이름 검색(플레이스홀더 "이름 검색"), 초대 "이메일"(플레이스홀더 "name@example.com", 모바일 = 초대 시트 안, 데스크톱 = 페이지 머리 인라인). #f0f0f0, rounded 16, 포커스 링 2px #141414. 형식 오류 = 입력 아래 #141414 아이콘 + body-sm "이메일 주소를 확인해 주세요"(핑크 없음). 하늘색: 검색 아이콘 #2b9fe0 (admin만)
- ex-data-table-cell: 모바일 "멤버"·"초대 대기" 행, 데스크톱 data-table 머리행·셀. "나" pill = #f3f3f3 + label #141414. 하늘색: 모바일 › 아이콘 #2b9fe0 (admin만)
- ex-modal-card: 헤더 한 줄 = 제목 왼쪽 + 오른쪽 위 × 닫기(누름 영역 44 이상), 1px #e0e0e0 테두리, 그림자·딤 없음, 모바일 위쪽 rounded 24·tab-bar 위, 데스크톱 rounded 24 가운데. ① 초대 시트(모바일만): "사용자 초대" + body-sm(#707070) "이메일로 초대 링크를 보내요" + button-pill-soft "초대 링크 복사" + "이메일" text-input 1개(이름 칸 없음) + 역할 segmented-control "학생 / 교사" + 전폭 button-primary "초대 보내기". ② 역할 변경 시트(모바일만, 데스크톱은 팝오버): "{이름}의 역할" + 라디오 "학생 / 교사 / admin" + "변경" + button-outline "사용자 삭제"(본인·마지막 admin 숨김, 마지막 admin은 caption "admin이 최소 1명 있어야 해요"). ③ 삭제 확인(예시, 모바일·데스크톱 공통): heading-3 "이 사용자를 삭제할까요?" + body #141414 "박OO · 사용·입고 기록은 남아요" + button-outline "취소" + button-primary "박OO 삭제"(1:1, 사이 8). 핑크 없음. 하늘색: 초대 링크 아이콘 #2b9fe0, 라디오 선택 행 #e6f4fc + 1px #2b9fe0 (admin만)
- segmented-control: 초대 역할 "학생 / 교사", 한 번에 하나. 모바일 = 초대 시트, 데스크톱 = 페이지 머리 인라인 폼 (admin만)
- segmented-control-active: 선택 역할 흰 pill. 하늘색: 1px #2b9fe0 테두리(글자 #141414) (admin만)
- button-pill-soft: 초대 "초대 링크 복사"(#f3f3f3, 라벨 #141414). 데스크톱은 인라인 폼 오른쪽 끝 (admin만)
- button-primary: "초대"(모바일 헤더 → 시트, 데스크톱 인라인 폼 = 바로 보내기, 이메일이 비거나 틀리면 비활성), 시트 "초대 보내기"·"변경", 삭제 확인 "박OO 삭제"(#141414 채움, #ffffff 글자, rounded 9999, 높이 44 이상). 하늘색 없음 (admin만)
- button-outline: 역할 변경 "사용자 삭제", 삭제 확인 "취소"(#ffffff, 1px #e0e0e0, 라벨 #141414) (admin만)
- ex-empty-state-card: 검색 0건 "찾는 사용자가 없어요", 다른 사용자 0명 "아직 초대한 사용자가 없어요". 데스크톱은 data-table 안. 하늘색: 안내 아이콘 #2b9fe0 (admin만)
- ex-toast: "초대를 보냈어요" / "역할을 바꿨어요" / "사용자를 삭제했어요". 모바일 tab-bar 위, 데스크톱 오른쪽 아래. 하늘색: 완료 체크 아이콘 #2b9fe0 (admin만)
- tab-bar: 모바일 전용 하단 탭바 1개(공통 규격). 데스크톱에는 두지 않는다. 하늘색: 활성 tab-item 아이콘 #2b9fe0만 (admin만)
- tab-item: "홈" · "시약" · "QR 스캔" · "기록" 4개. 활성 = "홈", 비활성 3개 #707070 (admin만)
### 반영한 레퍼런스
- https://uibowl.io/name/%EC%99%93%EC%84%AD?patterns=%EC%B7%A8%EC%86%8C%ED%95%98%EA%B8%B0&imgId=cmqt89aob001pjl044nphhj04
- https://uibowl.io/name/%EC%9A%B0%EB%A6%AC%EB%8F%99%EB%84%A4GS?patterns=%EB%A7%88%EC%9D%B4%ED%8E%98%EC%9D%B4%EC%A7%80&imgId=cmlesg83100fll3044egry232
- https://uibowl.io/website/%EB%A6%AC%EC%8A%A4%EB%8B%9D%EB%A7%88%EC%9D%B8%EB%93%9C?patterns=%EB%A7%88%EC%9D%B4%ED%8E%98%EC%9D%B4%EC%A7%80&imgId=cmsssakfn0008l104ol1ypu26
- https://uibowl.io/website/%EC%9E%94%EB%94%94?patterns=%EB%8C%80%EC%8B%9C%EB%B3%B4%EB%93%9C&imgId=cmpz4uprc0003ie04h1ia0clk
- https://uibowl.io/website/%EC%B1%84%EB%84%90%ED%86%A1?patterns=AI&imgId=cmudq45mh001qjy04qd93j3wk

## 화면 9
판매처 설정. admin만(학생·교사 노출 0). 모바일 = runs/20261007-0848 화면 9 그대로 + 요청 5-2: 판매처 행 = 이름 + 연락처만(웹사이트 주소는 행에 표시하지 않음, rules.json app_exceptions.sheet-close).
예시 상태(9-mobile · 9-desktop): "우리 학교 판매처" 탭, 판매처 3곳(과학교재사 · 043-210-1100 / 한빛실험기기 · 043-255-3300 / 대한시약 · 02-555-7700) 위에 "판매처 등록" 폼이 열린 상태(판매처명 "과학나라" 입력 중, 연락처·웹사이트 주소 빈 값).
모바일 활성 탭: "시약". 위→아래: nav-pill → segmented-control → 검색 → 판매처 목록 → 하단 고정 "판매처 등록" → tab-bar. 폼 시트는 tab-bar 위.
데스크톱 배치: app-sidebar("판매처" 현재) | 본문 페이지 = 페이지 머리(왼쪽 "판매처" + "3곳" / 오른쪽 button-primary "판매처 등록") → 툴바(segmented-control 왼쪽, 검색 오른쪽) → data-table(판매처명 · 연락처 + 행 끝 ⋮) + 오른쪽 detail-drawer "판매처 등록" 폼(여러 칸 입력이라 모달 대신 드로어). 삭제 확인 = 가운데 ex-modal-card.
### 구성 요소
- app-sidebar: 데스크톱 전용. 공통 규격, 학교명 "샘플고등학교" + 메뉴 + "정OO · admin" + nav-account-menu (admin만)
- sidebar-item: 데스크톱 전용. admin 10개(공통 메뉴). 현재 = "판매처". 학생·교사에게는 이 화면이 없다 (admin만)
- nav-pill: 모바일 전용. "Lab_Stock" 워드마크 + 제목 "판매처 설정" + 현재 학교명 "샘플고등학교" + nav-account-menu ▾ (admin만)
- nav-account-menu: 모바일 = 학교명 옆 ▾, 데스크톱 = app-sidebar 맨 아래. "로그아웃" 1개. 하늘색 없음 (admin만)
- segmented-control: "우리 학교 판매처 / 공통 목록", 활성 탭 하나. 데스크톱 = 툴바 왼쪽 (admin만)
- segmented-control-active: 활성 탭 흰 pill("우리 학교 판매처"). 하늘색: 1px #2b9fe0 테두리(글자 #141414) (admin만)
- text-input: 판매처 검색("판매처 검색"), 폼 입력 3개 — "판매처명"(필수, caption "필수" #707070), "연락처", "웹사이트 주소"(판매처 연결 시 새 창으로 여는 주소, 목록 행에는 표시 안 함). 부가 정보 칸 없음. #f0f0f0, rounded 16, 포커스 링 2px #141414. 하늘색: 검색 아이콘 #2b9fe0 (admin만)
- vendor-register: "우리 학교 판매처" 블록 1개. 모바일 = 샘플고등학교 판매처 목록(행 = 판매처명 title + 연락처 caption #707070 + 오른쪽 더보기 "수정"·"삭제") + 하단 고정 button-primary "판매처 등록" → 등록·수정 폼 시트 → 저장 후 목록. 데스크톱 = 페이지 머리 "판매처 등록" + data-table + detail-drawer 폼. 하늘색: 더보기 아이콘 #2b9fe0, 방금 등록·수정한 행 #e6f4fc (admin만)
- data-table: 데스크톱 전용. 열 = 판매처명(정렬) · 연락처 · 행 끝 ⋮("수정" → 드로어 폼 / "삭제" → 확인 모달). 웹사이트 주소 열 없음. "공통 목록" 탭은 같은 2열 보기 전용(⋮ 없음). 하늘색: ⋮ 아이콘 #2b9fe0 (admin만)
- detail-drawer: 데스크톱 전용. 폭 480, #ffffff, 왼쪽 1px #f0f0f0 선, 여백 24. 헤더 = heading-3 "판매처 등록"(수정이면 "판매처 수정") + 오른쪽 위 × 닫기 → body-sm(#707070) "우리 학교에서만 보여요" → "라벨 | 입력" 행 판매처명 · 연락처 · 웹사이트 주소 → 아래 고정 button-outline "취소" + button-primary "저장"(1:2, 판매처명이 비면 "저장" 비활성). × 와 "취소"는 같은 동작 (admin만)
- ex-data-table-cell: 모바일 "공통 목록" 탭 보기 전용 2열(판매처명 · 연락처), 데스크톱 data-table 머리행·셀. 하늘색 없음 (admin만)
- ex-modal-card: 모바일 ① 등록·수정 폼 시트(예시): 헤더 = heading-3 "판매처 등록" + 오른쪽 위 × 닫기 → body-sm(#707070) "우리 학교에서만 보여요" → 세로 입력 3개(판매처명 · 연락처 · 웹사이트 주소, 사이 16) → button-outline "취소" + button-primary "저장"(1:2). ② 삭제 확인(모바일·데스크톱 공통): "이 판매처를 삭제할까요?" + × + "취소" + "삭제". 1px #e0e0e0 테두리, 그림자·딤 없음, 모바일 위쪽 rounded 24·tab-bar 위, 데스크톱 rounded 24 가운데. 핑크·하늘색 없음 (admin만)
- button-primary: "판매처 등록"(모바일 하단 고정 tab-bar 바로 위, 데스크톱 페이지 머리 오른쪽), 폼 "저장", 삭제 확인 "삭제"(#141414 채움, #ffffff 글자, rounded 9999, 높이 44 이상). 하늘색 없음 (admin만)
- button-outline: 폼 "취소", 삭제 확인 "취소"(#ffffff, 1px #e0e0e0, 라벨 #141414) (admin만)
- ex-empty-state-card: 학교 판매처 0건 "등록한 판매처가 없어요" + 등록 진입. 하늘색: 안내 아이콘 #2b9fe0 (admin만)
- ex-toast: "판매처를 저장했어요" / "판매처를 삭제했어요". 모바일 tab-bar 위, 데스크톱 오른쪽 아래. 하늘색: 완료 체크 아이콘 #2b9fe0 (admin만)
- tab-bar: 모바일 전용 하단 탭바 1개(공통 규격). 데스크톱에는 두지 않는다. 하늘색: 활성 tab-item 아이콘 #2b9fe0만 (admin만)
- tab-item: "홈" · "시약" · "QR 스캔" · "기록" 4개. 활성 = "시약", 비활성 3개 #707070 (admin만)
### 반영한 레퍼런스
- https://uibowl.io/name/%EC%A7%91%EC%A7%80%EC%BC%9C?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&imgId=cmubaul16001ijs04tf5nxq2h
- https://uibowl.io/name/%EC%91%A5%EC%91%A5%EC%B0%B0%EC%B9%B5?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&imgId=cmub7kvlz0007js04xdyeh3c1
- https://uibowl.io/website/%EC%B1%84%EB%84%90%ED%86%A1?patterns=AI&imgId=cmudq45mh001qjy04qd93j3wk
- https://uibowl.io/website/%EC%82%AC%EB%B0%A9%EB%84%B7?patterns=%EB%A7%88%EC%9D%B4%ED%8E%98%EC%9D%B4%EC%A7%80&imgId=cmu4rq6wd000jjm04e29a62hh

## 화면 10
사용 기록 내역. 학생·교사·admin 모두. 샘플고등학교 기록만. 사용일로 묶고 사용일 최신순(같은 날 안에서는 기록 시각 최신순). 기록한 날이 사용일과 다를 때만 회색 캡션 "{M}월 {D}일에 기록". 모바일 = runs/20261007-0744 화면 10 그대로.
예시 상태: "전체", 기간 "최근 1개월". ① "10월 7일 · 오늘": 염산 · 학생 이OO · 14:05 · 20 mL / 질산은 · 교사 김OO · 10:20 · 2 g ② "10월 6일": 수산화나트륨 · 학생 박OO · 15:40 · 10 g ③ "10월 3일": 에탄올 · 교사 김OO · 50 mL + "10월 7일에 기록" / 염산 · 학생 최OO · 30 mL + "10월 6일에 기록". 데스크톱 프레임은 첫 행(염산 · 이OO)을 눌러 detail-drawer가 열린 상태.
모바일 활성 탭: "기록". 위→아래: nav-pill → segmented-control + 기간 선택 → 검색 → 사용일 그룹 목록 → tab-bar.
데스크톱 배치: app-sidebar("기록" 현재) | 본문 = 페이지 머리(왼쪽 "기록" + "5건" / 오른쪽 검색) → 툴바(segmented-control "전체 / 내 기록" + 기간 드롭다운) → data-table(사용일 묶음 머리 행 + 기록 행) → 페이지 번호 + 오른쪽 detail-drawer(기록 상세).
### 구성 요소
- app-sidebar: 데스크톱 전용. 공통 규격, 학교명 "샘플고등학교" + 역할별 메뉴 + nav-account-menu
- sidebar-item: 데스크톱 전용. 학생 5개 / 교사 8개 / admin 10개(공통 메뉴). 현재 = "기록"
- nav-pill: 모바일 전용. "Lab_Stock" 워드마크 + 제목 "사용 기록 내역" + 현재 학교명 "샘플고등학교" + nav-account-menu ▾
- nav-account-menu: 모바일 = 학교명 옆 ▾, 데스크톱 = app-sidebar 맨 아래. "로그아웃" 1개. 하늘색 없음
- segmented-control: "전체 / 내 기록", 한 번에 하나. 데스크톱 = 툴바 왼쪽
- segmented-control-active: 선택 "전체" 흰 pill. 하늘색: 1px #2b9fe0 테두리(글자 #141414)
- text-input: 기간 선택 상자("최근 1개월" ▾, 사용일 기준 — 데스크톱은 드롭다운: 오늘 · 최근 7일 · 최근 1개월 · 이번 학기)와 "시약명 검색"(#f0f0f0, rounded 16, 포커스 링 2px #141414). 하늘색: 검색·▾ 아이콘 #2b9fe0
- data-table: 데스크톱 전용. 열 = 사용일(정렬, 활성 ↓ #2b9fe0) · 시약명 · 사용자 · 사용량 · 기록 시각. 사용일 묶음 머리 행(caption #707070 "10월 7일 · 오늘" / "10월 6일" / "10월 3일", 왼쪽 #2b9fe0 짧은 인디케이터). 기록한 날이 다르면 시약명 아래 caption(#707070) "10월 7일에 기록". 선택 행 #e6f4fc. 0건이면 표 머리를 남기고 표 안 ex-empty-state-card
- ex-data-table-cell: 모바일 기록 목록 — 사용일 그룹 헤더(caption #707070, 그룹 사이 24) 아래 행 = 시약명(title) + 보조줄 body-sm(#707070) "학생 이OO · 14:05" + 오른쪽 사용량(body). 기록한 날이 다르면 보조줄 아래 caption "10월 7일에 기록"(보조줄은 이름만). 행 사이 12. 행을 누르면 상세. 데스크톱 data-table 머리행·셀 chrome. 하늘색: 누른 행 #e6f4fc, 그룹 헤더 왼쪽 #2b9fe0 인디케이터
- detail-drawer: 데스크톱 전용 기록 상세. 폭 480, #ffffff, 왼쪽 1px #f0f0f0 선, 여백 24, × 닫기. 시약명 heading-3 "염산" + 사용량 display "20 mL" → "항목 | 값" 행 "사용자 · 학생 이OO" · "사용일 · 2026-10-07" · "기록한 날"(다를 때만) · "메모" → msds-entry → 아래 고정 button-outline "닫기"
- ex-modal-card: 모바일 전용 기록 상세 시트(tab-bar 위, × 닫기). 시약명(heading-3) + 사용량(display) → "사용자" · "사용일" · "기록한 날"(다를 때만) · "메모" → msds-entry → button-outline "닫기". 데스크톱은 detail-drawer. 하늘색 없음
- msds-entry: 상세 안 button-pill-soft "MSDS 보기 ›"(#f3f3f3, 라벨 #141414, rounded 9999, 높이 44 이상) → 화면 16(모바일 MSDS 전용 화면, 데스크톱은 드로어가 MSDS 요약으로 바뀜). 학생·교사·admin 모두. 하늘색: › 아이콘 #2b9fe0
- button-outline: 상세 "닫기"(#ffffff, 1px #e0e0e0, 라벨 #141414, rounded 9999, 높이 44 이상)
- ex-empty-state-card: 결과 0건 "아직 사용 기록이 없어요" + 한 줄 "기간을 바꿔 보세요". 하늘색: 안내 아이콘 #2b9fe0
- tab-bar: 모바일 전용 하단 탭바 1개(공통 규격). 데스크톱에는 두지 않는다. 하늘색: 활성 tab-item 아이콘 #2b9fe0만
- tab-item: "홈" · "시약" · "QR 스캔" · "기록" 4개. 활성 = "기록", 비활성 3개 #707070
### 반영한 레퍼런스
- https://uibowl.io/name/%EB%AF%B8%EB%8B%88%EC%8A%A4%ED%83%81?patterns=%EB%82%B4%EC%97%AD&imgId=cmty2l8bh002gl404x15qm1dq
- https://uibowl.io/name/%ED%86%A0%EC%8A%A4%EC%A6%9D%EA%B6%8C?patterns=%EB%82%B4%EC%97%AD&imgId=cmrufrdyn0003jj04z74mofuh
- https://uibowl.io/website/%EB%BF%8C%EB%A6%AC%EC%98%A4?patterns=%EB%82%B4%EC%97%AD&imgId=cmu1vvu9l000vjv04jiybtxr8
- https://uibowl.io/website/%EB%A6%AC%EB%94%94?patterns=%EB%82%B4%EC%97%AD&imgId=cmuq7e6jd000wjs046c714kre
- https://uibowl.io/website/%EB%A6%AC%EC%BA%90%EC%B9%98?patterns=%EA%B2%80%EC%83%89&imgId=cmihk0pui000pl804eqhg1j1k

## 화면 11
시약장 설정. 학생·교사·admin 모두. 교사·admin은 전환·추가·이름 바꾸기·QR 인쇄·삭제·문 형태·단 수·칸 분류 편집·칸 시트(넣기·빼기), 학생은 전환과 배치도·칸 목록 보기만. 모바일 = runs/20261006-1223 화면 11 그대로.
예시 상태: 시약장 2개 "(1) 1번 시약장"(활성) · "(2) 2번 시약장". 1번 = 양문형 · 4단 8칸. 좌1단 = 산 + 염기(mix-warning), 좌2단 = 유기, 좌3단 = 인화성, 좌4단 = 기타, 우1단 = 산화제, 우2단 = 무기염, 우3단 = 독성, 우4단 = 기타. 시약 수: 좌1단 2, 좌2단 3, 우1단 1, 우3단 1. 선택 칸 = 좌1단. "칸 없음" 시약 2개.
모바일 활성 탭: "시약". 위→아래: nav-pill → cabinet-switcher(+ cabinet-add) → 시약장 이름 + "양문형 · 4단" → (교사·admin) 관리 줄 → (교사·admin) 문 형태·단 수 → 배치도 → 범례 → (교사·admin) 선택 칸 분류 칩 → mix-warning → "칸 없음" 시약 → (교사·admin) 하단 고정 "저장" → tab-bar.
데스크톱 배치: app-sidebar("시약장" 현재) | 본문 페이지 = 페이지 머리(왼쪽 "시약장" + "2개") → 가운데 단일 열 폭 640: cabinet-switcher 한 줄(+ cabinet-add) → 시약장 이름 + 관리 줄 → "라벨 | 입력" 행 문 형태 · 단 수 → 배치도 + 범례 → 선택 칸 분류 → mix-warning → "칸 없음" 시약 → (교사·admin) 본문 하단 고정 바 "저장". 칸 시트 = 칸에 붙은 팝오버, QR 인쇄 = 가운데 ex-modal-card.
### 구성 요소
- app-sidebar: 데스크톱 전용. 공통 규격, 학교명 "샘플고등학교" + 역할별 메뉴 + nav-account-menu
- sidebar-item: 데스크톱 전용. 학생 5개 / 교사 8개 / admin 10개(공통 메뉴). 현재 = "시약장"
- nav-pill: 모바일 전용. "Lab_Stock" 워드마크 + 제목 "시약장 설정" + 현재 학교명 "샘플고등학교" + nav-account-menu ▾. 학교 전환 없음
- nav-account-menu: 모바일 = 학교명 옆 ▾, 데스크톱 = app-sidebar 맨 아래. "로그아웃" 1개. 하늘색 없음
- cabinet-switcher: 시약장 전환 pill 가로 한 줄, pill마다 cabinet-number + 이름. 활성 = #e6f4fc 채움 + 1px #2b9fe0 테두리 + 라벨 #141414, 비활성 #f3f3f3. 모바일은 넘치면 가로 스크롤, 데스크톱은 한 줄에 모두. 저장 안 한 편집이 있으면 상태 11-unsaved 모달. 모든 역할. 하늘색: 활성 pill 채움·테두리
- cabinet-number: pill마다 이름 앞 작은 원(#ffffff, 1px #e0e0e0, rounded 9999) 안 숫자 "1"·"2"(label #141414). 고정 번호, 이름을 바꿔도 그대로. 시약장 이름 heading-3 앞에도 같은 원. 핑크·하늘색 글자 없음
- cabinet-add: cabinet-switcher 줄 끝 button-pill-soft "+ 시약장 추가" → "(3) 3번 시약장" 만들기. 하늘색: "+" 아이콘 #2b9fe0 (교사·admin만)
- cabinet-edit: 편집 영역 블록 1개. 관리 줄 = button-outline "이름 바꾸기" + qr-print + 조용한 텍스트 동작 "삭제"(link #141414, 핑크 금지) → cabinet-door-select · cabinet-shelf-select(데스크톱은 "라벨 | 입력" 행) · 선택 칸 storage-class-chip 묶음 · button-primary "저장"(모바일 하단 전폭, 데스크톱 본문 하단 고정 바). "이름 바꾸기"는 ex-modal-card 한 칸 입력 (교사·admin만)
- qr-print: 관리 줄 "이름 바꾸기" 옆 button-outline "QR 인쇄"(#ffffff, 1px #e0e0e0, 라벨 #141414, rounded 9999, 높이 44 이상). 상태 11-print의 qr-print-sheet(모바일 바텀시트, 데스크톱 가운데 ex-modal-card). 하늘색: 인쇄 아이콘 #2b9fe0 (교사·admin만)
- cabinet-door-select: 문 형태 pill "양문형 / 단문형", 하나만, 예시 "양문형". 하늘색: 선택 #e6f4fc + 1px #2b9fe0 테두리(글자 #141414) (교사·admin만)
- cabinet-shelf-select: 단 수 pill "3단 / 4단", 하나만, 예시 "4단". 하늘색: 선택 #e6f4fc + 1px #2b9fe0 테두리 (교사·admin만)
- cabinet-slot: 활성 시약장 정면 배치도 칸(8칸, #f3f3f3, rounded 16, 분류 이름 label #141414, 없으면 "미지정" #707070). 왼쪽 단 라벨, 위 문 라벨 "좌"/"우", 양문형은 가운데 통로. 누르면 칸 시트(상태 11-slot; 모바일 바텀시트, 데스크톱 칸에 붙은 팝오버) — 교사·admin 넣기·빼기, 학생 목록 보기만. 좌1단 오른쪽 위 #141414 경고 아이콘. 하늘색: 선택 칸 #e6f4fc + 2px #2b9fe0 테두리(글자 #141414)
- slot-count: 시약이 있는 칸 안 작은 pill(#ffffff, rounded 9999, label #141414) "2"·"3"·"1"·"1". 빈 칸 없음. 모든 역할. 핑크·하늘색 없음
- storage-class-chip: 분류 칩 8종 "유기·산·염기·산화제·인화성·무기염·독성·기타". cabinet-edit 안 선택 칸(좌1단) 분류 고르기(여러 개, 예시 "산"·"염기") + 배치도 아래 범례(보기 전용, 학생은 범례만). 하늘색: 선택 칩 #e6f4fc + 1px #2b9fe0 테두리
- mix-warning: "주의사항" 블록(#fbe9f0 바탕, rounded 16, 제목 heading-4 #141414 + 줄마다 #d6246a 경고 아이콘 + #141414 body-sm) "좌1단: 산과 염기는 섞이면 위험해요. 다른 칸에 나눠 보관하세요". 학생에게도 보기 전용. 하늘색 없음
- reagent-row: 소제목 heading-4 "칸 없음 시약 (2)" + 행(시약명 title + 재고량 body + caption "칸 없음" #707070, #f3f3f3, rounded 16, 사이 12). 누르면 화면 3. 하늘색: 누른 행 #e6f4fc
- ex-modal-card: "이름 바꾸기" 한 칸 입력(#ffffff, 1px #e0e0e0, rounded 24, 여백 24, × 닫기): heading-3 "시약장 이름" + text-input + caption "번호 1은 바뀌지 않아요"(#707070) + "취소" + "저장". 모바일 tab-bar 위, 데스크톱 가운데 (교사·admin만)
- text-input: 이름 시트 "시약장 이름"(#f0f0f0, rounded 16, 포커스 링 2px #141414) (교사·admin만)
- button-outline: 관리 줄 "이름 바꾸기", 이름 시트 "취소" (교사·admin만)
- button-primary: cabinet-edit "저장"(모바일 tab-bar 바로 위 전폭, 데스크톱 본문 하단 고정 바 오른쪽), 이름 시트 "저장". 하늘색 없음 (교사·admin만)
- ex-toast: "시약장 설정을 저장했어요" / "이름을 바꿨어요" / "3번 시약장을 추가했어요". 모바일 tab-bar 위, 데스크톱 오른쪽 아래. 하늘색: 완료 체크 아이콘 #2b9fe0 (교사·admin만)
- tab-bar: 모바일 전용 하단 탭바 1개(공통 규격). 데스크톱에는 두지 않는다. 하늘색: 활성 tab-item 아이콘 #2b9fe0만
- tab-item: "홈" · "시약" · "QR 스캔" · "기록" 4개. 활성 = "시약", 비활성 3개 #707070
### 반영한 레퍼런스
- https://uibowl.io/name/%EC%9B%8C%ED%81%AC%EC%98%A8?patterns=%ED%8A%9C%ED%86%A0%EB%A6%AC%EC%96%BC&imgId=cmudxbzpd0028l7046bsxhka0
- https://uibowl.io/name/%ED%8E%98%EC%9D%B4%EC%9B%8C%ED%81%AC?patterns=%ED%8A%9C%ED%86%A0%EB%A6%AC%EC%96%BC&imgId=cmtzo5k4p004jl704vz543akg
- https://uibowl.io/website/%EC%9E%94%EB%94%94?patterns=%EC%84%A4%EC%A0%95&imgId=cmpz4z8q30005ju04h03ux7s6
- https://uibowl.io/website/%EC%9C%84%EC%8B%9C%EC%BC%93?patterns=%EA%B3%84%EC%A2%8C&imgId=cmunb5pib0007l204n4d6jnbv

## 화면 12
QR 찾기(모바일 제목 "QR 스캔"). 학생·교사·admin 모두. 샘플고등학교 시약장 QR만 연다. 다른 학교 QR·인식 실패면 안내 + 시약장 번호로 직접 찾기(N1). 결과는 상태 화면 12-result. 모바일 = runs/20261006-1223 화면 12 그대로.
모바일 활성 탭: "QR 스캔". 위→아래: nav-pill → segmented-control "QR 스캔 / 번호로 찾기" → 안내 → 카메라 프레임 → 안내 1줄 → 하단 고정 "시약장 번호로 찾기" → tab-bar.
데스크톱 배치: app-sidebar("QR 찾기" 현재) | 본문 = 페이지 머리 "QR 찾기" + body-sm(#707070) "시약장 QR을 비추거나 번호를 입력하세요" → 2열 카드: 왼쪽 qr-scan(웹캠 미리보기), 오른쪽 qr-manual-entry(넓은 번호 입력 + "찾기"). 결과 = 오른쪽 detail-drawer에 qr-result-sheet 내용(시약장 요약 + 시약 표 + "배치도 보기"), 행을 누르면 드로어가 화면 3 시약 상세로.
### 구성 요소
- app-sidebar: 데스크톱 전용. 공통 규격, 학교명 "샘플고등학교" + 역할별 메뉴 + nav-account-menu
- sidebar-item: 데스크톱 전용. 학생 5개 / 교사 8개 / admin 10개(공통 메뉴). 현재 = "QR 찾기"
- nav-pill: 모바일 전용. 닫기(이전 화면) + 제목 "QR 스캔" + 현재 학교명 "샘플고등학교" + nav-account-menu ▾. 하늘색: 닫기 아이콘 #2b9fe0
- nav-account-menu: 모바일 = 학교명 옆 ▾, 데스크톱 = app-sidebar 맨 아래. "로그아웃" 1개. 하늘색 없음
- segmented-control: 모바일 전용 "QR 스캔 / 번호로 찾기" 두 탭, 기본 "QR 스캔". 데스크톱은 두 카드를 나란히 두어 쓰지 않는다
- segmented-control-active: 모바일 선택 탭 흰 pill. 하늘색: 1px #2b9fe0 테두리(글자 #141414)
- qr-scan: QR 스캔 본문. heading-4 "시약장 문에 붙은 QR을 맞춰주세요" + body-sm(#707070) "카메라는 시약장 QR을 읽는 데만 사용해요" → 카메라 미리보기(#262626, rounded 24) 안 1:1 코너 브라켓(#ffffff 선) → caption(#707070) "QR 인쇄 라벨의 번호로도 찾을 수 있어요" → button-pill-soft "플래시"(모바일만). 데스크톱 = 왼쪽 카드(#ffffff, 1px #f0f0f0, rounded 24, 여백 24) 안 웹캠 미리보기. 권한 없음 = #f3f3f3 자리 + "카메라 권한이 필요해요" + button-outline "권한 설정". 실패·다른 학교 QR = #141414 경고 아이콘 + body "QR을 읽지 못했어요. 시약장 번호로 찾아보세요" / "샘플고등학교 시약장 QR이 아니에요"(핑크 금지). 하늘색: 인식 중 프레임 선 #2b9fe0
- qr-manual-entry: 모바일 ① 하단 고정 button-outline "시약장 번호로 찾기"(→ "번호로 찾기" 탭) ② 탭 본문: 라벨 "시약장 번호" + 숫자 text-input(플레이스홀더 "예: 1") + 전폭 button-primary "찾기". 데스크톱 = 오른쪽 카드(#ffffff, 1px #f0f0f0, rounded 24, 여백 24): heading-4 "시약장 번호로 찾기" + 넓은 숫자 text-input + 오른쪽 button-primary "찾기". 비면 비활성. 없는 번호 = #141414 아이콘 + body-sm "샘플고등학교에 이 번호의 시약장이 없어요". 찾으면 결과(모바일 12-result 시트, 데스크톱 detail-drawer). 하늘색: 입력 왼쪽 아이콘 #2b9fe0
- text-input: qr-manual-entry "시약장 번호" 숫자 입력(#f0f0f0, rounded 16, 포커스 링 2px #141414)
- detail-drawer: 데스크톱 전용 결과 자리(이 프레임에서는 닫힘). 열리면 qr-result-sheet 내용 — 제목 cabinet-number + "1번 시약장" + × 닫기 → caption "양문형 · 4단 · 시약 4개" → 시약 표(시약명 · 칸 위치 · 재고 · badge-low-stock) → button-pill-soft "배치도 보기"(→ 화면 11)
- qr-result-sheet: 스캔·번호 찾기 결과(모바일 = 상태 화면 12-result 바텀시트, 데스크톱 = detail-drawer 안). 이 프레임에서는 닫힘
- button-pill-soft: qr-scan "플래시"(모바일)
- button-outline: 모바일 하단 고정 "시약장 번호로 찾기", 권한 상태 "권한 설정"
- button-primary: qr-manual-entry "찾기"(모바일 "번호로 찾기" 탭, 데스크톱 오른쪽 카드). 하늘색 없음
- tab-bar: 모바일 전용 하단 탭바 1개(공통 규격, QR 스캔 탭을 키우지 않음). 데스크톱에는 두지 않는다. 하늘색: 활성 tab-item 아이콘 #2b9fe0만
- tab-item: "홈" · "시약" · "QR 스캔" · "기록" 4개. 활성 = "QR 스캔", 비활성 3개 #707070
### 반영한 레퍼런스
- https://uibowl.io/name/%EC%B9%B4%EC%B9%B4%EC%98%A4T?patterns=%EC%B4%AC%EC%98%81%ED%95%98%EA%B8%B0&patternName=QR%EC%8A%A4%EC%BA%94-%EC%9E%90%EC%A0%84%EA%B1%B0%20%EB%B0%98%EB%82%A9
- https://uibowl.io/name/Atoms?patterns=%EC%B4%AC%EC%98%81%ED%95%98%EA%B8%B0&imgId=cm3vp36i0000al70czvfw3f09
- https://uibowl.io/website/%EB%A6%AC%EC%8A%A4%EB%8B%9D%EB%A7%88%EC%9D%B8%EB%93%9C?patterns=%EA%B2%80%EC%83%89&imgId=cmsss8y490003jv04xvtyntbp
- https://uibowl.io/website/%EB%A6%AC%EC%BA%90%EC%B9%98?patterns=%EB%82%B4%EC%97%AD&imgId=cmihk1yub0005li04jv0iyqbi

## 화면 13
홈. 로그인 후 첫 화면, 학생·교사·admin 모두. 같은 틀에서 역할마다 quick-action·카드 구성이 다르다. 모바일 = runs/20261006-1223 화면 13 그대로.
예시 상태: 전체 시약 42종, 재고 부족 3종(염산 · 50 mL, 에탄올 · 200 mL, 질산은 · 5 g), MSDS 없는 시약 4종, 시약장 2개(칸 16개 중 지정 14 · 미지정 2), 재주문 알림 3건, 최근 사용 기록 3줄.
모바일 활성 탭: "홈". 위→아래: nav-pill → quick-action(교사·admin 3칸 2+1, 학생 2칸) → home-summary ① 재고 요약 → (교사·admin) reorder-alert-card → home-summary ② 시약장 요약 → 최근 사용 기록 카드 → tab-bar.
데스크톱 배치: app-sidebar("홈" 현재) | 본문 = 페이지 머리(왼쪽 heading-2 "샘플고등학교" + body-sm(#707070) "오늘 10월 7일 · 전체 시약 42종" / 오른쪽 quick-action 버튼 줄) → 맨 위 전폭 숫자 타일 줄 "지금 처리할 것"(교사·admin = 재고 부족 3 · 재주문 알림 3 · MSDS 없는 시약 4 / 학생 = 재고 부족 3) → 아래 3열 위젯 격자(최근 사용 기록 data-table 2칸 폭 · 재고 부족 · 시약장 요약), 위젯마다 머리 제목 + 오른쪽 "전체 보기 ›".
### 구성 요소
- app-sidebar: 데스크톱 전용. 공통 규격, 학교명 "샘플고등학교" + 역할별 메뉴 + nav-account-menu
- sidebar-item: 데스크톱 전용. 학생 5개 / 교사 8개 / admin 10개(공통 메뉴). 현재 = "홈"
- nav-pill: 모바일 전용. "Lab_Stock" 워드마크 + 현재 학교명 "샘플고등학교" + nav-account-menu ▾. 학교 선택·전환 없음
- nav-account-menu: 모바일 = 학교명 옆 ▾, 데스크톱 = app-sidebar 맨 아래. "로그아웃" 1개. 하늘색 없음
- quick-action: 역할별 작업 바로가기. 모바일 = 칸(#f3f3f3, rounded 16, 여백 16, 위 원형 아이콘 바탕 #e6f4fc 안 #2b9fe0 아이콘 + 아래 label #141414, 사이 12) — 교사 3칸 "사용 기록 입력"(화면 4) · "입고"(화면 7, stock-intake 진입) · "시약장 설정"(화면 11), admin 3칸 "입고"(stock-intake 진입) · "사용자 관리"(화면 8, user-manage 진입) · "시약장 설정"(화면 11), 2+1 배치. 학생 2칸 "사용 기록 입력" · "시약장 보기"(보기 전용). 데스크톱 = 페이지 머리 오른쪽 버튼 줄(같은 역할별 항목·같은 연결): 마지막 항목은 button-primary, 나머지는 button-outline(교사 "사용 기록 입력" · "시약장 설정" + "입고" / admin "사용자 관리" · "시약장 설정" + "입고" / 학생 "시약장 보기" + "사용 기록 입력"). 하늘색: 모바일 아이콘 #2b9fe0 + 바탕 #e6f4fc, 누른 칸 #e6f4fc
- home-summary: 모바일 = 요약 카드 2장(#ffffff, 1px #f0f0f0, rounded 24, 여백 24). ① 재고 요약: heading-4 "재고 부족 3개" + badge-low-stock "3" → 부족 시약 칩 줄(#f3f3f3, rounded 9999, "염산 · 50 mL" 등, → 화면 3) → "전체 시약 42종". ② 시약장 요약: heading-4 "시약장 요약 ›"(→ 화면 11) → display "2개" → 구간 막대(지정 #2b9fe0 + 미지정 #e0e0e0, rounded 9999) → body-sm(#707070) "칸 16개 중 지정 14 · 미지정 2". 데스크톱 = ⓐ 숫자 타일(#ffffff, 1px #f0f0f0, rounded 24, 여백 24, caption 이름 + display 숫자): "재고 부족 3"(badge-low-stock 포함, → 화면 2 재고 부족) · (교사·admin) "MSDS 없는 시약 4"(→ 화면 2 MSDS 없는 시약 필터) ⓑ 위젯 "재고 부족"(부족 시약 칩 3개 + "전체 보기 ›") ⓒ 위젯 "시약장 요약"(같은 막대·문구 + "전체 보기 ›"). 0개면 "부족한 시약이 없어요" / 시약장 0개면 ex-empty-state-card. 하늘색: 막대 지정 구간, › 아이콘
- badge-low-stock: 재고 요약 개수 배지 "3", reorder-alert-card 안 "재고 부족"(#d6246a 채움, #ffffff label). 데스크톱 = "재고 부족 3" 타일 숫자 옆. 하늘색 없음
- reorder-alert-card: "재주문 알림" 카드(#f3f3f3, 테두리 없음, rounded 24, 여백 24). 모바일 = heading-4 "재주문 알림" + badge-low-stock + button-pill-soft "3건 ›"(→ 화면 6) + body "필요량보다 적은 시약이 3종 있어요". 데스크톱 = 숫자 타일 줄의 타일 1개(같은 #f3f3f3 카드: caption "재주문 알림" + display "3" + badge-low-stock + "3건 ›"). 판매처 연결 버튼 없음. 하늘색 없음 (교사·admin만)
- data-table: 데스크톱 전용 "최근 사용 기록" 위젯(2칸 폭). 열 = 사용일 · 시약명 · 사용자 · 사용량, 3행("10월 7일 · 염산 · 학생 이OO · 20 mL" 등), 머리 오른쪽 "전체 보기 ›"(→ 화면 10). 행을 누르면 화면 10 기록 상세
- reagent-row: 모바일 최근 사용 기록 카드(#ffffff, 1px #f0f0f0, rounded 24, 제목 heading-4 "최근 사용 기록") 안 3줄 = 시약명(title) + "학생 이OO · 20 mL"(body) + "오늘 14:05"(caption #707070), #f3f3f3, rounded 16, 사이 12. 누르면 화면 10. 하늘색: 누른 행 #e6f4fc
- button-pill-soft: 모바일 "더 보기 ›"(화면 10), reorder-alert-card "3건 ›"(교사·admin만), 데스크톱 위젯 머리 "전체 보기 ›". 하늘색: reorder-alert-card 밖 버튼의 › 아이콘만 #2b9fe0
- ex-empty-state-card: ① 시약장 0개 "등록된 시약장이 없어요" + 교사·admin button-outline "시약장 추가", 학생 body-sm(#707070) "선생님이 시약장을 등록하면 보여요". ② 최근 사용 기록 0건 "아직 사용 기록이 없어요" + button-outline "사용 기록 입력". 데스크톱은 해당 위젯 안. 하늘색: 안내 아이콘 #2b9fe0
- button-outline: ex-empty-state-card "시약장 추가"(교사·admin만), "사용 기록 입력", 데스크톱 quick-action 버튼 줄의 보조 버튼
- button-primary: 데스크톱 quick-action 버튼 줄의 마지막 버튼(교사·admin "입고", 학생 "사용 기록 입력"). #141414 채움, #ffffff 글자, rounded 9999, 높이 44 이상. 하늘색 없음
- tab-bar: 모바일 전용 하단 탭바 1개(공통 규격). 데스크톱에는 두지 않는다. 하늘색: 활성 tab-item 아이콘 #2b9fe0만
- tab-item: "홈" · "시약" · "QR 스캔" · "기록" 4개. 활성 = "홈". 역할별 작업은 tab-item으로 두지 않는다
### 반영한 레퍼런스
- https://uibowl.io/name/%EB%B9%BC%EA%B8%B0?patterns=%EB%A9%94%EC%9D%B8
- https://uibowl.io/name/RailOne?patterns=%EB%A9%94%EC%9D%B8&patternName=%ED%99%88
- https://uibowl.io/website/%EC%82%AC%EB%B0%A9%EB%84%B7?patterns=%EB%A9%94%EC%9D%B8&imgId=cmu4rq7ga000pjm04hw12bpue
- https://uibowl.io/website/%EB%8B%B9%EA%B7%BC%20%EB%B9%84%EC%A6%88%EB%8B%88%EC%8A%A4?patterns=%EB%8C%80%EC%8B%9C%EB%B3%B4%EB%93%9C&imgId=cmso68mja000el704vilcy6lq
- https://uibowl.io/website/%EB%A6%AC%EC%BA%90%EC%B9%98?patterns=%EB%8C%80%EC%8B%9C%EB%B3%B4%EB%93%9C&imgId=cmihk6p83000slb04vu0b6tso
- https://uibowl.io/website/%EB%A7%88%EC%9D%B4%ED%81%AC%EB%A1%9C%EC%86%8C%ED%94%84%ED%8A%B8%20%ED%81%B4%EB%9E%98%EB%A6%AC%ED%8B%B0%20(Microsoft%20Clarity)?patterns=AI&imgId=cmt17smig000klc04qa188qv5

## 화면 16
MSDS 요약(새 화면, rules.json msds_summary). 학생·교사·admin 모두(둘러보기도 같음). msds-entry "MSDS 보기"(화면 3·10 등)가 바깥 사이트 대신 이 화면을 연다. 역할별 차이 없음. 요약은 물질안전보건자료(한국산업안전보건공단) 내용을 서버에서 가져와 보여 준다(연결 값은 서버에서만, N2).
예시 상태(16-mobile · 16-desktop): 질산은(샘플고등학교 시약, 보관 분류 산화제). 신호어 "위험". 그림문자 3개 — 산화성 · 부식성 · 수생환경 유해성. 항목 요약 —
2. 유해·위험성: 화재를 강렬하게 할 수 있어요(산화제) / 피부에 심한 화상과 눈 손상을 일으켜요 / 수생생물에 매우 유독하고 오래 영향을 줘요
4. 응급조치 요령: 눈에 들어가면 물로 15분 이상 씻고 의사의 진료를 받아요 / 피부에 묻으면 오염된 옷을 벗고 물로 씻어요 / 삼켰을 때 억지로 토하게 하지 마세요
7. 취급 및 저장방법: 가연성 물질·환원제와 떨어뜨려 보관해요 / 빛을 피해 갈색 병에, 서늘하고 건조한 곳에 둬요 / 용기를 꼭 닫아 둬요
8. 노출방지 및 개인보호구: 보안경·내화학 장갑·실험복을 착용해요 / 가루가 날리면 국소 배기 장치를 켜요 / 작업 뒤 손을 씻어요
모바일 활성 탭: "시약". 위→아래: nav-pill(‹ + "MSDS · 질산은" + 학교명) → 출처 줄 → msds-summary(신호어 → 그림문자 줄 → 항목 2·4·7·8 카드) → msds-original-link(맨 아래 전폭) → tab-bar. 좌우 여백 16, 블록 사이 24.
데스크톱 배치: app-sidebar("시약" 현재) | 본문 = 화면 2 시약 목록(data-table, "질산은" 행 #e6f4fc 선택) + 오른쪽 detail-drawer 480 안: "‹ 시약 상세"(화면 3에서 왔을 때) + × 닫기 → heading-3 "MSDS · 질산은" + 출처 줄 → 항목 바로가기 줄(2 · 4 · 7 · 8) → msds-summary → 드로어 아래 고정 msds-original-link.
### 구성 요소
- app-sidebar: 데스크톱 전용. 공통 규격, 학교명 "샘플고등학교" + 역할별 메뉴 + nav-account-menu
- sidebar-item: 데스크톱 전용. 학생 5개 / 교사 8개 / admin 10개(공통 메뉴). 현재 = "시약"
- nav-pill: 모바일 전용 헤더. 뒤로가기 ‹(이전 화면 — 화면 3 또는 10) + heading-3 "MSDS · 질산은" + 현재 학교명 "샘플고등학교"(caption) + nav-account-menu ▾. 그 아래 출처 줄 caption(#707070) "물질안전보건자료 · 한국산업안전보건공단". 하늘색: 뒤로가기 아이콘 #2b9fe0
- nav-account-menu: 모바일 = 학교명 옆 ▾, 데스크톱 = app-sidebar 맨 아래. "로그아웃" 1개. 하늘색 없음
- data-table: 데스크톱 전용. 드로어 뒤 화면 2 시약 표(열·정렬·페이지 번호 화면 2와 같음), 선택 행 "질산은" #e6f4fc
- detail-drawer: 데스크톱 전용. 폭 480, 높이 900, #ffffff, 왼쪽 1px #f0f0f0 선, 여백 24, 딤 없음. 위→아래: 조용한 텍스트 동작 "‹ 시약 상세"(link #141414, 화면 3 드로어에서 왔을 때만) + 오른쪽 위 × 닫기 → heading-3 "MSDS · 질산은" → 출처 줄 caption(#707070) "물질안전보건자료 · 한국산업안전보건공단" → 항목 바로가기 줄(조용한 텍스트 동작 "2. 유해·위험성" · "4. 응급조치" · "7. 취급·저장" · "8. 보호구", 누르면 그 항목으로 스크롤, 현재 항목 아래 #2b9fe0 밑줄, 글자 #141414) → msds-summary(드로어 안 스크롤) → 아래 고정 줄(위 1px #f0f0f0 선) msds-original-link. 하늘색: × 아이콘 #2b9fe0, 바로가기 밑줄
- msds-summary: 요약 본문. ① 신호어 pill "위험"(#141414 채움, #ffffff label, rounded 9999. "경고"면 #f3f3f3 채움 + #141414 label) — 핑크·빨강 없음 → ② 그림문자 줄: ghs-pictogram 3개 가로(사이 16) → ③ 항목 카드 4장(#ffffff, 1px #f0f0f0 테두리, rounded 24, 여백 24, 사이 12): 제목 title "2. 유해·위험성" · "4. 응급조치 요령" · "7. 취급 및 저장방법" · "8. 노출방지 및 개인보호구"(번호 포함 원문 항목명) + 요약 3줄(body #141414, 줄마다 글머리) + 조용한 텍스트 동작 "더 보기"(link #141414, 누름 영역 44 이상, 누르면 그 카드가 펼쳐져 전체 내용). 내용 없는 항목 = 카드 안 body #707070 "내용이 없어요". 불러오는 중 = msds-skeleton(상태 16-loading), 실패 = ex-empty-state-card "요약을 불러오지 못했어요" + msds-original-link(상태 16-fail), 공단 MSDS가 아니면(직접 입력 주소) 요약 없이 msds-original-link만(상태 16-no-summary). 모바일·데스크톱 같은 순서. 하늘색: "더 보기" 옆 ▾ 아이콘 #2b9fe0
- ghs-pictogram: GHS 그림문자 1개 = 흰 바탕(#ffffff) 마름모(정사각형 45° 회전, 한 변 56) + 표준 빨강 #ff0000 테두리(두께 4) + 검정(#141414) 그림 + 아래 caption #141414 이름. 예시 3개 "산화성"(원 위 불꽃) · "부식성"(손·금속 부식) · "수생환경 유해성"(죽은 물고기·나무). 9종 중 해당 것만, 순서는 MSDS 표기 순. #ff0000은 이 컴포넌트 안에서만, 핑크 결정 신호를 대신하지 않는다
- msds-original-link: 맨 아래 전폭 button-outline "원문 MSDS 보기 ↗"(#ffffff, 1px #e0e0e0, 라벨 #141414, rounded 9999, 높이 44 이상) — 공단 MSDS 페이지를 새 창으로 연다. 모바일 = 항목 카드 아래(tab-bar 위 간격 16), 데스크톱 = detail-drawer 아래 고정 줄. 하늘색: ↗ 아이콘 #2b9fe0
- button-outline: msds-original-link 버튼 모양(위 정의)
- msds-skeleton: 불러오는 중 자리 표시 — 신호어 자리 짧은 막대 1 + 그림문자 자리 마름모 3 + 항목 카드마다 제목 막대 1·본문 막대 3(#f3f3f3, rounded 9999, 실제 배치와 같은 자리). 이 프레임에서는 숨김(상태 16-loading)
- ex-empty-state-card: 요약 실패 "요약을 불러오지 못했어요" + 한 줄 "원문에서 확인해 주세요" + msds-original-link. 이 프레임에서는 숨김(상태 16-fail). 핑크 없음, 아이콘 #141414
- tab-bar: 모바일 전용 하단 탭바 1개(공통 규격). 데스크톱에는 두지 않는다. 하늘색: 활성 tab-item 아이콘 #2b9fe0만
- tab-item: "홈" · "시약" · "QR 스캔" · "기록" 4개. 활성 = "시약", 비활성 3개 #707070
### 반영한 레퍼런스
- https://uibowl.io/name/%EB%A9%94%EB%94%94%EC%BD%94%EC%B9%98?patterns=%EC%83%81%EC%84%B8%EC%A0%95%EB%B3%B4%20%28PDP%29&imgId=cms8ebafr002el204u8vddkky
- https://uibowl.io/name/%EC%8F%98%EC%B9%B4?patterns=%EC%83%81%EC%84%B8%EC%A0%95%EB%B3%B4%20%28PDP%29&imgId=cmogjs1bf0019la04rxwg16ac
- https://uibowl.io/name/G%20car?patterns=%EA%B2%80%EC%83%89&imgId=cmo84t624000fl5045bz2r4ic
- https://uibowl.io/website/%EB%AA%A8%EA%B0%81%EC%9E%91?patterns=%EA%B2%80%EC%83%89&imgId=cmow9lnp1000yky0427encrx9
- https://uibowl.io/website/%EB%A7%88%ED%94%8C?patterns=%EC%83%81%EC%84%B8%EC%A0%95%EB%B3%B4%20%28PDP%29&imgId=cmnnx4cuq02ikju04zkbrvx39

## 역할별 노출
앱 전체(로그인 후 화면) 기준 개수. runs/20261007-0848 표를 기준으로 한다. 이번 run은 같은 컴포넌트를 데스크톱에서 다른 배치(사이드바·표·드로어·페이지)로 옮기고 화면 16을 더할 뿐, 표의 컴포넌트를 새로 더하거나 빼지 않으므로 숫자는 그대로다. 같은 컴포넌트가 모바일·데스크톱에 한 번씩 나오면 1로 센다.
msds-entry = 화면 3 1 + 화면 10 상세 1(학생·교사·admin 모두 2, R4). 화면 16은 msds-entry가 여는 목적지라 진입 개수를 바꾸지 않는다. 데스크톱 홈 숫자 타일 "재주문 알림"은 모바일 홈 reorder-alert-card와 같은 1개(교사·admin), 데스크톱 홈 quick-action 버튼 줄은 모바일 quick-action과 같은 진입(stock-intake·user-manage·cabinet-edit 각 1).
sidebar-item은 역할마다 다르지만(학생 5 · 교사 8 · admin 10) rules.json roles 대상이 아니라 표에 넣지 않는다 — 학생 메뉴에는 입고·실험 매뉴얼·재주문 알림·사용자·판매처가 없다. app-sidebar·data-table·detail-drawer·msds-summary·ghs-pictogram·msds-original-link·auto-threshold-badge·nav-account-menu도 표 대상이 아니다.

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
