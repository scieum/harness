# S1 채택 항목 — run 20261002-2019

구조·흐름·배치만 가져온다. 색·폰트·모서리는 docs/design.md를 따른다.
화면 1(로그인)에는 학교 선택을 두지 않는다. 소셜 로그인·자동 로그인·아이디 찾기는 가져오지 않는다.

## 화면 1
| # | ui_url | 가져올 것 |
|---|---|---|
| 1 | https://uibowl.io/name/%EB%A7%88%ED%94%8C?patterns=%EB%A1%9C%EA%B7%B8%EC%9D%B8%C2%B7%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85&patternName=%EC%9D%B4%EB%A9%94%EC%9D%BC%20%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85 | 로고 → 이메일·비밀번호(보기 토글) 필드 2개 → 전폭 로그인 버튼 → 비밀번호 찾기 링크 → "아직 회원이 아니신가요? 회원가입" 한 줄 링크의 세로 순서 |
| 2 | https://uibowl.io/name/%EC%8F%98%EC%B9%B4?patterns=%EB%A1%9C%EA%B7%B8%EC%9D%B8%C2%B7%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85&imgId=cmogjlpe3000ajs04ljmhxqd1 | 필드 2개 + 버튼만 남긴 최소 구성, 두 필드가 다 채워지기 전에는 로그인 버튼 비활성 |
| 3 | https://uibowl.io/name/%ED%95%9C%ED%8C%A8%EC%8A%A4?patterns=%EB%A1%9C%EA%B7%B8%EC%9D%B8%C2%B7%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85&imgId=cmq0n0zuu000hky04aw29j4qo | 상단 안내 제목 2줄 → 입력 → 로그인 버튼 바로 아래 "비밀번호 찾기" 텍스트 링크, 회원가입 진입은 화면 하단에 보조 버튼으로 분리 |
| 4 | https://uibowl.io/name/%EC%BD%94%EC%98%A4%EB%A1%B1%EB%AA%B0?patterns=%EB%A1%9C%EA%B7%B8%EC%9D%B8%C2%B7%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85&imgId=cms365yt10003ju04wka1ot1c | 필드 위 라벨(이메일·비밀번호)을 두는 라벨형 입력 구조와 로그인 버튼 아래 링크 줄 배치 (자동 로그인·소셜 버튼은 제외) |

## 화면 14
| # | ui_url | 가져올 것 |
|---|---|---|
| 1 | https://uibowl.io/name/%EC%B0%A8%EB%9E%80?patterns=%EB%A1%9C%EA%B7%B8%EC%9D%B8%C2%B7%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85&imgId=cmtwj2v0w0024l704w56lw8jy | 한 페이지 안: 입력 필드(이름·이메일·비밀번호·비밀번호 확인, 필수 표시) → 구분선 → "모두 동의" + 필수 약관 체크 → 하단 전폭 가입 버튼(필수 미충족 시 비활성) 순서 |
| 2 | https://uibowl.io/name/%EC%88%A8%EA%B3%A0?patterns=%EB%A1%9C%EA%B7%B8%EC%9D%B8%C2%B7%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85&imgId=xhpn2qsjti53neq92ezc87nn | 단계형 대안: 상단 진행 바 + 단계별 제목, 비밀번호 확인 필드 아래 일치 여부 인라인 1줄, 마지막에 약관 동의를 바텀시트로 받는 흐름 |
| 3 | https://uibowl.io/name/%EC%95%B3%ED%94%8C%EB%A6%AC?patterns=%EC%95%BD%EA%B4%80%EB%8F%99%EC%9D%98 | 단계 수를 우상단 "n/N"으로 표시(학교 → 정보 → 약관 등), 약관 행 우측 › 로 전문 보기 진입 |
| 4 | https://uibowl.io/name/redBus?patterns=%EC%A1%B0%ED%9A%8C%ED%95%98%EA%B8%B0&patternName=%EC%A7%80%EC%97%AD%26%EB%82%A0%EC%A7%9C%20%EC%84%A0%ED%83%9D | 시/도·지역·학교 3개 선택 필드를 한 묶음 안에 세로로 쌓아 가입 폼 최상단 블록으로 두는 배치 |
| 5 | https://uibowl.io/name/MakeMyTrip?patterns=%EC%98%88%EC%95%BD%C2%B7%EA%B2%B0%EC%A0%9C&patternName=1.%EB%82%A0%EC%A7%9C%20%EB%B0%8F%20%EC%A7%80%EC%97%AD%20%EC%84%A0%ED%83%9D | 필드 탭 → 선택 목록 → 값이 채워진 폼으로 복귀를 시/도 → 지역 → 학교 순으로 반복, 앞 단계 미선택 시 다음 필드 비활성 |
