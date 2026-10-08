# 게이트 (R5)

> 규칙 값의 SSOT: harness/rules.json (이 문서는 "언제·어디서·무엇을 세는지"만 정한다)
> 복귀 경로: harness/r3-pipeline.md §4

## 0. 전제: 노드 이름 규칙

- 컴포넌트 노드 이름 = design.md 컴포넌트명 (button-primary, badge-low-stock, reorder-alert-card, school-select …)
- 2026-10-02 추가 이름: `stock-intake`, `reagent-register`, `user-manage`, `cabinet-edit`, `cabinet-door-select`, `cabinet-shelf-select`, `cabinet-slot`, `storage-class-chip`, `mix-warning`, `qr-scan`, `qr-manual-entry`, `home-summary`, `quick-action`, `tab-bar`, `tab-item`, `landing-hero`, `feature-card`, `landing-cta`, `guest-entry`, `guest-banner`, `guest-lock`(2026-10-03), `cabinet-switcher`, `cabinet-add`(2026-10-04), `cabinet-number`, `qr-print`, `qr-print-sheet`, `qr-label`, `qr-result-sheet`, `slot-count`, `slot-sheet`, `slot-assign`, `reagent-location`, `location-edit`, `location-picker`, `reorder-threshold`, `threshold-edit`, `nav-account-menu`(2026-10-06), `intake-mode`, `doc-upload`, `doc-intake-table`, `doc-item-row`, `reagent-link`, `new-reagent-fields`, `msds-search`, `msds-candidates`, `msds-bulk-banner`, `suggest-badge`, `location-suggest`, `auto-threshold-badge`(2026-10-07), `list-filter-button`, `list-filter-sheet`, `filter-chip-row`, `usage-date`, `past-date-note`(2026-10-07 요청 3), `school-select-kind`(2026-10-07 요청 4), `app-sidebar`, `sidebar-item`, `data-table`, `detail-drawer`(2026-10-08 데스크톱), `msds-summary`, `ghs-pictogram`, `msds-original-link`, `msds-skeleton`(2026-10-08 화면 16), `product-shot`, `landing-tabs`, `landing-section`, `step-flow`, `cta-band`, `web-footer`(2026-10-08 랜딩)
- R5에서 추가한 이름: `manual-upload`, `vendor-link`, `vendor-register`, `msds-entry` (S2 설계서와 Figma 노드에 동일하게 사용)
- NEIS 학교 선택(2026-10-01)으로 추가한 이름: `school-select-sido`, `school-select-region`, `school-select-school` (school-select 대신 사용)
- 스크립트는 이름으로 노드를 찾는다 → 이름이 없거나 다르면 해당 규칙 "판정 불가" = 실패로 센다

## 1. 게이트 목록

| 게이트 | 위치 | 대상 파일 | 적용 규칙 | 통과 |
|---|---|---|---|---|
| G-S1 | S1 끝 | research/s1-references.md, research/s1-adopt.md | S1-a, S1-b | 위반 0 |
| G-S2 | S2 끝 | spec/s2-spec.md | R1~R7, C1, N1-d, N2-a, N2-c | 위반 0 |
| G-S3 | S3 끝, 승인 요청 전 | design/s3-keyscreens.json | D1~D8, D10, C1, C2, C3, N1-a~d, N2-a~c, GM1~5 | 위반 0일 때만 승인 요청 생성 |
| G-승인 ★사람 | S3→S4 | approval.md | result 줄 | result = approved |
| G-S5 | S5 | design/s4-frames.json | D1~D10, C1, C2, C3, N1-a~d, N2-a~c, GM1~5 | 위반 0 = 완료 |

## 2. 규칙

### S1 — 레퍼런스 (story-work 멈칫 2)

| ID | 조건 |
|---|---|
| S1-a | 대상 화면마다 uibowl ui_url 개수 3~5 |
| S1-b | 레퍼런스마다 "가져올 것" 1줄 이상, 빈 칸 0 |

### R — 역할별 노출 (story-service 결정 사항, s2-spec.md 역할 표에서 셈)

