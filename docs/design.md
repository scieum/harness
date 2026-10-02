## Overview

Lab_Stock is a SaaS for high-school science labs — it tracks each reagent's type, stock level, intake date, usage date, and user, links each reagent to its MSDS through a QR code, and connects the school to a vendor when stock runs low. Its own interface is engineered to get out of the way. The system is strictly monochrome: near-black ink (`{colors.ink}` — #141414) on a pure white canvas (`{colors.canvas}`), with structure carried by a ladder of barely-perceptible neutral tints rather than by shadows or color. The reagent data the app exists to show — names, quantities, dates, stock status — is what the chrome frames, the way a gallery wall frames paintings.

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

**`reorder-alert-card`** — reorder alert → vendor link

- `{colors.canvas-soft}` fill, borderless, `{rounded.md}` corners, padding `{spacing.lg}`
- `badge-low-stock` + reagent name in `{typography.heading-4}` + required vs. current amount in `{typography.body}`, closed by a `button-primary` "판매처 연결"

### Inputs & Forms

**`text-input`**

- `{colors.field}` fill, no border, `{colors.ink}` text with `{colors.text-faint}` placeholder, `{rounded.sm}` corners, padding `{spacing.sm} {spacing.md}`

**`text-input-focused`**

- Same chrome plus a 2px `{colors.ink}` ring — focus is signaled in ink, consistent with the monochrome system

### Navigation

**`nav-pill`** — Top Nav (Desktop)

- A floating, horizontally-centered stadium bar in `{colors.canvas-soft}`: "Lab_Stock" logomark + wordmark left, section links in `{typography.link}` right, capped by a `button-primary` CTA
- Detaches from the page edge with visible canvas above it; persists as a sticky element on scroll

**Top Nav (Mobile)**

- The pill tightens to logomark + CTA; links collapse behind the pill

**`tab-bar`** — Bottom Tab Bar (Mobile, added 2026-10-02, squared 2026-10-02)

- Primary mobile navigation: a full-width rectangular bar docked to the bottom edge — `{rounded.none}` (0), not a floating pill. The one deliberate exception to the stadium-pill language, so the bar reads as the device's frame rather than a control
- `{colors.canvas}` fill with a 1px `{colors.hairline-soft}` top border, no shadow
- Exactly four `tab-item`s, identical for every role: 홈 · 시약 · QR 스캔 · 기록. Equal width — the scan tab is not enlarged
- Each `tab-item` is an icon above a `{typography.label}` label, tap target ≥ 44px, square (no pill behind it)
- Active tab: `{colors.highlight}` icon with `{colors.ink}` label. Inactive: `{colors.text-muted}` icon and label
- Present on every mobile screen after login (screens 2–13); absent on login (screen 1) and on desktop, where `nav-pill` carries navigation
- Role-specific actions (입고, 사용자 관리) are never tabs; they live in the home `quick-action` area

### Signature Components

**Landing (screen 15, added 2026-10-03)** — the pre-login first screen

- **`landing-hero`** — "Lab_Stock" wordmark, a one-line description in `{typography.heading-1}`, a `{typography.body-lg}` light subtitle. Monochrome; no school name (nothing is selected before sign-up)
- **`feature-card`** — 3–4 cards (학교별 분리 · NEIS 학교 선택 · QR 스캔 · 재고 부족 알림): `{colors.canvas-soft}` fill, `{rounded.md}`, icon in `{colors.highlight}` + title + one line of body. The 재고 부족 알림 card may show a small `badge-low-stock` as an example (pink stays inside the badge)
- **`landing-cta`** — bottom action area: `button-primary` "회원가입" (→ 14) and `button-outline` "로그인" (→ 1). No tab bar on this screen

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
