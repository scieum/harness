# S1 채택 — runs/20261011-0813

구조·흐름·배치만 가져온다. 색·폰트·모서리는 design.md / rules.json을 따른다.

## 화면 2
| # | ui_url | 가져올 것 |
|---|---|---|
| 1 | https://uibowl.io/name/%EC%B9%B4%EC%B9%B4%EC%98%A4%EA%B3%A8%ED%94%84%EC%98%88%EC%95%BD?patterns=%EA%B2%80%EC%83%89&imgId=cmtwlue90002bjw04hgtwofel | 선택 모드에서 목록 맨 위에 '전체 선택' 행을 두고 같은 줄 오른쪽에 선택 개수를 표시 |
| 2 | https://uibowl.io/name/%EB%9D%BC%EC%9A%B4%EC%A6%88?patterns=%EC%9E%A5%EB%B0%94%EA%B5%AC%EB%8B%88&imgId=cmunlyn8s0005l804bcsbpzcr | 각 행 맨 왼쪽에 체크박스를 두고 행 내용은 그대로 오른쪽으로 밀어 배치 |
| 3 | https://uibowl.io/name/%EC%97%90%EC%9D%B4%EB%8B%B7?patterns=%ED%8E%B8%EC%A7%91%C2%B7%EC%88%98%EC%A0%95%ED%95%98%EA%B8%B0&imgId=cmtwlvjdt001lju04v7bmhhvn | 아래 고정 띠(취소/삭제) → 삭제 시 중앙 확인 모달로 개수를 다시 묻는 2단계 흐름 |
| 4 | https://uibowl.io/name/%EB%B9%84%EA%B8%80%EB%A3%A8?patterns=%EB%B6%81%EB%A7%88%ED%81%AC%C2%B7%EC%9C%84%EC%8B%9C%EB%A6%AC%EC%8A%A4%ED%8A%B8&imgId=cmpq8q4b2001rju042pzt4qlh | 선택 모드는 화면 머리를 '선택' 상태로 바꾸고 닫기(X)로 빠져나오는 구조 |

## 화면 10
| # | ui_url | 가져올 것 |
|---|---|---|
| 1 | https://uibowl.io/name/%EB%A7%88%EB%AF%B8%ED%86%A1?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&patternName=%EC%B2%B4%EC%A4%91%20%EA%B8%B0%EB%A1%9D%20%EC%B6%94%EA%B0%80 | 기록 목록 머리(제목·필터 줄) 오른쪽에 '+ 추가' 버튼을 붙여 목록 위에서 바로 진입 |
| 2 | https://uibowl.io/name/%EC%97%B4%ED%92%88%ED%83%80?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&patternName=%EA%B8%B0%EB%A1%9D%20%EC%B6%94%EA%B0%80 | 추가 후 새 기록이 목록의 해당 날짜 위치에 끼워져 보이는 흐름 |
| 3 | https://uibowl.io/name/%EB%A7%88%EB%AF%B8%ED%86%A1?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&patternName=%EC%84%B1%EC%9E%A5%20%EA%B8%B0%EB%A1%9D%20%EC%B6%94%EA%B0%80 | 추가 폼은 맨 위 날짜 → 입력칸 → 맨 아래 전체 폭 저장 버튼 고정 순서 |

## 화면 13
| # | ui_url | 가져올 것 |
|---|---|---|
| 1 | https://uibowl.io/name/Kia?patterns=%EB%A9%94%EC%9D%B8&imgId=cmpur0a3g000dl504qp9o8f4s | 요약 타일 제목에 '점검 필요 N'처럼 건수를 숫자로 넣고 타일 전체를 해당 목록으로 가는 링크로 |
| 2 | https://uibowl.io/website/%EB%A7%88%EC%9D%B4%ED%81%AC%EB%A1%9C%EC%86%8C%ED%94%84%ED%8A%B8%20%ED%81%B4%EB%9E%98%EB%A6%AC%ED%8B%B0%20(Microsoft%20Clarity)?patterns=%EB%A9%94%EC%9D%B8&patternName=%EB%8C%80%EC%8B%9C%EB%B3%B4%EB%93%9C | 요약 타일은 같은 크기로 한 줄에 나란히(라벨 위·숫자 아래) 놓고 기존 타일 줄에 1칸 추가 |
| 3 | https://uibowl.io/name/%EB%B3%B4%EB%A7%B5?patterns=%EB%A9%94%EC%9D%B8&imgId=cmr2zjo33000iij04gv6ptj59 | 404는 앱 틀(머리·탭바)을 유지한 채 본문 가운데 아이콘·제목·설명·'홈으로' 버튼 1개 |

