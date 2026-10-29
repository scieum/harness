# S1 가져올 것 — run 20261027-1613

- 구조·흐름·배치만. 색·폰트·모서리는 docs/design.md · rules.json이 정한다.

## 화면 13
| # | ui_url | 가져올 것 |
|---|---|---|
| 1 | https://uibowl.io/website/%ED%94%BC%EC%B2%98%EB%A7%81?patterns=AI&imgId=cmuz1dsag000ll304xjrioyls | 사이드바 주 메뉴와 떨어진 아래쪽 보조 묶음에 guide-link '사용 가이드 ↗'를 한 행으로 둠 |
| 2 | https://uibowl.io/website/%ED%9E%89%EC%8A%A4%ED%95%84%EB%93%9C%20(Higgsfield)?patterns=%EB%A7%88%EC%9D%B4%ED%8E%98%EC%9D%B4%EC%A7%80&imgId=cmtrw3r7g003aib04cnmeic4y | 도움 진입은 사이드바 바닥 쪽(계정·학교 정보 바로 위)에 붙여 주 메뉴 흐름을 끊지 않음 |
| 3 | https://uibowl.io/website/Npay%20%EC%A6%9D%EA%B6%8C?patterns=%EA%B3%A0%EA%B0%9D%EC%84%BC%ED%84%B0%C2%B7FAQ&imgId=cmvg2hf390003jh061i12flxl | 도움말 항목을 메뉴 목록 아래 별도 항목으로 두되 메뉴 행과 같은 행 높이·들여쓰기를 유지 |

## 화면 14
| # | ui_url | 가져올 것 |
|---|---|---|
| 1 | https://uibowl.io/name/%EB%AF%B8%EB%8B%88%EC%8A%A4%ED%83%81?patterns=%EC%95%BD%EA%B4%80%EB%8F%99%EC%9D%98&imgId=cmty2llwu002pl704p152k9w2 | 동의 행 = 왼쪽 체크 + 라벨 + 오른쪽 끝 펼침 아이콘, 펼침 아이콘만 눌러 내용을 여는 구조 |
| 2 | https://uibowl.io/name/%ED%94%8C%EB%A6%AC%ED%86%A0?patterns=%EC%95%BD%EA%B4%80%EB%8F%99%EC%9D%98&imgId=cmvisjbbi0044k108s5hbqpkk | 펼친 privacy-consent-detail 안에 수집 항목·목적·보유 기간을 항목별로 짧게 나열 |
| 3 | https://uibowl.io/name/iM%EB%B1%85%ED%81%AC?patterns=%EB%A1%9C%EA%B7%B8%EC%9D%B8%C2%B7%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85&imgId=cmp0ugm9t002yky04s0u5cd5l | 펼친 내용은 부모 동의 행 아래 들여쓴 하위 목록으로 붙여 어느 동의의 세부인지 바로 보이게 |
| 4 | https://uibowl.io/name/%EB%A7%88%EC%9D%B4%ED%98%84%EB%8C%80?patterns=%EB%A1%9C%EA%B7%B8%EC%9D%B8%C2%B7%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85&imgId=cmojm0g540005jp04b2jrd3g6 | 전문 보기는 버튼이 아닌 텍스트 링크 한 줄(privacy-link '개인정보 처리방침 전문 보기 ↗') |
| 5 | https://uibowl.io/name/%EC%84%B8%EC%9D%B4%EB%B8%8C%20(SAVE)?patterns=%EC%95%BD%EA%B4%80%EB%8F%99%EC%9D%98&imgId=cmuo3ak1j004bjp04fzibrcm5 | 항목 목록 다음 맨 끝에 처리방침 전문으로 넘기는 문장/링크를 두는 순서(항목 → 전문 링크) |

## 화면 15
| # | ui_url | 가져올 것 |
|---|---|---|
| 1 | https://uibowl.io/website/%EC%B9%B4%EC%B9%B4%EC%98%A4%ED%8E%98%EC%9D%B4%EC%A7%80?patterns=%EC%9D%B8%EC%A6%9D%ED%95%98%EA%B8%B0&imgId=cmtfgnm2b001xju044gyoj0mz | footer 링크 줄에서 '개인정보 처리방침'만 굵게 해 다른 링크와 구분 |
| 2 | https://uibowl.io/website/%EB%94%94%EB%A7%A8%EB%93%9C?patterns=%EB%A7%88%EC%9D%B4%ED%8E%98%EC%9D%B4%EC%A7%80&imgId=cmti7w8im000ykz040a1ads80 | footer-links를 web-footer 뒤 한 줄에 두 링크를 구분선(|)으로 나란히 배치 |
| 3 | https://uibowl.io/website/%EB%A6%AC%EB%B8%94?patterns=%EB%A1%9C%EA%B7%B8%EC%9D%B8%C2%B7%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85&imgId=cmuc27ubo000cl804kuclzweh | 로그인 전 화면에서도 링크 2개만 짧게 한 줄로 두어 본문 흐름을 방해하지 않음 |

