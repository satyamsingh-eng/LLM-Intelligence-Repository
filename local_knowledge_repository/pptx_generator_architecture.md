# PowerScale PPTX Generator Architecture & Coordinate Math Specification

## 1. Overview & Canvas Setup

This document defines the exact python-pptx helper abstractions, color constants, layout coordinate math, and verification architecture for programmatically generating native PowerScale presentations.

### Presentation Canvas Specifications
* **Aspect Ratio:** 16:9 Widescreen
* **Dimensions:** 13.333 inches (width) × 7.500 inches (height)
* **python-pptx Canvas Setup:**
  ```python
  from pptx import Presentation
  from pptx.util import Inches

  prs = Presentation()
  prs.slide_width = Inches(13.333)
  prs.slide_height = Inches(7.500)
  ```

---

## 2. PowerScale Color Constants

The design palette strictly adheres to PowerScale brand design guidelines using exact `RGBColor` constants from `pptx.dml.color`.

| Constant Name | Color Description | Hex Code | RGB Color Object | Primary Application |
| :--- | :--- | :--- | :--- | :--- |
| `BLUE` | PowerScale Primary Accent | `#0066FF` | `RGBColor(0, 102, 255)` | Header Eyebrows, Big KPI Numbers, Active Accents |
| `BLACK` | Pure Black | `#000000` | `RGBColor(0, 0, 0)` | High Contrast Element Fills / Accents |
| `CANVAS` | Off-White Background | `#FBFBFD` | `RGBColor(251, 251, 253)` | Slide Background Fill |
| `CARD_BG` | Card Container Background | `#F5F5F7` | `RGBColor(245, 245, 247)` | Card / Tile Container Solid Fill |
| `CARD_BORDER` | Card Border Stroke | `#E5E5E7` | `RGBColor(229, 229, 231)` | 1pt Card Outline Stroke |
| `TEXT_BODY` | Primary Body Text | `#1D1D1F` | `RGBColor(29, 29, 31)` | Slide Titles, Card Headers, Main Body Copy |
| `TEXT_MUTED` | Secondary / Muted Text | `#86868B` | `RGBColor(134, 134, 139)` | Subtitles, KPI Descriptions, Footers |

---

## 3. Precision Positioning & Layout Coordinate Math

To guarantee **zero text clipping**, **zero line wrapping errors**, and **zero shape overlaps**, all layouts use explicit, bounded grid calculations.

### Standard Slide Bounds & Margins
* **Left Outer Margin:** `0.800 inches`
* **Right Outer Margin:** `0.800 inches`
* **Usable Content Width:** `13.333 - (2 × 0.800) = 11.733 inches`
* **Header Block:**
  * Top: `0.600 inches`
  * Height: `1.000 inches`
* **Usable Content Area:**
  * Top: `1.800 inches`
  * Bottom: `6.700 inches`
  * Height: `4.900 inches`
* **Footer Block:**
  * Top: `7.000 inches`
  * Height: `0.300 inches`

### Grid Coordinate Math Formula
For an $N \times M$ grid of card containers:
$$\text{card\_w} = \frac{\text{CONTENT\_WIDTH} - (\text{gap\_x} \times (N - 1))}{N}$$
$$\text{card\_h} = \frac{\text{CONTENT\_HEIGHT} - (\text{gap\_y} \times (M - 1))}{M}$$
$$\text{left}_{c} = \text{MARGIN\_LEFT} + c \times (\text{card\_w} + \text{gap\_x}) \quad \text{for } c \in [0, N-1]$$
$$\text{top}_{r} = \text{CONTENT\_TOP} + r \times (\text{card\_h} + \text{gap\_y}) \quad \text{for } r \in [0, M-1]$$

### Exact Standard Layout Calculations

#### A. 4-Column KPI Dashboard Row
* **Columns ($N$):** 4, **Rows ($M$):** 1
* **Gap ($X$):** `0.300 inches`
* **Calculated Card Width:** $(11.733 - (3 \times 0.300)) / 4 = 2.708 \text{ inches}$
* **Calculated Card Height:** `2.200 inches`
* **Coordinates:**
  * Card 1: `(X: 0.800", Y: 1.800", W: 2.708", H: 2.200")`
  * Card 2: `(X: 3.808", Y: 1.800", W: 2.708", H: 2.200")`
  * Card 3: `(X: 6.816", Y: 1.800", W: 2.708", H: 2.200")`
  * Card 4: `(X: 9.824", Y: 1.800", W: 2.708", H: 2.200")` (Right edge = `12.532"`, Right Margin = `0.801"`)

