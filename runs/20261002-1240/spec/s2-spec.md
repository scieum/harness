# S2 설계 — run 20261002-1240

대상 화면: 11, 12, 7, 8 · 학교: 샘플고등학교 (input.json)
이어지는 작업: runs/20261002-1223 (같은 대상, G-S2 통과)의 재실행. 바뀐 것은 2026-10-02 사용자 결정 하나 — 화면 11 mix-warning은 재고 부족과 같은 핑크 #d6246a로 경고한다. 그 밖의 구성은 1223과 같다.
이전 작업: runs/20261002-1138 (화면 1·4·5·7·8·9·10, 하늘색 버전), runs/20261002-0838 (화면 2·3·6). 같은 컴포넌트 이름과 톤을 따른다. 화면 7·8은 1138 구성을 유지하고 research/s1-adopt.md 채택 항목(스테퍼·프리셋 칩·초대 대기 섹션·역할 변경 시트)을 더한다.
근거: docs/PRD.md §3·§6·§7(화면 11·12 추가), docs/story-service.md 결정 사항(시약장 설정·QR 스캔), docs/design.md, harness/rules.json(roles R1~R7, screens_required, cabinet, colors.accent.only_within), research/s1-adopt.md
색·폰트·모서리·간격은 docs/design.md와 harness/rules.json을 따른다. 허용 색 밖의 값(딤 반투명 검정, #f2f2f2 등)은 쓰지 않는다. 반투명 회색은 badge-overlay 안에서만 허용된다.
- 강조색 #d6246a는 재고 부족·혼재 경고 전용이다. badge-low-stock, reorder-alert-card, mix-warning 안에서만 쓴다. 이번 대상 화면 11·12·7·8에서 mix-warning 밖의 오류·경고·실패 안내에는 핑크를 쓰지 않는다. 그런 경고·오류는 #141414 아이콘 + #141414 문구로만 표시한다.
- 하늘색 #2b9fe0(선·인디케이터·아이콘·진행 막대)과 옅은 하늘색 #e6f4fc(선택 배경)는 선택 상태·활성 탭/세그먼트·링크 밑줄·진행·아이콘 강조에만 쓴다. 글자색으로 쓰지 않고(하늘색 위 글자는 #141414), badge-low-stock·reorder-alert-card·button-primary·mix-warning 안에는 쓰지 않는다.
학교 선택은 화면 1에만 있다. 화면 7·8·11·12에는 학교 선택을 두지 않고 nav-pill 안에 현재 학교명 "샘플고등학교"를 표시한다. 학교 전환 기능은 두지 않는다.
외부 서비스 연결 값은 서버에서만 다룬다. 어떤 화면에도 연결 값 입력·외부 서비스 설정·AI 엔진 선택 UI를 두지 않는다.
괄호 안 역할 표시가 없는 구성 요소는 학생·교사·admin 모두에게 보인다.
데스크탑 nav-pill 섹션 링크(1138에 더함): "시약 목록", "사용 기록 내역", "시약장 설정", "QR 스캔", 교사·admin에게만 "재주문 알림"·"입고·시약 등록", admin에게만 "사용자 관리"·"판매처 설정". 모바일에서는 링크를 접고 워드마크·학교명만 남긴다.

## 화면 11
학생·교사·admin 모두 들어온다. 교사·admin은 문 형태·단 수·칸별 보관 분류를 편집하고, 학생은 배치도를 보기만 한다(학생 화면에는 cabinet-edit 영역·편집 컨트롤·저장 버튼이 없다). 같은 학교(샘플고등학교)의 시약장만 보인다.
예시 상태: "1번 시약장", 양문형 · 4단 → 좌/우 × 1~4단 = 8칸. 좌1단 = 산 + 염기(mix-warning 표시), 좌2단 = 유기, 좌3단 = 인화성, 좌4단 = 기타, 우1단 = 산화제, 우2단 = 무기염, 우3단 = 독성, 우4단 = 기타. 선택된 칸은 좌1단.
위→아래 순서: 제목 → (교사·admin) 문 형태·단 수 선택 → 배치도 → 범례 → 선택 칸의 분류 칩 → 주의사항(mix-warning) → 저장.
### 구성 요소
- nav-pill: "Lab_Stock" 워드마크 + 제목 "시약장 설정" + 현재 학교명 "샘플고등학교" 텍스트. 제목 아래 heading-3 "1번 시약장". 하늘색: 데스크탑 현재 섹션 링크("시약장 설정") 아래 #2b9fe0 밑줄 인디케이터(글자는 #141414)
- cabinet-edit: 편집 영역 전체를 감싸는 블록 1개. 안에 cabinet-door-select · cabinet-shelf-select · 선택 칸의 storage-class-chip 묶음 · mix-warning · 하단 전폭 button-primary "저장"이 들어간다. 학생 화면에는 이 블록이 없다 (교사·admin만)
- cabinet-door-select: cabinet-edit 맨 위, 문 형태 2옵션 pill "양문형 / 단문형"(rules.json cabinet.door_types), 한 번에 하나만 선택. 고르면 아래 배치도의 열 수가 즉시 바뀐다(양문형 = 좌·우 2열, 단문형 = 1열). 예시 상태 "양문형" 선택. 하늘색: 선택 옵션 배경 #e6f4fc + 1px #2b9fe0 테두리(글자는 #141414), 미선택은 #f3f3f3 채움·#707070 글자 (교사·admin만)
- cabinet-shelf-select: cabinet-door-select 바로 아래, 단 수 2옵션 pill "3단 / 4단"(rules.json cabinet.shelves), 한 번에 하나만 선택. 고르면 배치도의 행 수가 즉시 바뀐다. 예시 상태 "4단" 선택. 하늘색: 선택 옵션 배경 #e6f4fc + 1px #2b9fe0 테두리(글자는 #141414) (교사·admin만)
- cabinet-slot: 시약장 정면 배치도의 칸 1개. 배치도 = 왼쪽에 단 라벨(caption "1단"~"4단"), 위쪽에 문 라벨(caption "좌" / "우"), 양문형이면 좌·우 묶음 사이를 가운데 통로처럼 비운다. 칸은 같은 크기 격자(#f3f3f3 채움, rounded 16), 칸 안에 지정된 분류 이름(label, #141414)을 적고, 분류가 없으면 caption "미지정"(#707070). 예시 상태 8칸. 교사·admin은 칸을 눌러 선택하고, 학생에게는 같은 배치도가 보기 전용으로 보인다(누름 동작 없음). 산 + 염기가 지정된 좌1단 칸에는 #141414 경고 아이콘을 칸 오른쪽 위에 둔다. 하늘색: 선택된 칸 배경 #e6f4fc + 2px #2b9fe0 테두리(글자는 #141414)
- storage-class-chip: 보관 분류 칩 8종 "유기·산·염기·산화제·인화성·무기염·독성·기타"(rules.json cabinet.storage_classes). cabinet-edit 안에서 선택된 칸(좌1단)의 분류를 고르는 칩 묶음, 두 줄 배치, 한 칸에 여러 개 선택 가능. 예시 상태 "산"·"염기" 선택. 칩 = rounded 9999, label 크기, 미선택 #f3f3f3 채움. 배치도 아래 범례 한 줄(미지정 · 선택 칸)에도 같은 칩 모양을 보기 전용으로 쓴다(학생에게는 범례만 보인다). 하늘색: 선택된 칩 배경 #e6f4fc + 1px #2b9fe0 테두리(글자는 #141414)
- mix-warning: 칩 묶음과 저장 버튼 사이 구분 영역의 "주의사항" 목록. 같은 칸에 rules.json cabinet.incompatible 조합(산+염기, 산화제+인화성, 산화제+유기, 산+인화성, 독성+산)이 지정되면 재고 부족과 같은 핑크로 경고한다(rules.json cabinet.warning_color #d6246a, 2026-10-02 사용자 결정). 줄마다 #d6246a 경고 아이콘 + #141414 body-sm 문구로 표시한다. 예시 상태 1줄 "좌1단: 산과 염기는 섞이면 위험해요. 다른 칸에 나눠 보관하세요". #ffffff 바탕 + 1px #d6246a 테두리, rounded 16. 핑크는 아이콘·테두리에만 쓰고, 하늘색은 쓰지 않는다. 학생 화면에도 배치도 아래에 같은 경고를 보기 전용으로 표시한다
- button-primary: cabinet-edit 하단 전폭 "저장". 하늘색 없음(#141414 채움) (교사·admin만)
- ex-toast: 저장 직후 "시약장 설정을 저장했어요" 알림. 하늘색: 완료 체크 아이콘 #2b9fe0 (교사·admin만)
### 반영한 레퍼런스
- https://uibowl.io/name/BookMyShow?patterns=%EC%98%88%EC%95%BD%C2%B7%EA%B2%B0%EC%A0%9C&patternName=3.%EC%A2%8C%EC%84%9D%20%EC%84%A0%ED%83%9D
- https://uibowl.io/name/Frontier%20Airlines?patterns=%EC%98%88%EC%95%BD%C2%B7%EA%B2%B0%EC%A0%9C&patternName=%EC%A2%8C%EC%84%9D%20%EC%84%A0%ED%83%9D
- https://uibowl.io/name/%ED%85%8C%EC%8A%AC%EB%9D%BC%20(Tesla)?patterns=%EC%A0%9C%EC%96%B4&patternName=%EC%B0%A8%EB%9F%89%EC%BB%A8%ED%8A%B8%EB%A1%A4
- https://uibowl.io/name/LG%20ThinQ?patterns=%EC%A0%9C%EC%96%B4&patternName=%EA%B1%B4%EC%A1%B0%EA%B8%B0
- https://uibowl.io/name/G%20car?patterns=%EC%8B%A0%EC%B2%AD%ED%95%98%EA%B8%B0&imgId=cmo85af8n00fcjr04s5erd4yk

## 화면 12
학생·교사·admin 모두 들어온다. 샘플고등학교 시약장 QR만 연다. 다른 학교 QR은 열지 않고 안내만 한다(N1).
위→아래 순서: 상단 바(닫기 · 플래시) → 탭 "QR 스캔 / 번호로 찾기" → 안내 2줄 → 카메라 프레임 → 실패 안내 줄 → 하단 고정 "시약장 번호로 찾기".
### 구성 요소
- nav-pill: 닫기(이전 화면) + 제목 "QR 스캔" + 현재 학교명 "샘플고등학교" 텍스트. 하늘색: 닫기 아이콘 #2b9fe0, 데스크탑 현재 섹션 링크("QR 스캔") 아래 #2b9fe0 밑줄 인디케이터
- segmented-control: nav-pill 아래 "QR 스캔 / 번호로 찾기" 두 탭, 한 번에 하나만 선택. 기본은 "QR 스캔". 선택된 탭은 segmented-control-active
- segmented-control-active: 선택된 탭 흰 pill. 하늘색: 1px #2b9fe0 테두리(글자는 #141414)
- qr-scan: "QR 스캔" 탭 본문. 상단 안내 heading-4 "시약장 문에 붙은 QR을 맞춰주세요" + body-sm(#707070) "카메라는 시약장 QR을 읽는 데만 사용해요". 가운데 카메라 미리보기 영역(#262626 채움, rounded 24) 안에 1:1 코너 브라켓 프레임(#ffffff 선). 딤·반투명 덮개는 쓰지 않는다. 프레임 아래 button-pill-soft "플래시". 카메라 권한이 없으면 미리보기 영역 자리에 #f3f3f3 채움 + #141414 문구 "카메라 권한이 필요해요" + button-outline "권한 설정"을 둔다. 인식 실패·다른 학교 QR이면 별도 화면 없이 미리보기 영역 아래 #ffffff 바탕에 #141414 경고 아이콘 + #141414 body 1줄("QR을 읽지 못했어요. 시약장 번호로 찾아보세요" / "샘플고등학교 시약장 QR이 아니에요")을 표시하고 아래 qr-manual-entry로 안내한다. 스캔 성공 → 아래 ex-modal-card 결과 시트. 하늘색: 인식 중 상태의 프레임 선 #2b9fe0
- qr-manual-entry: 두 곳. ① 화면 최하단 고정 button-outline "시약장 번호로 찾기"(누르면 "번호로 찾기" 탭으로 전환). ② "번호로 찾기" 탭 본문: 라벨 "시약장 번호" + text-input(플레이스홀더 "예: 1") + 하단 전폭 button-primary "찾기"(비어 있으면 비활성). 없는 번호면 입력 아래 #141414 아이콘 + #141414 body-sm "샘플고등학교에 이 번호의 시약장이 없어요". 찾으면 아래 ex-modal-card 결과 시트. 하늘색: 입력 왼쪽 검색 아이콘 #2b9fe0
- text-input: qr-manual-entry의 "시약장 번호" 입력. 포커스 링은 #141414
- ex-modal-card: 스캔·번호 찾기 결과 바텀시트. heading-3 "1번 시약장" + caption "양문형 · 4단" → 이 시약장의 reagent-row 목록 → 행을 누르면 시약 상세(화면 3)로, 시트 하단 button-outline "배치도 보기"는 화면 11로 간다. 첫 행 아래 msds-entry. 테두리 1px #e0e0e0, 그림자·딤 없음
- reagent-row: 결과 시트의 시약 한 줄 = 시약명(title) + 재고량·단위(body) + 칸 위치 caption("좌1단"). 재고가 기준 미만이면 행 안에 badge-low-stock(화면 2와 같은 규칙). 하늘색: 누른 행 배경 #e6f4fc
- badge-low-stock: reagent-row 안 "재고 부족" 칩(#d6246a 채움, #ffffff 글자). 하늘색 없음
- msds-entry: 결과 시트 안 button-pill-soft "MSDS 보기 ↗". 학생·교사·admin 모두. 하늘색: 바깥 화살표 아이콘 #2b9fe0(라벨 글자는 #141414)
- button-pill-soft: qr-scan "플래시", msds-entry "MSDS 보기 ↗"
- button-outline: 하단 고정 "시약장 번호로 찾기", 권한 상태 "권한 설정", 결과 시트 "배치도 보기"
- button-primary: "번호로 찾기" 탭 "찾기". 하늘색 없음
### 반영한 레퍼런스
- https://uibowl.io/name/%EC%B9%B4%EC%B9%B4%EC%98%A4T?patterns=%EC%B4%AC%EC%98%81%ED%95%98%EA%B8%B0&patternName=QR%EC%8A%A4%EC%BA%94-%EC%9E%90%EC%A0%84%EA%B1%B0%20%EB%B0%98%EB%82%A9
- https://uibowl.io/name/%EB%B3%BC%ED%8A%B8%EC%97%85?patterns=%EC%B4%AC%EC%98%81%ED%95%98%EA%B8%B0&patternName=QR%EC%8A%A4%EC%BA%94
- https://uibowl.io/name/%EB%A7%88%EB%AF%B8%ED%86%A1?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&imgId=cmpcmrk8h01s0jl04xuxmaavu
- https://uibowl.io/name/%EB%8B%A5%ED%84%B0%EB%8B%A4%EC%9D%B4%EC%96%B4%EB%A6%AC?patterns=%EC%B4%AC%EC%98%81%ED%95%98%EA%B8%B0&imgId=cmr7e4uyx00diju04jj009eeh
- https://uibowl.io/name/%EB%B9%BD%EB%8B%A4%EB%B0%A9?patterns=%EC%BF%A0%ED%8F%B0&imgId=cmsqw7eev001si604q3io8gzt

## 화면 7
이 화면은 교사·admin만 들어온다. 화면 3의 button-outline "입고"와 nav-pill 섹션 링크로 들어온다. 학생 nav에는 진입 링크가 없다(학생 노출 0).
1138 구성을 유지하고, stock-intake의 수량 입력을 스테퍼 + 프리셋 칩 + 재고 미리보기 1줄로 바꾼다.
### 구성 요소
- nav-pill: "Lab_Stock" 워드마크 + 제목 "입고·시약 등록" + 현재 학교명 "샘플고등학교" 텍스트. 하늘색: 데스크탑 현재 섹션 링크("입고·시약 등록") 아래 #2b9fe0 밑줄 인디케이터(글자는 #141414) (교사·admin만)
- segmented-control: 화면 상단에서 두 갈래를 먼저 고른다. "기존 시약 입고 / 새 시약 등록", 한 번에 하나만 선택. 선택된 옵션은 segmented-control-active (교사·admin만)
- segmented-control-active: 선택된 갈래의 흰 pill. 하늘색: 1px #2b9fe0 테두리로 선택 상태 표시(글자는 #141414) (교사·admin만)
- stock-intake: "기존 시약 입고" 갈래. 검색 → 선택 → 수량 입력 순서. 상단 text-input 검색 바("시약명 검색") → 결과 reagent-row 목록에서 시약 1개 선택 → 선택한 시약 카드(시약명 title + 오른쪽 닫기 X, #f3f3f3 채움, rounded 16) → 수량 행: 라벨 "입고 수량"(필수) 왼쪽, 오른쪽에 스테퍼 [− | 수량 | +](가운데는 직접 타이핑하는 text-input, 단위 suffix "병"/"mL"/"g") → 스테퍼 아래 프리셋 칩 한 줄 "1 · 5 · 10"(누르면 수량 칸에 그 값이 들어간다) → ⓘ 보조 1줄 body-sm(#707070) "현재 3병 → 입고 후 8병" → "입고일"(필수, 오늘 날짜 기본값) text-input → 하단 전폭 button-primary "입고". 수량이 0이면 −는 비활성(#adadad). 빈 값·음수는 입력 아래 #141414 body-sm 안내 "1 이상 입력하세요"(핑크 금지). 하늘색: 선택된 결과 행 배경 #e6f4fc + 왼쪽 #2b9fe0 선택 표시, ⓘ 아이콘 #2b9fe0 (교사·admin만)
- reagent-register: "새 시약 등록" 갈래. 라벨 위·입력 아래 세로 폼. "시약명"(필수), "종류"(필수, 드롭다운), "재고량"(필수) + 단위 suffix, "입고일"(필수), "MSDS 연결 주소" text-input → 하단 전폭 button-primary "시약 등록". 필수 라벨 옆 caption "필수". 하늘색: 종류 드롭다운의 펼침 아이콘 #2b9fe0, 열린 목록의 현재 선택 항목 배경 #e6f4fc (교사·admin만)
- text-input: stock-intake 검색 바, 스테퍼 가운데 수량 칸(단위 suffix #707070), 입고일, reagent-register 폼 입력. 하늘색: 검색 바 왼쪽 검색 아이콘 #2b9fe0, 날짜 입력 오른쪽 달력 아이콘 #2b9fe0. 포커스 링은 design.md대로 #141414 (교사·admin만)
- reagent-row: stock-intake 검색 결과 한 줄 = 시약명(title) + 현재 재고량·단위(body). 하늘색: 선택 상태는 위 stock-intake 설명과 같다. 재고 부족 표시는 이 화면에 두지 않는다 (교사·admin만)
- button-outline: 스테퍼 양끝 "−" · "+" 원형 pill(44 이상, 1px #e0e0e0 테두리). 하한 0에서 "−" 비활성 (교사·admin만)
- button-pill-soft: 프리셋 칩 "1" · "5" · "10", 검색 0건 안내의 "새 시약 등록". 하늘색: 선택된 프리셋 칩 배경 #e6f4fc + 1px #2b9fe0 테두리(글자는 #141414), 그림자 없음 (교사·admin만)
- button-primary: stock-intake "입고", reagent-register "시약 등록". 필수 항목이 비면 비활성. 하늘색 없음(#141414 채움) (교사·admin만)
- ex-empty-state-card: 검색 결과 0건일 때 검색 바는 유지하고 "찾는 시약이 없어요" 제목 + body-sm(#707070) "시약명을 확인하거나 새로 등록하세요" + button-pill-soft "새 시약 등록" (누르면 "새 시약 등록" 갈래로 전환). 하늘색: 안내 아이콘 #2b9fe0 (교사·admin만)
- ex-toast: 저장 직후 "입고를 기록했어요" / "시약을 등록했어요" 알림, 이후 화면 2로 돌아간다. 하늘색: 완료 체크 아이콘 #2b9fe0 (교사·admin만)
### 반영한 레퍼런스
- https://uibowl.io/name/%EB%B9%BC%EA%B8%B0?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&patternName=%EC%83%81%ED%92%88%20%EB%93%B1%EB%A1%9D
- https://uibowl.io/name/%EC%9A%B0%EB%A6%AC%EB%8F%99%EB%84%A4GS?patterns=%EC%A1%B0%ED%9A%8C%ED%95%98%EA%B8%B0&patternName=%EC%9E%AC%EA%B3%A0%EC%B0%BE%EA%B8%B0
- https://uibowl.io/name/%EB%A7%88%EC%9D%B4%ED%98%84%EB%8C%80?patterns=%EC%84%A0%EB%AC%BC%ED%95%98%EA%B8%B0&imgId=cmojmaunh000al204u4pkec37
- https://uibowl.io/name/%ED%8F%AC%EC%8A%A4%ED%8B%B0?patterns=%EC%9E%A5%EB%B0%94%EA%B5%AC%EB%8B%88&imgId=cmukh11i5000zl80421av0ejn
- https://uibowl.io/name/%EC%95%B3%ED%94%8C%EB%A6%AC?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&imgId=cmtpokqcx001ukz04i4g1gpag

## 화면 8
이 화면은 admin만 들어온다. 학생·교사 nav에는 진입 링크가 없다(학생·교사 노출 0).
1138 구성을 유지하고, 목록을 "멤버" / "초대 대기 (N)" 두 섹션으로 나누며, 역할 변경은 행 › → 바텀시트 라디오로 처리한다.
### 구성 요소
- nav-pill: "Lab_Stock" 워드마크 + 제목 "사용자 관리" + 현재 학교명 "샘플고등학교" 텍스트. 하늘색: 데스크탑 현재 섹션 링크("사용자 관리") 아래 #2b9fe0 밑줄 인디케이터 (admin만)
- user-manage: 화면 본문 전체 블록 1개. 헤더 한 줄 "샘플고등학교 사용자 N명"(heading-3) + 오른쪽 button-primary "초대" → text-input 이름 검색 → 섹션 "멤버"(heading-4): ex-data-table-cell 행 = 이름(title) + 본인 행 "나" 배지 + 보조줄 역할 텍스트 "학생"/"교사"/"admin"(body-sm, #707070) + 오른쪽 › (누르면 역할 변경 시트) → 섹션 "초대 대기 (2)"(heading-4): 행 = 이메일(body) + 초대일(caption, #707070) + 상태 텍스트 "대기"(label, #141414) → 화면 하단 유의사항 body-sm(#707070) "같은 학교(샘플고등학교) 계정만 초대할 수 있어요". 초대·역할 변경·삭제는 아래 ex-modal-card로 진행한다. 하늘색: 로그인한 admin 본인 행 배경 #e6f4fc (admin만)
- text-input: 사용자 목록 위 이름 검색 바(플레이스홀더 "이름 검색"), 초대 시트 안 초대 대상 입력("이름", "이메일"). 하늘색: 검색 아이콘 #2b9fe0 (admin만)
- ex-data-table-cell: "멤버"·"초대 대기" 섹션의 행. "나" 배지와 역할 텍스트는 label 크기 pill(#f3f3f3 채움, 글자 #141414)·보조줄 텍스트로 흑백만 쓴다. 하늘색: 오른쪽 › 아이콘 #2b9fe0 (본인 행 배경은 user-manage 설명대로) (admin만)
- ex-modal-card: 그림자·딤 없이 1px #e0e0e0 테두리 바텀시트·확인 카드. ① 초대 시트: 제목 "사용자 초대" + 안내문(body-lg) + button-pill-soft "초대 링크 복사" + 직접 입력 text-input + 역할 선택 segmented-control + 하단 전폭 button-primary "N명 초대"(0명이면 비활성). ② 역할 변경 시트: 제목 "{이름}의 역할" + 라디오 3행 "학생 / 교사 / admin"(행 = 역할 이름 + 오른쪽 원형 라디오) + 하단 전폭 button-primary "변경" + 맨 아래 button-outline "사용자 삭제". 본인 행과 학교의 마지막 admin 행에서는 "사용자 삭제"를 숨기고, 마지막 admin은 다른 역할로 바꿀 수 없다(라디오 비활성 + caption #707070 "admin이 최소 1명 있어야 해요"). ③ 삭제 확인: "이 사용자를 삭제할까요?" + button-outline "취소" + button-primary "삭제". 하늘색: 초대 링크 아이콘 #2b9fe0, 역할 변경 라디오의 선택 행 배경 #e6f4fc + 1px #2b9fe0 테두리 + 라디오 채움 #2b9fe0(글자는 #141414) (admin만)
- segmented-control: 초대 시트 안 역할 선택 "학생 / 교사", 한 번에 하나만 선택 (admin만)
- segmented-control-active: 선택된 역할 흰 pill. 하늘색: 1px #2b9fe0 테두리(글자는 #141414) (admin만)
- button-pill-soft: 초대 시트 "초대 링크 복사" (admin만)
- button-primary: 헤더 "초대", 시트 "N명 초대"·"변경", 확인 카드 "삭제". 하늘색 없음 (admin만)
- button-outline: 역할 변경 시트 "사용자 삭제", 확인 카드 "취소" (admin만)
- ex-empty-state-card: 검색 결과 0건이면 검색 바를 유지하고 "찾는 사용자가 없어요", 다른 사용자가 0명이면 "아직 초대한 사용자가 없어요" 1줄 + 하단 유의사항 유지. 하늘색: 안내 아이콘 #2b9fe0 (admin만)
- ex-toast: 초대·역할 변경·삭제 직후 "N명을 초대했어요" / "역할을 바꿨어요" / "사용자를 삭제했어요" 알림, 이후 사용자 목록으로 돌아온다. 하늘색: 완료 체크 아이콘 #2b9fe0 (admin만)
### 반영한 레퍼런스
- https://uibowl.io/name/%EC%9D%B4%EC%A7%80%ED%83%9C%EC%8A%A4%ED%81%AC?patterns=%ED%83%90%EC%83%89&patternName=%EA%B8%B0%EC%97%85%20%EA%B5%AC%EC%84%B1%EC%9B%90
- https://uibowl.io/name/%EC%8B%A0%ED%95%9C%20%EC%8A%88%ED%8D%BCSOL?patterns=%EA%B2%8C%EC%9D%B4%EB%AF%B8%ED%94%BC%EC%BC%80%EC%9D%B4%EC%85%98&imgId=cmsmkdjor0007jz04ehaecntc
- https://uibowl.io/name/%EC%91%A5%EC%91%A5%EC%B0%B0%EC%B9%B5?patterns=%EC%84%A4%EC%A0%95&imgId=cmub7kwx2000njs04uwzytdex
- https://uibowl.io/name/%ED%8C%A8%EC%8A%A4%EC%98%A4%EB%8D%94?patterns=%EA%B2%8C%EC%9D%B4%EB%AF%B8%ED%94%BC%EC%BC%80%EC%9D%B4%EC%85%98&imgId=cmspf7433001dl704mbiwaamm
- https://uibowl.io/name/%ED%8E%AB%ED%94%BC%20?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&patternName=%EA%B0%80%EC%A1%B1%20%EA%B5%AC%EC%84%B1%EC%9B%90

## 역할별 노출
앱 전체(화면 1~12) 기준 개수. runs/20261002-1138 표(화면 1~10)에 화면 11·12를 더했다.
manual-upload = 화면 6 진입 버튼 1 + 화면 5 업로드 영역 1. vendor-register = 화면 6 버튼 1 + 화면 9 블록 1 (admin만). msds-entry = 화면 3 1 + 화면 10 상세 1 + 화면 12 결과 시트 1. stock-intake·reagent-register = 화면 7 (교사·admin). user-manage = 화면 8 (admin만). cabinet-edit = 화면 11 (교사·admin, 학생은 배치도 보기만).

| 컴포넌트 | 학생 | 교사 | admin |
|---|---|---|---|
| manual-upload | 0 | 2 | 2 |
| reorder-alert-card | 0 | 1 | 1 |
| vendor-link | 0 | 1 | 1 |
| vendor-register | 0 | 0 | 2 |
| msds-entry | 3 | 3 | 3 |
| stock-intake | 0 | 1 | 1 |
| reagent-register | 0 | 1 | 1 |
| user-manage | 0 | 0 | 1 |
| cabinet-edit | 0 | 1 | 1 |
