# S1 채택 — 20261008-1610 (구조·흐름·배치만. 색·폰트·모서리는 design.md)

## 화면 16
| # | ui_url | 가져올 것 |
|---|---|---|
| 1 | https://uibowl.io/website/%EB%A7%A4%EB%8B%88%ED%8C%A8%EC%8A%A4%ED%8A%B8?patterns=%ED%81%90%EB%A0%88%EC%9D%B4%EC%85%98&imgId=cmulyw7j9001qjj04bmlsz9l1 | 16-loading/fail: detail-drawer 머리(제목·출처 줄)와 data-table은 그대로 두고 drawer 몸통만 실제 항목 순서(신호어 → 그림문자 → 항목 2·4·7·8) 모양의 msds-skeleton 줄로 채우며, 실패 시 같은 자리를 ex-empty-state-card + 아래 msds-original-link로 바꾼다 |
| 2 | https://uibowl.io/website/%ED%98%81%EC%8B%A0%EC%9D%98%EC%88%B2?patterns=%ED%95%84%ED%84%B0&imgId=cmiqzsrbu001ol404pjyckvpt | 2-filter/filter-empty·11-empty: 필터는 list-filter-button 아래 드롭다운 패널로 열고 적용 조건은 표 위 filter-chip-row에 남기며, 결과 0이면 표 열 제목을 유지한 채 표 몸통 가운데에 ex-empty-state-card + '필터 지우기' 버튼을 둔다 |
| 3 | https://uibowl.io/website/%EC%9E%94%EB%94%94?patterns=%EA%B8%B0%ED%83%80&imgId=cmpz4uagr000ajs04zj40zdih | 3-location·11-slot·7-suggest·msds 후보: 모바일 바텀시트 대신 누른 컨트롤(위치 칸·칸 셀·MSDS 찾기 버튼) 바로 아래에 붙는 팝오버로 열고 뒤를 어둡게 하지 않으며, 후보 0개면 팝오버 안에 빈 문구 + 동작 버튼 1개('직접 입력' 등)를 둔다 |
| 4 | https://uibowl.io/website/%EB%AF%B8%EB%A6%AC%EC%BA%94%EB%B2%84%EC%8A%A4?patterns=%EC%B7%A8%EC%86%8C%ED%95%98%EA%B8%B0&imgId=cmdzoh62g0025lb07uuyajbap | 11-delete·11-unsaved: 사이드바까지 덮는 가운데 ex-modal-card 하나로 질문형 제목 → 결과 설명(예: '시약은 칸 없음으로 남아요') → 오른쪽 아래 보조(계속 편집/취소) + 주(버리고 이동/삭제) 순서로 배치하고 × 닫기를 둔다 |
| 5 | https://uibowl.io/website/%EC%82%AC%EB%B0%A9%EB%84%B7?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&imgId=cmu4rq9d8000xjm04y191pizg | 7-doc-upload→doc-review(·doc-fail·12-result): 입고는 사이드바를 유지한 페이지에서 위 줄 intake-mode + doc-upload(파일 칸·형식/용량 안내)를 두고, 업로드 뒤 같은 페이지 아래가 전폭 doc-intake-table(품명·규격·수량 + 행마다 reagent-link)로 바뀌는 한 페이지 흐름으로 만든다 |
