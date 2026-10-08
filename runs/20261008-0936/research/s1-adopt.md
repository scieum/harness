# S1 가져올 것 — run 20261008-0936

구조·흐름·배치만. 색·폰트·모서리는 docs/design.md 와 rules.json 을 따른다.

## 화면 2
| # | ui_url | 가져올 것 |
|---|---|---|
| 1 | https://uibowl.io/website/%EB%A6%AC%EC%BA%90%EC%B9%98?patterns=%EA%B2%80%EC%83%89&imgId=cmihk0pui000pl804eqhg1j1k | 목록 머리 3줄(제목+개수 / 검색+주 버튼 오른쪽 위, 필터 칩 줄, 필터 왼쪽·내보내기 오른쪽) + 체크박스 열·정렬 열 제목 데이터 테이블 |
| 2 | https://uibowl.io/website/%EB%A6%AC%EC%BA%90%EC%B9%98?patterns=%EB%82%B4%EC%97%AD&imgId=cmihk42gx0007jp04md6giwds | 행 선택 시 바닥 가운데 떠 있는 일괄 동작 바("N개 선택됨 · MSDS 찾기 · ×"), 툴바는 그대로 둔다 |
| 3 | https://uibowl.io/website/%EB%BF%8C%EB%A6%AC%EC%98%A4?patterns=%EB%82%B4%EC%97%AD&imgId=cmu1vvu9l000vjv04jiybtxr8 | 제목 아래 요약 한 줄(재고 부족 N · MSDS 없음 N) 위치와 표 아래 가운데 페이지 번호 |
| 4 | https://uibowl.io/website/%EC%82%AC%EB%B0%A9%EB%84%B7?patterns=%ED%8E%B8%EC%A7%91%C2%B7%EC%88%98%EC%A0%95%ED%95%98%EA%B8%B0&imgId=cmu4rqsym001rl504326axccl | 필터 결과 0건일 때 표 머리는 남기고 표 안에 빈 상태 문구 |

## 화면 3
| # | ui_url | 가져올 것 |
|---|---|---|
| 1 | https://uibowl.io/website/%EB%A6%AC%EC%BA%90%EC%B9%98?patterns=%EB%82%B4%EC%97%AD&imgId=cmihk1yub0005li04jv0iyqbi | 목록 위 오른쪽 드로어(어둡게 하지 않음), 머리 닫기·⋮, 순서 = 시약명 → 상태 칩 → 탭 → 항목|값 2열 섹션 |
| 2 | https://uibowl.io/website/%EB%A6%AC%EC%BA%90%EC%B9%98?patterns=%EB%82%B4%EC%97%AD&imgId=cmihk1ytc0003li04whm7bprz | 드로어 열린 동안 왼쪽 목록 머리(제목·검색)는 그대로 보이고 선택 행만 강조 |
| 3 | https://uibowl.io/website/%EC%B1%84%EB%84%90%ED%86%A1?patterns=AI&imgId=cmudq46a2002ul4041tszo60n | 드로어 안 정보 묶음(보관 위치·재주문 기준·MSDS)을 접히는 섹션으로 나누는 방식 |
| 4 | https://uibowl.io/website/%EB%8B%B9%EA%B7%BC%20%EB%B9%84%EC%A6%88%EB%8B%88%EC%8A%A4?patterns=%EC%83%81%EC%84%B8%EC%A0%95%EB%B3%B4%20%28PDP%29&imgId=cmso6dgem00ualf04cqgg6fh8 | 무거운 편집(위치 바꾸기 피커 등)은 드로어 대신 페이지로 넘기고 맨 위 "← 시약 목록" 되돌아가기 |

## 화면 4
| # | ui_url | 가져올 것 |
|---|---|---|
| 1 | https://uibowl.io/website/%EB%8B%B9%EA%B7%BC%20%EB%B9%84%EC%A6%88%EB%8B%88%EC%8A%A4?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&imgId=cmso6f8zf000rl704l4qn0f5w | 짧은 기록 입력 = 가운데 작은 모달, 필드 세로(시약·양·사용일), 저장 버튼은 입력 전 비활성 |
| 2 | https://uibowl.io/website/%EB%A6%AC%EC%BA%90%EC%B9%98?patterns=%EB%82%B4%EC%97%AD&imgId=cmihk1yub0005li04jv0iyqbi | 시약 상세 드로어 안에서 바로 사용 기록을 여는 경우, 드로어 아래 고정 버튼 줄에서 시작 |
| 3 | https://uibowl.io/website/%EB%A6%AC%EC%BA%90%EC%B9%98?patterns=%EB%82%B4%EC%97%AD&imgId=cmihk42lp000jjp0436gwgn7n | 저장 후 오른쪽 아래 토스트(✓ + "기록했어요" + 시약명 한 줄), 화면 이동 없음 |
| 4 | https://uibowl.io/website/%EB%A6%AC%EB%94%94?patterns=%EB%82%B4%EC%97%AD&imgId=cmuq7e6jd000wjs046c714kre | 사용일 = 빠른 선택(오늘·어제) + 날짜 칸 한 줄 배치 |

