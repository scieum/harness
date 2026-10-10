# S1 레퍼런스 — runs/20261010-1340

주제: 개발 세션 요청 6 — 여러 시약 한 번에 사용 기록(화면 4), 시약 삭제(화면 3·10), 수업 기록(화면 4·10)

## 화면 3
| # | 앱 | ui_url | 화면 설명 |
|---|---|---|---|
| 1 | 에이닷 | https://uibowl.io/name/%EC%97%90%EC%9D%B4%EB%8B%B7?patterns=%ED%8E%B8%EC%A7%91%C2%B7%EC%88%98%EC%A0%95%ED%95%98%EA%B8%B0&patternName=%EC%B5%9C%EA%B7%BC%EA%B8%B0%EB%A1%9D%28%EC%82%AD%EC%A0%9C%29 | 항목 오른쪽 세로 점(⋮)을 누르면 고정·이름 변경·삭제 팝오버 메뉴가 뜨고, 삭제는 맨 아래에 놓인 뒤 확인 모달로 이어지는 흐름 |
| 2 | 캐시워크 | https://uibowl.io/name/%EC%BA%90%EC%8B%9C%EC%9B%8C%ED%81%AC?patterns=%ED%8E%B8%EC%A7%91%C2%B7%EC%88%98%EC%A0%95%ED%95%98%EA%B8%B0&patternName=%EA%B2%8C%EC%8B%9C%EA%B8%80%20%EC%82%AD%EC%A0%9C | 게시글 더보기 메뉴 → 삭제 확인 모달(취소/삭제 2버튼) → 삭제 완료 토스트로 끝나는 4단계 흐름 |
| 3 | 쑥쑥찰칵 | https://uibowl.io/name/%EC%91%A5%EC%91%A5%EC%B0%B0%EC%B9%B5?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&patternName=%EC%9D%BC%EA%B8%B0%2F%EC%88%98%EC%9C%A0%ED%85%80%20%ED%83%AD%20-%20%EC%88%98%EC%9C%A0%ED%85%80%20-%20%EB%82%B4%EC%97%AD%EC%82%AD%EC%A0%9C | 기록 상세에서 삭제 진입 → 중앙 모달로 되돌릴 수 없음을 안내하고 확인 후 목록으로 복귀하는 기록 삭제 흐름 |

## 화면 4
| # | 앱 | ui_url | 화면 설명 |
|---|---|---|---|
| 1 | 롯데백화점 | https://uibowl.io/name/%EB%A1%AF%EB%8D%B0%EB%B0%B1%ED%99%94%EC%A0%90?patterns=%EA%B2%80%EC%83%89&imgId=b3qcqg4mcd3ehb8r9e2ywhjt | 바텀시트 안에 항목명 왼쪽·체크박스 오른쪽인 세로 목록, 위에 분류 탭, 맨 아래 전체 폭 확인 버튼 고정 — 여러 개 골라 한 번에 확정 |
| 2 | 라운즈 | https://uibowl.io/name/%EB%9D%BC%EC%9A%B4%EC%A6%88?patterns=%EC%9E%A5%EB%B0%94%EA%B5%AC%EB%8B%88&imgId=cmunlyn8s0005l804bcsbpzcr | 담은 목록 각 행에 항목 정보·행 삭제(X)·수량 스텝퍼(− 1 +)가 있고, 화면 아래에 'N개 상품 주문하기' 고정 바 |
| 3 | 골프존 | https://uibowl.io/name/%EA%B3%A8%ED%94%84%EC%A1%B4?patterns=%EC%9E%A5%EB%B0%94%EA%B5%AC%EB%8B%88&imgId=cmunkg4m30025l904yg6x2ysv | 행 단위 카드(옵션 줄 + 수량 스텝퍼 + X), 하단 고정 바 왼쪽에 합계·오른쪽에 '총 0개 주문하기' 버튼 — 선택 개수가 버튼 문구에 반영 |
| 4 | 카카오골프예약 | https://uibowl.io/name/%EC%B9%B4%EC%B9%B4%EC%98%A4%EA%B3%A8%ED%94%84%EC%98%88%EC%95%BD?patterns=%EA%B2%80%EC%83%89&imgId=cmtwluex6011ijl043f9n1umq | 검색 바 바로 아래 '최근 검색' 라벨과 가로 스크롤 칩 줄(조건 조합이 한 칩에 함께 표기), 그 아래 추천 칩 |

## 화면 10
| # | 앱 | ui_url | 화면 설명 |
|---|---|---|---|
| 1 | 미니스탁 | https://uibowl.io/name/%EB%AF%B8%EB%8B%88%EC%8A%A4%ED%83%81?patterns=%EB%82%B4%EC%97%AD&patternName=%EC%A3%BC%EB%AC%B8%EB%82%B4%EC%97%AD | 주문 내역 목록 위 가로 칩 필터(드롭다운 칩 + 토글 칩), 월 구분 헤더, 취소된 건은 금액 취소선 + '구매취소' 보조 라벨로 목록에 남겨 표시 |
| 2 | 카카오골프예약 | https://uibowl.io/name/%EC%B9%B4%EC%B9%B4%EC%98%A4%EA%B3%A8%ED%94%84%EC%98%88%EC%95%BD?patterns=%EB%82%B4%EC%97%AD&patternName=%EB%82%98%EC%9D%98%EC%98%88%EC%95%BD%20-%20%EC%98%88%EC%95%BD%EB%82%B4%EC%97%AD%ED%83%AD | 탭 아래 아웃라인 칩 필터 줄 + '전체' 드롭다운, 결과 없을 때 아이콘·안내 2줄 빈 상태 |
| 3 | 폴센트 | https://uibowl.io/name/%ED%8F%B4%EC%84%BC%ED%8A%B8?patterns=%EC%95%8C%EB%A6%BC&patternName=%EC%95%8C%EB%A6%BC%20%EB%82%B4%EC%97%AD | 내역 상단 가로 스크롤 칩 필터(선택 칩 채움), 섹션별 카드 안에 개수 요약과 '해당하는 항목이 없어요' 빈 상태 |
