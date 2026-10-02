# S1 채택 항목 — run 20261001-1910

구조·흐름·배치만 가져온다. 색·폰트·모서리는 docs/design.md를 따른다.

## 화면 1
| # | ui_url | 가져올 것 |
|---|---|---|
| 1 | https://uibowl.io/name/%EC%8A%A4%ED%8A%9C%EB%94%94%EC%98%A4%EB%A9%94%EC%9D%B4%ED%8A%B8?patterns=%ED%95%84%ED%84%B0&patternName=%EC%A7%80%EC%97%AD%20%EC%84%A0%ED%83%9D | 지역 선택을 별도 단계(목록 화면)로 열고, 고른 값이 원래 필드 라벨로 돌아와 표시되는 흐름 |
| 2 | https://uibowl.io/name/redBus?patterns=%EC%A1%B0%ED%9A%8C%ED%95%98%EA%B8%B0&patternName=%EC%A7%80%EC%97%AD%26%EB%82%A0%EC%A7%9C%20%EC%84%A0%ED%83%9D | 시/도·지역·학교 3개 선택 필드를 한 묶음 안에 세로로 쌓고 그 아래 전폭 확인 버튼 1개를 두는 배치 |
| 3 | https://uibowl.io/name/MakeMyTrip?patterns=%EC%98%88%EC%95%BD%C2%B7%EA%B2%B0%EC%A0%9C&patternName=1.%EB%82%A0%EC%A7%9C%20%EB%B0%8F%20%EC%A7%80%EC%97%AD%20%EC%84%A0%ED%83%9D | 필드 탭 → 선택 화면 → 값이 채워진 폼으로 복귀를 단계마다 반복하는 순차 선택 흐름 (앞 단계 미선택 시 다음 필드 비활성) |

## 화면 4
| # | ui_url | 가져올 것 |
|---|---|---|
| 1 | https://uibowl.io/name/%EC%98%A4%ED%81%B4%EA%B3%A0?patterns=%EA%B8%80%EC%93%B0%EA%B8%B0&patternName=%EA%B8%B0%EB%A1%9D%ED%95%98%EA%B8%B0 | 라벨 위·입력 아래 세로 폼(날짜 드롭다운 → 수량·단위 → 사용자 → 메모), 필수 표시, 하단 전폭 "기록" 버튼 배치 |
| 2 | https://uibowl.io/name/%EC%98%A4%EB%8A%98%EC%9D%98%20%EB%A3%A8%ED%8B%B4?patterns=%EA%B8%80%EC%93%B0%EA%B8%B0&patternName=%EB%A3%A8%ED%8B%B4%20%EA%B8%B0%EB%A1%9D%ED%95%98%EA%B8%B0 | 저장 직후 토스트로 결과를 알리고 기록 목록으로 돌아오는 저장 피드백 흐름 |
| 3 | https://uibowl.io/name/%EB%A0%88%ED%8F%AC%EB%B8%8C?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&patternName=%EA%B8%B0%EB%A1%9D%ED%95%98%EA%B8%B0 | 폼 상단에 대상 요약(시약명·현재 재고) 블록을 고정해 무엇을 기록하는지 보여준 뒤 입력으로 이어지는 구조 |

## 화면 5
| # | ui_url | 가져올 것 |
|---|---|---|
| 1 | https://uibowl.io/name/%EB%8B%A4%EA%B8%80%EB%A1%9C?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&patternName=%EC%9C%A0%ED%8A%9C%EB%B8%8C%20%EB%A7%81%ED%81%AC%20%EC%97%85%EB%A1%9C%EB%93%9C | 파일 선택 전에는 하단 고정 실행(AI 추출) 버튼을 비활성으로 두고, 선택 후 활성화 → 처리 → 결과로 넘어가는 흐름 (키·모델 옵션 행은 가져오지 않음) |
| 2 | https://uibowl.io/name/%EC%88%98%ED%98%84%EC%9D%B4%EB%9E%91?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&patternName=%EA%B3%B5%EC%9C%A0%20%EC%95%A8%EB%B2%94%20%EC%97%85%EB%A1%9C%EB%93%9C | 추출 결과 확인 단계를 상단 제목+닫기, 본문 스크롤(결과 표·수정 가능 필드), 하단 전폭 "저장" 버튼으로 구성하는 배치 |
| 3 | https://uibowl.io/name/%ED%82%A4%ED%94%BC%EB%9F%BD?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&patternName=%EC%9D%B8%EC%A6%9D%EC%83%B7-%EC%97%85%EB%A1%9C%EB%93%9C | 상단 안내 문구 + 중앙 업로드/미리보기 영역 + 하단 진입 버튼, 업로드 후 로딩 상태를 거쳐 확인 단계로 가는 3단 흐름 |
