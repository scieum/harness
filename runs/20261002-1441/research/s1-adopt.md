# S1 채택 항목 — run 20261002-1441

구조·흐름·배치만 가져온다. 색·폰트·모서리는 docs/design.md를 따른다.
화면별 채택 내용은 출처 run(0838·1138·1301)의 s1-adopt.md 를 그대로 옮겼다.
하단 탭바 메모(공통): 화면 2~12 모바일 프레임은 모두 같은 하단 탭바를 최하단에 고정하고, 각 화면이 원래 가진 하단 고정 버튼(저장·기록·초대 등)은 탭바 바로 위에 쌓는다. 탭바의 구성·순서는 화면 13 기준을 따르며 탭바 활성 항목은 현재 화면이 속한 탭 하나만 둔다.

## 화면 2
| # | ui_url | 가져올 것 |
|---|---|---|
| 1 | https://uibowl.io/name/%EB%A9%94%EB%94%94%EC%BD%94%EC%B9%98?patterns=%EA%B2%80%EC%83%89&imgId=cms8e8sdi0007jm044by8323r | 상단 검색 바 + 행마다 시약명 1줄·보조 정보(재고량·입고일) 1줄의 2줄 리스트 행 구조 |
| 2 | https://uibowl.io/name/%EC%BF%A0%ED%8C%A1?patterns=%EB%A9%94%EC%9D%B8&imgId=pujxwsmnkvc7nav05jzqks8l | 재고 부족 상태를 행 안 이름 옆 배지(badge-low-stock)로 "잔여 N" 수치와 함께 붙이는 배치 (이 배지는 선택/강조 상태 대상 아님) |
| 3 | https://uibowl.io/name/%ED%81%AC%EB%AA%BD?patterns=%EC%B1%84%ED%8C%85&imgId=cmopsvj79001xjm04tk8cii2l | 리스트 위 필터 칩(전체/재고 부족) → 검색 바 → 리스트 순서의 상단 영역 배치; 칩은 한 번에 하나만 선택 상태를 갖는 단일 선택 구조 |
| 4 | https://uibowl.io/name/%EC%9A%B0%EB%A6%AC%EB%8F%99%EB%84%A4GS?patterns=%EC%A1%B0%ED%9A%8C%ED%95%98%EA%B8%B0&patternName=%EC%9E%AC%EA%B3%A0%EC%B0%BE%EA%B8%B0 | 검색 → 품목 리스트 → 행 탭 시 상세(화면 3)로 이동하는 조회 흐름 |

## 화면 3
| # | ui_url | 가져올 것 |
|---|---|---|
| 1 | https://uibowl.io/name/%EB%8B%AC%EB%8B%A4%EB%B0%A9?patterns=%EC%83%81%EC%84%B8%EC%A0%95%EB%B3%B4%20%28PDP%29&patternName=%EC%83%81%ED%92%88 | 상단 요약(시약명·현재 재고) 아래 탭/테이블로 입고일·사용 기록·사용자 속성을 나눠 정리하는 구조; 탭은 활성 탭 하나에 하단 인디케이터를 두는 구조 |
| 2 | https://uibowl.io/name/%EB%9F%BD%EB%A7%98?patterns=%EC%83%81%EC%84%B8%EC%A0%95%EB%B3%B4%20%28PDP%29&patternName=%EC%83%81%ED%92%88 | 상단 뒤로가기+제목 바, 본문 스크롤, 하단 고정 주요 액션 버튼(사용 기록) 배치 |
| 3 | https://uibowl.io/name/%ED%95%98%EB%82%98%EC%9B%90%ED%81%90?patterns=%EA%B0%84%ED%8E%B8%EA%B2%B0%EC%A0%9C&patternName=QR%EA%B2%B0%EC%A0%9C | MSDS QR을 독립 블록 중앙에 두고 바로 아래 설명 라벨을 붙이는 배치 (msds-entry); 세그먼트 전환은 활성 항목 하나만 선택 상태 |
| 4 | https://uibowl.io/name/%EC%B9%B4%EC%B9%B4%EC%98%A4T?patterns=%EC%B4%AC%EC%98%81%ED%95%98%EA%B8%B0&patternName=QR%EC%8A%A4%EC%BA%94-%EC%9E%90%EC%A0%84%EA%B1%B0%20%EB%B0%98%EB%82%A9 | QR 외에 "MSDS 직접 열기" 같은 대체 경로를 QR 아래 링크로 함께 두는 흐름 |

