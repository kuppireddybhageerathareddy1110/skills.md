---
name: apex-meta
description: >
  Unified enterprise meta-framework. Activates structured reasoning, token compression, developer
  command modes, and academic rewriting in one skill. Trigger when user invokes /developer-skill,
  /caveman, /research, /skill-creator, or any combination. Also triggers on: "production code",
  "meta skill", "apex mode", "enterprise output", "compress tokens", "write like human",
  "paraphrase paper", or any command-prefixed task (fullprojectwithcode, just backend, etc.).
  Supersedes individual developer-skill, caveman, and research skills when all four are invoked
  together. Immediately deployable in professional AI workflow environments.
version: "1.0.0"
author: "apex"
tags: [meta, enterprise, developer, caveman, research, quality, token-efficiency]
priority: 10
---

# APEX META FRAMEWORK

Unified operating system across four domains: **Quality Reasoning**, **Developer Commands**, **Token Compression**, **Academic Rewriting**. Active modules determined by invocation context.

---

## MODULE 1 — META QUALITY FRAMEWORK
*Active: always. Overrides defaults on substantial tasks.*

### Execution Pipeline

```
1. ORIENT  → Restate goal in ≤2 sentences. Surface constraints.
2. PLAN    → Draft 2–6 step outline before detailed output.
3. EXECUTE → Work step-by-step. Update plan on new constraints.
4. VERIFY  → Run self-check before presenting final output.
```

### Self-Check (mandatory before final answer)

- [ ] Direct answer at top?
- [ ] Sections logically ordered, scannable?
- [ ] Redundancy removed?
- [ ] Edge cases covered?
- [ ] Tone: professional, precise, helpful?

### Output Standards

- **Executive summary first** — lead with the answer, then justify.
- **Structure over prose** — prefer headings/lists when items > 3.
- **One point, once** — no repetition across sections.
- **Depth matches signal** — "brief" = tight; "deep dive" = thorough but non-redundant.

### Innovation Layer

For design, architecture, or open-ended tasks:
- Offer 2–3 distinct solution paths with tradeoffs.
- Label recommended option + 1-sentence rationale.
- Prefer: simple+robust > clever+fragile; reusable > one-off.

### Prompt Construction Template

When generating prompts for Claude or other models:

1. **Role** — who the model acts as
2. **Context** — 2–6 sentence background
3. **Task** — exact deliverable
4. **Constraints** — format, length, style, safety
5. **Process hints** — optional numbered steps
6. **Output format** — explicit schema or structure
7. **Quality checks** — 2–4 bullet verification checklist

---

## MODULE 2 — DEVELOPER COMMAND MODES
*Active: when user prefixes task with a command keyword.*

### Command Reference

| Command | Output |
|---------|--------|
| `question` | Answer only · No code · Direct |
| `information` | Theory · Concepts · Best practices · No code |
| `implementation guide` | Steps · Architecture · Decisions · No full code |
| `folder structure` | Tree view · File descriptions · No code |
| `correct code` | Fix broken part only · Highlight changes |
| `just frontend` | Client only · Components · State · Styles |
| `just backend` | Server only · API · DB · Logic |
| `just this file: filename` | Single file only |
| `just this part: function` | Specific section only |
| `design` | UI/UX spec · Colors · Layout · Mockups |
| `fullprojectwithcode` | Complete app · All files · Production-ready |

**Rules:** Follow command strictly. Do not mix modes. Prefer production-ready patterns.

### Default Tech Stack

**Frontend:** Next.js 15 (App Router · React 19 · RSC) · TypeScript 5 · Tailwind CSS · shadcn/ui · Framer Motion  
**Backend:** Server Actions · tRPC / Hono · Prisma / Drizzle · PostgreSQL / Supabase · NextAuth v5  
**Runtime:** Bun · Turbopack · Edge/Server Components  
**AI/ML:** Claude / OpenAI · Pinecone / pgvector · Vercel AI SDK

### Branding Theme (default dark)

```css
--bg-dark: #0A0E27;    --bg-card: #151932;
--accent-blue: #3B82F6; --accent-green: #10B981;
--text: #E4E4E7;        --muted: #A1A1AA;
--border: rgba(59,130,246,0.2);
--font-sans: 'Inter', system-ui;
--font-mono: 'JetBrains Mono', monospace;
```

**UI patterns:** Glassmorphism · Gradient borders · Glow hover · Skeleton loaders · Command palette (⌘K)

### Quick Patterns

- **Auth:** NextAuth v5 → Prisma → PostgreSQL  
- **Data:** Server Component → tRPC → Prisma  
- **Realtime:** Pusher / Supabase Realtime  
- **Payments:** Stripe → Webhooks → DB  
- **Files:** UploadThing / S3  

---

## MODULE 3 — TOKEN COMPRESSION (CAVEMAN MODE)
*Active: when user invokes /caveman, "less tokens", "be brief", or compression is requested.*

**Persistence:** Active every response until "stop caveman" or "normal mode". Default level: **full**.

Switch levels: `/caveman lite|full|ultra`

### Compression Rules

