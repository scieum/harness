# S2 설계 — run 20261002-1032

대상 화면: 7, 8, 10, 9, 1, 4, 5 · 학교: 샘플고등학교 (input.json)
이어지는 작업: runs/20261002-0838 (화면 2·3·6, 하늘색 버전), runs/20261001-1910 (화면 1·4·5, 하늘색 이전). 같은 컴포넌트 이름과 톤을 따른다. 화면 1·4·5는 1910 구성을 그대로 두고 하늘색 강조 위치만 더한다.
근거: docs/PRD.md §3·§4·§5·§7(화면 7~10 추가), docs/story-service.md 결정 사항(추가 화면 7~10), docs/design.md(2026-10-02 하늘색 강조색), research/s1-adopt.md, neis.json(화면 1 목록)
색·폰트·모서리·간격은 docs/design.md와 harness/rules.json을 따른다.
- 재고 부족 강조색 #d6246a는 badge-low-stock과 reorder-alert-card 안에서만 쓴다.
- 하늘색 #2b9fe0(선 굵기·인디케이터·아이콘·진행 막대)과 옅은 하늘색 #e6f4fc(선택 배경)는 선택 상태·활성 탭/세그먼트·링크 밑줄·진행·아이콘 강조에만 쓴다. 글자색으로 쓰지 않고(하늘색 위 글자는 #141414), badge-low-stock·reorder-alert-card·button-primary 안에는 쓰지 않는다.
학교 선택(school-select)은 화면 1에만 있다. 화면 4·5·7·8·9·10에는 학교 선택을 두지 않고 nav-pill 안에 현재 학교명 "샘플고등학교"를 표시한다. 학교 전환 기능은 두지 않는다.
외부 서비스 연결 값은 서버에서만 다룬다. 어떤 화면에도 연결 값 입력·외부 서비스 설정·AI 엔진 선택 UI를 두지 않는다.
괄호 안 역할 표시가 없는 구성 요소는 학생·교사·admin 모두에게 보인다.
새 화면 7~10의 데스크탑 nav-pill 섹션 링크: "시약 목록", "사용 기록 내역", 교사·admin에게만 "재주문 알림"·"입고·시약 등록", admin에게만 "사용자 관리"·"판매처 설정". 모바일에서는 링크를 접고 워드마크·학교명만 남긴다.

