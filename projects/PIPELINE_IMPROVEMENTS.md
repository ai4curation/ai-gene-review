# Pipeline Improvements: Findings and Recommendations

**Date:** 2026-04-24
**Tracking issue:** TBD (will be created from this doc)
**Status:** Analysis complete, no code changes yet

---

## 1. Review Skill Workflow

### Current Flow

```
fetch-gene → deep-research → [fetch-fitness] → [pub-cache] → annotation-reviewer
    → core-function-synthesizer → [reference-findings-summarizer] → [pathway-inference-agent]
```

### Critical Path

Deep research blocks annotation review, which blocks core function synthesis. This chain is inherent (each step needs previous output). Total: 10-20 min per gene.

### Parallelization Opportunities

Publication caching can run alongside deep research (only needs GOA file). Reference findings summarizer and core function synthesis can run in parallel after annotation review. Bioinformatics analysis can run anytime after fetch-gene.

### Failure Modes

| Failure | Impact | Current Recovery |
|---------|--------|-----------------|
| Deep research timeout | Blocks pipeline | Manual retry with different provider |
| fetch-gene fails | Nothing to review | Manual fix |
| All annotations UNDECIDED | Core synthesis empty | Usually means publications missing |
| Publication stubs | Weak evidence | `refresh-publications` can recover ~2100 articles |

**Gap:** No automatic fallback when deep research times out. Should try perplexity-lite automatically.

---

## 2. Validation Pipeline

### Key Finding: Bespoke Python is the Problem, Not LinkML

The per-file performance issue is **not upstream**. LinkML's `linkml-validate` CLI already supports:
- Config-based validation with `--config` option
- Plugins instantiated once and reused across files
- Batch validation via `data_sources` in config

Our `validator.py` re-creates `LinkMLValidator`, `DynamicEnumPlugin`, and `BindingValidationPlugin` per-file in `validate_multiple_files()`. For ~1200 files this means 1200x schema loads and plugin initializations.

### Dismech Already Does This Right

Dismech uses the standard toolchain with no custom Python validator loop:
- `linkml-validate` for schema validation
- `linkml-term-validator` with `conf/oak_config.yaml` for ontology term checks
- `linkml-reference-validator` with `conf/reference_validator_config.yaml` for quote verification
- Wrapper scripts (`scripts/run_reference_validator.sh`, `scripts/run_term_validator.sh`) for network resilience

### Recommendation: Migrate to Config-Based Validation

Replace the bespoke Python validator with:

1. A `conf/validation_config.yaml` for standard LinkML validation (schema + plugins)
2. A `conf/oak_config.yaml` for ontology adapters (dismech already has a good example with 15+ ontologies)
3. A `conf/reference_validator_config.yaml` for publication quote checking
4. Wrapper scripts for network resilience in CI
5. Keep only the domain-specific `check_best_practices_rules()` as custom Python — this covers GOA consistency, core function checks, annotation action validation, etc. that are genuinely ai-gene-review-specific

This eliminates the per-file re-instantiation problem entirely and reduces maintenance burden.

### CI Cache/Enum Problem

`cache/enums/` files are runtime-generated, not committed to git, and not cached in CI. First CI run triggers slow OAK adapter builds. Dismech avoids this by using pre-built SQLite adapters specified in `oak_config.yaml`.

---

## 3. GitHub Actions Automation (Lessons from Dismech)

Dismech has several workflows we should adopt or adapt:

### Workflows to Port

| Dismech Workflow | Purpose | Priority for aigr |
|-----------------|---------|-------------------|
| `curation-scanner.yml` | Scans unassigned issues every 4h, ranks by priority/staleness, picks ONE item | P1 — would automate review queue |
| `weekly-compliance.yaml` | Picks 5 lowest-scoring files, improves them, creates per-file PRs | P1 — graduated quality improvement |
| `post-review-agent.yml` | Scans PRs for reviewer comments, creates suggested changes or follow-up issues | P2 — reduces boss steering overhead |
| `claude-code-review.yml` | Structured PR review with severity levels, auto-approve/request-changes | Already have; compare quality |
| `generate-pages.yaml` | Auto-closes stale regen PRs, auto-merges with squash | P2 — our version lacks staleness cleanup |

### Patterns to Adopt

1. **Wrapper scripts for validators** — network resilience, warning-as-fail behavior
2. **PreToolUse hooks** — dismech validates disorder YAML before edits are applied (`.claude/hooks/validate_disorder_hook.py`)
3. **Model selection in workflow inputs** — allow Haiku/Sonnet/Opus choice per run
4. **`ai-controllers.json` allowlist** — for agent dispatch authorization
5. **Graduated compliance** — fix worst files first, not all at once
6. **Intelligent candidate ranking** — priority labels, thumbs-up reactions, staleness

