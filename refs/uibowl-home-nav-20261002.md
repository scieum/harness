# uibowl 비교 조사 — 홈 내비게이션 (A안 상단 nav-pill + 홈 바로가기 그리드 vs B안 하단 탭바)

- 조사일: 2026-10-02 · 하네스 실행 밖 비교 조사 (사용자 요청)
- 대상: Lab_Stock 홈 화면 (모바일 웹/반응형, 교사·학생·admin)
- 출처: uibowl 검색 결과의 ui_url만 사용. 대표 이미지를 직접 본 항목만 넣었다.
- 사용한 검색: search_components(하단 네비게이션 × 메인, 비즈니스툴/교육&도서), search_components(플로팅 버튼+하단 네비게이션 × 메인), search_components(하단 네비게이션 × 간편결제), search_ui_patterns(메인 × 비즈니스툴, 1~7페이지), search_by_ocr_text(스캔 / QR / 바코드 / 바로가기 / 자주 쓰는 × 메인)
- 표기: "업무형" = uibowl 분류 비즈니스툴 + 교육&도서

## 1. 하단 탭바 4~5개 홈 화면

| 앱 | ui_url | 관찰(탭 구성·위치·강조 방식) |
|---|---|---|
| 페이워크 (비즈니스툴) | https://uibowl.io/name/%ED%8E%98%EC%9D%B4%EC%9B%8C%ED%81%AC?patterns=%EB%A9%94%EC%9D%B8&imgId=cmtzo55qv002rl7047rsl7n07 | 탭 5개: 홈/문서함/사업 관리/정산 내역/더보기. 가운데 강조 없음. 활성 탭은 아이콘·라벨 색만 바뀜. 상단은 프로필+회사명+알림 아이콘 헤더 |
| 페이히어 (비즈니스툴, POS) | https://uibowl.io/name/%ED%8E%98%EC%9D%B4%ED%9E%88%EC%96%B4?patterns=%EB%A9%94%EC%9D%B8&imgId=cmnfmxnhh0003l8045z9h1r15 | 탭 4개: 홈/나의 매장/혜택/더보기. 가운데 강조 없음. 활성 탭은 아이콘·라벨이 진하게 바뀜. 상단은 사용자명+알림만 있는 얇은 헤더 |
| 시프티 (비즈니스툴, 근태) | https://uibowl.io/name/%EC%8B%9C%ED%94%84%ED%8B%B0?patterns=%EB%A9%94%EC%9D%B8&imgId=t2pbfghw1zvfsg1jdkzwf57a | 탭 5개: 홈/요청(숫자 배지)/근무일정/출퇴근기록/휴가. 어두운 단색 바, 활성 탭은 흰색. 상단은 햄버거+로고+알림. 홈 본문 첫 카드에 "출근하기" 주 버튼 |
| WeWork (비즈니스툴) | https://uibowl.io/name/WeWork%20(%EC%9C%84%EC%9B%8C%ED%81%AC)?patterns=%EB%A9%94%EC%9D%B8&imgId=cmgyp4xq2000ml104nd56ac8z | 탭 4개: 홈/내 예약/즐겨찾기/계정. 가운데 강조 없음. 활성 탭은 진한 아이콘·라벨. 탭바 바로 위에 "지도" 떠 있는 pill 버튼 |
| 아톡 (비즈니스툴, 업무 전화) | https://uibowl.io/name/%EC%95%84%ED%86%A1?patterns=%EB%A9%94%EC%9D%B8&imgId=cmi2lzams000ll2046f11gw1z | 탭 5개: 키패드/연락처/홈/통화목록/SMS. 홈이 가운데 자리이고 활성 색으로 표시. 별도로 키우거나 띄운 버튼은 없음 |
| 하이링구얼 (교육) | https://uibowl.io/name/%ED%95%98%EC%9D%B4%EB%A7%81%EA%B5%AC%EC%96%BC?patterns=%EB%A9%94%EC%9D%B8&imgId=cmnmkywio0003l804k22ndnyy | 탭 4개: 홈/단어장/피드/마이. 활성 탭은 진한 아이콘, 나머지는 흐린 회색. 주 동작("일기 작성하기")은 본문 전폭 버튼 |
| 스픽 (교육) | https://uibowl.io/name/%EC%8A%A4%ED%94%BD?patterns=%EB%A9%94%EC%9D%B8&imgId=cm8qwifdh001zjx0dm2sf6o9j | 탭 5개 (홈~프로필). 활성 탭은 아이콘·라벨 색 강조. 탭바 바로 위에 AI 대화 입력 바가 떠 있음 |
| 플랭 (교육) | https://uibowl.io/name/%ED%94%8C%EB%9E%AD?patterns=%EB%A9%94%EC%9D%B8&imgId=cmsu92dhj0003l204u6asw7pr | 탭 5개: 홈/AI 라이브챗/복습/리포트/챌린지. 활성 탭은 아이콘·라벨 색. 홈 본문 주 동작은 "오늘의 학습 시작하기" 전폭 버튼 |
| 컴포즈 (음식, 일반) | https://uibowl.io/name/%EC%BB%B4%ED%8F%AC%EC%A6%88?patterns=%EB%A9%94%EC%9D%B8&imgId=cmt6pefrh0007jr04bxkav8um | 탭 5개: 홈/카드/주문/기프트샵/더보기. 가운데 "주문"을 바 위로 솟은 원형 버튼으로 강조 |
| 써브웨이 (음식, 일반) | https://uibowl.io/name/%EC%8D%A8%EB%B8%8C%EC%9B%A8%EC%9D%B4?patterns=%EA%B0%84%ED%8E%B8%EA%B2%B0%EC%A0%9C&imgId=cmpb02p2l000xl7045gj02luo | 탭 5개: 홈/마이/주문/선물/더보기. 가운데 "주문"을 솟은 원형 버튼으로 강조. (홈이 아니라 카드충전 화면에서 확인) |

