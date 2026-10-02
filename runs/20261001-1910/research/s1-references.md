# S1 레퍼런스 — run 20261001-1910

대상 화면: 1, 4, 5 (docs/PRD.md §7)

## 화면 1
| # | 앱 | ui_url | 화면 설명 |
|---|---|---|---|
| 1 | 스튜디오메이트 | https://uibowl.io/name/%EC%8A%A4%ED%8A%9C%EB%94%94%EC%98%A4%EB%A9%94%EC%9D%B4%ED%8A%B8?patterns=%ED%95%84%ED%84%B0&patternName=%EC%A7%80%EC%97%AD%20%EC%84%A0%ED%83%9D | 지역 선택 필터: 목록 상단 "전국" 위치 칩을 눌러 지역 선택 단계로 들어가고, 선택 결과가 칩 라벨로 돌아오는 흐름 (4장) |
| 2 | redBus | https://uibowl.io/name/redBus?patterns=%EC%A1%B0%ED%9A%8C%ED%95%98%EA%B8%B0&patternName=%EC%A7%80%EC%97%AD%26%EB%82%A0%EC%A7%9C%20%EC%84%A0%ED%83%9D | 지역&날짜 선택: From/To/날짜 필드를 한 카드 안에 세로로 쌓고 아래 전폭 조회 버튼 1개 |
| 3 | MakeMyTrip | https://uibowl.io/name/MakeMyTrip?patterns=%EC%98%88%EC%95%BD%C2%B7%EA%B2%B0%EC%A0%9C&patternName=1.%EB%82%A0%EC%A7%9C%20%EB%B0%8F%20%EC%A7%80%EC%97%AD%20%EC%84%A0%ED%83%9D | 날짜 및 지역 선택 플로우: 진입 → 필드 탭 → 선택 화면 → 값이 채워진 폼으로 복귀하는 단계별 흐름 (9장) |

## 화면 4
| # | 앱 | ui_url | 화면 설명 |
|---|---|---|---|
| 1 | 오클고 | https://uibowl.io/name/%EC%98%A4%ED%81%B4%EA%B3%A0?patterns=%EA%B8%80%EC%93%B0%EA%B8%B0&patternName=%EA%B8%B0%EB%A1%9D%ED%95%98%EA%B8%B0 | 기록하기 바텀시트 폼: 라벨(필수 표시) 위·입력 아래로 날짜 드롭다운 → 장소 칩 → 선택값 → 시간 드롭다운 → 메모 순 세로 배치, 하단 전폭 "기록" 버튼 |
| 2 | 오늘의 루틴 | https://uibowl.io/name/%EC%98%A4%EB%8A%98%EC%9D%98%20%EB%A3%A8%ED%8B%B4?patterns=%EA%B8%80%EC%93%B0%EA%B8%B0&patternName=%EB%A3%A8%ED%8B%B4%20%EA%B8%B0%EB%A1%9D%ED%95%98%EA%B8%B0 | 루틴 기록하기: 탭(정보/진행 현황/오늘의 기록) + "오늘의 기록" 섹션의 날짜 행과 + 버튼으로 기록 추가, 저장 후 토스트 |
| 3 | 레포브 | https://uibowl.io/name/%EB%A0%88%ED%8F%AC%EB%B8%8C?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&patternName=%EA%B8%B0%EB%A1%9D%ED%95%98%EA%B8%B0 | 기록하기: 대상 요약(이름·분류·위치) 아래 하단 고정 "이 장소 기록하기" 버튼 → 기록 입력 단계로 이어지는 흐름 (8장) |

## 화면 5
| # | 앱 | ui_url | 화면 설명 |
|---|---|---|---|
| 1 | 다글로 | https://uibowl.io/name/%EB%8B%A4%EA%B8%80%EB%A1%9C?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&patternName=%EC%9C%A0%ED%8A%9C%EB%B8%8C%20%EB%A7%81%ED%81%AC%20%EC%97%85%EB%A1%9C%EB%93%9C | AI 받아쓰기 업로드: 상단 입력 필드 + 옵션 행(언어·주제) + 하단 고정 실행 버튼(입력 전 비활성) → 처리 결과로 이어지는 흐름 |
| 2 | 수현이랑 | https://uibowl.io/name/%EC%88%98%ED%98%84%EC%9D%B4%EB%9E%91?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&patternName=%EA%B3%B5%EC%9C%A0%20%EC%95%A8%EB%B2%94%20%EC%97%85%EB%A1%9C%EB%93%9C | 업로드 정보 입력: 칩 선택 → 제목 → 설명(글자 수 카운터) 세로 폼, 상단 제목+닫기, 하단 전폭 "완료" 버튼 |
| 3 | 키피럽 | https://uibowl.io/name/%ED%82%A4%ED%94%BC%EB%9F%BD?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&patternName=%EC%9D%B8%EC%A6%9D%EC%83%B7-%EC%97%85%EB%A1%9C%EB%93%9C | 인증샷 업로드: 상단 안내 문구 + 중앙 미리보기 영역 + 하단 갤러리/촬영 진입, 이후 로딩 → 결과 확인 단계 (7장) |
