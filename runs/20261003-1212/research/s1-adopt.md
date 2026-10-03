# S1 채택 항목 — run 20261003-1212

구조·흐름·배치만 가져온다. 색·폰트·모서리는 docs/design.md를 따른다.
화면 15(랜딩)는 탭바 없음, 한 장짜리 정적 랜딩(캐러셀·소셜 로그인·대형 일러스트 배너는 가져오지 않음).
둘러보기(13·2·3)는 데모 학교 읽기 전용: 데이터는 보이되 쓰기 동작만 잠그고, 상단 띠 1개 + 잠금 탭 시 가입 유도 1단계로 통일.

## 화면 15
| # | ui_url | 가져올 것 |
|---|---|---|
| 1 | https://uibowl.io/name/%EB%9E%AD%ED%94%8C%EB%A6%AD%EC%8A%A4?patterns=%EC%98%A8%EB%B3%B4%EB%94%A9&imgId=cmswzxy9v0003l404lllro7wu | 소개 문구 위계(작은 리드 1줄 → 굵은 핵심 한 줄) → 기능 목록 → 하단 CTA 순서, CTA는 채움 버튼 1개 + 그 아래 텍스트형 보조로 강조 차이를 둠 |
| 2 | https://uibowl.io/name/CES%202026?patterns=%EC%98%A8%EB%B3%B4%EB%94%A9&imgId=cmk5qewa10003jy04k4wwtudg | 제목 → 짧은 서비스 설명 → 전폭 주 버튼 → 바로 아래 텍스트 버튼("Not now" 자리 = "둘러보기")의 2단 CTA 배치 |
| 3 | https://uibowl.io/name/%EC%B1%84%EB%B9%84?patterns=%EC%83%81%EC%84%B8%EC%A0%95%EB%B3%B4%20%28PDP%29&patternName=%EC%84%9C%EB%B9%84%EC%8A%A4%20%EC%86%8C%EA%B0%9C | 기능 카드 세로 목록: 전폭 카드 4장(학교별 분리·NEIS 학교 선택·QR 스캔·재고 부족 알림)을 세로로 쌓고 카드 안은 아이콘 → 기능명 → 1~2줄 설명 |
| 4 | https://uibowl.io/name/%EB%83%89%EC%9E%A5%EA%B3%A0%ED%84%B8%EA%B8%B0?patterns=%EC%98%A8%EB%B3%B4%EB%94%A9&imgId=cmohwstxe001vl204icjh4dc7 | 하단 CTA 3단 스택: 채움 "회원가입" → 외곽선 "로그인" → 맨 아래 밑줄 텍스트 링크 "로그인 없이 둘러보기"로 둘러보기를 가장 약한 위계에 둠 |
| 5 | https://uibowl.io/name/G%20car?patterns=%EC%98%A8%EB%B3%B4%EB%94%A9&imgId=cmo85ethb000fjs04bga7173h | 대안 배치: 우상단(건너뛰기 자리)에 텍스트 "둘러보기"를 두고 하단은 로그인·회원가입 2버튼만 — 데스크탑 상단 바 우측 배치에 적용 |

## 화면 13
| # | ui_url | 가져올 것 |
|---|---|---|
| 1 | https://uibowl.io/name/%EB%A7%88%EC%9D%B4%ED%98%84%EB%8C%80?patterns=%EB%A9%94%EC%9D%B8&patternName=%ED%99%88%ED%99%94%EB%A9%B4%20%28%EB%A1%9C%EA%B7%B8%EC%9D%B8%20%EC%A0%84%29 | 홈 최상단(학교명 아래) 가입 유도 카드: 문구 "가입하면 우리 학교 시약장을 관리할 수 있어요" + 카드 안 전폭 "회원가입" 버튼, 그 아래 홈 섹션·탭바는 그대로 유지 |
| 2 | https://uibowl.io/name/%ED%95%B4%ED%94%BC%EB%AC%B8%EB%8D%B0%EC%9D%B4?patterns=%EB%A9%94%EC%9D%B8&patternName=%EB%A1%9C%EA%B7%B8%EC%9D%B8%20%EC%A0%84 | 쓰기 바로가기(사용 기록·입고)에 자물쇠 아이콘을 붙여 잠금 표시, 잠긴 섹션 자리는 자물쇠 + "가입하고 시작해보세요" + 설명 1줄 + 버튼 카드로 대체 |
| 3 | https://uibowl.io/name/%EB%AF%B8%EB%9E%98%EC%97%90%EC%85%8B%EC%A6%9D%EA%B6%8C%20M-STOCK?patterns=%EB%A9%94%EC%9D%B8&patternName=%ED%99%88%20-%20%EC%9E%90%EC%82%B0%20-%20%EB%A1%9C%EA%B7%B8%EC%9D%B8%20%EC%A0%84 | 상단 1줄 안내 띠(아이콘 + 문구 + 우측 화살표) 위치 = 헤더 바로 아래 · 콘텐츠 위, 개인 영역(최근 내 사용 기록) 카드만 "가입하고 내 기록 보기" + 버튼으로 대체 |
| 4 | https://uibowl.io/name/%ED%95%9C%ED%8C%A8%EC%8A%A4?patterns=%EB%A9%94%EC%9D%B8&patternName=%EB%A1%9C%EA%B7%B8%EC%9D%B8%20%EC%A0%84 | 요약 카드 숫자는 데모 학교 값으로 그대로 보여주고, 액션(바로가기 그리드)도 노출 유지 — 잠금은 탭 순간에 처리해 화면 구조를 로그인 홈과 동일하게 둠 |
| 5 | https://uibowl.io/name/Kia?patterns=%EB%A7%88%EC%9D%B4%ED%8E%98%EC%9D%B4%EC%A7%80&patternName=%EB%B9%84%EB%A1%9C%EA%B7%B8%EC%9D%B8-%EB%8B%A4%ED%81%AC%EB%AA%A8%EB%93%9C | 잠긴 기능 행에 보조문구 "가입 후 사용할 수 있어요"를 1줄로 붙이는 방식 (아이콘·제목·화살표 행 구조는 유지) |

