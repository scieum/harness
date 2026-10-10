# S2 설계 — run 20261010-1340

대상 화면: 3 (시약 상세) · 4 (사용 기록) · 10 (사용 기록 내역) + 상태 화면 3-delete · 4-picker · 4-empty · 4-error · 4-past-date · 학교: 샘플고등학교 (input.json) · 키스크린: 4-mobile, 4-desktop, 3-delete-mobile
변경 사유: 2026-10-10 사용자 결정(개발 세션 요청 6) — ① 여러 시약 한 번에 사용 기록(화면 4, 데스크톱 = 드로어가 아닌 본문 페이지) ② 시약 삭제(화면 3에서만, 교사·admin, 기록은 남고 화면 10에 '삭제된 시약') ③ 수업 기록(화면 4 입력, 화면 10 표시·반 필터).
근거: docs/PRD.md §3·§4·§7(3·4·10), docs/story-service.md 결정 사항 2026-10-10 세 행("여러 시약 한 번에 사용 기록"·"시약 삭제"·"수업 기록")과 "사용일" 행, docs/design.md "Batch usage record"·"Class"·"Reagent delete"·"Usage date"·"Desktop shell", harness/rules.json 1.25(usage_batch, reagent_delete, class_info, usage_date, screens_required 3·4·10, variants 3·4, roles R1~R7(R5에 reagent-more-menu·reagent-delete), desktop_shell.heavy_pages·desktop_required 4, colors.accent usage-over-stock), research/s1-adopt.md.
기준 설계(틀): 최신 S4 승인본 = runs/20261008-0936 화면 3·4·10(데스크톱 웹앱), 상태 4-past-date 모양 = runs/20261007-0744. 화면 3·10은 승인본 구성을 그대로 두고 요청 6 결정분만 더한다. 화면 4는 한 시약 폼 → 여러 시약 목록으로 바뀌고, 데스크톱은 드로어 → 본문 페이지로 바뀐다.

