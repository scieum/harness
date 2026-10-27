## Overview

Lab_Stock is a SaaS for school science labs (elementary, middle and high school — widened from high school only on 2026-10-07) — it tracks each reagent's type, stock level, intake date, usage date, and user, links each reagent to its MSDS through a QR code, and connects the school to a vendor when stock runs low. Its own interface is engineered to get out of the way. The system is strictly monochrome: near-black ink (`{colors.ink}` — #141414) on a pure white canvas (`{colors.canvas}`), with structure carried by a ladder of barely-perceptible neutral tints rather than by shadows or color. The reagent data the app exists to show — names, quantities, dates, stock status — is what the chrome frames, the way a gallery wall frames paintings.

The geometry does the brand work that color refuses to do. Every interactive element is a stadium pill (`{rounded.full}`): the floating navigation bar, every button, the segmented toggle, the status badges. Containers sit at a calm `{rounded.md}` (24px) and rows, inputs, and media tiles at `{rounded.sm}` (16px). Type is set in Pretendard with strong weight contrast — Bold 700 for every heading, Regular 400 for text, Light 300 for lead subtitles — which gives the monochrome pages a strong typographic voice without a single decorative flourish.

One color is allowed to interrupt: a deep pink accent (`{colors.accent}` — #d6246a), used for decision signals — the low-stock badge on reagent rows, the reorder alert that leads to a vendor, the cabinet mix warning, and the over-stock line on a usage row (`usage-over-stock`, added 2026-10-10). Its scarcity is the point; when pink appears, it is asking for a decision. (The mix warning — an unsafe storage combination in a reagent cabinet, `mix-warning` — was added 2026-10-02.)

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
- **Deep Pink** (`{colors.accent}` — #d6246a): The stock-shortage accent. Reserved for decision signals — the low-stock badge, the reorder alert, the cabinet mix warning (`mix-warning`), and the usage over-stock line (`usage-over-stock`). Never used decoratively, never used for CTAs.
- **Soft Pink** (`{colors.accent-soft}` — #fbe9f0): The pink at 10% over white (added 2026-10-02). Fills the cabinet mix warning (`mix-warning`) so the signal reads clearly without glare; text on it is `{colors.ink}` (15.8:1) and the warning icon stays `{colors.accent}` (4.17:1). Allowed only inside `badge-low-stock`, `reorder-alert-card`, `mix-warning`, and `usage-over-stock`.
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
- Card text (2026-10-08): "재주문 기준 N{단위}" and the alert date as "10월 7일 알림"
- After the vendor is confirmed (added 2026-10-06): a muted line "사이트를 새 창으로 열었어요. 열리지 않았다면 [직접 열기]" with the link as `button-pill-soft`

### Inputs & Forms

**`text-input`**

- `{colors.field}` fill, no border, `{colors.ink}` text with `{colors.text-faint}` placeholder, `{rounded.sm}` corners, padding `{spacing.sm} {spacing.md}`

**`text-input-focused`**

- Same chrome plus a 2px `{colors.ink}` ring — focus is signaled in ink, consistent with the monochrome system

### Navigation

**Desktop shell (screens 2–13, added 2026-10-08)** — the desktop is a web app, not a widened phone (refs/uibowl-desktop-web-20261008.md)

- **`app-sidebar`** — fixed left column, 240 wide, full height, `{rounded.none}`, `{colors.canvas-soft}` fill, 1px `{colors.hairline-soft}` right edge. Top: "Lab_Stock" wordmark + the school name in `{typography.title}` (one school per account — shown, never switched; N1). Middle: grouped menu of **`sidebar-item`**s — all roles: 홈 · 시약 · 센서 · 기록 · 시약장 · QR 찾기; teacher·admin add 입고 · 실험 매뉴얼 · 재주문 알림; admin adds 사용자 · 판매처. Each item = icon + `{typography.body}` label, 44 high, square; current item = `{colors.highlight-soft}` fill + `{colors.highlight}` icon, label `{colors.ink}`. Bottom: name · role + `nav-account-menu` ▾ (로그아웃). Replaces `nav-pill` on desktop screens 2–13; there is no bottom `tab-bar` on desktop
- Content area = everything right of the sidebar, page padding `{spacing.xl}`; page head = title (`{typography.heading-2}`) + count on the left, search · filter · primary `button-primary` on the right
- **`data-table`** — lists on desktop (screens 2 시약, 8 사용자, 9 판매처, 10 기록) are tables, not card stacks: `ex-data-table-cell` chrome inside a `{rounded.sm}` container with 1px `{colors.hairline-soft}` outline; sortable column heads (sort arrow in `{colors.text-muted}`, active in `{colors.highlight}`); row hover `{colors.canvas-soft}`; selected row `{colors.highlight-soft}`. Status such as `badge-low-stock` sits in its own column. Page numbers centered under the table when long
- **`detail-drawer`** — one item's detail (reagent on screen 3, usage record on 10, MSDS search results etc.) opens as a right drawer 480 wide that pushes the content aside (sidebar 240 + content 720 + drawer 480 — approved 2026-10-08, so the page head and search stay visible), full height, `{colors.canvas}` with 1px `{colors.hairline-soft}` left edge, × close top right. Order: title → status chips → "항목 | 값" two-column rows → actions at the bottom. Never a centered modal. Also used for short forms on desktop: vendor register (9). The usage record (4) became a page on 2026-10-10 because its reagent list grows
- Heavy work opens as a page in the content area, not a drawer: screen 4 (usage record, several reagents — 2026-10-10), 5 (manual), 7 (intake · document intake), 11 (cabinet setup). Forms are a centered single column ~640 wide with "label | control" rows separated by hairlines; long flows put the primary action in a sticky bottom bar
- Overlays: `ex-modal-card` only for confirms and one-field input. Mobile choice sheets (filter, MSDS candidates, location picker, cabinet choice) become a dropdown / popover anchored to their control on desktop
- Home (13) on desktop: a top row of number tiles "지금 처리할 것" (재고 부족 N · 재주문 알림 N · MSDS 없는 시약 N — role-scoped), below a 2–3 column grid of widgets (최근 사용 기록 `data-table` · 재고 부족 · 시약장 요약), each with "전체 보기 ›". The mobile `quick-action` tiles are replaced by the sidebar plus page-head buttons
- Mobile stays exactly as approved

**Pre-login desktop (screens 1·14·15, added 2026-10-08)**

- **`web-header`** — full-width top bar, 64 high, `{rounded.none}`, `{colors.canvas}` with a 1px `{colors.hairline-soft}` bottom edge: "Lab_Stock" wordmark left; `button-outline` "로그인" + `button-primary` "회원가입" right (the current page's own button is omitted). No `nav-pill`, no `app-sidebar`
- Screens 1 (login) and 14 (sign-up): split layout under the header — left half the form (single column ~440), right half a `{colors.canvas-soft}` service panel (one-line pitch + the four `feature-card` points in a list). Sign-up form uses numbered sections with hairlines: "1 학교 선택" (sido → region → kind → school) → "2 계정"
- Screen 15 (landing, approved 2026-10-08 after one rejection — refs/uibowl-landing-hero-20261008.md): the first 900px is a hero. Left text column: small tag, a two-line headline "우리 학교 시약장, / 한 화면에서 관리해요" at the largest allowed size in Bold 700, a two-line `{typography.body-lg}` subtitle, `landing-cta` (`button-primary` "회원가입하고 시작하기" + `button-outline` "로그인"), `guest-entry` "둘러보기 ›", and a muted caption "학교별 데이터 분리 · NEIS 학교 검색 · QR로 시약 찾기". The whole left text column (tag to caption, inner gaps unchanged) is vertically centered on the right panel, ±8px (added 2026-10-27 — it had sunk to the bottom, leaving ~400px empty above). Right: a `{colors.canvas-soft}` panel (`{rounded.lg}`) holding a browser frame with a real-size crop of the approved home (13-desktop; its sidebar is named `shot-sidebar` so it is not counted as the app shell), overlapped bottom-left by a white card with a few `data-table` rows — layered with hairlines, no shadows. The four `feature-card`s start at the fold (y ≈ 820) showing only their tops. Below the fold the page scrolls (15-desktop is the one tall frame: 1440 wide, 900–6000 high — added 2026-10-08):
  - **`product-shot`** — the hero's right side (panel + browser frame + overlapped table card) as one named group
  - **`landing-tabs`** — at the fold: centered tab row 시약 목록 · 사용 기록 · 재주문 알림 · QR 찾기 · 학교별 분리, active underline `{colors.highlight}`; sticks under `web-header` on scroll
  - Problem row: centered title "과학실 시약, 이렇게 관리하고 계신가요?" + three quote `feature-card`s in teacher voice + one line "Lab_Stock은 학교별 시약장 하나로 답해요."
  - **`landing-section`** ×4 — one per tab, text and a crop of an approved screen alternating left/right: small tag → one-line title (display size allowed) → three bullets → quiet link. Crops come from approved screens (2 list + filter, 13 recent usage + the 4-desktop batch page with 수업 (replaced 2026-10-11), reorder row with `badge-low-stock`, 11 cabinet slots)
  - **`step-flow`** — five numbered circles joined by a line (1 학교 선택 → 2 시약 등록 → 3 칸 지정 → 4 사용 기록 → 5 재주문 알림); current step `{colors.highlight}` ring, others gray; below, one card with "STEP n / 5" + title + text + three checks and that step's screen crop
  - Audience: `segmented-control` 교사 · 학생 · 관리자, each with two outlined capability cards and a crop of what that role sees (role exposure follows the role table)
  - Trust 2×2 divided by hairlines only: 학교별 데이터 분리 · 인증 정보는 서버에서만 처리 · NEIS 공식 학교 정보로 가입 · MSDS·GHS 정보 연결. No usage numbers until real ones exist
  - **`cta-band`** — `{colors.canvas-soft}` band, centered one-line title (display size allowed) + `button-primary` 회원가입 + `button-outline` 둘러보기
  - **`web-footer`** — one centered line only, above it a 1px `{colors.hairline-soft}` rule: "© 2026 사이음(sci_eum). 과학의 사이, 사람을 잇다." in `{typography.caption}` `{colors.text-muted}`. No columns (2026-10-08 사용자 결정 — replaces the four-column footer). Since 2026-10-27 (요청 10) the line continues with **`footer-links`** after " · ": "개인정보 처리방침" (`{typography.caption}` `{colors.ink}`, weight 600 so it is easy to find) · "사용 가이드" (`{colors.text-muted}`); mobile wraps to two centered lines (copyright / links). Every footer uses this text
- Display sizes 40 · 48 exist only inside `landing-hero`, `landing-section`, `cta-band` (the hero headline is 48)
- Section rhythm (approved 2026-10-08): below the hero every section sits in a full-width band (`{rounded.none}`, no shadow) and the bands alternate `{colors.canvas}` ↔ `{colors.canvas-soft}` (#f3f3f3) — 탭 줄 white · 문제 공감 gray (its cards turn white) · the four `landing-section`s white/gray/white/gray · 대상 탭 white · 안심 gray (grid hairlines #e0e0e0 on gray). Two bands invert to `{colors.ink}` (#141414): the `step-flow` section (white text, secondary #adadad, inactive circles #262626, current circle `{colors.highlight}` ring, card #262626) and the `cta-band`. Neutral bands are part of the tint ladder, not "colored section bands"
- Inverted primary (only inside an ink band): `button-primary` becomes a white fill with an ink label, and `button-outline` a white border with a white label — so the main action never disappears on black
- Scroll motion (for development; static in Figma): section titles and cards rise 16px and fade in over 0.4s as they enter the viewport, once; `landing-tabs` sticks under `web-header` and the tab of the section in view takes the `{colors.highlight}` underline; all motion is off when the viewer prefers reduced motion
- Guest desktop (둘러보기): the same `app-sidebar` as after login, school "데모 학교"; `sidebar-item`s 홈 · 시약 active, 기록 · QR 찾기 carry `guest-lock`; management items hidden; `guest-banner` across the top of the content area

**`nav-pill`** — Top Nav (mobile pre-login only from 2026-10-08)

- A floating, horizontally-centered stadium bar in `{colors.canvas-soft}`: "Lab_Stock" logomark + wordmark left, section links in `{typography.link}` right, capped by a `button-primary` CTA
- Detaches from the page edge with visible canvas above it; persists as a sticky element on scroll

- After login, the school name in the pill carries a small ▾ (**`nav-account-menu`**, added 2026-10-06): it opens a small `{colors.canvas}` menu (`{rounded.md}`, 1px `{colors.hairline-soft}` outline) with one item "로그아웃"
- **Mobile menu** — added 2026-10-12, **removed 2026-10-13**: no ☰ button and no menu sheet; the 관리 tab (screen 18) carries the same list, and account · 로그아웃 stay under the school name ▾ (`nav-account-menu`)

**Top Nav (Mobile)**

- The pill tightens to logomark + CTA; links collapse behind the pill

**`tab-bar`** — Bottom Tab Bar (Mobile, added 2026-10-02, squared 2026-10-02)

- Primary mobile navigation: a full-width rectangular bar docked to the bottom edge — `{rounded.none}` (0), not a floating pill. The one deliberate exception to the stadium-pill language, so the bar reads as the device's frame rather than a control
- `{colors.canvas}` fill with a 1px `{colors.hairline-soft}` top border, no shadow
- Exactly four `tab-item`s, identical for every role: 홈 · 관리 · QR 스캔 · 기록 (관리 replaced 시약 on 2026-10-13; grid icon of four squares). Equal width — the scan tab is not enlarged. 관리 is active on screen 18 and on every screen under it (2 · 5 · 6 · 7 · 8 · 9 · 11 · 17 and their details)
- Each `tab-item` is an icon above a `{typography.label}` label, tap target ≥ 44px, square (no pill behind it)
- Active tab: `{colors.highlight}` icon with `{colors.ink}` label. Inactive: `{colors.text-muted}` icon and label
- Until screen 12 ships (2026-10-11), the QR 스캔 `tab-item` is grayed (`{colors.text-faint}` icon and label) with a small "준비 중" caption under the icon; tapping it shows `ex-toast` "준비 중이에요". Still four tabs
- Present on every mobile screen after login (screens 2–13, 16, 17, 18); absent on login (screen 1) and on desktop, where `nav-pill` carries navigation
- Role-specific actions (입고, 사용자 관리) are never tabs; they live in the 관리 tab (screen 18, 2026-10-13) and the home `quick-action` area — three tiles (added 2026-10-06): teacher = 사용 기록 입력 · 입고 · 시약장 설정, admin = 입고 · 사용자 관리 · 시약장 설정; mobile lays them out 2 + 1

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
- **`qr-print-sheet`** — bottom sheet (mobile) / right `detail-drawer` with the cabinet choice as a dropdown (desktop, approved 2026-10-08): cabinet choice as `storage-class-chip`-style pills (default = current cabinet, plus "모두"), a white A4 preview tile (`{colors.hairline-soft}` outline, `{rounded.md}`) holding several `qr-label`s, closed by `button-primary` "인쇄". × close top right
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

- **`auto-threshold-badge`** — `{colors.canvas-soft}` pill "자동" in `{colors.ink}` `{typography.label}` beside the threshold in `reorder-threshold` / `reorder-alert-card`, with a caption that states the basis: "최근 사용량으로 계산했어요" (usage history) or "마지막 입고량의 20%로 계산했어요" (no usage yet). Manual and manual-extracted values show no badge. Not pink, not sky-blue — it is information, not a decision
- Screen 5: when the same reagent appears in several rows they merge into one, with a muted line "2개 행을 합쳤어요"

**School level (screen 14, added 2026-10-07)**

- **`school-select-kind`** — `segmented-control` with three options 초등학교 · 중학교 · 고등학교, placed after `school-select-region` and before `school-select-school`. No default: until one is chosen, `school-select-school` is disabled with the placeholder "학교급을 먼저 골라 주세요"
- No schools for that level in the region: in place of the school list, a muted line "이 지역에 {학교급}가 없어요 — 지역을 다시 골라 주세요". No pink

**Select mode & bulk delete (screens 2·17, added 2026-10-11)** — teacher·admin only

- **`list-select-toggle`** — mobile: `button-pill-soft` "선택" at the right of the page head; desktop: `button-outline` "선택" beside the filter. In select mode the head reads quiet "취소" · "N개 선택됨" · "전체 선택"; tapping a row toggles its check instead of opening detail
- **`select-checkbox`** — a 20px circle (`{rounded.full}`): unchecked `{colors.canvas}` with a 1px #adadad ring; checked `{colors.highlight}` fill with a white check. A checked row takes `{colors.highlight-soft}`. Mobile: left of each card. Desktop: the first `data-table` column, the head cell = select all (every row in the current filter and search, across pages, up to 100; beyond that a muted caption "앞의 100개만 골랐어요")
- **`bulk-action-bar`** — appears once one item is chosen: `{colors.canvas}` with a 1px `{colors.hairline-soft}` top edge, `{rounded.none}`; "N개 선택됨" in `{typography.title}` left, `button-primary` "삭제" (ink) right. Mobile: right above the `tab-bar`. Desktop: pinned to the bottom of the content area
- Confirm: `ex-modal-card` "시약 N개를 삭제할까요?" + three names and "외 N개" in `{typography.body-sm}` + "목록·시약장·재주문 알림에서 사라져요. 사용·입고 기록은 남아요." (sensors: "목록과 홈에서 사라져요.") + muted "되돌릴 수 없어요." + `button-outline` "취소" / `button-primary` "삭제". No pink. Then `ex-toast` "시약 N개를 삭제했어요"; the list stays and select mode ends

**Not found (added 2026-10-11)**

- Reuses `ex-empty-state-card`: "페이지를 찾을 수 없어요" + "주소가 바뀌었거나 없는 페이지예요."
- Signed in: inside the app shell (mobile `tab-bar`, desktop `app-sidebar` with no current item) with `button-primary` "홈으로" + `button-outline` "뒤로". Signed out: `web-header` (desktop) / `nav-pill` (mobile), no shell, `button-primary` "처음으로" (→ 15)

**No access (added 2026-10-12)**

- Opening a management address without the role still lands on home (13), which then shows one `ex-toast`: "교사·관리자만 쓸 수 있는 화면이에요" (admin-only screens: "관리자만 쓸 수 있는 화면이에요"). No card, no button, no pink

**Invite cancel (screen 8, added 2026-10-12)** — admin only

- **`invite-more-menu`** — a ⋯ icon button on each pending-invite row (mobile: card top right; desktop: last `data-table` column), opening the same small menu as `reagent-more-menu` with **`invite-cancel`** "초대 취소" in `{colors.ink}`
- Confirm: `ex-modal-card` "{이메일} 초대를 취소할까요?" + "보낸 초대로는 더 이상 가입할 수 없어요." + `button-outline` "닫기" / `button-primary` "초대 취소" (ink; "닫기" so two 취소 never sit side by side). Then `ex-toast` "초대를 취소했어요" and the row leaves

**Manage tab (screen 18, mobile only, added 2026-10-13)**

- Mobile replaces the 시약 tab with **관리**. Screen 18 = `nav-pill` (school name ▾) + page title "관리" in `{typography.heading-2}` + **`manage-list`**: three groups, each a muted `{typography.caption}` title over **`manage-row`**s, groups split by `{colors.hairline-soft}` — 재고 (시약 · 센서 · 시약장, every role) · 입고·주문 (입고 · 실험 매뉴얼 · 재주문 알림, teacher·admin) · 학교 (사용자 · 판매처, admin)
- **`manage-row`** — 56 high, square, `{colors.canvas}`: `{colors.ink}` icon + name in `{typography.title}` + a muted summary caption ("시약 128종 · 재고 부족 3", "센서 12개 · 고장 1", "시약장 2개", "알림 2건", "학생 40 · 교사 3 · admin 1", "4곳") + › at the right. Numbers are plain ink/muted text — no pink, no sky blue. No summary → name only
- **`manage-back`** — screens under 관리 (2 · 5 · 6 · 7 · 8 · 9 · 11 · 17) carry a "‹ 관리" `{typography.link}` at the left of the mobile page head; deeper screens (3, 16 …) keep their ‹ back
- Guest: only 시약 · 센서 rows (demo summaries); the other groups hidden; 관리 tab active, QR 스캔 · 기록 locked
- Desktop does not change — the `app-sidebar` already lists these

**Wipe — all reagents · records (screens 2 · 10, admin only, added 2026-10-13)**

- **`page-more-menu`** — a ⋯ icon button at the right of the page head on screens 2 and 10, both widths, admins only. It opens the small `reagent-more-menu`-style menu with **`reagent-wipe`** "시약 전체 삭제" (screen 2) or **`record-wipe`** "기록 삭제" (screen 10). Not part of select mode. Nothing to delete → the item is `{colors.text-faint}` with a caption "지울 시약이 없어요" / "지울 기록이 없어요"
- Danger is marked in ink, never pink or red: an outlined `{colors.ink}` warning triangle before the title
- **`school-name-confirm`** — caption "확인을 위해 학교 이름 {학교명}을 입력하세요" over a `text-input` whose placeholder is the school name; the confirm button turns on only on an exact match ("학교 이름이 달라요" muted otherwise). A disabled `button-primary` is #e0e0e0 with a #707070 label
- Reagents: `ex-modal-card` — "시약 {N}종을 모두 삭제할까요?" + "목록·시약장·홈·재주문 알림에서 사라지고 되돌릴 수 없어요. 사용·입고 기록은 남아요." + `school-name-confirm` + `button-outline` "닫기" / `button-primary` "전체 삭제". Then `ex-toast` "시약 {N}종을 삭제했어요" and the empty list
- Records: bottom sheet (mobile) / `detail-drawer` (desktop), × close — title "기록 삭제" → **`record-wipe-range`**: `segmented-control` "전체 | 이 날짜 이전" (default 이 날짜 이전) + a date `text-input` (no future; the day itself is kept) → **`wipe-preview`**: a `{colors.canvas-soft}` line "사용 기록 {N}건 · 입고 기록 {M}건을 지워요" + muted "지금 재고 수량은 그대로예요. 수업 정보도 함께 지워져요." (zero → "이 기간에 지울 기록이 없어요", button off) → `school-name-confirm` → `button-primary` "기록 {N+M}건 삭제". Then `ex-toast` "기록 {N}건을 삭제했어요"
- Home numbers and reorder alerts update at once. No entry for teachers, students, or guests

**Feature intro popup (screen 13, teacher·admin, added 2026-10-27 — refs/uibowl-feature-intro-popup-20261027.md)**

- **`feature-intro-popup`** — one reusable popup that introduces a new feature; only its content changes per feature. First feature: AI intake (screen 7 "서류로 입고"). Mobile = bottom sheet (top corners `{rounded.lg}`, dimmed screen behind, no ×). Desktop = centered modal of the `ex-modal-card` family but wider (≈560), × at top right = 닫기. No shadow, no pink — it informs, it does not warn
- Order: tag "새 기능" (`{colors.canvas-soft}` pill, `{typography.caption}`) → title "거래명세서만 올리면 AI가 입고 목록을 채워요" → a picture: a `{colors.canvas-soft}` panel holding a crop of the approved screen 7 (doc upload → review table) → three numbered steps "① 명세서·납품서 사진이나 PDF를 올려요 ② AI가 시약 이름·규격·수량을 읽어요 ③ 확인하고 한 번에 입고해요" → full-width `button-primary` "AI 입고 써 보기"
- **`feature-intro-dismiss`** — the last line: "일주일 동안 보지 않기" left · "닫기" right, both `{colors.text-muted}` text buttons, weaker than the primary button
- Behavior (for development): 닫기 hides it for this visit only; 일주일 동안 보지 않기 hides it for 7 days (browser storage); the primary button opens screen 7 서류로 입고 and the popup never returns for this feature. Shown only when entering home (13), one popup at a time, teachers and admins only — never students or guests. State frames `13-feature-intro-mobile` · `13-feature-intro-desktop` (teacher home under the popup)

**Privacy consent (screen 14, added 2026-10-27 — 요청 10)**

- `terms-agree` keeps its rows ("모두 동의" · "서비스 이용약관 동의 (필수)" · "개인정보 수집·이용 동의 (필수)"); required checks stay — no sign-up without them
- **`privacy-consent-detail`** — pressing › on the privacy row opens, right under it, a `{colors.canvas-soft}` box (`{rounded.md}`) holding a labelled list, not a table: each item = small title in `{typography.caption}` `{colors.text-muted}` over its text in `{typography.body-sm}` `{colors.ink}`, 12 apart. Order: 수집 목적 → 수집 항목 → 보유 기간 ("탈퇴할 때까지 (탈퇴·학교 계정 삭제 시 바로 파기)") → 처리 위탁·국외 이전 (Supabase · Vercel 서울, Google Gemini 국외 — 올린 파일은 읽기에만 쓰고 저장하지 않음) → 동의 거부 권리 → 보호책임자 ({운영자 이름} · {이메일}). The open row's › turns ⌄
- No scrolling inside the box: it opens fully and the page scrolls; the fixed "가입하기" stays
- **`privacy-link`** — last line of the box: "개인정보 처리방침 전문 보기 ↗" (`{typography.link}`, ink underline), opens screen 19 in a new tab so the form is kept. State frame `14-consent`

**Privacy policy (screen 19 `/privacy`, added 2026-10-27 — 요청 10)** — opens without login

- Signed-out shell: desktop `web-header` + one centered reading column (max 720) + `web-footer`; mobile `nav-pill` (signed out) + the same column + `web-footer`. No `tab-bar`, no `app-sidebar`
- **`privacy-doc`** — title "개인정보 처리방침" in `{typography.heading-2}`, "시행일 2026-10-27" caption muted, then **`privacy-toc`** (numbered link list in a `{colors.canvas-soft}` box), then numbered sections (`{typography.title}` heading + `{typography.body}`): 1 수집 목적 · 2 수집 항목 · 3 보유·파기 · 4 처리 위탁·국외 이전 · 5 이용자 권리 (열람·정정·삭제·처리정지 요청 방법) · 6 보호책임자 · 7 시행일
- **`privacy-table`** (section 4) — desktop `data-table` 업체 · 하는 일 · 위치; mobile one `{colors.canvas-soft}` card per company

**Usage guide link (added 2026-10-27 — 요청 10)** — every role, guest included; opens the static guide (`public/guide/`) in a new tab

- **`guide-link`** "사용 가이드 ↗" — desktop: bottom of `app-sidebar`, right above the name · role block, under a `{colors.hairline-soft}` rule; icon + `{typography.body}` `{colors.text-muted}`, 44 high; it is not a `sidebar-item` and is never "current". Mobile: screen 18 gets a fourth group "도움말" at the bottom with one `manage-row`-shaped line whose right mark is ↗ instead of ›. Landing and screen 19: `footer-links`
- ↗ means "opens in a new tab", as in "원문 MSDS 보기 ↗"
- Guide HTML (no Figma frames): Lab_Stock color and type tokens, hero = `{colors.canvas-soft}` band with `{typography.heading-1}` (no display sizes), current TOC item and search hits in `{colors.highlight-soft}`, no pink; screenshots only from guest demo data / 샘플고등학교

**Sign-up error summary (screen 14, added 2026-10-11)**

- **`signup-error-summary`** — one line right above the fixed "가입하기" button: the first error ("약관에 동의해 주세요"), or "… 외 N개" when there are more; `{colors.ink}` text with a small `{colors.text-muted}` info icon. No pink. Pressing the button also scrolls to and focuses the first errored field

**Add record (screen 10, added 2026-10-11)**

- **`record-add`** — `button-primary` "기록 추가" at the right of the page head on both widths (compact 44-high pill on mobile). No floating action button: it would need a shadow and would collide with the `tab-bar`. Every role. Opens an empty screen 4; saving returns to screen 10, where the new rows briefly take `{colors.highlight-soft}`

**Sensors (screen 17, added 2026-10-11)** — ownership only (no readings, no lending)

- Entry: desktop `sidebar-item` "센서" right under 시약 (every role); mobile: the 센서 row of the 관리 tab (screen 18). The `inventory-switch` "시약 | 센서" was removed on 2026-10-13
- **`sensor-list`** — desktop: page head "센서 N개" + search + `list-filter-button` + `list-select-toggle` + **`sensor-doc-add`** `button-outline` "서류로 등록" + **`sensor-add`** `button-primary` "센서 등록" (both teacher·admin, 2026-10-12); a `data-table` with columns 이름 · 종류 · 회사 · 모델 · 수량 · 보관 위치 · 상태, each row a **`sensor-row`**; a row opens a `detail-drawer`. Mobile: the same head under `inventory-switch`, `sensor-row` cards (`{colors.canvas-soft}`, `{rounded.sm}`): name in `{typography.title}`, "온도 · 버니어 · GDX-TMP" caption muted, "3개 · 과학실 뒤 선반", `sensor-status-badge` at the right; the mobile head's `sensor-add` is a `button-pill-soft` "등록" that opens a two-row sheet "서류로 등록" (caption "품의서·영수증을 AI가 읽어요") / "직접 입력". Filter sheet: 종류 as the same collapsed `sensor-type-group` rows (no search; a row shows "화학 · 2개" and starts open when something in it is chosen) → 회사 chips → 상태
- **`sensor-status-badge`** — monochrome, like the MSDS signal word: 고장 = `{colors.ink}` fill with white label; 점검 필요 = `{colors.canvas-soft}` with `{colors.ink}` label; 정상 = no fill, "정상" in `{colors.text-muted}`. Never pink or sky blue
- **`sensor-detail`** — mobile screen / desktop drawer: title + badge → "항목 | 값" rows 종류 · 회사 · 모델 · 수량 · 보관 위치 · 메모 · 등록일 → **`sensor-edit`** `button-outline` "수정" (teacher·admin); head ⋯ → **`sensor-delete`** "센서 삭제" (same confirm as reagent delete, "목록과 홈에서 사라져요")
- **`sensor-form`** — mobile screen / desktop drawer, × close: 이름 → **`sensor-type-select`** (a choose field "종류 [편광 ▾]", see below) → **`sensor-maker-select`** → 모델명 (optional; with 파스코 it becomes `sensor-model-suggest`) → 수량 + "개" → 보관 위치 (`segmented-control` "직접 입력 | 시약장 칸", the latter reuses `location-picker`) → 상태 `segmented-control` 정상 · 점검 필요 · 고장 (default 정상) → 메모 → `button-primary` "저장"
- **`sensor-maker-select`** — opens a bottom sheet (mobile) / dropdown (desktop) with a search `text-input` on top, groups "센서" (버니어 · 사이언스큐브 · 이지메이커 · 고릴라셀 · 파스코 · 동원 · 브로콜리 · 플로우랩 · 이티보드 · 포켓랩 · 헥사보드 · 뉴로그 · 아텍 · 코드위즈) and "현미경" (오선하이테크 · 씨앤에스에듀 · 오맥스 · 한국과학 · 마르시스에듀), and "직접 입력" last (turns into a `text-input`). Chosen item `{colors.highlight-soft}`
- **Sensor types (2026-10-12)** — 27, in four groups: 물리 (온도 · 힘 · 운동(거리) · 가속도 · 회전 · 전압 · 전류 · 자기장 · 조도 · 소리 · 압력 · 방사선) · 화학 (pH · 전도도 · 용존산소 · 이온·수질 · 분광 · 편광 · 색·탁도 · CO₂ · 산소) · 생명·지구 (심박·생체 · 습도 · 기상) · 장비 (인터페이스 · 코딩 보드 · 기타). Korean names only on screen
- **`sensor-type-select`** — a `{colors.field}` choose field (placeholder "종류 고르기"). It opens **`sensor-type-sheet`**: bottom sheet (mobile) / dropdown (desktop) with a search `text-input` "종류 검색" on top, then four collapsed **`sensor-type-group`** rows (2026-10-12) — group name in `{typography.title}` + count in `{typography.caption}` `{colors.text-muted}` ("물리 12") + ▸/▾ at the right, 52 high, split by `{colors.hairline-soft}`. Tapping a row opens only that group's wrapping chips (several may be open); the group holding the current choice starts open; typing opens just the groups with matches and shows only matching chips ("맞는 종류가 없어요" muted when none). The 27 are never all open at once. The chosen chip `{colors.highlight-soft}` + 1px `{colors.highlight}` border; one pick closes it
- **`sensor-model-suggest`** (company = 파스코) — a candidate list under the 모델명 input (dropdown on desktop): each row the model number in `{typography.title}` + "무선 편광계 · 편광" in `{typography.caption}` `{colors.text-muted}`, matched letters bold, up to six rows, a quiet "목록에 없어요 — 그대로 적기" last. Picking fills 모델명, 종류, and 이름 when empty; the filled fields flash `{colors.highlight-soft}` and **`catalog-fill-note`** reads muted "카탈로그에서 종류·이름을 채웠어요" under the field. Everything stays editable. Other companies: typed as before. The model number stays a caption on rows and a "모델" column / row
- **Sensor document intake (2026-10-12)** — teacher·admin, not in guest. Same flow as screen 7's document intake: mobile screen / desktop page (not a drawer). Step 1 `doc-upload` (PDF·JPG·PNG, one file, 4MB, "서버에 보관하지 않아요") + `button-primary` "AI로 읽기", reading state "서류를 읽는 중이에요". Step 2 `doc-intake-table` "읽은 센서 N개": 품명 · 회사 · 모델 · 수량 (+ desktop column 연결), each with a **`sensor-link`** line — "기존 센서에 더하기 · {이름} · 지금 3개 → 5개" by default when the same company + model exists, with quiet "바꾸기" · "빼기"; otherwise "새 센서로 등록", which expands **`new-sensor-fields`** (이름 · 종류 · 회사 · 모델 · 수량 · 보관 위치 · 상태, catalog values tagged muted "카탈로그"). Non-sensor items fold into "센서 아님 N개". Sticky `button-primary` "확인 후 등록 · N개" (one transaction, 1–50). Afterwards `ex-toast` "센서 N개를 등록했어요" → screen 17 with the changed rows briefly `{colors.highlight-soft}`. Zero found / failure reuses the 7-doc-fail shape: `ex-empty-state-card` "센서를 찾지 못했어요" (or "서류를 읽지 못했어요") + "다른 서류를 올리거나 직접 입력해 주세요" + `doc-upload` + `button-outline` "직접 입력". No pink
- Empty: `ex-empty-state-card` "아직 등록한 센서가 없어요" + "무선 센서와 현미경을 등록해 두면 수량과 상태를 한눈에 봐요" + `sensor-add` (teachers·admins; students see the text only)
- Home: **`sensor-alert-tile`** "고장·점검 필요 센서 N" for teachers·admins, only when N ≥ 1 — a desktop "지금 처리할 것" tile, a mobile `home-summary` line. Monochrome
- Guest: demo sensors, read-only

**List filter (screen 2, added 2026-10-07)** — every role, guest included

- **`list-filter-button`** — `button-pill-soft` "필터" with a filter icon, right of the search `text-input`. When filters are applied it carries a count pill (`{colors.highlight-soft}` fill, 1px `{colors.highlight}` border, `{colors.ink}` `{typography.label}`). The `segmented-control` "전체 / 재고 부족" stays as is
- **`list-filter-sheet`** — bottom sheet (mobile) / dropdown panel under the button (desktop), × close. Sections in order: 정렬 (`segmented-control`-style options 이름순 · 재고 적은 순 · 최근 입고순), 보관 분류 (`storage-class-chip`s, multi-select, plus "분류 없음"; selected = `{colors.highlight-soft}` + `{colors.highlight}` border), 보관 위치 (`cabinet-number` + name select → slot select, plus a "칸 없음만" toggle), "MSDS 없는 시약만" toggle. Footer `button-outline` "초기화" + `button-primary` "{N}종 보기"
- **`filter-chip-row`** — above the list: one `{colors.canvas-soft}` pill per applied filter with ×, a quiet "모두 지우기", and the result count "12종" in `{typography.caption}`. With "MSDS 없는 시약만" on, teachers·admins also see `msds-bulk-banner`
- No results: `ex-empty-state-card` "조건에 맞는 시약이 없어요" + `button-outline` "필터 지우기". No pink

**Usage date (screens 4·10, added 2026-10-07)**

- **`usage-date`** — "사용일" date `text-input`, the first shared field under the reagent list on screen 4 (2026-10-10), same shape as screen 7's 입고일. Defaults to today; future dates are disabled
- **`past-date-note`** — when the date is not today, a muted line above the save button: "10월 3일 사용으로 기록해요"
- Screen 10 groups and sorts by 사용일; when the recorded day differs, a muted caption "10월 6일에 기록" under the row

**Batch usage record (screen 4, added 2026-10-10)** — every role; one experiment uses several reagents, so one record holds several

- Mobile: its own screen. Desktop: a page in the content area (not a drawer). Entering from screen 3 "사용 기록" starts with that reagent already in the list; entering from home or the 기록 tab starts empty
- **`reagent-add`** — `button-pill-soft` "+ 시약 추가" above the list. Mobile opens **`reagent-picker`** as a bottom sheet: search `text-input` on top, recently used reagents first, each row with a check (checked row = `{colors.highlight-soft}`), reagents already in the list marked "담음" muted, footer `button-primary` "{N}개 담기". Desktop: the search `text-input` above the table drops a `reagent-picker` list under it; clicking a row adds it at once (several may be checked)
- **`usage-batch-list`** — head "담은 시약 N개". Mobile: a stack of **`usage-item-row`** cards (`{colors.canvas-soft}`, `{rounded.sm}`): reagent name in `{typography.title}` + "현재 120 mL" in `{typography.caption}` `{colors.text-muted}`, then a numeric `text-input` with the unit and a quiet "빼기". Desktop: a `data-table` with columns 시약명 · 현재 재고 · 사용량 (input + unit) · 빼기
- Shared fields under the list, in order: `usage-date` → `class-select` (optional) → 메모 (optional). The user is the signed-in person
- Save: a bar pinned to the bottom (above the `tab-bar` on mobile, sticky bottom bar on desktop) with `button-primary` "사용 기록 저장 · N개"; disabled while the list is empty or any row has an error. One save = one transaction: if any row fails, nothing is saved
- **`usage-over-stock`** — when the amount is more than the current stock, a line under that row in the `mix-warning` shape: `{colors.accent-soft}` fill, `{colors.accent}` icon, `{colors.ink}` text "재고 120 mL보다 많아요". Pink here is the stock-shortage signal. A blank or zero amount gets the 2px ink ring and a muted line "사용량을 적어 주세요" (no pink). A server rejection shows `ex-toast` "저장하지 못했어요 — 표시한 시약을 확인해 주세요" and marks the rows
- Empty: `ex-empty-state-card` "시약을 골라 주세요" + `reagent-add`. After saving: `ex-toast` "N개 시약 사용을 기록했어요"

**Class (screens 4·10, added 2026-10-10)** — optional

- **`class-select`** — "수업 (선택)": 학년 select (초등학교 1–6, 중·고등학교 1–3, by the school's level) + 반 select (1–20) + 수업명 `text-input` (placeholder "수업명 (예: 통합과학)", 20 characters). All three may stay empty. Mobile: 학년 and 반 share one row, 수업명 full width below. Desktop: one "수업 | [학년▾] [반▾] [수업명]" form row
- **`recent-class-chip`** — above the selects, caption "최근" + up to three `{colors.canvas-soft}` pills such as "1학년 2반 · 통합과학"; tapping one fills all three fields; the chosen chip takes `{colors.highlight-soft}` + 1px `{colors.highlight}` border
- **`class-label`** (screen 10) — "1학년 2반 · 통합과학", only the parts that exist ("1학년", "통합과학"). Mobile: a muted caption under the record row. Desktop: a `data-table` column "수업" ("—" in `{colors.text-faint}` when empty) and a "수업 | 값" row in the record drawer
- **`class-filter`** (screen 10) — `button-pill-soft` "반: 전체 ▾" above the records → bottom sheet (mobile) / dropdown (desktop): 학년 (전체 · 1 …) then 반 (학년 전체 · 1 …)

**Reagent delete (screens 3·10, added 2026-10-10)** — teacher·admin only

- **`reagent-more-menu`** — a ⋯ icon button at the top right of `reagent-detail-card` (mobile) or in the `detail-drawer` head left of × (desktop). It opens a small `{colors.canvas}` menu (`{rounded.md}`, 1px `{colors.hairline-soft}` outline) with **`reagent-delete`** "시약 삭제" in `{colors.ink}`. Never rendered for students or guests. Not on screen 2 table rows — deletion lives in one place
- Confirm: `ex-modal-card` "'{시약명}' 시약을 삭제할까요?" + "목록·시약장·재주문 알림에서 사라져요. 사용·입고 기록은 남아요." + muted "되돌릴 수 없어요." with `button-outline` "취소" and `button-primary` "삭제" — ink, like the cabinet delete. No pink: deleting is not a stock or safety signal. Afterwards `ex-toast` "시약을 삭제했어요" → screen 2
- **`deleted-reagent-tag`** (screen 10) — records of a deleted reagent keep their row: the name in `{colors.text-muted}` followed by a `{colors.canvas-soft}` pill "삭제된 시약" (`{colors.ink}` `{typography.label}`); no link to reagent detail

**Reagent slots (screens 11·3, added 2026-10-06)**

- **`slot-count`** — small `{colors.canvas}` pill inside a `cabinet-slot` showing how many reagents it holds ("3"), `{typography.label}` `{colors.ink}`. Empty slots show nothing. Never pink — a count is not a decision signal
- **`slot-sheet`** — tapping a `cabinet-slot` opens a sheet: slot name ("좌 2단") + its `storage-class-chip`s, the reagents in it as `reagent-row`s, each with a quiet "빼기" text action (teacher·admin). Students see the list only
- **`slot-assign`** — `button-primary` "시약 넣기" at the bottom of `slot-sheet` (teacher·admin only); opens a picker list of "칸 없음" reagents with a search `text-input`
- Class mismatch (warn, never block): when a reagent's storage class is not among the slot's classes, show `mix-warning` "이 칸은 {분류} 칸이에요 — 그래도 넣을 수 있어요"; when it forms a `cabinet.incompatible` pair with the slot or a reagent already there, the same `mix-warning` with stronger copy "{A}와 {B}는 섞으면 위험해요". Saving stays enabled in both cases
- **`reagent-location`** (screen 3) — a row in `reagent-detail-card`: caption "보관 위치" + "`cabinet-number` 이름 · 좌 2단" or "칸 없음" in `{colors.text-muted}`. Teachers·admins get **`location-edit`** — `button-pill-soft` "위치 바꾸기" — which opens **`location-picker`**: `cabinet-switcher` on top, the cabinet's `cabinet-slot` grid below (each with `slot-count`), tap a slot to choose; "칸 없음으로" as a quiet text action; `mix-warning` appears under the grid on mismatch; closed by `button-primary` "저장"
- **`reorder-threshold`** (screen 3) — a row in `reagent-detail-card`: caption "재주문 기준" + amount + unit, or "아직 없어요" muted. Teachers·admins get **`threshold-edit`** — tapping turns the amount into a numeric `text-input` with unit and `button-primary` "저장". Same field as the screen 5 extraction result

**Landing (screen 15, added 2026-10-03)** — the pre-login first screen

- **`landing-hero`** — no "Lab_Stock" wordmark (the top bar already carries it — 2026-10-12; mobile opens with a small muted tag "과학실 시약·센서 관리"), a one-line description in `{typography.heading-1}`, a `{typography.body-lg}` light subtitle. Monochrome; no school name (nothing is selected before sign-up)
- **`feature-card`** — 3–4 cards (학교별 분리 · NEIS 학교 선택 · QR 스캔 · 재고 부족 알림): `{colors.canvas-soft}` fill, `{rounded.md}`, icon in `{colors.highlight}` + title + one line of body. The 재고 부족 알림 card may show a small `badge-low-stock` as an example (pink stays inside the badge)
- **`landing-cta`** — bottom action area: `button-primary` "회원가입" (→ 14) and `button-outline` "로그인" (→ 1). No tab bar on this screen
- **`guest-entry`** — a third, quieter action under the CTAs: `button-pill-soft` "둘러보기" (→ guest home). Added 2026-10-03

**Guest mode (둘러보기, added 2026-10-03)** — read-only tour on the demo school

- **`guest-banner`** — full-width strip at the top of every guest screen, under `nav-pill`: `{colors.highlight-soft}` fill, `{rounded.none}`, text "둘러보는 중 — 가입하면 우리 학교 데이터로 시작해요" in `{colors.ink}` `{typography.body-sm}`, a compact `button-primary` "가입하기" (→ 14) at the end
- **`guest-lock`** — a small lock icon in `{colors.text-muted}`. Sits on every write action that stays visible but is disabled (e.g. "사용 기록 입력" in `quick-action`, "사용 기록" on reagent detail) and on the QR 스캔·기록 `tab-item`s. Tapping a locked item shows an `ex-toast` "가입하면 쓸 수 있어요" — never pink (no decision is pending)
- School name shown everywhere is the single demo school "데모 학교"

**MSDS summary (screen 16, added 2026-10-08)** — every role, guest included

- Opened by every `msds-entry` "MSDS 보기" instead of the outside site. Mobile: its own screen — back ‹ + "MSDS · {시약명}" in `{typography.heading-3}`, source line "물질안전보건자료 · 한국산업안전보건공단" in `{typography.caption}` `{colors.text-muted}`. Desktop: inside a `detail-drawer` over the reagent `data-table`
- **`msds-summary`** — the body: signal word pill ("위험" = `{colors.ink}` fill with white label; "경고" = `{colors.canvas-soft}` with `{colors.ink}` label — never pink or red), then the pictogram row, then four sections titled with their MSDS numbers "2. 유해·위험성" · "4. 응급조치 요령" · "7. 취급 및 저장방법" · "8. 노출방지 및 개인보호구" (`{typography.title}`), each a 3-line summary in `{typography.body}` + a quiet "더 보기" that expands it; an empty section reads "내용이 없어요" muted
- **`ghs-pictogram`** — the GHS standard: white diamond with a red #ff0000 frame and a black symbol, name below in `{typography.caption}` (산화성 · 부식성 · 급성 독성 …, 9 kinds). The only place #ff0000 may appear (a regulatory symbol, not a brand color); it never replaces the pink decision signal
- **`msds-original-link`** — full-width `button-outline` "원문 MSDS 보기 ↗" at the bottom, opens the KOSHA page in a new window. When the linked MSDS is not from KOSHA (a typed address), the summary is skipped and only this button shows
- Loading: **`msds-skeleton`** gray bars (`{colors.canvas-soft}`) in place of the sections. Failure: `ex-empty-state-card` "요약을 불러오지 못했어요" + `msds-original-link`

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

- Sheets and forms that open over a screen carry a × close at top right (added 2026-10-06 — user-manage sheet on 8, vendor-register form on 9). On 8 the delete confirm reads "{이름} · 사용·입고 기록은 남아요" and invite is email + role (학생 · 교사), no name field; the sheet head shows "학생 a · 교사 b · admin c". On 9 there is no extra-info field and vendor rows show name + contact only (no website)

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
- Reserve `{colors.accent}` for decision signals only (`badge-low-stock`, `reorder-alert-card`, `mix-warning`, `usage-over-stock`).
- Use `{colors.highlight}` / `{colors.highlight-soft}` for selection and emphasis everywhere else; keep text on them in `{colors.ink}`.
- Set every heading in Pretendard Bold 700 with line-height 1.3–1.35.
- Pair Bold 700 headings with 300-weight `{typography.body-lg}` subtitles for hierarchy without color.
- Keep MSDS QR codes at 1:1, uncropped.

### Don't

- Don't add drop shadows — elevation is fills and hairlines only.
- Don't use `{colors.accent}` for CTAs; primary actions are always `{colors.primary}` ink pills.
- Don't introduce accent hues beyond pink and sky blue, gradients on UI chrome, or colored section bands (neutral white/#f3f3f3/ink bands on the landing are allowed).
- Don't use sky blue as a text color, inside a pink decision signal, or as the `button-primary` fill.
- Don't apply letter-spacing or all-caps styling; the type system runs at natural tracking in sentence case.
- Don't put borders on form fields at rest — inputs are `{colors.field}` tint fills; the border appears only as the 2px ink focus ring.
- Don't square off pill geometry at small sizes — badges, chips, and toggles stay stadium-shaped.
