# 검증과 리뷰 (R8)

## 1. 기계 검증

- 명령: `python harness/tests/run_tests.py`
- 샘플: harness/tests/fixtures/pass, fixtures/fail (+ fail-expected.json)
- 통과 조건
  - pass → G-S1·S2·S3·S5 모두 exit 0
  - fail → 게이트별 규칙 ID·건수 = fail-expected.json (규칙 22종: S1 2 · R 4 · D 9 · N 5 · F 2)
  - ★ N1-a·N1-b·N1-c·N2-a·N2-b 5개 모두 검출
  - 빈 실행 폴더 → exit 2
- 한계: 샘플 노드 JSON은 손으로 만든 것. designer가 Figma에서 같은 형식으로 내보내는지는 §3 리허설에서 처음 확인한다.

## 2. R8에서 추가·수정한 규칙

| 항목 | 내용 | 위치 |
|---|---|---|
| F1 | runs/{id} 안 허용 목록 밖 파일 = 위반 | rules.json files.allowed |
| F2 | docs/ + harness/ 해시가 실행 시작 시와 다르면 위반 (harness/tests 제외) | rules.json hash_scope, state.json baseline_hash |
| N1-b 패턴 | `…(고등학교\|고)` → `…고등학교` ("재고" 오탐 수정) | rules.json never.N1 |

## 3. 사람 리뷰 — 첫 실제 실행 리허설

- 대상: "시안 돌려줘 2,3,6" 1회
- 끝난 뒤 아래 표를 채운다. 규칙 후보는 바로 반영하지 않고 "규칙 다시 뽑아줘"로 승인 후 반영한다.

### 기계는 통과, 사람이 보기엔 이상함 (→ 규칙 추가 후보)

| # | 프레임/노드 | 무엇이 이상한가 | 셀 수 있는 규칙 후보 |
|---|---|---|---|

### 기계가 막았는데 사람이 보기엔 괜찮음 (→ 규칙 완화 후보)

| # | 규칙 ID | 위반 내용 | 완화 후보 |
|---|---|---|---|

### 멈춘 지점

| # | 단계 | 게이트 | 이유 | 조치 |
|---|---|---|---|---|
