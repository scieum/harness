# S1 채택 항목 — run 20261001-1827

구조·흐름·배치만 가져온다. 색·폰트·모서리는 docs/design.md를 따른다.

## 화면 2
| # | ui_url | 가져올 것 |
|---|---|---|
| 1 | https://uibowl.io/name/%EB%A9%94%EB%94%94%EC%BD%94%EC%B9%98?patterns=%EA%B2%80%EC%83%89&imgId=cms8e8sdi0007jm044by8323r | 상단 검색 바 + 행마다 시약명 1줄·보조 정보(재고량·입고일) 1줄의 2줄 리스트 행 구조 |
| 2 | https://uibowl.io/name/%EC%BF%A0%ED%8C%A1?patterns=%EB%A9%94%EC%9D%B8&imgId=pujxwsmnkvc7nav05jzqks8l | 재고 부족 상태를 행 안 이름 옆 배지(badge-low-stock)로 "잔여 N" 수치와 함께 붙이는 배치 |
| 3 | https://uibowl.io/name/%ED%81%AC%EB%AA%BD?patterns=%EC%B1%84%ED%8C%85&imgId=cmopsvj79001xjm04tk8cii2l | 리스트 위 필터 칩(전체/재고 부족) → 검색 바 → 리스트 순서의 상단 영역 배치 |
| 4 | https://uibowl.io/name/%EC%9A%B0%EB%A6%AC%EB%8F%99%EB%84%A4GS?patterns=%EC%A1%B0%ED%9A%8C%ED%95%98%EA%B8%B0&patternName=%EC%9E%AC%EA%B3%A0%EC%B0%BE%EA%B8%B0 | 검색 → 품목 리스트 → 행 탭 시 상세(화면 3)로 이동하는 조회 흐름 |

## 화면 3
| # | ui_url | 가져올 것 |
|---|---|---|
| 1 | https://uibowl.io/name/%EB%8B%AC%EB%8B%A4%EB%B0%A9?patterns=%EC%83%81%EC%84%B8%EC%A0%95%EB%B3%B4%20%28PDP%29&patternName=%EC%83%81%ED%92%88 | 상단 요약(시약명·현재 재고) 아래 탭/테이블로 입고일·사용 기록·사용자 속성을 나눠 정리하는 구조 |
| 2 | https://uibowl.io/name/%EB%9F%BD%EB%A7%98?patterns=%EC%83%81%EC%84%B8%EC%A0%95%EB%B3%B4%20%28PDP%29&patternName=%EC%83%81%ED%92%88 | 상단 뒤로가기+제목 바, 본문 스크롤, 하단 고정 주요 액션 버튼(사용 기록) 배치 |
| 3 | https://uibowl.io/name/%ED%95%98%EB%82%98%EC%9B%90%ED%81%90?patterns=%EA%B0%84%ED%8E%B8%EA%B2%B0%EC%A0%9C&patternName=QR%EA%B2%B0%EC%A0%9C | MSDS QR을 독립 블록 중앙에 두고 바로 아래 설명 라벨을 붙이는 배치 (msds-entry) |
| 4 | https://uibowl.io/name/%EC%B9%B4%EC%B9%B4%EC%98%A4T?patterns=%EC%B4%AC%EC%98%81%ED%95%98%EA%B8%B0&patternName=QR%EC%8A%A4%EC%BA%94-%EC%9E%90%EC%A0%84%EA%B1%B0%20%EB%B0%98%EB%82%A9 | QR 외에 "MSDS 직접 열기" 같은 대체 경로를 QR 아래에 함께 두는 흐름 |

## 화면 6
| # | ui_url | 가져올 것 |
|---|---|---|
| 1 | https://uibowl.io/name/W%EC%BB%A8%EC%85%89?patterns=%EB%82%B4%EC%97%AD&patternName=%EC%9E%AC%EC%9E%85%EA%B3%A0%20%EC%95%8C%EB%A6%BC | 알림 카드(시약명·상태 배지·필요량 대비 재고) + 카드 하단 날짜·액션 버튼, 목록 아래 안내 아코디언 구조 |
| 2 | https://uibowl.io/name/%EB%8D%B0%EC%9D%BC%EB%A6%AC%EC%83%B7?patterns=%EC%8B%A0%EC%B2%AD%ED%95%98%EA%B8%B0&patternName=%EC%9E%AC%EC%9E%85%EA%B3%A0%20%EC%95%8C%EB%A6%BC | "판매처" 라벨-값 행(판매처명·부가 정보) 배치와 하단 고정 연결 버튼 → 확인 모달 흐름 |
| 3 | https://uibowl.io/name/%EB%8D%B0%EC%9D%BC%EB%A6%AC%EC%83%B7?patterns=%EB%82%B4%EC%97%AD&patternName=%EC%9E%AC%EC%9E%85%EA%B3%A0%20%EC%95%8C%EB%A6%BC%EB%82%B4%EC%97%AD | 상단 기준 안내 박스(재주문 기준 설명) + 알림 0건일 때 빈 화면 문구 배치 |
| 4 | https://uibowl.io/name/%EC%B9%A9%EC%8A%A4?patterns=%ED%91%B8%EC%8B%9C%EC%95%8C%EB%A6%BC | 알림 문구를 제목 1줄(시약명+부족) + 내용 1줄(필요량/현재량) + 시간으로 짜는 구조 |
