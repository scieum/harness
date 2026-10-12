# S2 설계 — run 20261012-1155

대상 화면: 17 (센서) + 상태 화면 17-type · 17-filter · 학교: 샘플고등학교 (input.json) · 키스크린: 17-type-mobile, 17-filter-mobile
변경 사유: 요청 8 후속 (2026-10-12, rules.json 1.28) — 센서 종류 27종을 sensor-type-group 4줄(물리 12 · 화학 9 · 생명·지구 3 · 장비 3)로 접어 둔다. ① 종류 시트(17-type) = 검색 아래 묶음 4줄, 기본 접힘, 누른 묶음만 펼침, 이미 고른 종류의 묶음은 처음부터 펼침 ② 필터 시트(17-filter) = 종류 구역도 같은 접힘 묶음 4줄(검색 없음), 묶음 줄에 고른 개수 "화학 · 2개", 고른 게 있는 묶음은 처음부터 펼침 → 회사 → 상태. 27종을 한꺼번에 펼쳐 두지 않는다.
근거: docs/PRD.md §7(17), docs/story-service.md 결정 사항 "센서 (화면 17)"·"센서 종류·카탈로그·서류로 등록", docs/design.md "Sensors"(sensor-type-select · sensor-type-sheet · sensor-type-group, Filter sheet)·"List filter"·"Desktop shell", harness/rules.json 1.28(sensor.type_select · sensor.filter · sensor.type_groups, variants 17.type·17.filter, screens_required 17, desktop_shell, tab_bar, mobile_menu, roles R1~R7, never.N1·N2), research/s1-adopt.md, 오케스트레이터 결정(2026-10-12: 폼·필터 시트 상태 ☰ 없음, 17 기본 모바일 ☰ 있음, 17-type 예시 = 화학만 펼침·편광 고름, 17-filter 예시 = '화학 · 2개' 펼침·pH·전도도 고름).
기준 설계(틀): input.json base — 화면 17·17-type = runs/20261012-0939 승인 S4 프레임(설계 = runs/20261012-0939/spec/s2-spec.md 화면 17·상태 화면 17-type). 승인본 구성은 그대로 두고 이번 묶음 접힘만 바꾼다. 17-filter는 화면 17 승인본 위에 list-filter-sheet를 연 상태.

색·폰트·모서리·간격은 docs/design.md와 harness/rules.json을 따른다. 허용 색 밖의 값(딤 반투명 검정 등)은 쓰지 않는다. 그림자는 쓰지 않는다(segmented-control-active 예외). 떠 있는 버튼(FAB)은 두지 않는다.
- 핑크 #d6246a·연핑크 #fbe9f0는 이번 대상(화면 17·17-type·17-filter)에 쓰지 않는다 — 센서 종류·필터·상태 배지는 재고 부족 신호가 아니다.
- 하늘색 #2b9fe0·옅은 하늘색 #e6f4fc는 선택·현재 위치·아이콘·체크에만 쓴다. 글자색 금지(그 위 글자 #141414). button-primary 안에는 쓰지 않는다. 센서 상태 배지에도 쓰지 않는다. 묶음 줄의 ▸/▾ 표시는 #707070(하늘색 아님), 고른 chip만 #e6f4fc + 1px #2b9fe0.
- sensor-status-badge는 무채색만: 고장 = #141414 채움 pill + #ffffff label, 점검 필요 = #f3f3f3 pill + #141414 label, 정상 = 채움 없이 #707070 글자 "정상".
학교 선택은 회원가입(화면 14)에만 있다. 화면 17과 상태 화면 17-type·17-filter에는 학교 선택·전환을 두지 않고 현재 학교명 "샘플고등학교"를 모바일은 nav-pill 안, 데스크톱은 app-sidebar 맨 위에 표시한다. 센서 목록·필터 결과는 모두 샘플고등학교 것만 보인다(N1).
외부 서비스 연결 값은 서버에서만 다룬다. 어떤 화면에도 연결 값 입력 칸·외부 서비스 설정·AI 엔진 선택 UI·관련 문구를 두지 않는다(N2). 센서 종류 27종·묶음은 개발 쪽 코드 상수라 관리 화면이 없다.
괄호 안 역할 표시가 없는 구성 요소는 그 화면에 들어오는 모든 역할에게 보인다. sensor-add·sensor-doc-add·list-select-toggle은 교사·admin만 — 학생 화면에는 그리지 않는다(R5). 17-type(등록·수정 폼)은 교사·admin만 들어온다. 17-filter는 모든 역할(학생은 머리에 "선택"·"서류로 등록"·"센서 등록"/"등록" 없음).