## 화면 7
이 화면은 교사·admin만 들어온다. 화면 3의 button-outline "입고"와 nav-pill 섹션 링크로 들어온다. 학생 nav에는 진입 링크가 없다(학생 노출 0).
### 구성 요소
- nav-pill: "Lab_Stock" 워드마크 + 제목 "입고·시약 등록" + 현재 학교명 "샘플고등학교" 텍스트. 하늘색: 데스크탑 현재 섹션 링크("입고·시약 등록") 아래 #2b9fe0 밑줄 인디케이터(글자는 #141414) (교사·admin만)
- segmented-control: 화면 상단에서 두 갈래를 먼저 고른다. "기존 시약 입고 / 새 시약 등록", 한 번에 하나만 선택. 선택된 옵션은 segmented-control-active (교사·admin만)
- segmented-control-active: 선택된 갈래의 흰 pill. 하늘색: 1px #2b9fe0 테두리로 선택 상태 표시(글자는 #141414) (교사·admin만)
- stock-intake: "기존 시약 입고" 갈래. 검색 → 선택 → 수량 입력 순서. 상단 text-input 검색 바("시약명 검색") → 결과 reagent-row 목록에서 시약 1개 선택 → 선택한 시약 아래 "입고 수량"(필수) + 단위, "입고일"(필수, 오늘 날짜 기본값) text-input → 하단 전폭 button-primary "입고". 하늘색: 선택된 결과 행 배경 #e6f4fc + 왼쪽 #2b9fe0 선택 표시 (교사·admin만)
- reagent-register: "새 시약 등록" 갈래. 라벨 위·입력 아래 세로 폼. "시약명"(필수), "종류"(필수, 드롭다운), "재고량"(필수) + 단위, "입고일"(필수), "MSDS 연결 주소" text-input → 하단 전폭 button-primary "시약 등록". 필수 라벨 옆 caption "필수". 하늘색: 종류 드롭다운의 펼침 아이콘 #2b9fe0, 열린 목록의 현재 선택 항목 배경 #e6f4fc (교사·admin만)
- text-input: stock-intake 검색 바와 수량·날짜 입력, reagent-register 폼 입력. 하늘색: 검색 바 왼쪽 검색 아이콘 #2b9fe0, 날짜 입력 오른쪽 달력 아이콘 #2b9fe0. 포커스 링은 design.md대로 #141414 (교사·admin만)
- reagent-row: stock-intake 검색 결과 한 줄 = 시약명(title) + 현재 재고량·단위(body). 하늘색: 선택 상태는 위 stock-intake 설명과 같다. 재고 부족 표시는 이 화면에 두지 않는다 (교사·admin만)
- button-primary: stock-intake "입고", reagent-register "시약 등록". 필수 항목이 비면 비활성. 하늘색 없음(#141414 채움) (교사·admin만)
- ex-empty-state-card: 검색 결과 0건일 때 "찾는 시약이 없어요" 문구 + button-pill-soft "새 시약 등록" (누르면 "새 시약 등록" 갈래로 전환). 하늘색: 안내 아이콘 #2b9fe0 (교사·admin만)
- ex-toast: 저장 직후 "입고를 기록했어요" / "시약을 등록했어요" 알림, 이후 화면 2로 돌아간다. 하늘색: 완료 체크 아이콘 #2b9fe0 (교사·admin만)
### 반영한 레퍼런스
- https://uibowl.io/name/%EB%B9%BC%EA%B8%B0?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&patternName=%EC%83%81%ED%92%88%20%EB%93%B1%EB%A1%9D
- https://uibowl.io/name/%EC%B0%A8%EB%9E%80?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&patternName=%EC%A7%81%EC%A0%91%ED%8C%90%EB%A7%A4%20%EC%83%81%ED%92%88%EB%93%B1%EB%A1%9D
- https://uibowl.io/name/%EC%9A%B0%EB%A6%AC%EB%8F%99%EB%84%A4GS?patterns=%EC%A1%B0%ED%9A%8C%ED%95%98%EA%B8%B0&patternName=%EC%9E%AC%EA%B3%A0%EC%B0%BE%EA%B8%B0

## 화면 8
이 화면은 admin만 들어온다. 학생·교사 nav에는 진입 링크가 없다(학생·교사 노출 0).
### 구성 요소
- nav-pill: "Lab_Stock" 워드마크 + 제목 "사용자 관리" + 현재 학교명 "샘플고등학교" 텍스트. 하늘색: 데스크탑 현재 섹션 링크("사용자 관리") 아래 #2b9fe0 밑줄 인디케이터 (admin만)
- user-manage: 화면 본문 전체 블록 1개. 상단 헤더 "샘플고등학교 사용자 N명"(heading-3) → button-primary "사용자 초대" → text-input 이름 검색 → 사용자 목록(ex-data-table-cell 행: 이름 · 역할 표시 "학생"/"교사"/"admin" · 행 오른쪽 삭제 버튼). 초대·삭제는 아래 ex-modal-card로 진행한다. 하늘색: 로그인한 admin 본인 행 배경 #e6f4fc (admin만)
- text-input: 사용자 목록 위 이름 검색 바(플레이스홀더 "이름 검색"), 초대 모달 안 초대 대상 입력("이름", "이메일"). 하늘색: 검색 아이콘 #2b9fe0 (admin만)
- ex-data-table-cell: 사용자 목록 머리행(이름 · 역할 · 관리)과 본문 행. 역할 칸은 label 크기 텍스트 pill(#f3f3f3 채움, 글자 #141414). 하늘색 없음(본인 행 배경은 user-manage 설명대로) (admin만)
- ex-modal-card: ① 초대 바텀시트: 제목 "사용자 초대" + 안내문(body-lg) + 초대 방법 button-pill-soft "초대 링크 복사" + 직접 입력 text-input + 역할 선택 segmented-control + 하단 전폭 button-primary "N명 초대"(0명이면 비활성). ② 삭제 확인: "이 사용자를 삭제할까요?" + button-outline "취소" + button-primary "삭제". 하늘색: "초대 링크 복사"의 링크 아이콘 #2b9fe0 (admin만)
- segmented-control: 초대 모달 안 역할 선택 "학생 / 교사", 한 번에 하나만 선택 (admin만)
- segmented-control-active: 선택된 역할 흰 pill. 하늘색: 1px #2b9fe0 테두리(글자는 #141414) (admin만)
- button-pill-soft: 초대 모달 "초대 링크 복사" (admin만)
- button-primary: "사용자 초대", 모달 "N명 초대"·"삭제". 하늘색 없음 (admin만)
- button-outline: 사용자 행 오른쪽 "삭제", 삭제 모달 "취소" (admin만)
- ex-empty-state-card: 검색 결과 0건일 때 "찾는 사용자가 없어요" 문구. 하늘색: 안내 아이콘 #2b9fe0 (admin만)
- ex-toast: 초대·삭제 직후 "N명을 초대했어요" / "사용자를 삭제했어요" 알림, 이후 사용자 목록으로 돌아온다. 하늘색: 완료 체크 아이콘 #2b9fe0 (admin만)
### 반영한 레퍼런스
- https://uibowl.io/name/%EC%9B%8C%ED%81%AC%EC%98%A8?patterns=%EC%B4%88%EB%8C%80%ED%95%98%EA%B8%B0%C2%B7%EB%B0%9B%EA%B8%B0&patternName=%EC%BB%A4%EB%AE%A4%EB%8B%88%ED%8B%B0%20%EB%A9%A4%EB%B2%84%20%EC%B4%88%EB%8C%80
- https://uibowl.io/name/%ED%8C%A8%EC%8A%A4%EC%98%A4%EB%8D%94?patterns=%EC%B4%88%EB%8C%80%ED%95%98%EA%B8%B0%C2%B7%EB%B0%9B%EA%B8%B0&patternName=%EA%B0%99%EC%9D%B4%EC%A3%BC%EB%AC%B8%20%EB%A9%A4%EB%B2%84
- https://uibowl.io/name/%EB%A9%94%EA%B0%80MCG%EC%BB%A4%ED%94%BC?patterns=%EC%B4%88%EB%8C%80%ED%95%98%EA%B8%B0%C2%B7%EB%B0%9B%EA%B8%B0&patternName=%EA%B0%99%EC%9D%B4%EC%A3%BC%EB%AC%B8%20%EB%A9%A4%EB%B2%84

## 화면 10
학생·교사·admin 모두 들어온다. 같은 학교(샘플고등학교)의 사용 기록만 보인다.
### 구성 요소
- nav-pill: "Lab_Stock" 워드마크 + 제목 "사용 기록 내역" + 현재 학교명 "샘플고등학교" 텍스트. 하늘색: 데스크탑 현재 섹션 링크("사용 기록 내역") 아래 #2b9fe0 밑줄 인디케이터
- segmented-control: 목록 위 필터 "전체 / 내 기록", 한 번에 하나만 선택. 선택된 옵션은 segmented-control-active
- segmented-control-active: 선택된 필터 흰 pill. 하늘색: 1px #2b9fe0 테두리(글자는 #141414)
- text-input: 필터 옆 기간 드롭다운("최근 1개월" 기본값)과 시약명 검색 바("시약명 검색"). 하늘색: 검색 아이콘·드롭다운 펼침 아이콘 #2b9fe0
- ex-data-table-cell: 기록 목록. 날짜(월) 그룹 헤더(caption) 아래 행마다 3열 = 날짜(좌, caption) · 시약명(title) / 사용자(body-sm)(중) · 사용량·단위(우, body). 행을 누르면 ex-modal-card 상세가 열린다. 하늘색: 누른 행 배경 #e6f4fc, 그룹 헤더 왼쪽 #2b9fe0 짧은 인디케이터
- ex-modal-card: 기록 상세. 상단 시약명(heading-3) + 사용량(display) 요약 → 라벨-값 행(사용자 · 일시 · 메모) → 그 아래 msds-entry → button-outline "닫기". 하늘색 없음
- msds-entry: 상세 모달 안 button-pill-soft "MSDS 보기 ↗". 학생·교사·admin 모두. 하늘색: 바깥 화살표 아이콘 #2b9fe0(라벨 글자는 #141414)
- button-outline: 상세 모달 "닫기"
- ex-empty-state-card: 필터 결과 0건일 때 "아직 사용 기록이 없어요" 문구. 하늘색: 안내 아이콘 #2b9fe0
### 반영한 레퍼런스
- https://uibowl.io/name/%ED%86%A0%EC%8A%A4%EC%A6%9D%EA%B6%8C?patterns=%EB%82%B4%EC%97%AD&patternName=%EA%B1%B0%EB%9E%98%EB%82%B4%EC%97%AD
- https://uibowl.io/name/%EB%AF%B8%EB%8B%88%EC%8A%A4%ED%83%81?patterns=%EB%82%B4%EC%97%AD&patternName=%EC%9B%90%ED%99%94%20%EA%B1%B0%EB%9E%98%EB%82%B4%EC%97%AD
- https://uibowl.io/name/%ED%86%A0%EC%8A%A4?patterns=%EB%82%B4%EC%97%AD&patternName=%EA%B1%B0%EB%9E%98%20%EC%83%81%EC%84%B8

## 화면 9
이 화면은 admin만 들어온다. 화면 6의 vendor-register 버튼과 nav-pill 섹션 링크로 들어온다. 학생·교사 nav에는 진입 링크가 없다(학생·교사 노출 0).
### 구성 요소
- nav-pill: "Lab_Stock" 워드마크 + 제목 "판매처 설정" + 현재 학교명 "샘플고등학교" 텍스트. 하늘색: 데스크탑 현재 섹션 링크("판매처 설정") 아래 #2b9fe0 밑줄 인디케이터 (admin만)
- segmented-control: 상단 "우리 학교 판매처 / 공통 목록" 두 탭, 활성 탭은 하나. 선택된 탭은 segmented-control-active (admin만)
- segmented-control-active: 활성 탭 흰 pill. 하늘색: 활성 탭 아래 #2b9fe0 인디케이터(글자는 #141414) (admin만)
- text-input: 탭 아래 판매처명 검색 바("판매처 검색"), 등록·수정 폼 입력("판매처명"(필수), "연락처", "웹사이트 주소"). 하늘색: 검색 아이콘 #2b9fe0 (admin만)
- vendor-register: "우리 학교 판매처" 탭 블록 1개. 학교 판매처 목록(행마다 판매처명·부가 정보 + 오른쪽 더보기 메뉴 "수정"·"삭제") + 하단 고정 button-primary "판매처 등록" → 세로 등록·수정 폼 → 저장 후 목록 복귀. 하늘색: 더보기 아이콘 #2b9fe0, 방금 등록·수정한 행 배경 #e6f4fc (admin만)
- ex-data-table-cell: "공통 목록" 탭의 서비스 공통 판매처 목록, 보기 전용 2열(판매처명 · 부가 정보). 수정·삭제 버튼 없음. 하늘색 없음 (admin만)
- ex-modal-card: 삭제 확인 "이 판매처를 삭제할까요?" + button-outline "취소" + button-primary "삭제". 하늘색 없음 (admin만)
- button-primary: 하단 고정 "판매처 등록", 폼 하단 전폭 "저장"(판매처명이 비면 비활성), 모달 "삭제". 하늘색 없음 (admin만)
- button-outline: 삭제 모달 "취소" (admin만)
- ex-empty-state-card: 학교 판매처가 0건일 때 가운데 아이콘 + "등록한 판매처가 없어요" 안내문 + 아래 등록 진입(하단 고정 "판매처 등록"과 같은 동작). 하늘색: 안내 아이콘 #2b9fe0 (admin만)
- ex-toast: 저장·삭제 직후 "판매처를 저장했어요" / "판매처를 삭제했어요" 알림. 하늘색: 완료 체크 아이콘 #2b9fe0 (admin만)
### 반영한 레퍼런스
- https://uibowl.io/name/%ED%8E%98%EC%9D%B4%EC%9B%8C%ED%81%AC?patterns=%EB%A9%94%EB%89%B4&patternName=%EA%B0%84%ED%8E%B8%EB%A9%94%EB%89%B4%20-%20%EA%B1%B0%EB%9E%98%EC%B2%98
- https://uibowl.io/name/%ED%8E%98%EC%9D%B4%EC%9B%8C%ED%81%AC?patterns=%ED%8E%B8%EC%A7%91%C2%B7%EC%88%98%EC%A0%95%ED%95%98%EA%B8%B0&patternName=%EA%B1%B0%EB%9E%98%EC%B2%98%EC%88%98%EC%A0%95
- https://uibowl.io/name/%ED%8E%98%EC%9D%B4%EC%9B%8C%ED%81%AC?patterns=%ED%8E%B8%EC%A7%91%C2%B7%EC%88%98%EC%A0%95%ED%95%98%EA%B8%B0&patternName=%EA%B1%B0%EB%9E%98%EC%B2%98%EC%B6%94%EA%B0%80

## 화면 1
### 구성 요소
- nav-pill: "Lab_Stock" 워드마크만 표시. 로그인 전이라 섹션 링크와 학교명은 없다. 하늘색 없음
- ex-auth-form-card: 로그인 카드. 제목 "로그인"(heading-3) + 보조 문구 "우리 학교를 선택하고 로그인하세요"(body-lg). 아래 학교 선택 3개 필드를 한 묶음 안에 세로로 쌓는다. 하늘색: 묶음 위 3단계 진행 막대(시/도 → 지역 → 학교 중 채운 단계만 #2b9fe0, 나머지 #e0e0e0)
- school-select-sido: 첫 번째 필드 "시/도". 탭하면 별도 선택 목록(neis.json sido_list)이 열리고, 고른 값이 필드에 돌아와 표시된다. 기본값 "충청북도". 하늘색: 선택 목록의 현재 선택 행 배경 #e6f4fc + 오른쪽 체크 아이콘 #2b9fe0
- school-select-region: 두 번째 필드 "지역(시/군/구)". 시/도를 고르기 전에는 비활성. 목록은 고른 시/도의 지역(neis.json region_list), 기본값 "청주시". 하늘색: 선택 목록의 현재 선택 행 배경 #e6f4fc + 체크 아이콘 #2b9fe0
- school-select-school: 세 번째 필드 "학교". 지역을 고르기 전에는 비활성. 목록은 고른 지역의 고등학교(neis.json school_list), 플레이스홀더 "학교 선택". 하늘색: 선택 목록의 현재 선택 행 배경 #e6f4fc + 체크 아이콘 #2b9fe0
- text-input: 학교 선택 묶음 아래 로그인 정보 입력 2개("아이디", "비밀번호"). 하늘색 없음(포커스 링은 #141414)
- button-primary: 카드 하단 전폭 "로그인". 학교를 고르기 전에는 비활성. 하늘색 없음
### 반영한 레퍼런스
- https://uibowl.io/name/%EC%8A%A4%ED%8A%9C%EB%94%94%EC%98%A4%EB%A9%94%EC%9D%B4%ED%8A%B8?patterns=%ED%95%84%ED%84%B0&patternName=%EC%A7%80%EC%97%AD%20%EC%84%A0%ED%83%9D
- https://uibowl.io/name/redBus?patterns=%EC%A1%B0%ED%9A%8C%ED%95%98%EA%B8%B0&patternName=%EC%A7%80%EC%97%AD%26%EB%82%A0%EC%A7%9C%20%EC%84%A0%ED%83%9D
- https://uibowl.io/name/MakeMyTrip?patterns=%EC%98%88%EC%95%BD%C2%B7%EA%B2%B0%EC%A0%9C&patternName=1.%EB%82%A0%EC%A7%9C%20%EB%B0%8F%20%EC%A7%80%EC%97%AD%20%EC%84%A0%ED%83%9D

## 화면 4
### 구성 요소
- nav-pill: 뒤로가기(화면 3) + 제목 "사용 기록" + 현재 학교명 "샘플고등학교" 텍스트. 데스크탑 섹션 링크는 화면 2와 같다("시약 목록", 교사·admin에게만 "재주문 알림"). 하늘색: 뒤로가기 아이콘 #2b9fe0, 데스크탑 "시약 목록" 아래 #2b9fe0 밑줄 인디케이터
- reagent-detail-card: 폼 상단 고정 요약. 시약명(title) + 현재 재고량·단위(body). 무엇을 기록하는지 보여준다. 재고 부족 배지는 두지 않는다. 하늘색 없음(중립 유지)
- text-input: 라벨 위·입력 아래 세로 폼. 순서대로 "사용 날짜"(필수), "사용량"(필수) + 단위, "사용자"(필수, 로그인한 사용자 이름이 기본값), "메모". 필수 라벨 옆에 caption "필수". 하늘색: "사용 날짜" 달력 아이콘 #2b9fe0, 단위 칩의 선택 상태 배경 #e6f4fc + 1px #2b9fe0 테두리(글자는 #141414)
- button-primary: 하단 전폭 "사용 기록 저장". 필수 항목이 비면 비활성. 학생·교사·admin 모두. 하늘색 없음
- ex-toast: 저장 직후 "사용 기록을 저장했어요" 알림, 이후 화면 3 "사용 기록" 탭으로 돌아간다. 하늘색: 완료 체크 아이콘 #2b9fe0
### 반영한 레퍼런스
- https://uibowl.io/name/%EC%98%A4%ED%81%B4%EA%B3%A0?patterns=%EA%B8%80%EC%93%B0%EA%B8%B0&patternName=%EA%B8%B0%EB%A1%9D%ED%95%98%EA%B8%B0
- https://uibowl.io/name/%EC%98%A4%EB%8A%98%EC%9D%98%20%EB%A3%A8%ED%8B%B4?patterns=%EA%B8%80%EC%93%B0%EA%B8%B0&patternName=%EB%A3%A8%ED%8B%B4%20%EA%B8%B0%EB%A1%9D%ED%95%98%EA%B8%B0
- https://uibowl.io/name/%EB%A0%88%ED%8F%AC%EB%B8%8C?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&patternName=%EA%B8%B0%EB%A1%9D%ED%95%98%EA%B8%B0

## 화면 5
이 화면은 교사·admin만 들어온다. 학생 화면에는 진입 링크와 업로드 버튼이 없다(학생 노출 0).
### 구성 요소
- nav-pill: 뒤로가기(화면 6) + 제목 "실험 매뉴얼" + 현재 학교명 "샘플고등학교" 텍스트. 하늘색: 뒤로가기 아이콘 #2b9fe0 (교사·admin만)
- manual-upload: 1단계 업로드. 상단 안내 문구 "실험 매뉴얼을 올리면 시약별 사용량을 찾아드려요"(body-lg) + 중앙 업로드/미리보기 타일(rounded 16, 비율 유지) + 미리보기 위 badge-overlay 파일 이름 태그. 하늘색: 업로드 타일 가운데 업로드 아이콘 #2b9fe0, 처리 중 진행 막대 #2b9fe0(트랙 #e6f4fc) (교사·admin만)
- badge-overlay: manual-upload 미리보기 위 파일 이름 태그. 하늘색 없음 (교사·admin만)
- text-input: 업로드 타일 아래 "조 수" 숫자 입력 1개. 하늘색 없음 (교사·admin만)
- button-primary: 1단계 하단 고정 "AI 추출". 파일과 조 수가 비면 비활성, 누르면 처리 중 상태 문구 "사용량을 찾고 있어요"를 거쳐 2단계로 간다. 하늘색 없음 (교사·admin만)
- extraction-table: 2단계 추출 결과 확인. 상단 제목 "추출 결과 확인" + 닫기, 본문 스크롤 표. ex-data-table-cell 4열 = 시약명 · 1조 사용량 · 단위 · 1반 1회 필요량(1조 사용량 × 조 수). 사용량 칸은 text-input으로 고칠 수 있다. 하늘색: 사용자가 고친 칸 배경 #e6f4fc (교사·admin만)
- ex-data-table-cell: extraction-table 안 머리행·본문 셀 (교사·admin만)
- button-outline: 2단계 하단 "다시 추출" (교사·admin만)
- button-primary: 2단계 하단 전폭 "확인 후 저장". 사용자가 확인한 뒤에만 저장된다. 하늘색 없음 (교사·admin만)
- ex-toast: 저장 직후 "재주문 기준을 저장했어요" 알림, 이후 화면 6으로 돌아간다. 하늘색: 완료 체크 아이콘 #2b9fe0 (교사·admin만)
### 반영한 레퍼런스
- https://uibowl.io/name/%EB%8B%A4%EA%B8%80%EB%A1%9C?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&patternName=%EC%9C%A0%ED%8A%9C%EB%B8%8C%20%EB%A7%81%ED%81%AC%20%EC%97%85%EB%A1%9C%EB%93%9C
- https://uibowl.io/name/%EC%88%98%ED%98%84%EC%9D%B4%EB%9E%91?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&patternName=%EA%B3%B5%EC%9C%A0%20%EC%95%A8%EB%B2%94%20%EC%97%85%EB%A1%9C%EB%93%9C
- https://uibowl.io/name/%ED%82%A4%ED%94%BC%EB%9F%BD?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&patternName=%EC%9D%B8%EC%A6%9D%EC%83%B7-%EC%97%85%EB%A1%9C%EB%93%9C

## 역할별 노출
앱 전체(화면 1~10, runs/20261001-1910·runs/20261002-0838 설계 포함) 기준 개수.
manual-upload = 화면 6 진입 버튼 1 + 화면 5 업로드 영역 1. vendor-register = 화면 6 버튼 1 + 화면 9 블록 1 (admin만). msds-entry = 화면 3 1 + 화면 10 상세 1. stock-intake·reagent-register = 화면 7 (교사·admin). user-manage = 화면 8 (admin만).

| 컴포넌트 | 학생 | 교사 | admin |
|---|---|---|---|
| manual-upload | 0 | 2 | 2 |
| reorder-alert-card | 0 | 1 | 1 |
| vendor-link | 0 | 1 | 1 |
| vendor-register | 0 | 0 | 2 |
| msds-entry | 2 | 2 | 2 |
| stock-intake | 0 | 1 | 1 |
| reagent-register | 0 | 1 | 1 |
| user-manage | 0 | 0 | 1 |
