# S2 설계 — run 20261012-0939

대상 화면: 8 (사용자 관리) · 13 (홈) · 15 (랜딩) · 17 (센서) + 상태 화면 8-invite-cancel · 13-menu(모바일 전용) · 13-no-access · 17-type · 17-model · 17-doc-upload · 17-doc-review · 17-doc-fail · 학교: 샘플고등학교 (input.json) · 키스크린: 17-doc-review-desktop, 17-type-mobile, 13-menu-mobile
변경 사유: 개발 세션 요청 8 (2026-10-12, rules.json 1.27.1) — ① 센서 종류 27종 묶음 시트(17-type) ② 회사 = 파스코면 모델명 자동완성 + 종류·이름 채움(17-model) ③ 센서 서류로 등록(17 머리 "서류로 등록", 17-doc-upload · 17-doc-review · 17-doc-fail) ④ 모바일 ☰ 전체 메뉴(13-menu = 모바일 프레임만, nav-pill이 보이는 목록·홈 모바일 프레임의 nav-pill 맨 왼쪽에 mobile-menu-button — 8 · 8-invite-cancel · 13 · 13-menu · 13-no-access · 17. 폼·서류·시트 상태는 × / ‹ 머리만) ⑤ 권한 없는 주소 → 홈 + 토스트(13-no-access, 학생 홈) ⑥ 초대 취소(화면 8 초대 대기 행 ⋯, 8-invite-cancel) ⑦ 랜딩 히어로 워드마크 없음(15-mobile 히어로 첫 줄 = 꼬리표 "과학실 시약·센서 관리", 15-desktop은 확인만).
근거: docs/PRD.md §7(8·13·15·17), docs/story-service.md 결정 사항 2026-10-12("센서 종류·카탈로그·서류로 등록"·"모바일 전체 메뉴"·"권한 없는 주소·초대 취소·랜딩 워드마크")과 "센서"·"추가 화면 7~10"·"홈"·"랜딩", docs/design.md "Sensors"·"Mobile menu"·"No access"·"Invite cancel"·"Desktop shell"·"Pre-login desktop"·"tab-bar"·"Document intake"·landing-hero, harness/rules.json 1.27.1(sensor.types·type_groups·type_select·catalog·add_mobile·doc, mobile_menu, no_access, invite_cancel, landing_hero_mark, frames.mobile_only_variants, variants 8·13·17, roles R1~R7(R5에 sensor-doc-add), guest.hidden_components, desktop_shell.menu, tab_bar.qr_pending·sensor_entry, never.N1·N2), research/s1-adopt.md, 오케스트레이터 결정(2026-10-12: 13-menu 구성 6개, 폼·서류·시트 상태 ☰ 없음, 17-model 예시 = 학교에 없는 모델 PS-3215).
기준 설계(틀): input.json base — 화면 13·15·17 = runs/20261011-0813 승인 S4 프레임(설계 = runs/20261011-0813/spec/s2-spec.md), 화면 8 = 그 이전 S4 승인본(설계 = runs/20261008-0936 화면 8 + 이후 공통 변경: 사이드바 "센서"·"QR 찾기" 비활성, 탭 'QR 스캔' 준비 중). 승인본 구성은 그대로 두고 요청 8 결정분만 더한다.