## 화면 4
| # | ui_url | 가져올 것 |
|---|---|---|
| 1 | https://uibowl.io/name/%EC%98%A4%ED%81%B4%EA%B3%A0?patterns=%EA%B8%80%EC%93%B0%EA%B8%B0&patternName=%EA%B8%B0%EB%A1%9D%ED%95%98%EA%B8%B0 | 라벨 위·입력 아래 세로 폼(날짜 드롭다운 → 수량·단위 → 사용자 → 메모), 필수 표시, 하단 전폭 "기록" 버튼 배치. 단위 칩 선택 상태에 하늘색 강조 위치를 둔다 |
| 2 | https://uibowl.io/name/%EC%98%A4%EB%8A%98%EC%9D%98%20%EB%A3%A8%ED%8B%B4?patterns=%EA%B8%80%EC%93%B0%EA%B8%B0&patternName=%EB%A3%A8%ED%8B%B4%20%EA%B8%B0%EB%A1%9D%ED%95%98%EA%B8%B0 | 저장 직후 토스트로 결과를 알리고 기록 목록으로 돌아오는 저장 피드백 흐름 |
| 3 | https://uibowl.io/name/%EB%A0%88%ED%8F%AC%EB%B8%8C?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&patternName=%EA%B8%B0%EB%A1%9D%ED%95%98%EA%B8%B0 | 폼 상단에 대상 요약(시약명·현재 재고) 블록을 고정해 무엇을 기록하는지 보여준 뒤 입력으로 이어지는 구조. 요약 블록의 재고 부족 표시는 하늘색이 아닌 별도 경고 처리로 둔다 |

## 화면 5
| # | ui_url | 가져올 것 |
|---|---|---|
| 1 | https://uibowl.io/name/%EB%8B%A4%EA%B8%80%EB%A1%9C?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&patternName=%EC%9C%A0%ED%8A%9C%EB%B8%8C%20%EB%A7%81%ED%81%AC%20%EC%97%85%EB%A1%9C%EB%93%9C | 파일 선택 전에는 하단 고정 실행(AI 추출) 버튼을 비활성으로 두고, 선택 후 활성화 → 처리 → 결과로 넘어가는 흐름 (키·모델 옵션 행은 가져오지 않음) |
| 2 | https://uibowl.io/name/%EC%88%98%ED%98%84%EC%9D%B4%EB%9E%91?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&patternName=%EA%B3%B5%EC%9C%A0%20%EC%95%A8%EB%B2%94%20%EC%97%85%EB%A1%9C%EB%93%9C | 추출 결과 확인 단계를 상단 제목+닫기, 본문 스크롤(결과 표·수정 가능 필드), 하단 전폭 "저장" 버튼으로 구성하는 배치 |
| 3 | https://uibowl.io/name/%ED%82%A4%ED%94%BC%EB%9F%BD?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&patternName=%EC%9D%B8%EC%A6%9D%EC%83%B7-%EC%97%85%EB%A1%9C%EB%93%9C | 상단 안내 문구 + 중앙 업로드/미리보기 영역 + 하단 진입 버튼, 업로드 후 로딩 상태를 거쳐 확인 단계로 가는 3단 흐름. 업로드 영역 아이콘과 처리 진행 표시 위치에 하늘색 강조를 둔다 |

## 화면 6
| # | ui_url | 가져올 것 |
|---|---|---|
| 1 | https://uibowl.io/name/W%EC%BB%A8%EC%85%89?patterns=%EB%82%B4%EC%97%AD&patternName=%EC%9E%AC%EC%9E%85%EA%B3%A0%20%EC%95%8C%EB%A6%BC | 알림 카드(시약명·상태 배지·필요량 대비 재고) + 카드 하단 날짜·액션 버튼, 목록 아래 안내 아코디언 구조 |
| 2 | https://uibowl.io/name/%EB%8D%B0%EC%9D%BC%EB%A6%AC%EC%83%B7?patterns=%EC%8B%A0%EC%B2%AD%ED%95%98%EA%B8%B0&patternName=%EC%9E%AC%EC%9E%85%EA%B3%A0%20%EC%95%8C%EB%A6%BC | "판매처" 라벨-값 행(판매처명·부가 정보) 배치와 하단 고정 연결 버튼 → 확인 모달 흐름 |
| 3 | https://uibowl.io/name/%EB%8D%B0%EC%9D%BC%EB%A6%AC%EC%83%B7?patterns=%EB%82%B4%EC%97%AD&patternName=%EC%9E%AC%EC%9E%85%EA%B3%A0%20%EC%95%8C%EB%A6%BC%EB%82%B4%EC%97%AD | 상단 기준 안내 박스(재주문 기준 설명) + 알림 0건일 때 빈 화면 문구 배치 |
| 4 | https://uibowl.io/name/%EC%B9%A9%EC%8A%A4?patterns=%ED%91%B8%EC%8B%9C%EC%95%8C%EB%A6%BC | 알림 문구를 제목 1줄(시약명+부족) + 내용 1줄(필요량/현재량) + 시간으로 짜는 구조 |

