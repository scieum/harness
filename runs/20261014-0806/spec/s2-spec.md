# S2 설계 — run 20261014-0806

대상 화면: 5 (실험 매뉴얼) · 6 (재주문 알림) · 7 (입고·시약 등록) · 8 (사용자 관리) · 9 (판매처 설정) · 11 (시약장 설정) · 상태 화면 없음 · 둘러보기 없음 · 학교: 샘플고등학교 (input.json) · 키스크린: 11-mobile, 7-mobile
변경 사유: 요청 9 마무리 (2026-10-14, rules.json 1.29) — 관리 아래 나머지 화면 5·6·7·8·9·11의 모바일 머리와 탭바만 바꾼다. ① 모바일 nav-pill 맨 왼쪽 manage-back "‹ 관리"(→ 화면 18) ② tab-bar 4개 "홈" · "관리" · "QR 스캔" · "기록", 활성 = "관리"(격자 아이콘) ③ ☰ mobile-menu-button·mobile-menu-sheet 없음. 본문 구성·데스크톱 구성은 바꾸지 않는다.
근거: docs/PRD.md §7, docs/story-service.md 결정 사항 2026-10-13(관리 탭), docs/design.md "Manage tab"(manage-back)·`tab-bar`·"Desktop shell", harness/rules.json 1.29(manage.back — "관리 아래 화면(2·5·6·7·8·9·11·17) 모바일 머리 왼쪽 '‹ 관리', tab-bar 활성 = '관리'", manage.desktop "데스크톱은 바꾸지 않는다", tab_bar.labels·labels_source·qr_pending, mobile_menu.removed, desktop_shell.menu, screens_required 7·11, roles R1~R8, never.N1·N2), research/s1-adopt.md.
기준 설계(틀): 각 화면의 최신 승인 설계를 그대로 옮긴다 — 화면 5·6·7·9·11 = runs/20261008-0936/spec/s2-spec.md(승인 2026-10-08, 이후 상태 화면만 runs/20261008-1610에서 추가), 화면 8 = runs/20261012-0939/spec/s2-spec.md 화면 8(승인). 이후 승인된 공통 변경 두 가지는 함께 반영한다: 데스크톱 사이드바 "센서"(시약 아래) + "QR 찾기" 비활성 '준비 중'(2026-10-11 요청 7), 모바일 tab-item "QR 스캔" 회색 '준비 중'(2026-10-11). 탭바 모양 = run 20261013-1938 S4-screens-v24(716:2) 2-mobile과 같게(input.json base).

색·폰트·모서리·간격은 docs/design.md와 harness/rules.json을 따른다. 허용 색 밖의 값(딤 반투명 검정 등)은 쓰지 않는다. 반투명 회색은 badge-overlay 안에서만. 그림자는 쓰지 않는다(segmented-control-active 예외). 떠 있는 버튼(FAB)은 두지 않는다.
- 핑크 #d6246a·연핑크 #fbe9f0는 badge-low-stock, reorder-alert-card, mix-warning 안에서만 쓴다(이번 대상 기준: 화면 6 재주문 알림 카드, 화면 11 혼재 주의사항). manage-back·tab-bar에는 핑크를 쓰지 않는다.
- 하늘색 #2b9fe0·옅은 하늘색 #e6f4fc는 선택·현재 위치·진행·아이콘·안내 띠에만 쓴다. 글자색 금지(그 위 글자 #141414). badge-low-stock·reorder-alert-card·button-primary·mix-warning 안에는 쓰지 않는다. manage-back은 ‹ 아이콘만 #2b9fe0, 라벨 "관리"는 #141414.
학교 선택은 회원가입(화면 14)에만 있다. 화면 5·6·7·8·9·11에는 학교 선택·전환을 두지 않고 현재 학교명 "샘플고등학교"를 모바일은 nav-pill 안(manage-back 오른쪽 끝, nav-account-menu ▾ 옆), 데스크톱은 app-sidebar 맨 위에 표시한다. 매뉴얼 추출 연결·재주문 알림·입고·사용자·판매처·시약장은 모두 샘플고등학교 것만 보인다(N1).
외부 서비스 연결 값(매뉴얼 AI 추출·서류 읽기·MSDS 조회)은 서버에서만 다룬다. 어떤 화면에도 연결 값 입력 칸·외부 서비스 설정·AI 엔진 선택 UI·관련 문구를 두지 않는다(N2).
괄호 안 역할 표시가 없는 구성 요소는 그 화면에 들어오는 모든 역할에게 보인다. 화면 5·6·7 = 교사·admin만, 화면 8·9 = admin만, 화면 11 = 학생·교사·admin(학생은 보기만) 들어온다. manage-back은 그 화면에 들어오는 모든 역할에게 같다.

