---
name: pro-ppt
description: >
  Professional PowerPoint generation skill. Use this whenever the user asks to create, build,
  generate, or make a presentation, slide deck, pitch deck, or .pptx file. Also triggers for:
  "make me slides", "create a deck", "build a presentation about X", "generate a ppt",
  "I need slides for [topic]", "can you make a powerpoint", or any request that would
  result in a .pptx output. Applies full design system: branded color palettes, bold layouts,
  icon support, charts, and QA. If the user gives a topic, just build it — don't ask
  unnecessary questions. Default to a professional business style unless told otherwise.
---

# Pro PPT Skill

Generate professional, visually compelling PowerPoint presentations using PptxGenJS.
No bland white slides. Every output uses intentional design, a coherent palette, and varied layouts.

---

## Quick Command Reference

| Command | Action |
|---------|--------|
| `/ppt [topic]` | Build full deck on topic (default: 8–10 slides) |
| `/ppt [topic] --slides N` | Specify slide count |
| `/ppt [topic] --style [dark/light/corporate/bold]` | Force a style |
| `/ppt [topic] --theme [palette name]` | Use specific palette from table below |
| `/ppt [topic] --data` | Include charts/data slides |
| `/outline [topic]` | Show slide outline before building |

If no command used, infer intent and build directly.

---

## Workflow

### Step 1 — Plan

Decide structure before writing code:
- Topic → appropriate slide count (5–7 for short, 8–12 for full deck, 15+ for detailed)
- Select palette from table below (match topic mood)
- Choose layout variety: title, section, two-column, stat callout, chart, closing

### Step 2 — Setup

```bash
# Install once per session if not present
npm install -g pptxgenjs react react-dom react-icons sharp 2>/dev/null || true
```

### Step 3 — Build

Write a single Node.js script. Use PptxGenJS. Follow all rules below.
Save output to `/home/claude/output.pptx`, then copy to `/mnt/user-data/outputs/`.

```javascript
const pptxgen = require("pptxgenjs");
const pres = new pptxgen();
pres.layout = "LAYOUT_16x9";  // 10" × 5.625"
```

### Step 4 — QA

```bash
# Run script
node presentation.js

# Extract text to verify content
python3 -c "
from pptx import Presentation
prs = Presentation('/home/claude/output.pptx')
for i, slide in enumerate(prs.slides, 1):
    print(f'=== Slide {i} ===')
    for shape in slide.shapes:
        if hasattr(shape, 'text') and shape.text.strip():
            print(shape.text.strip())
" 2>/dev/null || true
```

Fix any content issues. Then copy to outputs:
```bash
cp /home/claude/output.pptx /mnt/user-data/outputs/presentation.pptx
```

---

## Design System

### Color Palettes

Pick based on topic. Never default to generic blue.

| Palette | Primary | Secondary | Accent | Best For |
|---------|---------|-----------|--------|----------|
| **Midnight Executive** | `1E2761` | `CADCFC` | `FFFFFF` | Finance, legal, enterprise |
| **Coral Energy** | `F96167` | `2F3C7E` | `F9E795` | Startups, marketing, product |
| **Teal Trust** | `028090` | `02C39A` | `F0F4F8` | Health, SaaS, nonprofit |
| **Forest Depth** | `2C5F2D` | `97BC62` | `F5F5F5` | Sustainability, agriculture, ESG |
| **Warm Terracotta** | `B85042` | `E7E8D1` | `A7BEAE` | Education, culture, HR |
| **Charcoal Minimal** | `36454F` | `F2F2F2` | `212121` | Technical, consulting, B2B |
| **Berry Premium** | `6D2E46` | `A26769` | `ECE2D0` | Luxury, fashion, creative |
| **Cherry Bold** | `990011` | `FCF6F5` | `2F3C7E` | Sales, sports, high-impact |
| **Ocean Gradient** | `065A82` | `1C7293` | `E0F7FA` | Research, analytics, data |
| **Sage Calm** | `84B59F` | `69A297` | `F9F6F0` | Wellness, lifestyle, coaching |

### Typography

| Element | Font | Size | Style |
|---------|------|------|-------|
| Slide title | Calibri | 36–44pt | Bold |
| Section header | Calibri | 22–28pt | Bold |
| Body text | Calibri | 14–16pt | Regular |
| Stat callout | Calibri | 52–64pt | Bold |
| Caption/label | Calibri | 10–12pt | Regular, muted |

### Layout Patterns

Use variety — don't repeat the same layout twice in a row.

| Layout | Description |
|--------|-------------|
| **Title** | Full-bleed dark bg, centered title + subtitle, used for slide 1 and closing |
| **Two-column** | Text/bullets left, image/chart/icon right (or vice versa) |
| **Stat callout** | Large number (52–64pt) + label, 2–4 stats across slide |
| **Icon grid** | 3–4 icons in circles, header + short text below each |
| **Full-width statement** | Bold single sentence centered, dark bg, accent color |
| **Chart slide** | Title + chart, minimal text |
| **Section divider** | Solid accent color, section title, short description |
| **Timeline/process** | Numbered steps with connectors |
| **Closing** | Mirror of title slide, CTA or summary |

---

## Code Rules (CRITICAL)

Read [pptxgenjs.md](/mnt/skills/public/pptx/pptxgenjs.md) for full API reference. Hard rules:

1. **No `#` in hex colors** — `"FF0000"` ✅ `"#FF0000"` ❌ (corrupts file)
2. **No 8-char hex for opacity** — use `opacity` property in shadow objects
3. **No unicode bullets** — use `bullet: true` only
4. **`breakLine: true`** between array text items
5. **Fresh shadow object per shape** — never reuse options objects (PptxGenJS mutates in-place)
6. **No accent lines under titles** — use whitespace, color blocks, or background instead
7. **No cream/beige backgrounds** — use white `FFFFFF` or palette colors
8. **No decorative full-width bars** — unless user explicitly requests
9. **margin: 0** on text boxes aligned to shapes/icons
10. **Every slide needs a visual** — shape, icon, chart, or image; no text-only slides

