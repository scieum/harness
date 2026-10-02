# S2 설계 — run 20261002-1416

대상 화면: 13 (홈/대시보드) · 학교: 샘플고등학교 (input.json)
재실행 사유: runs/20261002-1335 설계 반려 — "설계 변경 — 홈 상단 바로가기 그리드 대신 하단 탭바 4개". 1335 설계를 기준으로 모바일 하단 tab-bar를 더하고 quick-action을 역할별 작업 2칸으로 줄였다. runs/20261002-1359 반려 — "탭바를 둥근 floating pill 말고 하단에 붙은 사각형으로". 1359 설계를 기준으로 tab-bar·tab-item 모양만 바꿨다.
이전 작업: runs/20261002-1301 (화면 11·12·7·8), runs/20261002-1138 (화면 1·4·5·7·8·9·10, 하늘색 버전), runs/20261002-0838 (화면 2·3·6). 같은 컴포넌트 이름과 톤을 따른다.
근거: docs/PRD.md §3·§6·§7, docs/story-service.md 결정 사항("모바일 하단 탭바", "홈 (화면 13)"), docs/design.md(`tab-bar` 섹션), harness/rules.json(roles R1~R7, screens_required 13, tab_bar, colors), research/s1-adopt.md
색·폰트·모서리·간격은 docs/design.md와 harness/rules.json을 따른다. 허용 색 밖의 값은 쓰지 않는다. 반투명 회색은 badge-overlay 안에서만 허용되며 이 화면에는 쓰지 않는다. 그림자는 쓰지 않는다.
- 강조색 #d6246a(핑크)와 연핑크 #fbe9f0는 재고 부족·재주문 알림 신호에만 쓴다. 이 화면에서는 badge-low-stock, reorder-alert-card 안에서만 쓴다. 그 밖의 안내·빈 상태에는 핑크를 쓰지 않는다.
- 하늘색 #2b9fe0(선·인디케이터·아이콘)과 옅은 하늘색 #e6f4fc(선택·아이콘 바탕)는 활성 탭·활성 nav 링크 밑줄·선택 상태·링크 화살표·아이콘 강조에만 쓴다. 글자색으로 쓰지 않고(하늘색 위 글자는 #141414), badge-low-stock·reorder-alert-card·button-primary 안에는 쓰지 않는다.
학교 선택은 화면 1에만 있다. 화면 13에는 학교 선택을 두지 않고 nav-pill 안에 현재 학교명 "샘플고등학교"를 표시한다. 학교 전환 기능은 두지 않는다. 화면의 모든 숫자·기록은 샘플고등학교 데이터만 보여준다(N1).
외부 서비스 연결 값은 서버에서만 다룬다. 홈에 연결 값 입력·외부 서비스 설정·AI 엔진 선택 UI를 두지 않는다.
괄호 안 역할 표시가 없는 구성 요소는 학생·교사·admin 모두에게 보인다.
내비게이션 분담: 모바일 = 하단 tab-bar 4개(홈·시약·QR 스캔·기록, 역할 무관 동일)가 화면 이동을 맡고, 상단 nav-pill은 워드마크·학교명만 남긴다. 데스크탑 = tab-bar 없이 nav-pill 섹션 링크 유지 — 맨 앞 "홈" + "시약 목록", "사용 기록 내역", "시약장 설정", "QR 스캔", 교사·admin에게만 "재주문 알림"·"입고·시약 등록", admin에게만 "사용자 관리"·"판매처 설정".
탭 목적지: 홈 = 화면 13, 시약 = 화면 2 시약 목록, QR 스캔 = 화면 12, 기록 = 화면 10 사용 기록 내역. 역할별 작업(입고·사용자 관리 등)은 탭으로 두지 않고 홈 quick-action에만 둔다. quick-action에는 탭과 목적지가 겹치는 항목(QR 스캔·시약 목록·사용 기록 내역)을 두지 않는다.