## 화면 7
| # | ui_url | 가져올 것 |
|---|---|---|
| 1 | https://uibowl.io/name/%EB%B9%BC%EA%B8%B0?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&patternName=%EC%83%81%ED%92%88%20%EB%93%B1%EB%A1%9D | 목록에서 고정 "+ 새 시약 등록" 진입점 → 별도 등록 폼(분류 드롭다운 포함)으로 넘어가는 2단계 흐름 |
| 2 | https://uibowl.io/name/%EC%9A%B0%EB%A6%AC%EB%8F%99%EB%84%A4GS?patterns=%EC%A1%B0%ED%9A%8C%ED%95%98%EA%B8%B0&patternName=%EC%9E%AC%EA%B3%A0%EC%B0%BE%EA%B8%B0 | 기존 시약 입고는 상단 검색 → 결과 리스트에서 선택 → 수량 입력 단계로 넘어가는 흐름 |
| 3 | https://uibowl.io/name/%EB%A7%88%EC%9D%B4%ED%98%84%EB%8C%80?patterns=%EC%84%A0%EB%AC%BC%ED%95%98%EA%B8%B0&imgId=cmojmaunh000al204u4pkec37 | 선택한 시약 카드(이름 + X) 아래 가운데를 직접 타이핑할 수 있는 [− 입력 +] 스테퍼, 아래 합계 줄 → CTA 순서 |
| 4 | https://uibowl.io/name/%ED%8F%AC%EC%8A%A4%ED%8B%B0?patterns=%EC%9E%A5%EB%B0%94%EA%B5%AC%EB%8B%88&imgId=cmukh11i5000zl80421av0ejn | 단위·규격 칩 선택 → 스테퍼 → ⓘ 한 줄 보조 안내(현재 재고 → 입고 후 재고) 순 배치 |
| 5 | https://uibowl.io/name/%EC%95%B3%ED%94%8C%EB%A6%AC?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&imgId=cmtpokqcx001ukz04i4g1gpag | 숫자 필드 안 단위 suffix(병·mL·g), 필수값 미입력 시 하단 저장 버튼 비활성 |

## 화면 8
| # | ui_url | 가져올 것 |
|---|---|---|
| 1 | https://uibowl.io/name/%EC%9D%B4%EC%A7%80%ED%83%9C%EC%8A%A4%ED%81%AC?patterns=%ED%83%90%EC%83%89&patternName=%EA%B8%B0%EC%97%85%20%EA%B5%AC%EC%84%B1%EC%9B%90 | 헤더 한 줄에 "사용자 N명 + 초대 버튼", 그 아래 검색 → 리스트, 행 = 이름 + 역할 배지 + 본인 '나' 배지 |
| 2 | https://uibowl.io/name/%EC%8B%A0%ED%95%9C%20%EC%8A%88%ED%8D%BCSOL?patterns=%EA%B2%8C%EC%9D%B4%EB%AF%B8%ED%94%BC%EC%BC%80%EC%9D%B4%EC%85%98&imgId=cmsmkdjor0007jz04ehaecntc | 활성 멤버와 '초대 대기 (N)'을 섹션으로 분리하고, 대기 행 = 이메일 + 초대일 + 상태 텍스트 |
| 3 | https://uibowl.io/name/%EC%91%A5%EC%91%A5%EC%B0%B0%EC%B9%B5?patterns=%EC%84%A4%EC%A0%95&imgId=cmub7kwx2000njs04uwzytdex | 행 보조줄에 역할 텍스트를 쓰고 우측 › 로 상세(역할 변경)에 진입하는 구조 |
| 4 | https://uibowl.io/name/%ED%8C%A8%EC%8A%A4%EC%98%A4%EB%8D%94?patterns=%EA%B2%8C%EC%9D%B4%EB%AF%B8%ED%94%BC%EC%BC%80%EC%9D%B4%EC%85%98&imgId=cmspf7433001dl704mbiwaamm | 본인 행에는 삭제 동작을 숨기고, 다른 행만 우측 끝 텍스트 '삭제'로 행 단위 제거 |
| 5 | https://uibowl.io/name/%ED%8E%AB%ED%94%BC%20?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&patternName=%EA%B0%80%EC%A1%B1%20%EA%B5%AC%EC%84%B1%EC%9B%90 | 다른 사용자 0명일 때 빈 상태 1줄 + 하단 유의사항(같은 학교 계정만 초대 가능)을 고정 |

