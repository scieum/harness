# S1 채택 — run 20261008-1233

- 구조·흐름·배치만 가져온다. 색·폰트·모서리는 docs/design.md를 따른다.

## 화면 1
| # | ui_url | 가져올 것 |
|---|---|---|
| 1 | https://uibowl.io/website/%EB%AE%A4%EC%A6%88%EB%B0%94%EC%9D%B4%20Museby?patterns=%EB%A1%9C%EA%B7%B8%EC%9D%B8%C2%B7%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85&imgId=cmttba7s2000okz04vi1241gp | 반 나눔 배치: 왼쪽 절반 = 폼(제목 → 입력 → 전폭 주 버튼 → 보조 동작), 오른쪽 절반 = 서비스 소개 패널, 약관·안내는 왼쪽 아래 |
| 2 | https://uibowl.io/website/%EC%9E%94%EB%94%94?patterns=%EB%A1%9C%EA%B7%B8%EC%9D%B8%C2%B7%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85&imgId=cmpz4v0pv00b7ld04afw5a58j | 폼 안 순서: 입력 2칸 → 보조 옵션 줄(왼쪽 체크 / 오른쪽 "비밀번호 찾기") → 입력 전 비활성 주 버튼 → 맨 아래 "회원가입" 링크 |
| 3 | https://uibowl.io/website/%EC%9C%A0%EA%B4%91%EA%B8%B0?patterns=%EB%A1%9C%EA%B7%B8%EC%9D%B8%C2%B7%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85&imgId=cmtb2zqla000kjr04j48pf8ll | 로그인 전에도 전폭 상단 바(로고 왼쪽 / 동작 오른쪽)를 유지하고 그 아래 영역만 반 나눔으로 바꾼다 |
| 4 | https://uibowl.io/website/%EB%A7%88%EC%9D%B4%ED%81%AC%EB%A1%9C%EC%86%8C%ED%94%84%ED%8A%B8%20%ED%81%B4%EB%9E%98%EB%A6%AC%ED%8B%B0%20(Microsoft%20Clarity)?patterns=%EB%9E%9C%EB%94%A9%ED%8E%98%EC%9D%B4%EC%A7%80&imgId=cmt180ji1000dkz04ef56j21k | 상단 바 오른쪽 끝 버튼 짝 배치(보조 1 + 주 1) — 로그인 화면에서는 "회원가입"·"둘러보기"를 이 자리에 둔다 |

## 화면 14
| # | ui_url | 가져올 것 |
|---|---|---|
| 1 | https://uibowl.io/website/%EC%9C%A0%EA%B4%91%EA%B8%B0?patterns=%EB%A1%9C%EA%B7%B8%EC%9D%B8%C2%B7%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85&imgId=cmtb2zqla000kjr04j48pf8ll | 번호 붙은 섹션 + 구분선("1. 학교 선택" → "2. 계정"), 확정된 값(선택한 학교)은 입력칸 대신 글자로 표시, 칸 안쪽 오른쪽 동작 버튼 |
| 2 | https://uibowl.io/website/%EB%AE%A4%EC%A6%88%EB%B0%94%EC%9D%B4%20Museby?patterns=%EB%A1%9C%EA%B7%B8%EC%9D%B8%C2%B7%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85&imgId=cmttba7s2000okz04vi1241gp | 화면 1과 같은 반 나눔 틀(왼쪽 폼 / 오른쪽 소개 패널)을 회원가입에도 그대로 써서 두 화면 구조를 맞춘다 |
| 3 | https://uibowl.io/website/%EC%9E%94%EB%94%94?patterns=%EB%A1%9C%EA%B7%B8%EC%9D%B8%C2%B7%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85&imgId=cmpz4v0pv00b7ld04afw5a58j | 폼 맨 아래 "이미 계정이 있나요? 로그인" 한 줄 링크, 필수값이 채워지기 전 주 버튼 비활성 |
| 4 | https://uibowl.io/website/%EB%AE%A4%EC%A6%88%EB%B0%94%EC%9D%B4%20Museby?patterns=%EB%A1%9C%EA%B7%B8%EC%9D%B8%C2%B7%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85&imgId=cmttba7ve000ykz043dveic7s | 가입 완료 뒤 작은 가운데 모달(아이콘 → 제목 → 설명 2줄 → 전폭 주 버튼 → 텍스트 버튼) 흐름 |
| 5 | https://uibowl.io/website/%EB%A6%AC%EB%94%94?patterns=%EB%82%B4%EC%97%AD&imgId=cmuq7e6jd000wjs046c714kre | 14-no-school: 학교 검색 결과 자리에 테두리 박스 빈 상태 2줄(검색된 학교 없음 / 다른 이름으로 찾기 안내)을 놓는다 |