## 화면 5
| # | ui_url | 가져올 것 |
|---|---|---|
| 1 | https://uibowl.io/website/%EB%AE%A4%EC%A6%88%EB%B0%94%EC%9D%B4%20Museby?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&imgId=cmttbab590028kz041nq3vokv | 위 가운데 스텝퍼(올리기 → 확인 → 저장) + 왼쪽 작업 카드 / 오른쪽 요약 열(조 수·시약 수)과 주 버튼 |
| 2 | https://uibowl.io/website/%EB%8B%B9%EA%B7%BC%20%EB%B9%84%EC%A6%88%EB%8B%88%EC%8A%A4?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&imgId=cmso6flkw000zl7046s1sne8f | AI 추출 중 상태 = 큰 진행 문구 + 결과 표 자리 스켈레톤 행, 다음 버튼은 끝날 때까지 비활성 |
| 3 | https://uibowl.io/website/%EC%82%AC%EB%B0%A9%EB%84%B7?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&imgId=cmu4rq8hn000zl604l8itbfr2 | 추출 결과를 전폭 표(시약·1조 양·조 수 곱한 양)로 보여 주고 표 위 오른쪽에 동작 |
| 4 | https://uibowl.io/website/%EB%A6%AC%EC%BA%90%EC%B9%98?patterns=%EB%82%B4%EC%97%AD&imgId=cmihk42ii000bjp04pdf72v47 | 사용자가 고친 값이 있을 때만 저장 활성 — "확인 후 저장" 흐름 |

## 화면 6
| # | ui_url | 가져올 것 |
|---|---|---|
| 1 | https://uibowl.io/website/%EC%9C%84%EC%8B%9C%EC%BC%93?patterns=%EC%95%8C%EB%A6%BC&imgId=cmunb6cq20050l204dynrrpgm | 알림 페이지 = 날짜 그룹 제목("10월 7일") 아래 항목, 항목 본문 바로 아래 동작 버튼(판매처 연결) |
| 2 | https://uibowl.io/website/%EB%8B%B9%EA%B7%BC%20%EB%B9%84%EC%A6%88%EB%8B%88%EC%8A%A4?patterns=%EC%95%8C%EB%A6%BC&imgId=cmso6iaqk0013l404zpu8jyfj | 상단 알림 아이콘 → 아래로 붙는 팝오버(최근 몇 건 + 바닥 "전체 보기") 와 전체 페이지 2단 구성 |
| 3 | https://uibowl.io/website/%EC%82%AC%EB%B0%A9%EB%84%B7?patterns=%EC%95%8C%EB%A6%BC&imgId=cmu4rqjcr004pjq04qsvv4bon | 알림이 많을 때 "N건" 개수 + 정렬 드롭다운을 목록 위 한 줄에 |
| 4 | https://uibowl.io/website/%EC%B1%84%EB%84%90%ED%86%A1?patterns=AI&imgId=cmudq45mh001qjy04qd93j3wk | 행 끝 ⋮ 메뉴로 보조 동작(알림 숨기기)을 숨겨 행을 단순하게 |