## 화면 18
| # | ui_url | 가져올 것 |
|---|---|---|
| 1 | https://uibowl.io/name/%EC%97%90%EC%9D%B4%EB%B8%94%EB%A6%AC?patterns=%EB%A7%88%EC%9D%B4%ED%8E%98%EC%9D%B4%EC%A7%80&imgId=qb6brliqfji7q5h65lsvu2r7 | 관리 탭 목록 끝에 묶음 제목 '도움말'을 두고 그 아래 행으로 가이드·처리방침 등을 묶음 |
| 2 | https://uibowl.io/name/%ED%8E%98%EC%9D%B4%ED%9E%88%EC%96%B4?patterns=%EC%84%A4%EC%A0%95&imgId=cmnfn0a7v0003jt04b35hxklt | '사용 가이드' 한 행을 다른 설정 행과 같은 형태로, 오른쪽 끝 표시만 외부 이동(↗)으로 바꿈 |
| 3 | https://uibowl.io/name/%ED%81%AC%EB%AA%BD?patterns=%EB%A7%88%EC%9D%B4%ED%8E%98%EC%9D%B4%EC%A7%80&imgId=cmopqffvu000fjl04q4jpxiog | 도움말 묶음은 기능 묶음들 뒤 맨 아래에 두어 주요 관리 항목보다 뒤 순서 |
| 4 | https://uibowl.io/name/%EC%A0%9C%ED%8E%98%ED%86%A0?patterns=%EC%84%A4%EC%A0%95&imgId=cmulc9f7c001fl2049rgd1hj4 | 문서·가이드 링크 묶음을 구분선으로 다른 묶음과 나눠 둘러보기(guest)에서도 같은 위치에 유지 |
| 5 | https://uibowl.io/name/Keepin?patterns=%EC%84%A4%EC%A0%95&imgId=cm0lpx4rh001ul80cz8hgnetu | 외부로 나가는 행은 같은 목록 행 안에서 오른쪽 끝 보조 표시로만 구분(행 구조 동일) |

## 화면 19
| # | ui_url | 가져올 것 |
|---|---|---|
| 1 | https://uibowl.io/name/%EB%82%98%EB%A7%8C%EC%9D%98%EB%8B%A5%ED%84%B0?patterns=%EC%95%BD%EA%B4%80%EB%8F%99%EC%9D%98&imgId=cm74d146z006dii0conp0ldug | privacy-doc 머리 순서 = 제목 → 머리말 문단 → 시행일 한 줄 → privacy-toc |
| 2 | https://uibowl.io/name/%EA%B5%AC%EA%B8%80%20%EC%A0%9C%EB%AF%B8%EB%82%98%EC%9D%B4%20(Google%20Gemini)?patterns=%EA%B3%B5%EC%A7%80%EC%82%AC%ED%95%AD&imgId=cmto3us98001ol4044rol8igk | 모바일 privacy-toc = '목차' 제목 아래 조항 이름 링크 세로 목록(누르면 해당 조항으로 이동) |
| 3 | https://uibowl.io/name/%EB%B9%BC%EA%B8%B0?patterns=%EA%B3%B5%EC%A7%80%EC%82%AC%ED%95%AD&imgId=cmsu3827y000gji04vsqgeimy | 위탁 조항의 privacy-table = 3열(구분·수탁자·위탁 업무) 표, 조항 소제목 바로 아래 |
| 4 | https://uibowl.io/name/%EB%B0%B0%EB%8B%AC%EC%9D%98%EB%AF%BC%EC%A1%B1?patterns=%EA%B3%B5%EC%A7%80%EC%82%AC%ED%95%AD&imgId=cmni7hqmb0015jg04xstayb73 | 조항마다 소제목 + 글머리표 짧은 줄로 끊고 표는 좁은 모바일 폭에서 셀 안 줄바꿈 허용 |
| 5 | https://uibowl.io/website/%EB%A6%AC%EB%94%94?patterns=%EA%B3%A0%EA%B0%9D%EC%84%BC%ED%84%B0%C2%B7FAQ&imgId=cmuq7edsw0017kz04purwnq87 | 데스크톱은 왼쪽 고정 목차 + 오른쪽 넓은 본문 2열, 본문 끝 뒤에 web-footer |
