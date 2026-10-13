# S1 레퍼런스 — runs/20261013-1938

주제: 개발 세션 요청 9 — 모바일 하단 탭 홈 · 관리 · QR 스캔 · 기록, 화면 18 관리 허브(묶음 3 + 요약 줄, 둘러보기 18-guest), 관리 아래 하위 화면 '‹ 관리' 머리(2·17), ☰·inventory-switch 없앰(2·13·17), 시약 전체 삭제(2-wipe)·기록 삭제(10-record-wipe) — admin + 학교명 직접 입력해야 켜지는 삭제 버튼, 기간 지정 + 미리보기 건수 (rules.json 1.29)

출처: 이번 실행에서도 uibowl 검색 도구를 쓸 수 없어 새 검색을 하지 못했다. 아래 ui_url은 모두 이전 기록(refs/uibowl-home-nav-20261002.md, refs/uibowl-research-20261002.md, refs/uibowl-desktop-web-20261008.md, runs/20261002-1032·20261008-0936·20261010-1340·20261011-0813·20261012-0939 S1 문서)에 남은 uibowl 검색 결과 값을 그대로 옮긴 것이며, 새로 만든 URL은 없다. 이전 기록에 "이름을 직접 입력해야 켜지는 삭제 버튼"(GitHub 저장소 삭제식) 화면 자체는 없어서, 가장 가까운 구조(위험 동작을 맨 아래로 떼어 두기 · 되돌릴 수 없음을 알리는 확인 모달 · 입력 전 비활성인 실행 버튼)를 조합해 근거로 삼았다.

## 화면 2
| # | 앱 | ui_url | 화면 설명 |
|---|---|---|---|
| 1 | 당근 비즈니스 | https://uibowl.io/website/%EB%8B%B9%EA%B7%BC%20%EB%B9%84%EC%A6%88%EB%8B%88%EC%8A%A4?patterns=%EC%83%81%EC%84%B8%EC%A0%95%EB%B3%B4%20%28PDP%29&imgId=cmso6dgem00ualf04cqgg6fh8 | 하위 페이지 맨 위 "↖ 광고 홈" 되돌아가기 칩 → 상태 라벨 → 큰 제목 순서, 상위 묶음으로 돌아가는 자리가 제목 위 (refs/uibowl-desktop-web-20261008.md 재사용) |
| 2 | 코웨이 IoCare+ | https://uibowl.io/name/%EC%BD%94%EC%9B%A8%EC%9D%B4%20IoCare%2B?patterns=%EC%84%A4%EC%A0%95&patternName=%EB%A9%A4%EB%B2%84%20%EA%B4%80%EB%A6%AC | 장소 관리 화면: 정보 목록·멤버 섹션 아래, 화면 맨 아래에 텍스트형 '장소 삭제'(위험 동작)를 따로 떼어 둠 (refs/uibowl-research-20261002.md 재사용) |
| 3 | 왓섭 | https://uibowl.io/name/%EC%99%93%EC%84%AD?patterns=%EC%B7%A8%EC%86%8C%ED%95%98%EA%B8%B0&imgId=cmqt89aob001pjl044nphhj04 | 삭제 모달: 질문형 제목 + 처리 결과를 설명하는 본문("기록도 남지 않아요") + 돌아가기/삭제하기 2버튼 (run 20261012-0939 재사용) |
| 4 | 다글로 | https://uibowl.io/name/%EB%8B%A4%EA%B8%80%EB%A1%9C?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&patternName=%EC%9C%A0%ED%8A%9C%EB%B8%8C%20%EB%A7%81%ED%81%AC%20%EC%97%85%EB%A1%9C%EB%93%9C | 상단 입력 필드 + 하단 고정 실행 버튼, 입력 전에는 실행 버튼 비활성 → 입력하면 켜짐 (run 20261002-1032 재사용) |
| 5 | 셔클 | https://uibowl.io/name/%EC%85%94%ED%81%B4?patterns=%EC%B7%A8%EC%86%8C%ED%95%98%EA%B8%B0&imgId=cmrt4shpb0007l104b7hb2rnd | 확인 모달: 질문 제목 · 설명 2줄 · 강조 안내 1줄, 아니요/네 두 버튼 가로 배치 (run 20261012-0939 재사용) |