## 화면 9
| # | ui_url | 가져올 것 |
|---|---|---|
| 1 | https://uibowl.io/name/%ED%8E%98%EC%9D%B4%EC%9B%8C%ED%81%AC?patterns=%EB%A9%94%EB%89%B4&patternName=%EA%B0%84%ED%8E%B8%EB%A9%94%EB%89%B4%20-%20%EA%B1%B0%EB%9E%98%EC%B2%98 | 판매처 목록: 상단 검색 바 + 행마다 우측 더보기(수정·삭제) 메뉴 + 하단 고정 "판매처 등록" 버튼 배치 |
| 2 | https://uibowl.io/name/%ED%8E%98%EC%9D%B4%EC%9B%8C%ED%81%AC?patterns=%ED%8E%B8%EC%A7%91%C2%B7%EC%88%98%EC%A0%95%ED%95%98%EA%B8%B0&patternName=%EA%B1%B0%EB%9E%98%EC%B2%98%EC%88%98%EC%A0%95 | 행 메뉴 → 수정 폼 진입, 삭제는 모달로 한 번 더 확인하는 수정·삭제 흐름 |
| 3 | https://uibowl.io/name/%ED%8E%98%EC%9D%B4%EC%9B%8C%ED%81%AC?patterns=%ED%8E%B8%EC%A7%91%C2%B7%EC%88%98%EC%A0%95%ED%95%98%EA%B8%B0&patternName=%EA%B1%B0%EB%9E%98%EC%B2%98%EC%B6%94%EA%B0%80 | 판매처가 0건일 때 아이콘·안내문 + 등록 버튼을 가운데 두는 빈 상태, 등록 폼(텍스트 필드 세로) 저장 후 목록으로 복귀하는 흐름 |

## 화면 10
| # | ui_url | 가져올 것 |
|---|---|---|
| 1 | https://uibowl.io/name/%ED%86%A0%EC%8A%A4%EC%A6%9D%EA%B6%8C?patterns=%EB%82%B4%EC%97%AD&patternName=%EA%B1%B0%EB%9E%98%EB%82%B4%EC%97%AD | 리스트 바로 위 "전체" 드롭다운 필터 + 행마다 날짜(좌)·시약명/사용자·유형(중)·증감 수량(우) 3열 배치 |
| 2 | https://uibowl.io/name/%EB%AF%B8%EB%8B%88%EC%8A%A4%ED%83%81?patterns=%EB%82%B4%EC%97%AD&patternName=%EC%9B%90%ED%99%94%20%EA%B1%B0%EB%9E%98%EB%82%B4%EC%97%AD | 섹션 제목 우측에 기간·유형 요약 필터("최근 N개월 · 전체")를 두고 월(날짜) 그룹 헤더로 기록을 묶는 구조, 행 우측에 증감과 남은 재고를 2줄로 표시 |
| 3 | https://uibowl.io/name/%ED%86%A0%EC%8A%A4?patterns=%EB%82%B4%EC%97%AD&patternName=%EA%B1%B0%EB%9E%98%20%EC%83%81%EC%84%B8 | 기록 행을 누르면 상단 시약명·수량 요약 + 라벨-값 행(사용자·일시·메모) 상세로 들어가는 목록 → 상세 흐름 |

