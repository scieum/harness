# S1 가져올 것 — runs/20261013-1938

구조·흐름·배치만 적는다. 색·글꼴·모서리는 design.md / rules.json이 정한다.
출처: uibowl 도구를 쓸 수 없어 새 검색 없이 이전 기록의 실제 ui_url만 썼다(s1-references.md 머리 참고).

## 화면 2
| # | ui_url | 가져올 것 |
|---|---|---|
| 1 | https://uibowl.io/website/%EB%8B%B9%EA%B7%BC%20%EB%B9%84%EC%A6%88%EB%8B%88%EC%8A%A4?patterns=%EC%83%81%EC%84%B8%EC%A0%95%EB%B3%B4%20%28PDP%29&imgId=cmso6dgem00ualf04cqgg6fh8 | 모바일 머리 왼쪽에 상위 묶음 이름을 쓴 되돌아가기 '‹ 관리'를 두고 그 아래 제목 — ☰·inventory-switch 자리는 비운다 |
| 2 | https://uibowl.io/name/%EC%BD%94%EC%9B%A8%EC%9D%B4%20IoCare%2B?patterns=%EC%84%A4%EC%A0%95&patternName=%EB%A9%A4%EB%B2%84%20%EA%B4%80%EB%A6%AC | '시약 전체 삭제' 진입은 목록 맨 아래(또는 관리 메뉴 끝)에 텍스트형으로 따로 떼어 admin에게만 둔다 |
| 3 | https://uibowl.io/name/%EC%99%93%EC%84%AD?patterns=%EC%B7%A8%EC%86%8C%ED%95%98%EA%B8%B0&imgId=cmqt89aob001pjl044nphhj04 | 2-wipe 확인 본문에 지워지는 범위(시약 N개·기록 포함 여부)와 되돌릴 수 없음을 결과 설명 문장으로 쓰고 돌아가기/삭제 2버튼 |
| 4 | https://uibowl.io/name/%EB%8B%A4%EA%B8%80%EB%A1%9C?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&patternName=%EC%9C%A0%ED%8A%9C%EB%B8%8C%20%EB%A7%81%ED%81%AC%20%EC%97%85%EB%A1%9C%EB%93%9C | 학교명 입력칸 하나 + 아래 삭제 버튼: 입력값이 학교명과 정확히 같을 때만 버튼이 켜지고 그 전에는 비활성 |
| 5 | https://uibowl.io/name/%EC%85%94%ED%81%B4?patterns=%EC%B7%A8%EC%86%8C%ED%95%98%EA%B8%B0&imgId=cmrt4shpb0007l104b7hb2rnd | 확인 시트 순서 = 질문 제목 → 설명 2줄 → 강조 안내 1줄('샘플고등학교'를 입력하세요) → 입력칸 → 2버튼 가로 |

## 화면 10
| # | ui_url | 가져올 것 |
|---|---|---|
| 1 | https://uibowl.io/website/%EB%A6%AC%EB%94%94?patterns=%EB%82%B4%EC%97%AD&imgId=cmuq7e6jd000wjs046c714kre | 기록 삭제 모달 첫 블록 = 빠른 기간 세그먼트 + 시작·끝 날짜 2칸, 바로 아래 '해당 기록 N건' 미리보기 줄 |
| 2 | https://uibowl.io/website/%EC%82%AC%EB%B0%A9%EB%84%B7?patterns=%ED%8E%B8%EC%A7%91%C2%B7%EC%88%98%EC%A0%95%ED%95%98%EA%B8%B0&imgId=cmu4rqsym001rl504326axccl | 날짜 범위 옆 빠른 버튼 줄 배치와 건수 줄을 왼쪽, 실행 동작을 오른쪽에 두는 한 줄 구성 |
| 3 | https://uibowl.io/website/%EC%9C%84%EC%8B%9C%EC%BC%93?patterns=%ED%95%84%ED%84%B0&imgId=cmunb6fr3003ul2040dnbgwff | 주 버튼 글자에 미리보기 건수를 넣는다('기록 N건 삭제'), 0건이면 버튼 비활성 |
| 4 | https://uibowl.io/name/%EC%91%A5%EC%91%A5%EC%B0%B0%EC%B9%B5?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&patternName=%EC%9D%BC%EA%B8%B0%2F%EC%88%98%EC%9C%A0%ED%85%80%20%ED%83%AD%20-%20%EC%88%98%EC%9C%A0%ED%85%80%20-%20%EB%82%B4%EC%97%AD%EC%82%AD%EC%A0%9C | 흐름 = 기록 목록 머리의 '기록 삭제'(admin) → 가운데 모달(되돌릴 수 없음 안내) → 삭제 후 목록 복귀 |
| 5 | https://uibowl.io/website/%EB%8B%B9%EA%B7%BC%20%EB%B9%84%EC%A6%88%EB%8B%88%EC%8A%A4?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&imgId=cmso6f8zf000rl704l4qn0f5w | 데스크톱 모달 구성: 필드 세로 나열(기간 → 학교명 입력) + 오른쪽 아래 실행 버튼은 학교명 일치 전 비활성 |