---

## Slide Structure Templates

### Title Slide
```javascript
// Dark background
slide.background = { color: PRIMARY };
// Large centered title
slide.addText(title, { x: 0.8, y: 1.8, w: 8.4, h: 1.4, fontSize: 44, bold: true, color: "FFFFFF", align: "center" });
// Subtitle
slide.addText(subtitle, { x: 0.8, y: 3.4, w: 8.4, h: 0.6, fontSize: 18, color: SECONDARY_HEX, align: "center" });
// Accent shape (bottom bar or side accent)
slide.addShape(pres.shapes.RECTANGLE, { x: 0, y: 5.2, w: 10, h: 0.42, fill: { color: ACCENT } });
```

### Stat Callout Slide (3 stats)
```javascript
const stats = [
  { value: "87%", label: "Customer Satisfaction" },
  { value: "$4.2M", label: "Revenue Growth" },
  { value: "3×", label: "Faster Deployment" }
];
stats.forEach((stat, i) => {
  const x = 0.5 + i * 3.2;
  // Card background
  slide.addShape(pres.shapes.RECTANGLE, { x, y: 1.2, w: 2.8, h: 3.0, fill: { color: "FFFFFF" }, shadow: makeShadow() });
  // Big number
  slide.addText(stat.value, { x, y: 1.5, w: 2.8, h: 1.4, fontSize: 52, bold: true, color: PRIMARY, align: "center", margin: 0 });
  // Label
  slide.addText(stat.label, { x, y: 3.1, w: 2.8, h: 0.7, fontSize: 13, color: "64748B", align: "center", margin: 0 });
});

// Always use a factory function for shadows:
const makeShadow = () => ({ type: "outer", blur: 8, offset: 3, angle: 135, color: "000000", opacity: 0.12 });
```

### Two-Column Content Slide
```javascript
// Left: text content
slide.addText(title, { x: 0.5, y: 0.4, w: 9, h: 0.7, fontSize: 28, bold: true, color: PRIMARY });
slide.addText(bullets, { x: 0.5, y: 1.3, w: 4.5, h: 3.8, fontSize: 15, color: "1E293B" });
// Right: accent shape or image placeholder
slide.addShape(pres.shapes.RECTANGLE, { x: 5.5, y: 1.0, w: 4.0, h: 4.0, fill: { color: SECONDARY } });
```

### Section Divider
```javascript
slide.background = { color: PRIMARY };
slide.addText(sectionNumber, { x: 0.5, y: 0.8, w: 9, h: 0.8, fontSize: 14, color: ACCENT, align: "center", bold: true });
slide.addText(sectionTitle, { x: 0.5, y: 1.8, w: 9, h: 1.4, fontSize: 40, bold: true, color: "FFFFFF", align: "center" });
slide.addText(sectionDesc, { x: 1.5, y: 3.4, w: 7, h: 0.8, fontSize: 16, color: SECONDARY, align: "center" });
```

---

## Icon Usage

When slides need icons (icon grid, features list):

```javascript
const React = require("react");
const ReactDOMServer = require("react-dom/server");
const sharp = require("sharp");
const { FaRocket, FaChartLine, FaUsers } = require("react-icons/fa");

async function iconToBase64(IconComponent, color = "#FFFFFF", size = 256) {
  const svg = ReactDOMServer.renderToStaticMarkup(
    React.createElement(IconComponent, { color, size: String(size) })
  );
  const buf = await sharp(Buffer.from(svg)).png().toBuffer();
  return "image/png;base64," + buf.toString("base64");
}

// Add icon circle + icon on slide:
slide.addShape(pres.shapes.OVAL, { x: 1.0, y: 1.5, w: 0.8, h: 0.8, fill: { color: ACCENT } });
const icon = await iconToBase64(FaRocket, "#FFFFFF", 256);
slide.addImage({ data: icon, x: 1.15, y: 1.65, w: 0.5, h: 0.5 });
```

---

## Slide Count Guidelines

| Presentation Type | Slides |
|-------------------|--------|
| Quick overview / intro | 5–7 |
| Standard business deck | 8–12 |
| Full pitch deck | 10–15 |
| Training / course module | 15–25 |
| Detailed report / research | 20+ |

Default: 8–10 slides unless specified.

---

## Standard Deck Structure

For a general topic deck, use this structure as base:
1. Title slide
2. Agenda / Overview
3. Context / Problem
4. Key insight or Section 1
5. Data / Evidence (chart or stats)
6. Section 2 content
7. Section 3 content
8. Summary / Key takeaways
9. Call to action / Next steps
10. Closing / Thank you

Adapt structure to fit topic. Add section dividers for longer decks.

---

## After Building

1. Run QA text extraction (see Step 4)
2. Fix any overflow or missing content
3. Copy to outputs: `cp /home/claude/output.pptx /mnt/user-data/outputs/[descriptive-name].pptx`
4. Present file to user via `present_files` tool
5. Give one-line summary of what was built (slide count, palette used, key sections)

---

## Common Mistakes to Avoid

- Repeating same layout slide after slide
- Using only title + bullet points (boring, lazy)
- Defaulting to blue when a bolder palette fits better
- Forgetting `makeShadow()` factory pattern (causes corruption on second shape)
- Writing `color: "#336699"` instead of `color: "336699"`
- Skipping QA — always extract text to verify content landed correctly
- Over-explaining to user what you're about to do — just build it