모바일 공통(승인본 + 요청 9 마무리):
- 머리(관리 아래 화면 머리, 화면 2·17 승인본 nav-pill ②와 같은 모양): nav-pill = 맨 왼쪽 manage-back "‹ 관리"(이전 워드마크·뒤로가기 자리) → 오른쪽 끝 현재 학교명 "샘플고등학교" + nav-account-menu ▾. "Lab_Stock" 워드마크·☰(mobile-menu-button)·뒤로가기 화살표는 두지 않는다. 승인본에서 nav-pill 안에 있던 화면 제목("실험 매뉴얼"·"재주문 알림"·"입고·시약 등록"·"판매처 설정"·"시약장 설정")은 nav-pill 바로 아래 페이지 머리 줄(heading-4 #141414, 좌우 여백 16, 위 16)로 내린다 — 화면 2·17 승인본과 같은 순서. 화면 8은 user-manage 헤더 heading-3 "샘플고등학교 사용자 5명"이 제목 역할이라 따로 제목 줄을 두지 않는다. 제목 줄 아래 본문은 승인본 그대로.
- manage-back: link "‹ 관리"(‹ 아이콘 #2b9fe0 + body #141414, 채움 없음, 누름 영역 44 이상) → 화면 18 관리. 화면 5에 승인본에서 있던 뒤로가기(→ 화면 6)도 이것으로 바뀐다.
- tab-bar: 화면 아래 가장자리 y 780~844(폭 390, 높이 64, rounded 0, #ffffff + 위쪽 1px #f0f0f0 선, 그림자 없음). tab-item 4개 "홈" · "관리" · "QR 스캔" · "기록"을 같은 폭으로 채운다(가운데 키운 버튼 없음). "관리" 아이콘 = 네 칸 격자. 활성 = "관리"(#2b9fe0 아이콘 + #141414 라벨), "홈"·"기록" = #707070 아이콘·라벨. "QR 스캔"은 화면 12 전까지 회색 — 아이콘·라벨 #adadad + 아이콘 아래 caption "준비 중"(#adadad), 누르면 ex-toast "준비 중이에요". 모양은 S4-screens-v24(716:2) 2-mobile 탭바와 같다.
- 하단 고정 바·버튼은 tab-bar 위쪽 선 바로 위. 시트는 tab-bar 위쪽 선 위에 붙는다(딤 없음, 1px #e0e0e0 테두리, 위쪽 rounded 24, 오른쪽 위 × 닫기).
데스크톱 공통(1440×900, rules.json desktop_shell, 요청 9로 바뀌지 않음): nav-pill·tab-bar·manage-back·mobile-menu-button 없음.
- app-sidebar: 왼쪽 고정 열 폭 240, 높이 전체, rounded 0, #f3f3f3 채움, 오른쪽 1px #f0f0f0 선. 맨 위 "Lab_Stock" 워드마크 + 학교명 "샘플고등학교"(title #141414, 전환 없음) → sidebar-item 묶음 → 맨 아래 "{이름} · {역할}"(body-sm) + nav-account-menu ▾.
- sidebar-item: 아이콘 + body 라벨, 높이 44, rounded 0. 현재 항목 = #e6f4fc 채움 + #2b9fe0 아이콘, 라벨 #141414. 메뉴(desktop_shell.menu): 학생 6개(홈·시약·센서·기록·시약장·QR 찾기) / 교사 9개(+ "관리" 입고·실험 매뉴얼·재주문 알림) / admin 11개(+ "학교 설정" 사용자·판매처). "QR 찾기"는 비활성 — 아이콘·라벨 #adadad + caption "준비 중"(#adadad), 누르면 ex-toast "준비 중이에요".
- 본문 = 사이드바 오른쪽, 페이지 여백 32. 페이지 머리 = 왼쪽 제목(heading-2) + 개수(caption #707070), 오른쪽 검색·주 버튼. 무거운 작업(5·7·11) = 본문 페이지, 가운데 단일 열 폭 640, 주 동작은 본문 하단 고정 바(#ffffff, 위 1px #f0f0f0 선, 오른쪽 정렬). data-table = ex-data-table-cell 머리행(caption #707070)·본문(body-sm), rounded 16 컨테이너 + 1px #f0f0f0 테두리, 선택 행 #e6f4fc. detail-drawer = 오른쪽 폭 480, 높이 전체, #ffffff, 왼쪽 1px #f0f0f0 선, 딤 없음, 오른쪽 위 × 닫기.
- 겹침: ex-modal-card는 확인·한 칸 입력에만(가운데 폭 440, rounded 24, 1px #e0e0e0, 그림자·딤 없음). 모바일 고르기 시트는 데스크톱에서 그 컨트롤에 붙은 드롭다운·팝오버. ex-toast는 모바일 tab-bar 바로 위 / 데스크톱 오른쪽 아래.
예시 데이터(승인본 그대로): 샘플고등학교 시약 42종, 재고 부족 3종(염산 · 50 mL, 에탄올 · 200 mL, 질산은 · 5 g), 시약장 2개(1번 시약장 · 2번 시약장). 데스크톱 프레임 기준 역할 = 화면 8·9는 admin "정OO · admin", 나머지는 교사 "김OO · 교사".

## 화면 5
실험 매뉴얼 → AI 추출 결과 확인. 교사·admin만(학생 노출 0). 승인본(runs/20261008-0936 화면 5) 그대로 + 요청 9: 모바일 nav-pill 뒤로가기(→ 화면 6) → manage-back "‹ 관리", 제목 "실험 매뉴얼"은 nav-pill 아래 제목 줄, 탭 "관리" 활성(승인본 "기록" → "관리"). 흐름: 1단계 업로드(파일 + 조 수, 조 수 처음 빈 값) → "AI 추출" → 2단계 추출 결과 확인 → "확인 후 저장".
예시 상태(5-mobile · 5-desktop, 승인본 그대로): 2단계. 접힌 manual-upload("산·염기 중화 실험.pdf", 조 수 4) 아래 extraction-table 행 4개 —
① 염산 · 1조 20 · mL → 80 mL / 우리 학교 시약 "염산" · 삭제 · "기존 기준 100 · 바뀌어요"
② 수산화나트륨 · 1조 5 · g → 20 g / "수산화나트륨" · 삭제 · "기존 기준 20 · 그대로 둬요"
③ 페놀프탈레인 용액 · 1조 2 · mL → 8 mL / "페놀프탈레인 용액" · 삭제 · "기존 기준 없음 · 새로 정해요"
④ 증류수 · 1조 150 · mL → 600 mL / "증류수" · 삭제 · "기존 기준 500 · 바뀌어요" + 무채색 안내 줄 "2개 행을 합쳤어요"
모바일 활성 탭: "관리". 위→아래: nav-pill(‹ 관리 + 학교명 ▾) → 제목 줄 heading-4 "실험 매뉴얼" → 접힌 manual-upload → extraction-table(행 카드) → 하단 버튼 줄("다시 추출" + "확인 후 저장") → tab-bar.
데스크톱 배치: app-sidebar("실험 매뉴얼" 현재) | 본문 페이지 = 페이지 머리 "실험 매뉴얼" → 가운데 단일 열 폭 640: 접힌 manual-upload 한 줄 → extraction-table 열 표(시약명 · 1조 사용량 · 단위 · 1반 1회 필요량, 행마다 아래 줄) → 본문 하단 고정 바(button-outline "다시 추출" + button-primary "확인 후 저장" 오른쪽 정렬). 승인본 그대로.
### 구성 요소
- app-sidebar: 데스크톱 전용. 공통 규격, 학교명 "샘플고등학교" + 메뉴 + nav-account-menu (교사·admin만)
- sidebar-item: 데스크톱 전용. 교사 9개(홈·시약·센서·기록·시약장·QR 찾기 / 입고·실험 매뉴얼·재주문 알림) / admin 11개(+ 사용자·판매처). 현재 = "실험 매뉴얼", "QR 찾기" 비활성 '준비 중'. 학생에게는 이 화면이 없다 (교사·admin만)
- nav-pill: 모바일 전용. 관리 아래 화면 머리 — 맨 왼쪽 manage-back "‹ 관리" + 오른쪽 현재 학교명 "샘플고등학교" + nav-account-menu ▾. 워드마크·☰·뒤로가기 없음. 학교 전환 없음 (교사·admin만)
- manage-back: 모바일 전용. nav-pill 맨 왼쪽 link "‹ 관리"(‹ 아이콘 + body #141414, 누름 영역 44 이상) → 화면 18. 승인본 뒤로가기(→ 화면 6) 자리. 데스크톱에는 두지 않는다. 하늘색: ‹ 아이콘 #2b9fe0 (교사·admin만)
- nav-account-menu: 모바일 = 학교명 옆 ▾, 데스크톱 = app-sidebar 맨 아래. "로그아웃" 1개. 하늘색 없음 (교사·admin만)
- manual-upload: 1단계 업로드 영역(승인본 그대로). 처음 상태 = body-lg "실험 매뉴얼을 올리면 시약별 사용량을 찾아드려요" + 업로드/미리보기 타일(rounded 16, 비율 유지) + "조 수" text-input(빈 값, 플레이스홀더 "예: 4") + button-primary "AI 추출"(파일·조 수가 비면 비활성). 추출 중 = 타일 안 진행 막대 + "사용량을 찾고 있어요". 2단계(예시) = 한 줄 높이로 접혀 파일 타일(작은 미리보기 + badge-overlay) 오른쪽에 "조 수 4"(고치면 필요량 다시 계산). 데스크톱 = 640 열 맨 위 같은 한 줄. 하늘색: 업로드 아이콘 #2b9fe0, 진행 막대 #2b9fe0(트랙 #e6f4fc) (교사·admin만)
- badge-overlay: 미리보기 위 파일 이름 태그 "산·염기 중화 실험.pdf"(rgba(115,115,115,0.56), #ffffff label, rounded 9999). 하늘색 없음 (교사·admin만)
- text-input: "조 수"(숫자, 기본 빈 값), 추출 행 "1조 사용량"(숫자), 단위 선택 상자(값 "mL" ▾, 목록 병 · mL · g — 데스크톱은 드롭다운), "우리 학교 시약" 선택 상자. #f0f0f0, 테두리 없음, rounded 16, 포커스 링 2px #141414. 하늘색: ▾ 아이콘 #2b9fe0 (교사·admin만)
- extraction-table: 2단계 추출 결과 확인(승인본 그대로). heading-3 "추출 결과 확인" + body-sm(#707070) "확인한 뒤 저장해야 반영돼요". 행 1줄 = 시약명(title) · 1조 사용량 + 단위 · 1반 1회 필요량(자동 계산) / 2줄(위 간격 8) = "우리 학교 시약" 선택 상자(샘플고등학교 시약만) → 조용한 텍스트 동작 "삭제"(link #141414, 확인 없음) → 줄 끝 body-sm(#707070) "기존 기준 {N} · 그대로 둬요 / 바뀌어요"(기준 없으면 "기존 기준 없음 · 새로 정해요"). 같은 시약이 여러 번 나오면 한 행으로 합치고 caption(#707070) "2개 행을 합쳤어요". 모바일 = 행마다 #f3f3f3 카드(rounded 16, 여백 16), 데스크톱 = rounded 16 표 컨테이너 안 ex-data-table-cell 행(폭 640). 하늘색: 고친 사용량 칸 배경 #e6f4fc (교사·admin만)
- ex-data-table-cell: 데스크톱 extraction-table 머리행(caption #707070 "시약명 · 1조 사용량 · 단위 · 1반 1회 필요량")과 본문 셀(body-sm), 행 구분 1px #f0f0f0 선 (교사·admin만)
- button-outline: 2단계 "다시 추출"(#ffffff, 1px #e0e0e0, 라벨 #141414, rounded 9999, 높이 44 이상). 모바일 = tab-bar 위 버튼 줄 왼쪽(비율 1:2), 데스크톱 = 하단 고정 바 "확인 후 저장" 왼쪽 (교사·admin만)
- button-primary: 1단계 "AI 추출", 2단계 "확인 후 저장"(#141414 채움, #ffffff 글자, rounded 9999, 높이 44 이상). 저장하면 각 행 필요량이 연결된 시약의 재주문 기준(화면 3 reorder-threshold와 같은 칸)에 들어간다. 연결 안 된 행이 있으면 비활성. 모바일 = tab-bar 위 버튼 줄 오른쪽, 데스크톱 = 본문 하단 고정 바 오른쪽 끝. 하늘색 없음 (교사·admin만)
- ex-toast: 저장 직후 "재주문 기준을 저장했어요", 이후 화면 6. 'QR 스캔' 탭·'QR 찾기' 메뉴 "준비 중이에요". 이 프레임에는 그리지 않는다. 모바일 tab-bar 위, 데스크톱 오른쪽 아래. 하늘색: 완료 체크 아이콘 #2b9fe0 (교사·admin만)
- tab-bar: 모바일 전용 하단 탭바 1개(공통 규격, S4-screens-v24 2-mobile과 같은 모양). 데스크톱에는 두지 않는다. 하늘색: 활성 tab-item 아이콘 #2b9fe0만 (교사·admin만)
- tab-item: "홈" · "관리" · "QR 스캔" · "기록" 4개. 활성 = "관리"(격자 아이콘 #2b9fe0, 라벨 #141414), "QR 스캔" 회색 '준비 중', "홈"·"기록" #707070 (교사·admin만)
### 반영한 레퍼런스
- https://uibowl.io/website/%EB%8B%B9%EA%B7%BC%20%EB%B9%84%EC%A6%88%EB%8B%88%EC%8A%A4?patterns=%EC%83%81%EC%84%B8%EC%A0%95%EB%B3%B4%20%28PDP%29&imgId=cmso6dgem00ualf04cqgg6fh8
- https://uibowl.io/name/%ED%8E%98%EC%9D%B4%EC%9B%8C%ED%81%AC?patterns=%EB%A9%94%EB%89%B4&patternName=%EA%B0%84%ED%8E%B8%EB%A9%94%EB%89%B4%20-%20%EA%B1%B0%EB%9E%98%EC%B2%98
- https://uibowl.io/name/%ED%8E%98%EC%9D%B4%ED%9E%88%EC%96%B4?patterns=%EB%A9%94%EC%9D%B8&imgId=cmnfmxdij001fl204l8u0mu8b
- https://uibowl.io/name/%ED%8E%98%EC%9D%B4%EC%9B%8C%ED%81%AC?patterns=%EB%A9%94%EC%9D%B8&imgId=cmtzo55qv002rl7047rsl7n07

## 화면 6
재주문 알림. 교사·admin만(학생 노출 0). 승인본(runs/20261008-0936 화면 6 — 카드 문구 reorder.card_text·reorder.auto 반영본) 그대로 + 요청 9: 모바일 nav-pill 워드마크 → manage-back "‹ 관리", 제목 "재주문 알림"은 nav-pill 아래 제목 줄, 탭 "관리" 활성(승인본 "시약" → "관리").
예시 상태(6-mobile · 6-desktop, 승인본 그대로): 알림 3건.
① 염산 — "재주문 기준 100 mL"(매뉴얼 추출 값, 배지 없음) · "현재 재고 50 mL" · "10월 7일 알림". 판매처 "확인" 뒤 상태 — vendor-link 아래 새 창 안내 줄이 보인다.
② 에탄올 — "재주문 기준 800 mL" + auto-threshold-badge "자동" + 캡션 "최근 사용량으로 계산했어요" · "현재 재고 200 mL" · "10월 7일 알림".
③ 질산은 — "재주문 기준 10 g" + auto-threshold-badge "자동" + 캡션 "마지막 입고량의 20%로 계산했어요"(사용 기록 없음, 마지막 입고 50 g) · "현재 재고 5 g" · "10월 6일 알림".
모바일 활성 탭: "관리". 위→아래: nav-pill(‹ 관리 + 학교명 ▾) → 제목 줄 heading-4 "재주문 알림" → 재주문 기준 안내 박스(manual-upload 진입) → reorder-alert-card 목록 → (admin) "판매처 등록" → tab-bar.
데스크톱 배치: app-sidebar("재주문 알림" 현재) | 본문 페이지 = 페이지 머리(왼쪽 "재주문 알림" + "3건" / 오른쪽 (admin) vendor-register "판매처 등록") → 가운데 단일 열 폭 640: 안내 박스 → reorder-alert-card 세로 목록(사이 12). 판매처 고르기는 vendor-link에 붙은 팝오버. 승인본 그대로.
### 구성 요소
- app-sidebar: 데스크톱 전용. 공통 규격, 학교명 "샘플고등학교" + 메뉴 + nav-account-menu (교사·admin만)
- sidebar-item: 데스크톱 전용. 교사 9개 / admin 11개(공통 메뉴). 현재 = "재주문 알림", "QR 찾기" 비활성 '준비 중'. 학생에게는 이 화면이 없다 (교사·admin만)
- nav-pill: 모바일 전용. 관리 아래 화면 머리 — 맨 왼쪽 manage-back "‹ 관리" + 오른쪽 현재 학교명 "샘플고등학교" + nav-account-menu ▾. 워드마크·☰ 없음. 학교 전환 없음 (교사·admin만)
- manage-back: 모바일 전용. nav-pill 맨 왼쪽 link "‹ 관리"(‹ 아이콘 + body #141414, 누름 영역 44 이상) → 화면 18. 데스크톱에는 두지 않는다. 하늘색: ‹ 아이콘 #2b9fe0 (교사·admin만)
- nav-account-menu: 모바일 = 학교명 옆 ▾, 데스크톱 = app-sidebar 맨 아래. "로그아웃" 1개. 하늘색 없음 (교사·admin만)
- manual-upload: 목록 위 재주문 기준 안내 박스(#e6f4fc 채움, rounded 16, 글자 #141414, "필요량 = 1반 1회 실험량 × 조 수 · 기준이 없는 시약은 최근 사용량(사용 기록이 없으면 마지막 입고량의 20%)으로 계산해요") 끝의 button-pill-soft "실험 매뉴얼 올리기" → 화면 5. 하늘색: 박스 채움 #e6f4fc, 정보 아이콘 #2b9fe0 (교사·admin만)
- reorder-alert-card: 알림 1건 카드(#f3f3f3, 테두리 없음, rounded 24, 여백 24, 승인본 그대로). 왼쪽 위 badge-low-stock "재고 부족" → 시약명(heading-4) → body "재주문 기준 {N}{단위}"(자동 값이면 숫자 바로 오른쪽 auto-threshold-badge "자동" + 그 줄 아래 caption #707070 근거 한 줄) → body "현재 재고 {M}{단위}" → caption(#707070) "{M}월 {D}일 알림" → 카드 하단 오른쪽 vendor-link. 판매처 "확인" 뒤 vendor-link 바로 아래(간격 8) 무채색 안내 줄: #707070 바깥 링크 아이콘 + body-sm(#707070) "사이트를 새 창으로 열었어요. 열리지 않았다면" + button-pill-soft "직접 열기". 데스크톱도 같은 카드(폭 640). 카드 안 하늘색 없음 (교사·admin만)
- badge-low-stock: reorder-alert-card 안 "재고 부족"(#d6246a 채움, #ffffff label, rounded 9999). 하늘색 없음 (교사·admin만)
- auto-threshold-badge: 자동 기준 카드(에탄올·질산은) 기준 숫자 오른쪽 pill "자동"(#f3f3f3 채움 + 1px #e0e0e0 테두리, label #141414, rounded 9999). 매뉴얼 추출·직접 입력 기준(염산)에는 없다. 핑크·하늘색 없음 (교사·admin만)
- vendor-link: reorder-alert-card 하단 오른쪽 button-primary "판매처 연결"(#141414 채움, #ffffff 글자, rounded 9999, 높이 44 이상). 누르면 판매처 고르기 — 모바일 = ex-modal-card 시트, 데스크톱 = 버튼에 붙은 팝오버. 하늘색 없음 (교사·admin만)
- ex-modal-card: 판매처 고르기(모바일 tab-bar 위 시트, 데스크톱은 같은 내용을 vendor-link 팝오버로, 1px #e0e0e0 테두리, 그림자·딤 없음). 제목 heading-3 "판매처 고르기" + 시약명 caption → 판매처 행 목록(샘플고등학교 판매처 먼저, 그다음 공통 목록) → button-outline "취소" + button-primary "확인". 하늘색: 선택 행 배경 #e6f4fc + 왼쪽 #2b9fe0 선택 표시 (교사·admin만)
- button-pill-soft: 안내 박스 "실험 매뉴얼 올리기", 카드 새 창 안내 줄 "직접 열기"(카드 위라 1px #e0e0e0 테두리, 라벨 #141414, rounded 9999). 하늘색 없음 (교사·admin만)
- button-outline: 판매처 고르기 "취소", (admin) "판매처 등록" (교사·admin만)
- vendor-register: button-outline "판매처 등록" → 화면 9. 모바일 = 알림 목록 아래, 데스크톱 = 페이지 머리 오른쪽 (admin만, 교사 화면에는 없음)
- ex-empty-state-card: 알림 0건 "재고가 부족한 시약이 없어요"(이 프레임 숨김). 하늘색: 안내 아이콘 #2b9fe0 (교사·admin만)
- ex-toast: 'QR 스캔' 탭·'QR 찾기' 메뉴 "준비 중이에요"(이 프레임에는 그리지 않음). 핑크 없음 (교사·admin만)
- tab-bar: 모바일 전용 하단 탭바 1개(공통 규격, S4-screens-v24 2-mobile과 같은 모양). 데스크톱에는 두지 않는다. 하늘색: 활성 tab-item 아이콘 #2b9fe0만 (교사·admin만)
- tab-item: "홈" · "관리" · "QR 스캔" · "기록" 4개. 활성 = "관리"(격자 아이콘), "QR 스캔" 회색 '준비 중', "홈"·"기록" #707070 (교사·admin만)
### 반영한 레퍼런스
- https://uibowl.io/website/%EB%8B%B9%EA%B7%BC%20%EB%B9%84%EC%A6%88%EB%8B%88%EC%8A%A4?patterns=%EC%83%81%EC%84%B8%EC%A0%95%EB%B3%B4%20%28PDP%29&imgId=cmso6dgem00ualf04cqgg6fh8
- https://uibowl.io/name/%ED%8E%98%EC%9D%B4%ED%9E%88%EC%96%B4?patterns=%EB%A9%94%EC%9D%B8&imgId=cmnfmxdij001fl204l8u0mu8b
- https://uibowl.io/name/%ED%8E%98%EC%9D%B4%ED%9E%88%EC%96%B4?patterns=%EB%A9%94%EC%9D%B8&imgId=cmnfmxnhh0003l8045z9h1r15
- https://uibowl.io/name/%ED%95%98%EC%9D%B4%EB%A7%81%EA%B5%AC%EC%96%BC?patterns=%EB%A9%94%EC%9D%B8&imgId=cmnmkywio0003l804k22ndnyy

## 화면 7
입고·시약 등록. 교사·admin만(홈 quick-action "입고", 화면 3 "입고", 관리 탭 "입고" 행, 데스크톱 sidebar-item "입고"). 승인본(runs/20261008-0936 화면 7) 그대로 — intake-mode 기본 "서류로 입고", 아직 파일 없는 첫 상태 — + 요청 9: 모바일 nav-pill 워드마크 → manage-back "‹ 관리", 제목 "입고·시약 등록"은 nav-pill 아래 제목 줄, 탭 "관리" 활성(승인본 "시약" → "관리"). 이후 흐름은 승인된 상태 화면 7-doc-upload → 7-doc-review → 7-suggest, 실패 7-doc-fail, MSDS 7-msds(이번 대상 아님).
모바일 활성 탭: "관리". 위→아래: nav-pill(‹ 관리 + 학교명 ▾) → 제목 줄 heading-4 "입고·시약 등록" → intake-mode → doc-upload → tab-bar.
데스크톱 배치: app-sidebar("입고" 현재) | 본문 페이지 = 페이지 머리 "입고" → 가운데 단일 열 폭 640: intake-mode → doc-upload 카드 → 본문 하단 고정 바(button-primary "AI로 읽기" 오른쪽, 파일 없으면 비활성). "직접 입력"은 같은 640 열의 "라벨 | 입력" 행 폼. 승인본 그대로.
### 구성 요소
- app-sidebar: 데스크톱 전용. 공통 규격, 학교명 "샘플고등학교" + 메뉴 + nav-account-menu (교사·admin만)
- sidebar-item: 데스크톱 전용. 교사 9개 / admin 11개(공통 메뉴). 현재 = "입고", "QR 찾기" 비활성 '준비 중'. 학생에게는 이 화면이 없다 (교사·admin만)
- nav-pill: 모바일 전용. 관리 아래 화면 머리 — 맨 왼쪽 manage-back "‹ 관리" + 오른쪽 현재 학교명 "샘플고등학교" + nav-account-menu ▾. 워드마크·☰ 없음. 학교 전환 없음 (교사·admin만)
- manage-back: 모바일 전용. nav-pill 맨 왼쪽 link "‹ 관리"(‹ 아이콘 + body #141414, 누름 영역 44 이상) → 화면 18. 그 아래 제목 줄 → intake-mode 순서. 데스크톱에는 두지 않는다. 하늘색: ‹ 아이콘 #2b9fe0 (교사·admin만)
- nav-account-menu: 모바일 = 학교명 옆 ▾, 데스크톱 = app-sidebar 맨 아래. "로그아웃" 1개 (교사·admin만)
- intake-mode: 제목 줄 아래 segmented-control 두 옵션 "직접 입력 / 서류로 입고", 한 번에 하나. 기본·이 프레임 = "서류로 입고". 데스크톱 = 640 열 맨 위 (교사·admin만)
- segmented-control: intake-mode 트랙(#f3f3f3, rounded 9999), "직접 입력" 모드 안 "기존 시약 입고 / 새 시약 등록" 토글 (교사·admin만)
- segmented-control-active: 선택 옵션 흰 pill. 하늘색: 1px #2b9fe0 테두리(글자 #141414) (교사·admin만)
- doc-upload: 올리기 카드 1개(ex-empty-state-card 모양, #ffffff, 1px #e0e0e0 테두리, rounded 24, 여백 24, 승인본 그대로). 가운데 업로드 아이콘 → heading-4 "품의서·영수증·거래명세서를 올려 주세요" → caption(#707070) "PDF·JPG·PNG, 4MB까지" → button-pill-soft "촬영하기" · "파일 선택"(데스크톱은 "파일 선택" + 끌어다 놓기 안내 caption "여기에 끌어다 놓아도 돼요") → button-primary "AI로 읽기"(모바일 = 카드 하단 전폭, 데스크톱 = 본문 하단 고정 바). 형식·크기 오류 = #141414 아이콘 + body-sm "PDF·JPG·PNG 4MB까지만 올릴 수 있어요"(핑크 금지). 하늘색: 업로드 아이콘 #2b9fe0 (교사·admin만)
- button-pill-soft: doc-upload "촬영하기"(모바일) · "파일 선택"(#f3f3f3, 라벨 #141414, rounded 9999). 하늘색: 왼쪽 아이콘 #2b9fe0 (교사·admin만)
- button-primary: "AI로 읽기"(#141414 채움, #ffffff 글자, rounded 9999, 높이 44 이상, 파일 없으면 비활성), 직접 입력의 "입고"·"시약 등록". 하늘색 없음 (교사·admin만)
- stock-intake: "직접 입력" 모드 "기존 시약 입고" 갈래 — 기존 구성 그대로(검색 → 선택 → 수량 → 입고일 → "입고"). 데스크톱 = 640 열 "라벨 | 입력" 행. 이 프레임에는 그리지 않는다 (교사·admin만)
- reagent-register: "직접 입력" 모드 "새 시약 등록" 갈래 — 기존 폼(시약명·종류·재고량·입고일) + MSDS 칸 옆 msds-search. 이 프레임에는 그리지 않는다 (교사·admin만)
- msds-search: reagent-register MSDS 칸 옆·서류 new-reagent-fields 안 button-pill-soft "MSDS 찾기"(모바일 msds-candidates 시트, 데스크톱 버튼에 붙은 팝오버). 이 프레임에는 그리지 않는다 (교사·admin만)
- text-input: 직접 입력 모드 검색·수량·입고일·폼 입력(#f0f0f0, rounded 16, 포커스 링 2px #141414). 이 프레임에는 그리지 않는다 (교사·admin만)
- ex-toast: 입고 저장 직후 "입고를 기록했어요", 'QR 스캔' 탭·'QR 찾기' 메뉴 "준비 중이에요". 모바일 tab-bar 위, 데스크톱 오른쪽 아래. 이 프레임에는 그리지 않는다 (교사·admin만)
- tab-bar: 모바일 전용 하단 탭바 1개(공통 규격, S4-screens-v24 2-mobile과 같은 모양). 데스크톱에는 두지 않는다. 하늘색: 활성 tab-item 아이콘 #2b9fe0만 (교사·admin만)
- tab-item: "홈" · "관리" · "QR 스캔" · "기록" 4개. 활성 = "관리"(격자 아이콘 — 입고 화면에서도 관리 탭 활성), "QR 스캔" 회색 '준비 중', "홈"·"기록" #707070 (교사·admin만)
### 반영한 레퍼런스
- https://uibowl.io/website/%EB%8B%B9%EA%B7%BC%20%EB%B9%84%EC%A6%88%EB%8B%88%EC%8A%A4?patterns=%EC%83%81%EC%84%B8%EC%A0%95%EB%B3%B4%20%28PDP%29&imgId=cmso6dgem00ualf04cqgg6fh8
- https://uibowl.io/name/%ED%8E%98%EC%9D%B4%EC%9B%8C%ED%81%AC?patterns=%EB%A9%94%EB%89%B4&patternName=%EA%B0%84%ED%8E%B8%EB%A9%94%EB%89%B4%20-%20%EA%B1%B0%EB%9E%98%EC%B2%98
- https://uibowl.io/name/%ED%8E%98%EC%9D%B4%EC%9B%8C%ED%81%AC?patterns=%EB%A9%94%EC%9D%B8&imgId=cmtzo55qv002rl7047rsl7n07
- https://uibowl.io/name/%ED%8E%98%EC%9D%B4%ED%9E%88%EC%96%B4?patterns=%EB%A9%94%EC%9D%B8&imgId=cmnfmxdij001fl204l8u0mu8b

## 화면 8
사용자 관리. admin만(학생·교사 노출 0). 승인본(runs/20261012-0939 화면 8 — 머리 인원 줄, 인라인 초대 폼, 멤버 표, 초대 대기 표 + 행 ⋯ invite-more-menu, 유의사항, 삭제 확인) 그대로 + 요청 9: 모바일 nav-pill에서 mobile-menu-button ☰·워드마크·제목 "사용자 관리"를 없애고 맨 왼쪽 manage-back "‹ 관리", 탭 "관리" 활성(승인본 "홈" → "관리"). 제목 줄은 따로 두지 않는다(user-manage 헤더 heading-3 "샘플고등학교 사용자 5명"이 바로 아래).
예시 상태(8-mobile · 8-desktop, 승인본 그대로): 멤버 5명(학생 3 · 교사 1 · admin 1 — 정OO(나) · 김OO · 박OO · 이OO · 최OO) · 초대 대기 2건(han@example.com · 교사 · 10월 10일 · 대기 / yoon@example.com · 학생 · 10월 11일 · 대기), 학생 "박OO" 삭제 확인이 열린 상태. 뒤 목록은 그대로 보인다. ⋯ 메뉴는 닫힘.
모바일 활성 탭: "관리". 위→아래: nav-pill(‹ 관리 + 학교명 ▾) → user-manage(헤더 "샘플고등학교 사용자 5명" + "초대" → 인원 줄 → 이름 검색 → 멤버 → 초대 대기(행 카드 오른쪽 위 ⋯) → 유의사항) → tab-bar. 삭제 확인 시트는 tab-bar 위.
데스크톱 배치: app-sidebar("사용자" 현재) | 본문 페이지 = 페이지 머리(왼쪽 "사용자" + "5명", 아래 인원 줄 / 오른쪽 인라인 초대 폼) → 툴바(이름 검색) → 멤버 data-table → "초대 대기 (2)" data-table(마지막 열 ⋯) → 유의사항. 삭제 확인 = 가운데 ex-modal-card. 승인본 그대로.
### 구성 요소
- app-sidebar: 데스크톱 전용. 공통 규격, 학교명 "샘플고등학교" + admin 메뉴 + "정OO · admin" + nav-account-menu (admin만)
- sidebar-item: 데스크톱 전용. admin 11개(홈·시약·센서·기록·시약장·QR 찾기 / 입고·실험 매뉴얼·재주문 알림 / 사용자·판매처). 현재 = "사용자", "QR 찾기" 비활성 '준비 중'. 학생·교사에게는 이 화면이 없다 (admin만)
- nav-pill: 모바일 전용. 관리 아래 화면 머리 — 맨 왼쪽 manage-back "‹ 관리" + 오른쪽 현재 학교명 "샘플고등학교" + nav-account-menu ▾. 워드마크·☰(mobile-menu-button) 없음. 학교 전환 없음 (admin만)
- manage-back: 모바일 전용. nav-pill 맨 왼쪽 link "‹ 관리"(‹ 아이콘 + body #141414, 누름 영역 44 이상) → 화면 18(승인본 ☰ 자리). 데스크톱에는 두지 않는다. 하늘색: ‹ 아이콘 #2b9fe0 (admin만)
- nav-account-menu: 모바일 = 학교명 옆 ▾, 데스크톱 = app-sidebar 맨 아래. "로그아웃" 1개. 하늘색 없음 (admin만)
- user-manage: 본문 블록 1개(승인본 그대로). 모바일 = 헤더 heading-3 "샘플고등학교 사용자 5명" + 오른쪽 button-primary "초대" → 인원 줄 body-sm #707070 "학생 3 · 교사 1 · admin 1" → 이름 검색 → "멤버"(heading-4): 행 = 이름(title) + 본인 "나" pill + 역할(body-sm #707070) + › → "초대 대기 (2)"(heading-4): 카드 행 = 이메일(title) + 역할 · 초대일 caption #707070 + 상태 "대기" + 오른쪽 위 invite-more-menu ⋯ → 유의사항 body-sm #707070 "같은 학교(샘플고등학교) 계정만 초대할 수 있어요". 데스크톱 = 페이지 머리(제목·인원 줄·인라인 초대 폼) + 멤버 data-table + 초대 대기 data-table + 유의사항. 하늘색: 본인 행 배경 #e6f4fc (admin만)
- data-table: 데스크톱 전용. ① 멤버 표 열 = 이름(정렬) · 이메일 · 역할(정렬) · 가입일(정렬) · 행 끝 ⋮(역할 바꾸기 · 사용자 삭제). ② 초대 대기 표 열 = 이메일 · 역할 · 초대일 · 상태 "대기" · 마지막 열 invite-more-menu ⋯(폭 48). 선택 행(박OO) #e6f4fc (admin만)
- invite-more-menu: 초대 대기 행의 ⋯ 아이콘 버튼(#141414, 채움 없음, 누름 영역 44 이상 — 모바일 카드 오른쪽 위, 데스크톱 data-table 마지막 열). 누르면 버튼 바로 아래 붙는 작은 메뉴(#ffffff, rounded 24, 1px #f0f0f0, 여백 8, 그림자 없음) 안 invite-cancel 1항목. 이 프레임에서는 닫힘(⋯만). 하늘색: 누른 동안 버튼 뒤 #e6f4fc 원 (admin만)
- invite-cancel: 메뉴 항목 "초대 취소"(body #141414, 높이 44, 왼쪽 아이콘 #141414). 누르면 확인 ex-modal-card(상태 화면 8-invite-cancel 승인본). 이 프레임에는 그리지 않는다. 핑크 없음 (admin만)
- text-input: 이름 검색, 초대 "이메일"(플레이스홀더 "name@example.com"). #f0f0f0, rounded 16, 포커스 링 2px #141414. 하늘색: 검색 아이콘 #2b9fe0 (admin만)
- ex-data-table-cell: 모바일 "멤버"·"초대 대기" 행, 데스크톱 data-table 머리행·셀. "나" pill = #f3f3f3 + label #141414 (admin만)
- ex-modal-card: ① 초대 시트(모바일만) ② 역할 변경 시트(모바일만) ③ 삭제 확인(예시, 열림): heading-3 "이 사용자를 삭제할까요?" + body "박OO · 사용·입고 기록은 남아요" + button-outline "취소" + button-primary "박OO 삭제". 모바일 = tab-bar 위 시트(위쪽 rounded 24), 데스크톱 = 가운데 폭 440 rounded 24. 1px #e0e0e0, 그림자·딤 없음, × 닫기. 핑크 없음 (admin만)
- segmented-control: 초대 역할 "학생 / 교사" (admin만)
- segmented-control-active: 선택 역할 흰 pill. 하늘색: 1px #2b9fe0 테두리(글자 #141414) (admin만)
- button-pill-soft: 초대 "초대 링크 복사" (admin만)
- button-primary: "초대", 삭제 확인 "박OO 삭제"(#141414 채움, #ffffff 글자, rounded 9999, 높이 44 이상). 하늘색 없음 (admin만)
- button-outline: 삭제 확인 "취소"(#ffffff, 1px #e0e0e0, 라벨 #141414) (admin만)
- ex-empty-state-card: 검색 0건 "찾는 사용자가 없어요"(이 프레임 숨김) (admin만)
- ex-toast: "초대를 보냈어요" / "역할을 바꿨어요" / "사용자를 삭제했어요" / "초대를 취소했어요", 'QR 스캔' 탭 "준비 중이에요"(이 프레임에는 그리지 않음). 하늘색: 완료 체크 아이콘 #2b9fe0 (admin만)
- tab-bar: 모바일 전용 하단 탭바 1개(공통 규격, S4-screens-v24 2-mobile과 같은 모양). 삭제 확인 시트는 이 바 위쪽 선 위에 붙는다. 데스크톱에는 두지 않는다 (admin만)
- tab-item: "홈" · "관리" · "QR 스캔" · "기록" 4개. 활성 = "관리"(격자 아이콘), "QR 스캔" 회색 '준비 중', "홈"·"기록" #707070 (admin만)
### 반영한 레퍼런스
- https://uibowl.io/website/%EB%8B%B9%EA%B7%BC%20%EB%B9%84%EC%A6%88%EB%8B%88%EC%8A%A4?patterns=%EC%83%81%EC%84%B8%EC%A0%95%EB%B3%B4%20%28PDP%29&imgId=cmso6dgem00ualf04cqgg6fh8
- https://uibowl.io/name/%ED%8E%98%EC%9D%B4%ED%9E%88%EC%96%B4?patterns=%EB%A9%94%EC%9D%B8&imgId=cmnfmxdij001fl204l8u0mu8b
- https://uibowl.io/name/WeWork%20(%EC%9C%84%EC%9B%8C%ED%81%AC)?patterns=%EB%A9%94%EC%9D%B8&imgId=cmgyp4xq2000ml104nd56ac8z
- https://uibowl.io/name/%ED%8E%98%EC%9D%B4%EC%9B%8C%ED%81%AC?patterns=%EB%A9%94%EB%89%B4&patternName=%EA%B0%84%ED%8E%B8%EB%A9%94%EB%89%B4%20-%20%EA%B1%B0%EB%9E%98%EC%B2%98

## 화면 9
판매처 설정. admin만(학생·교사 노출 0). 승인본(runs/20261008-0936 화면 9 — 판매처 행 = 이름 + 연락처만) 그대로 + 요청 9: 모바일 nav-pill 워드마크 → manage-back "‹ 관리", 제목 "판매처 설정"은 nav-pill 아래 제목 줄, 탭 "관리" 활성(승인본 "시약" → "관리").
예시 상태(9-mobile · 9-desktop, 승인본 그대로): "우리 학교 판매처" 탭, 판매처 3곳(과학교재사 · 043-210-1100 / 한빛실험기기 · 043-255-3300 / 대한시약 · 02-555-7700) 위에 "판매처 등록" 폼이 열린 상태(판매처명 "과학나라" 입력 중, 연락처·웹사이트 주소 빈 값).
모바일 활성 탭: "관리". 위→아래: nav-pill(‹ 관리 + 학교명 ▾) → 제목 줄 heading-4 "판매처 설정" → segmented-control → 검색 → 판매처 목록 → 하단 고정 "판매처 등록" → tab-bar. 폼 시트는 tab-bar 위.
데스크톱 배치: app-sidebar("판매처" 현재) | 본문 페이지 = 페이지 머리(왼쪽 "판매처" + "3곳" / 오른쪽 button-primary "판매처 등록") → 툴바(segmented-control 왼쪽, 검색 오른쪽) → data-table(판매처명 · 연락처 + 행 끝 ⋮) + 오른쪽 detail-drawer "판매처 등록" 폼. 삭제 확인 = 가운데 ex-modal-card. 승인본 그대로.
### 구성 요소
- app-sidebar: 데스크톱 전용. 공통 규격, 학교명 "샘플고등학교" + admin 메뉴 + "정OO · admin" + nav-account-menu (admin만)
- sidebar-item: 데스크톱 전용. admin 11개(공통 메뉴). 현재 = "판매처", "QR 찾기" 비활성 '준비 중'. 학생·교사에게는 이 화면이 없다 (admin만)
- nav-pill: 모바일 전용. 관리 아래 화면 머리 — 맨 왼쪽 manage-back "‹ 관리" + 오른쪽 현재 학교명 "샘플고등학교" + nav-account-menu ▾. 워드마크·☰ 없음. 학교 전환 없음 (admin만)
- manage-back: 모바일 전용. nav-pill 맨 왼쪽 link "‹ 관리"(‹ 아이콘 + body #141414, 누름 영역 44 이상) → 화면 18. 데스크톱에는 두지 않는다. 하늘색: ‹ 아이콘 #2b9fe0 (admin만)
- nav-account-menu: 모바일 = 학교명 옆 ▾, 데스크톱 = app-sidebar 맨 아래. "로그아웃" 1개. 하늘색 없음 (admin만)
- segmented-control: "우리 학교 판매처 / 공통 목록", 활성 탭 하나. 데스크톱 = 툴바 왼쪽 (admin만)
- segmented-control-active: 활성 탭 흰 pill("우리 학교 판매처"). 하늘색: 1px #2b9fe0 테두리(글자 #141414) (admin만)
- text-input: 판매처 검색("판매처 검색"), 폼 입력 3개 — "판매처명"(필수, caption "필수" #707070), "연락처", "웹사이트 주소"(판매처 연결 시 새 창으로 여는 주소, 목록 행에는 표시 안 함). 부가 정보 칸 없음. #f0f0f0, rounded 16, 포커스 링 2px #141414. 하늘색: 검색 아이콘 #2b9fe0 (admin만)
- vendor-register: "우리 학교 판매처" 블록 1개(승인본 그대로). 모바일 = 샘플고등학교 판매처 목록(행 = 판매처명 title + 연락처 caption #707070 + 오른쪽 더보기 "수정"·"삭제") + 하단 고정 button-primary "판매처 등록"(tab-bar 바로 위) → 등록·수정 폼 시트 → 저장 후 목록. 데스크톱 = 페이지 머리 "판매처 등록" + data-table + detail-drawer 폼. 하늘색: 더보기 아이콘 #2b9fe0, 방금 등록·수정한 행 #e6f4fc (admin만)
- data-table: 데스크톱 전용. 열 = 판매처명(정렬) · 연락처 · 행 끝 ⋮("수정" → 드로어 폼 / "삭제" → 확인 모달). 웹사이트 주소 열 없음. "공통 목록" 탭은 같은 2열 보기 전용(⋮ 없음). 하늘색: ⋮ 아이콘 #2b9fe0 (admin만)
- detail-drawer: 데스크톱 전용. 폭 480, #ffffff, 왼쪽 1px #f0f0f0 선, 여백 24. 헤더 = heading-3 "판매처 등록" + 오른쪽 위 × 닫기 → body-sm(#707070) "우리 학교에서만 보여요" → "라벨 | 입력" 행 판매처명 · 연락처 · 웹사이트 주소 → 아래 고정 button-outline "취소" + button-primary "저장"(1:2, 판매처명이 비면 "저장" 비활성) (admin만)
- ex-data-table-cell: 모바일 "공통 목록" 탭 보기 전용 2열(판매처명 · 연락처), 데스크톱 data-table 머리행·셀. 하늘색 없음 (admin만)
- ex-modal-card: 모바일 ① 등록·수정 폼 시트(예시, tab-bar 위): 헤더 = heading-3 "판매처 등록" + 오른쪽 위 × 닫기 → body-sm(#707070) "우리 학교에서만 보여요" → 세로 입력 3개(판매처명 · 연락처 · 웹사이트 주소, 사이 16) → button-outline "취소" + button-primary "저장"(1:2). ② 삭제 확인(모바일·데스크톱 공통): "이 판매처를 삭제할까요?" + × + "취소" + "삭제". 1px #e0e0e0 테두리, 그림자·딤 없음, 모바일 위쪽 rounded 24, 데스크톱 rounded 24 가운데. 핑크·하늘색 없음 (admin만)
- button-primary: "판매처 등록"(모바일 하단 고정 tab-bar 바로 위, 데스크톱 페이지 머리 오른쪽), 폼 "저장", 삭제 확인 "삭제"(#141414 채움, #ffffff 글자, rounded 9999, 높이 44 이상). 하늘색 없음 (admin만)
- button-outline: 폼 "취소", 삭제 확인 "취소"(#ffffff, 1px #e0e0e0, 라벨 #141414) (admin만)
- ex-empty-state-card: 학교 판매처 0건 "등록한 판매처가 없어요" + 등록 진입(이 프레임 숨김). 하늘색: 안내 아이콘 #2b9fe0 (admin만)
- ex-toast: "판매처를 저장했어요" / "판매처를 삭제했어요", 'QR 스캔' 탭 "준비 중이에요"(이 프레임에는 그리지 않음). 모바일 tab-bar 위, 데스크톱 오른쪽 아래. 하늘색: 완료 체크 아이콘 #2b9fe0 (admin만)
- tab-bar: 모바일 전용 하단 탭바 1개(공통 규격, S4-screens-v24 2-mobile과 같은 모양). 폼 시트는 이 바 위쪽 선 위에 붙는다. 데스크톱에는 두지 않는다 (admin만)
- tab-item: "홈" · "관리" · "QR 스캔" · "기록" 4개. 활성 = "관리"(격자 아이콘), "QR 스캔" 회색 '준비 중', "홈"·"기록" #707070 (admin만)
### 반영한 레퍼런스
- https://uibowl.io/website/%EB%8B%B9%EA%B7%BC%20%EB%B9%84%EC%A6%88%EB%8B%88%EC%8A%A4?patterns=%EC%83%81%EC%84%B8%EC%A0%95%EB%B3%B4%20%28PDP%29&imgId=cmso6dgem00ualf04cqgg6fh8
- https://uibowl.io/name/%ED%8E%98%EC%9D%B4%EC%9B%8C%ED%81%AC?patterns=%EB%A9%94%EB%89%B4&patternName=%EA%B0%84%ED%8E%B8%EB%A9%94%EB%89%B4%20-%20%EA%B1%B0%EB%9E%98%EC%B2%98
- https://uibowl.io/name/%ED%8E%98%EC%9D%B4%EC%9B%8C%ED%81%AC?patterns=%EB%A9%94%EC%9D%B8&imgId=cmtzo55qv002rl7047rsl7n07
- https://uibowl.io/name/%ED%95%98%EC%9D%B4%EB%A7%81%EA%B5%AC%EC%96%BC?patterns=%EB%A9%94%EC%9D%B8&imgId=cmnmkywio0003l804k22ndnyy

## 화면 11
시약장 설정. 학생·교사·admin 모두. 교사·admin은 전환·추가·이름 바꾸기·QR 인쇄·삭제·문 형태·단 수·칸 분류 편집·칸 시트(넣기·빼기), 학생은 전환과 배치도·칸 목록 보기만. 승인본(runs/20261008-0936 화면 11) 그대로 + 요청 9: 모바일 nav-pill 워드마크 → manage-back "‹ 관리", 제목 "시약장 설정"은 nav-pill 아래 제목 줄, 탭 "관리" 활성(승인본 "시약" → "관리").
예시 상태(승인본 그대로): 시약장 2개 "(1) 1번 시약장"(활성) · "(2) 2번 시약장". 1번 = 양문형 · 4단 8칸. 좌1단 = 산 + 염기(mix-warning), 좌2단 = 유기, 좌3단 = 인화성, 좌4단 = 기타, 우1단 = 산화제, 우2단 = 무기염, 우3단 = 독성, 우4단 = 기타. 시약 수: 좌1단 2, 좌2단 3, 우1단 1, 우3단 1. 선택 칸 = 좌1단. "칸 없음" 시약 2개. 교사 기준.
모바일 활성 탭: "관리". 위→아래: nav-pill(‹ 관리 + 학교명 ▾) → 제목 줄 heading-4 "시약장 설정" → cabinet-switcher(+ cabinet-add) → 시약장 이름 + "양문형 · 4단" → (교사·admin) 관리 줄 → (교사·admin) 문 형태·단 수 → 배치도 → 범례 → (교사·admin) 선택 칸 분류 칩 → mix-warning → "칸 없음" 시약 → (교사·admin) 하단 고정 "저장"(tab-bar 바로 위) → tab-bar.
데스크톱 배치: app-sidebar("시약장" 현재) | 본문 페이지 = 페이지 머리(왼쪽 "시약장" + "2개") → 가운데 단일 열 폭 640: cabinet-switcher 한 줄(+ cabinet-add) → 시약장 이름 + 관리 줄 → "라벨 | 입력" 행 문 형태 · 단 수 → 배치도 + 범례 → 선택 칸 분류 → mix-warning → "칸 없음" 시약 → (교사·admin) 본문 하단 고정 바 "저장". 칸 시트 = 칸에 붙은 팝오버, QR 인쇄 = 가운데 ex-modal-card. 승인본 그대로.
### 구성 요소
- app-sidebar: 데스크톱 전용. 공통 규격, 학교명 "샘플고등학교" + 역할별 메뉴 + nav-account-menu
- sidebar-item: 데스크톱 전용. 학생 6개 / 교사 9개 / admin 11개(공통 메뉴). 현재 = "시약장", "QR 찾기" 비활성 '준비 중'
- nav-pill: 모바일 전용. 관리 아래 화면 머리 — 맨 왼쪽 manage-back "‹ 관리" + 오른쪽 현재 학교명 "샘플고등학교" + nav-account-menu ▾. 워드마크·☰ 없음. 학교 전환 없음
- manage-back: 모바일 전용. nav-pill 맨 왼쪽 link "‹ 관리"(‹ 아이콘 + body #141414, 누름 영역 44 이상) → 화면 18. 그 아래 제목 줄 → cabinet-switcher 순서. 학생·교사·admin 모두 같다. 데스크톱에는 두지 않는다. 하늘색: ‹ 아이콘 #2b9fe0
- nav-account-menu: 모바일 = 학교명 옆 ▾, 데스크톱 = app-sidebar 맨 아래. "로그아웃" 1개. 하늘색 없음
- cabinet-switcher: 시약장 전환 pill 가로 한 줄, pill마다 cabinet-number + 이름. 활성 = #e6f4fc 채움 + 1px #2b9fe0 테두리 + 라벨 #141414, 비활성 #f3f3f3. 모바일은 넘치면 가로 스크롤, 데스크톱은 한 줄에 모두. 저장 안 한 편집이 있으면 상태 11-unsaved 모달. 모든 역할. 하늘색: 활성 pill 채움·테두리
- cabinet-number: pill마다 이름 앞 작은 원(#ffffff, 1px #e0e0e0, rounded 9999) 안 숫자 "1"·"2"(label #141414). 고정 번호, 이름을 바꿔도 그대로. 시약장 이름 heading-3 앞에도 같은 원. 핑크·하늘색 글자 없음
- cabinet-add: cabinet-switcher 줄 끝 button-pill-soft "+ 시약장 추가" → "(3) 3번 시약장" 만들기. 하늘색: "+" 아이콘 #2b9fe0 (교사·admin만)
- cabinet-edit: 편집 영역 블록 1개. 관리 줄 = button-outline "이름 바꾸기" + qr-print + 조용한 텍스트 동작 "삭제"(link #141414, 핑크 금지) → cabinet-door-select · cabinet-shelf-select(데스크톱은 "라벨 | 입력" 행) · 선택 칸 storage-class-chip 묶음 · button-primary "저장"(모바일 tab-bar 바로 위 전폭, 데스크톱 본문 하단 고정 바). "이름 바꾸기"는 ex-modal-card 한 칸 입력 (교사·admin만)
- qr-print: 관리 줄 "이름 바꾸기" 옆 button-outline "QR 인쇄"(#ffffff, 1px #e0e0e0, 라벨 #141414, rounded 9999, 높이 44 이상). 상태 11-print의 qr-print-sheet(모바일 바텀시트, 데스크톱 가운데 ex-modal-card). 하늘색: 인쇄 아이콘 #2b9fe0 (교사·admin만)
- cabinet-door-select: 문 형태 pill "양문형 / 단문형", 하나만, 예시 "양문형". 하늘색: 선택 #e6f4fc + 1px #2b9fe0 테두리(글자 #141414) (교사·admin만)
- cabinet-shelf-select: 단 수 pill "3단 / 4단", 하나만, 예시 "4단". 하늘색: 선택 #e6f4fc + 1px #2b9fe0 테두리 (교사·admin만)
- cabinet-slot: 활성 시약장 정면 배치도 칸(8칸, #f3f3f3, rounded 16, 분류 이름 label #141414, 없으면 "미지정" #707070). 왼쪽 단 라벨, 위 문 라벨 "좌"/"우", 양문형은 가운데 통로. 누르면 칸 시트(상태 11-slot; 모바일 바텀시트, 데스크톱 칸에 붙은 팝오버) — 교사·admin 넣기·빼기, 학생 목록 보기만. 좌1단 오른쪽 위 #141414 경고 아이콘. 하늘색: 선택 칸 #e6f4fc + 2px #2b9fe0 테두리(글자 #141414)
- slot-count: 시약이 있는 칸 안 작은 pill(#ffffff, rounded 9999, label #141414) "2"·"3"·"1"·"1". 빈 칸 없음. 모든 역할. 핑크·하늘색 없음
- storage-class-chip: 분류 칩 8종 "유기·산·염기·산화제·인화성·무기염·독성·기타". cabinet-edit 안 선택 칸(좌1단) 분류 고르기(여러 개, 예시 "산"·"염기") + 배치도 아래 범례(보기 전용, 학생은 범례만). 하늘색: 선택 칩 #e6f4fc + 1px #2b9fe0 테두리
- mix-warning: "주의사항" 블록(#fbe9f0 바탕, rounded 16, 제목 heading-4 #141414 + 줄마다 #d6246a 경고 아이콘 + #141414 body-sm) "좌1단: 산과 염기는 섞이면 위험해요. 다른 칸에 나눠 보관하세요". 학생에게도 보기 전용. 하늘색 없음
- reagent-row: 소제목 heading-4 "칸 없음 시약 (2)" + 행(시약명 title + 재고량 body + caption "칸 없음" #707070, #f3f3f3, rounded 16, 사이 12). 누르면 화면 3. 하늘색: 누른 행 #e6f4fc
- ex-modal-card: "이름 바꾸기" 한 칸 입력(#ffffff, 1px #e0e0e0, rounded 24, 여백 24, × 닫기): heading-3 "시약장 이름" + text-input + caption "번호 1은 바뀌지 않아요"(#707070) + "취소" + "저장". 모바일 tab-bar 위, 데스크톱 가운데. 이 프레임에서는 닫힘 (교사·admin만)
- text-input: 이름 시트 "시약장 이름"(#f0f0f0, rounded 16, 포커스 링 2px #141414) (교사·admin만)
- button-outline: 관리 줄 "이름 바꾸기", 이름 시트 "취소" (교사·admin만)
- button-primary: cabinet-edit "저장"(모바일 tab-bar 바로 위 전폭, 데스크톱 본문 하단 고정 바 오른쪽), 이름 시트 "저장". 하늘색 없음 (교사·admin만)
- ex-toast: "시약장 설정을 저장했어요" / "이름을 바꿨어요" / "3번 시약장을 추가했어요", 'QR 스캔' 탭·'QR 찾기' 메뉴 "준비 중이에요"(이 프레임에는 그리지 않음). 모바일 tab-bar 위, 데스크톱 오른쪽 아래. 하늘색: 완료 체크 아이콘 #2b9fe0
- tab-bar: 모바일 전용 하단 탭바 1개(공통 규격, S4-screens-v24 2-mobile과 같은 모양). 데스크톱에는 두지 않는다. 하늘색: 활성 tab-item 아이콘 #2b9fe0만
- tab-item: "홈" · "관리" · "QR 스캔" · "기록" 4개. 활성 = "관리"(격자 아이콘 — 시약장 설정 화면에서도 관리 탭 활성), "QR 스캔" 회색 '준비 중', "홈"·"기록" #707070
### 반영한 레퍼런스
- https://uibowl.io/website/%EB%8B%B9%EA%B7%BC%20%EB%B9%84%EC%A6%88%EB%8B%88%EC%8A%A4?patterns=%EC%83%81%EC%84%B8%EC%A0%95%EB%B3%B4%20%28PDP%29&imgId=cmso6dgem00ualf04cqgg6fh8
- https://uibowl.io/name/%ED%8E%98%EC%9D%B4%ED%9E%88%EC%96%B4?patterns=%EB%A9%94%EC%9D%B8&imgId=cmnfmxdij001fl204l8u0mu8b
- https://uibowl.io/name/%ED%8E%98%EC%9D%B4%EC%9B%8C%ED%81%AC?patterns=%EB%A9%94%EC%9D%B8&imgId=cmtzo55qv002rl7047rsl7n07
- https://uibowl.io/name/%ED%8E%98%EC%9D%B4%ED%9E%88%EC%96%B4?patterns=%EB%A9%94%EC%9D%B8&imgId=cmnfmxnhh0003l8045z9h1r15

## 역할별 노출
앱 전체(로그인 후 화면) 기준 개수. 직전 승인본 runs/20261013-1938 표를 그대로 옮긴다. 이번 변경은 모바일 머리(manage-back)와 탭바 라벨·활성만 바꾸고 본문 컴포넌트를 더하거나 빼지 않으므로 개수 영향이 없다.
- manage-back·manage-list·manage-row는 모든 역할에 있고 rules.json roles 대상이 아니어서 표에 넣지 않는다.
- mobile-menu-button·mobile-menu-sheet는 없앴다(roles 대상 아님, 개수 영향 없음).
- 화면 5 manual-upload·화면 6 manual-upload/reorder-alert-card/vendor-link/vendor-register·화면 7 stock-intake/reagent-register/doc-upload/msds-search·화면 8 user-manage/invite-more-menu/invite-cancel·화면 9 vendor-register·화면 11 cabinet-edit/cabinet-add/qr-print 개수는 승인본과 같다.

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
| doc-upload | 0 | 2 | 2 |
| msds-search | 0 | 2 | 2 |
| msds-bulk-banner | 0 | 1 | 1 |
| reagent-more-menu | 0 | 1 | 1 |
| reagent-delete | 0 | 1 | 1 |
| list-select-toggle | 0 | 2 | 2 |
| select-checkbox | 0 | 2 | 2 |
| bulk-action-bar | 0 | 2 | 2 |
| sensor-add | 0 | 1 | 1 |
| sensor-edit | 0 | 1 | 1 |
| sensor-delete | 0 | 1 | 1 |
| sensor-alert-tile | 0 | 1 | 1 |
| sensor-doc-add | 0 | 1 | 1 |
| invite-more-menu | 0 | 0 | 1 |
| invite-cancel | 0 | 0 | 1 |
| page-more-menu | 0 | 0 | 2 |
| reagent-wipe | 0 | 0 | 1 |
| record-wipe | 0 | 0 | 1 |
