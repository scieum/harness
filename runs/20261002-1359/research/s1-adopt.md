# S1 채택 항목 — run 20261002-1359

구조·흐름·배치만 가져온다. 색·폰트·모서리는 docs/design.md를 따른다.

## 화면 13
| # | ui_url | 가져올 것 |
|---|---|---|
| 1 | https://uibowl.io/name/%ED%8E%98%EC%9D%B4%ED%9E%88%EC%96%B4?patterns=%EB%A9%94%EC%9D%B8&imgId=cmnfmxnhh0003l8045z9h1r15 | 하단 탭바 4개를 균등 폭으로 두고 가운데 탭을 키우지 않으며, 활성 탭은 아이콘·라벨 상태 변화로만 표시. 상단은 학교명 + 알림만 있는 얇은 헤더로 줄이고 상단 바로가기 그리드는 두지 않음 |
| 2 | https://uibowl.io/name/%ED%8E%98%EC%9D%B4%EC%9B%8C%ED%81%AC?patterns=%EB%A9%94%EC%9D%B8&imgId=cmtzo55qv002rl7047rsl7n07 | 역할 분담: 탭바는 '목록·관리' 화면(홈/시약 목록/사용 기록/설정 류)으로 이동, 홈 본문 퀵 메뉴는 'QR 스캔·사용 등록' 같은 실행 동작만 둬서 탭과 같은 목적지를 중복하지 않음 |
| 3 | https://uibowl.io/name/%ED%97%A4%EC%9D%B4%EC%98%81%20%EC%BA%A0%ED%8D%BC%EC%8A%A4?patterns=%EB%A9%94%EC%9D%B8&imgId=cmmbj8sqh0004lh048k4kbkqd | 학교 앱 배치: 헤더에 학교 표시, 홈 첫 카드 안에 전폭 주 버튼(QR 스캔)을 두고 그 아래 역할별 퀵 메뉴 4칸 한 줄. 스캔은 탭이 아니라 홈 본문 카드에서 진입 |
| 4 | https://uibowl.io/name/%ED%95%98%EC%9D%B4%EB%A7%81%EA%B5%AC%EC%96%BC?patterns=%EB%A9%94%EC%9D%B8&imgId=cmnmkywio0003l804k22ndnyy | 탭 4개 구성(홈/관리 대상 목록/기록/마이) 패턴과 활성 1개·비활성 3개의 2단 상태 표시, 주 동작은 탭바에 넣지 않고 본문 전폭 버튼으로 분리 |
| 5 | https://uibowl.io/name/%EC%9E%90%EB%A6%AC%ED%86%A1?patterns=%EB%A9%94%EC%9D%B8&patternName=%ED%99%88%28%EC%9E%84%EB%8C%80%EC%9D%B8%29 | 홈 요약 카드: 시약장 합계 + 상태별(정상/부족/만료 임박) 구간 막대 + 보조 수치 1줄, 시약장 0개면 빈 상태 + 추가 버튼. 역할(학생/교사/admin)별로 카드 구성만 바꾸고 탭바 4개는 공통 유지 |