## 2. 상단 바/헤더 + 홈 본문 바로가기 그리드 (하단 탭바 유무 함께 표시)

| 앱 | ui_url | 관찰(탭 구성·위치·강조 방식) |
|---|---|---|
| 미리캔버스 (비즈니스툴) | https://uibowl.io/name/%EB%AF%B8%EB%A6%AC%EC%BA%94%EB%B2%84%EC%8A%A4?patterns=%EB%A9%94%EB%89%B4&imgId=cme13yq73000ll807aga2cnnr | 상단은 헤더 대신 검색 바. 바로 아래 5×2 아이콘 그리드(카테고리). 하단 탭바 있음, 4개: 홈/프로젝트/마이/새 디자인. 오른쪽 끝 "새 디자인"만 + 사각 아이콘으로 강조 |
| CapCut (비즈니스툴, 글로벌) | https://uibowl.io/name/CapCut?patterns=%EB%A9%94%EC%9D%B8&imgId=cmde00ppo0009l707xdib8e2n | 상단은 히어로 배너. 본문에 큰 "New project" 카드와 4×2 도구 그리드("All tools" 칸 포함). 하단 탭바 있음, 4개: Edit/Templates/Library/Me |
| Kia (모빌리티) | https://uibowl.io/name/Kia?patterns=%EB%A9%94%EC%9D%B8&imgId=cmpur0a2f000bl504w62hm2jr | 헤더: 로고 + 스캔 아이콘 + 알림 + 프로필. 본문에 "서비스 바로가기" 카드(4칸, 편집, 페이지 점 표시). 하단 탭바 있음, 5개: 홈/지도/제어/스토어/마이카 |
| 마이현대 (모빌리티) | https://uibowl.io/name/%EB%A7%88%EC%9D%B4%ED%98%84%EB%8C%80?patterns=%EB%A9%94%EC%9D%B8&imgId=cmojm2eh50003lb0481vxr81l | 헤더: 로고 + 바코드 아이콘 + 알림. 본문 중간에 "서비스 바로가기"(편집 가능) 섹션. 하단 탭바 있음, 5개: 홈/샵/제어/서비스/마이 |
| G car (모빌리티) | https://uibowl.io/name/G%20car?patterns=%EB%A9%94%EC%9D%B8&imgId=cmo84yk8i000ejy04g6sliwuv | 헤더: 로고 + 쿠폰 + 알림. 본문에 큰 카드 그리드(왕복 예약/오다/편도…)와 "원클릭 바로가기" 가로 줄. 하단 탭바 있음, 4개: 이동하기/콘텐츠/혜택찾기/마이 |
| 이지태스크 (비즈니스툴) | https://uibowl.io/name/%EC%9D%B4%EC%A7%80%ED%83%9C%EC%8A%A4%ED%81%AC?patterns=%EB%A9%94%EC%9D%B8&imgId=cm8piebx80009jl0dyphle7sr | 하단 탭바 없음. 헤더: 햄버거 + 로고 + 알림 + 오른쪽 위 주 버튼 "업무 맡기기". 본문은 바로가기 그리드 없이 "나의 업무" 세그먼트+목록. 오른쪽 아래 상담 FAB |
| 테라핏 (비즈니스툴) | https://uibowl.io/name/%ED%85%8C%EB%9D%BC%ED%95%8F?patterns=%EB%A9%94%EC%9D%B8&imgId=gaiaay76akidnyryvue7povb | 하단 탭바 없음. 대신 상단에 텍스트 탭 4개(테라핏 홈/예약 내역/측정 내역/회원 정보, 밑줄로 활성 표시). 섹션 제목 옆에 "새 예약" 버튼 |
| 에어팝 (비즈니스툴, 출입 인증) | https://uibowl.io/name/%EC%97%90%EC%96%B4%ED%8C%9D?patterns=%EB%A9%94%EC%9D%B8&imgId=x6kbpy4n8lyvl0hbceg4utyw | 하단 탭바 없음. 상단은 로고 + 햄버거만. 본문은 인증 카드 하나뿐인 단일 기능 앱 |
| 에스원 모바일카드 (비즈니스툴, 출입 인증) | https://uibowl.io/name/%EC%97%90%EC%8A%A4%EC%9B%90%20%EB%AA%A8%EB%B0%94%EC%9D%BC%EC%B9%B4%EB%93%9C?patterns=%EB%A9%94%EC%9D%B8&imgId=ecjuqrfh4r4quo2wrsjdkncj | 하단 탭바 없음. 헤더: 햄버거 + 제목 + 새로고침. 본문은 카드 한 장 + 테마 변경 버튼(단일 기능) |
| 메디코치 (운동&건강) | https://uibowl.io/name/%EB%A9%94%EB%94%94%EC%BD%94%EC%B9%98?patterns=%EB%A9%94%EC%9D%B8&imgId=cms8eal940047l204opy4iv4c | 캡처 범위 안에 하단 탭바 없음. 헤더: 로고 + 세그먼트(맞춤상담/약&약국) + 아이콘 2개. 본문 첫 카드가 검색창, 오른쪽 끝에 원형 QR 스캔 버튼이 붙어 있음 |

