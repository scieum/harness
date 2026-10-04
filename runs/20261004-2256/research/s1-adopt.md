# S1 채택 항목 — run 20261004-2256

구조·흐름·배치만 가져온다. 색·폰트·모서리는 docs/design.md를 따른다.
배치도 격자·범례 구조는 기존(run 20261002-1301 화면 11)을 유지하고, 이번에는 그 위의 "시약장 전환·관리" 층과 empty/delete 변형만 정한다.

## 화면 11
| # | ui_url | 가져올 것 |
|---|---|---|
| 1 | https://uibowl.io/name/%EB%8B%AC%EB%8B%A4%EB%B0%A9?patterns=iPhone%20%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7&imgId=cmuc8ychu001ljz04gcquihao | 전환 칩 줄: 배치도 위에 "1번 / 2번 …" 시약장 칩을 가로 한 줄(넘치면 가로 스크롤)로 두고 현재 칩만 선택 상태, 줄 맨 끝에 같은 높이의 "+ 추가" 칩을 고정 |
| 2 | https://uibowl.io/name/%ED%97%AC%EB%A1%9C%EC%9A%B0%EB%B4%87?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&imgId=cmr8u4gy30006jo04su091j5r | 관리 진입 위치: 전환 칩 줄의 우측 끝(칩 줄 밖)에 더보기/설정 아이콘 1개를 두어 현재 선택된 시약장에 대한 메뉴를 여는 구조, 칩 줄 아래는 선택 시약장의 속성(문 형태·단 수) 행 |
| 3 | https://uibowl.io/name/%EC%BB%A4%EB%A6%AC%EC%96%B4%ED%86%A1?patterns=%EB%B6%81%EB%A7%88%ED%81%AC%C2%B7%EC%9C%84%EC%8B%9C%EB%A6%AC%EC%8A%A4%ED%8A%B8&imgId=cmf0p85wt000hl704ad3u3tqc | 메뉴(이름 바꾸기 / 삭제) → '이름 바꾸기'는 바텀시트 1단계(제목 + 단일 입력 필드 + 글자 수 표시 + 전폭 저장)로 처리, 삭제는 메뉴 마지막 항목 |
| 4 | https://uibowl.io/name/%ED%8D%BC%EA%B7%B8%EC%83%B5?patterns=%EA%B3%84%EC%A2%8C&imgId=cmq7evao00095l204e0ekhshk | 삭제 확인 모달 문구 구조: 질문 1줄 "{N번 시약장}을 삭제할까요?" → 결과 안내 1~2줄(칸 배정이 해제되고 시약은 '미배정'으로 남음, 되돌릴 수 없음) → 취소(좌)/삭제(우) 가로 2버튼 |
| 5 | https://uibowl.io/name/%EB%B3%BC%ED%8A%B8%EC%97%85?patterns=%EA%B0%84%ED%8E%B8%EA%B2%B0%EC%A0%9C&imgId=cmojeenh70003lh04lxsv019h | 0개 빈 상태: 제목 줄에 "시약장 0" 개수 + 우측 '추가하기' 버튼 유지, 배치도 자리 중앙에 굵은 1줄 "등록된 시약장이 없어요" + 보조 1줄 "[추가하기]를 눌러 시약장을 만들어 주세요" |
