# Figma 사용자 직접 수정 조사 (2026-10-03, 읽기 전용)

파일: https://www.figma.com/design/yPF9ZLVjkg22kgSDD2aKEd
Figma에서는 아무것도 수정하지 않았다. use_figma 읽기 스크립트로 두 서브트리를 같은 순서로 걸으며 비교했다.

## 요약

| 비교 | 범위 | 결과 |
|---|---|---|
| A. `00 최신 시안`(107:2) 복사본 ↔ 원본 | 15화면 × mobile/desktop = 30쌍 | **변경 1개 화면(15 랜딩), 프레임 2개, 6곳**: 모두 문구 줄바꿈(`\n`) 삽입 |
| B. 원본 프레임 ↔ 마지막 내보내기 JSON | 1~15 원본 30프레임 + v8 둘러보기·15 8프레임 | **사용자 수정 0곳**. 표현 차이 1종(아래 참고)만 있음 |

종류별 개수 (A 기준)

| 종류 | 개수 |
|---|---|
| 문구(text.characters) — 줄바꿈 삽입 | 6 |
| 띄어쓰기 추가·삭제 | 0 |
| 글자 크기·굵기·자간·행간 | 0 |
| 위치·크기(x·y·width·height) | 0 |
| auto-layout padding·gap | 0 |
| radius·fills·strokes·effects | 0 |
| visible·노드 추가·삭제·이름 변경 | 0 |

- 변경된 프레임: `15-mobile` (00 복사본 157:2, 4곳), `15-desktop` (00 복사본 157:56, 2곳).
- 화면 1~14 복사본은 원본과 완전히 같다 (모든 노드의 문구·폰트·크기·padding·gap·색·radius·visible·이름·개수 일치).
- 6곳 모두 "기존 띄어쓰기 뒤에 강제 줄바꿈(`\n`)을 넣은" 형태다. 앞의 공백은 지워지지 않아 각 줄 끝에 공백 1칸이 남아 있다 (`"…보여요. \n다른…"`).
- 텍스트 상자 크기는 바뀌지 않았다. 원래도 2줄로 자동 줄바꿈되던 문장이라 높이(72/52/46)와 부모 카드 높이(163/158/159)가 그대로다. 바뀐 것은 줄이 끊기는 위치뿐이다.

## A. `00 최신 시안` 복사본 ↔ 원본

### 15-mobile — 복사본 157:2 ↔ 원본 155:3 (S4-screens-v7)

| 노드 경로(이름) | 복사본 id / 원본 id | 속성 | 이전 (원본) | 이후 (00 복사본) |
|---|---|---|---|---|
| 15-mobile › landing-body › landing-hero › hero-title | 157:8 / 155:9 | characters | `"과학실 시약, 학교별로 한눈에 관리해요"` | `"과학실 시약, \n학교별로 한눈에 관리해요"` |
| 15-mobile › landing-body › landing-hero › hero-subtitle | 157:9 / 155:10 | characters | `"시약 재고·사용 기록·MSDS를 QR로 연결하고, 재고가 부족하면 판매처까지 이어 줘요"` | `"시약 재고·사용 기록·MSDS를 QR로 연결하고, \n재고가 부족하면 판매처까지 이어 줘요"` |
| 15-mobile › landing-body › feature-list › feature-card(1번째, 학교별 분리) › feature-desc | 157:22 / 155:23 | characters | `"우리 학교 시약·재고·사용 기록만 보여요. 다른 학교와 섞이지 않아요"` | `"우리 학교 시약·재고·사용 기록만 보여요. \n다른 학교와 섞이지 않아요"` |
| 15-mobile › landing-body › feature-list › feature-card(2번째, NEIS 학교 선택) › feature-desc | 157:29 / 155:30 | characters | `"회원가입 때 시/도 → 지역 → 학교 순서로 우리 학교를 골라요"` | `"회원가입 때 시/도 → 지역 → 학교 순서로 \n우리 학교를 골라요"` |

### 15-desktop — 복사본 157:56 ↔ 원본 155:57 (S4-screens-v7)

| 노드 경로(이름) | 복사본 id / 원본 id | 속성 | 이전 (원본) | 이후 (00 복사본) |
|---|---|---|---|---|
| 15-desktop › content › feature-grid › feature-card(1번째, 학교별 분리) › feature-desc | 157:76 / 155:77 | characters | `"우리 학교 시약·재고·사용 기록만 보여요. 다른 학교와 섞이지 않아요"` | `"우리 학교 시약·재고·사용 기록만 보여요. \n다른 학교와 섞이지 않아요"` |
| 15-desktop › content › feature-grid › feature-card(2번째, NEIS 학교 선택) › feature-desc | 157:83 / 155:84 | characters | `"회원가입 때 시/도 → 지역 → 학교 순서로 우리 학교를 골라요"` | `"회원가입 때 시/도 → 지역 → 학교 순서로 \n우리 학교를 골라요"` |

(`\n` = 강제 줄바꿈. desktop hero-title·hero-subtitle은 바뀌지 않았다.)