## 화면 7
| # | ui_url | 가져올 것 |
|---|---|---|
| 1 | https://uibowl.io/website/%EC%82%AC%EB%B0%A9%EB%84%B7?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&imgId=cmu4rq8hn000zl604l8itbfr2 | 서류로 입고의 확인 표 = 전폭 표 한 장에서 여러 품목을 한 번에 입고 |
| 2 | https://uibowl.io/website/%EB%8B%B9%EA%B7%BC%20%EB%B9%84%EC%A6%88%EB%8B%88%EC%8A%A4?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&imgId=cmso6flkw000zl7046s1sne8f | AI 품목 읽는 중 = 진행 문구 + 표 자리 스켈레톤 + 이전/다음 바닥 버튼 |
| 3 | https://uibowl.io/website/%EB%AE%A4%EC%A6%88%EB%B0%94%EC%9D%B4%20Museby?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&imgId=cmttbab590028kz041nq3vokv | 스텝퍼(서류 올리기 → 확인 → 위치 추천) + 오른쪽 요약 열에 품목 수와 "한 번에 입고" 주 버튼 |
| 4 | https://uibowl.io/website/%EB%A6%AC%EC%BA%90%EC%B9%98?patterns=%EB%82%B4%EC%97%AD&imgId=cmihk42gx0007jp04md6giwds | 확인 표 행 체크 + 선택 행 일괄 동작(MSDS 찾기)을 바닥 바로 |
| 5 | https://uibowl.io/website/%EC%9C%84%EC%8B%9C%EC%BC%93?patterns=%EA%B3%84%EC%A2%8C&imgId=cmunb5pib0007l204n4d6jnbv | 직접 입력 탭의 폼 = 라벨 왼쪽 | 입력 오른쪽 가로 행, 주 버튼 카드 오른쪽 아래 |

## 화면 8
| # | ui_url | 가져올 것 |
|---|---|---|
| 1 | https://uibowl.io/website/%EB%A6%AC%EC%8A%A4%EB%8B%9D%EB%A7%88%EC%9D%B8%EB%93%9C?patterns=%EB%A7%88%EC%9D%B4%ED%8E%98%EC%9D%B4%EC%A7%80&imgId=cmsssakfn0008l104ol1ypu26 | 초대 = 제목 줄 오른쪽 인라인 폼(이메일 + 역할 선택 + 초대 버튼), 아래 사용자 표 |
| 2 | https://uibowl.io/website/%EC%9E%94%EB%94%94?patterns=%EB%8C%80%EC%8B%9C%EB%B3%B4%EB%93%9C&imgId=cmpz4uprc0003ie04h1ia0clk | 머리 요약 칩 줄("학생 a · 교사 b · admin c")을 제목 아래/오른쪽에 |
| 3 | https://uibowl.io/website/%EC%B1%84%EB%84%90%ED%86%A1?patterns=AI&imgId=cmudq45mh001qjy04qd93j3wk | 표 열 최소화(이름·이메일·역할·가입일) + 행 끝 ⋮ 에 삭제 |
| 4 | https://uibowl.io/website/%EB%A6%AC%EC%BA%90%EC%B9%98?patterns=%EA%B2%80%EC%83%89&imgId=cmihk0pui000pl804eqhg1j1k | 검색창 + 역할 필터를 표 위 한 줄 툴바로 |

## 화면 9
| # | ui_url | 가져올 것 |
|---|---|---|
| 1 | https://uibowl.io/website/%EC%B1%84%EB%84%90%ED%86%A1?patterns=AI&imgId=cmudq45mh001qjy04qd93j3wk | 판매처 표 = 이름·연락처 2열 + 행 끝 ⋮(수정·삭제), 오른쪽 위 주 버튼 "판매처 추가" |
| 2 | https://uibowl.io/website/%EC%82%AC%EB%B0%A9%EB%84%B7?patterns=%EB%A7%88%EC%9D%B4%ED%8E%98%EC%9D%B4%EC%A7%80&imgId=cmu4rq6wd000jjm04e29a62hh | 설정 하위 메뉴(사용자·판매처) 왼쪽 + 오른쪽 표 페이지 배치 |
| 3 | https://uibowl.io/website/%EB%8B%B9%EA%B7%BC%20%EB%B9%84%EC%A6%88%EB%8B%88%EC%8A%A4?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&imgId=cmso6f8zf000rl704l4qn0f5w | 판매처 추가 = 가운데 작은 모달, 필드 2개 세로, 완료는 입력 전 비활성 |
| 4 | https://uibowl.io/website/%EB%A6%AC%EC%8A%A4%EB%8B%9D%EB%A7%88%EC%9D%B8%EB%93%9C?patterns=%EB%A7%88%EC%9D%B4%ED%8E%98%EC%9D%B4%EC%A7%80&imgId=cmsssakfn0008l104ol1ypu26 | 판매처가 0개일 때 대안 — 제목 줄 인라인 추가 폼 |

