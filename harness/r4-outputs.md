# 산출물 (R4)

> 파이프라인: harness/r3-pipeline.md

## 1. 실행 폴더 (실행 1회 = 폴더 1개)

`runs/{YYYYMMDD-HHMM}/` — 하위 폴더 research/ spec/ design/ judge/ 는 에이전트별 편집 폴더 (harness/r6-roles.md)

| 파일 | 만드는 단계 | 내용 | 셀 수 있는 조건 |
|---|---|---|---|
| input.json | 실행 시작 | 대상 화면 ID 목록, school_name (기본 "샘플고등학교", R5 추가), school_sido·school_region (선택, 기본 = rules.json neis) | ID ⊂ {1..14}, 개수 1~14, school_name 1개 |
| neis.json | 실행 시작 (화면 14 회원가입이 대상일 때) | `harness/scripts/neis.py`가 NEIS에서 받은 시/도 목록·지역 목록·학교 목록 (키 없음) | sido_list ≥ 1, region_list ≥ 1, school_list ≥ 1 |
| research/s1-references.md | S1 | 레퍼런스 모음 | 화면당 ui_url 3~5개 |
| research/s1-adopt.md | S1 | 반영 항목 표 | 레퍼런스마다 "가져올 것" 1줄 |
| spec/s2-spec.md | S2 | 화면 설계서 | 대상 화면마다 구성 요소 ≥ 1, 역할별 노출 표 1개 |
| design/s3-keyscreens.json 또는 design/s3-keyscreens/{프레임}.json | S3 | 키스크린 노드 JSON (둘 중 하나만) | 프레임 2~3개, 390×844 |
| approval.md | G-승인 | 승인/거절, 사유, 날짜, 승인자 | 파일 1개, 결과 ∈ {approved, rejected} |
| design/s4-frames.json 또는 design/s4-frames/{프레임}.json | S4 | 전체 프레임 노드 JSON (둘 중 하나만. 크면 프레임별 파일, 2026-10-02) | 프레임 수 = 화면 수 × 2 |
| judge/gate-{S1,S2,S3,S5}.json | 각 게이트 | 판정 결과 (S5 위반 목록 포함, R6 변경) | violations 배열, 완료 시 gate-S5 길이 0 |
| state.json | 모든 단계 | 진행 상태 | §4 형식 |

## 2. Figma 명명 규칙

- Figma 파일 1개, 페이지 2개: `S3-keyscreens`, `S4-screens`
- 프레임 이름 = `{화면ID}-{mobile|desktop}` (예: `2-mobile`, `6-desktop`)
- 프레임 크기: mobile 390×844, desktop 1440×900
- 스크립트는 정규식 `^([1-9]|1[0-4])-(mobile|desktop)$` 로 프레임 수를 센다 (rules.json frames.name_pattern)

## 3. 규칙 SSOT

- SSOT = `harness/rules.json` (판정 스크립트는 이 파일만 읽는다)
- 원본 = docs/design.md, docs/story-service.md → 바뀌면 rules.json을 다시 만든다
- 담는 것: 허용 색, 허용 radius, 폰트·weight·letterSpacing, 그림자, N1·N2, 역할별 노출 결정
- 생성 시점: R5 게이트 확정 후

### R4 결정 (rules.json에 `"source": "R4 결정"`으로 표시)

| 항목 | 결정 |
|---|---|
| ex-modal-card·ex-toast 그림자 vs Don't "그림자 금지" | Don't 우선. 그림자 효과 = 0, 예외는 segmented-control-active 1개 |
| ex-data-table-cell "mono-caps" vs Don't "all-caps 금지" | Don't 우선. textCase = ORIGINAL만 허용 |
| `{colors.on-primary}` hex 미기재 | #ffffff |

허용 색 (design.md 기준, 중복 제거): #141414, #262626, #707070, #adadad, #e0e0e0, #f0f0f0, #f3f3f3, #ffffff, #d6246a
+ badge-overlay 전용 rgba(115, 115, 115, 0.56)

## 4. 재개

state.json 형식:

```json
{ "stage": "S1|S2|S3|G|S4|S5|done",
  "retries": { "S1": 0, "S5": 0 },
  "approval": "none|approved|rejected" }
```

- 재실행 시: 출력 파일이 있고 통과 조건을 만족하는 단계는 건너뛴다
- G-승인: approval.md의 결과 = approved 일 때만 통과. 재개 시 다시 묻지 않는다
- retries가 한도(S1 2회, S5 3회)에 닿으면 stage를 바꾸지 않고 멈춘다
