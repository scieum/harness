# S1 레퍼런스 — run 20261002-1441

대상 화면: 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 (docs/PRD.md §7)
이번 run은 화면 2~12 모바일에 하단 탭바를 넣는 일관성 작업이라 새 검색 없이 앞선 실행에서 G-S1을 통과한 uibowl 검색 결과를 그대로 모았다.
- 화면 2·3·6: runs/20261002-0838/research/
- 화면 4·5·9·10: runs/20261002-1138/research/ (4·5는 원래 runs/20261001-1910 결과)
- 화면 7·8·11·12: runs/20261002-1301/research/

## 화면 2
| # | 앱 | ui_url | 화면 설명 |
|---|---|---|---|
| 1 | 메디코치 | https://uibowl.io/name/%EB%A9%94%EB%94%94%EC%BD%94%EC%B9%98?patterns=%EA%B2%80%EC%83%89&imgId=cms8e8sdi0007jm044by8323r | 약국 검색: 상단 검색 바 + 결과 리스트(행마다 이름 1줄 + 보조 정보 1줄) |
| 2 | 쿠팡 | https://uibowl.io/name/%EC%BF%A0%ED%8C%A1?patterns=%EB%A9%94%EC%9D%B8&imgId=pujxwsmnkvc7nav05jzqks8l | 로켓프레시: 상품 카드 안에 "품절임박·잔여 N개" 상태 배지를 이름 위에 붙여 표시 |
| 3 | 크몽 | https://uibowl.io/name/%ED%81%AC%EB%AA%BD?patterns=%EC%B1%84%ED%8C%85&imgId=cmopsvj79001xjm04tk8cii2l | 메시지 목록: 상단 필터 칩(전체/안 읽음/거래 중) → 검색 바 → 리스트 순서 배치 |
| 4 | 우리동네GS | https://uibowl.io/name/%EC%9A%B0%EB%A6%AC%EB%8F%99%EB%84%A4GS?patterns=%EC%A1%B0%ED%9A%8C%ED%95%98%EA%B8%B0&patternName=%EC%9E%AC%EA%B3%A0%EC%B0%BE%EA%B8%B0 | 재고찾기: 검색 진입 → 품목 리스트 → 재고 결과 조회 흐름 |

## 화면 3
| # | 앱 | ui_url | 화면 설명 |
|---|---|---|---|
| 1 | 달다방 | https://uibowl.io/name/%EB%8B%AC%EB%8B%A4%EB%B0%A9?patterns=%EC%83%81%EC%84%B8%EC%A0%95%EB%B3%B4%20%28PDP%29&patternName=%EC%83%81%ED%92%88 | 상품 상세: 요약 정보 → 탭 → 아코디언·테이블로 상세 속성 정리 |
| 2 | 럽맘 | https://uibowl.io/name/%EB%9F%BD%EB%A7%98?patterns=%EC%83%81%EC%84%B8%EC%A0%95%EB%B3%B4%20%28PDP%29&patternName=%EC%83%81%ED%92%88 | 상품 상세: 상단 제목 바 + 대표 이미지 + 이름·설명 + 하단 고정 액션 버튼 |
| 3 | 하나원큐 | https://uibowl.io/name/%ED%95%98%EB%82%98%EC%9B%90%ED%81%90?patterns=%EA%B0%84%ED%8E%B8%EA%B2%B0%EC%A0%9C&patternName=QR%EA%B2%B0%EC%A0%9C | QR 결제: 세그먼트(바코드/QR) 전환 + 화면 중앙 QR + 아래 라벨 |
| 4 | 카카오T | https://uibowl.io/name/%EC%B9%B4%EC%B9%B4%EC%98%A4T?patterns=%EC%B4%AC%EC%98%81%ED%95%98%EA%B8%B0&patternName=QR%EC%8A%A4%EC%BA%94-%EC%9E%90%EC%A0%84%EA%B1%B0%20%EB%B0%98%EB%82%A9 | QR 스캔: 안내 문구 + 스캔 영역 + 하단 "직접 입력" 대체 경로 |

