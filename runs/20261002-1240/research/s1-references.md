# S1 레퍼런스 — run 20261002-1223

대상 화면: 11, 12, 7, 8 (docs/PRD.md §7)
화면 7·8·12는 refs/uibowl-research-20261002.md 의 실제 검색 결과(수량 입력·멤버 관리·QR 스캔)와 runs/20261002-1138 검색 결과에서 골랐다. 화면 11은 이번 run에서 새로 검색했다(좌석 선택, 제어+라디오 버튼, OCR "주의"+칩).

## 화면 11
| # | 앱 | ui_url | 화면 설명 |
|---|---|---|---|
| 1 | BookMyShow | https://uibowl.io/name/BookMyShow?patterns=%EC%98%88%EC%95%BD%C2%B7%EA%B2%B0%EC%A0%9C&patternName=3.%EC%A2%8C%EC%84%9D%20%EC%84%A0%ED%83%9D | 좌석 선택: 상단 시간 칩 가로 줄, 구역 제목별로 행 라벨(A~N)과 번호 칸이 격자로 놓이고, 하단에 범례(Available / Selected / Sold) 3종 |
| 2 | Frontier Airlines | https://uibowl.io/name/Frontier%20Airlines?patterns=%EC%98%88%EC%95%BD%C2%B7%EA%B2%B0%EC%A0%9C&patternName=%EC%A2%8C%EC%84%9D%20%EC%84%A0%ED%83%9D | 좌석 선택: 상단 열 라벨(A~F)과 가운데 통로를 두고 행 번호가 칸 사이에 오는 격자, 구역(UpFront Plus / Premium)을 테두리 묶음으로 나누고 불가 칸은 X, 하단 접이식 'Seat Legend'와 전폭 Continue |
| 3 | 테슬라 (Tesla) | https://uibowl.io/name/%ED%85%8C%EC%8A%AC%EB%9D%BC%20(Tesla)?patterns=%EC%A0%9C%EC%96%B4&patternName=%EC%B0%A8%EB%9F%89%EC%BB%A8%ED%8A%B8%EB%A1%A4 | 차량 컨트롤: 차량을 위에서 본 도식 위에 부위별 '열기' 텍스트를 직접 얹어 누르게 하고, 하단에 아이콘 액션 4개(플래시·경적·시작·환기) |
| 4 | LG ThinQ | https://uibowl.io/name/LG%20ThinQ?patterns=%EC%A0%9C%EC%96%B4&patternName=%EA%B1%B4%EC%A1%B0%EA%B8%B0 | 워시타워 제어: 상단 기기 이미지 아래 '세탁 / 건조' 탭으로 같은 기기의 위·아래 칸을 나눠 보여주고, 카드 리스트로 최근 코스, 설정은 바텀시트 라디오 |
| 5 | G car | https://uibowl.io/name/G%20car?patterns=%EC%8B%A0%EC%B2%AD%ED%95%98%EA%B8%B0&imgId=cmo85af8n00fcjr04s5erd4yk | 반납 연장: 상단 요약, 회색 구분 영역 안 '주의사항' 글머리 목록, 그 아래 휠 피커와 빠른 선택 칩(+10분 등), 하단 전폭 CTA |

## 화면 12
| # | 앱 | ui_url | 화면 설명 |
|---|---|---|---|
| 1 | 카카오T | https://uibowl.io/name/%EC%B9%B4%EC%B9%B4%EC%98%A4T?patterns=%EC%B4%AC%EC%98%81%ED%95%98%EA%B8%B0&patternName=QR%EC%8A%A4%EC%BA%94-%EC%9E%90%EC%A0%84%EA%B1%B0%20%EB%B0%98%EB%82%A9 | QR 스캔: 전체 카메라 딤, 상단 2줄 안내, 가운데 라운드 프레임과 조준점, 아래 원형 플래시 버튼, 최하단 바 '직접 입력' |
| 2 | 볼트업 | https://uibowl.io/name/%EB%B3%BC%ED%8A%B8%EC%97%85?patterns=%EC%B4%AC%EC%98%81%ED%95%98%EA%B8%B0&patternName=QR%EC%8A%A4%EC%BA%94 | QR 스캔: 상단 탭 'QR스캔 / 코드입력', 코너 브라켓 프레임 안에 부착 위치 안내 문구, 밝기 버튼, 하단 최근 장소 칩 |
| 3 | 마미톡 | https://uibowl.io/name/%EB%A7%88%EB%AF%B8%ED%86%A1?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&imgId=cmpcmrk8h01s0jl04xuxmaavu | 바코드 등록: 카메라 권한이 없으면 프레임 자리에 "카메라 권한이 필요해요" + '권한 설정하기' 버튼, 하단 '바코드 직접 등록하기' |
| 4 | 닥터다이어리 | https://uibowl.io/name/%EB%8B%A5%ED%84%B0%EB%8B%A4%EC%9D%B4%EC%96%B4%EB%A6%AC?patterns=%EC%B4%AC%EC%98%81%ED%95%98%EA%B8%B0&imgId=cmr7e4uyx00diju04jj009eeh | 스캔: 상단 플래시·닫기, 코너 브라켓 프레임, 하단 3액션 '갤러리 · 셔터 · 직접 입력' |
| 5 | 빽다방 | https://uibowl.io/name/%EB%B9%BD%EB%8B%A4%EB%B0%A9?patterns=%EC%BF%A0%ED%8F%B0&imgId=cmsqw7eev001si604q3io8gzt | 쿠폰 등록 바텀시트: 번호 입력 + 등록, 필드 아래 인라인 에러 "유효하지 않은 쿠폰번호입니다", 아래 '이미지 불러오기 / 바코드 인식하기' 카드 2개 |