## 3. 하단 탭바 + 홈 퀵 메뉴 혼합형

| 앱 | ui_url | 관찰(탭 구성·위치·강조 방식) |
|---|---|---|
| 페이워크 (비즈니스툴) | https://uibowl.io/name/%ED%8E%98%EC%9D%B4%EC%9B%8C%ED%81%AC?patterns=%EB%A9%94%EC%9D%B8&imgId=cmtzo55qv002rl7047rsl7n07 | 본문 중간에 4×2 문서 그리드(견적서/거래명세서/영수증/청구서/발주서…), 그 아래 "품목 추가"와 "사진으로 문서 만들기" 버튼. 하단 탭 5개. 그리드는 "만들기" 동작, 탭은 "보관함/관리" 화면으로 역할이 나뉨 |
| 페이히어 홈 (비즈니스툴) | https://uibowl.io/name/%ED%8E%98%EC%9D%B4%ED%9E%88%EC%96%B4?patterns=%EB%A9%94%EC%9D%B8&imgId=cmnfmxnhh0003l8045z9h1r15 | 본문 하단에 4×2 아이콘 그리드(마지막 칸 "전체보기"). 하단 탭 4개 |
| 페이히어 나의 매장 (비즈니스툴) | https://uibowl.io/name/%ED%8E%98%EC%9D%B4%ED%9E%88%EC%96%B4?patterns=%EB%A9%94%EC%9D%B8&imgId=cmnfmxdij001fl204l8u0mu8b | 화면 맨 위에 4×2 그리드, 첫 칸이 "스캐너". 그리드 아래 매출 현황 요약. 하단 탭 4개 중 "나의 매장" 활성 |
| 아톡 (비즈니스툴) | https://uibowl.io/name/%EC%95%84%ED%86%A1?patterns=%EB%A9%94%EC%9D%B8&imgId=cmi2lzams000ll2046f11gw1z | "아톡 서비스" 4×2 그리드(편집 링크, 페이지 점 2개). 하단 탭 5개, 가운데가 홈 |
| 한패스 (금융) | https://uibowl.io/name/%ED%95%9C%ED%8C%A8%EC%8A%A4?patterns=%EB%A9%94%EC%9D%B8&imgId=cmq0n25ok006ajy04umovql9l | 지갑 카드 아래에 "QR 송금받기/QR 송금하기" 2분할 바, 그 아래 4칸 그리드(해외송금/국내송금/바코드 결제/통합 QR 결제). 하단 탭 5개(가운데 "혜택"에 배지). 오른쪽 아래 상담 FAB |
| yes24 (교육&도서) | https://uibowl.io/name/yes24?patterns=%EB%A9%94%EC%9D%B8&imgId=o2ch1kisvzd4goa462lm8b1q | 배너 아래 5×2 아이콘 그리드. 하단 탭 5개(홈/메뉴/검색/MY/최근 본) + 오른쪽 FAB |
| 헤이영 캠퍼스 (교육, 대학) | https://uibowl.io/name/%ED%97%A4%EC%9D%B4%EC%98%81%20%EC%BA%A0%ED%8D%BC%EC%8A%A4?patterns=%EB%A9%94%EC%9D%B8&imgId=cmmbj8sqh0004lh048k4kbkqd | 헤더: 학교 로고 + 채팅 + 알림. 첫 카드는 모바일 학생증, 안에 전폭 "QR" 버튼. 그 아래 "MY메뉴" 4칸. 하단 탭은 3개뿐(학사/혜택/전체 메뉴) + FAB(+) |
| 카카오T (모빌리티) | https://uibowl.io/name/%EC%B9%B4%EC%B9%B4%EC%98%A4T?patterns=%EB%A9%94%EB%89%B4&imgId=cmoaq6tuc000iju04mi7fpyit | 상황별 탭(이동할 때/운전할 때…) 안에 서비스 그리드 + "자주 쓰는 서비스" 줄(편집, 빈 칸 "추가"). 하단 탭 5개, 홈이 가운데 |

