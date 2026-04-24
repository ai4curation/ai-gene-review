# Pipeline Improvements: Findings and Recommendations

**Date:** 2026-04-24
**Branch:** chore/pipeline-improvements
**Status:** Analysis complete, no code changes

---

## 1. Review Skill Workflow

### Current Flow

The `/review` skill dispatches a sequential pipeline:

```
fetch-gene → deep-research → [fetch-fitness] → [pub-cache] → annotation-reviewer
    → core-function-synthesizer → [reference-findings-summarizer] → [pathway-inference-agent]
```

### Bottleneck: Deep Research → Annotation Review is the Critical Path

Deep research (Phase 2) **blocks** annotation review (Phase 5), which **blocks** core function synthesis (Phase 6). This is inherent — each step needs the previous step's output. The sequential chain alone takes 10-20 minutes per gene.

### Parallelization Opportunities

**Currently sequential but could be parallel:**
- Publication caching (`fetch-gene-pmids`) can run alongside deep research — it only needs the GOA file, not deep research output
- Reference findings summarizer (Phase 7) is independent of core function synthesis (Phase 6) — both can run after annotation review
- Bioinformatics analysis (Phase 8) can run anytime after fetch-gene

**Recommended parallel schedule:**
```
Phase 1: fetch-gene (sequential, fast)
Phase 2+4: deep-research + pub-cache + [bioinformatics setup] (parallel)
Phase 5: annotation-review (waits for Phase 2+4)
Phase 6+7: core-function-synthesizer + reference-findings-summarizer (parallel)
Phase 9: pathway-inference (depends on Phase 6)
```

Estimated time savings: 30-40% when deep research is the bottleneck.

### Failure Modes

| Failure | Impact | Current Recovery |
|---------|--------|-----------------|
| Deep research timeout | Blocks entire pipeline | Retry with different provider (perplexity-lite is fastest) |
| fetch-gene fails (bad symbol) | Nothing to review | Manual fix; no auto-retry |
| All annotations UNDECIDED | Core synthesis has nothing | Usually means publications missing; run `fetch-gene-pmids` |
| Publication stubs | Weak evidence for decisions | `refresh-publications` can recover ~2100 articles |

**Missing:** No automatic fallback when deep research times out. The review skill should try a faster provider (perplexity-lite) if the primary provider fails, rather than requiring manual re-invocation.

### Redundant Work Between Agents

Low concern: annotation-reviewer and reference-findings-summarizer both read PMID files, but extract different things (curation decisions vs structured findings). The overhead of reading cached files is minimal.

### Recommendation: Agent Prompt Delivery

The review skill dispatches sub-agents via `/annotation-reviewer`, `/core-function-synthesizer`, etc. When run under boss/tp orchestration, prompt delivery can fail silently. The sub-agents should emit a structured "ready" signal after loading context, so the orchestrator can verify they started correctly.

---

## 2. Validation Pipeline

### Architecture

Validation uses LinkML + custom plugins:
- **JsonSchemaDataValidator** — hard schema errors
- **DynamicEnumPlugin** — validates GO branch membership (MF/BP/CC)
- **BindingValidationPlugin** — validates term labels against ontology
- **ReferenceValidationPlugin** — validates publication quotes

### Performance: validate-all is Slow

**Root cause:** Plugin initialization happens **per-file**. For ~1200 files, this means:
- 1200x cache reloads (`cache/enums/*.csv`)
- 1200x schema parses
- 1200x plugin initialization

The validator re-creates `LinkMLValidator`, `DynamicEnumPlugin`, and `BindingValidationPlugin` instances inside the loop in `validate_multiple_files()`. The enum cache files exist on disk but are loaded into memory for each file independently.

**Recommendation (P0):** Move plugin initialization outside the file loop. Create the `LinkMLValidator` once, iterate over files. This alone should cut validate-all time by 50%+.

**Recommendation (P1):** Consider parallel validation — files are independent, so 8-16 file batches could run concurrently.

### CI Cache/Enum Problem

**The issue:** `cache/enums/` contains runtime-generated files (hashed filenames like `gobiologicalprocessenum_769282d9de2a.csv`). These are not committed to git. In CI:

1. No pre-built enums exist
2. First file triggers OAK adapter to build enums (slow, network-dependent)
3. Each subsequent file may reload from disk but still re-initializes plugins
4. OAK may fail if network is restricted or dependency not fully installed

