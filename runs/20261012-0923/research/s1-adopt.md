# S1 채택 — runs/20261012-0923

구조·흐름·배치만 가져온다. 색·폰트·모서리는 design.md / rules.json을 따른다.

## 화면 8
| # | ui_url | 가져올 것 |
|---|---|---|
| 1 | https://uibowl.io/website/%EB%A6%AC%EC%8A%A4%EB%8B%9D%EB%A7%88%EC%9D%B8%EB%93%9C?patterns=%EB%A7%88%EC%9D%B4%ED%8E%98%EC%9D%B4%EC%A7%80&imgId=cmsssakfn0008l104ol1ypu26 | 초대 폼과 구성원 표 구조는 승인본 그대로 두고 초대 대기 행만 표 안에 같은 열 구조로 유지 |
| 2 | https://uibowl.io/website/%EC%B1%84%EB%84%90%ED%86%A1?patterns=AI&imgId=cmudq45mh001qjy04qd93j3wk | 초대 대기 행 맨 오른쪽 끝 열에 ⋯ 버튼 하나만 두고 다른 동작 버튼은 행에 늘어놓지 않음 |
| 3 | https://uibowl.io/name/%EC%97%90%EC%9D%B4%EB%8B%B7?patterns=%ED%8E%B8%EC%A7%91%C2%B7%EC%88%98%EC%A0%95%ED%95%98%EA%B8%B0&patternName=%EC%B5%9C%EA%B7%BC%EA%B8%B0%EB%A1%9D%28%EC%82%AD%EC%A0%9C%29 | ⋯를 누르면 버튼 바로 아래 붙는 팝오버 메뉴, 되돌릴 수 없는 '초대 취소'는 메뉴 맨 아래 → 확인 모달로 이어지는 2단계 |
| 4 | https://uibowl.io/name/%EC%85%94%ED%81%B4?patterns=%EC%B7%A8%EC%86%8C%ED%95%98%EA%B8%B0&imgId=cmrt4shpb0007l104b7hb2rnd | 취소 확인 모달 구조: 질문형 제목 1줄 + 설명 2줄 + 아래 가로 2버튼(돌아가기 / 초대 취소) |
| 5 | https://uibowl.io/name/%EC%99%93%EC%84%AD?patterns=%EC%B7%A8%EC%86%8C%ED%95%98%EA%B8%B0&imgId=cmqt89aob001pjl044nphhj04 | 모달 본문에 취소 뒤 결과(받은 사람의 초대 링크가 더 이상 열리지 않음)를 한 문장으로 설명 |

## 화면 13
| # | ui_url | 가져올 것 |
|---|---|---|
| 1 | https://uibowl.io/name/%ED%8E%98%EC%9D%B4%EC%9B%8C%ED%81%AC?patterns=%EB%A9%94%EB%89%B4&patternName=%EA%B0%84%ED%8E%B8%EB%A9%94%EB%89%B4%20-%20%EA%B1%B0%EB%9E%98%EC%B2%98 | ☰ 전체 메뉴 시트는 역할이 볼 수 있는 메뉴를 묶음별로 한 화면에 모두 나열하고, 항목을 누르면 시트가 닫히며 해당 화면으로 이동 |
| 2 | https://uibowl.io/name/%EB%83%89%EC%9E%A5%EA%B3%A0%ED%84%B8%EA%B8%B0?patterns=%EC%B4%88%EB%8C%80%ED%95%98%EA%B8%B0%C2%B7%EB%B0%9B%EA%B8%B0&imgId=cmohwt39000b9jm04x67jmza1 | 메뉴 진입 버튼은 상단 머리 왼쪽 끝(nav-pill 왼쪽)에 아이콘 하나로 두고 오른쪽 아이콘 배치는 그대로 |
| 3 | https://uibowl.io/website/%EB%A6%AC%EC%BA%90%EC%B9%98?patterns=%EB%82%B4%EC%97%AD&imgId=cmihk42lp000jjp0436gwgn7n | 권한 없음 안내는 화면을 막지 않는 토스트(아이콘 + 한 줄 + 닫기)로, 뒤의 학생 홈은 그대로 보이게 |
| 4 | https://uibowl.io/name/%EC%BA%90%EC%8B%9C%EC%9B%8C%ED%81%AC?patterns=%ED%8E%B8%EC%A7%91%C2%B7%EC%88%98%EC%A0%95%ED%95%98%EA%B8%B0&patternName=%EA%B2%8C%EC%8B%9C%EA%B8%80%20%EC%82%AD%EC%A0%9C | 모바일 토스트 위치는 하단 탭바 바로 위 한 줄, 잠시 뒤 사라지는 흐름 |