| ID | 조건 |
|---|---|
| R1 | 학생 행: 매뉴얼 업로드 버튼(manual-upload) = 0 |
| R2 | 학생 행: 재주문 알림(reorder-alert-card) = 0, 판매처 버튼(vendor-link) = 0 |
| R3 | 판매처 등록 버튼(vendor-register): admin 행에만 존재 (교사·학생 = 0) |
| R4 | MSDS 진입점(msds-entry): 학생·교사·admin 행 각각 ≥ 1 |
| R5 | 학생 행: 입고(stock-intake) = 0, 시약 등록(reagent-register) = 0, 재주문 기준 고치기(threshold-edit) = 0, 서류 입고(doc-upload)·MSDS 찾기(msds-search·msds-bulk-banner) = 0 (화면 7, 2026-10-02 · 화면 3, 2026-10-06 · 화면 7·3·2, 2026-10-07) |
| R6 | 사용자 관리(user-manage): admin 행에만 존재 (화면 8, 2026-10-02) |
| R7 | 학생 행: 시약장 편집(cabinet-edit)·시약장 추가(cabinet-add)·시약 넣기(slot-assign)·위치 바꾸기(location-edit)·QR 인쇄(qr-print) = 0 (화면 11·3, 2026-10-02·10-04·10-06) |

### C — 화면별 필수 컴포넌트 (2026-10-02)

| ID | 조건 |
|---|---|
| C1 | rules.json `screens_required`의 화면(2 시약 목록, 3 시약 상세, 4 사용 기록, 7 입고·등록, 11 시약장 설정, 12 QR 스캔, 13 홈, 15 랜딩): S2는 설계서 해당 화면 구성 요소에, S3·S5는 해당 화면 프레임 노드 이름에 필수 컴포넌트가 모두 있음. 상태 프레임({ID}-{state}-*, state = rules.json frames.variant_name_pattern)은 rules.json `variants`의 목록으로 검사 (2026-10-04 · 10-06) |
| C2 | 하단 탭바: 화면 2~13 mobile 프레임마다 tab-bar 1개(radius 0 사각형) + 그 안 tab-item 4개, 화면 1·14·15·desktop 프레임에는 tab-bar 0 (2026-10-02) |
| C3 | 데스크톱 틀: 화면 2~13 desktop 프레임마다 app-sidebar 1개(radius 0, 폭 240) + 그 안 sidebar-item ≥ 3, nav-pill 0, 화면별 desktop 필수(2·8·9·10 data-table, 3 detail-drawer — 상태 프레임 제외). mobile 프레임은 app-sidebar 0 (2026-10-08, 값 = rules.json desktop_shell) · 로그인 전 1·14·15 desktop = web-header 1, nav-pill·app-sidebar 0 (desktop_shell.pre_login) · 15-desktop 필수 product-shot·landing-tabs·landing-section·step-flow·cta-band·web-footer(2026-10-08) |

### D — 디자인 가이드 (story-work 멈칫 7)

