# S2 설계 — run 20261001-1827

대상 화면: 2, 3, 6 · 학교명: 샘플고등학교
구조·흐름·배치만 레퍼런스에서 가져온다. 색·폰트·모서리·간격은 docs/design.md를 따른다.
모바일(390×844)은 단일 열, 데스크탑(1440×900)은 같은 구성 요소를 가운데 정렬 본문 폭 안에 배치한다.
화면 2·3·6에는 학교를 고르는 요소를 두지 않고, nav-pill 안에 현재 학교명 "샘플고등학교"만 표시한다.

## 화면 2
### 구성 요소
- nav-pill: 상단 고정. 왼쪽 "Lab_Stock" 로고 + 현재 학교명 "샘플고등학교" 텍스트(표시만, 변경 불가). 데스크탑은 섹션 링크 "시약 목록"·"재주문 알림"(교사·admin에게만), 모바일은 로고 + 학교명으로 축소
- segmented-control: 리스트 위 필터 2개 "전체" / "재고 부족" (활성 항목은 segmented-control-active)
- text-input: 필터 아래 시약명 검색 바 (placeholder "시약 이름 검색")
- reagent-row: 행마다 1줄 시약명(title) + 2줄 재고량·단위(body), 입고일(caption, muted). 행 탭 시 화면 3으로 이동. 행 간격 12px
- badge-low-stock: 재고가 1반 1회 필요량보다 적은 reagent-row의 시약명 옆에 "재고 부족" 표시
- ex-empty-state-card: 검색 결과 0건 또는 "재고 부족" 필터 결과 0건일 때 안내 문구
### 반영한 레퍼런스
- https://uibowl.io/name/%EB%A9%94%EB%94%94%EC%BD%94%EC%B9%98?patterns=%EA%B2%80%EC%83%89&imgId=cms8e8sdi0007jm044by8323r
- https://uibowl.io/name/%EC%BF%A0%ED%8C%A1?patterns=%EB%A9%94%EC%9D%B8&imgId=pujxwsmnkvc7nav05jzqks8l
- https://uibowl.io/name/%ED%81%AC%EB%AA%BD?patterns=%EC%B1%84%ED%8C%85&imgId=cmopsvj79001xjm04tk8cii2l
- https://uibowl.io/name/%EC%9A%B0%EB%A6%AC%EB%8F%99%EB%84%A4GS?patterns=%EC%A1%B0%ED%9A%8C%ED%95%98%EA%B8%B0&patternName=%EC%9E%AC%EA%B3%A0%EC%B0%BE%EA%B8%B0

## 화면 3
### 구성 요소
- nav-pill: 상단 바. 뒤로가기(화면 2) + 제목 "시약 상세" + 현재 학교명 "샘플고등학교" 텍스트(표시만)
- reagent-detail-card: 상단 요약. 시약명(heading-3), 현재 재고량(display) + 단위, 입고일(caption, muted)
- badge-low-stock: 재고가 필요량보다 적을 때 reagent-detail-card 안 시약명 옆에 "재고 부족" 표시
- segmented-control: 요약 아래 탭 2개 "사용 기록" / "입고 기록" (활성 항목은 segmented-control-active)
- ex-data-table-cell: 선택한 탭의 표. 열 = 날짜 · 사용자 · 수량
- msds-entry: MSDS 진입 블록. msds-qr-tile(QR 1:1, 블록 중앙) + 바로 아래 설명 라벨 "QR을 스캔하면 MSDS가 열려요" + 대체 경로 button-pill-soft "MSDS 보기 ↗". 학생·교사·admin 모두에게 표시
- button-primary: 하단 고정 "사용 기록" (화면 4로 이동). 모든 역할에게 표시
- button-outline: button-primary 옆 "입고". 교사·admin에게만 표시 (PRD §3 교사 권한)
### 반영한 레퍼런스
- https://uibowl.io/name/%EB%8B%AC%EB%8B%A4%EB%B0%A9?patterns=%EC%83%81%EC%84%B8%EC%A0%95%EB%B3%B4%20%28PDP%29&patternName=%EC%83%81%ED%92%88
- https://uibowl.io/name/%EB%9F%BD%EB%A7%98?patterns=%EC%83%81%EC%84%B8%EC%A0%95%EB%B3%B4%20%28PDP%29&patternName=%EC%83%81%ED%92%88
- https://uibowl.io/name/%ED%95%98%EB%82%98%EC%9B%90%ED%81%90?patterns=%EA%B0%84%ED%8E%B8%EA%B2%B0%EC%A0%9C&patternName=QR%EA%B2%B0%EC%A0%9C
- https://uibowl.io/name/%EC%B9%B4%EC%B9%B4%EC%98%A4T?patterns=%EC%B4%AC%EC%98%81%ED%95%98%EA%B8%B0&patternName=QR%EC%8A%A4%EC%BA%94-%EC%9E%90%EC%A0%84%EA%B1%B0%20%EB%B0%98%EB%82%A9

## 화면 6
### 구성 요소
- nav-pill: 상단 바. 제목 "재주문 알림" + 현재 학교명 "샘플고등학교" 텍스트(표시만). 교사·admin에게만 이 화면 진입 링크가 보임 (학생에게는 화면 6 없음)
- reorder-alert-card: 알림 1건 = 카드 1장. badge-low-stock + 1줄 시약명(heading-4) + 2줄 "필요량 N / 현재 M"(body, 1반 1회 실험 필요량 기준) + 판매처 라벨-값 행(판매처명) + 카드 하단 날짜(caption, muted)
- badge-low-stock: reorder-alert-card 안 시약명 앞 "재고 부족"
- vendor-link: reorder-alert-card를 닫는 button-primary "판매처 연결". 누르면 확인 모달
- ex-modal-card: vendor-link 확인 모달. 판매처명 표시 + button-primary "연결" / button-outline "취소"
- vendor-register: 목록 아래 button-outline "판매처 등록". admin에게만 표시
- ex-empty-state-card: 알림 0건일 때 "재고가 부족한 시약이 없어요" 문구
### 반영한 레퍼런스
- https://uibowl.io/name/W%EC%BB%A8%EC%85%89?patterns=%EB%82%B4%EC%97%AD&patternName=%EC%9E%AC%EC%9E%85%EA%B3%A0%20%EC%95%8C%EB%A6%BC
- https://uibowl.io/name/%EB%8D%B0%EC%9D%BC%EB%A6%AC%EC%83%B7?patterns=%EC%8B%A0%EC%B2%AD%ED%95%98%EA%B8%B0&patternName=%EC%9E%AC%EC%9E%85%EA%B3%A0%20%EC%95%8C%EB%A6%BC
- https://uibowl.io/name/%EB%8D%B0%EC%9D%BC%EB%A6%AC%EC%83%B7?patterns=%EB%82%B4%EC%97%AD&patternName=%EC%9E%AC%EC%9E%85%EA%B3%A0%20%EC%95%8C%EB%A6%BC%EB%82%B4%EC%97%AD
- https://uibowl.io/name/%EC%B9%A9%EC%8A%A4?patterns=%ED%91%B8%EC%8B%9C%EC%95%8C%EB%A6%BC

## 역할별 노출
| 컴포넌트 | 학생 | 교사 | admin |
|---|---|---|---|
| manual-upload | 0 | 0 | 0 |
| reorder-alert-card | 0 | 1 | 1 |
| vendor-link | 0 | 1 | 1 |
| vendor-register | 0 | 0 | 1 |
| msds-entry | 1 | 1 | 1 |
