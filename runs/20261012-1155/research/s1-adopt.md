# S1 채택 — runs/20261012-1155

구조·흐름·배치만 가져온다. 색·폰트·모서리는 design.md / rules.json(1.28)을 따른다.

## 화면 17
| # | ui_url | 가져올 것 |
|---|---|---|
| 1 | https://uibowl.io/name/%ED%86%A0%EC%8A%A4%EC%A6%9D%EA%B6%8C?patterns=%EC%BB%A4%EB%AE%A4%EB%8B%88%ED%8B%B0&imgId=cmsb4ub9l0009jo042gue22tj | 종류 시트 틀은 승인본 그대로(제목 + 검색칸 → 묶음별 행, 고른 행 오른쪽 체크) 두고 묶음 안 행 목록만 접었다 펼치는 구조로 바꿈 |
| 2 | https://uibowl.io/name/%EB%8B%AC%EB%8B%A4%EB%B0%A9?patterns=%EC%83%81%EC%84%B8%EC%A0%95%EB%B3%B4%20%28PDP%29&patternName=%EC%83%81%ED%92%88 | 묶음 4개를 같은 높이의 아코디언 머리 줄(묶음 이름 왼쪽, 펼침 표시 오른쪽)로 세로로 쌓고, 누른 묶음만 바로 아래로 행이 펼쳐짐 |
| 3 | https://uibowl.io/name/%EB%84%A4%EC%9D%B4%EB%B2%84%EB%B8%94%EB%A1%9C%EA%B7%B8?patterns=%ED%95%84%ED%84%B0&imgId=cmumdx3pp008yjm04zoku825b | 필터 시트 안에서 접힌 줄은 머리 한 줄만 보이고 ⌄를 눌러 그 자리에서 펼치는 흐름 — 시트를 벗어나지 않음 |
| 4 | https://uibowl.io/name/%EC%B9%B4%EC%B9%B4%EC%98%A4%EA%B3%A8%ED%94%84%EC%98%88%EC%95%BD?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&imgId=cmtwlux30003ll10402s3yw0o | 필터 시트 배치: 제목 + × 머리, 본문은 종류(접힌 묶음) → 회사 → 상태 순 구역, 맨 아래 초기화/적용 2버튼 고정 |
| 5 | https://uibowl.io/name/%EC%B9%B4%EC%B9%B4%EC%98%A4%EA%B3%A8%ED%94%84%EC%98%88%EC%95%BD?patterns=%EA%B2%80%EC%83%89&imgId=cmtwlue90002bjw04hgtwofel | 고른 개수는 묶음 머리 줄 이름 뒤에 'N개'로 붙여(예: '화학 · 2개') 접혀 있어도 선택 상태가 보이게, 0개면 개수 표시 생략 |
