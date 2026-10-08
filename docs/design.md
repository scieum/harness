## Overview

Lab_Stock is a SaaS for school science labs (elementary, middle and high school — widened from high school only on 2026-10-07) — it tracks each reagent's type, stock level, intake date, usage date, and user, links each reagent to its MSDS through a QR code, and connects the school to a vendor when stock runs low. Its own interface is engineered to get out of the way. The system is strictly monochrome: near-black ink (`{colors.ink}` — #141414) on a pure white canvas (`{colors.canvas}`), with structure carried by a ladder of barely-perceptible neutral tints rather than by shadows or color. The reagent data the app exists to show — names, quantities, dates, stock status — is what the chrome frames, the way a gallery wall frames paintings.

The geometry does the brand work that color refuses to do. Every interactive element is a stadium pill (`{rounded.full}`): the floating navigation bar, every button, the segmented toggle, the status badges. Containers sit at a calm `{rounded.md}` (24px) and rows, inputs, and media tiles at `{rounded.sm}` (16px). Type is set in Pretendard with strong weight contrast — Bold 700 for every heading, Regular 400 for text, Light 300 for lead subtitles — which gives the monochrome pages a strong typographic voice without a single decorative flourish.

One color is allowed to interrupt: a deep pink accent (`{colors.accent}` — #d6246a), used for decision signals — the low-stock badge on reagent rows, the reorder alert that leads to a vendor, and the cabinet mix warning. Its scarcity is the point; when pink appears, it is asking for a decision. (The mix warning — an unsafe storage combination in a reagent cabinet, `mix-warning` — was added 2026-10-02.)

A second, calmer hue marks where the user is (added 2026-10-02): sky blue (`{colors.highlight}` — #2b9fe0) with its pale tint (`{colors.highlight-soft}` — #e6f4fc) highlights selection and focus — the chosen school, the active tab or segment, links, progress, and icons. It never appears in a pink decision signal and never fills a primary CTA.

**Key Characteristics:**

- Gallery-white monochrome palette — `{colors.ink}` on `{colors.canvas}`, brand chroma limited to the `{colors.accent}` pink (stock shortage) and the `{colors.highlight}` sky blue (selection and emphasis)
- Stadium-pill interaction language: nav bar, buttons, toggles, and badges all at `{rounded.full}`
- Shadow-free elevation — hierarchy built from a neutral tint ladder (`{colors.canvas-soft}`, `{colors.field}`, `{colors.hairline}`) and 1px hairlines
- Pretendard with weight contrast: 700 headings at 1.3–1.35 line-height, 400 body at 1.5, 300 light subtitles
- Pink means "a decision is needed" — stock is short, or a cabinet slot mixes unsafe classes — and nothing else; sky blue means "selected / here" and is never used for stock shortage
- Content supplies the information: reagent data, MSDS QR codes, and uploaded experiment manuals carry the screen

## Colors

Source screens (PRD §7): login (personal email + password), sign-up (NEIS school select), reagent list, reagent detail (MSDS QR), usage record, manual upload → extraction review, reorder alert → vendor link.

### Brand & Accent

- **Ink Black** (`{colors.primary}` — #141414): The brand color. Fills every primary CTA pill and all display typography. Lab_Stock's identity is this near-black, softened just off pure black.
- **Deep Pink** (`{colors.accent}` — #d6246a): The stock-shortage accent. Reserved for decision signals — the low-stock badge, the reorder alert, and the cabinet mix warning (`mix-warning`). Never used decoratively, never used for CTAs.
- **Soft Pink** (`{colors.accent-soft}` — #fbe9f0): The pink at 10% over white (added 2026-10-02). Fills the cabinet mix warning (`mix-warning`) so the signal reads clearly without glare; text on it is `{colors.ink}` (15.8:1) and the warning icon stays `{colors.accent}` (4.17:1). Allowed only inside `badge-low-stock`, `reorder-alert-card`, and `mix-warning`.
- **Sky Blue** (`{colors.highlight}` — #2b9fe0): Emphasis accent for everything except stock shortage — selected-state borders and indicators, active tab/segment markers, links underline, progress bars, and icons. Contrast on white is 2.94:1, so it is never a text color; text placed on it is `{colors.ink}` (6.26:1). Never inside `badge-low-stock`, `reorder-alert-card`, or as the fill of `button-primary`.
- **Sky Tint** (`{colors.highlight-soft}` — #e6f4fc): Pale background for selected rows, chosen options, and informational surfaces; text on it is `{colors.ink}` (16.41:1). Same exclusions as Sky Blue.

### Surface

- **Canvas** (`{colors.canvas}` — #ffffff): Default page and card background across all screens.
- **Soft Canvas** (`{colors.canvas-soft}` — #f3f3f3): The workhorse tint — a 6% ink wash over white. Fills the floating nav pill, reagent rows, the reorder alert card, soft utility pills, and segmented-control tracks.
- **Field** (`{colors.field}` — #f0f0f0): An 8% ink wash used as the fill for form inputs, giving fields presence without borders.
- **Soft Hairline** (`{colors.hairline-soft}` — #f0f0f0): 1px card outlines — the faintest possible edge, used on white-on-white cards (reagent detail, MSDS QR tile).
- **Hairline** (`{colors.hairline}` — #e0e0e0): The stronger 16% control border, used on outlined pill buttons and interactive chrome.

### Text

- **Ink** (`{colors.ink}` — #141414): Headings, body copy, and nav links.
- **Soft Ink** (`{colors.ink-soft}` — #262626): Slightly lifted dark used for secondary lockups.
- **Muted** (`{colors.text-muted}` — #707070): Secondary copy — supporting paragraphs, dates, units, underlined inline links.
- **Faint** (`{colors.text-faint}` — #adadad): Tertiary text — placeholders, fine print.

### Semantic

- The system ships no dedicated success/warning/error palette; state communication stays within the monochrome ladder, with `{colors.accent}` reserved for stock shortage and `{colors.highlight}` / `{colors.highlight-soft}` for selection and emphasis.

## Typography

### Font Family

**Pretendard** — a Korean–Latin neo-grotesque used exclusively, across every screen and every role. On the web it is loaded as **Pretendard Variable**; in Figma use the static weights (Light 300 · Regular 400 · SemiBold 600 · Bold 700). The brand's voice comes from weight contrast: headings at Bold 700, running text at Regular 400, and lead subtitles at a light 300. Fallback stack: `-apple-system, BlinkMacSystemFont, "Apple SD Gothic Neo", "Noto Sans KR", sans-serif`. **Figma mockup substitute:** when Pretendard is unavailable in the Figma environment, mockups may use **IBM Plex Sans KR** at the same weights (300 · 400 · 600 · 700); the shipped product always uses Pretendard.

Sizes below are set for the mobile baseline frame (390×844). Korean glyphs need more vertical room than Latin, so headings sit at 1.3–1.35 and body text at 1.5.

### Hierarchy

| Token                    | Size | Weight | Line Height | Letter Spacing | Use                                                      |
| ------------------------ | ---- | ------ | ----------- | -------------- | -------------------------------------------------------- |
| `{typography.display}`   | 32px | 700    | 1.3         | 0              | Key counters (e.g. stock quantity on reagent detail)     |
| `{typography.heading-1}` | 28px | 700    | 1.3         | 0              | Screen titles                                            |
| `{typography.heading-2}` | 24px | 700    | 1.35        | 0              | Section headings on content screens                      |
| `{typography.heading-3}` | 20px | 700    | 1.35        | 0              | Card-level headlines, auth headings                      |
| `{typography.heading-4}` | 18px | 700    | 1.35        | 0              | Sub-section headings                                     |
| `{typography.title}`     | 17px | 600    | 1.4         | 0              | Reagent names, emphasized rows                           |
| `{typography.body-lg}`   | 17px | 300    | 1.5         | 0              | Lead paragraphs — the light counterpoint to 700 headings |
| `{typography.body}`      | 15px | 400    | 1.5         | 0              | Default body copy                                        |
| `{typography.body-sm}`   | 13px | 400    | 1.5         | 0              | Supporting copy, table cells, legal text                 |
| `{typography.link}`      | 15px | 600    | 1.5         | 0              | Nav links and button labels                              |
| `{typography.label}`     | 12px | 600    | 1.4         | 0              | Badge and pill labels                                    |
| `{typography.caption}`   | 12px | 400    | 1.4         | 0              | Captions, metadata (dates, units), form fine print       |

### Principles

- **Weight contrast is the drama.** Pairing 700 headings against 300 light subtitles (e.g. 32px display over 17px light lead) creates hierarchy without color or ornament.
- **Controlled leading.** Headings sit at 1.3–1.35 — tight, but with enough room for Korean glyphs. Body text opens up to 1.5.
- **Zero letter-spacing everywhere.** Pretendard is trusted at its natural fit; no tracking adjustments at any size.

## Layout

### Spacing System

- **Base unit**: 8px, with 4px half-steps for fine rhythm
- **Tokens**: `{spacing.xxs}` 4px · `{spacing.xs}` 8px · `{spacing.sm}` 12px · `{spacing.md}` 16px · `{spacing.lg}` 24px · `{spacing.xl}` 32px · `{spacing.section}` 48px · `{spacing.section-lg}` 64px
- Buttons are fixed-height pills padded horizontally at `{spacing.md}`; inputs pad `{spacing.sm} {spacing.md}`
- Screen side padding is `{spacing.md}` (16px); sections are separated by `{spacing.section}` (48px), and `{spacing.section-lg}` (64px) separates major acts on long screens

### Grid & Container

- Content rides a centered single column on mobile. Lists (reagent rows, extraction results) stack vertically with `{spacing.sm}` gaps.
- The floating nav pill is detached from the viewport edge and horizontally centered, rather than a full-width bar — the page canvas visibly wraps around it.

### Whitespace Philosophy

Whitespace is the primary grouping device. Sections are separated by `{spacing.section}` to `{spacing.section-lg}` of empty canvas with no divider rules; within cards, generous `{spacing.lg}` padding keeps content off the hairline edges.

### Responsive Strategy

#### Screen Size

Designed mobile-first; desktop is also in scope (PRD §8 — layouts respond to the viewer's screen size).

| Name     | Width × Height | Notes                                                        |
| -------- | -------------- | ------------------------------------------------------------ |
| Baseline | 390 × 844      | Default design frame for all key screens (Figma)             |
| Minimum  | 360px width    | Layouts must hold without horizontal scroll; long text wraps |
| Desktop  | 1440 × 900     | Provisional default — to be confirmed in harness round R2     |

- Side padding: `{spacing.md}` (16px) on both sides at mobile widths.
- Content is single-column by default; grids collapse to one column at the minimum width.

#### Touch Targets

- Pill buttons and nav CTAs are fixed-height stadium shapes comfortably above the 44px minimum; form inputs pad to a similar height via `{spacing.sm} {spacing.md}`.
- The segmented toggle presents each option as a full pill target, not a small radio dot.

#### Collapsing Strategy

- The floating `nav-pill` persists on scroll and across breakpoints, tightening to logomark + CTA on narrow screens.
- Multi-column grids collapse column-by-column rather than reflowing horizontally.

#### Image Behavior

- MSDS QR codes keep a 1:1 aspect ratio at all sizes and are never cropped.
- Uploaded manual previews keep their aspect ratio inside `{rounded.sm}` tiles.

## Elevation & Depth

| Level   | Treatment                                       | Use                                                  |
| ------- | ----------------------------------------------- | ---------------------------------------------------- |
| 0       | Flat on `{colors.canvas}`                       | Default — most of every screen                       |
| 1       | `{colors.canvas-soft}` fill, no border          | Nav pill, reagent rows, reorder alert card, soft pills |
| 2       | 1px `{colors.hairline-soft}` outline on white   | Reagent detail card, MSDS QR tile                    |
| Inverse | `{colors.ink}` fill, `{colors.on-primary}` text | Primary CTAs                                         |

The system is essentially shadow-free: no drop shadows appear on any card, button, or nav element. Elevation is communicated by _fill difference_ (white vs. 6–8% ink tints) and by hairlines, which keeps every surface print-flat. The one soft-shadow exception is the active segment of the segmented control, which lifts off its `{colors.canvas-soft}` track as a white pill.

## Shapes

### Border Radius Scale

| Token            | Value  | Use                                                         |
| ---------------- | ------ | ----------------------------------------------------------- |
| `{rounded.none}` | 0px    | QR code image itself (inside its tile)                      |
| `{rounded.sm}`   | 16px   | Inputs, reagent rows, manual preview tiles, table containers |
| `{rounded.md}`   | 24px   | Content cards, reagent detail card, MSDS QR tile, alert card |
| `{rounded.full}` | 9999px | Every pill: nav, buttons, badges, toggles                   |

## Components

### Buttons

**`button-primary`** — "로그인", "입고", "사용 기록 저장", "확인 후 저장", "판매처 연결"

- Fill `{colors.primary}`, label `{colors.on-primary}` in `{typography.link}`, shape `{rounded.full}`, padding `0px {spacing.md}` on a fixed-height pill
- The single CTA style everywhere

**`button-outline`** — secondary action beside a primary (e.g. "취소", "다시 추출")

- Fill `{colors.canvas}`, label `{colors.ink}`, 1px `{colors.hairline}` border, shape `{rounded.full}`
- The de-emphasized twin of the primary pill; used when two actions sit side by side

**`button-pill-soft`** — "MSDS 보기 ↗", in-page links

- Fill `{colors.canvas-soft}`, label `{colors.ink}`, shape `{rounded.full}`
- Tertiary utility pill for outbound and in-page links; no border, relies on its tint fill

### Lab_Stock Screen Components

Composed only from the primitives and tokens above; no new literal values.

**`reagent-row`** — one reagent on the reagent list

- Full-width `{colors.canvas-soft}` bar, `{rounded.sm}` corners, padding `{spacing.md}`
- Reagent name in `{typography.title}`, quantity + unit in `{typography.body}`, intake date in `{typography.caption}` `{colors.text-muted}`
- Carries `badge-low-stock` when stock is below the required amount; rows stack with `{spacing.sm}` gaps

**`badge-low-stock`** — compact `{colors.accent}` chip with `{colors.on-primary}` `{typography.label}` text ("재고 부족"), shape `{rounded.full}`

**`reagent-detail-card`** — reagent detail screen

- `{colors.canvas}` fill, 1px `{colors.hairline-soft}` outline, `{rounded.md}` corners, padding `{spacing.lg}`
- Stock quantity in `{typography.display}`, field labels in `{typography.caption}` `{colors.text-muted}`

**`msds-qr-tile`** — MSDS link on reagent detail

- `{colors.canvas}` fill, 1px `{colors.hairline-soft}` outline, `{rounded.md}` corners; the QR image inside at 1:1, `{rounded.none}`
- Paired with a `button-pill-soft` "MSDS 보기 ↗"

**`extraction-table`** — manual upload → AI extraction review

- Uses `ex-data-table-cell` chrome inside a `{rounded.sm}` container; editable cells use `text-input`
- Closed by a `button-primary` "확인 후 저장" (results are saved only after the user confirms — PRD §5)
- Each extracted row has a second line (added 2026-10-06): "우리 학교 시약" select + delete, and a muted note "기존 기준 N · 그대로 둬요 / 바뀌어요". Unit is a select (병 · mL · g). The 조 수 field starts empty

**`reorder-alert-card`** — reorder alert → vendor link

- `{colors.canvas-soft}` fill, borderless, `{rounded.md}` corners, padding `{spacing.lg}`
- `badge-low-stock` + reagent name in `{typography.heading-4}` + required vs. current amount in `{typography.body}`, closed by a `button-primary` "판매처 연결"
- After the vendor is confirmed (added 2026-10-06): a muted line "사이트를 새 창으로 열었어요. 열리지 않았다면 [직접 열기]" with the link as `button-pill-soft`

### Inputs & Forms

**`text-input`**

- `{colors.field}` fill, no border, `{colors.ink}` text with `{colors.text-faint}` placeholder, `{rounded.sm}` corners, padding `{spacing.sm} {spacing.md}`

**`text-input-focused`**

- Same chrome plus a 2px `{colors.ink}` ring — focus is signaled in ink, consistent with the monochrome system

### Navigation

**Desktop shell (screens 2–13, added 2026-10-08)** — the desktop is a web app, not a widened phone (refs/uibowl-desktop-web-20261008.md)

- **`app-sidebar`** — fixed left column, 240 wide, full height, `{rounded.none}`, `{colors.canvas-soft}` fill, 1px `{colors.hairline-soft}` right edge. Top: "Lab_Stock" wordmark + the school name in `{typography.title}` (one school per account — shown, never switched; N1). Middle: grouped menu of **`sidebar-item`**s — all roles: 홈 · 시약 · 기록 · 시약장 · QR 찾기; teacher·admin add 입고 · 실험 매뉴얼 · 재주문 알림; admin adds 사용자 · 판매처. Each item = icon + `{typography.body}` label, 44 high, square; current item = `{colors.highlight-soft}` fill + `{colors.highlight}` icon, label `{colors.ink}`. Bottom: name · role + `nav-account-menu` ▾ (로그아웃). Replaces `nav-pill` on desktop screens 2–13; there is no bottom `tab-bar` on desktop
- Content area = everything right of the sidebar, page padding `{spacing.xl}`; page head = title (`{typography.heading-2}`) + count on the left, search · filter · primary `button-primary` on the right
- **`data-table`** — lists on desktop (screens 2 시약, 8 사용자, 9 판매처, 10 기록) are tables, not card stacks: `ex-data-table-cell` chrome inside a `{rounded.sm}` container with 1px `{colors.hairline-soft}` outline; sortable column heads (sort arrow in `{colors.text-muted}`, active in `{colors.highlight}`); row hover `{colors.canvas-soft}`; selected row `{colors.highlight-soft}`. Status such as `badge-low-stock` sits in its own column. Page numbers centered under the table when long
- **`detail-drawer`** — one item's detail (reagent on screen 3, usage record on 10, MSDS search results etc.) opens as a right drawer 480 wide over the table, full height, `{colors.canvas}` with 1px `{colors.hairline-soft}` left edge, × close top right. Order: title → status chips → "항목 | 값" two-column rows → actions at the bottom. Never a centered modal
- Heavy work opens as a page in the content area, not a drawer: screen 5 (manual), 7 (intake · document intake), 11 (cabinet setup). Forms are a centered single column ~640 wide with "label | control" rows separated by hairlines; long flows put the primary action in a sticky bottom bar
- Overlays: `ex-modal-card` only for confirms and one-field input. Mobile choice sheets (filter, MSDS candidates, location picker, cabinet choice) become a dropdown / popover anchored to their control on desktop
- Home (13) on desktop: a top row of number tiles "지금 처리할 것" (재고 부족 N · 재주문 알림 N · MSDS 없는 시약 N — role-scoped), below a 2–3 column grid of widgets (최근 사용 기록 `data-table` · 재고 부족 · 시약장 요약), each with "전체 보기 ›". The mobile `quick-action` tiles are replaced by the sidebar plus page-head buttons
- Mobile stays exactly as approved

**`nav-pill`** — Top Nav (Desktop · pre-login screens 1·14·15 only from 2026-10-08)

- A floating, horizontally-centered stadium bar in `{colors.canvas-soft}`: "Lab_Stock" logomark + wordmark left, section links in `{typography.link}` right, capped by a `button-primary` CTA
- Detaches from the page edge with visible canvas above it; persists as a sticky element on scroll

- After login, the school name in the pill carries a small ▾ (**`nav-account-menu`**, added 2026-10-06): it opens a small `{colors.canvas}` menu (`{rounded.md}`, 1px `{colors.hairline-soft}` outline) with one item "로그아웃"

**Top Nav (Mobile)**

- The pill tightens to logomark + CTA; links collapse behind the pill

**`tab-bar`** — Bottom Tab Bar (Mobile, added 2026-10-02, squared 2026-10-02)

- Primary mobile navigation: a full-width rectangular bar docked to the bottom edge — `{rounded.none}` (0), not a floating pill. The one deliberate exception to the stadium-pill language, so the bar reads as the device's frame rather than a control
- `{colors.canvas}` fill with a 1px `{colors.hairline-soft}` top border, no shadow
- Exactly four `tab-item`s, identical for every role: 홈 · 시약 · QR 스캔 · 기록. Equal width — the scan tab is not enlarged
- Each `tab-item` is an icon above a `{typography.label}` label, tap target ≥ 44px, square (no pill behind it)
- Active tab: `{colors.highlight}` icon with `{colors.ink}` label. Inactive: `{colors.text-muted}` icon and label
- Present on every mobile screen after login (screens 2–13); absent on login (screen 1) and on desktop, where `nav-pill` carries navigation
- Role-specific actions (입고, 사용자 관리) are never tabs; they live in the home `quick-action` area — three tiles (added 2026-10-06): teacher = 사용 기록 입력 · 입고 · 시약장 설정, admin = 입고 · 사용자 관리 · 시약장 설정; mobile lays them out 2 + 1

### Signature Components

**Multiple cabinets (screen 11, added 2026-10-04)**

- **`cabinet-switcher`** — horizontal row of pills, one per cabinet ("1번 시약장", "2번 시약장", …), scrolls sideways when long. Active cabinet = `{colors.highlight-soft}` fill + `{colors.highlight}` 1px border, label `{colors.ink}`; others `{colors.canvas-soft}`. Visible to every role
- **`cabinet-add`** — `button-pill-soft` "+ 시약장 추가" at the end of the switcher (teacher·admin only; never rendered for students)
- Rename and delete live inside `cabinet-edit`: `button-outline` "이름 바꾸기" and a quiet text action "삭제". Delete opens an `ex-modal-card` confirm — "이 시약장을 삭제할까요? 배치된 시약 N개는 '칸 없음'으로 바뀌어요" with `button-outline` "취소" and `button-primary` "삭제". No pink: deleting a cabinet is not a stock or safety signal
- Unassigned reagents show the slot label "칸 없음" in `{colors.text-muted}`
- Empty state (no cabinets yet): `ex-empty-state-card` "아직 시약장이 없어요" + one line of guidance; teachers·admins get `cabinet-add` inside the card, students see the text only
- Unsaved edits (added 2026-10-06): switching cabinets or leaving with unsaved `cabinet-edit` changes opens an `ex-modal-card` — "저장하지 않은 변경이 있어요" with `button-outline` "버리고 이동" and `button-primary` "계속 편집". No pink

**Cabinet number & QR print (screens 11·12, added 2026-10-06)**

- **`cabinet-number`** — every cabinet has a fixed school-local number (1, 2, 3 …) separate from its editable name; a deleted number is never reused. Rendered as a small `{colors.canvas}` circle with 1px `{colors.hairline}` border and the numeral in `{colors.ink}` `{typography.label}`, placed before the name inside each `cabinet-switcher` pill and on the QR label. Never pink, never sky-blue text
- **`qr-print`** — `button-outline` "QR 인쇄" in the screen 11 management row beside "이름 바꾸기" (teacher·admin only; never rendered for students)
- **`qr-print-sheet`** — bottom sheet (mobile) / `ex-modal-card` (desktop): cabinet choice as `storage-class-chip`-style pills (default = current cabinet, plus "모두"), a white A4 preview tile (`{colors.hairline-soft}` outline, `{rounded.md}`) holding several `qr-label`s, closed by `button-primary` "인쇄". × close top right
- **`qr-label`** — one printable label: QR image 1:1 `{rounded.none}`, school name in `{typography.caption}`, `cabinet-number` + cabinet name in `{typography.title}`, one line "QR을 찍으면 이 시약장의 시약을 봐요" in `{typography.caption}` `{colors.text-muted}`. Monochrome only — it is printed
- **`qr-result-sheet`** (screen 12) — after a scan or a manual number lookup: sheet titled `cabinet-number` + cabinet name, the cabinet's reagents as `reagent-row`s each with its slot ("좌 2단" / "칸 없음" muted), closed by `button-pill-soft` "배치도 보기" (→ that cabinet on screen 11). `qr-manual-entry` asks for "시약장 번호" (numeric `text-input`)

**Document intake (screen 7, added 2026-10-07)**

- **`intake-mode`** — `segmented-control` at the top of screen 7: "서류로 입고" (default) / "직접 입력"
- **`doc-upload`** — `ex-empty-state-card`-style drop zone: "품의서·영수증·거래명세서를 올려 주세요" + caption "PDF·JPG·PNG, 4MB까지", `button-primary` "AI로 읽기". While reading: the same card with a progress line in `{colors.highlight}` and "읽는 중이에요". Teacher·admin only
- **`doc-intake-table`** — `extraction-table` chrome. Each `doc-item-row` = 품명(서류 표기) · 규격 · 수량 on line 1, and **`reagent-link`** on line 2: "우리 학교 시약" select (auto-linked, "바꾸기"), a quiet "빼기", or "새 시약으로 등록". Unit conversion as a muted caption ("500 mL × 4병 = 2,000 mL"). On mobile each row is a `{colors.canvas-soft}` card. Intake date field at the top ("서류 날짜", editable). Non-reagent items fold at the bottom as "시약 아님 N개" (muted, expandable). Closed by `button-primary` "확인 후 입고"
- **`new-reagent-fields`** — choosing "새 시약으로 등록" expands that row downward: 이름 · 보관 분류 (`storage-class-chip`s with the AI pick marked by `suggest-badge`) · 단위 · 재고량 · MSDS (`msds-search`)
- Failure / nothing found: `ex-empty-state-card` "서류에서 품목을 찾지 못했어요" + one line of guidance + `doc-upload` again. No pink — nothing is low on stock

**MSDS search (screens 7·3·2, added 2026-10-07)**

- **`msds-search`** — `button-pill-soft` "MSDS 찾기" next to the MSDS field (screen 7) or in place of `msds-qr-tile` when a reagent has none (screen 3; students see "MSDS가 아직 없어요" muted instead). Teacher·admin only
- **`msds-candidates`** — sheet listing candidates: 물질명 in `{typography.title}` + "CAS 7647-01-0" in `{typography.caption}` `{colors.text-muted}`; the chosen one gets the `{colors.highlight-soft}` selection fill; closed by `button-primary` "이 MSDS로". Zero results: "찾지 못했어요 — 직접 입력" with a `text-input` for the address
- **`msds-bulk-banner`** (screen 2) — `{colors.highlight-soft}` strip above the list: "MSDS 없는 시약 N종" + `button-pill-soft` "한 번에 찾기" → `msds-candidates` per reagent in sequence (reagent name as the sheet title, "건너뛰기"). Teacher·admin only

**Location suggestion (screens 7·3·11, added 2026-10-07)**

- **`suggest-badge`** — small pill "추천": `{colors.highlight-soft}` fill, 1px `{colors.highlight}` border, `{colors.ink}` `{typography.label}`. Marks the suggested `cabinet-slot` in `location-picker` and `slot-sheet` (which starts selected) and the AI's storage-class pick. Never pink
- **`location-suggest`** — after saving with new reagents: list of `reagent-row`s, each with "추천 위치: `cabinet-number` 이름 · 좌 2단" + `button-outline` "다른 칸" and `button-primary` "여기에 두기"; footer `button-primary` "모두 추천대로" and a quiet "나중에" (→ screen 2). No matching slot: muted line "맞는 칸이 없어요 — 시약장 설정에서 칸 분류를 정해 주세요" with `button-pill-soft` "시약장 설정"

**Auto reorder threshold (screens 3·6, added 2026-10-07)**

- **`auto-threshold-badge`** — `{colors.canvas-soft}` pill "자동" in `{colors.ink}` `{typography.label}` beside the threshold in `reorder-threshold` / `reorder-alert-card`, with a caption "최근 사용량으로 계산했어요". Manual and manual-extracted values show no badge. Not pink, not sky-blue — it is information, not a decision
- Screen 5: when the same reagent appears in several rows they merge into one, with a muted line "2개 행을 합쳤어요"

**School level (screen 14, added 2026-10-07)**

- **`school-select-kind`** — `segmented-control` with three options 초등학교 · 중학교 · 고등학교, placed after `school-select-region` and before `school-select-school`. No default: until one is chosen, `school-select-school` is disabled with the placeholder "학교급을 먼저 골라 주세요"
- No schools for that level in the region: in place of the school list, a muted line "이 지역에 {학교급}이 없어요 — 지역을 다시 골라 주세요". No pink

**List filter (screen 2, added 2026-10-07)** — every role, guest included

- **`list-filter-button`** — `button-pill-soft` "필터" with a filter icon, right of the search `text-input`. When filters are applied it carries a count pill (`{colors.highlight-soft}` fill, 1px `{colors.highlight}` border, `{colors.ink}` `{typography.label}`). The `segmented-control` "전체 / 재고 부족" stays as is
- **`list-filter-sheet`** — bottom sheet (mobile) / dropdown panel under the button (desktop), × close. Sections in order: 정렬 (`segmented-control`-style options 이름순 · 재고 적은 순 · 최근 입고순), 보관 분류 (`storage-class-chip`s, multi-select, plus "분류 없음"; selected = `{colors.highlight-soft}` + `{colors.highlight}` border), 보관 위치 (`cabinet-number` + name select → slot select, plus a "칸 없음만" toggle), "MSDS 없는 시약만" toggle. Footer `button-outline` "초기화" + `button-primary` "{N}종 보기"
- **`filter-chip-row`** — above the list: one `{colors.canvas-soft}` pill per applied filter with ×, a quiet "모두 지우기", and the result count "12종" in `{typography.caption}`. With "MSDS 없는 시약만" on, teachers·admins also see `msds-bulk-banner`
- No results: `ex-empty-state-card` "조건에 맞는 시약이 없어요" + `button-outline` "필터 지우기". No pink

**Usage date (screens 4·10, added 2026-10-07)**

- **`usage-date`** — "사용일" date `text-input` under the quantity on screen 4, same shape as screen 7's 입고일. Defaults to today; future dates are disabled
- **`past-date-note`** — when the date is not today, a muted line above the save button: "10월 3일 사용으로 기록해요"
- Screen 10 groups and sorts by 사용일; when the recorded day differs, a muted caption "10월 6일에 기록" under the row

**Reagent slots (screens 11·3, added 2026-10-06)**

- **`slot-count`** — small `{colors.canvas}` pill inside a `cabinet-slot` showing how many reagents it holds ("3"), `{typography.label}` `{colors.ink}`. Empty slots show nothing. Never pink — a count is not a decision signal
- **`slot-sheet`** — tapping a `cabinet-slot` opens a sheet: slot name ("좌 2단") + its `storage-class-chip`s, the reagents in it as `reagent-row`s, each with a quiet "빼기" text action (teacher·admin). Students see the list only
- **`slot-assign`** — `button-primary` "시약 넣기" at the bottom of `slot-sheet` (teacher·admin only); opens a picker list of "칸 없음" reagents with a search `text-input`
- Class mismatch (warn, never block): when a reagent's storage class is not among the slot's classes, show `mix-warning` "이 칸은 {분류} 칸이에요 — 그래도 넣을 수 있어요"; when it forms a `cabinet.incompatible` pair with the slot or a reagent already there, the same `mix-warning` with stronger copy "{A}와 {B}는 섞으면 위험해요". Saving stays enabled in both cases
- **`reagent-location`** (screen 3) — a row in `reagent-detail-card`: caption "보관 위치" + "`cabinet-number` 이름 · 좌 2단" or "칸 없음" in `{colors.text-muted}`. Teachers·admins get **`location-edit`** — `button-pill-soft` "위치 바꾸기" — which opens **`location-picker`**: `cabinet-switcher` on top, the cabinet's `cabinet-slot` grid below (each with `slot-count`), tap a slot to choose; "칸 없음으로" as a quiet text action; `mix-warning` appears under the grid on mismatch; closed by `button-primary` "저장"
- **`reorder-threshold`** (screen 3) — a row in `reagent-detail-card`: caption "재주문 기준" + amount + unit, or "아직 없어요" muted. Teachers·admins get **`threshold-edit`** — tapping turns the amount into a numeric `text-input` with unit and `button-primary` "저장". Same field as the screen 5 extraction result

**Landing (screen 15, added 2026-10-03)** — the pre-login first screen

- **`landing-hero`** — "Lab_Stock" wordmark, a one-line description in `{typography.heading-1}`, a `{typography.body-lg}` light subtitle. Monochrome; no school name (nothing is selected before sign-up)
- **`feature-card`** — 3–4 cards (학교별 분리 · NEIS 학교 선택 · QR 스캔 · 재고 부족 알림): `{colors.canvas-soft}` fill, `{rounded.md}`, icon in `{colors.highlight}` + title + one line of body. The 재고 부족 알림 card may show a small `badge-low-stock` as an example (pink stays inside the badge)
- **`landing-cta`** — bottom action area: `button-primary` "회원가입" (→ 14) and `button-outline` "로그인" (→ 1). No tab bar on this screen
- **`guest-entry`** — a third, quieter action under the CTAs: `button-pill-soft` "둘러보기" (→ guest home). Added 2026-10-03

**Guest mode (둘러보기, added 2026-10-03)** — read-only tour on the demo school

- **`guest-banner`** — full-width strip at the top of every guest screen, under `nav-pill`: `{colors.highlight-soft}` fill, `{rounded.none}`, text "둘러보는 중 — 가입하면 우리 학교 데이터로 시작해요" in `{colors.ink}` `{typography.body-sm}`, a compact `button-primary` "가입하기" (→ 14) at the end
- **`guest-lock`** — a small lock icon in `{colors.text-muted}`. Sits on every write action that stays visible but is disabled (e.g. "사용 기록 입력" in `quick-action`, "사용 기록" on reagent detail) and on the QR 스캔·기록 `tab-item`s. Tapping a locked item shows an `ex-toast` "가입하면 쓸 수 있어요" — never pink (no decision is pending)
- School name shown everywhere is the single demo school "데모 학교"

**`badge-overlay`** — translucent gray pill (rgba(115, 115, 115, 0.56)) with `{colors.on-primary}` `{typography.label}` text, laid over image content (manual preview tags)

**`segmented-control`** + **`segmented-control-active`** — two-option toggle: a `{colors.canvas-soft}` stadium track holding two pill options; the active option is a `{colors.canvas}` white pill, the inactive label sits in `{colors.text-muted}`

### Examples (illustrative)

> Kit-mirror demonstration surfaces. Each `ex-*` entry references brand-native primitives via token syntax so downstream consumers re-skin the same surfaces consistently; none carries invented literal values.

**`ex-app-shell-row`** — Sidebar nav row inside the App Shell example. Active state uses brand primary as the indicator.

- Properties: `backgroundColor`, `activeIndicator`, `rounded`, `padding`

**`ex-data-table-cell`** — Default data-table th + td chrome. Header uses mono-caps eyebrow typography; body uses body-sm.

- Properties: `headerBackground`, `headerTypography`, `bodyTypography`, `cellPadding`, `rowBorder`

**`ex-auth-form-card`** — Sign-in card (login with school select). Re-uses feature-card chrome with text-input primitives inside.

- Properties: `backgroundColor`, `rounded`, `padding`

**`ex-modal-card`** — Modal dialog surface — same chrome as feature-card with elevated shadow.

- Sheets and forms that open over a screen carry a × close at top right (added 2026-10-06 — user-manage sheet on 8, vendor-register form on 9). On 8 the delete confirm reads "{이름} · 사용·입고 기록은 남아요" and invite is email only (no name field); on 9 there is no extra-info field

- Properties: `backgroundColor`, `rounded`, `padding`

**`ex-empty-state-card`** — Empty-state illustration frame (e.g. no reagents registered yet).

- Properties: `backgroundColor`, `rounded`, `padding`, `captionTypography`

**`ex-toast`** — Toast notification surface — feature-card shape + medium shadow.

- Properties: `backgroundColor`, `rounded`, `padding`, `typography`

## Do's and Don'ts

### Do

- Keep the canvas `{colors.canvas}` white and let reagent data supply the information.
- Use `{rounded.full}` for every interactive element — a rectangular button does not exist in this system.
- Build emphasis with the tint ladder: `{colors.canvas-soft}` fill for rows and alerts, `{colors.hairline-soft}` outlines for resting cards.
- Reserve `{colors.accent}` for decision signals only (`badge-low-stock`, `reorder-alert-card`, `mix-warning`).
- Use `{colors.highlight}` / `{colors.highlight-soft}` for selection and emphasis everywhere else; keep text on them in `{colors.ink}`.
- Set every heading in Pretendard Bold 700 with line-height 1.3–1.35.
- Pair Bold 700 headings with 300-weight `{typography.body-lg}` subtitles for hierarchy without color.
- Keep MSDS QR codes at 1:1, uncropped.

### Don't

- Don't add drop shadows — elevation is fills and hairlines only.
- Don't use `{colors.accent}` for CTAs; primary actions are always `{colors.primary}` ink pills.
- Don't introduce accent hues beyond pink and sky blue, gradients on UI chrome, or colored section bands.
- Don't use sky blue as a text color, inside a pink decision signal, or as the `button-primary` fill.
- Don't apply letter-spacing or all-caps styling; the type system runs at natural tracking in sentence case.
- Don't put borders on form fields at rest — inputs are `{colors.field}` tint fills; the border appears only as the 2px ink focus ring.
- Don't square off pill geometry at small sizes — badges, chips, and toggles stay stadium-shaped.
