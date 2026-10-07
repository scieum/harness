# S2 설계 — run 20261007-1305

대상 화면: 14 (회원가입) · 상태 화면 14-no-school · 학교 기본값: input.json (이 화면에는 현재 학교명을 표시하지 않는다)
변경 사유: 2026-10-07 사용자 결정(개발 세션 요청 4) — 초·중·고 학교급. 회원가입 학교 선택을 시/도 → 지역 → 학교급 → 학교 4단계로 바꾸고, 그 지역에 그 학교급 학교가 없을 때의 안내 상태를 더한다.
근거: docs/design.md "School level (screen 14)"(school-select-kind), docs/story-service.md 결정 사항 "학교 선택" 행, harness/rules.json never.N1 school_select_levels·school_kind_select·screens_required 14·variants 14 no-school·neis.school_kinds, research/s1-adopt.md, neis.json(시안 목록 값).
기준 설계(수정하지 않음): runs/20261002-2019/spec/s2-spec.md 화면 14. 기존 구성 요소 이름(nav-pill, ex-auth-form-card, school-select-sido, school-select-region, school-select-school, text-input, button-primary)과 톤을 그대로 유지하고, 학교급 칸·학교 0개 안내·로그인으로 돌아가는 보조 버튼만 더하거나 바꾼다.
색·폰트·모서리·간격은 docs/design.md와 harness/rules.json을 따른다. 허용 색 밖의 값은 쓰지 않는다. 그림자는 쓰지 않는다(segmented-control-active 예외).
- 핑크 #d6246a·연핑크 #fbe9f0는 쓰지 않는다(재고·혼재 신호가 없는 화면). 학교 0개 안내도 무채색이다.
- 하늘색 #2b9fe0(선·인디케이터·아이콘·진행 막대)과 옅은 하늘색 #e6f4fc(선택 바탕)는 선택 상태·진행·아이콘 강조에만 쓴다. 글자색으로 쓰지 않고(그 위 글자는 #141414), button-primary 안에는 쓰지 않는다.
로그인 전 화면이라 역할 구분이 없고, 역할별 노출 표의 컴포넌트를 하나도 담지 않는다. 하단 탭바(tab-bar)는 모바일·데스크탑 모두 두지 않는다. nav-pill에 현재 학교명·nav-account-menu를 두지 않는다(학교를 고르는 중).
학교는 이 화면(14)에서만 고른다. 학교 목록은 서버가 불러온 NEIS 값을 보여줄 뿐이며, 고른 학교는 계정에 저장되어 로그인 후 그 학교 데이터만 보인다(N1).
외부 서비스 연결 값은 서버에서만 다룬다. 이 화면에 연결 값 입력 칸·외부 서비스 설정·AI 엔진 선택 UI·관련 문구를 두지 않는다(N2).

