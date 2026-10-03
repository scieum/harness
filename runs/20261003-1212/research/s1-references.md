# S1 레퍼런스 — run 20261003-1212

대상 화면: 15 (docs/PRD.md §7) · 둘러보기 참고: 13 · 2 · 3 (input.json guest_screens)
검색: 화면 15 = runs/20261003-0112 레퍼런스 3개 재사용 + search_by_ocr_text "둘러보기"(온보딩), "로그인 없이"
둘러보기 = search_by_ocr_text "비회원으로", "로그인이 필요", "로그인하고", "체험 중", "가입하고", "로그인하면", "로그인 필요"(상세정보 PDP) / search_ui_patterns "로그인 전"(1·2쪽), "비로그인"

## 화면 15
| # | 앱 | ui_url | 화면 설명 |
|---|---|---|---|
| 1 | 랭플릭스 | https://uibowl.io/name/%EB%9E%AD%ED%94%8C%EB%A6%AD%EC%8A%A4?patterns=%EC%98%A8%EB%B3%B4%EB%94%A9&imgId=cmswzxy9v0003l404lllro7wu | 로그인 전 첫 화면: 상단 대형 비주얼, 하단에 3줄 헤드라인(작은 리드 1줄 + 강조 2줄) → 체크 아이콘 붙은 기능 3줄 세로 목록 → 전폭 채움 "시작하기" 버튼 → 그 아래 텍스트형 "이미 계정이 있습니다" (0112 재사용) |
| 2 | CES 2026 | https://uibowl.io/name/CES%202026?patterns=%EC%98%A8%EB%B3%B4%EB%94%A9&imgId=cmk5qewa10003jy04k4wwtudg | 비즈니스툴 웰컴: 상단 배너 이미지 → "Welcome to ..." 굵은 제목 → 서비스 설명 본문 → 전폭 채움 "Log in now" + 아래 텍스트 버튼 "Not now" (0112 재사용) |
| 3 | 채비 | https://uibowl.io/name/%EC%B1%84%EB%B9%84?patterns=%EC%83%81%EC%84%B8%EC%A0%95%EB%B3%B4%20%28PDP%29&patternName=%EC%84%9C%EB%B9%84%EC%8A%A4%20%EC%86%8C%EA%B0%9C | 서비스 소개: 좌측 정렬 2줄 리드 아래 기능별 전폭 카드를 세로로 쌓음, 카드마다 기능명 제목 → 설명 2~3줄 → 일러스트 (0112 재사용) |
| 4 | 냉장고털기 | https://uibowl.io/name/%EB%83%89%EC%9E%A5%EA%B3%A0%ED%84%B8%EA%B8%B0?patterns=%EC%98%A8%EB%B3%B4%EB%94%A9&imgId=cmohwstxe001vl204icjh4dc7 | 온보딩 마지막 장: 상단 중앙 제목 + 설명 2줄 → 앱 화면 목업 → 페이지 점 → 하단 전폭 채움 "로그인하고 시작하기" → 바로 아래 밑줄 텍스트 링크 "로그인 하지않고 둘러보기" |
| 5 | G car | https://uibowl.io/name/G%20car?patterns=%EC%98%A8%EB%B3%B4%EB%94%A9&imgId=cmo85ethb000fjs04bga7173h | 렌터카 시작 화면: 우상단 밑줄 텍스트 "둘러보기"(건너뛰기 자리), 중앙 대형 비주얼 캐러셀 + 페이지 점, 하단 "로그인"(외곽선)·"회원가입"(채움) 반반 가로 2버튼, 맨 아래 개인정보 처리방침 링크 |

