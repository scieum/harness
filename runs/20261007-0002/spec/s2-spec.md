# S2 설계 — run 20261007-0002

대상 화면: 2 (시약 목록), 3 (시약 상세), 7 (입고·시약 등록) + 상태 화면 2-msds-bulk, 3-location, 3-msds, 7-doc-upload, 7-doc-review, 7-doc-fail, 7-suggest, 7-msds · 학교: 샘플고등학교 (input.json)
변경 사유: 2026-10-07 사용자 결정(개발 세션 요청 2) — 서류로 입고, MSDS 자동 찾기, 위치 자동 추천, 자동 재주문 기준 표시. 근거: docs/PRD.md §3·§4·§7(2·3·7), docs/story-service.md 결정 사항 2026-10-06 행("시약 칸 배치"·"재주문 기준 직접 입력"·"앱 예외 반영")과 2026-10-07 행("서류로 입고"·"MSDS 자동 찾기"·"위치 자동 추천"·"자동 재주문 기준 표시"), docs/design.md("Document intake"·"MSDS search"·"Location suggestion"·"Auto reorder threshold"·"Reagent slots"), harness/rules.json(roles R1~R7, screens_required 3·7, variants 2·3·7, intake, msds, suggest, reorder.auto, colors, tab_bar), research/s1-adopt.md.
기준 설계(수정하지 않음): 화면 3 = runs/20261006-1223, 화면 2·7 = runs/20261002-1441 + 공통 nav-account-menu(runs/20261006-1223). 기존 구성 요소를 유지하고 2026-10-07 결정분만 더하거나 바꾼다.
S1이 레퍼런스를 찾지 못한 부분(화면 7 확인 표 구조, 화면 3 '자동' 표시)은 docs/design.md 정의(doc-intake-table·doc-item-row·reagent-link·new-reagent-fields, auto-threshold-badge)대로 설계한다.
색·폰트·모서리·간격은 docs/design.md와 harness/rules.json을 따른다. 허용 색 밖의 값(딤 반투명 검정 등)은 쓰지 않는다. 반투명 회색은 badge-overlay 안에서만. 그림자는 쓰지 않는다(segmented-control-active 예외).
- 핑크 #d6246a·연핑크 #fbe9f0는 badge-low-stock, reorder-alert-card, mix-warning 안에서만 쓴다. 서류 읽기 실패·MSDS 없음·후보 0개·맞는 칸 없음 안내에는 핑크를 쓰지 않고 #141414 아이콘 + #141414/#707070 문구로만 표시한다.
- 하늘색 #2b9fe0(선·인디케이터·아이콘·진행 막대)과 옅은 하늘색 #e6f4fc(선택 배경·안내 띠)는 선택 상태·활성 탭·진행·아이콘·msds-bulk-banner 띠·suggest-badge에만 쓴다. 글자색으로 쓰지 않고(그 위 글자는 #141414), badge-low-stock·reorder-alert-card·button-primary·mix-warning 안에는 쓰지 않는다.
- suggest-badge = #e6f4fc 채움 + 1px #2b9fe0 테두리 + #141414 label "추천"(핑크 금지). auto-threshold-badge = #f3f3f3 채움 + #141414 label "자동"(핑크·하늘색 금지).
학교 선택은 회원가입(화면 14)에만 있다. 이번 대상 화면과 상태 화면에는 학교 선택을 두지 않고 nav-pill 안에 현재 학교명 "샘플고등학교"를 표시한다. 학교 전환 기능은 두지 않는다. 시약·서류 품목 연결·MSDS 연결·추천 칸은 모두 샘플고등학교 것만 보인다(N1).
외부 서비스 연결 값(AI 읽기·MSDS 조회)은 서버에서만 다룬다. 어떤 화면에도 연결 값 입력 칸·외부 서비스 설정·AI 엔진 선택 UI·관련 문구를 두지 않는다(N2).
괄호 안 역할 표시가 없는 구성 요소는 학생·교사·admin 모두에게 보인다. 학생 화면에는 doc-upload, msds-search, msds-bulk-banner, stock-intake, reagent-register, threshold-edit, location-edit를 그리지 않는다(R5·R7). 화면 7과 그 상태 화면은 교사·admin 전용이다.
모바일 공통: tab-bar는 화면 아래 가장자리 y 780~844(높이 64, rounded 0)에 붙고 본문 스크롤은 y 780에서 끝난다. 하단 고정 버튼은 tab-bar 바로 위(간격 16). 바텀시트는 tab-bar 위쪽 선 위에 붙는다(딤 없음, 1px #e0e0e0 테두리로 구분, 위쪽 rounded 24, 오른쪽 위 × 닫기). 데스크탑에는 tab-bar 없이 nav-pill 섹션 링크를 유지하고, 시트는 화면 가운데 ex-modal-card 크기로 연다.
nav-account-menu(공통): 모든 대상 화면의 nav-pill 학교명 "샘플고등학교" 옆 작은 ▾. 메뉴 항목 "로그아웃" 1개. 프레임에는 닫힌 상태(▾만)로 그린다.

## 화면 2
시약 목록. 학생·교사·admin 모두 들어온다. 교사·admin에게는 MSDS 없는 시약이 있을 때 목록 위에 일괄 찾기 띠(msds-bulk-banner)가 보인다. 학생 화면에는 띠가 없다.
예시 상태: 시약 42종 중 MSDS 없는 시약 4종, 재고 부족 3종(염산 · 1병, 에탄올 · 200mL, 질산은 · 5g).
모바일 활성 탭: "시약". 위→아래: nav-pill → (교사·admin) msds-bulk-banner(제목 바로 아래, 필터 위 고정) → segmented-control "전체 / 재고 부족" → 검색 text-input → reagent-row 목록 → tab-bar. 좌우 여백 16, 행 사이 12.
데스크탑: nav-pill 아래 가운데 단일 열 같은 순서, 띠는 본문 열 전체 폭, tab-bar 없음.
### 구성 요소
- nav-pill: "Lab_Stock" 워드마크 + 현재 학교명 "샘플고등학교" + 학교명 옆 nav-account-menu ▾. 데스크탑 섹션 링크("시약 목록", 교사·admin에게만 "재주문 알림"). 학교 전환 기능 없음. 하늘색: 데스크탑 현재 섹션 링크("시약 목록") 아래 #2b9fe0 밑줄(글자 #141414)
- nav-account-menu: 학교명 옆 ▾, 메뉴 항목 "로그아웃" 1개. 하늘색 없음
- msds-bulk-banner: nav-pill 바로 아래·필터 위, 높이 한 줄짜리 전체 폭 띠(모바일 x 0, 폭 390, rounded 0, #e6f4fc 채움, 테두리 없음, 안쪽 여백 12·16). 왼쪽 body-sm #141414 "MSDS 없는 시약 4종", 오른쪽 button-pill-soft "한 번에 찾기"(높이 44 이상) 1개만. 누르면 상태 화면 2-msds-bulk. 목록 행 구조는 바꾸지 않는다. MSDS 없는 시약이 0종이면 띠를 숨긴다. 하늘색: 띠 채움 #e6f4fc (교사·admin만)
- button-pill-soft: msds-bulk-banner 안 "한 번에 찾기"(#f3f3f3 채움, 라벨 #141414, rounded 9999). 하늘색 없음 (교사·admin만)
- segmented-control: 리스트 위 필터 "전체 / 재고 부족", 한 번에 하나
- segmented-control-active: 선택 필터 흰 pill. 하늘색: 1px #2b9fe0 테두리(글자 #141414)
- text-input: 필터 아래 검색 바 "시약명 검색"(#f0f0f0, rounded 16, 포커스 링 2px #141414). 하늘색: 검색 아이콘 #2b9fe0
- reagent-row: 시약 한 줄 = 시약명(title) + 재고량·단위(body) + 입고일(caption #707070), #f3f3f3, rounded 16, 행 사이 12. 누르면 화면 3. 하늘색: 오른쪽 › 아이콘 #2b9fe0, 누른 행 배경 #e6f4fc
- badge-low-stock: 재고 부족 행 시약명 옆 "재고 부족"(#d6246a 채움, #ffffff label). 하늘색 없음
- ex-empty-state-card: 검색·필터 결과 0건 "찾는 시약이 없어요". 하늘색: 안내 아이콘 #2b9fe0
- tab-bar: 모바일 전용 하단 탭바 1개(x 0, 폭 390, 높이 64, y 780~844, rounded 0, #ffffff + 위쪽 1px #f0f0f0 선, 그림자 없음, tab-item 4개 같은 폭). 데스크탑에는 두지 않는다. 하늘색: 활성 tab-item 아이콘 #2b9fe0만
- tab-item: "홈" · "시약" · "QR 스캔" · "기록" 4개, 사각형 누름 영역(rounded 0), 높이 48, 아이콘 위 + label 아래. 활성 = "시약"(#2b9fe0 아이콘 + 라벨 #141414), 비활성 3개 #707070
### 반영한 레퍼런스
- https://uibowl.io/name/%EC%BD%94%EB%B9%97?patterns=%EB%AA%A9%EB%A1%9D%20%28PLP%29&imgId=cmr8h8m21000ijk0451n114b1
- https://uibowl.io/name/%EB%AF%B8%EB%9E%98%EC%97%90%EC%85%8B%EC%A6%9D%EA%B6%8C%20M-STOCK?patterns=%EC%95%BD%EA%B4%80%EB%8F%99%EC%9D%98&imgId=cmrx9e5zg0019jv04zrb4nm94
- https://uibowl.io/name/MEXC?patterns=%EB%AA%A9%EB%A1%9D%20%28PLP%29&imgId=cmu9n15e0001vkx04vvzg8864

## 상태 화면 2-msds-bulk
교사·admin이 화면 2 띠의 "한 번에 찾기"를 누른 상태(프레임 2-msds-bulk-mobile · 2-msds-bulk-desktop). 학생에게는 이 상태가 없다.
뒤 화면은 화면 2 그대로(딤 없음). MSDS 없는 시약 4종을 차례로 하나씩 msds-candidates 시트로 보여준다. 예시 = 첫 번째 시약 "질산은"(1 / 4), 후보 3개 중 첫 후보를 고른 상태. 모바일 = tab-bar 위 바텀시트, 데스크탑 = 가운데 시트.
### 구성 요소
- nav-pill: 화면 2 nav-pill 그대로 — "Lab_Stock" + 현재 학교명 "샘플고등학교" + nav-account-menu ▾ (교사·admin만)
- nav-account-menu: 학교명 옆 ▾(닫힌 상태) (교사·admin만)
- msds-bulk-banner: 시트 뒤에 보이는 띠 "MSDS 없는 시약 4종"(#e6f4fc, 누름 동작 없음) (교사·admin만)
- reagent-row: 시트 뒤 목록 행(누름 동작 없음) (교사·admin만)
- msds-candidates: 시트 1개(#ffffff, 1px #e0e0e0 테두리, 위쪽 rounded 24, 여백 24, 오른쪽 위 × 닫기). 위→아래: 제목 heading-3 시약명 "질산은" + 오른쪽 caption(#707070) "1 / 4" → caption(#707070) "알맞은 MSDS를 골라 주세요" → 후보 행 3개(행 = 물질명 title #141414 위 + "CAS 7761-88-8" caption #707070 아래, #f3f3f3 채움, rounded 16, 행 사이 12, 누름 영역 44 이상): "질산은" · "질산은 용액" · "질산은(분석용)" — 선택 행 = 첫 행 → 목록 맨 끝 행 "찾는 게 없어요 — 직접 입력"(누르면 그 자리에서 text-input "MSDS 주소"가 펼쳐짐) → 하단 줄: 왼쪽 조용한 텍스트 동작 "건너뛰기"(link #141414, 채움·테두리 없음, 누름 영역 44 이상) + 오른쪽 button-primary "이 MSDS로". 후보 0개면 후보 자리에 body-sm #141414 "찾지 못했어요 — 직접 입력" + text-input. 고르기 전에는 "이 MSDS로" 비활성. "이 MSDS로"·"건너뛰기" 뒤에는 다음 시약(2 / 4)으로 넘어간다. 하늘색: 선택 행 배경 #e6f4fc + 오른쪽 #2b9fe0 체크 아이콘(글자 #141414) (교사·admin만)
- text-input: "직접 입력" 행을 펼쳤을 때 "MSDS 주소" 입력(#f0f0f0, rounded 16, 포커스 링 2px #141414). 하늘색 없음 (교사·admin만)
- button-primary: 시트 하단 "이 MSDS로"(#141414 채움, #ffffff 글자, rounded 9999, 높이 44 이상). 하늘색 없음 (교사·admin만)
- ex-toast: 마지막 시약까지 끝난 뒤 "MSDS 3종을 연결했어요 · 1종 건너뜀", 띠 숫자가 줄어든다. 하늘색: 완료 체크 아이콘 #2b9fe0 (교사·admin만)
- tab-bar: 모바일 전용 하단 탭바 1개(화면 2와 같음). 시트는 이 바 위쪽 선 위에 붙는다. 데스크탑에는 두지 않는다 (교사·admin만)
- tab-item: 4개 "홈" · "시약" · "QR 스캔" · "기록". 활성 = "시약" (교사·admin만)
### 반영한 레퍼런스
- https://uibowl.io/name/CJ%EB%8D%94%EB%A7%88%EC%BC%93?patterns=%EC%83%81%EC%84%B8%EC%A0%95%EB%B3%B4%20%28PDP%29&imgId=cmnn6372y0019l404vauwc9wd
- https://uibowl.io/name/MEXC?patterns=%EB%AA%A9%EB%A1%9D%20%28PLP%29&imgId=cmu9n15e0001vkx04vvzg8864

## 화면 3
시약 상세. 학생·교사·admin 모두 들어온다. 교사·admin은 보관 위치를 바꾸고(location-edit) 재주문 기준을 숫자로 고친다(threshold-edit). 학생은 보기만 한다. 재주문 기준을 아무도 정하지 않은 시약은 자동 기준을 보여주고 auto-threshold-badge "자동"을 붙인다(rules.json reorder.auto). 직접 입력·매뉴얼 추출 값이 있으면 그 값이 우선이고 배지는 없다.
예시 상태: 과산화수소, 현재 재고 2병, 재주문 기준 = 자동 3병(재고 부족 배지 표시), 보관 위치 "1번 시약장 · 우 1단"(분류 산화제 칸), MSDS 있음.
모바일 활성 탭: "시약". 위→아래: nav-pill → reagent-detail-card(시약명·재고 → reagent-location 줄 → reorder-threshold 줄) → segmented-control "정보 / 사용 기록" → 표 → msds-entry → 하단 고정 "사용 기록"(+ 교사·admin "입고") → tab-bar. 좌우 여백 16, 블록 사이 24.
데스크탑: nav-pill 아래 가운데 단일 열 같은 순서, tab-bar 없음.
### 구성 요소
- nav-pill: 뒤로가기(화면 2) + 제목 "시약 상세" + 현재 학교명 "샘플고등학교" + 학교명 옆 nav-account-menu ▾. 학교 전환 기능 없음. 하늘색: 뒤로가기 아이콘 #2b9fe0
- nav-account-menu: 학교명 옆 ▾, 메뉴 항목 "로그아웃" 1개. 하늘색 없음
- reagent-detail-card: 상단 요약 카드(#ffffff, 1px #f0f0f0 테두리, rounded 24, 여백 24). 시약명(title) + badge-low-stock, 현재 재고 display "2" + 단위 "병", 입고일 caption 라벨-값, 그 아래 reagent-location 줄과 reorder-threshold 줄을 한 줄씩 쌓는다. 하늘색 없음
- badge-low-stock: 재고 2병 < 재주문 기준 3병이라 시약명 옆 "재고 부족"(#d6246a 채움, #ffffff label). 자동 기준이어도 같은 규칙. 하늘색 없음
- reagent-location: 카드 안 한 줄. caption "보관 위치"(#707070) + 값 "cabinet-number(1) 1번 시약장 · 우 1단"(body #141414). 칸이 없으면 "칸 없음"(#707070). 교사·admin은 줄 오른쪽에 location-edit. 학생은 값만 본다
- cabinet-number: reagent-location 값 앞 작은 원(#ffffff, 1px #e0e0e0 테두리, rounded 9999) 안 숫자 "1"(label #141414). 핑크·하늘색 글자 없음
- location-edit: reagent-location 줄 오른쪽 button-pill-soft "위치 바꾸기"(#f3f3f3, 라벨 #141414, rounded 9999, 높이 44 이상). 누르면 상태 화면 3-location의 location-picker(추천 칸 suggest-badge가 처음 선택) (교사·admin만)
- reorder-threshold: 카드 안 reagent-location 아래 한 줄. caption "재주문 기준"(#707070) + 값 "3병"(body #141414) + 값 오른쪽 auto-threshold-badge "자동", 줄 아래 caption(#707070) "최근 사용량으로 계산했어요" 한 줄. 값이 없고 자동 계산도 못 하면 "아직 없어요"(#707070). 화면 5 AI 추출 값과 같은 칸. 학생은 값·배지·캡션만 본다
- auto-threshold-badge: reorder-threshold 값 옆 작은 pill "자동"(#f3f3f3 채움, 테두리 없음, rounded 9999, label #141414). 직접 입력·매뉴얼 추출 값이면 배지와 캡션을 그리지 않는다. 핑크·하늘색 없음 — 정보이지 결정 신호가 아니다. 모든 역할
- threshold-edit: reorder-threshold 값 오른쪽 연필 아이콘(누름 영역 44 이상). 누르면 값 자리가 숫자 text-input(값 "3" + 단위 suffix "병")과 줄 아래 button-primary "저장"으로 바뀐다. 저장하면 직접 입력 값이 되어 "자동" 배지·캡션이 사라진다. 빈 값·음수는 입력 아래 #141414 body-sm "1 이상 입력하세요"(핑크 금지). 하늘색: 연필 아이콘 #2b9fe0 (교사·admin만)
- text-input: threshold-edit 편집 상태 숫자 입력(#f0f0f0, 테두리 없음, rounded 16, 포커스 링 2px #141414, 단위 suffix #707070) (교사·admin만)
- segmented-control: 요약 아래 "정보 / 사용 기록" 두 탭
- segmented-control-active: 활성 탭 흰 pill. 하늘색: 활성 탭 아래 #2b9fe0 인디케이터(글자 #141414)
- ex-data-table-cell: "정보" 탭 = 시약 속성 라벨-값 표, "사용 기록" 탭 = 날짜·사용자·사용량 3열 표. 하늘색: 가장 최근 사용 기록 행 배경 #e6f4fc
- msds-entry: MSDS 블록. MSDS가 있으면 msds-qr-tile(QR 1:1, rounded 0, 아래 라벨 "QR로 MSDS 열기") + button-pill-soft "MSDS 보기 ↗". 학생·교사·admin 모두 1개. MSDS가 없는 시약이면 QR 자리에 caption(#707070) "MSDS가 아직 없어요"를 두고, 교사·admin에게만 그 아래 msds-search(상태 화면 3-msds). 하늘색: ↗ 아이콘 #2b9fe0
- msds-search: MSDS 없는 시약일 때 msds-entry 안 button-pill-soft "MSDS 찾기"(#f3f3f3, 라벨 #141414, rounded 9999, 높이 44 이상). 누르면 상태 화면 3-msds의 msds-candidates. 예시 시약(과산화수소)은 MSDS가 있어 이 프레임에는 그리지 않는다. 하늘색: 왼쪽 검색 아이콘 #2b9fe0 (교사·admin만)
- button-primary: 하단 고정 "사용 기록"(→ 화면 4, 모든 역할), threshold-edit 편집 상태 "저장"(교사·admin). #141414 채움, #ffffff 글자, rounded 9999, 높이 44 이상. 하늘색 없음
- button-outline: 하단 고정 "사용 기록" 옆 "입고"(→ 화면 7) (교사·admin만)
- ex-toast: 저장 직후 "재주문 기준을 3병으로 바꿨어요" / "보관 위치를 바꿨어요". 모바일은 tab-bar 위. 하늘색: 완료 체크 아이콘 #2b9fe0 (교사·admin만)
- tab-bar: 모바일 전용 하단 탭바 1개(화면 2와 같은 규격). 데스크탑에는 두지 않는다. 하늘색: 활성 tab-item 아이콘 #2b9fe0만
- tab-item: "홈" · "시약" · "QR 스캔" · "기록" 4개. 활성 = "시약", 비활성 3개 #707070
### 반영한 레퍼런스
- https://uibowl.io/name/Bitget?patterns=%EC%9D%B8%EC%A6%9D%ED%95%98%EA%B8%B0&imgId=cmukqaul5002ll60430j2ykk1
- https://uibowl.io/name/%ED%86%A0%EC%8A%A4%EC%A6%9D%EA%B6%8C?patterns=%EC%BB%A4%EB%AE%A4%EB%8B%88%ED%8B%B0&imgId=cmsb4ub9l0009jo042gue22tj

## 상태 화면 3-location
교사·admin이 화면 3에서 "위치 바꾸기"를 누른 상태(프레임 3-location-mobile · 3-location-desktop). 학생에게는 이 상태가 없다.
뒤 화면은 화면 3 그대로(딤 없음). 위에 location-picker. 모바일 = tab-bar 위 바텀시트, 데스크탑 = 가운데 시트.
예시 상태: 현재 위치 1번 시약장 · 우 1단(산화제, 시약 3개). 추천 규칙(rules.json suggest.rule: 분류가 맞고 금지 조합이 없는 칸 → 시약 적은 칸 → 시약장 번호·칸 순)에 따라 2번 시약장 · 우 2단(산화제, 시약 0개)이 추천 칸이고, 피커는 2번 시약장이 열린 채 그 칸이 처음 선택되어 있다. 분류가 맞아 mix-warning은 숨김.
### 구성 요소
- nav-pill: 뒤 화면 3 nav-pill 그대로 — 뒤로가기 + "시약 상세" + 현재 학교명 "샘플고등학교" + nav-account-menu ▾. 하늘색: 뒤로가기 아이콘 #2b9fe0 (교사·admin만)
- nav-account-menu: 학교명 옆 ▾(닫힌 상태) (교사·admin만)
- reagent-detail-card: 시트 뒤 화면 3 요약 카드(누름 동작 없음). 하늘색 없음 (교사·admin만)
- reagent-location: 시트 뒤 카드 안 "보관 위치 · (1) 1번 시약장 · 우 1단" — 저장 전이라 옛 위치 (교사·admin만)
- location-picker: 시트 1개(#ffffff, 1px #e0e0e0 테두리, 위쪽 rounded 24, 여백 24). 위→아래: 제목 heading-3 "보관 위치 바꾸기" + × 닫기 → caption(#707070) "과산화수소 · 산화제" → 구역 제목 heading-4 "추천" + 추천 칸 1행(cabinet-number "2" + "2번 시약장 · 우 2단" body #141414 + suggest-badge, 선택 상태 #e6f4fc 배경) → 구역 제목 heading-4 "전체" + cabinet-switcher → 고른 시약장의 cabinet-slot 배치도(양문형 · 3단, 각 칸 분류 이름 + slot-count) → 조용한 텍스트 동작 "칸 없음으로"(link #141414, 누름 영역 44 이상) → mix-warning(조건부) → 하단 전폭 button-primary "저장". 추천 칸이 처음 선택이라 "저장"은 바로 활성 (교사·admin만)
- cabinet-switcher: "전체" 구역 시약장 전환 pill 한 줄 "(1) 1번 시약장" · "(2) 2번 시약장". 활성 = "2번 시약장"(#e6f4fc 채움 + 1px #2b9fe0 테두리, 라벨 #141414), 비활성 #f3f3f3. 피커 안에는 cabinet-add 없음. 하늘색: 활성 pill 채움·테두리 (교사·admin만)
- cabinet-number: 추천 행·cabinet-switcher pill 이름 앞 작은 원(#ffffff, 1px #e0e0e0) 안 숫자 "1"·"2"(label #141414) (교사·admin만)
- cabinet-slot: 2번 시약장 배치도 칸 6개(#f3f3f3, rounded 16, 분류 이름 label #141414, 없으면 "미지정" #707070). 왼쪽 단 라벨 "1단"~"3단", 위 문 라벨 "좌"/"우". 누르면 그 칸 선택. 선택 칸 = "우 2단"(산화제). 하늘색: 선택 칸 배경 #e6f4fc + 2px #2b9fe0 테두리(글자 #141414) (교사·admin만)
- slot-count: 시약이 있는 cabinet-slot 오른쪽 위 작은 pill(#ffffff, rounded 9999, label #141414) — 예: 좌 1단 "2", 좌 2단 "3". 빈 칸(우 2단 포함)에는 없음. 핑크·하늘색 없음 (교사·admin만)
- suggest-badge: 추천 칸 표시 pill "추천"(#e6f4fc 채움, 1px #2b9fe0 테두리, label #141414, rounded 9999). 두 곳 — "추천" 구역 행 오른쪽, 배치도의 우 2단 칸 왼쪽 위 모서리. 선택 상태(칸 테두리)와는 따로 보인다. 핑크 금지 (교사·admin만)
- mix-warning: 다른 칸을 골라 분류가 맞지 않을 때만 배치도 아래(#fbe9f0 바탕, rounded 16, #d6246a 경고 아이콘 + #141414 body-sm). "이 칸은 {분류} 칸이에요 — 그래도 넣을 수 있어요" / 금지 조합이면 "{A}와 {B}는 섞으면 위험해요" + "그래도 저장할 수 있어요". 이 예시(추천 칸 선택)에서는 숨김. 하늘색 없음 (교사·admin만)
- button-primary: 피커 하단 전폭 "저장"(#141414 채움, #ffffff 글자, rounded 9999, 높이 44 이상). mix-warning이 있어도 활성. 하늘색 없음 (교사·admin만)
- tab-bar: 모바일 전용 하단 탭바 1개(화면 3과 같음). 시트는 이 바 위에 붙는다. 데스크탑에는 두지 않는다 (교사·admin만)
- tab-item: 4개 "홈" · "시약" · "QR 스캔" · "기록". 활성 = "시약" (교사·admin만)
### 반영한 레퍼런스
- https://uibowl.io/name/Bitget?patterns=%EC%9D%B8%EC%A6%9D%ED%95%98%EA%B8%B0&imgId=cmukqaul5002ll60430j2ykk1
- https://uibowl.io/name/%ED%81%AC%EB%AA%BD?patterns=%EC%98%88%EC%95%BD%C2%B7%EA%B2%B0%EC%A0%9C&imgId=cmopq830p000zlb0439kx2zpr

## 상태 화면 3-msds
교사·admin이 MSDS 없는 시약의 상세에서 "MSDS 찾기"를 누른 상태(프레임 3-msds-mobile · 3-msds-desktop). 학생에게는 이 상태가 없다(학생은 msds-entry 자리에 "MSDS가 아직 없어요"만 본다).
예시 상태: 질산은 상세(재고 5g). 뒤 화면 = 화면 3(MSDS 없음 상태), 위에 msds-candidates 시트. 후보 3개 중 첫 후보 선택. 모바일 = tab-bar 위 바텀시트, 데스크탑 = 가운데 시트.
### 구성 요소
- nav-pill: 뒤로가기 + "시약 상세" + 현재 학교명 "샘플고등학교" + nav-account-menu ▾. 하늘색: 뒤로가기 아이콘 #2b9fe0 (교사·admin만)
- nav-account-menu: 학교명 옆 ▾(닫힌 상태) (교사·admin만)
- reagent-detail-card: 시트 뒤 질산은 요약 카드(누름 동작 없음). 하늘색 없음 (교사·admin만)
- msds-entry: 시트 뒤 MSDS 블록 — QR 자리에 caption(#707070) "MSDS가 아직 없어요" + 그 아래 msds-search (교사·admin만)
- msds-search: msds-entry 안 button-pill-soft "MSDS 찾기"(눌린 상태, 시트가 열림). 하늘색: 검색 아이콘 #2b9fe0 (교사·admin만)
- msds-candidates: 시트 1개(#ffffff, 1px #e0e0e0 테두리, 위쪽 rounded 24, 여백 24, × 닫기). 위→아래: 제목 heading-3 "MSDS 찾기" → caption(#707070) "질산은" → 검색 text-input(값 "질산은", 바꿔서 다시 찾을 수 있음) → 후보 행 3개(물질명 title 위 + "CAS 7761-88-8" caption #707070 아래, #f3f3f3, rounded 16, 행 사이 12): "질산은" · "질산은 용액" · "질산은(분석용)", 선택 = 첫 행 → 목록 맨 끝 "찾는 게 없어요 — 직접 입력" 행(누르면 그 자리에서 "MSDS 주소" text-input이 펼쳐짐) → 하단 전폭 button-primary "이 MSDS로". 후보 0개 = 결과 자리에 body-sm #141414 "찾지 못했어요 — 직접 입력" + text-input. 고르기 전 "이 MSDS로" 비활성. 하늘색: 선택 행 배경 #e6f4fc + 오른쪽 #2b9fe0 체크 아이콘(글자 #141414) (교사·admin만)
- text-input: 시트 안 검색 입력과 "직접 입력" 펼침의 "MSDS 주소" 입력(#f0f0f0, rounded 16, 포커스 링 2px #141414). 하늘색: 검색 아이콘 #2b9fe0 (교사·admin만)
- button-primary: 시트 하단 "이 MSDS로"(#141414 채움, #ffffff 글자, rounded 9999, 높이 44 이상). 하늘색 없음 (교사·admin만)
- ex-toast: 연결 직후 "MSDS를 연결했어요" → msds-entry가 QR + "MSDS 보기 ↗"로 바뀐다. 하늘색: 완료 체크 아이콘 #2b9fe0 (교사·admin만)
- tab-bar: 모바일 전용 하단 탭바 1개(화면 3과 같음). 시트는 이 바 위에 붙는다. 데스크탑에는 두지 않는다 (교사·admin만)
- tab-item: 4개 "홈" · "시약" · "QR 스캔" · "기록". 활성 = "시약" (교사·admin만)
### 반영한 레퍼런스
- https://uibowl.io/name/%ED%86%A0%EC%8A%A4%EC%A6%9D%EA%B6%8C?patterns=%EC%BB%A4%EB%AE%A4%EB%8B%88%ED%8B%B0&imgId=cmsb4ub9l0009jo042gue22tj
- https://uibowl.io/name/%EC%95%B3%ED%94%8C%EB%A6%AC?patterns=%EA%B2%80%EC%83%89&imgId=cmtpokg65000pi804zwlm86ih
- https://uibowl.io/name/%EB%84%A4%EC%9D%B4%EB%B2%84%EB%B8%94%EB%A1%9C%EA%B7%B8?patterns=%ED%95%84%ED%84%B0&imgId=cmumdx3pp008yjm04zoku825b

## 화면 7
입고·시약 등록. 교사·admin만 들어온다(홈 quick-action "입고", 화면 3 "입고", 데스크탑 nav-pill 섹션 링크). 학생에게는 진입 링크가 없다.
맨 위 intake-mode로 "직접 입력 / 서류로 입고"를 고른다. 기본 = "서류로 입고". 이 프레임은 서류로 입고의 첫 상태(아직 파일 없음). 파일을 올린 뒤의 흐름은 상태 화면 7-doc-upload(읽는 중) → 7-doc-review(확인 표) → 7-suggest(위치 추천), 실패는 7-doc-fail, MSDS 고르기는 7-msds.
"직접 입력"을 고르면 기존 구성(runs/20261002-1441 화면 7: segmented-control "기존 시약 입고 / 새 시약 등록" + stock-intake / reagent-register)이 그대로 나오고, 새 시약 등록 폼의 MSDS 칸 옆에 msds-search가 붙는다. 직접 입력 화면은 이 프레임에 그리지 않는다.
모바일 활성 탭: "시약". 위→아래: nav-pill → intake-mode → doc-upload → tab-bar. 좌우 여백 16, 블록 사이 24.
데스크탑: nav-pill 아래 가운데 단일 열 같은 순서, tab-bar 없음.
### 구성 요소
- nav-pill: "Lab_Stock" 워드마크 + 제목 "입고·시약 등록" + 현재 학교명 "샘플고등학교" + 학교명 옆 nav-account-menu ▾. 하늘색: 데스크탑 현재 섹션 링크("입고·시약 등록") 밑줄 #2b9fe0 (교사·admin만)
- nav-account-menu: 학교명 옆 ▾, 메뉴 항목 "로그아웃" 1개 (교사·admin만)
- intake-mode: 화면 맨 위 segmented-control 두 옵션 "직접 입력 / 서류로 입고", 한 번에 하나. 기본·이 프레임 = "서류로 입고"(segmented-control-active) (교사·admin만)
- segmented-control: intake-mode의 트랙(#f3f3f3, rounded 9999), 그리고 "직접 입력" 모드 안의 "기존 시약 입고 / 새 시약 등록" 토글 (교사·admin만)
- segmented-control-active: 선택 옵션 흰 pill. 하늘색: 1px #2b9fe0 테두리(글자 #141414) (교사·admin만)
- doc-upload: 올리기 영역 카드 1개(ex-empty-state-card 모양, #ffffff, 1px #e0e0e0 테두리, rounded 24, 여백 24). 가운데 업로드 아이콘 → heading-4 "품의서·영수증·거래명세서를 올려 주세요" → caption(#707070) "PDF·JPG·PNG, 4MB까지" → 2열 button-pill-soft "촬영하기" · "파일 선택"(같은 폭, 높이 44 이상) → 하단 전폭 button-primary "AI로 읽기"(파일이 없으면 비활성). 4MB를 넘거나 다른 형식이면 카드 안 #141414 아이콘 + body-sm "PDF·JPG·PNG 4MB까지만 올릴 수 있어요"(핑크 금지). 하늘색: 업로드 아이콘 #2b9fe0 (교사·admin만)
- button-pill-soft: doc-upload 안 "촬영하기" · "파일 선택"(#f3f3f3, 라벨 #141414, rounded 9999). 하늘색: 왼쪽 아이콘 #2b9fe0 (교사·admin만)
- button-primary: doc-upload "AI로 읽기"(#141414 채움, #ffffff 글자, rounded 9999, 높이 44 이상, 파일 없으면 비활성). 직접 입력 모드의 "입고"·"시약 등록". 하늘색 없음 (교사·admin만)
- stock-intake: "직접 입력" 모드의 "기존 시약 입고" 갈래 — 기존 구성 그대로(검색 → 선택 → 수량 스테퍼·프리셋 칩 → 입고일 → "입고"). 이 프레임에는 그리지 않는다 (교사·admin만)
- reagent-register: "직접 입력" 모드의 "새 시약 등록" 갈래 — 기존 폼(시약명·종류·재고량·입고일) + MSDS 칸 옆 msds-search. 이 프레임에는 그리지 않는다 (교사·admin만)
- msds-search: reagent-register MSDS 칸 옆 button-pill-soft "MSDS 찾기"(누르면 상태 화면 7-msds와 같은 msds-candidates 시트). 서류로 입고에서는 new-reagent-fields 안에 같은 버튼. 이 프레임에는 그리지 않는다 (교사·admin만)
- text-input: 직접 입력 모드의 검색·수량·입고일·폼 입력(#f0f0f0, rounded 16, 포커스 링 2px #141414). 이 프레임에는 그리지 않는다 (교사·admin만)
- ex-toast: 입고 저장 직후 "입고를 기록했어요" (교사·admin만)
- tab-bar: 모바일 전용 하단 탭바 1개(화면 2와 같은 규격). 데스크탑에는 두지 않는다. 하늘색: 활성 tab-item 아이콘 #2b9fe0만 (교사·admin만)
- tab-item: "홈" · "시약" · "QR 스캔" · "기록" 4개. 활성 = "시약", 비활성 3개 #707070 (교사·admin만)
### 반영한 레퍼런스
- https://uibowl.io/name/%ED%8E%98%EC%9D%B4%EC%9B%8C%ED%81%AC?patterns=%EC%B4%AC%EC%98%81%ED%95%98%EA%B8%B0

## 상태 화면 7-doc-upload
서류를 올리고 "AI로 읽기"를 누른 직후 읽는 중 상태(프레임 7-doc-upload-mobile · 7-doc-upload-desktop). 교사·admin 전용.
예시 상태: 거래명세서 사진 1장 "거래명세서_1007.jpg"(1.8MB). 헤더와 intake-mode는 그대로 남고, doc-upload 카드가 진행 상태로 바뀐다. 취소할 수 있다.
### 구성 요소
- nav-pill: "Lab_Stock" + "입고·시약 등록" + 현재 학교명 "샘플고등학교" + nav-account-menu ▾ (교사·admin만)
- nav-account-menu: 학교명 옆 ▾(닫힌 상태) (교사·admin만)
- intake-mode: "직접 입력 / 서류로 입고", 활성 = "서류로 입고". 읽는 동안 누름 동작 없음 (교사·admin만)
- segmented-control-active: intake-mode 활성 옵션 흰 pill. 하늘색: 1px #2b9fe0 테두리(글자 #141414) (교사·admin만)
- doc-upload: 같은 카드(#ffffff, 1px #e0e0e0, rounded 24, 여백 24)가 진행 상태로 바뀜. 위→아래: 올린 서류 미리보기 타일(비율 유지, rounded 16) + 그 위 badge-overlay 파일 이름 → 진행 막대(트랙 #e6f4fc, 채움 #2b9fe0, rounded 9999) → heading-4 "읽는 중이에요" → body-sm(#707070) "품목·규격·수량을 찾고 있어요" → caption(#707070) "잠시만 기다려 주세요" → button-outline "취소". 하단 button-primary "AI로 읽기"는 비활성으로 남는다. 하늘색: 진행 막대 #2b9fe0 + 트랙 #e6f4fc (교사·admin만)
- badge-overlay: 미리보기 위 파일 이름 태그 "거래명세서_1007.jpg"(rgba(115,115,115,0.56) 채움, #ffffff label, rounded 9999). 하늘색 없음 (교사·admin만)
- button-outline: doc-upload 안 "취소"(#ffffff, 1px #e0e0e0, 라벨 #141414, rounded 9999, 높이 44 이상) — 누르면 화면 7 첫 상태로 (교사·admin만)
- button-primary: "AI로 읽기" 비활성(누름 없음). 하늘색 없음 (교사·admin만)
- tab-bar: 모바일 전용 하단 탭바 1개(화면 7과 같음). 데스크탑에는 두지 않는다 (교사·admin만)
- tab-item: 4개 "홈" · "시약" · "QR 스캔" · "기록". 활성 = "시약" (교사·admin만)
### 반영한 레퍼런스
- https://uibowl.io/name/%ED%8E%98%EC%9D%B4%EC%9B%8C%ED%81%AC?patterns=%EC%B4%AC%EC%98%81%ED%95%98%EA%B8%B0&imgId=cmtzo56zo001gib048x2rj3i2
- https://uibowl.io/name/%EB%A6%AC%EB%8B%A4?patterns=%EC%B4%AC%EC%98%81%ED%95%98%EA%B8%B0&imgId=cmliyank30009jp04rcy8en7a

## 상태 화면 7-doc-review
AI가 서류를 읽은 뒤의 확인 표(프레임 7-doc-review-mobile · 7-doc-review-desktop). 교사·admin 전용. 결과는 사용자가 확인한 뒤에만 입고된다(PRD §5).
예시 상태: 서류 날짜 2026-10-07. 품목 3개 + 시약 아님 2개.
① "염산 35% 500mL" · 규격 500 mL · 수량 4 → 우리 학교 시약 "염산" 자동 연결, 환산 "500 mL × 4병 = 2,000 mL"
② "질산칼륨 500g" · 규격 500 g · 수량 1 → 우리 학교에 없음 → "새 시약으로 등록"을 고른 상태라 행이 아래로 펼쳐짐(new-reagent-fields)
③ "아세트산(빙초산) 500mL" · 규격 500 mL · 수량 2 → "새 시약으로 등록" 입력을 마치고 접힌 상태, 2줄에 요약 caption(#707070) "새 시약 · 산 · 1,000 mL", 환산 "500 mL × 2병 = 1,000 mL"
시약 아님 2개(니트릴 장갑 · 비커 250mL)는 표 아래 접힘.
모바일 = 행마다 #f3f3f3 카드 세로 쌓기, 데스크탑 = 표(머리행 품명 · 규격 · 수량, 행 아래 줄 reagent-link).
### 구성 요소
- nav-pill: "Lab_Stock" + "입고·시약 등록" + 현재 학교명 "샘플고등학교" + nav-account-menu ▾ (교사·admin만)
- nav-account-menu: 학교명 옆 ▾(닫힌 상태) (교사·admin만)
- intake-mode: "직접 입력 / 서류로 입고", 활성 = "서류로 입고" (교사·admin만)
- segmented-control-active: intake-mode 활성 옵션 흰 pill. 하늘색: 1px #2b9fe0 테두리(글자 #141414) (교사·admin만)
- doc-intake-table: 확인 표 블록 1개(extraction-table 모양, rounded 16 컨테이너). 위→아래: heading-3 "읽은 내용 확인" + caption(#707070) "고칠 곳이 있으면 고친 뒤 입고하세요" → 입고일 줄 라벨 "서류 날짜" + text-input "2026-10-07"(고칠 수 있음, 서류에 날짜가 없으면 오늘) → doc-item-row 3개(행 사이 12) → 접힌 묶음 줄 "시약 아님 2개 ▾"(body-sm #707070, 누르면 펼쳐 품명만 보기) → 하단 전폭 button-primary "확인 후 입고". 하늘색: 사용자가 고친 칸 배경 #e6f4fc (교사·admin만)
- doc-item-row: 서류 품목 1개. 1줄 = 품명(서류 표기 그대로, title #141414) · 규격(body) · 수량(body, 고칠 수 있는 숫자 text-input). 2줄 = reagent-link. 3줄 = 단위 환산 caption(#707070) "500 mL × 4병 = 2,000 mL". 모바일 = #f3f3f3 카드(rounded 16, 여백 16), 데스크탑 = ex-data-table-cell 행. 하늘색 없음 (교사·admin만)
- reagent-link: doc-item-row 2줄. 자동 연결(①) = caption "우리 학교 시약"(#707070) + 선택 상자(text-input 모양, #ffffff 채움(#f3f3f3 카드 위), rounded 16, 값 "염산" + ▾) + 조용한 텍스트 동작 "바꾸기" · "빼기"(link #141414, 채움·테두리 없음, 누름 영역 44 이상). 연결할 시약이 없으면(②·③) 선택 상자 자리에 pill "새 시약으로 등록"(선택됨 상태). "빼기"를 누르면 그 행은 이번 입고에서 빠지고 흐린 글자(#adadad)로 남아 되돌릴 수 있다. 하늘색: ▾ 아이콘 #2b9fe0, "새 시약으로 등록" 선택 상태 #e6f4fc + 1px #2b9fe0 테두리(글자 #141414) (교사·admin만)
- new-reagent-fields: ② 행이 아래로 펼쳐진 입력 묶음(행 카드 안, 위 구분 여백 12). 라벨 위·입력 아래 세로: "이름" text-input "질산칼륨" → "보관 분류" storage-class-chip 8종(AI 추천 "산화제" 칩에 suggest-badge, 처음 선택) → "단위" 선택 상자 "g"(병·mL·g) → "재고량" text-input "500" + suffix "g" → "MSDS" 줄 = caption "아직 없어요"(#707070) + msds-search. 하늘색 없음(칩·배지 규칙은 각 항목대로) (교사·admin만)
- storage-class-chip: new-reagent-fields "보관 분류" 칩 8종 "유기·산·염기·산화제·인화성·무기염·독성·기타", 하나 선택. 미선택 = #ffffff 채움 + 1px #e0e0e0 테두리(#f3f3f3 카드 위 구분), rounded 9999, label #141414. 하늘색: 선택 칩 "산화제" #e6f4fc + 1px #2b9fe0 테두리(글자 #141414) (교사·admin만)
- suggest-badge: "산화제" 칩 바로 옆 작은 pill "추천"(#e6f4fc 채움, 1px #2b9fe0 테두리, label #141414, rounded 9999) — AI가 고른 분류 표시. 핑크 금지 (교사·admin만)
- msds-search: new-reagent-fields MSDS 줄 오른쪽 pill "MSDS 찾기"(#ffffff 채움(#f3f3f3 카드 위 구분), 라벨 #141414, rounded 9999, 높이 44 이상). 누르면 상태 화면 7-msds. 하늘색: 검색 아이콘 #2b9fe0 (교사·admin만)
- text-input: "서류 날짜", 수량, reagent-link 선택 상자, new-reagent-fields 이름·단위·재고량(테두리 없음, rounded 16, 포커스 링 2px #141414, 단위 suffix #707070 — 흰 화면 위 #f0f0f0, #f3f3f3 카드 위 #ffffff). 하늘색: 날짜 달력 아이콘 #2b9fe0 (교사·admin만)
- button-primary: 표 하단 전폭 "확인 후 입고"(모바일 tab-bar 바로 위, #141414 채움, #ffffff 글자, rounded 9999, 높이 44 이상). 새 시약 행의 이름·보관 분류·단위·재고량이 비면 비활성. 하늘색 없음 (교사·admin만)
- ex-toast: 입고 직후 "3개 품목을 입고했어요" → 새 시약이 있으면 상태 화면 7-suggest, 없으면 화면 2. 하늘색: 완료 체크 아이콘 #2b9fe0 (교사·admin만)
- tab-bar: 모바일 전용 하단 탭바 1개(화면 7과 같음). 데스크탑에는 두지 않는다 (교사·admin만)
- tab-item: 4개 "홈" · "시약" · "QR 스캔" · "기록". 활성 = "시약" (교사·admin만)
### 반영한 레퍼런스
- https://uibowl.io/name/%ED%9E%88%EB%A1%9C%EC%9D%B8%EC%8A%A4?patterns=%EC%95%8C%EB%A6%BC&imgId=cmqgadbzq00m3if04dv0zhlhx

## 상태 화면 7-doc-fail
AI가 서류를 읽지 못했거나 품목이 0개인 상태(프레임 7-doc-fail-mobile · 7-doc-fail-desktop). 교사·admin 전용. 핑크 없음 — 재고 부족이 아니다.
예시 상태: 흐린 영수증 사진을 올려 품목을 찾지 못함. 두 갈래 동작 = 다시 올리기 / 직접 입력.
### 구성 요소
- nav-pill: "Lab_Stock" + "입고·시약 등록" + 현재 학교명 "샘플고등학교" + nav-account-menu ▾ (교사·admin만)
- nav-account-menu: 학교명 옆 ▾(닫힌 상태) (교사·admin만)
- intake-mode: "직접 입력 / 서류로 입고", 활성 = "서류로 입고" (교사·admin만)
- segmented-control-active: intake-mode 활성 옵션 흰 pill. 하늘색: 1px #2b9fe0 테두리(글자 #141414) (교사·admin만)
- ex-empty-state-card: 실패 안내 카드(#ffffff, 1px #f0f0f0 테두리, rounded 24, 여백 24). 올린 서류 미리보기 작은 타일(rounded 16, 비율 유지) → #141414 안내 아이콘 → heading-4 "서류에서 품목을 찾지 못했어요" → body-sm(#707070) "글자가 잘 보이게 다시 찍거나 PDF로 올려 주세요" → button-outline "직접 입력"(누르면 intake-mode가 "직접 입력"으로 바뀜). 하늘색 없음(아이콘 #141414) (교사·admin만)
- doc-upload: 카드 아래 다시 올리기 영역(화면 7 첫 상태와 같은 카드). heading-4 "다른 파일 올리기" + caption(#707070) "PDF·JPG·PNG, 4MB까지" + button-pill-soft "촬영하기" · "파일 선택" + 하단 전폭 button-primary "AI로 읽기"(새 파일 전 비활성). 하늘색: 업로드 아이콘 #2b9fe0 (교사·admin만)
- button-primary: doc-upload "AI로 읽기". 하늘색 없음 (교사·admin만)
- button-outline: ex-empty-state-card "직접 입력"(#ffffff, 1px #e0e0e0, 라벨 #141414, rounded 9999, 높이 44 이상) (교사·admin만)
- tab-bar: 모바일 전용 하단 탭바 1개(화면 7과 같음). 데스크탑에는 두지 않는다 (교사·admin만)
- tab-item: 4개 "홈" · "시약" · "QR 스캔" · "기록". 활성 = "시약" (교사·admin만)
### 반영한 레퍼런스
- https://uibowl.io/name/%EC%95%84%EC%9D%B4%EC%BF%A0%EC%B9%B4?patterns=%EC%B4%AC%EC%98%81%ED%95%98%EA%B8%B0&imgId=cmp0t6j63000fl904x800o216

## 상태 화면 7-suggest
7-doc-review에서 "확인 후 입고"를 누른 직후 위치 추천 단계(프레임 7-suggest-mobile · 7-suggest-desktop). 직접 입력으로 새 시약을 등록한 뒤에도 같은 단계. 교사·admin 전용. 위치는 나중에 화면 3·11에서 언제든 고칠 수 있다.
예시 상태: 새 시약 2개 — 질산칼륨(산화제) → 추천 "2번 시약장 · 우 2단", 아세트산(산) → 맞는 칸 없음. 화면 맨 위에 직전 ex-toast "3개 품목을 입고했어요".
### 구성 요소
- nav-pill: "Lab_Stock" + 제목 "입고·시약 등록" + 현재 학교명 "샘플고등학교" + nav-account-menu ▾ (교사·admin만)
- nav-account-menu: 학교명 옆 ▾(닫힌 상태) (교사·admin만)
- ex-toast: 단계 위 "3개 품목을 입고했어요"(#ffffff, 1px #f0f0f0 테두리, rounded 24). 하늘색: 완료 체크 아이콘 #2b9fe0 (교사·admin만)
- location-suggest: 위치 추천 블록 1개. 위→아래: heading-3 "보관 위치 정하기" → caption(#707070) "새 시약 2개의 칸을 추천했어요" → reagent-row 2개(행 사이 12) → 하단 전폭 button-primary "모두 추천대로"(모바일 tab-bar 바로 위) + 그 아래 조용한 텍스트 동작 "나중에"(link #141414, 누름 영역 44 이상, → 화면 2). ① 질산칼륨 행 = 시약명 title + 분류 caption "산화제"(#707070) → "추천 위치: cabinet-number(2) 2번 시약장 · 우 2단"(body #141414) + suggest-badge → 버튼 둘 button-outline "다른 칸"(→ location-picker) · button-primary "여기에 두기". ② 아세트산 행 = 시약명 + 분류 caption "산" → body-sm #707070 "맞는 칸이 없어요 — 시약장 설정에서 칸 분류를 정해 주세요" + button-pill-soft "시약장 설정"(→ 화면 11). 핑크 없음 (교사·admin만)
- reagent-row: location-suggest 안 새 시약 행(#f3f3f3, rounded 16, 여백 16). 하늘색: "여기에 두기" 뒤 완료 행은 오른쪽 #2b9fe0 체크 아이콘 + caption "2번 시약장 · 우 2단에 뒀어요"(#141414) (교사·admin만)
- cabinet-number: 추천 위치 앞 작은 원(#ffffff, 1px #e0e0e0, rounded 9999) 안 숫자 "2"(label #141414). 핑크·하늘색 글자 없음 (교사·admin만)
- suggest-badge: 추천 위치 줄 끝 pill "추천"(#e6f4fc 채움, 1px #2b9fe0 테두리, label #141414, rounded 9999). 핑크 금지 (교사·admin만)
- button-outline: 행마다 "다른 칸"(#ffffff, 1px #e0e0e0, 라벨 #141414, rounded 9999, 높이 44 이상) (교사·admin만)
- button-primary: 행마다 "여기에 두기", 하단 전폭 "모두 추천대로"(#141414 채움, #ffffff 글자, rounded 9999, 높이 44 이상). 맞는 칸이 없는 행은 "모두 추천대로"에서 빠진다. 하늘색 없음 (교사·admin만)
- button-pill-soft: 맞는 칸 없음 행의 "시약장 설정"(#ffffff 채움(#f3f3f3 행 위 구분), 라벨 #141414, rounded 9999, 높이 44 이상). 하늘색: › 아이콘 #2b9fe0 (교사·admin만)
- tab-bar: 모바일 전용 하단 탭바 1개(화면 7과 같음). 데스크탑에는 두지 않는다 (교사·admin만)
- tab-item: 4개 "홈" · "시약" · "QR 스캔" · "기록". 활성 = "시약" (교사·admin만)
### 반영한 레퍼런스
- https://uibowl.io/name/%ED%9E%88%EB%A1%9C%EC%9D%B8%EC%8A%A4?patterns=%EC%95%8C%EB%A6%BC&imgId=cmqgadbzq00m3if04dv0zhlhx

## 상태 화면 7-msds
7-doc-review의 질산칼륨 새 시약 행에서 "MSDS 찾기"를 누른 상태(프레임 7-msds-mobile · 7-msds-desktop). 교사·admin 전용. 직접 입력의 새 시약 등록 폼에서 누른 경우도 같은 시트.
뒤 화면은 7-doc-review 그대로(딤 없음), 위에 msds-candidates 시트. 예시: 후보 3개 중 첫 후보 선택. 모바일 = tab-bar 위 바텀시트, 데스크탑 = 가운데 시트.
### 구성 요소
- nav-pill: "Lab_Stock" + "입고·시약 등록" + 현재 학교명 "샘플고등학교" + nav-account-menu ▾ (교사·admin만)
- nav-account-menu: 학교명 옆 ▾(닫힌 상태) (교사·admin만)
- doc-intake-table: 시트 뒤 확인 표(누름 동작 없음) (교사·admin만)
- new-reagent-fields: 시트 뒤 펼쳐진 질산칼륨 입력 묶음(누름 동작 없음) (교사·admin만)
- msds-search: 시트 뒤 new-reagent-fields 안 "MSDS 찾기"(눌린 상태). 하늘색: 검색 아이콘 #2b9fe0 (교사·admin만)
- msds-candidates: 시트 1개(#ffffff, 1px #e0e0e0 테두리, 위쪽 rounded 24, 여백 24, × 닫기). 위→아래: 제목 heading-3 "MSDS 찾기" → caption(#707070) "질산칼륨" → 검색 text-input(값 "질산칼륨") → 후보 행 3개(물질명 title 위 + CAS caption #707070 아래, #f3f3f3, rounded 16, 행 사이 12): "질산칼륨 · CAS 7757-79-1" · "질산칼륨 용액 · CAS 7757-79-1" · "아질산칼륨 · CAS 7758-09-0", 선택 = 첫 행 → 맨 끝 "찾는 게 없어요 — 직접 입력" 행(그 자리에서 "MSDS 주소" text-input 펼침) → 하단 전폭 button-primary "이 MSDS로". 후보 0개 = "찾지 못했어요 — 직접 입력" + text-input. 고르기 전 비활성. 고르면 시트가 닫히고 new-reagent-fields MSDS 줄이 "질산칼륨 · CAS 7757-79-1"로 바뀐다. 하늘색: 선택 행 배경 #e6f4fc + 오른쪽 #2b9fe0 체크 아이콘(글자 #141414) (교사·admin만)
- text-input: 시트 검색 입력과 "MSDS 주소" 입력(#f0f0f0, rounded 16, 포커스 링 2px #141414). 하늘색: 검색 아이콘 #2b9fe0 (교사·admin만)
- button-primary: 시트 하단 "이 MSDS로"(#141414 채움, #ffffff 글자, rounded 9999, 높이 44 이상). 하늘색 없음 (교사·admin만)
- tab-bar: 모바일 전용 하단 탭바 1개(화면 7과 같음). 시트는 이 바 위에 붙는다. 데스크탑에는 두지 않는다 (교사·admin만)
- tab-item: 4개 "홈" · "시약" · "QR 스캔" · "기록". 활성 = "시약" (교사·admin만)
### 반영한 레퍼런스
- https://uibowl.io/name/%ED%86%A0%EC%8A%A4%EC%A6%9D%EA%B6%8C?patterns=%EC%BB%A4%EB%AE%A4%EB%8B%88%ED%8B%B0&imgId=cmsb4ub9l0009jo042gue22tj
- https://uibowl.io/name/%EC%95%B3%ED%94%8C%EB%A6%AC?patterns=%EA%B2%80%EC%83%89&imgId=cmtpokg65000pi804zwlm86ih
- https://uibowl.io/name/%EB%84%A4%EC%9D%B4%EB%B2%84%EB%B8%94%EB%A1%9C%EA%B7%B8?patterns=%ED%95%84%ED%84%B0&imgId=cmumdx3pp008yjm04zoku825b

## 역할별 노출
앱 전체(화면 1~13) 기준 개수. runs/20261006-1223 표를 기준으로 2026-10-07 변경을 반영했다. 같은 화면의 상태 화면에 다시 나오는 같은 컴포넌트는 그 화면 1개로 센다.
새 행: doc-upload = 화면 7 1(첫 상태·7-doc-upload·7-doc-fail 같은 영역). msds-search = 화면 3 1(MSDS 없는 시약, 3-msds) + 화면 7 1(직접 입력 새 시약 폼·서류 new-reagent-fields, 7-doc-review·7-msds). msds-bulk-banner = 화면 2 1. 셋 다 교사·admin만, 학생 0(R5).
그대로인 것: msds-entry = 화면 3 1 + 화면 10 상세 1(학생·교사·admin 모두 2 — 화면 3은 MSDS가 없는 시약이어도 msds-entry 블록과 "MSDS가 아직 없어요"가 학생에게 보인다). stock-intake = 화면 7 직접 입력 1 + 홈 quick-action 1. reagent-register = 화면 7 직접 입력 1. threshold-edit·location-edit = 화면 3 1(7-suggest의 "다른 칸"은 location-suggest 안 동작이라 location-edit로 세지 않음).
intake-mode·doc-intake-table·doc-item-row·reagent-link·new-reagent-fields·location-suggest·msds-candidates는 화면 7·상태 화면(교사·admin 전용) 안에만 있고, suggest-badge·auto-threshold-badge·reorder-threshold·reagent-location·nav-account-menu는 rules.json roles 대상이 아니라 표에 넣지 않는다.

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
| doc-upload | 0 | 1 | 1 |
| msds-search | 0 | 2 | 2 |
| msds-bulk-banner | 0 | 1 | 1 |