## 화면 14
회원가입. 화면 1의 "회원가입 ›" 또는 화면 15 "회원가입"으로 들어온다. 학교(시/도 → 지역 → 학교급 → 학교)와 계정 정보(이름·개인 이메일·비밀번호)를 받는다.
레퍼런스 결정: 한 페이지 유지(기준 설계와 같음). 앞 단계를 고르기 전에는 다음 칸이 비활성이라 순서가 강제된다(레퍼런스 1). 학교급은 목록·시트가 아니라 3칸을 한눈에 보이는 가로 segmented-control로 둔다(레퍼런스 3). 시/도·지역·학교는 ▾ 선택 상자 → 제목 + × 닫기 바텀시트 목록(레퍼런스 4).
예시 상태(프레임 14-mobile · 14-desktop, neis.json): 시/도 "충청북도" 선택됨 → 지역 "청주시" 선택됨 → 학교급 아직 고르지 않음(3칸 모두 비활성 라벨, 흰 pill 없음) → 학교 칸 비활성 "학교급을 먼저 골라 주세요". 계정 필드는 비어 있고, 약관 모두 미동의, 가입 버튼 비활성.
모바일(390×844) 위→아래: nav-pill → ex-auth-form-card(제목 → 학교 블록[진행 막대 → 시/도 → 지역 → 학교급 → 학교] → 계정 블록[이름 → 개인 이메일 → 비밀번호 → 비밀번호 확인] → 약관 동의) → 카드 아래 로그인 줄 → 하단 고정 "가입하기". 좌우 여백 16, 필드 사이 12, 블록 사이 24. 본문이 스크롤되고 button-primary는 화면 하단에 고정. 하단 탭바 없음.
데스크탑(1440×900): nav-pill 아래 가운데 단일 열 카드, 같은 순서. 버튼은 카드 맨 아래, 로그인 줄은 카드 아래. 하단 탭바 없음.
### 구성 요소
- nav-pill: 뒤로가기(화면 1) + "Lab_Stock" 워드마크 + 제목 "회원가입". 학교를 고르는 중이라 학교명·nav-account-menu는 표시하지 않는다. 하늘색: 뒤로가기 아이콘 #2b9fe0
- ex-auth-form-card: 가입 카드(#ffffff, 1px #f0f0f0 테두리, rounded 24, 안쪽 여백 24). 제목 "회원가입"(heading-3) + 보조 문구 "우리 학교를 고르고 계정을 만드세요"(body-lg). ① 학교 블록: 소제목 "학교"(heading-4) + 안내 박스 1개(#e6f4fc 채움, rounded 16, 여백 16, 글자 #141414 body-sm "고른 학교의 시약·기록만 보여요. 가입한 뒤에는 바꿀 수 없어요", 왼쪽 정보 아이콘 #2b9fe0 — 레퍼런스 5) + 4단계 진행 막대(시/도 → 지역 → 학교급 → 학교 중 채운 단계만 #2b9fe0, 나머지 #e0e0e0, rounded 9999, 예시 상태 = 2칸 채움) + 아래 시/도·지역·학교급·학교 4칸을 이 순서로 세로로 쌓는다. ② 계정 블록: 소제목 "계정"(heading-4) + text-input 4개(라벨 위·입력 아래, 라벨 옆 caption "필수" #707070). ③ 약관 동의: "모두 동의" 한 줄(body) → 1px #f0f0f0 구분선 → 필수 약관 2줄 "서비스 이용약관 동의 (필수)", "개인정보 수집·이용 동의 (필수)"(body-sm), 각 줄 오른쪽 › 전문 보기. 각 줄 왼쪽 원형 체크(rounded 9999, 누름 영역 44 이상): 미동의 = 1px #e0e0e0 원, 동의 = #2b9fe0 채움 원 + #ffffff 체크. 예시 상태 = 모두 미동의. 하늘색: 안내 박스, 진행 막대 채운 구간, 동의한 체크 원, 약관 › 아이콘(글자는 모두 #141414)
- school-select-sido: 학교 블록 첫 번째 칸 "시/도"(▾ 선택 상자, text-input 모양 #f0f0f0 rounded 16). 누르면 바텀시트(제목 "시/도 선택" + 오른쪽 위 × 닫기, 1px #e0e0e0 테두리, 위쪽 rounded 24, 딤 없음, 데스크탑은 가운데 ex-modal-card 모양) 목록(neis.json sido_list)이 열리고 고른 값이 칸에 돌아온다. 예시 값 "충청북도"(선택됨). 시/도를 바꾸면 지역·학교급·학교가 비워진다. 하늘색: 선택된 칸 = #e6f4fc 바탕 + 오른쪽 #2b9fe0 체크 아이콘(값 글자 #141414), 시트의 현재 선택 행 배경 #e6f4fc + 체크 #2b9fe0
- school-select-region: 두 번째 칸 "지역(시/군/구)". 시/도를 고르기 전에는 비활성(#f0f0f0 바탕, 글자 #adadad). 목록은 고른 시/도의 지역(neis.json region_list, 바텀시트 제목 "지역 선택" + ×). 예시 값 "청주시"(선택됨). 지역을 바꾸면 학교가 비워진다(학교급은 유지). 하늘색: 선택된 칸 = #e6f4fc 바탕 + #2b9fe0 체크 아이콘(글자 #141414), 시트 현재 선택 행 #e6f4fc + 체크 #2b9fe0
- school-select-kind: 세 번째 칸 "학교급" — 라벨(caption "필수") 아래 segmented-control 3칸 "초등학교 · 중학교 · 고등학교"(#f3f3f3 트랙, rounded 9999, 각 칸 같은 폭 전폭 pill 누름 영역 44 이상). 기본값 없음: 고르기 전에는 흰 pill(segmented-control-active)이 없고 3칸 라벨 모두 #707070. 지역을 고르기 전에는 트랙 전체 비활성(라벨 #adadad). 고르면 그 칸이 흰 pill로 떠오르고(segmented-control-active, 1px #2b9fe0 테두리, 라벨 #141414) 학교 칸이 켜진다. 학교급을 바꾸면 학교가 비워진다. 예시 상태 = 지역은 골랐고 학교급은 아직 고르지 않음(3칸 #707070, 선택 가능). 특수학교·각종학교 칸은 없다. 하늘색: 선택된 칸 테두리 #2b9fe0만(글자 #141414)
- school-select-school: 네 번째 칸 "학교". 학교급을 고르기 전에는 비활성 — #f0f0f0 바탕 + 칸 안 플레이스홀더 "학교급을 먼저 골라 주세요"(#adadad) + 오른쪽 ▾ #adadad (예시 상태, 레퍼런스 1). 학교급을 고르면 플레이스홀더 "학교 선택"(#adadad) + ▾ #707070로 켜지고, 누르면 바텀시트(제목 "학교 선택" + ×, 위쪽 학교 이름 검색 text-input) 목록 = 고른 지역·학교급의 학교(neis.json school_list). 목록 행 = 학교명(title) + 주소 보조줄(caption #707070) 2줄(레퍼런스 5). 고르면 #e6f4fc 바탕 + #2b9fe0 체크(글자 #141414). 학교가 0개면 상태 화면 14-no-school. 하늘색: 시트 현재 선택 행 배경 #e6f4fc + 체크 #2b9fe0
- text-input: 계정 블록 입력 4개 "이름", "개인 이메일"(플레이스홀더 "name@example.com"), "비밀번호"(가림, 보기 토글 눈 아이콘 #707070), "비밀번호 확인"(가림). #f0f0f0 채움, 테두리 없음, rounded 16, 포커스 링 2px #141414. "비밀번호 확인" 아래 일치 여부 인라인 1줄(caption): 일치 = #2b9fe0 체크 아이콘 + "비밀번호가 일치해요"(#141414), 불일치 = "비밀번호가 일치하지 않아요"(#141414), 비어 있으면 숨김. 하늘색: 일치 체크 아이콘만
- button-primary: 전폭 "가입하기"(#141414 채움, #ffffff 글자 link, rounded 9999, 높이 44 이상). 학교 4칸(시/도·지역·학교급·학교)·계정 4칸·필수 약관 2개가 모두 채워지고 비밀번호가 일치하기 전에는 비활성. 예시 상태 = 비활성. 누르면 계정에 고른 학교를 저장하고 화면 13(홈)으로 간다. 하늘색 없음
- button-pill-soft: 카드 아래 한 줄 "이미 계정이 있으신가요?"(body-sm, #707070) 옆 "로그인 ›"(#f3f3f3 채움, 라벨 #141414, rounded 9999, 높이 44 이상) → 화면 1. 화면 1의 "회원가입 ›" 줄과 짝을 이루는 로그인 링크. 하늘색: 오른쪽 › 아이콘 #2b9fe0(라벨 #141414)
### 반영한 레퍼런스
- https://uibowl.io/name/%EC%95%B3%ED%94%8C%EB%A6%AC?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&imgId=cmtpokofc00ldla042tc04f2x
- https://uibowl.io/name/%EC%97%B4%ED%92%88%ED%83%80?patterns=%EB%A1%9C%EA%B7%B8%EC%9D%B8%C2%B7%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85&imgId=cmq9613iq000ejv04xv68xieo
- https://uibowl.io/name/iM%EB%B1%85%ED%81%AC?patterns=%EB%A1%9C%EA%B7%B8%EC%9D%B8%C2%B7%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85&imgId=cmp0ugxyx00tpkz04wwkohxi8
- https://uibowl.io/name/%EC%8B%A0%ED%95%9C%20%EC%8A%88%ED%8D%BCSOL?patterns=%EA%B3%84%EC%A2%8C&imgId=cmsmkjhjp00ecjr04kvjih9wt

## 상태 화면 14-no-school
화면 14에서 학교급까지 골랐는데 그 지역에 그 학교급 학교가 0개인 상태. 레퍼런스 2: 목록 자리를 그대로 두고 그 자리에 안내 한 줄만 넣는다.
예시 상태(프레임 14-no-school-mobile · 14-no-school-desktop): 시/도 "충청북도" 선택됨 → 지역 "청주시" 선택됨 → 학교급 "고등학교" 선택됨(segmented-control-active) → 학교 칸 자리에 무채색 안내 "이 지역에 고등학교가 없어요 — 지역을 다시 골라 주세요". 진행 막대 3칸 채움. 계정 필드 비어 있음, 가입 버튼 비활성. (값은 neis.json 예시 값을 그대로 쓴 시안용 상태 — 실제 0개 여부와 무관하게 0개일 때의 모양을 보여준다.)
모바일·데스크탑 배치는 화면 14와 같고 학교 칸 자리만 바뀐다. 하단 탭바 없음.
### 구성 요소
- nav-pill: 화면 14와 같음 — 뒤로가기(화면 1) + "Lab_Stock" 워드마크 + 제목 "회원가입". 학교명 없음. 하늘색: 뒤로가기 아이콘 #2b9fe0
- ex-auth-form-card: 화면 14와 같은 가입 카드. 학교 블록 안내 박스·4단계 진행 막대(예시 = 3칸 채움) → 시/도 → 지역 → 학교급 → 학교 자리 순서. 계정 블록·약관 동의는 화면 14와 같음(비어 있음·미동의). 하늘색: 안내 박스, 진행 막대 채운 구간, 약관 › 아이콘
- school-select-sido: "시/도" 값 "충청북도"(선택됨, #e6f4fc 바탕 + #2b9fe0 체크, 글자 #141414)
- school-select-region: "지역(시/군/구)" 값 "청주시"(선택됨, #e6f4fc 바탕 + #2b9fe0 체크, 글자 #141414). 안내 문구가 가리키는 다시 고를 칸
- school-select-kind: segmented-control 3칸 "초등학교 · 중학교 · 고등학교", "고등학교" 선택됨(segmented-control-active). 다른 학교급을 고르면 학교 칸이 다시 계산된다. 하늘색: 선택 칸 테두리 #2b9fe0(글자 #141414)
- school-select-school: 학교 칸 자리 그대로(같은 높이·폭, rounded 16, #f3f3f3 채움, 테두리 없음) 안에 ▾·선택 상자 대신 무채색 안내 한 줄 — #707070 정보 아이콘 + body-sm #141414 "이 지역에 고등학교가 없어요 — 지역을 다시 골라 주세요"({학교급} = 고른 학교급 이름). 누를 수 없음(목록이 열리지 않음). 핑크 없음, 하늘색 없음
- segmented-control: 학교급 트랙(#f3f3f3, rounded 9999). 고르지 않은 칸 라벨 #707070
- segmented-control-active: 선택된 학교급 "고등학교" 흰 pill(#ffffff, 그림자 허용 예외). 하늘색: 1px #2b9fe0 테두리(글자 #141414)
- text-input: 계정 블록 입력 4개(화면 14와 같음, 비어 있음)
- button-primary: 전폭 "가입하기" 비활성(학교 미선택). 하늘색 없음
- button-pill-soft: 카드 아래 "이미 계정이 있으신가요?" + "로그인 ›" → 화면 1(화면 14와 같음). 하늘색: › 아이콘 #2b9fe0
### 반영한 레퍼런스
- https://uibowl.io/name/%EC%95%84%EC%9D%B4%EC%BF%A0%EC%B9%B4?patterns=%ED%95%84%ED%84%B0&imgId=cmp0thltg016ll904utyi4ydx
- https://uibowl.io/name/%EC%95%B3%ED%94%8C%EB%A6%AC?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&imgId=cmtpokofc00ldla042tc04f2x
- https://uibowl.io/name/%EC%97%B4%ED%92%88%ED%83%80?patterns=%EB%A1%9C%EA%B7%B8%EC%9D%B8%C2%B7%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85&imgId=cmq9613iq000ejv04xv68xieo

## 역할별 노출
앱 전체(화면 1~13) 기준 개수. runs/20261007-0848 표를 그대로 옮겼다. 화면 14는 로그인 전 화면이라 표의 컴포넌트를 하나도 담지 않으므로 숫자가 바뀌지 않는다. msds-entry = 화면 3 1 + 화면 10 상세 1(학생·교사·admin 모두, R4 충족).

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