색·폰트·모서리·간격은 docs/design.md와 harness/rules.json을 따른다. 허용 색 밖의 값(딤 반투명 검정 등)은 쓰지 않는다. 그림자는 쓰지 않는다(segmented-control-active 예외).
- 핑크 #d6246a·연핑크 #fbe9f0는 badge-low-stock, usage-over-stock 안에서만 쓴다(이번 대상 화면 기준). 시약 삭제 메뉴·삭제 확인 모달·삭제된 시약 표시·빈 상태·빈 사용량 안내·지난 날짜 안내에는 핑크를 쓰지 않는다.
- 하늘색 #2b9fe0·옅은 하늘색 #e6f4fc는 선택·현재 위치·아이콘·체크 표시에만 쓴다. 글자색 금지(그 위 글자 #141414). badge-low-stock·button-primary·usage-over-stock 안에는 쓰지 않는다.
- 삭제 확인의 "삭제" 버튼은 검정 button-primary(#141414 채움, #ffffff 글자) — 시약장 삭제와 같다.
학교 선택은 회원가입(화면 14)에만 있다. 대상 화면과 상태 화면에는 학교 선택·전환을 두지 않고 현재 학교명 "샘플고등학교"를 모바일은 nav-pill 안, 데스크톱은 app-sidebar 맨 위에 표시한다. 시약 고르기 목록·최근 수업 칩·사용 기록은 모두 샘플고등학교 것만 보인다(N1).
외부 서비스 연결 값은 서버에서만 다룬다. 어떤 화면에도 연결 값 입력 칸·외부 서비스 설정·AI 엔진 선택 UI·관련 문구를 두지 않는다(N2).
괄호 안 역할 표시가 없는 구성 요소는 학생·교사·admin 모두에게 보인다. reagent-more-menu·reagent-delete는 교사·admin만(학생 화면에는 그리지 않는다, R5). 여러 시약 사용 기록(화면 4 전체)·수업·반 필터·삭제된 시약 표시는 모든 역할이 같다.

모바일 공통(승인본 그대로): tab-bar는 화면 아래 가장자리 y 780~844(폭 390, 높이 64, rounded 0, #ffffff + 위쪽 1px #f0f0f0 선, 그림자 없음)에 붙고 tab-item 4개("홈"·"시약"·"QR 스캔"·"기록")를 같은 폭으로 채운다. 하단 고정 바·버튼은 tab-bar 바로 위. 시트는 tab-bar 위쪽 선 위에 붙는다(딤 없음, 1px #e0e0e0 테두리, 위쪽 rounded 24, 오른쪽 위 × 닫기). nav-pill = 얇은 헤더(뒤로가기 또는 워드마크 + 제목 + 학교명 + nav-account-menu ▾).
데스크톱 공통(1440×900, rules.json desktop_shell): nav-pill·tab-bar 없음.
- app-sidebar: 왼쪽 고정 열 폭 240, 높이 전체, rounded 0, #f3f3f3 채움, 오른쪽 1px #f0f0f0 선. 맨 위 "Lab_Stock" 워드마크 + 학교명 "샘플고등학교"(title #141414, 전환 없음) → sidebar-item 묶음 → 맨 아래 "{이름} · {역할}"(body-sm) + nav-account-menu ▾.
- sidebar-item: 아이콘 + body 라벨, 높이 44, rounded 0. 현재 항목 = #e6f4fc 채움 + #2b9fe0 아이콘, 라벨 #141414. 학생 5개(홈·시약·기록·시약장·QR 찾기) / 교사 8개(+ "관리" 입고·실험 매뉴얼·재주문 알림) / admin 10개(+ "학교 설정" 사용자·판매처).
- 본문 = 사이드바 오른쪽, 페이지 여백 32. data-table = ex-data-table-cell 머리행(caption #707070)·본문(body-sm), rounded 16 컨테이너 + 1px #f0f0f0 테두리, 선택 행 #e6f4fc. detail-drawer = 오른쪽 폭 480, 높이 전체, #ffffff, 왼쪽 1px #f0f0f0 선, 딤 없음, 오른쪽 위 × 닫기. 무거운 작업(화면 4) = 본문 페이지: 가운데 단일 열 폭 640, "라벨 | 입력" 행 사이 1px #f0f0f0 선, 주 동작은 본문 하단 고정 바(#ffffff, 위 1px #f0f0f0 선).
- 겹침: ex-modal-card는 확인에만(가운데, rounded 24, 1px #e0e0e0, 그림자·딤 없음). 모바일 고르기 시트(시약 고르기·반 필터·날짜)는 데스크톱에서 그 컨트롤에 붙은 드롭다운·팝오버(#ffffff, 1px #e0e0e0, rounded 24). ex-toast는 오른쪽 아래.
예시 데이터(공통): 오늘 = 2026-10-10. 샘플고등학교 시약 42종. 데스크톱 프레임 기준 역할 = 교사 "김OO · 교사"(3-delete도 교사).
- 화면 4 담은 시약 3개: 에탄올(현재 1,200 mL, 사용량 50 mL) · 페놀프탈레인 용액(현재 120 mL, 사용량 10 mL) · 수산화나트륨(현재 500 g, 사용량 5 g). 수업 = "1학년 2반 · 통합과학"(최근 칩으로 채움), 메모 빈 값.
- 최근 수업 칩 3개: "1학년 2반 · 통합과학" · "1학년 3반 · 통합과학" · "2학년 1반 · 화학".

## 화면 3
시약 상세. 학생·교사·admin 모두. 승인본(runs/20261008-0936 화면 3) 그대로 — 과산화수소, 재고 2병, 재주문 기준 자동 3병 + 재고 부족, 보관 위치 1번 시약장 · 우 1단, MSDS 있음. 바뀐 것 두 가지: ① 교사·admin에게 reagent-more-menu ⋯(메뉴 항목 reagent-delete "시약 삭제") ② "사용 기록" 버튼이 여러 시약 사용 기록(화면 4)을 이 시약이 담긴 채로 연다(데스크톱은 드로어 안 폼이 아니라 본문 페이지로 이동). 이 프레임에서 메뉴는 닫힘(⋯ 버튼만), 열린 흐름은 상태 화면 3-delete.
모바일 활성 탭: "시약". 위→아래: nav-pill → reagent-detail-card(오른쪽 위 (교사·admin) ⋯ · 시약명·재고 → reagent-location → reorder-threshold) → segmented-control "정보 / 사용 기록" → 표 → msds-entry → 하단 고정 "사용 기록"(+ 교사·admin "입고") → tab-bar.
데스크톱 배치: app-sidebar("시약" 현재) | 본문 = 화면 2 시약 목록 data-table("과산화수소" 행 #e6f4fc 선택) + 오른쪽 detail-drawer 480(머리 = (교사·admin) ⋯ + × → 시약명·상태 칩 → segmented-control → "항목 | 값" 행 → msds-entry → 아래 고정 동작 줄).
### 구성 요소
- app-sidebar: 데스크톱 전용. 공통 규격, 학교명 "샘플고등학교" + 역할별 메뉴 + nav-account-menu
- sidebar-item: 데스크톱 전용. 학생 5개 / 교사 8개 / admin 10개. 현재 = "시약"
- nav-pill: 모바일 전용. 뒤로가기(화면 2) + 제목 "시약 상세" + 현재 학교명 "샘플고등학교" + nav-account-menu ▾. 학교 전환 없음. 하늘색: 뒤로가기 아이콘 #2b9fe0
- nav-account-menu: 모바일 = 학교명 옆 ▾, 데스크톱 = app-sidebar 맨 아래. 메뉴 항목 "로그아웃" 1개. 하늘색 없음
- data-table: 데스크톱 전용. 드로어 뒤 화면 2 시약 표(열·정렬·페이지 번호 화면 2와 같음), 선택 행 "과산화수소" #e6f4fc. 행 끝에 삭제·더보기 없음(삭제는 화면 3 한 곳에만)
- detail-drawer: 데스크톱 전용. 폭 480, 높이 900, #ffffff, 왼쪽 1px #f0f0f0 선, 여백 24. 머리 오른쪽 = (교사·admin) reagent-more-menu ⋯ + 그 오른쪽 × 닫기(각 누름 영역 44 이상, 사이 8). 위→아래: heading-3 "과산화수소" → 상태 칩 줄(badge-low-stock "재고 부족" + storage-class-chip "산화제" 보기 전용) → segmented-control "정보 / 사용 기록" → "항목 | 값" 2열 행: 현재 재고 "2병"(display) · 입고일 · reagent-location 행 · reorder-threshold 행 → msds-entry → 아래 고정 동작 줄: button-primary "사용 기록"(→ 화면 4 본문 페이지, 과산화수소가 담긴 채) + (교사·admin) button-outline "입고". 하늘색: × 아이콘 #2b9fe0
- reagent-detail-card: 모바일 = 상단 요약 카드(#ffffff, 1px #f0f0f0 테두리, rounded 24, 여백 24): 시약명(title) + badge-low-stock, 카드 오른쪽 위 (교사·admin) reagent-more-menu ⋯, 현재 재고 display "2" + 단위 "병", 입고일 caption, 그 아래 reagent-location 줄·reorder-threshold 줄. 데스크톱 = detail-drawer 안 "항목 | 값" 행으로 같은 내용. 하늘색 없음
- reagent-more-menu: ⋯ 아이콘 버튼(#141414 아이콘, 채움 없음, 누름 영역 44 이상). 모바일 = reagent-detail-card 오른쪽 위, 데스크톱 = detail-drawer 머리 × 왼쪽. 누르면 버튼 아래 작은 메뉴(#ffffff, rounded 24, 1px #f0f0f0 테두리, 여백 8, 그림자 없음)에 reagent-delete 1개. 이 프레임에서는 닫힘(버튼만). 핑크 없음. 하늘색: 누른 동안 버튼 뒤 #e6f4fc 원 (교사·admin만)
- reagent-delete: reagent-more-menu 메뉴 항목 "시약 삭제"(body #141414, 왼쪽 휴지통 아이콘 #141414, 높이 44). 누르면 삭제 확인 ex-modal-card(상태 화면 3-delete). 이 프레임에서는 메뉴가 닫혀 보이지 않는다. 핑크·하늘색 없음 (교사·admin만)
- badge-low-stock: 재고 2병 < 재주문 기준 3병이라 "재고 부족"(#d6246a 채움, #ffffff label, rounded 9999). 모바일 = 시약명 옆, 데스크톱 = 드로어 상태 칩 줄. 하늘색 없음
- storage-class-chip: 데스크톱 드로어 상태 칩 줄 "산화제"(보기 전용, #f3f3f3 채움, label #141414, rounded 9999). 하늘색·핑크 없음
- reagent-location: caption "보관 위치"(#707070) + 값 "cabinet-number(1) 1번 시약장 · 우 1단"(body #141414). 칸이 없으면 "칸 없음"(#707070). 교사·admin은 줄 오른쪽 location-edit. 학생은 값만
- cabinet-number: reagent-location 값 앞 작은 원(#ffffff, 1px #e0e0e0, rounded 9999) 안 숫자 "1"(label #141414). 핑크·하늘색 글자 없음
- location-edit: reagent-location 줄 오른쪽 button-pill-soft "위치 바꾸기"(#f3f3f3, 라벨 #141414, rounded 9999, 높이 44 이상). 모바일 = 3-location 바텀시트, 데스크톱 = 버튼에 붙은 팝오버(승인본 그대로) (교사·admin만)
- reorder-threshold: caption "재주문 기준"(#707070) + 값 "3병" + auto-threshold-badge "자동", 줄 아래 caption(#707070) "최근 사용량으로 계산했어요". 학생은 값·배지·캡션만
- auto-threshold-badge: 값 옆 pill "자동"(#f3f3f3 채움, rounded 9999, label #141414). 핑크·하늘색 없음
- threshold-edit: reorder-threshold 값 오른쪽 연필 아이콘(누름 영역 44 이상) → 숫자 text-input + button-primary "저장"(승인본 그대로). 하늘색: 연필 아이콘 #2b9fe0 (교사·admin만)
- text-input: threshold-edit 편집 상태 숫자 입력(#f0f0f0, rounded 16, 포커스 링 2px #141414) (교사·admin만)
- segmented-control: "정보 / 사용 기록" 두 탭. 모바일 = 요약 아래, 데스크톱 = 드로어 상태 칩 아래
- segmented-control-active: 활성 탭 흰 pill. 하늘색: 활성 탭 아래 #2b9fe0 인디케이터(글자 #141414)
- ex-data-table-cell: "정보" 탭 = 시약 속성 라벨-값 표, "사용 기록" 탭 = 날짜·사용자·사용량 3열 표. 하늘색: 가장 최근 사용 기록 행 배경 #e6f4fc
- msds-entry: msds-qr-tile + button-pill-soft "MSDS 보기 ›"(→ 화면 16). 학생·교사·admin 모두 1개. 하늘색: › 아이콘 #2b9fe0
- msds-qr-tile: msds-entry 안 QR 타일(#ffffff, 1px #f0f0f0, rounded 24, QR 1:1 rounded 0, 아래 라벨 "QR로 MSDS 열기")
- button-primary: 하단 고정 "사용 기록"(→ 화면 4, 이 시약이 usage-batch-list에 담긴 채 시작, 모든 역할), threshold-edit "저장"(교사·admin). #141414 채움, #ffffff 글자, rounded 9999, 높이 44 이상. 하늘색 없음
- button-outline: "사용 기록" 옆 "입고"(→ 화면 7) (교사·admin만)
- ex-toast: "재주문 기준을 3병으로 바꿨어요" / "보관 위치를 바꿨어요". 모바일 tab-bar 위, 데스크톱 오른쪽 아래. 하늘색: 완료 체크 아이콘 #2b9fe0 (교사·admin만)
- tab-bar: 모바일 전용 하단 탭바 1개(공통 규격). 데스크톱에는 두지 않는다. 하늘색: 활성 tab-item 아이콘 #2b9fe0만
- tab-item: "홈" · "시약" · "QR 스캔" · "기록" 4개. 활성 = "시약", 비활성 3개 #707070
### 반영한 레퍼런스
- https://uibowl.io/name/%EC%97%90%EC%9D%B4%EB%8B%B7?patterns=%ED%8E%B8%EC%A7%91%C2%B7%EC%88%98%EC%A0%95%ED%95%98%EA%B8%B0&patternName=%EC%B5%9C%EA%B7%BC%EA%B8%B0%EB%A1%9D%28%EC%82%AD%EC%A0%9C%29
- https://uibowl.io/name/%EC%BA%90%EC%8B%9C%EC%9B%8C%ED%81%AC?patterns=%ED%8E%B8%EC%A7%91%C2%B7%EC%88%98%EC%A0%95%ED%95%98%EA%B8%B0&patternName=%EA%B2%8C%EC%8B%9C%EA%B8%80%20%EC%82%AD%EC%A0%9C

## 상태 화면 3-delete
시약 삭제 확인(프레임 3-delete-mobile · 3-delete-desktop). 교사·admin만 이 상태에 온다(학생 화면에는 ⋯ 자체가 없다). 흐름: ⋯ → 메뉴 "시약 삭제" → 이 확인 모달 → "삭제" → ex-toast "시약을 삭제했어요" → 화면 2(목록·시약장·홈·재주문 알림에서 빠짐). 되돌리기 없음. 핑크 없음 — 삭제는 재고·안전 신호가 아니다.
예시 상태: 과산화수소. 메뉴에서 "시약 삭제"를 누른 직후라 메뉴는 닫혔고, ⋯ 버튼은 눌린 표시로 남고, 확인 모달이 열린 상태. 뒤 화면은 화면 3 그대로 보인다(딤 없음).
모바일: 모달 = tab-bar 위 시트 모양(위쪽 rounded 24). 데스크톱 배치: app-sidebar("시약" 현재) | 화면 2 data-table("과산화수소" 선택) + 오른쪽 detail-drawer(머리 ⋯ 눌린 표시) 위 가운데 ex-modal-card.
### 구성 요소
- app-sidebar: 데스크톱 전용. 공통 규격, 학교명 "샘플고등학교" + 교사 메뉴 + "김OO · 교사" + nav-account-menu (교사·admin만)
- sidebar-item: 데스크톱 전용. 교사 8개 / admin 10개. 현재 = "시약" (교사·admin만)
- nav-pill: 모바일 전용. 화면 3 nav-pill 그대로 — 뒤로가기 + "시약 상세" + 현재 학교명 "샘플고등학교" + nav-account-menu ▾ (교사·admin만)
- nav-account-menu: 닫힌 ▾ (교사·admin만)
- data-table: 데스크톱 전용. 모달 뒤 화면 2 시약 표, 선택 행 "과산화수소" #e6f4fc (교사·admin만)
- detail-drawer: 데스크톱 전용. 모달 뒤 화면 3 드로어 그대로(과산화수소) (교사·admin만)
- reagent-detail-card: 모바일 전용. 모달 뒤 화면 3 요약 카드 그대로(과산화수소 · 2병 · badge-low-stock) (교사·admin만)
- reagent-more-menu: 모바일 = reagent-detail-card 오른쪽 위, 데스크톱 = 드로어 머리 × 왼쪽의 ⋯ 버튼. 메뉴는 닫힘. 눌린 표시 = 버튼 뒤 #e6f4fc 원(아이콘 #141414). 핑크 없음 (교사·admin만)
- badge-low-stock: 모달 뒤 시약명 옆 "재고 부족"(#d6246a 채움, #ffffff label). 모달 안에는 없음 (교사·admin만)
- ex-modal-card: 삭제 확인 1개(#ffffff, 1px #e0e0e0 테두리, 여백 24, 그림자·딤 없음, 오른쪽 위 × 닫기 누름 영역 44 이상). 모바일 = tab-bar 위 시트(전폭, 위쪽 rounded 24), 데스크톱 = 화면 가운데 폭 440, rounded 24. 위→아래: heading-3 "'과산화수소' 시약을 삭제할까요?" → body #141414 "목록·시약장·재주문 알림에서 사라져요. 사용·입고 기록은 남아요." → body-sm #707070 "되돌릴 수 없어요." → 버튼 줄(위 간격 24): 왼쪽 button-outline "취소" + 오른쪽 button-primary "삭제"(1:1, 사이 8). × 와 "취소"는 같은 동작(모달만 닫힘). 핑크·하늘색 없음 (교사·admin만)
- button-outline: 모달 "취소"(#ffffff, 1px #e0e0e0, 라벨 #141414, rounded 9999, 높이 44 이상) (교사·admin만)
- button-primary: 모달 "삭제"(검정 — #141414 채움, #ffffff 글자, rounded 9999, 높이 44 이상, 시약장 삭제와 같은 모양). 핑크·하늘색 없음 (교사·admin만)
- ex-toast: "삭제" 뒤 "시약을 삭제했어요"(모바일 tab-bar 위, 데스크톱 오른쪽 아래) → 화면 2. 이 프레임에는 그리지 않는다. 하늘색: 완료 체크 아이콘 #2b9fe0 (교사·admin만)
- tab-bar: 모바일 전용 하단 탭바 1개(공통 규격). 시트는 이 바 위쪽 선 위에 붙는다. 데스크톱에는 두지 않는다. 하늘색: 활성 tab-item 아이콘 #2b9fe0만 (교사·admin만)
- tab-item: 4개 "홈" · "시약" · "QR 스캔" · "기록". 활성 = "시약" (교사·admin만)
### 반영한 레퍼런스
- https://uibowl.io/name/%EC%BA%90%EC%8B%9C%EC%9B%8C%ED%81%AC?patterns=%ED%8E%B8%EC%A7%91%C2%B7%EC%88%98%EC%A0%95%ED%95%98%EA%B8%B0&patternName=%EA%B2%8C%EC%8B%9C%EA%B8%80%20%EC%82%AD%EC%A0%9C
- https://uibowl.io/name/%EC%91%A5%EC%91%A5%EC%B0%B0%EC%B9%B5?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&patternName=%EC%9D%BC%EA%B8%B0%2F%EC%88%98%EC%9C%A0%ED%85%80%20%ED%83%AD%20-%20%EC%88%98%EC%9C%A0%ED%85%80%20-%20%EB%82%B4%EC%97%AD%EC%82%AD%EC%A0%9C
- https://uibowl.io/name/%EC%97%90%EC%9D%B4%EB%8B%B7?patterns=%ED%8E%B8%EC%A7%91%C2%B7%EC%88%98%EC%A0%95%ED%95%98%EA%B8%B0&patternName=%EC%B5%9C%EA%B7%BC%EA%B8%B0%EB%A1%9D%28%EC%82%AD%EC%A0%9C%29

## 화면 4
여러 시약 한 번에 사용 기록. 학생·교사·admin 모두(둘러보기는 잠금 그대로). 진입: 화면 3 "사용 기록"(그 시약이 담긴 채 시작) · 홈 quick-action "사용 기록 입력"·데스크톱 sidebar-item "기록"에서 "사용 기록 입력"(빈 채 시작 = 상태 화면 4-empty). 시약마다 사용량만 적고, 사용일·수업·메모는 묶음 공통. 사용자 = 로그인한 사람(입력 칸 없음). "사용 기록 저장 · N개" 한 번 = 한 트랜잭션(하나라도 실패하면 전부 취소).
예시 상태(4-mobile · 4-desktop): 공통 예시 데이터의 3개가 담기고 사용량이 모두 정상, 사용일 = 오늘 "2026-10-10"(past-date-note 숨김), 수업 "1학년 2반 · 통합과학", 저장 버튼 활성 "사용 기록 저장 · 3개".
모바일 활성 탭: "기록". 위→아래: nav-pill → 머리 줄(heading-4 "담은 시약 3개" 왼쪽 + reagent-add 오른쪽) → usage-batch-list(usage-item-row 카드 3장, 사이 12) → 공통 칸(사용일 → 수업 → 메모, 사이 16) → 하단 고정 저장 바(tab-bar 바로 위) → tab-bar. 목록·공통 칸은 저장 바 위에서 스크롤. 좌우 여백 16.
데스크톱 배치: app-sidebar("기록" 현재) | 본문 페이지(드로어 아님) = 페이지 머리(왼쪽 heading-2 "사용 기록" + caption "여러 시약을 한 번에 기록해요") → 가운데 단일 열 폭 640: reagent-add 검색 칸(아래로 reagent-picker 드롭다운, 이 프레임에서는 닫힘) → usage-batch-list(머리 "담은 시약 3개" + data-table 시약명 | 현재 재고 | 사용량 | 빼기) → "라벨 | 입력" 행 사용일 · 수업 · 메모 → 본문 하단 고정 바(왼쪽 body-sm "담은 시약 3개" / 오른쪽 button-primary "사용 기록 저장 · 3개").
### 구성 요소
- app-sidebar: 데스크톱 전용. 공통 규격, 학교명 "샘플고등학교" + 역할별 메뉴 + nav-account-menu
- sidebar-item: 데스크톱 전용. 학생 5개 / 교사 8개 / admin 10개. 현재 = "기록"
- nav-pill: 모바일 전용. 뒤로가기(들어온 화면) + 제목 "사용 기록" + 현재 학교명 "샘플고등학교" + nav-account-menu ▾. 하늘색: 뒤로가기 아이콘 #2b9fe0
- nav-account-menu: 모바일 = 학교명 옆 ▾, 데스크톱 = app-sidebar 맨 아래. "로그아웃" 1개. 하늘색 없음
- reagent-add: 시약 담기 진입. 모바일 = 머리 줄 오른쪽 button-pill-soft "+ 시약 추가"(#f3f3f3, 라벨 #141414, rounded 9999, 높이 44 이상) → reagent-picker 바텀시트(상태 화면 4-picker). 데스크톱 = 640 열 맨 위 검색 칸(text-input 모양 #f0f0f0, rounded 16, 왼쪽 + 아이콘, placeholder "시약 추가 — 이름으로 찾기", 포커스 링 2px #141414) → 칸 아래 reagent-picker 드롭다운. 하늘색: + 아이콘 #2b9fe0
- reagent-picker: 시약 고르기 목록(이 프레임에서는 닫힘). 모바일 바텀시트 / 데스크톱 검색 칸 아래 드롭다운. 구성은 상태 화면 4-picker
- usage-batch-list: 담은 시약 목록 1개. 머리 heading-4 "담은 시약 3개". 모바일 = usage-item-row 카드 세로 쌓기(사이 12). 데스크톱 = data-table(폭 640) 머리행 "시약명 · 현재 재고 · 사용량 · (빼기)", 본문 행 = usage-item-row. 담은 순서대로(화면 3에서 온 시약이 맨 위)
- usage-item-row: 담은 시약 1개. 모바일 = 카드(#f3f3f3, rounded 16, 여백 16): 1줄 시약명(title #141414) + 오른쪽 위 조용한 텍스트 동작 "빼기"(link #141414, 누름 영역 44 이상, 확인 없음) / 2줄 caption #707070 "현재 1,200 mL" / 3줄 사용량 숫자 text-input(카드 위라 #ffffff 채움, rounded 16, 값 "50") + 오른쪽 단위 caption #707070 "mL"(시약 단위 고정) / 그 아래 오류 문구 자리(정상일 땐 비움, 상태 화면 4-error). 데스크톱 = data-table 한 행: 시약명(title) · 현재 재고(body-sm #707070 "1,200 mL") · 사용량(숫자 text-input 폭 120 + 단위) · "빼기"(link #141414). 오류는 그 행 바로 아래 줄. 예시 3행: 에탄올 1,200 mL / 50 · 페놀프탈레인 용액 120 mL / 10 · 수산화나트륨 500 g / 5. 핑크 없음(정상). 하늘색: 포커스된 행의 입력 아래 없음 — 포커스는 2px #141414 링
- text-input: usage-item-row 사용량 숫자 입력, 메모(placeholder "메모 (선택)"), class-select 수업명. #f0f0f0(카드 안 사용량은 #ffffff), 테두리 없음, rounded 16, 포커스 링 2px #141414
- usage-date: 공통 칸 첫 줄 "사용일"(필수) 날짜 칸 — 화면 7 입고일과 같은 모양(text-input 모양 #f0f0f0, rounded 16, 값 "2026-10-10", 오른쪽 달력 아이콘). 기본 오늘, 오늘 이후 흐림(#adadad, 누름 없음). 모바일 = 누르면 날짜 고르기 시트(tab-bar 위, × 닫기, 하단 button-primary "완료"), 데스크톱 = "사용일 | [날짜 칸]" 행, 칸 아래 달력 팝오버. 오늘이 아니면 past-date-note(상태 화면 4-past-date). 하늘색: 달력 아이콘 #2b9fe0, 선택 날짜 원 #e6f4fc + 1px #2b9fe0 테두리(숫자 #141414)
- class-select: 공통 칸 둘째 줄 "수업 (선택)". 위에 recent-class-chip 줄 → 학년 select(text-input 모양, "1학년" ▾, 목록 = 샘플고등학교 학교급 고등학교 1~3학년) + 반 select("2반" ▾, 1~20반) + 수업명 text-input(값 "통합과학", placeholder "수업명 (예: 통합과학)", 20자). 셋 다 비워도 저장된다. 모바일 = 학년·반 반씩 한 줄(사이 8) + 수업명 아래 전폭. 데스크톱 = "수업 | [학년▾][반▾][수업명]" 한 행. 하늘색: ▾ 아이콘 #2b9fe0
- recent-class-chip: class-select 위 caption #707070 "최근" + pill 최대 3개 가로 한 줄(모바일 넘치면 가로 스크롤): "1학년 2반 · 통합과학"(선택됨) · "1학년 3반 · 통합과학" · "2학년 1반 · 화학". 미선택 = #f3f3f3 채움, label #141414, rounded 9999, 높이 44 이상. 누르면 세 칸이 채워진다. 하늘색: 선택 칩 #e6f4fc 채움 + 1px #2b9fe0 테두리(글자 #141414)
- past-date-note: 사용일이 오늘이 아닐 때만 저장 바 바로 위 무채색 한 줄(이 프레임에서는 숨김, 상태 화면 4-past-date)
- button-primary: 저장 바 "사용 기록 저장 · 3개"(#141414 채움, #ffffff 글자, rounded 9999, 높이 44 이상). 모바일 = tab-bar 바로 위 고정 바(#ffffff, 위 1px #f0f0f0 선, 여백 12·16) 안 전폭, 데스크톱 = 본문 하단 고정 바 오른쪽. 담은 시약 0개이거나 오류 행이 있으면 비활성. 날짜 시트 "완료"도 같은 모양. 하늘색 없음
- ex-toast: 저장 직후 "3개 시약 사용을 기록했어요" → 들어온 화면으로(화면 3에서 왔으면 화면 3). 서버 거절이면 "저장하지 못했어요 — 표시한 시약을 확인해 주세요"(아무것도 저장 안 됨, 문제 행 표시). 모바일 tab-bar 위, 데스크톱 오른쪽 아래. 이 프레임에는 그리지 않는다. 하늘색: 완료 체크 아이콘 #2b9fe0
- data-table: 데스크톱 전용. usage-batch-list의 표(위 정의). rounded 16 컨테이너, 1px #f0f0f0 테두리, 머리행 caption #707070. 정렬 없음
- ex-data-table-cell: 데스크톱 data-table 머리행·셀 chrome, 행 구분 1px #f0f0f0 선
- tab-bar: 모바일 전용 하단 탭바 1개(공통 규격). 저장 바는 이 바 위. 데스크톱에는 두지 않는다. 하늘색: 활성 tab-item 아이콘 #2b9fe0만
- tab-item: "홈" · "시약" · "QR 스캔" · "기록" 4개. 활성 = "기록", 비활성 3개 #707070
### 반영한 레퍼런스
- https://uibowl.io/name/%EB%9D%BC%EC%9A%B4%EC%A6%88?patterns=%EC%9E%A5%EB%B0%94%EA%B5%AC%EB%8B%88&imgId=cmunlyn8s0005l804bcsbpzcr
- https://uibowl.io/name/%EA%B3%A8%ED%94%84%EC%A1%B4?patterns=%EC%9E%A5%EB%B0%94%EA%B5%AC%EB%8B%88&imgId=cmunkg4m30025l904yg6x2ysv
- https://uibowl.io/name/%EC%B9%B4%EC%B9%B4%EC%98%A4%EA%B3%A8%ED%94%84%EC%98%88%EC%95%BD?patterns=%EA%B2%80%EC%83%89&imgId=cmtwluex6011ijl043f9n1umq
- https://uibowl.io/name/%EB%A1%AF%EB%8D%B0%EB%B0%B1%ED%99%94%EC%A0%90?patterns=%EA%B2%80%EC%83%89&imgId=b3qcqg4mcd3ehb8r9e2ywhjt

## 상태 화면 4-picker
시약 고르기가 열린 상태(프레임 4-picker-mobile · 4-picker-desktop). 모든 역할 같다. 샘플고등학교 시약만 나온다.
예시 상태: 화면 3(에탄올)에서 들어와 에탄올 1개가 담긴 상태에서 "+ 시약 추가"를 누름. 목록 = 최근 사용한 시약 먼저 — 에탄올("담음") · 페놀프탈레인 용액(체크) · 수산화나트륨(체크) · 염산 · 증류수 · 질산은. 선택 2개.
모바일: tab-bar 위 바텀시트(딤 없음, 뒤에 화면 4 "담은 시약 1개"가 보임). 데스크톱 배치: app-sidebar("기록" 현재) | 본문 페이지 640 열 — reagent-add 검색 칸 포커스 + 바로 아래 붙은 reagent-picker 드롭다운(폭 640, 최대 높이 360, 안에서 스크롤), 그 아래 usage-batch-list 표(드롭다운에서 체크한 행이 바로 표에 추가되어 3행).
### 구성 요소
- app-sidebar: 데스크톱 전용. 공통 규격, 학교명 "샘플고등학교" + 역할별 메뉴 + nav-account-menu
- sidebar-item: 데스크톱 전용. 학생 5개 / 교사 8개 / admin 10개. 현재 = "기록"
- nav-pill: 모바일 전용. 화면 4 nav-pill 그대로 — 뒤로가기 + "사용 기록" + 현재 학교명 "샘플고등학교" + nav-account-menu ▾
- nav-account-menu: 닫힌 ▾
- reagent-add: 모바일 = 시트 뒤 "+ 시약 추가"(누른 상태), 데스크톱 = 포커스된 검색 칸(2px #141414 링, 빈 값 placeholder "시약 추가 — 이름으로 찾기"). 하늘색: + 아이콘 #2b9fe0
- reagent-picker: 시약 고르기 1개. 모바일 = 바텀시트(#ffffff, 1px #e0e0e0, 위쪽 rounded 24, 여백 24, 오른쪽 위 × 닫기): heading-3 "시약 추가" → 검색 text-input "시약명 검색"(#f0f0f0, rounded 16) → caption #707070 "최근 사용한 시약" → 행 목록(행 높이 56, 사이 1px #f0f0f0 선): 왼쪽 시약명(title) + 아래 caption #707070 "현재 1,200 mL", 오른쪽 체크 원(누름 영역 44 이상). 이미 담은 시약 = 체크 대신 caption #707070 "담음", 누름 없음. 체크한 행 = #e6f4fc 배경 + #2b9fe0 채운 체크 원(흰 체크). 하단 고정 button-primary 전폭 "2개 담기"(0개면 비활성). 데스크톱 = 검색 칸 아래 드롭다운(#ffffff, 1px #e0e0e0, rounded 24, 여백 8): caption "최근 사용한 시약" + 같은 행(왼쪽 체크박스 원 + 시약명 + 오른쪽 "현재 …"), 행을 누르면 바로 표에 추가되고 체크 표시가 남는다(여러 개 가능, "담음"은 회색), 드롭다운 아래 끝 조용한 텍스트 동작 "닫기". 하늘색: 체크한 행 #e6f4fc, 체크 원 #2b9fe0, 검색 아이콘 #2b9fe0
- usage-batch-list: 모바일 = 시트 뒤 "담은 시약 1개" + usage-item-row 1장(에탄올). 데스크톱 = 드롭다운 아래 표 "담은 시약 3개"(에탄올 · 페놀프탈레인 용액 · 수산화나트륨, 새로 추가된 두 행 사용량 빈 칸)
- usage-item-row: 모바일 = 시트 뒤 에탄올 카드, 데스크톱 = 표 행 3개(새 행은 사용량 빈 값 — 아직 오류 표시 없음, 저장을 누르거나 칸을 떠날 때 "사용량을 적어 주세요")
- text-input: 시트 검색 "시약명 검색", 행 사용량 입력(#f0f0f0, rounded 16, 포커스 링 2px #141414)
- data-table: 데스크톱 전용. usage-batch-list 표(시약명 · 현재 재고 · 사용량 · 빼기)
- button-primary: 모바일 시트 "2개 담기"(#141414 채움, #ffffff 글자, rounded 9999, 높이 44 이상), 뒤 저장 바 "사용 기록 저장 · 1개". 데스크톱 하단 고정 바 "사용 기록 저장 · 3개"(새 두 행 사용량이 비어 비활성). 하늘색 없음
- tab-bar: 모바일 전용 하단 탭바 1개(공통 규격). 시트는 이 바 위. 데스크톱에는 두지 않는다. 하늘색: 활성 tab-item 아이콘 #2b9fe0만
- tab-item: 4개 "홈" · "시약" · "QR 스캔" · "기록". 활성 = "기록"
### 반영한 레퍼런스
- https://uibowl.io/name/%EB%A1%AF%EB%8D%B0%EB%B0%B1%ED%99%94%EC%A0%90?patterns=%EA%B2%80%EC%83%89&imgId=b3qcqg4mcd3ehb8r9e2ywhjt
- https://uibowl.io/name/%EB%9D%BC%EC%9A%B4%EC%A6%88?patterns=%EC%9E%A5%EB%B0%94%EA%B5%AC%EB%8B%88&imgId=cmunlyn8s0005l804bcsbpzcr

## 상태 화면 4-empty
담은 시약이 없는 첫 상태(프레임 4-empty-mobile · 4-empty-desktop) — 홈·기록에서 들어왔을 때. 모든 역할 같다. 핑크 없음.
예시 상태: 담은 시약 0개. 사용일 오늘 "2026-10-10", 수업·메모 빈 값(최근 칩 3개는 보임). 저장 버튼 비활성.
모바일 위→아래: nav-pill → 머리 heading-4 "담은 시약 0개" → ex-empty-state-card(안에 reagent-add) → 공통 칸 → 하단 고정 저장 바 → tab-bar. 데스크톱 배치: app-sidebar("기록" 현재) | 본문 페이지 640 열 — reagent-add 검색 칸 → usage-batch-list 표(머리행만 남기고 표 안에 ex-empty-state-card) → "라벨 | 입력" 행 사용일 · 수업 · 메모 → 하단 고정 바(비활성 저장).
### 구성 요소
- app-sidebar: 데스크톱 전용. 공통 규격, 학교명 "샘플고등학교" + 역할별 메뉴 + nav-account-menu
- sidebar-item: 데스크톱 전용. 학생 5개 / 교사 8개 / admin 10개. 현재 = "기록"
- nav-pill: 모바일 전용. 뒤로가기(홈) + "사용 기록" + 현재 학교명 "샘플고등학교" + nav-account-menu ▾
- nav-account-menu: 닫힌 ▾
- usage-batch-list: 머리 "담은 시약 0개". 모바일 = 카드 자리에 ex-empty-state-card, 데스크톱 = 표 머리행 아래 ex-empty-state-card
- ex-empty-state-card: 빈 상태 카드(#ffffff, 1px #f0f0f0 테두리, rounded 24, 여백 24, 가운데 정렬). #141414 플라스크 아이콘 → heading-4 "시약을 골라 주세요" → body-sm #707070 "실험에 쓴 시약을 모두 담고 한 번에 저장해요" → 모바일 = 카드 안 reagent-add, 데스크톱 = body-sm #707070 "위 검색 칸에서 시약을 찾아 담아 주세요". 핑크·하늘색 없음(아이콘 #141414)
- reagent-add: 모바일 = 빈 상태 카드 안 button-pill-soft "+ 시약 추가"(#f3f3f3, 라벨 #141414, rounded 9999, 높이 44 이상) → reagent-picker 시트. 데스크톱 = 640 열 맨 위 검색 칸(placeholder "시약 추가 — 이름으로 찾기") → reagent-picker 드롭다운. 하늘색: + 아이콘 #2b9fe0
- usage-date: "사용일" 값 "2026-10-10"(화면 4와 같은 모양). 하늘색: 달력 아이콘 #2b9fe0
- class-select: "수업 (선택)" 학년·반 select 빈 값("학년" ▾ · "반" ▾, #adadad placeholder) + 수업명 placeholder "수업명 (예: 통합과학)". 하늘색: ▾ 아이콘 #2b9fe0
- recent-class-chip: caption "최근" + 3개 미선택 pill(#f3f3f3, label #141414). 하늘색 없음(선택 없음)
- text-input: 메모(빈 값, placeholder "메모 (선택)"), 수업명(#f0f0f0, rounded 16)
- data-table: 데스크톱 전용. usage-batch-list 표 머리행(시약명 · 현재 재고 · 사용량 · 빼기)만 + 표 안 빈 상태 카드
- button-primary: 저장 바 "사용 기록 저장" 비활성(#141414 채움 위 흐림 처리 대신 #e0e0e0 채움 + 라벨 #adadad, rounded 9999, 높이 44 이상). 모바일 tab-bar 바로 위, 데스크톱 하단 고정 바 오른쪽. 하늘색 없음
- tab-bar: 모바일 전용 하단 탭바 1개(공통 규격). 데스크톱에는 두지 않는다. 하늘색: 활성 tab-item 아이콘 #2b9fe0만
- tab-item: 4개 "홈" · "시약" · "QR 스캔" · "기록". 활성 = "기록"
### 반영한 레퍼런스
- https://uibowl.io/name/%EA%B3%A8%ED%94%84%EC%A1%B4?patterns=%EC%9E%A5%EB%B0%94%EA%B5%AC%EB%8B%88&imgId=cmunkg4m30025l904yg6x2ysv
- https://uibowl.io/name/%EB%A1%AF%EB%8D%B0%EB%B0%B1%ED%99%94%EC%A0%90?patterns=%EA%B2%80%EC%83%89&imgId=b3qcqg4mcd3ehb8r9e2ywhjt

## 상태 화면 4-error
사용량 오류가 있는 상태(프레임 4-error-mobile · 4-error-desktop). 모든 역할 같다. 핑크는 usage-over-stock 안에서만 — 사용량이 재고보다 많다 = 재고 부족 신호.
예시 상태: 화면 4와 같은 3개. 페놀프탈레인 용액 사용량 "150"(현재 120 mL) → 그 행 아래 usage-over-stock. 수산화나트륨 사용량 빈 값 → 입력 칸 2px #141414 링 + muted 안내. 에탄올은 정상. 저장 버튼 비활성.
모바일 위→아래: 화면 4와 같고 오류 행 아래에 줄이 붙는다. 데스크톱 배치: app-sidebar("기록" 현재) | 본문 페이지 640 열 — 화면 4와 같은 순서, data-table의 페놀프탈레인 용액 행 바로 아래 전폭 usage-over-stock 줄, 수산화나트륨 행 아래 muted 안내 줄.
### 구성 요소
- app-sidebar: 데스크톱 전용. 공통 규격, 학교명 "샘플고등학교" + 역할별 메뉴 + nav-account-menu
- sidebar-item: 데스크톱 전용. 학생 5개 / 교사 8개 / admin 10개. 현재 = "기록"
- nav-pill: 모바일 전용. 화면 4 nav-pill 그대로 — 뒤로가기 + "사용 기록" + 현재 학교명 "샘플고등학교" + nav-account-menu ▾
- nav-account-menu: 닫힌 ▾
- reagent-add: 모바일 머리 줄 "+ 시약 추가", 데스크톱 검색 칸(화면 4와 같음). 하늘색: + 아이콘 #2b9fe0
- usage-batch-list: "담은 시약 3개" + 행 3개(화면 4와 같은 구성)
- usage-item-row: ① 에탄올 50 mL 정상 ② 페놀프탈레인 용액 — 사용량 칸 값 "150"(입력 칸 모양 그대로) + 행 아래(간격 8) usage-over-stock ③ 수산화나트륨 — 사용량 칸 빈 값 + 2px #141414 테두리 + 그 아래 body-sm #707070 "사용량을 적어 주세요"(핑크 없음). 모바일 = 카드 안 맨 아래, 데스크톱 = 행 바로 아래 줄
- usage-over-stock: 페놀프탈레인 용액 행 아래 경고 줄 1개(mix-warning 모양): #fbe9f0 채움, rounded 16, 여백 12·16, 왼쪽 #d6246a 경고 아이콘 + body-sm #141414 "재고 120 mL보다 많아요". 모바일 = 카드 안 전폭, 데스크톱 = 표 행 아래 전폭(표 안 셀 한 칸을 가로로 합침). 이 줄이 있는 동안 저장 비활성. 하늘색 없음
- text-input: 사용량 입력(오류 칸 = 2px #141414 링), 메모, 수업명(#f0f0f0 / 카드 안 #ffffff, rounded 16)
- usage-date: "사용일" 값 "2026-10-10". 하늘색: 달력 아이콘 #2b9fe0
- class-select: "수업 (선택)" 1학년 · 2반 · 통합과학(화면 4와 같음). 하늘색: ▾ 아이콘 #2b9fe0
- recent-class-chip: "1학년 2반 · 통합과학" 선택. 하늘색: 선택 칩 #e6f4fc + 1px #2b9fe0 테두리(글자 #141414)
- data-table: 데스크톱 전용. usage-batch-list 표, 오류 행 아래 줄 포함
- button-primary: 저장 바 "사용 기록 저장 · 3개" 비활성(#e0e0e0 채움 + 라벨 #adadad, rounded 9999, 높이 44 이상). 오류를 고치면 활성. 핑크·하늘색 없음
- ex-toast: 서버 거절일 때만 "저장하지 못했어요 — 표시한 시약을 확인해 주세요"(문제 행에 같은 usage-over-stock 줄, 전부 취소). 이 프레임(입력 중 오류)에는 그리지 않는다. 핑크 없음, 아이콘 #141414
- tab-bar: 모바일 전용 하단 탭바 1개(공통 규격). 데스크톱에는 두지 않는다. 하늘색: 활성 tab-item 아이콘 #2b9fe0만
- tab-item: 4개 "홈" · "시약" · "QR 스캔" · "기록". 활성 = "기록"
### 반영한 레퍼런스
- https://uibowl.io/name/%EB%9D%BC%EC%9A%B4%EC%A6%88?patterns=%EC%9E%A5%EB%B0%94%EA%B5%AC%EB%8B%88&imgId=cmunlyn8s0005l804bcsbpzcr
- https://uibowl.io/name/%EA%B3%A8%ED%94%84%EC%A1%B4?patterns=%EC%9E%A5%EB%B0%94%EA%B5%AC%EB%8B%88&imgId=cmunkg4m30025l904yg6x2ysv

## 상태 화면 4-past-date
사용일을 지난 날로 고른 상태(프레임 4-past-date-mobile · 4-past-date-desktop). 모든 역할 같다. 핑크 없음 — 확인 안내다.
예시 상태: 화면 4와 같은 3개·같은 수업, 사용일 "2026-10-07"(날짜 시트·팝오버는 닫힘). 저장 바 바로 위 안내 한 줄. 저장 활성.
데스크톱 배치: app-sidebar("기록" 현재) | 본문 페이지 640 열 — 화면 4와 같은 순서, 사용일 행 값 "2026-10-07", 본문 하단 고정 바 바로 위(바 안 왼쪽 요약 대신) past-date-note.
### 구성 요소
- app-sidebar: 데스크톱 전용. 공통 규격, 학교명 "샘플고등학교" + 역할별 메뉴 + nav-account-menu
- sidebar-item: 데스크톱 전용. 학생 5개 / 교사 8개 / admin 10개. 현재 = "기록"
- nav-pill: 모바일 전용. 화면 4 nav-pill 그대로 — 뒤로가기 + "사용 기록" + 현재 학교명 "샘플고등학교" + nav-account-menu ▾
- nav-account-menu: 닫힌 ▾
- reagent-add: 모바일 머리 줄 "+ 시약 추가", 데스크톱 검색 칸. 하늘색: + 아이콘 #2b9fe0
- usage-batch-list: "담은 시약 3개" + 행 3개(화면 4와 같음, 오류 없음)
- usage-item-row: 에탄올 50 mL · 페놀프탈레인 용액 10 mL · 수산화나트륨 5 g(화면 4와 같은 모양)
- usage-date: "사용일"(필수) 값 "2026-10-07"(#f0f0f0, rounded 16, 오른쪽 달력 아이콘). 다시 누르면 10월 7일이 선택된 채 열린다(오늘 이후 흐림). 하늘색: 달력 아이콘 #2b9fe0
- past-date-note: 저장 바 바로 위(간격 8) 무채색 한 줄 — 왼쪽 작은 달력 아이콘 #707070 + body-sm #707070 "10월 7일 사용으로 기록해요". 채움·테두리 없음. 사용일을 오늘로 되돌리면 사라진다. 핑크·하늘색 없음
- class-select: "수업 (선택)" 1학년 · 2반 · 통합과학. 하늘색: ▾ 아이콘 #2b9fe0
- recent-class-chip: "1학년 2반 · 통합과학" 선택. 하늘색: 선택 칩 #e6f4fc + 1px #2b9fe0 테두리(글자 #141414)
- text-input: 사용량 입력, 메모, 수업명(#f0f0f0 / 카드 안 #ffffff, rounded 16)
- data-table: 데스크톱 전용. usage-batch-list 표
- button-primary: 저장 바 "사용 기록 저장 · 3개"(#141414 채움, #ffffff 글자, rounded 9999, 높이 44 이상). 지난 날이어도 바로 저장(추가 확인 없음), 뒤 ex-toast "3개 시약 사용을 기록했어요". 하늘색 없음
- tab-bar: 모바일 전용 하단 탭바 1개(공통 규격). 데스크톱에는 두지 않는다. 하늘색: 활성 tab-item 아이콘 #2b9fe0만
- tab-item: 4개 "홈" · "시약" · "QR 스캔" · "기록". 활성 = "기록"
### 반영한 레퍼런스
- https://uibowl.io/name/%EA%B3%A8%ED%94%84%EC%A1%B4?patterns=%EC%9E%A5%EB%B0%94%EA%B5%AC%EB%8B%88&imgId=cmunkg4m30025l904yg6x2ysv
- https://uibowl.io/name/%EC%B9%B4%EC%B9%B4%EC%98%A4%EA%B3%A8%ED%94%84%EC%98%88%EC%95%BD?patterns=%EA%B2%80%EC%83%89&imgId=cmtwluex6011ijl043f9n1umq

## 화면 10
사용 기록 내역. 학생·교사·admin 모두. 샘플고등학교 기록만. 승인본(runs/20261008-0936 화면 10) 구성 그대로 + 요청 6: 기록마다 수업 표시(class-label), 목록 위 반 필터(class-filter), 삭제된 시약 기록 표시(deleted-reagent-tag). 사용일로 묶고 사용일 최신순(같은 날 안에서는 기록 시각 최신순). 기록한 날이 사용일과 다를 때만 회색 캡션 "{M}월 {D}일에 기록". 여러 시약 한 번 저장은 시약마다 한 행(같은 시각·같은 수업).
예시 상태: "전체", 기간 "최근 1개월", 반 "전체". 6건 —
① "10월 10일 · 오늘": 에탄올 · 교사 김OO · 14:05 · 50 mL · 1학년 2반 · 통합과학 / 페놀프탈레인 용액 · 교사 김OO · 14:05 · 10 mL · 1학년 2반 · 통합과학 / 수산화나트륨 · 교사 김OO · 14:05 · 5 g · 1학년 2반 · 통합과학
② "10월 8일": 염산 · 학생 이OO · 10:20 · 20 mL · 2학년 1반 / 과망가니즈산 칼륨(삭제된 시약) · 교사 박OO · 09:40 · 5 g · 수업 없음
③ "10월 7일": 질산은 · 교사 김OO · 2 g · 통합과학 + "10월 8일에 기록"
데스크톱 프레임은 첫 행(에탄올)을 눌러 detail-drawer가 열린 상태.
모바일 활성 탭: "기록". 위→아래: nav-pill → segmented-control + 기간 선택 → 검색 → class-filter 줄 → 사용일 그룹 목록 → tab-bar.
데스크톱 배치: app-sidebar("기록" 현재) | 본문 = 페이지 머리(왼쪽 "기록" + "6건" / 오른쪽 검색) → 툴바(segmented-control "전체 / 내 기록" + 기간 드롭다운 + class-filter "반: 전체 ▾") → data-table(사용일 묶음 머리 행 + 기록 행, 열에 "수업") → 페이지 번호 + 오른쪽 detail-drawer(기록 상세, "수업 | 값" 행).
### 구성 요소
- app-sidebar: 데스크톱 전용. 공통 규격, 학교명 "샘플고등학교" + 역할별 메뉴 + nav-account-menu
- sidebar-item: 데스크톱 전용. 학생 5개 / 교사 8개 / admin 10개. 현재 = "기록"
- nav-pill: 모바일 전용. "Lab_Stock" 워드마크 + 제목 "사용 기록 내역" + 현재 학교명 "샘플고등학교" + nav-account-menu ▾
- nav-account-menu: 모바일 = 학교명 옆 ▾, 데스크톱 = app-sidebar 맨 아래. "로그아웃" 1개. 하늘색 없음
- segmented-control: "전체 / 내 기록", 한 번에 하나. 데스크톱 = 툴바 왼쪽
- segmented-control-active: 선택 "전체" 흰 pill. 하늘색: 1px #2b9fe0 테두리(글자 #141414)
- text-input: 기간 선택 상자("최근 1개월" ▾, 사용일 기준)와 "시약명 검색"(#f0f0f0, rounded 16, 포커스 링 2px #141414). 하늘색: 검색·▾ 아이콘 #2b9fe0
- class-filter: 반 필터 button-pill-soft "반: 전체 ▾"(#f3f3f3, 라벨 #141414, rounded 9999, 높이 44 이상). 모바일 = 검색 아래 한 줄 왼쪽, 데스크톱 = 툴바 기간 드롭다운 오른쪽. 누르면 모바일 바텀시트 / 데스크톱 버튼 아래 드롭다운: 학년(전체 · 1학년 · 2학년 · 3학년) → 반(학년 전체 · 1반 … 20반), 하단 button-primary "적용". 적용 중이면 라벨이 "반: 1학년 2반 ▾"로 바뀌고 #e6f4fc 채움 + 1px #2b9fe0 테두리(글자 #141414). 이 프레임은 "전체"·닫힘. 하늘색: ▾ 아이콘 #2b9fe0
- class-label: 기록 행의 수업 표기 "{학년}학년 {반}반 · {수업명}", 있는 것만("2학년 1반", "통합과학"). 모바일 = 행 보조줄 아래 caption #707070 한 줄(없으면 줄 없음). 데스크톱 = data-table 열 "수업"(body-sm #141414, 없으면 "—" #adadad) + 드로어 "수업 | 1학년 2반 · 통합과학" 행. 핑크·하늘색 없음
- deleted-reagent-tag: 삭제된 시약 기록(과망가니즈산 칼륨) 시약명 바로 오른쪽 pill "삭제된 시약"(#f3f3f3 채움, label #141414, rounded 9999). 그 행의 시약명은 #707070. 기록 행·상세는 그대로 열리지만 시약 상세(화면 3)로 가는 링크·› 없음. 모든 역할. 핑크·하늘색 없음
- data-table: 데스크톱 전용. 열 = 사용일(정렬, 활성 ↓ #2b9fe0) · 시약명 · 수업 · 사용자 · 사용량 · 기록 시각. 사용일 묶음 머리 행(caption #707070 "10월 10일 · 오늘" / "10월 8일" / "10월 7일", 왼쪽 #2b9fe0 짧은 인디케이터). 기록한 날이 다르면 시약명 아래 caption "10월 8일에 기록". 삭제된 시약 행 = 시약명 #707070 + deleted-reagent-tag. 선택 행(에탄올) #e6f4fc. 0건이면 표 머리를 남기고 표 안 ex-empty-state-card
- ex-data-table-cell: 모바일 기록 목록 — 사용일 그룹 헤더(caption #707070, 그룹 사이 24) 아래 행 = 시약명(title) + 보조줄 body-sm #707070 "교사 김OO · 14:05" + 그 아래 class-label caption + 오른쪽 사용량(body). 기록한 날이 다르면 caption "10월 8일에 기록" 한 줄 더. 행 사이 12. 데스크톱 data-table 머리행·셀 chrome. 하늘색: 누른 행 #e6f4fc, 그룹 헤더 왼쪽 #2b9fe0 인디케이터
- detail-drawer: 데스크톱 전용 기록 상세. 폭 480, #ffffff, 왼쪽 1px #f0f0f0 선, 여백 24, × 닫기. heading-3 "에탄올" + display "50 mL" → "항목 | 값" 행 사용자 "교사 김OO" · 사용일 "2026-10-10" · 수업 "1학년 2반 · 통합과학"(없으면 "—" #adadad) · 기록한 날(다를 때만) · 메모 → msds-entry → 아래 고정 button-outline "닫기". 삭제된 시약 기록이면 제목 옆 deleted-reagent-tag, msds-entry 대신 caption #707070 "삭제된 시약이에요"
- ex-modal-card: 모바일 전용 기록 상세 시트(tab-bar 위, × 닫기). 드로어와 같은 내용(수업 행 포함). 하늘색 없음
- msds-entry: 상세 안 button-pill-soft "MSDS 보기 ›"(#f3f3f3, 라벨 #141414, rounded 9999, 높이 44 이상) → 화면 16. 학생·교사·admin 모두. 하늘색: › 아이콘 #2b9fe0
- button-pill-soft: class-filter 버튼, msds-entry 버튼(위 정의)
- button-outline: 상세 "닫기"(#ffffff, 1px #e0e0e0, 라벨 #141414, rounded 9999, 높이 44 이상)
- ex-empty-state-card: 결과 0건 "아직 사용 기록이 없어요" + 한 줄 "기간이나 반을 바꿔 보세요". 핑크 없음. 하늘색: 안내 아이콘 #2b9fe0
- tab-bar: 모바일 전용 하단 탭바 1개(공통 규격). 데스크톱에는 두지 않는다. 하늘색: 활성 tab-item 아이콘 #2b9fe0만
- tab-item: "홈" · "시약" · "QR 스캔" · "기록" 4개. 활성 = "기록", 비활성 3개 #707070
### 반영한 레퍼런스
- https://uibowl.io/name/%EB%AF%B8%EB%8B%88%EC%8A%A4%ED%83%81?patterns=%EB%82%B4%EC%97%AD&patternName=%EC%A3%BC%EB%AC%B8%EB%82%B4%EC%97%AD
- https://uibowl.io/name/%EC%B9%B4%EC%B9%B4%EC%98%A4%EA%B3%A8%ED%94%84%EC%98%88%EC%95%BD?patterns=%EB%82%B4%EC%97%AD&patternName=%EB%82%98%EC%9D%98%EC%98%88%EC%95%BD%20-%20%EC%98%88%EC%95%BD%EB%82%B4%EC%97%AD%ED%83%AD
- https://uibowl.io/name/%ED%8F%B4%EC%84%BC%ED%8A%B8?patterns=%EC%95%8C%EB%A6%BC&patternName=%EC%95%8C%EB%A6%BC%20%EB%82%B4%EC%97%AD

## 역할별 노출
앱 전체(로그인 후 화면) 기준 개수. runs/20261008-0936 표를 기준으로 이번 변경을 반영했다. 같은 화면의 상태 화면·모바일·데스크톱에 다시 나오는 같은 컴포넌트는 그 화면 1개로 센다.
이번 변경: 화면 3에 reagent-more-menu 1 · reagent-delete 1(교사·admin만, 학생 0 — R5). 상태 화면 3-delete는 같은 화면이라 더하지 않는다. 화면 4(여러 시약 사용 기록)·화면 10(수업·반 필터·삭제된 시약)은 모든 역할 같고 표의 컴포넌트를 더하거나 빼지 않는다.
msds-entry = 화면 3 1 + 화면 10 상세 1(학생·교사·admin 모두 2, R4). 나머지 행은 runs/20261008-0936 값 그대로.
reagent-add·reagent-picker·usage-batch-list·usage-item-row·usage-over-stock·class-select·recent-class-chip·class-label·class-filter·deleted-reagent-tag·usage-date·past-date-note는 모든 역할에 같고 rules.json roles 대상이 아니라 표에 넣지 않는다.

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
