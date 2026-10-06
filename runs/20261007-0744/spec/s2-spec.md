# S2 설계 — run 20261007-0744

대상 화면: 2 (시약 목록), 4 (사용 기록), 10 (사용 기록 내역) + 상태 화면 2-filter, 2-filter-empty, 4-past-date · 학교: 샘플고등학교 (input.json)
변경 사유: 2026-10-07 사용자 결정(개발 세션 요청 3) — 시약 목록 필터·정렬, 사용일 고르기. 근거: docs/PRD.md §3·§4·§7(2·4·10), docs/story-service.md 결정 사항 2026-10-07 행("시약 목록 필터·정렬"·"사용일")과 "MSDS 자동 찾기" 행, docs/design.md("List filter"·"Usage date"·"MSDS search"·"Multiple cabinets"·"Cabinet number"), harness/rules.json(roles R1~R7, screens_required 2·4, variants 2·4, list_filter, usage_date, cabinet, colors, tab_bar), research/s1-adopt.md.
기준 설계(수정하지 않음): 화면 2 = runs/20261007-0002(msds-bulk-banner 포함), 화면 4·10 = runs/20261002-1441 + 공통 nav-account-menu(runs/20261006-1223). 기존 구성 요소를 유지하고 2026-10-07 요청 3 결정분만 더하거나 바꾼다.
색·폰트·모서리·간격은 docs/design.md와 harness/rules.json을 따른다. 허용 색 밖의 값(딤 반투명 검정 등)은 쓰지 않는다. 그림자는 쓰지 않는다(segmented-control-active 예외).
- 핑크 #d6246a는 badge-low-stock 안에서만 쓴다. 필터 결과 없음·지난 날짜 안내에는 핑크를 쓰지 않고 #141414 아이콘 + #141414/#707070 문구로만 표시한다.
- 하늘색 #2b9fe0(선·인디케이터·아이콘·토글 켜짐 트랙)과 옅은 하늘색 #e6f4fc(선택 배경·안내 띠)는 선택 상태·활성 탭·적용 개수 배지·msds-bulk-banner 띠에만 쓴다. 글자색으로 쓰지 않고(그 위 글자는 #141414), badge-low-stock·button-primary 안에는 쓰지 않는다.
학교 선택은 회원가입(화면 14)에만 있다. 이번 대상 화면과 상태 화면에는 학교 선택을 두지 않고 nav-pill 안에 현재 학교명 "샘플고등학교"를 표시한다. 학교 전환 기능은 두지 않는다. 필터의 보관 위치 목록(시약장·칸)과 사용 기록은 모두 샘플고등학교 것만 보인다(N1).
외부 서비스 연결 값은 서버에서만 다룬다. 어떤 화면에도 연결 값 입력 칸·외부 서비스 설정·AI 엔진 선택 UI·관련 문구를 두지 않는다(N2).
괄호 안 역할 표시가 없는 구성 요소는 학생·교사·admin 모두에게 보인다. 필터·정렬(list-filter-button·list-filter-sheet·filter-chip-row)과 사용일(usage-date·past-date-note)은 모든 역할에 같다(rules.json list_filter.roles). 학생 화면에는 msds-bulk-banner를 그리지 않는다(R5).
모바일 공통: tab-bar는 화면 아래 가장자리 y 780~844(높이 64, rounded 0)에 붙고 본문 스크롤은 y 780에서 끝난다. 하단 고정 버튼은 tab-bar 바로 위(간격 16). 바텀시트는 tab-bar 위쪽 선 위에 붙는다(딤 없음, 1px #e0e0e0 테두리로 구분, 위쪽 rounded 24, 오른쪽 위 × 닫기). 데스크탑에는 tab-bar 없이 nav-pill 섹션 링크를 유지한다. 화면 2 필터 패널은 데스크탑에서 list-filter-button 바로 아래 드롭다운 패널로 연다.
nav-account-menu(공통): 모든 대상 화면의 nav-pill 학교명 "샘플고등학교" 옆 작은 ▾. 메뉴 항목 "로그아웃" 1개. 프레임에는 닫힌 상태(▾만)로 그린다.
예시 데이터(공통): 오늘 = 2026-10-07. 샘플고등학교 시약 42종, 재고 부족 3종(염산 · 1병, 에탄올 · 200mL, 질산은 · 5g), MSDS 없는 시약 4종, 시약장 2개(1번 시약장 · 2번 시약장).

## 화면 2
시약 목록. 학생·교사·admin 모두 들어온다. 검색 입력 오른쪽에 list-filter-button "필터"가 새로 붙는다. 기존 segmented-control "전체 / 재고 부족"은 그대로 둔다(필터와 함께 쓴다). 교사·admin에게는 MSDS 없는 시약이 있을 때 목록 위 msds-bulk-banner가 보인다(기존).
예시 상태: 필터 적용 없음(기본 정렬 이름순), "전체" 선택, 42종. 그래서 filter-chip-row와 개수 배지는 이 프레임에서 숨김.
모바일 활성 탭: "시약". 위→아래: nav-pill → (교사·admin) msds-bulk-banner → segmented-control "전체 / 재고 부족" → 검색 줄(text-input + 오른쪽 list-filter-button) → (필터 적용 시) filter-chip-row → reagent-row 목록 → tab-bar. 좌우 여백 16, 행 사이 12.
데스크탑: nav-pill 아래 가운데 단일 열 같은 순서, tab-bar 없음.
### 구성 요소
- nav-pill: "Lab_Stock" 워드마크 + 현재 학교명 "샘플고등학교" + 학교명 옆 nav-account-menu ▾. 데스크탑 섹션 링크("시약 목록", 교사·admin에게만 "재주문 알림"). 학교 전환 기능 없음. 하늘색: 데스크탑 현재 섹션 링크("시약 목록") 아래 #2b9fe0 밑줄(글자 #141414)
- nav-account-menu: 학교명 옆 ▾, 메뉴 항목 "로그아웃" 1개. 하늘색 없음
- msds-bulk-banner: nav-pill 바로 아래·segmented-control 위 한 줄 전폭 띠(모바일 x 0, 폭 390, rounded 0, #e6f4fc 채움, 안쪽 여백 12·16). 왼쪽 body-sm #141414 "MSDS 없는 시약 4종", 오른쪽 button-pill-soft "한 번에 찾기"(높이 44 이상). 누르면 기존 상태 화면 2-msds-bulk. MSDS 없는 시약이 0종이면 숨김. 하늘색: 띠 채움 #e6f4fc (교사·admin만)
- button-pill-soft: msds-bulk-banner 안 "한 번에 찾기"(#f3f3f3 채움, 라벨 #141414, rounded 9999). 하늘색 없음 (교사·admin만)
- segmented-control: 리스트 위 "전체 / 재고 부족", 한 번에 하나. 필터와 따로 동작하고 둘 다 결과에 적용된다
- segmented-control-active: 선택 옵션 흰 pill("전체"). 하늘색: 1px #2b9fe0 테두리(글자 #141414)
- text-input: 검색 줄 왼쪽 "시약명 검색"(#f0f0f0, rounded 16, 포커스 링 2px #141414). 오른쪽 list-filter-button 자리만큼 줄어든 폭(사이 8). 하늘색: 검색 아이콘 #2b9fe0
- list-filter-button: 검색 text-input 오른쪽 button-pill-soft "필터"(#f3f3f3 채움, 왼쪽 필터 아이콘, 라벨 #141414 link, rounded 9999, 높이 44 이상). 누르면 상태 화면 2-filter의 list-filter-sheet. 필터가 적용되면 라벨 오른쪽에 개수 pill(예 "2", #e6f4fc 채움 + 1px #2b9fe0 테두리, label #141414, rounded 9999). 이 프레임은 적용 없음이라 개수 pill 숨김. 하늘색: 필터 아이콘 #2b9fe0 (개수 pill 규칙은 적용 시)
- filter-chip-row: 필터가 하나 이상 적용됐을 때만 검색 줄 아래·목록 위에 나타나는 가로 스크롤 한 줄(적용 칩 #f3f3f3 pill + × / 조용한 텍스트 동작 "모두 지우기" / 오른쪽 caption "12종"). 이 프레임에서는 숨김 — 모양은 상태 화면 2-filter·2-filter-empty
- reagent-row: 시약 한 줄 = 시약명(title) + 재고량·단위(body) + 입고일(caption #707070), #f3f3f3, rounded 16, 행 사이 12. 누르면 화면 3. 정렬 기본 = 이름순. 하늘색: 오른쪽 › 아이콘 #2b9fe0, 누른 행 배경 #e6f4fc
- badge-low-stock: 재고 부족 행 시약명 옆 "재고 부족"(#d6246a 채움, #ffffff label, rounded 9999). 하늘색 없음
- ex-empty-state-card: 필터 없이 검색만으로 결과 0건일 때 "찾는 시약이 없어요". 필터가 적용된 0건은 상태 화면 2-filter-empty. 하늘색: 안내 아이콘 #2b9fe0
- tab-bar: 모바일 전용 하단 탭바 1개(x 0, 폭 390, 높이 64, y 780~844, rounded 0, #ffffff + 위쪽 1px #f0f0f0 선, 그림자 없음, tab-item 4개 같은 폭). 데스크탑에는 두지 않는다. 하늘색: 활성 tab-item 아이콘 #2b9fe0만
- tab-item: "홈" · "시약" · "QR 스캔" · "기록" 4개, 사각형 누름 영역(rounded 0), 높이 48, 아이콘 위 + label 아래. 활성 = "시약"(#2b9fe0 아이콘 + 라벨 #141414), 비활성 3개 #707070
### 반영한 레퍼런스
- https://uibowl.io/name/%EB%B3%BC%ED%8A%B8%EC%97%85?patterns=%ED%95%84%ED%84%B0&imgId=cmojep21l001hjs04hvksxikk
- https://uibowl.io/name/%EC%B9%B4%EC%B9%B4%EC%98%A4%EA%B3%A8%ED%94%84%EC%98%88%EC%95%BD?patterns=%ED%95%84%ED%84%B0&imgId=cmtwlv9y9002eky04rfw0ikms

## 상태 화면 2-filter
화면 2에서 "필터"를 눌러 list-filter-sheet가 열린 상태(프레임 2-filter-mobile · 2-filter-desktop). 모든 역할 같다(교사·admin은 뒤 화면에 msds-bulk-banner가 함께 보인다).
예시 상태: 이미 보관 분류 "산" 1개가 적용되어 목록이 12종(뒤 화면 filter-chip-row "산 ×" · "12종", list-filter-button 개수 "1"). 사용자가 시트를 다시 열어 정렬을 "재고 적은 순"으로 바꾸고 보관 분류 "산화제"를 더 고른 상태 → 하단 "18종 보기". 보관 위치는 "모든 시약장", "칸 없음만"·"MSDS 없는 시약만" 토글은 꺼짐.
모바일 = tab-bar 위 바텀시트(딤 없음, 뒤 화면은 화면 2 그대로). 데스크탑 = list-filter-button 바로 아래 드롭다운 패널(폭 400, 오른쪽 끝을 버튼에 맞춤).
### 구성 요소
- nav-pill: 화면 2 nav-pill 그대로 — "Lab_Stock" + 현재 학교명 "샘플고등학교" + nav-account-menu ▾. 하늘색: 데스크탑 "시약 목록" 밑줄 #2b9fe0
- nav-account-menu: 학교명 옆 ▾(닫힌 상태)
- msds-bulk-banner: 시트 뒤 띠 "MSDS 없는 시약 4종"(#e6f4fc, 누름 동작 없음) (교사·admin만)
- segmented-control: 시트 뒤 "전체 / 재고 부족"(누름 동작 없음)
- segmented-control-active: 시트 뒤 선택 옵션 "전체" 흰 pill. 하늘색: 1px #2b9fe0 테두리(글자 #141414)
- text-input: 시트 뒤 검색 "시약명 검색"(#f0f0f0, rounded 16). 하늘색: 검색 아이콘 #2b9fe0
- list-filter-button: 시트 뒤 "필터" + 개수 pill "1"(#e6f4fc 채움 + 1px #2b9fe0 테두리, label #141414, rounded 9999) — 저장 전이라 이미 적용된 개수. 하늘색: 필터 아이콘 #2b9fe0, 개수 pill 채움·테두리
- filter-chip-row: 시트 뒤 검색 줄 아래 한 줄. 적용 칩 "산 ×"(#f3f3f3 채움, label #141414, rounded 9999, × 누름 영역 44 이상) → 조용한 텍스트 동작 "모두 지우기"(link #141414, 채움·테두리 없음) → 줄 오른쪽 끝 caption(#707070) "12종". 칩이 많으면 가로 스크롤. 하늘색 없음
- reagent-row: 시트 뒤 "산" 필터 결과 행(누름 동작 없음), #f3f3f3, rounded 16. 하늘색 없음
- badge-low-stock: 시트 뒤 재고 부족 행(염산 · 1병) 시약명 옆 "재고 부족"(#d6246a 채움, #ffffff label). 하늘색 없음
- list-filter-sheet: 시트 1개(#ffffff, 1px #e0e0e0 테두리, 모바일 위쪽 rounded 24 / 데스크탑 rounded 24, 여백 24, 오른쪽 위 × 닫기). 위→아래, 구역 사이 24: ① 제목 heading-3 "필터" → ② 구역 "정렬"(heading-4) + 한 줄 pill 3개 "이름순"(기본) · "재고 적은 순" · "최근 입고순", 한 번에 하나, 선택 = "재고 적은 순" → ③ 구역 "보관 분류"(heading-4) + 오른쪽 caption(#707070) "여러 개 고를 수 있어요" + storage-class-chip 9개 줄바꿈 배치 → ④ 구역 "보관 위치"(heading-4) + 시약장 선택 상자(text-input 모양, 값 "모든 시약장" ▾, 목록 = "모든 시약장" · cabinet-number(1) "1번 시약장" · cabinet-number(2) "2번 시약장") → 그 아래 칸 선택 상자(값 "모든 칸" ▾, 시약장을 고르기 전에는 비활성 #adadad) → 토글 줄 "칸 없음만"(body #141414 + 오른쪽 토글, 꺼짐) → ⑤ 토글 줄 "MSDS 없는 시약만"(꺼짐, 켜고 적용하면 교사·admin 목록 위에 msds-bulk-banner가 함께 보임) → ⑥ 하단 고정 줄(위 1px #f0f0f0 선, 위 여백 16): 왼쪽 좁은 button-outline "초기화" + 오른쪽 넓은 button-primary "18종 보기"(비율 1:2, 사이 8). 시트 안은 스크롤되고 하단 줄은 고정. 결과가 0종이면 "0종 보기"로 보이고 누르면 상태 화면 2-filter-empty. 정렬 pill·토글: 미선택 pill = #f3f3f3 채움, 라벨 #141414, rounded 9999, 높이 44 이상 / 토글 꺼짐 = #e0e0e0 트랙 + #ffffff 손잡이, 켜짐 = #2b9fe0 트랙 + #ffffff 손잡이. 하늘색: 선택 정렬 pill #e6f4fc 채움 + 1px #2b9fe0 테두리(글자 #141414), 선택 상자 ▾ 아이콘 #2b9fe0, 토글 켜짐 트랙
- storage-class-chip: list-filter-sheet "보관 분류" 칩 9개 — "유기" · "산" · "염기" · "산화제" · "인화성" · "무기염" · "독성" · "기타" · "분류 없음". 여러 개 선택. 미선택 = #f3f3f3 채움, label #141414, rounded 9999, 높이 44 이상. 선택 = "산"·"산화제". 핑크 없음(혼재 경고가 아니다). 하늘색: 선택 칩 #e6f4fc 채움 + 1px #2b9fe0 테두리(글자 #141414)
- cabinet-number: 보관 위치 시약장 목록의 이름 앞 작은 원(#ffffff, 1px #e0e0e0, rounded 9999) 안 숫자 "1"·"2"(label #141414). 핑크·하늘색 글자 없음
- button-outline: 시트 하단 "초기화"(#ffffff, 1px #e0e0e0, 라벨 #141414, rounded 9999, 높이 44 이상) — 누르면 시트 안 선택이 기본값(이름순, 분류·위치·토글 없음)으로 돌아간다. 하늘색 없음
- button-primary: 시트 하단 "18종 보기"(#141414 채움, #ffffff 글자, rounded 9999, 높이 44 이상) — 누르면 시트가 닫히고 목록·filter-chip-row("산 ×" · "산화제 ×" · "18종")·개수 pill "2"가 바뀐다. 정렬 바꾸기는 칩으로 세지 않는다. 하늘색 없음
- tab-bar: 모바일 전용 하단 탭바 1개(화면 2와 같음). 시트는 이 바 위쪽 선 위에 붙는다. 데스크탑에는 두지 않는다. 하늘색: 활성 tab-item 아이콘 #2b9fe0만
- tab-item: 4개 "홈" · "시약" · "QR 스캔" · "기록". 활성 = "시약"
### 반영한 레퍼런스
- https://uibowl.io/name/%EC%B9%B4%EC%B9%B4%EC%98%A4%EA%B3%A8%ED%94%84%EC%98%88%EC%95%BD?patterns=%ED%95%84%ED%84%B0&imgId=cmtwlv9y9002eky04rfw0ikms
- https://uibowl.io/name/Kia?patterns=%ED%95%84%ED%84%B0&imgId=cmpurx7l00005kt04fgdc2lvh
- https://uibowl.io/name/%EB%B3%BC%ED%8A%B8%EC%97%85?patterns=%ED%95%84%ED%84%B0&imgId=cmojep21l001hjs04hvksxikk
- https://uibowl.io/name/%ED%94%8C%EB%A6%AC%EB%8D%94%EC%8A%A4?patterns=%ED%95%84%ED%84%B0&imgId=cmubb0zcz0038l404q4aoyftn

## 상태 화면 2-filter-empty
적용한 필터에 맞는 시약이 0종인 상태(프레임 2-filter-empty-mobile · 2-filter-empty-desktop). 모든 역할 같다. 핑크 없음 — 재고 부족이 아니다.
예시 상태: 보관 분류 "독성" + 보관 위치 "2번 시약장" 적용 → 0종. list-filter-button 개수 "2". 목록 자리에 빈 상태 카드.
### 구성 요소
- nav-pill: 화면 2 nav-pill 그대로 — "Lab_Stock" + 현재 학교명 "샘플고등학교" + nav-account-menu ▾. 하늘색: 데스크탑 "시약 목록" 밑줄 #2b9fe0
- nav-account-menu: 학교명 옆 ▾(닫힌 상태)
- msds-bulk-banner: 화면 2와 같은 띠 "MSDS 없는 시약 4종" + "한 번에 찾기"(학교 전체 기준이라 필터 결과와 상관없이 보임). 하늘색: 띠 채움 #e6f4fc (교사·admin만)
- segmented-control: "전체 / 재고 부족", 선택 = "전체"
- segmented-control-active: "전체" 흰 pill. 하늘색: 1px #2b9fe0 테두리(글자 #141414)
- text-input: 검색 "시약명 검색"(빈 값, #f0f0f0, rounded 16). 하늘색: 검색 아이콘 #2b9fe0
- list-filter-button: "필터" + 개수 pill "2"(#e6f4fc 채움 + 1px #2b9fe0 테두리, label #141414). 누르면 list-filter-sheet(2-filter와 같은 시트, 지금 조건이 선택된 채). 하늘색: 필터 아이콘 #2b9fe0, 개수 pill 채움·테두리
- filter-chip-row: 검색 줄 아래 한 줄. 적용 칩 "독성 ×" · "cabinet-number(2) 2번 시약장 ×"(#f3f3f3 채움, label #141414, rounded 9999, × 누름 영역 44 이상) → "모두 지우기"(link #141414) → 오른쪽 끝 caption(#707070) "0종". 하늘색 없음
- cabinet-number: "2번 시약장" 칩 안 이름 앞 작은 원(#ffffff, 1px #e0e0e0) 안 숫자 "2"(label #141414). 핑크·하늘색 글자 없음
- ex-empty-state-card: 목록 자리 가운데 카드(#ffffff, 1px #f0f0f0 테두리, rounded 24, 여백 24). #141414 안내 아이콘 → heading-4 "조건에 맞는 시약이 없어요" → body-sm(#707070) "칩을 하나씩 빼거나 필터를 지워 보세요" → button-outline "필터 지우기". 핑크 없음. 하늘색 없음(아이콘 #141414)
- button-outline: 빈 상태 카드 안 "필터 지우기"(#ffffff, 1px #e0e0e0, 라벨 #141414, rounded 9999, 높이 44 이상) — 누르면 모든 필터가 빠지고 화면 2(42종)로. 정렬은 그대로 둔다. 하늘색 없음
- tab-bar: 모바일 전용 하단 탭바 1개(화면 2와 같음). 데스크탑에는 두지 않는다. 하늘색: 활성 tab-item 아이콘 #2b9fe0만
- tab-item: 4개 "홈" · "시약" · "QR 스캔" · "기록". 활성 = "시약"
### 반영한 레퍼런스
- https://uibowl.io/name/%EC%98%A4%EC%9D%BC%EB%82%98%EC%9A%B0?patterns=%EA%B2%80%EC%83%89&imgId=cmtpnvoci000rlh04frsnnhkt
- https://uibowl.io/name/%EB%B3%BC%ED%8A%B8%EC%97%85?patterns=%ED%95%84%ED%84%B0&imgId=cmojep21l001hjs04hvksxikk

## 화면 4
사용 기록 입력. 학생·교사·admin 모두 들어온다(화면 3 "사용 기록", 홈 quick-action "사용 기록 입력"). 기존 "사용 날짜" 입력을 usage-date "사용일"로 바꿔 사용량 바로 아래로 옮긴다. 기본 = 오늘, 오늘 이후는 고를 수 없다.
예시 상태: 에탄올(현재 재고 1,200 mL), 사용량 50 mL 입력, 사용일 = 오늘 "2026-10-07"(그래서 past-date-note 숨김).
모바일 활성 탭: "기록". 위→아래: nav-pill → reagent-detail-card → 폼(사용량 → 사용일 → 사용자 → 메모) → 하단 전폭 "사용 기록 저장" → tab-bar. 좌우 여백 16, 입력 사이 16.
데스크탑: nav-pill 아래 가운데 단일 열 같은 순서, tab-bar 없음.
### 구성 요소
- nav-pill: 뒤로가기(화면 3) + 제목 "사용 기록" + 현재 학교명 "샘플고등학교" + 학교명 옆 nav-account-menu ▾. 데스크탑 섹션 링크("시약 목록", 교사·admin에게만 "재주문 알림"). 하늘색: 뒤로가기 아이콘 #2b9fe0, 데스크탑 "시약 목록" 밑줄 #2b9fe0
- nav-account-menu: 학교명 옆 ▾, 메뉴 항목 "로그아웃" 1개. 하늘색 없음
- reagent-detail-card: 폼 위 요약(#ffffff, 1px #f0f0f0 테두리, rounded 24, 여백 24). 시약명 "에탄올"(title) + 현재 재고 "1,200 mL"(body). 재고 부족 배지는 두지 않는다. 하늘색 없음
- text-input: 라벨 위·입력 아래 세로 폼. "사용량"(필수) 숫자 입력 + 단위 칩(병·mL·g, 선택 "mL"), "사용자"(필수, 로그인한 사용자 이름 기본값), "메모". 필수 라벨 옆 caption "필수"(#707070). #f0f0f0, rounded 16, 포커스 링 2px #141414. 하늘색: 단위 칩 선택 상태 #e6f4fc + 1px #2b9fe0 테두리(글자 #141414)
- usage-date: 사용량 바로 아래 날짜 입력 1개. 라벨 "사용일"(필수) + text-input 모양 날짜 칸(#f0f0f0, rounded 16, 값 "2026-10-07", 오른쪽 달력 아이콘) — 화면 7 입고일과 같은 모양. 누르면 날짜 고르기 시트(tab-bar 위, × 닫기)가 오늘이 선택된 채 열리고, 오늘 이후 날짜는 흐리게(#adadad, 누름 없음), 하단 button-primary "완료"로 확정하면 칸 값만 바뀐다(폼 하단 저장 버튼은 그대로). 오늘이 아닌 날을 고르면 past-date-note가 나타난다(상태 화면 4-past-date). 하늘색: 달력 아이콘 #2b9fe0, 시트 안 선택 날짜 원 #e6f4fc + 1px #2b9fe0 테두리(숫자 #141414)
- button-primary: 하단 전폭 "사용 기록 저장"(#141414 채움, #ffffff 글자, rounded 9999, 높이 44 이상, 모바일 tab-bar 바로 위). 사용량·사용일·사용자가 비면 비활성. 학생·교사·admin 모두. usage-date 시트의 "완료"도 같은 모양. 하늘색 없음
- ex-toast: 저장 직후 "사용 기록을 저장했어요"(오늘 사용일 때), 이후 화면 3 "사용 기록" 탭으로. 모바일은 tab-bar 위. 하늘색: 완료 체크 아이콘 #2b9fe0
- tab-bar: 모바일 전용 하단 탭바 1개(화면 2와 같은 규격). 하단 저장 버튼은 이 바 위에 쌓는다. 데스크탑에는 두지 않는다. 하늘색: 활성 tab-item 아이콘 #2b9fe0만
- tab-item: "홈" · "시약" · "QR 스캔" · "기록" 4개. 활성 = "기록"(#2b9fe0 아이콘 + 라벨 #141414), 비활성 3개 #707070
### 반영한 레퍼런스
- https://uibowl.io/name/%EB%83%89%EC%9E%A5%EA%B3%A0%ED%84%B8%EA%B8%B0?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&imgId=cmohwpkck001bl2044p9wk6ef
- https://uibowl.io/name/%ED%82%A4%ED%94%BC%EB%9F%BD?patterns=%EB%A9%94%EC%9D%B8&imgId=cmow8tk98000el704gib8a8ij

## 상태 화면 4-past-date
사용일을 오늘이 아닌 지난 날로 고른 상태(프레임 4-past-date-mobile · 4-past-date-desktop). 모든 역할 같다. 핑크 없음 — 결정이 필요한 신호가 아니라 확인 안내다.
예시 상태: 에탄올, 사용량 50 mL, 사용일 "2026-10-03"(날짜 고르기 시트에서 "완료"를 누른 뒤, 시트는 닫힘). 저장 버튼 바로 위에 안내 한 줄.
### 구성 요소
- nav-pill: 화면 4 nav-pill 그대로 — 뒤로가기 + "사용 기록" + 현재 학교명 "샘플고등학교" + nav-account-menu ▾. 하늘색: 뒤로가기 아이콘 #2b9fe0
- nav-account-menu: 학교명 옆 ▾(닫힌 상태)
- reagent-detail-card: 폼 위 요약 "에탄올" + "1,200 mL". 하늘색 없음
- text-input: "사용량" 50 + 단위 칩 "mL", "사용자"(기본값), "메모"(#f0f0f0, rounded 16). 하늘색: 단위 칩 선택 상태 #e6f4fc + 1px #2b9fe0 테두리(글자 #141414)
- usage-date: 사용량 아래 "사용일"(필수) 날짜 칸, 값 "2026-10-03"(#f0f0f0, rounded 16, 오른쪽 달력 아이콘). 다시 누르면 날짜 고르기 시트가 10월 3일이 선택된 채 열린다(오늘 이후 흐림). 하늘색: 달력 아이콘 #2b9fe0
- past-date-note: 저장 버튼 바로 위(버튼 위 간격 8) 무채색 안내 한 줄. 왼쪽 작은 달력 아이콘 #707070 + body-sm #707070 "10월 3일 사용으로 기록해요". 채움·테두리 없음. 사용일을 오늘로 되돌리면 사라진다. 핑크·하늘색 없음
- button-primary: 하단 전폭 "사용 기록 저장"(#141414 채움, #ffffff 글자, rounded 9999, 높이 44 이상, 모바일 tab-bar 바로 위). 지난 날이어도 바로 저장된다(추가 확인 없음). 저장 뒤 ex-toast "10월 3일 사용 기록을 저장했어요". 하늘색 없음
- tab-bar: 모바일 전용 하단 탭바 1개(화면 4와 같음). 데스크탑에는 두지 않는다. 하늘색: 활성 tab-item 아이콘 #2b9fe0만
- tab-item: 4개 "홈" · "시약" · "QR 스캔" · "기록". 활성 = "기록"
### 반영한 레퍼런스
- https://uibowl.io/name/%EB%A9%94%EA%B0%80MCG%EC%BB%A4%ED%94%BC?patterns=%EB%82%B4%EC%97%AD&imgId=cmt6me0kb000gl804oncd5vge
- https://uibowl.io/name/%ED%82%A4%ED%94%BC%EB%9F%BD?patterns=%EB%A9%94%EC%9D%B8&imgId=cmow8tk98000el704gib8a8ij

## 화면 10
사용 기록 내역. 학생·교사·admin 모두 들어온다. 같은 학교(샘플고등학교)의 사용 기록만 보인다. 기록은 사용일로 묶고 사용일 최신순으로 정렬한다(같은 날 안에서는 기록 시각 최신순). 기록한 날이 사용일과 다를 때만 행 아래 회색 캡션 "{M}월 {D}일에 기록"을 붙인다.
예시 상태: "전체", 기간 "최근 1개월". 그룹 3개 —
① "10월 7일 · 오늘": 염산 · 학생 이OO · 14:05 · 20 mL / 질산은 · 교사 김OO · 10:20 · 2 g
② "10월 6일": 수산화나트륨 · 학생 박OO · 15:40 · 10 g
③ "10월 3일": 에탄올 · 교사 김OO · 50 mL + 캡션 "10월 7일에 기록" / 염산 · 학생 최OO · 30 mL + 캡션 "10월 6일에 기록"
모바일 활성 탭: "기록". 위→아래: nav-pill → segmented-control "전체 / 내 기록" + 기간 선택 → 검색 → 사용일 그룹 목록 → tab-bar. 좌우 여백 16.
데스크탑: nav-pill 아래 가운데 단일 열 같은 순서, tab-bar 없음.
### 구성 요소
- nav-pill: "Lab_Stock" 워드마크 + 제목 "사용 기록 내역" + 현재 학교명 "샘플고등학교" + 학교명 옆 nav-account-menu ▾. 하늘색: 데스크탑 현재 섹션 링크("사용 기록 내역") 밑줄 #2b9fe0(글자 #141414)
- nav-account-menu: 학교명 옆 ▾, 메뉴 항목 "로그아웃" 1개. 하늘색 없음
- segmented-control: 목록 위 "전체 / 내 기록", 한 번에 하나
- segmented-control-active: 선택 옵션 "전체" 흰 pill. 하늘색: 1px #2b9fe0 테두리(글자 #141414)
- text-input: segmented-control 오른쪽 기간 선택 상자("최근 1개월" ▾, 사용일 기준)와 그 아래 "시약명 검색"(#f0f0f0, rounded 16, 포커스 링 2px #141414). 하늘색: 검색 아이콘·▾ 아이콘 #2b9fe0
- ex-data-table-cell: 기록 목록. 사용일 그룹 헤더(caption #707070, "10월 7일 · 오늘" / "10월 6일" / "10월 3일", 그룹 사이 24) 아래 그날의 행. 행 = 왼쪽 위 시약명(title #141414) + 그 아래 보조줄 body-sm(#707070) "학생 이OO · 14:05"(사용자 · 기록 시각) + 오른쪽 사용량·단위(body #141414). 기록한 날이 사용일과 다르면 보조줄 아래에 caption(#707070) 한 줄 "10월 7일에 기록"을 더하고, 이때 보조줄은 사용자 이름만. 행 사이 구분은 여백 12(구분선 없음). 행을 누르면 ex-modal-card 상세. 하늘색: 누른 행 배경 #e6f4fc, 그룹 헤더 왼쪽 #2b9fe0 짧은 인디케이터
- ex-modal-card: 기록 상세 시트(모바일 tab-bar 위, × 닫기). 시약명(heading-3) + 사용량(display) → 라벨-값 행 "사용자" · "사용일" · "기록한 날"(사용일과 다를 때만, 예 "2026-10-07 09:12") · "메모" → msds-entry → button-outline "닫기". 하늘색 없음
- msds-entry: 상세 시트 안 button-pill-soft "MSDS 보기 ↗"(#f3f3f3, 라벨 #141414, rounded 9999, 높이 44 이상). 학생·교사·admin 모두. 하늘색: ↗ 아이콘 #2b9fe0
- button-outline: 상세 시트 "닫기"(#ffffff, 1px #e0e0e0, 라벨 #141414, rounded 9999, 높이 44 이상)
- ex-empty-state-card: 필터·기간 결과 0건일 때 "아직 사용 기록이 없어요". 하늘색: 안내 아이콘 #2b9fe0
- tab-bar: 모바일 전용 하단 탭바 1개(화면 2와 같은 규격). 목록 스크롤은 이 바 위쪽 선에서 끝난다. 데스크탑에는 두지 않는다. 하늘색: 활성 tab-item 아이콘 #2b9fe0만
- tab-item: "홈" · "시약" · "QR 스캔" · "기록" 4개. 활성 = "기록"(#2b9fe0 아이콘 + 라벨 #141414), 비활성 3개 #707070
### 반영한 레퍼런스
- https://uibowl.io/name/%EB%AF%B8%EB%8B%88%EC%8A%A4%ED%83%81?patterns=%EB%82%B4%EC%97%AD&imgId=cmty2l8bh002gl404x15qm1dq
- https://uibowl.io/name/%ED%86%A0%EC%8A%A4%EC%A6%9D%EA%B6%8C?patterns=%EB%82%B4%EC%97%AD&imgId=cmrufrdyn0003jj04z74mofuh
- https://uibowl.io/name/%EB%B9%BD%EB%8B%A4%EB%B0%A9?patterns=%EB%82%B4%EC%97%AD&imgId=cmsqropcg0006jr04p2xixv13
- https://uibowl.io/name/%EB%8B%A5%ED%84%B0%EB%8B%A4%EC%9D%B4%EC%96%B4%EB%A6%AC?patterns=%ED%8F%AC%EC%9D%B8%ED%8A%B8&imgId=cmr7eca84000qk404rcsp3efe

## 역할별 노출
앱 전체(화면 1~13) 기준 개수. runs/20261007-0002 표를 기준으로 이번 변경을 반영했다. 같은 화면의 상태 화면에 다시 나오는 같은 컴포넌트는 그 화면 1개로 센다.
msds-entry = 화면 3 1 + 화면 10 상세 1 → 학생·교사·admin 모두 2(화면 2 목록에는 msds-entry 없음, R4 학생 ≥ 1 충족).
msds-bulk-banner = 화면 2 1(2-filter·2-filter-empty에 다시 나와도 같은 띠, 교사·admin만, 학생 0 — R5). 나머지 행은 runs/20261007-0002 값 그대로.
list-filter-button·list-filter-sheet·filter-chip-row·storage-class-chip·usage-date·past-date-note는 모든 역할에 같고 rules.json roles 대상이 아니라 표에 넣지 않는다(새 역할 규칙 없음).

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