## 화면 15
| # | ui_url | 가져올 것 |
|---|---|---|
| 1 | https://uibowl.io/website/%EB%A7%88%EC%9D%B4%ED%81%AC%EB%A1%9C%EC%86%8C%ED%94%84%ED%8A%B8%20%ED%81%B4%EB%9E%98%EB%A6%AC%ED%8B%B0%20(Microsoft%20Clarity)?patterns=%EB%9E%9C%EB%94%A9%ED%8E%98%EC%9D%B4%EC%A7%80&imgId=cmt180ji1000dkz04ef56j21k | 히어로 2열: 왼쪽 제목 + 설명 + 버튼 2개(시작하기 / 둘러보기), 오른쪽 실제 제품 화면 조각. 상단 바 오른쪽 로그인(보조) + 시작(주) 짝 |
| 2 | https://uibowl.io/website/%EB%A6%AC%EC%8A%A4%EB%8B%9D%EB%A7%88%EC%9D%B8%EB%93%9C?patterns=%EB%9E%9C%EB%94%A9%ED%8E%98%EC%9D%B4%EC%A7%80&imgId=cmsssa2md000vl404rq691ip5 | 히어로 아래 기능 카드 격자(카드마다 제목 + 설명 + 하위 항목) — Lab_Stock은 4열로 |
| 3 | https://uibowl.io/website/%EB%BF%8C%EB%A6%AC%EC%98%A4?patterns=%EB%9E%9C%EB%94%A9%ED%8E%98%EC%9D%B4%EC%A7%80&imgId=cmu1vvwu9000cjj04vs8uvy90 | 히어로 위 작은 키워드 줄(대상: 교사·학생·관리자) + 가운데 큰 제목 구성 |
| 4 | https://uibowl.io/website/%EB%A6%AC%EC%8A%A4%EB%8B%9D%EB%A7%88%EC%9D%B8%EB%93%9C?patterns=%EC%83%81%EC%84%B8%EC%A0%95%EB%B3%B4%20%28PDP%29&imgId=cmsssh7ff000bi804stb2ki6y | 페이지 끝 전폭 CTA 띠(가운데 제목 1줄 + 설명 1줄 + 버튼) 다음 푸터(왼쪽 정보 / 오른쪽 링크 열) 순서 |
| 5 | https://uibowl.io/website/%ED%94%8C%EB%A6%AC%EB%8D%94%EC%8A%A4%20(plithus)?patterns=%ED%83%90%EC%83%89&imgId=cmssgtlmk0003l704ennjaybp | 둘러보기 섹션: 사용 흐름 단계를 가로 한 줄 카드로 연결해 보여 주고 끝에 "둘러보기" 진입 버튼 |

## 화면 13
| # | ui_url | 가져올 것 |
|---|---|---|
| 1 | https://uibowl.io/website/%EB%AF%B9%EC%8A%A4%ED%8C%A8%EB%84%90%20(mixpanel)?patterns=%EB%B6%81%EB%A7%88%ED%81%AC%C2%B7%EC%9C%84%EC%8B%9C%EB%A6%AC%EC%8A%A4%ED%8A%B8&imgId=cmuxmlodo0003js04xhbgfj5d | 둘러보기 홈: 로그인 후와 같은 사이드바 그대로 + 본문 맨 위 전폭 안내 띠(데모 학교 안내 한 줄 / 오른쪽 "회원가입" 버튼) + 그 아래 샘플 대시보드 |
| 2 | https://uibowl.io/website/%EB%A6%AC%EC%8A%A4%EB%8B%9D%EB%A7%88%EC%9D%B8%EB%93%9C?patterns=%EB%9E%9C%EB%94%A9%ED%8E%98%EC%9D%B4%EC%A7%80&imgId=cmsssa2md000vl404rq691ip5 | 로그인 전에도 사이드바 메뉴 전체를 노출하고, 로그인이 필요한 메뉴는 자리를 지운 채 잠금 표시로 남겨 앱 구조를 보여 준다 |
| 3 | https://uibowl.io/website/%EC%82%AC%EB%B0%A9%EB%84%B7?patterns=%EB%A9%94%EC%9D%B8&imgId=cmu4rq7ga000pjm04hw12bpue | 맨 위 상태 숫자 띠 + 아래 격자 위젯("전체보기 >")의 대시보드 배치를 샘플 데이터로 채움 |
| 4 | https://uibowl.io/website/%EB%8B%B9%EA%B7%BC%20%EB%B9%84%EC%A6%88%EB%8B%88%EC%8A%A4?patterns=%EB%8C%80%EC%8B%9C%EB%B3%B4%EB%93%9C&imgId=cmso68mja000el704vilcy6lq | 제목 + 한 줄 정보(데모 학교명) 아래 숫자 타일 4개 한 줄 구성 |

