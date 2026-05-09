# Compression Metrics

Use this table to measure token/word reduction across intensity levels.

| Sample | Original Words | Lite Words | Full Words | Ultra Words | Notes |
| --- | ---: | ---: | ---: | ---: | --- |
| Auth middleware bug | 24 | 17 | 10 | 7 | Preserve exact technical cause. |
| DB pooling explanation | 22 | 16 | 11 | 8 | Keep DB/connection terms. |
| React rerender issue | 28 | 20 | 13 | 8 | Keep hook names unchanged. |
| Cache invalidation | 31 | 23 | 15 | 10 | Keep event trigger clear. |

## Quality Checks

- Meaning unchanged.
- Critical nouns retained.
- Error strings and code unchanged.
- Warnings remain explicit.
- Ultra mode still readable.

## Target Reductions

- Lite: 15-30%
- Full: 40-65%
- Ultra: 60-80%
- Wenyan modes: measure by characters, not English word count.
