# S2 설계 — run 20261007-0848

대상 화면: 5 (실험 매뉴얼 → 추출 결과 확인), 6 (재주문 알림), 8 (사용자 관리), 9 (판매처 설정) · 상태 화면 없음 · 학교: 샘플고등학교 (input.json)
변경 사유: 개발 앱에 이미 들어간 동작(앱 예외)을 시안에 반영한다. 근거: docs/story-service.md 결정 사항 "앱 예외 반영 (2026-10-06, 개발 세션)"·"자동 재주문 기준 표시 (화면 3·6, 2026-10-07)" 행, harness/rules.json app_exceptions(nav-account-menu·extraction-link-row·extraction-merge·sheet-close·vendor-new-window)·reorder.auto, docs/design.md(extraction-table, reorder-alert-card, auto-threshold-badge, ex-modal-card, nav-account-menu, tab-bar), research/s1-adopt.md.
기준 설계(수정하지 않음): runs/20261002-1441/spec/s2-spec.md 화면 5·6·8·9(tab-bar 버전) + 공통 nav-account-menu(runs/20261006-1223). 기존 구성 요소 이름과 구성을 유지하고, 위 예외로 정해진 부분만 더하거나 바꾼다.
색·폰트·모서리·간격은 docs/design.md와 harness/rules.json을 따른다. 허용 색 밖의 값(딤 반투명 검정 등)은 쓰지 않는다. 반투명 회색은 badge-overlay 안에서만 쓴다. 그림자는 쓰지 않는다(segmented-control-active 예외).
- 핑크 #d6246a·연핑크 #fbe9f0는 badge-low-stock·reorder-alert-card 안에서만 쓴다. 사용자 삭제·판매처 삭제·추출 표 삭제·입력 오류 안내에는 핑크를 쓰지 않고 #141414 아이콘 + #141414/#707070 문구로만 표시한다.
- 하늘색 #2b9fe0(선·인디케이터·아이콘·진행 막대)과 옅은 하늘색 #e6f4fc(선택 배경·안내 박스)는 선택 상태·활성 탭·링크 밑줄·진행·아이콘 강조에만 쓴다. 글자색으로 쓰지 않고(그 위 글자는 #141414), badge-low-stock·reorder-alert-card·button-primary 안에는 쓰지 않는다.
- auto-threshold-badge "자동"은 #f3f3f3 회색 pill + #141414 글자. 핑크·하늘색 없음(정보이지 결정 신호가 아니다).
학교 선택은 회원가입(화면 14)에만 있다. 이번 대상 화면에는 학교 선택을 두지 않고 nav-pill 안에 현재 학교명 "샘플고등학교"를 표시한다. 학교 전환 기능은 두지 않는다. 추출 표의 "우리 학교 시약" 목록, 재주문 알림, 사용자 목록, 학교 판매처 목록은 모두 샘플고등학교 것만 보인다(N1).
외부 서비스 연결 값은 서버에서만 다룬다. 어떤 화면에도 연결 값 입력 칸·외부 서비스 설정·AI 엔진 선택 UI·관련 문구를 두지 않는다(N2). 화면 5의 입력 라벨은 "조 수"·"1조 사용량"·"단위"·"우리 학교 시약"뿐이다.
괄호 안 역할 표시가 없는 구성 요소는 그 화면에 들어오는 모든 역할에게 보인다. 화면 5·6 = 교사·admin만, 화면 8·9 = admin만 들어온다.
모바일 공통: tab-bar는 화면 아래 가장자리 y 780~844(폭 390, 높이 64, rounded 0, #ffffff + 위쪽 1px #f0f0f0 선, 그림자 없음)에 붙고 tab-item 4개("홈"·"시약"·"QR 스캔"·"기록")를 같은 폭으로 채운다. 본문 스크롤은 y 780에서 끝난다. 하단 고정 버튼은 tab-bar 바로 위(간격 16). 시트는 tab-bar 위쪽 선 위에 붙는다(딤 없음, 1px #e0e0e0 테두리로 구분, 위쪽 rounded 24, 오른쪽 위 × 닫기). 데스크탑에는 tab-bar 없이 nav-pill 섹션 링크를 유지하고, 시트는 가운데 ex-modal-card(rounded 24, × 닫기)로 연다.
nav-account-menu(공통): 모든 대상 화면 nav-pill 학교명 "샘플고등학교" 옆 작은 ▾. 누르면 #ffffff 작은 메뉴(rounded 24, 1px #f0f0f0 테두리)에 항목 "로그아웃" 1개. 프레임에는 닫힌 상태(▾만)로 그린다.
예시 데이터(공통): 오늘 = 2026-10-07. 샘플고등학교 재고 부족 3종(염산 · 1병, 에탄올 · 200 mL, 질산은 · 5 g).

## 화면 5
실험 매뉴얼 → AI 추출 결과 확인. 교사·admin만 들어온다(화면 6 "실험 매뉴얼 올리기"). 학생 화면에는 진입 링크와 업로드 버튼이 없다(학생 노출 0).
흐름: 1단계 업로드(파일 + 조 수) → "AI 추출" → 2단계 추출 결과 확인 → "확인 후 저장". 조 수 입력은 처음에 빈 값이고, 파일과 조 수가 모두 있어야 "AI 추출"이 켜진다.
예시 상태(프레임 5-mobile · 5-desktop): 2단계. 위쪽에 올린 파일이 접힌 manual-upload 타일("산·염기 중화 실험.pdf", 조 수 4)로 남고, 그 아래 extraction-table이 펼쳐진 상태. 추출 행 4개 —
① 염산 · 1조 20 · mL → 1반 1회 80 mL / 아래 줄: 우리 학교 시약 "염산" · 삭제 · "기존 기준 100 · 바뀌어요"
② 수산화나트륨 · 1조 5 · g → 20 g / 아래 줄: "수산화나트륨" · 삭제 · "기존 기준 20 · 그대로 둬요"
③ 페놀프탈레인 용액 · 1조 2 · mL → 8 mL / 아래 줄: "페놀프탈레인 용액" · 삭제 · "기존 기준 없음 · 새로 정해요"
④ 증류수 · 1조 150 · mL → 600 mL / 아래 줄: "증류수" · 삭제 · "기존 기준 500 · 바뀌어요" + 그 아래 무채색 안내 줄 "2개 행을 합쳤어요"
모바일 활성 탭: "기록". 위→아래: nav-pill → 접힌 manual-upload(파일 타일 + 조 수) → extraction-table(제목·안내 → 행 카드 목록) → 하단 버튼 줄("다시 추출" + "확인 후 저장") → tab-bar. 좌우 여백 16, 행 사이 12. 모바일에서 추출 행은 행마다 #f3f3f3 카드(rounded 16)로 쌓는다.
데스크탑: nav-pill 아래 가운데 단일 열 같은 순서, 추출 표는 열 표(시약명 · 1조 사용량 · 단위 · 1반 1회 필요량) + 행마다 아래 줄. tab-bar 없음.
### 구성 요소
- nav-pill: 뒤로가기(화면 6) + 제목 "실험 매뉴얼" + 현재 학교명 "샘플고등학교" + 학교명 옆 nav-account-menu ▾. 데스크탑 섹션 링크("시약 목록", "재주문 알림"). 하늘색: 뒤로가기 아이콘 #2b9fe0, 데스크탑 "재주문 알림" 밑줄 #2b9fe0(글자 #141414) (교사·admin만)
- nav-account-menu: 학교명 옆 ▾, 메뉴 항목 "로그아웃" 1개. 하늘색 없음 (교사·admin만)
- manual-upload: 1단계 업로드 영역. 처음 상태 = 안내 문구 body-lg "실험 매뉴얼을 올리면 시약별 사용량을 찾아드려요" + 업로드/미리보기 타일(rounded 16, 비율 유지) + 그 아래 "조 수" text-input(빈 값, 플레이스홀더 "예: 4") + 하단 고정 button-primary "AI 추출"(파일·조 수가 비면 비활성). 추출 중 = 타일 안 진행 막대 + "사용량을 찾고 있어요". 2단계(예시 상태) = 영역이 한 줄 높이로 접혀 파일 타일(작은 미리보기 + badge-overlay 파일 이름) 오른쪽에 "조 수 4"(text-input, 고칠 수 있음, 고치면 필요량 열이 다시 계산됨). 하늘색: 업로드 아이콘 #2b9fe0, 진행 막대 #2b9fe0(트랙 #e6f4fc) (교사·admin만)
- badge-overlay: 미리보기 위 파일 이름 태그 "산·염기 중화 실험.pdf"(rgba(115,115,115,0.56), #ffffff label, rounded 9999). 하늘색 없음 (교사·admin만)
- text-input: "조 수"(숫자, 기본 빈 값), 추출 행의 "1조 사용량"(숫자, 고칠 수 있음), 단위 선택 상자, "우리 학교 시약" 선택 상자. 모두 #f0f0f0 채움, 테두리 없음, rounded 16, 포커스 링 2px #141414. 단위 선택 상자 = 사용량 칸 오른쪽에 같은 높이로 붙은 좁은 칸(값 "mL" ▾, 목록 병 · mL · g). 하늘색: 선택 상자 ▾ 아이콘 #2b9fe0 (교사·admin만)
- extraction-table: 2단계 추출 결과 확인. 맨 위 heading-3 "추출 결과 확인" + body-sm(#707070) "확인한 뒤 저장해야 반영돼요". 행 = 1줄: 시약명(title) · 1조 사용량 text-input + 단위 선택 상자 · 1반 1회 필요량(body, 1조 사용량 × 조 수, 자동 계산) / 2줄(행 바로 아래 붙은 보조 줄, 위 간격 8): "우리 학교 시약" 선택 상자(값 = 연결된 샘플고등학교 시약 이름 ▾, 목록은 샘플고등학교 시약만) → 조용한 텍스트 동작 "삭제"(link #141414, 채움·테두리 없음, 누름 영역 44 이상, 누르면 그 행이 표에서 빠짐, 확인 없음) → 줄 끝 body-sm(#707070) "기존 기준 {N} · 그대로 둬요 / 바뀌어요"(새 필요량이 기존 재주문 기준과 같으면 "그대로 둬요", 다르면 "바뀌어요", 기존 기준이 없으면 "기존 기준 없음 · 새로 정해요"). 같은 시약이 여러 번 나오면 한 행으로 합치고(사용량 합산) 그 행 2줄 아래에 무채색 안내 줄 caption(#707070) "2개 행을 합쳤어요"(채움·테두리 없음, 왼쪽 작은 #707070 아이콘). 모바일 = 행마다 #f3f3f3 카드(rounded 16, 여백 16), 데스크탑 = rounded 16 표 컨테이너 안 ex-data-table-cell 행. 하늘색: 사용자가 고친 사용량 칸 배경 #e6f4fc (교사·admin만)
- ex-data-table-cell: 데스크탑 extraction-table 머리행(caption #707070 "시약명 · 1조 사용량 · 단위 · 1반 1회 필요량")과 본문 셀(body-sm). 행 구분은 여백 12 (교사·admin만)
- button-outline: 2단계 하단 "다시 추출"(#ffffff, 1px #e0e0e0, 라벨 #141414, rounded 9999, 높이 44 이상) — 누르면 같은 파일·조 수로 다시 읽는다. 모바일에서는 tab-bar 바로 위 버튼 줄 왼쪽(좁게, 비율 1:2) (교사·admin만)
- button-primary: 1단계 "AI 추출", 2단계 "확인 후 저장"(#141414 채움, #ffffff 글자, rounded 9999, 높이 44 이상). "확인 후 저장"은 버튼 줄 오른쪽(넓게). 저장하면 각 행의 필요량이 연결된 시약의 재주문 기준(화면 3 reorder-threshold와 같은 칸)에 들어간다. 연결된 시약이 없는 행이 있으면 비활성. 하늘색 없음 (교사·admin만)
- ex-toast: 저장 직후 "재주문 기준을 저장했어요", 이후 화면 6으로. 모바일은 tab-bar 위. 하늘색: 완료 체크 아이콘 #2b9fe0 (교사·admin만)
- tab-bar: 모바일 전용 하단 탭바 1개(공통 규격). 하단 버튼 줄은 이 바 위에 쌓는다. 데스크탑에는 두지 않는다. 하늘색: 활성 tab-item 아이콘 #2b9fe0만 (교사·admin만 — 화면 자체가 교사·admin 전용)
- tab-item: "홈" · "시약" · "QR 스캔" · "기록" 4개, 사각형 누름 영역(rounded 0), 높이 48, 아이콘 위 + label 아래. 활성 = "기록"(#2b9fe0 아이콘 + 라벨 #141414), 비활성 3개 #707070 (교사·admin만)
### 반영한 레퍼런스
- https://uibowl.io/name/%ED%8E%98%EC%9D%B4%ED%9E%88%EC%96%B4?patterns=%EC%B4%AC%EC%98%81%ED%95%98%EA%B8%B0&imgId=cmnfmykft001zl204e2svm4y5
- https://uibowl.io/name/%ED%95%98%EB%82%98%EC%B9%B4%EB%93%9C?patterns=%EC%95%8C%EB%A6%BC&imgId=cmh1hz3nr000rib04np2myjwf
- https://uibowl.io/name/%EA%B3%A8%ED%94%84%EC%A1%B4?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&imgId=cmunkfw4m0069jq041c3fhn4u
- https://uibowl.io/name/%EB%83%89%EC%9E%A5%EA%B3%A0%ED%84%B8%EA%B8%B0?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&imgId=cmohwpx3w00fyjm047ryhdpgb

## 화면 6
재주문 알림. 교사·admin만 들어온다. 학생 nav에는 진입 링크가 없다(학생 노출 0).
예시 상태(프레임 6-mobile · 6-desktop): 알림 3건.
① 염산 — 재주문 기준 100 mL(매뉴얼 추출 값, 배지 없음) / 현재 1병(50 mL 남음). 판매처 "확인" 뒤 상태: 카드 안 vendor-link 아래 새 창 안내 줄이 보인다.
② 에탄올 — 재주문 기준 800 mL + auto-threshold-badge "자동" + 캡션 "최근 사용량으로 계산했어요" / 현재 200 mL.
③ 질산은 — 재주문 기준 10 g(직접 입력 값, 배지 없음) / 현재 5 g.
모바일 활성 탭: "시약". 위→아래: nav-pill → 재주문 기준 안내 박스(manual-upload 진입) → reorder-alert-card 목록 → (admin) "판매처 등록" → tab-bar. 좌우 여백 16, 카드 사이 12.
데스크탑: nav-pill 아래 가운데 단일 열 같은 순서, tab-bar 없음.
### 구성 요소
- nav-pill: "Lab_Stock" 워드마크 + 제목 "재주문 알림" + 현재 학교명 "샘플고등학교" + 학교명 옆 nav-account-menu ▾. 학교 전환 기능 없음. 하늘색: 데스크탑 현재 섹션 링크("재주문 알림") 밑줄 #2b9fe0(글자 #141414) (교사·admin만)
- nav-account-menu: 학교명 옆 ▾, 메뉴 항목 "로그아웃" 1개. 하늘색 없음 (교사·admin만)
- manual-upload: 알림 목록 위 재주문 기준 안내 박스(#e6f4fc 채움, rounded 16, 글자 #141414, "필요량 = 1반 1회 실험량 × 조 수 · 기준이 없는 시약은 최근 사용량으로 계산해요") 끝의 button-pill-soft "실험 매뉴얼 올리기" → 화면 5. 하늘색: 박스 채움 #e6f4fc, 정보 아이콘 #2b9fe0 (교사·admin만)
- reorder-alert-card: 알림 1건 카드(#f3f3f3 채움, 테두리 없음, rounded 24, 여백 24). 왼쪽 위 badge-low-stock "재고 부족" → 시약명(heading-4) → "재주문 기준 {N} / 현재 재고 {M}"(body) — 기준이 자동 값이면 기준 숫자 바로 오른쪽에 auto-threshold-badge "자동"을 인라인으로 붙이고 그 줄 아래 caption(#707070) "최근 사용량으로 계산했어요" 한 줄 → 알림 날짜(caption #707070) → 카드 하단 오른쪽 vendor-link. 판매처 "확인" 뒤에는 vendor-link 바로 아래(간격 8) 무채색 안내 줄: #707070 바깥 링크 아이콘 + body-sm(#707070) "사이트를 새 창으로 열었어요. 열리지 않았다면" + button-pill-soft "직접 열기"(높이 44 이상). 카드 안에는 하늘색을 쓰지 않는다 (교사·admin만)
- badge-low-stock: reorder-alert-card 안 "재고 부족"(#d6246a 채움, #ffffff label, rounded 9999). 하늘색 없음 (교사·admin만)
- auto-threshold-badge: 자동 기준 카드(에탄올)의 기준 숫자 오른쪽 pill "자동"(#f3f3f3 채움 + 카드 바탕과 구분되도록 1px #e0e0e0 테두리, label #141414, rounded 9999). 매뉴얼 추출·직접 입력 기준에는 붙이지 않는다. 핑크·하늘색 없음 (교사·admin만)
- vendor-link: reorder-alert-card 하단 오른쪽 button-primary "판매처 연결"(#141414 채움, #ffffff 글자, rounded 9999, 높이 44 이상). 누르면 ex-modal-card 판매처 확인. 하늘색 없음 (교사·admin만)
- ex-modal-card: vendor-link를 누르면 뜨는 판매처 확인 시트(모바일 tab-bar 위, 데스크탑 가운데 카드, 1px #e0e0e0 테두리, 그림자·딤 없음). 제목 heading-3 "판매처 고르기" + 시약명 caption → 판매처 행 목록(행 = 판매처명 title + 웹사이트 주소 caption #707070, 샘플고등학교 판매처 먼저, 그다음 공통 목록) → button-outline "취소" + button-primary "확인". "확인"을 누르면 시트가 닫히고 판매처 사이트가 새 창으로 열리며 카드에 새 창 안내 줄이 나타난다. 하늘색: 선택된 판매처 행 배경 #e6f4fc + 왼쪽 #2b9fe0 선택 표시 (교사·admin만)
- button-pill-soft: 안내 박스 "실험 매뉴얼 올리기", 카드 안 새 창 안내 줄 "직접 열기"(카드 바탕 #f3f3f3 위라 1px #e0e0e0 테두리로 구분, 라벨 #141414, rounded 9999). 하늘색 없음 (교사·admin만)
- button-outline: 판매처 확인 시트 "취소", 목록 아래 "판매처 등록"(admin만, vendor-register) (교사·admin만)
- vendor-register: 알림 목록 아래 button-outline "판매처 등록" → 화면 9 (admin만, 교사 화면에는 없음)
- ex-empty-state-card: 알림이 0건일 때 "재고가 부족한 시약이 없어요". 하늘색: 안내 아이콘 #2b9fe0 (교사·admin만)
- tab-bar: 모바일 전용 하단 탭바 1개(공통 규격). 알림 목록 스크롤은 이 바 위쪽 선에서 끝난다. 데스크탑에는 두지 않는다. 하늘색: 활성 tab-item 아이콘 #2b9fe0만 (교사·admin만 — 화면 자체가 교사·admin 전용)
- tab-item: "홈" · "시약" · "QR 스캔" · "기록" 4개. 활성 = "시약"(#2b9fe0 아이콘 + 라벨 #141414), 비활성 3개 #707070 (교사·admin만)
### 반영한 레퍼런스
- https://uibowl.io/name/%ED%8F%B4%EC%84%BC%ED%8A%B8?patterns=%ED%98%9C%ED%83%9D&imgId=cmpuvbnmd002xla04lzx58y7e
- https://uibowl.io/name/%ED%8F%AC%EC%8A%A4%ED%85%94%EB%9F%AC?patterns=%EC%84%A0%EB%AC%BC%ED%95%98%EA%B8%B0&imgId=cmr9xc0k1000cl804lfr839ze
- https://uibowl.io/name/%EC%99%93%EC%84%AD?patterns=%EC%B7%A8%EC%86%8C%ED%95%98%EA%B8%B0&imgId=cmqt886wr00ckk004podt4d02
- https://uibowl.io/name/%ED%86%A0%EC%8A%A4?patterns=%EC%83%81%EC%84%B8%EC%A0%95%EB%B3%B4%20%28PDP%29&imgId=cmrtwe8la005jl204biikq9ad

## 화면 8
사용자 관리. admin만 들어온다(홈 quick-action "사용자 관리"). 학생·교사 nav에는 진입 링크가 없다(학생·교사 노출 0).
예시 상태(프레임 8-mobile · 8-desktop): 사용자 목록(멤버 5명 · 초대 대기 2건) 위에 학생 "박OO"의 삭제 확인 시트가 열린 상태(역할 변경 시트에서 "사용자 삭제"를 누른 뒤). 뒤 목록은 그대로 보인다.
모바일 활성 탭: "홈". 위→아래: nav-pill → user-manage(헤더 "샘플고등학교 사용자 5명" + "초대" → 이름 검색 → 멤버 → 초대 대기 → 유의사항) → tab-bar. 시트는 tab-bar 위쪽 선 위에 붙는다.
데스크탑: nav-pill 아래 가운데 단일 열, 시트는 가운데 ex-modal-card. tab-bar 없음.
### 구성 요소
- nav-pill: "Lab_Stock" 워드마크 + 제목 "사용자 관리" + 현재 학교명 "샘플고등학교" + 학교명 옆 nav-account-menu ▾. 하늘색: 데스크탑 현재 섹션 링크("사용자 관리") 밑줄 #2b9fe0(글자 #141414) (admin만)
- nav-account-menu: 학교명 옆 ▾, 메뉴 항목 "로그아웃" 1개. 하늘색 없음 (admin만)
- user-manage: 화면 본문 전체 블록 1개. 헤더 한 줄 heading-3 "샘플고등학교 사용자 5명" + 오른쪽 button-primary "초대" → text-input 이름 검색 → 섹션 "멤버"(heading-4): 행 = 이름(title) + 본인 행 "나" pill + 보조줄 역할 "학생"/"교사"/"admin"(body-sm #707070) + 오른쪽 ›(누르면 역할 변경 시트) → 섹션 "초대 대기 (2)"(heading-4): 행 = 이메일(body) + 초대일(caption #707070) + 상태 "대기"(label #141414) → 하단 유의사항 body-sm(#707070) "같은 학교(샘플고등학교) 계정만 초대할 수 있어요". 초대·역할 변경·삭제는 ex-modal-card 시트로 진행한다. 하늘색: 로그인한 admin 본인 행 배경 #e6f4fc (admin만)
- text-input: 목록 위 이름 검색(플레이스홀더 "이름 검색"), 초대 시트의 "이메일" 입력 1개(플레이스홀더 "name@example.com"). #f0f0f0, rounded 16, 포커스 링 2px #141414. 이메일 형식이 틀리면 입력 바로 아래 #141414 아이콘 + body-sm #141414 "이메일 주소를 확인해 주세요"(핑크 없음). 하늘색: 검색 아이콘 #2b9fe0 (admin만)
- ex-data-table-cell: "멤버"·"초대 대기" 행. "나" pill은 #f3f3f3 채움 + label #141414, 역할은 보조줄 텍스트로 흑백만. 행 구분은 여백 12. 하늘색: 오른쪽 › 아이콘 #2b9fe0 (admin만)
- ex-modal-card: 시트 3종. 모두 헤더 한 줄 = 제목 왼쪽 정렬 + 오른쪽 위 × 닫기(누름 영역 44 이상, #141414 아이콘), 1px #e0e0e0 테두리, 그림자·딤 없음, 모바일 위쪽 rounded 24·tab-bar 위, 데스크탑 rounded 24 가운데, 하단 버튼 고정. ① 초대 시트: 제목 "사용자 초대" + body-sm(#707070) "이메일로 초대 링크를 보내요" + button-pill-soft "초대 링크 복사" + "이메일" text-input 1개(이름 칸 없음) + 역할 segmented-control "학생 / 교사" + 하단 전폭 button-primary "초대 보내기"(이메일이 비거나 형식이 틀리면 비활성). ② 역할 변경 시트: 제목 "{이름}의 역할" + 라디오 3행 "학생 / 교사 / admin" + 하단 전폭 button-primary "변경" + 맨 아래 button-outline "사용자 삭제". 본인 행과 학교의 마지막 admin 행에서는 "사용자 삭제"를 숨기고, 마지막 admin은 다른 역할로 바꿀 수 없다(라디오 비활성 + caption #707070 "admin이 최소 1명 있어야 해요"). ③ 삭제 확인(예시 상태): 제목 heading-3 "이 사용자를 삭제할까요?" + 본문 body #141414 "박OO · 사용·입고 기록은 남아요" + 하단 버튼 줄 button-outline "취소" + button-primary "박OO 삭제"(비율 1:1, 사이 8). 핑크 없음. 하늘색: 초대 링크 아이콘 #2b9fe0, 역할 변경 라디오 선택 행 배경 #e6f4fc + 1px #2b9fe0 테두리 + 라디오 채움 #2b9fe0(글자 #141414) (admin만)
- segmented-control: 초대 시트 역할 선택 "학생 / 교사", 한 번에 하나 (admin만)
- segmented-control-active: 선택된 역할 흰 pill. 하늘색: 1px #2b9fe0 테두리(글자 #141414) (admin만)
- button-pill-soft: 초대 시트 "초대 링크 복사"(#f3f3f3, 라벨 #141414, rounded 9999) (admin만)
- button-primary: 헤더 "초대", 시트 "초대 보내기"·"변경", 삭제 확인 "박OO 삭제"(#141414 채움, #ffffff 글자, rounded 9999, 높이 44 이상). 하늘색 없음 (admin만)
- button-outline: 역할 변경 시트 "사용자 삭제", 삭제 확인 "취소"(#ffffff, 1px #e0e0e0, 라벨 #141414, rounded 9999, 높이 44 이상) (admin만)
- ex-empty-state-card: 검색 결과 0건이면 검색 바를 유지하고 "찾는 사용자가 없어요", 다른 사용자가 0명이면 "아직 초대한 사용자가 없어요" + 하단 유의사항 유지. 하늘색: 안내 아이콘 #2b9fe0 (admin만)
- ex-toast: "초대를 보냈어요" / "역할을 바꿨어요" / "사용자를 삭제했어요", 이후 사용자 목록으로. 모바일은 tab-bar 위. 하늘색: 완료 체크 아이콘 #2b9fe0 (admin만)
- tab-bar: 모바일 전용 하단 탭바 1개(공통 규격). 시트는 이 바 위쪽 선 위에 붙는다. 데스크탑에는 두지 않는다. 하늘색: 활성 tab-item 아이콘 #2b9fe0만 (admin만 — 화면 자체가 admin 전용)
- tab-item: "홈" · "시약" · "QR 스캔" · "기록" 4개. 활성 = "홈"(#2b9fe0 아이콘 + 라벨 #141414), 비활성 3개 #707070 (admin만)
### 반영한 레퍼런스
- https://uibowl.io/name/%EC%99%93%EC%84%AD?patterns=%EC%B7%A8%EC%86%8C%ED%95%98%EA%B8%B0&imgId=cmqt89aob001pjl044nphhj04
- https://uibowl.io/name/%EC%91%A5%EC%91%A5%EC%B0%B0%EC%B9%B5?patterns=%EC%84%A4%EC%A0%95&imgId=cmub7kz5f0097lb0415vsfhhk
- https://uibowl.io/name/%EC%9A%B0%EB%A6%AC%EB%8F%99%EB%84%A4GS?patterns=%EB%A7%88%EC%9D%B4%ED%8E%98%EC%9D%B4%EC%A7%80&imgId=cmlesg83100fll3044egry232
- https://uibowl.io/name/%EC%B9%B4%EC%B9%B4%EC%98%A4%EA%B3%A8%ED%94%84%EC%98%88%EC%95%BD?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&imgId=cmtwlux30003ll10402s3yw0o

## 화면 9
판매처 설정. admin만 들어온다(화면 6 "판매처 등록", nav-pill 섹션 링크). 학생·교사 nav에는 진입 링크가 없다(학생·교사 노출 0).
예시 상태(프레임 9-mobile · 9-desktop): "우리 학교 판매처" 탭, 판매처 3곳 목록 위에 "판매처 등록" 폼 시트가 열린 상태(판매처명 "과학나라" 입력 중, 연락처·웹사이트 주소 빈 값). 뒤 목록은 그대로 보인다.
모바일 활성 탭: "시약". 위→아래: nav-pill → segmented-control "우리 학교 판매처 / 공통 목록" → 검색 → 판매처 목록 → 하단 고정 "판매처 등록" → tab-bar. 폼 시트는 tab-bar 위쪽 선 위에 붙는다.
데스크탑: nav-pill 아래 가운데 단일 열, 폼은 가운데 ex-modal-card. tab-bar 없음.
### 구성 요소
- nav-pill: "Lab_Stock" 워드마크 + 제목 "판매처 설정" + 현재 학교명 "샘플고등학교" + 학교명 옆 nav-account-menu ▾. 하늘색: 데스크탑 현재 섹션 링크("판매처 설정") 밑줄 #2b9fe0(글자 #141414) (admin만)
- nav-account-menu: 학교명 옆 ▾, 메뉴 항목 "로그아웃" 1개. 하늘색 없음 (admin만)
- segmented-control: 상단 "우리 학교 판매처 / 공통 목록", 활성 탭 하나 (admin만)
- segmented-control-active: 활성 탭 흰 pill("우리 학교 판매처"). 하늘색: 1px #2b9fe0 테두리(글자 #141414) (admin만)
- text-input: 탭 아래 판매처 검색("판매처 검색"), 폼 시트 입력 3개 — "판매처명"(필수, caption "필수" #707070), "연락처", "웹사이트 주소". 부가 정보 칸은 두지 않는다. #f0f0f0, rounded 16, 포커스 링 2px #141414. 하늘색: 검색 아이콘 #2b9fe0 (admin만)
- vendor-register: "우리 학교 판매처" 탭 블록 1개. 샘플고등학교 판매처 목록(행 = 판매처명 title + 웹사이트 주소 caption #707070 + 오른쪽 더보기 메뉴 "수정"·"삭제") + 하단 고정 button-primary "판매처 등록" → ex-modal-card 등록·수정 폼 시트 → 저장 후 목록 복귀. 하늘색: 더보기 아이콘 #2b9fe0, 방금 등록·수정한 행 배경 #e6f4fc (admin만)
- ex-data-table-cell: "공통 목록" 탭의 서비스 공통 판매처 목록, 보기 전용 2열(판매처명 · 웹사이트 주소). 수정·삭제 없음. 하늘색 없음 (admin만)
- ex-modal-card: ① 등록·수정 폼 시트(예시 상태): 헤더 한 줄 = 제목 heading-3 "판매처 등록"(수정이면 "판매처 수정") 왼쪽 + 오른쪽 위 × 닫기(누름 영역 44 이상, 뒤로가기 없음) → body-sm(#707070) "우리 학교에서만 보여요" → 라벨 위·입력 아래 세로 입력 3개(판매처명 · 연락처 · 웹사이트 주소, 사이 16) → 하단 고정 버튼 줄 button-outline "취소" + button-primary "저장"(비율 1:2, 사이 8, 판매처명이 비면 "저장" 비활성). × 와 "취소"는 같은 동작(저장하지 않고 닫기). ② 삭제 확인: 제목 "이 판매처를 삭제할까요?" + × 닫기 + button-outline "취소" + button-primary "삭제". 1px #e0e0e0 테두리, 그림자·딤 없음, 모바일 위쪽 rounded 24·tab-bar 위, 데스크탑 rounded 24 가운데. 핑크 없음. 하늘색 없음 (admin만)
- button-primary: 하단 고정 "판매처 등록", 폼 "저장", 삭제 확인 "삭제"(#141414 채움, #ffffff 글자, rounded 9999, 높이 44 이상). 모바일 "판매처 등록"은 tab-bar 바로 위. 하늘색 없음 (admin만)
- button-outline: 폼 시트 "취소", 삭제 확인 "취소"(#ffffff, 1px #e0e0e0, 라벨 #141414, rounded 9999, 높이 44 이상) (admin만)
- ex-empty-state-card: 학교 판매처가 0건일 때 "등록한 판매처가 없어요" + 아래 등록 진입(하단 고정 "판매처 등록"과 같은 동작). 하늘색: 안내 아이콘 #2b9fe0 (admin만)
- ex-toast: "판매처를 저장했어요" / "판매처를 삭제했어요". 모바일은 tab-bar 위. 하늘색: 완료 체크 아이콘 #2b9fe0 (admin만)
- tab-bar: 모바일 전용 하단 탭바 1개(공통 규격). 하단 고정 버튼·폼 시트는 이 바 위에 쌓는다. 데스크탑에는 두지 않는다. 하늘색: 활성 tab-item 아이콘 #2b9fe0만 (admin만 — 화면 자체가 admin 전용)
- tab-item: "홈" · "시약" · "QR 스캔" · "기록" 4개. 활성 = "시약"(#2b9fe0 아이콘 + 라벨 #141414), 비활성 3개 #707070 (admin만)
### 반영한 레퍼런스
- https://uibowl.io/name/%EC%A7%91%EC%A7%80%EC%BC%9C?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&imgId=cmubaul16001ijs04tf5nxq2h
- https://uibowl.io/name/%ED%8F%B4%EC%84%BC%ED%8A%B8?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&imgId=cmpuv1xvn00drld04o609wd7w
- https://uibowl.io/name/%EC%91%A5%EC%91%A5%EC%B0%B0%EC%B9%B5?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&imgId=cmub7kvlz0007js04xdyeh3c1
- https://uibowl.io/name/%EB%83%89%EC%9E%A5%EA%B3%A0%ED%84%B8%EA%B8%B0?patterns=%EC%B4%88%EB%8C%80%ED%95%98%EA%B8%B0%C2%B7%EB%B0%9B%EA%B8%B0&imgId=cmohwt39000b9jm04x67jmza1

## 역할별 노출
앱 전체(화면 1~13) 기준 개수. runs/20261007-0744 표를 기준으로 한다. 이번 run은 화면 5·6·8·9 안의 배치·문구만 바꾸고 표의 컴포넌트를 새로 더하거나 빼지 않으므로 숫자는 그대로다.
manual-upload = 화면 6 안내 박스 진입 1 + 화면 5 업로드 영역 1(교사·admin). reorder-alert-card = 화면 6 1 + 홈 카드 1(교사·admin). vendor-link = 화면 6 1(교사·admin). vendor-register = 화면 6 버튼 1 + 화면 9 블록 1(admin만). user-manage = 화면 8 1 + 홈 quick-action 1(admin만). msds-entry = 화면 3 1 + 화면 10 상세 1(학생·교사·admin 모두, R4 충족).
auto-threshold-badge·nav-account-menu는 rules.json roles 대상이 아니라 표에 넣지 않는다.

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