## 화면 10
| # | 앱 | ui_url | 화면 설명 |
|---|---|---|---|
| 1 | 리디 | https://uibowl.io/website/%EB%A6%AC%EB%94%94?patterns=%EB%82%B4%EC%97%AD&imgId=cmuq7e6jd000wjs046c714kre | (PC) 회색 박스 안 기간 세그먼트(오늘/7일/15일/1개월/3개월/1년) + 날짜 범위 2칸 + "조회", 아래 "총 0건" (refs/uibowl-desktop-web-20261008.md 재사용) |
| 2 | 사방넷 | https://uibowl.io/website/%EC%82%AC%EB%B0%A9%EB%84%B7?patterns=%ED%8E%B8%EC%A7%91%C2%B7%EC%88%98%EC%A0%95%ED%95%98%EA%B8%B0&imgId=cmu4rqsym001rl504326axccl | (PC) 날짜 범위 옆 빠른 버튼(오늘/어제/7일/당월/최근3개월), 그 아래 "자료수 0 건" 왼쪽 · 동작 버튼 오른쪽 (refs/uibowl-desktop-web-20261008.md 재사용) |
| 3 | 위시켓 | https://uibowl.io/website/%EC%9C%84%EC%8B%9C%EC%BC%93?patterns=%ED%95%84%ED%84%B0&imgId=cmunb6fr3003ul2040dnbgwff | (PC) 큰 조건 모달, 바닥 왼쪽 "필터 초기화" / 오른쪽 주 버튼 "66,663개의 프로젝트 보기" — 결과 개수를 버튼 글자에 넣음 (refs/uibowl-desktop-web-20261008.md 재사용) |
| 4 | 쑥쑥찰칵 | https://uibowl.io/name/%EC%91%A5%EC%91%A5%EC%B0%B0%EC%B9%B5?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&patternName=%EC%9D%BC%EA%B8%B0%2F%EC%88%98%EC%9C%A0%ED%85%80%20%ED%83%AD%20-%20%EC%88%98%EC%9C%A0%ED%85%80%20-%20%EB%82%B4%EC%97%AD%EC%82%AD%EC%A0%9C | 기록 삭제 흐름: 삭제 진입 → 가운데 모달로 되돌릴 수 없음을 안내 → 확인 후 목록 복귀 (run 20261010-1340 재사용) |
| 5 | 당근 비즈니스 | https://uibowl.io/website/%EB%8B%B9%EA%B7%BC%20%EB%B9%84%EC%A6%88%EB%8B%88%EC%8A%A4?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&imgId=cmso6f8zf000rl704l4qn0f5w | (PC) 가운데 모달(약 420px), 필드 세로 나열, 오른쪽 아래 "완료"는 입력 전 비활성 (refs/uibowl-desktop-web-20261008.md 재사용) |

## 화면 13
| # | 앱 | ui_url | 화면 설명 |
|---|---|---|---|
| 1 | 페이워크 | https://uibowl.io/name/%ED%8E%98%EC%9D%B4%EC%9B%8C%ED%81%AC?patterns=%EB%A9%94%EC%9D%B8&imgId=cmtzo55qv002rl7047rsl7n07 | 홈: 하단 탭 5개(홈/문서함/사업 관리/정산 내역/더보기), 홈 그리드는 '만들기' 동작, 탭은 '보관함/관리' 화면으로 역할 분리 (refs/uibowl-home-nav-20261002.md 재사용) |
| 2 | 페이히어 | https://uibowl.io/name/%ED%8E%98%EC%9D%B4%ED%9E%88%EC%96%B4?patterns=%EB%A9%94%EC%9D%B8&imgId=cmnfmxnhh0003l8045z9h1r15 | 홈: 탭 4개(홈/나의 매장/혜택/더보기), 상단은 사용자명+알림만 있는 얇은 머리, 활성 탭은 아이콘·라벨만 진하게 (refs/uibowl-home-nav-20261002.md 재사용) |
| 3 | 헤이영 캠퍼스 | https://uibowl.io/name/%ED%97%A4%EC%9D%B4%EC%98%81%20%EC%BA%A0%ED%8D%BC%EC%8A%A4?patterns=%EB%A9%94%EC%9D%B8&imgId=cmmbj8sqh0004lh048k4kbkqd | 머리에 학교 로고 + 아이콘, 첫 카드 안 'QR' 버튼, 하단 탭에 '전체 메뉴'를 두어 메뉴 진입을 탭으로 처리 (refs/uibowl-home-nav-20261002.md 재사용) |
| 4 | Kia | https://uibowl.io/name/Kia?patterns=%EB%A9%94%EC%9D%B8&imgId=cmpur0a3g000dl504qp9o8f4s | 홈 '내 차의 상태' 카드 + '소모품 교체 1건 >' 카드 — 점검 필요 건수를 제목 숫자로 (run 20261011-0813 재사용) |

