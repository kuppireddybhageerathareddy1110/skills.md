# Reasoning Patterns

Use these patterns when applying the Apex orient -> plan -> execute -> verify loop.

## Pattern 1: Production Bug

**Task:** Fix intermittent login failures after a session refresh.

**Orient:** User-facing auth failure. Risk: stale token handling may affect all protected routes.

**Plan:**
1. Reproduce failure path.
2. Inspect middleware and session refresh code.
3. Patch expiry comparison and refresh retry logic.
4. Add regression test.
5. Verify protected and public routes.

**Execute:** Keep edits scoped to auth middleware, session utilities, and tests.

**Verify:** Confirm expired, near-expired, and valid sessions behave correctly.

## Pattern 2: Architecture Decision

**Task:** Choose API style for a dashboard with internal UI and third-party integrations.

**Orient:** Internal UI wants type safety; external clients need stable contracts.

**Plan:**
1. Separate internal and external consumers.
2. Compare tRPC, REST, and GraphQL.
3. Pick default and exception path.
4. Define migration and testing approach.

**Execute:** Recommend tRPC for internal app, REST for external API, shared schema validation.

**Verify:** Decision covers auth, versioning, observability, SDK generation, and future teams.

## Pattern 3: Research Synthesis

**Task:** Summarize three papers into implementation guidance.

**Orient:** Need accurate claims, not generic summary.

**Plan:**
1. Extract core contribution from each paper.
2. Compare assumptions and evaluation settings.
3. Identify repeatable implementation patterns.
4. Mark uncertainty and missing evidence.

**Execute:** Produce synthesis table, then implementation checklist.

**Verify:** Every recommendation maps to evidence or is clearly labeled inference.

## Pattern 4: Full Product Build

**Task:** Build an AI-powered CRM MVP.

**Orient:** Large scope. Need thin vertical slice before broad features.

**Plan:**
1. Define user roles and core workflow.
2. Pick stack and data model.
3. Build auth, contacts, notes, AI summary, and audit trail.
4. Add tests for critical flows.
5. Verify browser and API behavior.

**Execute:** Prioritize end-to-end usable workflow over decorative surface area.

**Verify:** User can log in, add contact, record note, generate summary, and revisit history.

## Pattern 5: Code Review

**Task:** Review a PR that touches billing and webhooks.

**Orient:** High-risk area. Look for money movement, idempotency, and replay issues first.

**Plan:**
1. Inspect changed files and tests.
2. Trace webhook event lifecycle.
3. Check idempotency, signature verification, and state transitions.
4. Report findings by severity.

**Execute:** Lead with concrete bugs and line references.

**Verify:** Findings are reproducible, scoped, and not stylistic preferences.
