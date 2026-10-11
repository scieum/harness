# S2 설계 — run 20261011-0813

대상 화면: 2 (시약 목록) · 10 (사용 기록 내역) · 13 (홈) · 14 (회원가입) · 15 (랜딩) · 17 (센서, 새 화면) + 상태 화면 2-select · 2-bulk-delete · 13-not-found · 1-not-found · 14-error · 17-detail · 17-form · 17-empty · 17-select · 학교: 샘플고등학교 (input.json) · 키스크린: 17-desktop, 2-select-mobile, 17-form-mobile
변경 사유: 개발 세션 요청 7 (2026-10-11, rules.json 1.26) — ① 여러 개 한 번에 삭제(화면 2·17, 교사·admin) ② 모바일 'QR 스캔' 탭 = 회색 '준비 중'(탭 4개 유지), 데스크톱 'QR 찾기' 메뉴 = 비활성 '준비 중' ③ 찾을 수 없는 주소(13-not-found 로그인 후 · 1-not-found 로그인 전) ④ 가입 오류 요약 한 줄(14-error) ⑤ 랜딩 '사용 기록' 그림 = 새 화면 4 조각 ⑥ 기록 추가(화면 10 머리) ⑦ 무선 센서·현미경 보유 관리 화면 17 + 홈 센서 타일 + 데스크톱 사이드바 '센서'·모바일 '시약' 탭 안 inventory-switch.
근거: docs/PRD.md §7(2·10·12·13·14·15·17, 찾을 수 없는 주소), docs/story-service.md 결정 사항 2026-10-11 여섯 행("여러 개 한 번에 삭제"·"QR 탭 준비 중"·"찾을 수 없는 주소"·"가입 오류 요약"·"기록 추가"·"센서")과 "학교 선택"·"랜딩", docs/design.md "Select mode & bulk delete"·"Not found"·"Sign-up error summary"·"Add record"·"Sensors"·"Desktop shell"·"Pre-login desktop"·"tab-bar"·"School level"·"List filter", harness/rules.json 1.26(bulk_delete, not_found, signup_error, record_add, sensor, tab_bar.qr_pending·sensor_entry, landing_shot, desktop_shell.menu·desktop_required 17, screens_required 10·17, variants 2·13·1·14·17, roles R1~R7(R5에 list-select-toggle·select-checkbox·bulk-action-bar·sensor-add·sensor-edit·sensor-delete·sensor-alert-tile), never.N1·N2), research/s1-adopt.md, runs/20261011-0813/neis.json(화면 14 목록 값).
기준 설계(틀): input.json base — 화면 2·10·13·14 = 이전 S4 승인본(2·13 = runs/20261008-0936 설계 + 이후 승인 반영, 10 = runs/20261010-1340, 14 = runs/20261008-1233, 4 = S4-screens-v20), 15 = Figma S4-screens-v18 15-desktop·15-mobile(runs/20261008-2144 설계). 승인본 구성은 그대로 두고 요청 7 결정분만 더한다. 화면 17은 새로 설계한다(화면 2의 목록·필터·드로어 틀을 그대로 쓴다).