## 4. 스캔이 핵심인 앱의 스캔 버튼 위치

| 앱 | ui_url | 관찰(탭 구성·위치·강조 방식) |
|---|---|---|
| 페이히어 (POS, 비즈니스툴) | https://uibowl.io/name/%ED%8E%98%EC%9D%B4%ED%9E%88%EC%96%B4?patterns=%EB%A9%94%EC%9D%B8&imgId=cmnfmxdij001fl204l8u0mu8b | 위치 = 홈 그리드 첫 칸 "스캐너". 다른 그리드 칸과 크기 같음, 별도 강조 없음. 탭바에는 스캔 없음 |
| 한패스 (금융) | https://uibowl.io/name/%ED%95%9C%ED%8C%A8%EC%8A%A4?patterns=%EB%A9%94%EC%9D%B8&imgId=cmq0n25ok006ajy04umovql9l | 위치 = 홈 본문. 진한 띠에 "QR 송금받기/하기" + 그리드에 "바코드 결제/통합 QR 결제". 탭바(5개)에는 스캔 없음 |
| 하나카드 (금융, 간편결제) | https://uibowl.io/name/%ED%95%98%EB%82%98%EC%B9%B4%EB%93%9C?patterns=%EA%B0%84%ED%8E%B8%EA%B2%B0%EC%A0%9C&imgId=cmh1ig3nt0006l704vpbqemqi | 위치 = 탭바 가운데 "결제"(원형 아이콘으로 강조). 결제 화면 안에서는 헤더 오른쪽 "QR스캔" 텍스트 버튼 + 카드 아래 "QR/PC결제", "바코드" 버튼 |
| 페이코 (금융) | https://uibowl.io/name/%ED%8E%98%EC%9D%B4%EC%BD%94?patterns=%EA%B0%84%ED%8E%B8%EA%B2%B0%EC%A0%9C&imgId=cmupp0iwh000mlg04ybe0ldx2 | 위치 = 탭바 가운데 "결제"(5개 중 3번째, 활성 색). 결제 화면 상단 텍스트 탭에 "QR 결제" |
| L.POINT with L.PAY (적립) | https://uibowl.io/name/L.POINT%20with%20L.PAY?patterns=%EA%B0%84%ED%8E%B8%EA%B2%B0%EC%A0%9C&imgId=cltvfcb9p0052js0878sngw7u | 위치 = 탭바 가운데 "결제"(바코드 아이콘, 활성 색). 결제 화면 맨 위에 바코드 카드 |
| 바나프레소 (음식) | https://uibowl.io/name/%EB%B0%94%EB%82%98%ED%94%84%EB%A0%88%EC%86%8C?patterns=%EB%A9%94%EC%9D%B8&imgId=dru02mddmwz0eti3t99lossf | 위치 = 홈 본문 카드. 스탬프/쿠폰/포인트 줄 오른쪽 옆 "라벨 QR 스캔" 칸. 탭바 가운데는 "주문"(솟은 원형)이고 스캔이 아님 |
| 볼트업 (모빌리티, 충전) | https://uibowl.io/name/%EB%B3%BC%ED%8A%B8%EC%97%85?patterns=%EB%A9%94%EC%9D%B8&imgId=cmojegn7w0003js04t40p9k0j | 위치 = 첫 탭("충전") 화면이 곧 QR 스캐너(상단 QR스캔/코드입력 전환). 하단 탭 3개: 충전/찾기/더보기 |
| 카카오T 자전거/킥보드 (모빌리티) | https://uibowl.io/name/%EC%B9%B4%EC%B9%B4%EC%98%A4T?patterns=%EB%A9%94%EC%9D%B8&imgId=cmoaq858w0005jz04urn8lcty | 위치 = 화면 하단에 고정된 전폭 주 버튼 "QR 스캔하기"(지도 위 바텀시트). 탭바 아님 |
| Kia (모빌리티) | https://uibowl.io/name/Kia?patterns=%EB%A9%94%EC%9D%B8&imgId=cmpur0a2f000bl504w62hm2jr | 위치 = 헤더 오른쪽 스캔 아이콘(알림·프로필과 나란히, 강조 없음). 탭바(5개)에는 스캔 없음 |
| 메디코치 (운동&건강) | https://uibowl.io/name/%EB%A9%94%EB%94%94%EC%BD%94%EC%B9%98?patterns=%EB%A9%94%EC%9D%B8&imgId=cms8eal940047l204opy4iv4c | 위치 = 홈 첫 카드 검색창 오른쪽 끝의 원형 QR 버튼("검색 또는 QR코드를 스캔하세요"). 캡처 범위에 탭바 없음 |