### 변경 없음 (A)

| 화면 | 00 복사본 mobile / desktop | 원본 mobile / desktop | 원본 페이지 |
|---|---|---|---|
| 1 | 150:2 / 150:34 | 148:3 / 148:131 | S4-screens-v6 |
| 2~12 | 140:* · 107:* (요청 표의 id) | 111:* (요청 표의 id) | S4-screens-v5 |
| 13 | 107:1930 / 107:2035 | 105:3 / 105:108 | S4-screens-v4 |
| 14 | 150:71 / 150:167 | 148:35 / 148:168 | S4-screens-v6 |

원본 id 30개는 모두 실제로 존재했다.

### 00 페이지의 목록 밖 노드

프레임 30개 외에 최상위 TEXT 15개가 있다 (화면 번호 라벨, 원본 페이지에 대응 노드 없음 — 비교 대상 아님).

| id | 이름 | 문구 |
|---|---|---|
| 107:115 | label-1 | "1 로그인" |
| 107:256 | label-2 | "2 시약 목록" |
| 107:398 | label-3 | "3 시약 상세" |
| 107:507 | label-4 | "4 사용 기록 입력" |
| 107:695 | label-5 | "5 매뉴얼 업로드" |
| 107:825 | label-6 | "6 재주문·판매처" |
| 107:996 | label-7 | "7 입고·시약 등록" |
| 107:1201 | label-8 | "8 사용자 관리" |
| 107:1356 | label-9 | "9 판매처 설정" |
| 107:1546 | label-10 | "10 사용 기록 내역" |
| 107:1792 | label-11 | "11 시약장 설정" |
| 107:1929 | label-12 | "12 QR 스캔" |
| 107:2134 | label-13 | "13 홈" |
| 150:272 | label-14 | "14 회원가입" |
| 157:110 | label-15 | "15 랜딩" |

## B. 원본 프레임 ↔ 마지막 내보내기 JSON (노드 id 대조)

비교 속성: id·이름·노드 개수/순서, characters, fontSize, fontWeight, letterSpacing, width·height, padding, gap, cornerRadius, fills, strokes. (JSON에는 x·y·lineHeight·visible이 없어 이 항목은 B에서 비교하지 못했다. A에서는 비교했다.)

| 원본 | JSON | 결과 |
|---|---|---|
| 1·14 (148:*) | runs/20261002-2019/design/s4-frames/{1,14}-{mobile,desktop}.json | 일치 |
| 2~12 (111:*) | runs/20261002-1441/design/s4-frames/{2..12}-{mobile,desktop}.json | 일치 (아래 표현 차이 제외) |
| 13 (105:*) | runs/20261002-1416/design/s4-frames/13-{mobile,desktop}.json | 일치 |
| 15 (v7 155:*) | runs/20261003-0112/design/s4-frames/15-{mobile,desktop}.json | 일치 |
| v8 166:* — 15-mobile/desktop, 13·2·3-guest-mobile/desktop (8프레임) | runs/20261003-1212/design/s4-frames/*.json | 일치 |

표현 차이 (사용자 수정 아님, 내보내기 방식 차이)

| 프레임 › 노드 | id | 속성 | JSON 값 | Figma 실제 값 |
|---|---|---|---|---|
| 6-mobile › ex-modal-card | 111:717 | cornerRadius | 24 | 혼합: 위 24 / 24, 아래 0 / 0 |
| 8-mobile › ex-modal-card | 111:1099 | cornerRadius | 24 | 혼합: 위 24 / 24, 아래 0 / 0 |
| 10-mobile › ex-modal-card | 111:1505 | cornerRadius | 24 | 혼합: 위 24 / 24, 아래 0 / 0 |

(하단 시트 모양이라 위쪽 모서리만 둥근 상태로 처음부터 그려졌고, 내보낼 때 왼쪽 위 값만 기록된 것으로 보인다.)

## 참고: 15 랜딩 수정이 최신 v8에 반영됐는지

v8 `15-mobile`(166:3) / `15-desktop`(166:62)을 00 복사본과 문구만 대조했다.

| 노드 | 00 복사본 (사용자 수정) | v8 |
|---|---|---|
| 15-mobile hero-title | 줄바꿈 있음 | 없음 (`"과학실 시약, 학교별로 한눈에 관리해요"`) |
| 15-mobile hero-subtitle | 줄바꿈 있음 | 없음 |
| 15-mobile feature-desc (학교별 분리) | 줄바꿈 있음 | 있음 (166:23, 같은 문자열) |
| 15-mobile feature-desc (NEIS 학교 선택) | 줄바꿈 있음 | 있음 (166:30, 같은 문자열) |
| 15-desktop feature-desc (학교별 분리) | 줄바꿈 있음 | 없음 (166:82) |
| 15-desktop feature-desc (NEIS 학교 선택) | 줄바꿈 있음 | 없음 (166:89) |

즉 사용자 수정 6곳 중 2곳(mobile feature-desc 2개)만 v8에 들어가 있고 4곳은 빠져 있다.