## 화면 10
| # | ui_url | 가져올 것 |
|---|---|---|
| 1 | https://uibowl.io/website/%EB%BF%8C%EB%A6%AC%EC%98%A4?patterns=%EB%82%B4%EC%97%AD&imgId=cmu1vvu9l000vjv04jiybtxr8 | 필터 줄 → 표(사용일 열 정렬) → 아래 가운데 페이지 번호 순서 |
| 2 | https://uibowl.io/website/%EC%82%AC%EB%B0%A9%EB%84%B7?patterns=%ED%8E%B8%EC%A7%91%C2%B7%EC%88%98%EC%A0%95%ED%95%98%EA%B8%B0&imgId=cmu4rqsym001rl504326axccl | 기간 빠른 버튼(오늘/7일/이번 달) + "N건" 개수 한 줄 |
| 3 | https://uibowl.io/website/%EB%A6%AC%EB%94%94?patterns=%EB%82%B4%EC%97%AD&imgId=cmuq7e6jd000wjs046c714kre | 기간에 기록 없음 = 표 자리 테두리 박스 안 빈 상태 2줄(원인 + 기간 바꾸기 안내) |
| 4 | https://uibowl.io/website/%EB%A6%AC%EC%BA%90%EC%B9%98?patterns=%EA%B2%80%EC%83%89&imgId=cmihk0pui000pl804eqhg1j1k | 필터 왼쪽 / 내보내기 오른쪽 툴바 배치, 사용일 그룹 행은 표 안 묶음 머리로 |

## 화면 11
| # | ui_url | 가져올 것 |
|---|---|---|
| 1 | https://uibowl.io/website/%EB%A7%88%EC%9D%B4%ED%81%AC%EB%A1%9C%EC%86%8C%ED%94%84%ED%8A%B8%20%ED%81%B4%EB%9E%98%EB%A6%AC%ED%8B%B0%20(Microsoft%20Clarity)?patterns=AI&imgId=cmt17smk2000olc04aj4zaicl | 왼쪽 하위 열 = 시약장 목록(번호 + 이름, 활성 강조) + 아래 "시약장 추가", 오른쪽 본문 = 선택한 시약장 |
| 2 | https://uibowl.io/website/%EC%9E%94%EB%94%94?patterns=%EC%84%A4%EC%A0%95&imgId=cmpz4z8q30005ju04h03ux7s6 | 문 형태·단 수 = 그림 미리보기 선택 카드 2개 나란히, 섹션 사이 구분, 바닥 취소/저장 |
| 3 | https://uibowl.io/website/%EC%B1%84%EB%84%90%ED%86%A1?patterns=AI&imgId=cmudq46a2002ul4041tszo60n | 3단 = 시약장 목록 · 가운데 배치도 · 칸을 누르면 오른쪽 칸 패널(칸의 시약 목록, 넣기·빼기) |
| 4 | https://uibowl.io/website/%EC%9C%84%EC%8B%9C%EC%BC%93?patterns=%EA%B3%84%EC%A2%8C&imgId=cmunb5pib0007l204n4d6jnbv | 본문 카드 머리 제목·설명 → 편집 영역 → 오른쪽 아래 주 버튼(저장) 순서 |

## 화면 12
| # | ui_url | 가져올 것 |
|---|---|---|
| 1 | https://uibowl.io/website/%EB%A6%AC%EC%8A%A4%EB%8B%9D%EB%A7%88%EC%9D%B8%EB%93%9C?patterns=%EA%B2%80%EC%83%89&imgId=cmsss8y490003jv04xvtyntbp | 시약장 번호 찾기 첫 화면 = 큰 제목 + 한 줄 설명 + 가운데 넓은 입력창과 오른쪽 찾기 버튼 |
| 2 | https://uibowl.io/website/%EB%A6%AC%EC%BA%90%EC%B9%98?patterns=%EA%B2%80%EC%83%89&imgId=cmihk0pui000pl804eqhg1j1k | 결과 = 입력 바로 아래 표(시약명·칸 위치·재고) |
| 3 | https://uibowl.io/website/%EB%A6%AC%EC%BA%90%EC%B9%98?patterns=%EB%82%B4%EC%97%AD&imgId=cmihk1yub0005li04jv0iyqbi | 결과 행을 누르면 오른쪽 드로어로 시약 상세(화면 3과 같은 드로어) |
| 4 | https://uibowl.io/website/%EC%B1%84%EB%84%90%ED%86%A1?patterns=AI&imgId=cmudq46a2002ul4041tszo60n | 결과 머리에 시약장 요약 + "배치도 보기"(→11) 링크를 오른쪽 패널 머리처럼 배치 |

