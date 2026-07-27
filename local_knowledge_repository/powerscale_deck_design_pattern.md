# Power Scale Ventures — Executive Pitch Deck Design Pattern Specification

**Source Reference**: `POWER SCALE  (1).pdf` (17 Slides)  
**Extracted Date**: July 27, 2026  
**Target Purpose**: Standardized PPT / Presentation Template & HTML Design System  

---

## 1. Aesthetic Identity & Design Philosophy

The Power Scale design language is an **Apple-inspired, executive flat design system**. It prioritizes high-contrast typography, generous negative space, structured card containers, ultra-clean borders, and electric blue accenting to convey institutional credibility and modern precision.

* **Aspect Ratio**: 16:9 Landscape ($1920 \times 1080\text{px}$ aspect ratio / $1500 \times 844\text{px}$ rendering canvas).
* **Theme System**: Dual Light / Dark themes.
  * **Primary Light Theme**: Default for content, data tables, pipeline lists, and bios (`#fbfbfd` / `#ffffff` background).
  * **Secondary Dark Theme**: Used for high-impact transition slides, value propositions, and summary cards (`#000000` background).

---

## 2. Color Palette & Exact HEX Tokens

| Token Name | HEX Code | Role & Usage |
| :--- | :---: | :--- |
| **Primary Accent Blue** | `#0066ff` | Brand accent, primary category eyebrows, KPI highlights, active pills, chevron icons. |
| **Pure White** | `#ffffff` | Primary background (Light Mode) / Heading text (Dark Mode). |
| **Off-White Canvas** | `#fbfbfd` | Default slide background tone (Light Mode). |
| **Card Fill (Light)** | `#f5f5f7` | Default card background container (Light Mode). |
| **Secondary Card Fill** | `#f0f0f2` | Alternate table row or nested card container. |
| **Card Fill (Dark)** | `#1d1d1f` | Card container fill (Dark Mode). |
| **Pure Black Heading** | `#000000` | Main slide titles (H1), hero headlines, slide numbers. |
| **Primary Body Text** | `#1d1d1f` | Paragraph body copy, lead text. |
| **Secondary Body Copy** | `#515154` | Subtitles, secondary bullet points, table cell text. |
| **Muted Caption Text** | `#86868b` | Eyebrow badges, footer confidentiality text, inactive metadata. |
| **Clean Border Line** | `#e5e5e7` | 1px card outlines, horizontal divider rules, table borders. |
| **Soft Blue Badge Fill** | `rgba(0,102,255,0.10)` | Background tint for active pill badges and status tags. |

---

## 3. Typography Hierarchy (Font Family: `Inter`)

All slides exclusively use the **Inter** sans-serif font family:

| Element | Font Weight | Point Size | Letter Spacing | Color |
| :--- | :--- | :---: | :---: | :--- |
| **Cover / Hero Title** | `Inter ExtraBold` | 48pt – 60pt | -1.0px | `#000000` or `#ffffff` |
| **Slide Main Title (H1)** | `Inter Bold` | 28pt – 32pt | -0.5px | `#000000` (Light) / `#ffffff` (Dark) |
| **Eyebrow Category Tag** | `Inter Bold` / `SemiBold` | 10pt – 11pt | +1.5px (UPPERCASE) | `#0066ff` or `#86868b` |
| **Card Header / Subtitle (H2)**| `Inter Bold` | 14pt – 16pt | -0.2px | `#000000` or `#1d1d1f` |
| **Body Paragraph** | `Inter Regular` | 10.5pt – 11pt | 0.0px (1.4 line-height) | `#1d1d1f` or `#515154` |
| **KPI Big Numbers** | `Inter ExtraBold` | 32pt – 40pt | -1.0px | `#0066ff` or `#000000` |
| **Pill Badges / Tags** | `Inter SemiBold` | 9pt – 10pt | +0.5px | `#0066ff` |
| **Footer Disclaimer** | `Inter Regular` | 8pt | +1.0px (UPPERCASE) | `#86868b` |

---

## 4. Component Layout Patterns

### A. Slide Header Block
```
┌────────────────────────────────────────────────────────────────────────┐
│ EYEBROW CATEGORY TAG (#0066ff or #86868b, 10pt UPPERCASE)              │
│ Main Slide Heading Title (#000000, 30pt Bold)                          │
└────────────────────────────────────────────────────────────────────────┘
```

### B. Standard 3-Card Grid (Light Theme)
```
┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐
│ Card Title      │  │ Card Title      │  │ Card Title      │
│ [Pill Tag]      │  │ [Pill Tag]      │  │ [Pill Tag]      │
│                 │  │                 │  │                 │
│ Body text block │  │ Body text block │  │ Body text block │
└─────────────────┘  └─────────────────┘  └─────────────────┘
* Fill: #f5f5f7 | Border: 1px #e5e5e7 | Radius: 16px | Padding: 24px
```

### C. Large KPI Stat Display Card
```
┌────────────────────────────────────────────────────────────────────────┐
│  $100M+                        200+                   65               │
│  Target Fund Size              Global Founder Network  Active Deals    │
└────────────────────────────────────────────────────────────────────────┘
* Stat: 36pt Inter ExtraBold (#0066ff) | Label: 10pt Inter Regular (#515154)
```

### D. Footer Rule & Metadata Bar
```
──────────────────────────────────────────────────────────────────────────
POWERSCALE VENTURES | CONFIDENTIAL INSTITUTIONAL THESIS                 04
```
* Border-top: 1px solid `#e5e5e7`
* Text: 8pt UPPERCASE `#86868b`

---

## 5. Slide Structural Archetypes in the Deck

1. **Cover Slide (Slide 1 & 17)**: Black / White full-screen canvas, bold brand wordmark, electric blue accent line/tagline.
2. **Overview / Executive Summary (Slide 2 & 3)**: Left 1/3 title & thesis + Right 2/3 2x2 grid of soft gray feature cards (`#f5f5f7`).
3. **Pipeline & Table Cards (Slide 4, 6, 11)**: Structured cards with pill tags, company logos/metrics, and horizontal data rows.
4. **Dark Value Proposition (Slide 10)**: Pure black slide with dark gray cards (`#1d1d1f`), glowing white titles, and electric blue numbered callouts (`01`, `02`, `03`).
5. **Leadership & Team Bios (Slide 14 & 15)**: Left profile photo container + Right structured bio card with background highlights, track record pills, and advisory tags.