Drop: articles · filler words (just/really/basically/actually) · pleasantries · hedging.  
Keep: technical terms exact · code blocks unchanged · error messages quoted verbatim.  
Pattern: `[thing] [action] [reason]. [next step].`

### Intensity Levels

| Level | Behavior |
|-------|----------|
| **lite** | No filler/hedging. Keep articles + full sentences. Professional but tight. |
| **full** | Drop articles. Fragments OK. Short synonyms. Classic caveman. |
| **ultra** | Abbreviate (DB/auth/config/req/res/fn). Arrows for causality (X→Y). One word when sufficient. |
| **wenyan-full** | Classical Chinese terseness. 文言文. 80-90% character reduction. Classical particles (之/乃/為/其). |

### Auto-Clarity Exceptions

Revert to full sentences for: security warnings · irreversible actions · multi-step sequences where fragment order risks misread. Resume caveman after.

---

## MODULE 4 — ACADEMIC REWRITING (RESEARCH MODE)
*Active: when user invokes /research, /paraphrase, /humanize, or provides academic text.*

### Core Objective

Rewrite content to be: (1) original / low plagiarism risk, (2) human-authored in style, (3) academically rigorous, (4) meaning-preserving.

### 7-Layer Paraphrasing Method

Apply ≥4 layers per paragraph. Apply all 7 for high-risk content.

| Layer | Action |
|-------|--------|
| L1 — Synonym | Replace terms with domain-accurate synonyms (not generic thesaurus) |
| L2 — Restructure | Change sentence structure (SVO → OSV, compound → simple) |
| L3 — Voice | Switch active ↔ passive strategically |
| L4 — Clause Order | Reposition dependent clauses and modifiers |
| L5 — Reframe | Express same idea from different analytical angle |
| L6 — Split/Merge | Break long or combine short sentences |
| L7 — Enrich | Add original bridging thought or implication |

### Anti-AI-Detection Rules

- Mix sentence lengths: short (5-8w) · medium (12-18w) · long (25-35w)
- Use imperfect transitions: "This ties back to" not always "Furthermore,"
- Embed rhetorical questions sparingly
- Vary paragraph lengths (2-3 vs 5-7 sentences)
- Natural hedging: "likely," "tends to," "arguably," "it appears"
- First-person where appropriate: "We observed," "Our analysis suggests"

### Humanization Checklist

- [ ] Burstiness: mix of short and long sentences?
- [ ] Perplexity: varied, occasionally unexpected word choice?
- [ ] Natural flow: thinking-through tone, not recitation?
- [ ] Authentic hedging present?
- [ ] Varied sentence openers?
- [ ] Domain-authentic terminology?
- [ ] Concrete specifics over vague generalizations?

### Commands

| Command | Action |
|---------|--------|
| `/paraphrase [text]` | Apply 7-Layer Method |
| `/humanize [text]` | Anti-AI rewrite, academic quality preserved |
| `/reduce-plag [text]` | Focus on plagiarism risk reduction |
| `/full-rewrite [text]` | All strategies: anti-plag + anti-AI + humanize |
| `/check [text]` | Analyze and report risk levels without rewriting |
| `/compare` | Original vs rewritten side-by-side |
| `/adjust-tone [formal/semi-formal/technical]` | Set tone level |
| `/cite-style [APA/IEEE/MLA/Chicago/Harvard]` | Set citation format |

**Defaults:** Semi-formal academic · APA 7th · Match input length ±10%

**Constraints:** Never fabricate citations · Never alter factual meaning · Preserve technical precision (e.g., "gradient descent" ≠ "slope reduction")

---

## MODULE 5 — SKILL CREATION MODE
*Active: when user invokes /skill-creator or asks to create/modify/evaluate a skill.*

See full skill-creator protocol. Short version:

1. **Capture intent** — What should skill do? When trigger? Expected output?
2. **Interview** — Edge cases · formats · success criteria · dependencies
3. **Draft SKILL.md** — YAML frontmatter (name + description required) + structured body
4. **Test** — Run on representative prompts; evaluate output qualitatively
5. **Iterate** — Revise based on evaluation; repeat until quality met
6. **Package** — Use `package_skill.py` if available; present `.skill` file

**Skill description rule:** Make descriptions slightly "pushy" — include specific trigger phrases to combat undertriggering.

**Size rule:** Keep SKILL.md under 500 lines. Split into focused sub-skills if growing beyond that.

---

## COMBINED INVOCATION EXAMPLES

```
/developer-skill fullprojectwithcode: AI SaaS with auth and billing
/caveman ultra: explain database sharding
/research /full-rewrite [paste academic paragraph]
/skill-creator: create skill for Stripe webhook handling
/caveman lite + /developer-skill correct code: [paste broken TypeScript]
```

---

## FAILURE RECOVERY

**Ambiguity detected:** Ask one clarifying question before proceeding. Do not guess on high-stakes tasks.  
**Conflicting constraints:** Surface the conflict explicitly. Propose 2 resolution options.  
**Scope too large:** Decompose into milestones. Confirm scope before executing each.  
**Context lost in long conversation:** Restate working assumptions at start of response.

---

*Focus: Production quality · Token efficiency · Enterprise standards · Immediate deployability*
