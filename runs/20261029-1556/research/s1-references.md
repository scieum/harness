# S1 레퍼런스 — run 20261029-1556

- 대상: 화면 13(13-desktop 사이드바 board-link만) · 14(상태 14-consent, 약관 age-confirm 줄) · 18(관리 탭 '도움말' 묶음에 board-link) · 20(새 화면 게시판, 상태 20-detail·new·empty·student)
- 출처: 이번 uibowl 검색 결과의 ui_url만 사용 (search_by_ocr_text "만 14세 이상"×약관동의 / "게시판"(PC) / "문의"(PC)×사이드 네비게이션 / "고객센터"(PC)×사이드 네비게이션 / "문의하기"×마이페이지 / "답변완료"×문의하기 / "답변 내용"×문의하기 · search_ui_patterns 문의하기 · search_components 아코디언×고객센터·FAQ)
- 오케스트레이터 후보(캐시워크·롯데시네마·G car·퍼그샵·페이워크)는 이번 검색 결과에 ui_url이 나오지 않아 쓰지 않고, 같은 역할의 검색 결과로 바꿈

## 화면 13
| # | 앱 | ui_url | 화면 설명 |
|---|---|---|---|
| 1 | Npay 증권 | https://uibowl.io/website/Npay%20%EC%A6%9D%EA%B6%8C?patterns=%EA%B3%A0%EA%B0%9D%EC%84%BC%ED%84%B0%C2%B7FAQ&imgId=cmvg2hf390003jh061i12flxl | PC 왼쪽 세로 메뉴(프로필 아래 메뉴 목록) + 오른쪽 고객센터 본문 — FAQ 검색·자주 찾는 칩·FAQ 목록이 본문에, 고객센터 진입은 메뉴 목록 안 한 항목 |
| 2 | KRDS | https://uibowl.io/website/KRDS?patterns=%EB%AC%B8%EC%9D%98%ED%95%98%EA%B8%B0&imgId=cmnqqy3l80004i90485kh3whj | PC 왼쪽 하위 메뉴(소식·소통: 새소식·자주 묻는 질문·적용 사례·문의 및 건의·용어 사전) 중 '문의 및 건의'가 현재 항목으로 표시, 오른쪽 본문 = 제목 → 안내 상자 → 분류·검색 → 게시글 목록 |
| 3 | 레뷰 (REVU) | https://uibowl.io/website/%EB%A0%88%EB%B7%B0%20(REVU)?patterns=%EB%82%B4%EC%97%AD&imgId=cmvepnf0c000sl606tagx4sv7 | PC 왼쪽 사이드 메뉴가 묶음 제목(활동관리·계정관리·고객센터)으로 나뉘고, 문의 항목이 맨 아래 '고객센터' 묶음에 같은 행 모양으로 들어감 |

## 화면 14
| # | 앱 | ui_url | 화면 설명 |
|---|---|---|---|
| 1 | 석가머니 | https://uibowl.io/name/%EC%84%9D%EA%B0%80%EB%A8%B8%EB%8B%88?patterns=%EC%95%BD%EA%B4%80%EB%8F%99%EC%9D%98&imgId=cmvfy6yjy0039l706526nm0qq | 모바일 약관 바텀시트 — 회색 상자 '모두 동의해요' 아래 체크 행 4줄, 마지막 줄이 '만 14세 이상이에요 (필수)', 약관 행만 오른쪽 '보기' |
| 2 | 앳플리 | https://uibowl.io/name/%EC%95%B3%ED%94%8C%EB%A6%AC?patterns=%EC%95%BD%EA%B4%80%EB%8F%99%EC%9D%98&imgId=cmtpoktbe003gkz04h7vfsb8a | 모바일 회원가입 약관 — '[필수] 만 14세 이상입니다.' 행이 다른 약관 행과 같은 체크 행 모양, 약관 행은 오른쪽 › / 나이 행은 › 없음, 아래 고정 '모두 동의' |
| 3 | 미소 | https://uibowl.io/name/%EB%AF%B8%EC%86%8C?patterns=%EC%95%BD%EA%B4%80%EB%8F%99%EC%9D%98&imgId=cmqt6jy3n00mvjp04xw22obmk | 모바일 동의 바텀시트 — '[필수] 미소 이용약관 및 동의사항' 묶음을 펼치면(⌃) 들여쓴 하위 체크 줄에 '14세 이상 성인입니다'가 포함, 아래 '모두 동의하기' |