## 화면 13
| # | ui_url | 가져올 것 |
|---|---|---|
| 1 | https://uibowl.io/website/%EC%82%AC%EB%B0%A9%EB%84%B7?patterns=%EB%A9%94%EC%9D%B8&imgId=cmu4rq7ga000pjm04hw12bpue | 맨 위 전폭 숫자 띠(재고 부족·MSDS 없음·오늘 기록·시약장 수), 아래 격자 위젯마다 "전체보기 >" |
| 2 | https://uibowl.io/website/%EB%8B%B9%EA%B7%BC%20%EB%B9%84%EC%A6%88%EB%8B%88%EC%8A%A4?patterns=%EB%8C%80%EC%8B%9C%EB%B3%B4%EB%93%9C&imgId=cmso68mja000el704vilcy6lq | 제목(학교명) + 한 줄 정보, 해야 할 일 카드를 숫자 타일 위에 |
| 3 | https://uibowl.io/website/%EB%A6%AC%EC%BA%90%EC%B9%98?patterns=%EB%8C%80%EC%8B%9C%EB%B3%B4%EB%93%9C&imgId=cmihk6p83000slb04vu0b6tso | 폭이 다른 3열 위젯 격자, 위젯 머리 = 제목 + 오른쪽 링크, 상단 오른쪽 기준 시각 |
| 4 | https://uibowl.io/website/%EB%A7%88%EC%9D%B4%ED%81%AC%EB%A1%9C%EC%86%8C%ED%94%84%ED%8A%B8%20%ED%81%B4%EB%9E%98%EB%A6%AC%ED%8B%B0%20(Microsoft%20Clarity)?patterns=AI&imgId=cmt17smig000klc04qa188qv5 | 숫자 타일 한 줄 아래 목록형 위젯(최근 사용 기록 작은 표)과 요약 위젯을 2~3열로 섞기 |
| 5 | https://uibowl.io/website/%EC%9E%94%EB%94%94?patterns=%EB%8C%80%EC%8B%9C%EB%B3%B4%EB%93%9C&imgId=cmpz4uprc0003ie04h1ia0clk | 역할별 노출 차이 — 섹션 제목 오른쪽 요약 칩으로 역할에 따라 숨길 블록을 섹션 단위로 묶기 |

## 화면 16
| # | ui_url | 가져올 것 |
|---|---|---|
| 1 | https://uibowl.io/name/%EB%A9%94%EB%94%94%EC%BD%94%EC%B9%98?patterns=%EC%83%81%EC%84%B8%EC%A0%95%EB%B3%B4%20%28PDP%29&imgId=cms8ebafr002el204u8vddkky | (모바일) 맨 위 시약명 요약 카드 → 항목별 카드(머리 제목 + 짧은 문장 목록) 세로 나열 |
| 2 | https://uibowl.io/name/%EC%8F%98%EC%B9%B4?patterns=%EC%83%81%EC%84%B8%EC%A0%95%EB%B3%B4%20%28PDP%29&imgId=cmogjs1bf0019la04rxwg16ac | 경고 아이콘(GHS 그림문자 자리) + 신호어를 카드 맨 위에 두고, 번호 붙은 항목(2·4·7·8) 소제목 + 요약 줄 |
| 3 | https://uibowl.io/name/G%20car?patterns=%EA%B2%80%EC%83%89&imgId=cmo84t624000fl5045bz2r4ic | (모바일) 로딩 스켈레톤 = 머리 줄(아이콘 + 2줄 막대) + 본문 막대 여러 줄, 실제 레이아웃과 같은 자리 |
| 4 | https://uibowl.io/website/%EB%AA%A8%EA%B0%81%EC%9E%91?patterns=%EA%B2%80%EC%83%89&imgId=cmow9lnp1000yky0427encrx9 | (PC) 드로어/본문 안 스켈레톤을 섹션 묶음 단위(그림문자 줄 · 항목 카드들)로 나눠 반복 |
| 5 | https://uibowl.io/website/%EB%A7%88%ED%94%8C?patterns=%EC%83%81%EC%84%B8%EC%A0%95%EB%B3%B4%20%28PDP%29&imgId=cmnnx4cuq02ikju04zkbrvx39 | (PC) 넓은 화면은 항목 바로가기(탭/앵커) 한 줄 + 아래 소제목·글머리 섹션, 맨 아래 "원문 보기(안전보건공단)" 링크 |