## 화면 2
| # | ui_url | 가져올 것 |
|---|---|---|
| 1 | https://uibowl.io/website/%EC%B1%84%EB%84%90%ED%86%A1?patterns=%EB%AA%A9%EB%A1%9D%20%28PLP%29&imgId=cmudq4ko40041jx04pjl68ftt | 사이드바 + 본문 위 전폭 안내 띠(아이콘 + 한 줄 + 링크) + 바로 아래 표 — 띠는 표를 밀어 내리고 겹치지 않음 |
| 2 | https://uibowl.io/website/%EB%A6%AC%EC%BA%90%EC%B9%98?patterns=%EA%B2%80%EC%83%89&imgId=cmihk0pui000pl804eqhg1j1k | 로그인 후 목록과 같은 머리 3줄 + 표 구조를 유지하되, 쓰기 동작(주 버튼·일괄 동작)은 잠금/숨김으로 바꿀 자리 |
| 3 | https://uibowl.io/website/%EB%AF%B9%EC%8A%A4%ED%8C%A8%EB%84%90%20(mixpanel)?patterns=%EB%A6%AC%EB%B7%B0%EC%93%B0%EA%B8%B0&imgId=cmuxmm2c10009jn04qhjm9sf4 | 안내 띠를 페이지 이동과 관계없이 본문 맨 위에 고정해 모든 둘러보기 화면에 같은 위치로 둔다 |
| 4 | https://uibowl.io/website/%EB%A6%AC%EC%8A%A4%EB%8B%9D%EB%A7%88%EC%9D%B8%EB%93%9C?patterns=%EA%B2%80%EC%83%89&imgId=cmsss8y490003jv04xvtyntbp | 상단 바 오른쪽 계정 자리를 둘러보기에서는 로그인 / 회원가입 버튼으로 바꾸는 배치 |

## 화면 3
| # | ui_url | 가져올 것 |
|---|---|---|
| 1 | https://uibowl.io/website/%EB%A6%AC%EC%BA%90%EC%B9%98?patterns=%EB%82%B4%EC%97%AD&imgId=cmihk1yub0005li04jv0iyqbi | 상세 드로어 순서(제목 → 메타 칩 → 탭 → 항목|값) 그대로, 편집·사용 기록 버튼만 잠금 상태로 |
| 2 | https://uibowl.io/website/%EB%AF%B9%EC%8A%A4%ED%8C%A8%EB%84%90%20(mixpanel)?patterns=%EB%A6%AC%EB%B7%B0%EC%93%B0%EA%B8%B0&imgId=cmuxmm2c10009jn04qhjm9sf4 | 오른쪽 패널을 열어도 본문 맨 위 안내 띠는 사라지지 않고 그대로 유지 |
| 3 | https://uibowl.io/website/%EC%B1%84%EB%84%90%ED%86%A1?patterns=AI&imgId=cmudq46a2002ul4041tszo60n | 사이드바 · 목록 · 오른쪽 상세 패널이 동시에 보이는 3단 폭 배분 |
| 4 | https://uibowl.io/website/%EC%B1%84%EB%84%90%ED%86%A1?patterns=%EB%A9%94%EC%9D%B8&imgId=cmudq3ztp000cl704tva1cnep | 3단 화면에서도 얇은 안내 띠 한 줄을 맨 위에 고정하는 배치 |

## 화면 16
| # | ui_url | 가져올 것 |
|---|---|---|
| 1 | https://uibowl.io/website/%EB%A7%88%ED%94%8C?patterns=%EC%83%81%EC%84%B8%EC%A0%95%EB%B3%B4%20%28PDP%29&imgId=cmnnx4cuq02ikju04zkbrvx39 | MSDS 요약 본문: 섹션 탭 줄 + 굵은 소제목 + 글머리 목록 구조(데모 시약 기준) |
| 2 | https://uibowl.io/website/%EB%AA%A8%EA%B0%81%EC%9E%91?patterns=%EA%B2%80%EC%83%89&imgId=cmow9lnp1000yky0427encrx9 | 요약 불러오는 중 스켈레톤(칩 막대 + 행 막대 묶음) 배치 |
| 3 | https://uibowl.io/website/%EB%A6%AC%EC%BA%90%EC%B9%98?patterns=%EB%82%B4%EC%97%AD&imgId=cmihk1yub0005li04jv0iyqbi | MSDS 요약을 시약 상세 드로어 안 탭/섹션으로 열어 목록을 가리지 않음 |
| 4 | https://uibowl.io/website/%EB%AF%B9%EC%8A%A4%ED%8C%A8%EB%84%90%20(mixpanel)?patterns=%EB%B6%81%EB%A7%88%ED%81%AC%C2%B7%EC%9C%84%EC%8B%9C%EB%A6%AC%EC%8A%A4%ED%8A%B8&imgId=cmuxmlodo0003js04xhbgfj5d | 샘플 내용임을 알리는 맨 위 안내 띠를 MSDS 화면에도 같은 자리에 유지 |