| ID | 조건 |
|---|---|
| D1 | 모든 fill·stroke·text 색 ∈ colors.allowed · #ff0000은 ghs-pictogram 안에서만(2026-10-08, rules.json colors.allowed_rgba) |
| D2 | #d6246a·#fbe9f0(연핑크) 노드는 badge-low-stock·reorder-alert-card·mix-warning(2026-10-02 추가)의 자손일 때만 허용 |
| D3 | cornerRadius ∈ radius.allowed |
| D4 | fontFamily ∈ {Pretendard, IBM Plex Sans KR(Figma 시안 대체)}, weight·fontSize ∈ 허용 집합 · 랜딩 큰 글자 40·48은 landing-hero·landing-section·cta-band 안에서만(2026-10-08, typography.display_sizes) |
| D5 | letterSpacing = 0, textCase = ORIGINAL |
| D6 | DROP_SHADOW 개수 = 0 (segmented-control-active 예외) |
| D7 | auto-layout padding·gap ∈ spacing.allowed |
| D8 | button-* 노드: cornerRadius = 9999, height ≥ 44 |
| D9 | 프레임 수 = 화면 수 × 2 (+ 둘러보기 guest_screens × 2 + 상태 variants × 2), 크기 ∈ {390×844, 1440×900} (S5만) · 15-desktop만 1440×900~6000 세로 프레임(2026-10-08, frames.tall) |
| D10 | 하늘색(#2b9fe0·#e6f4fc): badge-low-stock·reorder-alert-card·mix-warning·button-primary 안에서 0, 텍스트 노드 글자색으로 0 (2026-10-02) |

### N — 어기면 안 되는 것 ★ (story-service N1·N2)

| ID | 근거 | 조건 |
|---|---|---|
| N1-a | 학교별 분리 | 화면 2~13 프레임마다 input.json의 school_name 텍스트 노드 ≥ 1 |
| N1-b | 학교별 분리 | 화면 2~13 텍스트에서 학교명 패턴 매칭 종류 = 1 (화면 1·14 제외 — 14 회원가입 학교 목록은 여러 학교명이 정상) |
| N1-c | 학교별 분리 | school-select* 노드는 화면 14(회원가입)에만 → 다른 화면(로그인 1 포함)에서 0 |
| N1-d | 학교 선택 (NEIS) | 화면 14(rules.json never.N1.school_select_screen): school-select-sido → school-select-region → school-select-school 각 1개, 이 순서 (S2는 설계서 화면 14 구성 요소, S3·S5는 화면 14 프레임 노드 순서) |
| N2-a | 키 서버 전용 | 금지어 포함 텍스트 = 0 (프레임 + s2-spec.md) |
| N2-b | 키 서버 전용 | 화면 5의 text-input 중 라벨에 키·모델·model 포함 = 0 |
| N2-c | 키 서버 전용 | 키 형식 문자열(32자리 16진수) = 0 (프레임 + s2-spec.md). 실제 키 값은 .env에만 |

### GM — 둘러보기(비회원) 모드 (2026-10-03)

둘러보기 프레임 = 이름 `{화면}-guest-{mobile|desktop}` (rules.json frames.guest_name_pattern). input.json `guest_screens`에 있는 화면만 만든다(D9이 셈). 일반 프레임 규칙(N1-a·b, C1, C2)은 둘러보기 프레임에 적용하지 않고 아래 GM 규칙을 쓴다. D 규칙은 모든 프레임에 적용.

| ID | 조건 |
|---|---|
| GM1 | guest-banner 1개 + 그 안 button-primary(가입) |
| GM2 | rules.json guest.hidden_components (입고·등록·매뉴얼·사용자 관리·시약장 편집·판매처·재주문·학교 선택) = 0 |
| GM3 | 학교명 = "데모 학교" ≥ 1, 실제 학교명 패턴(…고등학교)·input school_name = 0 |
| GM4 | mobile: tab-bar 1·tab-item 4·탭바 안 guest-lock 2(QR 스캔·기록), desktop: tab-bar 0 · desktop = app-sidebar 1·그 안 guest-lock 2(기록·QR 찾기)·nav-pill 0 (2026-10-08) |
| GM5 | 화면 13·3 둘러보기: 탭바 밖 guest-lock ≥ 1 (쓰기 동작 잠금) |

## 3. 사람 승인 (1곳)

S3 끝에 G-S3가 통과하면 하네스가 멈추고 approval.md 템플릿을 생성한다.

```
keyscreens: {Figma 링크}
precheck: G-S3 위반 0
result:           ← approved | rejected
reason:           ← 1줄
approver:
date:
```

- result가 비어 있으면 state.stage = G 에서 대기
- rejected → reason에 "설계" 포함 시 S2, 아니면 S3 (횟수 제한 없음)

## 4. 실패 시 복귀

| 게이트 | 실패 | 복귀 | 한도 |
|---|---|---|---|
| G-S1 | S1-a 미달 | S1 (검색어 변경) | 2회 → 사람 |
| G-S1 | S1-b 빈 칸 | S1 (해당 레퍼런스만) | 2회 → 사람 |
| G-S2 | R1~R7·C1·N1-d·N2-a·N2-c 위반 | S2 | 2회 → 사람 |
| G-S3 | 위반 ≥ 1 | S3 (위반 노드만) | 3회 → 사람 |
| G-S5 | 위반 ≥ 1 | S4 (위반 노드만) | 3회 → 사람 |
