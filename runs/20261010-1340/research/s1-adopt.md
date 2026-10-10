# S1 채택 — runs/20261010-1340

(구조·흐름·배치만 가져온다. 색·폰트·모서리는 design.md를 따른다.)

## 화면 3
| # | ui_url | 가져올 것 |
|---|---|---|
| 1 | https://uibowl.io/name/%EC%97%90%EC%9D%B4%EB%8B%B7?patterns=%ED%8E%B8%EC%A7%91%C2%B7%EC%88%98%EC%A0%95%ED%95%98%EA%B8%B0&patternName=%EC%B5%9C%EA%B7%BC%EA%B8%B0%EB%A1%9D%28%EC%82%AD%EC%A0%9C%29 | 상단 오른쪽 ⋯ 버튼 → 앵커 팝오버 메뉴, 삭제 항목은 메뉴 맨 아래 배치 |
| 2 | https://uibowl.io/name/%EC%BA%90%EC%8B%9C%EC%9B%8C%ED%81%AC?patterns=%ED%8E%B8%EC%A7%91%C2%B7%EC%88%98%EC%A0%95%ED%95%98%EA%B8%B0&patternName=%EA%B2%8C%EC%8B%9C%EA%B8%80%20%EC%82%AD%EC%A0%9C | 메뉴 → 확인 모달(취소 왼쪽·삭제 오른쪽 2버튼) → 완료 토스트 후 목록 복귀의 흐름 |
| 3 | https://uibowl.io/name/%EC%91%A5%EC%91%A5%EC%B0%B0%EC%B9%B5?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&patternName=%EC%9D%BC%EA%B8%B0%2F%EC%88%98%EC%9C%A0%ED%85%80%20%ED%83%AD%20-%20%EC%88%98%EC%9C%A0%ED%85%80%20-%20%EB%82%B4%EC%97%AD%EC%82%AD%EC%A0%9C | 모달 본문에 대상 이름 + '되돌릴 수 없음' 안내 한 줄을 제목 아래 배치 |

## 화면 4
| # | ui_url | 가져올 것 |
|---|---|---|
| 1 | https://uibowl.io/name/%EB%A1%AF%EB%8D%B0%EB%B0%B1%ED%99%94%EC%A0%90?patterns=%EA%B2%80%EC%83%89&imgId=b3qcqg4mcd3ehb8r9e2ywhjt | 담기 바텀시트 = 위 검색 입력 + 이름 왼쪽·체크박스 오른쪽 행 목록 + 아래 고정 확인 버튼(선택 개수 표기) |
| 2 | https://uibowl.io/name/%EB%9D%BC%EC%9A%B4%EC%A6%88?patterns=%EC%9E%A5%EB%B0%94%EA%B5%AC%EB%8B%88&imgId=cmunlyn8s0005l804bcsbpzcr | 담은 목록 행 구성 = 시약명·단위 + 오른쪽 위 행 삭제 X + 행 아래 수량 입력, 행 아래 오류 문구 자리 확보 |
| 3 | https://uibowl.io/name/%EA%B3%A8%ED%94%84%EC%A1%B4?patterns=%EC%9E%A5%EB%B0%94%EA%B5%AC%EB%8B%88&imgId=cmunkg4m30025l904yg6x2ysv | 하단 고정 저장 바 = 왼쪽 요약(담은 N개) + 오른쪽 'N개 저장' 주 버튼, 목록 스크롤과 분리 |
| 4 | https://uibowl.io/name/%EC%B9%B4%EC%B9%B4%EC%98%A4%EA%B3%A8%ED%94%84%EC%98%88%EC%95%BD?patterns=%EA%B2%80%EC%83%89&imgId=cmtwluex6011ijl043f9n1umq | 학년·반 입력 바로 아래 '최근' 라벨 + 가로 스크롤 칩 줄, 칩 하나에 학년·반·수업 조합을 함께 표기 |

## 화면 10
| # | ui_url | 가져올 것 |
|---|---|---|
| 1 | https://uibowl.io/name/%EB%AF%B8%EB%8B%88%EC%8A%A4%ED%83%81?patterns=%EB%82%B4%EC%97%AD&patternName=%EC%A3%BC%EB%AC%B8%EB%82%B4%EC%97%AD | 삭제된 시약 기록은 목록에 남기고 이름 취소선 + '삭제된 시약' 보조 라벨로 표시, 날짜 구분 헤더 유지 |
| 2 | https://uibowl.io/name/%EC%B9%B4%EC%B9%B4%EC%98%A4%EA%B3%A8%ED%94%84%EC%98%88%EC%95%BD?patterns=%EB%82%B4%EC%97%AD&patternName=%EB%82%98%EC%9D%98%EC%98%88%EC%95%BD%20-%20%EC%98%88%EC%95%BD%EB%82%B4%EC%97%AD%ED%83%AD | 목록 위 반·수업 필터 칩 줄 + 드롭다운, 필터 결과 0건이면 아이콘·안내 2줄 빈 상태 |
| 3 | https://uibowl.io/name/%ED%8F%B4%EC%84%BC%ED%8A%B8?patterns=%EC%95%8C%EB%A6%BC&patternName=%EC%95%8C%EB%A6%BC%20%EB%82%B4%EC%97%AD | 기록 행에 부가 정보(학년·반·수업)를 시약명 아래 보조 줄로 배치, 가로 스크롤 필터 칩 |
