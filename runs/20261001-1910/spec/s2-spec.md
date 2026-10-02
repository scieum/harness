# S2 설계 — run 20261001-1910

대상 화면: 1, 4, 5 · 학교: 샘플고등학교 (input.json)
이어지는 작업: runs/20261001-1844 (화면 2·3·6). 같은 컴포넌트 이름과 톤을 따른다.
근거: docs/PRD.md §3·§4·§5·§7, docs/story-service.md 결정 사항, research/s1-adopt.md, neis.json(화면 1 목록)
색·폰트·모서리·간격은 docs/design.md와 harness/rules.json을 따른다. 재고 부족 강조색 #d6246a는 badge-low-stock과 reorder-alert-card 안에서만 쓴다(화면 1·4·5에서는 쓰지 않는다).
학교 선택(school-select)은 화면 1에만 있다. 화면 4·5에는 school-select를 두지 않고 nav-pill 안에 현재 학교명 "샘플고등학교"를 표시한다.
외부 서비스 연결 값은 서버에서만 다룬다. 어떤 화면에도 연결 값 입력·외부 서비스 설정·AI 엔진 선택 UI를 두지 않는다.
괄호 안 역할 표시가 없는 구성 요소는 학생·교사·admin 모두에게 보인다.

## 화면 1
### 구성 요소
- nav-pill: "Lab_Stock" 워드마크만 표시. 로그인 전이라 섹션 링크와 학교명은 없다
- ex-auth-form-card: 로그인 카드. 제목 "로그인"(heading-3) + 보조 문구 "우리 학교를 선택하고 로그인하세요"(body-lg). 아래 학교 선택 3개 필드를 한 묶음 안에 세로로 쌓는다
- school-select-sido: 첫 번째 필드 "시/도". 탭하면 별도 선택 목록(neis.json sido_list)이 열리고, 고른 값이 필드에 돌아와 표시된다. 기본값 "충청북도"
- school-select-region: 두 번째 필드 "지역(시/군/구)". 시/도를 고르기 전에는 비활성. 목록은 고른 시/도의 지역(neis.json region_list), 기본값 "청주시"
- school-select-school: 세 번째 필드 "학교". 지역을 고르기 전에는 비활성. 목록은 고른 지역의 고등학교(neis.json school_list), 플레이스홀더 "학교 선택"
- text-input: 학교 선택 묶음 아래 로그인 정보 입력 2개("아이디", "비밀번호")
- button-primary: 카드 하단 전폭 "로그인". 학교를 고르기 전에는 비활성
### 반영한 레퍼런스
- https://uibowl.io/name/%EC%8A%A4%ED%8A%9C%EB%94%94%EC%98%A4%EB%A9%94%EC%9D%B4%ED%8A%B8?patterns=%ED%95%84%ED%84%B0&patternName=%EC%A7%80%EC%97%AD%20%EC%84%A0%ED%83%9D
- https://uibowl.io/name/redBus?patterns=%EC%A1%B0%ED%9A%8C%ED%95%98%EA%B8%B0&patternName=%EC%A7%80%EC%97%AD%26%EB%82%A0%EC%A7%9C%20%EC%84%A0%ED%83%9D
- https://uibowl.io/name/MakeMyTrip?patterns=%EC%98%88%EC%95%BD%C2%B7%EA%B2%B0%EC%A0%9C&patternName=1.%EB%82%A0%EC%A7%9C%20%EB%B0%8F%20%EC%A7%80%EC%97%AD%20%EC%84%A0%ED%83%9D

