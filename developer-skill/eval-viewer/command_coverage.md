# Command Coverage Matrix

| Command | UI Task | Backend Task | Full-Stack Task |
| --- | --- | --- | --- |
| `question` | Explains component behavior without code. | Explains API behavior without code. | Answers architecture question directly. |
| `information` | Gives design/system concepts. | Gives database/auth concepts. | Gives best practices and tradeoffs. |
| `implementation guide` | Steps for component build. | Steps for service/API build. | Architecture and sequence, no full code. |
| `folder structure` | Component tree and responsibilities. | Route/service/model tree. | Monorepo/app tree. |
| `correct code` | Fixes broken component section. | Fixes handler/query bug. | Fixes integration bug with minimal patch. |
| `just frontend` | Components, state, styles only. | Rejects backend expansion. | Client integration stubs only. |
| `just backend` | Rejects UI expansion. | API, DB, auth logic only. | Server implementation only. |
| `just this file` | Edits one TSX file. | Edits one API/model file. | Edits named file only. |
| `just this part` | Edits named component/function. | Edits named handler/query. | Edits named section only. |
| `design` | UI spec, layout, colors. | API ergonomics if requested. | Product UX and interaction model. |
| `fullprojectwithcode` | Complete frontend files. | Complete backend files. | Complete runnable project. |

## Pass Criteria

- Command mode is followed strictly.
- No unrelated scope expansion.
- Production risks are named for full-stack work.
- Verification command or manual check is included when code changes are made.
