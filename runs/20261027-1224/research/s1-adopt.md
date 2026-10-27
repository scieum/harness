# S1 가져올 것 — run 20261027-1224

- 구조·흐름·배치만. 색·폰트·모서리는 docs/design.md · rules.json이 정한다.

## 화면 13
| # | ui_url | 가져올 것 |
|---|---|---|
| 1 | https://uibowl.io/name/%EB%AA%A8%EB%91%90%EC%9D%98%EC%A3%BC%EC%B0%A8%EC%9E%A5?patterns=%EC%8B%A0%EC%B2%AD%ED%95%98%EA%B8%B0&imgId=cmcld2g1u000fk107yclukc50 | 모바일은 바텀시트로, 위에서 아래로 제목 → 기능 설명 그림(화면 7 조각) → 전폭 주 버튼 → 맨 아래 보지 않기 텍스트 순서 |
| 2 | https://uibowl.io/name/%EB%8D%B0%EC%9D%BC%EB%A6%AC%EC%83%B7?patterns=%EC%95%BD%EA%B4%80%EB%8F%99%EC%9D%98&imgId=cm90v7lis001bk10dcwvwu420 | 그림을 제목 바로 아래 크게 두고 주 버튼은 하나만 — 보지 않기는 주 버튼보다 약한 텍스트 버튼으로 버튼 아래에 |
| 3 | https://uibowl.io/name/%ED%8C%A8%EC%8A%A4%EC%98%A4%EB%8D%94?patterns=%EC%8B%A0%EC%B2%AD%ED%95%98%EA%B8%B0&imgId=cmsph1e6f00ccjp04i4cje3i8 | "그냥 닫기"를 주 버튼과 별개의 두 번째 텍스트 행동으로 둬서 보지 않기와 역할을 나누는 구성 |
| 4 | https://uibowl.io/name/LG%20ThinQ?patterns=AI&imgId=cmf2a9pjn000tjl04eyw47yvv | 맨 아래 한 줄에 왼쪽 "일주일 동안 보지 않기" · 오른쪽 "닫기" 텍스트 버튼 2개를 좌우로 배치(feature-intro-dismiss) |
| 5 | https://uibowl.io/website/%EC%82%AC%EB%B0%A9%EB%84%B7?patterns=AI&imgId=cmu4rq2t60005l60421mauau0 | 데스크톱은 가운데 모달로, AI가 하는 일을 그림 + 단계 설명(3단계)으로 보여 주고 보지 않기는 모달 맨 아래 줄에 |

## 화면 15
| # | ui_url | 가져올 것 |
|---|---|---|
| 1 | https://uibowl.io/website/%EB%A7%88%EC%9D%B4%ED%81%AC%EB%A1%9C%EC%86%8C%ED%94%84%ED%8A%B8%20%ED%81%B4%EB%9E%98%EB%A6%AC%ED%8B%B0%20(Microsoft%20Clarity)?patterns=%EB%9E%9C%EB%94%A9%ED%8E%98%EC%9D%B4%EC%A7%80&imgId=cmt180ji1000dkz04ef56j21k | 왼쪽 글 묶음(꼬리표·헤드라인·부제·버튼·특징 한 줄)을 하나의 덩어리로 묶어 오른쪽 제품 화면 패널의 세로 가운데에 맞춤 |
| 2 | https://uibowl.io/website/%EC%84%BC%EC%84%9C%ED%83%80%EC%9B%8C?patterns=%EB%9E%9C%EB%94%A9%ED%8E%98%EC%9D%B4%EC%A7%80&imgId=cmtfd83b80003l804cq6f05lo | 글 묶음 중심선 = 오른쪽 제품 화면 묶음(본 화면 + 겹친 카드 포함 전체 범위) 중심선으로 맞추는 기준 |
| 3 | https://uibowl.io/website/braintrust?patterns=%EB%9E%9C%EB%94%A9%ED%8E%98%EC%9D%B4%EC%A7%80&imgId=cm5vzhejt003pla0cs5ayo0x7 | 글 묶음이 짧아도 위로 붙이지 않고 패널 높이 가운데에 두어 위·아래 빈 공간을 같게 |
| 4 | https://uibowl.io/website/%EB%8B%B9%EA%B7%BC%20%EB%B9%84%EC%A6%88%EB%8B%88%EC%8A%A4?patterns=%EB%9E%9C%EB%94%A9%ED%8E%98%EC%9D%B4%EC%A7%80&imgId=cmso68wbc000clf04biyhswza | 두 열을 같은 띠 안에서 세로 중심 정렬(교차축 가운데)로 묶는 2열 배치 방식 |
| 5 | https://uibowl.io/website/KRDS?patterns=%EB%9E%9C%EB%94%A9%ED%8E%98%EC%9D%B4%EC%A7%80&imgId=cmnqqvr26000kl50444y648go | 왼쪽 글 묶음의 내부 순서(헤드라인 → 부제 → 버튼)는 유지하고 묶음 전체 위치만 오른쪽 그래픽 높이의 가운데로 이동 |
