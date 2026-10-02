# S1 채택 항목 — run 20261002-1223

구조·흐름·배치만 가져온다. 색·폰트·모서리는 docs/design.md를 따른다.

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
