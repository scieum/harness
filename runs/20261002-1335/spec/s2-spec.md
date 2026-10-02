# S2 설계 — run 20261002-1335

대상 화면: 13 (홈/대시보드) · 학교: 샘플고등학교 (input.json)
이전 작업: runs/20261002-1301 (화면 11·12·7·8), runs/20261002-1138 (화면 1·4·5·7·8·9·10, 하늘색 버전), runs/20261002-0838 (화면 2·3·6). 같은 컴포넌트 이름과 톤을 따른다.
근거: docs/PRD.md §3·§6·§7(13 홈 추가), docs/story-service.md 결정 사항("홈 (화면 13)"), docs/design.md, harness/rules.json(roles R1~R7, screens_required 13, colors), research/s1-adopt.md
색·폰트·모서리·간격은 docs/design.md와 harness/rules.json을 따른다. 허용 색 밖의 값은 쓰지 않는다. 반투명 회색은 badge-overlay 안에서만 허용되며 이 화면에는 쓰지 않는다.
- 강조색 #d6246a(핑크)와 연핑크 #fbe9f0는 재고 부족·재주문 알림 신호에만 쓴다. 이 화면에서는 badge-low-stock, reorder-alert-card 안에서만 쓴다. 그 밖의 안내·빈 상태에는 핑크를 쓰지 않는다.
- 하늘색 #2b9fe0(선·인디케이터·아이콘)과 옅은 하늘색 #e6f4fc(선택·아이콘 바탕)는 활성 nav 링크 밑줄·선택 상태·링크 화살표·아이콘 강조에만 쓴다. 글자색으로 쓰지 않고(하늘색 위 글자는 #141414), badge-low-stock·reorder-alert-card·button-primary 안에는 쓰지 않는다.
학교 선택은 화면 1에만 있다. 화면 13에는 학교 선택을 두지 않고 nav-pill 안에 현재 학교명 "샘플고등학교"를 표시한다. 학교 전환 기능은 두지 않는다. 화면의 모든 숫자·기록은 샘플고등학교 데이터만 보여준다(N1).
외부 서비스 연결 값은 서버에서만 다룬다. 홈에 연결 값 입력·외부 서비스 설정·AI 엔진 선택 UI를 두지 않는다.
괄호 안 역할 표시가 없는 구성 요소는 학생·교사·admin 모두에게 보인다.
데스크탑 nav-pill 섹션 링크(1301에 더함): 맨 앞 "홈" + "시약 목록", "사용 기록 내역", "시약장 설정", "QR 스캔", 교사·admin에게만 "재주문 알림"·"입고·시약 등록", admin에게만 "사용자 관리"·"판매처 설정". 모바일에서는 링크를 접고 워드마크·학교명만 남긴다.

