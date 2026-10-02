# S1 채택 항목 — run 20261002-1032

구조·흐름·배치만 가져온다. 색·폰트·모서리는 docs/design.md를 따른다.
화면 1·4·5는 runs/20261001-1910/research/s1-adopt.md 를 재사용하고, 하늘색 강조(선택·활성·링크·진행·아이콘 한정, 재고 부족에는 쓰지 않음)를 어디에 둘지 위치만 한 줄 덧붙였다.

## 화면 7
| # | ui_url | 가져올 것 |
|---|---|---|
| 1 | https://uibowl.io/name/%EB%B9%BC%EA%B8%B0?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&patternName=%EC%83%81%ED%92%88%20%EB%93%B1%EB%A1%9D | 시약 목록 화면에서 고정 "+ 새 시약 등록" 진입점을 두고 별도 등록 폼(분류 드롭다운 포함)으로 넘어가는 2단계 흐름 |
| 2 | https://uibowl.io/name/%EC%B0%A8%EB%9E%80?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&patternName=%EC%A7%81%EC%A0%91%ED%8C%90%EB%A7%A4%20%EC%83%81%ED%92%88%EB%93%B1%EB%A1%9D | 화면 상단에서 "기존 시약 입고(수량 증가)" / "새 시약 등록" 두 갈래를 먼저 고르게 하고, 주 경로 버튼 아래 "또는" 구분으로 보조 경로를 두는 배치 |
| 3 | https://uibowl.io/name/%EC%9A%B0%EB%A6%AC%EB%8F%99%EB%84%A4GS?patterns=%EC%A1%B0%ED%9A%8C%ED%95%98%EA%B8%B0&patternName=%EC%9E%AC%EA%B3%A0%EC%B0%BE%EA%B8%B0 | 입고 대상 시약을 상단 검색 입력으로 찾고 결과 리스트에서 골라 수량 입력 단계로 넘어가는 검색 → 선택 흐름 |

## 화면 8
| # | ui_url | 가져올 것 |
|---|---|---|
| 1 | https://uibowl.io/name/%EC%9B%8C%ED%81%AC%EC%98%A8?patterns=%EC%B4%88%EB%8C%80%ED%95%98%EA%B8%B0%C2%B7%EB%B0%9B%EA%B8%B0&patternName=%EC%BB%A4%EB%AE%A4%EB%8B%88%ED%8B%B0%20%EB%A9%A4%EB%B2%84%20%EC%B4%88%EB%8C%80 | 상단에 학교(그룹)명·사용자 수 헤더를 두고 그 아래 "사용자 초대" 진입점 → 바텀시트에서 초대 입력을 받는 구조 |
| 2 | https://uibowl.io/name/%ED%8C%A8%EC%8A%A4%EC%98%A4%EB%8D%94?patterns=%EC%B4%88%EB%8C%80%ED%95%98%EA%B8%B0%C2%B7%EB%B0%9B%EA%B8%B0&patternName=%EA%B0%99%EC%9D%B4%EC%A3%BC%EB%AC%B8%20%EB%A9%A4%EB%B2%84 | 초대 방법(링크 복사·직접 입력)을 상단에 나란히 두고, 하단 전폭 버튼 라벨에 대상 수("N명 초대")를 반영하며 0명일 때 비활성으로 두는 패턴 |
| 3 | https://uibowl.io/name/%EB%A9%94%EA%B0%80MCG%EC%BB%A4%ED%94%BC?patterns=%EC%B4%88%EB%8C%80%ED%95%98%EA%B8%B0%C2%B7%EB%B0%9B%EA%B8%B0&patternName=%EA%B0%99%EC%9D%B4%EC%A3%BC%EB%AC%B8%20%EB%A9%A4%EB%B2%84 | 제목+안내문 → 검색 입력 → 사용자 리스트(빈 상태 문구 포함) → 하단 전폭 확정 버튼 순 세로 배치, 확정 후 멤버 목록 단계로 복귀 |