## 화면 13
| # | 앱 | ui_url | 화면 설명 |
|---|---|---|---|
| 1 | 마이현대 | https://uibowl.io/name/%EB%A7%88%EC%9D%B4%ED%98%84%EB%8C%80?patterns=%EB%A9%94%EC%9D%B8&patternName=%ED%99%88%ED%99%94%EB%A9%B4%20%28%EB%A1%9C%EA%B7%B8%EC%9D%B8%20%EC%A0%84%29 | 로그인 전 홈: 상단 비주얼 아래 흰 카드 "편안한 모빌리티 라이프를 위해 로그인이 필요합니다" + 우측 앱 아이콘 + 카드 안 전폭 "로그인" 버튼, 그 아래 검색·서비스 바로가기는 그대로 노출, 하단 탭바 5개 유지 |
| 2 | 해피문데이 | https://uibowl.io/name/%ED%95%B4%ED%94%BC%EB%AC%B8%EB%8D%B0%EC%9D%B4?patterns=%EB%A9%94%EC%9D%B8&patternName=%EB%A1%9C%EA%B7%B8%EC%9D%B8%20%EC%A0%84 | 로그인 전 홈: 주간 달력 카드(기록 없음 상태) 안에 "월경일 기록"·"로그인" 버튼 나란히, 아래 오늘 기록 섹션, 자물쇠 일러스트가 붙은 카드 "로그인하고 시작해보세요" + 설명 2줄 + 전폭 "로그인" 버튼, 탭바 유지 |
| 3 | 미래에셋증권 M-STOCK | https://uibowl.io/name/%EB%AF%B8%EB%9E%98%EC%97%90%EC%85%8B%EC%A6%9D%EA%B6%8C%20M-STOCK?patterns=%EB%A9%94%EC%9D%B8&patternName=%ED%99%88%20-%20%EC%9E%90%EC%82%B0%20-%20%EB%A1%9C%EA%B7%B8%EC%9D%B8%20%EC%A0%84 | 로그인 전 홈(자산 탭): 상단 탭·하위 탭은 그대로, 상단에 1줄 안내 배너, "순자산" 카드 본문을 일러스트 + "로그인하고 자산보기" + 전폭 "로그인" 버튼으로 대체, 아래 섹션은 계속 노출 |
| 4 | 한패스 | https://uibowl.io/name/%ED%95%9C%ED%8C%A8%EC%8A%A4?patterns=%EB%A9%94%EC%9D%B8&patternName=%EB%A1%9C%EA%B7%B8%EC%9D%B8%20%EC%A0%84 | 로그인 전 홈: 최상단 지갑 카드의 잔액 자리를 "로그인 해주세요." 큰 문구로 대체, 카드 하단 "충전하기·ATM 출금" 액션과 아래 QR·송금 바로가기 그리드는 그대로 노출 |
| 5 | Kia | https://uibowl.io/name/Kia?patterns=%EB%A7%88%EC%9D%B4%ED%8E%98%EC%9D%B4%EC%A7%80&patternName=%EB%B9%84%EB%A1%9C%EA%B7%B8%EC%9D%B8-%EB%8B%A4%ED%81%AC%EB%AA%A8%EB%93%9C | 비로그인 탭 화면: 최상단 큰 카드 "지금 로그인하고 편안한 모빌리티 라이프를 경험하세요." + 카드 안 전폭 "로그인", 아래 기능 행에 보조문구 "로그인 후 차량 지원 여부에 따라 사용 가능", 리포트 섹션은 빈 틀로 노출 |