## 화면 13
로그인 후 첫 화면. 학생·교사·admin 모두 들어오고, 같은 홈 틀에서 역할마다 바로가기·카드 구성이 달라진다. 다른 화면(2 시약 목록, 4 사용 기록 입력, 6 재주문 알림, 7 입고, 8 사용자 관리, 10 사용 기록 내역, 11 시약장 설정, 12 QR 스캔)으로 가는 진입점을 한곳에 모은다.
예시 상태: 전체 시약 42종, 재고 부족 3종(염산 · 1병, 에탄올 · 200mL, 질산은 · 5g), 시약장 2개(칸 16개 중 지정 14 · 미지정 2), 재주문 알림 3건, 최근 사용 기록 3줄.
모바일 위→아래 순서: nav-pill → quick-action 그리드 → home-summary(재고 요약 카드 → 시약장 요약 카드) → (교사·admin) reorder-alert-card → 최근 사용 기록 카드. 섹션은 독립 카드로 세로 스택하고 카드 사이는 24 간격.
데스크탑(1440): nav-pill 아래 2열. 왼쪽 열 = quick-action 그리드 + home-summary, 오른쪽 열 = (교사·admin) reorder-alert-card + 최근 사용 기록 카드. 학생은 오른쪽 열에 최근 사용 기록 카드만 둔다.
### 구성 요소
- nav-pill: "Lab_Stock" 워드마크 + 현재 학교명 "샘플고등학교" 텍스트(상단 한 줄 "학교명"). 학교 선택·전환 컨트롤은 두지 않는다. 하늘색: 데스크탑 현재 섹션 링크("홈") 아래 #2b9fe0 밑줄 인디케이터(글자는 #141414)
- quick-action: 4열 아이콘 바로가기 그리드, 첫 칸은 항상 "QR 스캔". 칸 = 원형 아이콘 바탕(#e6f4fc, rounded 9999) 안 #2b9fe0 아이콘 + 아래 label(#141414), 칸 전체가 44 이상 누름 영역. 역할별 항목: 학생 4칸 "QR 스캔"(화면 12) · "사용 기록 입력"(화면 4) · "시약 목록"(화면 2) · "사용 기록 내역"(화면 10). 교사 4칸 "QR 스캔" · "사용 기록 입력" · "입고"(화면 7, stock-intake 진입) · "시약 목록". admin 4칸 "QR 스캔" · "사용 기록 입력" · "입고"(화면 7, stock-intake 진입) · "사용자 관리"(화면 8, user-manage 진입). 학생 그리드에는 입고·사용자 관리 칸이 없고, 교사 그리드에는 사용자 관리 칸이 없다. 하늘색: 아이콘 #2b9fe0 + 아이콘 바탕 #e6f4fc, 누른 칸 바탕 #e6f4fc
- home-summary: 요약 카드 2장(#ffffff, 1px #f0f0f0 테두리, rounded 24, 안쪽 여백 24). ① 재고 요약 카드: 맨 위 한 줄 heading-4 "재고 부족 3개"(#141414) + 오른쪽 badge-low-stock "3" → 바로 아래 부족 시약 칩 가로 줄(칩 = #f3f3f3 채움, rounded 9999, label #141414 "염산 · 1병" / "에탄올 · 200mL" / "질산은 · 5g", 누르면 화면 3 시약 상세) → 여백 → 보조 수치 2행 "전체 시약"(caption #707070) + "42종"(title), "시약장"(caption #707070) + "2개"(title) → 카드 하단 button-pill-soft "시약 목록 보기 >"(화면 2). 재고 부족이 0개면 badge-low-stock과 칩 줄을 숨기고 body(#141414) "부족한 시약이 없어요" 1줄. ② 시약장 요약 카드: 섹션 제목 heading-4 "시약장 요약 >"(누르면 화면 11, 학생은 배치도 보기 전용) → 큰 숫자 display "2개" → 상태별 구간 막대 1줄(지정 칸 #2b9fe0 구간 + 미지정 칸 #e0e0e0 구간, rounded 9999) → 보조 1줄 body-sm(#707070) "칸 16개 중 지정 14 · 미지정 2". 시약장이 0개면 이 카드 자리에 ex-empty-state-card. 하늘색: 시약장 요약 막대의 지정 구간 #2b9fe0, 제목 옆 › 아이콘 #2b9fe0. 핑크는 badge-low-stock 안에서만
- badge-low-stock: 재고 요약 카드 제목 옆 개수 배지 "3", reorder-alert-card 제목 옆 "재고 부족"(#d6246a 채움, #ffffff label 글자, rounded 9999). 하늘색 없음
- reorder-alert-card: 교사·admin 전용 '재주문 알림' 카드. #f3f3f3 채움, 테두리 없음, rounded 24, 안쪽 여백 24. 제목 heading-4 "재주문 알림" 옆 badge-low-stock "재고 부족" + 오른쪽 button-pill-soft "3건 >"(누르면 화면 6 재주문 알림 목록). 본문 body 1줄 "필요량보다 적은 시약이 3종 있어요"(#141414). 판매처 연결 버튼은 이 카드에 두지 않고 화면 6에서만 연다. 하늘색 쓰지 않음(› 아이콘도 #141414). 학생 홈에는 이 카드가 없다 (교사·admin만)
- reagent-row: 최근 사용 기록 카드 안 3줄. 카드 = #ffffff, 1px #f0f0f0 테두리, rounded 24, 제목 heading-4 "최근 사용 기록". 행 = 시약명(title) + 사용자 이름·사용량(body, 예: "김학생 · 20mL") + 시각 caption(#707070, 예: "오늘 10:20"), #f3f3f3 채움, rounded 16, 행 사이 12. 행을 누르면 화면 10 사용 기록 내역의 해당 기록으로 간다. 재고 부족 배지는 이 행에 두지 않는다(재고 요약 카드에서만). 기록이 0건이면 행 자리에 ex-empty-state-card. 하늘색: 누른 행 배경 #e6f4fc
- button-pill-soft: 재고 요약 카드 "시약 목록 보기 >", 최근 사용 기록 카드 하단 "더 보기 >"(화면 10), reorder-alert-card "3건 >"(교사·admin만). 하늘색: reorder-alert-card 밖의 버튼에만 오른쪽 › 아이콘 #2b9fe0(라벨 글자는 #141414)
- ex-empty-state-card: ① 시약장 0개: body(#141414) "등록된 시약장이 없어요" + 교사·admin에게만 button-outline "시약장 추가"(화면 11 cabinet-edit 진입), 학생에게는 body-sm(#707070) "선생님이 시약장을 등록하면 보여요". ② 최근 사용 기록 0건: "아직 사용 기록이 없어요" + button-outline "사용 기록 입력"(화면 4). 하늘색: 안내 아이콘 #2b9fe0
- button-outline: ex-empty-state-card의 "시약장 추가"(교사·admin만), "사용 기록 입력". 1px #e0e0e0 테두리, rounded 9999
### 반영한 레퍼런스
- https://uibowl.io/name/%ED%8E%98%EC%9D%B4%EC%9B%8C%ED%81%AC?patterns=%EB%A9%94%EC%9D%B8
- https://uibowl.io/name/%ED%8E%98%EC%9D%B4%ED%9E%88%EC%96%B4?patterns=%EB%A9%94%EC%9D%B8&patternName=%EB%82%98%EC%9D%98%20%EB%A7%A4%EC%9E%A5
- https://uibowl.io/name/%EC%9E%90%EB%A6%AC%ED%86%A1?patterns=%EB%A9%94%EC%9D%B8&patternName=%ED%99%88%28%EC%9E%84%EB%8C%80%EC%9D%B8%29
- https://uibowl.io/name/%EB%83%89%EC%9E%A5%EA%B3%A0%ED%84%B8%EA%B8%B0?patterns=%EA%B2%80%EC%83%89&patternName=%ED%99%88%ED%99%94%EB%A9%B4%20%EC%9E%AC%EB%A3%8C
- https://uibowl.io/name/%ED%86%A0%EC%8A%A4?patterns=%EB%A9%94%EC%9D%B8&imgId=cmrtvehtz00gzjc047yebr296

## 역할별 노출
앱 전체(화면 1~13) 기준 개수. runs/20261002-1301 표(화면 1~12)에 화면 13 홈 진입점을 더했다.
홈에서 더한 것: reorder-alert-card = 홈 카드 1 (교사·admin). stock-intake = 홈 quick-action "입고" 1 (교사·admin). user-manage = 홈 quick-action "사용자 관리" 1 (admin만). cabinet-edit = 홈 시약장 0개 빈 상태의 "시약장 추가" 1 (교사·admin). 홈에는 manual-upload·vendor-link·vendor-register·reagent-register·msds-entry 진입을 두지 않는다(1301 값 유지). 학생 홈의 reorder-alert-card·vendor-link·stock-intake = 0.

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
