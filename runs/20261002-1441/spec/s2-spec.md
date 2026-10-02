# S2 설계 — run 20261002-1441

대상 화면: 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 · 학교: 샘플고등학교 (input.json)
목적: 이미 완성된 화면 2~12의 모바일 프레임에 하단 tab-bar를 넣어 홈(화면 13, runs/20261002-1416)과 일관되게 맞춘다. 각 화면의 내용·구성은 바꾸지 않는다.
각 화면 섹션은 최신 승인 설계를 그대로 옮기고 tab-bar·tab-item 두 줄만 더했다.
- 화면 2·3·6: runs/20261002-0838/spec/s2-spec.md
- 화면 4·5·9·10: runs/20261002-1138/spec/s2-spec.md
- 화면 7·8·11·12: runs/20261002-1301/spec/s2-spec.md
- tab-bar·tab-item 정의: runs/20261002-1416/spec/s2-spec.md (화면 13)
근거: docs/PRD.md, docs/story-service.md 결정 사항("모바일 하단 탭바"), docs/design.md(`tab-bar` 섹션), harness/rules.json(roles R1~R7, screens_required, tab_bar, cabinet, colors), research/s1-adopt.md
색·폰트·모서리·간격은 docs/design.md와 harness/rules.json을 따른다. 허용 색 밖의 값은 쓰지 않는다. 반투명 회색은 badge-overlay 안에서만 허용된다. 그림자는 쓰지 않는다(segmented-control-active 예외).
- 강조색 #d6246a와 연핑크 #fbe9f0는 badge-low-stock, reorder-alert-card, mix-warning 안에서만 쓴다. mix-warning 밖의 오류·경고·실패 안내에는 핑크를 쓰지 않고 #141414 아이콘 + #141414 문구로만 표시한다.
- 하늘색 #2b9fe0(선·인디케이터·아이콘·진행 막대)과 옅은 하늘색 #e6f4fc(선택 배경)는 선택 상태·활성 탭/세그먼트·링크 밑줄·진행·아이콘 강조에만 쓴다. 글자색으로 쓰지 않고(하늘색 위 글자는 #141414), badge-low-stock·reorder-alert-card·button-primary·mix-warning 안에는 쓰지 않는다.
학교 선택은 화면 1에만 있다. 화면 2~12에는 학교 선택을 두지 않고 nav-pill 안에 현재 학교명 "샘플고등학교"를 표시한다. 학교 전환 기능은 두지 않는다.
외부 서비스 연결 값은 서버에서만 다룬다. 어떤 화면에도 연결 값 입력·외부 서비스 설정·AI 엔진 선택 UI를 두지 않는다.
괄호 안 역할 표시가 없는 구성 요소는 학생·교사·admin 모두에게 보인다.
내비게이션 분담(화면 13과 같음): 모바일 = 하단 tab-bar 4개(홈·시약·QR 스캔·기록, 역할 무관 동일)가 화면 이동을 맡고, 상단 nav-pill은 워드마크(또는 뒤로가기·닫기)·제목·학교명만 남긴다. 데스크탑 = tab-bar 없이 nav-pill 섹션 링크 유지.
탭 목적지: 홈 = 화면 13, 시약 = 화면 2, QR 스캔 = 화면 12, 기록 = 화면 10. 화면별 활성 탭: 시약 = 화면 2·3·6·7·9·11, 기록 = 화면 4·5·10, QR 스캔 = 화면 12, 홈 = 화면 8(홈 quick-action "사용자 관리"로 들어온다). 활성 탭은 화면마다 하나만 둔다.
모바일 배치 공통: tab-bar는 화면 아래 가장자리 y 780~844(높이 64)에 붙는다. 본문 스크롤 영역은 tab-bar 위쪽 선(y 780)에서 끝나고, 마지막 요소 아래 16 여백을 둔다. 화면이 원래 가진 하단 고정 버튼(저장·입고·찾기 등)은 tab-bar 바로 위로 올려 쌓는다(버튼 아래 끝과 tab-bar 위쪽 선 사이 16). 어떤 요소도 tab-bar 뒤로 가려지지 않는다.

## 화면 2
모바일 활성 탭: "시약".
### 구성 요소
- nav-pill: "Lab_Stock" 워드마크와 현재 학교명 "샘플고등학교" 텍스트. 데스크탑에서는 섹션 링크("시약 목록", 교사·admin에게만 "재주문 알림")가 함께 보이고, 모바일에서는 워드마크·학교명만 남긴다. 학교 전환 기능은 두지 않는다. 하늘색: 현재 섹션 링크("시약 목록") 아래 #2b9fe0 밑줄 인디케이터(글자는 #141414)
- segmented-control: 리스트 위 필터 "전체 / 재고 부족" 두 옵션, 한 번에 하나만 선택. 선택된 옵션은 segmented-control-active
- segmented-control-active: 선택된 필터 옵션의 흰 pill. 하늘색: 1px #2b9fe0 테두리로 선택 상태 표시(글자는 #141414)
- text-input: 필터 아래 시약명 검색 바. 플레이스홀더 "시약명 검색". 하늘색: 바 왼쪽 검색 아이콘 #2b9fe0. 포커스 링은 design.md대로 #141414
- reagent-row: 시약 한 줄 = 1행 시약명(title) + 2행 보조 정보(재고량·단위, 입고일 caption). 행을 탭하면 화면 3으로 이동. 행 사이 간격 12. 하늘색: 오른쪽 이동 화살표 아이콘 #2b9fe0, 누른 상태의 행 배경 #e6f4fc. 재고 부족 행의 배지 안에는 하늘색을 쓰지 않는다
- badge-low-stock: 재고가 필요량보다 적은 시약 행에서 시약명 옆에 "재고 부족" 라벨. 잔여 수치는 같은 행 2행의 재고량으로 보여준다. 하늘색 없음
- ex-empty-state-card: 검색 결과가 0건이거나 "재고 부족" 필터 결과가 0건일 때 안내 문구. 하늘색: 안내 아이콘 #2b9fe0
- tab-bar: 모바일 전용 하단 탭바 1개. 화면 아래 가장자리에 붙은 전폭 사각형 바(x 0, 폭 390, 높이 64, 위치 y 780~844, rounded 0). #ffffff 채움 + 위쪽에만 1px #f0f0f0 선, 그림자 없음, 화면 아래·좌우 띄움 없음(floating pill 아님). 안쪽 위아래 여백 8, 좌우 여백 0. 안에 tab-item 4개를 같은 폭으로 꽉 채워 둔다. 역할 무관 동일. 리스트 스크롤 영역은 tab-bar 위쪽 선에서 끝난다. 데스크탑 프레임에는 두지 않는다. 하늘색: 활성 tab-item의 #2b9fe0 아이콘만(바탕 채움 없음)
- tab-item: tab-bar 안 4개, 왼쪽부터 "홈"(화면 13) · "시약"(화면 2) · "QR 스캔"(화면 12) · "기록"(화면 10). 각 항목 = 같은 폭(390 ÷ 4) 사각형 누름 영역(rounded 0, 채움 없음, pill 없음), 높이 48(44 이상), 아이콘 위 + label(12/600) 아래, 아이콘과 라벨 사이 4. 이 화면의 활성 = "시약": #2b9fe0 아이콘 + 라벨 #141414, 뒤 바탕 없음. 비활성 3개("홈"·"QR 스캔"·"기록"): 아이콘·라벨 #707070
### 반영한 레퍼런스
- https://uibowl.io/name/%EB%A9%94%EB%94%94%EC%BD%94%EC%B9%98?patterns=%EA%B2%80%EC%83%89&imgId=cms8e8sdi0007jm044by8323r
- https://uibowl.io/name/%EC%BF%A0%ED%8C%A1?patterns=%EB%A9%94%EC%9D%B8&imgId=pujxwsmnkvc7nav05jzqks8l
- https://uibowl.io/name/%ED%81%AC%EB%AA%BD?patterns=%EC%B1%84%ED%8C%85&imgId=cmopsvj79001xjm04tk8cii2l
- https://uibowl.io/name/%EC%9A%B0%EB%A6%AC%EB%8F%99%EB%84%A4GS?patterns=%EC%A1%B0%ED%9A%8C%ED%95%98%EA%B8%B0&patternName=%EC%9E%AC%EA%B3%A0%EC%B0%BE%EA%B8%B0