## 화면 15
| # | ui_url | 가져올 것 |
|---|---|---|
| 1 | https://uibowl.io/name/%EB%9E%AD%ED%94%8C%EB%A6%AD%EC%8A%A4?patterns=%EC%98%A8%EB%B3%B4%EB%94%A9&imgId=cmswzxy9v0003l404lllro7wu | 모바일 히어로 첫 줄을 작은 꼬리표 1줄('과학실 시약·센서 관리')로 두고 그 아래 강조 헤드라인 2줄이 이어지는 3단 구조 |
| 2 | https://uibowl.io/name/%ED%8E%98%EC%9D%B4%EC%9B%8C%ED%81%AC?patterns=%EC%98%A8%EB%B3%B4%EB%94%A9&patternName=%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85%20%EC%A0%84 | 히어로 안에는 서비스 이름 대신 가치 제안 헤드라인만 두고 버튼은 아래 전폭 세로 스택 |
| 3 | https://uibowl.io/name/CES%202026?patterns=%EC%98%A8%EB%B3%B4%EB%94%A9&imgId=cmk5qewa10003jy04k4wwtudg | 꼬리표 → 제목 → 설명 → 주 버튼 + 텍스트 버튼 순서를 바꾸지 않고 꼬리표 줄만 교체 |
| 4 | https://uibowl.io/website/%EB%A7%88%EC%9D%B4%ED%81%AC%EB%A1%9C%EC%86%8C%ED%94%84%ED%8A%B8%20%ED%81%B4%EB%9E%98%EB%A6%AC%ED%8B%B0%20(Microsoft%20Clarity)?patterns=%EB%9E%9C%EB%94%A9%ED%8E%98%EC%9D%B4%EC%A7%80&imgId=cmt180ji1000dkz04ef56j21k | 로고(워드마크)는 상단 바에만 한 번 두고 히어로 글 열에는 반복하지 않음 — 15-desktop 확인 기준 |

## 화면 17
| # | ui_url | 가져올 것 |
|---|---|---|
| 1 | https://uibowl.io/name/%ED%86%A0%EC%8A%A4%EC%A6%9D%EA%B6%8C?patterns=%EC%BB%A4%EB%AE%A4%EB%8B%88%ED%8B%B0&imgId=cmsb4ub9l0009jo042gue22tj | 센서 종류 시트: 맨 위 제목 + 검색칸, 아래 묶음 제목별 행 목록, 고른 행 오른쪽 체크, 검색 시 묶음 제목은 남기고 맞는 행만 |
| 2 | https://uibowl.io/name/Bitget?patterns=%EC%9D%B8%EC%A6%9D%ED%95%98%EA%B8%B0&imgId=cmukqaul5002ll60430j2ykk1 | 모델번호 자동완성: 입력칸 바로 아래 후보 목록(모델번호 + 이름 한 줄), 맨 위 구역은 입력과 가장 맞는 후보 |
| 3 | https://uibowl.io/website/%EC%82%AC%EB%B0%A9%EB%84%B7?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&imgId=cmu4rq9d8000xjm04y191pizg | 데스크톱 서류 등록은 모달이 아닌 페이지(사이드 레일 유지): 파일 올리기 칸 → 읽은 결과 전폭 확인 표로 이어지는 흐름 |
| 4 | https://uibowl.io/name/%ED%8E%98%EC%9D%B4%ED%9E%88%EC%96%B4?patterns=%EC%B4%AC%EC%98%81%ED%95%98%EA%B8%B0&imgId=cmnfmykft001zl204e2svm4y5 | 확인 표 위에 원본 서류 미리보기 + "맞는지 확인해 주세요" 안내 1줄, 아래 다시 올리기 / 등록 2버튼 |
| 5 | https://uibowl.io/name/%EC%95%84%EC%9D%B4%EC%BF%A0%EC%B9%B4?patterns=%EC%B4%AC%EC%98%81%ED%95%98%EA%B8%B0&imgId=cmp0t6j63000fl904x800o216 | 읽기 실패: 실패 이유 2줄 + '다시 올리기 / 직접 입력' 두 갈래 동작으로 막다른 길을 없앰 |
