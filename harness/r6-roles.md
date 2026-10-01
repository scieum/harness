# 역할 (R6)

> 게이트: harness/r5-gates.md · 규칙: harness/rules.json

## 1. 에이전트

| 에이전트 | 단계 | 편집 폴더 (1개) | 도구 |
|---|---|---|---|
| researcher | S1 | runs/{id}/research/ | Read, Write, uibowl MCP |
| planner | S2 | runs/{id}/spec/ | Read, Write |
| designer | S3, S4 | runs/{id}/design/ | Read, Write, Figma MCP (유일한 Figma 쓰기 권한) |
| judge ★읽기전용 | G-S1·S2·S3·S5 | runs/{id}/judge/ (스크립트만 씀) | Read, Bash(judge.py만) |
| 오케스트레이터 (메인 세션) | 순서·재시도·승인 | runs/{id}/ 루트 파일 3개 | 전체, 단 단계 산출물은 직접 쓰지 않음 |

- 모든 에이전트: docs/, harness/ 는 읽기 전용
- 다른 에이전트 폴더 쓰기 = 0
- 정의 파일: .claude/agents/{researcher,planner,designer,judge}.md

## 2. 판정자

- 판정 = harness/scripts/judge.py (Python 3.12)
- 호출: `python harness/scripts/judge.py --gate {S1|S2|S3|S5} --run runs/{id}`
- 출력: judge/gate-{X}.json = `{gate, pass, violations:[{rule, node, actual, allowed}]}`
- 종료 코드: 0 통과 / 1 실패 / 2 판정 불가(파일 없음·이름 규칙 위반)
- judge 에이전트는 수정하지 않는다. 결과 파일만 오케스트레이터에게 보고

## 3. 자연어 트리거

| 말 | 동작 |
|---|---|
| "시안 돌려줘 [번호]" | 새 runs/{id}, S1부터. 번호 생략 = 1~6 |
| "이어서 해줘" | 최근 runs/ 의 state.json에서 재개 |
| "승인했어" / "반려했어 [사유]" | approval.md 기록 → G-승인 |
| "검수만 해줘" | 최근 run에 G-S5만 |
| "규칙 다시 뽑아줘" | design.md → rules.json 재생성안 제시, 사용자 승인 후 저장 (실행 중 금지) |

## 4. 알려진 한계 (R8에서 처리)

- agents의 tools 필드는 도구 종류만 제한한다. 폴더 쓰기 범위와 "Bash는 judge.py만"은 지시문 + settings.json 허용 목록으로만 막혀 있다.
- 기계적 강제(PreToolUse 훅 또는 judge.py의 폴더 밖 파일 검사)는 R8에서 결정한다.
