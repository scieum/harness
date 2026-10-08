# S1 레퍼런스 — 20261008-1610 (데스크톱 1440 재구성 2차-b · 상태 프레임)

- 판정 단위: input.json screens = [16]. 레퍼런스는 상태 프레임 20종(2·3·4·7·11·12·16 variants) 데스크톱에 함께 쓴다.
- 출처: uibowl 검색 결과의 ui_url만 사용 (platform=PC). 3번은 refs/uibowl-desktop-web-20261008.md "6. 오버레이"의 uibowl 결과 값을 재사용.
- 사용한 검색: search_components 스켈레톤(PC) / 빈 화면 × 필터(PC) / 모달 × 삭제(PC) · search_by_ocr_text "엑셀 업로드"(PC) · search_ui_patterns 업로드 × 비즈니스툴(PC)
- 쓰임 구분: (a) 드로어 안 로딩·실패 → 16-loading·16-fail·16-no-summary · (b) 표 위 필터 패널·빈 결과 → 2-filter·2-filter-empty·11-empty · (c) 칸/위치 팝오버 → 3-location·11-slot·7-suggest·3-msds·2-msds-bulk·7-msds · (d) 확인 모달 → 11-delete·11-unsaved·11-print·4-past-date · (e) 업로드 → 결과 확인 표 → 7-doc-upload·7-doc-review·7-doc-fail·12-result

## 화면 16
| # | 앱 | ui_url | 화면 설명 |
|---|---|---|---|
| 1 | 매니패스트 | https://uibowl.io/website/%EB%A7%A4%EB%8B%88%ED%8C%A8%EC%8A%A4%ED%8A%B8?patterns=%ED%81%90%EB%A0%88%EC%9D%B4%EC%85%98&imgId=cmulyw7j9001qjj04bmlsz9l1 | (a) 생성 중 상태. 옆 패널은 위에 설명 문단을 남기고 그 아래 내용 자리를 회색 가로줄 스켈레톤으로 채운다. 본문 가운데에는 아이콘 + "PRD가 작성 중입니다." 제목 + 한 줄 안내, 그 아래 실제 문서 틀(제목 줄·항목 라벨)과 같은 모양의 스켈레톤 카드. 사이드 내비와 머리 탭은 그대로 남는다 |
| 2 | 혁신의숲 | https://uibowl.io/website/%ED%98%81%EC%8B%A0%EC%9D%98%EC%88%B2?patterns=%ED%95%84%ED%84%B0&imgId=cmiqzsrbu001ol404pjyckvpt | (b) 데이터룸 목록. 표 위에 드롭다운 필터 버튼 줄 2줄(조건마다 라벨 + ▾, 적용된 조건은 값·개수 표시), 그 아래 하위 탭 줄과 표 열 제목은 그대로 두고 표 몸통 자리에 가운데 정렬 빈 결과 문구 여러 줄 + 버튼 2개(테두리 / 채움) |
| 3 | 잔디 | https://uibowl.io/website/%EC%9E%94%EB%94%94?patterns=%EA%B8%B0%ED%83%80&imgId=cmpz4uagr000ajs04zj40zdih | (c) 헤더 아이콘에서 아래로 붙어 나오는 팝오버(약 430px). 뒤를 어둡게 하지 않고, 안에 빈 상태 문구 + 설명 + 동작 버튼 1개를 담는다 (refs 6번 표 재사용) |
| 4 | 미리캔버스 | https://uibowl.io/website/%EB%AF%B8%EB%A6%AC%EC%BA%94%EB%B2%84%EC%8A%A4?patterns=%EC%B7%A8%EC%86%8C%ED%95%98%EA%B8%B0&imgId=cmdzoh62g0025lb07uuyajbap | (d) 워크스페이스 삭제 확인. 사이드바가 있는 설정 화면 위에 전체를 어둡게 하고 가운데 모달(약 420px): 오른쪽 위 ×, 질문형 제목, 결과 설명 2~3줄, 확인용 입력칸, 동의 체크, 경고 박스, 오른쪽 아래 "취소"(보조) + 삭제(주) 버튼 |
| 5 | 사방넷 | https://uibowl.io/website/%EC%82%AC%EB%B0%A9%EB%84%B7?patterns=%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0&imgId=cmu4rq9d8000xjm04y191pizg | (e) 상품 대량 등록 페이지. 페이지 제목 아래 첫 줄에 파일 선택 칸 + 오른쪽 동작 버튼 묶음(엑셀자료선택·업로드), 그 아래 번호 붙은 업로드 안내 목록, 아래 전폭 표(No. · 항목 · 설명). 9장 흐름에서 업로드 후 결과 표로 이어진다. 모달이 아니라 사이드 레일 + 작업 탭을 유지한 페이지 |