색·폰트·모서리·간격은 docs/design.md와 harness/rules.json을 따른다. 허용 색 밖의 값(딤 반투명 검정 등)은 쓰지 않는다. 그림자는 쓰지 않는다(segmented-control-active 예외). 떠 있는 버튼(FAB)은 두지 않는다.
- 핑크 #d6246a·연핑크 #fbe9f0는 badge-low-stock, reorder-alert-card, usage-over-stock 안에서만 쓴다(이번 대상 기준: 화면 2·13 재고 부족 배지, 13 재주문 알림, 15 조각 안 배지). 선택 모드·체크·삭제 띠·삭제 확인 모달·센서 상태 배지·센서 타일·404·가입 오류 요약에는 핑크를 쓰지 않는다.
- 하늘색 #2b9fe0·옅은 하늘색 #e6f4fc는 선택·현재 위치·아이콘·체크 표시에만 쓴다. 글자색 금지(그 위 글자 #141414). badge-low-stock·reorder-alert-card·button-primary·mix-warning 안에는 쓰지 않는다. 센서 상태 배지에도 쓰지 않는다.
- 삭제 버튼(bulk-action-bar "삭제", 확인 모달 "삭제", 센서 삭제 확인 "삭제")은 모두 검정 button-primary(#141414 채움, #ffffff 글자) — 시약장·시약 삭제와 같다.
- sensor-status-badge는 무채색만: 고장 = #141414 채움 pill + #ffffff label, 점검 필요 = #f3f3f3 pill + #141414 label, 정상 = 채움 없이 #707070 글자 "정상".
학교 선택은 회원가입(화면 14)에만 있다. 화면 2·10·13·17과 상태 화면 2-*·13-not-found·17-*에는 학교 선택·전환을 두지 않고 현재 학교명 "샘플고등학교"를 모바일은 nav-pill 안, 데스크톱은 app-sidebar 맨 위에 표시한다. 시약·센서·기록·홈 요약은 모두 샘플고등학교 것만 보인다(N1). 화면 14·15·1-not-found는 로그인 전이라 현재 학교명을 표시하지 않는다.
외부 서비스 연결 값(NEIS 학교 목록·센서 브랜드 목록·MSDS 요약)은 서버에서만 다룬다. 어떤 화면에도 연결 값 입력 칸·외부 서비스 설정·AI 엔진 선택 UI·관련 문구를 두지 않는다(N2).
괄호 안 역할 표시가 없는 구성 요소는 학생·교사·admin 모두에게 보인다. list-select-toggle·select-checkbox·bulk-action-bar·sensor-add·sensor-edit·sensor-delete·sensor-alert-tile은 교사·admin만 — 학생 화면에는 그리지 않는다(R5). 화면 17 목록·상세 보기, inventory-switch, record-add는 모든 역할이 같다.

모바일 공통(승인본 그대로 + 요청 7-2): tab-bar는 화면 아래 가장자리 y 780~844(폭 390, 높이 64, rounded 0, #ffffff + 위쪽 1px #f0f0f0 선, 그림자 없음)에 붙고 tab-item 4개("홈"·"시약"·"QR 스캔"·"기록")를 같은 폭으로 채운다. "QR 스캔" tab-item은 화면 12가 나오기 전까지 회색 — 아이콘·라벨 #adadad + 아이콘 아래 caption "준비 중"(#adadad), 누르면 ex-toast "준비 중이에요". 탭 4개는 그대로. 하단 고정 바·버튼·bulk-action-bar는 tab-bar 바로 위. 시트는 tab-bar 위쪽 선 위에 붙는다(딤 없음, 1px #e0e0e0 테두리, 위쪽 rounded 24, 오른쪽 위 × 닫기). nav-pill = 얇은 헤더(뒤로가기 또는 워드마크 + 제목 + 학교명 + nav-account-menu ▾). 센서는 탭이 아니라 '시약' 탭 안: 화면 2·17 모바일 맨 위 inventory-switch(segmented-control "시약 | 센서"), 마지막 고른 쪽을 기억. 화면 17 모바일에서 활성 탭은 "시약".
데스크톱 공통(1440×900, rules.json desktop_shell): nav-pill·tab-bar 없음.
- app-sidebar: 왼쪽 고정 열 폭 240, 높이 전체, rounded 0, #f3f3f3 채움, 오른쪽 1px #f0f0f0 선. 맨 위 "Lab_Stock" 워드마크 + 학교명 "샘플고등학교"(title #141414, 전환 없음) → sidebar-item 묶음 → 맨 아래 "{이름} · {역할}"(body-sm) + nav-account-menu ▾.
- sidebar-item: 아이콘 + body 라벨, 높이 44, rounded 0. 현재 항목 = #e6f4fc 채움 + #2b9fe0 아이콘, 라벨 #141414. 메뉴(rules.json desktop_shell.menu): 학생 6개(홈·시약·센서·기록·시약장·QR 찾기) / 교사 9개(+ "관리" 입고·실험 매뉴얼·재주문 알림) / admin 11개(+ "학교 설정" 사용자·판매처). "센서"는 "시약" 바로 아래(→ 화면 17). "QR 찾기"는 비활성 — 아이콘·라벨 #adadad + 라벨 오른쪽 caption "준비 중"(#adadad), 누르면 ex-toast "준비 중이에요".
- 본문 = 사이드바 오른쪽, 페이지 여백 32. 페이지 머리 = 왼쪽 제목(heading-2) + 개수(caption #707070), 오른쪽 검색·필터·선택·주 버튼. data-table = ex-data-table-cell 머리행(caption #707070)·본문(body-sm), rounded 16 컨테이너 + 1px #f0f0f0 테두리, 선택 행 #e6f4fc. detail-drawer = 오른쪽 폭 480, 높이 전체, #ffffff, 왼쪽 1px #f0f0f0 선, 딤 없음, 오른쪽 위 × 닫기(짧은 폼도 드로어 — 센서 등록·수정).
- 겹침: ex-modal-card는 확인에만(가운데, rounded 24, 1px #e0e0e0, 그림자·딤 없음). 모바일 고르기 시트(필터·회사 고르기·반 필터)는 데스크톱에서 그 컨트롤에 붙은 드롭다운·팝오버(#ffffff, 1px #e0e0e0, rounded 24). ex-toast는 오른쪽 아래.
예시 데이터(공통): 오늘 = 2026-10-11. 샘플고등학교 시약 42종, 재고 부족 3종(염산 · 50 mL, 에탄올 · 200 mL, 질산은 · 5 g), MSDS 없는 시약 4종, 재주문 알림 3건. 데스크톱 프레임 기준 역할 = 교사 "김OO · 교사".
- 센서 7개(이름 · 종류 · 회사 · 모델 · 수량 · 보관 위치 · 상태): 무선 온도 센서 · 온도 · 버니어 · GDX-TMP · 3개 · 과학실 뒤 선반 · 정상 / 무선 pH 센서 · pH · 버니어 · GDX-PH · 2개 · 1번 시약장 · 좌 1단 · 점검 필요 / 무선 힘 센서 · 힘 · 파스코 · PS-3202 · 4개 · 과학실 뒤 선반 · 정상 / 운동 센서 · 운동(거리) · 파스코 · PS-3219 · 2개 · 준비실 서랍 · 고장 / 전압 센서 · 전압 · 사이언스큐브 · — · 6개 · 준비실 서랍 · 정상 / CO₂ 센서 · CO₂ · 이지메이커 · — · 1개 · 과학실 뒤 선반 · 정상 / 디지털 현미경 · 기타 · 오맥스 · — · 2개 · 생물 준비실 · 정상. 고장 1 + 점검 필요 1 = 홈 센서 타일 2.

## 화면 2
시약 목록. 학생·교사·admin 모두. 승인본 그대로(필터 적용 없음, 이름순, "전체", 42종) + 요청 7: ① 모바일 맨 위 inventory-switch "시약 | 센서"("시약" 선택) ② 교사·admin에게 list-select-toggle "선택"(선택 모드 진입, 상태 화면 2-select) ③ 모바일 'QR 스캔' 탭 회색 '준비 중', 데스크톱 사이드바 '센서' 추가·'QR 찾기' 비활성. 행 끝에 삭제 버튼은 여전히 없다(여러 개 삭제는 선택 모드에서만, 하나 삭제는 화면 3에서만).
모바일 활성 탭: "시약". 위→아래: nav-pill → inventory-switch → (교사·admin) msds-bulk-banner → 페이지 머리 줄(왼쪽 heading-4 "시약 42종" + 오른쪽 (교사·admin) list-select-toggle) → segmented-control → 검색 줄(text-input + list-filter-button) → (필터 적용 시) filter-chip-row → reagent-row 목록 → tab-bar. 좌우 여백 16.
데스크톱 배치: app-sidebar("시약" 현재) | 본문 = 페이지 머리(왼쪽 "시약" + "42종" + 요약 줄 / 오른쪽 검색 text-input 폭 320 + list-filter-button + (교사·admin) list-select-toggle) → (교사·admin) msds-bulk-banner → 툴바(segmented-control 왼쪽, filter-chip-row 오른쪽) → data-table → 페이지 번호 "1 2 3".
### 구성 요소
- app-sidebar: 데스크톱 전용. 공통 규격, 워드마크 + 학교명 "샘플고등학교" + 역할별 메뉴 + 이름·역할·nav-account-menu
- sidebar-item: 데스크톱 전용. 학생 6개 / 교사 9개 / admin 11개("센서" 포함, "QR 찾기" 비활성 '준비 중'). 현재 = "시약"(#e6f4fc 채움 + #2b9fe0 아이콘, 라벨 #141414)
- nav-pill: 모바일 전용. "Lab_Stock" 워드마크 + 현재 학교명 "샘플고등학교" + nav-account-menu ▾. 학교 전환 없음
- nav-account-menu: 모바일 = 학교명 옆 ▾, 데스크톱 = app-sidebar 맨 아래. "로그아웃" 1개. 하늘색 없음
- inventory-switch: 모바일 전용. nav-pill 바로 아래 전폭 segmented-control "시약 | 센서"(#f3f3f3 트랙, rounded 9999, 두 칸 같은 폭, 누름 영역 44 이상). "시약" 선택(흰 pill), "센서"를 누르면 화면 17. 마지막 고른 쪽을 기억. 데스크톱에는 두지 않는다(사이드바 "센서"가 대신). 하늘색: 선택 칸 1px #2b9fe0 테두리(글자 #141414)
- msds-bulk-banner: 모바일 = inventory-switch 아래 전폭 띠(rounded 0, #e6f4fc, 여백 12·16) "MSDS 없는 시약 4종" + button-pill-soft "한 번에 찾기", 데스크톱 = 페이지 머리 아래 본문 폭 띠(rounded 16). 승인본 그대로. 하늘색: 띠 채움 #e6f4fc (교사·admin만)
- list-select-toggle: 선택 모드 진입. 모바일 = 페이지 머리 줄 오른쪽 button-pill-soft "선택"(#f3f3f3, 라벨 #141414, rounded 9999, 높이 44 이상), 데스크톱 = 페이지 머리 list-filter-button 오른쪽 button-outline "선택"(#ffffff, 1px #e0e0e0, 라벨 #141414, rounded 9999, 높이 44 이상). 누르면 상태 화면 2-select. 이 프레임은 선택 모드 아님. 핑크 없음 (교사·admin만)
- segmented-control: "전체 / 재고 부족", 한 번에 하나. 데스크톱 = 툴바 왼쪽
- segmented-control-active: 선택 옵션 흰 pill("전체", inventory-switch "시약"). 하늘색: 1px #2b9fe0 테두리(글자 #141414)
- text-input: 검색 "시약명 검색"(#f0f0f0, rounded 16, 포커스 링 2px #141414). 하늘색: 검색 아이콘 #2b9fe0
- list-filter-button: 검색 오른쪽 button-pill-soft "필터"(왼쪽 필터 아이콘, 높이 44 이상). 모바일 바텀시트 / 데스크톱 드롭다운 패널. 적용 개수 pill은 적용 없음이라 숨김. 하늘색: 필터 아이콘 #2b9fe0
- list-filter-sheet: 필터 패널(이 프레임에서는 닫힘, 승인본 2-filter 모양)
- filter-chip-row: 필터 적용 시에만(이 프레임 숨김)
- data-table: 데스크톱 전용 시약 표(승인본 그대로). 열 = 시약명(정렬, 활성 ↑ #2b9fe0) · 보관 분류 · 보관 위치 · 재고 · 상태(badge-low-stock) · 최근 입고일 · MSDS. 한 페이지 20행, 페이지 번호 "1 2 3". 행을 누르면 화면 3 드로어. 선택 모드가 아니면 체크 열 없음
- reagent-row: 모바일 전용. 시약명(title) + 재고량·단위(body) + 입고일(caption #707070), #f3f3f3, rounded 16, 행 사이 12. 누르면 화면 3. 하늘색: › 아이콘 #2b9fe0
- badge-low-stock: 재고 부족 3종 "재고 부족"(#d6246a 채움, #ffffff label, rounded 9999). 모바일 = 시약명 옆, 데스크톱 = 상태 열. 하늘색 없음
- button-pill-soft: list-select-toggle(모바일), msds-bulk-banner "한 번에 찾기"
- button-outline: list-select-toggle(데스크톱) (교사·admin만)
- ex-empty-state-card: 검색 결과 0건 "찾는 시약이 없어요"(이 프레임 숨김). 하늘색: 안내 아이콘 #2b9fe0
- ex-toast: 'QR 스캔' 탭·'QR 찾기' 메뉴를 누르면 "준비 중이에요"(이 프레임에는 그리지 않음). 핑크 없음
- tab-bar: 모바일 전용 하단 탭바 1개(공통 규격). 데스크톱에는 두지 않는다. 하늘색: 활성 tab-item 아이콘 #2b9fe0만
- tab-item: "홈" · "시약" · "QR 스캔" · "기록" 4개. 활성 = "시약". "QR 스캔" = 아이콘·라벨 #adadad + 아이콘 아래 caption "준비 중", 나머지 비활성 2개 #707070
### 반영한 레퍼런스
- https://uibowl.io/name/%EB%B9%84%EA%B8%80%EB%A3%A8?patterns=%EB%B6%81%EB%A7%88%ED%81%AC%C2%B7%EC%9C%84%EC%8B%9C%EB%A6%AC%EC%8A%A4%ED%8A%B8&imgId=cmpq8q4b2001rju042pzt4qlh
- https://uibowl.io/name/%EC%B9%B4%EC%B9%B4%EC%98%A4%EA%B3%A8%ED%94%84%EC%98%88%EC%95%BD?patterns=%EA%B2%80%EC%83%89&imgId=cmtwlue90002bjw04hgtwofel

## 상태 화면 2-select
선택 모드(프레임 2-select-mobile · 2-select-desktop, 키스크린 2-select-mobile). 교사·admin만 이 상태에 온다(학생 화면에는 "선택" 자체가 없다). 흐름: "선택" → 머리가 선택 상태로 바뀜 → 행을 누르면 상세 대신 체크가 바뀜 → 1개 이상이면 아래 bulk-action-bar → "삭제" → 상태 화면 2-bulk-delete. 핑크 없음(재고 부족 배지는 행 안에 그대로).
예시 상태: 교사 김OO. 이름순 "전체" 42종 중 5개 선택 — 과산화수소 · 구리 가루 · 글리세린 · 나프탈렌 · 녹말 가루. 머리 "5개 선택됨".
모바일 위→아래: nav-pill → inventory-switch → msds-bulk-banner → 선택 머리 줄(왼쪽 조용한 "취소" · 가운데 title "5개 선택됨" · 오른쪽 조용한 "전체 선택") → segmented-control → 검색 줄 → reagent-row 목록(행마다 왼쪽 select-checkbox, 행 내용은 오른쪽으로 밀림) → bulk-action-bar(tab-bar 바로 위) → tab-bar.
데스크톱 배치: app-sidebar("시약" 현재) | 본문 = 페이지 머리(왼쪽 "시약" + "42종" / 오른쪽 검색 + list-filter-button + list-select-toggle이 "취소"로 바뀜) → 툴바 → data-table(첫 열 select-checkbox, 머리 칸 = 전체 선택, 고른 5행 #e6f4fc) → 본문 아래 고정 bulk-action-bar(사이드바 오른쪽 본문 폭 전체).
### 구성 요소
- app-sidebar: 데스크톱 전용. 공통 규격, 학교명 "샘플고등학교" + 교사 메뉴 + "김OO · 교사" + nav-account-menu (교사·admin만)
- sidebar-item: 데스크톱 전용. 교사 9개 / admin 11개. 현재 = "시약", "QR 찾기" 비활성 '준비 중' (교사·admin만)
- nav-pill: 모바일 전용. 화면 2 nav-pill 그대로 — 워드마크 + 현재 학교명 "샘플고등학교" + nav-account-menu ▾ (교사·admin만)
- nav-account-menu: 닫힌 ▾ (교사·admin만)
- inventory-switch: 모바일 전용. "시약 | 센서", "시약" 선택. 하늘색: 선택 칸 1px #2b9fe0 테두리 (교사·admin만)
- list-select-toggle: 선택 모드 머리. 모바일 = 페이지 머리 줄이 바뀜: 왼쪽 조용한 텍스트 동작 "취소"(link #141414, 누름 영역 44 이상, 누르면 선택 모드 끝·체크 모두 해제) · 가운데 title #141414 "5개 선택됨" · 오른쪽 조용한 텍스트 동작 "전체 선택"(지금 필터·검색 결과 전체, 페이지 넘어 최대 100개, 넘으면 머리 아래 caption #707070 "앞의 100개만 골랐어요"). 데스크톱 = 페이지 머리 오른쪽 button-outline "선택"이 "취소"로 바뀌고 제목 옆 caption 자리에 "5개 선택됨", 전체 선택은 data-table 머리 칸 select-checkbox. 핑크·하늘색 없음 (교사·admin만)
- select-checkbox: 20px 원(rounded 9999). 안 고름 = #ffffff + 1px #adadad 테두리, 고름 = #2b9fe0 채움 + #ffffff 체크. 모바일 = reagent-row 카드 왼쪽(누름 영역 44 이상, 카드 내용은 오른쪽으로 밀림), 데스크톱 = data-table 첫 열 + 머리 칸(전체 선택, 일부만 골랐으면 #2b9fe0 채움 + 흰 가로줄). 예시 = 5개 고름. 하늘색: 고른 체크 원 #2b9fe0 (교사·admin만)
- reagent-row: 모바일 전용. 선택 모드 행 = 왼쪽 select-checkbox + 시약명·재고·입고일(화면 2와 같음), › 아이콘 숨김. 고른 행 = #e6f4fc 채움(안 고른 행 #f3f3f3). 행을 누르면 체크가 바뀜(상세로 가지 않음) (교사·admin만)
- data-table: 데스크톱 전용. 화면 2 표 + 맨 앞 select-checkbox 열(폭 48). 고른 5행 #e6f4fc. 행을 누르면 체크가 바뀜(드로어 열지 않음) (교사·admin만)
- badge-low-stock: 재고 부족 시약 행 안 "재고 부족"(#d6246a 채움, #ffffff label) 그대로. 고른 행이어도 배지 안 색은 바뀌지 않음 (교사·admin만)
- bulk-action-bar: 1개 이상 고르면 나타나는 띠 1개. #ffffff + 위 1px #f0f0f0 선, rounded 0, 여백 12·16. 왼쪽 title #141414 "5개 선택됨", 오른쪽 button-primary "삭제"(검정). 모바일 = tab-bar 바로 위 전폭(폭 390), 데스크톱 = 본문 아래 고정(사이드바 오른쪽 본문 폭, 오른쪽 여백 32). 0개가 되면 사라짐. 핑크·하늘색 없음 (교사·admin만)
- button-primary: bulk-action-bar "삭제"(#141414 채움, #ffffff 글자, rounded 9999, 높이 44 이상) → 상태 화면 2-bulk-delete. 하늘색 없음 (교사·admin만)
- button-outline: 데스크톱 list-select-toggle "취소" (교사·admin만)
- msds-bulk-banner: 화면 2와 같은 띠(그대로 보임). 하늘색: 띠 채움 #e6f4fc (교사·admin만)
- segmented-control: "전체 / 재고 부족"(선택 모드 중에도 바꿀 수 있고, 바꾸면 체크 유지) (교사·admin만)
- text-input: 검색 "시약명 검색" (교사·admin만)
- list-filter-button: 검색 오른쪽 "필터" (교사·admin만)
- tab-bar: 모바일 전용 하단 탭바 1개(공통 규격). bulk-action-bar는 이 바 위. 데스크톱에는 두지 않는다. 하늘색: 활성 tab-item 아이콘 #2b9fe0만 (교사·admin만)
- tab-item: 4개 "홈" · "시약" · "QR 스캔" · "기록". 활성 = "시약", "QR 스캔" 회색 '준비 중' (교사·admin만)
### 반영한 레퍼런스
- https://uibowl.io/name/%EC%B9%B4%EC%B9%B4%EC%98%A4%EA%B3%A8%ED%94%84%EC%98%88%EC%95%BD?patterns=%EA%B2%80%EC%83%89&imgId=cmtwlue90002bjw04hgtwofel
- https://uibowl.io/name/%EB%9D%BC%EC%9A%B4%EC%A6%88?patterns=%EC%9E%A5%EB%B0%94%EA%B5%AC%EB%8B%88&imgId=cmunlyn8s0005l804bcsbpzcr
- https://uibowl.io/name/%EB%B9%84%EA%B8%80%EB%A3%A8?patterns=%EB%B6%81%EB%A7%88%ED%81%AC%C2%B7%EC%9C%84%EC%8B%9C%EB%A6%AC%EC%8A%A4%ED%8A%B8&imgId=cmpq8q4b2001rju042pzt4qlh

## 상태 화면 2-bulk-delete
여러 개 삭제 확인(프레임 2-bulk-delete-mobile · 2-bulk-delete-desktop). 교사·admin만. 2-select에서 "삭제"를 누른 직후 — 뒤 화면은 2-select 그대로 보이고(딤 없음) 확인 모달이 열린 상태. "삭제" → ex-toast "시약 5개를 삭제했어요", 목록 그대로, 선택 모드 끝(목록·시약장·홈·재주문 알림에서 빠짐, 사용·입고 기록은 남고 화면 10에 '삭제된 시약'). 되돌리기 없음. 핑크 없음 — 삭제는 재고·안전 신호가 아니다.
예시 상태: 5개 선택(과산화수소 · 구리 가루 · 글리세린 · 나프탈렌 · 녹말 가루).
모바일: 모달 = tab-bar 위 시트 모양(전폭, 위쪽 rounded 24), 그 뒤 bulk-action-bar는 시트에 가려짐. 데스크톱 배치: app-sidebar("시약" 현재) | 2-select 본문(data-table 5행 선택 + 아래 bulk-action-bar) 위 가운데 ex-modal-card 폭 440.
### 구성 요소
- app-sidebar: 데스크톱 전용. 공통 규격, 학교명 "샘플고등학교" + 교사 메뉴 + nav-account-menu (교사·admin만)
- sidebar-item: 데스크톱 전용. 교사 9개 / admin 11개. 현재 = "시약" (교사·admin만)
- nav-pill: 모바일 전용. 화면 2 nav-pill 그대로 — 현재 학교명 "샘플고등학교" (교사·admin만)
- nav-account-menu: 닫힌 ▾ (교사·admin만)
- inventory-switch: 모바일 전용. 모달 뒤 "시약 | 센서"("시약" 선택) (교사·admin만)
- list-select-toggle: 모달 뒤 선택 머리 "취소 · 5개 선택됨 · 전체 선택"(모바일) / "취소" 버튼(데스크톱) 그대로 (교사·admin만)
- select-checkbox: 모달 뒤 고른 5행 체크 그대로(#2b9fe0 채움 + 흰 체크) (교사·admin만)
- reagent-row: 모바일 전용. 모달 뒤 선택 모드 행(고른 행 #e6f4fc) (교사·admin만)
- data-table: 데스크톱 전용. 모달 뒤 체크 열이 있는 시약 표, 고른 5행 #e6f4fc (교사·admin만)
- bulk-action-bar: 모달 뒤 "5개 선택됨" + "삭제" 띠(모바일은 시트에 가려짐, 데스크톱은 본문 아래 그대로) (교사·admin만)
- ex-modal-card: 여러 개 삭제 확인 1개(#ffffff, 1px #e0e0e0 테두리, 여백 24, 그림자·딤 없음, 오른쪽 위 × 닫기 누름 영역 44 이상). 모바일 = tab-bar 위 시트(전폭, 위쪽 rounded 24), 데스크톱 = 화면 가운데 폭 440, rounded 24. 위→아래: heading-3 "시약 5개를 삭제할까요?" → body-sm #141414 "과산화수소, 구리 가루, 글리세린 외 2개" → body #141414 "목록·시약장·재주문 알림에서 사라져요. 사용·입고 기록은 남아요." → body-sm #707070 "되돌릴 수 없어요." → 버튼 줄(위 간격 24): 왼쪽 button-outline "취소" + 오른쪽 button-primary "삭제"(1:1, 사이 8). × 와 "취소"는 같은 동작(모달만 닫히고 선택 유지). 핑크·하늘색 없음 (교사·admin만)
- button-outline: 모달 "취소"(#ffffff, 1px #e0e0e0, 라벨 #141414, rounded 9999, 높이 44 이상) (교사·admin만)
- button-primary: 모달 "삭제"(검정 — #141414 채움, #ffffff 글자, rounded 9999, 높이 44 이상), 뒤 bulk-action-bar "삭제". 핑크·하늘색 없음 (교사·admin만)
- ex-toast: "삭제" 뒤 "시약 5개를 삭제했어요"(모바일 tab-bar 위, 데스크톱 오른쪽 아래). 이 프레임에는 그리지 않는다. 하늘색: 완료 체크 아이콘 #2b9fe0 (교사·admin만)
- tab-bar: 모바일 전용 하단 탭바 1개(공통 규격). 시트는 이 바 위쪽 선 위에 붙는다. 데스크톱에는 두지 않는다 (교사·admin만)
- tab-item: 4개 "홈" · "시약" · "QR 스캔" · "기록". 활성 = "시약", "QR 스캔" 회색 '준비 중' (교사·admin만)
### 반영한 레퍼런스
- https://uibowl.io/name/%EC%97%90%EC%9D%B4%EB%8B%B7?patterns=%ED%8E%B8%EC%A7%91%C2%B7%EC%88%98%EC%A0%95%ED%95%98%EA%B8%B0&imgId=cmtwlvjdt001lju04v7bmhhvn

## 화면 10
사용 기록 내역. 학생·교사·admin 모두. 샘플고등학교 기록만. 승인본(runs/20261010-1340 화면 10) 구성 그대로 — 사용일로 묶고 최신순, 수업 표시(class-label), 반 필터(class-filter), 삭제된 시약 표시(deleted-reagent-tag) — + 요청 7-6: 페이지 머리 오른쪽 record-add "기록 추가"(모든 역할). 떠 있는 버튼 없음. 흐름: "기록 추가" → 빈 화면 4(상태 4-empty 모양) → 저장하면 화면 10으로 돌아오고 새 기록 행을 잠깐 #e6f4fc로 표시.
예시 상태: "전체", 기간 "최근 1개월", 반 "전체". 6건 —
① "10월 10일 · 어제": 에탄올 · 교사 김OO · 14:05 · 50 mL · 1학년 2반 · 통합과학 / 페놀프탈레인 용액 · 교사 김OO · 14:05 · 10 mL · 1학년 2반 · 통합과학 / 수산화나트륨 · 교사 김OO · 14:05 · 5 g · 1학년 2반 · 통합과학
② "10월 8일": 염산 · 학생 이OO · 10:20 · 20 mL · 2학년 1반 / 과망가니즈산 칼륨(삭제된 시약) · 교사 박OO · 09:40 · 5 g · 수업 없음
③ "10월 7일": 질산은 · 교사 김OO · 2 g · 통합과학 + "10월 8일에 기록"
데스크톱 프레임은 첫 행(에탄올)을 눌러 detail-drawer가 열린 상태.
모바일 활성 탭: "기록". 위→아래: nav-pill → 페이지 머리 줄(왼쪽 heading-4 "사용 기록 6건" + 오른쪽 record-add) → segmented-control + 기간 선택 → 검색 → class-filter 줄 → 사용일 그룹 목록 → tab-bar.
데스크톱 배치: app-sidebar("기록" 현재) | 본문 = 페이지 머리(왼쪽 "기록" + "6건" / 오른쪽 검색 + record-add) → 툴바(segmented-control "전체 / 내 기록" + 기간 드롭다운 + class-filter) → data-table(사용일 묶음 머리 행 + 기록 행, 열 "수업") → 페이지 번호 + 오른쪽 detail-drawer(기록 상세).
### 구성 요소
- app-sidebar: 데스크톱 전용. 공통 규격, 학교명 "샘플고등학교" + 역할별 메뉴 + nav-account-menu
- sidebar-item: 데스크톱 전용. 학생 6개 / 교사 9개 / admin 11개. 현재 = "기록", "QR 찾기" 비활성 '준비 중'
- nav-pill: 모바일 전용. "Lab_Stock" 워드마크 + 제목 "사용 기록 내역" + 현재 학교명 "샘플고등학교" + nav-account-menu ▾
- nav-account-menu: 모바일 = 학교명 옆 ▾, 데스크톱 = app-sidebar 맨 아래. "로그아웃" 1개. 하늘색 없음
- record-add: 페이지 머리 오른쪽 button-primary "기록 추가"(#141414 채움, #ffffff 글자, rounded 9999, 왼쪽 + 아이콘 #ffffff). 모바일 = 머리 줄 오른쪽 높이 44 작은 pill(폭은 라벨에 맞춤), 데스크톱 = 검색 text-input 오른쪽(사이 8, 높이 44). 누르면 빈 화면 4(데스크톱 본문 페이지). 떠 있는 버튼·그림자 없음, tab-bar와 겹치지 않음. 모든 역할. 하늘색 없음
- segmented-control: "전체 / 내 기록", 한 번에 하나. 데스크톱 = 툴바 왼쪽
- segmented-control-active: 선택 "전체" 흰 pill. 하늘색: 1px #2b9fe0 테두리(글자 #141414)
- text-input: 기간 선택 상자("최근 1개월" ▾, 사용일 기준)와 "시약명 검색"(#f0f0f0, rounded 16, 포커스 링 2px #141414). 하늘색: 검색·▾ 아이콘 #2b9fe0
- class-filter: 반 필터 button-pill-soft "반: 전체 ▾"(높이 44 이상). 모바일 = 검색 아래 줄 왼쪽, 데스크톱 = 툴바 기간 드롭다운 오른쪽. 모바일 바텀시트 / 데스크톱 드롭다운: 학년 → 반, 하단 "적용". 이 프레임은 "전체"·닫힘(승인본 그대로). 하늘색: ▾ 아이콘 #2b9fe0
- class-label: 기록 행의 수업 표기 "{학년}학년 {반}반 · {수업명}", 있는 것만. 모바일 = 행 보조줄 아래 caption #707070, 데스크톱 = data-table 열 "수업"(없으면 "—" #adadad) + 드로어 "수업 | 값" 행. 핑크·하늘색 없음
- deleted-reagent-tag: 과망가니즈산 칼륨 시약명 오른쪽 pill "삭제된 시약"(#f3f3f3 채움, label #141414, rounded 9999), 시약명 #707070, 시약 상세 링크·› 없음. 여러 개 삭제로 지운 시약도 같다. 핑크·하늘색 없음
- data-table: 데스크톱 전용. 열 = 사용일(정렬, 활성 ↓ #2b9fe0) · 시약명 · 수업 · 사용자 · 사용량 · 기록 시각. 사용일 묶음 머리 행("10월 10일 · 어제" / "10월 8일" / "10월 7일"). 선택 행(에탄올) #e6f4fc. 기록 추가 직후 돌아오면 새 행이 잠깐 #e6f4fc(이 프레임 아님). 0건이면 표 안 ex-empty-state-card
- ex-data-table-cell: 모바일 기록 목록 — 사용일 그룹 헤더(caption #707070) 아래 행 = 시약명(title) + 보조줄 body-sm #707070 "교사 김OO · 14:05" + class-label + 오른쪽 사용량(body). 데스크톱 data-table 셀 chrome. 하늘색: 누른 행 #e6f4fc, 그룹 헤더 왼쪽 #2b9fe0 인디케이터
- detail-drawer: 데스크톱 전용 기록 상세(승인본 그대로). heading-3 "에탄올" + display "50 mL" → "항목 | 값" 사용자 · 사용일 "2026-10-10" · 수업 "1학년 2반 · 통합과학" · 메모 → msds-entry → 아래 고정 button-outline "닫기"
- ex-modal-card: 모바일 전용 기록 상세 시트(tab-bar 위, × 닫기). 드로어와 같은 내용. 이 프레임에서는 닫힘
- msds-entry: 상세 안 button-pill-soft "MSDS 보기 ›" → 화면 16. 학생·교사·admin 모두. 하늘색: › 아이콘 #2b9fe0
- button-pill-soft: class-filter 버튼, msds-entry 버튼
- button-outline: 상세 "닫기"
- ex-empty-state-card: 결과 0건 "아직 사용 기록이 없어요" + "기간이나 반을 바꿔 보세요"(이 프레임 숨김). 핑크 없음
- ex-toast: 기록 추가 저장 뒤 화면 4가 띄우는 "3개 시약 사용을 기록했어요"는 이 화면으로 돌아온 뒤 보임(이 프레임에는 그리지 않음). 'QR 스캔' 탭을 누르면 "준비 중이에요"
- tab-bar: 모바일 전용 하단 탭바 1개(공통 규격). 데스크톱에는 두지 않는다. 하늘색: 활성 tab-item 아이콘 #2b9fe0만
- tab-item: "홈" · "시약" · "QR 스캔" · "기록" 4개. 활성 = "기록", "QR 스캔" 회색 '준비 중', 나머지 2개 #707070
### 반영한 레퍼런스
- https://uibowl.io/name/%EB%A7%88%EB%AF%B8%ED%86%A1?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&patternName=%EC%B2%B4%EC%A4%91%20%EA%B8%B0%EB%A1%9D%20%EC%B6%94%EA%B0%80
- https://uibowl.io/name/%EC%97%B4%ED%92%88%ED%83%80?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&patternName=%EA%B8%B0%EB%A1%9D%20%EC%B6%94%EA%B0%80
- https://uibowl.io/name/%EB%A7%88%EB%AF%B8%ED%86%A1?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&patternName=%EC%84%B1%EC%9E%A5%20%EA%B8%B0%EB%A1%9D%20%EC%B6%94%EA%B0%80

## 화면 13
홈. 로그인 후 첫 화면, 학생·교사·admin 모두. 승인본 그대로(quick-action·home-summary·reorder-alert-card·최근 사용 기록) + 요청 7-7: 교사·admin에게 고장·점검 필요 센서가 1개 이상일 때만 sensor-alert-tile "고장·점검 필요 센서 2"(→ 화면 17, 상태 필터 고장·점검 필요). 학생은 센서 타일 없음. 무채색.
예시 상태: 전체 시약 42종, 재고 부족 3종, MSDS 없는 시약 4종, 시약장 2개(칸 16개 중 지정 14 · 미지정 2), 재주문 알림 3건, 최근 사용 기록 3줄, 센서 고장 1 · 점검 필요 1.
모바일 활성 탭: "홈". 위→아래: nav-pill → quick-action(교사·admin 3칸 2+1, 학생 2칸) → home-summary ① 재고 요약(교사·admin은 카드 맨 아래 sensor-alert-tile 줄) → (교사·admin) reorder-alert-card → home-summary ② 시약장 요약 → 최근 사용 기록 카드 → tab-bar.
데스크톱 배치: app-sidebar("홈" 현재) | 본문 = 페이지 머리(왼쪽 heading-2 "샘플고등학교" + "오늘 10월 11일 · 전체 시약 42종" / 오른쪽 quick-action 버튼 줄) → 숫자 타일 줄 "지금 처리할 것"(교사·admin = 재고 부족 3 · 재주문 알림 3 · MSDS 없는 시약 4 · 고장·점검 필요 센서 2 — 같은 크기 4칸 한 줄 / 학생 = 재고 부족 3) → 3열 위젯 격자(최근 사용 기록 data-table 2칸 폭 · 재고 부족 · 시약장 요약).
### 구성 요소
- app-sidebar: 데스크톱 전용. 공통 규격, 학교명 "샘플고등학교" + 역할별 메뉴 + nav-account-menu
- sidebar-item: 데스크톱 전용. 학생 6개 / 교사 9개 / admin 11개. 현재 = "홈", "QR 찾기" 비활성 '준비 중'
- nav-pill: 모바일 전용. "Lab_Stock" 워드마크 + 현재 학교명 "샘플고등학교" + nav-account-menu ▾. 학교 선택·전환 없음
- nav-account-menu: 모바일 = 학교명 옆 ▾, 데스크톱 = app-sidebar 맨 아래. "로그아웃" 1개. 하늘색 없음
- quick-action: 역할별 작업 바로가기(승인본 그대로). 모바일 = 교사 3칸 "사용 기록 입력" · "입고"(stock-intake 진입) · "시약장 설정", admin 3칸 "입고" · "사용자 관리"(user-manage 진입) · "시약장 설정", 2+1. 학생 2칸 "사용 기록 입력" · "시약장 보기". 데스크톱 = 페이지 머리 오른쪽 버튼 줄(같은 항목). 하늘색: 모바일 아이콘 #2b9fe0 + 바탕 #e6f4fc
- home-summary: 모바일 = 요약 카드 2장(#ffffff, 1px #f0f0f0, rounded 24, 여백 24) ① 재고 요약 "재고 부족 3개" + 부족 시약 칩 + "전체 시약 42종" (+ 교사·admin 카드 맨 아래 sensor-alert-tile 줄) ② 시약장 요약(막대 + "칸 16개 중 지정 14 · 미지정 2"). 데스크톱 = 숫자 타일(#ffffff, 1px #f0f0f0, rounded 24, 여백 24, 위 caption 이름 · 아래 display 숫자, 타일 전체가 링크): "재고 부족 3" · (교사·admin) "MSDS 없는 시약 4" + 위젯 "재고 부족"·"시약장 요약". 하늘색: 막대 지정 구간, › 아이콘
- sensor-alert-tile: 고장·점검 필요 센서 N(예시 2). 고장·점검 필요가 0개면 그리지 않는다. 모바일 = home-summary ① 카드 맨 아래 1px #f0f0f0 선 위 한 줄: 왼쪽 센서 아이콘 #141414 + body #141414 "고장·점검 필요 센서 2" + 오른쪽 › (줄 전체 누름 영역 44 이상, → 화면 17 상태 필터 고장·점검 필요). 데스크톱 = "지금 처리할 것" 줄 4번째 숫자 타일(다른 타일과 같은 크기·모양: #ffffff, 1px #f0f0f0, rounded 24, caption #707070 "고장·점검 필요 센서" + display #141414 "2", 타일 전체가 링크). 무채색 — 핑크·하늘색 채움·배지 없음. 하늘색: › 아이콘만 #2b9fe0 (교사·admin만)
- badge-low-stock: 재고 요약 개수 배지 "3", reorder-alert-card 안 "재고 부족"(#d6246a 채움, #ffffff label). 데스크톱 = "재고 부족 3" 타일 숫자 옆. 하늘색 없음
- reorder-alert-card: "재주문 알림" 카드(#f3f3f3, rounded 24). 모바일 = heading-4 "재주문 알림" + badge-low-stock + "3건 ›" + "필요량보다 적은 시약이 3종 있어요", 데스크톱 = 숫자 타일 줄의 타일 1개. 판매처 연결 버튼 없음. 하늘색 없음 (교사·admin만)
- data-table: 데스크톱 전용 "최근 사용 기록" 위젯(2칸 폭). 열 = 사용일 · 시약명 · 사용자 · 사용량, 3행, 머리 오른쪽 "전체 보기 ›"(→ 화면 10)
- reagent-row: 모바일 최근 사용 기록 카드 안 3줄(시약명 + "학생 이OO · 20 mL" + 시각). 누르면 화면 10. 하늘색: 누른 행 #e6f4fc
- button-pill-soft: 모바일 "더 보기 ›", reorder-alert-card "3건 ›"(교사·admin만), 데스크톱 위젯 머리 "전체 보기 ›". 하늘색: reorder-alert-card 밖 › 아이콘만
- ex-empty-state-card: 시약장 0개 / 최근 사용 기록 0건 안내(이 프레임 숨김, 승인본 그대로)
- button-outline: 데스크톱 quick-action 버튼 줄 보조 버튼, 빈 상태 버튼
- button-primary: 데스크톱 quick-action 버튼 줄 마지막 버튼(교사·admin "입고", 학생 "사용 기록 입력"). 하늘색 없음
- tab-bar: 모바일 전용 하단 탭바 1개(공통 규격). 데스크톱에는 두지 않는다. 하늘색: 활성 tab-item 아이콘 #2b9fe0만
- tab-item: "홈" · "시약" · "QR 스캔" · "기록" 4개. 활성 = "홈", "QR 스캔" 회색 '준비 중'. 역할별 작업은 tab-item으로 두지 않는다
### 반영한 레퍼런스
- https://uibowl.io/name/Kia?patterns=%EB%A9%94%EC%9D%B8&imgId=cmpur0a3g000dl504qp9o8f4s
- https://uibowl.io/website/%EB%A7%88%EC%9D%B4%ED%81%AC%EB%A1%9C%EC%86%8C%ED%94%84%ED%8A%B8%20%ED%81%B4%EB%9E%98%EB%A6%AC%ED%8B%B0%20(Microsoft%20Clarity)?patterns=%EB%A9%94%EC%9D%B8&patternName=%EB%8C%80%EC%8B%9C%EB%B3%B4%EB%93%9C

## 상태 화면 13-not-found
로그인 후 찾을 수 없는 주소(프레임 13-not-found-mobile · 13-not-found-desktop). 모든 역할 같다. 앱 셸(모바일 nav-pill·tab-bar, 데스크톱 app-sidebar)을 유지한 채 본문 가운데 빈 상태 카드 1개. 현재 메뉴 없음. 핑크 없음.
예시 상태: 교사 김OO, 없는 주소로 들어옴.
모바일 위→아래: nav-pill → 본문 가운데 ex-empty-state-card(안에 버튼 2개) → tab-bar(활성 탭 없음). 데스크톱 배치: app-sidebar(현재 항목 없음) | 본문 가운데(세로·가로 가운데) ex-empty-state-card 폭 440.
### 구성 요소
- app-sidebar: 데스크톱 전용. 공통 규격, 학교명 "샘플고등학교" + 역할별 메뉴 + nav-account-menu
- sidebar-item: 데스크톱 전용. 학생 6개 / 교사 9개 / admin 11개. 현재 항목 없음(모두 #e6f4fc 없음, 아이콘 #707070), "QR 찾기" 비활성 '준비 중'
- nav-pill: 모바일 전용. "Lab_Stock" 워드마크 + 현재 학교명 "샘플고등학교" + nav-account-menu ▾
- nav-account-menu: 닫힌 ▾. "로그아웃" 1개
- ex-empty-state-card: 찾을 수 없는 주소 카드 1개(#ffffff, 1px #f0f0f0 테두리, rounded 24, 여백 24, 가운데 정렬). #141414 안내 아이콘(나침반) → heading-3 "페이지를 찾을 수 없어요" → body #707070 "주소가 바뀌었거나 없는 페이지예요." → 버튼 줄(위 간격 24, 사이 8): button-primary "홈으로"(→ 화면 13) + button-outline "뒤로"(이전 화면). 모바일 = 좌우 여백 16 전폭 카드, 버튼 1:1 나란히. 핑크·하늘색 없음
- button-primary: 카드 "홈으로"(#141414 채움, #ffffff 글자, rounded 9999, 높이 44 이상). 하늘색 없음
- button-outline: 카드 "뒤로"(#ffffff, 1px #e0e0e0, 라벨 #141414, rounded 9999, 높이 44 이상)
- tab-bar: 모바일 전용 하단 탭바 1개(공통 규격). 데스크톱에는 두지 않는다
- tab-item: 4개 "홈" · "시약" · "QR 스캔" · "기록". 활성 없음 — "홈"·"시약"·"기록" 아이콘·라벨 #707070, "QR 스캔" 회색 '준비 중'(#adadad)
### 반영한 레퍼런스
- https://uibowl.io/name/%EB%B3%B4%EB%A7%B5?patterns=%EB%A9%94%EC%9D%B8&imgId=cmr2zjo33000iij04gv6ptj59

## 상태 화면 1-not-found
로그인 전 찾을 수 없는 주소(프레임 1-not-found-mobile · 1-not-found-desktop). 역할 없음. 앱 셸 없음 — 데스크톱 web-header, 모바일 nav-pill(워드마크만), tab-bar·app-sidebar 없음. 학교명·학교 선택 없음. 핑크 없음.
모바일 위→아래: nav-pill → 본문 가운데 ex-empty-state-card(안에 "처음으로"). 데스크톱 배치: web-header(오른쪽 "로그인" + "회원가입") | 아래 본문 가운데 ex-empty-state-card 폭 440.
### 구성 요소
- web-header: 데스크톱 전용. 로그인 전 공통 규격(전폭 1440, 높이 64, rounded 0, #ffffff + 아래 1px #f0f0f0). 왼쪽 "Lab_Stock" 워드마크(→ 화면 15), 오른쪽 button-outline "로그인"(→ 화면 1) + button-primary "회원가입"(→ 화면 14), 사이 8. 하늘색 없음
- nav-pill: 모바일 전용. "Lab_Stock" 워드마크만(#f3f3f3, rounded 9999). 학교명·nav-account-menu 없음. 데스크톱에는 두지 않는다
- ex-empty-state-card: 카드 1개(#ffffff, 1px #f0f0f0 테두리, rounded 24, 여백 24, 가운데 정렬). #141414 안내 아이콘 → heading-3 "페이지를 찾을 수 없어요" → body #707070 "주소가 바뀌었거나 없는 페이지예요." → 위 간격 24 button-primary "처음으로"(→ 화면 15) 1개. 핑크·하늘색 없음
- button-primary: 카드 "처음으로", 데스크톱 web-header "회원가입"(#141414 채움, #ffffff 글자, rounded 9999, 높이 44 이상). 하늘색 없음
- button-outline: 데스크톱 web-header "로그인"(#ffffff, 1px #e0e0e0, 라벨 #141414, rounded 9999, 높이 44 이상)
### 반영한 레퍼런스
- https://uibowl.io/name/%EB%B3%B4%EB%A7%B5?patterns=%EB%A9%94%EC%9D%B8&imgId=cmr2zjo33000iij04gv6ptj59

## 화면 14
회원가입. 학교(시/도 → 지역 → 학교급 → 학교)와 계정(이름·개인 이메일·비밀번호)을 받는다. 승인본(runs/20261008-1233 화면 14) 그대로 + 요청 7-4: "가입하기"는 늘 누를 수 있고, 누르면 검사해서 빠지거나 틀린 칸이 있으면 버튼 바로 위 signup-error-summary 한 줄 + 첫 오류 칸으로 스크롤·포커스(상태 화면 14-error). 현재 학교명은 표시하지 않는다(학교를 고르는 중).
예시 상태(14-mobile · 14-desktop, neis.json): 시/도 "충청북도" 선택됨 → 지역 "청주시" 선택됨 → 학교급 아직 고르지 않음(3칸 #707070) → 학교 칸 비활성 "학교급을 먼저 골라 주세요". 계정 칸 비어 있음, 약관 모두 미동의, 진행 막대 2칸 채움. 아직 누르지 않아 오류 요약 없음.
모바일(390×844) 위→아래: nav-pill → ex-auth-form-card(제목 → 학교 블록[안내 박스 → 진행 막대 → 시/도 → 지역 → 학교급 → 학교] → 계정 블록[이름 → 개인 이메일 → 비밀번호 → 비밀번호 확인] → 약관 동의) → 카드 아래 로그인 줄 → 하단 고정 영역(signup-error-summary 자리 + "가입하기"). 하단 탭바 없음.
데스크톱 배치: web-header(오른쪽 button-outline "로그인"만) | 아래 반 나눔 — 왼쪽 폼 열 폭 440(heading-1 "회원가입" → "1 학교 선택"[안내 박스 → 진행 막대 → 시/도 → 지역 → 학교급 → 학교] → 구분선 → "2 계정"[이름 → 개인 이메일 → 비밀번호 → 비밀번호 확인 → 약관 동의 → signup-error-summary 자리 → 전폭 "가입하기"] → "이미 계정이 있으신가요? 로그인 ›") / 오른쪽 #f3f3f3 서비스 소개 패널(feature-card 4개). 목록은 칸 아래 드롭다운. 하단 탭바 없음.
### 구성 요소
- web-header: 데스크톱 전용. 로그인 전 공통 규격(높이 64, rounded 0, #ffffff + 아래 1px #f0f0f0). 왼쪽 "Lab_Stock" 워드마크(→ 화면 15), 오른쪽 button-outline "로그인"(→ 화면 1)만. 하늘색 없음
- nav-pill: 모바일 전용. 뒤로가기(화면 1) + "Lab_Stock" 워드마크 + 제목 "회원가입". 학교명·nav-account-menu 없음. 하늘색: 뒤로가기 아이콘 #2b9fe0
- ex-auth-form-card: 가입 폼(승인본 그대로). 모바일 = 카드(#ffffff, 1px #f0f0f0, rounded 24, 여백 24) 제목 "회원가입" + "우리 학교를 고르고 계정을 만드세요". 데스크톱 = 왼쪽 폼 열, 번호 섹션 "1 학교 선택" → 구분선 → "2 계정". 학교 블록: 안내 박스(#e6f4fc, rounded 16, 정보 아이콘 #2b9fe0 + body-sm #141414 "고른 학교의 시약·기록만 보여요. 가입한 뒤에는 바꿀 수 없어요") → 4단계 진행 막대(예시 2칸 #2b9fe0, 나머지 #e0e0e0) → 학교 4칸. 계정 블록: text-input 4개. 약관 동의: "모두 동의" + 필수 2줄(원형 체크). 하늘색: 안내 박스, 진행 막대, 동의 체크 원, › 아이콘
- school-select-sido: 첫 번째 칸 "시/도"(▾ 선택 상자, #f0f0f0, rounded 16). 목록 = neis.json sido_list 17개(모바일 바텀시트 "시/도 선택" + ×, 데스크톱 칸 아래 드롭다운). 예시 값 "충청북도"(선택됨). 바꾸면 지역·학교급·학교가 비워진다. 하늘색: 선택된 칸 #e6f4fc + #2b9fe0 체크(글자 #141414)
- school-select-region: 두 번째 칸 "지역(시/군/구)". 시/도 전 비활성. 목록 = neis.json region_list 11개(괴산군 … 청주시 · 충주시). 예시 값 "청주시"(선택됨). 바꾸면 학교가 비워진다. 하늘색: 선택된 칸 #e6f4fc + #2b9fe0 체크
- school-select-kind: 세 번째 칸 "학교급" — segmented-control 3칸 "초등학교 · 중학교 · 고등학교"(neis.json kind_list). 기본값 없음(예시 = 3칸 #707070, 흰 pill 없음). 고르면 흰 pill + 1px #2b9fe0 테두리, 학교 칸이 켜진다. 특수학교·각종학교 칸 없음. 하늘색: 선택 칸 테두리만
- school-select-school: 네 번째 칸 "학교". 학교급 전 비활성 — #f0f0f0 + 플레이스홀더 "학교급을 먼저 골라 주세요"(#adadad) + ▾ #adadad(예시 상태). 켜지면 목록 = 고른 지역·학교급 학교(neis.json school_list, 고등학교 38개: 금천고등학교 · 봉명고등학교 · … · 흥덕고등학교), 위 검색 text-input. 0개면 상태 14-no-school(승인본). 하늘색: 목록 선택 행 #e6f4fc + 체크 #2b9fe0
- segmented-control: school-select-kind 트랙(#f3f3f3, rounded 9999)
- segmented-control-active: 학교급을 고른 뒤 흰 pill(예시 상태에서는 없음). 하늘색: 1px #2b9fe0 테두리
- text-input: 계정 4칸 "이름" · "개인 이메일"(플레이스홀더 "name@example.com") · "비밀번호"(가림, 눈 아이콘 #707070) · "비밀번호 확인"(가림). #f0f0f0, rounded 16, 포커스 링 2px #141414. 오류 칸은 2px #141414 테두리 + 칸 아래 body-sm #707070 안내 한 줄(상태 14-error). 하늘색: 일치 체크 아이콘만
- signup-error-summary: 오류 요약 한 줄 자리 — 모바일 = 하단 고정 "가입하기" 바로 위, 데스크톱 = 섹션 2 "가입하기" 바로 위. "가입하기"를 눌렀는데 오류가 있을 때만 보인다(이 프레임에서는 숨김, 상태 14-error). 핑크 없음
- button-primary: 전폭 "가입하기"(#141414 채움, #ffffff 글자, rounded 9999, 높이 44 이상). 2026-10-11부터 늘 누를 수 있음 — 누르면 검사, 오류가 있으면 signup-error-summary + 첫 오류 칸으로 스크롤·포커스, 없으면 계정에 고른 학교를 저장하고 화면 13. 모바일 = 화면 하단 고정, 데스크톱 = 섹션 2 맨 아래. 하늘색 없음
- button-outline: 데스크톱 web-header "로그인" → 화면 1
- button-pill-soft: 폼 아래 "이미 계정이 있으신가요?" + "로그인 ›" → 화면 1. 하늘색: › 아이콘 #2b9fe0
- feature-card: 데스크톱 전용. 오른쪽 서비스 소개 패널 4개 목록(승인본 그대로, badge-low-stock 없음). 하늘색: 아이콘만
### 반영한 레퍼런스
- https://uibowl.io/name/%ED%8E%98%EC%9D%B4%EC%BD%94?patterns=%EB%A1%9C%EA%B7%B8%EC%9D%B8%C2%B7%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85&imgId=cmupp0tss0016l904iev4lrxz
- https://uibowl.io/name/EVSIS?patterns=%EB%A1%9C%EA%B7%B8%EC%9D%B8%C2%B7%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85&imgId=cmokqecp5001dkw04pg7dqabn

## 상태 화면 14-error
가입하기를 눌렀는데 오류가 있는 상태(프레임 14-error-mobile · 14-error-desktop). 로그인 전, 역할 없음. 버튼 바로 위 오류 요약 한 줄 + 문제 칸에만 칸 아래 안내 문구, 나머지 칸은 그대로. 첫 오류 칸으로 스크롤·포커스(개발 쪽). 서버 오류(입력과 무관, 예: 가입 처리 실패)는 칸이 아닌 같은 요약 줄 한 줄로 보인다. 핑크 없음.
예시 상태(neis.json): 시/도 "충청북도" → 지역 "청주시" → 학교급 "고등학교" → 학교 "청주고등학교" 모두 선택(진행 막대 4칸), 이름 "김OO" · 개인 이메일 "kim@example.com" · 비밀번호 · 비밀번호 확인 일치, 필수 약관 2개 미동의 → 요약 "약관에 동의해 주세요". 오류가 여럿이면 "{첫 오류 문구} 외 N개"(예: "비밀번호가 일치하지 않아요 외 1개"). 화면은 약관 동의 묶음으로 스크롤된 상태(모바일은 약관 줄이 고정 영역 바로 위에 보임).
모바일 위→아래: 화면 14와 같은 순서(스크롤 아래쪽) → 하단 고정 영역(signup-error-summary 한 줄 → "가입하기"). 데스크톱 배치: web-header("로그인"만) | 왼쪽 폼 열 섹션 2 아래쪽(약관 동의 → signup-error-summary → "가입하기") / 오른쪽 서비스 소개 패널. 하단 탭바 없음.
### 구성 요소
- web-header: 데스크톱 전용. 화면 14와 같음 — 왼쪽 워드마크, 오른쪽 button-outline "로그인"만. 하늘색 없음
- nav-pill: 모바일 전용. 화면 14와 같음 — 뒤로가기 + "Lab_Stock" + "회원가입". 학교명 없음
- ex-auth-form-card: 화면 14와 같은 가입 폼. 진행 막대 4칸 채움. 약관 동의 묶음 = 오류 칸: 필수 2줄의 원형 체크에 2px #141414 링(포커스) + 묶음 아래 body-sm #707070 "필수 약관에 동의해 주세요". 다른 칸은 오류 표시 없음. 하늘색: 안내 박스, 진행 막대, › 아이콘(오류 표시는 하늘색·핑크 아님)
- school-select-sido: "시/도" 값 "충청북도"(선택됨, #e6f4fc + #2b9fe0 체크, 글자 #141414)
- school-select-region: "지역(시/군/구)" 값 "청주시"(선택됨)
- school-select-kind: segmented-control "초등학교 · 중학교 · 고등학교", "고등학교" 선택됨(흰 pill + 1px #2b9fe0 테두리)
- school-select-school: "학교" 값 "청주고등학교"(neis.json school_list 중, 선택됨 #e6f4fc + #2b9fe0 체크)
- segmented-control: 학교급 트랙(#f3f3f3, rounded 9999)
- segmented-control-active: "고등학교" 흰 pill. 하늘색: 1px #2b9fe0 테두리
- text-input: 계정 4칸 채움(오류 없음). 비밀번호 확인 아래 "비밀번호가 일치해요"(#2b9fe0 체크 아이콘 + #141414 글자)
- signup-error-summary: 버튼 바로 위 한 줄(간격 8) — 왼쪽 작은 안내 아이콘 #707070(16) + body-sm #141414 "약관에 동의해 주세요". 채움·테두리 없음, 왼쪽 정렬. 여럿이면 "… 외 N개". 모든 칸이 고쳐지면 사라진다. 모바일 = 하단 고정 영역(#ffffff, 위 1px #f0f0f0 선, 여백 12·16) 안 "가입하기" 위, 데스크톱 = 섹션 2 "가입하기" 위. 핑크·하늘색 없음
- button-primary: 전폭 "가입하기"(눌린 뒤에도 활성, #141414 채움, #ffffff 글자, rounded 9999, 높이 44 이상). 하늘색 없음
- button-outline: 데스크톱 web-header "로그인"
- button-pill-soft: 폼 아래 "로그인 ›"(스크롤 아래쪽이라 모바일은 화면 밖일 수 있음). 하늘색: › 아이콘 #2b9fe0
- feature-card: 데스크톱 전용. 오른쪽 서비스 소개 패널 4개 목록. 하늘색: 아이콘만
### 반영한 레퍼런스
- https://uibowl.io/name/%ED%8E%98%EC%9D%B4%EC%BD%94?patterns=%EB%A1%9C%EA%B7%B8%EC%9D%B8%C2%B7%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85&imgId=cmupp0tss0016l904iev4lrxz
- https://uibowl.io/name/EVSIS?patterns=%EB%A1%9C%EA%B7%B8%EC%9D%B8%C2%B7%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85&imgId=cmokqecp5001dkw04pg7dqabn
- https://uibowl.io/name/%EB%A7%88%EC%9D%B4%ED%98%84%EB%8C%80?patterns=%EB%A1%9C%EA%B7%B8%EC%9D%B8%C2%B7%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85&imgId=cmojm0qqb00iejs043ihvynj2
- https://uibowl.io/name/%EC%88%98%ED%98%84%EC%9D%B4%EB%9E%91?patterns=%EC%9D%B8%EC%A6%9D%ED%95%98%EA%B8%B0&imgId=cmouxls7i0010k004p8404isj

## 화면 15
랜딩. 로그인 전 첫 화면. 바탕 = Figma S4-screens-v18 15-desktop · 15-mobile(runs/20261008-2144 설계 그대로). 15-mobile은 바뀌는 것이 없다. 15-desktop은 landing-section ② "사용 기록"의 그림만 바꾼다(rules.json landing_shot) — 이전 조각 ⓑ(4-desktop 사용 기록 드로어, 한 시약 폼)를 승인된 S4-screens-v20 4-desktop 본문 페이지 조각(여러 시약 담기 + 수업)으로 교체. 섹션 순서·위치·높이(1440 × 5498)·문구·다른 조각은 그대로. 학교명·학교 선택·tab-bar·app-sidebar 없음.
CTA 위계: 채움 "회원가입" → 외곽선 "로그인" → 가장 약한 "둘러보기" 3단. 페이지 끝 cta-band에서 한 번 더.
모바일(390×844, 그대로) 위→아래: nav-pill → landing-hero → feature-card 4장 → 하단 고정 영역(landing-cta 버튼 2개 세로 + guest-entry). 하단 탭바 없음.
데스크톱 배치: 1440 × 5498 세로 긴 프레임 한 장, web-header(위 고정) | 가운데 콘텐츠 폭 1200 — 히어로(landing-hero · product-shot · landing-cta · guest-entry) → landing-tabs → 문제 공감 feature-card 3 → landing-section 4(좌우 번갈아, ②의 조각 ⓑ만 교체) → step-flow 5단계 → 대상 탭 → 안심 2×2 → cta-band → web-footer 한 줄. 섹션 배경 리듬(흰 ↔ #f3f3f3, step-flow·cta-band #141414 반전)과 반전 버튼은 승인본 그대로.
landing-section ② 새 조각(조각 왼쪽 · 글 오른쪽, 글은 그대로 — 꼬리표 "사용 기록" → "누가 얼마나 썼는지 남겨요" → 점 목록 3 → "둘러보기에서 보기 ›"): ⓐ 승인 13-desktop 홈 "최근 사용 기록" 위젯(그대로) ⓑ 승인 v20 4-desktop 본문 페이지의 640 열 윗부분 — 머리 "담은 시약 3개" + 표 3행(에탄올 1,200 mL / 50 · 페놀프탈레인 용액 120 mL / 10 · 수산화나트륨 500 g / 5) + "수업 | 1학년 2반 · 통합과학" 행 + 하단 바 "사용 기록 저장 · 3개" 일부. ⓑ를 ⓐ 오른쪽 아래에 겹치고, 왼쪽 가장자리에서 잘림. 조각 안에는 사이드바를 넣지 않는다. 조각 = 납작한 묶음 "shot-4"(안 노드 이름에 usage-batch-list·class-select 등 컴포넌트명을 쓰지 않음), #ffffff 바탕, 1px #f0f0f0 테두리, rounded 16, 그림자 없음. 조각 안 학교명 없음, 핑크 없음(사용량 정상 예시).
### 구성 요소
- web-header: 데스크톱 전용. 로그인 전 공통 규격(전폭 1440, 높이 64, rounded 0, #ffffff + 아래 1px #f0f0f0). 왼쪽 워드마크, 오른쪽 button-outline "로그인" + button-primary "회원가입". 긴 페이지에서 위 고정. 하늘색 없음
- nav-pill: 모바일 전용(그대로). "Lab_Stock" 워드마크만. 데스크톱에는 두지 않는다
- landing-hero: 모바일 = 승인본 그대로. 데스크톱 = 히어로 왼쪽 글 열(꼬리표 → 2줄 헤드라인 "우리 학교 시약장, / 한 화면에서 관리해요" 48 Bold 700 → body-lg 부제 → landing-cta → guest-entry → caption). 모노크롬, 학교명 없음
- product-shot: 데스크톱 전용. 히어로 오른쪽 묶음(승인본 그대로 — #f3f3f3 패널 + 브라우저 틀 + 13-desktop 조각 + 겹친 data-table 카드). 핑크는 조각 안 badge-low-stock 안에서만
- shot-sidebar: 데스크톱 전용. product-shot · 대상 탭 교사 조각 안 승인 화면 사이드바 이름(app-sidebar로 세지 않음). 새 shot-4 조각에는 없음
- landing-cta: 모바일 = 하단 고정 전폭 버튼 2개 세로 "회원가입" · "로그인", 데스크톱 = 히어로 글 열 두 버튼 나란히 "회원가입하고 시작하기" · "로그인"(그대로)
- button-primary: landing-cta · web-header · cta-band "회원가입"(#141414 채움, #ffffff 글자, rounded 9999, 높이 44 이상. #141414 띠 안 cta-band에서는 반전 — #ffffff 채움 + #141414 라벨). 하늘색 없음
- button-outline: landing-cta · web-header "로그인", cta-band "둘러보기"(#141414 띠 안에서는 #ffffff 테두리·라벨). 하늘색 없음
- guest-entry: button-pill-soft "둘러보기 ›" 1개(→ 둘러보기 13). 하늘색: › 아이콘 #2b9fe0
- button-pill-soft: guest-entry "둘러보기 ›"
- landing-tabs: 데스크톱 전용. 탭 5개 "시약 목록 · 사용 기록 · 재주문 알림 · QR 찾기 · 학교별 분리", 활성 밑줄 2px #2b9fe0, 스크롤 시 web-header 아래 고정(그대로)
- feature-card: 모바일 = 기능 카드 4장(그대로, ④에 예시 badge-low-stock), 데스크톱 = 문제 공감 3장(그대로). 하늘색: 아이콘만
- badge-low-stock: 모바일 feature-card ④ 예시 배지, 데스크톱 product-shot · landing-section ① · ③ 조각 안 재고 부족 표시. 핑크는 이 배지 안에서만. 새 shot-4 조각에는 없음
- data-table: 데스크톱 전용. product-shot 겹친 카드, landing-section ① 조각, ② 조각 ⓐ 안 승인 표(누름 동작 없음)
- landing-section: 데스크톱 전용 4개(위치·문구 그대로). ② "사용 기록"만 조각 ⓑ 교체 — 위 "landing-section ② 새 조각" 그대로. ① 시약 목록 = 2-desktop data-table + 2-filter 필터 패널, ③ 재주문 알림 = 6-desktop 알림 행 + 3-desktop 재주문 기준 행, ④ QR 찾기 = 11-desktop 배치도 + 12-result 결과 드로어(그대로). 하늘색: 글머리 점 · › 아이콘
- step-flow: 데스크톱 전용(그대로). 번호 원 5개 + 카드 1장(STEP 1 / 5 학교 선택 + shot-14 조각, school-select-* 이름 없음). #141414 반전 띠
- segmented-control: 데스크톱 전용. 대상 탭 "교사 · 학생 · 관리자"(활성 = 교사, 그대로)
- segmented-control-active: "교사" 흰 pill. 하늘색: 1px #2b9fe0 테두리
- cta-band: 데스크톱 전용(그대로). #141414 반전 띠, 제목 "우리 학교 시약장, 오늘 시작해요"(40) + "회원가입" · "둘러보기"
- web-footer: 데스크톱 전용(그대로). 위 1px #f0f0f0 선, 가운데 한 줄 caption #707070 "© 2026 사이음(sci_eum). 과학의 사이, 사람을 잇다."
### 반영한 레퍼런스
- https://uibowl.io/website/%EC%9C%84%EC%8B%9C%EC%BC%93?patterns=%EB%A9%94%EC%9D%B8
- https://uibowl.io/website/%ED%94%BC%EC%B2%98%EB%A7%81?patterns=%EB%9E%9C%EB%94%A9%ED%8E%98%EC%9D%B4%EC%A7%80&imgId=cmuz1dxh50003jp045amg9m8u
- https://uibowl.io/website/%EB%A6%AC%EC%8A%A4%EB%8B%9D%EB%A7%88%EC%9D%B8%EB%93%9C?patterns=%EB%9E%9C%EB%94%A9%ED%8E%98%EC%9D%B4%EC%A7%80&imgId=cmsssa2md000vl404rq691ip5

## 화면 17
센서(새 화면). 무선 센서·현미경 보유 관리만 — 측정값·대여 없음. 학생·교사·admin 모두(학생은 보기만). 샘플고등학교 센서만(N1). 진입: 데스크톱 sidebar-item "센서"(모든 역할), 모바일 '시약' 탭 안 inventory-switch "센서". 홈 sensor-alert-tile에서 오면 상태 필터(고장·점검 필요)가 걸린 채 열린다. 행을 누르면 상세(상태 화면 17-detail), "센서 등록"은 폼(17-form), 0개면 17-empty, "선택"은 17-select.
예시 상태(17-mobile · 17-desktop, 키스크린 17-desktop): 공통 예시 데이터의 센서 7개, 필터 없음, 이름순. 데스크톱 프레임은 교사 기준, 드로어 닫힘.
모바일 활성 탭: "시약". 위→아래: nav-pill → inventory-switch("센서" 선택) → 페이지 머리 줄(왼쪽 heading-4 "센서 7개" + 오른쪽 (교사·admin) list-select-toggle · sensor-add) → 검색 줄(text-input + list-filter-button) → sensor-list(sensor-row 카드 7장, 사이 12) → tab-bar. 좌우 여백 16.
데스크톱 배치: app-sidebar("센서" 현재) | 본문 = 페이지 머리(왼쪽 heading-2 "센서" + caption "7개" / 오른쪽 검색 text-input 폭 320 + list-filter-button + (교사·admin) list-select-toggle + (교사·admin) sensor-add) → sensor-list = data-table(열 이름 · 종류 · 회사 · 모델 · 수량 · 보관 위치 · 상태, 7행) → 행을 누르면 오른쪽 detail-drawer.
### 구성 요소
- app-sidebar: 데스크톱 전용. 공통 규격, 워드마크 + 학교명 "샘플고등학교" + 역할별 메뉴 + 이름·역할·nav-account-menu
- sidebar-item: 데스크톱 전용. 학생 6개 / 교사 9개 / admin 11개. 현재 = "센서"("시약" 바로 아래, #e6f4fc 채움 + #2b9fe0 아이콘, 라벨 #141414), "QR 찾기" 비활성 '준비 중'
- nav-pill: 모바일 전용. "Lab_Stock" 워드마크 + 현재 학교명 "샘플고등학교" + nav-account-menu ▾. 학교 전환 없음
- nav-account-menu: 모바일 = 학교명 옆 ▾, 데스크톱 = app-sidebar 맨 아래. "로그아웃" 1개. 하늘색 없음
- inventory-switch: 모바일 전용. nav-pill 바로 아래 전폭 segmented-control "시약 | 센서", "센서" 선택(흰 pill). "시약"을 누르면 화면 2. 마지막 고른 쪽 기억. 하늘색: 선택 칸 1px #2b9fe0 테두리(글자 #141414)
- segmented-control: inventory-switch 트랙(#f3f3f3, rounded 9999)
- segmented-control-active: inventory-switch "센서" 흰 pill. 하늘색: 1px #2b9fe0 테두리
- sensor-list: 센서 목록 1개. 머리 "센서 7개". 모바일 = sensor-row 카드 세로 쌓기(사이 12). 데스크톱 = data-table(아래). 이름순 기본. 검색은 이름·모델
- sensor-row: 센서 1개. 모바일 = 카드(#f3f3f3, rounded 16, 여백 16): 1줄 이름(title #141414) + 오른쪽 위 sensor-status-badge / 2줄 caption #707070 "온도 · 버니어 · GDX-TMP"(모델 없으면 "운동(거리) · 파스코"처럼 있는 것만) / 3줄 body-sm #141414 "3개 · 과학실 뒤 선반"(시약장 칸이면 cabinet-number 원 + "1번 시약장 · 좌 1단"). 누르면 상세(17-detail). 데스크톱 = data-table 한 행: 이름(title) · 종류 · 회사 · 모델("—" #adadad) · 수량 "3개" · 보관 위치 · 상태(sensor-status-badge). 하늘색: 모바일 › 아이콘 #2b9fe0, 누른 행 #e6f4fc
- sensor-status-badge: 상태 배지(무채색). 고장 = #141414 채움 pill + #ffffff label "고장", 점검 필요 = #f3f3f3 pill(카드 위에서는 #ffffff 채움 + 1px #e0e0e0 테두리로 구분) + #141414 label "점검 필요", 정상 = 채움 없이 label #707070 "정상". rounded 9999. 예시 = 운동 센서 고장 · 무선 pH 센서 점검 필요 · 나머지 정상. 핑크·하늘색 없음
- data-table: 데스크톱 전용. sensor-list 표 — 열 = 이름(정렬, 활성 ↑ #2b9fe0) · 종류 · 회사 · 모델 · 수량(정렬) · 보관 위치 · 상태(정렬). 7행, 행 = sensor-row. 행 hover #f3f3f3, 선택 행 #e6f4fc. rounded 16 컨테이너, 1px #f0f0f0. 선택 모드가 아니면 체크 열 없음
- ex-data-table-cell: data-table 머리행(caption #707070)·셀(body-sm) chrome, 행 구분 1px #f0f0f0
- text-input: 검색 "센서 이름·모델 검색"(#f0f0f0, rounded 16, 포커스 링 2px #141414). 모바일 = 검색 줄 왼쪽, 데스크톱 = 머리 오른쪽 폭 320. 하늘색: 검색 아이콘 #2b9fe0
- list-filter-button: 검색 오른쪽 button-pill-soft "필터"(필터 아이콘, 높이 44 이상). 적용 개수 pill(#e6f4fc 채움 + 1px #2b9fe0 테두리, label #141414)은 이 프레임 숨김. 하늘색: 필터 아이콘 #2b9fe0
- list-filter-sheet: 센서 필터(이 프레임 닫힘). 모바일 = tab-bar 위 바텀시트, 데스크톱 = 버튼 아래 드롭다운 패널(폭 400, rounded 24, 1px #e0e0e0). 순서 = 종류 chip 여러 개(14종) → 회사 chip 여러 개(목록에 있는 회사만) → 상태 3개(정상 · 점검 필요 · 고장) → button-outline "초기화" + button-primary "{N}개 보기". 고른 chip = #e6f4fc + 1px #2b9fe0 테두리(글자 #141414)
- list-select-toggle: 선택 모드 진입. 모바일 = 머리 줄 오른쪽 button-pill-soft "선택"(sensor-add 왼쪽, 사이 8), 데스크톱 = list-filter-button 오른쪽 button-outline "선택". 누르면 17-select. 핑크 없음 (교사·admin만)
- sensor-add: button-primary "센서 등록"(#141414 채움, #ffffff 글자, rounded 9999, 높이 44 이상). 모바일 = 머리 줄 맨 오른쪽 작은 pill(왼쪽 + 아이콘, 라벨 "등록"), 데스크톱 = 페이지 머리 맨 오른쪽 "센서 등록". 누르면 sensor-form(17-form, 모바일 전용 화면 / 데스크톱 detail-drawer). 하늘색 없음 (교사·admin만)
- detail-drawer: 데스크톱 전용. 센서 상세·등록·수정 자리(이 프레임 닫힘). 폭 480, #ffffff, 왼쪽 1px #f0f0f0 선, × 닫기
- button-pill-soft: 모바일 list-select-toggle "선택"(교사·admin만), list-filter-button "필터"
- button-outline: 데스크톱 list-select-toggle "선택" (교사·admin만)
- button-primary: sensor-add "센서 등록" (교사·admin만)
- ex-empty-state-card: 검색·필터 결과 0건 "조건에 맞는 센서가 없어요" + button-outline "필터 지우기"(이 프레임 숨김), 센서 0개는 17-empty. 핑크 없음
- tab-bar: 모바일 전용 하단 탭바 1개(공통 규격). 데스크톱에는 두지 않는다. 하늘색: 활성 tab-item 아이콘 #2b9fe0만
- tab-item: "홈" · "시약" · "QR 스캔" · "기록" 4개. 활성 = "시약"(센서는 시약 탭 안), "QR 스캔" 회색 '준비 중', 나머지 2개 #707070
### 반영한 레퍼런스
- https://uibowl.io/name/Kia?patterns=%EB%82%B4%EC%97%AD&imgId=cmpuohezz0015k104h5xybl51
- https://uibowl.io/name/%EC%BD%94%EC%9B%A8%EC%9D%B4%20IoCare%2B?patterns=%EB%A9%94%EC%9D%B8

## 상태 화면 17-detail
센서 상세(프레임 17-detail-mobile · 17-detail-desktop). 모든 역할이 보고, 수정·삭제는 교사·admin만. 하나 삭제 = 머리 ⋯ → "센서 삭제" → 확인 모달(시약 삭제와 같은 모양, "목록과 홈에서 사라져요") → ex-toast "센서를 삭제했어요" → 화면 17. 되돌리기 없음.
예시 상태: 교사 김OO, "무선 pH 센서"(점검 필요). 항목 — 종류 pH · 회사 버니어 · 모델 GDX-PH · 수량 2개 · 보관 위치 1번 시약장 · 좌 1단 · 메모 "전극 보관액 교체 필요" · 등록일 2026-09-02.
모바일 활성 탭: "시약". 위→아래: nav-pill(뒤로가기 + "센서 상세" + 학교명) → sensor-detail(제목 + 배지, 오른쪽 위 ⋯ → 항목 | 값 행) → 하단 고정 sensor-edit(tab-bar 바로 위) → tab-bar.
데스크톱 배치: app-sidebar("센서" 현재) | 본문 = 화면 17 sensor-list data-table("무선 pH 센서" 행 #e6f4fc 선택) + 오른쪽 detail-drawer 480(머리 = (교사·admin) ⋯ + × → sensor-detail → 아래 고정 sensor-edit).
### 구성 요소
- app-sidebar: 데스크톱 전용. 공통 규격, 학교명 "샘플고등학교" + 역할별 메뉴 + nav-account-menu
- sidebar-item: 데스크톱 전용. 학생 6개 / 교사 9개 / admin 11개. 현재 = "센서"
- nav-pill: 모바일 전용. 뒤로가기(화면 17) + 제목 "센서 상세" + 현재 학교명 "샘플고등학교" + nav-account-menu ▾. 하늘색: 뒤로가기 아이콘 #2b9fe0
- nav-account-menu: 닫힌 ▾
- data-table: 데스크톱 전용. 드로어 뒤 화면 17 센서 표, 선택 행 "무선 pH 센서" #e6f4fc
- sensor-row: 데스크톱 전용. 드로어 뒤 표의 행들(화면 17과 같음)
- detail-drawer: 데스크톱 전용. 폭 480, 높이 900, #ffffff, 왼쪽 1px #f0f0f0 선, 여백 24, 딤 없음. 머리 오른쪽 = (교사·admin) sensor-delete ⋯ 버튼 + × 닫기(각 누름 영역 44 이상, 사이 8). 안 = sensor-detail, 아래 고정 줄(위 1px #f0f0f0 선) = (교사·admin) sensor-edit. 하늘색: × 아이콘 #2b9fe0
- sensor-detail: 센서 상세 본문. 모바일 = 전용 화면(좌우 여백 16), 데스크톱 = detail-drawer 안. 위→아래: heading-3 "무선 pH 센서" + 오른쪽 sensor-status-badge → "항목 | 값" 2열 행(행 사이 1px #f0f0f0, 항목 caption #707070 · 값 body #141414): 종류 "pH" · 회사 "버니어" · 모델 "GDX-PH" · 수량 "2개" · 보관 위치 "cabinet-number(1) 1번 시약장 · 좌 1단" · 메모 "전극 보관액 교체 필요" · 등록일 "2026-09-02". 측정값·대여 행 없음. 학생은 행만 보이고 ⋯·수정 없음. 하늘색 없음
- sensor-status-badge: 제목 오른쪽 "점검 필요"(#f3f3f3 pill + #141414 label, rounded 9999). 핑크·하늘색 없음
- sensor-edit: button-outline "수정"(#ffffff, 1px #e0e0e0, 라벨 #141414, rounded 9999, 높이 44 이상). 모바일 = tab-bar 바로 위 고정 바(#ffffff, 위 1px #f0f0f0, 여백 12·16) 안 전폭, 데스크톱 = 드로어 아래 고정 줄 전폭. 누르면 값이 채워진 sensor-form(제목 "센서 수정"). 하늘색 없음 (교사·admin만)
- sensor-delete: 머리 ⋯ 아이콘 버튼(#141414, 채움 없음, 누름 영역 44 이상 — 모바일 sensor-detail 제목 줄 오른쪽 끝, 데스크톱 드로어 머리 × 왼쪽)과 그 메뉴(#ffffff, rounded 24, 1px #f0f0f0, 여백 8, 그림자 없음)의 항목 "센서 삭제"(body #141414, 휴지통 아이콘 #141414, 높이 44). 이 프레임에서는 메뉴 닫힘(⋯만). 누르면 ex-modal-card: heading-3 "'무선 pH 센서'를 삭제할까요?" · body "목록과 홈에서 사라져요." · body-sm #707070 "되돌릴 수 없어요." · button-outline "취소" + button-primary "삭제"(검정). 핑크 없음. 하늘색: ⋯ 누른 동안 버튼 뒤 #e6f4fc 원 (교사·admin만)
- ex-modal-card: 센서 삭제 확인(이 프레임에는 그리지 않음, 위 sensor-delete 문구) (교사·admin만)
- button-outline: sensor-edit "수정" (교사·admin만)
- ex-toast: 삭제 뒤 "센서를 삭제했어요", 수정 저장 뒤 "센서 정보를 바꿨어요"(이 프레임에는 그리지 않음). 하늘색: 완료 체크 아이콘 #2b9fe0 (교사·admin만)
- tab-bar: 모바일 전용 하단 탭바 1개(공통 규격). 데스크톱에는 두지 않는다
- tab-item: 4개 "홈" · "시약" · "QR 스캔" · "기록". 활성 = "시약", "QR 스캔" 회색 '준비 중'
### 반영한 레퍼런스
- https://uibowl.io/name/%ED%97%A4%EC%9D%B4%EB%94%9C%EB%9F%AC?patterns=%EC%A1%B0%ED%9A%8C%ED%95%98%EA%B8%B0&imgId=cmliqgu3b000ule04taw4hhl7
- https://uibowl.io/name/Kia?patterns=%EB%82%B4%EC%97%AD&imgId=cmpuohezz0015k104h5xybl51

## 상태 화면 17-form
센서 등록 폼(프레임 17-form-mobile · 17-form-desktop, 키스크린 17-form-mobile). 교사·admin만 이 상태에 온다(학생 화면에는 "센서 등록"·"수정"이 없다). 수정도 같은 폼(제목 "센서 수정", 값 채움). "저장" → ex-toast "센서를 등록했어요" → 화면 17(새 행 잠깐 #e6f4fc).
예시 상태: 새 등록 입력 중 — 이름 "무선 온도 센서" · 종류 "온도" 선택 · 회사 "버니어" 선택 · 모델명 "GDX-TMP" · 수량 3 · 보관 위치 "직접 입력" "과학실 뒤 선반" · 상태 "정상"(기본) · 메모 빈 값. 회사 고르기 시트·드롭다운은 닫힘. 저장 활성.
모바일 활성 탭: "시약". 위→아래: nav-pill(× 닫기 + "센서 등록" + 학교명) → sensor-form(이름 → 종류 → 회사 → 모델명 → 수량 → 보관 위치 → 상태 → 메모, 칸 사이 16) → 하단 고정 저장 바(tab-bar 바로 위) → tab-bar. 폼은 저장 바 위에서 스크롤. 좌우 여백 16.
데스크톱 배치: app-sidebar("센서" 현재) | 본문 = 화면 17 sensor-list data-table(그대로) + 오른쪽 detail-drawer 480 = 짧은 폼(머리 heading-3 "센서 등록" + × → sensor-form "라벨 위 · 입력 아래" 세로 → 아래 고정 줄 button-primary "저장").
### 구성 요소
- app-sidebar: 데스크톱 전용. 공통 규격, 학교명 "샘플고등학교" + 교사 메뉴 + nav-account-menu (교사·admin만)
- sidebar-item: 데스크톱 전용. 교사 9개 / admin 11개. 현재 = "센서" (교사·admin만)
- nav-pill: 모바일 전용. 왼쪽 × 닫기(화면 17, 입력이 있으면 그대로 닫힘) + 제목 "센서 등록" + 현재 학교명 "샘플고등학교" + nav-account-menu ▾. 하늘색: × 아이콘 #2b9fe0 (교사·admin만)
- nav-account-menu: 닫힌 ▾ (교사·admin만)
- data-table: 데스크톱 전용. 드로어 뒤 화면 17 센서 표(선택 행 없음) (교사·admin만)
- detail-drawer: 데스크톱 전용. 폭 480, 높이 900, #ffffff, 왼쪽 1px #f0f0f0 선, 여백 24, 오른쪽 위 × 닫기. 안 = heading-3 "센서 등록" → sensor-form(안에서 스크롤) → 아래 고정 줄(위 1px #f0f0f0) button-primary "저장" 전폭 (교사·admin만)
- sensor-form: 등록·수정 폼 1개. 칸 순서(라벨 body #141414 위 · 입력 아래, 선택 칸은 라벨 옆 caption #707070 "(선택)"): ① 이름 text-input 값 "무선 온도 센서"(placeholder "예: 무선 온도 센서") ② 종류 sensor-type-select ③ 회사 sensor-maker-select ④ 모델명 (선택) text-input 값 "GDX-TMP" ⑤ 수량 숫자 text-input 값 "3" + 오른쪽 caption #707070 "개" ⑥ 보관 위치 segmented-control "직접 입력 | 시약장 칸"(기본 직접 입력, 예시 직접 입력) + 아래 text-input 값 "과학실 뒤 선반"("시약장 칸"을 고르면 그 자리에 location-picker 진입 버튼 — 승인본 위치 고르기 재사용) ⑦ 상태 segmented-control 3칸 "정상 · 점검 필요 · 고장"(기본 정상) ⑧ 메모 (선택) text-input(placeholder "메모 (선택)"). 이름·종류·회사·수량이 비면 저장 비활성. 측정값·대여 칸 없음. 핑크 없음 (교사·admin만)
- sensor-type-select: 종류 chip 하나 고르기 — 14개 "온도 · pH · 힘 · 운동(거리) · 전압 · 전류 · 조도 · 압력 · CO₂ · 산소 · 습도 · 소리 · 심박 · 기타", 줄바꿈 chip 묶음(사이 8). 미선택 = #f3f3f3 pill + label #141414(rounded 9999, 높이 44 이상), 선택 = #e6f4fc 채움 + 1px #2b9fe0 테두리(글자 #141414). 예시 = "온도" 선택. 하늘색: 선택 chip (교사·admin만)
- sensor-maker-select: 회사 고르기 칸(text-input 모양 #f0f0f0, rounded 16, 값 "버니어", 오른쪽 ▾). 누르면 모바일 = tab-bar 위 바텀시트(× 닫기, 제목 "회사 선택"), 데스크톱 = 칸 아래 드롭다운(#ffffff, 1px #e0e0e0, rounded 24, 칸과 같은 폭, 최대 높이 360 안 스크롤): 맨 위 검색 text-input "회사 검색" → 묶음 제목 caption #707070 "센서" + 14개(버니어 · 사이언스큐브 · 이지메이커 · 고릴라셀 · 파스코 · 동원 · 브로콜리 · 플로우랩 · 이티보드 · 포켓랩 · 헥사보드 · 뉴로그 · 아텍 · 코드위즈) → "현미경" + 5개(오선하이테크 · 씨앤에스에듀 · 오맥스 · 한국과학 · 마르시스에듀) → 맨 끝 "직접 입력"(고르면 칸이 text-input으로 바뀜). 행 높이 44 이상, 고른 항목 #e6f4fc + 오른쪽 #2b9fe0 체크(글자 #141414). 이 프레임에서는 닫힘(칸에 "버니어"). 하늘색: ▾ 아이콘, 고른 행 (교사·admin만)
- segmented-control: 보관 위치 "직접 입력 | 시약장 칸", 상태 "정상 · 점검 필요 · 고장"(#f3f3f3 트랙, rounded 9999). 상태 칸에 핑크·검정 채움 없음(배지와 달리 고르기 컨트롤) (교사·admin만)
- segmented-control-active: "직접 입력", "정상" 흰 pill. 하늘색: 1px #2b9fe0 테두리(글자 #141414) (교사·admin만)
- text-input: 이름 · 모델명 · 수량 · 보관 위치 직접 입력 · 메모, 회사 검색(#f0f0f0, rounded 16, 포커스 링 2px #141414) (교사·admin만)
- location-picker: 보관 위치 "시약장 칸"을 고를 때 여는 승인본 위치 고르기(cabinet-switcher + 칸 격자, 데스크톱 팝오버 / 모바일 바텀시트). 이 프레임은 "직접 입력"이라 닫힘 (교사·admin만)
- button-primary: "저장"(#141414 채움, #ffffff 글자, rounded 9999, 높이 44 이상). 모바일 = tab-bar 바로 위 고정 바(#ffffff, 위 1px #f0f0f0, 여백 12·16) 안 전폭, 데스크톱 = 드로어 아래 고정 줄 전폭. 예시 = 활성. 하늘색 없음 (교사·admin만)
- ex-toast: 저장 뒤 "센서를 등록했어요"(이 프레임에는 그리지 않음). 하늘색: 완료 체크 아이콘 #2b9fe0 (교사·admin만)
- tab-bar: 모바일 전용 하단 탭바 1개(공통 규격). 저장 바·회사 시트는 이 바 위. 데스크톱에는 두지 않는다 (교사·admin만)
- tab-item: 4개 "홈" · "시약" · "QR 스캔" · "기록". 활성 = "시약", "QR 스캔" 회색 '준비 중' (교사·admin만)
### 반영한 레퍼런스
- https://uibowl.io/name/%EC%99%93%EC%84%AD?patterns=%ED%8E%B8%EC%A7%91%C2%B7%EC%88%98%EC%A0%95%ED%95%98%EA%B8%B0&imgId=cmqt8b6x80014kz040po6xf03
- https://uibowl.io/name/%ED%97%A4%EC%9D%B4%EB%94%9C%EB%9F%AC?patterns=%EC%A1%B0%ED%9A%8C%ED%95%98%EA%B8%B0&imgId=cmliqgu3b000ule04taw4hhl7

## 상태 화면 17-empty
센서 0개(프레임 17-empty-mobile · 17-empty-desktop, 교사 기준). 학생은 같은 카드에서 sensor-add 없이 글만 본다. 핑크 없음.
모바일 활성 탭: "시약". 위→아래: nav-pill → inventory-switch("센서" 선택) → 머리 heading-4 "센서 0개" → 본문 가운데 ex-empty-state-card(안에 sensor-add) → tab-bar. 검색·필터·선택은 0개라 숨김.
데스크톱 배치: app-sidebar("센서" 현재) | 본문 = 페이지 머리(왼쪽 heading-2 "센서" + caption "0개", 오른쪽 비움) → 본문 가운데 ex-empty-state-card 폭 440(안에 sensor-add).
### 구성 요소
- app-sidebar: 데스크톱 전용. 공통 규격, 학교명 "샘플고등학교" + 역할별 메뉴 + nav-account-menu
- sidebar-item: 데스크톱 전용. 학생 6개 / 교사 9개 / admin 11개. 현재 = "센서"
- nav-pill: 모바일 전용. "Lab_Stock" 워드마크 + 현재 학교명 "샘플고등학교" + nav-account-menu ▾
- nav-account-menu: 닫힌 ▾
- inventory-switch: 모바일 전용. "시약 | 센서", "센서" 선택. 하늘색: 선택 칸 1px #2b9fe0 테두리
- segmented-control: inventory-switch 트랙
- segmented-control-active: "센서" 흰 pill. 하늘색: 1px #2b9fe0 테두리
- ex-empty-state-card: 빈 상태 카드 1개(#ffffff, 1px #f0f0f0 테두리, rounded 24, 여백 24, 가운데 정렬). #141414 센서 아이콘 → heading-4 "아직 등록한 센서가 없어요" → body-sm #707070 "무선 센서와 현미경을 등록해 두면 수량과 상태를 한눈에 봐요" → (교사·admin) 위 간격 24 sensor-add. 학생은 버튼 없이 글까지만. 핑크·하늘색 없음(아이콘 #141414)
- sensor-add: 카드 안 button-primary "센서 등록"(#141414 채움, #ffffff 글자, rounded 9999, 높이 44 이상; 모바일 = 카드 안 전폭) → 17-form. 하늘색 없음 (교사·admin만)
- button-primary: sensor-add "센서 등록" (교사·admin만)
- tab-bar: 모바일 전용 하단 탭바 1개(공통 규격). 데스크톱에는 두지 않는다
- tab-item: 4개 "홈" · "시약" · "QR 스캔" · "기록". 활성 = "시약", "QR 스캔" 회색 '준비 중'
### 반영한 레퍼런스
- https://uibowl.io/name/%EC%A7%81%EB%B0%A9%20%EC%8A%A4%EB%A7%88%ED%8A%B8%EB%8F%84%EC%96%B4%EB%9D%BD?patterns=%EC%8B%A0%EC%B2%AD%ED%95%98%EA%B8%B0&imgId=cmco48dn3000bkz07v19ohvuw
- https://uibowl.io/name/%EC%BD%94%EC%9B%A8%EC%9D%B4%20IoCare%2B?patterns=%EB%A9%94%EC%9D%B8

## 상태 화면 17-select
센서 선택 모드(프레임 17-select-mobile · 17-select-desktop). 교사·admin만. 2-select와 같은 규칙 — 행을 누르면 체크, 전체 선택 = 지금 필터·검색 결과(최대 100개), 1개 이상이면 bulk-action-bar → "삭제" → ex-modal-card "센서 2개를 삭제할까요?" · "운동 센서, 무선 pH 센서" · "목록과 홈에서 사라져요." · muted "되돌릴 수 없어요." · "취소" / 검정 "삭제" → ex-toast "센서 2개를 삭제했어요", 목록 그대로, 선택 모드 끝. 핑크 없음.
예시 상태: 교사 김OO, 7개 중 2개 선택 — 운동 센서(고장) · 무선 pH 센서(점검 필요). 확인 모달은 닫힘.
모바일 활성 탭: "시약". 위→아래: nav-pill → inventory-switch("센서") → 선택 머리 줄("취소" · "2개 선택됨" · "전체 선택") → 검색 줄 → sensor-row 카드(왼쪽 select-checkbox) → bulk-action-bar(tab-bar 바로 위) → tab-bar.
데스크톱 배치: app-sidebar("센서" 현재) | 본문 = 페이지 머리(왼쪽 "센서" + "2개 선택됨" / 오른쪽 검색 + list-filter-button + list-select-toggle "취소", sensor-add 숨김) → data-table(첫 열 select-checkbox, 머리 칸 = 전체 선택, 고른 2행 #e6f4fc) → 본문 아래 고정 bulk-action-bar.
### 구성 요소
- app-sidebar: 데스크톱 전용. 공통 규격, 학교명 "샘플고등학교" + 교사 메뉴 + nav-account-menu (교사·admin만)
- sidebar-item: 데스크톱 전용. 교사 9개 / admin 11개. 현재 = "센서" (교사·admin만)
- nav-pill: 모바일 전용. "Lab_Stock" 워드마크 + 현재 학교명 "샘플고등학교" + nav-account-menu ▾ (교사·admin만)
- nav-account-menu: 닫힌 ▾ (교사·admin만)
- inventory-switch: 모바일 전용. "시약 | 센서", "센서" 선택 (교사·admin만)
- list-select-toggle: 선택 모드 머리. 모바일 = 머리 줄이 "취소"(조용한 텍스트 동작) · title "2개 선택됨" · "전체 선택"으로 바뀜, 데스크톱 = button-outline "선택"이 "취소"로 바뀌고 제목 옆 "2개 선택됨". 핑크·하늘색 없음 (교사·admin만)
- select-checkbox: 20px 원(rounded 9999). 안 고름 = #ffffff + 1px #adadad, 고름 = #2b9fe0 채움 + #ffffff 체크. 모바일 = sensor-row 카드 왼쪽(누름 영역 44 이상), 데스크톱 = data-table 첫 열 + 머리 칸(일부 선택 = #2b9fe0 채움 + 흰 가로줄). 하늘색: 고른 체크 원 (교사·admin만)
- sensor-list: 선택 모드 목록(모바일 카드 / 데스크톱 표) (교사·admin만)
- sensor-row: 선택 모드 행 = 왼쪽 select-checkbox + 이름·종류·회사·수량·위치(화면 17과 같음), › 숨김. 고른 행 #e6f4fc(안 고른 행 모바일 #f3f3f3). 행을 누르면 체크가 바뀜 (교사·admin만)
- sensor-status-badge: 행 안 배지 그대로(운동 센서 "고장" #141414 채움 + #ffffff label, 무선 pH 센서 "점검 필요", 나머지 "정상" #707070). 고른 행에서도 무채색 (교사·admin만)
- data-table: 데스크톱 전용. 화면 17 표 + 맨 앞 select-checkbox 열(폭 48), 고른 2행 #e6f4fc (교사·admin만)
- text-input: 검색 "센서 이름·모델 검색" (교사·admin만)
- list-filter-button: "필터" (교사·admin만)
- bulk-action-bar: 띠 1개. #ffffff + 위 1px #f0f0f0 선, rounded 0, 여백 12·16. 왼쪽 title "2개 선택됨", 오른쪽 button-primary "삭제"(검정). 모바일 = tab-bar 바로 위 전폭, 데스크톱 = 본문 아래 고정. 핑크·하늘색 없음 (교사·admin만)
- button-primary: bulk-action-bar "삭제"(#141414 채움, #ffffff 글자, rounded 9999, 높이 44 이상) → 확인 ex-modal-card (교사·admin만)
- button-outline: 데스크톱 list-select-toggle "취소" (교사·admin만)
- ex-modal-card: "삭제"를 누르면 여는 확인(이 프레임에는 그리지 않음, 위 문구 — 2-bulk-delete와 같은 모양) (교사·admin만)
- tab-bar: 모바일 전용 하단 탭바 1개(공통 규격). bulk-action-bar는 이 바 위. 데스크톱에는 두지 않는다 (교사·admin만)
- tab-item: 4개 "홈" · "시약" · "QR 스캔" · "기록". 활성 = "시약", "QR 스캔" 회색 '준비 중' (교사·admin만)
### 반영한 레퍼런스
- https://uibowl.io/name/Kia?patterns=%EB%82%B4%EC%97%AD&imgId=cmpuohezz0015k104h5xybl51
- https://uibowl.io/name/%EB%9D%BC%EC%9A%B4%EC%A6%88?patterns=%EC%9E%A5%EB%B0%94%EA%B5%AC%EB%8B%88&imgId=cmunlyn8s0005l804bcsbpzcr

## 역할별 노출
앱 전체(로그인 후 화면) 기준 개수. runs/20261010-1340 표를 기준으로 이번 변경을 반영했다. 같은 화면의 상태 화면·모바일·데스크톱에 다시 나오는 같은 컴포넌트는 그 화면 1개로 센다(예: 화면 17의 sensor-add는 목록 머리·17-empty 카드에 나와도 1).
이번 변경(교사·admin만, 학생 0 — R5):
- list-select-toggle = 화면 2 1 + 화면 17 1 → 2. select-checkbox = 화면 2(2-select) 1 + 화면 17(17-select) 1 → 2. bulk-action-bar = 화면 2 1 + 화면 17 1 → 2.
- sensor-add = 화면 17 1. sensor-edit = 화면 17(17-detail) 1. sensor-delete = 화면 17(17-detail) 1. sensor-alert-tile = 화면 13 1(고장·점검 필요 ≥ 1일 때만).
- 학생: 화면 2·17에 "선택"·체크·삭제 띠 없음, 화면 17에 "센서 등록"·"수정"·⋯ 없음(17-empty는 글만), 홈에 센서 타일 없음 → 모두 0.
화면 10 record-add, 화면 17 sensor-list·sensor-row·sensor-status-badge·sensor-detail·inventory-switch, signup-error-summary, 404 카드는 모든 역할에 같거나 로그인 전이라 rules.json roles 대상이 아니어서 표에 넣지 않는다. 화면 15는 로그인 전이라 표의 컴포넌트를 담지 않는다(shot-* 묶음). msds-entry = 화면 3 1 + 화면 10 상세 1(학생·교사·admin 모두 2, R4). 나머지 행은 runs/20261010-1340 값 그대로.

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
| reagent-more-menu | 0 | 1 | 1 |
| reagent-delete | 0 | 1 | 1 |
| list-select-toggle | 0 | 2 | 2 |
| select-checkbox | 0 | 2 | 2 |
| bulk-action-bar | 0 | 2 | 2 |
| sensor-add | 0 | 1 | 1 |
| sensor-edit | 0 | 1 | 1 |
| sensor-delete | 0 | 1 | 1 |
| sensor-alert-tile | 0 | 1 | 1 |
