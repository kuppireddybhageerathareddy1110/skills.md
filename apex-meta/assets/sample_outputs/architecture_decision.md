# Sample Output: Architecture Decision

## Orient

The dashboard is first-party, but exports and partner integrations need stable API contracts. One API style does not need to serve both surfaces.

## Plan

1. Split consumers into internal UI and external integrations.
2. Compare type safety, versioning, docs, and client generation.
3. Pick default per consumer.
4. Define revisit trigger.

## Execute

Use tRPC for internal dashboard calls and REST for partner-facing endpoints. Share Zod schemas where possible so validation and types stay aligned.

## Verify

- Internal app gets end-to-end TypeScript safety.
- External consumers get stable URLs and documented contracts.
- Versioning is isolated to REST API.
- Shared validation avoids schema drift.