## 화면 2
| # | 앱 | ui_url | 화면 설명 |
|---|---|---|---|
| 1 | 아파트아이 | https://uibowl.io/name/%EC%95%84%ED%8C%8C%ED%8A%B8%EC%95%84%EC%9D%B4?patterns=%EB%A7%88%EC%9D%B4%ED%8E%98%EC%9D%B4%EC%A7%80&patternName=%EB%B9%84%EB%A1%9C%EA%B7%B8%EC%9D%B8%ED%96%88%EC%9D%84%20%EA%B2%BD%EC%9A%B0 | 비로그인 탭 화면: 제목 바로 아래 한 줄 띠 "로그인 후 이용할 수 있어요"(좌) + 작은 알약형 "로그인" 버튼(우), 그 아래 아이콘 바로가기·목록은 그대로 노출 |
| 2 | 쏘카 | https://uibowl.io/name/%EC%8F%98%EC%B9%B4?patterns=%EB%A9%94%EC%9D%B8&patternName=%EB%A1%9C%EA%B7%B8%EC%9D%B8%20%EC%A0%84 | 로그인 전 메인: 서비스 카드 목록은 전부 노출, 화면 하단에 떠 있는 전폭 "로그인하기" 고정 버튼으로 스크롤 중에도 가입 유도 유지 |
| 3 | 코오롱몰 | https://uibowl.io/name/%EC%BD%94%EC%98%A4%EB%A1%B1%EB%AA%B0?patterns=%EB%B6%81%EB%A7%88%ED%81%AC%C2%B7%EC%9C%84%EC%8B%9C%EB%A6%AC%EC%8A%A4%ED%8A%B8&patternName=%EB%A1%9C%EA%B7%B8%EC%9D%B8%20%EC%A0%84 | 로그인 전 위시리스트 탭: 상단 세그먼트 탭(상품·브랜드)은 유지, 본문 중앙에 "로그인하고 마음에 드는 상품을 저장해보세요." 2줄 + 외곽선 "로그인 하기" 버튼, 하단 탭바 유지 (탭 단위 잠금) |
| 4 | 코오롱몰 | https://uibowl.io/name/%EC%BD%94%EC%98%A4%EB%A1%B1%EB%AA%B0?patterns=%EC%9E%A5%EB%B0%94%EA%B5%AC%EB%8B%88&imgId=cms36dumn0007l7041q8folw3 | 로그인 전 장바구니: 빈 상태 문구 → "쇼핑하기" 버튼 → 밑줄 텍스트 링크 "로그인하고 멤버십 혜택 확인하기", 동작 시 중앙 팝업 "로그인이 필요한 서비스입니다. 로그인 페이지로 이동하시겠습니까?" + 취소/확인 2버튼 |

## 화면 3
| # | 앱 | ui_url | 화면 설명 |
|---|---|---|---|
| 1 | 채비 | https://uibowl.io/name/%EC%B1%84%EB%B9%84?patterns=%EB%A9%94%EC%9D%B8&imgId=cmoi0a0cw000kjv049hmrvovp | 로그인 전 메인에서 기능 탭 시: 배경 화면을 어둡게 두고 중앙 팝업에 느낌표 아이콘 + "로그인이 필요한 서비스입니다" + 하단 취소/확인 가로 2버튼 |
| 2 | 해피문데이 | https://uibowl.io/name/%ED%95%B4%ED%94%BC%EB%AC%B8%EB%8D%B0%EC%9D%B4?patterns=%EC%98%A8%EB%B3%B4%EB%94%A9&imgId=cmtwleyy0002ijr04dxtnh7zj | 저장 동작 시 전체 화면 게이트: 좌상단 뒤로가기, 좌측 정렬 2줄 제목 "세팅을 저장하려면 로그인이 필요해요!", 하단에 말풍선 배지 "3초만에 가입하기" + 전폭 버튼 세로 3개 + 텍스트 "도움말" |
| 3 | 포스텔러 | https://uibowl.io/name/%ED%8F%AC%EC%8A%A4%ED%85%94%EB%9F%AC?patterns=%EB%A1%9C%EA%B7%B8%EC%9D%B8%C2%B7%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85&imgId=cmr9wx3ii000bl804c5z1vixq | 기능 진입 시 로그인 게이트: 우상단 닫기(X), 2줄 제목 "운세 이용을 위해 로그인이 필요해요." → 이점 1줄 + "회원가입은 30초면 충분해요." → 일러스트 → 로그인 버튼 세로 목록 → 하단 안내 각주 |
| 4 | 컬리 | https://uibowl.io/name/%EC%BB%AC%EB%A6%AC?patterns=%EC%83%81%EC%84%B8%EC%A0%95%EB%B3%B4%20%28PDP%29&imgId=cmfyzh8s9000xkw04nno3avlo | 상품 상세: 상단 뒤로가기 + 제목, 상단 세그먼트 탭(상품설명·상세정보·후기·문의), 본문 아코디언 안내, 하단 고정 액션 바(좌 하트 아이콘 버튼 + 우 전폭 주 버튼) |
