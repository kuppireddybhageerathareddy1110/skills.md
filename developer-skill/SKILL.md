---
name: developer-skill
description: Developer-focused AI response rules with structured command modes
version: "2024.1"
updated: "2026-04-19"
author: "you"
tags: ["ai", "developer", "nextjs", "typescript", "fullstack"]
---

# skill.md

## Command Reference

### `question`
Answer only • No code • Direct solution

### `implementation guide`
Steps • Architecture • Decisions • No full code

### `folder structure`
Tree view • File descriptions • No code

### `correct code`
Fix broken part only • Highlight changes only

### `fullprojectwithcode`
Complete app • All files • Production-ready

### `information`
Theory • Concepts • Best practices • No code

### `design`
UI/UX specs • Colors • Layout • Mockups

### `just frontend`
Client only • Components • State • Styles

### `just backend`
Server only • API • Database • Logic

### `just this file`
Single file only  
Format: `just this file: filename.tsx`

### `just this part of code`
Specific function/section only  
Format: `just this part: function name`

---

## Tech Stack (Optimized)

### Frontend
- Next.js 15 (App Router, React 19, RSC)
- TypeScript 5
- Tailwind CSS + shadcn/ui
- Framer Motion / GSAP

### Backend
- Next.js Server Actions
- tRPC / Hono
- Prisma ORM / Drizzle ORM
- PostgreSQL / Supabase
- NextAuth.js v5 / Lucia Auth

### Runtime & Tooling
- Bun runtime
- Turbopack
- Edge / Server Components

---

## Branding Theme

```css
--bg-dark: #0A0E27;
--bg-card: #151932;
--accent-blue: #3B82F6;
--accent-green: #10B981;
--text: #E4E4E7;
--muted: #A1A1AA;
--border: rgba(59, 130, 246, 0.2);

--font-sans: 'Inter', system-ui;
--font-mono: 'JetBrains Mono', monospace;
```

### UI Style
- Glassmorphism cards
- Gradient borders
- Glow hover effects
- Smooth transitions
- Micro-interactions
- Dark mode first

### Component Features
- Skeleton loaders
- Toast notifications
- Command palette (⌘K)
- Responsive tables
- Charts

---

## Usage

```bash
"fullprojectwithcode: SaaS dashboard with auth"
"just backend: stripe webhook handler"
"folder structure: NextJS 15 monorepo"
"design: landing page for AI startup"
"correct code: [paste error]"
"just this file: middleware.ts"
```

---

## Quick Patterns

### Auth
NextAuth v5 → Prisma → PostgreSQL

### Data Fetching
Server Component → tRPC → Prisma

### Realtime
Pusher / Ably / Supabase Realtime

### Payments
Stripe → Webhooks → Database

### File Upload
UploadThing / Cloudinary / S3

---

## Component Libraries

- shadcn/ui (default)
- Radix UI
- Headless UI
- Aceternity UI
- Magic UI

---

## Response Modes Matrix

| Command | Code | Explanation | Output |
|--------|------|------------|--------|
| question | ❌ | ✅ | Answer |
| information | ❌ | ✅ | Explanation |
| implementation guide | Partial | ✅ | Structured |
| folder structure | ❌ | Minimal | Tree |
| design | Mockups | ✅ | UI Spec |
| correct code | ✅ | Minimal | Patch |
| just frontend | ✅ | ✅ | Frontend |
| just backend | ✅ | ✅ | Backend |
| fullprojectwithcode | ✅ | ✅ | Complete |

---

## AI/ML Stack (Optional)

- LLM: OpenAI / Claude
- Vector DB: Pinecone / pgvector
- Framework: LangChain / Vercel AI SDK
- Streaming: AI SDK RSC

---

## Rules

- Follow command strictly
- Do not mix response modes
- Optimize for token efficiency
- Prefer production-ready patterns
- Avoid unnecessary explanations in code modes

---

## Invocation Pattern

Use skill.md guidelines.
<command>: <task>

Example:
Use skill.md guidelines.
fullprojectwithcode: AI SaaS app with auth and billing

---

Focus: Production quality + token efficiency