#### B. 3-Column Feature Grid
* **Columns ($N$):** 3, **Rows ($M$):** 1
* **Gap ($X$):** `0.350 inches`
* **Calculated Card Width:** $(11.733 - (2 \times 0.350)) / 3 = 3.677 \text{ inches}$
* **Calculated Card Height:** `4.900 inches`
* **Coordinates:**
  * Card 1: `(X: 0.800", Y: 1.800", W: 3.677", H: 4.900")`
  * Card 2: `(X: 4.827", Y: 1.800", W: 3.677", H: 4.900")`
  * Card 3: `(X: 8.854", Y: 1.800", W: 3.677", H: 4.900")` (Right edge = `12.531"`, Right Margin = `0.802"`)

#### C. 2-Column Split Feature Row
* **Columns ($N$):** 2, **Rows ($M$):** 1
* **Gap ($X$):** `0.300 inches`
* **Calculated Card Width:** $(11.733 - 0.300) / 2 = 5.716 \text{ inches}$
* **Calculated Card Height:** `2.400 inches`
* **Coordinates:**
  * Card 1: `(X: 0.800", Y: 4.300", W: 5.716", H: 2.400")`
  * Card 2: `(X: 6.816", Y: 4.300", W: 5.716", H: 2.400")` (Right edge = `12.532"`, Right Margin = `0.801"`)

---

## 4. Python Helper Functions API Reference

The helper module (`powerscale_pptx.py`) provides 4 core slide component abstraction functions and helper math utilities.

### 1. `add_header(slide, eyebrow_text, title_text, left=MARGIN_LEFT, top=MARGIN_TOP_HEADER, width=CONTENT_WIDTH, height=Inches(1.0))`
Constructs a standard PowerScale title block with a blue uppercase eyebrow and dark bold slide title.
* **Text Frame Configuration:** `word_wrap = True`, zero internal margins (`margin_left/right/top/bottom = Inches(0)`).
* **Eyebrow Style:** 12pt Calibri Bold, `BLUE` (`#0066FF`), space after = 4pt.
* **Title Style:** 32pt Calibri Bold, `TEXT_BODY` (`#1D1D1F`).

### 2. `add_card(slide, left, top, width, height, bg_color=CARD_BG, border_color=CARD_BORDER)`
Draws a background container shape with solid fill and 1pt stroke.
* **Shape:** `MSO_SHAPE.RECTANGLE`
* **Fill:** Solid `CARD_BG` (`#F5F5F7`)
* **Line:** 1pt `CARD_BORDER` (`#E5E5E7`)

### 3. `add_kpi_block(slide, left, top, width, height, number_str, label_text, bg_color=CARD_BG, border_color=CARD_BORDER, num_color=BLUE)`
Constructs a KPI metric card with a large stat number and descriptive label.
* **Container:** Card rectangle via `add_card()`.
* **Internal Text Frame:** Padded by `pad_x = Inches(0.25)`, `pad_y = Inches(0.25)`, zero internal margins.
* **Big Number Style:** 44pt Calibri Bold, `BLUE` (`#0066FF`), space after = 6pt.
* **Label Style:** 13pt Calibri Regular, `TEXT_BODY` (`#1D1D1F`).

### 4. `add_footer(slide, slide_num_str, left=MARGIN_LEFT, top=FOOTER_TOP, width=CONTENT_WIDTH, height=Inches(0.3))`
Constructs the slide footer with platform branding and right-aligned slide number.
* **Branding Run:** "PowerScale Platform Architecture" in 10pt Calibri `TEXT_MUTED` (`#86868B`).
* **Slide Number Box:** Right-aligned 10pt Calibri `TEXT_MUTED` (`#86868B`).

### 5. `calculate_grid_positions(cols, rows, left, top, width, height, gap_x, gap_y)`
Generates list of `(left, top, card_w, card_h)` coordinate tuples for structured grids.

---

## 5. Verification & Test Pipeline

### Execution Steps
1. **Slide Generation:** `generate_test_deck.py` created `powerscale_demo.pptx` featuring 3 distinct slide layouts (Title slide, KPI Dashboard slide, 3-Card Architecture slide).
2. **OOXML Schema Validation:** Ran PowerPoint validator script (`validate.py`).
   * **Result:** `All validations PASSED!` (No corrupt XML elements, bad relationships, or invalid tags).
3. **Headless Conversion & Visual Inspection:**
   * Converted `.pptx` to `.pdf` via headless LibreOffice (`soffice --headless --convert-to pdf`).
   * Exported PDF pages to JPEG images via `pdftoppm -jpeg -r 150`.
   * Inspected rendered slides using multimodal vision model (`vision_analyze`).
   * **Audit Outcome:** Verified clean typography alignment, crisp background card fills, zero text clipping or overlapping, accurate brand color rendering, and consistent margins across all slides.

---

## 6. Code Artifacts Created

* `powerscale_pptx.py` - Core helper module containing exact constants, mathematical bounds algorithms, and shape builders.
* `generate_test_deck.py` - Complete test suite script demonstrating PowerScale slide deck generation.
* `powerscale_demo.pptx` - Validated PowerPoint presentation output.
* `local_knowledge_repository/pptx_generator_architecture.md` - Complete architectural specifications and coordinate math reference.