## 화면 3
모바일 활성 탭: "시약". 하단 고정 버튼("사용 기록", "입고")은 tab-bar 바로 위로 올린다.
### 구성 요소
- nav-pill: 뒤로가기(화면 2) + 제목 "시약 상세" + 현재 학교명 "샘플고등학교" 텍스트. 학교 전환 기능은 두지 않는다. 하늘색: 뒤로가기 아이콘 #2b9fe0
- reagent-detail-card: 상단 요약. 시약명(title), 현재 재고량(display) + 단위, 입고일 라벨-값(caption 라벨). 하늘색 없음(재고 부족 배지가 들어가는 카드라 중립 유지)
- badge-low-stock: 재고가 필요량보다 적을 때만 reagent-detail-card 안 시약명 옆에 "재고 부족". 하늘색 없음
- segmented-control: 요약 아래 "정보 / 사용 기록" 두 탭, 활성 탭은 하나. 선택된 탭은 segmented-control-active
- segmented-control-active: 활성 탭의 흰 pill. 하늘색: 활성 탭 아래 #2b9fe0 인디케이터(글자는 #141414)
- ex-data-table-cell: "정보" 탭은 시약 속성(입고일 등) 라벨-값 표, "사용 기록" 탭은 사용 날짜·사용자·사용량 3열 표. 하늘색: 가장 최근 사용 기록 행 배경 #e6f4fc
- msds-entry: msds-qr-tile(MSDS QR 1:1을 독립 블록 중앙에, 바로 아래 설명 라벨 "QR로 MSDS 열기") + 그 아래 대체 경로 button-pill-soft "MSDS 보기 ↗". 학생·교사·admin 모두에게 1개. 하늘색: "MSDS 보기 ↗"의 바깥 화살표 아이콘 #2b9fe0(라벨 글자는 #141414). QR 이미지 자체는 흑백 유지
- button-primary: 하단 고정 "사용 기록" → 화면 4. 학생·교사·admin 모두. 모바일에서는 tab-bar 바로 위(버튼 아래 끝과 tab-bar 위쪽 선 사이 16)에 둔다. 하늘색 없음(#141414 채움)
- button-outline: 하단 고정 버튼 옆 "입고" (교사·admin만, 학생 화면에는 없음). 모바일에서는 "사용 기록"과 같은 줄, tab-bar 바로 위
- tab-bar: 모바일 전용 하단 탭바 1개. 화면 아래 가장자리에 붙은 전폭 사각형 바(x 0, 폭 390, 높이 64, 위치 y 780~844, rounded 0). #ffffff 채움 + 위쪽에만 1px #f0f0f0 선, 그림자 없음, 화면 아래·좌우 띄움 없음(floating pill 아님). 안쪽 위아래 여백 8, 좌우 여백 0. 안에 tab-item 4개를 같은 폭으로 꽉 채워 둔다. 역할 무관 동일. 하단 고정 버튼 줄은 이 바 위에 쌓는다. 데스크탑 프레임에는 두지 않는다. 하늘색: 활성 tab-item의 #2b9fe0 아이콘만(바탕 채움 없음)
- tab-item: tab-bar 안 4개, 왼쪽부터 "홈"(화면 13) · "시약"(화면 2) · "QR 스캔"(화면 12) · "기록"(화면 10). 각 항목 = 같은 폭(390 ÷ 4) 사각형 누름 영역(rounded 0, 채움 없음, pill 없음), 높이 48(44 이상), 아이콘 위 + label(12/600) 아래, 아이콘과 라벨 사이 4. 이 화면의 활성 = "시약": #2b9fe0 아이콘 + 라벨 #141414, 뒤 바탕 없음. 비활성 3개("홈"·"QR 스캔"·"기록"): 아이콘·라벨 #707070
### 반영한 레퍼런스
- https://uibowl.io/name/%EB%8B%AC%EB%8B%A4%EB%B0%A9?patterns=%EC%83%81%EC%84%B8%EC%A0%95%EB%B3%B4%20%28PDP%29&patternName=%EC%83%81%ED%92%88
- https://uibowl.io/name/%EB%9F%BD%EB%A7%98?patterns=%EC%83%81%EC%84%B8%EC%A0%95%EB%B3%B4%20%28PDP%29&patternName=%EC%83%81%ED%92%88
- https://uibowl.io/name/%ED%95%98%EB%82%98%EC%9B%90%ED%81%90?patterns=%EA%B0%84%ED%8E%B8%EA%B2%B0%EC%A0%9C&patternName=QR%EA%B2%B0%EC%A0%9C
- https://uibowl.io/name/%EC%B9%B4%EC%B9%B4%EC%98%A4T?patterns=%EC%B4%AC%EC%98%81%ED%95%98%EA%B8%B0&patternName=QR%EC%8A%A4%EC%BA%94-%EC%9E%90%EC%A0%84%EA%B1%B0%20%EB%B0%98%EB%82%A9

## 화면 4
모바일 활성 탭: "기록". 하단 전폭 "사용 기록 저장" 버튼은 tab-bar 바로 위로 올린다.
### 구성 요소
- nav-pill: 뒤로가기(화면 3) + 제목 "사용 기록" + 현재 학교명 "샘플고등학교" 텍스트. 데스크탑 섹션 링크는 화면 2와 같다("시약 목록", 교사·admin에게만 "재주문 알림"). 하늘색: 뒤로가기 아이콘 #2b9fe0, 데스크탑 "시약 목록" 아래 #2b9fe0 밑줄 인디케이터
- reagent-detail-card: 폼 상단 고정 요약. 시약명(title) + 현재 재고량·단위(body). 무엇을 기록하는지 보여준다. 재고 부족 배지는 두지 않는다. 하늘색 없음(중립 유지)
- text-input: 라벨 위·입력 아래 세로 폼. 순서대로 "사용 날짜"(필수), "사용량"(필수) + 단위, "사용자"(필수, 로그인한 사용자 이름이 기본값), "메모". 필수 라벨 옆에 caption "필수". 하늘색: "사용 날짜" 달력 아이콘 #2b9fe0, 단위 칩의 선택 상태 배경 #e6f4fc + 1px #2b9fe0 테두리(글자는 #141414)
- button-primary: 하단 전폭 "사용 기록 저장". 필수 항목이 비면 비활성. 학생·교사·admin 모두. 모바일에서는 tab-bar 바로 위(버튼 아래 끝과 tab-bar 위쪽 선 사이 16)에 둔다. 하늘색 없음
- ex-toast: 저장 직후 "사용 기록을 저장했어요" 알림, 이후 화면 3 "사용 기록" 탭으로 돌아간다. 모바일에서는 tab-bar 위에 뜬다. 하늘색: 완료 체크 아이콘 #2b9fe0
- tab-bar: 모바일 전용 하단 탭바 1개. 화면 아래 가장자리에 붙은 전폭 사각형 바(x 0, 폭 390, 높이 64, 위치 y 780~844, rounded 0). #ffffff 채움 + 위쪽에만 1px #f0f0f0 선, 그림자 없음, 화면 아래·좌우 띄움 없음(floating pill 아님). 안쪽 위아래 여백 8, 좌우 여백 0. 안에 tab-item 4개를 같은 폭으로 꽉 채워 둔다. 역할 무관 동일. 하단 저장 버튼은 이 바 위에 쌓는다. 데스크탑 프레임에는 두지 않는다. 하늘색: 활성 tab-item의 #2b9fe0 아이콘만(바탕 채움 없음)
- tab-item: tab-bar 안 4개, 왼쪽부터 "홈"(화면 13) · "시약"(화면 2) · "QR 스캔"(화면 12) · "기록"(화면 10). 각 항목 = 같은 폭(390 ÷ 4) 사각형 누름 영역(rounded 0, 채움 없음, pill 없음), 높이 48(44 이상), 아이콘 위 + label(12/600) 아래, 아이콘과 라벨 사이 4. 이 화면의 활성 = "기록": #2b9fe0 아이콘 + 라벨 #141414, 뒤 바탕 없음. 비활성 3개("홈"·"시약"·"QR 스캔"): 아이콘·라벨 #707070
### 반영한 레퍼런스
- https://uibowl.io/name/%EC%98%A4%ED%81%B4%EA%B3%A0?patterns=%EA%B8%80%EC%93%B0%EA%B8%B0&patternName=%EA%B8%B0%EB%A1%9D%ED%95%98%EA%B8%B0
- https://uibowl.io/name/%EC%98%A4%EB%8A%98%EC%9D%98%20%EB%A3%A8%ED%8B%B4?patterns=%EA%B8%80%EC%93%B0%EA%B8%B0&patternName=%EB%A3%A8%ED%8B%B4%20%EA%B8%B0%EB%A1%9D%ED%95%98%EA%B8%B0
- https://uibowl.io/name/%EB%A0%88%ED%8F%AC%EB%B8%8C?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&patternName=%EA%B8%B0%EB%A1%9D%ED%95%98%EA%B8%B0

## 화면 5
이 화면은 교사·admin만 들어온다. 학생 화면에는 진입 링크와 업로드 버튼이 없다(학생 노출 0).
모바일 활성 탭: "기록". 하단 고정 "AI 추출"과 2단계 하단 버튼("다시 추출", "확인 후 저장")은 tab-bar 바로 위로 올린다.
### 구성 요소
- nav-pill: 뒤로가기(화면 6) + 제목 "실험 매뉴얼" + 현재 학교명 "샘플고등학교" 텍스트. 하늘색: 뒤로가기 아이콘 #2b9fe0 (교사·admin만)
- manual-upload: 1단계 업로드. 상단 안내 문구 "실험 매뉴얼을 올리면 시약별 사용량을 찾아드려요"(body-lg) + 중앙 업로드/미리보기 타일(rounded 16, 비율 유지) + 미리보기 위 badge-overlay 파일 이름 태그. 하늘색: 업로드 타일 가운데 업로드 아이콘 #2b9fe0, 처리 중 진행 막대 #2b9fe0(트랙 #e6f4fc) (교사·admin만)
- badge-overlay: manual-upload 미리보기 위 파일 이름 태그. 하늘색 없음 (교사·admin만)
- text-input: 업로드 타일 아래 "조 수" 숫자 입력 1개. 하늘색 없음 (교사·admin만)
- button-primary: 1단계 하단 고정 "AI 추출". 파일과 조 수가 비면 비활성, 누르면 처리 중 상태 문구 "사용량을 찾고 있어요"를 거쳐 2단계로 간다. 모바일에서는 tab-bar 바로 위에 둔다. 하늘색 없음 (교사·admin만)
- extraction-table: 2단계 추출 결과 확인. 상단 제목 "추출 결과 확인" + 닫기, 본문 스크롤 표. ex-data-table-cell 4열 = 시약명 · 1조 사용량 · 단위 · 1반 1회 필요량(1조 사용량 × 조 수). 사용량 칸은 text-input으로 고칠 수 있다. 하늘색: 사용자가 고친 칸 배경 #e6f4fc (교사·admin만)
- ex-data-table-cell: extraction-table 안 머리행·본문 셀 (교사·admin만)
- button-outline: 2단계 하단 "다시 추출". 모바일에서는 tab-bar 바로 위 버튼 줄 (교사·admin만)
- button-primary: 2단계 하단 전폭 "확인 후 저장". 사용자가 확인한 뒤에만 저장된다. 모바일에서는 tab-bar 바로 위에 둔다. 하늘색 없음 (교사·admin만)
- ex-toast: 저장 직후 "재주문 기준을 저장했어요" 알림, 이후 화면 6으로 돌아간다. 하늘색: 완료 체크 아이콘 #2b9fe0 (교사·admin만)
- tab-bar: 모바일 전용 하단 탭바 1개. 화면 아래 가장자리에 붙은 전폭 사각형 바(x 0, 폭 390, 높이 64, 위치 y 780~844, rounded 0). #ffffff 채움 + 위쪽에만 1px #f0f0f0 선, 그림자 없음, 화면 아래·좌우 띄움 없음(floating pill 아님). 안쪽 위아래 여백 8, 좌우 여백 0. 안에 tab-item 4개를 같은 폭으로 꽉 채워 둔다. 역할 무관 동일. 하단 고정 버튼 줄은 이 바 위에 쌓는다. 데스크탑 프레임에는 두지 않는다. 하늘색: 활성 tab-item의 #2b9fe0 아이콘만(바탕 채움 없음)
- tab-item: tab-bar 안 4개, 왼쪽부터 "홈"(화면 13) · "시약"(화면 2) · "QR 스캔"(화면 12) · "기록"(화면 10). 각 항목 = 같은 폭(390 ÷ 4) 사각형 누름 영역(rounded 0, 채움 없음, pill 없음), 높이 48(44 이상), 아이콘 위 + label(12/600) 아래, 아이콘과 라벨 사이 4. 이 화면의 활성 = "기록": #2b9fe0 아이콘 + 라벨 #141414, 뒤 바탕 없음. 비활성 3개("홈"·"시약"·"QR 스캔"): 아이콘·라벨 #707070
### 반영한 레퍼런스
- https://uibowl.io/name/%EB%8B%A4%EA%B8%80%EB%A1%9C?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&patternName=%EC%9C%A0%ED%8A%9C%EB%B8%8C%20%EB%A7%81%ED%81%AC%20%EC%97%85%EB%A1%9C%EB%93%9C
- https://uibowl.io/name/%EC%88%98%ED%98%84%EC%9D%B4%EB%9E%91?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&patternName=%EA%B3%B5%EC%9C%A0%20%EC%95%A8%EB%B2%94%20%EC%97%85%EB%A1%9C%EB%93%9C
- https://uibowl.io/name/%ED%82%A4%ED%94%BC%EB%9F%BD?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&patternName=%EC%9D%B8%EC%A6%9D%EC%83%B7-%EC%97%85%EB%A1%9C%EB%93%9C

## 화면 6
이 화면은 교사·admin만 들어온다. 학생 nav에는 진입 링크가 없다(학생 노출 0).
모바일 활성 탭: "시약".
### 구성 요소
- nav-pill: "Lab_Stock" 워드마크 + 제목 "재주문 알림" + 현재 학교명 "샘플고등학교" 텍스트. 학교 전환 기능은 두지 않는다. 하늘색: 데스크탑 현재 섹션 링크("재주문 알림") 아래 #2b9fe0 밑줄 인디케이터 (교사·admin만)
- manual-upload: 알림 목록 위 재주문 기준 안내 박스(배경 #e6f4fc, 글자 #141414, "필요량 = 1반 1회 실험량 × 조 수") 끝의 button-pill-soft "실험 매뉴얼 올리기" → 화면 5. 하늘색: 안내 박스 배경 #e6f4fc와 정보 아이콘 #2b9fe0 (교사·admin만)
- reorder-alert-card: 알림 1건 = badge-low-stock "재고 부족" + 시약명(heading-4) 1줄 + "필요량 N / 현재 재고 M"(body) 1줄 + 알림 날짜(caption). 필요량은 1반 1회 실험량 × 조 수 기준임을 카드 안 보조 문구로 표시. 하늘색 없음 (교사·admin만)
- badge-low-stock: reorder-alert-card 안 "재고 부족" 라벨. 하늘색 없음 (교사·admin만)
- vendor-link: reorder-alert-card 하단 button-primary "판매처 연결". 카드 안이라 하늘색 없음 (교사·admin만)
- ex-modal-card: vendor-link를 누르면 뜨는 확인 모달. "판매처" 라벨-값 행(판매처명·부가 정보) + button-outline "취소" + button-primary "확인". 하늘색: 선택된 판매처 행 배경 #e6f4fc + 왼쪽 #2b9fe0 선택 표시 (교사·admin만)
- vendor-register: 목록 아래 button-outline "판매처 등록" (admin만, 교사 화면에는 없음)
- ex-empty-state-card: 알림이 0건일 때 "재고가 부족한 시약이 없어요" 문구. 하늘색: 안내 아이콘 #2b9fe0 (교사·admin만)
- tab-bar: 모바일 전용 하단 탭바 1개. 화면 아래 가장자리에 붙은 전폭 사각형 바(x 0, 폭 390, 높이 64, 위치 y 780~844, rounded 0). #ffffff 채움 + 위쪽에만 1px #f0f0f0 선, 그림자 없음, 화면 아래·좌우 띄움 없음(floating pill 아님). 안쪽 위아래 여백 8, 좌우 여백 0. 안에 tab-item 4개를 같은 폭으로 꽉 채워 둔다. 역할 무관 동일. 알림 목록 스크롤 영역은 tab-bar 위쪽 선에서 끝난다. 데스크탑 프레임에는 두지 않는다. 하늘색: 활성 tab-item의 #2b9fe0 아이콘만(바탕 채움 없음) (교사·admin만 — 이 화면 자체가 교사·admin 전용)
- tab-item: tab-bar 안 4개, 왼쪽부터 "홈"(화면 13) · "시약"(화면 2) · "QR 스캔"(화면 12) · "기록"(화면 10). 각 항목 = 같은 폭(390 ÷ 4) 사각형 누름 영역(rounded 0, 채움 없음, pill 없음), 높이 48(44 이상), 아이콘 위 + label(12/600) 아래, 아이콘과 라벨 사이 4. 이 화면의 활성 = "시약": #2b9fe0 아이콘 + 라벨 #141414, 뒤 바탕 없음. 비활성 3개("홈"·"QR 스캔"·"기록"): 아이콘·라벨 #707070 (교사·admin만 — 이 화면 자체가 교사·admin 전용)
### 반영한 레퍼런스
- https://uibowl.io/name/W%EC%BB%A8%EC%85%89?patterns=%EB%82%B4%EC%97%AD&patternName=%EC%9E%AC%EC%9E%85%EA%B3%A0%20%EC%95%8C%EB%A6%BC
- https://uibowl.io/name/%EB%8D%B0%EC%9D%BC%EB%A6%AC%EC%83%B7?patterns=%EC%8B%A0%EC%B2%AD%ED%95%98%EA%B8%B0&patternName=%EC%9E%AC%EC%9E%85%EA%B3%A0%20%EC%95%8C%EB%A6%BC
- https://uibowl.io/name/%EB%8D%B0%EC%9D%BC%EB%A6%AC%EC%83%B7?patterns=%EB%82%B4%EC%97%AD&patternName=%EC%9E%AC%EC%9E%85%EA%B3%A0%20%EC%95%8C%EB%A6%BC%EB%82%B4%EC%97%AD
- https://uibowl.io/name/%EC%B9%A9%EC%8A%A4?patterns=%ED%91%B8%EC%8B%9C%EC%95%8C%EB%A6%BC

## 화면 7
이 화면은 교사·admin만 들어온다. 화면 3의 button-outline "입고"와 nav-pill 섹션 링크로 들어온다. 학생 nav에는 진입 링크가 없다(학생 노출 0).
1138 구성을 유지하고, stock-intake의 수량 입력을 스테퍼 + 프리셋 칩 + 재고 미리보기 1줄로 바꾼다(runs/20261002-1301 그대로).
모바일 활성 탭: "시약". 하단 전폭 "입고" / "시약 등록" 버튼은 tab-bar 바로 위로 올린다.
### 구성 요소
- nav-pill: "Lab_Stock" 워드마크 + 제목 "입고·시약 등록" + 현재 학교명 "샘플고등학교" 텍스트. 하늘색: 데스크탑 현재 섹션 링크("입고·시약 등록") 아래 #2b9fe0 밑줄 인디케이터(글자는 #141414) (교사·admin만)
- segmented-control: 화면 상단에서 두 갈래를 먼저 고른다. "기존 시약 입고 / 새 시약 등록", 한 번에 하나만 선택. 선택된 옵션은 segmented-control-active (교사·admin만)
- segmented-control-active: 선택된 갈래의 흰 pill. 하늘색: 1px #2b9fe0 테두리로 선택 상태 표시(글자는 #141414) (교사·admin만)
- stock-intake: "기존 시약 입고" 갈래. 검색 → 선택 → 수량 입력 순서. 상단 text-input 검색 바("시약명 검색") → 결과 reagent-row 목록에서 시약 1개 선택 → 선택한 시약 카드(시약명 title + 오른쪽 닫기 X, #f3f3f3 채움, rounded 16) → 수량 행: 라벨 "입고 수량"(필수) 왼쪽, 오른쪽에 스테퍼 [− | 수량 | +](가운데는 직접 타이핑하는 text-input, 단위 suffix "병"/"mL"/"g") → 스테퍼 아래 프리셋 칩 한 줄 "1 · 5 · 10"(누르면 수량 칸에 그 값이 들어간다) → ⓘ 보조 1줄 body-sm(#707070) "현재 3병 → 입고 후 8병" → "입고일"(필수, 오늘 날짜 기본값) text-input → 하단 전폭 button-primary "입고"(모바일에서는 tab-bar 바로 위). 수량이 0이면 −는 비활성(#adadad). 빈 값·음수는 입력 아래 #141414 body-sm 안내 "1 이상 입력하세요"(핑크 금지). 하늘색: 선택된 결과 행 배경 #e6f4fc + 왼쪽 #2b9fe0 선택 표시, ⓘ 아이콘 #2b9fe0 (교사·admin만)
- reagent-register: "새 시약 등록" 갈래. 라벨 위·입력 아래 세로 폼. "시약명"(필수), "종류"(필수, 드롭다운), "재고량"(필수) + 단위 suffix, "입고일"(필수), "MSDS 연결 주소" text-input → 하단 전폭 button-primary "시약 등록"(모바일에서는 tab-bar 바로 위). 필수 라벨 옆 caption "필수". 하늘색: 종류 드롭다운의 펼침 아이콘 #2b9fe0, 열린 목록의 현재 선택 항목 배경 #e6f4fc (교사·admin만)
- text-input: stock-intake 검색 바, 스테퍼 가운데 수량 칸(단위 suffix #707070), 입고일, reagent-register 폼 입력. 하늘색: 검색 바 왼쪽 검색 아이콘 #2b9fe0, 날짜 입력 오른쪽 달력 아이콘 #2b9fe0. 포커스 링은 design.md대로 #141414 (교사·admin만)
- reagent-row: stock-intake 검색 결과 한 줄 = 시약명(title) + 현재 재고량·단위(body). 하늘색: 선택 상태는 위 stock-intake 설명과 같다. 재고 부족 표시는 이 화면에 두지 않는다 (교사·admin만)
- button-outline: 스테퍼 양끝 "−" · "+" 원형 pill(44 이상, 1px #e0e0e0 테두리). 하한 0에서 "−" 비활성 (교사·admin만)
- button-pill-soft: 프리셋 칩 "1" · "5" · "10", 검색 0건 안내의 "새 시약 등록". 하늘색: 선택된 프리셋 칩 배경 #e6f4fc + 1px #2b9fe0 테두리(글자는 #141414), 그림자 없음 (교사·admin만)
- button-primary: stock-intake "입고", reagent-register "시약 등록". 필수 항목이 비면 비활성. 모바일에서는 tab-bar 바로 위(버튼 아래 끝과 tab-bar 위쪽 선 사이 16)에 둔다. 하늘색 없음(#141414 채움) (교사·admin만)
- ex-empty-state-card: 검색 결과 0건일 때 검색 바는 유지하고 "찾는 시약이 없어요" 제목 + body-sm(#707070) "시약명을 확인하거나 새로 등록하세요" + button-pill-soft "새 시약 등록" (누르면 "새 시약 등록" 갈래로 전환). 하늘색: 안내 아이콘 #2b9fe0 (교사·admin만)
- ex-toast: 저장 직후 "입고를 기록했어요" / "시약을 등록했어요" 알림, 이후 화면 2로 돌아간다. 하늘색: 완료 체크 아이콘 #2b9fe0 (교사·admin만)
- tab-bar: 모바일 전용 하단 탭바 1개. 화면 아래 가장자리에 붙은 전폭 사각형 바(x 0, 폭 390, 높이 64, 위치 y 780~844, rounded 0). #ffffff 채움 + 위쪽에만 1px #f0f0f0 선, 그림자 없음, 화면 아래·좌우 띄움 없음(floating pill 아님). 안쪽 위아래 여백 8, 좌우 여백 0. 안에 tab-item 4개를 같은 폭으로 꽉 채워 둔다. 역할 무관 동일. 하단 전폭 버튼은 이 바 위에 쌓는다. 데스크탑 프레임에는 두지 않는다. 하늘색: 활성 tab-item의 #2b9fe0 아이콘만(바탕 채움 없음) (교사·admin만 — 이 화면 자체가 교사·admin 전용)
- tab-item: tab-bar 안 4개, 왼쪽부터 "홈"(화면 13) · "시약"(화면 2) · "QR 스캔"(화면 12) · "기록"(화면 10). 각 항목 = 같은 폭(390 ÷ 4) 사각형 누름 영역(rounded 0, 채움 없음, pill 없음), 높이 48(44 이상), 아이콘 위 + label(12/600) 아래, 아이콘과 라벨 사이 4. 이 화면의 활성 = "시약": #2b9fe0 아이콘 + 라벨 #141414, 뒤 바탕 없음. 비활성 3개("홈"·"QR 스캔"·"기록"): 아이콘·라벨 #707070 (교사·admin만 — 이 화면 자체가 교사·admin 전용)
### 반영한 레퍼런스
- https://uibowl.io/name/%EB%B9%BC%EA%B8%B0?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&patternName=%EC%83%81%ED%92%88%20%EB%93%B1%EB%A1%9D
- https://uibowl.io/name/%EC%9A%B0%EB%A6%AC%EB%8F%99%EB%84%A4GS?patterns=%EC%A1%B0%ED%9A%8C%ED%95%98%EA%B8%B0&patternName=%EC%9E%AC%EA%B3%A0%EC%B0%BE%EA%B8%B0
- https://uibowl.io/name/%EB%A7%88%EC%9D%B4%ED%98%84%EB%8C%80?patterns=%EC%84%A0%EB%AC%BC%ED%95%98%EA%B8%B0&imgId=cmojmaunh000al204u4pkec37
- https://uibowl.io/name/%ED%8F%AC%EC%8A%A4%ED%8B%B0?patterns=%EC%9E%A5%EB%B0%94%EA%B5%AC%EB%8B%88&imgId=cmukh11i5000zl80421av0ejn
- https://uibowl.io/name/%EC%95%B3%ED%94%8C%EB%A6%AC?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&imgId=cmtpokqcx001ukz04i4g1gpag

## 화면 8
이 화면은 admin만 들어온다. 학생·교사 nav에는 진입 링크가 없다(학생·교사 노출 0).
1138 구성을 유지하고, 목록을 "멤버" / "초대 대기 (N)" 두 섹션으로 나누며, 역할 변경은 행 › → 바텀시트 라디오로 처리한다(runs/20261002-1301 그대로).
모바일 활성 탭: "홈"(홈 quick-action "사용자 관리"로 들어온다). 바텀시트 하단 전폭 버튼("N명 초대", "변경")은 tab-bar 바로 위로 올린다.
### 구성 요소
- nav-pill: "Lab_Stock" 워드마크 + 제목 "사용자 관리" + 현재 학교명 "샘플고등학교" 텍스트. 하늘색: 데스크탑 현재 섹션 링크("사용자 관리") 아래 #2b9fe0 밑줄 인디케이터 (admin만)
- user-manage: 화면 본문 전체 블록 1개. 헤더 한 줄 "샘플고등학교 사용자 N명"(heading-3) + 오른쪽 button-primary "초대" → text-input 이름 검색 → 섹션 "멤버"(heading-4): ex-data-table-cell 행 = 이름(title) + 본인 행 "나" 배지 + 보조줄 역할 텍스트 "학생"/"교사"/"admin"(body-sm, #707070) + 오른쪽 › (누르면 역할 변경 시트) → 섹션 "초대 대기 (2)"(heading-4): 행 = 이메일(body) + 초대일(caption, #707070) + 상태 텍스트 "대기"(label, #141414) → 화면 하단 유의사항 body-sm(#707070) "같은 학교(샘플고등학교) 계정만 초대할 수 있어요". 초대·역할 변경·삭제는 아래 ex-modal-card로 진행한다. 하늘색: 로그인한 admin 본인 행 배경 #e6f4fc (admin만)
- text-input: 사용자 목록 위 이름 검색 바(플레이스홀더 "이름 검색"), 초대 시트 안 초대 대상 입력("이름", "이메일"). 하늘색: 검색 아이콘 #2b9fe0 (admin만)
- ex-data-table-cell: "멤버"·"초대 대기" 섹션의 행. "나" 배지와 역할 텍스트는 label 크기 pill(#f3f3f3 채움, 글자 #141414)·보조줄 텍스트로 흑백만 쓴다. 하늘색: 오른쪽 › 아이콘 #2b9fe0 (본인 행 배경은 user-manage 설명대로) (admin만)
- ex-modal-card: 그림자·딤 없이 1px #e0e0e0 테두리 바텀시트·확인 카드. ① 초대 시트: 제목 "사용자 초대" + 안내문(body-lg) + button-pill-soft "초대 링크 복사" + 직접 입력 text-input + 역할 선택 segmented-control + 하단 전폭 button-primary "N명 초대"(0명이면 비활성). ② 역할 변경 시트: 제목 "{이름}의 역할" + 라디오 3행 "학생 / 교사 / admin"(행 = 역할 이름 + 오른쪽 원형 라디오) + 하단 전폭 button-primary "변경" + 맨 아래 button-outline "사용자 삭제". 본인 행과 학교의 마지막 admin 행에서는 "사용자 삭제"를 숨기고, 마지막 admin은 다른 역할로 바꿀 수 없다(라디오 비활성 + caption #707070 "admin이 최소 1명 있어야 해요"). ③ 삭제 확인: "이 사용자를 삭제할까요?" + button-outline "취소" + button-primary "삭제". 모바일에서 바텀시트는 tab-bar 위쪽 선(y 780) 위에 붙는다. 하늘색: 초대 링크 아이콘 #2b9fe0, 역할 변경 라디오의 선택 행 배경 #e6f4fc + 1px #2b9fe0 테두리 + 라디오 채움 #2b9fe0(글자는 #141414) (admin만)
- segmented-control: 초대 시트 안 역할 선택 "학생 / 교사", 한 번에 하나만 선택 (admin만)
- segmented-control-active: 선택된 역할 흰 pill. 하늘색: 1px #2b9fe0 테두리(글자는 #141414) (admin만)
- button-pill-soft: 초대 시트 "초대 링크 복사" (admin만)
- button-primary: 헤더 "초대", 시트 "N명 초대"·"변경", 확인 카드 "삭제". 하늘색 없음 (admin만)
- button-outline: 역할 변경 시트 "사용자 삭제", 확인 카드 "취소" (admin만)
- ex-empty-state-card: 검색 결과 0건이면 검색 바를 유지하고 "찾는 사용자가 없어요", 다른 사용자가 0명이면 "아직 초대한 사용자가 없어요" 1줄 + 하단 유의사항 유지. 하늘색: 안내 아이콘 #2b9fe0 (admin만)
- ex-toast: 초대·역할 변경·삭제 직후 "N명을 초대했어요" / "역할을 바꿨어요" / "사용자를 삭제했어요" 알림, 이후 사용자 목록으로 돌아온다. 하늘색: 완료 체크 아이콘 #2b9fe0 (admin만)
- tab-bar: 모바일 전용 하단 탭바 1개. 화면 아래 가장자리에 붙은 전폭 사각형 바(x 0, 폭 390, 높이 64, 위치 y 780~844, rounded 0). #ffffff 채움 + 위쪽에만 1px #f0f0f0 선, 그림자 없음, 화면 아래·좌우 띄움 없음(floating pill 아님). 안쪽 위아래 여백 8, 좌우 여백 0. 안에 tab-item 4개를 같은 폭으로 꽉 채워 둔다. 역할 무관 동일. 하단 유의사항까지의 스크롤 영역은 tab-bar 위쪽 선에서 끝난다. 데스크탑 프레임에는 두지 않는다. 하늘색: 활성 tab-item의 #2b9fe0 아이콘만(바탕 채움 없음) (admin만 — 이 화면 자체가 admin 전용)
- tab-item: tab-bar 안 4개, 왼쪽부터 "홈"(화면 13) · "시약"(화면 2) · "QR 스캔"(화면 12) · "기록"(화면 10). 각 항목 = 같은 폭(390 ÷ 4) 사각형 누름 영역(rounded 0, 채움 없음, pill 없음), 높이 48(44 이상), 아이콘 위 + label(12/600) 아래, 아이콘과 라벨 사이 4. 이 화면의 활성 = "홈": #2b9fe0 아이콘 + 라벨 #141414, 뒤 바탕 없음. 비활성 3개("시약"·"QR 스캔"·"기록"): 아이콘·라벨 #707070 (admin만 — 이 화면 자체가 admin 전용)
### 반영한 레퍼런스
- https://uibowl.io/name/%EC%9D%B4%EC%A7%80%ED%83%9C%EC%8A%A4%ED%81%AC?patterns=%ED%83%90%EC%83%89&patternName=%EA%B8%B0%EC%97%85%20%EA%B5%AC%EC%84%B1%EC%9B%90
- https://uibowl.io/name/%EC%8B%A0%ED%95%9C%20%EC%8A%88%ED%8D%BCSOL?patterns=%EA%B2%8C%EC%9D%B4%EB%AF%B8%ED%94%BC%EC%BC%80%EC%9D%B4%EC%85%98&imgId=cmsmkdjor0007jz04ehaecntc
- https://uibowl.io/name/%EC%91%A5%EC%91%A5%EC%B0%B0%EC%B9%B5?patterns=%EC%84%A4%EC%A0%95&imgId=cmub7kwx2000njs04uwzytdex
- https://uibowl.io/name/%ED%8C%A8%EC%8A%A4%EC%98%A4%EB%8D%94?patterns=%EA%B2%8C%EC%9D%B4%EB%AF%B8%ED%94%BC%EC%BC%80%EC%9D%B4%EC%85%98&imgId=cmspf7433001dl704mbiwaamm
- https://uibowl.io/name/%ED%8E%AB%ED%94%BC%20?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&patternName=%EA%B0%80%EC%A1%B1%20%EA%B5%AC%EC%84%B1%EC%9B%90

## 화면 9
이 화면은 admin만 들어온다. 화면 6의 vendor-register 버튼과 nav-pill 섹션 링크로 들어온다. 학생·교사 nav에는 진입 링크가 없다(학생·교사 노출 0).
모바일 활성 탭: "시약". 하단 고정 "판매처 등록"과 폼 하단 전폭 "저장"은 tab-bar 바로 위로 올린다.
### 구성 요소
- nav-pill: "Lab_Stock" 워드마크 + 제목 "판매처 설정" + 현재 학교명 "샘플고등학교" 텍스트. 하늘색: 데스크탑 현재 섹션 링크("판매처 설정") 아래 #2b9fe0 밑줄 인디케이터 (admin만)
- segmented-control: 상단 "우리 학교 판매처 / 공통 목록" 두 탭, 활성 탭은 하나. 선택된 탭은 segmented-control-active (admin만)
- segmented-control-active: 활성 탭 흰 pill. 하늘색: 활성 탭 아래 #2b9fe0 인디케이터(글자는 #141414) (admin만)
- text-input: 탭 아래 판매처명 검색 바("판매처 검색"), 등록·수정 폼 입력("판매처명"(필수), "연락처", "웹사이트 주소"). 하늘색: 검색 아이콘 #2b9fe0 (admin만)
- vendor-register: "우리 학교 판매처" 탭 블록 1개. 학교 판매처 목록(행마다 판매처명·부가 정보 + 오른쪽 더보기 메뉴 "수정"·"삭제") + 하단 고정 button-primary "판매처 등록" → 세로 등록·수정 폼 → 저장 후 목록 복귀. 하늘색: 더보기 아이콘 #2b9fe0, 방금 등록·수정한 행 배경 #e6f4fc (admin만)
- ex-data-table-cell: "공통 목록" 탭의 서비스 공통 판매처 목록, 보기 전용 2열(판매처명 · 부가 정보). 수정·삭제 버튼 없음. 하늘색 없음 (admin만)
- ex-modal-card: 삭제 확인 "이 판매처를 삭제할까요?" + button-outline "취소" + button-primary "삭제". 하늘색 없음 (admin만)
- button-primary: 하단 고정 "판매처 등록", 폼 하단 전폭 "저장"(판매처명이 비면 비활성), 모달 "삭제". 모바일에서 "판매처 등록"·"저장"은 tab-bar 바로 위(버튼 아래 끝과 tab-bar 위쪽 선 사이 16)에 둔다. 하늘색 없음 (admin만)
- button-outline: 삭제 모달 "취소" (admin만)
- ex-empty-state-card: 학교 판매처가 0건일 때 가운데 아이콘 + "등록한 판매처가 없어요" 안내문 + 아래 등록 진입(하단 고정 "판매처 등록"과 같은 동작). 하늘색: 안내 아이콘 #2b9fe0 (admin만)
- ex-toast: 저장·삭제 직후 "판매처를 저장했어요" / "판매처를 삭제했어요" 알림. 하늘색: 완료 체크 아이콘 #2b9fe0 (admin만)
- tab-bar: 모바일 전용 하단 탭바 1개. 화면 아래 가장자리에 붙은 전폭 사각형 바(x 0, 폭 390, 높이 64, 위치 y 780~844, rounded 0). #ffffff 채움 + 위쪽에만 1px #f0f0f0 선, 그림자 없음, 화면 아래·좌우 띄움 없음(floating pill 아님). 안쪽 위아래 여백 8, 좌우 여백 0. 안에 tab-item 4개를 같은 폭으로 꽉 채워 둔다. 역할 무관 동일. 하단 고정 버튼은 이 바 위에 쌓는다. 데스크탑 프레임에는 두지 않는다. 하늘색: 활성 tab-item의 #2b9fe0 아이콘만(바탕 채움 없음) (admin만 — 이 화면 자체가 admin 전용)
- tab-item: tab-bar 안 4개, 왼쪽부터 "홈"(화면 13) · "시약"(화면 2) · "QR 스캔"(화면 12) · "기록"(화면 10). 각 항목 = 같은 폭(390 ÷ 4) 사각형 누름 영역(rounded 0, 채움 없음, pill 없음), 높이 48(44 이상), 아이콘 위 + label(12/600) 아래, 아이콘과 라벨 사이 4. 이 화면의 활성 = "시약": #2b9fe0 아이콘 + 라벨 #141414, 뒤 바탕 없음. 비활성 3개("홈"·"QR 스캔"·"기록"): 아이콘·라벨 #707070 (admin만 — 이 화면 자체가 admin 전용)
### 반영한 레퍼런스
- https://uibowl.io/name/%ED%8E%98%EC%9D%B4%EC%9B%8C%ED%81%AC?patterns=%EB%A9%94%EB%89%B4&patternName=%EA%B0%84%ED%8E%B8%EB%A9%94%EB%89%B4%20-%20%EA%B1%B0%EB%9E%98%EC%B2%98
- https://uibowl.io/name/%ED%8E%98%EC%9D%B4%EC%9B%8C%ED%81%AC?patterns=%ED%8E%B8%EC%A7%91%C2%B7%EC%88%98%EC%A0%95%ED%95%98%EA%B8%B0&patternName=%EA%B1%B0%EB%9E%98%EC%B2%98%EC%88%98%EC%A0%95
- https://uibowl.io/name/%ED%8E%98%EC%9D%B4%EC%9B%8C%ED%81%AC?patterns=%ED%8E%B8%EC%A7%91%C2%B7%EC%88%98%EC%A0%95%ED%95%98%EA%B8%B0&patternName=%EA%B1%B0%EB%9E%98%EC%B2%98%EC%B6%94%EA%B0%80

## 화면 10
학생·교사·admin 모두 들어온다. 같은 학교(샘플고등학교)의 사용 기록만 보인다.
모바일 활성 탭: "기록".
### 구성 요소
- nav-pill: "Lab_Stock" 워드마크 + 제목 "사용 기록 내역" + 현재 학교명 "샘플고등학교" 텍스트. 하늘색: 데스크탑 현재 섹션 링크("사용 기록 내역") 아래 #2b9fe0 밑줄 인디케이터
- segmented-control: 목록 위 필터 "전체 / 내 기록", 한 번에 하나만 선택. 선택된 옵션은 segmented-control-active
- segmented-control-active: 선택된 필터 흰 pill. 하늘색: 1px #2b9fe0 테두리(글자는 #141414)
- text-input: 필터 옆 기간 드롭다운("최근 1개월" 기본값)과 시약명 검색 바("시약명 검색"). 하늘색: 검색 아이콘·드롭다운 펼침 아이콘 #2b9fe0
- ex-data-table-cell: 기록 목록. 날짜(월) 그룹 헤더(caption) 아래 행마다 3열 = 날짜(좌, caption) · 시약명(title) / 사용자(body-sm)(중) · 사용량·단위(우, body). 행을 누르면 ex-modal-card 상세가 열린다. 하늘색: 누른 행 배경 #e6f4fc, 그룹 헤더 왼쪽 #2b9fe0 짧은 인디케이터
- ex-modal-card: 기록 상세. 상단 시약명(heading-3) + 사용량(display) 요약 → 라벨-값 행(사용자 · 일시 · 메모) → 그 아래 msds-entry → button-outline "닫기". 모바일에서 상세 시트는 tab-bar 위쪽 선(y 780) 위에 붙는다. 하늘색 없음
- msds-entry: 상세 모달 안 button-pill-soft "MSDS 보기 ↗". 학생·교사·admin 모두. 하늘색: 바깥 화살표 아이콘 #2b9fe0(라벨 글자는 #141414)
- button-outline: 상세 모달 "닫기"
- ex-empty-state-card: 필터 결과 0건일 때 "아직 사용 기록이 없어요" 문구. 하늘색: 안내 아이콘 #2b9fe0
- tab-bar: 모바일 전용 하단 탭바 1개. 화면 아래 가장자리에 붙은 전폭 사각형 바(x 0, 폭 390, 높이 64, 위치 y 780~844, rounded 0). #ffffff 채움 + 위쪽에만 1px #f0f0f0 선, 그림자 없음, 화면 아래·좌우 띄움 없음(floating pill 아님). 안쪽 위아래 여백 8, 좌우 여백 0. 안에 tab-item 4개를 같은 폭으로 꽉 채워 둔다. 역할 무관 동일. 기록 목록 스크롤 영역은 tab-bar 위쪽 선에서 끝난다. 데스크탑 프레임에는 두지 않는다. 하늘색: 활성 tab-item의 #2b9fe0 아이콘만(바탕 채움 없음)
- tab-item: tab-bar 안 4개, 왼쪽부터 "홈"(화면 13) · "시약"(화면 2) · "QR 스캔"(화면 12) · "기록"(화면 10). 각 항목 = 같은 폭(390 ÷ 4) 사각형 누름 영역(rounded 0, 채움 없음, pill 없음), 높이 48(44 이상), 아이콘 위 + label(12/600) 아래, 아이콘과 라벨 사이 4. 이 화면의 활성 = "기록": #2b9fe0 아이콘 + 라벨 #141414, 뒤 바탕 없음. 비활성 3개("홈"·"시약"·"QR 스캔"): 아이콘·라벨 #707070
### 반영한 레퍼런스
- https://uibowl.io/name/%ED%86%A0%EC%8A%A4%EC%A6%9D%EA%B6%8C?patterns=%EB%82%B4%EC%97%AD&patternName=%EA%B1%B0%EB%9E%98%EB%82%B4%EC%97%AD
- https://uibowl.io/name/%EB%AF%B8%EB%8B%88%EC%8A%A4%ED%83%81?patterns=%EB%82%B4%EC%97%AD&patternName=%EC%9B%90%ED%99%94%20%EA%B1%B0%EB%9E%98%EB%82%B4%EC%97%AD
- https://uibowl.io/name/%ED%86%A0%EC%8A%A4?patterns=%EB%82%B4%EC%97%AD&patternName=%EA%B1%B0%EB%9E%98%20%EC%83%81%EC%84%B8

## 화면 11
학생·교사·admin 모두 들어온다. 교사·admin은 문 형태·단 수·칸별 보관 분류를 편집하고, 학생은 배치도를 보기만 한다(학생 화면에는 cabinet-edit 영역·편집 컨트롤·저장 버튼이 없다). 같은 학교(샘플고등학교)의 시약장만 보인다.
예시 상태: "1번 시약장", 양문형 · 4단 → 좌/우 × 1~4단 = 8칸. 좌1단 = 산 + 염기(mix-warning 표시), 좌2단 = 유기, 좌3단 = 인화성, 좌4단 = 기타, 우1단 = 산화제, 우2단 = 무기염, 우3단 = 독성, 우4단 = 기타. 선택된 칸은 좌1단.
위→아래 순서: 제목 → (교사·admin) 문 형태·단 수 선택 → 배치도 → 범례 → 선택 칸의 분류 칩 → 주의사항(mix-warning) → 저장 → (모바일) tab-bar.
모바일 활성 탭: "시약". cabinet-edit 하단 전폭 "저장"은 tab-bar 바로 위로 올린다.
### 구성 요소
- nav-pill: "Lab_Stock" 워드마크 + 제목 "시약장 설정" + 현재 학교명 "샘플고등학교" 텍스트. 제목 아래 heading-3 "1번 시약장". 하늘색: 데스크탑 현재 섹션 링크("시약장 설정") 아래 #2b9fe0 밑줄 인디케이터(글자는 #141414)
- cabinet-edit: 편집 영역 전체를 감싸는 블록 1개. 안에 cabinet-door-select · cabinet-shelf-select · 선택 칸의 storage-class-chip 묶음 · mix-warning · 하단 전폭 button-primary "저장"이 들어간다. 학생 화면에는 이 블록이 없다 (교사·admin만)
- cabinet-door-select: cabinet-edit 맨 위, 문 형태 2옵션 pill "양문형 / 단문형"(rules.json cabinet.door_types), 한 번에 하나만 선택. 고르면 아래 배치도의 열 수가 즉시 바뀐다(양문형 = 좌·우 2열, 단문형 = 1열). 예시 상태 "양문형" 선택. 하늘색: 선택 옵션 배경 #e6f4fc + 1px #2b9fe0 테두리(글자는 #141414), 미선택은 #f3f3f3 채움·#707070 글자 (교사·admin만)
- cabinet-shelf-select: cabinet-door-select 바로 아래, 단 수 2옵션 pill "3단 / 4단"(rules.json cabinet.shelves), 한 번에 하나만 선택. 고르면 배치도의 행 수가 즉시 바뀐다. 예시 상태 "4단" 선택. 하늘색: 선택 옵션 배경 #e6f4fc + 1px #2b9fe0 테두리(글자는 #141414) (교사·admin만)
- cabinet-slot: 시약장 정면 배치도의 칸 1개. 배치도 = 왼쪽에 단 라벨(caption "1단"~"4단"), 위쪽에 문 라벨(caption "좌" / "우"), 양문형이면 좌·우 묶음 사이를 가운데 통로처럼 비운다. 칸은 같은 크기 격자(#f3f3f3 채움, rounded 16), 칸 안에 지정된 분류 이름(label, #141414)을 적고, 분류가 없으면 caption "미지정"(#707070). 예시 상태 8칸. 교사·admin은 칸을 눌러 선택하고, 학생에게는 같은 배치도가 보기 전용으로 보인다(누름 동작 없음). 산 + 염기가 지정된 좌1단 칸에는 #141414 경고 아이콘을 칸 오른쪽 위에 둔다. 하늘색: 선택된 칸 배경 #e6f4fc + 2px #2b9fe0 테두리(글자는 #141414)
- storage-class-chip: 보관 분류 칩 8종 "유기·산·염기·산화제·인화성·무기염·독성·기타"(rules.json cabinet.storage_classes). cabinet-edit 안에서 선택된 칸(좌1단)의 분류를 고르는 칩 묶음, 두 줄 배치, 한 칸에 여러 개 선택 가능. 예시 상태 "산"·"염기" 선택. 칩 = rounded 9999, label 크기, 미선택 #f3f3f3 채움. 배치도 아래 범례 한 줄(미지정 · 선택 칸)에도 같은 칩 모양을 보기 전용으로 쓴다(학생에게는 범례만 보인다). 하늘색: 선택된 칩 배경 #e6f4fc + 1px #2b9fe0 테두리(글자는 #141414)
- mix-warning: 칩 묶음과 저장 버튼 사이 구분 영역의 "주의사항" 목록. 같은 칸에 rules.json cabinet.incompatible 조합(산+염기, 산화제+인화성, 산화제+유기, 산+인화성, 독성+산)이 지정되면 핑크 신호로 경고한다(rules.json cabinet.warning_color #d6246a, 2026-10-02 사용자 결정). 핫핑크가 쨍하지 않도록 바탕은 연핑크 틴트 #fbe9f0(rules.json colors.accent_soft, docs/design.md Soft Pink — 흰 바탕 위 핑크 10%), 테두리 없음, rounded 16. 제목 heading-4 "주의사항"(#141414) + 줄마다 #d6246a 경고 아이콘 + #141414 body-sm 문구(#fbe9f0 위 대비 15.8:1). 예시 상태 1줄 "좌1단: 산과 염기는 섞이면 위험해요. 다른 칸에 나눠 보관하세요". 진한 핑크 #d6246a는 경고 아이콘에만 쓰고 글자·채움에는 쓰지 않는다. 하늘색은 쓰지 않는다. 학생 화면에도 배치도 아래에 같은 경고를 보기 전용으로 표시한다
- button-primary: cabinet-edit 하단 전폭 "저장". 모바일에서는 tab-bar 바로 위(버튼 아래 끝과 tab-bar 위쪽 선 사이 16)에 둔다. 하늘색 없음(#141414 채움) (교사·admin만)
- ex-toast: 저장 직후 "시약장 설정을 저장했어요" 알림. 하늘색: 완료 체크 아이콘 #2b9fe0 (교사·admin만)
- tab-bar: 모바일 전용 하단 탭바 1개. 화면 아래 가장자리에 붙은 전폭 사각형 바(x 0, 폭 390, 높이 64, 위치 y 780~844, rounded 0). #ffffff 채움 + 위쪽에만 1px #f0f0f0 선, 그림자 없음, 화면 아래·좌우 띄움 없음(floating pill 아님). 안쪽 위아래 여백 8, 좌우 여백 0. 안에 tab-item 4개를 같은 폭으로 꽉 채워 둔다. 역할 무관 동일(학생 화면에도 같은 tab-bar, 저장 버튼 없이 배치도·범례·주의사항 스크롤 영역이 이 바 위에서 끝난다). 데스크탑 프레임에는 두지 않는다. 하늘색: 활성 tab-item의 #2b9fe0 아이콘만(바탕 채움 없음)
- tab-item: tab-bar 안 4개, 왼쪽부터 "홈"(화면 13) · "시약"(화면 2) · "QR 스캔"(화면 12) · "기록"(화면 10). 각 항목 = 같은 폭(390 ÷ 4) 사각형 누름 영역(rounded 0, 채움 없음, pill 없음), 높이 48(44 이상), 아이콘 위 + label(12/600) 아래, 아이콘과 라벨 사이 4. 이 화면의 활성 = "시약": #2b9fe0 아이콘 + 라벨 #141414, 뒤 바탕 없음. 비활성 3개("홈"·"QR 스캔"·"기록"): 아이콘·라벨 #707070
### 반영한 레퍼런스
- https://uibowl.io/name/BookMyShow?patterns=%EC%98%88%EC%95%BD%C2%B7%EA%B2%B0%EC%A0%9C&patternName=3.%EC%A2%8C%EC%84%9D%20%EC%84%A0%ED%83%9D
- https://uibowl.io/name/Frontier%20Airlines?patterns=%EC%98%88%EC%95%BD%C2%B7%EA%B2%B0%EC%A0%9C&patternName=%EC%A2%8C%EC%84%9D%20%EC%84%A0%ED%83%9D
- https://uibowl.io/name/%ED%85%8C%EC%8A%AC%EB%9D%BC%20(Tesla)?patterns=%EC%A0%9C%EC%96%B4&patternName=%EC%B0%A8%EB%9F%89%EC%BB%A8%ED%8A%B8%EB%A1%A4
- https://uibowl.io/name/LG%20ThinQ?patterns=%EC%A0%9C%EC%96%B4&patternName=%EA%B1%B4%EC%A1%B0%EA%B8%B0
- https://uibowl.io/name/G%20car?patterns=%EC%8B%A0%EC%B2%AD%ED%95%98%EA%B8%B0&imgId=cmo85af8n00fcjr04s5erd4yk

## 화면 12
학생·교사·admin 모두 들어온다. 샘플고등학교 시약장 QR만 연다. 다른 학교 QR은 열지 않고 안내만 한다(N1).
위→아래 순서: 상단 바(닫기 · 플래시) → 탭 "QR 스캔 / 번호로 찾기" → 안내 2줄 → 카메라 프레임 → 실패 안내 줄 → 하단 고정 "시약장 번호로 찾기" → (모바일) tab-bar. tab-bar는 카메라 미리보기 영역 아래에 두고 카메라 영역과 겹치지 않는다.
모바일 활성 탭: "QR 스캔". 하단 고정 "시약장 번호로 찾기"와 "번호로 찾기" 탭의 하단 전폭 "찾기"는 tab-bar 바로 위로 올린다.
### 구성 요소
- nav-pill: 닫기(이전 화면) + 제목 "QR 스캔" + 현재 학교명 "샘플고등학교" 텍스트. 하늘색: 닫기 아이콘 #2b9fe0, 데스크탑 현재 섹션 링크("QR 스캔") 아래 #2b9fe0 밑줄 인디케이터
- segmented-control: nav-pill 아래 "QR 스캔 / 번호로 찾기" 두 탭, 한 번에 하나만 선택. 기본은 "QR 스캔". 선택된 탭은 segmented-control-active
- segmented-control-active: 선택된 탭 흰 pill. 하늘색: 1px #2b9fe0 테두리(글자는 #141414)
- qr-scan: "QR 스캔" 탭 본문. 상단 안내 heading-4 "시약장 문에 붙은 QR을 맞춰주세요" + body-sm(#707070) "카메라는 시약장 QR을 읽는 데만 사용해요". 가운데 카메라 미리보기 영역(#262626 채움, rounded 24) 안에 1:1 코너 브라켓 프레임(#ffffff 선). 딤·반투명 덮개는 쓰지 않는다. 프레임 아래 button-pill-soft "플래시". 카메라 권한이 없으면 미리보기 영역 자리에 #f3f3f3 채움 + #141414 문구 "카메라 권한이 필요해요" + button-outline "권한 설정"을 둔다. 인식 실패·다른 학교 QR이면 별도 화면 없이 미리보기 영역 아래 #ffffff 바탕에 #141414 경고 아이콘 + #141414 body 1줄("QR을 읽지 못했어요. 시약장 번호로 찾아보세요" / "샘플고등학교 시약장 QR이 아니에요")을 표시하고 아래 qr-manual-entry로 안내한다. 스캔 성공 → 아래 ex-modal-card 결과 시트. 모바일에서 카메라 미리보기 영역은 tab-bar 위쪽에서 끝난다. 하늘색: 인식 중 상태의 프레임 선 #2b9fe0
- qr-manual-entry: 두 곳. ① 화면 최하단 고정 button-outline "시약장 번호로 찾기"(누르면 "번호로 찾기" 탭으로 전환, 모바일에서는 tab-bar 바로 위). ② "번호로 찾기" 탭 본문: 라벨 "시약장 번호" + text-input(플레이스홀더 "예: 1") + 하단 전폭 button-primary "찾기"(비어 있으면 비활성, 모바일에서는 tab-bar 바로 위). 없는 번호면 입력 아래 #141414 아이콘 + #141414 body-sm "샘플고등학교에 이 번호의 시약장이 없어요". 찾으면 아래 ex-modal-card 결과 시트. 하늘색: 입력 왼쪽 검색 아이콘 #2b9fe0
- text-input: qr-manual-entry의 "시약장 번호" 입력. 포커스 링은 #141414
- ex-modal-card: 스캔·번호 찾기 결과 바텀시트. heading-3 "1번 시약장" + caption "양문형 · 4단" → 이 시약장의 reagent-row 목록 → 행을 누르면 시약 상세(화면 3)로, 시트 하단 button-outline "배치도 보기"는 화면 11로 간다. 첫 행 아래 msds-entry. 테두리 1px #e0e0e0, 그림자·딤 없음. 모바일에서 결과 시트는 tab-bar 위쪽 선(y 780) 위에 붙는다
- reagent-row: 결과 시트의 시약 한 줄 = 시약명(title) + 재고량·단위(body) + 칸 위치 caption("좌1단"). 재고가 기준 미만이면 행 안에 badge-low-stock(화면 2와 같은 규칙). 하늘색: 누른 행 배경 #e6f4fc
- badge-low-stock: reagent-row 안 "재고 부족" 칩(#d6246a 채움, #ffffff 글자). 하늘색 없음
- msds-entry: 결과 시트 안 button-pill-soft "MSDS 보기 ↗". 학생·교사·admin 모두. 하늘색: 바깥 화살표 아이콘 #2b9fe0(라벨 글자는 #141414)
- button-pill-soft: qr-scan "플래시", msds-entry "MSDS 보기 ↗"
- button-outline: 하단 고정 "시약장 번호로 찾기", 권한 상태 "권한 설정", 결과 시트 "배치도 보기"
- button-primary: "번호로 찾기" 탭 "찾기". 하늘색 없음
- tab-bar: 모바일 전용 하단 탭바 1개. 카메라 미리보기 영역과 하단 고정 "시약장 번호로 찾기" 아래, 화면 아래 가장자리에 붙은 전폭 사각형 바(x 0, 폭 390, 높이 64, 위치 y 780~844, rounded 0). #ffffff 채움 + 위쪽에만 1px #f0f0f0 선, 그림자 없음, 화면 아래·좌우 띄움 없음(floating pill 아님). 안쪽 위아래 여백 8, 좌우 여백 0. 안에 tab-item 4개를 같은 폭으로 꽉 채워 둔다(QR 스캔 탭을 키우지 않음). 역할 무관 동일. 데스크탑 프레임에는 두지 않는다. 하늘색: 활성 tab-item의 #2b9fe0 아이콘만(바탕 채움 없음)
- tab-item: tab-bar 안 4개, 왼쪽부터 "홈"(화면 13) · "시약"(화면 2) · "QR 스캔"(화면 12) · "기록"(화면 10). 각 항목 = 같은 폭(390 ÷ 4) 사각형 누름 영역(rounded 0, 채움 없음, pill 없음), 높이 48(44 이상), 아이콘 위 + label(12/600) 아래, 아이콘과 라벨 사이 4. 이 화면의 활성 = "QR 스캔": #2b9fe0 아이콘 + 라벨 #141414, 뒤 바탕 없음. 비활성 3개("홈"·"시약"·"기록"): 아이콘·라벨 #707070
### 반영한 레퍼런스
- https://uibowl.io/name/%EC%B9%B4%EC%B9%B4%EC%98%A4T?patterns=%EC%B4%AC%EC%98%81%ED%95%98%EA%B8%B0&patternName=QR%EC%8A%A4%EC%BA%94-%EC%9E%90%EC%A0%84%EA%B1%B0%20%EB%B0%98%EB%82%A9
- https://uibowl.io/name/%EB%B3%BC%ED%8A%B8%EC%97%85?patterns=%EC%B4%AC%EC%98%81%ED%95%98%EA%B8%B0&patternName=QR%EC%8A%A4%EC%BA%94
- https://uibowl.io/name/%EB%A7%88%EB%AF%B8%ED%86%A1?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&imgId=cmpcmrk8h01s0jl04xuxmaavu
- https://uibowl.io/name/%EB%8B%A5%ED%84%B0%EB%8B%A4%EC%9D%B4%EC%96%B4%EB%A6%AC?patterns=%EC%B4%AC%EC%98%81%ED%95%98%EA%B8%B0&imgId=cmr7e4uyx00diju04jj009eeh
- https://uibowl.io/name/%EB%B9%BD%EB%8B%A4%EB%B0%A9?patterns=%EC%BF%A0%ED%8F%B0&imgId=cmsqw7eev001si604q3io8gzt

## 역할별 노출
앱 전체(화면 1~13) 기준 개수. runs/20261002-1416 표를 그대로 쓴다. 이번 run은 화면 2~12 모바일에 tab-bar·tab-item만 더했고, tab-bar·tab-item은 역할 무관 동일하며 표의 컴포넌트를 담지 않으므로 숫자는 바뀌지 않는다.
manual-upload = 화면 6 진입 버튼 1 + 화면 5 업로드 영역 1. reorder-alert-card = 화면 6 1 + 홈 카드 1 (교사·admin). vendor-register = 화면 6 버튼 1 + 화면 9 블록 1 (admin만). msds-entry = 화면 3 1 + 화면 10 상세 1 + 화면 12 결과 시트 1. stock-intake = 화면 7 1 + 홈 quick-action 1 (교사·admin). reagent-register = 화면 7 (교사·admin). user-manage = 화면 8 1 + 홈 quick-action 1 (admin만). cabinet-edit = 화면 11 1 + 홈 빈 상태 "시약장 추가" 1 (교사·admin, 학생은 배치도 보기만).

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