## 화면 4
| # | 앱 | ui_url | 화면 설명 |
|---|---|---|---|
| 1 | 오클고 | https://uibowl.io/name/%EC%98%A4%ED%81%B4%EA%B3%A0?patterns=%EA%B8%80%EC%93%B0%EA%B8%B0&patternName=%EA%B8%B0%EB%A1%9D%ED%95%98%EA%B8%B0 | 기록하기 바텀시트 폼: 라벨(필수 표시) 위·입력 아래로 날짜 드롭다운 → 장소 칩 → 선택값 → 시간 드롭다운 → 메모 순 세로 배치, 하단 전폭 "기록" 버튼 |
| 2 | 오늘의 루틴 | https://uibowl.io/name/%EC%98%A4%EB%8A%98%EC%9D%98%20%EB%A3%A8%ED%8B%B4?patterns=%EA%B8%80%EC%93%B0%EA%B8%B0&patternName=%EB%A3%A8%ED%8B%B4%20%EA%B8%B0%EB%A1%9D%ED%95%98%EA%B8%B0 | 루틴 기록하기: 탭(정보/진행 현황/오늘의 기록) + "오늘의 기록" 섹션의 날짜 행과 + 버튼으로 기록 추가, 저장 후 토스트 |
| 3 | 레포브 | https://uibowl.io/name/%EB%A0%88%ED%8F%AC%EB%B8%8C?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&patternName=%EA%B8%B0%EB%A1%9D%ED%95%98%EA%B8%B0 | 기록하기: 대상 요약(이름·분류·위치) 아래 하단 고정 "이 장소 기록하기" 버튼 → 기록 입력 단계로 이어지는 흐름 (8장) |

## 화면 5
| # | 앱 | ui_url | 화면 설명 |
|---|---|---|---|
| 1 | 다글로 | https://uibowl.io/name/%EB%8B%A4%EA%B8%80%EB%A1%9C?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&patternName=%EC%9C%A0%ED%8A%9C%EB%B8%8C%20%EB%A7%81%ED%81%AC%20%EC%97%85%EB%A1%9C%EB%93%9C | AI 받아쓰기 업로드: 상단 입력 필드 + 옵션 행(언어·주제) + 하단 고정 실행 버튼(입력 전 비활성) → 처리 결과로 이어지는 흐름 |
| 2 | 수현이랑 | https://uibowl.io/name/%EC%88%98%ED%98%84%EC%9D%B4%EB%9E%91?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&patternName=%EA%B3%B5%EC%9C%A0%20%EC%95%A8%EB%B2%94%20%EC%97%85%EB%A1%9C%EB%93%9C | 업로드 정보 입력: 칩 선택 → 제목 → 설명(글자 수 카운터) 세로 폼, 상단 제목+닫기, 하단 전폭 "완료" 버튼 |
| 3 | 키피럽 | https://uibowl.io/name/%ED%82%A4%ED%94%BC%EB%9F%BD?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&patternName=%EC%9D%B8%EC%A6%9D%EC%83%B7-%EC%97%85%EB%A1%9C%EB%93%9C | 인증샷 업로드: 상단 안내 문구 + 중앙 미리보기 영역 + 하단 갤러리/촬영 진입, 이후 로딩 → 결과 확인 단계 (7장) |

## 화면 6
| # | 앱 | ui_url | 화면 설명 |
|---|---|---|---|
| 1 | W컨셉 | https://uibowl.io/name/W%EC%BB%A8%EC%85%89?patterns=%EB%82%B4%EC%97%AD&patternName=%EC%9E%AC%EC%9E%85%EA%B3%A0%20%EC%95%8C%EB%A6%BC | 재입고 알림 목록: 카드(썸네일·이름·상태 배지) + 카드 하단 날짜·액션 버튼 + 하단 안내 아코디언 |
| 2 | 데일리샷 | https://uibowl.io/name/%EB%8D%B0%EC%9D%BC%EB%A6%AC%EC%83%B7?patterns=%EC%8B%A0%EC%B2%AD%ED%95%98%EA%B8%B0&patternName=%EC%9E%AC%EC%9E%85%EA%B3%A0%20%EC%95%8C%EB%A6%BC | 재입고 알림 신청: 상세 안 "판매처" 행(매장명·거리·주소) + 하단 고정 "재입고 알림" 버튼 → 모달 |
| 3 | 데일리샷 | https://uibowl.io/name/%EB%8D%B0%EC%9D%BC%EB%A6%AC%EC%83%B7?patterns=%EB%82%B4%EC%97%AD&patternName=%EC%9E%AC%EC%9E%85%EA%B3%A0%20%EC%95%8C%EB%A6%BC%EB%82%B4%EC%97%AD | 재입고 알림 내역: 상단 안내 박스 + 내역 없을 때 빈 화면 문구 |
| 4 | 칩스 | https://uibowl.io/name/%EC%B9%A9%EC%8A%A4?patterns=%ED%91%B8%EC%8B%9C%EC%95%8C%EB%A6%BC | 푸시 알림: 제목 1줄 + 내용 1줄 + 시간으로 구성된 알림 배너 |

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

