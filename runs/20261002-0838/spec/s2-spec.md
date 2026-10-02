# S2 설계 — run 20261002-0838

대상 화면: 2, 3, 6 · 학교: 샘플고등학교 (input.json)
이어지는 작업: runs/20261001-1910 (화면 1·4·5), 이전 설계 runs/20261001-1844 (화면 2·3·6, 하늘색 이전). 같은 컴포넌트 이름과 톤을 따른다.
근거: docs/PRD.md §3·§5·§7, docs/story-service.md 결정 사항, docs/design.md(2026-10-02 하늘색 강조색), research/s1-adopt.md
색·폰트·모서리·간격은 docs/design.md와 harness/rules.json을 따른다.
- 재고 부족 강조색 #d6246a는 badge-low-stock과 reorder-alert-card 안에서만 쓴다.
- 하늘색 #2b9fe0(선 굵기·인디케이터·아이콘)과 옅은 하늘색 #e6f4fc(선택 배경)는 선택 상태·활성 탭/세그먼트·링크 밑줄·진행·아이콘 강조에만 쓴다. 글자색으로 쓰지 않고(하늘색 위 글자는 #141414), badge-low-stock·reorder-alert-card·button-primary 안에는 쓰지 않는다.
학교 선택(school-select)은 화면 1에만 있다. 화면 2·3·6에는 학교 선택을 두지 않고 nav-pill 안에 현재 학교명 "샘플고등학교"를 표시한다.
외부 서비스 연결 값은 서버에서만 다룬다. 어떤 화면에도 연결 값 입력·외부 서비스 설정·AI 엔진 선택 UI를 두지 않는다.
괄호 안 역할 표시가 없는 구성 요소는 학생·교사·admin 모두에게 보인다.

## 화면 2
### 구성 요소
- nav-pill: "Lab_Stock" 워드마크와 현재 학교명 "샘플고등학교" 텍스트. 데스크탑에서는 섹션 링크("시약 목록", 교사·admin에게만 "재주문 알림")가 함께 보이고, 모바일에서는 워드마크·학교명만 남긴다. 학교 전환 기능은 두지 않는다. 하늘색: 현재 섹션 링크("시약 목록") 아래 #2b9fe0 밑줄 인디케이터(글자는 #141414)
- segmented-control: 리스트 위 필터 "전체 / 재고 부족" 두 옵션, 한 번에 하나만 선택. 선택된 옵션은 segmented-control-active
- segmented-control-active: 선택된 필터 옵션의 흰 pill. 하늘색: 1px #2b9fe0 테두리로 선택 상태 표시(글자는 #141414)
- text-input: 필터 아래 시약명 검색 바. 플레이스홀더 "시약명 검색". 하늘색: 바 왼쪽 검색 아이콘 #2b9fe0. 포커스 링은 design.md대로 #141414
- reagent-row: 시약 한 줄 = 1행 시약명(title) + 2행 보조 정보(재고량·단위, 입고일 caption). 행을 탭하면 화면 3으로 이동. 행 사이 간격 12. 하늘색: 오른쪽 이동 화살표 아이콘 #2b9fe0, 누른 상태의 행 배경 #e6f4fc. 재고 부족 행의 배지 안에는 하늘색을 쓰지 않는다
- badge-low-stock: 재고가 필요량보다 적은 시약 행에서 시약명 옆에 "재고 부족" 라벨. 잔여 수치는 같은 행 2행의 재고량으로 보여준다. 하늘색 없음
- ex-empty-state-card: 검색 결과가 0건이거나 "재고 부족" 필터 결과가 0건일 때 안내 문구. 하늘색: 안내 아이콘 #2b9fe0
### 반영한 레퍼런스
- https://uibowl.io/name/%EB%A9%94%EB%94%94%EC%BD%94%EC%B9%98?patterns=%EA%B2%80%EC%83%89&imgId=cms8e8sdi0007jm044by8323r
- https://uibowl.io/name/%EC%BF%A0%ED%8C%A1?patterns=%EB%A9%94%EC%9D%B8&imgId=pujxwsmnkvc7nav05jzqks8l
- https://uibowl.io/name/%ED%81%AC%EB%AA%BD?patterns=%EC%B1%84%ED%8C%85&imgId=cmopsvj79001xjm04tk8cii2l
- https://uibowl.io/name/%EC%9A%B0%EB%A6%AC%EB%8F%99%EB%84%A4GS?patterns=%EC%A1%B0%ED%9A%8C%ED%95%98%EA%B8%B0&patternName=%EC%9E%AC%EA%B3%A0%EC%B0%BE%EA%B8%B0

