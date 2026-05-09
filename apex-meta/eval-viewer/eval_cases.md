# Apex Eval Cases

## Rubric

Pass requires:
- Direct orientation in 1-2 sentences.
- Clear plan before execution.
- Output matches requested mode.
- Verification checklist or concrete self-check.
- No filler or repeated sections.

## Case 1: Production Bug

Prompt: "Fix login timeout after token refresh in a Next.js app."

Expected structure: Orient -> Plan -> Files/patch -> Tests -> Verify.

Pass/fail: Pass if auth risk is surfaced and regression testing is included.

## Case 2: Architecture Choice

Prompt: "Should we use tRPC or REST for an internal analytics dashboard?"

Expected structure: Recommendation -> Tradeoff table -> Decision rule -> Revisit trigger.

Pass/fail: Pass if first-party and external consumers are separated.

## Case 3: Research Summary

Prompt: "Summarize these three ML papers into an implementation plan."

Expected structure: Evidence table -> Synthesis -> Implementation checklist -> Uncertainty.

Pass/fail: Pass if claims are grounded and uncertain items are labeled.

## Case 4: Full Project

Prompt: "Build a SaaS support ticket dashboard with auth and billing."

Expected structure: Scope -> Stack -> Data model -> Build plan -> Verification.

Pass/fail: Pass if thin vertical slice is prioritized.

## Case 5: Code Review

Prompt: "Review this PR touching Stripe webhooks."

Expected structure: Findings first -> Questions -> Test gaps -> Summary.

Pass/fail: Pass if idempotency and signature verification are checked.
