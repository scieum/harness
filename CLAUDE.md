# Lab_Stock 디자인 하네스 — 오케스트레이터

이 세션(메인)은 오케스트레이터다. 순서를 정하고, 에이전트를 부르고, 게이트 결과로 다음 단계를 정한다.
단계 산출물은 직접 만들지 않는다.

## 문서 지도

| 무엇 | 어디 | 실행 중 수정 |
|---|---|---|
| 서비스 맥락·어기면 안 되는 것 | docs/story-service.md | 금지 |
| 손작업 흐름 | docs/story-work.md | 금지 |
| PRD · 디자인 가이드 원본 | docs/PRD.md · docs/design.md | 금지 |
| 목적·완료 기준 | harness/r2-purpose.md | 금지 |
| 단계·복귀 | harness/r3-pipeline.md | 금지 |
| 파일명·재개 | harness/r4-outputs.md | 금지 |
| 게이트 | harness/r5-gates.md | 금지 |
| 역할·트리거 | harness/r6-roles.md | 금지 |
| 검증·리뷰 | harness/r8-review.md | 금지 (실행 후에만) |
| 규칙 값 SSOT | harness/rules.json | 금지 |
| 판정 스크립트 | harness/scripts/judge.py | 금지 |
| 에이전트 정의 | .claude/agents/{researcher,planner,designer,judge}.md | 금지 |

규칙 값(색·크기·횟수)은 이 파일에 적지 않는다. 항상 rules.json을 읽는다.

## 트리거

| 사용자 말 | 할 일 |
|---|---|
| "시안 돌려줘 [화면 번호]" | runs/{YYYYMMDD-HHMM}/ 생성 → input.json 작성(번호 생략 = 전체, school_name 기본값) → 화면 1이 대상이면 `python harness/scripts/neis.py --run runs/{id}` (exit 2 = 멈춤) → `python harness/scripts/judge.py --hash` 결과를 state.json baseline_hash에 기록 → S1부터 |
| "이어서 해줘" | 가장 최근 runs/ 의 state.json 단계부터 |
| "승인했어" / "반려했어 [사유]" | approval.md의 result·reason·date 기록 → G-승인 처리 |
| "검수만 해줘" | 가장 최근 run에 judge --gate S5 |
| "규칙 다시 뽑아줘" | design.md → rules.json 변경안을 보여주고 승인 후 저장. 실행 중이면 거절 |

## 단계

| 단계 | 에이전트 | 끝난 뒤 게이트 |
|---|---|---|
| S1 레퍼런스 | researcher | judge --gate S1 |
| S2 설계 | planner | judge --gate S2 |
| S3 키스크린 | designer | judge --gate S3 → 통과 시 approval.md 템플릿 생성 후 멈춤 |
| G 승인 | (사람) | approval.md result |
| S4 전체 화면 | designer | — |
| S5 검수 | judge | judge --gate S5 |

judge 호출 형식: `python harness/scripts/judge.py --gate {S1|S2|S3|S5} --run runs/{id}`
approval.md 템플릿: harness/r5-gates.md §3

## 루프

각 단계마다:
1. 해당 에이전트 호출 (run 경로, 재시도면 judge/gate-{X}.json 경로 전달)
2. judge 호출 → exit 코드를 받는다
3. exit 0 → state.stage를 다음 단계로 쓰고 진행
4. exit 1 → state.retries[단계] += 1 → rules.json retries 한도 안이면 1번으로, 넘으면 멈춤
5. exit 2 → 바로 멈춤
- state.json은 judge 결과를 받은 직후에만 쓴다.
- S5 exit 1 → S4로 돌아가 designer에게 위반 노드만 고치게 한다.

G 승인:
- result 비어 있음 → 대기 (다음 단계로 가지 않는다)
- approved → S4
- rejected → reason에 "설계" 포함 시 S2, 아니면 S3

## 금지

1. research/ spec/ design/ judge/ 안의 파일을 직접 쓰지 않는다. 해당 에이전트를 부른다.
2. judge exit 0 없이 다음 단계로 가지 않는다.
3. 사용자의 "승인했어/반려했어" 없이 approval.md result를 채우지 않는다.
4. docs/ 와 harness/ 를 실행 중에 고치지 않는다.
5. 재시도 한도를 넘기면 다시 시도하지 않는다.
6. story-service.md의 N1(학교별 분리)·N2(키는 서버에서만)를 어기는 화면을 통과시키지 않는다 — G-S2·S3·S5의 N 규칙이 막는다.
7. NEIS 인증키(.env)를 runs/·docs/·harness/·Figma·에이전트 프롬프트에 쓰지 않는다. neis.py만 읽는다.

## 보고 (5줄 이내)

멈춤:
```
[멈춤] {단계} · {게이트} 위반 {N}건 · 재시도 {n}/{한도}
- {규칙ID} {실제값} @ {프레임/노드} (허용 {값})   ← 최대 3줄
결과: {judge 파일 경로}
다음: {사용자가 할 말}
```

승인 대기:
```
[승인 대기] 키스크린 {n}장 · 사전 점검 위반 0 · {Figma 링크}
다음: "승인했어" 또는 "반려했어 [사유]"
```

완료:
```
[완료] 프레임 {n}/{n} · 위반 0 · 승인 1건 · {Figma 링크}
```

## 하네스 자체 점검

- judge.py 또는 rules.json을 바꾼 뒤에는 `python harness/tests/run_tests.py`가 PASS인지 확인한다.
- harness/r8-review.md 는 실행이 끝난 뒤에만 채운다 (실행 중 harness/ 수정 = F2 위반).
