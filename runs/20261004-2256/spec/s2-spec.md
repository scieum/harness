# S2 설계 — run 20261004-2256

대상 화면: 11 (시약장 설정) + 상태 화면 11-empty, 11-delete · 학교: 샘플고등학교 (input.json)
변경 사유: 2026-10-04 사용자 결정 — 학교당 시약장 여러 개. 상단 시약장 전환(모든 역할), 시약장 추가·이름 바꾸기·삭제(교사·admin만), 삭제 전 확인, 삭제하면 그 시약장에 배치된 시약은 "칸 없음"(배치 해제, 시약 자체는 남음), 시약장 0개 빈 화면(PRD §7 11, story-service 결정 사항 "여러 시약장", rules.json cabinet.multiple·default_name·unassigned_label·on_delete·manage_roles, screens_required 11, variants 11, roles R7).
기준 설계(수정하지 않음): runs/20261002-1301/spec/s2-spec.md 화면 11(배치도·범례·분류 칩·연핑크 mix-warning), runs/20261002-1441/spec/s2-spec.md 화면 11(tab-bar 버전, 활성 탭 "시약"). 두 설계의 구성 요소를 그대로 유지하고, 그 위에 시약장 전환·관리 층과 상태 프레임 2장(empty·delete)만 더한다.
근거: docs/PRD.md §3·§6·§7, docs/story-service.md(N1·N2, 결정 사항 "시약장 설정"·"여러 시약장"·"모바일 하단 탭바"), docs/design.md(Multiple cabinets, tab-bar, ex-modal-card, ex-empty-state-card), harness/rules.json(roles R1~R7, screens_required, variants, cabinet, tab_bar, colors), research/s1-adopt.md
색·폰트·모서리·간격은 docs/design.md와 harness/rules.json을 따른다. 허용 색 밖의 값(딤 반투명 검정 등)은 쓰지 않는다. 그림자는 쓰지 않는다(segmented-control-active 예외, 이 화면에는 없음).
- 강조색 #d6246a와 연핑크 #fbe9f0는 이 화면에서 mix-warning 안에서만 쓴다(runs/20261002-1301 기준: 바탕 #fbe9f0, 경고 아이콘 #d6246a, 글자 #141414). 시약장 삭제·빈 상태·이름 바꾸기·"칸 없음"에는 핑크를 쓰지 않는다 — 재고나 안전 신호가 아니다.
- 하늘색 #2b9fe0(선·인디케이터·아이콘)과 옅은 하늘색 #e6f4fc(선택 배경)는 선택 상태·활성 탭·아이콘 강조에만 쓴다. 글자색으로 쓰지 않고(하늘색 위 글자는 #141414), mix-warning·button-primary 안에는 쓰지 않는다.
학교 선택은 회원가입(화면 14)에만 있다. 화면 11과 두 상태 화면에는 학교 선택을 두지 않고 nav-pill 안에 현재 학교명 "샘플고등학교"를 표시한다. 학교 전환 기능은 두지 않는다. 시약장 목록·배치·"칸 없음" 시약은 모두 샘플고등학교 것만 보인다(N1).
외부 서비스 연결 값은 서버에서만 다룬다. 어떤 화면에도 연결 값 입력·외부 서비스 설정·AI 엔진 선택 UI를 두지 않는다.
괄호 안 역할 표시가 없는 구성 요소는 학생·교사·admin 모두에게 보인다.
모바일 공통(runs/20261002-1441): tab-bar는 화면 아래 가장자리 y 780~844(높이 64)에 붙고, 본문 스크롤 영역은 tab-bar 위쪽 선(y 780)에서 끝난다. 하단 고정 버튼은 tab-bar 바로 위(버튼 아래 끝과 tab-bar 위쪽 선 사이 16)에 둔다. 바텀시트·확인 카드는 tab-bar 위쪽 선 위에 붙는다. 세 프레임 모두 활성 탭 = "시약". 데스크탑 프레임에는 tab-bar를 두지 않고 nav-pill 섹션 링크("시약장 설정" 현재 링크)를 유지한다.