## 화면 14
| # | ui_url | 가져올 것 |
|---|---|---|
| 1 | https://uibowl.io/name/%ED%8E%98%EC%9D%B4%EC%BD%94?patterns=%EB%A1%9C%EA%B7%B8%EC%9D%B8%C2%B7%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85&imgId=cmupp0tss0016l904iev4lrxz | 오류 요약 박스 구조(아이콘 + 제목 1줄 + 설명)와 해당 칸 강조를 함께 쓰는 2중 표시 |
| 2 | https://uibowl.io/name/EVSIS?patterns=%EB%A1%9C%EA%B7%B8%EC%9D%B8%C2%B7%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85&imgId=cmokqecp5001dkw04pg7dqabn | 제출 오류 요약을 주 버튼 바로 위에 두어 누른 자리에서 바로 보이게 배치 |
| 3 | https://uibowl.io/name/%EB%A7%88%EC%9D%B4%ED%98%84%EB%8C%80?patterns=%EB%A1%9C%EA%B7%B8%EC%9D%B8%C2%B7%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85&imgId=cmojm0qqb00iejs043ihvynj2 | 긴 폼에서는 문제 칸에만 칸 아래 안내 문구를 붙이고 나머지 칸은 그대로 |
| 4 | https://uibowl.io/name/%EC%88%98%ED%98%84%EC%9D%B4%EB%9E%91?patterns=%EC%9D%B8%EC%A6%9D%ED%95%98%EA%B8%B0&imgId=cmouxls7i0010k004p8404isj | 서버 오류(입력과 무관)는 칸이 아닌 폼 수준 한 줄로 분리해 표시 |

## 화면 15
| # | ui_url | 가져올 것 |
|---|---|---|
| 1 | https://uibowl.io/website/%EC%9C%84%EC%8B%9C%EC%BC%93?patterns=%EB%A9%94%EC%9D%B8 | 섹션 그림 자리에 실제 제품 화면 조각을 잘라 넣는 방식(조각 단위로 교체) |
| 2 | https://uibowl.io/website/%ED%94%BC%EC%B2%98%EB%A7%81?patterns=%EB%9E%9C%EB%94%A9%ED%8E%98%EC%9D%B4%EC%A7%80&imgId=cmuz1dxh50003jp045amg9m8u | 제품 캡처는 섹션 레이아웃은 그대로 두고 그림 영역 크기에 맞춰 잘라 배치 |
| 3 | https://uibowl.io/website/%EB%A6%AC%EC%8A%A4%EB%8B%9D%EB%A7%88%EC%9D%B8%EB%93%9C?patterns=%EB%9E%9C%EB%94%A9%ED%8E%98%EC%9D%B4%EC%A7%80&imgId=cmsssa2md000vl404rq691ip5 | 기능 설명 섹션의 그림은 해당 기능 목록 조각(행 2~3개)만 보여주는 크롭 |

## 화면 17
| # | ui_url | 가져올 것 |
|---|---|---|
| 1 | https://uibowl.io/name/Kia?patterns=%EB%82%B4%EC%97%AD&imgId=cmpuohezz0015k104h5xybl51 | 목록 행: 굵은 장비명 + 아래 '회사 · 모델 · 수량' 한 줄 + 오른쪽 위 상태 배지 |
| 2 | https://uibowl.io/name/%ED%97%A4%EC%9D%B4%EB%94%9C%EB%9F%AC?patterns=%EC%A1%B0%ED%9A%8C%ED%95%98%EA%B8%B0&imgId=cmliqgu3b000ule04taw4hhl7 | 상세: 머리에 장비명 크게, 아래 라벨-값 2열 행(회사·모델·수량·상태·위치) |
| 3 | https://uibowl.io/name/%EC%99%93%EC%84%AD?patterns=%ED%8E%B8%EC%A7%91%C2%B7%EC%88%98%EC%A0%95%ED%95%98%EA%B8%B0&imgId=cmqt8b6x80014kz040po6xf03 | 브랜드 고르기: 맨 위 검색칸 + 결과 목록, 선택 행에 '선택됨' 라벨·체크 표시 |
| 4 | https://uibowl.io/name/%EC%A7%81%EB%B0%A9%20%EC%8A%A4%EB%A7%88%ED%8A%B8%EB%8F%84%EC%96%B4%EB%9D%BD?patterns=%EC%8B%A0%EC%B2%AD%ED%95%98%EA%B8%B0&imgId=cmco48dn3000bkz07v19ohvuw | 빈 상태: 가운데 아이콘·제목·설명 2줄, 맨 아래 전체 폭 '장비 등록' 버튼 |
| 5 | https://uibowl.io/name/%EC%BD%94%EC%9B%A8%EC%9D%B4%20IoCare%2B?patterns=%EB%A9%94%EC%9D%B8 | 분류 칩 탭을 유지한 채 본문만 빈 상태로 바꾸고 가운데 등록 버튼으로 이어지는 흐름 |