## 화면 13
로그인 후 첫 화면. 학생·교사·admin 모두 들어오고, 같은 홈 틀에서 역할마다 quick-action·카드 구성이 달라진다. tab-bar 4개는 모든 역할에 같다.
예시 상태: 전체 시약 42종, 재고 부족 3종(염산 · 1병, 에탄올 · 200mL, 질산은 · 5g), 시약장 2개(칸 16개 중 지정 14 · 미지정 2), 재주문 알림 3건, 최근 사용 기록 3줄.
모바일(390×844) 위→아래 순서: nav-pill(얇은 헤더) → quick-action 2칸 한 줄 → home-summary ① 재고 요약 카드 → (교사·admin) reorder-alert-card → home-summary ② 시약장 요약 카드 → 최근 사용 기록 카드. 화면 하단에 tab-bar 고정. 섹션은 독립 카드로 세로 스택하고 카드 사이는 24 간격, 좌우 여백 16.
모바일 첫 화면(스크롤 전)은 nav-pill · quick-action · 재고 요약 카드 · (교사·admin) reorder-alert-card까지만 보이도록 간결하게 둔다. 본문 스크롤 영역은 tab-bar 위쪽 가장자리(y 780)에서 끝난다 — 본문 아래에 tab-bar 높이 64만큼 비우고, 스크롤 영역 안 마지막 카드 아래에 16 여백을 둬서 마지막 카드 아래 끝이 tab-bar 위쪽 선보다 16 위에 온다(64·16 모두 rules.json spacing 값). 어떤 카드도 tab-bar 뒤로 가려진 채 끝나지 않는다.
데스크탑(1440): tab-bar 없음. nav-pill 아래 2열. 왼쪽 열 = quick-action 2칸 + home-summary(재고 요약 카드 → 시약장 요약 카드), 오른쪽 열 = (교사·admin) reorder-alert-card + 최근 사용 기록 카드. 학생은 오른쪽 열에 최근 사용 기록 카드만 둔다.
### 구성 요소
- nav-pill: "Lab_Stock" 워드마크 + 현재 학교명 "샘플고등학교" 텍스트(상단 한 줄 "학교명"). 학교 선택·전환 컨트롤은 두지 않는다. 모바일 = 워드마크·학교명만 있는 얇은 헤더(섹션 링크 없음, 이동은 tab-bar가 맡음). 데스크탑 = 위 섹션 링크 유지. 하늘색: 데스크탑 현재 섹션 링크("홈") 아래 #2b9fe0 밑줄 인디케이터(글자는 #141414)
- quick-action: 역할별 작업 바로가기 2칸 한 줄(같은 폭 2열, 칸 사이 12). 칸 = #f3f3f3 채움, rounded 16, 안쪽 여백 16, 왼쪽 원형 아이콘 바탕(#e6f4fc, rounded 9999) 안 #2b9fe0 아이콘 + 오른쪽 label(link, #141414), 칸 전체가 44 이상 누름 영역. 탭과 겹치는 QR 스캔·시약 목록·사용 기록 내역 칸은 두지 않는다. 역할별 항목: 학생 2칸 "사용 기록 입력"(화면 4) · "시약장 보기"(화면 11 배치도 보기 전용, 편집 컨트롤 없음). 교사 2칸 "사용 기록 입력"(화면 4) · "입고"(화면 7, stock-intake 진입). admin 2칸 "입고"(화면 7, stock-intake 진입) · "사용자 관리"(화면 8, user-manage 진입). 학생 quick-action에는 입고·사용자 관리 칸이 없고, 교사 quick-action에는 사용자 관리 칸이 없다. 하늘색: 아이콘 #2b9fe0 + 아이콘 바탕 #e6f4fc, 누른 칸 바탕 #e6f4fc
- home-summary: 요약 카드 2장(#ffffff, 1px #f0f0f0 테두리, rounded 24, 안쪽 여백 24). ① 재고 요약 카드: 맨 위 한 줄 heading-4 "재고 부족 3개"(#141414) + 오른쪽 badge-low-stock "3" → 바로 아래 부족 시약 칩 가로 줄(칩 = #f3f3f3 채움, rounded 9999, label #141414 "염산 · 1병" / "에탄올 · 200mL" / "질산은 · 5g", 누르면 화면 3 시약 상세) → 보조 수치 1행 "전체 시약"(caption #707070) + "42종"(title). 재고 부족이 0개면 badge-low-stock과 칩 줄을 숨기고 body(#141414) "부족한 시약이 없어요" 1줄. ② 시약장 요약 카드: 섹션 제목 heading-4 "시약장 요약 >"(누르면 화면 11, 학생은 배치도 보기 전용) → 큰 숫자 display "2개" → 상태별 구간 막대 1줄(지정 칸 #2b9fe0 구간 + 미지정 칸 #e0e0e0 구간, rounded 9999) → 보조 1줄 body-sm(#707070) "칸 16개 중 지정 14 · 미지정 2". 시약장이 0개면 이 카드 자리에 ex-empty-state-card. 하늘색: 시약장 요약 막대의 지정 구간 #2b9fe0, 제목 옆 › 아이콘 #2b9fe0. 핑크는 badge-low-stock 안에서만
- badge-low-stock: 재고 요약 카드 제목 옆 개수 배지 "3", reorder-alert-card 제목 옆 "재고 부족"(#d6246a 채움, #ffffff label 글자, rounded 9999). 하늘색 없음
- reorder-alert-card: 교사·admin 전용 '재주문 알림' 카드. #f3f3f3 채움, 테두리 없음, rounded 24, 안쪽 여백 24. 제목 heading-4 "재주문 알림" 옆 badge-low-stock "재고 부족" + 오른쪽 button-pill-soft "3건 >"(누르면 화면 6 재주문 알림 목록). 본문 body 1줄 "필요량보다 적은 시약이 3종 있어요"(#141414). 판매처 연결 버튼은 이 카드에 두지 않고 화면 6에서만 연다. 하늘색 쓰지 않음(› 아이콘도 #141414). 학생 홈에는 이 카드가 없다 (교사·admin만)
- reagent-row: 최근 사용 기록 카드 안 3줄. 카드 = #ffffff, 1px #f0f0f0 테두리, rounded 24, 제목 heading-4 "최근 사용 기록". 행 = 시약명(title) + 사용자 이름·사용량(body, 예: "김학생 · 20mL") + 시각 caption(#707070, 예: "오늘 10:20"), #f3f3f3 채움, rounded 16, 행 사이 12. 행을 누르면 화면 10 사용 기록 내역의 해당 기록으로 간다. 재고 부족 배지는 이 행에 두지 않는다(재고 요약 카드에서만). 기록이 0건이면 행 자리에 ex-empty-state-card. 하늘색: 누른 행 배경 #e6f4fc
- button-pill-soft: 최근 사용 기록 카드 하단 "더 보기 >"(화면 10), reorder-alert-card "3건 >"(교사·admin만). 하늘색: reorder-alert-card 밖의 버튼에만 오른쪽 › 아이콘 #2b9fe0(라벨 글자는 #141414)
- ex-empty-state-card: ① 시약장 0개: body(#141414) "등록된 시약장이 없어요" + 교사·admin에게만 button-outline "시약장 추가"(화면 11 cabinet-edit 진입), 학생에게는 body-sm(#707070) "선생님이 시약장을 등록하면 보여요". ② 최근 사용 기록 0건: "아직 사용 기록이 없어요" + button-outline "사용 기록 입력"(화면 4). 하늘색: 안내 아이콘 #2b9fe0
- button-outline: ex-empty-state-card의 "시약장 추가"(교사·admin만), "사용 기록 입력". 1px #e0e0e0 테두리, rounded 9999
- tab-bar: 모바일 전용 하단 탭바 1개. 화면 아래 가장자리에 붙은 전폭 사각형 바(x 0, 폭 390, 높이 64, 위치 y 780~844, rounded 0). #ffffff 채움 + 위쪽에만 1px #f0f0f0 선, 그림자 없음, 화면 아래·좌우 띄움 없음(floating pill 아님). 안쪽 위아래 여백 8, 좌우 여백 0. 안에 tab-item 4개를 같은 폭으로 꽉 채워 둔다(QR 스캔 탭을 키우지 않음). 역할 무관 동일. 데스크탑 프레임에는 두지 않는다. 하늘색: 활성 tab-item의 #2b9fe0 아이콘만(바탕 채움 없음)
- tab-item: tab-bar 안 4개, 왼쪽부터 "홈"(화면 13) · "시약"(화면 2) · "QR 스캔"(화면 12) · "기록"(화면 10). 각 항목 = 같은 폭(390 ÷ 4) 사각형 누름 영역(rounded 0, 채움 없음, pill 없음), 높이 48(44 이상), 아이콘 위 + label(12/600) 아래, 아이콘과 라벨 사이 4. 이 화면의 활성 = "홈": #2b9fe0 아이콘 + 라벨 #141414, 뒤 바탕 없음. 비활성 3개("시약"·"QR 스캔"·"기록"): 아이콘·라벨 #707070. 입고·사용자 관리 등 역할별 작업은 tab-item으로 두지 않는다
### 반영한 레퍼런스
- https://uibowl.io/name/%ED%8E%98%EC%9D%B4%ED%9E%88%EC%96%B4?patterns=%EB%A9%94%EC%9D%B8&imgId=cmnfmxnhh0003l8045z9h1r15
- https://uibowl.io/name/%ED%8E%98%EC%9D%B4%EC%9B%8C%ED%81%AC?patterns=%EB%A9%94%EC%9D%B8&imgId=cmtzo55qv002rl7047rsl7n07
- https://uibowl.io/name/%ED%97%A4%EC%9D%B4%EC%98%81%20%EC%BA%A0%ED%8D%BC%EC%8A%A4?patterns=%EB%A9%94%EC%9D%B8&imgId=cmmbj8sqh0004lh048k4kbkqd
- https://uibowl.io/name/%ED%95%98%EC%9D%B4%EB%A7%81%EA%B5%AC%EC%96%BC?patterns=%EB%A9%94%EC%9D%B8&imgId=cmnmkywio0003l804k22ndnyy
- https://uibowl.io/name/%EC%9E%90%EB%A6%AC%ED%86%A1?patterns=%EB%A9%94%EC%9D%B8&patternName=%ED%99%88%28%EC%9E%84%EB%8C%80%EC%9D%B8%29

## 역할별 노출
앱 전체(화면 1~13) 기준 개수. runs/20261002-1301 표(화면 1~12)에 화면 13 홈 진입점을 더했다(1335 표와 숫자 같음).
홈에서 더한 것: reorder-alert-card = 홈 카드 1 (교사·admin). stock-intake = 홈 quick-action "입고" 1 (교사·admin). user-manage = 홈 quick-action "사용자 관리" 1 (admin만). cabinet-edit = 홈 시약장 0개 빈 상태의 "시약장 추가" 1 (교사·admin). 학생 quick-action "시약장 보기"는 보기 전용이라 cabinet-edit이 아니다. tab-bar·tab-item은 역할 무관 동일하고 표의 컴포넌트를 담지 않는다. 홈에는 manual-upload·vendor-link·vendor-register·reagent-register·msds-entry 진입을 두지 않는다(1301 값 유지). 학생 홈의 reorder-alert-card·vendor-link·stock-intake = 0.

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
