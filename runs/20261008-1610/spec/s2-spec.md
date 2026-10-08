# S2 설계 — run 20261008-1610

대상: 화면 16 + 상태 화면 20종(2-msds-bulk · 2-filter · 2-filter-empty, 3-location · 3-msds, 4-past-date, 7-doc-upload · 7-doc-review · 7-doc-fail · 7-suggest · 7-msds, 11-empty · 11-delete · 11-slot · 11-print · 11-unsaved, 12-result, 16-loading · 16-fail · 16-no-summary) · 학교: 샘플고등학교 (input.json) · 키스크린: 11-slot-desktop, 7-doc-review-desktop, 16-loading-mobile
변경 사유: 데스크톱 재구성 2차-b. 1차(runs/20261008-0936)는 기본 화면만 웹앱 틀(app-sidebar · data-table · detail-drawer · 무거운 작업은 페이지)로 바꿨고, 상태 화면 데스크톱은 아직 옛 틀(nav-pill + 가운데 단일 열 · 가운데 시트)이다. 이번에는 상태 화면 20종의 데스크톱을 docs/design.md "Desktop shell" 틀로 옮기고, 화면 16의 상태 3종(16-loading · 16-fail · 16-no-summary)을 모바일까지 새로 설계한다.
근거: docs/design.md "Desktop shell"·"MSDS summary"·"List filter"·"Usage date"·"Document intake"·"MSDS search"·"Location suggestion"·"Reagent slots"·"Multiple cabinets"·"Cabinet number & QR print", docs/story-service.md 결정 사항(2026-10-04 ~ 2026-10-08 행), harness/rules.json(roles R1~R7, screens_required 16, variants, desktop_shell, msds_summary, cabinet, list_filter, usage_date, intake, msds, suggest, tab_bar, colors), research/s1-adopt.md.
모바일 기준 설계(수정하지 않고 옮김): 화면 16 = runs/20261008-0936. 2-filter · 2-filter-empty · 4-past-date = runs/20261007-0744. 2-msds-bulk · 3-location · 3-msds · 7-doc-upload · 7-doc-review · 7-doc-fail · 7-suggest · 7-msds = runs/20261007-0002. 11-slot · 11-print · 11-unsaved · 12-result = runs/20261006-1223. 11-empty · 11-delete = runs/20261004-2256. 옮기면서 바꾸는 것은 세 가지뿐 — ① nav-pill 설명에서 "데스크탑 섹션 링크"를 뺀다(데스크톱은 app-sidebar) ② 공통 nav-account-menu(runs/20261006-1223)를 11-empty · 11-delete에도 적는다 ③ msds-entry "MSDS 보기"는 화면 16을 열어 ↗ 대신 › 로 표기한다(1차와 같음). 16-loading · 16-fail · 16-no-summary 모바일은 docs/design.md "MSDS summary"와 rules.json msds_summary로 새로 쓴다.
데스크톱 바탕(input.json desktop_base): 1차 승인 데스크톱(runs/20261008-0936 spec, Figma S4-screens-v15 374:2)의 같은 화면 desktop 틀을 그대로 두고 상태 부분만 바꾼다.
색·폰트·모서리·간격은 docs/design.md와 harness/rules.json을 따른다. 허용 색 밖의 값(딤 반투명 검정 등)은 쓰지 않는다. 반투명 회색은 badge-overlay 안에서만. 그림자는 쓰지 않는다(segmented-control-active 예외).
- 핑크 #d6246a · 연핑크 #fbe9f0는 badge-low-stock, reorder-alert-card, mix-warning 안에서만 쓴다. 필터 결과 없음 · 지난 날짜 안내 · 서류 읽기 실패 · 후보 0개 · 맞는 칸 없음 · 시약장 삭제 · 저장 안 한 편집 · MSDS 요약 실패에는 핑크를 쓰지 않는다(#141414 아이콘 + #141414/#707070 문구).
- 하늘색 #2b9fe0 · 옅은 하늘색 #e6f4fc는 선택 · 현재 위치 · 진행 · 아이콘 · 안내 띠 · suggest-badge · 적용 개수 pill에만 쓴다. 글자색 금지(그 위 글자 #141414), badge-low-stock · reorder-alert-card · button-primary · mix-warning 안에는 쓰지 않는다. app-sidebar 현재 sidebar-item, data-table 선택 행 · 활성 정렬 화살표는 하늘색 규칙대로.
- 빨강 #ff0000은 화면 16 ghs-pictogram 마름모 테두리 안에서만 쓴다. 16-loading의 그림문자 자리(msds-skeleton)에는 빨강을 쓰지 않는다(#f3f3f3 회색만).
- qr-label은 인쇄물이라 흑백(#141414 · #707070 · #ffffff · #e0e0e0)만.
학교 선택은 회원가입(화면 14)에만 있다. 대상 화면 · 상태 화면 모두 학교 선택 · 전환이 없고 현재 학교명 "샘플고등학교"를 모바일은 nav-pill 안, 데스크톱은 app-sidebar 맨 위에 표시한다. 시약 · 시약장 · 칸 · 서류 품목 연결 · MSDS 연결 · 추천 칸 · QR 결과는 모두 샘플고등학교 것만 보인다(N1). qr-label 학교명도 "샘플고등학교" 1종.
외부 서비스 연결 값(AI 읽기 · MSDS 조회 · 요약)은 서버에서만 다룬다. 어떤 화면에도 연결 값 입력 칸 · 외부 서비스 설정 · AI 엔진 선택 UI · 관련 문구를 두지 않는다(N2).
괄호 안 역할 표시가 없는 구성 요소는 그 상태에 들어오는 모든 역할에게 보인다. 교사·admin 전용 상태: 2-msds-bulk, 3-location, 3-msds, 7-*, 11-delete, 11-slot(넣기 · 빼기), 11-print, 11-unsaved. 모든 역할 상태: 2-filter, 2-filter-empty, 4-past-date, 11-empty(학생은 cabinet-add 없이 문구만), 12-result, 16-*. 학생 화면에는 doc-upload, msds-search, msds-bulk-banner, stock-intake, reagent-register, threshold-edit, location-edit, slot-assign, qr-print, cabinet-add, cabinet-edit을 그리지 않는다(R5 · R7).

모바일 공통(승인본 그대로): tab-bar는 화면 아래 가장자리 y 780~844(폭 390, 높이 64, rounded 0, #ffffff + 위쪽 1px #f0f0f0 선, 그림자 없음)에 붙고 tab-item 4개("홈" · "시약" · "QR 스캔" · "기록")를 같은 폭으로 채운다. 하단 고정 버튼은 tab-bar 바로 위(간격 16). 바텀시트 · 확인 카드는 tab-bar 위쪽 선 위에 붙는다(딤 없음, 1px #e0e0e0 테두리, 위쪽 rounded 24, 오른쪽 위 × 닫기). 모바일 nav-pill = 얇은 헤더(뒤로가기 또는 워드마크 + 제목 + 학교명 + nav-account-menu ▾).

데스크톱 공통(1440×900, rules.json desktop_shell): nav-pill · tab-bar 없음.
- app-sidebar: 왼쪽 고정 열 폭 240, 높이 전체, rounded 0, #f3f3f3 채움, 오른쪽 1px #f0f0f0 선. 맨 위 "Lab_Stock" 워드마크 + 학교명 "샘플고등학교"(title #141414, 전환 없음) → 가운데 sidebar-item 묶음 → 맨 아래 "{이름} · {역할}"(body-sm) + nav-account-menu ▾(닫힌 상태).
- sidebar-item: 아이콘 + body 라벨, 높이 44, 사각형(rounded 0). 현재 항목 = #e6f4fc 채움 + #2b9fe0 아이콘, 라벨 #141414. 비활성 = #707070 아이콘 / #141414 라벨. 역할별 메뉴(rules.json desktop_shell.menu, 묶음 제목 caption #707070):
  - 학생 5개: 홈 · 시약 · 기록 · 시약장 · QR 찾기
  - 교사 8개: 홈 · 시약 · 기록 · 시약장 · QR 찾기 / "관리" 입고 · 실험 매뉴얼 · 재주문 알림
  - admin 10개: 교사 8개 + "학교 설정" 사용자 · 판매처
  - 현재 항목: 2-* · 3-* · 4-* · 16-* = "시약", 7-* = "입고", 11-* = "시약장", 12-result = "QR 찾기".
- 본문 = 사이드바 오른쪽 전체, 페이지 여백 32. 페이지 머리 = 왼쪽 제목(heading-2) + 개수(caption #707070), 오른쪽 검색 · 필터 · 주 버튼.
- data-table: ex-data-table-cell 머리행(caption #707070) · 본문(body-sm) + rounded 16 컨테이너, 1px #f0f0f0 테두리. 정렬 가능한 열 머리(화살표 #707070, 활성 #2b9fe0), 행 hover #f3f3f3, 선택 행 #e6f4fc. badge-low-stock은 상태 열.
- detail-drawer: 오른쪽 폭 480, 높이 900, #ffffff, 왼쪽 1px #f0f0f0 선, 여백 24, 오른쪽 위 × 닫기(누름 영역 44 이상). 본문을 밀어내는 배치(docs/design.md 승인안: 사이드바 240 + 본문 720 + 드로어 480) — 본문 페이지 머리 · 검색이 그대로 보인다. 딤 없음. 순서 = 제목 → 상태 칩 → "항목 | 값" 2열 행 → 아래 고정 동작 줄(위 1px #f0f0f0 선). 가운데 모달로 열지 않는다.
- 무거운 작업(7 · 11) = 본문 페이지. 가운데 단일 열 폭 640, "라벨 | 입력" 행 사이 1px #f0f0f0 선, 주 동작은 본문 하단 고정 바(#ffffff, 위 1px #f0f0f0 선, 오른쪽 정렬).
- 팝오버 · 드롭다운(모바일 고르기 시트의 데스크톱 모양): 누른 컨트롤에 바로 붙어 열림(s1-adopt #3), #ffffff, 1px #e0e0e0 테두리, rounded 24, 여백 24, 그림자 · 딤 없음, 오른쪽 위 × 닫기, 내용이 길면 안쪽 스크롤 + 아래 동작 줄 고정. 이번 run: 2-filter(list-filter-sheet 드롭다운 패널), 2-msds-bulk · 3-msds · 7-msds(msds-candidates 팝오버), 3-location(location-picker 팝오버), 11-slot(slot-sheet 팝오버).
- detail-drawer로 여는 상태: 3-* · 4-past-date · 16-*(바탕이 시약 상세 드로어), 11-print(qr-print-sheet), 12-result(qr-result-sheet).
- ex-modal-card(확인만): 11-delete · 11-unsaved. 프레임 가운데(사이드바 위까지 겹치는 자리, s1-adopt #4), 폭 480, #ffffff, 1px #e0e0e0 테두리, rounded 24, 여백 24, 딤 · 그림자 없음, 오른쪽 위 × 닫기. 위→아래 질문형 제목(heading-3) → 결과 설명 → 오른쪽 아래 버튼 2개(보조 button-outline 왼쪽 + 주 button-primary 오른쪽, 사이 8).
- 7-* · 11-*의 다른 상태는 본문 페이지 위 상태(페이지가 바뀐 모습). ex-toast는 오른쪽 아래(#ffffff, 1px #f0f0f0 테두리, rounded 24).
예시 데이터(공통): 오늘 = 2026-10-07. 샘플고등학교 시약 42종, 재고 부족 3종, MSDS 없는 시약 4종, 시약장 2개(1번 시약장 · 2번 시약장). 데스크톱 프레임 기준 역할 = 교사 "김OO · 교사"(sidebar-item 8개). 학생 · admin은 메뉴 수만 다르다.

## 화면 16
MSDS 요약(새 화면, rules.json msds_summary). 학생·교사·admin 모두(둘러보기도 같음). msds-entry "MSDS 보기"(화면 3·10 등)가 바깥 사이트 대신 이 화면을 연다. 역할별 차이 없음. 요약은 물질안전보건자료(한국산업안전보건공단) 내용을 서버에서 가져와 보여 준다(연결 값은 서버에서만, N2).
예시 상태(16-mobile · 16-desktop): 질산은(샘플고등학교 시약, 보관 분류 산화제). 신호어 "위험". 그림문자 3개 — 산화성 · 부식성 · 수생환경 유해성. 항목 요약 —
2. 유해·위험성: 화재를 강렬하게 할 수 있어요(산화제) / 피부에 심한 화상과 눈 손상을 일으켜요 / 수생생물에 매우 유독하고 오래 영향을 줘요
4. 응급조치 요령: 눈에 들어가면 물로 15분 이상 씻고 의사의 진료를 받아요 / 피부에 묻으면 오염된 옷을 벗고 물로 씻어요 / 삼켰을 때 억지로 토하게 하지 마세요
7. 취급 및 저장방법: 가연성 물질·환원제와 떨어뜨려 보관해요 / 빛을 피해 갈색 병에, 서늘하고 건조한 곳에 둬요 / 용기를 꼭 닫아 둬요
8. 노출방지 및 개인보호구: 보안경·내화학 장갑·실험복을 착용해요 / 가루가 날리면 국소 배기 장치를 켜요 / 작업 뒤 손을 씻어요
모바일 활성 탭: "시약". 위→아래: nav-pill(‹ + "MSDS · 질산은" + 학교명) → 출처 줄 → msds-summary(신호어 → 그림문자 줄 → 항목 2·4·7·8 카드) → msds-original-link(맨 아래 전폭) → tab-bar. 좌우 여백 16, 블록 사이 24.
데스크톱 배치: app-sidebar("시약" 현재) | 본문 = 화면 2 시약 목록(data-table, "질산은" 행 #e6f4fc 선택) + 오른쪽 detail-drawer 480 안: "‹ 시약 상세"(화면 3에서 왔을 때) + × 닫기 → heading-3 "MSDS · 질산은" + 출처 줄 → 항목 바로가기 줄(2 · 4 · 7 · 8) → msds-summary → 드로어 아래 고정 msds-original-link.
### 구성 요소
- app-sidebar: 데스크톱 전용. 공통 규격, 학교명 "샘플고등학교" + 역할별 메뉴 + nav-account-menu
- sidebar-item: 데스크톱 전용. 학생 5개 / 교사 8개 / admin 10개(공통 메뉴). 현재 = "시약"
- nav-pill: 모바일 전용 헤더. 뒤로가기 ‹(이전 화면 — 화면 3 또는 10) + heading-3 "MSDS · 질산은" + 현재 학교명 "샘플고등학교"(caption) + nav-account-menu ▾. 그 아래 출처 줄 caption(#707070) "물질안전보건자료 · 한국산업안전보건공단". 하늘색: 뒤로가기 아이콘 #2b9fe0
- nav-account-menu: 모바일 = 학교명 옆 ▾, 데스크톱 = app-sidebar 맨 아래. "로그아웃" 1개. 하늘색 없음
- data-table: 데스크톱 전용. 드로어 뒤 화면 2 시약 표(열·정렬·페이지 번호 화면 2와 같음), 선택 행 "질산은" #e6f4fc
- detail-drawer: 데스크톱 전용. 폭 480, 높이 900, #ffffff, 왼쪽 1px #f0f0f0 선, 여백 24, 딤 없음. 위→아래: 조용한 텍스트 동작 "‹ 시약 상세"(link #141414, 화면 3 드로어에서 왔을 때만) + 오른쪽 위 × 닫기 → heading-3 "MSDS · 질산은" → 출처 줄 caption(#707070) "물질안전보건자료 · 한국산업안전보건공단" → 항목 바로가기 줄(조용한 텍스트 동작 "2. 유해·위험성" · "4. 응급조치" · "7. 취급·저장" · "8. 보호구", 누르면 그 항목으로 스크롤, 현재 항목 아래 #2b9fe0 밑줄, 글자 #141414) → msds-summary(드로어 안 스크롤) → 아래 고정 줄(위 1px #f0f0f0 선) msds-original-link. 하늘색: × 아이콘 #2b9fe0, 바로가기 밑줄
- msds-summary: 요약 본문. ① 신호어 pill "위험"(#141414 채움, #ffffff label, rounded 9999. "경고"면 #f3f3f3 채움 + #141414 label) — 핑크·빨강 없음 → ② 그림문자 줄: ghs-pictogram 3개 가로(사이 16) → ③ 항목 카드 4장(#ffffff, 1px #f0f0f0 테두리, rounded 24, 여백 24, 사이 12): 제목 title "2. 유해·위험성" · "4. 응급조치 요령" · "7. 취급 및 저장방법" · "8. 노출방지 및 개인보호구"(번호 포함 원문 항목명) + 요약 3줄(body #141414, 줄마다 글머리) + 조용한 텍스트 동작 "더 보기"(link #141414, 누름 영역 44 이상, 누르면 그 카드가 펼쳐져 전체 내용). 내용 없는 항목 = 카드 안 body #707070 "내용이 없어요". 불러오는 중 = msds-skeleton(상태 16-loading), 실패 = ex-empty-state-card "요약을 불러오지 못했어요" + msds-original-link(상태 16-fail), 공단 MSDS가 아니면(직접 입력 주소) 요약 없이 msds-original-link만(상태 16-no-summary). 모바일·데스크톱 같은 순서. 하늘색: "더 보기" 옆 ▾ 아이콘 #2b9fe0
- ghs-pictogram: GHS 그림문자 1개 = 흰 바탕(#ffffff) 마름모(정사각형 45° 회전, 한 변 56) + 표준 빨강 #ff0000 테두리(두께 4) + 검정(#141414) 그림 + 아래 caption #141414 이름. 예시 3개 "산화성"(원 위 불꽃) · "부식성"(손·금속 부식) · "수생환경 유해성"(죽은 물고기·나무). 9종 중 해당 것만, 순서는 MSDS 표기 순. #ff0000은 이 컴포넌트 안에서만, 핑크 결정 신호를 대신하지 않는다
- msds-original-link: 맨 아래 전폭 button-outline "원문 MSDS 보기 ↗"(#ffffff, 1px #e0e0e0, 라벨 #141414, rounded 9999, 높이 44 이상) — 공단 MSDS 페이지를 새 창으로 연다. 모바일 = 항목 카드 아래(tab-bar 위 간격 16), 데스크톱 = detail-drawer 아래 고정 줄. 하늘색: ↗ 아이콘 #2b9fe0
- button-outline: msds-original-link 버튼 모양(위 정의)
- msds-skeleton: 불러오는 중 자리 표시 — 신호어 자리 짧은 막대 1 + 그림문자 자리 마름모 3 + 항목 카드마다 제목 막대 1·본문 막대 3(#f3f3f3, rounded 9999, 실제 배치와 같은 자리). 이 프레임에서는 숨김(상태 16-loading)
- ex-empty-state-card: 요약 실패 "요약을 불러오지 못했어요" + 한 줄 "원문에서 확인해 주세요" + msds-original-link. 이 프레임에서는 숨김(상태 16-fail). 핑크 없음, 아이콘 #141414
- tab-bar: 모바일 전용 하단 탭바 1개(공통 규격). 데스크톱에는 두지 않는다. 하늘색: 활성 tab-item 아이콘 #2b9fe0만
- tab-item: "홈" · "시약" · "QR 스캔" · "기록" 4개. 활성 = "시약", 비활성 3개 #707070
### 반영한 레퍼런스
- https://uibowl.io/name/%EB%A9%94%EB%94%94%EC%BD%94%EC%B9%98?patterns=%EC%83%81%EC%84%B8%EC%A0%95%EB%B3%B4%20%28PDP%29&imgId=cms8ebafr002el204u8vddkky
- https://uibowl.io/name/%EC%8F%98%EC%B9%B4?patterns=%EC%83%81%EC%84%B8%EC%A0%95%EB%B3%B4%20%28PDP%29&imgId=cmogjs1bf0019la04rxwg16ac
- https://uibowl.io/name/G%20car?patterns=%EA%B2%80%EC%83%89&imgId=cmo84t624000fl5045bz2r4ic
- https://uibowl.io/website/%EB%AA%A8%EA%B0%81%EC%9E%91?patterns=%EA%B2%80%EC%83%89&imgId=cmow9lnp1000yky0427encrx9
- https://uibowl.io/website/%EB%A7%88%ED%94%8C?patterns=%EC%83%81%EC%84%B8%EC%A0%95%EB%B3%B4%20%28PDP%29&imgId=cmnnx4cuq02ikju04zkbrvx39
- https://uibowl.io/website/%EB%A7%A4%EB%8B%88%ED%8C%A8%EC%8A%A4%ED%8A%B8?patterns=%ED%81%90%EB%A0%88%EC%9D%B4%EC%85%98&imgId=cmulyw7j9001qjj04bmlsz9l1

## 상태 화면 2-msds-bulk
교사·admin이 화면 2 띠의 "한 번에 찾기"를 누른 상태(프레임 2-msds-bulk-mobile · 2-msds-bulk-desktop). 학생에게는 이 상태가 없다. 모바일 = runs/20261007-0002 그대로.
MSDS 없는 시약 4종을 차례로 하나씩 msds-candidates로 보여준다. 예시 = 첫 번째 시약 "질산은"(1 / 4), 후보 3개 중 첫 후보를 고른 상태. 모바일 = tab-bar 위 바텀시트(뒤 화면 2 그대로, 딤 없음).
데스크톱 배치: app-sidebar("시약" 현재) | 본문 = 화면 2 데스크톱 그대로(페이지 머리 "시약" + "42종" → msds-bulk-banner → 툴바 → data-table) + 띠의 "한 번에 찾기" 바로 아래에 붙은 msds-candidates 팝오버(폭 400, 오른쪽 끝을 버튼에 맞춤, 표 위에 겹침, 딤 없음). 표에서 지금 시약 "질산은" 행 #e6f4fc.
### 구성 요소
- app-sidebar: 데스크톱 전용. 공통 규격, 학교명 "샘플고등학교" + 교사 메뉴 + "김OO · 교사" + nav-account-menu (교사·admin만)
- sidebar-item: 데스크톱 전용. 교사 8개 / admin 10개(공통 메뉴). 현재 = "시약" (교사·admin만)
- nav-pill: 모바일 전용. 화면 2 nav-pill 그대로 — "Lab_Stock" + 현재 학교명 "샘플고등학교" + nav-account-menu ▾. 데스크톱에는 두지 않는다 (교사·admin만)
- nav-account-menu: 모바일 = 학교명 옆 ▾, 데스크톱 = app-sidebar 맨 아래(닫힌 상태) (교사·admin만)
- msds-bulk-banner: 모바일 = 시트 뒤에 보이는 띠 "MSDS 없는 시약 4종"(#e6f4fc, 누름 동작 없음). 데스크톱 = 페이지 머리 아래 본문 폭 띠(rounded 16, #e6f4fc 채움, 왼쪽 body-sm #141414 "MSDS 없는 시약 4종", 오른쪽 "한 번에 찾기" — 팝오버가 열린 상태). 하늘색: 띠 채움 #e6f4fc (교사·admin만)
- button-pill-soft: 띠 안 "한 번에 찾기"(#f3f3f3 채움, 라벨 #141414, rounded 9999, 높이 44 이상). 하늘색 없음 (교사·admin만)
- reagent-row: 모바일 전용. 시트 뒤 목록 행(누름 동작 없음) (교사·admin만)
- data-table: 데스크톱 전용. 팝오버 뒤 화면 2 시약 표(열·정렬·페이지 번호 화면 2와 같음, 누름 동작 없음), 지금 찾는 시약 "질산은" 행 #e6f4fc (교사·admin만)
- msds-candidates: 시트 1개 — 모바일 = tab-bar 위 바텀시트(#ffffff, 1px #e0e0e0 테두리, 위쪽 rounded 24, 여백 24, × 닫기), 데스크톱 = "한 번에 찾기"에 붙은 팝오버(폭 400, rounded 24, 같은 내용). 위→아래: 제목 heading-3 시약명 "질산은" + 오른쪽 caption(#707070) "1 / 4" → caption(#707070) "알맞은 MSDS를 골라 주세요" → 후보 행 3개(행 = 물질명 title #141414 위 + "CAS 7761-88-8" caption #707070 아래, #f3f3f3 채움, rounded 16, 행 사이 12, 누름 영역 44 이상): "질산은" · "질산은 용액" · "질산은(분석용)" — 선택 행 = 첫 행 → 목록 맨 끝 행 "찾는 게 없어요 — 직접 입력"(누르면 그 자리에서 text-input "MSDS 주소"가 펼쳐짐) → 하단 줄: 왼쪽 조용한 텍스트 동작 "건너뛰기"(link #141414, 누름 영역 44 이상) + 오른쪽 button-primary "이 MSDS로". 후보 0개면 후보 자리에 body-sm #141414 "찾지 못했어요 — 직접 입력" + text-input. 고르기 전에는 "이 MSDS로" 비활성. "이 MSDS로"·"건너뛰기" 뒤에는 다음 시약(2 / 4)으로 넘어가고, 데스크톱 표의 선택 행도 그 시약으로 옮겨간다. 하늘색: 선택 행 배경 #e6f4fc + 오른쪽 #2b9fe0 체크 아이콘(글자 #141414) (교사·admin만)
- text-input: "직접 입력" 행을 펼쳤을 때 "MSDS 주소" 입력(#f0f0f0, rounded 16, 포커스 링 2px #141414). 하늘색 없음 (교사·admin만)
- button-primary: 시트·팝오버 하단 "이 MSDS로"(#141414 채움, #ffffff 글자, rounded 9999, 높이 44 이상). 하늘색 없음 (교사·admin만)
- ex-toast: 마지막 시약까지 끝난 뒤 "MSDS 3종을 연결했어요 · 1종 건너뜀", 띠 숫자가 줄어든다. 모바일 tab-bar 위, 데스크톱 오른쪽 아래. 하늘색: 완료 체크 아이콘 #2b9fe0 (교사·admin만)
- tab-bar: 모바일 전용 하단 탭바 1개(공통 규격). 시트는 이 바 위쪽 선 위에 붙는다. 데스크톱에는 두지 않는다 (교사·admin만)
- tab-item: 4개 "홈" · "시약" · "QR 스캔" · "기록". 활성 = "시약" (교사·admin만)
### 반영한 레퍼런스
- https://uibowl.io/name/CJ%EB%8D%94%EB%A7%88%EC%BC%93?patterns=%EC%83%81%EC%84%B8%EC%A0%95%EB%B3%B4%20%28PDP%29&imgId=cmnn6372y0019l404vauwc9wd
- https://uibowl.io/name/MEXC?patterns=%EB%AA%A9%EB%A1%9D%20%28PLP%29&imgId=cmu9n15e0001vkx04vvzg8864
- https://uibowl.io/website/%EC%9E%94%EB%94%94?patterns=%EA%B8%B0%ED%83%80&imgId=cmpz4uagr000ajs04zj40zdih

## 상태 화면 2-filter
화면 2에서 "필터"를 눌러 list-filter-sheet가 열린 상태(프레임 2-filter-mobile · 2-filter-desktop). 모든 역할 같다(교사·admin은 뒤에 msds-bulk-banner가 함께 보인다). 모바일 = runs/20261007-0744 그대로.
예시 상태: 이미 보관 분류 "산" 1개가 적용되어 목록이 12종(filter-chip-row "산 ×" · "12종", list-filter-button 개수 "1"). 사용자가 필터를 다시 열어 정렬을 "재고 적은 순"으로 바꾸고 보관 분류 "산화제"를 더 고른 상태 → 하단 "18종 보기". 보관 위치는 "모든 시약장", "칸 없음만"·"MSDS 없는 시약만" 토글은 꺼짐. 모바일 = tab-bar 위 바텀시트(딤 없음).
데스크톱 배치: app-sidebar("시약" 현재) | 본문 = 화면 2 데스크톱 그대로(페이지 머리 왼쪽 "시약" + "12종" / 오른쪽 검색 text-input 폭 320 + list-filter-button "필터 1" → (교사·admin) msds-bulk-banner → 툴바 segmented-control 왼쪽 · filter-chip-row 오른쪽 → data-table "산" 결과 12행) + list-filter-button 바로 아래 드롭다운 패널 list-filter-sheet(폭 400, 오른쪽 끝을 버튼에 맞춤, 표 위에 겹침, 딤 없음, s1-adopt #2).
### 구성 요소
- app-sidebar: 데스크톱 전용. 공통 규격, 학교명 "샘플고등학교" + 역할별 메뉴 + 이름·역할 + nav-account-menu
- sidebar-item: 데스크톱 전용. 학생 5개 / 교사 8개 / admin 10개(공통 메뉴). 현재 = "시약"
- nav-pill: 모바일 전용. 화면 2 nav-pill 그대로 — "Lab_Stock" + 현재 학교명 "샘플고등학교" + nav-account-menu ▾. 데스크톱에는 두지 않는다
- nav-account-menu: 모바일 = 학교명 옆 ▾, 데스크톱 = app-sidebar 맨 아래(닫힌 상태)
- msds-bulk-banner: 패널 뒤 띠 "MSDS 없는 시약 4종"(#e6f4fc, 누름 동작 없음). 모바일 = nav-pill 아래 전폭 띠, 데스크톱 = 페이지 머리 아래 본문 폭 띠(rounded 16) (교사·admin만)
- segmented-control: 뒤 "전체 / 재고 부족"(누름 동작 없음). 데스크톱 = 툴바 왼쪽
- segmented-control-active: 뒤 선택 옵션 "전체" 흰 pill. 하늘색: 1px #2b9fe0 테두리(글자 #141414)
- text-input: 뒤 검색 "시약명 검색"(#f0f0f0, rounded 16). 모바일 = 검색 줄 왼쪽, 데스크톱 = 페이지 머리 오른쪽 폭 320. 하늘색: 검색 아이콘 #2b9fe0
- list-filter-button: "필터" + 개수 pill "1"(#e6f4fc 채움 + 1px #2b9fe0 테두리, label #141414, rounded 9999) — 저장 전이라 이미 적용된 개수. 데스크톱은 눌린 상태로 아래에 패널이 붙는다. 하늘색: 필터 아이콘 #2b9fe0, 개수 pill 채움·테두리
- filter-chip-row: 뒤 한 줄. 적용 칩 "산 ×"(#f3f3f3 채움, label #141414, rounded 9999, × 누름 영역 44 이상) → 조용한 텍스트 동작 "모두 지우기"(link #141414) → 줄 오른쪽 끝 caption(#707070) "12종". 모바일 = 검색 줄 아래, 데스크톱 = 툴바 segmented-control 오른쪽. 하늘색 없음
- reagent-row: 모바일 전용. 시트 뒤 "산" 필터 결과 행(누름 동작 없음), #f3f3f3, rounded 16. 하늘색 없음
- data-table: 데스크톱 전용. 패널 뒤 "산" 결과 12행 시약 표(열 = 화면 2와 같음, 정렬 화살표는 아직 이름순 ↑ #2b9fe0, 누름 동작 없음)
- badge-low-stock: 뒤 재고 부족 행(염산 · 1병) "재고 부족"(#d6246a 채움, #ffffff label). 모바일 = 시약명 옆, 데스크톱 = data-table 상태 열. 하늘색 없음
- list-filter-sheet: 필터 1개(#ffffff, 1px #e0e0e0 테두리, 여백 24, 오른쪽 위 × 닫기) — 모바일 = tab-bar 위 바텀시트(위쪽 rounded 24), 데스크톱 = list-filter-button 아래 드롭다운 패널(폭 400, rounded 24, 패널 안 스크롤 + 하단 줄 고정). 위→아래, 구역 사이 24: ① 제목 heading-3 "필터" → ② 구역 "정렬"(heading-4) + 한 줄 pill 3개 "이름순"(기본) · "재고 적은 순" · "최근 입고순", 한 번에 하나, 선택 = "재고 적은 순" → ③ 구역 "보관 분류"(heading-4) + 오른쪽 caption(#707070) "여러 개 고를 수 있어요" + storage-class-chip 9개 줄바꿈 배치 → ④ 구역 "보관 위치"(heading-4) + 시약장 선택 상자(text-input 모양, 값 "모든 시약장" ▾, 목록 = "모든 시약장" · cabinet-number(1) "1번 시약장" · cabinet-number(2) "2번 시약장") → 칸 선택 상자(값 "모든 칸" ▾, 시약장을 고르기 전 비활성 #adadad) → 토글 줄 "칸 없음만"(body #141414 + 오른쪽 토글, 꺼짐) → ⑤ 토글 줄 "MSDS 없는 시약만"(꺼짐) → ⑥ 하단 고정 줄(위 1px #f0f0f0 선, 위 여백 16): 왼쪽 좁은 button-outline "초기화" + 오른쪽 넓은 button-primary "18종 보기"(비율 1:2, 사이 8). 결과가 0종이면 "0종 보기"로 보이고 누르면 상태 화면 2-filter-empty. 정렬 pill 미선택 = #f3f3f3 채움, 라벨 #141414, rounded 9999, 높이 44 이상 / 토글 꺼짐 = #e0e0e0 트랙 + #ffffff 손잡이, 켜짐 = #2b9fe0 트랙 + #ffffff 손잡이. 하늘색: 선택 정렬 pill #e6f4fc 채움 + 1px #2b9fe0 테두리(글자 #141414), 선택 상자 ▾ 아이콘 #2b9fe0, 토글 켜짐 트랙
- storage-class-chip: list-filter-sheet "보관 분류" 칩 9개 — "유기" · "산" · "염기" · "산화제" · "인화성" · "무기염" · "독성" · "기타" · "분류 없음". 여러 개 선택. 미선택 = #f3f3f3 채움, label #141414, rounded 9999, 높이 44 이상. 선택 = "산"·"산화제". 핑크 없음. 하늘색: 선택 칩 #e6f4fc 채움 + 1px #2b9fe0 테두리(글자 #141414)
- cabinet-number: 보관 위치 시약장 목록의 이름 앞 작은 원(#ffffff, 1px #e0e0e0, rounded 9999) 안 숫자 "1"·"2"(label #141414). 핑크·하늘색 글자 없음
- button-outline: 필터 하단 "초기화"(#ffffff, 1px #e0e0e0, 라벨 #141414, rounded 9999, 높이 44 이상) — 누르면 필터 안 선택이 기본값으로 돌아간다. 하늘색 없음
- button-primary: 필터 하단 "18종 보기"(#141414 채움, #ffffff 글자, rounded 9999, 높이 44 이상) — 누르면 필터가 닫히고 목록(데스크톱은 data-table)·filter-chip-row("산 ×" · "산화제 ×" · "18종")·개수 pill "2"가 바뀐다. 하늘색 없음
- tab-bar: 모바일 전용 하단 탭바 1개(공통 규격). 시트는 이 바 위쪽 선 위에 붙는다. 데스크톱에는 두지 않는다. 하늘색: 활성 tab-item 아이콘 #2b9fe0만
- tab-item: 4개 "홈" · "시약" · "QR 스캔" · "기록". 활성 = "시약"
### 반영한 레퍼런스
- https://uibowl.io/name/%EC%B9%B4%EC%B9%B4%EC%98%A4%EA%B3%A8%ED%94%84%EC%98%88%EC%95%BD?patterns=%ED%95%84%ED%84%B0&imgId=cmtwlv9y9002eky04rfw0ikms
- https://uibowl.io/name/Kia?patterns=%ED%95%84%ED%84%B0&imgId=cmpurx7l00005kt04fgdc2lvh
- https://uibowl.io/name/%EB%B3%BC%ED%8A%B8%EC%97%85?patterns=%ED%95%84%ED%84%B0&imgId=cmojep21l001hjs04hvksxikk
- https://uibowl.io/name/%ED%94%8C%EB%A6%AC%EB%8D%94%EC%8A%A4?patterns=%ED%95%84%ED%84%B0&imgId=cmubb0zcz0038l404q4aoyftn
- https://uibowl.io/website/%ED%98%81%EC%8B%A0%EC%9D%98%EC%88%B2?patterns=%ED%95%84%ED%84%B0&imgId=cmiqzsrbu001ol404pjyckvpt

## 상태 화면 2-filter-empty
적용한 필터에 맞는 시약이 0종인 상태(프레임 2-filter-empty-mobile · 2-filter-empty-desktop). 모든 역할 같다. 핑크 없음 — 재고 부족이 아니다. 모바일 = runs/20261007-0744 그대로.
예시 상태: 보관 분류 "독성" + 보관 위치 "2번 시약장" 적용 → 0종. list-filter-button 개수 "2". 목록 자리에 빈 상태 카드.
데스크톱 배치: app-sidebar("시약" 현재) | 본문 = 페이지 머리(왼쪽 "시약" + "0종" / 오른쪽 검색 + list-filter-button "필터 2") → (교사·admin) msds-bulk-banner → 툴바(segmented-control 왼쪽, filter-chip-row 오른쪽) → data-table: 열 머리행은 그대로 두고 표 몸통 가운데에 ex-empty-state-card + "필터 지우기"(s1-adopt #2). 페이지 번호 없음.
### 구성 요소
- app-sidebar: 데스크톱 전용. 공통 규격, 학교명 "샘플고등학교" + 역할별 메뉴 + 이름·역할 + nav-account-menu
- sidebar-item: 데스크톱 전용. 학생 5개 / 교사 8개 / admin 10개(공통 메뉴). 현재 = "시약"
- nav-pill: 모바일 전용. 화면 2 nav-pill 그대로 — "Lab_Stock" + 현재 학교명 "샘플고등학교" + nav-account-menu ▾. 데스크톱에는 두지 않는다
- nav-account-menu: 모바일 = 학교명 옆 ▾, 데스크톱 = app-sidebar 맨 아래(닫힌 상태)
- msds-bulk-banner: 화면 2와 같은 띠 "MSDS 없는 시약 4종" + "한 번에 찾기"(학교 전체 기준이라 필터 결과와 상관없이 보임). 모바일 = 전폭 띠, 데스크톱 = 본문 폭 띠(rounded 16). 하늘색: 띠 채움 #e6f4fc (교사·admin만)
- segmented-control: "전체 / 재고 부족", 선택 = "전체". 데스크톱 = 툴바 왼쪽
- segmented-control-active: "전체" 흰 pill. 하늘색: 1px #2b9fe0 테두리(글자 #141414)
- text-input: 검색 "시약명 검색"(빈 값, #f0f0f0, rounded 16). 데스크톱 = 페이지 머리 오른쪽 폭 320. 하늘색: 검색 아이콘 #2b9fe0
- list-filter-button: "필터" + 개수 pill "2"(#e6f4fc 채움 + 1px #2b9fe0 테두리, label #141414). 누르면 list-filter-sheet(모바일 시트, 데스크톱 드롭다운 패널, 지금 조건이 선택된 채). 하늘색: 필터 아이콘 #2b9fe0, 개수 pill 채움·테두리
- filter-chip-row: 적용 칩 "독성 ×" · "cabinet-number(2) 2번 시약장 ×"(#f3f3f3 채움, label #141414, rounded 9999, × 누름 영역 44 이상) → "모두 지우기"(link #141414) → 오른쪽 끝 caption(#707070) "0종". 모바일 = 검색 줄 아래, 데스크톱 = 툴바 segmented-control 오른쪽. 하늘색 없음
- cabinet-number: "2번 시약장" 칩 안 이름 앞 작은 원(#ffffff, 1px #e0e0e0) 안 숫자 "2"(label #141414). 핑크·하늘색 글자 없음
- data-table: 데스크톱 전용. 열 머리행(시약명 · 보관 분류 · 보관 위치 · 재고 · 상태 · 최근 입고일 · MSDS)은 남기고 행 0개, 표 몸통 가운데에 ex-empty-state-card
- ex-empty-state-card: 목록 자리 가운데 카드(#ffffff, 1px #f0f0f0 테두리, rounded 24, 여백 24). #141414 안내 아이콘 → heading-4 "조건에 맞는 시약이 없어요" → body-sm(#707070) "칩을 하나씩 빼거나 필터를 지워 보세요" → button-outline "필터 지우기". 모바일 = 목록 자리, 데스크톱 = data-table 몸통 안. 핑크 없음. 하늘색 없음(아이콘 #141414)
- button-outline: 빈 상태 카드 안 "필터 지우기"(#ffffff, 1px #e0e0e0, 라벨 #141414, rounded 9999, 높이 44 이상) — 누르면 모든 필터가 빠지고 화면 2(42종)로. 정렬은 그대로. 하늘색 없음
- tab-bar: 모바일 전용 하단 탭바 1개(공통 규격). 데스크톱에는 두지 않는다. 하늘색: 활성 tab-item 아이콘 #2b9fe0만
- tab-item: 4개 "홈" · "시약" · "QR 스캔" · "기록". 활성 = "시약"
### 반영한 레퍼런스
- https://uibowl.io/name/%EC%98%A4%EC%9D%BC%EB%82%98%EC%9A%B0?patterns=%EA%B2%80%EC%83%89&imgId=cmtpnvoci000rlh04frsnnhkt
- https://uibowl.io/name/%EB%B3%BC%ED%8A%B8%EC%97%85?patterns=%ED%95%84%ED%84%B0&imgId=cmojep21l001hjs04hvksxikk
- https://uibowl.io/website/%ED%98%81%EC%8B%A0%EC%9D%98%EC%88%B2?patterns=%ED%95%84%ED%84%B0&imgId=cmiqzsrbu001ol404pjyckvpt

## 상태 화면 3-location
교사·admin이 화면 3에서 "위치 바꾸기"를 누른 상태(프레임 3-location-mobile · 3-location-desktop). 학생에게는 이 상태가 없다. 모바일 = runs/20261007-0002 그대로.
예시 상태: 과산화수소, 현재 위치 1번 시약장 · 우 1단(산화제, 시약 3개). 추천 규칙(rules.json suggest.rule)에 따라 2번 시약장 · 우 2단(산화제, 시약 0개)이 추천 칸이고, 피커는 2번 시약장이 열린 채 그 칸이 처음 선택되어 있다. 분류가 맞아 mix-warning은 숨김. 모바일 = tab-bar 위 바텀시트(뒤 화면 3 그대로, 딤 없음).
데스크톱 배치: app-sidebar("시약" 현재) | 본문 720 = 화면 2 시약 표("과산화수소" 행 #e6f4fc 선택) | detail-drawer 480 = 화면 3 시약 상세(1차 승인 배치 그대로) + 드로어 "보관 위치" 행의 "위치 바꾸기"에 붙은 location-picker 팝오버(폭 400, 드로어 왼쪽으로 펼쳐 표 위에 겹침, 딤 없음, s1-adopt #3).
### 구성 요소
- app-sidebar: 데스크톱 전용. 공통 규격, 학교명 "샘플고등학교" + 교사 메뉴 + "김OO · 교사" + nav-account-menu (교사·admin만)
- sidebar-item: 데스크톱 전용. 교사 8개 / admin 10개(공통 메뉴). 현재 = "시약" (교사·admin만)
- nav-pill: 모바일 전용. 뒤 화면 3 nav-pill 그대로 — 뒤로가기 + "시약 상세" + 현재 학교명 "샘플고등학교" + nav-account-menu ▾. 하늘색: 뒤로가기 아이콘 #2b9fe0 (교사·admin만)
- nav-account-menu: 모바일 = 학교명 옆 ▾, 데스크톱 = app-sidebar 맨 아래(닫힌 상태) (교사·admin만)
- data-table: 데스크톱 전용. 드로어 왼쪽 화면 2 시약 표(본문 720 폭), 선택 행 "과산화수소" #e6f4fc. 팝오버가 열린 동안 누름 동작 없음 (교사·admin만)
- detail-drawer: 데스크톱 전용. 화면 3 시약 상세 드로어 그대로(× 닫기 → heading-3 "과산화수소" → 상태 칩 줄 badge-low-stock "재고 부족" + 보관 분류 "산화제" → segmented-control "정보 / 사용 기록" → "항목 | 값" 행: 현재 재고 "2병" · 입고일 · reagent-location 행 · reorder-threshold 행 → msds-entry → 아래 고정 "사용 기록" + "입고"). 팝오버가 열린 동안 누름 동작 없음 (교사·admin만)
- reagent-detail-card: 모바일 = 시트 뒤 화면 3 요약 카드(누름 동작 없음), 데스크톱 = 카드 테두리 없이 드로어 "항목 | 값" 행으로 같은 내용. 하늘색 없음 (교사·admin만)
- reagent-location: 카드(데스크톱은 드로어 행) 안 "보관 위치 · (1) 1번 시약장 · 우 1단" — 저장 전이라 옛 위치 (교사·admin만)
- location-edit: reagent-location 줄 오른쪽 button-pill-soft "위치 바꾸기"(#f3f3f3, 라벨 #141414, rounded 9999, 높이 44 이상) — 눌린 상태. 데스크톱 팝오버는 이 버튼에 붙는다 (교사·admin만)
- location-picker: 피커 1개(#ffffff, 1px #e0e0e0 테두리, 여백 24) — 모바일 = tab-bar 위 바텀시트(위쪽 rounded 24), 데스크톱 = 팝오버(폭 400, rounded 24, 안쪽 스크롤 + "저장" 줄 고정). 위→아래: 제목 heading-3 "보관 위치 바꾸기" + × 닫기 → caption(#707070) "과산화수소 · 산화제" → 구역 제목 heading-4 "추천" + 추천 칸 1행(cabinet-number "2" + "2번 시약장 · 우 2단" body #141414 + suggest-badge, 선택 상태 #e6f4fc 배경) → 구역 제목 heading-4 "전체" + cabinet-switcher → 고른 시약장의 cabinet-slot 배치도(양문형 · 3단, 각 칸 분류 이름 + slot-count) → 조용한 텍스트 동작 "칸 없음으로"(link #141414, 누름 영역 44 이상) → mix-warning(조건부) → 하단 전폭 button-primary "저장". 추천 칸이 처음 선택이라 "저장"은 바로 활성 (교사·admin만)
- cabinet-switcher: "전체" 구역 시약장 전환 pill 한 줄 "(1) 1번 시약장" · "(2) 2번 시약장". 활성 = "2번 시약장"(#e6f4fc 채움 + 1px #2b9fe0 테두리, 라벨 #141414), 비활성 #f3f3f3. 피커 안에는 cabinet-add 없음. 하늘색: 활성 pill 채움·테두리 (교사·admin만)
- cabinet-number: 추천 행·cabinet-switcher pill·reagent-location 값 이름 앞 작은 원(#ffffff, 1px #e0e0e0) 안 숫자 "1"·"2"(label #141414) (교사·admin만)
- cabinet-slot: 2번 시약장 배치도 칸 6개(#f3f3f3, rounded 16, 분류 이름 label #141414, 없으면 "미지정" #707070). 왼쪽 단 라벨 "1단"~"3단", 위 문 라벨 "좌"/"우". 누르면 그 칸 선택. 선택 칸 = "우 2단"(산화제). 데스크톱 팝오버 폭 400 안에 6칸이 한 화면에 들어온다. 하늘색: 선택 칸 배경 #e6f4fc + 2px #2b9fe0 테두리(글자 #141414) (교사·admin만)
- slot-count: 시약이 있는 cabinet-slot 오른쪽 위 작은 pill(#ffffff, rounded 9999, label #141414) — 예: 좌 1단 "2", 좌 2단 "3". 빈 칸(우 2단 포함)에는 없음. 핑크·하늘색 없음 (교사·admin만)
- suggest-badge: 추천 칸 표시 pill "추천"(#e6f4fc 채움, 1px #2b9fe0 테두리, label #141414, rounded 9999). 두 곳 — "추천" 구역 행 오른쪽, 배치도의 우 2단 칸 왼쪽 위 모서리. 선택 상태(칸 테두리)와는 따로 보인다. 핑크 금지 (교사·admin만)
- mix-warning: 다른 칸을 골라 분류가 맞지 않을 때만 배치도 아래(#fbe9f0 바탕, rounded 16, #d6246a 경고 아이콘 + #141414 body-sm). "이 칸은 {분류} 칸이에요 — 그래도 넣을 수 있어요" / 금지 조합이면 "{A}와 {B}는 섞으면 위험해요" + "그래도 저장할 수 있어요". 이 예시(추천 칸 선택)에서는 숨김. 하늘색 없음 (교사·admin만)
- button-primary: 피커 하단 전폭 "저장"(#141414 채움, #ffffff 글자, rounded 9999, 높이 44 이상). mix-warning이 있어도 활성. 저장하면 데스크톱은 팝오버가 닫히고 드로어 "보관 위치" 행이 바뀌며 오른쪽 아래 ex-toast "보관 위치를 바꿨어요". 하늘색 없음 (교사·admin만)
- tab-bar: 모바일 전용 하단 탭바 1개(공통 규격). 시트는 이 바 위에 붙는다. 데스크톱에는 두지 않는다 (교사·admin만)
- tab-item: 4개 "홈" · "시약" · "QR 스캔" · "기록". 활성 = "시약" (교사·admin만)
### 반영한 레퍼런스
- https://uibowl.io/name/Bitget?patterns=%EC%9D%B8%EC%A6%9D%ED%95%98%EA%B8%B0&imgId=cmukqaul5002ll60430j2ykk1
- https://uibowl.io/name/%ED%81%AC%EB%AA%BD?patterns=%EC%98%88%EC%95%BD%C2%B7%EA%B2%B0%EC%A0%9C&imgId=cmopq830p000zlb0439kx2zpr
- https://uibowl.io/website/%EC%9E%94%EB%94%94?patterns=%EA%B8%B0%ED%83%80&imgId=cmpz4uagr000ajs04zj40zdih

## 상태 화면 3-msds
교사·admin이 MSDS 없는 시약의 상세에서 "MSDS 찾기"를 누른 상태(프레임 3-msds-mobile · 3-msds-desktop). 학생에게는 이 상태가 없다(학생은 msds-entry 자리에 "MSDS가 아직 없어요"만 본다). 모바일 = runs/20261007-0002 그대로.
예시 상태: 질산은 상세(재고 5 g). 뒤 = 화면 3(MSDS 없음 상태), 위에 msds-candidates. 후보 3개 중 첫 후보 선택. 모바일 = tab-bar 위 바텀시트.
데스크톱 배치: app-sidebar("시약" 현재) | 본문 720 = 화면 2 시약 표("질산은" 행 #e6f4fc 선택) | detail-drawer 480 = 질산은 시약 상세(msds-entry 자리 "MSDS가 아직 없어요" + "MSDS 찾기") + "MSDS 찾기"에 붙은 msds-candidates 팝오버(폭 400, 드로어 왼쪽으로 펼쳐 표 위에 겹침, 딤 없음).
### 구성 요소
- app-sidebar: 데스크톱 전용. 공통 규격, 학교명 "샘플고등학교" + 교사 메뉴 + "김OO · 교사" + nav-account-menu (교사·admin만)
- sidebar-item: 데스크톱 전용. 교사 8개 / admin 10개(공통 메뉴). 현재 = "시약" (교사·admin만)
- nav-pill: 모바일 전용. 뒤로가기 + "시약 상세" + 현재 학교명 "샘플고등학교" + nav-account-menu ▾. 하늘색: 뒤로가기 아이콘 #2b9fe0 (교사·admin만)
- nav-account-menu: 모바일 = 학교명 옆 ▾, 데스크톱 = app-sidebar 맨 아래(닫힌 상태) (교사·admin만)
- data-table: 데스크톱 전용. 드로어 왼쪽 화면 2 시약 표, 선택 행 "질산은" #e6f4fc(MSDS 열 "없음" #707070). 팝오버가 열린 동안 누름 동작 없음 (교사·admin만)
- detail-drawer: 데스크톱 전용. 질산은 시약 상세 드로어(× 닫기 → heading-3 "질산은" → 상태 칩 줄 badge-low-stock "재고 부족" + 보관 분류 "산화제" → segmented-control → "항목 | 값" 행 → msds-entry → 아래 고정 "사용 기록" + "입고"). 누름 동작 없음 (교사·admin만)
- reagent-detail-card: 모바일 = 시트 뒤 질산은 요약 카드(누름 동작 없음), 데스크톱 = 드로어 "항목 | 값" 행으로 같은 내용. 하늘색 없음 (교사·admin만)
- msds-entry: 시트 뒤 MSDS 블록 — QR 자리에 caption(#707070) "MSDS가 아직 없어요" + 그 아래 msds-search (교사·admin만)
- msds-search: msds-entry 안 button-pill-soft "MSDS 찾기"(눌린 상태, 시트·팝오버가 열림). 하늘색: 검색 아이콘 #2b9fe0 (교사·admin만)
- msds-candidates: 1개(#ffffff, 1px #e0e0e0 테두리, 여백 24, × 닫기) — 모바일 = tab-bar 위 바텀시트(위쪽 rounded 24), 데스크톱 = "MSDS 찾기"에 붙은 팝오버(폭 400, rounded 24). 위→아래: 제목 heading-3 "MSDS 찾기" → caption(#707070) "질산은" → 검색 text-input(값 "질산은", 바꿔서 다시 찾을 수 있음) → 후보 행 3개(물질명 title 위 + "CAS 7761-88-8" caption #707070 아래, #f3f3f3, rounded 16, 행 사이 12): "질산은" · "질산은 용액" · "질산은(분석용)", 선택 = 첫 행 → 목록 맨 끝 "찾는 게 없어요 — 직접 입력" 행(누르면 그 자리에서 "MSDS 주소" text-input이 펼쳐짐) → 하단 전폭 button-primary "이 MSDS로". 후보 0개 = 결과 자리에 body-sm #141414 "찾지 못했어요 — 직접 입력" + text-input. 고르기 전 "이 MSDS로" 비활성. 하늘색: 선택 행 배경 #e6f4fc + 오른쪽 #2b9fe0 체크 아이콘(글자 #141414) (교사·admin만)
- text-input: 안쪽 검색 입력과 "직접 입력" 펼침의 "MSDS 주소" 입력(#f0f0f0, rounded 16, 포커스 링 2px #141414). 하늘색: 검색 아이콘 #2b9fe0 (교사·admin만)
- button-primary: 하단 "이 MSDS로"(#141414 채움, #ffffff 글자, rounded 9999, 높이 44 이상). 하늘색 없음 (교사·admin만)
- ex-toast: 연결 직후 "MSDS를 연결했어요" → msds-entry가 QR + "MSDS 보기 ›"로 바뀐다. 모바일 tab-bar 위, 데스크톱 오른쪽 아래. 하늘색: 완료 체크 아이콘 #2b9fe0 (교사·admin만)
- tab-bar: 모바일 전용 하단 탭바 1개(공통 규격). 시트는 이 바 위에 붙는다. 데스크톱에는 두지 않는다 (교사·admin만)
- tab-item: 4개 "홈" · "시약" · "QR 스캔" · "기록". 활성 = "시약" (교사·admin만)
### 반영한 레퍼런스
- https://uibowl.io/name/%ED%86%A0%EC%8A%A4%EC%A6%9D%EA%B6%8C?patterns=%EC%BB%A4%EB%AE%A4%EB%8B%88%ED%8B%B0&imgId=cmsb4ub9l0009jo042gue22tj
- https://uibowl.io/name/%EC%95%B3%ED%94%8C%EB%A6%AC?patterns=%EA%B2%80%EC%83%89&imgId=cmtpokg65000pi804zwlm86ih
- https://uibowl.io/name/%EB%84%A4%EC%9D%B4%EB%B2%84%EB%B8%94%EB%A1%9C%EA%B7%B8?patterns=%ED%95%84%ED%84%B0&imgId=cmumdx3pp008yjm04zoku825b
- https://uibowl.io/website/%EC%9E%94%EB%94%94?patterns=%EA%B8%B0%ED%83%80&imgId=cmpz4uagr000ajs04zj40zdih

## 상태 화면 4-past-date
사용일을 오늘이 아닌 지난 날로 고른 상태(프레임 4-past-date-mobile · 4-past-date-desktop). 모든 역할 같다. 핑크 없음 — 확인 안내다. 모바일 = runs/20261007-0744 그대로.
예시 상태: 에탄올(현재 재고 1,200 mL), 사용량 50 mL, 사용일 "2026-10-03"(날짜를 고른 뒤 시트·달력은 닫힘). 저장 버튼 바로 위에 안내 한 줄.
데스크톱 배치: app-sidebar("시약" 현재) | 본문 720 = 화면 2 시약 표("에탄올" 행 #e6f4fc 선택) | detail-drawer 480 = 화면 4 사용 기록 폼(1차 승인 배치 그대로: "‹ 시약 상세" → "사용 기록" + "에탄올 · 현재 1,200 mL" → "라벨 | 입력" 행 사용량 · 사용일 · 사용자 · 메모) + 아래 고정 줄 = past-date-note 한 줄 위, "사용 기록 저장" 아래.
### 구성 요소
- app-sidebar: 데스크톱 전용. 공통 규격, 학교명 "샘플고등학교" + 역할별 메뉴 + 이름·역할 + nav-account-menu
- sidebar-item: 데스크톱 전용. 학생 5개 / 교사 8개 / admin 10개(공통 메뉴). 현재 = "시약"
- nav-pill: 모바일 전용. 화면 4 nav-pill 그대로 — 뒤로가기 + "사용 기록" + 현재 학교명 "샘플고등학교" + nav-account-menu ▾. 하늘색: 뒤로가기 아이콘 #2b9fe0
- nav-account-menu: 모바일 = 학교명 옆 ▾, 데스크톱 = app-sidebar 맨 아래(닫힌 상태)
- data-table: 데스크톱 전용. 드로어 왼쪽 화면 2 시약 표, 선택 행 "에탄올" #e6f4fc
- detail-drawer: 데스크톱 전용. 폭 480, 높이 900, #ffffff, 왼쪽 1px #f0f0f0 선, 여백 24, × 닫기. 위→아래: 조용한 텍스트 동작 "‹ 시약 상세"(link #141414, 누름 영역 44 이상) → heading-3 "사용 기록" + caption(#707070) "에탄올 · 현재 1,200 mL" → "라벨 | 입력" 행(사이 1px #f0f0f0 선): 사용량 · 사용일(usage-date) · 사용자 · 메모 → 아래 고정 줄(위 1px #f0f0f0 선): past-date-note → button-primary "사용 기록 저장" 전폭
- reagent-detail-card: 모바일 = 폼 위 요약 "에탄올" + "1,200 mL"(#ffffff, 1px #f0f0f0 테두리, rounded 24, 여백 24). 데스크톱 = 드로어 제목 아래 caption 한 줄로 대신. 하늘색 없음
- text-input: "사용량" 50 + 단위 칩 "mL", "사용자"(로그인한 사용자 기본값), "메모"(#f0f0f0, rounded 16). 모바일 = 라벨 위·입력 아래, 데스크톱 = 라벨 왼쪽 | 입력 오른쪽. 하늘색: 단위 칩 선택 상태 #e6f4fc + 1px #2b9fe0 테두리(글자 #141414)
- usage-date: 사용량 아래 "사용일"(필수) 날짜 칸, 값 "2026-10-03"(#f0f0f0, rounded 16, 오른쪽 달력 아이콘). 다시 누르면 모바일은 날짜 고르기 시트, 데스크톱은 칸 아래 붙는 달력 팝오버가 10월 3일이 선택된 채 열린다(오늘 이후 흐림 #adadad). 하늘색: 달력 아이콘 #2b9fe0
- past-date-note: 저장 버튼 바로 위(버튼 위 간격 8) 무채색 안내 한 줄. 왼쪽 작은 달력 아이콘 #707070 + body-sm #707070 "10월 3일 사용으로 기록해요". 채움·테두리 없음. 모바일 = 하단 전폭 버튼 위, 데스크톱 = 드로어 아래 고정 줄 안 버튼 위. 사용일을 오늘로 되돌리면 사라진다. 핑크·하늘색 없음
- button-primary: "사용 기록 저장"(#141414 채움, #ffffff 글자, rounded 9999, 높이 44 이상). 모바일 = 하단 전폭 tab-bar 바로 위, 데스크톱 = 드로어 아래 고정 줄 전폭. 지난 날이어도 바로 저장된다(추가 확인 없음). 하늘색 없음
- ex-toast: 저장 직후 "10월 3일 사용 기록을 저장했어요". 모바일 tab-bar 위, 데스크톱 오른쪽 아래(드로어는 시약 상세로). 하늘색: 완료 체크 아이콘 #2b9fe0
- tab-bar: 모바일 전용 하단 탭바 1개(공통 규격). 데스크톱에는 두지 않는다. 하늘색: 활성 tab-item 아이콘 #2b9fe0만
- tab-item: 4개 "홈" · "시약" · "QR 스캔" · "기록". 활성 = "기록"
### 반영한 레퍼런스
- https://uibowl.io/name/%EB%A9%94%EA%B0%80MCG%EC%BB%A4%ED%94%BC?patterns=%EB%82%B4%EC%97%AD&imgId=cmt6me0kb000gl804oncd5vge
- https://uibowl.io/name/%ED%82%A4%ED%94%BC%EB%9F%BD?patterns=%EB%A9%94%EC%9D%B8&imgId=cmow8tk98000el704gib8a8ij

## 상태 화면 7-doc-upload
서류를 올리고 "AI로 읽기"를 누른 직후 읽는 중 상태(프레임 7-doc-upload-mobile · 7-doc-upload-desktop). 교사·admin 전용. 모바일 = runs/20261007-0002 그대로.
예시 상태: 거래명세서 사진 1장 "거래명세서_1007.jpg"(1.8MB). 헤더와 intake-mode는 그대로 남고, doc-upload 카드가 진행 상태로 바뀐다. 취소할 수 있다.
데스크톱 배치: app-sidebar("입고" 현재) | 본문 페이지(화면 7 데스크톱 1차 승인 배치 그대로) = 페이지 머리 "입고" → 가운데 단일 열 폭 640: intake-mode → doc-upload 카드(진행 상태) → 본문 하단 고정 바(button-primary "AI로 읽기" 오른쪽, 비활성).
### 구성 요소
- app-sidebar: 데스크톱 전용. 공통 규격, 학교명 "샘플고등학교" + 교사 메뉴 + "김OO · 교사" + nav-account-menu (교사·admin만)
- sidebar-item: 데스크톱 전용. 교사 8개 / admin 10개(공통 메뉴). 현재 = "입고" (교사·admin만)
- nav-pill: 모바일 전용. "Lab_Stock" + "입고·시약 등록" + 현재 학교명 "샘플고등학교" + nav-account-menu ▾ (교사·admin만)
- nav-account-menu: 모바일 = 학교명 옆 ▾, 데스크톱 = app-sidebar 맨 아래(닫힌 상태) (교사·admin만)
- intake-mode: "직접 입력 / 서류로 입고", 활성 = "서류로 입고". 읽는 동안 누름 동작 없음. 데스크톱 = 640 열 맨 위 (교사·admin만)
- segmented-control-active: intake-mode 활성 옵션 흰 pill. 하늘색: 1px #2b9fe0 테두리(글자 #141414) (교사·admin만)
- doc-upload: 같은 카드(#ffffff, 1px #e0e0e0, rounded 24, 여백 24)가 진행 상태로 바뀜. 위→아래: 올린 서류 미리보기 타일(비율 유지, rounded 16) + 그 위 badge-overlay 파일 이름 → 진행 막대(트랙 #e6f4fc, 채움 #2b9fe0, rounded 9999) → heading-4 "읽는 중이에요" → body-sm(#707070) "품목·규격·수량을 찾고 있어요" → caption(#707070) "잠시만 기다려 주세요" → button-outline "취소". 데스크톱 = 640 열 안 같은 카드(미리보기 타일 폭 240 가운데). 하늘색: 진행 막대 #2b9fe0 + 트랙 #e6f4fc (교사·admin만)
- badge-overlay: 미리보기 위 파일 이름 태그 "거래명세서_1007.jpg"(rgba(115,115,115,0.56) 채움, #ffffff label, rounded 9999). 하늘색 없음 (교사·admin만)
- button-outline: doc-upload 안 "취소"(#ffffff, 1px #e0e0e0, 라벨 #141414, rounded 9999, 높이 44 이상) — 누르면 화면 7 첫 상태로 (교사·admin만)
- button-primary: "AI로 읽기" 비활성(누름 없음). 모바일 = 카드 하단 전폭, 데스크톱 = 본문 하단 고정 바 오른쪽. 하늘색 없음 (교사·admin만)
- tab-bar: 모바일 전용 하단 탭바 1개(공통 규격). 데스크톱에는 두지 않는다 (교사·admin만)
- tab-item: 4개 "홈" · "시약" · "QR 스캔" · "기록". 활성 = "시약" (교사·admin만)
### 반영한 레퍼런스
- https://uibowl.io/name/%ED%8E%98%EC%9D%B4%EC%9B%8C%ED%81%AC?patterns=%EC%B4%AC%EC%98%81%ED%95%98%EA%B8%B0&imgId=cmtzo56zo001gib048x2rj3i2
- https://uibowl.io/name/%EB%A6%AC%EB%8B%A4?patterns=%EC%B4%AC%EC%98%81%ED%95%98%EA%B8%B0&imgId=cmliyank30009jp04rcy8en7a
- https://uibowl.io/website/%EC%82%AC%EB%B0%A9%EB%84%B7?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&imgId=cmu4rq9d8000xjm04y191pizg

## 상태 화면 7-doc-review
AI가 서류를 읽은 뒤의 확인 표(프레임 7-doc-review-mobile · 7-doc-review-desktop, 7-doc-review-desktop은 키스크린). 교사·admin 전용. 결과는 사용자가 확인한 뒤에만 입고된다(PRD §5). 모바일 = runs/20261007-0002 그대로.
예시 상태: 서류 날짜 2026-10-07. 품목 3개 + 시약 아님 2개.
① "염산 35% 500mL" · 규격 500 mL · 수량 4 → 우리 학교 시약 "염산" 자동 연결, 환산 "500 mL × 4병 = 2,000 mL"
② "질산칼륨 500g" · 규격 500 g · 수량 1 → 우리 학교에 없음 → "새 시약으로 등록"을 고른 상태라 행이 아래로 펼쳐짐(new-reagent-fields)
③ "아세트산(빙초산) 500mL" · 규격 500 mL · 수량 2 → "새 시약으로 등록" 입력을 마치고 접힌 상태, 2줄에 요약 caption(#707070) "새 시약 · 산 · 1,000 mL", 환산 "500 mL × 2병 = 1,000 mL"
시약 아님 2개(니트릴 장갑 · 비커 250mL)는 표 아래 접힘. 모바일 = 행마다 #f3f3f3 카드 세로 쌓기.
데스크톱 배치: app-sidebar("입고" 현재) | 본문 페이지 = 페이지 머리 "입고" → intake-mode(왼쪽 정렬) → 업로드 뒤 같은 페이지 아래가 본문 폭 전체 doc-intake-table로 바뀐 한 페이지 흐름(s1-adopt #5): 표 머리 줄(왼쪽 heading-3 "읽은 내용 확인" + caption / 오른쪽 "서류 날짜" 칸) → 표(머리행 품명 · 규격 · 수량 · 단위 환산, 행마다 아래 줄 reagent-link, ② 행은 아래로 new-reagent-fields 펼침) → 접힌 "시약 아님 2개 ▾" → 본문 하단 고정 바(button-primary "확인 후 입고" 오른쪽).
### 구성 요소
- app-sidebar: 데스크톱 전용. 공통 규격, 학교명 "샘플고등학교" + 교사 메뉴 + "김OO · 교사" + nav-account-menu (교사·admin만)
- sidebar-item: 데스크톱 전용. 교사 8개 / admin 10개(공통 메뉴). 현재 = "입고" (교사·admin만)
- nav-pill: 모바일 전용. "Lab_Stock" + "입고·시약 등록" + 현재 학교명 "샘플고등학교" + nav-account-menu ▾ (교사·admin만)
- nav-account-menu: 모바일 = 학교명 옆 ▾, 데스크톱 = app-sidebar 맨 아래(닫힌 상태) (교사·admin만)
- intake-mode: "직접 입력 / 서류로 입고", 활성 = "서류로 입고". 데스크톱 = 페이지 머리 아래 왼쪽 (교사·admin만)
- segmented-control-active: intake-mode 활성 옵션 흰 pill. 하늘색: 1px #2b9fe0 테두리(글자 #141414) (교사·admin만)
- doc-intake-table: 확인 표 블록 1개(extraction-table 모양, rounded 16 컨테이너, 1px #f0f0f0 테두리). 위→아래: heading-3 "읽은 내용 확인" + caption(#707070) "고칠 곳이 있으면 고친 뒤 입고하세요" → 라벨 "서류 날짜" + text-input "2026-10-07"(고칠 수 있음, 서류에 날짜가 없으면 오늘; 데스크톱은 머리 줄 오른쪽) → doc-item-row 3개(모바일 행 사이 12, 데스크톱 행 사이 1px #f0f0f0 선) → 접힌 묶음 줄 "시약 아님 2개 ▾"(body-sm #707070, 누르면 펼쳐 품명만 보기) → button-primary "확인 후 입고"(모바일 하단 전폭, 데스크톱 본문 하단 고정 바). 데스크톱 = 본문 폭 전체 표(머리행 caption #707070 "품명 · 규격 · 수량 · 단위 환산"). 하늘색: 사용자가 고친 칸 배경 #e6f4fc (교사·admin만)
- doc-item-row: 서류 품목 1개. 1줄 = 품명(서류 표기 그대로, title #141414) · 규격(body) · 수량(body, 고칠 수 있는 숫자 text-input). 2줄 = reagent-link. 3줄 = 단위 환산 caption(#707070) "500 mL × 4병 = 2,000 mL"(데스크톱은 1줄의 "단위 환산" 열). 모바일 = #f3f3f3 카드(rounded 16, 여백 16), 데스크톱 = ex-data-table-cell 행. 하늘색 없음 (교사·admin만)
- ex-data-table-cell: 데스크톱 doc-intake-table 머리행(caption #707070)과 본문 셀(body-sm), 행 구분 1px #f0f0f0 선 (교사·admin만)
- reagent-link: doc-item-row 2줄. 자동 연결(①) = caption "우리 학교 시약"(#707070) + 선택 상자(text-input 모양, rounded 16, 값 "염산" + ▾ — 모바일은 #f3f3f3 카드 위라 #ffffff 채움, 데스크톱은 흰 표 위라 #f0f0f0 채움) + 조용한 텍스트 동작 "바꾸기" · "빼기"(link #141414, 누름 영역 44 이상). 연결할 시약이 없으면(②·③) 선택 상자 자리에 pill "새 시약으로 등록"(선택됨 상태). "빼기"를 누르면 그 행은 이번 입고에서 빠지고 흐린 글자(#adadad)로 남아 되돌릴 수 있다. 데스크톱 "바꾸기"는 선택 상자 아래 드롭다운(샘플고등학교 시약만). 하늘색: ▾ 아이콘 #2b9fe0, "새 시약으로 등록" 선택 상태 #e6f4fc + 1px #2b9fe0 테두리(글자 #141414) (교사·admin만)
- new-reagent-fields: ② 행이 아래로 펼쳐진 입력 묶음(위 구분 여백 12). 모바일 = 라벨 위·입력 아래 세로, 데스크톱 = 행 안 "라벨 | 입력" 행(사이 1px #f0f0f0 선). 순서: "이름" text-input "질산칼륨" → "보관 분류" storage-class-chip 8종(AI 추천 "산화제" 칩에 suggest-badge, 처음 선택) → "단위" 선택 상자 "g"(병·mL·g) → "재고량" text-input "500" + suffix "g" → "MSDS" 줄 = caption "아직 없어요"(#707070) + msds-search. 하늘색 없음(칩·배지 규칙은 각 항목대로) (교사·admin만)
- storage-class-chip: new-reagent-fields "보관 분류" 칩 8종 "유기·산·염기·산화제·인화성·무기염·독성·기타", 하나 선택. 미선택 = 모바일 #ffffff 채움 + 1px #e0e0e0 테두리(카드 위 구분), 데스크톱 #f3f3f3 채움, rounded 9999, label #141414. 하늘색: 선택 칩 "산화제" #e6f4fc + 1px #2b9fe0 테두리(글자 #141414) (교사·admin만)
- suggest-badge: "산화제" 칩 바로 옆 작은 pill "추천"(#e6f4fc 채움, 1px #2b9fe0 테두리, label #141414, rounded 9999) — AI가 고른 분류 표시. 핑크 금지 (교사·admin만)
- msds-search: new-reagent-fields MSDS 줄 오른쪽 pill "MSDS 찾기"(모바일 #ffffff 채움, 데스크톱 #f3f3f3 채움, 라벨 #141414, rounded 9999, 높이 44 이상). 누르면 상태 화면 7-msds(모바일 시트, 데스크톱 이 버튼에 붙은 팝오버). 하늘색: 검색 아이콘 #2b9fe0 (교사·admin만)
- text-input: "서류 날짜", 수량, reagent-link 선택 상자, new-reagent-fields 이름·단위·재고량(테두리 없음, rounded 16, 포커스 링 2px #141414, 단위 suffix #707070 — 흰 바탕 위 #f0f0f0, #f3f3f3 카드 위 #ffffff). 하늘색: 날짜 달력 아이콘 #2b9fe0 (교사·admin만)
- button-primary: "확인 후 입고"(#141414 채움, #ffffff 글자, rounded 9999, 높이 44 이상). 모바일 = 표 하단 전폭 tab-bar 바로 위, 데스크톱 = 본문 하단 고정 바 오른쪽. 새 시약 행의 이름·보관 분류·단위·재고량이 비면 비활성. 하늘색 없음 (교사·admin만)
- ex-toast: 입고 직후 "3개 품목을 입고했어요" → 새 시약이 있으면 상태 화면 7-suggest, 없으면 화면 2. 모바일 tab-bar 위, 데스크톱 오른쪽 아래. 하늘색: 완료 체크 아이콘 #2b9fe0 (교사·admin만)
- tab-bar: 모바일 전용 하단 탭바 1개(공통 규격). 데스크톱에는 두지 않는다 (교사·admin만)
- tab-item: 4개 "홈" · "시약" · "QR 스캔" · "기록". 활성 = "시약" (교사·admin만)
### 반영한 레퍼런스
- https://uibowl.io/name/%ED%9E%88%EB%A1%9C%EC%9D%B8%EC%8A%A4?patterns=%EC%95%8C%EB%A6%BC&imgId=cmqgadbzq00m3if04dv0zhlhx
- https://uibowl.io/website/%EC%82%AC%EB%B0%A9%EB%84%B7?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&imgId=cmu4rq9d8000xjm04y191pizg

## 상태 화면 7-doc-fail
AI가 서류를 읽지 못했거나 품목이 0개인 상태(프레임 7-doc-fail-mobile · 7-doc-fail-desktop). 교사·admin 전용. 핑크 없음 — 재고 부족이 아니다. 모바일 = runs/20261007-0002 그대로.
예시 상태: 흐린 영수증 사진을 올려 품목을 찾지 못함. 두 갈래 동작 = 다시 올리기 / 직접 입력.
데스크톱 배치: app-sidebar("입고" 현재) | 본문 페이지 = 페이지 머리 "입고" → 가운데 단일 열 폭 640: intake-mode → ex-empty-state-card(실패 안내) → doc-upload(다시 올리기, 끌어다 놓기 안내) → 본문 하단 고정 바(button-primary "AI로 읽기" 오른쪽, 새 파일 전 비활성).
### 구성 요소
- app-sidebar: 데스크톱 전용. 공통 규격, 학교명 "샘플고등학교" + 교사 메뉴 + "김OO · 교사" + nav-account-menu (교사·admin만)
- sidebar-item: 데스크톱 전용. 교사 8개 / admin 10개(공통 메뉴). 현재 = "입고" (교사·admin만)
- nav-pill: 모바일 전용. "Lab_Stock" + "입고·시약 등록" + 현재 학교명 "샘플고등학교" + nav-account-menu ▾ (교사·admin만)
- nav-account-menu: 모바일 = 학교명 옆 ▾, 데스크톱 = app-sidebar 맨 아래(닫힌 상태) (교사·admin만)
- intake-mode: "직접 입력 / 서류로 입고", 활성 = "서류로 입고". 데스크톱 = 640 열 맨 위 (교사·admin만)
- segmented-control-active: intake-mode 활성 옵션 흰 pill. 하늘색: 1px #2b9fe0 테두리(글자 #141414) (교사·admin만)
- ex-empty-state-card: 실패 안내 카드(#ffffff, 1px #f0f0f0 테두리, rounded 24, 여백 24). 올린 서류 미리보기 작은 타일(rounded 16, 비율 유지) → #141414 안내 아이콘 → heading-4 "서류에서 품목을 찾지 못했어요" → body-sm(#707070) "글자가 잘 보이게 다시 찍거나 PDF로 올려 주세요" → button-outline "직접 입력"(누르면 intake-mode가 "직접 입력"으로 바뀜). 데스크톱 = 640 열 안 같은 카드. 하늘색 없음(아이콘 #141414) (교사·admin만)
- doc-upload: 카드 아래 다시 올리기 영역(화면 7 첫 상태와 같은 카드). heading-4 "다른 파일 올리기" + caption(#707070) "PDF·JPG·PNG, 4MB까지" + button-pill-soft "촬영하기" · "파일 선택"(데스크톱은 "파일 선택" + caption "여기에 끌어다 놓아도 돼요") + button-primary "AI로 읽기"(새 파일 전 비활성; 모바일 카드 하단 전폭, 데스크톱 본문 하단 고정 바). 하늘색: 업로드 아이콘 #2b9fe0 (교사·admin만)
- button-pill-soft: doc-upload "촬영하기"(모바일) · "파일 선택"(#f3f3f3, 라벨 #141414, rounded 9999, 높이 44 이상). 하늘색: 왼쪽 아이콘 #2b9fe0 (교사·admin만)
- button-primary: doc-upload "AI로 읽기". 하늘색 없음 (교사·admin만)
- button-outline: ex-empty-state-card "직접 입력"(#ffffff, 1px #e0e0e0, 라벨 #141414, rounded 9999, 높이 44 이상) (교사·admin만)
- tab-bar: 모바일 전용 하단 탭바 1개(공통 규격). 데스크톱에는 두지 않는다 (교사·admin만)
- tab-item: 4개 "홈" · "시약" · "QR 스캔" · "기록". 활성 = "시약" (교사·admin만)
### 반영한 레퍼런스
- https://uibowl.io/name/%EC%95%84%EC%9D%B4%EC%BF%A0%EC%B9%B4?patterns=%EC%B4%AC%EC%98%81%ED%95%98%EA%B8%B0&imgId=cmp0t6j63000fl904x800o216
- https://uibowl.io/website/%EC%82%AC%EB%B0%A9%EB%84%B7?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&imgId=cmu4rq9d8000xjm04y191pizg

## 상태 화면 7-suggest
7-doc-review에서 "확인 후 입고"를 누른 직후 위치 추천 단계(프레임 7-suggest-mobile · 7-suggest-desktop). 직접 입력으로 새 시약을 등록한 뒤에도 같은 단계. 교사·admin 전용. 위치는 나중에 화면 3·11에서 언제든 고칠 수 있다. 모바일 = runs/20261007-0002 그대로.
예시 상태: 새 시약 2개 — 질산칼륨(산화제) → 추천 "2번 시약장 · 우 2단", 아세트산(산) → 맞는 칸 없음. 직전 ex-toast "3개 품목을 입고했어요".
데스크톱 배치: app-sidebar("입고" 현재) | 본문 페이지 = 페이지 머리 "입고" → 가운데 단일 열 폭 640: location-suggest(제목 → 안내 → 새 시약 행 2개, 행 안 동작 버튼은 행 오른쪽) → 본문 하단 고정 바(왼쪽 "나중에", 오른쪽 button-primary "모두 추천대로"). ex-toast는 오른쪽 아래. "다른 칸"은 그 버튼에 붙는 location-picker 팝오버(이 프레임에서는 닫힘).
### 구성 요소
- app-sidebar: 데스크톱 전용. 공통 규격, 학교명 "샘플고등학교" + 교사 메뉴 + "김OO · 교사" + nav-account-menu (교사·admin만)
- sidebar-item: 데스크톱 전용. 교사 8개 / admin 10개(공통 메뉴). 현재 = "입고" (교사·admin만)
- nav-pill: 모바일 전용. "Lab_Stock" + 제목 "입고·시약 등록" + 현재 학교명 "샘플고등학교" + nav-account-menu ▾ (교사·admin만)
- nav-account-menu: 모바일 = 학교명 옆 ▾, 데스크톱 = app-sidebar 맨 아래(닫힌 상태) (교사·admin만)
- ex-toast: "3개 품목을 입고했어요"(#ffffff, 1px #f0f0f0 테두리, rounded 24). 모바일 = 단계 위, 데스크톱 = 오른쪽 아래. 하늘색: 완료 체크 아이콘 #2b9fe0 (교사·admin만)
- location-suggest: 위치 추천 블록 1개. 위→아래: heading-3 "보관 위치 정하기" → caption(#707070) "새 시약 2개의 칸을 추천했어요" → reagent-row 2개(행 사이 12) → button-primary "모두 추천대로" + 조용한 텍스트 동작 "나중에"(link #141414, 누름 영역 44 이상, → 화면 2) — 모바일 = 하단 전폭 버튼(tab-bar 바로 위) + 그 아래 "나중에", 데스크톱 = 본문 하단 고정 바(왼쪽 "나중에", 오른쪽 "모두 추천대로"). ① 질산칼륨 행 = 시약명 title + 분류 caption "산화제"(#707070) → "추천 위치: cabinet-number(2) 2번 시약장 · 우 2단"(body #141414) + suggest-badge → 버튼 둘 button-outline "다른 칸"(→ location-picker; 모바일 시트, 데스크톱 팝오버) · button-primary "여기에 두기". ② 아세트산 행 = 시약명 + 분류 caption "산" → body-sm #707070 "맞는 칸이 없어요 — 시약장 설정에서 칸 분류를 정해 주세요" + button-pill-soft "시약장 설정"(→ 화면 11). 핑크 없음 (교사·admin만)
- reagent-row: location-suggest 안 새 시약 행(#f3f3f3, rounded 16, 여백 16). 데스크톱 = 640 폭 행, 왼쪽 시약명·추천 위치 / 오른쪽 버튼 둘. 하늘색: "여기에 두기" 뒤 완료 행은 오른쪽 #2b9fe0 체크 아이콘 + caption "2번 시약장 · 우 2단에 뒀어요"(#141414) (교사·admin만)
- cabinet-number: 추천 위치 앞 작은 원(#ffffff, 1px #e0e0e0, rounded 9999) 안 숫자 "2"(label #141414). 핑크·하늘색 글자 없음 (교사·admin만)
- suggest-badge: 추천 위치 줄 끝 pill "추천"(#e6f4fc 채움, 1px #2b9fe0 테두리, label #141414, rounded 9999). 핑크 금지 (교사·admin만)
- button-outline: 행마다 "다른 칸"(#ffffff, 1px #e0e0e0, 라벨 #141414, rounded 9999, 높이 44 이상) (교사·admin만)
- button-primary: 행마다 "여기에 두기", "모두 추천대로"(#141414 채움, #ffffff 글자, rounded 9999, 높이 44 이상). 맞는 칸이 없는 행은 "모두 추천대로"에서 빠진다. 하늘색 없음 (교사·admin만)
- button-pill-soft: 맞는 칸 없음 행의 "시약장 설정"(#ffffff 채움(#f3f3f3 행 위 구분), 라벨 #141414, rounded 9999, 높이 44 이상). 하늘색: › 아이콘 #2b9fe0 (교사·admin만)
- tab-bar: 모바일 전용 하단 탭바 1개(공통 규격). 데스크톱에는 두지 않는다 (교사·admin만)
- tab-item: 4개 "홈" · "시약" · "QR 스캔" · "기록". 활성 = "시약" (교사·admin만)
### 반영한 레퍼런스
- https://uibowl.io/name/%ED%9E%88%EB%A1%9C%EC%9D%B8%EC%8A%A4?patterns=%EC%95%8C%EB%A6%BC&imgId=cmqgadbzq00m3if04dv0zhlhx
- https://uibowl.io/website/%EC%9E%94%EB%94%94?patterns=%EA%B8%B0%ED%83%80&imgId=cmpz4uagr000ajs04zj40zdih

## 상태 화면 7-msds
7-doc-review의 질산칼륨 새 시약 행에서 "MSDS 찾기"를 누른 상태(프레임 7-msds-mobile · 7-msds-desktop). 교사·admin 전용. 직접 입력의 새 시약 등록 폼에서 누른 경우도 같다. 모바일 = runs/20261007-0002 그대로.
뒤 화면은 7-doc-review 그대로(딤 없음), 위에 msds-candidates. 예시: 후보 3개 중 첫 후보 선택. 모바일 = tab-bar 위 바텀시트.
데스크톱 배치: app-sidebar("입고" 현재) | 본문 페이지 = 7-doc-review 데스크톱 그대로(본문 폭 doc-intake-table, ② 질산칼륨 행 펼침) + new-reagent-fields "MSDS 찾기"에 붙은 msds-candidates 팝오버(폭 400, 버튼 아래로 열림, 표 위에 겹침, 딤 없음, s1-adopt #3).
### 구성 요소
- app-sidebar: 데스크톱 전용. 공통 규격, 학교명 "샘플고등학교" + 교사 메뉴 + "김OO · 교사" + nav-account-menu (교사·admin만)
- sidebar-item: 데스크톱 전용. 교사 8개 / admin 10개(공통 메뉴). 현재 = "입고" (교사·admin만)
- nav-pill: 모바일 전용. "Lab_Stock" + "입고·시약 등록" + 현재 학교명 "샘플고등학교" + nav-account-menu ▾ (교사·admin만)
- nav-account-menu: 모바일 = 학교명 옆 ▾, 데스크톱 = app-sidebar 맨 아래(닫힌 상태) (교사·admin만)
- doc-intake-table: 뒤 확인 표(누름 동작 없음). 데스크톱 = 본문 폭 전체 표 (교사·admin만)
- new-reagent-fields: 뒤 펼쳐진 질산칼륨 입력 묶음(누름 동작 없음) (교사·admin만)
- msds-search: new-reagent-fields 안 "MSDS 찾기"(눌린 상태). 데스크톱 팝오버는 이 버튼에 붙는다. 하늘색: 검색 아이콘 #2b9fe0 (교사·admin만)
- msds-candidates: 1개(#ffffff, 1px #e0e0e0 테두리, 여백 24, × 닫기) — 모바일 = tab-bar 위 바텀시트(위쪽 rounded 24), 데스크톱 = 팝오버(폭 400, rounded 24). 위→아래: 제목 heading-3 "MSDS 찾기" → caption(#707070) "질산칼륨" → 검색 text-input(값 "질산칼륨") → 후보 행 3개(물질명 title 위 + CAS caption #707070 아래, #f3f3f3, rounded 16, 행 사이 12): "질산칼륨 · CAS 7757-79-1" · "질산칼륨 용액 · CAS 7757-79-1" · "아질산칼륨 · CAS 7758-09-0", 선택 = 첫 행 → 맨 끝 "찾는 게 없어요 — 직접 입력" 행(그 자리에서 "MSDS 주소" text-input 펼침) → 하단 전폭 button-primary "이 MSDS로". 후보 0개 = "찾지 못했어요 — 직접 입력" + text-input. 고르기 전 비활성. 고르면 닫히고 new-reagent-fields MSDS 줄이 "질산칼륨 · CAS 7757-79-1"로 바뀐다. 하늘색: 선택 행 배경 #e6f4fc + 오른쪽 #2b9fe0 체크 아이콘(글자 #141414) (교사·admin만)
- text-input: 안쪽 검색 입력과 "MSDS 주소" 입력(#f0f0f0, rounded 16, 포커스 링 2px #141414). 하늘색: 검색 아이콘 #2b9fe0 (교사·admin만)
- button-primary: 하단 "이 MSDS로"(#141414 채움, #ffffff 글자, rounded 9999, 높이 44 이상). 하늘색 없음 (교사·admin만)
- tab-bar: 모바일 전용 하단 탭바 1개(공통 규격). 시트는 이 바 위에 붙는다. 데스크톱에는 두지 않는다 (교사·admin만)
- tab-item: 4개 "홈" · "시약" · "QR 스캔" · "기록". 활성 = "시약" (교사·admin만)
### 반영한 레퍼런스
- https://uibowl.io/name/%ED%86%A0%EC%8A%A4%EC%A6%9D%EA%B6%8C?patterns=%EC%BB%A4%EB%AE%A4%EB%8B%88%ED%8B%B0&imgId=cmsb4ub9l0009jo042gue22tj
- https://uibowl.io/name/%EC%95%B3%ED%94%8C%EB%A6%AC?patterns=%EA%B2%80%EC%83%89&imgId=cmtpokg65000pi804zwlm86ih
- https://uibowl.io/name/%EB%84%A4%EC%9D%B4%EB%B2%84%EB%B8%94%EB%A1%9C%EA%B7%B8?patterns=%ED%95%84%ED%84%B0&imgId=cmumdx3pp008yjm04zoku825b
- https://uibowl.io/website/%EC%9E%94%EB%94%94?patterns=%EA%B8%B0%ED%83%80&imgId=cmpz4uagr000ajs04zj40zdih

## 상태 화면 11-empty
시약장이 0개인 학교의 화면 11. 교사 기준으로 그린다(프레임 11-empty-mobile · 11-empty-desktop). 학생에게는 같은 카드가 cabinet-add 없이 문구만 보인다. 모바일 = runs/20261004-2256 그대로(+ 공통 nav-account-menu).
시약장이 없으므로 cabinet-switcher · 배치도 · cabinet-edit · mix-warning · "칸 없음" 시약 목록은 그리지 않는다(빈 상태 카드 하나에 집중). 모바일 위→아래: nav-pill → 제목 줄 heading-3 "시약장 0" → 화면 가운데 ex-empty-state-card → tab-bar.
데스크톱 배치: app-sidebar("시약장" 현재) | 본문 페이지 = 페이지 머리(왼쪽 "시약장" + "0개") → 가운데 단일 열 폭 640 가운데에 ex-empty-state-card 1개(카드 안 cabinet-add). 하단 고정 바 없음.
### 구성 요소
- app-sidebar: 데스크톱 전용. 공통 규격, 학교명 "샘플고등학교" + 역할별 메뉴 + 이름·역할 + nav-account-menu
- sidebar-item: 데스크톱 전용. 학생 5개 / 교사 8개 / admin 10개(공통 메뉴). 현재 = "시약장"
- nav-pill: 모바일 전용. "Lab_Stock" 워드마크 + 제목 "시약장 설정" + 현재 학교명 "샘플고등학교" + nav-account-menu ▾. 학교 전환 없음
- nav-account-menu: 모바일 = 학교명 옆 ▾, 데스크톱 = app-sidebar 맨 아래(닫힌 상태). 메뉴 항목 "로그아웃" 1개. 하늘색 없음
- ex-empty-state-card: 배치도 자리 가운데 빈 상태 카드(#ffffff 채움, 1px #f0f0f0 테두리, rounded 24, 안쪽 여백 24, 가운데 정렬). 위에서부터 시약장 아이콘 → heading-4 "아직 시약장이 없어요"(#141414) → 안내 1줄 body-sm(#707070) "'+ 시약장 추가'를 눌러 첫 시약장을 만들어 주세요" → 카드 안 cabinet-add. 학생 화면에서는 cabinet-add를 그리지 않고 안내 1줄을 "교사가 시약장을 추가하면 여기에 보여요"로 바꾼다. 데스크톱 = 640 열 안 같은 카드. 핑크 없음. 하늘색: 시약장 아이콘 #2b9fe0
- cabinet-add: ex-empty-state-card 안 안내 문구 아래 button-pill-soft "+ 시약장 추가"(#f3f3f3 채움, 라벨 #141414, rounded 9999, 높이 44 이상). 누르면 "1번 시약장"을 만들고 화면 11 기본 상태로 바뀐다. 학생 화면에는 그리지 않는다. 하늘색: "+" 아이콘 #2b9fe0(라벨 글자는 #141414) (교사·admin만)
- tab-bar: 모바일 전용 하단 탭바 1개(공통 규격). 데스크톱에는 두지 않는다. 하늘색: 활성 tab-item의 #2b9fe0 아이콘만
- tab-item: tab-bar 안 4개 "홈" · "시약" · "QR 스캔" · "기록", 같은 폭 사각형 누름 영역(rounded 0), 높이 48. 활성 = "시약": #2b9fe0 아이콘 + 라벨 #141414. 비활성 3개: 아이콘·라벨 #707070
### 반영한 레퍼런스
- https://uibowl.io/name/%EB%B3%BC%ED%8A%B8%EC%97%85?patterns=%EA%B0%84%ED%8E%B8%EA%B2%B0%EC%A0%9C&imgId=cmojeenh70003lh04lxsv019h
- https://uibowl.io/name/%EB%8B%AC%EB%8B%A4%EB%B0%A9?patterns=iPhone%20%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7&imgId=cmuc8ychu001ljz04gcquihao
- https://uibowl.io/website/%ED%98%81%EC%8B%A0%EC%9D%98%EC%88%B2?patterns=%ED%95%84%ED%84%B0&imgId=cmiqzsrbu001ol404pjyckvpt

## 상태 화면 11-delete
교사·admin이 "2번 시약장"을 고른 뒤 cabinet-edit의 "삭제"를 누른 상태(프레임 11-delete-mobile · 11-delete-desktop). 학생에게는 이 상태가 없다. 모바일 = runs/20261004-2256 그대로(+ 공통 nav-account-menu).
뒤 화면은 화면 11 그대로이고 cabinet-switcher의 활성 pill = "2번 시약장"(예시: 양문형 · 3단, 배치된 시약 6개). 그 위에 확인 카드. 딤·반투명 덮개 없이 1px #e0e0e0 테두리로만 구분한다. 핑크 금지. 모바일 = 확인 카드가 바텀시트로 tab-bar 위쪽 선 위에 붙는다.
데스크톱 배치: app-sidebar("시약장" 현재) | 본문 페이지 = 화면 11 데스크톱 1차 승인 배치 그대로(페이지 머리 "시약장" + "2개" → 640 열: cabinet-switcher(활성 "2번 시약장") + cabinet-add → 시약장 이름 + 관리 줄 → 문 형태 · 단 수 → 배치도 …) + 프레임 가운데 ex-modal-card 확인 카드(폭 480, 사이드바 위까지 겹치는 가운데 자리, 딤 없음, s1-adopt #4).
### 구성 요소
- app-sidebar: 데스크톱 전용. 공통 규격, 학교명 "샘플고등학교" + 교사 메뉴 + "김OO · 교사" + nav-account-menu (교사·admin만)
- sidebar-item: 데스크톱 전용. 교사 8개 / admin 10개(공통 메뉴). 현재 = "시약장" (교사·admin만)
- nav-pill: 모바일 전용. "Lab_Stock" 워드마크 + 제목 "시약장 설정" + 현재 학교명 "샘플고등학교" + nav-account-menu ▾ (교사·admin만)
- nav-account-menu: 모바일 = 학교명 옆 ▾, 데스크톱 = app-sidebar 맨 아래(닫힌 상태). 메뉴 항목 "로그아웃" 1개 (교사·admin만)
- cabinet-switcher: 화면 11과 같은 전환 pill 줄. "1번 시약장"(비활성, #f3f3f3 채움) · "2번 시약장"(활성, #e6f4fc 채움 + 1px #2b9fe0 테두리, 라벨 #141414). 확인 카드 뒤에서 그대로 보여 어떤 시약장을 지우는지 알 수 있다. 데스크톱 = 640 열 맨 위 한 줄. 하늘색: 활성 pill 채움 #e6f4fc + 테두리 #2b9fe0 (교사·admin만)
- cabinet-number: 전환 pill 이름 앞 숫자 원 "1"·"2"(#ffffff, 1px #e0e0e0, rounded 9999, label #141414). 핑크·하늘색 글자 없음 (교사·admin만)
- cabinet-add: cabinet-switcher 줄 끝 button-pill-soft "+ 시약장 추가". 카드가 열린 동안 누름 동작 없음. 하늘색: "+" 아이콘 #2b9fe0 (교사·admin만)
- cabinet-edit: 확인 카드 뒤에 보이는 2번 시약장 편집 블록(관리 줄 "이름 바꾸기" · "삭제", 문 형태·단 수 선택; 데스크톱은 1차 승인 배치의 "라벨 | 입력" 행). 카드가 열린 동안 누름 동작 없음. 하늘색: 선택 옵션 배경 #e6f4fc + 1px #2b9fe0 테두리 (교사·admin만)
- ex-modal-card: 삭제 확인 카드. #ffffff 채움, 1px #e0e0e0 테두리, 그림자·딤 없음, rounded 24, 안쪽 여백 24, 오른쪽 위 × 닫기(누름 영역 44 이상). 제목 heading-3 "이 시약장을 삭제할까요?"(#141414) → 안내 body-sm(#141414) "배치된 시약 6개는 '칸 없음'으로 바뀌어요" → 보조 1줄 caption(#707070) "시약 정보와 재고는 지워지지 않아요" → 버튼 2개 button-outline "취소"(왼쪽) + button-primary "삭제"(오른쪽). 모바일 = 바텀시트(위쪽 rounded 24, 가로 2버튼 1:1), 데스크톱 = 프레임 가운데 폭 480(버튼은 오른쪽 아래 정렬, 사이 8). 핑크 없음. 하늘색 없음 (교사·admin만)
- button-outline: 확인 카드 "취소". #ffffff 채움, 1px #e0e0e0 테두리, 라벨 #141414, rounded 9999, 높이 44 이상 (교사·admin만)
- button-primary: 확인 카드 "삭제". #141414 채움, #ffffff 글자, rounded 9999, 높이 44 이상. 누르면 2번 시약장이 switcher에서 빠지고 "1번 시약장"이 활성이 되며, 배치됐던 시약은 화면 11 "칸 없음 시약" 목록으로 옮겨진다(rules.json cabinet.on_delete). 하늘색 없음, 핑크 없음 (교사·admin만)
- ex-toast: 삭제 직후 "2번 시약장을 삭제했어요". 모바일 tab-bar 위, 데스크톱 오른쪽 아래. 하늘색: 완료 체크 아이콘 #2b9fe0 (교사·admin만)
- tab-bar: 모바일 전용 하단 탭바 1개(공통 규격). 확인 카드는 이 바 위쪽 선 위에 붙고 바를 가리지 않는다. 데스크톱에는 두지 않는다. 하늘색: 활성 tab-item의 #2b9fe0 아이콘만 (교사·admin만)
- tab-item: tab-bar 안 4개 "홈" · "시약" · "QR 스캔" · "기록". 활성 = "시약". 비활성 3개 #707070 (교사·admin만)
### 반영한 레퍼런스
- https://uibowl.io/name/%ED%8D%BC%EA%B7%B8%EC%83%B5?patterns=%EA%B3%84%EC%A2%8C&imgId=cmq7evao00095l204e0ekhshk
- https://uibowl.io/name/%EC%BB%A4%EB%A6%AC%EC%96%B4%ED%86%A1?patterns=%EB%B6%81%EB%A7%88%ED%81%AC%C2%B7%EC%9C%84%EC%8B%9C%EB%A6%AC%EC%8A%A4%ED%8A%B8&imgId=cmf0p85wt000hl704ad3u3tqc
- https://uibowl.io/website/%EB%AF%B8%EB%A6%AC%EC%BA%94%EB%B2%84%EC%8A%A4?patterns=%EC%B7%A8%EC%86%8C%ED%95%98%EA%B8%B0&imgId=cmdzoh62g0025lb07uuyajbap

## 상태 화면 11-slot
교사가 화면 11에서 칸 "좌 2단"(분류 유기)을 누르고 "시약 넣기"로 "칸 없음" 시약 중 염산(분류 산)을 고른 상태(프레임 11-slot-mobile · 11-slot-desktop, 11-slot-desktop은 키스크린). 학생은 같은 칸 시트를 목록만(빼기·넣기 없이) 본다 — 이 프레임은 교사 기준. 모바일 = runs/20261006-1223 그대로.
뒤 화면은 화면 11(1번 시약장) 그대로, 위에 slot-sheet. 염산(산)은 유기 칸 분류에 없으므로 약한 문구 mix-warning, 저장 허용. 모바일 = 바텀시트(tab-bar 위쪽 선 위).
데스크톱 배치: app-sidebar("시약장" 현재) | 본문 페이지 = 화면 11 데스크톱 1차 승인 배치 그대로(페이지 머리 "시약장" + "2개" → 640 열: cabinet-switcher → 이름 + 관리 줄 → 문 형태 · 단 수 → 배치도(좌 2단 선택) + 범례 …) + 누른 칸 "좌 2단" 오른쪽에 붙어 열리는 slot-sheet 팝오버(폭 400, 배치도 위에 겹침, 딤 없음, 안쪽 스크롤 + 아래 slot-assign 줄 고정, s1-adopt #3).
### 구성 요소
- app-sidebar: 데스크톱 전용. 공통 규격, 학교명 "샘플고등학교" + 교사 메뉴 + "김OO · 교사" + nav-account-menu (교사·admin만)
- sidebar-item: 데스크톱 전용. 교사 8개 / admin 10개(공통 메뉴). 현재 = "시약장" (교사·admin만)
- nav-pill: 모바일 전용. "Lab_Stock" + "시약장 설정" + 현재 학교명 "샘플고등학교" + nav-account-menu ▾ (교사·admin만)
- nav-account-menu: 모바일 = 학교명 옆 ▾, 데스크톱 = app-sidebar 맨 아래(닫힌 상태) (교사·admin만)
- cabinet-switcher: 뒤 전환 pill 줄 "(1) 1번 시약장"(활성) · "(2) 2번 시약장". 팝오버·시트가 열린 동안 누름 동작 없음. 하늘색: 활성 pill 채움·테두리 (교사·admin만)
- cabinet-number: 전환 pill 이름 앞 숫자 원 "1"·"2"(#ffffff, 1px #e0e0e0, label #141414) (교사·admin만)
- cabinet-slot: 뒤 배치도(8칸). 누른 칸 "좌 2단"이 선택 상태 — 데스크톱 팝오버는 이 칸에 붙는다. 하늘색: 선택 칸 #e6f4fc + 2px #2b9fe0 테두리 (교사·admin만)
- slot-count: 배치도 칸 안 시약 수 pill(좌 2단 "3" 등, #ffffff, rounded 9999, label #141414, 무채색) (교사·admin만)
- slot-sheet: 1개(#ffffff, 1px #e0e0e0 테두리, 여백 24, 오른쪽 위 × 닫기) — 모바일 = 바텀시트(위쪽 rounded 24), 데스크톱 = 칸에 붙은 팝오버(폭 400, rounded 24). 위→아래: 제목 heading-3 "좌 2단" + 그 칸 storage-class-chip "유기"(보기 전용) → 소제목 heading-4 "이 칸의 시약 (3)" + reagent-row 3개(에탄올 · 아세톤 · 메탄올), 행마다 오른쪽 조용한 텍스트 동작 "빼기"(link #141414, 누름 영역 44 이상) → 구분 여백 → 소제목 heading-4 "넣을 시약 고르기" + 검색 text-input + "칸 없음" reagent-row 2개(염산 · 질산은), 선택 = 염산 → mix-warning → 하단 전폭 slot-assign (교사·admin만)
- storage-class-chip: slot-sheet 제목 옆 칸 분류 칩 "유기"(보기 전용, #f3f3f3 채움, rounded 9999, label #141414). 뒤 화면 범례에도 같은 칩 (교사·admin만)
- reagent-row: 칸 안 시약 행(시약명 title + 재고량 body + 분류 caption #707070, #f3f3f3 채움, rounded 16)과 피커의 "칸 없음" 시약 행(caption "칸 없음" #707070). 하늘색: 피커에서 선택한 행(염산) #e6f4fc 배경 + 오른쪽 #2b9fe0 체크 아이콘(글자 #141414) (교사·admin만)
- text-input: 피커 검색 바 "시약명 검색"(#f0f0f0, rounded 16). 하늘색: 검색 아이콘 #2b9fe0 (교사·admin만)
- mix-warning: 피커 목록 아래 경고 블록(#fbe9f0 바탕, rounded 16, #d6246a 경고 아이콘 + #141414 body-sm) "이 칸은 유기 칸이에요 — 그래도 넣을 수 있어요". 금지 조합이면 "{A}와 {B}는 섞으면 위험해요". 막지 않는다. 하늘색 없음 (교사·admin만)
- slot-assign: slot-sheet 하단 전폭 button-primary "시약 넣기"(#141414 채움, #ffffff 글자, rounded 9999, 높이 44 이상). 피커가 닫혀 있으면 누를 때 피커를 열고, 시약을 고른 상태에서는 그 시약을 이 칸에 넣는다. mix-warning이 있어도 활성. 하늘색 없음 (교사·admin만)
- ex-toast: 넣기·빼기 직후 "염산을 좌 2단에 넣었어요" / "에탄올을 뺐어요(칸 없음)". 모바일 tab-bar 위, 데스크톱 오른쪽 아래. 하늘색: 완료 체크 아이콘 #2b9fe0 (교사·admin만)
- tab-bar: 모바일 전용 하단 탭바 1개(공통 규격). 시트는 이 바 위에 붙는다. 데스크톱에는 두지 않는다 (교사·admin만)
- tab-item: 4개 "홈" · "시약" · "QR 스캔" · "기록". 활성 = "시약" (교사·admin만)
### 반영한 레퍼런스
- https://uibowl.io/name/%EC%9B%8C%ED%81%AC%EC%98%A8?patterns=%ED%8A%9C%ED%86%A0%EB%A6%AC%EC%96%BC&imgId=cmudxbzpd0028l7046bsxhka0
- https://uibowl.io/name/%EC%85%80%EB%A0%88%ED%8A%B8%EB%A6%BD?patterns=%EB%A1%9C%EA%B7%B8%EC%9D%B8%C2%B7%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85&imgId=cmqp02zja000sjr04ea8bxiax
- https://uibowl.io/website/%EC%9E%94%EB%94%94?patterns=%EA%B8%B0%ED%83%80&imgId=cmpz4uagr000ajs04zj40zdih

## 상태 화면 11-print
교사·admin이 화면 11 관리 줄의 "QR 인쇄"를 누른 상태(프레임 11-print-mobile · 11-print-desktop). 학생에게는 이 상태가 없다. 모바일 = runs/20261006-1223 그대로.
예시 상태: 시약장 선택 = "모두"(기본값은 지금 시약장 "1번 시약장", 사용자가 "모두"로 바꿈) → A4 미리보기에 라벨 2개. 모바일 = 바텀시트(위 A4 미리보기 + 아래 고정 영역), 시약장 고르기는 pill 줄.
데스크톱 배치: app-sidebar("시약장" 현재) | 본문 페이지 720 = 화면 11 데스크톱 1차 승인 배치(640 열) 그대로 | 오른쪽 detail-drawer 480 = qr-print-sheet(제목 → 시약장 고르기 드롭다운 → A4 미리보기 → 아래 고정 "인쇄"). 시약장 고르기는 모바일 pill 줄 대신 드롭다운(rules.json desktop_shell.overlay — 모바일 고르기 → 데스크톱 드롭다운).
### 구성 요소
- app-sidebar: 데스크톱 전용. 공통 규격, 학교명 "샘플고등학교" + 교사 메뉴 + "김OO · 교사" + nav-account-menu (교사·admin만)
- sidebar-item: 데스크톱 전용. 교사 8개 / admin 10개(공통 메뉴). 현재 = "시약장" (교사·admin만)
- nav-pill: 모바일 전용. "Lab_Stock" + "시약장 설정" + 현재 학교명 "샘플고등학교" + nav-account-menu ▾ (교사·admin만)
- nav-account-menu: 모바일 = 학교명 옆 ▾, 데스크톱 = app-sidebar 맨 아래(닫힌 상태) (교사·admin만)
- cabinet-switcher: 뒤 전환 pill 줄(누름 동작 없음). 하늘색: 활성 pill 채움·테두리 (교사·admin만)
- detail-drawer: 데스크톱 전용. 오른쪽 폭 480, 높이 900, #ffffff, 왼쪽 1px #f0f0f0 선, 여백 24, × 닫기, 본문 페이지를 밀어낸다(딤 없음). 안에 qr-print-sheet 내용, 아래 고정 줄(위 1px #f0f0f0 선)에 "인쇄" (교사·admin만)
- qr-print-sheet: 인쇄 시트 1개(#ffffff, 1px #e0e0e0 테두리, 여백 24, 오른쪽 위 × 닫기) — 모바일 = 바텀시트(위쪽 rounded 24), 데스크톱 = detail-drawer 안(드로어 자체가 테두리). 위→아래: 제목 heading-3 "QR 인쇄" → 시약장 고르기(모바일 = pill 줄 "(1) 1번 시약장" · "(2) 2번 시약장" · "모두", storage-class-chip 모양, 예시 "모두" 선택 / 데스크톱 = 라벨 "시약장" + text-input 모양 선택 상자 값 "모두" ▾, 열면 아래 드롭다운 목록 "(1) 1번 시약장" · "(2) 2번 시약장" · "모두") → A4 미리보기 타일(#ffffff, 1px #f0f0f0 테두리, rounded 24, A4 비율, 데스크톱 드로어 폭에 맞춤) 안에 qr-label 2개를 격자로 → caption(#707070) "A4 한 장에 라벨 2개" → 하단 고정 전폭 button-primary "인쇄". 하늘색: 모바일 선택 pill #e6f4fc + 1px #2b9fe0 테두리(글자 #141414), 데스크톱 ▾ 아이콘 #2b9fe0 — 미리보기 타일 안에는 하늘색 없음 (교사·admin만)
- text-input: 데스크톱 시약장 고르기 선택 상자(#f0f0f0, rounded 16, 값 "모두" + ▾). 하늘색: ▾ 아이콘 #2b9fe0 (교사·admin만)
- qr-label: 인쇄 라벨 1개(미리보기 안 2개: 1번·2번 시약장). QR 이미지 1:1(rounded 0, 흑백) → 학교명 caption "샘플고등학교"(#141414) → cabinet-number + 시약장 이름 title "1번 시약장" → caption(#707070) "QR을 찍으면 이 시약장의 시약을 봐요". 라벨 테두리 1px #e0e0e0, rounded 16. 흑백만, 핑크·하늘색 없음 (교사·admin만)
- cabinet-number: qr-label 안 시약장 이름 앞 숫자 원 "1"·"2"(#ffffff, 1px #e0e0e0, label #141414)와 시약장 고르기 항목 안 숫자 원 (교사·admin만)
- button-primary: qr-print-sheet 하단 "인쇄"(#141414 채움, #ffffff 글자, rounded 9999, 높이 44 이상). 모바일 = 시트 하단 고정, 데스크톱 = 드로어 아래 고정 줄 전폭. 하늘색 없음 (교사·admin만)
- tab-bar: 모바일 전용 하단 탭바 1개(공통 규격). 데스크톱에는 두지 않는다 (교사·admin만)
- tab-item: 4개 "홈" · "시약" · "QR 스캔" · "기록". 활성 = "시약" (교사·admin만)
### 반영한 레퍼런스
- https://uibowl.io/name/%ED%8E%98%EC%9D%B4%EC%9B%8C%ED%81%AC?patterns=%ED%8A%9C%ED%86%A0%EB%A6%AC%EC%96%BC&imgId=cmtzo5k4p004jl704vz543akg
- https://uibowl.io/website/%EB%A7%A4%EB%8B%88%ED%8C%A8%EC%8A%A4%ED%8A%B8?patterns=%ED%81%90%EB%A0%88%EC%9D%B4%EC%85%98&imgId=cmulyw7j9001qjj04bmlsz9l1

## 상태 화면 11-unsaved
교사·admin이 cabinet-edit에서 분류 칩을 바꾸고 저장하지 않은 채 cabinet-switcher의 "2번 시약장"(또는 tab-item · sidebar-item 등 이탈)을 누른 상태(프레임 11-unsaved-mobile · 11-unsaved-desktop). 학생에게는 편집이 없어 이 상태가 없다. 모바일 = runs/20261006-1223 그대로.
뒤 화면은 화면 11(1번 시약장, 편집 중) 그대로. 딤 없음, 핑크 없음. 모바일 = 확인 카드가 tab-bar 위 바텀시트.
데스크톱 배치: app-sidebar("시약장" 현재) | 본문 페이지 = 화면 11 데스크톱 1차 승인 배치 그대로(편집 중, 하단 고정 바 "저장" 보임) + 프레임 가운데 ex-modal-card 확인 카드(폭 480, 사이드바 위까지 겹치는 가운데 자리, 딤 없음, s1-adopt #4).
### 구성 요소
- app-sidebar: 데스크톱 전용. 공통 규격, 학교명 "샘플고등학교" + 교사 메뉴 + "김OO · 교사" + nav-account-menu (교사·admin만)
- sidebar-item: 데스크톱 전용. 교사 8개 / admin 10개(공통 메뉴). 현재 = "시약장"(아직 이동 전) (교사·admin만)
- nav-pill: 모바일 전용. "Lab_Stock" + "시약장 설정" + 현재 학교명 "샘플고등학교" + nav-account-menu ▾ (교사·admin만)
- nav-account-menu: 모바일 = 학교명 옆 ▾, 데스크톱 = app-sidebar 맨 아래(닫힌 상태) (교사·admin만)
- cabinet-switcher: 카드 뒤 전환 pill 줄, 활성은 아직 "(1) 1번 시약장". 하늘색: 활성 pill 채움·테두리 (교사·admin만)
- cabinet-edit: 카드 뒤 편집 중 블록(누름 동작 없음). 데스크톱 = 640 열 "라벨 | 입력" 행 + 본문 하단 고정 바 "저장" (교사·admin만)
- ex-modal-card: 확인 카드(#ffffff, 1px #e0e0e0 테두리, 그림자·딤 없음, rounded 24, 여백 24, 오른쪽 위 × 닫기 = "계속 편집"과 같은 동작). 제목 heading-3 "저장하지 않은 변경이 있어요"(#141414) → body-sm(#707070) "이동하면 1번 시약장에서 바꾼 내용이 사라져요" → 버튼 2개 button-outline "버리고 이동"(왼쪽) + button-primary "계속 편집"(오른쪽). 모바일 = 바텀시트(가로 2버튼), 데스크톱 = 프레임 가운데 폭 480(버튼 오른쪽 아래 정렬, 사이 8). 핑크·하늘색 없음 (교사·admin만)
- button-outline: 카드 "버리고 이동" — 편집을 버리고 누른 곳(2번 시약장 또는 누른 메뉴)으로 이동 (교사·admin만)
- button-primary: 카드 "계속 편집" — 카드를 닫고 편집 화면에 머문다. 하늘색 없음 (교사·admin만)
- tab-bar: 모바일 전용 하단 탭바 1개(공통 규격). 데스크톱에는 두지 않는다 (교사·admin만)
- tab-item: 4개 "홈" · "시약" · "QR 스캔" · "기록". 활성 = "시약" (교사·admin만)
### 반영한 레퍼런스
- https://uibowl.io/name/%EC%85%94%ED%81%B4?patterns=%EC%B7%A8%EC%86%8C%ED%95%98%EA%B8%B0&imgId=cmrt4shpb0007l104b7hb2rnd
- https://uibowl.io/name/%EC%97%90%EC%9D%B4%EB%8B%B7?patterns=%EB%A1%9C%EA%B7%B8%EC%9D%B8%C2%B7%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85&imgId=cmtwlutwc000vju04jr6t829j
- https://uibowl.io/website/%EB%AF%B8%EB%A6%AC%EC%BA%94%EB%B2%84%EC%8A%A4?patterns=%EC%B7%A8%EC%86%8C%ED%95%98%EA%B8%B0&imgId=cmdzoh62g0025lb07uuyajbap

## 상태 화면 12-result
스캔 성공 또는 번호 "1" 찾기 직후(프레임 12-result-mobile · 12-result-desktop). 모든 역할 같다(역할별 차이 없음). 모바일 = runs/20261006-1223 그대로.
예시 상태: 1번 시약장 · 양문형 · 4단, 시약 4개 — 염산 1병(좌 1단, 재고 부족), 수산화나트륨 500g(좌 1단), 에탄올 200mL(좌 2단), 과산화수소 2병(우 1단, 재고 부족). 모바일 = 화면 12 카메라 화면 위에 qr-result-sheet가 반쯤 올라온 바텀시트.
데스크톱 배치: app-sidebar("QR 찾기" 현재) | 본문 720 = 화면 12 데스크톱 1차 승인 배치(페이지 머리 "QR 찾기" + 안내 → 2열 카드: 왼쪽 qr-scan 웹캠, 오른쪽 qr-manual-entry 값 "1") — 드로어에 밀려 두 카드는 각 폭 316, 사이 24 | detail-drawer 480 = qr-result-sheet 내용(시약장 요약 + 시약 표 + "배치도 보기").
### 구성 요소
- app-sidebar: 데스크톱 전용. 공통 규격, 학교명 "샘플고등학교" + 역할별 메뉴 + 이름·역할 + nav-account-menu
- sidebar-item: 데스크톱 전용. 학생 5개 / 교사 8개 / admin 10개(공통 메뉴). 현재 = "QR 찾기"
- nav-pill: 모바일 전용. 닫기 + "QR 스캔" + 현재 학교명 "샘플고등학교" + nav-account-menu ▾. 하늘색: 닫기 아이콘 #2b9fe0
- nav-account-menu: 모바일 = 학교명 옆 ▾, 데스크톱 = app-sidebar 맨 아래(닫힌 상태)
- qr-scan: 뒤 카메라 미리보기 영역(#262626, rounded 24, 누름 동작 없음). 데스크톱 = 본문 왼쪽 카드(#ffffff, 1px #f0f0f0, rounded 24, 여백 24) 안 웹캠 미리보기
- qr-manual-entry: 데스크톱 전용 오른쪽 카드(#ffffff, 1px #f0f0f0, rounded 24, 여백 24): heading-4 "시약장 번호로 찾기" + 숫자 text-input(값 "1") + button-primary "찾기". 모바일은 시트 뒤 하단 고정 "시약장 번호로 찾기"(누름 동작 없음). 하늘색: 입력 왼쪽 아이콘 #2b9fe0
- text-input: 데스크톱 qr-manual-entry "시약장 번호" 숫자 입력(#f0f0f0, rounded 16, 값 "1")
- button-primary: 데스크톱 qr-manual-entry "찾기"(#141414 채움, #ffffff 글자, rounded 9999, 높이 44 이상). 하늘색 없음
- detail-drawer: 데스크톱 전용. 오른쪽 폭 480, 높이 900, #ffffff, 왼쪽 1px #f0f0f0 선, 여백 24, 딤 없음. 안에 qr-result-sheet 내용, 아래 고정 줄(위 1px #f0f0f0 선)에 "배치도 보기"
- qr-result-sheet: 결과 1개 — 모바일 = 바텀시트(#ffffff, 1px #e0e0e0 테두리, 그림자·딤 없음, 위쪽 rounded 24, 여백 24), 데스크톱 = detail-drawer 안. 위→아래: 제목 줄 cabinet-number "1" + heading-3 "1번 시약장" + 오른쪽 위 × 닫기 → caption(#707070) "양문형 · 4단 · 시약 4개" → 시약 4개(모바일 = reagent-row, 행마다 칸 위치 / 데스크톱 = 표: 시약명 · 칸 위치 · 재고 · 상태 열, ex-data-table-cell) → 하단 전폭 button-pill-soft "배치도 보기"(→ 화면 11, 그 시약장 활성). 행을 누르면 화면 3 시약 상세(데스크톱은 드로어가 시약 상세로 바뀜). 하늘색: × 아이콘 #2b9fe0
- cabinet-number: 결과 제목 앞 숫자 원 "1"(#ffffff 채움, 1px #e0e0e0 테두리, rounded 9999, label #141414). 핑크·하늘색 글자 없음
- reagent-row: 모바일 전용. 시트 안 시약 행 = 시약명(title) + 재고량·단위(body) + 칸 위치 caption "좌 1단"(#141414) / 칸 없음이면 "칸 없음"(#707070). #f3f3f3 채움, rounded 16, 행 사이 12. 하늘색: 누른 행 배경 #e6f4fc
- ex-data-table-cell: 데스크톱 전용. 드로어 안 시약 표 머리행(caption #707070 "시약명 · 칸 위치 · 재고 · 상태")·셀(body-sm), rounded 16 컨테이너, 1px #f0f0f0 테두리, 행 hover #f3f3f3
- badge-low-stock: 재고 부족 행(염산·과산화수소) "재고 부족"(#d6246a 채움, #ffffff label). 모바일 = 시약명 옆, 데스크톱 = 상태 열. 하늘색 없음
- button-pill-soft: 하단 "배치도 보기"(#f3f3f3 채움, 라벨 #141414, rounded 9999, 높이 44 이상). 모바일 = 시트 하단 전폭, 데스크톱 = 드로어 아래 고정 줄 전폭. 하늘색: 오른쪽 › 아이콘 #2b9fe0
- tab-bar: 모바일 전용 하단 탭바 1개(공통 규격). 시트는 이 바 위에 붙는다. 데스크톱에는 두지 않는다
- tab-item: 4개 "홈" · "시약" · "QR 스캔" · "기록". 활성 = "QR 스캔"
### 반영한 레퍼런스
- https://uibowl.io/name/RailOne?patterns=%EA%B3%A0%EA%B0%9D%EC%84%BC%ED%84%B0%C2%B7FAQ&imgId=cmukplzwq001ale04e7612l65
- https://uibowl.io/name/%EC%B1%84%EB%B9%84?patterns=%EC%83%81%EC%84%B8%EC%A0%95%EB%B3%B4%20%28PDP%29&patternName=%EC%B6%A9%EC%A0%84%EC%86%8C
- https://uibowl.io/website/%EC%82%AC%EB%B0%A9%EB%84%B7?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&imgId=cmu4rq9d8000xjm04y191pizg

## 상태 화면 16-loading
MSDS 요약을 서버에서 불러오는 중(프레임 16-loading-mobile · 16-loading-desktop, 16-loading-mobile은 키스크린). 모든 역할 같다. 모바일·데스크톱 모두 새로(docs/design.md "MSDS summary" Loading, rules.json msds_summary.states).
예시 상태: 질산은(화면 16과 같은 시약). 머리(제목·출처 줄)와 원문 보기 버튼은 그대로 두고, 요약 본문 자리만 실제 항목 순서(신호어 → 그림문자 → 항목 2·4·7·8)와 같은 모양의 회색 막대로 채운다(s1-adopt #1). 글자·그림문자·빨강 없음.
모바일 활성 탭: "시약". 위→아래: nav-pill(‹ + "MSDS · 질산은" + 학교명) → 출처 줄 → msds-summary(안에 msds-skeleton) → msds-original-link(맨 아래 전폭) → tab-bar. 좌우 여백 16, 블록 사이 24.
데스크톱 배치: app-sidebar("시약" 현재) | 본문 720 = 화면 2 시약 표("질산은" 행 #e6f4fc 선택) | detail-drawer 480 = 화면 16 데스크톱과 같은 머리("‹ 시약 상세" + × → "MSDS · 질산은" → 출처 줄) → 드로어 몸통 msds-summary 자리에 msds-skeleton → 아래 고정 줄 msds-original-link. 항목 바로가기 줄은 불러오기 전이라 그리지 않는다.
### 구성 요소
- app-sidebar: 데스크톱 전용. 공통 규격, 학교명 "샘플고등학교" + 역할별 메뉴 + 이름·역할 + nav-account-menu
- sidebar-item: 데스크톱 전용. 학생 5개 / 교사 8개 / admin 10개(공통 메뉴). 현재 = "시약"
- nav-pill: 모바일 전용 헤더. 뒤로가기 ‹(이전 화면 — 화면 3 또는 10) + heading-3 "MSDS · 질산은" + 현재 학교명 "샘플고등학교"(caption) + nav-account-menu ▾. 그 아래 출처 줄 caption(#707070) "물질안전보건자료 · 한국산업안전보건공단". 하늘색: 뒤로가기 아이콘 #2b9fe0
- nav-account-menu: 모바일 = 학교명 옆 ▾, 데스크톱 = app-sidebar 맨 아래(닫힌 상태). "로그아웃" 1개. 하늘색 없음
- data-table: 데스크톱 전용. 드로어 왼쪽 화면 2 시약 표(본문 720 폭), 선택 행 "질산은" #e6f4fc
- detail-drawer: 데스크톱 전용. 폭 480, 높이 900, #ffffff, 왼쪽 1px #f0f0f0 선, 여백 24, 딤 없음. 위→아래: 조용한 텍스트 동작 "‹ 시약 상세"(link #141414) + 오른쪽 위 × 닫기 → heading-3 "MSDS · 질산은" → 출처 줄 caption(#707070) "물질안전보건자료 · 한국산업안전보건공단" → msds-summary(msds-skeleton) → 아래 고정 줄(위 1px #f0f0f0 선) msds-original-link. 하늘색: × 아이콘 #2b9fe0
- msds-summary: 요약 본문 자리(화면 16과 같은 위치·폭). 불러오는 동안 안에 msds-skeleton만 있고, 다 불러오면 같은 자리에 신호어 → 그림문자 → 항목 카드로 바뀐다. 실패하면 상태 16-fail
- msds-skeleton: 회색 자리 표시(#f3f3f3 채움만, 글자 없음, 움직임 표시는 개발 쪽). 실제 배치와 같은 자리·같은 순서: ① 신호어 자리 짧은 막대 1개(폭 56, 높이 24, rounded 9999) → ② 그림문자 자리 마름모 3개 가로(사이 16, 각 = 한 변 56 정사각형 45° 회전, rounded 0, #f3f3f3 채움·테두리 없음 — 빨강 없음) + 마름모마다 아래 이름 자리 짧은 막대(폭 48, 높이 12, rounded 9999) → ③ 항목 카드 4장(#ffffff, 1px #f0f0f0 테두리, rounded 24, 여백 24, 사이 12) 안마다 제목 막대 1개(폭 60%, 높이 16, rounded 9999) + 본문 막대 3개(높이 12, rounded 9999, 사이 8, 마지막 막대는 폭 70%). 모바일은 카드 넷째 장이 화면 아래로 이어져 스크롤, 데스크톱은 드로어 안 스크롤. 핑크·하늘색·빨강 없음
- msds-original-link: 전폭 button-outline "원문 MSDS 보기 ↗"(#ffffff, 1px #e0e0e0, 라벨 #141414, rounded 9999, 높이 44 이상) — 원문 주소는 이미 있어 불러오는 중에도 누를 수 있다(새 창). 모바일 = 스켈레톤 카드 아래(스크롤 끝, tab-bar 위 간격 16), 데스크톱 = detail-drawer 아래 고정 줄. 하늘색: ↗ 아이콘 #2b9fe0
- button-outline: msds-original-link 버튼 모양(위 정의)
- tab-bar: 모바일 전용 하단 탭바 1개(공통 규격). 데스크톱에는 두지 않는다. 하늘색: 활성 tab-item 아이콘 #2b9fe0만
- tab-item: "홈" · "시약" · "QR 스캔" · "기록" 4개. 활성 = "시약", 비활성 3개 #707070
### 반영한 레퍼런스
- https://uibowl.io/website/%EB%A7%A4%EB%8B%88%ED%8C%A8%EC%8A%A4%ED%8A%B8?patterns=%ED%81%90%EB%A0%88%EC%9D%B4%EC%85%98&imgId=cmulyw7j9001qjj04bmlsz9l1
- https://uibowl.io/name/%EB%A9%94%EB%94%94%EC%BD%94%EC%B9%98?patterns=%EC%83%81%EC%84%B8%EC%A0%95%EB%B3%B4%20%28PDP%29&imgId=cms8ebafr002el204u8vddkky

## 상태 화면 16-fail
MSDS 요약을 불러오지 못한 상태(프레임 16-fail-mobile · 16-fail-desktop). 모든 역할 같다. 핑크 없음 — 결정이 필요한 신호가 아니다. 모바일·데스크톱 모두 새로(docs/design.md "MSDS summary" Failure).
예시 상태: 질산은. 머리(제목·출처 줄)는 그대로, msds-summary 자리를 ex-empty-state-card가 대신하고 그 아래 원문 보기 버튼(s1-adopt #1).
모바일 활성 탭: "시약". 위→아래: nav-pill(‹ + "MSDS · 질산은" + 학교명) → 출처 줄 → ex-empty-state-card → msds-original-link(카드 바로 아래 전폭, 간격 16) → tab-bar. 좌우 여백 16.
데스크톱 배치: app-sidebar("시약" 현재) | 본문 720 = 화면 2 시약 표("질산은" 행 #e6f4fc 선택) | detail-drawer 480 = 머리("‹ 시약 상세" + × → "MSDS · 질산은" → 출처 줄) → 드로어 몸통 위쪽에 ex-empty-state-card → 아래 고정 줄 msds-original-link.
### 구성 요소
- app-sidebar: 데스크톱 전용. 공통 규격, 학교명 "샘플고등학교" + 역할별 메뉴 + 이름·역할 + nav-account-menu
- sidebar-item: 데스크톱 전용. 학생 5개 / 교사 8개 / admin 10개(공통 메뉴). 현재 = "시약"
- nav-pill: 모바일 전용 헤더. 뒤로가기 ‹ + heading-3 "MSDS · 질산은" + 현재 학교명 "샘플고등학교"(caption) + nav-account-menu ▾. 그 아래 출처 줄 caption(#707070) "물질안전보건자료 · 한국산업안전보건공단". 하늘색: 뒤로가기 아이콘 #2b9fe0
- nav-account-menu: 모바일 = 학교명 옆 ▾, 데스크톱 = app-sidebar 맨 아래(닫힌 상태). "로그아웃" 1개. 하늘색 없음
- data-table: 데스크톱 전용. 드로어 왼쪽 화면 2 시약 표, 선택 행 "질산은" #e6f4fc
- detail-drawer: 데스크톱 전용. 폭 480, 높이 900, #ffffff, 왼쪽 1px #f0f0f0 선, 여백 24, 딤 없음. 위→아래: "‹ 시약 상세"(link #141414) + × 닫기 → heading-3 "MSDS · 질산은" → 출처 줄 caption(#707070) → ex-empty-state-card → 아래 고정 줄(위 1px #f0f0f0 선) msds-original-link. 하늘색: × 아이콘 #2b9fe0
- ex-empty-state-card: 실패 안내 카드(#ffffff, 1px #f0f0f0 테두리, rounded 24, 여백 24, 가운데 정렬). #141414 안내 아이콘 → heading-4 "요약을 불러오지 못했어요"(#141414) → body-sm(#707070) "원문에서 확인해 주세요". 모바일 = 출처 줄 아래 본문 폭, 데스크톱 = 드로어 몸통 위쪽. 다시 시도 버튼 없음(다시 열면 다시 불러온다). 핑크 없음, 하늘색 없음(아이콘 #141414)
- msds-original-link: 전폭 button-outline "원문 MSDS 보기 ↗"(#ffffff, 1px #e0e0e0, 라벨 #141414, rounded 9999, 높이 44 이상) — 공단 MSDS 페이지를 새 창으로 연다. 모바일 = 카드 바로 아래(간격 16), 데스크톱 = detail-drawer 아래 고정 줄. 하늘색: ↗ 아이콘 #2b9fe0
- button-outline: msds-original-link 버튼 모양(위 정의)
- tab-bar: 모바일 전용 하단 탭바 1개(공통 규격). 데스크톱에는 두지 않는다. 하늘색: 활성 tab-item 아이콘 #2b9fe0만
- tab-item: "홈" · "시약" · "QR 스캔" · "기록" 4개. 활성 = "시약", 비활성 3개 #707070
### 반영한 레퍼런스
- https://uibowl.io/website/%EB%A7%A4%EB%8B%88%ED%8C%A8%EC%8A%A4%ED%8A%B8?patterns=%ED%81%90%EB%A0%88%EC%9D%B4%EC%85%98&imgId=cmulyw7j9001qjj04bmlsz9l1
- https://uibowl.io/name/%EC%98%A4%EC%9D%BC%EB%82%98%EC%9A%B0?patterns=%EA%B2%80%EC%83%89&imgId=cmtpnvoci000rlh04frsnnhkt

## 상태 화면 16-no-summary
연결된 MSDS가 공단 MSDS가 아니어서(직접 입력한 주소) 요약 없이 원문 보기만 있는 상태(프레임 16-no-summary-mobile · 16-no-summary-desktop). 모든 역할 같다. 모바일·데스크톱 모두 새로(rules.json msds_summary.original_link).
예시 상태: 페놀프탈레인 용액(MSDS는 2-msds-bulk · 3-msds "직접 입력"으로 넣은 주소). 공단 자료가 아니므로 출처 줄 · 신호어 · 그림문자 · 항목 카드를 그리지 않는다. 화면에는 제목과 msds-original-link만.
모바일 활성 탭: "시약". 위→아래: nav-pill(‹ + "MSDS · 페놀프탈레인 용액" + 학교명) → msds-original-link(제목 바로 아래 전폭, 간격 24) → 빈 캔버스 → tab-bar. 좌우 여백 16.
데스크톱 배치: app-sidebar("시약" 현재) | 본문 720 = 화면 2 시약 표("페놀프탈레인 용액" 행 #e6f4fc 선택) | detail-drawer 480 = "‹ 시약 상세" + × → heading-3 "MSDS · 페놀프탈레인 용액" → 바로 아래 전폭 msds-original-link(간격 24). 아래 고정 줄 없음.
### 구성 요소
- app-sidebar: 데스크톱 전용. 공통 규격, 학교명 "샘플고등학교" + 역할별 메뉴 + 이름·역할 + nav-account-menu
- sidebar-item: 데스크톱 전용. 학생 5개 / 교사 8개 / admin 10개(공통 메뉴). 현재 = "시약"
- nav-pill: 모바일 전용 헤더. 뒤로가기 ‹ + heading-3 "MSDS · 페놀프탈레인 용액"(길면 두 줄) + 현재 학교명 "샘플고등학교"(caption) + nav-account-menu ▾. 출처 줄 없음. 하늘색: 뒤로가기 아이콘 #2b9fe0
- nav-account-menu: 모바일 = 학교명 옆 ▾, 데스크톱 = app-sidebar 맨 아래(닫힌 상태). "로그아웃" 1개. 하늘색 없음
- data-table: 데스크톱 전용. 드로어 왼쪽 화면 2 시약 표, 선택 행 "페놀프탈레인 용액" #e6f4fc(MSDS 열 "있음")
- detail-drawer: 데스크톱 전용. 폭 480, 높이 900, #ffffff, 왼쪽 1px #f0f0f0 선, 여백 24, 딤 없음. 위→아래: "‹ 시약 상세"(link #141414) + × 닫기 → heading-3 "MSDS · 페놀프탈레인 용액" → msds-original-link. 나머지는 빈 #ffffff. 하늘색: × 아이콘 #2b9fe0
- msds-original-link: 전폭 button-outline "원문 MSDS 보기 ↗"(#ffffff, 1px #e0e0e0, 라벨 #141414, rounded 9999, 높이 44 이상) — 직접 입력된 주소를 새 창으로 연다. 모바일 = nav-pill 아래(간격 24), 데스크톱 = 드로어 제목 아래(간격 24). 요약 실패가 아니라 원래 요약이 없는 경우라 안내 카드·핑크 없음. 하늘색: ↗ 아이콘 #2b9fe0
- button-outline: msds-original-link 버튼 모양(위 정의)
- tab-bar: 모바일 전용 하단 탭바 1개(공통 규격). 데스크톱에는 두지 않는다. 하늘색: 활성 tab-item 아이콘 #2b9fe0만
- tab-item: "홈" · "시약" · "QR 스캔" · "기록" 4개. 활성 = "시약", 비활성 3개 #707070
### 반영한 레퍼런스
- https://uibowl.io/website/%EB%A7%A4%EB%8B%88%ED%8C%A8%EC%8A%A4%ED%8A%B8?patterns=%ED%81%90%EB%A0%88%EC%9D%B4%EC%85%98&imgId=cmulyw7j9001qjj04bmlsz9l1
- https://uibowl.io/website/%EB%A7%88%ED%94%8C?patterns=%EC%83%81%EC%84%B8%EC%A0%95%EB%B3%B4%20%28PDP%29&imgId=cmnnx4cuq02ikju04zkbrvx39

## 역할별 노출
앱 전체(로그인 후 화면) 기준 개수. runs/20261008-0936 표 숫자를 그대로 유지한다. 이번 run은 상태 화면의 데스크톱 배치(사이드바 · 드로어 · 팝오버 · 페이지 · 확인 모달)를 바꾸고 화면 16의 상태 3종을 더할 뿐, 표의 컴포넌트를 새로 더하거나 빼지 않는다. 같은 화면의 상태 화면에 다시 나오는 같은 컴포넌트는 그 화면 1개로 센다(예: 3-location의 location-edit = 화면 3의 1개, 2-*의 msds-bulk-banner = 화면 2의 1개, 11-empty · 11-delete의 cabinet-add = 화면 11의 1개, 11-delete · 11-unsaved의 cabinet-edit = 화면 11의 1개, 11-slot의 slot-assign = 1개, 3-msds · 7-msds · 7-doc-review의 msds-search = 화면 3 · 화면 7 각 1개, 7-*의 doc-upload = 화면 7의 1개).
msds-entry = 화면 3 1 + 화면 10 상세 1(학생·교사·admin 모두 2, R4). 화면 16과 16-* 상태는 msds-entry가 여는 목적지라 진입 개수를 바꾸지 않는다. 학생에게 열리는 상태(2-filter · 2-filter-empty · 4-past-date · 11-empty · 12-result · 16-*)에는 표의 교사·admin 전용 컴포넌트가 없다(11-empty 학생 = cabinet-add 없이 문구만, 2-filter* 학생 = msds-bulk-banner 없음).
sidebar-item은 역할마다 다르지만(학생 5 · 교사 8 · admin 10) rules.json roles 대상이 아니라 표에 넣지 않는다. app-sidebar · data-table · detail-drawer · msds-summary · msds-skeleton · ghs-pictogram · msds-original-link · nav-account-menu · qr-print-sheet · slot-sheet · location-picker · msds-candidates도 표 대상이 아니다.

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