## 화면 10
| # | ui_url | 가져올 것 |
|---|---|---|
| 1 | https://uibowl.io/name/%ED%86%A0%EC%8A%A4%EC%A6%9D%EA%B6%8C?patterns=%EB%82%B4%EC%97%AD&patternName=%EA%B1%B0%EB%9E%98%EB%82%B4%EC%97%AD | 리스트 바로 위 "전체" 드롭다운 필터 + 행마다 날짜(좌)·시약명/사용자·유형(중)·증감 수량(우) 3열 배치 |
| 2 | https://uibowl.io/name/%EB%AF%B8%EB%8B%88%EC%8A%A4%ED%83%81?patterns=%EB%82%B4%EC%97%AD&patternName=%EC%9B%90%ED%99%94%20%EA%B1%B0%EB%9E%98%EB%82%B4%EC%97%AD | 섹션 제목 우측에 기간·유형 요약 필터("최근 N개월 · 전체")를 두고 월(날짜) 그룹 헤더로 기록을 묶는 구조, 행 우측에 증감과 남은 재고를 2줄로 표시 |
| 3 | https://uibowl.io/name/%ED%86%A0%EC%8A%A4?patterns=%EB%82%B4%EC%97%AD&patternName=%EA%B1%B0%EB%9E%98%20%EC%83%81%EC%84%B8 | 기록 행을 누르면 상단 시약명·수량 요약 + 라벨-값 행(사용자·일시·메모) 상세로 들어가는 목록 → 상세 흐름 |

## 화면 9
| # | ui_url | 가져올 것 |
|---|---|---|
| 1 | https://uibowl.io/name/%ED%8E%98%EC%9D%B4%EC%9B%8C%ED%81%AC?patterns=%EB%A9%94%EB%89%B4&patternName=%EA%B0%84%ED%8E%B8%EB%A9%94%EB%89%B4%20-%20%EA%B1%B0%EB%9E%98%EC%B2%98 | 판매처 목록: 상단 검색 바 + 행마다 우측 더보기(수정·삭제) 메뉴 + 하단 고정 "판매처 등록" 버튼 배치 |
| 2 | https://uibowl.io/name/%ED%8E%98%EC%9D%B4%EC%9B%8C%ED%81%AC?patterns=%ED%8E%B8%EC%A7%91%C2%B7%EC%88%98%EC%A0%95%ED%95%98%EA%B8%B0&patternName=%EA%B1%B0%EB%9E%98%EC%B2%98%EC%88%98%EC%A0%95 | 행 메뉴 → 수정 폼 진입, 삭제는 모달로 한 번 더 확인하는 수정·삭제 흐름 |
| 3 | https://uibowl.io/name/%ED%8E%98%EC%9D%B4%EC%9B%8C%ED%81%AC?patterns=%ED%8E%B8%EC%A7%91%C2%B7%EC%88%98%EC%A0%95%ED%95%98%EA%B8%B0&patternName=%EA%B1%B0%EB%9E%98%EC%B2%98%EC%B6%94%EA%B0%80 | 판매처가 0건일 때 아이콘·안내문 + 등록 버튼을 가운데 두는 빈 상태, 등록 폼(텍스트 필드 세로) 저장 후 목록으로 복귀하는 흐름 |

## 화면 1
| # | ui_url | 가져올 것 |
|---|---|---|
| 1 | https://uibowl.io/name/%EC%8A%A4%ED%8A%9C%EB%94%94%EC%98%A4%EB%A9%94%EC%9D%B4%ED%8A%B8?patterns=%ED%95%84%ED%84%B0&patternName=%EC%A7%80%EC%97%AD%20%EC%84%A0%ED%83%9D | 지역 선택을 별도 단계(목록 화면)로 열고, 고른 값이 원래 필드 라벨로 돌아와 표시되는 흐름. 하늘색 강조는 선택 목록의 현재 선택 행에만 둔다 |
| 2 | https://uibowl.io/name/redBus?patterns=%EC%A1%B0%ED%9A%8C%ED%95%98%EA%B8%B0&patternName=%EC%A7%80%EC%97%AD%26%EB%82%A0%EC%A7%9C%20%EC%84%A0%ED%83%9D | 시/도·지역·학교 3개 선택 필드를 한 묶음 안에 세로로 쌓고 그 아래 전폭 확인 버튼 1개를 두는 배치 |
| 3 | https://uibowl.io/name/MakeMyTrip?patterns=%EC%98%88%EC%95%BD%C2%B7%EA%B2%B0%EC%A0%9C&patternName=1.%EB%82%A0%EC%A7%9C%20%EB%B0%8F%20%EC%A7%80%EC%97%AD%20%EC%84%A0%ED%83%9D | 필드 탭 → 선택 화면 → 값이 채워진 폼으로 복귀를 단계마다 반복하는 순차 선택 흐름 (앞 단계 미선택 시 다음 필드 비활성). 진행 단계 표시 위치에 하늘색 진행 강조를 둔다 |

