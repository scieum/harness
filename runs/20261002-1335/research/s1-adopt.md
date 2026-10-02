# S1 채택 항목 — run 20261002-1335

구조·흐름·배치만 가져온다. 색·폰트·모서리는 docs/design.md를 따른다.

## 화면 13
| # | ui_url | 가져올 것 |
|---|---|---|
| 1 | https://uibowl.io/name/%ED%8E%98%EC%9D%B4%EC%9B%8C%ED%81%AC?patterns=%EB%A9%94%EC%9D%B8 | 상단 한 줄 "학교명 + 알림", 그 아래 '최근 사용 기록' 카드에 3줄(시약명·사용자·시각)만 보여주고 카드 하단 '더 보기 >'로 사용 기록 화면 이동 |
| 2 | https://uibowl.io/name/%ED%8E%98%EC%9D%B4%ED%9E%88%EC%96%B4?patterns=%EB%A9%94%EC%9D%B8&patternName=%EB%82%98%EC%9D%98%20%EB%A7%A4%EC%9E%A5 | 첫 칸에 'QR 스캔'을 둔 4열 아이콘 바로가기 그리드(역할별로 항목 수가 달라짐), 그 아래 '시약장 요약 >' 섹션 제목 + 큰 숫자 + 세부 2행 박스 순서 |
| 3 | https://uibowl.io/name/%EC%9E%90%EB%A6%AC%ED%86%A1?patterns=%EB%A9%94%EC%9D%B8&patternName=%ED%99%88%28%EC%9E%84%EB%8C%80%EC%9D%B8%29 | 같은 홈 틀에서 역할(학생/교사/admin)마다 바로가기·카드 구성을 바꾸는 방식, 시약장 요약 카드는 합계 + 상태별 구간 막대 + 보조 수치 1줄, 시약장 0개면 빈 상태 + 추가 버튼 |
| 4 | https://uibowl.io/name/%EB%83%89%EC%9E%A5%EA%B3%A0%ED%84%B8%EA%B8%B0?patterns=%EA%B2%80%EC%83%89&patternName=%ED%99%88%ED%99%94%EB%A9%B4%20%EC%9E%AC%EB%A3%8C | 재고 부족 요약을 "재고 부족 N개" 문장 + 개수 배지로 맨 위에 두고, 바로 아래 부족 시약을 칩(시약명 · 남은 수량) 가로 줄로 나열해 누르면 상세로 이동 |
| 5 | https://uibowl.io/name/%ED%86%A0%EC%8A%A4?patterns=%EB%A9%94%EC%9D%B8&imgId=cmrtvehtz00gzjc047yebr296 | 섹션을 독립 카드로 세로 스택하고, 교사·admin 전용 '재주문 알림' 카드는 제목 옆 상태 배지 + 우측 'N건' 배지 버튼으로 재주문 목록에 진입 |