## 화면 11
학생·교사·admin 모두 들어온다. 교사·admin은 시약장을 전환·추가하고, 고른 시약장의 이름 바꾸기·삭제와 문 형태·단 수·칸별 보관 분류를 편집한다. 학생은 cabinet-switcher로 시약장을 전환해 배치도를 보기만 한다(학생 화면에는 cabinet-add·cabinet-edit 영역·편집 컨트롤·저장 버튼이 없다).
예시 상태: 시약장 2개("1번 시약장", "2번 시약장"), 활성 = "1번 시약장". 1번 시약장은 양문형 · 4단 → 좌/우 × 1~4단 = 8칸. 좌1단 = 산 + 염기(mix-warning 표시), 좌2단 = 유기, 좌3단 = 인화성, 좌4단 = 기타, 우1단 = 산화제, 우2단 = 무기염, 우3단 = 독성, 우4단 = 기타. 선택된 칸은 좌1단. 칸이 정해지지 않은 시약 2개("칸 없음").
모바일(390×844) 위→아래: nav-pill → cabinet-switcher(끝에 cabinet-add) → 시약장 이름 heading-3 "1번 시약장" + caption "양문형 · 4단" → (교사·admin) cabinet-edit 상단 관리 줄("이름 바꾸기" · "삭제") → (교사·admin) 문 형태·단 수 선택 → 배치도 → 범례 → (교사·admin) 선택 칸의 분류 칩 → 주의사항(mix-warning) → "칸 없음" 시약 목록 → (교사·admin) 하단 고정 "저장" → tab-bar. 좌우 여백 16, 블록 사이 24.
데스크탑(1440×900): nav-pill 아래 가운데 단일 열에 같은 순서. cabinet-switcher는 한 줄에 모두 펼쳐 보이고, "저장"은 cabinet-edit 맨 아래. tab-bar 없음.
### 구성 요소
- nav-pill: "Lab_Stock" 워드마크 + 제목 "시약장 설정" + 현재 학교명 "샘플고등학교" 텍스트. 학교 전환 기능은 두지 않는다. 하늘색: 데스크탑 현재 섹션 링크("시약장 설정") 아래 #2b9fe0 밑줄 인디케이터(글자는 #141414)
- cabinet-switcher: nav-pill 바로 아래 시약장 전환 pill 가로 한 줄. 시약장마다 pill 1개, 이름 기본값 "{n}번 시약장"(rules.json cabinet.default_name). 예시 상태 "1번 시약장"(활성) · "2번 시약장". 넘치면 가로 스크롤(모바일), 한 번에 하나만 활성. pill = rounded 9999, link 크기 라벨, 높이 44 이상. 활성 = #e6f4fc 채움 + 1px #2b9fe0 테두리 + 라벨 #141414, 비활성 = #f3f3f3 채움 + 라벨 #141414. 누르면 아래 시약장 이름·배치도·범례·주의사항·"칸 없음" 목록이 그 시약장으로 바뀐다. 학생·교사·admin 모두 보인다(학생 줄에는 cabinet-add 없이 시약장 pill만). 하늘색: 활성 pill 채움 #e6f4fc + 테두리 #2b9fe0
- cabinet-add: cabinet-switcher 줄 맨 끝에 고정된 button-pill-soft "+ 시약장 추가"(같은 높이, #f3f3f3 채움, 라벨 #141414, rounded 9999, 높이 44 이상). 누르면 다음 번호 이름("3번 시약장")으로 새 시약장을 만들고 switcher의 활성 pill이 된다. 학생 화면에는 그리지 않는다. 하늘색: "+" 아이콘 #2b9fe0(라벨 글자는 #141414) (교사·admin만)
- cabinet-edit: 편집 영역 전체를 감싸는 블록 1개. 맨 위 관리 줄 = button-outline "이름 바꾸기" + 오른쪽 조용한 텍스트 동작 "삭제"(link 크기, #141414 글자, 채움·테두리 없음, 누름 영역 44 이상, 핑크 금지). 그 아래 cabinet-door-select · cabinet-shelf-select · 선택 칸의 storage-class-chip 묶음 · mix-warning · 하단 전폭 button-primary "저장"이 들어간다. "이름 바꾸기"는 아래 ex-modal-card 이름 시트를, "삭제"는 상태 화면 11-delete 확인 카드를 연다. 학생 화면에는 이 블록이 없다. 하늘색 없음 (교사·admin만)
- cabinet-door-select: cabinet-edit 관리 줄 아래, 문 형태 2옵션 pill "양문형 / 단문형"(rules.json cabinet.door_types), 한 번에 하나만 선택. 고르면 아래 배치도의 열 수가 즉시 바뀐다(양문형 = 좌·우 2열, 단문형 = 1열). 예시 상태 "양문형" 선택. 하늘색: 선택 옵션 배경 #e6f4fc + 1px #2b9fe0 테두리(글자는 #141414), 미선택은 #f3f3f3 채움·#707070 글자 (교사·admin만)
- cabinet-shelf-select: cabinet-door-select 바로 아래, 단 수 2옵션 pill "3단 / 4단"(rules.json cabinet.shelves), 한 번에 하나만 선택. 고르면 배치도의 행 수가 즉시 바뀐다. 예시 상태 "4단" 선택. 하늘색: 선택 옵션 배경 #e6f4fc + 1px #2b9fe0 테두리(글자는 #141414) (교사·admin만)
- cabinet-slot: 활성 시약장 정면 배치도의 칸 1개. 배치도 = 왼쪽에 단 라벨(caption "1단"~"4단"), 위쪽에 문 라벨(caption "좌" / "우"), 양문형이면 좌·우 묶음 사이를 가운데 통로처럼 비운다. 칸은 같은 크기 격자(#f3f3f3 채움, rounded 16), 칸 안에 지정된 분류 이름(label, #141414)을 적고, 분류가 없으면 caption "미지정"(#707070). 예시 상태 8칸. 교사·admin은 칸을 눌러 선택하고, 학생에게는 같은 배치도가 보기 전용으로 보인다(누름 동작 없음). 산 + 염기가 지정된 좌1단 칸에는 #141414 경고 아이콘을 칸 오른쪽 위에 둔다. 하늘색: 선택된 칸 배경 #e6f4fc + 2px #2b9fe0 테두리(글자는 #141414)
- storage-class-chip: 보관 분류 칩 8종 "유기·산·염기·산화제·인화성·무기염·독성·기타"(rules.json cabinet.storage_classes). cabinet-edit 안에서 선택된 칸(좌1단)의 분류를 고르는 칩 묶음, 두 줄 배치, 한 칸에 여러 개 선택 가능. 예시 상태 "산"·"염기" 선택. 칩 = rounded 9999, label 크기, 미선택 #f3f3f3 채움. 배치도 아래 범례 한 줄(미지정 · 선택 칸)에도 같은 칩 모양을 보기 전용으로 쓴다(학생에게는 범례만 보인다). 하늘색: 선택된 칩 배경 #e6f4fc + 1px #2b9fe0 테두리(글자는 #141414)
- mix-warning: 칩 묶음과 저장 버튼 사이 구분 영역의 "주의사항" 목록(runs/20261002-1301 기준 그대로). 같은 칸에 rules.json cabinet.incompatible 조합(산+염기, 산화제+인화성, 산화제+유기, 산+인화성, 독성+산)이 지정되면 핑크 신호로 경고한다. 바탕 연핑크 #fbe9f0, 테두리 없음, rounded 16. 제목 heading-4 "주의사항"(#141414) + 줄마다 #d6246a 경고 아이콘 + #141414 body-sm 문구. 예시 상태 1줄 "좌1단: 산과 염기는 섞이면 위험해요. 다른 칸에 나눠 보관하세요". #d6246a는 경고 아이콘에만 쓰고 글자·채움에는 쓰지 않는다. 하늘색은 쓰지 않는다. 학생 화면에도 배치도 아래에 같은 경고를 보기 전용으로 표시한다
- reagent-row: 주의사항 아래 소제목 heading-4 "칸 없음 시약 (2)" + 칸이 정해지지 않은 시약 행 목록. 행 = 시약명(title) + 재고량·단위(body) + 칸 위치 자리에 caption "칸 없음"(rules.json cabinet.unassigned_label, #707070). #f3f3f3 채움, rounded 16, 행 사이 12. 행을 누르면 시약 상세(화면 3). 시약장을 삭제해 배치가 풀린 시약도 여기에 모인다. 학생은 보기만. 하늘색: 누른 행 배경 #e6f4fc
- ex-modal-card: "이름 바꾸기" 바텀시트 1단계. 그림자·딤 없이 1px #e0e0e0 테두리, #ffffff 채움, rounded 24, 안쪽 여백 24. 제목 heading-3 "시약장 이름" + text-input 1개(현재 이름 "1번 시약장"이 들어 있음) + 입력 오른쪽 아래 글자 수 caption(#707070) + 하단 전폭 button-primary "저장"(비어 있으면 비활성) + button-outline "취소". 모바일에서는 tab-bar 위쪽 선(y 780) 위에 붙는다. 하늘색 없음 (교사·admin만)
- text-input: 이름 시트 안 "시약장 이름" 입력 1개. #f0f0f0 채움, 테두리 없음, rounded 16, 포커스 링 2px #141414 (교사·admin만)
- button-outline: cabinet-edit 관리 줄 "이름 바꾸기", 이름 시트 "취소". #ffffff 채움, 1px #e0e0e0 테두리, 라벨 #141414, rounded 9999, 높이 44 이상 (교사·admin만)
- button-primary: cabinet-edit 하단 전폭 "저장"(모바일에서는 tab-bar 바로 위 고정), 이름 시트 "저장". #141414 채움, #ffffff 글자, rounded 9999, 높이 44 이상. 하늘색 없음 (교사·admin만)
- ex-toast: 저장 직후 "시약장 설정을 저장했어요", 이름 바꾼 뒤 "이름을 바꿨어요", 추가 직후 "3번 시약장을 추가했어요" 알림. 모바일에서는 tab-bar 위에 뜬다. 하늘색: 완료 체크 아이콘 #2b9fe0 (교사·admin만)
- tab-bar: 모바일 전용 하단 탭바 1개. 화면 아래 가장자리에 붙은 전폭 사각형 바(x 0, 폭 390, 높이 64, 위치 y 780~844, rounded 0). #ffffff 채움 + 위쪽에만 1px #f0f0f0 선, 그림자 없음, floating pill 아님. 안쪽 위아래 여백 8, 좌우 여백 0. 안에 tab-item 4개를 같은 폭으로 꽉 채워 둔다. 역할 무관 동일(학생 화면은 저장 버튼 없이 스크롤 영역이 이 바 위에서 끝난다). 데스크탑 프레임에는 두지 않는다. 하늘색: 활성 tab-item의 #2b9fe0 아이콘만(바탕 채움 없음)
- tab-item: tab-bar 안 4개, 왼쪽부터 "홈"(화면 13) · "시약"(화면 2) · "QR 스캔"(화면 12) · "기록"(화면 10). 각 항목 = 같은 폭(390 ÷ 4) 사각형 누름 영역(rounded 0, 채움 없음, pill 없음), 높이 48, 아이콘 위 + label(12/600) 아래, 아이콘과 라벨 사이 4. 활성 = "시약": #2b9fe0 아이콘 + 라벨 #141414, 뒤 바탕 없음. 비활성 3개("홈"·"QR 스캔"·"기록"): 아이콘·라벨 #707070
### 반영한 레퍼런스
- https://uibowl.io/name/%EB%8B%AC%EB%8B%A4%EB%B0%A9?patterns=iPhone%20%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7&imgId=cmuc8ychu001ljz04gcquihao
- https://uibowl.io/name/%ED%97%AC%EB%A1%9C%EC%9A%B0%EB%B4%87?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&imgId=cmr8u4gy30006jo04su091j5r
- https://uibowl.io/name/%EC%BB%A4%EB%A6%AC%EC%96%B4%ED%86%A1?patterns=%EB%B6%81%EB%A7%88%ED%81%AC%C2%B7%EC%9C%84%EC%8B%9C%EB%A6%AC%EC%8A%A4%ED%8A%B8&imgId=cmf0p85wt000hl704ad3u3tqc
- https://uibowl.io/name/BookMyShow?patterns=%EC%98%88%EC%95%BD%C2%B7%EA%B2%B0%EC%A0%9C&patternName=3.%EC%A2%8C%EC%84%9D%20%EC%84%A0%ED%83%9D
- https://uibowl.io/name/Frontier%20Airlines?patterns=%EC%98%88%EC%95%BD%C2%B7%EA%B2%B0%EC%A0%9C&patternName=%EC%A2%8C%EC%84%9D%20%EC%84%A0%ED%83%9D

## 상태 화면 11-empty
시약장이 0개인 학교의 화면 11. 교사 기준으로 그린다(프레임 11-empty-mobile · 11-empty-desktop). 학생에게는 같은 카드가 cabinet-add 버튼 없이 문구만 보인다.
시약장이 없으므로 cabinet-switcher·배치도·cabinet-edit·mix-warning은 그리지 않는다. "칸 없음" 시약 목록도 두지 않는다(빈 상태 카드 하나에 집중).
모바일(390×844) 위→아래: nav-pill → 제목 줄 heading-3 "시약장 0" → 화면 가운데 ex-empty-state-card → tab-bar. 좌우 여백 16. 데스크탑: nav-pill 아래 가운데 단일 열에 같은 카드, tab-bar 없음.
### 구성 요소
- nav-pill: "Lab_Stock" 워드마크 + 제목 "시약장 설정" + 현재 학교명 "샘플고등학교" 텍스트. 학교 전환 기능은 두지 않는다. 하늘색: 데스크탑 현재 섹션 링크("시약장 설정") 아래 #2b9fe0 밑줄 인디케이터(글자는 #141414)
- ex-empty-state-card: 배치도 자리 가운데 빈 상태 카드(#ffffff 채움, 1px #f0f0f0 테두리, rounded 24, 안쪽 여백 24, 가운데 정렬). 위에서부터 시약장 아이콘 → heading-4 "아직 시약장이 없어요"(#141414) → 안내 1줄 body-sm(#707070) "'+ 시약장 추가'를 눌러 첫 시약장을 만들어 주세요" → 카드 안 cabinet-add. 학생 화면에서는 cabinet-add를 그리지 않고 안내 1줄을 "교사가 시약장을 추가하면 여기에 보여요"로 바꾼다. 핑크 없음. 하늘색: 시약장 아이콘 #2b9fe0
- cabinet-add: ex-empty-state-card 안 안내 문구 아래 button-pill-soft "+ 시약장 추가"(#f3f3f3 채움, 라벨 #141414, rounded 9999, 높이 44 이상). 누르면 "1번 시약장"을 만들고 화면 11 기본 상태로 바뀐다. 학생 화면에는 그리지 않는다. 하늘색: "+" 아이콘 #2b9fe0(라벨 글자는 #141414) (교사·admin만)
- tab-bar: 모바일 전용 하단 탭바 1개. 화면 11과 같다(x 0, 폭 390, 높이 64, y 780~844, rounded 0, #ffffff 채움 + 위쪽 1px #f0f0f0 선, 그림자 없음, tab-item 4개 같은 폭). 데스크탑 프레임에는 두지 않는다. 하늘색: 활성 tab-item의 #2b9fe0 아이콘만
- tab-item: tab-bar 안 4개 "홈" · "시약" · "QR 스캔" · "기록", 같은 폭 사각형 누름 영역(rounded 0), 높이 48, 아이콘 위 + label(12/600) 아래. 활성 = "시약": #2b9fe0 아이콘 + 라벨 #141414. 비활성 3개: 아이콘·라벨 #707070
### 반영한 레퍼런스
- https://uibowl.io/name/%EB%B3%BC%ED%8A%B8%EC%97%85?patterns=%EA%B0%84%ED%8E%B8%EA%B2%B0%EC%A0%9C&imgId=cmojeenh70003lh04lxsv019h
- https://uibowl.io/name/%EB%8B%AC%EB%8B%A4%EB%B0%A9?patterns=iPhone%20%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7&imgId=cmuc8ychu001ljz04gcquihao

## 상태 화면 11-delete
교사·admin이 "2번 시약장"을 고른 뒤 cabinet-edit의 "삭제"를 누른 상태(프레임 11-delete-mobile · 11-delete-desktop). 학생에게는 이 상태가 없다.
뒤 화면은 화면 11 그대로이고 cabinet-switcher의 활성 pill = "2번 시약장"(예시: 양문형 · 3단, 배치된 시약 6개). 그 위에 확인 카드가 뜬다. 딤·반투명 덮개는 쓰지 않는다 — 기존 화면 6 확인 시트처럼 1px #e0e0e0 테두리로만 구분한다. 핑크 금지(시약장 삭제는 재고·안전 신호가 아니다).
모바일(390×844): 위쪽에 nav-pill · cabinet-switcher · 시약장 이름이 그대로 보이고, 확인 카드는 바텀시트로 tab-bar 위쪽 선(y 780) 위에 붙는다. 데스크탑: 화면 가운데 확인 카드, tab-bar 없음.
### 구성 요소
- nav-pill: "Lab_Stock" 워드마크 + 제목 "시약장 설정" + 현재 학교명 "샘플고등학교" 텍스트. 하늘색: 데스크탑 현재 섹션 링크("시약장 설정") 아래 #2b9fe0 밑줄 인디케이터(글자는 #141414) (교사·admin만)
- cabinet-switcher: 화면 11과 같은 전환 pill 줄. "1번 시약장"(비활성, #f3f3f3 채움) · "2번 시약장"(활성, #e6f4fc 채움 + 1px #2b9fe0 테두리, 라벨 #141414). 확인 카드 뒤에서 그대로 보여 어떤 시약장을 지우는지 알 수 있다. 하늘색: 활성 pill 채움 #e6f4fc + 테두리 #2b9fe0 (교사·admin만)
- cabinet-add: cabinet-switcher 줄 끝 button-pill-soft "+ 시약장 추가". 카드가 열린 동안 누름 동작 없음. 하늘색: "+" 아이콘 #2b9fe0 (교사·admin만)
- cabinet-edit: 확인 카드 뒤에 보이는 2번 시약장 편집 블록(관리 줄 "이름 바꾸기" · "삭제", 문 형태·단 수 선택). 카드가 열린 동안 누름 동작 없음. 하늘색: 선택 옵션 배경 #e6f4fc + 1px #2b9fe0 테두리 (교사·admin만)
- ex-modal-card: 삭제 확인 카드. #ffffff 채움, 1px #e0e0e0 테두리, 그림자·딤 없음, rounded 24, 안쪽 여백 24. 제목 heading-3 "이 시약장을 삭제할까요?"(#141414) → 안내 body-sm(#141414) "배치된 시약 6개는 '칸 없음'으로 바뀌어요" → 보조 1줄 caption(#707070) "시약 정보와 재고는 지워지지 않아요" → 가로 2버튼 button-outline "취소"(왼쪽) + button-primary "삭제"(오른쪽). 핑크 없음. 하늘색 없음 (교사·admin만)
- button-outline: 확인 카드 "취소". #ffffff 채움, 1px #e0e0e0 테두리, 라벨 #141414, rounded 9999, 높이 44 이상 (교사·admin만)
- button-primary: 확인 카드 "삭제". #141414 채움, #ffffff 글자, rounded 9999, 높이 44 이상. 누르면 2번 시약장이 switcher에서 빠지고 "1번 시약장"이 활성이 되며, 배치됐던 시약은 화면 11 "칸 없음 시약" 목록으로 옮겨진다(rules.json cabinet.on_delete). 하늘색 없음, 핑크 없음 (교사·admin만)
- ex-toast: 삭제 직후 "2번 시약장을 삭제했어요" 알림. 하늘색: 완료 체크 아이콘 #2b9fe0 (교사·admin만)
- tab-bar: 모바일 전용 하단 탭바 1개. 화면 11과 같다(x 0, 폭 390, 높이 64, y 780~844, rounded 0, #ffffff 채움 + 위쪽 1px #f0f0f0 선, 그림자 없음, tab-item 4개 같은 폭). 확인 카드는 이 바 위쪽 선 위에 붙고 바를 가리지 않는다. 데스크탑 프레임에는 두지 않는다. 하늘색: 활성 tab-item의 #2b9fe0 아이콘만
- tab-item: tab-bar 안 4개 "홈" · "시약" · "QR 스캔" · "기록", 같은 폭 사각형 누름 영역(rounded 0), 높이 48, 아이콘 위 + label(12/600) 아래. 활성 = "시약": #2b9fe0 아이콘 + 라벨 #141414. 비활성 3개: 아이콘·라벨 #707070
### 반영한 레퍼런스
- https://uibowl.io/name/%ED%8D%BC%EA%B7%B8%EC%83%B5?patterns=%EA%B3%84%EC%A2%8C&imgId=cmq7evao00095l204e0ekhshk
- https://uibowl.io/name/%EC%BB%A4%EB%A6%AC%EC%96%B4%ED%86%A1?patterns=%EB%B6%81%EB%A7%88%ED%81%AC%C2%B7%EC%9C%84%EC%8B%9C%EB%A6%AC%EC%8A%A4%ED%8A%B8&imgId=cmf0p85wt000hl704ad3u3tqc

## 역할별 노출
앱 전체 기준 개수. runs/20261002-2019 표를 그대로 옮기고 cabinet-add 행을 더했다.
cabinet-edit = 화면 11 1 + 홈 빈 상태 "시약장 추가" 1 (교사·admin, 학생 0 — 기존과 같음). cabinet-add = 화면 11 cabinet-switcher 끝 1 (교사·admin, 학생 0). 11-empty의 cabinet-add는 같은 화면 11의 다른 상태(시약장 0개일 때는 switcher가 없어 함께 보이지 않음)라 따로 세지 않는다. 11-delete는 교사·admin에게만 있는 상태이며 학생 숫자를 바꾸지 않는다. cabinet-switcher는 모든 역할에 보이며 rules.json roles 대상이 아니라 표에 넣지 않는다.

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
| cabinet-add | 0 | 1 | 1 |