## 화면 4
| # | ui_url | 가져올 것 |
|---|---|---|
| 1 | https://uibowl.io/name/%EC%98%A4%ED%81%B4%EA%B3%A0?patterns=%EA%B8%80%EC%93%B0%EA%B8%B0&patternName=%EA%B8%B0%EB%A1%9D%ED%95%98%EA%B8%B0 | 라벨 위·입력 아래 세로 폼(날짜 드롭다운 → 수량·단위 → 사용자 → 메모), 필수 표시, 하단 전폭 "기록" 버튼 배치. 단위 칩 선택 상태에 하늘색 강조 위치를 둔다 |
| 2 | https://uibowl.io/name/%EC%98%A4%EB%8A%98%EC%9D%98%20%EB%A3%A8%ED%8B%B4?patterns=%EA%B8%80%EC%93%B0%EA%B8%B0&patternName=%EB%A3%A8%ED%8B%B4%20%EA%B8%B0%EB%A1%9D%ED%95%98%EA%B8%B0 | 저장 직후 토스트로 결과를 알리고 기록 목록으로 돌아오는 저장 피드백 흐름 |
| 3 | https://uibowl.io/name/%EB%A0%88%ED%8F%AC%EB%B8%8C?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&patternName=%EA%B8%B0%EB%A1%9D%ED%95%98%EA%B8%B0 | 폼 상단에 대상 요약(시약명·현재 재고) 블록을 고정해 무엇을 기록하는지 보여준 뒤 입력으로 이어지는 구조. 요약 블록의 재고 부족 표시는 하늘색이 아닌 별도 경고 처리로 둔다 |

## 화면 5
| # | ui_url | 가져올 것 |
|---|---|---|
| 1 | https://uibowl.io/name/%EB%8B%A4%EA%B8%80%EB%A1%9C?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&patternName=%EC%9C%A0%ED%8A%9C%EB%B8%8C%20%EB%A7%81%ED%81%AC%20%EC%97%85%EB%A1%9C%EB%93%9C | 파일 선택 전에는 하단 고정 실행(AI 추출) 버튼을 비활성으로 두고, 선택 후 활성화 → 처리 → 결과로 넘어가는 흐름 (키·모델 옵션 행은 가져오지 않음) |
| 2 | https://uibowl.io/name/%EC%88%98%ED%98%84%EC%9D%B4%EB%9E%91?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&patternName=%EA%B3%B5%EC%9C%A0%20%EC%95%A8%EB%B2%94%20%EC%97%85%EB%A1%9C%EB%93%9C | 추출 결과 확인 단계를 상단 제목+닫기, 본문 스크롤(결과 표·수정 가능 필드), 하단 전폭 "저장" 버튼으로 구성하는 배치 |
| 3 | https://uibowl.io/name/%ED%82%A4%ED%94%BC%EB%9F%BD?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&patternName=%EC%9D%B8%EC%A6%9D%EC%83%B7-%EC%97%85%EB%A1%9C%EB%93%9C | 상단 안내 문구 + 중앙 업로드/미리보기 영역 + 하단 진입 버튼, 업로드 후 로딩 상태를 거쳐 확인 단계로 가는 3단 흐름. 업로드 영역 아이콘과 처리 진행 표시 위치에 하늘색 강조를 둔다 |
