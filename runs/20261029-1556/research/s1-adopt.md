# S1 가져올 것 — run 20261029-1556

- 구조·흐름·배치만. 색·폰트·모서리는 docs/design.md · rules.json이 정한다.

## 화면 13
| # | ui_url | 가져올 것 |
|---|---|---|
| 1 | https://uibowl.io/website/Npay%20%EC%A6%9D%EA%B6%8C?patterns=%EA%B3%A0%EA%B0%9D%EC%84%BC%ED%84%B0%C2%B7FAQ&imgId=cmvg2hf390003jh061i12flxl | board-link '게시판'을 다른 sidebar-item과 같은 행 모양(아이콘 + 라벨, 같은 높이·들여쓰기)으로 메뉴 목록 안에 둠 |
| 2 | https://uibowl.io/website/KRDS?patterns=%EB%AC%B8%EC%9D%98%ED%95%98%EA%B8%B0&imgId=cmnqqy3l80004i90485kh3whj | 화면 20에서는 board-link를 sidebar-item 현재 항목과 같은 방식으로 표시해 지금 위치를 알림 |
| 3 | https://uibowl.io/website/%EB%A0%88%EB%B7%B0%20(REVU)?patterns=%EB%82%B4%EC%97%AD&imgId=cmvepnf0c000sl606tagx4sv7 | 문의·도움 진입은 사이드바 아래쪽 묶음에 모아 둠 — board-link를 guide-link 바로 위, 이름·역할 칸 위쪽에 |

## 화면 14
| # | ui_url | 가져올 것 |
|---|---|---|
| 1 | https://uibowl.io/name/%EC%84%9D%EA%B0%80%EB%A8%B8%EB%8B%88?patterns=%EC%95%BD%EA%B4%80%EB%8F%99%EC%9D%98&imgId=cmvfy6yjy0039l706526nm0qq | age-confirm '만 14세 이상입니다 (필수)'를 terms-agree 마지막(셋째 약관) 줄로, 위 '모두 동의'가 함께 체크하는 순서 |
| 2 | https://uibowl.io/name/%EC%95%B3%ED%94%8C%EB%A6%AC?patterns=%EC%95%BD%EA%B4%80%EB%8F%99%EC%9D%98&imgId=cmtpoktbe003gkz04h7vfsb8a | 나이 확인 줄을 다른 약관 행과 같은 체크 행 구조(왼쪽 체크 + 라벨 + 오른쪽 끝 표시)로 맞춰 따로 튀지 않게 |
| 3 | https://uibowl.io/name/%EB%AF%B8%EC%86%8C?patterns=%EC%95%BD%EA%B4%80%EB%8F%99%EC%9D%98&imgId=cmqt6jy3n00mvjp04xw22obmk | › 를 누르면 그 행 바로 아래에 한 줄 설명이 펼쳐지고 › 가 ⌄ 로 바뀌는 행 안 펼침 흐름 |

## 화면 18
| # | ui_url | 가져올 것 |
|---|---|---|
| 1 | https://uibowl.io/name/%EC%B0%A8%EB%9E%80?patterns=%EB%A7%88%EC%9D%B4%ED%8E%98%EC%9D%B4%EC%A7%80&imgId=cmtwj2vr0000njr04c0puv2kw | 묶음 제목 '도움말' 아래 게시판(문의) 행과 가이드 행을 한 묶음으로 세로 나열 |
| 2 | https://uibowl.io/name/%EB%B9%BC%EA%B8%B0?patterns=%EB%A7%88%EC%9D%B4%ED%8E%98%EC%9D%B4%EC%A7%80&imgId=cmsu39z4z00eajv04guutwvzj | 기능 묶음들 뒤 맨 아래 지원 묶음 순서, board-link는 manage-row와 같은 아이콘 + 이름 + › 행 |
| 3 | https://uibowl.io/name/%EB%B3%B4%EB%A7%B5?patterns=%EB%A7%88%EC%9D%B4%ED%8E%98%EC%9D%B4%EC%A7%80&imgId=cmr2zi6fs0006l104cnmb2duz | 문의 진입 행은 다른 행과 구조를 바꾸지 않고 오른쪽 요약 caption('답변 완료 1') 자리만 더함 |

## 화면 20
| # | ui_url | 가져올 것 |
|---|---|---|
| 1 | https://uibowl.io/name/%EC%98%A4%EC%9D%BC%EB%82%98%EC%9A%B0?patterns=%EB%AC%B8%EC%9D%98%ED%95%98%EA%B8%B0&imgId=cmtpnvv5p001ajo04pqnetzma | board-post-row = 제목 한 줄 / 아래 메타 줄(글쓴이 · 날짜) + 상태, 페이지 머리 오른쪽에 board-write 알약 |
| 2 | https://uibowl.io/name/%EB%9D%BC%EC%9D%B4%ED%94%84%EC%BA%90%EC%B9%98?patterns=%EB%AC%B8%EC%9D%98%ED%95%98%EA%B8%B0&imgId=cmqzb48yx003yju04rnwhv1yb | 20-empty = board-tabs는 그대로 두고 그 아래 ex-empty-state-card 한 장 + board-write 진입 |
| 3 | https://uibowl.io/name/%EC%A0%A0%EB%94%94?patterns=%EA%B3%A0%EA%B0%9D%EC%84%BC%ED%84%B0%C2%B7FAQ&imgId=cmradcdot0027k204q9o4qkmx | faq-item = 질문 한 줄 + 오른쪽 펼침 표시, 펼치면 질문 바로 아래 답 상자가 붙는 아코디언 |
| 4 | https://uibowl.io/name/%ED%95%B4%ED%94%BC%EB%AC%B8%EB%8D%B0%EC%9D%B4?patterns=%EB%AC%B8%EC%9D%98%ED%95%98%EA%B8%B0&imgId=cmtwleq9n0044l704bgq32c1l | board-form 순서 = 분류 선택 → 제목 → board-privacy-note → 본문 → '등록', 안내 문구는 입력 칸 사이 한 줄 |
| 5 | https://uibowl.io/name/%EC%8F%98%EC%B9%B4?patterns=%EB%AC%B8%EC%9D%98%ED%95%98%EA%B8%B0&imgId=cmogjptrp02kpl104qg664v7v | board-detail = 제목 → 날짜·상태 배지 줄 → 본문 순서, 그 아래에 board-answer 상자를 이어 붙임 |
