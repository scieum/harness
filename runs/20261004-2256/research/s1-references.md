# S1 레퍼런스 — run 20261004-2256

대상 화면: 11 (variants: empty, delete) (docs/PRD.md §7)
이번 run은 "여러 개를 전환·관리하는 UI"(전환 칩 + 끝 "+ 추가", 이름 바꾸기·삭제, 삭제 확인 모달, 0개 빈 상태)를 새로 검색했다. 배치도 격자 자체는 run 20261002-1301 화면 11 레퍼런스를 그대로 따른다.

## 화면 11
| # | 앱 | ui_url | 화면 설명 |
|---|---|---|---|
| 1 | 달다방 | https://uibowl.io/name/%EB%8B%AC%EB%8B%A4%EB%B0%A9?patterns=iPhone%20%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7&imgId=cmuc8ychu001ljz04gcquihao | 멀티프로필 전환: '프로필 변경' 패널에 프로필 항목이 가로 한 줄로 놓이고(현재 항목은 테두리 강조), 줄 맨 끝에 같은 크기의 '+ 프로필 추가' 항목 |
| 2 | 헬로우봇 | https://uibowl.io/name/%ED%97%AC%EB%A1%9C%EC%9A%B0%EB%B4%87?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&imgId=cmr8u4gy30006jo04su091j5r | 대상 전환 바텀시트: 상단 한 줄에 '+' 원형 버튼 → 선택된 이름 칩, 같은 줄 우측 끝에 설정(톱니) 아이콘, 아래 카드에 선택 항목의 속성 행(이름·생년월일 등 + ›)과 하단 전폭 '확인' |
| 3 | 커리어톡 | https://uibowl.io/name/%EC%BB%A4%EB%A6%AC%EC%96%B4%ED%86%A1?patterns=%EB%B6%81%EB%A7%88%ED%81%AC%C2%B7%EC%9C%84%EC%8B%9C%EB%A6%AC%EC%8A%A4%ED%8A%B8&imgId=cmf0p85wt000hl704ad3u3tqc | 보드 삭제 및 편집: 보드 메뉴에서 '이름 변경' 진입 시 바텀시트에 뒤로가기 + 제목, 단일 텍스트 필드(글자 수 8/10자 표시), 전폭 '저장' |
| 4 | 퍼그샵 | https://uibowl.io/name/%ED%8D%BC%EA%B7%B8%EC%83%B5?patterns=%EA%B3%84%EC%A2%8C&imgId=cmq7evao00095l204e0ekhshk | 계좌 삭제 확인 모달: 1줄 질문 "정말로 내 계좌를 삭제하시겠어요?" + 결과 안내 2줄(복구 불가, 이미 신청한 요청은 그대로 진행) + 취소/삭제하기 가로 2버튼, 뒤 편집 시트 맨 아래에 '삭제하기' 버튼 |
| 5 | 볼트업 | https://uibowl.io/name/%EB%B3%BC%ED%8A%B8%EC%97%85?patterns=%EA%B0%84%ED%8E%B8%EA%B2%B0%EC%A0%9C&imgId=cmojeenh70003lh04lxsv019h | 결제수단 관리 0개: 섹션 제목 '등록한 카드 0'(개수 표시) 우측에 '추가하기' 버튼, 본문 중앙에 굵은 1줄 "등록된 결제수단이 없어요" + 보조 2줄 "[추가하기] 버튼을 눌러 … 등록해 주세요." |