## 화면 2
| # | ui_url | 가져올 것 |
|---|---|---|
| 1 | https://uibowl.io/name/%EC%95%84%ED%8C%8C%ED%8A%B8%EC%95%84%EC%9D%B4?patterns=%EB%A7%88%EC%9D%B4%ED%8E%98%EC%9D%B4%EC%A7%80&patternName=%EB%B9%84%EB%A1%9C%EA%B7%B8%EC%9D%B8%ED%96%88%EC%9D%84%20%EA%B2%BD%EC%9A%B0 | 상단 띠 구조: 헤더 바로 아래 전폭 1줄 "샘플 학교 둘러보기 중 · 가입하면 우리 학교 시약을 관리해요"(좌) + 작은 "가입하기" 버튼(우), 13·2·3 모두 같은 위치·문구로 고정 |
| 2 | https://uibowl.io/name/%EC%8F%98%EC%B9%B4?patterns=%EB%A9%94%EC%9D%B8&patternName=%EB%A1%9C%EA%B7%B8%EC%9D%B8%20%EC%A0%84 | 목록은 전부 보여주고 쓰기 진입점(시약 추가 FAB)만 잠금 — 상단 띠가 스크롤로 사라지는 대안으로 하단 고정 가입 버튼 배치 참고 |
| 3 | https://uibowl.io/name/%EC%BD%94%EC%98%A4%EB%A1%B1%EB%AA%B0?patterns=%EB%B6%81%EB%A7%88%ED%81%AC%C2%B7%EC%9C%84%EC%8B%9C%EB%A6%AC%EC%8A%A4%ED%8A%B8&patternName=%EB%A1%9C%EA%B7%B8%EC%9D%B8%20%EC%A0%84 | 탭 일부 잠금: 탭바·세그먼트는 그대로 두고 잠긴 탭(사용 기록 입력·설정 등) 진입 시 본문 중앙에 안내 2줄 + 가입 버튼 1개의 빈 상태로 대체 |
| 4 | https://uibowl.io/name/%EC%BD%94%EC%98%A4%EB%A1%B1%EB%AA%B0?patterns=%EC%9E%A5%EB%B0%94%EA%B5%AC%EB%8B%88&imgId=cms36dumn0007l7041q8folw3 | 잠긴 버튼 탭 → 중앙 팝업 "회원가입이 필요한 기능이에요" + 취소/가입하기 2버튼 흐름, 목록 하단에 밑줄 텍스트 링크 "가입하고 우리 학교 시약 보기" 보조 유도 |

## 화면 3
| # | ui_url | 가져올 것 |
|---|---|---|
| 1 | https://uibowl.io/name/%EC%B1%84%EB%B9%84?patterns=%EB%A9%94%EC%9D%B8&imgId=cmoi0a0cw000kjv049hmrvovp | 쓰기 버튼(사용 기록·입고·수정) 탭 시 화면 이동 없이 중앙 팝업: 아이콘 → 1줄 제목 "가입하면 사용할 수 있어요" → 취소/가입하기 가로 2버튼 |
| 2 | https://uibowl.io/name/%ED%95%B4%ED%94%BC%EB%AC%B8%EB%8D%B0%EC%9D%B4?patterns=%EC%98%A8%EB%B3%B4%EB%94%A9&imgId=cmtwleyy0002ijr04dxtnh7zj | 가입 유도 문구 구조 "{동작}하려면 회원가입이 필요해요"(예: 사용 기록을 저장하려면) — 동작명을 문구에 넣어 왜 막혔는지 보여줌 |
| 3 | https://uibowl.io/name/%ED%8F%AC%EC%8A%A4%ED%85%94%EB%9F%AC?patterns=%EB%A1%9C%EA%B7%B8%EC%9D%B8%C2%B7%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85&imgId=cmr9wx3ii000bl804c5z1vixq | 유도 팝업 안 순서: 제목 → 이점 1줄("우리 학교 시약장을 따로 관리") → 주 버튼 "회원가입" → 보조 텍스트 "로그인", 닫기(X)로 둘러보기 복귀 |
| 4 | https://uibowl.io/name/%EC%BB%AC%EB%A6%AC?patterns=%EC%83%81%EC%84%B8%EC%A0%95%EB%B3%B4%20%28PDP%29&imgId=cmfyzh8s9000xkw04nno3avlo | 상세 하단 고정 액션 바 구조 유지(좌 보조 아이콘 버튼 + 우 전폭 "사용 기록" 주 버튼)하되 둘러보기에서는 주 버튼을 비활성 + 자물쇠 아이콘으로 표시, MSDS 보기는 활성 유지 |