## 화면 13
| # | ui_url | 가져올 것 |
|---|---|---|
| 1 | https://uibowl.io/name/%ED%8E%98%EC%9D%B4%EC%9B%8C%ED%81%AC?patterns=%EB%A9%94%EC%9D%B8&imgId=cmtzo55qv002rl7047rsl7n07 | 하단 탭에 관리 탭을 따로 두고 홈은 오늘 할 일·바로 실행만 맡게 역할을 나눈다 (탭 순서 홈·관리·QR 스캔·기록) |
| 2 | https://uibowl.io/name/%ED%8E%98%EC%9D%B4%ED%9E%88%EC%96%B4?patterns=%EB%A9%94%EC%9D%B8&imgId=cmnfmxnhh0003l8045z9h1r15 | ☰를 없앤 뒤 머리는 학교명 + 알림 정도의 얇은 한 줄만 남긴다 |
| 3 | https://uibowl.io/name/%ED%97%A4%EC%9D%B4%EC%98%81%20%EC%BA%A0%ED%8D%BC%EC%8A%A4?patterns=%EB%A9%94%EC%9D%B8&imgId=cmmbj8sqh0004lh048k4kbkqd | 전체 메뉴 진입을 머리 아이콘이 아니라 하단 탭 하나로 옮기는 구조(우리는 '관리' 탭) |
| 4 | https://uibowl.io/name/Kia?patterns=%EB%A9%94%EC%9D%B8&imgId=cmpur0a3g000dl504qp9o8f4s | 기존 홈 상태 카드 배치는 그대로 두고 '… N건 >'으로 관리 하위 화면에 이어지는 연결만 유지 |

## 화면 17
| # | ui_url | 가져올 것 |
|---|---|---|
| 1 | https://uibowl.io/website/%EB%8B%B9%EA%B7%BC%20%EB%B9%84%EC%A6%88%EB%8B%88%EC%8A%A4?patterns=%EC%83%81%EC%84%B8%EC%A0%95%EB%B3%B4%20%28PDP%29&imgId=cmso6dgem00ualf04cqgg6fh8 | 모바일 머리 왼쪽 '‹ 관리' 되돌아가기 + 제목 '기자재·장비', ☰ 자리 없음 — 화면 2와 같은 머리 |
| 2 | https://uibowl.io/name/%ED%8E%98%EC%9D%B4%EC%9B%8C%ED%81%AC?patterns=%EB%A9%94%EB%89%B4&patternName=%EA%B0%84%ED%8E%B8%EB%A9%94%EB%89%B4%20-%20%EA%B1%B0%EB%9E%98%EC%B2%98 | 관리 허브 행을 눌러 들어온 하위 화면도 검색·목록·하단 동작 배치는 그대로 유지 |
| 3 | https://uibowl.io/name/Kia?patterns=%EB%82%B4%EC%97%AD&imgId=cmpuohezz0015k104h5xybl51 | 기존 행 카드 구조(이름 + 조건 한 줄 + 상태 배지)를 바꾸지 않는다 — 머리만 교체 |
| 4 | https://uibowl.io/name/%ED%8E%98%EC%9D%B4%ED%9E%88%EC%96%B4?patterns=%EB%A9%94%EC%9D%B8&imgId=cmnfmxdij001fl204l8u0mu8b | 하위 화면에 있어도 하단 탭은 '관리'가 활성인 채로 유지 |

## 화면 18
| # | ui_url | 가져올 것 |
|---|---|---|
| 1 | https://uibowl.io/website/%EC%82%AC%EB%B0%A9%EB%84%B7?patterns=%EB%A9%94%EB%89%B4&imgId=cmu4rpvqh000cjy04yej53zvj | 묶음 3개(예: 재고·시설·학교 운영)마다 묶음 제목 아래 행 목록, 행 = 아이콘 + 이름 + 설명 한 줄 + › |
| 2 | https://uibowl.io/name/%ED%8E%98%EC%9D%B4%ED%9E%88%EC%96%B4?patterns=%EB%A9%94%EC%9D%B8&imgId=cmnfmxdij001fl204l8u0mu8b | 관리 탭 첫 화면 맨 위에 요약 줄(시약 N · 장비 N · 부족 N)을 한 줄로 두고 그 아래 묶음 목록 |
| 3 | https://uibowl.io/name/%ED%8E%98%EC%9D%B4%EC%9B%8C%ED%81%AC?patterns=%EB%A9%94%EC%9D%B8&imgId=cmtzo55qv002rl7047rsl7n07 | 관리는 홈과 분리된 탭 화면 — 머리는 제목 '관리'만, 되돌아가기 없음 |
| 4 | https://uibowl.io/website/%EC%9E%94%EB%94%94?patterns=%EB%8C%80%EC%8B%9C%EB%B3%B4%EB%93%9C&imgId=cmpz4uprc0003ie04h1ia0clk | admin 전용 항목(사용자 관리 등)은 별도 묶음으로 모으고, 역할에 따라 묶음 자체를 숨긴다(둘러보기 18-guest는 예시 값 + 쓰기 항목 잠금) |
| 5 | https://uibowl.io/name/%EC%BD%94%EC%9B%A8%EC%9D%B4%20IoCare%2B?patterns=%EC%84%A4%EC%A0%95&patternName=%EB%A9%A4%EB%B2%84%20%EA%B4%80%EB%A6%AC | 시약 전체 삭제·기록 삭제 같은 위험 진입은 허브 맨 아래 따로 떼어 admin에게만 보인다 |