**Recommendation (P0):** Add a `just warm-cache` recipe that builds enum cache files, and call it in CI before `validate-all`. Consider committing the cache files to git (they're small: ~850KB total) as a fallback.

**Recommendation (P1):** Add GitHub Actions cache for `cache/enums/` directory with hash key based on schema version.

### Missing Config Path

`validator.py` line 258 references `config/oak_config.yaml` which doesn't exist in most environments. Plugins silently skip validation when this is missing. Should either create a default config or log a visible warning.

---

## 3. Boss/TP Agent Orchestration

### Prompt Delivery Failures

Known issue: `tp new` creates the session and attempts to deliver the initial prompt, but delivery can fail silently. The boss skill documents a verification step (`tp peek <slug> -n 15`) but this is manual.

**Recommendation:** After `tp new`, always run `tp peek` automatically and redeliver with `tp send --wait` if the prompt didn't land. The boss skill already documents this pattern but it's not enforced.

### Codex vs Claude Profile Reliability

The boss skill supports both Codex and Claude Code as worker agents. In practice:
- Claude Code workers are more reliable for gene reviews (they can invoke sub-skills)
- Codex workers handle simpler, more isolated tasks better
- Profile selection is manual and error-prone

**Recommendation:** Default to Claude Code for gene review tasks. Only use Codex for truly isolated, single-file tasks where skill invocation isn't needed.

### Worktree Cleanup

Worktrees live at `~/worktrees/ai-gene-review-<slug>/`. Cleanup uses `tp clean --status done-ish --force`. Issues:
- Worktrees from failed/abandoned sessions can accumulate
- No periodic cleanup mechanism
- `tp clean` only cleans sessions boss marked as `done-ish`

**Recommendation:** Add a `just clean-worktrees` recipe that finds orphaned worktrees (no matching tmux session) and offers to remove them. Also add a scheduled cleanup for worktrees older than 7 days.

### PR Follow-Through

The boss skill correctly identifies that "PR opened" is not "done". But the poll-review-fix cycle is manual and repetitive. Each worker must:
1. Wait for claude-code-review bot
2. Read review comments
3. Fix issues
4. Push
5. Wait for CI

**Recommendation:** Create a `post-pr` sub-skill that automates the poll-fix-push cycle, reducing the boss's steering overhead.

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

1. **`supporting_text_substring_not_found` (150)** — Supporting text quotes don't match cached publication text. Causes: stale publication cache, paraphrased quotes, OCR artifacts in PDF extraction.

2. **`low_annotations_supporting_text_coverage` (141)** — 40-100% of annotations lack supporting text. Worst offenders: GLRX3, SCGB2A2, EDF1, GADD45G (0% coverage).

3. **`missing_aliases` (120)** — Gene aliases not captured. Low severity but affects search.

4. **`no_deep_research_results` (80)** — Annotations don't reference deep research files. Indicates incomplete pipeline runs.

5. **`pending_annotations` (75)** — Unresolved PENDING actions (4-41 per gene).

6. **`missing_core_functions` (67)** — Core function synthesis not run.

7. **`todo_placeholder` (67)** — Descriptions contain "TODO".

8. **`inconsistent_review_actions` (32)** — Same GO term has different actions across evidence types (e.g., ACCEPT for IEA but KEEP_AS_NON_CORE for NAS).

### Observations

- Supporting text validation is the **single biggest quality issue**. The 75% stub rate in publications means most annotations can't be text-verified.
- DROME's 93% warning rate suggests batch-imported reviews that weren't fully curated.
- Inconsistent review actions (same term, different decisions by evidence type) may indicate a schema gap — should the schema enforce consistency, or is this intentional for edge cases?

**Recommendation (P1):** Add a `just quality-report` recipe that generates a dashboard of warning patterns by organism, highlighting genes most in need of completion.

**Recommendation (P2):** Consider adding a `PARTIALLY_REVIEWED` status to track genes where annotation review is done but core functions / references are incomplete.

---

## 5. Publication Caching System

### Scale

- **14,841 PMID-keyed files**, 50 DOI-keyed files
- **75% are stubs** (abstract only), 25% have full text
- Three-tier retrieval: XML (69.5% of successes) → HTML (30.5%) → PDF (0.1%)

### DOI vs PMID Keying

DOI files use an incompatible schema (`reference_id`, `content_type`) vs PMID files (`pmid`, `full_text_available`, `full_text_extraction_method`). Only 50 DOI files exist, but they're effectively invisible to the validation and review pipeline.

**Recommendation (P1):** Either convert all DOI files to PMID-keyed format (most DOIs have PMIDs) or add DOI→PMID lookup to the fetch pipeline so references are unified.

### Stub Entries

~11,168 stub entries. Estimated ~2,100 have PMC IDs and could be recovered via `refresh-publications`. The `refresh-publications` recipe exists but isn't run systematically.

**Recommendation (P2):** Add a CI job or scheduled task that periodically runs `refresh-publications` for genes currently under active review, prioritizing stubs cited in existing annotations.

### Full-Text Availability

| Category | Count | Notes |
|----------|-------|-------|
| No PMC ID | ~8,000 | Older articles, non-OA journals — can't recover |
| PMC but no full text | ~2,100 | Recoverable via refresh |
| Successfully retrieved | 3,640 | Working |
| Abstract extracted only | ~332 | Publisher blocks, partial HTML |

### PMC Override System

`src/ai_gene_review/etl/pmc_overrides.tsv` has only 2 entries despite NCBI linkage errors being common. This is underutilized.

**Recommendation (P2):** When `refresh-publications` fails for a PMC article, log the failure to a candidates file for manual override review.

---

## 6. Deep Research Providers

### Provider Comparison

| Provider | Typical Time | Quality | Reliability | Notes |
|----------|-------------|---------|-------------|-------|
| Perplexity (sonar-deep-research) | ~2 min | High, 38 citations avg | Good | Fastest, best default |
| Perplexity-lite (sonar-pro) | ~1 min | Medium | Good | Fast fallback |
| Falcon (Edison) | ~9 min | Good, 30 citations avg | Good | Legacy, slower |
| OpenAI (Deep Research) | ~5-10 min | Thorough | Moderate | Most detailed |
| Cyberian | Variable | Unknown | Poor for large genes | VCP was too big |

### Coverage Gaps

- Only ~40% of human genes have any deep research
- Coverage is uneven: some genes have 3 providers, many have none
- High-priority genes (BRCA1, BRCA2, EGFR) lack deep research entirely
- No systematic prioritization of which genes to research

### Timeout Issues

All providers use 600s (10 min) timeout. Cyberian fails for large/complex genes like VCP where the research scope exceeds the timeout. No adaptive timeout based on gene complexity.

**Recommendation (P1):** Add a `just deep-research-status` recipe that shows coverage gaps, prioritized by:
1. Genes with active reviews but no deep research
2. Genes with high annotation counts (likely complex, most benefit from research)
3. Genes under active curation projects

**Recommendation (P2):** Implement automatic provider fallback in the deep research client: if primary provider times out, retry with perplexity-lite before failing.

**Recommendation (P3):** For known-large genes (high annotation count or long UniProt record), use a higher timeout or chunk the research query.

---

## Prioritized Recommendations Summary

### P0 — High Impact, Fix Soon

| # | Area | Recommendation |
|---|------|---------------|
| 1 | Validation | Move plugin initialization outside file loop in `validate_multiple_files()` |
| 2 | CI | Add `just warm-cache` step before `validate-all` in CI workflows |
| 3 | CI | Consider committing `cache/enums/` files (850KB total) as CI fallback |

### P1 — Important, Plan for Next Sprint

| # | Area | Recommendation |
|---|------|---------------|
| 4 | Review workflow | Parallelize pub-cache with deep-research in `/review` |
| 5 | Review workflow | Auto-fallback to perplexity-lite when primary deep research provider times out |
| 6 | Publications | Unify DOI/PMID keying — convert or add DOI→PMID lookup |
| 7 | Deep research | Add `just deep-research-status` recipe showing coverage gaps |
| 8 | Data quality | Add `just quality-report` dashboard by organism and warning type |
| 9 | Validation | Log visible warning when `oak_config.yaml` is missing |

### P2 — Nice to Have

| # | Area | Recommendation |
|---|------|---------------|
| 10 | Publications | Periodic `refresh-publications` for genes under active review |
| 11 | Publications | Log refresh failures to candidates file for override review |
| 12 | Data quality | Add `PARTIALLY_REVIEWED` status for incomplete pipeline runs |
| 13 | Boss/TP | Add `just clean-worktrees` for orphaned worktree cleanup |
| 14 | Boss/TP | Create `post-pr` sub-skill for automated poll-fix-push cycle |
| 15 | Validation | Parallel file validation (8-16 concurrent batches) |

### P3 — Future

| # | Area | Recommendation |
|---|------|---------------|
| 16 | Deep research | Adaptive timeout based on gene complexity |
| 17 | Deep research | Chunked research queries for large genes |
| 18 | Boss/TP | Default to Claude Code profile for gene review tasks |
