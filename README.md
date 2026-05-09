# Skills

This repository contains a curated set of Codex/Claude-style skills. Each skill is available in two forms:

- Editable source folders, such as `ai/SKILL.md` and `pro-ppt/SKILL.md`
- Packaged `.skill` archives, such as `ai.skill` and `pro-ppt.skill`

Use the folder form when editing, reviewing, or extending a skill. Use the packaged archive form when importing a skill into a compatible agent environment.

## Repository Layout

Each skill folder follows the same structure:

```text
skill-name/
  SKILL.md
  templates/
  references/
  scripts/
  assets/
  eval-viewer/
```

The support folders are intentionally present for every skill:

- `templates/`: reusable prompts, document layouts, project skeletons, or output formats.
- `references/`: background material, examples, checklists, and domain notes.
- `scripts/`: helper scripts for generation, validation, packaging, or evaluation.
- `assets/`: images, icons, sample files, datasets, and other binary or static assets.
- `eval-viewer/`: evaluation notes, viewer files, dashboards, or artifacts used to inspect skill outputs.

## Included Skills

| Skill | Purpose |
| --- | --- |
| `ai` | AI/ML engineering reference for model building, training, inference, explainability, and ML project work. |
| `ai-architect-workflow` | End-to-end AI architecture workflow covering strategy, system design, implementation planning, and review. |
| `apex-meta` | Enterprise meta-framework for structured reasoning, delivery quality, and multi-domain execution. |
| `api-contract-generator` | API contract generation skill for clear endpoint, schema, and integration specifications. |
| `caveman` | Ultra-compressed communication mode for concise, token-efficient answers. |
| `code-review-architect` | Code review and architecture audit skill focused on risks, regressions, and production readiness. |
| `data-analysis-eda` | Exploratory data analysis workflow for profiling, cleaning, visualization, and insight generation. |
| `data-scientist-workflow` | Full data science project workflow from problem framing through modeling and communication. |
| `developer-skill` | Developer response rules for implementation, debugging, testing, and software delivery. |
| `financial-analysis` | Financial analysis workflow for statements, metrics, valuation, risk, and investment-style review. |
| `ml-pipeline-validator` | ML pipeline validation skill for data, training, evaluation, reproducibility, and deployment checks. |
| `omega` | Unified multi-domain meta-skill that routes complex requests across architecture, AI, research, finance, docs, and delivery modules. |
| `pro-ppt` | Professional PowerPoint generation skill for business decks, pitch decks, reports, and presentations. |
| `quantum-ai-engineer-workflow` | Quantum AI and ML engineering workflow covering hybrid systems, research, and implementation planning. |
| `research` | Research-oriented skill for gathering, synthesizing, and presenting information. |

## Editing Workflow

1. Update the relevant `SKILL.md`.
2. Add supporting material to the matching `templates`, `references`, `scripts`, `assets`, or `eval-viewer` folder.
3. Repackage the skill archive if your runtime imports `.skill` files.
4. Commit both the editable source and packaged archive when they should remain in sync.

## License

This repository is licensed under the MIT License. See `LICENSE.txt`.