## 화면 17
| # | 앱 | ui_url | 화면 설명 |
|---|---|---|---|
| 1 | 당근 비즈니스 | https://uibowl.io/website/%EB%8B%B9%EA%B7%BC%20%EB%B9%84%EC%A6%88%EB%8B%88%EC%8A%A4?patterns=%EC%83%81%EC%84%B8%EC%A0%95%EB%B3%B4%20%28PDP%29&imgId=cmso6dgem00ualf04cqgg6fh8 | 하위 페이지 맨 위 "↖ 광고 홈" 되돌아가기 칩, 그 아래 제목 — 상위 묶음 이름을 되돌아가기 글자로 씀 (refs/uibowl-desktop-web-20261008.md 재사용) |
| 2 | 페이워크 | https://uibowl.io/name/%ED%8E%98%EC%9D%B4%EC%9B%8C%ED%81%AC?patterns=%EB%A9%94%EB%89%B4&patternName=%EA%B0%84%ED%8E%B8%EB%A9%94%EB%89%B4%20-%20%EA%B1%B0%EB%9E%98%EC%B2%98 | 간편메뉴 그리드에서 '거래처'를 눌러 들어간 하위 화면: 상단 검색 바, 구분 목록, 하단 2버튼 (run 20261002-1032 재사용) |
| 3 | Kia | https://uibowl.io/name/Kia?patterns=%EB%82%B4%EC%97%AD&imgId=cmpuohezz0015k104h5xybl51 | 보증 항목 목록: 행마다 카드, 굵은 항목명 + 조건 한 줄, 오른쪽 위 작은 상태 배지 (run 20261011-0813 재사용) |
| 4 | 페이히어 | https://uibowl.io/name/%ED%8E%98%EC%9D%B4%ED%9E%88%EC%96%B4?patterns=%EB%A9%94%EC%9D%B8&imgId=cmnfmxdij001fl204l8u0mu8b | '나의 매장' 탭 화면: 맨 위 4×2 관리 그리드, 그 아래 현황 요약, 하단 탭 '나의 매장' 활성 유지 (refs/uibowl-home-nav-20261002.md 재사용) |

## 화면 18
| # | 앱 | ui_url | 화면 설명 |
|---|---|---|---|
| 1 | 사방넷 | https://uibowl.io/website/%EC%82%AC%EB%B0%A9%EB%84%B7?patterns=%EB%A9%94%EB%89%B4&imgId=cmu4rpvqh000cjy04yej53zvj | (PC) 전체 메뉴: 묶음(서비스관리/상품관리/주문관리/재고관리 …)마다 아이콘 + 제목 + 설명 한 줄, 그 아래 항목 목록 (refs/uibowl-desktop-web-20261008.md 재사용) |
| 2 | 페이히어 | https://uibowl.io/name/%ED%8E%98%EC%9D%B4%ED%9E%88%EC%96%B4?patterns=%EB%A9%94%EC%9D%B8&imgId=cmnfmxdij001fl204l8u0mu8b | '나의 매장' 탭: 관리 기능 그리드 + 아래 매출 현황 요약, 하단 탭에서 관리 탭이 활성 (refs/uibowl-home-nav-20261002.md 재사용) |
| 3 | 페이워크 | https://uibowl.io/name/%ED%8E%98%EC%9D%B4%EC%9B%8C%ED%81%AC?patterns=%EB%A9%94%EC%9D%B8&imgId=cmtzo55qv002rl7047rsl7n07 | 하단 탭 5개 중 '사업 관리' 탭을 따로 두어 관리 화면을 홈과 분리 (refs/uibowl-home-nav-20261002.md 재사용) |
| 4 | 잔디 | https://uibowl.io/website/%EC%9E%94%EB%94%94?patterns=%EB%8C%80%EC%8B%9C%EB%B3%B4%EB%93%9C&imgId=cmpz4uprc0003ie04h1ia0clk | (PC) 관리자 영역 메뉴(대시보드/팀 관리/멤버 관리/메시지 설정/다운로드 기록/보안 설정/결제 정보)를 한 목록으로 묶고, 섹션 제목 오른쪽에 요약 칩 2개 (refs/uibowl-desktop-web-20261008.md 재사용) |
| 5 | 코웨이 IoCare+ | https://uibowl.io/name/%EC%BD%94%EC%9B%A8%EC%9D%B4%20IoCare%2B?patterns=%EC%84%A4%EC%A0%95&patternName=%EB%A9%A4%EB%B2%84%20%EA%B4%80%EB%A6%AC | 관리 화면: 정보 목록 → 멤버 섹션 → 맨 아래 위험 동작 분리 (refs/uibowl-research-20261002.md 재사용) |