## 화면 3
### 구성 요소
- nav-pill: 뒤로가기(화면 2) + 제목 "시약 상세" + 현재 학교명 "샘플고등학교" 텍스트. 학교 전환 기능은 두지 않는다. 하늘색: 뒤로가기 아이콘 #2b9fe0
- reagent-detail-card: 상단 요약. 시약명(title), 현재 재고량(display) + 단위, 입고일 라벨-값(caption 라벨). 하늘색 없음(재고 부족 배지가 들어가는 카드라 중립 유지)
- badge-low-stock: 재고가 필요량보다 적을 때만 reagent-detail-card 안 시약명 옆에 "재고 부족". 하늘색 없음
- segmented-control: 요약 아래 "정보 / 사용 기록" 두 탭, 활성 탭은 하나. 선택된 탭은 segmented-control-active
- segmented-control-active: 활성 탭의 흰 pill. 하늘색: 활성 탭 아래 #2b9fe0 인디케이터(글자는 #141414)
- ex-data-table-cell: "정보" 탭은 시약 속성(입고일 등) 라벨-값 표, "사용 기록" 탭은 사용 날짜·사용자·사용량 3열 표. 하늘색: 가장 최근 사용 기록 행 배경 #e6f4fc
- msds-entry: msds-qr-tile(MSDS QR 1:1을 독립 블록 중앙에, 바로 아래 설명 라벨 "QR로 MSDS 열기") + 그 아래 대체 경로 button-pill-soft "MSDS 보기 ↗". 학생·교사·admin 모두에게 1개. 하늘색: "MSDS 보기 ↗"의 바깥 화살표 아이콘 #2b9fe0(라벨 글자는 #141414). QR 이미지 자체는 흑백 유지
- button-primary: 하단 고정 "사용 기록" → 화면 4. 학생·교사·admin 모두. 하늘색 없음(#141414 채움)
- button-outline: 하단 고정 버튼 옆 "입고" (교사·admin만, 학생 화면에는 없음)
### 반영한 레퍼런스
- https://uibowl.io/name/%EB%8B%AC%EB%8B%A4%EB%B0%A9?patterns=%EC%83%81%EC%84%B8%EC%A0%95%EB%B3%B4%20%28PDP%29&patternName=%EC%83%81%ED%92%88
- https://uibowl.io/name/%EB%9F%BD%EB%A7%98?patterns=%EC%83%81%EC%84%B8%EC%A0%95%EB%B3%B4%20%28PDP%29&patternName=%EC%83%81%ED%92%88
- https://uibowl.io/name/%ED%95%98%EB%82%98%EC%9B%90%ED%81%90?patterns=%EA%B0%84%ED%8E%B8%EA%B2%B0%EC%A0%9C&patternName=QR%EA%B2%B0%EC%A0%9C
- https://uibowl.io/name/%EC%B9%B4%EC%B9%B4%EC%98%A4T?patterns=%EC%B4%AC%EC%98%81%ED%95%98%EA%B8%B0&patternName=QR%EC%8A%A4%EC%BA%94-%EC%9E%90%EC%A0%84%EA%B1%B0%20%EB%B0%98%EB%82%A9

## 화면 6
이 화면은 교사·admin만 들어온다. 학생 nav에는 진입 링크가 없다(학생 노출 0).
### 구성 요소
- nav-pill: "Lab_Stock" 워드마크 + 제목 "재주문 알림" + 현재 학교명 "샘플고등학교" 텍스트. 학교 전환 기능은 두지 않는다. 하늘색: 데스크탑 현재 섹션 링크("재주문 알림") 아래 #2b9fe0 밑줄 인디케이터 (교사·admin만)
- manual-upload: 알림 목록 위 재주문 기준 안내 박스(배경 #e6f4fc, 글자 #141414, "필요량 = 1반 1회 실험량 × 조 수") 끝의 button-pill-soft "실험 매뉴얼 올리기" → 화면 5. 하늘색: 안내 박스 배경 #e6f4fc와 정보 아이콘 #2b9fe0 (교사·admin만)
- reorder-alert-card: 알림 1건 = badge-low-stock "재고 부족" + 시약명(heading-4) 1줄 + "필요량 N / 현재 재고 M"(body) 1줄 + 알림 날짜(caption). 필요량은 1반 1회 실험량 × 조 수 기준임을 카드 안 보조 문구로 표시. 하늘색 없음 (교사·admin만)
- badge-low-stock: reorder-alert-card 안 "재고 부족" 라벨. 하늘색 없음 (교사·admin만)
- vendor-link: reorder-alert-card 하단 button-primary "판매처 연결". 카드 안이라 하늘색 없음 (교사·admin만)
- ex-modal-card: vendor-link를 누르면 뜨는 확인 모달. "판매처" 라벨-값 행(판매처명·부가 정보) + button-outline "취소" + button-primary "확인". 하늘색: 선택된 판매처 행 배경 #e6f4fc + 왼쪽 #2b9fe0 선택 표시 (교사·admin만)
- vendor-register: 목록 아래 button-outline "판매처 등록" (admin만, 교사 화면에는 없음)
- ex-empty-state-card: 알림이 0건일 때 "재고가 부족한 시약이 없어요" 문구. 하늘색: 안내 아이콘 #2b9fe0 (교사·admin만)
### 반영한 레퍼런스
- https://uibowl.io/name/W%EC%BB%A8%EC%85%89?patterns=%EB%82%B4%EC%97%AD&patternName=%EC%9E%AC%EC%9E%85%EA%B3%A0%20%EC%95%8C%EB%A6%BC
- https://uibowl.io/name/%EB%8D%B0%EC%9D%BC%EB%A6%AC%EC%83%B7?patterns=%EC%8B%A0%EC%B2%AD%ED%95%98%EA%B8%B0&patternName=%EC%9E%AC%EC%9E%85%EA%B3%A0%20%EC%95%8C%EB%A6%BC
- https://uibowl.io/name/%EB%8D%B0%EC%9D%BC%EB%A6%AC%EC%83%B7?patterns=%EB%82%B4%EC%97%AD&patternName=%EC%9E%AC%EC%9E%85%EA%B3%A0%20%EC%95%8C%EB%A6%BC%EB%82%B4%EC%97%AD
- https://uibowl.io/name/%EC%B9%A9%EC%8A%A4?patterns=%ED%91%B8%EC%8B%9C%EC%95%8C%EB%A6%BC

## 역할별 노출
앱 전체(화면 1~6, runs/20261001-1910 설계 포함) 기준 개수. manual-upload는 화면 6 진입 버튼 1 + 화면 5 업로드 영역 1.

| 컴포넌트 | 학생 | 교사 | admin |
|---|---|---|---|
| manual-upload | 0 | 2 | 2 |
| reorder-alert-card | 0 | 1 | 1 |
| vendor-link | 0 | 1 | 1 |
| vendor-register | 0 | 0 | 1 |
| msds-entry | 1 | 1 | 1 |
