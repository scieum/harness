# S2 설계 — run 20261002-2019

대상 화면: 1 (로그인), 14 (회원가입) · 학교 기본값: input.json
변경 사유: 2026-10-02 사용자 결정 — 로그인은 개인 이메일·비밀번호만, 학교는 회원가입에서 한 번 골라 계정에 저장한다(PRD §7 1·14, story-service 결정 사항 "학교 선택", rules.json never.N1 school_select_screen = 14, auth).
기준 설계: runs/20261001-1910 화면 1(학교 고르기 포함 로그인), runs/20261002-1138 화면 1(하늘색 톤). 둘 다 수정하지 않고, 학교 3단계 블록과 진행 막대·선택 목록 표현은 화면 14로 옮겨 그대로 쓴다. 같은 컴포넌트 이름과 톤을 따른다.
근거: docs/PRD.md §5·§6·§7, docs/story-service.md(N1·N2, 결정 사항 "학교 선택"·"모바일 하단 탭바"), docs/design.md(ex-auth-form-card, text-input, button-primary, button-pill-soft, nav-pill), harness/rules.json(never.N1, auth, tab_bar, colors), research/s1-adopt.md, neis.json(화면 14 목록 값)
색·폰트·모서리·간격은 docs/design.md와 harness/rules.json을 따른다. 허용 색 밖의 값은 쓰지 않는다. 그림자는 쓰지 않는다.
- 핑크 #d6246a·연핑크 #fbe9f0는 두 화면 모두 쓰지 않는다(재고 신호가 없는 화면).
- 하늘색 #2b9fe0(선·인디케이터·아이콘·진행 막대)과 옅은 하늘색 #e6f4fc(선택 바탕)는 선택 상태·진행·아이콘 강조에만 쓴다. 글자색으로 쓰지 않고(하늘색 위 글자는 #141414), button-primary 안에는 쓰지 않는다.
두 화면은 로그인 전 화면이라 역할 구분이 없고, 역할별 노출 표의 컴포넌트를 하나도 담지 않는다. 하단 탭바는 두 화면 모두 모바일·데스크탑에 두지 않는다(로그인 후 화면 2~13 전용).
외부 서비스 연결 값은 서버에서만 다룬다. 학교 목록은 서버가 불러온 값을 보여줄 뿐이며, 두 화면에 연결 값 입력·외부 서비스 설정·AI 엔진 선택 UI를 두지 않는다.
학교는 회원가입(화면 14)에서만 고르고, 로그인(화면 1)에는 학교 관련 입력·표시를 두지 않는다. 로그인하면 계정에 저장된 학교의 데이터만 보인다(N1).

