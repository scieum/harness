# S2 설계 — run 20261008-2144

대상: 화면 15 (랜딩) 하나 · 키스크린: 15-desktop, 15-mobile (input.json) · 학교: 화면 15는 로그인 전 화면이라 현재 학교명 표시·학교 선택이 없다.
변경 사유: 2026-10-08 사용자 결정 "푸터 = © 2026 사이음(sci_eum). 과학의 사이, 사람을 잇다. 한 줄"(rules.json footer, docs/design.md web-footer). 직전 run 20261008-1936 설계서 화면 15를 그대로 옮기고 web-footer만 바꾼다 — 4열 · 약관 링크를 없애고 가운데 한 줄 caption #707070, 위 1px #f0f0f0(hairline-soft) 선. 15-desktop 높이는 푸터가 줄어든 만큼 줄인다(5807 → 5498).
근거: docs/design.md "Pre-login desktop (screens 1·14·15)" Screen 15 항목·"Landing (screen 15)"·web-footer, docs/story-service.md 결정 사항 "랜딩"·"학교 선택"·"MSDS 요약"·N1·N2, harness/rules.json(footer, desktop_shell.pre_login.landing_sections·desktop_required 15, typography.display_sizes, frames.tall, screens_required 15, colors, radius, spacing, roles R1~R7), research/s1-adopt.md(#1~#5).
바탕(수정하지 않고 옮김): input.json base = Figma S4-screens-v18 (521:2) 15-desktop · 15-mobile. 15-mobile은 바뀌는 것이 없다(runs/20261008-1233 설계서 화면 15의 모바일 그대로, 모바일에는 web-footer가 없다). 15-desktop은 web-footer 위(y 0~5414)를 승인본 그대로 두고 web-footer만 바꾼다.

색·폰트·모서리·간격은 docs/design.md와 harness/rules.json을 따른다. 허용 색 밖의 값은 쓰지 않는다. 그림자는 쓰지 않는다(segmented-control-active 예외). 모서리는 0 · 16 · 24 · 9999만. 간격은 0 · 4 · 8 · 12 · 16 · 24 · 32 · 48 · 64만 — 섹션 위아래 여백 64, 섹션 사이 64, 섹션 안 묶음 사이 48·32·24, web-footer 위아래 여백 32.
- 글자 크기: 기본 12 · 13 · 15 · 17 · 18 · 20 · 24 · 28 · 32. 큰 글자 40 · 48은 landing-hero(헤드라인 48) · landing-section(제목 40) · cta-band(제목 40) 안에서만. 문제 공감 · step-flow · 대상 · 안심 섹션 제목은 32(display) 이하. web-footer 글자는 caption 12.
- 핑크 #d6246a · 연핑크 #fbe9f0는 badge-low-stock 안에서만(모바일 feature-card ④ 예시 배지, 데스크톱 product-shot · landing-section 화면 조각 안 재고 부족 배지). 그 밖 어디에도 쓰지 않는다.
- 하늘색 #2b9fe0 · 옅은 하늘색 #e6f4fc는 아이콘 · 활성 탭 밑줄 · step-flow 현재 단계 테두리 · 선택 표시에만. 글자색 금지(그 위 글자 #141414), button-primary · badge-low-stock 안에는 쓰지 않는다. web-footer에는 하늘색이 없다.
- 빨강 #ff0000은 쓰지 않는다(이 화면에는 ghs-pictogram을 두지 않는다).
학교 선택은 회원가입(화면 14)에만 있다. 화면 15에는 학교 선택 컴포넌트가 없다 — step-flow 1단계 화면 조각(화면 14 섹션 "1 학교 선택")은 납작한 이미지 묶음 "shot-14"로 두고, 안의 노드 이름에 school-select-* 를 쓰지 않는다. 승인 화면 조각 안에 학교명이 보이면 승인 히어로 조각과 같은 학교명 1종만 쓴다(N1).
외부 서비스 연결 정보(NEIS 학교 목록 · AI 읽기 · MSDS 요약)는 서버에서만 다룬다. 어떤 영역에도 연결 정보 입력 칸 · 설정 UI · AI 엔진 선택 UI를 두지 않는다. 안심 섹션 문구는 "인증 정보는 서버에서만 처리"로 쓴다(N2).
승인 화면 조각 공통: 실제 승인 프레임(S4-screens-v15 · v16)의 해당 부분을 실제 크기로 잘라 쓴다(새로 그리지 않음). 조각 = #ffffff 바탕, 1px #f0f0f0 테두리, rounded 16, 그림자 없음, 섹션 가장자리에서 잘림. 조각 안 사이드바는 shot-sidebar로 이름을 바꾼다(app-sidebar 금지). 조각 안 노드 이름에 역할별 노출 표의 컴포넌트명(reorder-alert-card · vendor-link · slot-assign · qr-print · cabinet-edit · stock-intake 등)과 school-select-* 를 쓰지 않는다 — 조각은 "shot-{화면 번호}" 묶음 하나로 센다. 조각 안 핑크는 badge-low-stock 안에서만.

## 화면 15
랜딩. 로그인 전 첫 화면. 서비스가 무엇인지 보여 주고 회원가입(화면 14) · 로그인(화면 1)으로 보내거나, 가입 없이 둘러보기(둘러보기 화면 13, 데모 학교)로 보낸다. 캐러셀 · 소셜 로그인 · 대형 일러스트 · 운영 숫자(학교 수 · 사용자 수) 없음. 학교명 · 학교 선택 · tab-bar · app-sidebar · nav-pill(데스크톱) 없음.
CTA 위계: 채움 "회원가입" → 외곽선 "로그인" → 가장 약한 "둘러보기" 3단. 페이지 끝 cta-band에서 한 번 더(회원가입 · 둘러보기).
모바일(390×844, runs/20261008-1233 그대로) 위→아래: nav-pill → landing-hero → feature-card 4장 세로 목록(사이 12) → 하단 고정 영역(landing-cta 전폭 버튼 2개 세로 + 그 아래 guest-entry). 좌우 여백 16, hero와 카드 목록 사이 32. 하단 탭바 없음.
데스크톱 배치: 1440 × 5498 세로 긴 프레임 한 장(15-desktop), web-header(위 고정) | 가운데 콘텐츠 폭 1200 — 히어로(landing-hero · product-shot · landing-cta · guest-entry) → landing-tabs(접는 선, 스크롤 시 web-header 아래 고정) → 문제 공감 feature-card 3 → landing-section 4(좌우 번갈아) → step-flow 5단계 → 대상 탭(segmented-control 교사 · 학생 · 관리자) → 안심 2×2 → cta-band → web-footer 가운데 한 줄. 하단 탭바 없음.

데스크톱 섹션별 y 범위(프레임 높이 5498 — 허용 900~6000 안). 0~11은 S4-screens-v18 15-desktop 승인본 위치 그대로, 12 web-footer만 바뀐다:
| 순서 | 섹션 | y 범위 | 높이 |
|---|---|---|---|
| 0 | web-header | 0 ~ 64 | 64 |
| 1 | 히어로 (승인본 그대로, 헤드라인 48) | v18 그대로 | v18 그대로 |
| 2 | landing-tabs (접는 선) | v18 그대로 | 64 |
| 3 | 문제 공감 (feature-card 3) | v18 그대로 | v18 그대로 |
| 4~7 | landing-section ① ~ ④ (좌우 번갈아) | v18 그대로 | v18 그대로 |
| 8 | step-flow 5단계 | v18 그대로 | v18 그대로 |
| 9 | 대상 탭 (교사 · 학생 · 관리자) | v18 그대로 | v18 그대로 |
| 10 | 안심 2×2 | v18 그대로 | v18 그대로 |
| 11 | cta-band | 5104 ~ 5414 | 310 |
| 12 | web-footer (한 줄) | 5414 ~ 5498 | 84 (이전 393 → 309 줄어듦) |
블록 사이 64(landing-section 4개는 서로 붙여 쌓고 섹션 안 위아래 여백 64로 나눔). 섹션 사이 구분선 없이 여백으로만 나눈다(cta-band만 #f3f3f3 띠, web-footer만 위 1px #f0f0f0 선).

섹션별 내용(데스크톱):
1. 히어로(s1-adopt #1) — 승인본 그대로. 왼쪽 글 열: 작은 꼬리표(승인본 문구) → 2줄 헤드라인 "우리 학교 시약장, / 한 화면에서 관리해요"(48, Bold 700, #141414) → 2줄 부제 body-lg #707070(승인본 문구) → landing-cta(button-primary "회원가입하고 시작하기" + button-outline "로그인") → guest-entry "둘러보기 ›" → caption #707070 "학교별 데이터 분리 · NEIS 학교 검색 · QR로 시약 찾기". 오른쪽: product-shot(승인본 그대로 — #f3f3f3 패널 안 브라우저 틀 + 승인 13-desktop 홈 실제 크기 조각(아래 · 오른쪽 잘림, 사이드바 = shot-sidebar) + 왼쪽 아래로 걸친 흰 카드 data-table 몇 행, hairline만).
2. landing-tabs(s1-adopt #2) — 가운데 탭 줄 5개 "시약 목록 · 사용 기록 · 재주문 알림 · QR 찾기 · 학교별 분리". 탭 = 아래 섹션과 1:1(① ② ③ ④ landing-section, "학교별 분리" → 안심 2×2). 활성 탭 = 지금 보이는 섹션.
3. 문제 공감 — 가운데 제목 "과학실 시약, 이렇게 관리하고 계신가요?"(display 32, #141414) → 48 → feature-card 3장 한 줄(같은 폭, 사이 24, 교사 목소리 인용) → 32 → 가운데 body-lg #707070 한 줄 "Lab_Stock은 학교별 시약장 하나로 답해요."
4. landing-section ①(글 왼쪽 · 조각 오른쪽, s1-adopt #2 · #3) — 꼬리표 "시약 목록" → 제목 "필요한 시약을 바로 찾아요"(40) → 점 목록 3 "이름 · 보관 분류 · 보관 위치로 거르고 정렬해요" · "재고가 부족한 시약은 배지로 바로 보여요" · "MSDS 요약을 목록에서 바로 열어요" → 조용한 링크 "둘러보기에서 보기 ›"(→ 둘러보기 2). 조각 2장 계단식: ⓐ 승인 2-desktop 본문의 data-table 위쪽(머리행 + 6행, 염산 · 에탄올 행 badge-low-stock) ⓑ 승인 2-filter-desktop의 list-filter-sheet 드롭다운 패널 윗부분(정렬 pill 3 + 보관 분류 칩, "산" · "산화제" 선택)을 ⓐ 왼쪽 아래에 겹침. 오른쪽 가장자리에서 잘림.
5. landing-section ②(조각 왼쪽 · 글 오른쪽) — 꼬리표 "사용 기록" → 제목 "누가 얼마나 썼는지 남겨요"(40) → 점 목록 3 "학생 · 교사 누구나 사용량을 기록해요" · "사용일을 골라 지난 날 사용도 남겨요" · "기록이 쌓이면 재주문 기준을 자동으로 계산해요" → 조용한 링크 "둘러보기에서 보기 ›"(→ 둘러보기 13). 조각: ⓐ 승인 13-desktop 홈의 "최근 사용 기록" 위젯(data-table 3행: 사용일 · 시약명 · 사용자 · 사용량) ⓑ 승인 4-desktop 사용 기록 detail-drawer 윗부분("사용 기록" · "에탄올 · 현재 1,200 mL" · 사용량 · 사용일 행 + "사용 기록 저장")을 ⓐ 오른쪽 아래에 겹침. 왼쪽 가장자리에서 잘림.
6. landing-section ③(글 왼쪽 · 조각 오른쪽) — 꼬리표 "재주문 알림" → 제목 "부족해지기 전에 알려 줘요"(40) → 점 목록 3 "재주문 기준보다 적으면 교사 · 관리자에게 알려요" · "알림에서 판매처로 바로 이어져요" · "기준은 직접 넣거나 자동으로 계산해요" → 조용한 링크 "둘러보기에서 보기 ›"(→ 둘러보기 3). 조각: ⓐ 승인 6-desktop 재주문 알림 목록의 첫 행(badge-low-stock "재고 부족" + "염산" + "재주문 기준 2병" + "10월 7일 알림", 판매처 버튼 부분은 잘라 냄) ⓑ 승인 3-desktop 시약 상세 detail-drawer의 "항목 | 값" 행 중 현재 재고 · 재주문 기준(값 + "자동" 회색 pill + 캡션 "최근 사용량으로 계산했어요") 부분을 ⓐ 왼쪽 아래에 겹침. 오른쪽 가장자리에서 잘림.
7. landing-section ④(조각 왼쪽 · 글 오른쪽) — 꼬리표 "QR 찾기" → 제목 "시약장 QR로 칸까지 찾아요"(40) → 점 목록 3 "시약장마다 고정 번호와 QR 라벨이 있어요" · "QR을 찍으면 그 시약장의 시약과 칸이 보여요" · "섞으면 위험한 조합은 칸에 넣을 때 알려 줘요" → 조용한 링크 "둘러보기에서 보기 ›"(→ 둘러보기 13). 조각: ⓐ 승인 11-desktop 시약장 설정 페이지의 배치도(시약장 번호 원 + 칸 6개 + 칸별 분류 이름 · 시약 수, 편집 버튼 줄은 잘라 냄) ⓑ 승인 12-result-desktop 결과 드로어 윗부분(시약장 번호 "1" + "1번 시약장" + 시약 3행과 칸 위치)을 ⓐ 오른쪽 아래에 겹침. 왼쪽 가장자리에서 잘림.
8. step-flow(s1-adopt #4) — 가운데 제목 "다섯 단계면 시작해요"(display 32) → 48 → 번호 원 5개를 1px #e0e0e0 선으로 이은 가로 스텝퍼(1 학교 선택 → 2 시약 등록 → 3 칸 지정 → 4 사용 기록 → 5 재주문 알림, 원 아래 label) → 32 → 카드 1장(#ffffff, 1px #f0f0f0, rounded 24, 여백 32): 왼쪽 caption #707070 "STEP 1 / 5" → heading-2 "학교 선택" → body #707070 "회원가입 때 시/도 → 지역 → 학교급 → 학교 순서로 우리 학교를 골라요" → 체크 목록 3 "NEIS 공식 학교 정보로 골라요" · "초 · 중 · 고 학교급을 먼저 골라요" · "가입한 뒤에는 우리 학교 데이터만 보여요" / 오른쪽 그 단계 조각 = 승인 14-desktop 왼쪽 폼 열 섹션 "1 학교 선택"(안내 박스 → 진행 막대 → 시/도 · 지역 · 학교급 · 학교 4칸) 부분, 납작한 묶음 "shot-14". 다른 단계 조각(예시 표시는 1단계만): 2 = 승인 7-desktop 서류로 입고 페이지 윗부분, 3 = 승인 11-desktop 배치도, 4 = 승인 4-desktop 사용 기록 드로어, 5 = 승인 6-desktop 재주문 알림 행.
9. 대상 탭 — 가운데 제목 "역할마다 필요한 만큼 보여요"(display 32) → 32 → 가운데 segmented-control "교사 · 학생 · 관리자"(활성 = 교사) → 32 → 아래 2열: 왼쪽 외곽선 기능 카드 2장 세로(#ffffff, 1px #e0e0e0, rounded 24, 여백 24, 아이콘 #2b9fe0 + heading-4 + body #707070) / 오른쪽 그 역할 화면 조각. 교사 = "입고 · 실험 매뉴얼" — "서류를 올리면 AI가 품목을 읽고, 확인한 뒤 저장해요" · "재주문 알림 · 판매처" — "부족한 시약을 알림에서 바로 주문처로 이어요", 조각 = 승인 13-desktop 교사 홈 "지금 처리할 것" 숫자 타일 줄 + shot-sidebar(교사 메뉴 8). 학생 = "시약 찾기 · MSDS 보기" · "사용 기록 남기기", 조각 = 승인 16-desktop MSDS 요약 드로어 윗부분(그림문자는 잘라 냄 — #ff0000 없음). 관리자 = "사용자 초대 · 관리" · "판매처 등록", 조각 = 승인 8-desktop 사용자 data-table 윗부분. 역할별 노출은 역할별 노출 표를 따른다(학생 탭 카드 · 조각에 입고 · 매뉴얼 · 재주문 · 판매처 · 시약장 편집 없음).
10. 안심 2×2 — 가운데 제목 "안심하고 쓰도록 만들었어요"(display 32) → 48 → 2×2 격자(hairline 1px #f0f0f0 가로 · 세로 선으로만 나눔, 카드 채움 · 테두리 · 모서리 없음, 칸 여백 32). 칸 = 아이콘 #2b9fe0 + heading-4 + body #707070: ① "학교별 데이터 분리" — "다른 학교의 시약 · 재고 · 사용 기록과 섞이지 않아요" ② "인증 정보는 서버에서만 처리" — "외부 서비스 연결 정보는 서버에서만 다루고 화면에 두지 않아요" ③ "NEIS 공식 학교 정보로 가입" — "나이스 학교기본정보로 우리 학교를 골라요" ④ "MSDS · GHS 정보 연결" — "한국산업안전보건공단 MSDS 요약과 GHS 그림문자를 보여 줘요". 운영 숫자 없음.
11. cta-band(y 5104~5414, s1-adopt #5) — 전폭 #f3f3f3 띠(rounded 0), 가운데 제목 "우리 학교 시약장, 오늘 시작해요"(40) → 16 → body-lg #707070 "학교를 고르고 이메일로 가입하면 바로 시작해요" → 32 → 버튼 2개 나란히(사이 12) button-primary "회원가입"(→ 14) + button-outline "둘러보기"(→ 둘러보기 13).
12. web-footer(y 5414~5498, s1-adopt #5 · rules.json footer — 이번 run에서 바뀌는 유일한 부분) — 전폭 #ffffff, 위 1px #f0f0f0(hairline-soft) 선, 위아래 여백 32. 가운데 정렬 한 줄 caption(12, Regular 400) #707070 "© 2026 사이음(sci_eum). 과학의 사이, 사람을 잇다." 열 · 워드마크 · 서비스/도움말/문의 링크 · 개인정보처리방침 · 이용약관 링크 모두 없음.

### 구성 요소
- web-header: 데스크톱 전용. 로그인 전 공통 규격(전폭 1440, 높이 64, rounded 0, #ffffff + 아래 1px #f0f0f0, 그림자 없음, 좌우 여백 32). 왼쪽 "Lab_Stock" 워드마크, 오른쪽 button-outline "로그인"(→ 화면 1) + button-primary "회원가입"(→ 화면 14), 사이 8. 긴 페이지에서 위에 고정. 하늘색 없음
- nav-pill: 모바일 전용(runs/20261008-1233 그대로). "Lab_Stock" 워드마크만(#f3f3f3 바, rounded 9999, 그림자 없음). 섹션 링크 · 학교명 · CTA 없음. 데스크톱에는 두지 않는다. 하늘색 없음
- landing-hero: 모바일 = 승인본 그대로(리드 "Lab_Stock" body #707070 → heading-1 "과학실 시약, 학교별로 한눈에 관리해요" → body-lg #707070 부제, 왼쪽 정렬). 데스크톱 = 히어로 왼쪽 글 열(승인본 그대로): 꼬리표 → 2줄 헤드라인 "우리 학교 시약장, / 한 화면에서 관리해요" 48 Bold 700 #141414 → 2줄 body-lg 부제 #707070 → landing-cta → guest-entry → caption #707070 "학교별 데이터 분리 · NEIS 학교 검색 · QR로 시약 찾기". 모노크롬, 학교명 없음. 하늘색 없음
- product-shot: 데스크톱 전용. 히어로 오른쪽 묶음 1개(승인본 그대로) — #f3f3f3 패널(rounded 24) 안 브라우저 틀 + 승인 13-desktop 홈 실제 크기 조각(아래 · 오른쪽 잘림) + 왼쪽 아래로 걸친 흰 카드(#ffffff, 1px #f0f0f0, rounded 16) 안 data-table 몇 행. 층은 hairline으로만, 그림자 없음. 핑크는 조각 안 badge-low-stock 안에서만
- shot-sidebar: 데스크톱 전용. product-shot · 대상 탭 교사 조각 안 승인 화면 사이드바의 이름(app-sidebar로 세지 않도록). 모양은 승인 화면 그대로
- landing-cta: 행동 영역. button-primary + button-outline. 모바일 = 하단 고정 #ffffff 영역(위 1px #f0f0f0, 여백 16) 전폭 버튼 2개 세로(사이 8) "회원가입" · "로그인"(승인본 그대로). 데스크톱 = 히어로 글 열 안 두 버튼 나란히(사이 12) "회원가입하고 시작하기"(→ 14) · "로그인"(→ 1)(승인본 그대로). 하늘색 없음
- button-primary: landing-cta · web-header "회원가입" · cta-band "회원가입"(#141414 채움, #ffffff 글자 link, rounded 9999, 높이 44 이상). 하늘색 없음
- button-outline: landing-cta · web-header "로그인", cta-band "둘러보기"(#ffffff, 1px #e0e0e0, #141414 글자 link, rounded 9999, 높이 44 이상). 하늘색 없음
- guest-entry: 가장 조용한 세 번째 행동 — button-pill-soft "둘러보기 ›" 1개(→ 둘러보기 13, 데모 학교 홈). 모바일 = 하단 고정 영역 맨 아래 가운데, 데스크톱 = landing-cta 아래 12 간격 왼쪽 맞춤(승인본 그대로). 하늘색: › 아이콘 #2b9fe0
- button-pill-soft: guest-entry "둘러보기 ›"(#f3f3f3, 테두리 없음, 라벨 #141414, rounded 9999, 높이 44 이상, 폭은 라벨에 맞춤). 하늘색: › 아이콘만
- landing-tabs: 데스크톱 전용. 접는 선 가운데 탭 줄 5개 "시약 목록 · 사용 기록 · 재주문 알림 · QR 찾기 · 학교별 분리"(link 15, 탭 높이 44 이상, 사이 32). 활성 탭 = 라벨 #141414 + 아래 2px #2b9fe0 밑줄, 비활성 라벨 #707070. 아래 1px #f0f0f0 선. 누르면 해당 섹션으로 스크롤, 스크롤 시 web-header 바로 아래(y 64)에 고정. 예시 = "시약 목록" 활성. 하늘색: 활성 밑줄만
- feature-card: 모바일 = 기능 카드 4장(승인본 그대로: ① 학교별 분리 ② NEIS 학교 선택 "회원가입 때 시/도 → 지역 → 학교급 → 학교 순서로 우리 학교를 골라요" ③ QR 스캔 ④ 재고 부족 알림 + 예시 badge-low-stock, #f3f3f3, rounded 24, 여백 24, 아이콘 #2b9fe0). 데스크톱 = 문제 공감 3장 한 줄(같은 폭, 사이 24, #f3f3f3, 테두리 없음, rounded 24, 여백 32): 위 따옴표 아이콘 #2b9fe0 → body-lg #141414 인용 → caption #707070 "— 과학 교사". ① "시약이 얼마나 남았는지 장을 열어 봐야 알아요" ② "누가 언제 얼마나 썼는지 공책에 적다 보니 빠지는 게 많아요" ③ "MSDS를 보려면 매번 사이트를 찾아 들어가야 해요". 데스크톱 카드에는 배지 없음. 하늘색: 아이콘만
- badge-low-stock: 모바일 feature-card ④ 제목 옆 예시 배지 1개, 데스크톱 product-shot · landing-section ① · ③ 조각 안 재고 부족 표시(#d6246a 채움, label "재고 부족" #ffffff, rounded 9999). 핑크는 이 배지 안에서만. 하늘색 없음
- data-table: 데스크톱 전용. product-shot 겹친 카드와 landing-section ① · ② 조각 안 승인 표(ex-data-table-cell 머리행 caption #707070 · 셀 body-sm, rounded 16 컨테이너, 1px #f0f0f0). 조각이라 누름 동작 없음
- landing-section: 데스크톱 전용 4개(각 480, s1-adopt #2 · #3, 위치 v18 그대로). 2열(글 열 폭 480 · 조각 열 나머지, 사이 64), ①③ 글 왼쪽 · ②④ 글 오른쪽으로 번갈아. 글 열 위→아래: 꼬리표(label #141414, #f3f3f3 pill rounded 9999) → 24 → 제목 1줄 40 Bold 700 #141414 → 24 → 점 목록 3(body #141414, 글머리 점 #2b9fe0, 줄 사이 12) → 32 → 조용한 링크 "둘러보기에서 보기 ›"(link #141414, 누름 영역 44 이상, › #2b9fe0). 조각 열 = 승인 화면 조각 2장 계단식 겹침(뒤 조각 큰 것, 앞 조각 작은 것을 대각선 아래로 걸침), 바깥 가장자리에서 잘림. ① 시약 목록 = 2-desktop data-table + 2-filter-desktop 필터 패널 ② 사용 기록 = 13-desktop 최근 사용 기록 위젯 + 4-desktop 사용 기록 드로어 ③ 재주문 알림 = 6-desktop 알림 행(판매처 버튼 잘라 냄) + 3-desktop 드로어 재주문 기준 행 ④ QR 찾기 = 11-desktop 배치도(편집 줄 잘라 냄) + 12-result-desktop 결과 드로어. 문구는 위 "섹션별 내용" 4~7. 하늘색: 글머리 점 · › 아이콘
- step-flow: 데스크톱 전용(s1-adopt #4, 위치 v18 그대로). 번호 원 5개(지름 44, rounded 9999)를 1px #e0e0e0 선으로 이은 가로 줄 + 원 아래 label #141414 "학교 선택 · 시약 등록 · 칸 지정 · 사용 기록 · 재주문 알림". 현재 단계(1) = #ffffff 원 + 2px #2b9fe0 테두리 + 숫자 #141414, 나머지 = #f3f3f3 원 + 숫자 #707070. 아래 카드 1장(#ffffff, 1px #f0f0f0, rounded 24, 여백 32): 왼쪽 "STEP 1 / 5" → "학교 선택" → 설명 → 체크 3(체크 아이콘 #2b9fe0 + body #141414) / 오른쪽 승인 14-desktop "1 학교 선택" 섹션 조각(shot-14, school-select-* 이름 없음). 단계를 누르면 카드 내용 · 조각이 그 단계로 바뀐다. 하늘색: 현재 단계 테두리 · 체크 아이콘
- segmented-control: 데스크톱 전용. 대상 탭 "교사 · 학생 · 관리자" 3칸(#f3f3f3 트랙, rounded 9999, 같은 폭 pill 누름 영역 44 이상, 비활성 라벨 #707070). 고른 역할의 카드 2장 · 조각이 바뀐다. 예시 = "교사"
- segmented-control-active: "교사" 흰 pill(#ffffff, 그림자 허용 예외, 라벨 #141414). 하늘색: 1px #2b9fe0 테두리
- cta-band: 데스크톱 전용(y 5104~5414, s1-adopt #5, v18 그대로). 전폭 #f3f3f3 띠(rounded 0, 위아래 여백 64), 가운데 제목 "우리 학교 시약장, 오늘 시작해요" 40 Bold 700 #141414 → body-lg #707070 한 줄 → button-primary "회원가입"(→ 14) + button-outline "둘러보기"(→ 둘러보기 13) 나란히(사이 12). 하늘색 없음
- web-footer: 데스크톱 전용(y 5414~5498, 높이 84, s1-adopt #5 · rules.json footer · docs/design.md web-footer). 전폭 #ffffff, rounded 0, 위 1px #f0f0f0(hairline-soft) 선, 위아래 여백 32. 가운데 정렬 한 줄 caption 12 Regular 400 #707070(text-muted) "© 2026 사이음(sci_eum). 과학의 사이, 사람을 잇다." 열 · 워드마크 · 링크 · 약관 링크 없음(누름 영역 없음). 하늘색 없음
### 반영한 레퍼런스
- https://uibowl.io/website/%EB%A7%88%EC%9D%B4%ED%81%AC%EB%A1%9C%EC%86%8C%ED%94%84%ED%8A%B8%20%ED%81%B4%EB%9E%98%EB%A6%AC%ED%8B%B0%20(Microsoft%20Clarity)?patterns=%EB%9E%9C%EB%94%A9%ED%8E%98%EC%9D%B4%EC%A7%80&imgId=cmt180ji1000dkz04ef56j21k
- https://uibowl.io/website/%EB%A7%88%EC%9D%B4%ED%81%AC%EB%A1%9C%EC%86%8C%ED%94%84%ED%8A%B8%20%ED%81%B4%EB%9E%98%EB%A6%AC%ED%8B%B0%20(Microsoft%20Clarity)?patterns=%EB%9E%9C%EB%94%A9%ED%8E%98%EC%9D%B4%EC%A7%80&imgId=cmt180jkd000jkz042m47nqbn
- https://uibowl.io/website/%ED%94%8C%EB%A6%AC%EB%8D%94%EC%8A%A4%20(plithus)?patterns=%EB%9E%9C%EB%94%A9%ED%8E%98%EC%9D%B4%EC%A7%80&imgId=cmssgqukq000pl4047xzrrltr
- https://uibowl.io/website/%EB%AE%A4%EC%A6%88%EB%B0%94%EC%9D%B4%20Museby?patterns=%EB%9E%9C%EB%94%A9%ED%8E%98%EC%9D%B4%EC%A7%80&imgId=cmttba73x000el404ldps2v6m
- https://uibowl.io/website/%ED%94%8C%EB%A6%AC%EB%8D%94%EC%8A%A4%20(plithus)?patterns=%EB%9E%9C%EB%94%A9%ED%8E%98%EC%9D%B4%EC%A7%80&imgId=cmssgqur6001dl4049g6t7jn8

## 역할별 노출
앱 전체(로그인 후 화면) 기준 개수. runs/20261008-1936 표 숫자를 그대로 유지한다. 화면 15는 로그인 전 화면이라 표의 컴포넌트를 하나도 담지 않는다 — landing-section · step-flow · 대상 탭의 승인 화면 조각은 "shot-{화면 번호}" 묶음 이미지로 세고, 안의 노드에 표의 컴포넌트명을 쓰지 않는다. 대상 탭의 역할별 카드 · 조각 내용은 이 표를 따른다(학생 = 표의 교사 · admin 전용 기능 없음). msds-entry = 화면 3 1 + 화면 10 상세 1(학생 · 교사 · admin 모두 2, R4).

| 컴포넌트 | 학생 | 교사 | admin |
|---|---|---|---|
| manual-upload | 0 | 2 | 2 |
| reorder-alert-card | 0 | 2 | 2 |
| vendor-link | 0 | 1 | 1 |
| vendor-register | 0 | 0 | 2 |
| msds-entry | 2 | 2 | 2 |
| stock-intake | 0 | 2 | 2 |
| reagent-register | 0 | 1 | 1 |
| user-manage | 0 | 0 | 2 |
| cabinet-edit | 0 | 3 | 3 |
| cabinet-add | 0 | 1 | 1 |
| slot-assign | 0 | 1 | 1 |
| location-edit | 0 | 1 | 1 |
| qr-print | 0 | 1 | 1 |
| threshold-edit | 0 | 1 | 1 |
| doc-upload | 0 | 1 | 1 |
| msds-search | 0 | 2 | 2 |
| msds-bulk-banner | 0 | 1 | 1 |