---

## 4. Schema and Data Quality

### Quality by Organism

| Organism | Entries | Warning Rate | Key Issues |
|----------|---------|-------------|------------|
| human | 893 | 70% | Best coverage, moderate warnings |
| mouse | 209 | 81% | Higher warning rate, less complete |
| yeast | 217 | 71% | Similar to human |
| DROME | 84 | 93% | Highest warning rate, needs attention |
| ARATH | 122 | 75% | Moderate |
| pombe | 40 | 55% | Most mature reviews |
| worm | 0 | — | No validation entries |

### Top Validation Warnings (Human, n=624)

1. **`supporting_text_substring_not_found` (150)** — Quotes don't match cached publication text
2. **`low_annotations_supporting_text_coverage` (141)** — 40-100% of annotations lack supporting text
3. **`missing_aliases` (120)** — Gene aliases not captured
4. **`no_deep_research_results` (80)** — Annotations don't reference deep research files
5. **`pending_annotations` (75)** — Unresolved PENDING actions
6. **`missing_core_functions` (67)** — Core function synthesis not run
7. **`todo_placeholder` (67)** — Descriptions contain "TODO"
8. **`inconsistent_review_actions` (32)** — Same GO term, different actions by evidence type

### Key Observation

Supporting text validation is the single biggest quality issue, compounded by 75% publication stub rate.

---

## 5. Publication Caching System

- **14,841 PMID-keyed files**, 50 DOI-keyed files
- **75% are stubs** (abstract only), 25% have full text
- Three-tier retrieval: XML (69.5%) → HTML (30.5%) → PDF (0.1%)
- DOI files use incompatible schema (`reference_id`, `content_type`) vs PMID files — effectively invisible to pipeline
- ~2,100 articles with PMC IDs are recoverable via `refresh-publications`
- PMC override system has only 2 entries despite common NCBI linkage errors

---

## 6. Deep Research Providers

| Provider | Typical Time | Citations | Reliability |
|----------|-------------|-----------|-------------|
| Perplexity (sonar-deep-research) | ~2 min | 38 avg | Good |
| Perplexity-lite (sonar-pro) | ~1 min | fewer | Good |
| Falcon (Edison) | ~9 min | 30 avg | Good |
| OpenAI (Deep Research) | ~5-10 min | thorough | Moderate |
| Cyberian | variable | unknown | Poor for large genes |

- Only ~40% of human genes have any deep research
- High-priority genes (BRCA1, BRCA2, EGFR) lack deep research
- Cyberian fails for large genes (VCP too big for 600s timeout)
- No automatic provider fallback

---

## 7. Boss/TP Orchestration

- Prompt delivery can fail silently; verification (`tp peek`) is manual
- Worktrees from failed sessions accumulate with no periodic cleanup
- PR follow-through (poll-review-fix-push cycle) is manual and repetitive
- Dismech's `post-review-agent.yml` pattern would reduce steering overhead

---

## Prioritized Issue Breakdown

### P0 — Validation Overhaul

**Replace bespoke Python validator with standard LinkML toolchain + config files.**
- Create `conf/oak_config.yaml` (model after dismech)
- Create `conf/reference_validator_config.yaml`
- Use `linkml-validate`, `linkml-term-validator`, `linkml-reference-validator` CLIs
- Add wrapper scripts for network resilience
- Keep only `check_best_practices_rules()` as custom Python
- Add `just warm-cache` to CI

### P1 — GitHub Actions Automation

Port from dismech:
- **Weekly compliance workflow** — graduated quality improvement
- **Curation scanner** — automated review queue management
- **PreToolUse validation hook** — prevent invalid YAML edits
- **Model selection inputs** in workflow dispatch

### P1 — Review Workflow Improvements

- Parallelize pub-cache with deep-research in `/review`
- Auto-fallback to perplexity-lite on deep research timeout
- Add `just deep-research-status` showing coverage gaps
- Add `just quality-report` dashboard by organism

### P2 — Publication System

- Unify DOI/PMID keying
- Periodic `refresh-publications` for active review genes
- Log refresh failures for override review

### P2 — Boss/TP Improvements

- Port `post-review-agent.yml` pattern for automated PR follow-through
- Add `just clean-worktrees` for orphaned worktree cleanup
- Scheduled worktree cleanup (>7 days)

### P3 — Deep Research

- Adaptive timeout based on gene complexity
- Chunked research queries for large genes