## 화면 9
| # | 앱 | ui_url | 화면 설명 |
|---|---|---|---|
| 1 | 페이워크 | https://uibowl.io/name/%ED%8E%98%EC%9D%B4%EC%9B%8C%ED%81%AC?patterns=%EB%A9%94%EB%89%B4&patternName=%EA%B0%84%ED%8E%B8%EB%A9%94%EB%89%B4%20-%20%EA%B1%B0%EB%9E%98%EC%B2%98 | 간편메뉴-거래처: 그리드 메뉴의 "거래처" 진입 → 상단 검색 바, 최근 거래/전체 구분 리스트(행마다 더보기 메뉴), 하단 2버튼(연락처로 등록·거래처 등록) |
| 2 | 페이워크 | https://uibowl.io/name/%ED%8E%98%EC%9D%B4%EC%9B%8C%ED%81%AC?patterns=%ED%8E%B8%EC%A7%91%C2%B7%EC%88%98%EC%A0%95%ED%95%98%EA%B8%B0&patternName=%EA%B1%B0%EB%9E%98%EC%B2%98%EC%88%98%EC%A0%95 | 거래처수정: 목록 행의 메뉴에서 수정 진입, 모달로 수정/삭제를 확인하는 흐름 (3장) |
| 3 | 페이워크 | https://uibowl.io/name/%ED%8E%98%EC%9D%B4%EC%9B%8C%ED%81%AC?patterns=%ED%8E%B8%EC%A7%91%C2%B7%EC%88%98%EC%A0%95%ED%95%98%EA%B8%B0&patternName=%EA%B1%B0%EB%9E%98%EC%B2%98%EC%B6%94%EA%B0%80 | 거래처추가: 빈 상태(아이콘·안내문 + 주/보조 버튼 세로 2개) → 텍스트 필드 입력 폼 → 등록 완료 후 목록 복귀 (9장) |

## 화면 10
| # | 앱 | ui_url | 화면 설명 |
|---|---|---|---|
| 1 | 토스증권 | https://uibowl.io/name/%ED%86%A0%EC%8A%A4%EC%A6%9D%EA%B6%8C?patterns=%EB%82%B4%EC%97%AD&patternName=%EA%B1%B0%EB%9E%98%EB%82%B4%EC%97%AD | 거래내역: 상단 탭 + 요약 블록, "전체" 드롭다운 필터 아래 날짜(좌)·항목/시각·유형(중)·금액(우) 3열 행 리스트 (4장) |
| 2 | 미니스탁 | https://uibowl.io/name/%EB%AF%B8%EB%8B%88%EC%8A%A4%ED%83%81?patterns=%EB%82%B4%EC%97%AD&patternName=%EC%9B%90%ED%99%94%20%EA%B1%B0%EB%9E%98%EB%82%B4%EC%97%AD | 원화 거래내역: 섹션 제목 우측 "최근 6개월·전체" 기간/유형 필터, 월 단위 그룹 헤더 아래 항목명·유형·날짜 / 증감·잔액 2열 행 |
| 3 | 토스 | https://uibowl.io/name/%ED%86%A0%EC%8A%A4?patterns=%EB%82%B4%EC%97%AD&patternName=%EA%B1%B0%EB%9E%98%20%EC%83%81%EC%84%B8 | 거래 상세: 상단 대상·금액 강조, 아래 라벨-값 행(카테고리·메모·상대·일시), 하단에 최근 이력 요약 섹션 |

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