## 화면 1
로그인. 개인 이메일 + 비밀번호만 받는다. 아이디 찾기·소셜 로그인·자동 로그인은 두지 않는다.
모바일(390×844) 위→아래: nav-pill → ex-auth-form-card(제목 → 이메일 → 비밀번호 → 로그인 버튼 → 비밀번호 찾기 링크) → 카드 아래 "아직 회원이 아니신가요?" + 회원가입 보조 버튼. 좌우 여백 16, 블록 사이 24. 하단 탭바 없음.
데스크탑(1440×900): nav-pill 아래 가운데 단일 열에 같은 카드와 회원가입 줄을 둔다. 하단 탭바 없음.
### 구성 요소
- nav-pill: "Lab_Stock" 워드마크만 표시. 로그인 전이라 섹션 링크·학교명·CTA는 없다. 하늘색 없음
- ex-auth-form-card: 로그인 카드(#ffffff, 1px #f0f0f0 테두리, rounded 24, 안쪽 여백 24). 위에 제목 "로그인"(heading-3) + 보조 문구 "개인 이메일로 로그인하세요"(body-lg). 아래 text-input 2개(라벨 위·입력 아래) → button-primary "로그인" → 버튼 바로 아래 가운데 "비밀번호 찾기" 밑줄 텍스트 링크(body-sm, #707070, 누름 영역 44 이상). 학교 관련 필드·문구는 두지 않는다. 하늘색 없음
- text-input: 라벨 "개인 이메일"(플레이스홀더 "name@example.com", #adadad), 라벨 "비밀번호"(가림 입력, 오른쪽 보기 토글 눈 아이콘 #707070). #f0f0f0 채움, 테두리 없음, rounded 16. 포커스 링은 2px #141414. 하늘색 없음
- button-primary: 카드 안 전폭 "로그인"(#141414 채움, #ffffff 글자, rounded 9999, 높이 44 이상). 두 필드가 모두 채워지기 전에는 비활성. 하늘색 없음
- button-pill-soft: 카드 아래 한 줄 "아직 회원이 아니신가요?"(body-sm, #707070) 옆 "회원가입 ›"(#f3f3f3 채움, 라벨 #141414, rounded 9999, 높이 44 이상). 누르면 화면 14 회원가입. 하늘색: 오른쪽 › 아이콘 #2b9fe0(라벨 글자는 #141414)
### 반영한 레퍼런스
- https://uibowl.io/name/%EB%A7%88%ED%94%8C?patterns=%EB%A1%9C%EA%B7%B8%EC%9D%B8%C2%B7%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85&patternName=%EC%9D%B4%EB%A9%94%EC%9D%BC%20%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85
- https://uibowl.io/name/%EC%8F%98%EC%B9%B4?patterns=%EB%A1%9C%EA%B7%B8%EC%9D%B8%C2%B7%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85&imgId=cmogjlpe3000ajs04ljmhxqd1
- https://uibowl.io/name/%ED%95%9C%ED%8C%A8%EC%8A%A4?patterns=%EB%A1%9C%EA%B7%B8%EC%9D%B8%C2%B7%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85&imgId=cmq0n0zuu000hky04aw29j4qo
- https://uibowl.io/name/%EC%BD%94%EC%98%A4%EB%A1%B1%EB%AA%B0?patterns=%EB%A1%9C%EA%B7%B8%EC%9D%B8%C2%B7%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85&imgId=cms365yt10003ju04wka1ot1c

## 화면 14
회원가입. 화면 1의 "회원가입"으로 들어온다. 학교(시/도 → 지역 → 학교)와 계정 정보(이름·개인 이메일·비밀번호)를 받는다.
레퍼런스 결정: 한 페이지. 화면당 프레임이 1장(14-mobile·14-desktop)이고 학교 3필드가 이미 앞 필드 선택 전 비활성으로 순서를 강제하므로, 단계를 나누지 않고 한 카드 안에 학교 블록 → 계정 블록 → 약관 순서로 둔다.
예시 상태(neis.json): 시/도 "충청북도" 선택됨 → 지역 "청주시" 선택됨 → 학교는 아직 고르지 않음(플레이스홀더 "학교 선택"). 계정 필드는 비어 있고, 가입 버튼은 비활성.
모바일(390×844) 위→아래: nav-pill → ex-auth-form-card(제목 → 학교 진행 막대 → 시/도 → 지역 → 학교 → 구분 여백 → 이름 → 개인 이메일 → 비밀번호 → 비밀번호 확인 → 약관 동의 → 가입하기). 카드가 길면 본문이 스크롤되고 button-primary는 화면 하단에 고정한다. 좌우 여백 16, 필드 사이 12, 블록 사이 24. 하단 탭바 없음.
데스크탑(1440×900): nav-pill 아래 가운데 단일 열 카드. 버튼은 카드 맨 아래. 하단 탭바 없음.
### 구성 요소
- nav-pill: 뒤로가기(화면 1) + "Lab_Stock" 워드마크 + 제목 "회원가입". 학교를 고르는 중이라 학교명은 표시하지 않는다. 하늘색: 뒤로가기 아이콘 #2b9fe0
- ex-auth-form-card: 가입 카드(#ffffff, 1px #f0f0f0 테두리, rounded 24, 안쪽 여백 24). 제목 "회원가입"(heading-3) + 보조 문구 "우리 학교를 고르고 계정을 만드세요"(body-lg). ① 학교 블록: 소제목 "학교"(heading-4) + 3단계 진행 막대(시/도 → 지역 → 학교 중 채운 단계만 #2b9fe0, 나머지 #e0e0e0, rounded 9999. 예시 상태 = 2칸 채움) + 아래 시/도·지역·학교 필드 3개를 한 묶음으로 세로로 쌓는다. ② 계정 블록: 소제목 "계정"(heading-4) + text-input 4개(라벨 위·입력 아래, 라벨 옆 caption "필수"). ③ 약관 동의: "모두 동의" 한 줄(body, #141414) → 1px #f0f0f0 구분선 → 필수 약관 2줄 "서비스 이용약관 동의 (필수)", "개인정보 수집·이용 동의 (필수)"(body-sm, #141414), 각 줄 오른쪽 › 를 누르면 전문 보기. 각 줄 왼쪽 원형 체크(rounded 9999, 누름 영역 44 이상): 미동의 = 1px #e0e0e0 원, 동의 = #2b9fe0 채움 원 + #ffffff 체크 표시. 예시 상태 = 모두 미동의. 하늘색: 진행 막대 채운 구간, 동의한 체크 원, 약관 줄 › 아이콘 #2b9fe0(글자는 모두 #141414)
- school-select-sido: 학교 블록 첫 번째 필드 "시/도". 탭하면 별도 선택 목록(neis.json sido_list)이 열리고, 고른 값이 필드에 돌아와 표시된다. 예시 상태 값 "충청북도"(선택됨). 하늘색: 값이 선택된 필드 = #e6f4fc 바탕 + 오른쪽 #2b9fe0 체크 아이콘(값 글자는 #141414), 선택 목록의 현재 선택 행 배경 #e6f4fc + 오른쪽 체크 아이콘 #2b9fe0
- school-select-region: 두 번째 필드 "지역(시/군/구)". 시/도를 고르기 전에는 비활성(#f0f0f0 바탕, 글자 #adadad). 목록은 고른 시/도의 지역(neis.json region_list). 예시 상태 값 "청주시"(선택됨). 하늘색: 값이 선택된 필드 = #e6f4fc 바탕 + 오른쪽 #2b9fe0 체크 아이콘(값 글자는 #141414), 선택 목록의 현재 선택 행 배경 #e6f4fc + 체크 아이콘 #2b9fe0
- school-select-school: 세 번째 필드 "학교". 지역을 고르기 전에는 비활성. 목록은 고른 지역의 고등학교(neis.json school_list). 예시 상태 = 아직 고르지 않음: #f0f0f0 바탕 + 플레이스홀더 "학교 선택"(#adadad) + 오른쪽 펼침 아이콘 #707070. 고르면 위 두 필드와 같이 #e6f4fc 바탕 + #2b9fe0 체크 아이콘(글자 #141414). 하늘색: 선택 목록의 현재 선택 행 배경 #e6f4fc + 체크 아이콘 #2b9fe0
- text-input: 계정 블록 입력 4개 "이름", "개인 이메일"(플레이스홀더 "name@example.com"), "비밀번호"(가림, 보기 토글 눈 아이콘 #707070), "비밀번호 확인"(가림). #f0f0f0 채움, 테두리 없음, rounded 16, 포커스 링 2px #141414. "비밀번호 확인" 아래 일치 여부 인라인 1줄(caption): 일치 = #2b9fe0 체크 아이콘 + "비밀번호가 일치해요"(#141414), 불일치 = "비밀번호가 일치하지 않아요"(#141414), 비어 있으면 숨김. 하늘색: 일치 체크 아이콘만
- button-primary: 전폭 "가입하기"(#141414 채움, #ffffff 글자, rounded 9999, 높이 44 이상). 학교 3필드·계정 4필드·필수 약관 2개가 모두 채워지고 비밀번호가 일치하기 전에는 비활성. 예시 상태 = 비활성. 누르면 계정에 고른 학교를 저장하고 로그인 후 첫 화면(화면 13)으로 간다. 하늘색 없음
### 반영한 레퍼런스
- https://uibowl.io/name/%EC%B0%A8%EB%9E%80?patterns=%EB%A1%9C%EA%B7%B8%EC%9D%B8%C2%B7%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85&imgId=cmtwj2v0w0024l704w56lw8jy
- https://uibowl.io/name/%EC%88%A8%EA%B3%A0?patterns=%EB%A1%9C%EA%B7%B8%EC%9D%B8%C2%B7%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85&imgId=xhpn2qsjti53neq92ezc87nn
- https://uibowl.io/name/%EC%95%B3%ED%94%8C%EB%A6%AC?patterns=%EC%95%BD%EA%B4%80%EB%8F%99%EC%9D%98
- https://uibowl.io/name/redBus?patterns=%EC%A1%B0%ED%9A%8C%ED%95%98%EA%B8%B0&patternName=%EC%A7%80%EC%97%AD%26%EB%82%A0%EC%A7%9C%20%EC%84%A0%ED%83%9D
- https://uibowl.io/name/MakeMyTrip?patterns=%EC%98%88%EC%95%BD%C2%B7%EA%B2%B0%EC%A0%9C&patternName=1.%EB%82%A0%EC%A7%9C%20%EB%B0%8F%20%EC%A7%80%EC%97%AD%20%EC%84%A0%ED%83%9D

## 역할별 노출
앱 전체 기준 개수. runs/20261002-1416 표를 그대로 옮겼다. 화면 1·14는 로그인 전 화면이라 표의 컴포넌트를 하나도 담지 않으므로 숫자가 바뀌지 않는다.

| 컴포넌트 | 학생 | 교사 | admin |
|---|---|---|---|
| manual-upload | 0 | 2 | 2 |
| reorder-alert-card | 0 | 2 | 2 |
| vendor-link | 0 | 1 | 1 |
| vendor-register | 0 | 0 | 2 |
| msds-entry | 3 | 3 | 3 |
| stock-intake | 0 | 2 | 2 |
| reagent-register | 0 | 1 | 1 |
| user-manage | 0 | 0 | 2 |
| cabinet-edit | 0 | 2 | 2 |