## 화면 11
| # | ui_url | 가져올 것 |
|---|---|---|
| 1 | https://uibowl.io/name/BookMyShow?patterns=%EC%98%88%EC%95%BD%C2%B7%EA%B2%B0%EC%A0%9C&patternName=3.%EC%A2%8C%EC%84%9D%20%EC%84%A0%ED%83%9D | 단(행) 라벨을 왼쪽에 두고 칸을 같은 크기 격자로 나열한 배치도 + 격자 아래 상태 범례(미지정·선택·분류별) 한 줄 |
| 2 | https://uibowl.io/name/Frontier%20Airlines?patterns=%EC%98%88%EC%95%BD%C2%B7%EA%B2%B0%EC%A0%9C&patternName=%EC%A2%8C%EC%84%9D%20%EC%84%A0%ED%83%9D | 양문형일 때 좌·우 문을 가운데 통로처럼 갈라 두 칸 묶음으로 보여주고 상단에 열(문) 라벨, 격자 아래 접이식 범례 + 하단 전폭 저장 버튼 |
| 3 | https://uibowl.io/name/%ED%85%8C%EC%8A%AC%EB%9D%BC%20(Tesla)?patterns=%EC%A0%9C%EC%96%B4&patternName=%EC%B0%A8%EB%9F%89%EC%BB%A8%ED%8A%B8%EB%A1%A4 | 시약장 정면 도식 위의 칸을 직접 눌러 설정하는 방식(칸 안에 현재 분류 라벨 표기), 누르면 바텀시트로 분류 칩 선택 |
| 4 | https://uibowl.io/name/LG%20ThinQ?patterns=%EC%A0%9C%EC%96%B4&patternName=%EA%B1%B4%EC%A1%B0%EA%B8%B0 | 상단에 문 형태(양문형/단문형)·단 수(3단/4단)를 탭·세그먼트로 먼저 고르게 하고, 그 아래 도식이 즉시 바뀌는 위→아래 설정 순서 |
| 5 | https://uibowl.io/name/G%20car?patterns=%EC%8B%A0%EC%B2%AD%ED%95%98%EA%B8%B0&imgId=cmo85af8n00fcjr04s5erd4yk | 위험 조합 경고를 격자와 저장 버튼 사이의 구분 영역에 '주의사항' 글머리 목록으로 두고, 선택용 칩은 그 아래 한 줄로 배치 |

## 화면 12
| # | ui_url | 가져올 것 |
|---|---|---|
| 1 | https://uibowl.io/name/%EC%B9%B4%EC%B9%B4%EC%98%A4T?patterns=%EC%B4%AC%EC%98%81%ED%95%98%EA%B8%B0&patternName=QR%EC%8A%A4%EC%BA%94-%EC%9E%90%EC%A0%84%EA%B1%B0%20%EB%B0%98%EB%82%A9 | 상단 안내 2줄 → 가운데 프레임 → 플래시 버튼 → 최하단 '시약장 번호로 찾기' 수동 대안 고정의 세로 배치 |
| 2 | https://uibowl.io/name/%EB%B3%BC%ED%8A%B8%EC%97%85?patterns=%EC%B4%AC%EC%98%81%ED%95%98%EA%B8%B0&patternName=QR%EC%8A%A4%EC%BA%94 | 안내 문구에 "시약장 문에 붙은 QR"처럼 부착 위치를 명시하고, 스캔/직접 입력을 같은 화면 상단 탭으로 전환 |
| 3 | https://uibowl.io/name/%EB%A7%88%EB%AF%B8%ED%86%A1?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&imgId=cmpcmrk8h01s0jl04xuxmaavu | 카메라 권한 거부 상태를 프레임 자리에 안내 문구 + 권한 설정 버튼으로 처리하고 수동 대안은 하단에 그대로 유지 |
| 4 | https://uibowl.io/name/%EB%8B%A5%ED%84%B0%EB%8B%A4%EC%9D%B4%EC%96%B4%EB%A6%AC?patterns=%EC%B4%AC%EC%98%81%ED%95%98%EA%B8%B0&imgId=cmr7e4uyx00diju04jj009eeh | 상단 바에 닫기·플래시를 양끝 배치하고 코너 브라켓 프레임을 쓰는 구조 |
| 5 | https://uibowl.io/name/%EB%B9%BD%EB%8B%A4%EB%B0%A9?patterns=%EC%BF%A0%ED%8F%B0&imgId=cmsqw7eev001si604q3io8gzt | 인식 실패·다른 학교 QR일 때 별도 화면 없이 인라인 1줄 안내 + 다른 입력 수단 제시 |