모바일 공통(승인본 그대로): tab-bar는 화면 아래 가장자리 y 780~844(폭 390, 높이 64, rounded 0, #ffffff + 위쪽 1px #f0f0f0 선, 그림자 없음)에 붙고 tab-item 4개("홈"·"시약"·"QR 스캔"·"기록")를 같은 폭으로 채운다. "QR 스캔" tab-item은 화면 12 전까지 회색 — 아이콘·라벨 #adadad + 아이콘 아래 caption "준비 중"(#adadad), 누르면 ex-toast "준비 중이에요". 시트는 tab-bar 위쪽 선 위에 붙는다(딤 없음, 1px #e0e0e0 테두리, 위쪽 rounded 24, 오른쪽 위 × 닫기). 센서는 탭이 아니라 '시약' 탭 안(inventory-switch "시약 | 센서") + 전체 메뉴 "센서". 화면 17·17-type·17-filter 모바일 활성 탭은 "시약".
- nav-pill 두 가지: ① 목록 머리(17 기본) = 맨 왼쪽 mobile-menu-button ☰(44×44, 동그란 아이콘 버튼, 글자 없음, 아이콘 #141414) → "Lab_Stock" 워드마크 → 학교명 + nav-account-menu ▾. ② 폼·시트 상태 머리(17-type · 17-filter) = 맨 왼쪽 × 닫기(17-type) 또는 ‹ 뒤로(17-filter) → 제목 → 학교명 + nav-account-menu ▾. ☰(mobile-menu-button)는 두지 않는다.
데스크톱 공통(1440×900, rules.json desktop_shell): nav-pill·tab-bar·mobile-menu-button 없음.
- app-sidebar: 왼쪽 고정 열 폭 240, 높이 전체, rounded 0, #f3f3f3 채움, 오른쪽 1px #f0f0f0 선. 맨 위 "Lab_Stock" 워드마크 + 학교명 "샘플고등학교"(title #141414, 전환 없음) → sidebar-item 묶음 → 맨 아래 "{이름} · {역할}"(body-sm) + nav-account-menu ▾.
- sidebar-item: 아이콘 + body 라벨, 높이 44, rounded 0. 현재 항목 = #e6f4fc 채움 + #2b9fe0 아이콘, 라벨 #141414. 메뉴(rules.json desktop_shell.menu): 학생 6개(홈·시약·센서·기록·시약장·QR 찾기) / 교사 9개(+ "관리" 입고·실험 매뉴얼·재주문 알림) / admin 11개(+ "학교 설정" 사용자·판매처). "QR 찾기"는 비활성 — 아이콘·라벨 #adadad + caption "준비 중"(#adadad).
- 본문 = 사이드바 오른쪽, 페이지 여백 32. 페이지 머리 = 왼쪽 제목(heading-2) + 개수(caption #707070), 오른쪽 검색·필터·선택·보조·주 버튼. data-table = ex-data-table-cell 머리행(caption #707070)·본문(body-sm), rounded 16 컨테이너 + 1px #f0f0f0 테두리, 선택 행 #e6f4fc. detail-drawer = 오른쪽 폭 480, 높이 전체, #ffffff, 왼쪽 1px #f0f0f0 선, 딤 없음, 오른쪽 위 × 닫기(센서 등록·수정 폼도 드로어).
- 겹침: 모바일 고르기 시트(종류·필터)는 데스크톱에서 그 컨트롤에 붙은 드롭다운·팝오버(#ffffff, 1px #e0e0e0, rounded 24, 그림자·딤 없음).
- sensor-type-group 공통 모양(종류 시트·필터 시트 같은 줄): 묶음 줄 1개 = 높이 52, 전폭, 사각(rounded 0), 채움 없음, 줄 사이 1px #f0f0f0 선. 왼쪽 묶음 이름(title #141414) + 바로 뒤 개수 caption #707070, 오른쪽 끝 ▸(접힘)/▾(펼침) 아이콘 #707070(누름 영역 44 이상, 줄 전체가 누름 영역). 펼치면 줄 바로 아래로 그 묶음 chip이 줄바꿈(chip 사이 8, 위아래 여백 12, 좌우 0). chip = #f3f3f3 pill + label #141414(rounded 9999, 높이 44 이상, 좌우 여백 16), 고른 chip = #e6f4fc 채움 + 1px #2b9fe0 테두리(글자 #141414) + 라벨 오른쪽 작은 #2b9fe0 체크. 여러 묶음을 함께 펼칠 수 있다. 처음 열 때 고른 것이 있는 묶음만 펼침, 나머지는 접힘. 개수 표기: 종류 시트 = 그 묶음 종류 수("물리 12"), 필터 시트 = 고른 개수("화학 · 2개", 0개면 개수 생략 — 이름만).
예시 데이터(공통): 오늘 = 2026-10-12. 데스크톱 프레임 기준 역할 = 교사 "김OO · 교사".
- 센서 7개(이름 · 종류 · 회사 · 모델 · 수량 · 보관 위치 · 상태): 무선 온도 센서 · 온도 · 파스코 · PS-3201 · 3개 · 과학실 뒤 선반 · 정상 / 무선 pH 센서 · pH · 버니어 · GDX-PH · 2개 · 1번 시약장 · 좌 1단 · 점검 필요 / 무선 힘 센서 · 힘 · 파스코 · PS-3202 · 4개 · 과학실 뒤 선반 · 정상 / 운동 센서 · 운동(거리) · 파스코 · PS-3219 · 2개 · 준비실 서랍 · 고장 / 무선 편광계 · 편광 · 파스코 · PS-3237 · 1개 · 준비실 서랍 · 정상 / 전압 센서 · 전압 · 사이언스큐브 · — · 6개 · 준비실 서랍 · 정상 / 디지털 현미경 · 기타 · 오맥스 · — · 2개 · 생물 준비실 · 정상.
- 회사(목록에 있는 회사만): 파스코 · 버니어 · 사이언스큐브 · 오맥스.

## 화면 17
센서. 무선 센서·현미경 보유 관리만 — 측정값·대여 없음. 학생·교사·admin 모두(학생은 보기만). 샘플고등학교 센서만(N1). 승인본(runs/20261012-0939 화면 17) 그대로 + 요청 8 후속: list-filter-sheet의 종류 구역 = sensor-type-group 4줄 접힘(검색 없음, 묶음 줄에 고른 개수, 고른 게 있는 묶음은 처음부터 펼침). 이 프레임에서는 필터 시트가 닫혀 있어 화면 모양은 승인본과 같다.
예시 상태(17-mobile · 17-desktop): 공통 예시 데이터의 센서 7개, 필터 없음, 이름순. 교사 기준, 드로어·등록 시트·필터 시트 닫힘.
모바일 활성 탭: "시약". 위→아래: nav-pill(☰ 포함) → inventory-switch("센서" 선택) → 페이지 머리 줄(왼쪽 heading-4 "센서 7개" + 오른쪽 (교사·admin) list-select-toggle "선택" · sensor-add "등록") → 검색 줄(text-input + list-filter-button) → sensor-list(sensor-row 카드 7장, 사이 12) → tab-bar. 좌우 여백 16.
데스크톱 배치: app-sidebar("센서" 현재) | 본문 = 페이지 머리(왼쪽 heading-2 "센서" + caption "7개" / 오른쪽 검색 text-input 폭 320 + list-filter-button + (교사·admin) list-select-toggle + (교사·admin) sensor-doc-add "서류로 등록" + (교사·admin) sensor-add "센서 등록", 사이 8) → sensor-list = data-table(열 이름 · 종류 · 회사 · 모델 · 수량 · 보관 위치 · 상태, 7행) → 행을 누르면 오른쪽 detail-drawer.
### 구성 요소
- app-sidebar: 데스크톱 전용. 공통 규격, 워드마크 + 학교명 "샘플고등학교" + 역할별 메뉴 + 이름·역할·nav-account-menu
- sidebar-item: 데스크톱 전용. 학생 6개 / 교사 9개 / admin 11개. 현재 = "센서"("시약" 바로 아래), "QR 찾기" 비활성 '준비 중'
- nav-pill: 모바일 전용. mobile-menu-button ☰ + "Lab_Stock" 워드마크 + 현재 학교명 "샘플고등학교" + nav-account-menu ▾. 학교 전환 없음
- mobile-menu-button: 모바일 전용. nav-pill 맨 왼쪽 ☰(44×44, rounded 9999, 채움 없음, 아이콘 #141414, 글자 없음). 시트를 열면 "센서"가 지금 화면(#e6f4fc). 이 프레임에서는 닫힘. 데스크톱에는 두지 않는다
- nav-account-menu: 모바일 = 학교명 옆 ▾, 데스크톱 = app-sidebar 맨 아래. "로그아웃" 1개. 하늘색 없음
- inventory-switch: 모바일 전용. nav-pill 바로 아래 전폭 segmented-control "시약 | 센서", "센서" 선택. "시약"을 누르면 화면 2. 하늘색: 선택 칸 1px #2b9fe0 테두리(글자 #141414)
- segmented-control: inventory-switch 트랙(#f3f3f3, rounded 9999)
- segmented-control-active: inventory-switch "센서" 흰 pill. 하늘색: 1px #2b9fe0 테두리
- sensor-list: 센서 목록 1개. 머리 "센서 7개". 모바일 = sensor-row 카드 세로 쌓기(사이 12). 데스크톱 = data-table. 이름순 기본. 검색은 이름·모델
- sensor-row: 센서 1개. 모바일 = 카드(#f3f3f3, rounded 16, 여백 16): 1줄 이름(title #141414) + 오른쪽 위 sensor-status-badge / 2줄 caption #707070 "온도 · 파스코 · PS-3201"(모델 없으면 "전압 · 사이언스큐브"처럼 있는 것만) / 3줄 body-sm #141414 "3개 · 과학실 뒤 선반"(시약장 칸이면 cabinet-number 원 + "1번 시약장 · 좌 1단"). 데스크톱 = data-table 한 행: 이름(title) · 종류 · 회사 · 모델("—" #adadad) · 수량 · 보관 위치 · 상태. 하늘색: 모바일 › 아이콘 #2b9fe0, 누른 행 #e6f4fc
- sensor-status-badge: 상태 배지(무채색). 고장 = #141414 채움 pill + #ffffff label, 점검 필요 = #f3f3f3 pill(카드 위에서는 #ffffff 채움 + 1px #e0e0e0 테두리) + #141414 label, 정상 = 채움 없이 #707070 "정상". rounded 9999. 예시 = 운동 센서 고장 · 무선 pH 센서 점검 필요 · 나머지 정상. 핑크·하늘색 없음
- cabinet-number: 무선 pH 센서 보관 위치 앞 작은 원 "1"(#ffffff, 1px #e0e0e0, label #141414)
- data-table: 데스크톱 전용. sensor-list 표 — 열 = 이름(정렬, 활성 ↑ #2b9fe0) · 종류 · 회사 · 모델 · 수량(정렬) · 보관 위치 · 상태(정렬). 7행. 행 hover #f3f3f3, 선택 행 #e6f4fc. rounded 16 컨테이너, 1px #f0f0f0
- ex-data-table-cell: data-table 머리행(caption #707070)·셀(body-sm) chrome, 행 구분 1px #f0f0f0
- text-input: 검색 "센서 이름·모델 검색"(#f0f0f0, rounded 16, 포커스 링 2px #141414). 하늘색: 검색 아이콘 #2b9fe0
- list-filter-button: 검색 오른쪽 button-pill-soft "필터"(필터 아이콘, 높이 44 이상). 적용 개수 pill은 이 프레임 숨김(적용 중이면 #e6f4fc 채움 + 1px #2b9fe0 테두리, 글자 #141414). 하늘색: 필터 아이콘 #2b9fe0
- list-filter-sheet: 센서 필터(이 프레임 닫힘 — 연 모양은 상태 화면 17-filter). 모바일 = tab-bar 위 바텀시트, 데스크톱 = 버튼 아래 드롭다운 패널(폭 400, rounded 24, 1px #e0e0e0, 안에서 스크롤). 순서 = 종류(sensor-type-group 4줄 물리 · 화학 · 생명·지구 · 장비, 기본 접힘, 검색 없음, 묶음 줄에 고른 개수 "화학 · 2개", 고른 게 있는 묶음은 처음부터 펼침, chip 여러 개 고르기) → 회사 chip 여러 개(목록에 있는 회사만) → 상태 3개(정상 · 점검 필요 · 고장) → button-outline "초기화" + button-primary "{N}개 보기". 27종을 한꺼번에 펼쳐 두지 않는다. 고른 chip = #e6f4fc + 1px #2b9fe0 테두리(글자 #141414)
- list-select-toggle: 선택 모드 진입. 모바일 = 머리 줄 button-pill-soft "선택"(sensor-add 왼쪽, 사이 8), 데스크톱 = list-filter-button 오른쪽 button-outline "선택". 누르면 17-select(승인본). 핑크 없음 (교사·admin만)
- sensor-doc-add: 서류로 등록 진입. 데스크톱 = 페이지 머리 sensor-add 바로 왼쪽 button-outline "서류로 등록"(왼쪽 서류 아이콘 #141414) → 본문 페이지(17-doc-upload, 승인본). 모바일 = sensor-add "등록" 시트의 첫 줄 "서류로 등록" + caption #707070 "품의서·영수증을 AI가 읽어요"(이 프레임에서는 시트 닫힘). 하늘색 없음 (교사·admin만)
- sensor-add: 센서 등록 진입. 데스크톱 = 페이지 머리 맨 오른쪽 button-primary "센서 등록" → detail-drawer sensor-form. 모바일 = 머리 줄 맨 오른쪽 button-pill-soft "등록"(#f3f3f3, 라벨 #141414, 왼쪽 + 아이콘, 높이 44) → 작은 바텀시트 2줄: "서류로 등록" / "직접 입력"(→ sensor-form 전용 화면, 머리 × 만 — ☰ 없음), 행 높이 52 이상. 이 프레임에서는 시트 닫힘. 하늘색 없음 (교사·admin만)
- detail-drawer: 데스크톱 전용. 센서 상세·등록·수정 자리(이 프레임 닫힘). 폭 480, #ffffff, 왼쪽 1px #f0f0f0 선, × 닫기
- button-pill-soft: 모바일 list-select-toggle "선택"·sensor-add "등록"(교사·admin만), list-filter-button "필터"
- button-outline: 데스크톱 list-select-toggle "선택"·sensor-doc-add "서류로 등록" (교사·admin만)
- button-primary: 데스크톱 sensor-add "센서 등록"(#141414 채움, #ffffff 글자, rounded 9999, 높이 44 이상). 하늘색 없음 (교사·admin만)
- ex-empty-state-card: 검색·필터 결과 0건 "조건에 맞는 센서가 없어요" + button-outline "필터 지우기"(이 프레임 숨김). 핑크 없음
- ex-toast: 서류로 등록 뒤 "센서 3개를 등록했어요", 'QR 스캔' 탭 "준비 중이에요"(이 프레임에는 그리지 않음)
- tab-bar: 모바일 전용 하단 탭바 1개(공통 규격). 데스크톱에는 두지 않는다. 하늘색: 활성 tab-item 아이콘 #2b9fe0만
- tab-item: "홈" · "시약" · "QR 스캔" · "기록" 4개. 활성 = "시약"(센서는 시약 탭 안), "QR 스캔" 회색 '준비 중'
### 반영한 레퍼런스
- https://uibowl.io/name/%ED%86%A0%EC%8A%A4%EC%A6%9D%EA%B6%8C?patterns=%EC%BB%A4%EB%AE%A4%EB%8B%88%ED%8B%B0&imgId=cmsb4ub9l0009jo042gue22tj
- https://uibowl.io/name/%EC%B9%B4%EC%B9%B4%EC%98%A4%EA%B3%A8%ED%94%84%EC%98%88%EC%95%BD?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&imgId=cmtwlux30003ll10402s3yw0o

## 상태 화면 17-type
센서 종류 고르기 시트(프레임 17-type-mobile · 17-type-desktop, 키스크린 17-type-mobile). 교사·admin만(등록·수정 폼). 승인본(runs/20261012-0939 17-type) 틀 그대로 — 머리 + 검색 칸 → 묶음별 행, 고른 chip 오른쪽 체크 — 에서 묶음 안 chip 목록만 접었다 펼치는 구조로 바꾼다. 흐름: sensor-form의 종류 칸 "종류 ▾" → sensor-type-sheet → 검색 아래 sensor-type-group 4줄(기본 접힘, 이미 고른 종류의 묶음은 처음부터 펼침) → 묶음 줄을 누르면 그 묶음만 그 자리에서 아래로 펼침(다시 누르면 접힘, 여러 묶음 함께 펼침 가능) → chip 하나를 누르면 그 값이 칸에 들어가고 바로 닫힘. 검색 글자가 있으면 맞는 chip이 있는 묶음만 펼쳐 맞는 chip만 보이고, 맞는 게 없으면 body-sm #707070 "맞는 종류가 없어요". 핑크 없음.
예시 상태: 교사 김OO, 새 센서 등록 중 — 이름 "무선 편광계", 종류 "편광"을 이미 고른 뒤 종류 칸을 다시 누른 직후. 검색 비어 있음. "화학 9" 묶음만 처음부터 펼침(▾, chip 9개, "편광" 고름), "물리 12" · "생명·지구 3" · "장비 3"은 접힘(▸, 머리 한 줄만). 회사 "파스코", 나머지 기본값.
모바일 활성 탭: "시약". 위→아래: nav-pill(× + "센서 등록" + 학교명, ☰ 없음) → sensor-form(종류 칸 포커스) → sensor-type-sheet(tab-bar 위, 폼 위를 덮는 바텀시트 — 머리 "종류 선택" + × → 검색 → 물리 줄 → 화학 줄 + 펼친 chip → 생명·지구 줄 → 장비 줄, 안에서 스크롤) → tab-bar.
데스크톱 배치: app-sidebar("센서" 현재) | 본문 = 화면 17 sensor-list data-table(그대로) + 오른쪽 detail-drawer 480 = "센서 등록" 폼, 종류 칸 바로 아래 붙은 드롭다운 sensor-type-sheet(칸과 같은 폭 432, 최대 높이 480 안 스크롤 — 검색 → 묶음 4줄, 화학만 펼침).
### 구성 요소
- app-sidebar: 데스크톱 전용. 공통 규격, 학교명 "샘플고등학교" + 교사 메뉴 + "김OO · 교사" + nav-account-menu (교사·admin만)
- sidebar-item: 데스크톱 전용. 교사 9개 / admin 11개. 현재 = "센서", "QR 찾기" 비활성 '준비 중' (교사·admin만)
- nav-pill: 모바일 전용. 폼 머리 — 맨 왼쪽 × 닫기(화면 17) + 제목 "센서 등록" + 현재 학교명 "샘플고등학교" + nav-account-menu ▾. mobile-menu-button ☰ 없음. 하늘색: × 아이콘 #2b9fe0 (교사·admin만)
- nav-account-menu: 닫힌 ▾ (교사·admin만)
- data-table: 데스크톱 전용. 드로어 뒤 화면 17 센서 표(7행) (교사·admin만)
- ex-data-table-cell: 데스크톱 드로어 뒤 표 머리행·셀 chrome (교사·admin만)
- detail-drawer: 데스크톱 전용. 폭 480, 높이 900, #ffffff, 왼쪽 1px #f0f0f0 선, 여백 24, × 닫기. 안 = heading-3 "센서 등록" → sensor-form → 아래 고정 줄 button-primary "저장" (교사·admin만)
- sensor-form: 등록 폼 1개(승인본 칸 순서): ① 이름 text-input 값 "무선 편광계" ② 종류 sensor-type-select 값 "편광" ③ 회사 sensor-maker-select 값 "파스코" ④ 모델명 (선택) text-input(파스코라 입력하면 sensor-model-suggest, 비어 있음) ⑤ 수량 "1" + "개" ⑥ 보관 위치 segmented-control "직접 입력 | 시약장 칸" + text-input ⑦ 상태 segmented-control "정상 · 점검 필요 · 고장"(정상) ⑧ 메모 (선택). 핑크 없음 (교사·admin만)
- sensor-type-select: 종류 고르기 칸 "종류"(라벨 body #141414) — #f0f0f0 칸, rounded 16, 값 "편광"(#141414) + 오른쪽 ▾(비었으면 placeholder "종류 고르기" #adadad). 이 프레임 = 눌린 상태(포커스 링 2px #141414). 하늘색: ▾ 아이콘 #2b9fe0 (교사·admin만)
- sensor-type-sheet: 종류 시트 1개. 모바일 = tab-bar 위 바텀시트(#ffffff, 위쪽 rounded 24, 1px #e0e0e0, 딤 없음, 여백 16·24, 머리 title "종류 선택" + 오른쪽 위 × 닫기 누름 영역 44 이상, 안에서 스크롤), 데스크톱 = 종류 칸 아래 드롭다운(#ffffff, 1px #e0e0e0, rounded 24, 여백 16, 머리·× 없음, 최대 높이 480). 위→아래: 검색 text-input "종류 검색"(#f0f0f0, rounded 16, 왼쪽 검색 아이콘) → 위 간격 12 → sensor-type-group 4줄. 27종을 한꺼번에 펼쳐 두지 않는다. 하나 고르면 바로 닫힘. 화면에는 한국어 이름만. 하늘색: 검색 아이콘 (교사·admin만)
- sensor-type-group: 묶음 줄 4개(공통 모양 — 높이 52, 줄 사이 1px #f0f0f0, 묶음 이름 title #141414 + 종류 수 caption #707070, 오른쪽 ▸/▾ #707070). ① "물리 12" ▸ 접힘 ② "화학 9" ▾ 펼침 — 줄 아래 chip 줄바꿈 9개: pH · 전도도 · 용존산소 · 이온·수질 · 분광 · 편광(고름) · 색·탁도 · CO₂ · 산소 ③ "생명·지구 3" ▸ 접힘 ④ "장비 3" ▸ 접힘. chip = #f3f3f3 pill + label #141414(rounded 9999, 높이 44 이상), 고른 chip "편광" = #e6f4fc 채움 + 1px #2b9fe0 테두리(글자 #141414) + 오른쪽 작은 #2b9fe0 체크. 펼친 묶음 줄은 채움 없음(하늘색 아님). 하늘색: 고른 chip 채움·테두리·체크 (교사·admin만)
- sensor-maker-select: 회사 칸 값 "파스코"(#f0f0f0, rounded 16, ▾). 닫힘 (교사·admin만)
- segmented-control: 보관 위치 "직접 입력 | 시약장 칸", 상태 "정상 · 점검 필요 · 고장"(모바일은 시트 아래 가려짐) (교사·admin만)
- segmented-control-active: "직접 입력", "정상" 흰 pill. 하늘색: 1px #2b9fe0 테두리 (교사·admin만)
- text-input: 이름 · 모델명 · 수량 · 보관 위치 · 메모, 종류 검색(#f0f0f0, rounded 16, 포커스 링 2px #141414) (교사·admin만)
- button-primary: "저장"(모바일 = tab-bar 위 고정 바 — 시트가 열린 동안 시트에 가려짐, 데스크톱 = 드로어 아래 고정 줄 전폭). 이 프레임 = 활성(이름·종류·회사·수량 채움). 하늘색 없음 (교사·admin만)
- tab-bar: 모바일 전용 하단 탭바 1개(공통 규격). 시트는 이 바 위. 데스크톱에는 두지 않는다 (교사·admin만)
- tab-item: 4개 "홈" · "시약" · "QR 스캔" · "기록". 활성 = "시약", "QR 스캔" 회색 '준비 중' (교사·admin만)
### 반영한 레퍼런스
- https://uibowl.io/name/%ED%86%A0%EC%8A%A4%EC%A6%9D%EA%B6%8C?patterns=%EC%BB%A4%EB%AE%A4%EB%8B%88%ED%8B%B0&imgId=cmsb4ub9l0009jo042gue22tj
- https://uibowl.io/name/%EB%8B%AC%EB%8B%A4%EB%B0%A9?patterns=%EC%83%81%EC%84%B8%EC%A0%95%EB%B3%B4%20%28PDP%29&patternName=%EC%83%81%ED%92%88

## 상태 화면 17-filter
센서 필터 시트(프레임 17-filter-mobile · 17-filter-desktop, 키스크린 17-filter-mobile). 모든 역할(학생은 뒤 화면 머리에 "선택"·"서류로 등록"·"센서 등록"/"등록" 없음 — 시트 구성은 같다). 흐름: 화면 17 list-filter-button "필터" → list-filter-sheet. 종류 구역 = sensor-type-group 4줄(기본 접힘, 검색 없음). 묶음 줄을 누르면 시트를 벗어나지 않고 그 자리에서 아래로 펼침(다시 누르면 접힘, 여러 묶음 함께 펼침 가능). chip 여러 개 고르기. 묶음 줄에 고른 개수("화학 · 2개", 0개면 생략)라 접혀 있어도 선택이 보인다. 고른 게 있는 묶음은 시트를 다시 열 때 처음부터 펼침. → 회사 chip → 상태 chip → 맨 아래 "초기화" / "{N}개 보기" 고정. "{N}개 보기"를 누르면 시트가 닫히고 목록이 걸러지며 list-filter-button에 적용 개수 pill. 핑크 없음.
예시 상태: 교사 김OO, 화면 17(센서 7개)에서 필터를 열어 "화학" 묶음을 펼치고 pH · 전도도를 고른 직후(아직 적용 전 — 뒤 목록은 7개 그대로). 종류: "물리" 접힘 · "화학 · 2개" 펼침(pH·전도도 고름) · "생명·지구" 접힘 · "장비" 접힘. 회사·상태는 고른 것 없음. 결과 = 무선 pH 센서 1개 → 버튼 "1개 보기".
모바일 활성 탭: "시약". 위→아래: nav-pill(‹ + "센서" + 학교명, ☰ 없음) → list-filter-sheet(nav-pill 아래부터 tab-bar 위쪽 선까지 높은 바텀시트 — 머리 "필터" + × → 종류(물리 줄 → 화학 · 2개 줄 + 펼친 chip → 생명·지구 줄 → 장비 줄) → 회사 → 상태, 안에서 스크롤 → 시트 맨 아래 고정 버튼 줄 "초기화" · "1개 보기"; 뒤 화면 17 목록은 시트에 가려져 그리지 않는다) → tab-bar.
데스크톱 배치: app-sidebar("센서" 현재) | 본문 = 화면 17 그대로(페이지 머리 + sensor-list data-table 7행) + list-filter-button 바로 아래 붙은 드롭다운 list-filter-sheet(폭 400, rounded 24, 1px #e0e0e0, 최대 높이 = 버튼 아래부터 본문 아래 여백 32까지, 안에서 스크롤, 맨 아래 버튼 줄 고정). list-filter-button은 열린 상태.
### 구성 요소
- app-sidebar: 데스크톱 전용. 공통 규격, 학교명 "샘플고등학교" + 역할별 메뉴 + "김OO · 교사" + nav-account-menu
- sidebar-item: 데스크톱 전용. 학생 6개 / 교사 9개 / admin 11개. 현재 = "센서", "QR 찾기" 비활성 '준비 중'
- nav-pill: 모바일 전용. 시트 상태 머리 — 맨 왼쪽 ‹ 뒤로(화면 17) + 제목 "센서" + 현재 학교명 "샘플고등학교" + nav-account-menu ▾. mobile-menu-button ☰ 없음. 하늘색: ‹ 아이콘 #2b9fe0
- nav-account-menu: 닫힌 ▾
- sensor-list: 데스크톱 = 드롭다운 뒤 화면 17 센서 목록 그대로(머리 "센서" + "7개", 아직 적용 전). 모바일 = 시트에 가려져 그리지 않는다
- data-table: 데스크톱 전용. 드롭다운 뒤 화면 17 센서 표 — 열 이름 · 종류 · 회사 · 모델 · 수량 · 보관 위치 · 상태, 7행(드롭다운에 가린 부분은 가려진 채)
- ex-data-table-cell: 데스크톱 표 머리행(caption #707070)·셀(body-sm) chrome
- sensor-row: 데스크톱 표 7행(공통 예시 데이터)
- sensor-status-badge: 데스크톱 표 상태 열(운동 센서 고장 · 무선 pH 센서 점검 필요 · 나머지 정상, 무채색). 핑크·하늘색 없음
- text-input: 데스크톱 페이지 머리 검색 "센서 이름·모델 검색"(폭 320, 비어 있음). 하늘색: 검색 아이콘 #2b9fe0
- list-filter-button: 데스크톱 페이지 머리 button-pill-soft "필터"(열린 상태 — 버튼 뒤 #e6f4fc, 글자 #141414, 적용 전이라 개수 pill 없음). 모바일은 시트에 가려짐. 하늘색: 필터 아이콘 #2b9fe0, 열린 상태 채움
- list-filter-sheet: 센서 필터 시트 1개. 모바일 = tab-bar 위 높은 바텀시트(#ffffff, 위쪽 rounded 24·아래 0, 1px #e0e0e0, 딤·그림자 없음, 좌우 여백 16), 데스크톱 = 버튼 아래 드롭다운 패널(#ffffff, 1px #e0e0e0, rounded 24, 여백 16). 머리: title "필터" + 오른쪽 위 × 닫기(누름 영역 44 이상). 본문(안에서 스크롤, 구역 사이 24, 구역 제목 heading-4 #141414): ① "종류" — sensor-type-group 4줄(검색 없음) ② "회사" — chip 줄바꿈 4개: 파스코 · 버니어 · 사이언스큐브 · 오맥스(고른 것 없음) ③ "상태" — chip 3개: 정상 · 점검 필요 · 고장(고른 것 없음). 맨 아래 고정 버튼 줄(#ffffff, 위 1px #f0f0f0, 여백 12·16, 1:1, 사이 8): 왼쪽 button-outline "초기화" + 오른쪽 button-primary "1개 보기". chip = #f3f3f3 pill + label #141414(rounded 9999, 높이 44 이상), 고른 chip = #e6f4fc 채움 + 1px #2b9fe0 테두리(글자 #141414) + 작은 #2b9fe0 체크. 하늘색: 고른 chip, × 아이콘
- sensor-type-group: 필터 종류 구역 묶음 줄 4개(공통 모양 — 높이 52, 줄 사이 1px #f0f0f0, 묶음 이름 title #141414 + 고른 개수 caption #707070, 오른쪽 ▸/▾ #707070). ① "물리" ▸ 접힘(고른 것 없음 — 개수 생략) ② "화학 · 2개" ▾ 펼침 — 줄 아래 chip 줄바꿈 9개: pH(고름) · 전도도(고름) · 용존산소 · 이온·수질 · 분광 · 편광 · 색·탁도 · CO₂ · 산소 ③ "생명·지구" ▸ 접힘 ④ "장비" ▸ 접힘. 여러 개 고르기(체크 표시만 바뀌고 시트는 열린 채). 펼친 묶음 줄은 채움 없음. 하늘색: 고른 chip pH·전도도 채움·테두리·체크
- list-select-toggle: 데스크톱 페이지 머리 button-outline "선택"(드롭다운 뒤, 그대로). 모바일은 시트에 가려짐 (교사·admin만)
- sensor-doc-add: 데스크톱 페이지 머리 button-outline "서류로 등록"(그대로) (교사·admin만)
- sensor-add: 데스크톱 페이지 머리 button-primary "센서 등록"(그대로) (교사·admin만)
- button-pill-soft: 데스크톱 list-filter-button "필터"
- button-outline: 시트 "초기화"(#ffffff, 1px #e0e0e0, 라벨 #141414, rounded 9999, 높이 44 이상, 고른 것을 모두 지우고 묶음을 모두 접음), 데스크톱 머리 "선택"·"서류로 등록"(교사·admin만). 하늘색 없음
- button-primary: 시트 "1개 보기"(#141414 채움, #ffffff 글자, rounded 9999, 높이 44 이상, 결과 0개면 "0개 보기" 비활성), 데스크톱 머리 "센서 등록"(교사·admin만). 하늘색 없음
- tab-bar: 모바일 전용 하단 탭바 1개(공통 규격). 시트는 이 바 위쪽 선 위에 붙는다. 데스크톱에는 두지 않는다
- tab-item: 4개 "홈" · "시약" · "QR 스캔" · "기록". 활성 = "시약", "QR 스캔" 회색 '준비 중'
### 반영한 레퍼런스
- https://uibowl.io/name/%EB%84%A4%EC%9D%B4%EB%B2%84%EB%B8%94%EB%A1%9C%EA%B7%B8?patterns=%ED%95%84%ED%84%B0&imgId=cmumdx3pp008yjm04zoku825b
- https://uibowl.io/name/%EC%B9%B4%EC%B9%B4%EC%98%A4%EA%B3%A8%ED%94%84%EC%98%88%EC%95%BD?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&imgId=cmtwlux30003ll10402s3yw0o
- https://uibowl.io/name/%EC%B9%B4%EC%B9%B4%EC%98%A4%EA%B3%A8%ED%94%84%EC%98%88%EC%95%BD?patterns=%EA%B2%80%EC%83%89&imgId=cmtwlue90002bjw04hgtwofel
- https://uibowl.io/name/%EB%8B%AC%EB%8B%A4%EB%B0%A9?patterns=%EC%83%81%EC%84%B8%EC%A0%95%EB%B3%B4%20%28PDP%29&patternName=%EC%83%81%ED%92%88

## 역할별 노출
앱 전체(로그인 후 화면) 기준 개수. runs/20261012-0939 승인 표 그대로 — 이번 변경(종류 묶음 접힘)은 roles 대상 컴포넌트의 개수를 바꾸지 않는다. 같은 화면의 상태 화면·모바일·데스크톱에 다시 나오는 같은 컴포넌트는 그 화면 1개로 센다(예: 화면 17의 sensor-add·sensor-doc-add·list-select-toggle은 17·17-filter 머리에 나와도 1).
- 학생: 화면 17·17-filter에 "선택"·"등록"·"서류로 등록"·"센서 등록" 없음 → list-select-toggle·sensor-add·sensor-doc-add 0(R5). 17-type은 교사·admin만 들어온다.
- sensor-type-sheet·sensor-type-group·list-filter-sheet는 rules.json roles 대상이 아니어서 표에 넣지 않는다(sensor-type-sheet는 교사·admin 폼 안, list-filter-sheet·필터 안 sensor-type-group은 모든 역할).
- msds-entry = 화면 3 1 + 화면 10 상세 1(학생·교사·admin 모두 2, R4). 나머지 행은 runs/20261012-0939 값 그대로.

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
| doc-upload | 0 | 2 | 2 |
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
| sensor-doc-add | 0 | 1 | 1 |
| invite-more-menu | 0 | 0 | 1 |
| invite-cancel | 0 | 0 | 1 |