색·폰트·모서리·간격은 docs/design.md와 harness/rules.json을 따른다. 허용 색 밖의 값(딤 반투명 검정 등)은 쓰지 않는다. 그림자는 쓰지 않는다(segmented-control-active 예외). 떠 있는 버튼(FAB)은 두지 않는다.
- 핑크 #d6246a·연핑크 #fbe9f0는 badge-low-stock, reorder-alert-card 안에서만 쓴다(이번 대상 기준: 화면 13 재고 부족 배지·재주문 알림, 15 조각 안 배지). 메뉴 시트·권한 토스트·초대 취소·센서 종류 시트·모델 후보·서류로 등록·센서 상태 배지에는 핑크를 쓰지 않는다.
- 하늘색 #2b9fe0·옅은 하늘색 #e6f4fc는 선택·현재 위치·아이콘·체크·진행 표시에만 쓴다. 글자색 금지(그 위 글자 #141414). badge-low-stock·reorder-alert-card·button-primary 안에는 쓰지 않는다. 센서 상태 배지에도 쓰지 않는다.
- 되돌릴 수 없는 동작 버튼(초대 취소 확인 "초대 취소")은 검정 button-primary(#141414 채움, #ffffff 글자) — 시약·센서 삭제와 같다.
- sensor-status-badge는 무채색만: 고장 = #141414 채움 pill + #ffffff label, 점검 필요 = #f3f3f3 pill + #141414 label, 정상 = 채움 없이 #707070 글자 "정상".
- ex-toast는 승인본 모양 그대로(무채색, 그림자 없음) — 모바일 tab-bar 바로 위, 데스크톱 오른쪽 아래.
학교 선택은 회원가입(화면 14)에만 있다. 화면 8·13·17과 상태 화면 8-*·13-*·17-*에는 학교 선택·전환을 두지 않고 현재 학교명 "샘플고등학교"를 모바일은 nav-pill 안(13-menu는 메뉴 시트 머리에도), 데스크톱은 app-sidebar 맨 위에 표시한다. 사용자·센서·홈 요약·서류에서 읽은 센서 연결은 모두 샘플고등학교 것만 보인다(N1). 화면 15는 로그인 전이라 현재 학교명을 표시하지 않는다.
외부 서비스 연결 값(서류 AI 읽기·센서 브랜드 목록)은 서버에서만 다룬다. 어떤 화면에도 연결 값 입력 칸·외부 서비스 설정·AI 엔진 선택 UI·관련 문구를 두지 않는다(N2). 파스코 모델 목록은 개발 쪽 코드 상수라 관리 화면이 없다.
괄호 안 역할 표시가 없는 구성 요소는 그 화면에 들어오는 모든 역할에게 보인다. 화면 8 = admin만 들어온다. sensor-add·sensor-doc-add·list-select-toggle·sensor-alert-tile·reorder-alert-card는 교사·admin만, invite-more-menu·invite-cancel·user-manage는 admin만 — 학생 화면에는 그리지 않는다(R2·R5·R6).

모바일 공통(승인본 그대로 + 요청 8-6): tab-bar는 화면 아래 가장자리 y 780~844(폭 390, 높이 64, rounded 0, #ffffff + 위쪽 1px #f0f0f0 선, 그림자 없음)에 붙고 tab-item 4개("홈"·"시약"·"QR 스캔"·"기록")를 같은 폭으로 채운다. "QR 스캔" tab-item은 화면 12 전까지 회색 — 아이콘·라벨 #adadad + 아이콘 아래 caption "준비 중"(#adadad), 누르면 ex-toast "준비 중이에요". 하단 고정 바·버튼은 tab-bar 바로 위. 시트는 tab-bar 위쪽 선 위에 붙는다(딤 없음, 1px #e0e0e0 테두리, 위쪽 rounded 24, 오른쪽 위 × 닫기). 센서는 탭이 아니라 '시약' 탭 안(inventory-switch "시약 | 센서") + 전체 메뉴 "센서". 화면 17 모바일 활성 탭은 "시약".
- nav-pill 두 가지: ① 목록·홈 머리(8 · 8-invite-cancel 배경 · 13 · 13-menu · 13-no-access · 17 기본) = 맨 왼쪽 mobile-menu-button ☰(44×44, 동그란 아이콘 버튼, 글자 없음, 아이콘 #141414) → 워드마크(또는 제목) → 학교명 + nav-account-menu ▾. ② 폼·서류·시트 상태 머리(17-type · 17-model · 17-doc-upload · 17-doc-review · 17-doc-fail, 그리고 전용 화면으로 덮는 모바일 폼 — 센서 등록·수정 폼 등) = 맨 왼쪽 × 닫기 또는 ‹ 뒤로 → 제목 → 학교명 + nav-account-menu ▾. ☰(mobile-menu-button)는 두지 않는다.
데스크톱 공통(1440×900, rules.json desktop_shell): nav-pill·tab-bar·mobile-menu-button 없음.
- app-sidebar: 왼쪽 고정 열 폭 240, 높이 전체, rounded 0, #f3f3f3 채움, 오른쪽 1px #f0f0f0 선. 맨 위 "Lab_Stock" 워드마크 + 학교명 "샘플고등학교"(title #141414, 전환 없음) → sidebar-item 묶음 → 맨 아래 "{이름} · {역할}"(body-sm) + nav-account-menu ▾.
- sidebar-item: 아이콘 + body 라벨, 높이 44, rounded 0. 현재 항목 = #e6f4fc 채움 + #2b9fe0 아이콘, 라벨 #141414. 메뉴(rules.json desktop_shell.menu): 학생 6개(홈·시약·센서·기록·시약장·QR 찾기) / 교사 9개(+ "관리" 입고·실험 매뉴얼·재주문 알림) / admin 11개(+ "학교 설정" 사용자·판매처). "QR 찾기"는 비활성 — 아이콘·라벨 #adadad + caption "준비 중"(#adadad), 누르면 ex-toast "준비 중이에요".
- 본문 = 사이드바 오른쪽, 페이지 여백 32. 페이지 머리 = 왼쪽 제목(heading-2) + 개수(caption #707070), 오른쪽 검색·필터·선택·보조·주 버튼. data-table = ex-data-table-cell 머리행(caption #707070)·본문(body-sm), rounded 16 컨테이너 + 1px #f0f0f0 테두리, 선택 행 #e6f4fc. detail-drawer = 오른쪽 폭 480, 높이 전체, #ffffff, 왼쪽 1px #f0f0f0 선, 딤 없음, 오른쪽 위 × 닫기(센서 등록·수정 폼도 드로어). 무거운 작업(서류로 등록) = 본문 페이지.
- 겹침: ex-modal-card는 확인에만(가운데, rounded 24, 1px #e0e0e0, 그림자·딤 없음). 모바일 고르기 시트(종류·회사·필터)는 데스크톱에서 그 컨트롤에 붙은 드롭다운·팝오버(#ffffff, 1px #e0e0e0, rounded 24). ex-toast는 모바일 tab-bar 바로 위 / 데스크톱 오른쪽 아래.
- 모바일 전용 상태(rules.json frames.mobile_only_variants): 13-menu는 13-menu-mobile 프레임만 만든다. 데스크톱은 app-sidebar가 같은 메뉴를 늘 펼쳐 두므로 13-menu-desktop은 없다.
예시 데이터(공통): 오늘 = 2026-10-12. 샘플고등학교 시약 42종, 재고 부족 3종(염산 · 50 mL, 에탄올 · 200 mL, 질산은 · 5 g), MSDS 없는 시약 4종, 시약장 2개, 재주문 알림 3건. 데스크톱 프레임 기준 역할 = 교사 "김OO · 교사"(화면 8·8-invite-cancel·13-menu = admin "정OO · admin", 13-no-access = 학생 "이OO · 학생").
- 센서 7개(이름 · 종류 · 회사 · 모델 · 수량 · 보관 위치 · 상태) — 파스코 행은 카탈로그 모델: 무선 온도 센서 · 온도 · 파스코 · PS-3201 · 3개 · 과학실 뒤 선반 · 정상 / 무선 pH 센서 · pH · 버니어 · GDX-PH · 2개 · 1번 시약장 · 좌 1단 · 점검 필요 / 무선 힘 센서 · 힘 · 파스코 · PS-3202 · 4개 · 과학실 뒤 선반 · 정상 / 운동 센서 · 운동(거리) · 파스코 · PS-3219 · 2개 · 준비실 서랍 · 고장 / 무선 편광계 · 편광 · 파스코 · PS-3237 · 1개 · 준비실 서랍 · 정상 / 전압 센서 · 전압 · 사이언스큐브 · — · 6개 · 준비실 서랍 · 정상 / 디지털 현미경 · 기타 · 오맥스 · — · 2개 · 생물 준비실 · 정상. 고장 1 + 점검 필요 1 = 홈 센서 타일 2.

## 화면 8
사용자 관리. admin만(학생·교사 노출 0). 승인본 그대로(머리 인원 줄, 인라인 초대 폼, 멤버 표, 초대 대기 표, 유의사항, 삭제 확인) + 공통 변경(사이드바 "센서"·"QR 찾기" 비활성, 탭 'QR 스캔' 준비 중, 모바일 nav-pill ☰) + 요청 8-3: 초대 대기 행마다 invite-more-menu ⋯(행 맨 오른쪽 끝 하나, 다른 동작 버튼은 행에 늘어놓지 않음).
예시 상태(8-mobile · 8-desktop, 승인본 그대로): 멤버 5명(학생 3 · 교사 1 · admin 1 — 정OO(나) · 김OO · 박OO · 이OO · 최OO) · 초대 대기 2건(han@example.com · 교사 · 10월 10일 · 대기 / yoon@example.com · 학생 · 10월 11일 · 대기), 학생 "박OO" 삭제 확인이 열린 상태. 뒤 목록은 그대로 보인다. ⋯ 메뉴는 닫힘.
모바일 활성 탭: "홈". 위→아래: nav-pill → user-manage(헤더 "샘플고등학교 사용자 5명" + "초대" → 인원 줄 → 이름 검색 → 멤버 → 초대 대기(행 카드 오른쪽 위 ⋯) → 유의사항) → tab-bar. 삭제 확인 시트는 tab-bar 위.
데스크톱 배치: app-sidebar("사용자" 현재) | 본문 페이지 = 페이지 머리(왼쪽 "사용자" + "5명", 아래 인원 줄 / 오른쪽 인라인 초대 폼) → 툴바(이름 검색) → 멤버 data-table → "초대 대기 (2)" data-table(마지막 열 ⋯) → 유의사항. 삭제 확인 = 가운데 ex-modal-card.
### 구성 요소
- app-sidebar: 데스크톱 전용. 공통 규격, 학교명 "샘플고등학교" + admin 메뉴 + "정OO · admin" + nav-account-menu (admin만)
- sidebar-item: 데스크톱 전용. admin 11개(홈·시약·센서·기록·시약장·QR 찾기 / 입고·실험 매뉴얼·재주문 알림 / 사용자·판매처). 현재 = "사용자", "QR 찾기" 비활성 '준비 중'. 학생·교사에게는 이 화면이 없다 (admin만)
- nav-pill: 모바일 전용. mobile-menu-button ☰ + "Lab_Stock" 워드마크 + 제목 "사용자 관리" + 현재 학교명 "샘플고등학교" + nav-account-menu ▾ (admin만)
- mobile-menu-button: 모바일 전용. nav-pill 맨 왼쪽 ☰ 아이콘 버튼(44×44, rounded 9999, 채움 없음, 아이콘 #141414, 글자 없음). 누르면 mobile-menu-sheet(상태 화면 13-menu 모양, 현재 = "사용자"). 이 프레임에서는 닫힘. 데스크톱에는 두지 않는다 (admin만)
- nav-account-menu: 모바일 = 학교명 옆 ▾, 데스크톱 = app-sidebar 맨 아래. "로그아웃" 1개. 하늘색 없음 (admin만)
- user-manage: 본문 블록 1개(승인본 그대로). 모바일 = 헤더 heading-3 "샘플고등학교 사용자 5명" + 오른쪽 button-primary "초대" → 인원 줄 body-sm #707070 "학생 3 · 교사 1 · admin 1" → 이름 검색 → "멤버"(heading-4): 행 = 이름(title) + 본인 "나" pill + 역할(body-sm #707070) + › → "초대 대기 (2)"(heading-4): 카드 행 = 이메일(title) + 역할 · 초대일 caption #707070 + 상태 "대기" + 오른쪽 위 invite-more-menu ⋯ → 유의사항 body-sm #707070 "같은 학교(샘플고등학교) 계정만 초대할 수 있어요". 데스크톱 = 페이지 머리(제목·인원 줄·인라인 초대 폼) + 멤버 data-table + 초대 대기 data-table + 유의사항. 하늘색: 본인 행 배경 #e6f4fc (admin만)
- data-table: 데스크톱 전용. ① 멤버 표 열 = 이름(정렬) · 이메일 · 역할(정렬) · 가입일(정렬) · 행 끝 ⋮(역할 바꾸기 · 사용자 삭제). ② 초대 대기 표 열 = 이메일 · 역할 · 초대일 · 상태 "대기" · 마지막 열 invite-more-menu ⋯(폭 48). 선택 행(박OO) #e6f4fc (admin만)
- invite-more-menu: 초대 대기 행의 ⋯ 아이콘 버튼(#141414, 채움 없음, 누름 영역 44 이상 — 모바일 카드 오른쪽 위, 데스크톱 data-table 마지막 열). 누르면 버튼 바로 아래 붙는 작은 메뉴(reagent-more-menu와 같은 모양: #ffffff, rounded 24, 1px #f0f0f0, 여백 8, 그림자 없음) 안 invite-cancel 1항목. 이 프레임에서는 닫힘(⋯만). 하늘색: 누른 동안 버튼 뒤 #e6f4fc 원 (admin만)
- invite-cancel: 메뉴 항목 "초대 취소"(body #141414, 높이 44, 왼쪽 아이콘 #141414). 메뉴 맨 아래. 누르면 확인 ex-modal-card(상태 화면 8-invite-cancel). 이 프레임에는 그리지 않는다. 핑크 없음 (admin만)
- text-input: 이름 검색, 초대 "이메일"(플레이스홀더 "name@example.com"). #f0f0f0, rounded 16, 포커스 링 2px #141414. 하늘색: 검색 아이콘 #2b9fe0 (admin만)
- ex-data-table-cell: 모바일 "멤버"·"초대 대기" 행, 데스크톱 data-table 머리행·셀. "나" pill = #f3f3f3 + label #141414 (admin만)
- ex-modal-card: ① 초대 시트(모바일만, 승인본) ② 역할 변경 시트(모바일만) ③ 삭제 확인(예시, 열림): heading-3 "이 사용자를 삭제할까요?" + body "박OO · 사용·입고 기록은 남아요" + button-outline "취소" + button-primary "박OO 삭제". 모바일 = tab-bar 위 시트(위쪽 rounded 24), 데스크톱 = 가운데 폭 440 rounded 24. 1px #e0e0e0, 그림자·딤 없음, × 닫기. 핑크 없음 (admin만)
- segmented-control: 초대 역할 "학생 / 교사" (admin만)
- segmented-control-active: 선택 역할 흰 pill. 하늘색: 1px #2b9fe0 테두리(글자 #141414) (admin만)
- button-pill-soft: 초대 "초대 링크 복사" (admin만)
- button-primary: "초대", 삭제 확인 "박OO 삭제"(#141414 채움, #ffffff 글자, rounded 9999, 높이 44 이상). 하늘색 없음 (admin만)
- button-outline: 삭제 확인 "취소"(#ffffff, 1px #e0e0e0, 라벨 #141414) (admin만)
- ex-empty-state-card: 검색 0건 "찾는 사용자가 없어요"(이 프레임 숨김) (admin만)
- ex-toast: "초대를 보냈어요" / "역할을 바꿨어요" / "사용자를 삭제했어요" / "초대를 취소했어요"(이 프레임에는 그리지 않음). 하늘색: 완료 체크 아이콘 #2b9fe0 (admin만)
- tab-bar: 모바일 전용 하단 탭바 1개(공통 규격). 데스크톱에는 두지 않는다 (admin만)
- tab-item: "홈" · "시약" · "QR 스캔" · "기록" 4개. 활성 = "홈", "QR 스캔" 회색 '준비 중' (admin만)
### 반영한 레퍼런스
- https://uibowl.io/website/%EB%A6%AC%EC%8A%A4%EB%8B%9D%EB%A7%88%EC%9D%B8%EB%93%9C?patterns=%EB%A7%88%EC%9D%B4%ED%8E%98%EC%9D%B4%EC%A7%80&imgId=cmsssakfn0008l104ol1ypu26
- https://uibowl.io/website/%EC%B1%84%EB%84%90%ED%86%A1?patterns=AI&imgId=cmudq45mh001qjy04qd93j3wk

## 상태 화면 8-invite-cancel
초대 취소 확인(프레임 8-invite-cancel-mobile · 8-invite-cancel-desktop). admin만. 흐름: 초대 대기 행 ⋯ → 메뉴 "초대 취소" → 확인 모달 → "초대 취소" → ex-toast "초대를 취소했어요", 그 행이 빠짐. "닫기"·× = 모달만 닫힘. 되돌리기 없음. 핑크 없음.
예시 상태: admin 정OO, 초대 대기 "han@example.com · 교사 · 10월 10일" 행의 ⋯에서 "초대 취소"를 고른 직후 — 메뉴는 닫히고 그 행의 ⋯ 버튼만 남은 채 모달이 열린 상태. 뒤 화면은 화면 8 목록(삭제 확인 없음)이 그대로 보인다(딤 없음).
모바일 활성 탭: "홈". 위→아래: nav-pill(배경 화면 8 머리 그대로, ☰ 포함) → user-manage(초대 대기 카드 2장, han@example.com 카드 ⋯) → 모달 = tab-bar 위 시트 → tab-bar.
데스크톱 배치: app-sidebar("사용자" 현재) | 화면 8 본문(초대 대기 data-table의 han@example.com 행 #e6f4fc) 위 가운데 ex-modal-card 폭 440.
### 구성 요소
- app-sidebar: 데스크톱 전용. 공통 규격, 학교명 "샘플고등학교" + admin 메뉴 + "정OO · admin" + nav-account-menu (admin만)
- sidebar-item: 데스크톱 전용. admin 11개. 현재 = "사용자", "QR 찾기" 비활성 '준비 중' (admin만)
- nav-pill: 모바일 전용. 배경 화면 8 머리 — mobile-menu-button ☰ + 워드마크 + 제목 "사용자 관리" + 현재 학교명 "샘플고등학교" + nav-account-menu ▾ (admin만)
- mobile-menu-button: 모바일 전용. 배경 nav-pill 맨 왼쪽 ☰(44×44), 닫힘 (admin만)
- nav-account-menu: 닫힌 ▾ (admin만)
- user-manage: 모달 뒤 화면 8 블록 그대로(멤버 5명 · 초대 대기 2건) (admin만)
- data-table: 데스크톱 전용. 모달 뒤 멤버 표 + 초대 대기 표, han@example.com 행 #e6f4fc (admin만)
- ex-data-table-cell: 모바일 초대 대기 카드 행, 데스크톱 표 셀 (admin만)
- invite-more-menu: han@example.com 행의 ⋯ 버튼(모바일 카드 오른쪽 위, 데스크톱 마지막 열). 메뉴는 닫힘. 하늘색: 방금 누른 ⋯ 뒤 #e6f4fc 원 (admin만)
- invite-cancel: 방금 고른 메뉴 항목 "초대 취소"(메뉴는 닫혀 이 프레임에는 그리지 않음 — 모달 버튼과 같은 동작) (admin만)
- ex-modal-card: 초대 취소 확인 1개(#ffffff, 1px #e0e0e0 테두리, 여백 24, 그림자·딤 없음, 오른쪽 위 × 닫기 누름 영역 44 이상). 모바일 = tab-bar 위 시트(전폭, 위쪽 rounded 24), 데스크톱 = 가운데 폭 440, rounded 24. 위→아래: heading-3 "han@example.com 초대를 취소할까요?"(질문형 1줄, 길면 줄바꿈) → body #141414 "보낸 초대로는 더 이상 가입할 수 없어요." → 버튼 줄(위 간격 24, 1:1, 사이 8): 왼쪽 button-outline "닫기" + 오른쪽 button-primary "초대 취소". '취소' 두 개가 나란히 서지 않게 왼쪽은 "닫기". 핑크·하늘색 없음 (admin만)
- button-outline: 모달 "닫기"(#ffffff, 1px #e0e0e0, 라벨 #141414, rounded 9999, 높이 44 이상) (admin만)
- button-primary: 모달 "초대 취소"(검정 — #141414 채움, #ffffff 글자, rounded 9999, 높이 44 이상), 뒤 화면 "초대". 하늘색 없음 (admin만)
- ex-toast: "초대 취소" 뒤 "초대를 취소했어요"(모바일 tab-bar 위, 데스크톱 오른쪽 아래). 이 프레임에는 그리지 않는다. 하늘색: 완료 체크 아이콘 #2b9fe0 (admin만)
- tab-bar: 모바일 전용 하단 탭바 1개(공통 규격). 시트는 이 바 위쪽 선 위에 붙는다 (admin만)
- tab-item: 4개 "홈" · "시약" · "QR 스캔" · "기록". 활성 = "홈", "QR 스캔" 회색 '준비 중' (admin만)
### 반영한 레퍼런스
- https://uibowl.io/name/%EC%97%90%EC%9D%B4%EB%8B%B7?patterns=%ED%8E%B8%EC%A7%91%C2%B7%EC%88%98%EC%A0%95%ED%95%98%EA%B8%B0&patternName=%EC%B5%9C%EA%B7%BC%EA%B8%B0%EB%A1%9D%28%EC%82%AD%EC%A0%9C%29
- https://uibowl.io/name/%EC%85%94%ED%81%B4?patterns=%EC%B7%A8%EC%86%8C%ED%95%98%EA%B8%B0&imgId=cmrt4shpb0007l104b7hb2rnd
- https://uibowl.io/name/%EC%99%93%EC%84%AD?patterns=%EC%B7%A8%EC%86%8C%ED%95%98%EA%B8%B0&imgId=cmqt89aob001pjl044nphhj04

## 화면 13
홈. 로그인 후 첫 화면, 학생·교사·admin 모두. 승인본(runs/20261011-0813 화면 13) 그대로 — quick-action · home-summary · (교사·admin) reorder-alert-card · (교사·admin) sensor-alert-tile · 최근 사용 기록 — + 요청 8-6: 모바일 nav-pill 맨 왼쪽 mobile-menu-button ☰(→ 상태 화면 13-menu, 모바일 전용). 하단 탭 4개는 그대로.
예시 상태: 교사 김OO. 전체 시약 42종, 재고 부족 3종, MSDS 없는 시약 4종, 시약장 2개(칸 16개 중 지정 14 · 미지정 2), 재주문 알림 3건, 최근 사용 기록 3줄, 센서 고장 1 · 점검 필요 1.
모바일 활성 탭: "홈". 위→아래: nav-pill(☰ + 워드마크 + 학교명 ▾) → quick-action(교사 3칸 2+1) → home-summary ① 재고 요약(맨 아래 sensor-alert-tile 줄) → reorder-alert-card → home-summary ② 시약장 요약 → 최근 사용 기록 카드 → tab-bar.
데스크톱 배치: app-sidebar("홈" 현재) | 본문 = 페이지 머리(왼쪽 heading-2 "샘플고등학교" + "오늘 10월 12일 · 전체 시약 42종" / 오른쪽 quick-action 버튼 줄) → 숫자 타일 줄 "지금 처리할 것"(교사·admin = 재고 부족 3 · 재주문 알림 3 · MSDS 없는 시약 4 · 고장·점검 필요 센서 2 / 학생 = 재고 부족 3) → 3열 위젯 격자(최근 사용 기록 data-table 2칸 폭 · 재고 부족 · 시약장 요약).
### 구성 요소
- app-sidebar: 데스크톱 전용. 공통 규격, 학교명 "샘플고등학교" + 역할별 메뉴 + nav-account-menu
- sidebar-item: 데스크톱 전용. 학생 6개 / 교사 9개 / admin 11개. 현재 = "홈", "QR 찾기" 비활성 '준비 중'
- nav-pill: 모바일 전용. mobile-menu-button ☰ + "Lab_Stock" 워드마크 + 현재 학교명 "샘플고등학교" + nav-account-menu ▾. 학교 선택·전환 없음
- mobile-menu-button: 모바일 전용. nav-pill 맨 왼쪽 ☰ 아이콘 버튼(44×44, rounded 9999, 채움 없음, 아이콘 #141414, 글자 없음). 누르면 mobile-menu-sheet(상태 화면 13-menu). 이 프레임에서는 닫힘. 오른쪽 아이콘 배치는 그대로. 데스크톱에는 두지 않는다(app-sidebar가 같은 메뉴)
- nav-account-menu: 모바일 = 학교명 옆 ▾, 데스크톱 = app-sidebar 맨 아래. "로그아웃" 1개. 하늘색 없음
- quick-action: 역할별 작업 바로가기(승인본 그대로). 모바일 = 교사 3칸 "사용 기록 입력" · "입고"(stock-intake 진입) · "시약장 설정", admin 3칸 "입고" · "사용자 관리"(user-manage 진입) · "시약장 설정", 2+1. 학생 2칸 "사용 기록 입력" · "시약장 보기". 데스크톱 = 페이지 머리 오른쪽 버튼 줄. 하늘색: 모바일 아이콘 #2b9fe0 + 바탕 #e6f4fc
- home-summary: 모바일 = 요약 카드 2장(#ffffff, 1px #f0f0f0, rounded 24, 여백 24) ① 재고 요약 "재고 부족 3개" + 부족 시약 칩 + "전체 시약 42종"(+ 교사·admin 카드 맨 아래 sensor-alert-tile 줄) ② 시약장 요약(막대 + "칸 16개 중 지정 14 · 미지정 2"). 데스크톱 = 숫자 타일(#ffffff, 1px #f0f0f0, rounded 24, 여백 24) "재고 부족 3" · (교사·admin) "MSDS 없는 시약 4" + 위젯 "재고 부족"·"시약장 요약". 하늘색: 막대 지정 구간, › 아이콘
- sensor-alert-tile: 고장·점검 필요 센서 2. 0개면 그리지 않는다. 모바일 = home-summary ① 카드 맨 아래 한 줄(센서 아이콘 #141414 + body "고장·점검 필요 센서 2" + ›, 누름 영역 44 이상, → 화면 17 상태 필터), 데스크톱 = "지금 처리할 것" 4번째 숫자 타일(같은 크기·모양). 무채색. 하늘색: › 아이콘만 (교사·admin만)
- badge-low-stock: 재고 요약 개수 배지 "3", reorder-alert-card 안 "재고 부족"(#d6246a 채움, #ffffff label). 하늘색 없음
- reorder-alert-card: "재주문 알림" 카드(#f3f3f3, rounded 24). 모바일 = heading-4 "재주문 알림" + badge-low-stock + "3건 ›" + "필요량보다 적은 시약이 3종 있어요", 데스크톱 = 숫자 타일 줄의 타일 1개. 판매처 연결 버튼 없음. 하늘색 없음 (교사·admin만)
- data-table: 데스크톱 전용 "최근 사용 기록" 위젯(2칸 폭). 열 = 사용일 · 시약명 · 사용자 · 사용량, 3행, 머리 오른쪽 "전체 보기 ›"
- reagent-row: 모바일 최근 사용 기록 카드 안 3줄. 누르면 화면 10. 하늘색: 누른 행 #e6f4fc
- button-pill-soft: 모바일 "더 보기 ›", reorder-alert-card "3건 ›"(교사·admin만), 데스크톱 위젯 "전체 보기 ›"
- button-outline: 데스크톱 quick-action 버튼 줄 보조 버튼
- button-primary: 데스크톱 quick-action 버튼 줄 마지막 버튼(교사·admin "입고", 학생 "사용 기록 입력"). 하늘색 없음
- ex-empty-state-card: 시약장 0개 / 최근 사용 기록 0건 안내(이 프레임 숨김)
- ex-toast: 권한 없는 주소로 들어와 홈으로 보내졌을 때 한 번(상태 화면 13-no-access), 'QR 스캔' 탭·'QR 찾기' 메뉴 "준비 중이에요". 이 프레임에는 그리지 않는다
- tab-bar: 모바일 전용 하단 탭바 1개(공통 규격). 데스크톱에는 두지 않는다. 하늘색: 활성 tab-item 아이콘 #2b9fe0만
- tab-item: "홈" · "시약" · "QR 스캔" · "기록" 4개. 활성 = "홈", "QR 스캔" 회색 '준비 중'. 역할별 작업은 tab-item으로 두지 않는다
### 반영한 레퍼런스
- https://uibowl.io/name/%EB%83%89%EC%9E%A5%EA%B3%A0%ED%84%B8%EA%B8%B0?patterns=%EC%B4%88%EB%8C%80%ED%95%98%EA%B8%B0%C2%B7%EB%B0%9B%EA%B8%B0&imgId=cmohwt39000b9jm04x67jmza1

## 상태 화면 13-menu
모바일 전체 메뉴(프레임 13-menu-mobile만, 키스크린 13-menu-mobile). admin 기준(rules.json mobile_menu.guest — 상태 프레임 13-menu는 admin). 흐름: 홈 nav-pill ☰ → 전체 높이 바텀시트 → 항목을 누르면 시트가 닫히며 그 화면으로 이동. ×·바깥 = 닫힘. 하단 tab-bar 4개·inventory-switch는 그대로. 핑크 없음.
예시 상태: admin 정OO, 홈(화면 13 admin)에서 ☰을 누른 직후. 지금 화면 = "홈".
모바일 위→아래: nav-pill(☰ 누른 상태) → mobile-menu-sheet(nav-pill 아래부터 tab-bar 위쪽 선까지 전체 높이 — 뒤 admin 홈은 시트에 가려져 그리지 않는다) → tab-bar.
데스크톱: 모바일 전용 — 13-menu-desktop 프레임은 만들지 않는다(rules.json frames.mobile_only_variants, 데스크톱은 app-sidebar가 같은 메뉴).
### 구성 요소
- nav-pill: 모바일 전용. mobile-menu-button ☰ + "Lab_Stock" 워드마크 + 현재 학교명 "샘플고등학교" + nav-account-menu ▾
- mobile-menu-button: 모바일 전용. nav-pill 맨 왼쪽 ☰ 아이콘 버튼(44×44, rounded 9999, 아이콘 #141414, 글자 없음). 시트가 열린 동안 버튼 뒤 #e6f4fc 원. 하늘색: 누른 상태 원 #e6f4fc
- mobile-menu-sheet: 모바일 전용 전체 높이 바텀시트 1개(#ffffff, 위쪽 rounded 24·아래 rounded 0, 1px #e0e0e0 테두리, 딤·그림자 없음, tab-bar 위쪽 선 위에 붙음, 안에서 스크롤). 머리(여백 16·24, 아래 1px #f0f0f0 선): title #141414 "샘플고등학교" + caption #707070 "정OO · admin" + 오른쪽 위 × 닫기(누름 영역 44 이상). 목록 = desktop_shell.menu와 같은 역할별 묶음, 묶음 사이 1px #f0f0f0 선 + 묶음 제목 caption #707070: ① (제목 없음) 홈 · 시약 · 센서 · 기록 · 시약장 · QR 스캔 ② "관리" 입고 · 실험 매뉴얼 · 재주문 알림 ③ "학교 설정" 사용자 · 판매처. 항목 = 왼쪽 아이콘(#707070) + body #141414 라벨, 높이 52, 사각(rounded 0), 좌우 여백 16. 지금 화면 "홈" = #e6f4fc 채움 + #2b9fe0 아이콘(라벨 #141414). "QR 스캔" = 아이콘·라벨 #adadad + 라벨 오른쪽 caption "준비 중"(#adadad), 누르면 ex-toast "준비 중이에요". 맨 아래(위 1px #f0f0f0 선) 조용한 글자 동작 "로그아웃"(body #707070, 높이 52). 학생은 ①만, 교사는 ①②. 하늘색: 지금 화면 항목 채움·아이콘, × 아이콘
- nav-account-menu: 닫힌 ▾. "로그아웃" 1개
- tab-bar: 모바일 전용 하단 탭바 1개(공통 규격). 시트는 이 바 위쪽 선 위에 붙고 탭바는 그대로 보인다
- tab-item: 4개 "홈" · "시약" · "QR 스캔" · "기록". 활성 = "홈", "QR 스캔" 회색 '준비 중'
### 반영한 레퍼런스
- https://uibowl.io/name/%ED%8E%98%EC%9D%B4%EC%9B%8C%ED%81%AC?patterns=%EB%A9%94%EB%89%B4&patternName=%EA%B0%84%ED%8E%B8%EB%A9%94%EB%89%B4%20-%20%EA%B1%B0%EB%9E%98%EC%B2%98
- https://uibowl.io/name/%EB%83%89%EC%9E%A5%EA%B3%A0%ED%84%B8%EA%B8%B0?patterns=%EC%B4%88%EB%8C%80%ED%95%98%EA%B8%B0%C2%B7%EB%B0%9B%EA%B8%B0&imgId=cmohwt39000b9jm04x67jmza1

## 상태 화면 13-no-access
권한 없는 주소 안내(프레임 13-no-access-mobile · 13-no-access-desktop). 학생 홈 + ex-toast 한 번. 학생이 교사·admin 화면(예: 입고) 주소로 들어와 홈(13)으로 보내진 직후. 카드·버튼·핑크 없음. 화면을 막지 않고 뒤 학생 홈이 그대로 보인다. 토스트는 잠시 뒤 사라진다(개발 쪽).
예시 상태: 학생 이OO, 학생 홈(quick-action 2칸 "사용 기록 입력" · "시약장 보기", 재고 요약, 시약장 요약, 최근 사용 기록 — reorder-alert-card·sensor-alert-tile 없음) + 토스트 "교사·관리자만 쓸 수 있는 화면이에요". (admin만 쓰는 화면이면 문구 "관리자만 쓸 수 있는 화면이에요".)
모바일 위→아래: nav-pill → quick-action(2칸) → home-summary ①(센서 줄 없음) → home-summary ② → 최근 사용 기록 카드 → ex-toast(tab-bar 바로 위 한 줄, 좌우 여백 16) → tab-bar.
데스크톱 배치: app-sidebar("홈" 현재, 학생 6개) | 본문 = 학생 홈(페이지 머리 + "지금 처리할 것" 타일 "재고 부족 3" + 위젯 격자) + 오른쪽 아래 ex-toast(오른쪽·아래 여백 32).
### 구성 요소
- app-sidebar: 데스크톱 전용. 공통 규격, 학교명 "샘플고등학교" + 학생 메뉴 + "이OO · 학생" + nav-account-menu
- sidebar-item: 데스크톱 전용. 학생 6개(홈 · 시약 · 센서 · 기록 · 시약장 · QR 찾기). 현재 = "홈", "QR 찾기" 비활성 '준비 중'. 관리 묶음 없음
- nav-pill: 모바일 전용. mobile-menu-button ☰ + "Lab_Stock" 워드마크 + 현재 학교명 "샘플고등학교" + nav-account-menu ▾
- mobile-menu-button: 모바일 전용. nav-pill 맨 왼쪽 ☰(44×44), 닫힘(시트를 열면 학생 묶음 ①만)
- nav-account-menu: 닫힌 ▾
- quick-action: 학생 2칸 "사용 기록 입력" · "시약장 보기"(모바일), 데스크톱 = 페이지 머리 버튼 줄. 하늘색: 모바일 아이콘 #2b9fe0 + 바탕 #e6f4fc
- home-summary: 학생 홈 요약(모바일 카드 2장, 센서 줄 없음 / 데스크톱 "재고 부족 3" 타일 + 위젯). 하늘색: 막대 지정 구간, › 아이콘
- badge-low-stock: 재고 요약 개수 배지 "3"(#d6246a 채움, #ffffff label)
- data-table: 데스크톱 전용 "최근 사용 기록" 위젯
- reagent-row: 모바일 최근 사용 기록 카드 안 3줄
- button-pill-soft: 모바일 "더 보기 ›", 데스크톱 "전체 보기 ›"
- button-primary: 데스크톱 quick-action "사용 기록 입력". 하늘색 없음
- button-outline: 데스크톱 quick-action "시약장 보기"
- ex-toast: 권한 안내 토스트 1개 — 승인본 ex-toast 모양 그대로(무채색, rounded 9999, 그림자 없음): 왼쪽 작은 안내 아이콘 + body-sm "교사·관리자만 쓸 수 있는 화면이에요" + 오른쪽 × 닫기(누름 영역 44 이상). 다른 버튼 없음. 모바일 = tab-bar 바로 위(간격 8) 전폭 한 줄, 데스크톱 = 오른쪽 아래. 핑크·하늘색 없음
- tab-bar: 모바일 전용 하단 탭바 1개(공통 규격). 토스트는 이 바 바로 위. 데스크톱에는 두지 않는다
- tab-item: 4개 "홈" · "시약" · "QR 스캔" · "기록". 활성 = "홈", "QR 스캔" 회색 '준비 중'
### 반영한 레퍼런스
- https://uibowl.io/website/%EB%A6%AC%EC%BA%90%EC%B9%98?patterns=%EB%82%B4%EC%97%AD&imgId=cmihk42lp000jjp0436gwgn7n
- https://uibowl.io/name/%EC%BA%90%EC%8B%9C%EC%9B%8C%ED%81%AC?patterns=%ED%8E%B8%EC%A7%91%C2%B7%EC%88%98%EC%A0%95%ED%95%98%EA%B8%B0&patternName=%EA%B2%8C%EC%8B%9C%EA%B8%80%20%EC%82%AD%EC%A0%9C

## 화면 15
랜딩. 로그인 전 첫 화면. 바탕 = runs/20261011-0813 승인 S4 15-desktop · 15-mobile. 요청 8-4(rules.json landing_hero_mark): landing-hero 안에 "Lab_Stock" 워드마크를 두지 않는다 — 워드마크는 상단 바(모바일 nav-pill · 데스크톱 web-header)에만 1번. 15-mobile = 히어로 첫 줄 "Lab_Stock" → 작은 꼬리표 "과학실 시약·센서 관리"(caption #707070)로 교체, 그 아래 헤드라인·부제·버튼 순서는 그대로. 15-desktop = 그대로(히어로 글 열에 워드마크가 없음을 확인만, 1440 × 5498, 섹션·문구·조각 그대로). 학교명·학교 선택·tab-bar·app-sidebar 없음.
CTA 위계: 채움 "회원가입" → 외곽선 "로그인" → 가장 약한 "둘러보기" 3단. 페이지 끝 cta-band에서 한 번 더(데스크톱).
모바일(390×844) 위→아래: nav-pill(워드마크만) → landing-hero(꼬리표 "과학실 시약·센서 관리" → 강조 헤드라인 2줄 → 부제) → feature-card 4장 → 하단 고정 영역(landing-cta 버튼 2개 세로 + guest-entry). 하단 탭바 없음.
데스크톱 배치: 1440 × 5498 세로 긴 프레임 한 장(그대로), web-header(위 고정) | 가운데 콘텐츠 폭 1200 — 히어로(landing-hero · product-shot · landing-cta · guest-entry) → landing-tabs → 문제 공감 feature-card 3 → landing-section 4 → step-flow 5단계 → 대상 탭 → 안심 2×2 → cta-band → web-footer 한 줄.
### 구성 요소
- web-header: 데스크톱 전용. 로그인 전 공통 규격(전폭 1440, 높이 64, rounded 0, #ffffff + 아래 1px #f0f0f0). 왼쪽 "Lab_Stock" 워드마크(페이지의 유일한 워드마크), 오른쪽 button-outline "로그인" + button-primary "회원가입". 하늘색 없음
- nav-pill: 모바일 전용(그대로). "Lab_Stock" 워드마크만(#f3f3f3, rounded 9999) — 모바일 페이지의 유일한 워드마크. 학교명·mobile-menu-button 없음(로그인 전). 데스크톱에는 두지 않는다
- landing-hero: 히어로 글 묶음. 안에 "Lab_Stock" 워드마크 없음. 모바일 = 첫 줄 꼬리표 caption #707070 "과학실 시약·센서 관리"(이전 첫 줄 "Lab_Stock" 대체) → 강조 헤드라인 2줄(승인본 문구·크기 그대로) → body-lg 부제(승인본 그대로). 데스크톱 = 승인본 그대로 — 꼬리표 → 2줄 헤드라인 "우리 학교 시약장, / 한 화면에서 관리해요" 48 Bold 700 → body-lg 부제 → landing-cta → guest-entry → caption. 모노크롬, 학교명 없음
- product-shot: 데스크톱 전용(그대로). 핑크는 조각 안 badge-low-stock 안에서만
- shot-sidebar: 데스크톱 전용. product-shot · 대상 탭 교사 조각 안 승인 화면 사이드바 이름(app-sidebar로 세지 않음, 그대로)
- landing-cta: 모바일 = 하단 고정 전폭 버튼 2개 세로 "회원가입" · "로그인", 데스크톱 = 히어로 글 열 "회원가입하고 시작하기" · "로그인"(그대로)
- button-primary: landing-cta · web-header · cta-band "회원가입"(#141414 채움, #ffffff 글자, rounded 9999, 높이 44 이상. #141414 띠 안 cta-band에서는 반전). 하늘색 없음
- button-outline: landing-cta · web-header "로그인", cta-band "둘러보기". 하늘색 없음
- guest-entry: button-pill-soft "둘러보기 ›" 1개(→ 둘러보기 13). 하늘색: › 아이콘 #2b9fe0
- button-pill-soft: guest-entry "둘러보기 ›"
- landing-tabs: 데스크톱 전용(그대로). 활성 밑줄 2px #2b9fe0
- feature-card: 모바일 = 기능 카드 4장(그대로, ④에 예시 badge-low-stock), 데스크톱 = 문제 공감 3장(그대로). 하늘색: 아이콘만
- badge-low-stock: 모바일 feature-card ④ 예시 배지, 데스크톱 조각 안 재고 부족 표시(그대로)
- data-table: 데스크톱 전용. product-shot 겹친 카드, landing-section 조각 안 승인 표(그대로)
- landing-section: 데스크톱 전용 4개(그대로 — ② 조각 = shot-4)
- step-flow: 데스크톱 전용(그대로). #141414 반전 띠
- segmented-control: 데스크톱 전용. 대상 탭 "교사 · 학생 · 관리자"(그대로)
- segmented-control-active: "교사" 흰 pill. 하늘색: 1px #2b9fe0 테두리
- cta-band: 데스크톱 전용(그대로)
- web-footer: 데스크톱 전용(그대로). caption #707070 "© 2026 사이음(sci_eum). 과학의 사이, 사람을 잇다."
### 반영한 레퍼런스
- https://uibowl.io/name/%EB%9E%AD%ED%94%8C%EB%A6%AD%EC%8A%A4?patterns=%EC%98%A8%EB%B3%B4%EB%94%A9&imgId=cmswzxy9v0003l404lllro7wu
- https://uibowl.io/name/%ED%8E%98%EC%9D%B4%EC%9B%8C%ED%81%AC?patterns=%EC%98%A8%EB%B3%B4%EB%94%A9&patternName=%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85%20%EC%A0%84
- https://uibowl.io/name/CES%202026?patterns=%EC%98%A8%EB%B3%B4%EB%94%A9&imgId=cmk5qewa10003jy04k4wwtudg
- https://uibowl.io/website/%EB%A7%88%EC%9D%B4%ED%81%AC%EB%A1%9C%EC%86%8C%ED%94%84%ED%8A%B8%20%ED%81%B4%EB%9E%98%EB%A6%AC%ED%8B%B0%20(Microsoft%20Clarity)?patterns=%EB%9E%9C%EB%94%A9%ED%8E%98%EC%9D%B4%EC%A7%80&imgId=cmt180ji1000dkz04ef56j21k

## 화면 17
센서. 무선 센서·현미경 보유 관리만 — 측정값·대여 없음. 학생·교사·admin 모두(학생은 보기만). 샘플고등학교 센서만(N1). 승인본(runs/20261011-0813 화면 17) 그대로 + 요청 8: ① 데스크톱 페이지 머리에 sensor-doc-add button-outline "서류로 등록"(sensor-add 왼쪽) ② 모바일 머리 sensor-add = button-pill-soft "등록" → 작은 바텀시트 2줄("서류로 등록" / "직접 입력") ③ 예시 파스코 행 = 카탈로그 모델번호(PS-3201 무선 온도 센서, PS-3202 무선 힘 센서, PS-3219 운동 센서, PS-3237 무선 편광계) ④ 필터 종류 = 27종 4묶음 ⑤ 모바일 nav-pill ☰(목록 화면이라 둠).
예시 상태(17-mobile · 17-desktop): 공통 예시 데이터의 센서 7개, 필터 없음, 이름순. 교사 기준, 드로어·등록 시트 닫힘.
모바일 활성 탭: "시약". 위→아래: nav-pill → inventory-switch("센서" 선택) → 페이지 머리 줄(왼쪽 heading-4 "센서 7개" + 오른쪽 (교사·admin) list-select-toggle "선택" · sensor-add "등록") → 검색 줄(text-input + list-filter-button) → sensor-list(sensor-row 카드 7장, 사이 12) → tab-bar. 좌우 여백 16.
데스크톱 배치: app-sidebar("센서" 현재) | 본문 = 페이지 머리(왼쪽 heading-2 "센서" + caption "7개" / 오른쪽 검색 text-input 폭 320 + list-filter-button + (교사·admin) list-select-toggle + (교사·admin) sensor-doc-add "서류로 등록" + (교사·admin) sensor-add "센서 등록", 사이 8) → sensor-list = data-table(열 이름 · 종류 · 회사 · 모델 · 수량 · 보관 위치 · 상태, 7행) → 행을 누르면 오른쪽 detail-drawer.
### 구성 요소
- app-sidebar: 데스크톱 전용. 공통 규격, 워드마크 + 학교명 "샘플고등학교" + 역할별 메뉴 + 이름·역할·nav-account-menu
- sidebar-item: 데스크톱 전용. 학생 6개 / 교사 9개 / admin 11개. 현재 = "센서"("시약" 바로 아래), "QR 찾기" 비활성 '준비 중'
- nav-pill: 모바일 전용. mobile-menu-button ☰ + "Lab_Stock" 워드마크 + 현재 학교명 "샘플고등학교" + nav-account-menu ▾. 학교 전환 없음
- mobile-menu-button: 모바일 전용. nav-pill 맨 왼쪽 ☰(44×44, rounded 9999, 아이콘 #141414). 시트를 열면 "센서"가 지금 화면(#e6f4fc). 이 프레임에서는 닫힘
- nav-account-menu: 모바일 = 학교명 옆 ▾, 데스크톱 = app-sidebar 맨 아래. "로그아웃" 1개. 하늘색 없음
- inventory-switch: 모바일 전용. nav-pill 바로 아래 전폭 segmented-control "시약 | 센서", "센서" 선택. "시약"을 누르면 화면 2. 하늘색: 선택 칸 1px #2b9fe0 테두리(글자 #141414)
- segmented-control: inventory-switch 트랙(#f3f3f3, rounded 9999)
- segmented-control-active: inventory-switch "센서" 흰 pill. 하늘색: 1px #2b9fe0 테두리
- sensor-list: 센서 목록 1개. 머리 "센서 7개". 모바일 = sensor-row 카드 세로 쌓기(사이 12). 데스크톱 = data-table. 이름순 기본. 검색은 이름·모델
- sensor-row: 센서 1개. 모바일 = 카드(#f3f3f3, rounded 16, 여백 16): 1줄 이름(title #141414) + 오른쪽 위 sensor-status-badge / 2줄 caption #707070 "온도 · 파스코 · PS-3201"(모델 없으면 "전압 · 사이언스큐브"처럼 있는 것만, 무선 편광계 = "편광 · 파스코 · PS-3237") / 3줄 body-sm #141414 "3개 · 과학실 뒤 선반"(시약장 칸이면 cabinet-number 원 + "1번 시약장 · 좌 1단"). 데스크톱 = data-table 한 행: 이름(title) · 종류 · 회사 · 모델("—" #adadad) · 수량 · 보관 위치 · 상태. 카탈로그 한국어 이름은 이름 칸에만. 하늘색: 모바일 › 아이콘 #2b9fe0, 누른 행 #e6f4fc
- sensor-status-badge: 상태 배지(무채색). 고장 = #141414 채움 pill + #ffffff label, 점검 필요 = #f3f3f3 pill(카드 위에서는 #ffffff 채움 + 1px #e0e0e0 테두리) + #141414 label, 정상 = 채움 없이 #707070 "정상". rounded 9999. 예시 = 운동 센서 고장 · 무선 pH 센서 점검 필요 · 나머지 정상. 핑크·하늘색 없음
- data-table: 데스크톱 전용. sensor-list 표 — 열 = 이름(정렬, 활성 ↑ #2b9fe0) · 종류 · 회사 · 모델 · 수량(정렬) · 보관 위치 · 상태(정렬). 7행. 행 hover #f3f3f3, 선택 행 #e6f4fc. rounded 16 컨테이너, 1px #f0f0f0
- ex-data-table-cell: data-table 머리행(caption #707070)·셀(body-sm) chrome, 행 구분 1px #f0f0f0
- text-input: 검색 "센서 이름·모델 검색"(#f0f0f0, rounded 16, 포커스 링 2px #141414). 하늘색: 검색 아이콘 #2b9fe0
- list-filter-button: 검색 오른쪽 button-pill-soft "필터"(필터 아이콘, 높이 44 이상). 적용 개수 pill은 이 프레임 숨김. 하늘색: 필터 아이콘 #2b9fe0
- list-filter-sheet: 센서 필터(이 프레임 닫힘). 모바일 = tab-bar 위 바텀시트, 데스크톱 = 버튼 아래 드롭다운 패널(폭 400, rounded 24, 1px #e0e0e0, 안에서 스크롤). 순서 = 종류(묶음 제목 물리 · 화학 · 생명·지구 · 장비 아래 chip 여러 개 고르기, 맨 위 검색 없음, 27종) → 회사 chip 여러 개(목록에 있는 회사만) → 상태 3개(정상 · 점검 필요 · 고장) → button-outline "초기화" + button-primary "{N}개 보기". 고른 chip = #e6f4fc + 1px #2b9fe0 테두리(글자 #141414)
- list-select-toggle: 선택 모드 진입. 모바일 = 머리 줄 button-pill-soft "선택"(sensor-add 왼쪽, 사이 8), 데스크톱 = list-filter-button 오른쪽 button-outline "선택". 누르면 17-select(승인본). 핑크 없음 (교사·admin만)
- sensor-doc-add: 서류로 등록 진입. 데스크톱 = 페이지 머리 sensor-add 바로 왼쪽 button-outline "서류로 등록"(#ffffff, 1px #e0e0e0, 라벨 #141414, rounded 9999, 높이 44 이상, 왼쪽 서류 아이콘 #141414) → 본문 페이지(상태 화면 17-doc-upload). 모바일 = sensor-add "등록" 시트의 첫 줄 "서류로 등록" + caption #707070 "품의서·영수증을 AI가 읽어요"(이 프레임에서는 시트 닫힘). 하늘색 없음 (교사·admin만)
- sensor-add: 센서 등록 진입. 데스크톱 = 페이지 머리 맨 오른쪽 button-primary "센서 등록"(#141414 채움, #ffffff 글자, rounded 9999, 높이 44 이상) → detail-drawer sensor-form. 모바일 = 머리 줄 맨 오른쪽 button-pill-soft "등록"(#f3f3f3, 라벨 #141414, 왼쪽 + 아이콘, 높이 44) → 작은 바텀시트(tab-bar 위, 위쪽 rounded 24, × 닫기) 2줄: sensor-doc-add "서류로 등록" + caption "품의서·영수증을 AI가 읽어요" / "직접 입력"(→ sensor-form 전용 화면, 머리 × 만 — ☰ 없음), 행 높이 52 이상. 이 프레임에서는 시트 닫힘. 하늘색 없음 (교사·admin만)
- detail-drawer: 데스크톱 전용. 센서 상세·등록·수정 자리(이 프레임 닫힘). 폭 480, #ffffff, 왼쪽 1px #f0f0f0 선, × 닫기
- button-pill-soft: 모바일 list-select-toggle "선택"·sensor-add "등록"(교사·admin만), list-filter-button "필터"
- button-outline: 데스크톱 list-select-toggle "선택"·sensor-doc-add "서류로 등록" (교사·admin만)
- button-primary: 데스크톱 sensor-add "센서 등록" (교사·admin만)
- ex-empty-state-card: 검색·필터 결과 0건 "조건에 맞는 센서가 없어요" + button-outline "필터 지우기"(이 프레임 숨김). 핑크 없음
- ex-toast: 서류로 등록 뒤 "센서 3개를 등록했어요"(바뀐 행 잠깐 #e6f4fc), 'QR 스캔' 탭 "준비 중이에요"(이 프레임에는 그리지 않음)
- tab-bar: 모바일 전용 하단 탭바 1개(공통 규격). 데스크톱에는 두지 않는다. 하늘색: 활성 tab-item 아이콘 #2b9fe0만
- tab-item: "홈" · "시약" · "QR 스캔" · "기록" 4개. 활성 = "시약"(센서는 시약 탭 안), "QR 스캔" 회색 '준비 중'
### 반영한 레퍼런스
- https://uibowl.io/name/%ED%86%A0%EC%8A%A4%EC%A6%9D%EA%B6%8C?patterns=%EC%BB%A4%EB%AE%A4%EB%8B%88%ED%8B%B0&imgId=cmsb4ub9l0009jo042gue22tj
- https://uibowl.io/website/%EC%82%AC%EB%B0%A9%EB%84%B7?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&imgId=cmu4rq9d8000xjm04y191pizg

## 상태 화면 17-type
센서 종류 고르기 시트(프레임 17-type-mobile · 17-type-desktop, 키스크린 17-type-mobile). 교사·admin만(등록·수정 폼). 흐름: sensor-form의 종류 칸 "종류 고르기 ▾" → sensor-type-sheet → chip 하나를 누르면 그 값이 칸에 들어가고 바로 닫힘. 검색하면 묶음 제목은 남기고 맞는 chip만 보인다(맞는 chip이 없는 묶음은 숨김). 핑크 없음.
예시 상태: 교사 김OO, 새 센서 등록 중 — 이름 "무선 편광계" 입력, 종류 칸 비어 있음(placeholder "종류 고르기"), 회사 "파스코", 나머지 기본값. 종류 칸을 누른 직후 — 검색 비어 있음, 27종 4묶음 모두 보임, 고른 chip 없음.
모바일 활성 탭: "시약". 위→아래: nav-pill(× + "센서 등록" + 학교명, ☰ 없음) → sensor-form(종류 칸 포커스) → sensor-type-sheet(tab-bar 위, 폼 위를 덮는 높은 바텀시트, 안에서 스크롤) → tab-bar.
데스크톱 배치: app-sidebar("센서" 현재) | 본문 = 화면 17 sensor-list data-table(그대로) + 오른쪽 detail-drawer 480 = "센서 등록" 폼, 종류 칸 바로 아래 붙은 드롭다운 sensor-type-sheet(칸과 같은 폭 432, 최대 높이 480 안 스크롤).
### 구성 요소
- app-sidebar: 데스크톱 전용. 공통 규격, 학교명 "샘플고등학교" + 교사 메뉴 + nav-account-menu (교사·admin만)
- sidebar-item: 데스크톱 전용. 교사 9개 / admin 11개. 현재 = "센서" (교사·admin만)
- nav-pill: 모바일 전용. 폼 머리 — 맨 왼쪽 × 닫기(화면 17) + 제목 "센서 등록" + 현재 학교명 "샘플고등학교" + nav-account-menu ▾. mobile-menu-button ☰ 없음. 하늘색: × 아이콘 #2b9fe0 (교사·admin만)
- nav-account-menu: 닫힌 ▾ (교사·admin만)
- data-table: 데스크톱 전용. 드로어 뒤 화면 17 센서 표 (교사·admin만)
- detail-drawer: 데스크톱 전용. 폭 480, 높이 900, #ffffff, 왼쪽 1px #f0f0f0 선, 여백 24, × 닫기. 안 = heading-3 "센서 등록" → sensor-form → 아래 고정 줄 button-primary "저장" (교사·admin만)
- sensor-form: 등록 폼 1개(승인본 칸 순서): ① 이름 text-input 값 "무선 편광계" ② 종류 sensor-type-select ③ 회사 sensor-maker-select 값 "파스코" ④ 모델명 (선택) text-input(파스코라 입력하면 sensor-model-suggest, 비어 있음) ⑤ 수량 "1" + "개" ⑥ 보관 위치 segmented-control "직접 입력 | 시약장 칸" + text-input ⑦ 상태 segmented-control "정상 · 점검 필요 · 고장"(정상) ⑧ 메모 (선택). 종류가 비어 저장 비활성. 핑크 없음 (교사·admin만)
- sensor-type-select: 종류 고르기 칸 "종류"(라벨 body #141414) — #f0f0f0 칸, rounded 16, placeholder "종류 고르기"(#adadad) + 오른쪽 ▾. 이 프레임 = 눌린 상태(포커스 링 2px #141414). 고르면 "편광 ▾"처럼 값 표시. 하늘색: ▾ 아이콘 #2b9fe0 (교사·admin만)
- sensor-type-sheet: 종류 시트 1개. 모바일 = tab-bar 위 바텀시트(#ffffff, 위쪽 rounded 24, 1px #e0e0e0, 딤 없음, 머리 title "종류 선택" + 오른쪽 위 × 닫기), 데스크톱 = 종류 칸 아래 드롭다운(#ffffff, 1px #e0e0e0, rounded 24, 여백 16, 머리·× 없음). 위→아래: 검색 text-input "종류 검색"(#f0f0f0, rounded 16, 검색 아이콘) → 묶음 4개(각 묶음 제목 title #141414, 묶음 사이 24, 제목 아래 chip 줄바꿈 사이 8): "물리" 온도 · 힘 · 운동(거리) · 가속도 · 회전 · 전압 · 전류 · 자기장 · 조도 · 소리 · 압력 · 방사선 / "화학" pH · 전도도 · 용존산소 · 이온·수질 · 분광 · 편광 · 색·탁도 · CO₂ · 산소 / "생명·지구" 심박·생체 · 습도 · 기상 / "장비" 인터페이스 · 코딩 보드 · 기타. chip = #f3f3f3 pill + label #141414(rounded 9999, 높이 44 이상), 고른 chip = #e6f4fc 채움 + 1px #2b9fe0 테두리(글자 #141414) + 오른쪽 작은 #2b9fe0 체크(이 프레임에는 고른 chip 없음). 하나 고르면 바로 닫힘. 화면에는 한국어 이름만. 하늘색: 검색 아이콘, 고른 chip (교사·admin만)
- sensor-maker-select: 회사 칸 값 "파스코"(#f0f0f0, rounded 16, ▾). 닫힘 (교사·admin만)
- segmented-control: 보관 위치 "직접 입력 | 시약장 칸", 상태 "정상 · 점검 필요 · 고장"(시트 아래 가려짐) (교사·admin만)
- segmented-control-active: "직접 입력", "정상" 흰 pill. 하늘색: 1px #2b9fe0 테두리 (교사·admin만)
- text-input: 이름 · 모델명 · 수량 · 보관 위치 · 메모, 종류 검색(#f0f0f0, rounded 16, 포커스 링 2px #141414) (교사·admin만)
- button-primary: "저장"(모바일 = tab-bar 위 고정 바 — 시트가 열린 동안 시트에 가려짐, 데스크톱 = 드로어 아래 고정 줄 전폭). 이 프레임 = 비활성(종류 비어 있음), 비활성 모양은 승인본 17-form과 같게. 하늘색 없음 (교사·admin만)
- tab-bar: 모바일 전용 하단 탭바 1개(공통 규격). 시트는 이 바 위. 데스크톱에는 두지 않는다 (교사·admin만)
- tab-item: 4개 "홈" · "시약" · "QR 스캔" · "기록". 활성 = "시약", "QR 스캔" 회색 '준비 중' (교사·admin만)
### 반영한 레퍼런스
- https://uibowl.io/name/%ED%86%A0%EC%8A%A4%EC%A6%9D%EA%B6%8C?patterns=%EC%BB%A4%EB%AE%A4%EB%8B%88%ED%8B%B0&imgId=cmsb4ub9l0009jo042gue22tj

## 상태 화면 17-model
파스코 모델 자동완성(프레임 17-model-mobile · 17-model-desktop). 교사·admin만. 흐름: 회사 = "파스코" → 모델명 칸에 입력 → 칸 바로 아래 후보 목록(모델번호·이름으로 검색 — "PS-321" 또는 "비색") → 고르면 모델명 = 모델번호, 종류 = 카탈로그 종류, 이름이 비었으면 이름 = 한국어 이름 → 채운 칸 잠깐 #e6f4fc + 모델명 아래 catalog-fill-note. 모든 칸은 고칠 수 있다. 다른 회사는 모델명 직접 입력(목록 없음). 핑크 없음.
예시 상태: 교사 김OO, 샘플고등학교에 아직 없는 모델을 새로 등록 — 이름 비어 있던 채 회사 "파스코" 고름 → 모델명 "PS-321" 입력 → 후보 5줄 중 "PS-3215"를 누른 바로 그 순간: 모델명 "PS-3215", 이름 "무선 비색·탁도"·종류 "색·탁도 ▾" 채워져 칸이 #e6f4fc, 모델명 칸 바로 아래 catalog-fill-note, 그 아래 후보 목록은 고른 행 표시가 남은 채 아직 열려 있음(다음 순간 닫힘).
모바일 활성 탭: "시약". 위→아래: nav-pill(× + "센서 등록" + 학교명, ☰ 없음) → sensor-form(이름 → 종류 → 회사 → 모델명 → catalog-fill-note → sensor-model-suggest 목록(입력 아래 인라인) → 수량 …) → 하단 고정 저장 바(tab-bar 바로 위) → tab-bar.
데스크톱 배치: app-sidebar("센서" 현재) | 본문 = 화면 17 sensor-list data-table + 오른쪽 detail-drawer 480 "센서 등록" 폼, 모델명 칸 아래 catalog-fill-note, 그 아래 붙은 드롭다운 sensor-model-suggest(칸과 같은 폭).
### 구성 요소
- app-sidebar: 데스크톱 전용. 공통 규격, 학교명 "샘플고등학교" + 교사 메뉴 + nav-account-menu (교사·admin만)
- sidebar-item: 데스크톱 전용. 교사 9개 / admin 11개. 현재 = "센서" (교사·admin만)
- nav-pill: 모바일 전용. 폼 머리 — 맨 왼쪽 × 닫기 + 제목 "센서 등록" + 현재 학교명 "샘플고등학교" + nav-account-menu ▾. mobile-menu-button ☰ 없음. 하늘색: × 아이콘 #2b9fe0 (교사·admin만)
- nav-account-menu: 닫힌 ▾ (교사·admin만)
- data-table: 데스크톱 전용. 드로어 뒤 화면 17 센서 표 (교사·admin만)
- detail-drawer: 데스크톱 전용. 폭 480, 높이 900, 여백 24, × 닫기. 안 = heading-3 "센서 등록" → sensor-form(안에서 스크롤) → 아래 고정 줄 button-primary "저장" (교사·admin만)
- sensor-form: 등록 폼 1개: ① 이름 text-input 값 "무선 비색·탁도"(카탈로그로 채움, #e6f4fc) ② 종류 sensor-type-select 값 "색·탁도 ▾"(카탈로그로 채움, #e6f4fc) ③ 회사 sensor-maker-select 값 "파스코" ④ 모델명 text-input 값 "PS-3215"(#e6f4fc) + 바로 아래 catalog-fill-note + sensor-model-suggest ⑤ 수량 "1" + "개" ⑥ 보관 위치 "직접 입력" + text-input 빈 값 ⑦ 상태 "정상" ⑧ 메모 (선택). 채운 칸 = #e6f4fc 채움 + 글자 #141414(잠깐, 이후 #f0f0f0로 돌아감). 핑크 없음. 하늘색: 채운 칸 #e6f4fc (교사·admin만)
- sensor-model-suggest: 모델명 후보 목록 1개(회사 = 파스코일 때만). 모바일 = 모델명 칸 아래 인라인 목록(#ffffff, 1px #e0e0e0, rounded 16), 데스크톱 = 칸 아래 드롭다운(#ffffff, 1px #e0e0e0, rounded 24, 칸과 같은 폭). 행(높이 52 이상, 여백 12·16, 행 사이 1px #f0f0f0) = 모델번호 title #141414(입력과 맞은 글자 "PS-321" Bold 700, 나머지 Regular 400) + 아래 caption #707070 "{한국어 이름} · {종류}". 예시 5줄(최대 6줄): PS-3210 "무선 전도도 · 전도도" / PS-3211 "무선 전압 · 전압" / PS-3212 "무선 전류 · 전류" / PS-3213 "무선 빛(구형) · 조도" / PS-3215 "무선 비색·탁도 · 색·탁도"(고른 행 = #e6f4fc 채움 + 오른쪽 #2b9fe0 체크, 글자 #141414). 맨 끝 조용한 줄 body-sm #707070 "목록에 없어요 — 그대로 적기". 하늘색: 고른 행 채움·체크 (교사·admin만)
- catalog-fill-note: 모델명 칸 바로 아래 한 줄 caption #707070 "카탈로그에서 종류·이름을 채웠어요"(채운 칸만 이름 — 이름이 원래 있었으면 "카탈로그에서 종류를 채웠어요"). 왼쪽 작은 정보 아이콘 #707070(16). 채움·테두리 없음. 핑크·하늘색 없음 (교사·admin만)
- sensor-type-select: 종류 칸 값 "색·탁도 ▾"(채운 칸 #e6f4fc). 하늘색: ▾ 아이콘 #2b9fe0 (교사·admin만)
- sensor-maker-select: 회사 칸 값 "파스코" ▾(닫힘). 다른 회사면 sensor-model-suggest가 열리지 않는다 (교사·admin만)
- segmented-control: 보관 위치 "직접 입력 | 시약장 칸", 상태 "정상 · 점검 필요 · 고장" (교사·admin만)
- segmented-control-active: "직접 입력", "정상" 흰 pill. 하늘색: 1px #2b9fe0 테두리 (교사·admin만)
- text-input: 이름 · 모델명(포커스 링 2px #141414) · 수량 · 보관 위치 · 메모(#f0f0f0, rounded 16) (교사·admin만)
- button-primary: "저장"(모바일 tab-bar 위 고정 바 전폭, 데스크톱 드로어 아래 고정 줄 전폭). 예시 = 활성(이름·종류·회사·수량 채움). 하늘색 없음 (교사·admin만)
- ex-toast: 저장 뒤 "센서를 등록했어요"(이 프레임에는 그리지 않음) (교사·admin만)
- tab-bar: 모바일 전용 하단 탭바 1개(공통 규격). 데스크톱에는 두지 않는다 (교사·admin만)
- tab-item: 4개 "홈" · "시약" · "QR 스캔" · "기록". 활성 = "시약", "QR 스캔" 회색 '준비 중' (교사·admin만)
### 반영한 레퍼런스
- https://uibowl.io/name/Bitget?patterns=%EC%9D%B8%EC%A6%9D%ED%95%98%EA%B8%B0&imgId=cmukqaul5002ll60430j2ykk1

## 상태 화면 17-doc-upload
센서 서류로 등록 1단계 — 서류 올리기(프레임 17-doc-upload-mobile · 17-doc-upload-desktop). 교사·admin만(둘러보기 없음). 화면 7 서류로 입고와 같은 흐름: 파일 1개 → "AI로 읽기" → 읽는 중 → 17-doc-review(또는 17-doc-fail). 모바일 = 전용 화면, 데스크톱 = 본문 페이지(사이드바 유지, 드로어 아님). 핑크 없음.
예시 상태: 교사 김OO, 파일 "2026 센서 구입 영수증.pdf"(1.2MB)를 고른 상태, "AI로 읽기" 활성. 읽는 중 상태(doc-upload 안 #2b9fe0 진행 줄 + "서류를 읽는 중이에요")는 이 프레임에는 그리지 않는다.
모바일 활성 탭: "시약". 위→아래: nav-pill(× + "서류로 등록" + 학교명, ☰ 없음) → sensor-doc-add 머리(heading-3 "서류로 등록" + caption "품의서·영수증을 AI가 읽어요") → doc-upload 카드 → tab-bar. "AI로 읽기"는 카드 하단 전폭.
데스크톱 배치: app-sidebar("센서" 현재) | 본문 페이지 = sensor-doc-add 페이지 머리(왼쪽 "‹ 센서" 돌아가기 + heading-2 "서류로 등록" + caption "품의서·영수증을 AI가 읽어요") → 가운데 단일 열 폭 640 doc-upload 카드 → 본문 하단 고정 바(#ffffff, 위 1px #f0f0f0, 오른쪽 button-primary "AI로 읽기").
### 구성 요소
- app-sidebar: 데스크톱 전용. 공통 규격, 학교명 "샘플고등학교" + 교사 메뉴 + nav-account-menu (교사·admin만)
- sidebar-item: 데스크톱 전용. 교사 9개 / admin 11개. 현재 = "센서" (교사·admin만)
- nav-pill: 모바일 전용. 서류 머리 — 맨 왼쪽 × 닫기(화면 17) + 제목 "서류로 등록" + 현재 학교명 "샘플고등학교" + nav-account-menu ▾. mobile-menu-button ☰ 없음. 하늘색: × 아이콘 #2b9fe0 (교사·admin만)
- nav-account-menu: 닫힌 ▾ (교사·admin만)
- sensor-doc-add: 서류로 등록 흐름의 머리 묶음(화면 17 "서류로 등록" 버튼이 연 화면). 모바일 = nav-pill 아래 heading-3 "서류로 등록" + caption #707070 "품의서·영수증을 AI가 읽어요", 데스크톱 = 페이지 머리 "‹ 센서"(button-pill-soft, → 화면 17) + heading-2 "서류로 등록" + 같은 caption. 하늘색: ‹ 아이콘 #2b9fe0 (교사·admin만)
- doc-upload: 올리기 카드 1개(화면 7 doc-upload 재사용 — ex-empty-state-card 모양, #ffffff, 1px #e0e0e0, rounded 24, 여백 24). 가운데 업로드 아이콘 → heading-4 "품의서·영수증을 올려 주세요" → caption #707070 "PDF·JPG·PNG 1개, 4MB까지 · 서버에 보관하지 않아요" → 고른 파일 줄(#f3f3f3, rounded 16, 여백 12·16: 서류 아이콘 #141414 + body-sm "2026 센서 구입 영수증.pdf" + caption #707070 "1.2MB" + 오른쪽 × 빼기 누름 영역 44) → button-pill-soft "촬영하기"(모바일) · "파일 바꾸기"(데스크톱은 끌어다 놓기 안내 caption "여기에 끌어다 놓아도 돼요") → (모바일) 카드 하단 전폭 button-primary "AI로 읽기". 형식·크기 오류 = #141414 아이콘 + body-sm "PDF·JPG·PNG 4MB까지만 올릴 수 있어요"(핑크 금지). 하늘색: 업로드 아이콘 #2b9fe0 (교사·admin만)
- button-pill-soft: doc-upload "촬영하기" · "파일 바꾸기", 데스크톱 "‹ 센서". 하늘색: 왼쪽 아이콘 #2b9fe0 (교사·admin만)
- button-primary: "AI로 읽기"(#141414 채움, #ffffff 글자, rounded 9999, 높이 44 이상, 파일 없으면 비활성 — 예시 활성). 모바일 = 카드 하단 전폭, 데스크톱 = 본문 하단 고정 바 오른쪽. 하늘색 없음 (교사·admin만)
- tab-bar: 모바일 전용 하단 탭바 1개(공통 규격). 데스크톱에는 두지 않는다 (교사·admin만)
- tab-item: 4개 "홈" · "시약" · "QR 스캔" · "기록". 활성 = "시약", "QR 스캔" 회색 '준비 중' (교사·admin만)
### 반영한 레퍼런스
- https://uibowl.io/website/%EC%82%AC%EB%B0%A9%EB%84%B7?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&imgId=cmu4rq9d8000xjm04y191pizg

## 상태 화면 17-doc-review
센서 서류로 등록 2단계 — 읽은 결과 확인(프레임 17-doc-review-mobile · 17-doc-review-desktop, 키스크린 17-doc-review-desktop). 교사·admin만. 화면 7 doc-review와 같은 방식: 행 = 서류 품목 1개 + 아래 줄 sensor-link. 같은 학교에 같은 회사+모델이 있으면 기본 "기존 센서에 더하기", 없으면 "새 센서로 등록"(행이 아래로 펼쳐져 new-sensor-fields). 센서·현미경이 아닌 품목은 표 아래 접힌 묶음. "확인 후 등록 · N개" 한 번 = 한 트랜잭션(1~50개, 하나라도 틀리면 전부 취소, 문제 행 2px #141414 테두리 + #707070 안내 줄) → ex-toast "센서 3개를 등록했어요" → 화면 17(바뀐 행 잠깐 #e6f4fc). 핑크 없음.
예시 상태: 교사 김OO, "2026 센서 구입 영수증.pdf"에서 읽은 센서 3개 + 센서 아님 1개:
① 무선 온도 센서 · 파스코 · PS-3201 · 2개 → sensor-link "기존 센서에 더하기 · 무선 온도 센서 · 지금 3개 → 5개"
② 무선 편광계 · 파스코 · PS-3237 · 1개 → sensor-link "기존 센서에 더하기 · 무선 편광계 · 지금 1개 → 2개"
③ 무선 CO₂ 센서 · 이지메이커 · (모델 없음) · 2개 → sensor-link "새 센서로 등록"(펼침) → new-sensor-fields: 이름 "무선 CO₂ 센서" · 종류 "CO₂" · 회사 "이지메이커" · 모델 빈 값 · 수량 2 · 보관 위치 직접 입력 "과학실 뒤 선반" · 상태 정상
접힌 묶음 "센서 아님 1개"(배송비).
모바일 활성 탭: "시약". 위→아래: nav-pill(× + "서류로 등록" + 학교명, ☰ 없음) → sensor-doc-add 머리(heading-3 "서류로 등록") → 파일 줄 + 안내 1줄 → doc-intake-table(머리 "읽은 센서 3개", 행마다 #f3f3f3 카드, ③ 카드 펼침) → "센서 아님 1개" 접힘 → 하단 고정 띠 "확인 후 등록 · 3개"(tab-bar 바로 위) → tab-bar.
데스크톱 배치: app-sidebar("센서" 현재) | 본문 페이지 = sensor-doc-add 페이지 머리("‹ 센서" + heading-2 "서류로 등록") → 파일 줄("2026 센서 구입 영수증.pdf") + 안내 1줄 body-sm #141414 "읽은 내용이 맞는지 확인해 주세요" → doc-intake-table 전폭 data-table(열 품명 · 회사 · 모델 · 수량 · 연결, 행 아래 sensor-link 줄, ③ 행 아래 new-sensor-fields 펼침) → "센서 아님 1개" 접힘 → 본문 하단 고정 바(오른쪽 button-primary "확인 후 등록 · 3개").
### 구성 요소
- app-sidebar: 데스크톱 전용. 공통 규격, 학교명 "샘플고등학교" + 교사 메뉴 + "김OO · 교사" + nav-account-menu (교사·admin만)
- sidebar-item: 데스크톱 전용. 교사 9개 / admin 11개. 현재 = "센서", "QR 찾기" 비활성 '준비 중' (교사·admin만)
- nav-pill: 모바일 전용. 서류 머리 — 맨 왼쪽 × 닫기 + 제목 "서류로 등록" + 현재 학교명 "샘플고등학교" + nav-account-menu ▾. mobile-menu-button ☰ 없음 (교사·admin만)
- nav-account-menu: 닫힌 ▾ (교사·admin만)
- sensor-doc-add: 서류로 등록 흐름의 머리 묶음. 모바일 = heading-3 "서류로 등록", 데스크톱 = 페이지 머리 "‹ 센서" + heading-2 "서류로 등록". 아래 파일 줄(서류 아이콘 + body-sm "2026 센서 구입 영수증.pdf") + 안내 body-sm #141414 "읽은 내용이 맞는지 확인해 주세요". 하늘색: ‹ 아이콘 (교사·admin만)
- doc-intake-table: 확인 표 1개(화면 7 doc-intake-table 재사용, extraction-table chrome). 머리 heading-4 "읽은 센서 3개". 데스크톱 = data-table 전폭(rounded 16 컨테이너, 1px #f0f0f0): 열 품명(서류 표기) · 회사 · 모델 · 수량 · 연결, 셀 body-sm, 행 아래 sensor-link 줄(행 사이 1px #f0f0f0). 모바일 = 행마다 카드(#f3f3f3, rounded 16, 여백 16, 사이 12): 1줄 품명(title) + 2줄 caption #707070 "파스코 · PS-3201 · 2개" + 3줄 sensor-link. 표 아래 접힌 묶음 "센서 아님 1개 ›"(body-sm #707070, 누르면 펼침 — 배송비). 하늘색: 접힘 › 아이콘 (교사·admin만)
- data-table: 데스크톱 전용. doc-intake-table 표 몸체(위 열 구성). 본문 페이지라 화면 17 표는 뒤에 없다 (교사·admin만)
- ex-data-table-cell: 데스크톱 표 머리행(caption #707070)·셀 chrome (교사·admin만)
- sensor-link: 행 아래 연결 줄. ① ② = 왼쪽 링크 아이콘 #2b9fe0 + body-sm #141414 "기존 센서에 더하기 · 무선 온도 센서 · 지금 3개 → 5개" + 오른쪽 조용한 글자 동작 "바꾸기" · "빼기"(body-sm #707070 밑줄, 누름 영역 44 이상). "바꾸기" = 우리 학교 센서 고르기 시트(모바일) / 팝오버(데스크톱) + 맨 아래 "새 센서로 등록". ③ = body-sm #141414 "새 센서로 등록" + 펼침 ▴ + "빼기". 데스크톱 = 열 "연결" 칸에 요약("더하기 3 → 5" / "새 센서") + 행 아래 줄 전체. 핑크 없음. 하늘색: 링크 아이콘 (교사·admin만)
- new-sensor-fields: ③ 행 아래로 펼친 입력 묶음(#ffffff, 1px #f0f0f0, rounded 16, 여백 16; 데스크톱 = 표 안 행 아래 전폭, 2열 "라벨 | 입력"): 이름 text-input "무선 CO₂ 센서" · 종류 sensor-type-select "CO₂ ▾" · 회사 sensor-maker-select "이지메이커 ▾" · 모델 text-input 빈 값(placeholder "모델명 (선택)") · 수량 "2" + "개" · 보관 위치 segmented-control "직접 입력 | 시약장 칸" + text-input "과학실 뒤 선반" · 상태 segmented-control "정상 · 점검 필요 · 고장"(정상). 카탈로그(파스코)로 채운 값이면 그 칸 옆 caption #707070 "카탈로그"(이 예시는 이지메이커라 없음). 핑크 없음 (교사·admin만)
- sensor-type-select: new-sensor-fields 종류 칸 "CO₂ ▾"(닫힘) (교사·admin만)
- sensor-maker-select: new-sensor-fields 회사 칸 "이지메이커 ▾"(닫힘) (교사·admin만)
- segmented-control: new-sensor-fields 보관 위치·상태 (교사·admin만)
- segmented-control-active: "직접 입력", "정상" 흰 pill. 하늘색: 1px #2b9fe0 테두리 (교사·admin만)
- text-input: new-sensor-fields 이름·모델·수량·보관 위치(#f0f0f0, rounded 16, 포커스 링 2px #141414) (교사·admin만)
- button-pill-soft: 데스크톱 "‹ 센서" (교사·admin만)
- button-primary: "확인 후 등록 · 3개"(#141414 채움, #ffffff 글자, rounded 9999, 높이 44 이상). 모바일 = tab-bar 바로 위 고정 띠(#ffffff, 위 1px #f0f0f0, 여백 12·16) 전폭, 데스크톱 = 본문 하단 고정 바 오른쪽. 연결할 행 0개면 비활성. 하늘색 없음 (교사·admin만)
- ex-toast: 등록 뒤 "센서 3개를 등록했어요"(이 프레임에는 그리지 않음). 서버 거절 시 "등록하지 못했어요 — 표시한 행을 확인해 주세요" (교사·admin만)
- tab-bar: 모바일 전용 하단 탭바 1개(공통 규격). 고정 띠는 이 바 위. 데스크톱에는 두지 않는다 (교사·admin만)
- tab-item: 4개 "홈" · "시약" · "QR 스캔" · "기록". 활성 = "시약", "QR 스캔" 회색 '준비 중' (교사·admin만)
### 반영한 레퍼런스
- https://uibowl.io/website/%EC%82%AC%EB%B0%A9%EB%84%B7?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&imgId=cmu4rq9d8000xjm04y191pizg
- https://uibowl.io/name/%ED%8E%98%EC%9D%B4%ED%9E%88%EC%96%B4?patterns=%EC%B4%AC%EC%98%81%ED%95%98%EA%B8%B0&imgId=cmnfmykft001zl204e2svm4y5

## 상태 화면 17-doc-fail
센서 서류 읽기 실패·0개(프레임 17-doc-fail-mobile · 17-doc-fail-desktop). 교사·admin만. 7-doc-fail 모양 재사용 — 막다른 길 없이 '다시 올리기 / 직접 입력' 두 갈래. 핑크 없음(재고·안전 신호 아님).
예시 상태: 교사 김OO, "2026 센서 구입 영수증.pdf"를 읽었지만 센서·현미경 품목 0개 → 제목 "센서를 찾지 못했어요". (서류 자체를 읽지 못하면 제목만 "서류를 읽지 못했어요".)
모바일 활성 탭: "시약". 위→아래: nav-pill(× + "서류로 등록" + 학교명, ☰ 없음) → sensor-doc-add 머리 → ex-empty-state-card(실패 안내 + button-outline "직접 입력") → doc-upload(다시 올리기 카드) → tab-bar.
데스크톱 배치: app-sidebar("센서" 현재) | 본문 페이지 = sensor-doc-add 페이지 머리("‹ 센서" + "서류로 등록") → 가운데 단일 열 640: ex-empty-state-card → doc-upload → 본문 하단 고정 바(button-primary "AI로 읽기", 새 파일 전 비활성).
### 구성 요소
- app-sidebar: 데스크톱 전용. 공통 규격, 학교명 "샘플고등학교" + 교사 메뉴 + nav-account-menu (교사·admin만)
- sidebar-item: 데스크톱 전용. 교사 9개 / admin 11개. 현재 = "센서" (교사·admin만)
- nav-pill: 모바일 전용. 서류 머리 — 맨 왼쪽 × 닫기 + 제목 "서류로 등록" + 현재 학교명 "샘플고등학교" + nav-account-menu ▾. mobile-menu-button ☰ 없음 (교사·admin만)
- nav-account-menu: 닫힌 ▾ (교사·admin만)
- sensor-doc-add: 서류로 등록 흐름의 머리 묶음(모바일 heading-3 "서류로 등록" / 데스크톱 "‹ 센서" + heading-2 "서류로 등록") (교사·admin만)
- ex-empty-state-card: 실패 카드 1개(#ffffff, 1px #f0f0f0, rounded 24, 여백 24, 가운데 정렬). #141414 안내 아이콘 → heading-4 "센서를 찾지 못했어요" → body-sm #707070 "다른 서류를 올리거나 직접 입력해 주세요"(이유 2줄 이내) → 위 간격 24 button-outline "직접 입력"(→ sensor-form, 모바일 전용 화면 / 데스크톱 화면 17 + detail-drawer). 핑크·하늘색 없음 (교사·admin만)
- doc-upload: 다시 올리기 카드(17-doc-upload와 같은 모양, 고른 파일 없음): 업로드 아이콘 → "품의서·영수증을 올려 주세요" → caption "PDF·JPG·PNG 1개, 4MB까지 · 서버에 보관하지 않아요" → button-pill-soft "촬영하기" · "파일 선택" → (모바일) 카드 하단 button-primary "AI로 읽기"(비활성). 하늘색: 업로드 아이콘 #2b9fe0 (교사·admin만)
- button-outline: 카드 "직접 입력"(#ffffff, 1px #e0e0e0, 라벨 #141414, rounded 9999, 높이 44 이상) (교사·admin만)
- button-pill-soft: doc-upload "촬영하기" · "파일 선택", 데스크톱 "‹ 센서" (교사·admin만)
- button-primary: "AI로 읽기"(새 파일 전 비활성). 하늘색 없음 (교사·admin만)
- tab-bar: 모바일 전용 하단 탭바 1개(공통 규격). 데스크톱에는 두지 않는다 (교사·admin만)
- tab-item: 4개 "홈" · "시약" · "QR 스캔" · "기록". 활성 = "시약", "QR 스캔" 회색 '준비 중' (교사·admin만)
### 반영한 레퍼런스
- https://uibowl.io/name/%EC%95%84%EC%9D%B4%EC%BF%A0%EC%B9%B4?patterns=%EC%B4%AC%EC%98%81%ED%95%98%EA%B8%B0&imgId=cmp0t6j63000fl904x800o216

## 역할별 노출
앱 전체(로그인 후 화면) 기준 개수. runs/20261011-0813 표를 기준으로 이번 변경을 반영했다. 같은 화면의 상태 화면·모바일·데스크톱에 다시 나오는 같은 컴포넌트는 그 화면 1개로 센다(예: 화면 17의 sensor-doc-add는 데스크톱 머리 버튼·모바일 등록 시트 줄·17-doc-* 머리에 나와도 1).
이번 변경:
- sensor-doc-add = 화면 17 1(교사·admin만, 학생 0 — R5).
- doc-upload = 화면 7 1 + 화면 17(17-doc-upload·17-doc-fail) 1 → 교사·admin 2, 학생 0(R5).
- invite-more-menu · invite-cancel = 화면 8 1(admin만, 학생·교사 0 — 화면 8은 admin만 들어온다).
- mobile-menu-button · mobile-menu-sheet는 모든 역할에 있고(시트 안 항목만 역할별 — 학생은 관리 묶음 없음) rules.json roles 대상이 아니어서 표에 넣지 않는다. 시트의 "입고"·"사용자" 항목은 화면 이동 링크이고 stock-intake·user-manage 컴포넌트가 아니다.
- 학생: 화면 17에 "선택"·"등록"·"서류로 등록" 없음, 홈에 센서 타일·재주문 알림 없음, 13-no-access 학생 홈도 같음 → 모두 0.
sensor-type-sheet·sensor-model-suggest·catalog-fill-note·sensor-link·new-sensor-fields는 교사·admin만 여는 폼 안이라 학생 노출 0이며 rules.json roles 대상이 아니어서 표에 넣지 않는다. 화면 15는 로그인 전이라 표의 컴포넌트를 담지 않는다(shot-* 묶음). msds-entry = 화면 3 1 + 화면 10 상세 1(학생·교사·admin 모두 2, R4). 나머지 행은 runs/20261011-0813 값 그대로.

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
