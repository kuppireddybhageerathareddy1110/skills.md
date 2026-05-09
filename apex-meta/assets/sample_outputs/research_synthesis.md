# Sample Output: Research Synthesis

## Orient

The papers agree on the value of retrieval augmentation but differ in evaluation setup. Treat implementation guidance as conditional, not universal.

## Plan

1. Extract each paper's contribution.
2. Compare datasets, baselines, and metrics.
3. Identify patterns that repeat across evidence.
4. Convert patterns into implementation steps.
5. Mark uncertainty.

## Execute

Implement retrieval quality checks before model tuning. Improve chunking, metadata filters, and answer citation first; tune generation only after retrieval recall is acceptable.

## Verify

- Claims map to cited paper findings.
- Assumptions are stated.
- Implementation steps are testable.
- Missing evidence is visible.
