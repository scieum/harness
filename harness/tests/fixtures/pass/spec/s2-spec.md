# 화면 설계서

## 화면 14
### 구성 요소
- school-select-sido: 시/도 선택
- school-select-region: 지역(시/군/구) 선택
- school-select-school: 학교 선택
- button-primary: 주요 행동
### 반영한 레퍼런스
- https://uibowl.io/screen/101

## 화면 2
### 구성 요소
- button-primary: 주요 행동
### 반영한 레퍼런스
- https://uibowl.io/screen/201

## 역할별 노출
| 컴포넌트 | 학생 | 교사 | admin |
|---|---|---|---|
| manual-upload | 0 | 1 | 1 |
| reorder-alert-card | 0 | 1 | 1 |
| vendor-link | 0 | 1 | 1 |
| vendor-register | 0 | 0 | 1 |
| msds-entry | 1 | 1 | 1 |
| stock-intake | 0 | 1 | 1 |
| reagent-register | 0 | 1 | 1 |
| user-manage | 0 | 0 | 1 |
| cabinet-edit | 0 | 1 | 1 |
