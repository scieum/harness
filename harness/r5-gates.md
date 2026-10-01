# 게이트 (R5)

> 규칙 값의 SSOT: harness/rules.json (이 문서는 "언제·어디서·무엇을 세는지"만 정한다)
> 복귀 경로: harness/r3-pipeline.md §4

## 0. 전제: 노드 이름 규칙

- 컴포넌트 노드 이름 = design.md 컴포넌트명 (button-primary, badge-low-stock, reorder-alert-card, school-select …)
- R5에서 추가한 이름: `manual-upload`, `vendor-link`, `vendor-register`, `msds-entry` (S2 설계서와 Figma 노드에 동일하게 사용)
- 스크립트는 이름으로 노드를 찾는다 → 이름이 없거나 다르면 해당 규칙 "판정 불가" = 실패로 센다

## 1. 게이트 목록

| 게이트 | 위치 | 대상 파일 | 적용 규칙 | 통과 |
|---|---|---|---|---|
| G-S1 | S1 끝 | research/s1-references.md, research/s1-adopt.md | S1-a, S1-b | 위반 0 |
| G-S2 | S2 끝 | spec/s2-spec.md | R1~R4, N2-a | 위반 0 |
| G-S3 | S3 끝, 승인 요청 전 | design/s3-keyscreens.json | D1~D8, N1-a~c, N2-a~b | 위반 0일 때만 승인 요청 생성 |
| G-승인 ★사람 | S3→S4 | approval.md | result 줄 | result = approved |
| G-S5 | S5 | design/s4-frames.json | D1~D9, N1-a~c, N2-a~b | 위반 0 = 완료 |

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

### D — 디자인 가이드 (story-work 멈칫 7)

| ID | 조건 |
|---|---|
| D1 | 모든 fill·stroke·text 색 ∈ colors.allowed |
| D2 | #d6246a 노드는 badge-low-stock 또는 reorder-alert-card의 자손일 때만 허용 |
| D3 | cornerRadius ∈ radius.allowed |
| D4 | fontFamily ∈ {Pretendard, IBM Plex Sans KR(Figma 시안 대체)}, weight·fontSize ∈ 허용 집합 |
| D5 | letterSpacing = 0, textCase = ORIGINAL |
| D6 | DROP_SHADOW 개수 = 0 (segmented-control-active 예외) |
| D7 | auto-layout padding·gap ∈ spacing.allowed |
| D8 | button-* 노드: cornerRadius = 9999, height ≥ 44 |
| D9 | 프레임 수 = 화면 수 × 2, 크기 ∈ {390×844, 1440×900} (S5만) |

### N — 어기면 안 되는 것 ★ (story-service N1·N2)

| ID | 근거 | 조건 |
|---|---|---|
| N1-a | 학교별 분리 | 화면 2~6 프레임마다 input.json의 school_name 텍스트 노드 ≥ 1 |
| N1-b | 학교별 분리 | 전체 텍스트에서 학교명 패턴 매칭 종류 = 1 |
| N1-c | 학교별 분리 | school-select 노드는 화면 1에만 → 화면 2~6에서 0 |
| N2-a | 키 서버 전용 | 금지어 포함 텍스트 = 0 (프레임 + s2-spec.md) |
| N2-b | 키 서버 전용 | 화면 5의 text-input 중 라벨에 키·모델·model 포함 = 0 |

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
| G-S2 | R·N2-a 위반 | S2 | 2회 → 사람 |
| G-S3 | 위반 ≥ 1 | S3 (위반 노드만) | 3회 → 사람 |
| G-S5 | 위반 ≥ 1 | S4 (위반 노드만) | 3회 → 사람 |