참고(같은 조사 중 확인했으나 표에 넣지 않음): [쏘카일레클](https://uibowl.io/name/%EC%8F%98%EC%B9%B4%EC%9D%BC%EB%A0%88%ED%81%B4?patterns=%EB%A9%94%EC%9D%B8&imgId=clvamggft000ejn09i80qosn9)도 카카오T와 같은 형태(하단 고정 "기기 QR 스캔하기" 전폭 버튼). [컴포즈](https://uibowl.io/name/%EC%BB%B4%ED%8F%AC%EC%A6%88?patterns=%EB%A9%94%EC%9D%B8&imgId=cmt6pefrh0007jr04bxkav8um)는 홈 스탬프 카드 안에 "바코드로 적립" 버튼이 있음.

## 집계

중복 없이 앱 단위로 셈 (카카오T 홈과 자전거 화면은 1개 앱으로 침). 대상 29개.

- 하단 탭바 있음 24 / 없음 5 (없음: 이지태스크, 테라핏, 에어팝, 에스원 모바일카드, 메디코치(캡처 기준))
- 탭 개수 (탭바 있는 24개): 5개 16 · 4개 6 · 3개 2
- 업무형 앱
  - 비즈니스툴 11개: 탭바 있음 7 / 없음 4 → 64%. 없는 4개 중 2개(에어팝, 에스원)는 출입 인증 단일 기능 앱
  - 교육&도서 5개: 탭바 있음 5 / 없음 0 → 100%
  - 비즈니스툴+교육 합계 16개: 있음 12 / 없음 4 → 75%
- 혼합형(탭바 + 홈 퀵 그리드): 8개 확인. 업무형 중에서는 페이워크, 페이히어, 아톡, yes24, 헤이영 캠퍼스
- 가운데 강조 탭: 솟은 원형 "주문" 3 (컴포즈, 써브웨이, 바나프레소), 가운데 "결제" 3 (하나카드, 페이코, L.POINT), 가운데 "홈" 2 (아톡, 카카오T). 비즈니스툴 탭바 앱 7개 중 가운데를 따로 키운 경우는 0
- 스캔 버튼 위치 (4번 표 10개):
  - 탭바 가운데 3 — 하나카드, 페이코, L.POINT. 셋 다 금융/적립 앱이고 스캔 전용이 아니라 "결제" 탭
  - 홈 본문 카드/그리드 3 — 페이히어, 한패스, 바나프레소
  - 헤더 아이콘 1 — Kia
  - 검색창 안 버튼 1 — 메디코치
  - 하단 고정 전폭 CTA 1 — 카카오T
  - 첫 탭 화면이 스캐너 자체 1 — 볼트업
  - FAB 0
  - 덧붙임: 헤이영 캠퍼스(3번 표)도 홈 카드 안 QR 버튼 → 홈 본문 쪽 사례가 하나 더 있음

## 관찰 요약

1. 확인한 홈 화면 29개 중 24개(83%)가 하단 탭바를 쓴다. 비즈니스툴만 보면 11개 중 7개(64%)로 더 낮다. 탭바가 없는 경우는 단일 기능 앱(출입 인증)이거나 헤더 CTA·상단 텍스트 탭으로 대신한 경우다.
2. 업무형 앱의 탭은 4~5개이고 "홈 + 관리 대상 목록/기록 + 더보기·마이" 구성이 많다(페이워크 문서함·정산 내역, 시프티 근무일정·출퇴근기록, 페이히어 나의 매장). 활성 표시는 대부분 아이콘·라벨 색이나 굵기만 바꾸고, 업무형에서는 가운데를 키운 버튼이 없다.
3. 탭바와 홈 퀵 그리드를 같이 쓰는 혼합형이 흔하다(8개). 페이워크·페이히어는 그리드에 "만들기·실행" 동작을, 탭에 "목록·관리" 화면을 두어 역할을 나눴다.
4. 스캔이 핵심인 앱에서 스캔을 탭바 가운데 둔 3개는 모두 결제 앱의 "결제" 탭이다. 업무용 POS(페이히어)는 스캐너를 홈 그리드 첫 칸에 두었고, 모빌리티 앱은 하단 고정 전폭 버튼(카카오T)이나 스캐너가 곧 첫 화면인 방식(볼트업)을 쓴다.
5. 스캔을 FAB로 둔 사례는 0개다. 보조 진입점은 헤더 아이콘(Kia·마이현대), 검색창 안 버튼(메디코치), 홈 카드 안 버튼(헤이영 캠퍼스 학생증 QR) 형태로 나왔다.