## 화면 7
| # | 앱 | ui_url | 화면 설명 |
|---|---|---|---|
| 1 | 빼기 | https://uibowl.io/name/%EB%B9%BC%EA%B8%B0?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&patternName=%EC%83%81%ED%92%88%20%EB%93%B1%EB%A1%9D | 상품 등록: 목록 화면 우하단 플로팅 "+ 상품 등록" 버튼으로 등록 폼(드롭다운 포함)에 진입하는 2단계 흐름 |
| 2 | 우리동네GS | https://uibowl.io/name/%EC%9A%B0%EB%A6%AC%EB%8F%99%EB%84%A4GS?patterns=%EC%A1%B0%ED%9A%8C%ED%95%98%EA%B8%B0&patternName=%EC%9E%AC%EA%B3%A0%EC%B0%BE%EA%B8%B0 | 재고찾기: 상단 검색 입력 + 아래 검색어 목록, 이후 결과 리스트로 이어지는 흐름 |
| 3 | 마이현대 | https://uibowl.io/name/%EB%A7%88%EC%9D%B4%ED%98%84%EB%8C%80?patterns=%EC%84%A0%EB%AC%BC%ED%95%98%EA%B8%B0&imgId=cmojmaunh000al204u4pkec37 | 옵션 드롭다운 아래 선택 항목 카드(이름 + X), 박스형 스테퍼 [− 입력 +](가운데 입력 필드), 오른쪽 금액, 아래 총액과 CTA |
| 4 | 포스티 | https://uibowl.io/name/%ED%8F%AC%EC%8A%A4%ED%8B%B0?patterns=%EC%9E%A5%EB%B0%94%EA%B5%AC%EB%8B%88&imgId=cmukh11i5000zl80421av0ejn | 옵션/수량 변경 바텀시트: 옵션 칩 그리드 선택 → 회색 카드 안 스테퍼, 아래 ⓘ 최대 수량 안내 1줄, 하단 '변경하기' |
| 5 | 앳플리 | https://uibowl.io/name/%EC%95%B3%ED%94%8C%EB%A6%AC?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&imgId=cmtpokqcx001ukz04i4g1gpag | 세트 행 숫자 필드 안 단위 suffix(Kg·회), 행 끝 삭제, '+ 세트 추가', 필수값이 비면 하단 저장 비활성 |

## 화면 8
| # | 앱 | ui_url | 화면 설명 |
|---|---|---|---|
| 1 | 이지태스크 | https://uibowl.io/name/%EC%9D%B4%EC%A7%80%ED%83%9C%EC%8A%A4%ED%81%AC?patterns=%ED%83%90%EC%83%89&patternName=%EA%B8%B0%EC%97%85%20%EA%B5%AC%EC%84%B1%EC%9B%90 | 구성원 화면: 제목 옆 인원 수 배지와 우측 '초대하기', 필터·이름 검색 카드, 행마다 '관리자' 역할 배지와 '나' 배지 |
| 2 | 신한 슈퍼SOL | https://uibowl.io/name/%EC%8B%A0%ED%95%9C%20%EC%8A%88%ED%8D%BCSOL?patterns=%EA%B2%8C%EC%9D%B4%EB%AF%B8%ED%94%BC%EC%BC%80%EC%9D%B4%EC%85%98&imgId=cmsmkdjor0007jz04ehaecntc | '가족 현황' 카드와 별도 카드 '인증 대기중 (총 1명)'을 분리, 대기 행에 날짜와 상태 텍스트, 하단 '+ 가족 초대하기' |
| 3 | 쑥쑥찰칵 | https://uibowl.io/name/%EC%91%A5%EC%91%A5%EC%B0%B0%EC%B9%B5?patterns=%EC%84%A4%EC%A0%95&imgId=cmub7kwx2000njs04uwzytdex | 가족 구성원 목록: 상단 초대 카드, 행 = 이름 + '나' 배지 + 보조줄 "엄마 · 관리자" + 권한 칩, 우측 › |
| 4 | 패스오더 | https://uibowl.io/name/%ED%8C%A8%EC%8A%A4%EC%98%A4%EB%8D%94?patterns=%EA%B2%8C%EC%9D%B4%EB%AF%B8%ED%94%BC%EC%BC%80%EC%9D%B4%EC%85%98&imgId=cmspf7433001dl704mbiwaamm | 참여자 목록 '2/12' 카운터, 본인 행은 "(나)"만 있고 삭제 없음, 다른 행 우측 텍스트 '삭제', 아래 '+ 멤버 추가' |
| 5 | 펫피 | https://uibowl.io/name/%ED%8E%AB%ED%94%BC%20?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&patternName=%EA%B0%80%EC%A1%B1%20%EA%B5%AC%EC%84%B1%EC%9B%90 | 구성원 0명 빈 상태 문구, 하단 유의사항 목록(초대 가능 조건), 우상단 초대 아이콘 |
