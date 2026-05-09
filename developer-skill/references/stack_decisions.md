# Stack Decisions

Use this guide when choosing defaults for full-stack projects.

## tRPC vs REST

Choose **tRPC** when:
- Frontend and backend live in the same TypeScript repo.
- Main consumer is the first-party web app.
- Type safety and refactor speed matter more than public API stability.
- You do not need third-party SDKs immediately.

Choose **REST** when:
- External clients or mobile apps consume the API.
- Endpoint contracts need versioning and documentation.
- Integrations need simple HTTP semantics.
- You want OpenAPI generation.

Recommended default: tRPC for internal product surfaces, REST for public integrations.

## Prisma vs Drizzle

Choose **Prisma** when:
- Team wants fast schema modeling and migrations.
- Data access is mostly CRUD.
- Developer experience matters more than SQL control.
- You benefit from Prisma Studio and mature docs.

Choose **Drizzle** when:
- You want SQL-like query control.
- Bundle size and edge compatibility matter.
- Team is comfortable with explicit relational modeling.
- You need tighter control over generated SQL.

Recommended default: Prisma for product MVPs, Drizzle for SQL-heavy or edge-focused apps.

## Server Actions vs API Routes

Choose **Server Actions** when:
- Mutations are called directly from React forms/components.
- The action is first-party and UI-bound.
- You want less client boilerplate.

Choose **API Routes / Route Handlers** when:
- Endpoint is called by external systems.
- Webhooks are involved.
- You need explicit request/response control.

## Supabase vs Plain Postgres

Choose **Supabase** when:
- You need hosted Postgres plus auth, storage, realtime, or dashboard tooling.
- Speed matters more than deep infrastructure control.

Choose **plain Postgres** when:
- Infrastructure is already managed elsewhere.
- You need strict control over extensions, networking, and backups.

## NextAuth vs Clerk vs Custom Auth

Choose **NextAuth** when:
- You want open-source auth in a Next.js app.
- Existing OAuth/email providers are enough.
- You can own session and database configuration.

Choose **Clerk** when:
- You need polished hosted auth, orgs, MFA, and user management quickly.

Avoid custom auth unless requirements force it.

## Decision Template

```text
Use [choice] because [primary constraint].
Avoid [alternative] because [tradeoff].
Revisit when [future trigger].
```
