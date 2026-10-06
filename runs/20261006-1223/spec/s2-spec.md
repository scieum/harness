# S2 설계 — run 20261006-1223

대상 화면: 3 (시약 상세), 11 (시약장 설정), 12 (QR 스캔), 13 (홈) + 상태 화면 3-location, 11-slot, 11-print, 11-unsaved, 12-result · 학교: 샘플고등학교 (input.json)
변경 사유: 2026-10-06 사용자 결정(개발 세션 요청) — 시약 칸 배치, 시약장 고정 번호·QR 인쇄, 재주문 기준 직접 입력, 저장 안 한 편집 확인, 앱 예외(nav-account-menu, 홈 quick-action 3칸). 근거: docs/PRD.md §5·§7(3·11·12·13), docs/story-service.md 결정 사항 2026-10-06 행("시약 칸 배치"·"시약장 번호·QR 인쇄"·"재주문 기준 직접 입력"·"저장 안 한 편집"·"앱 예외 반영"), docs/design.md("Cabinet number & QR print"·"Reagent slots"·"Multiple cabinets"·nav-account-menu·tab-bar quick-action 3칸), harness/rules.json(roles R1~R7, screens_required 3·11·12·13, variants, cabinet, reorder, app_exceptions, tab_bar, colors), research/s1-adopt.md.
기준 설계(수정하지 않음): 화면 3·12 = runs/20261002-1441, 화면 11 = runs/20261004-2256, 화면 13 = runs/20261002-1416. 기존 구성 요소를 유지하고 2026-10-06 결정분만 더하거나 바꾼다.
색·폰트·모서리·간격은 docs/design.md와 harness/rules.json을 따른다. 허용 색 밖의 값(딤 반투명 검정 등)은 쓰지 않는다. 그림자는 쓰지 않는다(segmented-control-active 예외).
- 핑크 #d6246a·연핑크 #fbe9f0는 badge-low-stock, reorder-alert-card, mix-warning 안에서만 쓴다. cabinet-number, slot-count, qr-label, 저장 안 한 편집 모달, "칸 없음" 표시에는 핑크를 쓰지 않는다.
- 하늘색 #2b9fe0(선·인디케이터·아이콘)과 옅은 하늘색 #e6f4fc(선택 배경)는 선택 상태·활성 탭·아이콘에만 쓴다. 글자색으로 쓰지 않고(하늘색 위 글자는 #141414), badge-low-stock·reorder-alert-card·button-primary·mix-warning 안에는 쓰지 않는다. cabinet-number 숫자는 하늘색 글자 금지.
- qr-label은 인쇄물이라 흑백(#141414·#707070·#ffffff·#e0e0e0)만 쓴다.
학교 선택은 회원가입(화면 14)에만 있다. 이번 대상 화면과 상태 화면에는 학교 선택을 두지 않고 nav-pill 안에 현재 학교명 "샘플고등학교"를 표시한다. 학교 전환 기능은 두지 않는다. 시약장·칸·시약·QR 결과는 모두 샘플고등학교 것만 보인다(N1). qr-label의 학교명도 "샘플고등학교" 1종.
외부 서비스 연결 값은 서버에서만 다룬다. 어떤 화면에도 연결 값 입력·외부 서비스 설정·AI 엔진 선택 UI를 두지 않는다.
괄호 안 역할 표시가 없는 구성 요소는 학생·교사·admin 모두에게 보인다. 학생 화면에는 threshold-edit, location-edit, slot-assign, qr-print, cabinet-add, cabinet-edit을 그리지 않는다(R5·R7).
모바일 공통: tab-bar는 화면 아래 가장자리 y 780~844(높이 64)에 붙고 본문 스크롤은 y 780에서 끝난다. 하단 고정 버튼은 tab-bar 바로 위(간격 16). 바텀시트·확인 카드는 tab-bar 위쪽 선 위에 붙는다(딤 없음, 1px #e0e0e0 테두리로 구분). 데스크탑에는 tab-bar 없이 nav-pill 섹션 링크를 유지하고, 시트는 화면 가운데 ex-modal-card로 연다.
nav-account-menu(공통, rules.json app_exceptions): 모든 대상 화면의 nav-pill 학교명 "샘플고등학교" 옆 작은 ▾. 누르면 #ffffff 작은 메뉴(rounded 24, 1px #f0f0f0 테두리)에 항목 "로그아웃" 1개만. 프레임에는 닫힌 상태(▾만)로 그린다.

## 화면 3
시약 상세. 학생·교사·admin 모두 들어온다. 교사·admin은 보관 위치를 바꾸고(location-edit) 재주문 기준을 숫자로 고친다(threshold-edit). 학생은 두 줄을 보기만 한다.
예시 상태: 과산화수소, 현재 재고 2병, 재주문 기준 3병(재고 부족 배지 표시), 보관 위치 "1번 시약장 · 우 1단"(분류 산화제 칸).
모바일 활성 탭: "시약". 위→아래: nav-pill → reagent-detail-card(시약명·재고 → reagent-location 줄 → reorder-threshold 줄) → segmented-control "정보 / 사용 기록" → 표 → msds-entry → 하단 고정 "사용 기록"(+ 교사·admin "입고") → tab-bar. 좌우 여백 16, 블록 사이 24.
데스크탑: nav-pill 아래 가운데 단일 열 같은 순서, tab-bar 없음.
### 구성 요소
- nav-pill: 뒤로가기(화면 2) + 제목 "시약 상세" + 현재 학교명 "샘플고등학교" 텍스트 + 학교명 옆 nav-account-menu ▾. 학교 전환 기능 없음. 하늘색: 뒤로가기 아이콘 #2b9fe0
- nav-account-menu: 학교명 옆 ▾, 메뉴 항목 "로그아웃" 1개(공통 정의). 하늘색 없음
- reagent-detail-card: 상단 요약 카드(#ffffff, 1px #f0f0f0 테두리, rounded 24, 안쪽 여백 24). 시약명(title) + badge-low-stock, 현재 재고 display "2" + 단위 "병", 입고일 caption 라벨-값, 그 아래 reagent-location 줄과 reorder-threshold 줄을 라벨-값 한 줄씩 쌓는다. 하늘색 없음
- badge-low-stock: 재고 2병 < 재주문 기준 3병이라 시약명 옆 "재고 부족"(#d6246a 채움, #ffffff label). 하늘색 없음
- reagent-location: reagent-detail-card 안 한 줄. 왼쪽 caption "보관 위치"(#707070) + 값 "cabinet-number(1) 1번 시약장 · 우 1단"(body, #141414). 칸이 없으면 값 자리에 "칸 없음"(#707070). 교사·admin은 줄 오른쪽에 location-edit. 학생은 값만 본다
- cabinet-number: reagent-location 값 앞 작은 원(#ffffff 채움, 1px #e0e0e0 테두리, rounded 9999) 안 숫자 "1"(label, #141414). 핑크·하늘색 글자 없음
- location-edit: reagent-location 줄 오른쪽 button-pill-soft "위치 바꾸기"(#f3f3f3 채움, 라벨 #141414, rounded 9999, 높이 44 이상). 누르면 상태 화면 3-location의 location-picker가 열린다 (교사·admin만)
- reorder-threshold: reagent-detail-card 안 reagent-location 아래 한 줄. caption "재주문 기준"(#707070) + 값 "3병"(body, #141414). 값이 없으면 "아직 없어요"(#707070). 화면 5 AI 추출 결과와 같은 칸이다. 학생은 값만 본다
- threshold-edit: reorder-threshold 줄의 값 오른쪽 연필 아이콘(누름 영역 44 이상). 누르면 값 자리가 숫자 text-input(값 "3" + 단위 suffix "병")으로 바뀌고 줄 아래 button-primary "저장"이 나온다. 빈 값·음수는 입력 아래 #141414 body-sm "1 이상 입력하세요"(핑크 금지). 하늘색: 연필 아이콘 #2b9fe0 (교사·admin만)
- text-input: threshold-edit 편집 상태의 숫자 입력(#f0f0f0 채움, 테두리 없음, rounded 16, 포커스 링 2px #141414, 단위 suffix #707070) (교사·admin만)
- segmented-control: 요약 아래 "정보 / 사용 기록" 두 탭, 선택된 탭은 segmented-control-active
- segmented-control-active: 활성 탭 흰 pill. 하늘색: 활성 탭 아래 #2b9fe0 인디케이터(글자는 #141414)
- ex-data-table-cell: "정보" 탭 = 시약 속성 라벨-값 표, "사용 기록" 탭 = 날짜·사용자·사용량 3열 표. 하늘색: 가장 최근 사용 기록 행 배경 #e6f4fc
- msds-entry: msds-qr-tile(QR 1:1, rounded 0, 아래 라벨 "QR로 MSDS 열기") + button-pill-soft "MSDS 보기 ↗". 학생·교사·admin 모두 1개. 하늘색: ↗ 아이콘 #2b9fe0
- button-primary: 하단 고정 "사용 기록"(→ 화면 4, 모든 역할), threshold-edit 편집 상태 "저장"(교사·admin). #141414 채움, #ffffff 글자, rounded 9999, 높이 44 이상. 하늘색 없음
- button-outline: 하단 고정 "사용 기록" 옆 "입고"(→ 화면 7) (교사·admin만)
- ex-toast: 저장 직후 "재주문 기준을 3병으로 바꿨어요" / "보관 위치를 바꿨어요". 모바일에서는 tab-bar 위에 뜬다. 하늘색: 완료 체크 아이콘 #2b9fe0 (교사·admin만)
- tab-bar: 모바일 전용 하단 탭바 1개(x 0, 폭 390, 높이 64, y 780~844, rounded 0, #ffffff 채움 + 위쪽 1px #f0f0f0 선, 그림자 없음, tab-item 4개 같은 폭). 데스크탑에는 두지 않는다. 하늘색: 활성 tab-item 아이콘 #2b9fe0만
- tab-item: "홈" · "시약" · "QR 스캔" · "기록" 4개, 같은 폭 사각형 누름 영역(rounded 0), 높이 48, 아이콘 위 + label 아래. 활성 = "시약"(#2b9fe0 아이콘 + 라벨 #141414), 비활성 3개 아이콘·라벨 #707070
### 반영한 레퍼런스
- https://uibowl.io/name/%EC%B1%84%EB%B9%84?patterns=%EC%83%81%EC%84%B8%EC%A0%95%EB%B3%B4%20%28PDP%29&patternName=%EC%B6%A9%EC%A0%84%EC%86%8C
- https://uibowl.io/name/%EC%91%A5%EC%91%A5%EC%B0%B0%EC%B9%B5?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&imgId=cmub7kvlz0007js04xdyeh3c1
- https://uibowl.io/name/%EC%98%A4%EB%8A%98%EC%9D%98%20%EB%A3%A8%ED%8B%B4?patterns=%EC%83%81%EC%84%B8%EC%A0%95%EB%B3%B4%20%28PDP%29&patternName=%EB%A3%A8%ED%8B%B4%20%EC%83%81%EC%84%B8

## 상태 화면 3-location
교사·admin이 화면 3에서 "위치 바꾸기"를 누른 상태(프레임 3-location-mobile · 3-location-desktop). 학생에게는 이 상태가 없다.
뒤 화면은 화면 3 그대로(과산화수소 상세, 흐림·딤 없이 그대로 보임). 그 위에 location-picker가 뜬다. 모바일 = 바텀시트(tab-bar 위쪽 선 위), 데스크탑 = 화면 가운데 ex-modal-card 크기의 시트.
예시 상태: 현재 위치 1번 시약장 · 우 1단(산화제). 피커에서 cabinet-switcher로 "2번 시약장"을 고르고 칸 "좌 2단"(분류 유기)을 선택함 → 산화제와 유기는 rules.json cabinet.incompatible 조합이라 강한 문구의 mix-warning. 저장은 막지 않는다(rules.json cabinet.class_mismatch).
### 구성 요소
- nav-pill: 뒤 화면 3의 nav-pill 그대로 — 뒤로가기 + "시약 상세" + 현재 학교명 "샘플고등학교" + nav-account-menu ▾. 하늘색: 뒤로가기 아이콘 #2b9fe0 (교사·admin만)
- nav-account-menu: 학교명 옆 ▾(닫힌 상태) (교사·admin만)
- reagent-detail-card: 시트 뒤에 보이는 화면 3 요약 카드(누름 동작 없음). 하늘색 없음 (교사·admin만)
- reagent-location: 시트 뒤 카드 안 "보관 위치 · (1) 1번 시약장 · 우 1단" — 아직 저장 전이라 옛 위치를 보여준다 (교사·admin만)
- location-picker: 시트 1개(#ffffff 채움, 1px #e0e0e0 테두리, 위쪽 rounded 24, 안쪽 여백 24). 위→아래: 제목 heading-3 "보관 위치 바꾸기" + 오른쪽 위 × 닫기 → 보조 caption(#707070) "과산화수소 · 산화제" → cabinet-switcher → 고른 시약장의 cabinet-slot 배치도(양문형 · 3단 = 좌/우 × 1~3단, 각 칸에 분류 이름 + slot-count) → 조용한 텍스트 동작 "칸 없음으로"(link, #141414, 채움·테두리 없음, 누름 영역 44 이상) → mix-warning → 하단 전폭 button-primary "저장". 칸을 고르기 전에는 "저장" 비활성 (교사·admin만)
- cabinet-switcher: location-picker 맨 위 시약장 전환 pill 가로 한 줄 "(1) 1번 시약장" · "(2) 2번 시약장". 활성 = "2번 시약장"(#e6f4fc 채움 + 1px #2b9fe0 테두리, 라벨 #141414), 비활성 #f3f3f3. 피커 안에는 cabinet-add를 두지 않는다. 하늘색: 활성 pill 채움·테두리 (교사·admin만)
- cabinet-number: cabinet-switcher pill마다 이름 앞 작은 원(#ffffff, 1px #e0e0e0 테두리) 안 숫자 "1"·"2"(label, #141414) (교사·admin만)
- cabinet-slot: 2번 시약장 배치도 칸 6개(#f3f3f3 채움, rounded 16, 칸 안 분류 이름 label #141414, 분류 없으면 "미지정" #707070). 왼쪽 단 라벨 "1단"~"3단", 위 문 라벨 "좌"/"우". 누르면 그 칸을 고른다. 선택 칸 = "좌 2단"(유기). 하늘색: 선택 칸 배경 #e6f4fc + 2px #2b9fe0 테두리(글자는 #141414) (교사·admin만)
- slot-count: 시약이 있는 cabinet-slot 안 오른쪽 위 작은 pill(#ffffff 채움, rounded 9999, label #141414) — 예: 좌 1단 "2", 좌 2단 "3", 우 1단 "1". 빈 칸에는 그리지 않는다. 핑크 금지 (교사·admin만)
- mix-warning: 배치도 아래 경고 블록(#fbe9f0 바탕, 테두리 없음, rounded 16, #d6246a 경고 아이콘 + #141414 body-sm). 문구 "산화제와 유기는 섞으면 위험해요" + 보조 1줄 "그래도 저장할 수 있어요". 분류만 다르고 금지 조합이 아니면 "이 칸은 {분류} 칸이에요 — 그래도 넣을 수 있어요". 칸이 맞으면 숨김. 하늘색 없음 (교사·admin만)
- button-primary: location-picker 하단 전폭 "저장"(#141414 채움, #ffffff 글자, rounded 9999, 높이 44 이상). mix-warning이 있어도 활성. 하늘색 없음 (교사·admin만)
- tab-bar: 모바일 전용 하단 탭바 1개(화면 3과 같음). 시트는 이 바 위쪽 선 위에 붙고 바를 가리지 않는다. 데스크탑에는 두지 않는다. 하늘색: 활성 tab-item 아이콘 #2b9fe0만 (교사·admin만)
- tab-item: 4개 "홈" · "시약" · "QR 스캔" · "기록". 활성 = "시약". 비활성 3개 #707070 (교사·admin만)
### 반영한 레퍼런스
- https://uibowl.io/name/iM%EB%B1%85%ED%81%AC?patterns=%EB%82%B4%EC%97%AD&imgId=cmp0txdm900jhl204vgbdwgxj
- https://uibowl.io/name/%EB%A7%88%EC%9D%B4%ED%98%84%EB%8C%80?patterns=%EC%A7%80%EB%8F%84%EB%B7%B0%C2%B7%EB%82%B4%EC%A3%BC%EB%B3%80&imgId=cmojklc13000bjr04d7uta0pj
- https://uibowl.io/name/%EC%98%A4%EB%8A%98%EC%9D%98%20%EB%A3%A8%ED%8B%B4?patterns=%EC%83%81%EC%84%B8%EC%A0%95%EB%B3%B4%20%28PDP%29&patternName=%EB%A3%A8%ED%8B%B4%20%EC%83%81%EC%84%B8

## 화면 11
시약장 설정. 학생·교사·admin 모두 들어온다. 교사·admin은 시약장 전환·추가, 이름 바꾸기·QR 인쇄·삭제, 문 형태·단 수·칸별 분류 편집, 칸 누르기 → 칸 시트(상태 11-slot)를 쓴다. 학생은 시약장 전환과 배치도·칸 시트 목록 보기만 한다.
예시 상태: 시약장 2개 "(1) 1번 시약장"(활성) · "(2) 2번 시약장". 1번 시약장 = 양문형 · 4단, 8칸. 좌1단 = 산 + 염기(mix-warning), 좌2단 = 유기, 좌3단 = 인화성, 좌4단 = 기타, 우1단 = 산화제, 우2단 = 무기염, 우3단 = 독성, 우4단 = 기타. 칸별 시약 수: 좌1단 2, 좌2단 3, 우1단 1, 우3단 1. 선택 칸 = 좌1단. "칸 없음" 시약 2개.
모바일 활성 탭: "시약". 위→아래: nav-pill → cabinet-switcher(끝에 cabinet-add) → heading-3 시약장 이름 + caption "양문형 · 4단" → (교사·admin) cabinet-edit 관리 줄("이름 바꾸기" · "QR 인쇄" · "삭제") → (교사·admin) 문 형태·단 수 선택 → 배치도 → 범례 → (교사·admin) 선택 칸 분류 칩 → mix-warning → "칸 없음" 시약 목록 → (교사·admin) 하단 고정 "저장" → tab-bar. 좌우 여백 16, 블록 사이 24.
데스크탑: nav-pill 아래 가운데 단일 열 같은 순서, cabinet-switcher 한 줄에 모두 펼침, tab-bar 없음.
### 구성 요소
- nav-pill: "Lab_Stock" 워드마크 + 제목 "시약장 설정" + 현재 학교명 "샘플고등학교" + 학교명 옆 nav-account-menu ▾. 학교 전환 기능 없음. 하늘색: 데스크탑 현재 섹션 링크("시약장 설정") 아래 #2b9fe0 밑줄(글자는 #141414)
- nav-account-menu: 학교명 옆 ▾, 메뉴 항목 "로그아웃" 1개. 하늘색 없음
- cabinet-switcher: 시약장 전환 pill 가로 한 줄, pill마다 cabinet-number + 이름. 활성 = #e6f4fc 채움 + 1px #2b9fe0 테두리 + 라벨 #141414, 비활성 = #f3f3f3. 넘치면 가로 스크롤(모바일). 저장하지 않은 편집이 있을 때 다른 pill을 누르면 상태 11-unsaved 모달. 모든 역할. 하늘색: 활성 pill 채움·테두리
- cabinet-number: cabinet-switcher pill마다 이름 앞 작은 원(#ffffff 채움, 1px #e0e0e0 테두리, rounded 9999) 안 숫자 "1"·"2"(label, #141414). 학교 안 고정 번호로 이름을 바꿔도 그대로, 삭제된 번호는 다시 쓰지 않는다(rules.json cabinet.number). 시약장 이름 heading-3 앞에도 같은 원을 둔다. 핑크·하늘색 글자 없음
- cabinet-add: cabinet-switcher 줄 끝 button-pill-soft "+ 시약장 추가". 누르면 다음 번호 "(3) 3번 시약장"을 만든다. 하늘색: "+" 아이콘 #2b9fe0 (교사·admin만)
- cabinet-edit: 편집 영역 블록 1개. 맨 위 관리 줄 = button-outline "이름 바꾸기" + qr-print + 오른쪽 조용한 텍스트 동작 "삭제"(link, #141414, 채움·테두리 없음, 누름 영역 44 이상, 핑크 금지). 그 아래 cabinet-door-select · cabinet-shelf-select · 선택 칸 storage-class-chip 묶음 · 하단 전폭 button-primary "저장". "이름 바꾸기"는 ex-modal-card 이름 시트를 연다 (교사·admin만)
- qr-print: cabinet-edit 관리 줄 "이름 바꾸기" 옆 button-outline "QR 인쇄"(#ffffff 채움, 1px #e0e0e0 테두리, 라벨 #141414, rounded 9999, 높이 44 이상). 누르면 상태 11-print의 qr-print-sheet. 하늘색: 왼쪽 인쇄 아이콘 #2b9fe0(라벨 글자는 #141414) (교사·admin만)
- cabinet-door-select: 문 형태 2옵션 pill "양문형 / 단문형", 하나만 선택, 예시 "양문형". 하늘색: 선택 옵션 #e6f4fc + 1px #2b9fe0 테두리(글자 #141414) (교사·admin만)
- cabinet-shelf-select: 단 수 2옵션 pill "3단 / 4단", 하나만 선택, 예시 "4단". 하늘색: 선택 옵션 #e6f4fc + 1px #2b9fe0 테두리 (교사·admin만)
- cabinet-slot: 활성 시약장 정면 배치도의 칸 1개(8칸, #f3f3f3 채움, rounded 16, 분류 이름 label #141414, 없으면 "미지정" #707070). 왼쪽 단 라벨, 위 문 라벨 "좌"/"우", 양문형은 가운데 통로처럼 비움. 칸을 누르면 칸 시트(상태 11-slot)가 열린다 — 교사·admin은 넣기·빼기, 학생은 그 칸 시약 목록 보기만. 좌1단 칸 오른쪽 위에 #141414 경고 아이콘. 하늘색: 선택 칸 #e6f4fc + 2px #2b9fe0 테두리(글자 #141414)
- slot-count: 시약이 있는 cabinet-slot 안 작은 pill(#ffffff 채움, rounded 9999, label #141414) "2"·"3"·"1"·"1". 빈 칸에는 없음. 모든 역할. 핑크·하늘색 없음
- storage-class-chip: 분류 칩 8종 "유기·산·염기·산화제·인화성·무기염·독성·기타". cabinet-edit 안 선택 칸(좌1단) 분류 고르기(여러 개 선택, 예시 "산"·"염기" 선택) + 배치도 아래 범례(보기 전용, 학생에게는 범례만). 하늘색: 선택 칩 #e6f4fc + 1px #2b9fe0 테두리
- mix-warning: "주의사항" 블록(#fbe9f0 바탕, 테두리 없음, rounded 16, 제목 heading-4 #141414 + 줄마다 #d6246a 경고 아이콘 + #141414 body-sm). 예시 1줄 "좌1단: 산과 염기는 섞이면 위험해요. 다른 칸에 나눠 보관하세요". 학생에게도 보기 전용으로 보인다. 하늘색 없음
- reagent-row: 소제목 heading-4 "칸 없음 시약 (2)" + 행(시약명 title + 재고량 body + caption "칸 없음" #707070, #f3f3f3 채움, rounded 16, 행 사이 12). 행을 누르면 화면 3. 하늘색: 누른 행 배경 #e6f4fc
- ex-modal-card: "이름 바꾸기" 시트(#ffffff, 1px #e0e0e0 테두리, rounded 24, 여백 24, 오른쪽 위 × 닫기). 제목 heading-3 "시약장 이름" + text-input(현재 이름) + caption "번호 1은 바뀌지 않아요"(#707070) + button-outline "취소" + button-primary "저장" (교사·admin만)
- text-input: 이름 시트 "시약장 이름" 입력(#f0f0f0, 테두리 없음, rounded 16, 포커스 링 2px #141414) (교사·admin만)
- button-outline: 관리 줄 "이름 바꾸기", 이름 시트 "취소" (교사·admin만)
- button-primary: cabinet-edit 하단 전폭 "저장"(모바일 tab-bar 바로 위), 이름 시트 "저장". 하늘색 없음 (교사·admin만)
- ex-toast: "시약장 설정을 저장했어요" / "이름을 바꿨어요" / "3번 시약장을 추가했어요". 하늘색: 완료 체크 아이콘 #2b9fe0 (교사·admin만)
- tab-bar: 모바일 전용 하단 탭바 1개(화면 3과 같은 규격). 학생 화면은 저장 버튼 없이 스크롤이 이 바 위에서 끝난다. 데스크탑에는 두지 않는다. 하늘색: 활성 tab-item 아이콘 #2b9fe0만
- tab-item: 4개 "홈" · "시약" · "QR 스캔" · "기록". 활성 = "시약". 비활성 3개 #707070
### 반영한 레퍼런스
- https://uibowl.io/name/%EC%9B%8C%ED%81%AC%EC%98%A8?patterns=%ED%8A%9C%ED%86%A0%EB%A6%AC%EC%96%BC&imgId=cmudxbzpd0028l7046bsxhka0
- https://uibowl.io/name/%ED%8E%98%EC%9D%B4%EC%9B%8C%ED%81%AC?patterns=%ED%8A%9C%ED%86%A0%EB%A6%AC%EC%96%BC&imgId=cmtzo5k4p004jl704vz543akg

## 상태 화면 11-slot
교사가 화면 11에서 칸 "좌 2단"(분류 유기)을 누르고 "시약 넣기"로 "칸 없음" 시약 중 염산(분류 산)을 고른 상태(프레임 11-slot-mobile · 11-slot-desktop). 학생은 같은 칸 시트를 목록만(빼기·넣기 없이) 본다 — 이 프레임은 교사 기준.
뒤 화면은 화면 11(1번 시약장) 그대로, 위에 slot-sheet. 모바일 = 바텀시트(tab-bar 위쪽 선 위), 데스크탑 = 가운데 시트. 염산(산)은 유기 칸 분류에 없으므로 약한 문구 mix-warning, 저장 허용.
### 구성 요소
- nav-pill: "Lab_Stock" + "시약장 설정" + 현재 학교명 "샘플고등학교" + nav-account-menu ▾ (교사·admin만)
- nav-account-menu: 학교명 옆 ▾(닫힌 상태) (교사·admin만)
- cabinet-switcher: 시트 뒤 전환 pill 줄 "(1) 1번 시약장"(활성) · "(2) 2번 시약장". 시트가 열린 동안 누름 동작 없음. 하늘색: 활성 pill 채움·테두리 (교사·admin만)
- cabinet-number: 전환 pill 이름 앞 숫자 원 "1"·"2"(#ffffff, 1px #e0e0e0, label #141414) (교사·admin만)
- cabinet-slot: 시트 뒤 배치도. 누른 칸 "좌 2단"이 선택 상태. 하늘색: 선택 칸 #e6f4fc + 2px #2b9fe0 테두리 (교사·admin만)
- slot-count: 배치도 칸 안 시약 수 pill(좌 2단 "3" 등, 무채색) (교사·admin만)
- slot-sheet: 시트 1개(#ffffff, 1px #e0e0e0 테두리, 위쪽 rounded 24, 여백 24, 오른쪽 위 × 닫기). 위→아래: 제목 heading-3 "좌 2단" + 그 칸 storage-class-chip "유기"(보기 전용) → 소제목 heading-4 "이 칸의 시약 (3)" + reagent-row 3개(에탄올 · 아세톤 · 메탄올), 행마다 오른쪽 조용한 텍스트 동작 "빼기"(link #141414, 누름 영역 44 이상) → 구분 여백 → 소제목 heading-4 "넣을 시약 고르기" + 검색 text-input + "칸 없음" reagent-row 2개(염산 · 질산은), 선택 = 염산 → mix-warning → 하단 전폭 slot-assign (교사·admin만)
- storage-class-chip: slot-sheet 제목 옆 칸 분류 칩 "유기"(보기 전용, #f3f3f3 채움, rounded 9999, label #141414) (교사·admin만)
- reagent-row: 칸 안 시약 행(시약명 title + 재고량 body + 분류 caption #707070, #f3f3f3 채움, rounded 16)과 피커의 "칸 없음" 시약 행(caption "칸 없음" #707070). 하늘색: 피커에서 선택한 행(염산) #e6f4fc 배경 + 오른쪽 #2b9fe0 체크 아이콘(글자 #141414) (교사·admin만)
- text-input: 피커 검색 바 "시약명 검색"(#f0f0f0, rounded 16). 하늘색: 검색 아이콘 #2b9fe0 (교사·admin만)
- mix-warning: 피커 목록 아래 경고 블록(#fbe9f0 바탕, rounded 16, #d6246a 경고 아이콘 + #141414 body-sm) "이 칸은 유기 칸이에요 — 그래도 넣을 수 있어요". 금지 조합이면 "{A}와 {B}는 섞으면 위험해요". 막지 않는다. 하늘색 없음 (교사·admin만)
- slot-assign: slot-sheet 하단 전폭 button-primary "시약 넣기"(#141414 채움, #ffffff 글자, rounded 9999, 높이 44 이상). 피커가 닫혀 있으면 누를 때 피커를 열고, 시약을 고른 상태에서는 그 시약을 이 칸에 넣는다. mix-warning이 있어도 활성. 하늘색 없음 (교사·admin만)
- ex-toast: 넣기·빼기 직후 "염산을 좌 2단에 넣었어요" / "에탄올을 뺐어요(칸 없음)". 하늘색: 완료 체크 아이콘 #2b9fe0 (교사·admin만)
- tab-bar: 모바일 전용 하단 탭바 1개(화면 11과 같음). 시트는 이 바 위에 붙는다. 데스크탑에는 두지 않는다 (교사·admin만)
- tab-item: 4개 "홈" · "시약" · "QR 스캔" · "기록". 활성 = "시약" (교사·admin만)
### 반영한 레퍼런스
- https://uibowl.io/name/%EC%9B%8C%ED%81%AC%EC%98%A8?patterns=%ED%8A%9C%ED%86%A0%EB%A6%AC%EC%96%BC&imgId=cmudxbzpd0028l7046bsxhka0
- https://uibowl.io/name/%EC%85%80%EB%A0%88%ED%8A%B8%EB%A6%BD?patterns=%EB%A1%9C%EA%B7%B8%EC%9D%B8%C2%B7%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85&imgId=cmqp02zja000sjr04ea8bxiax

## 상태 화면 11-print
교사·admin이 화면 11 관리 줄의 "QR 인쇄"를 누른 상태(프레임 11-print-mobile · 11-print-desktop). 학생에게는 이 상태가 없다.
모바일 = 바텀시트(tab-bar 위쪽 선 위, 위 A4 미리보기 + 아래 고정 영역), 데스크탑 = 가운데 ex-modal-card 형태. 예시 상태: 시약장 선택 = "모두"(기본값은 지금 시약장 "1번 시약장", 사용자가 "모두"로 바꿈) → A4 미리보기에 라벨 2개.
### 구성 요소
- nav-pill: "Lab_Stock" + "시약장 설정" + 현재 학교명 "샘플고등학교" + nav-account-menu ▾ (교사·admin만)
- nav-account-menu: 학교명 옆 ▾(닫힌 상태) (교사·admin만)
- cabinet-switcher: 시트 뒤 전환 pill 줄(누름 동작 없음). 하늘색: 활성 pill 채움·테두리 (교사·admin만)
- qr-print-sheet: 인쇄 시트 1개(#ffffff, 1px #e0e0e0 테두리, 위쪽 rounded 24, 여백 24, 오른쪽 위 × 닫기). 위→아래: 제목 heading-3 "QR 인쇄" → 시약장 선택 pill 줄 "(1) 1번 시약장" · "(2) 2번 시약장" · "모두"(storage-class-chip 모양 pill, 예시 "모두" 선택) → A4 미리보기 타일(#ffffff, 1px #f0f0f0 테두리, rounded 24, A4 비율) 안에 qr-label 2개를 격자로 → caption(#707070) "A4 한 장에 라벨 2개" → 하단 고정 전폭 button-primary "인쇄". 하늘색: 선택 pill #e6f4fc + 1px #2b9fe0 테두리(글자 #141414) — 미리보기 타일 안에는 하늘색 없음 (교사·admin만)
- qr-label: 인쇄 라벨 1개(미리보기 안 2개: 1번·2번 시약장). QR 이미지 1:1(rounded 0, 흑백) → 학교명 caption "샘플고등학교"(#141414) → cabinet-number + 시약장 이름 title "1번 시약장" → caption(#707070) "QR을 찍으면 이 시약장의 시약을 봐요". 라벨 테두리 1px #e0e0e0, rounded 16. 흑백만, 핑크·하늘색 없음 (교사·admin만)
- cabinet-number: qr-label 안 시약장 이름 앞 숫자 원 "1"·"2"(#ffffff, 1px #e0e0e0, label #141414)와 선택 pill 안 숫자 원 (교사·admin만)
- button-primary: qr-print-sheet 하단 "인쇄"(#141414 채움, #ffffff 글자, rounded 9999, 높이 44 이상). 하늘색 없음 (교사·admin만)
- tab-bar: 모바일 전용 하단 탭바 1개(화면 11과 같음). 데스크탑에는 두지 않는다 (교사·admin만)
- tab-item: 4개 "홈" · "시약" · "QR 스캔" · "기록". 활성 = "시약" (교사·admin만)
### 반영한 레퍼런스
- https://uibowl.io/name/%ED%8E%98%EC%9D%B4%EC%9B%8C%ED%81%AC?patterns=%ED%8A%9C%ED%86%A0%EB%A6%AC%EC%96%BC&imgId=cmtzo5k4p004jl704vz543akg

## 상태 화면 11-unsaved
교사·admin이 cabinet-edit에서 분류 칩을 바꾸고 저장하지 않은 채 cabinet-switcher의 "2번 시약장"(또는 tab-item 등 이탈)을 누른 상태(프레임 11-unsaved-mobile · 11-unsaved-desktop). 학생에게는 편집이 없어 이 상태가 없다.
뒤 화면은 화면 11(1번 시약장, 편집 중) 그대로. 확인 카드는 모바일 = tab-bar 위 바텀시트, 데스크탑 = 가운데. 딤 없음, 핑크 없음.
### 구성 요소
- nav-pill: "Lab_Stock" + "시약장 설정" + 현재 학교명 "샘플고등학교" + nav-account-menu ▾ (교사·admin만)
- nav-account-menu: 학교명 옆 ▾(닫힌 상태) (교사·admin만)
- cabinet-switcher: 카드 뒤 전환 pill 줄, 활성은 아직 "(1) 1번 시약장". 하늘색: 활성 pill 채움·테두리 (교사·admin만)
- cabinet-edit: 카드 뒤 편집 중 블록(누름 동작 없음) (교사·admin만)
- ex-modal-card: 확인 카드(#ffffff, 1px #e0e0e0 테두리, 그림자·딤 없음, rounded 24, 여백 24). 제목 heading-3 "저장하지 않은 변경이 있어요"(#141414) → body-sm(#707070) "이동하면 1번 시약장에서 바꾼 내용이 사라져요" → 가로 2버튼 button-outline "버리고 이동"(왼쪽) + button-primary "계속 편집"(오른쪽). 핑크·하늘색 없음 (교사·admin만)
- button-outline: 카드 "버리고 이동" — 편집을 버리고 누른 시약장(2번)으로 이동 (교사·admin만)
- button-primary: 카드 "계속 편집" — 카드를 닫고 편집 화면에 머문다. 하늘색 없음 (교사·admin만)
- tab-bar: 모바일 전용 하단 탭바 1개(화면 11과 같음). 데스크탑에는 두지 않는다 (교사·admin만)
- tab-item: 4개 "홈" · "시약" · "QR 스캔" · "기록". 활성 = "시약" (교사·admin만)
### 반영한 레퍼런스
- https://uibowl.io/name/%EC%85%94%ED%81%B4?patterns=%EC%B7%A8%EC%86%8C%ED%95%98%EA%B8%B0&imgId=cmrt4shpb0007l104b7hb2rnd
- https://uibowl.io/name/%EC%97%90%EC%9D%B4%EB%8B%B7?patterns=%EB%A1%9C%EA%B7%B8%EC%9D%B8%C2%B7%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85&imgId=cmtwlutwc000vju04jr6t829j

## 화면 12
QR 스캔. 학생·교사·admin 모두 들어온다. 샘플고등학교 시약장 QR만 연다. 다른 학교 QR·인식 실패면 안내 + 시약장 번호로 직접 찾기(N1). 스캔·번호 찾기 결과는 상태 화면 12-result.
모바일 활성 탭: "QR 스캔". 위→아래: nav-pill → segmented-control "QR 스캔 / 번호로 찾기" → 안내 → 카메라 프레임 → 안내 1줄 → 하단 고정 "시약장 번호로 찾기" → tab-bar.
데스크탑: nav-pill 아래 가운데 단일 열, tab-bar 없음.
### 구성 요소
- nav-pill: 닫기(이전 화면) + 제목 "QR 스캔" + 현재 학교명 "샘플고등학교" + nav-account-menu ▾. 하늘색: 닫기 아이콘 #2b9fe0, 데스크탑 현재 섹션 링크("QR 스캔") 밑줄 #2b9fe0
- nav-account-menu: 학교명 옆 ▾, 메뉴 항목 "로그아웃" 1개. 하늘색 없음
- segmented-control: "QR 스캔 / 번호로 찾기" 두 탭, 기본 "QR 스캔"
- segmented-control-active: 선택 탭 흰 pill. 하늘색: 1px #2b9fe0 테두리(글자 #141414)
- qr-scan: "QR 스캔" 탭 본문. heading-4 "시약장 문에 붙은 QR을 맞춰주세요" + body-sm(#707070) "카메라는 시약장 QR을 읽는 데만 사용해요" → 카메라 미리보기(#262626 채움, rounded 24) 안 1:1 코너 브라켓(#ffffff 선) → 아래 caption(#707070) "QR 인쇄 라벨의 번호로도 찾을 수 있어요" → button-pill-soft "플래시". 권한 없음 = #f3f3f3 자리 + "카메라 권한이 필요해요" + button-outline "권한 설정". 인식 실패·다른 학교 QR = 미리보기 아래 #141414 경고 아이콘 + #141414 body "QR을 읽지 못했어요. 시약장 번호로 찾아보세요" / "샘플고등학교 시약장 QR이 아니에요"(핑크 금지). 성공 → 상태 12-result. 하늘색: 인식 중 프레임 선 #2b9fe0
- qr-manual-entry: ① 하단 고정 button-outline "시약장 번호로 찾기"(→ "번호로 찾기" 탭, 모바일 tab-bar 바로 위). ② "번호로 찾기" 탭 본문: 라벨 "시약장 번호" + 숫자 text-input(플레이스홀더 "예: 1", QR 라벨·전환 pill의 cabinet-number와 같은 번호) + 하단 전폭 button-primary "찾기"(비면 비활성). 없는 번호 = #141414 아이콘 + body-sm "샘플고등학교에 이 번호의 시약장이 없어요". 찾으면 상태 12-result. 하늘색: 입력 왼쪽 아이콘 #2b9fe0
- text-input: qr-manual-entry "시약장 번호" 숫자 입력(#f0f0f0, rounded 16, 포커스 링 2px #141414)
- button-pill-soft: qr-scan "플래시"
- button-outline: 하단 고정 "시약장 번호로 찾기", 권한 상태 "권한 설정"
- button-primary: "번호로 찾기" 탭 "찾기". 하늘색 없음
- tab-bar: 모바일 전용 하단 탭바 1개(규격은 화면 3과 같음, QR 스캔 탭을 키우지 않음). 카메라 영역과 겹치지 않는다. 데스크탑에는 두지 않는다. 하늘색: 활성 tab-item 아이콘 #2b9fe0만
- tab-item: 4개 "홈" · "시약" · "QR 스캔" · "기록". 활성 = "QR 스캔". 비활성 3개 #707070
### 반영한 레퍼런스
- https://uibowl.io/name/%EC%B9%B4%EC%B9%B4%EC%98%A4T?patterns=%EC%B4%AC%EC%98%81%ED%95%98%EA%B8%B0&patternName=QR%EC%8A%A4%EC%BA%94-%EC%9E%90%EC%A0%84%EA%B1%B0%20%EB%B0%98%EB%82%A9
- https://uibowl.io/name/Atoms?patterns=%EC%B4%AC%EC%98%81%ED%95%98%EA%B8%B0&imgId=cm3vp36i0000al70czvfw3f09

## 상태 화면 12-result
스캔 성공 또는 번호 "1" 찾기 직후(프레임 12-result-mobile · 12-result-desktop). 모든 역할 같은 시트(역할별 차이 없음).
뒤 화면은 화면 12 카메라 화면 그대로, 위에 qr-result-sheet가 반쯤 올라온다. 모바일 = tab-bar 위쪽 선 위 바텀시트, 데스크탑 = 가운데 시트.
예시 상태: 1번 시약장 · 양문형 · 4단, 시약 4개 — 염산 1병(좌 1단, 재고 부족), 수산화나트륨 500g(좌 1단), 에탄올 200mL(좌 2단), 과산화수소 2병(우 1단, 재고 부족).
### 구성 요소
- nav-pill: 닫기 + "QR 스캔" + 현재 학교명 "샘플고등학교" + nav-account-menu ▾. 하늘색: 닫기 아이콘 #2b9fe0
- nav-account-menu: 학교명 옆 ▾(닫힌 상태)
- qr-scan: 시트 뒤에 보이는 카메라 미리보기 영역(#262626, rounded 24, 누름 동작 없음)
- qr-result-sheet: 결과 시트 1개(#ffffff, 1px #e0e0e0 테두리, 그림자·딤 없음, 위쪽 rounded 24, 여백 24). 위→아래: 제목 줄 cabinet-number "1" + heading-3 "1번 시약장" + 오른쪽 위 × 닫기 → caption(#707070) "양문형 · 4단 · 시약 4개" → reagent-row 4개(행마다 칸 위치) → 하단 전폭 button-pill-soft "배치도 보기"(→ 화면 11, 그 시약장 활성). 행을 누르면 화면 3 시약 상세. 하늘색: × 아이콘 #2b9fe0
- cabinet-number: 시트 제목 앞 숫자 원 "1"(#ffffff 채움, 1px #e0e0e0 테두리, rounded 9999, label #141414). 핑크·하늘색 글자 없음
- reagent-row: 시트 안 시약 행 = 시약명(title) + 재고량·단위(body) + 칸 위치 caption "좌 1단"(#141414) / 칸 없음이면 "칸 없음"(#707070). #f3f3f3 채움, rounded 16, 행 사이 12. 하늘색: 누른 행 배경 #e6f4fc
- badge-low-stock: 재고 부족 행(염산·과산화수소) 시약명 옆 "재고 부족"(#d6246a 채움, #ffffff label). 하늘색 없음
- button-pill-soft: 시트 하단 "배치도 보기"(#f3f3f3 채움, 라벨 #141414, rounded 9999, 높이 44 이상). 하늘색: 오른쪽 › 아이콘 #2b9fe0
- tab-bar: 모바일 전용 하단 탭바 1개(화면 12와 같음). 시트는 이 바 위에 붙는다. 데스크탑에는 두지 않는다
- tab-item: 4개 "홈" · "시약" · "QR 스캔" · "기록". 활성 = "QR 스캔"
### 반영한 레퍼런스
- https://uibowl.io/name/RailOne?patterns=%EA%B3%A0%EA%B0%9D%EC%84%BC%ED%84%B0%C2%B7FAQ&imgId=cmukplzwq001ale04e7612l65
- https://uibowl.io/name/%EC%B1%84%EB%B9%84?patterns=%EC%83%81%EC%84%B8%EC%A0%95%EB%B3%B4%20%28PDP%29&patternName=%EC%B6%A9%EC%A0%84%EC%86%8C

## 화면 13
홈. 로그인 후 첫 화면, 학생·교사·admin 모두. 같은 틀에서 역할마다 quick-action·카드 구성이 다르다. tab-bar 4개는 모든 역할 같다.
예시 상태: 전체 시약 42종, 재고 부족 3종(염산 · 1병, 에탄올 · 200mL, 질산은 · 5g), 시약장 2개(칸 16개 중 지정 14 · 미지정 2), 재주문 알림 3건, 최근 사용 기록 3줄.
모바일 활성 탭: "홈". 위→아래: nav-pill → quick-action(교사·admin 3칸 2+1, 학생 2칸) → home-summary ① 재고 요약 → (교사·admin) reorder-alert-card → home-summary ② 시약장 요약 → 최근 사용 기록 카드 → tab-bar. 카드 사이 24, 좌우 여백 16.
데스크탑: nav-pill 아래 2열(왼쪽 quick-action 3칸 한 줄 + home-summary, 오른쪽 (교사·admin) reorder-alert-card + 최근 사용 기록), tab-bar 없음.
### 구성 요소
- nav-pill: "Lab_Stock" 워드마크 + 현재 학교명 "샘플고등학교" + 학교명 옆 nav-account-menu ▾. 학교 선택·전환 없음. 모바일 = 얇은 헤더, 데스크탑 = 섹션 링크 유지. 하늘색: 데스크탑 현재 섹션 링크("홈") 밑줄 #2b9fe0
- nav-account-menu: 학교명 옆 ▾, 메뉴 항목 "로그아웃" 1개. 하늘색 없음
- quick-action: 역할별 작업 바로가기 칸(#f3f3f3 채움, rounded 16, 여백 16, 위 원형 아이콘 바탕 #e6f4fc 안 #2b9fe0 아이콘 + 아래 label link #141414, 칸 전체 누름 영역 44 이상, 칸 사이 12). 교사 3칸 "사용 기록 입력"(화면 4) · "입고"(화면 7, stock-intake 진입) · "시약장 설정"(화면 11). admin 3칸 "입고"(화면 7, stock-intake 진입) · "사용자 관리"(화면 8, user-manage 진입) · "시약장 설정"(화면 11). 모바일 3칸 = 위 2칸 같은 폭 + 아래 1칸 가로 전체(2+1), 데스크탑 = 한 줄 3칸. 학생 2칸 한 줄 "사용 기록 입력"(화면 4) · "시약장 보기"(화면 11 보기 전용). 탭과 겹치는 QR 스캔·시약 목록·사용 기록 내역 칸은 두지 않는다. 하늘색: 아이콘 #2b9fe0 + 아이콘 바탕 #e6f4fc, 누른 칸 #e6f4fc
- home-summary: 요약 카드 2장(#ffffff, 1px #f0f0f0 테두리, rounded 24, 여백 24). ① 재고 요약: heading-4 "재고 부족 3개" + badge-low-stock "3" → 부족 시약 칩 줄(#f3f3f3, rounded 9999, "염산 · 1병" 등, 누르면 화면 3) → "전체 시약 42종". 0개면 "부족한 시약이 없어요". ② 시약장 요약: heading-4 "시약장 요약 ›"(→ 화면 11) → display "2개" → 구간 막대(지정 #2b9fe0 + 미지정 #e0e0e0, rounded 9999) → body-sm(#707070) "칸 16개 중 지정 14 · 미지정 2". 시약장 0개면 ex-empty-state-card. 하늘색: 막대 지정 구간, › 아이콘
- badge-low-stock: 재고 요약 카드 개수 배지 "3", reorder-alert-card 제목 옆 "재고 부족"(#d6246a 채움, #ffffff label). 하늘색 없음
- reorder-alert-card: "재주문 알림" 카드(#f3f3f3, 테두리 없음, rounded 24, 여백 24). heading-4 "재주문 알림" + badge-low-stock + button-pill-soft "3건 ›"(→ 화면 6) + body "필요량보다 적은 시약이 3종 있어요". 판매처 연결 버튼은 두지 않는다. 하늘색 없음 (교사·admin만)
- reagent-row: 최근 사용 기록 카드(#ffffff, 1px #f0f0f0, rounded 24, 제목 heading-4 "최근 사용 기록") 안 3줄 = 시약명(title) + "김학생 · 20mL"(body) + "오늘 10:20"(caption #707070), #f3f3f3, rounded 16, 행 사이 12. 누르면 화면 10. 하늘색: 누른 행 #e6f4fc
- button-pill-soft: 최근 사용 기록 "더 보기 ›"(화면 10), reorder-alert-card "3건 ›"(교사·admin만). 하늘색: reorder-alert-card 밖 버튼의 › 아이콘만 #2b9fe0
- ex-empty-state-card: ① 시약장 0개: "등록된 시약장이 없어요" + 교사·admin에게만 button-outline "시약장 추가"(화면 11), 학생은 body-sm(#707070) "선생님이 시약장을 등록하면 보여요". ② 최근 사용 기록 0건: "아직 사용 기록이 없어요" + button-outline "사용 기록 입력". 하늘색: 안내 아이콘 #2b9fe0
- button-outline: ex-empty-state-card "시약장 추가"(교사·admin만), "사용 기록 입력"
- tab-bar: 모바일 전용 하단 탭바 1개(규격은 화면 3과 같음). 데스크탑에는 두지 않는다. 하늘색: 활성 tab-item 아이콘 #2b9fe0만
- tab-item: 4개 "홈" · "시약" · "QR 스캔" · "기록". 활성 = "홈". 역할별 작업은 tab-item으로 두지 않는다
### 반영한 레퍼런스
- https://uibowl.io/name/%EB%B9%BC%EA%B8%B0?patterns=%EB%A9%94%EC%9D%B8
- https://uibowl.io/name/RailOne?patterns=%EB%A9%94%EC%9D%B8&patternName=%ED%99%88
- https://uibowl.io/name/%EB%8B%AC%EB%8B%A4%EB%B0%A9?patterns=%EB%A9%94%EC%9D%B8
- https://uibowl.io/name/%ED%95%98%EB%82%98%EC%9B%90%ED%81%90?patterns=%EA%B3%84%EC%A2%8C&imgId=cmsebr5xp008sjx04yvvubhnj

## 역할별 노출
앱 전체(화면 1~13) 기준 개수. runs/20261004-2256 표를 기준으로 2026-10-06 변경을 반영했다.
바뀐 것: msds-entry 3 → 2 — 화면 12 결과가 상태 화면 12-result(qr-result-sheet)로 옮겨졌고, design.md qr-result-sheet 정의(시약 목록 + 칸 위치 + 배치도 보기)를 따라 MSDS 버튼을 두지 않음(행을 누르면 MSDS가 있는 화면 3으로 감). 남은 것 = 화면 3 1 + 화면 10 상세 1. cabinet-edit 2 → 3 — 홈 quick-action "시약장 설정"(교사·admin) 1 추가. 새 행: threshold-edit = 화면 3 1, location-edit = 화면 3 1, slot-assign = 상태 11-slot 칸 시트 1, qr-print = 화면 11 관리 줄 1 (모두 교사·admin, 학생 0). cabinet-add = 화면 11 1(그대로). 3-location·11-slot·11-print·11-unsaved는 교사·admin 전용 상태라 학생 숫자를 바꾸지 않는다. 학생 quick-action "시약장 보기"는 보기 전용이라 cabinet-edit이 아니다. cabinet-switcher·cabinet-number·slot-count·reagent-location·reorder-threshold·nav-account-menu는 모든 역할 공통이고 rules.json roles 대상이 아니라 표에 넣지 않는다.

| 컴포넌트 | 학생 | 교사 | admin |
|---|---|---|---|
| manual-upload | 0 | 2 | 2 |
| reorder-alert-card | 0 | 2 | 2 |
| vendor-link | 0 | 1 | 1 |
| vendor-register | 0 | 0 | 2 |
| msds-entry | 2 | 2 | 2 |
| stock-intake | 0 | 2 | 2 |
| reagent-register | 0 | 1 | 1 |
| threshold-edit | 0 | 1 | 1 |
| user-manage | 0 | 0 | 2 |
| cabinet-edit | 0 | 3 | 3 |
| cabinet-add | 0 | 1 | 1 |
| slot-assign | 0 | 1 | 1 |
| location-edit | 0 | 1 | 1 |
| qr-print | 0 | 1 | 1 |