## 화면 18
| # | 앱 | ui_url | 화면 설명 |
|---|---|---|---|
| 1 | 차란 | https://uibowl.io/name/%EC%B0%A8%EB%9E%80?patterns=%EB%A7%88%EC%9D%B4%ED%8E%98%EC%9D%B4%EC%A7%80&imgId=cmtwj2vr0000njr04c0puv2kw | 모바일 마이 탭 — 굵은 묶음 제목(판매·고객센터·앱 설정·정보) 아래 › 행, '고객센터' 묶음 = 공지사항 · FAQ · 문의하기 3줄 |
| 2 | 빼기 | https://uibowl.io/name/%EB%B9%BC%EA%B8%B0?patterns=%EB%A7%88%EC%9D%B4%ED%8E%98%EC%9D%B4%EC%A7%80&imgId=cmsu39z4z00eajv04guutwvzj | 모바일 마이페이지 — '나의 거래' 묶음 뒤 '고객지원' 묶음, 아이콘 + 라벨 + › 행으로 공지사항 · 자주 묻는 질문(FAQ) · 1:1 문의하기 · 시스템 설정 |
| 3 | 보맵 | https://uibowl.io/name/%EB%B3%B4%EB%A7%B5?patterns=%EB%A7%88%EC%9D%B4%ED%8E%98%EC%9D%B4%EC%A7%80&imgId=cmr2zi6fs0006l104cnmb2duz | 모바일 마이 탭 — 위 카드 2개 아래 아이콘 + 라벨 + › 목록, '문의하기'가 공지사항·설정과 같은 행 모양으로 나열 |

## 화면 20
| # | 앱 | ui_url | 화면 설명 |
|---|---|---|---|
| 1 | 오일나우 | https://uibowl.io/name/%EC%98%A4%EC%9D%BC%EB%82%98%EC%9A%B0?patterns=%EB%AC%B8%EC%9D%98%ED%95%98%EA%B8%B0&imgId=cmtpnvv5p001ajo04pqnetzma | 모바일 문의 목록 — 머리 오른쪽 '문의하기' 알약 버튼, 행 = 제목(굵게) / 아래 메타 줄 '답변대기 · 작성자 · 날짜', 행 사이 얇은 구분선 |
| 2 | 라이프캐치 | https://uibowl.io/name/%EB%9D%BC%EC%9D%B4%ED%94%84%EC%BA%90%EC%B9%98?patterns=%EB%AC%B8%EC%9D%98%ED%95%98%EA%B8%B0&imgId=cmqzb48yx003yju04rnwhv1yb | 모바일 고객센터 — 위 탭 '자주 묻는 질문 | 나의 문의 내역', 내 문의 탭이 비었을 때 가운데 아이콘 + '문의 내역이 없습니다.' + 아래 전폭 '1:1 문의하기' |
| 3 | 젠디 | https://uibowl.io/name/%EC%A0%A0%EB%94%94?patterns=%EA%B3%A0%EA%B0%9D%EC%84%BC%ED%84%B0%C2%B7FAQ&imgId=cmradcdot0027k204q9o4qkmx | 모바일 자주 묻는 질문 — 'Q' 한 줄 질문 행 + 오른쪽 ⌄, 첫 행이 펼쳐져(⌃) 같은 카드 안 질문 아래 답 문단 |
| 4 | 해피문데이 | https://uibowl.io/name/%ED%95%B4%ED%94%BC%EB%AC%B8%EB%8D%B0%EC%9D%B4?patterns=%EB%AC%B8%EC%9D%98%ED%95%98%EA%B8%B0&imgId=cmtwleq9n0044l704bgq32c1l | 모바일 의견과 제안 작성 — 안내 문단 → '제안 유형' 선택 상자 → '내용' 큰 입력 → 전폭 '보내기'(비활성) → 글머리표 안내(개인정보 관련 포함) |
| 5 | 쏘카 | https://uibowl.io/name/%EC%8F%98%EC%B9%B4?patterns=%EB%AC%B8%EC%9D%98%ED%95%98%EA%B8%B0&imgId=cmogjptrp02kpl104qg664v7v | 모바일 내 문의 상세 — 큰 제목 옆 작은 '답변 대기 중' 배지, 아래 날짜(회색) → 본문 문단, 위 ‹ 뒤로 |
