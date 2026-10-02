# S1 레퍼런스 — run 20261002-1032

대상 화면: 7, 8, 10, 9, 1, 4, 5 (docs/PRD.md §7)
화면 1·4·5는 runs/20261001-1910/research/ 의 검색 결과를 그대로 재사용했다(새 검색 없음).

## 화면 7
| # | 앱 | ui_url | 화면 설명 |
|---|---|---|---|
| 1 | 빼기 | https://uibowl.io/name/%EB%B9%BC%EA%B8%B0?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&patternName=%EC%83%81%ED%92%88%20%EB%93%B1%EB%A1%9D | 상품 등록: 목록 화면 우하단 플로팅 "+ 상품 등록" 버튼으로 등록 폼(드롭다운 포함)에 진입하는 2단계 흐름 |
| 2 | 차란 | https://uibowl.io/name/%EC%B0%A8%EB%9E%80?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&patternName=%EC%A7%81%EC%A0%91%ED%8C%90%EB%A7%A4%20%EC%83%81%ED%92%88%EB%93%B1%EB%A1%9D | 직접판매 상품등록: 상단 질문형 제목 + 등록 방법 카드 2x2 + 전폭 주 버튼, 아래 "또는" 구분 뒤 보조 입력 필드, 이후 단계별 입력 (10장) |
| 3 | 우리동네GS | https://uibowl.io/name/%EC%9A%B0%EB%A6%AC%EB%8F%99%EB%84%A4GS?patterns=%EC%A1%B0%ED%9A%8C%ED%95%98%EA%B8%B0&patternName=%EC%9E%AC%EA%B3%A0%EC%B0%BE%EA%B8%B0 | 재고찾기: 상단 검색 입력 + 아래 번호 붙은 2열 검색어 목록, 이후 결과 리스트로 이어지는 흐름 (3장) |

## 화면 8
| # | 앱 | ui_url | 화면 설명 |
|---|---|---|---|
| 1 | 워크온 | https://uibowl.io/name/%EC%9B%8C%ED%81%AC%EC%98%A8?patterns=%EC%B4%88%EB%8C%80%ED%95%98%EA%B8%B0%C2%B7%EB%B0%9B%EA%B8%B0&patternName=%EC%BB%A4%EB%AE%A4%EB%8B%88%ED%8B%B0%20%EB%A9%A4%EB%B2%84%20%EC%B4%88%EB%8C%80 | 커뮤니티 멤버 초대: 그룹 헤더(이름·인원 수) 아래 "멤버 초대" 칩 → 바텀시트로 초대 대상 선택, 대상이 없을 때 빈 화면 + 비활성 하단 버튼 |
| 2 | 패스오더 | https://uibowl.io/name/%ED%8C%A8%EC%8A%A4%EC%98%A4%EB%8D%94?patterns=%EC%B4%88%EB%8C%80%ED%95%98%EA%B8%B0%C2%B7%EB%B0%9B%EA%B8%B0&patternName=%EA%B0%99%EC%9D%B4%EC%A3%BC%EB%AC%B8%20%EB%A9%A4%EB%B2%84 | 같이주문 멤버 추가: 상단 추가 방법 카드 2개(링크 복사·QR) + 탭(최근/연락처) + "직접 입력 +" 버튼, 하단 "N명에게 초대 메시지 보내기" 버튼 (3장) |
| 3 | 메가MCG커피 | https://uibowl.io/name/%EB%A9%94%EA%B0%80MCG%EC%BB%A4%ED%94%BC?patterns=%EC%B4%88%EB%8C%80%ED%95%98%EA%B8%B0%C2%B7%EB%B0%9B%EA%B8%B0&patternName=%EA%B0%99%EC%9D%B4%EC%A3%BC%EB%AC%B8%20%EB%A9%A4%EB%B2%84 | 같이주문 멤버: 바텀시트 상단 제목+안내문 + 검색 입력, 목록(없으면 빈 상태), 하단 전폭 "초대장 보내기" 버튼, 이후 멤버 목록 단계 (6장) |

## 화면 10
| # | 앱 | ui_url | 화면 설명 |
|---|---|---|---|
| 1 | 토스증권 | https://uibowl.io/name/%ED%86%A0%EC%8A%A4%EC%A6%9D%EA%B6%8C?patterns=%EB%82%B4%EC%97%AD&patternName=%EA%B1%B0%EB%9E%98%EB%82%B4%EC%97%AD | 거래내역: 상단 탭 + 요약 블록, "전체" 드롭다운 필터 아래 날짜(좌)·항목/시각·유형(중)·금액(우) 3열 행 리스트 (4장) |
| 2 | 미니스탁 | https://uibowl.io/name/%EB%AF%B8%EB%8B%88%EC%8A%A4%ED%83%81?patterns=%EB%82%B4%EC%97%AD&patternName=%EC%9B%90%ED%99%94%20%EA%B1%B0%EB%9E%98%EB%82%B4%EC%97%AD | 원화 거래내역: 섹션 제목 우측 "최근 6개월·전체" 기간/유형 필터, 월 단위 그룹 헤더 아래 항목명·유형·날짜 / 증감·잔액 2열 행 |
| 3 | 토스 | https://uibowl.io/name/%ED%86%A0%EC%8A%A4?patterns=%EB%82%B4%EC%97%AD&patternName=%EA%B1%B0%EB%9E%98%20%EC%83%81%EC%84%B8 | 거래 상세: 상단 대상·금액 강조, 아래 라벨-값 행(카테고리·메모·상대·일시), 하단에 최근 이력 요약 섹션 |

## 화면 9
| # | 앱 | ui_url | 화면 설명 |
|---|---|---|---|
| 1 | 페이워크 | https://uibowl.io/name/%ED%8E%98%EC%9D%B4%EC%9B%8C%ED%81%AC?patterns=%EB%A9%94%EB%89%B4&patternName=%EA%B0%84%ED%8E%B8%EB%A9%94%EB%89%B4%20-%20%EA%B1%B0%EB%9E%98%EC%B2%98 | 간편메뉴-거래처: 그리드 메뉴의 "거래처" 진입 → 상단 검색 바, 최근 거래/전체 구분 리스트(행마다 더보기 메뉴), 하단 2버튼(연락처로 등록·거래처 등록) |
| 2 | 페이워크 | https://uibowl.io/name/%ED%8E%98%EC%9D%B4%EC%9B%8C%ED%81%AC?patterns=%ED%8E%B8%EC%A7%91%C2%B7%EC%88%98%EC%A0%95%ED%95%98%EA%B8%B0&patternName=%EA%B1%B0%EB%9E%98%EC%B2%98%EC%88%98%EC%A0%95 | 거래처수정: 목록 행의 메뉴에서 수정 진입, 모달로 수정/삭제를 확인하는 흐름 (3장) |
| 3 | 페이워크 | https://uibowl.io/name/%ED%8E%98%EC%9D%B4%EC%9B%8C%ED%81%AC?patterns=%ED%8E%B8%EC%A7%91%C2%B7%EC%88%98%EC%A0%95%ED%95%98%EA%B8%B0&patternName=%EA%B1%B0%EB%9E%98%EC%B2%98%EC%B6%94%EA%B0%80 | 거래처추가: 빈 상태(아이콘·안내문 + 주/보조 버튼 세로 2개) → 텍스트 필드 입력 폼 → 등록 완료 후 목록 복귀 (9장) |

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