## 화면 4
### 구성 요소
- nav-pill: 뒤로가기(화면 3) + 제목 "사용 기록" + 현재 학교명 "샘플고등학교" 텍스트. 학교 전환 기능은 두지 않는다. 데스크탑 섹션 링크는 화면 2와 같다("시약 목록", 교사·admin에게만 "재주문 알림")
- reagent-detail-card: 폼 상단 고정 요약. 시약명(title) + 현재 재고량·단위(body). 무엇을 기록하는지 보여준다. 재고 부족 배지는 두지 않는다
- text-input: 라벨 위·입력 아래 세로 폼. 순서대로 "사용 날짜"(필수), "사용량"(필수) + 단위, "사용자"(필수, 로그인한 사용자 이름이 기본값), "메모". 필수 라벨 옆에 caption "필수"
- button-primary: 하단 전폭 "사용 기록 저장". 필수 항목이 비면 비활성. 학생·교사·admin 모두
- ex-toast: 저장 직후 "사용 기록을 저장했어요" 알림, 이후 화면 3 "사용 기록" 탭으로 돌아간다
### 반영한 레퍼런스
- https://uibowl.io/name/%EC%98%A4%ED%81%B4%EA%B3%A0?patterns=%EA%B8%80%EC%93%B0%EA%B8%B0&patternName=%EA%B8%B0%EB%A1%9D%ED%95%98%EA%B8%B0
- https://uibowl.io/name/%EC%98%A4%EB%8A%98%EC%9D%98%20%EB%A3%A8%ED%8B%B4?patterns=%EA%B8%80%EC%93%B0%EA%B8%B0&patternName=%EB%A3%A8%ED%8B%B4%20%EA%B8%B0%EB%A1%9D%ED%95%98%EA%B8%B0
- https://uibowl.io/name/%EB%A0%88%ED%8F%AC%EB%B8%8C?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&patternName=%EA%B8%B0%EB%A1%9D%ED%95%98%EA%B8%B0

## 화면 5
이 화면은 교사·admin만 들어온다. 학생 화면에는 진입 링크와 업로드 버튼이 없다(학생 노출 0).
### 구성 요소
- nav-pill: 뒤로가기(화면 6) + 제목 "실험 매뉴얼" + 현재 학교명 "샘플고등학교" 텍스트. 학교 전환 기능은 두지 않는다 (교사·admin만)
- manual-upload: 1단계 업로드. 상단 안내 문구 "실험 매뉴얼을 올리면 시약별 사용량을 찾아드려요"(body-lg) + 중앙 업로드/미리보기 타일(rounded 16, 비율 유지) + 미리보기 위 badge-overlay 파일 이름 태그 (교사·admin만)
- badge-overlay: manual-upload 미리보기 위 파일 이름 태그 (교사·admin만)
- text-input: 업로드 타일 아래 "조 수" 숫자 입력 1개 (교사·admin만)
- button-primary: 1단계 하단 고정 "AI 추출". 파일과 조 수가 비면 비활성, 누르면 처리 중 상태 문구 "사용량을 찾고 있어요"를 거쳐 2단계로 간다 (교사·admin만)
- extraction-table: 2단계 추출 결과 확인. 상단 제목 "추출 결과 확인" + 닫기, 본문 스크롤 표. ex-data-table-cell 4열 = 시약명 · 1조 사용량 · 단위 · 1반 1회 필요량(1조 사용량 × 조 수). 사용량 칸은 text-input으로 고칠 수 있다 (교사·admin만)
- ex-data-table-cell: extraction-table 안 머리행·본문 셀 (교사·admin만)
- button-outline: 2단계 하단 "다시 추출" (교사·admin만)
- button-primary: 2단계 하단 전폭 "확인 후 저장". 사용자가 확인한 뒤에만 저장된다 (교사·admin만)
- ex-toast: 저장 직후 "재주문 기준을 저장했어요" 알림, 이후 화면 6으로 돌아간다 (교사·admin만)
### 반영한 레퍼런스
- https://uibowl.io/name/%EB%8B%A4%EA%B8%80%EB%A1%9C?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&patternName=%EC%9C%A0%ED%8A%9C%EB%B8%8C%20%EB%A7%81%ED%81%AC%20%EC%97%85%EB%A1%9C%EB%93%9C
- https://uibowl.io/name/%EC%88%98%ED%98%84%EC%9D%B4%EB%9E%91?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&patternName=%EA%B3%B5%EC%9C%A0%20%EC%95%A8%EB%B2%94%20%EC%97%85%EB%A1%9C%EB%93%9C
- https://uibowl.io/name/%ED%82%A4%ED%94%BC%EB%9F%BD?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&patternName=%EC%9D%B8%EC%A6%9D%EC%83%B7-%EC%97%85%EB%A1%9C%EB%93%9C

## 역할별 노출
앱 전체(화면 1~6, runs/20261001-1844 설계 포함) 기준 개수. manual-upload는 화면 6 진입 버튼 1 + 화면 5 업로드 영역 1.

| 컴포넌트 | 학생 | 교사 | admin |
|---|---|---|---|
| manual-upload | 0 | 2 | 2 |
| reorder-alert-card | 0 | 1 | 1 |
| vendor-link | 0 | 1 | 1 |
| vendor-register | 0 | 0 | 1 |
| msds-entry | 1 | 1 | 1 |
