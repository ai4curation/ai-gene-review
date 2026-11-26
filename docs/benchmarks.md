# Time-split annotation benchmarks

`ai-gene-review benchmark` builds benchmarks of protein function annotations
that no predictor could have seen. A target is an annotation that is in a later
GO release and absent from a baseline release on or before a cutoff date. The
targets are then checked, mostly by code, for leakage, near-duplication and
balance. The schema is `src/ai_gene_review/schema/benchmark.yaml` (LinkML). The
skill that drives it is `.claude/skills/benchmark-builder/`. The worked example is
`benchmarks/human-goa-2025-06/`.

## Purpose

The benchmark expands the analysis in the fable-sequence-to-function preprint
(`ai4curation/fable-sequence-to-function`). That preprint asked small,
hand-built questions of a model that sees the sequence alone. This benchmark asks
the same kind of question on many more proteins, with time-split, leakage-checked
targets. It also compares conditions item by item:

| condition | context | what the predictor sees |
|---|---|---|
| `blind` | `BLIND` | the sequence only (`peptalk ask --context blind`, the fs2f protocol), optionally with a shuffled-sequence control |
| `organism` | `ORGANISM` | the sequence plus organism and taxon id |
| `full` | `FULL` | the sequence plus the UniProt-style header: accession, protein name, gene |
| `agent-review` | `AGENT_REVIEW` | combined reasoning: an agent reads the sequence and reasons over knowledge and context, as in an ai-gene-review review seeded with baseline-release annotations only |

The difference between `blind` and `agent-review` on the same item separates
reading the sequence from recalling or retrieving knowledge about the named
protein. Decoy terms and shuffled sequences measure how often a predictor says
yes regardless.

## Workflow

```bash
just benchmark-build  benchmarks/<id>/<id>-spec.yaml    # draw items -> <id>.yaml
just benchmark-check  benchmarks/<id>/<id>.yaml         # -> <id>-check-report.{yaml,md}
just benchmark-export benchmarks/<id>/<id>.yaml         # -> run-inputs/ (FASTA, claims, baseline GOA)
peptalk ask run-inputs/<id>.fasta --claims run-inputs/<id>-claims.tsv --context blind --shuffle-control > runs/blind.jsonl
just benchmark-score  benchmarks/<id>/<id>.yaml --peptalk runs/blind.jsonl --reviews-dir runs/agent-review/genes
just validate-benchmarks
```

GO release files and UniProt responses are cached in `.cache/benchmark/`
(git-ignored). `run-inputs/` and `runs/` are git-ignored too: `export`
regenerates the inputs, and run outputs belong with whoever ran them.

### The spec

A `BenchmarkSpec` states the request: taxon, cutoff date, baseline and current
GO releases, aspects, optional GO branches, evidence codes (default: CAFA's EXP,
IDA, IPI, IMP, IGI, IEP, TAS, IC), excluded terms (default: roots, binding,
protein binding), whether NOT annotations count as negative targets, size, seed,
feature quotas (for example `PSEUDOENZYME`, with a UniProt query), the number of
decoys per item, and the evaluation conditions. Each condition records its
model and, where known, the model's training cutoff.

`min_reference_date` keeps only targets whose supporting PubMed references
were all published on or after a date. A target that also rests on an older
paper is dropped whole, and the earliest supporting paper becomes the target's
`reference`. This matters more for language models than it did for CAFA. A
GO time split only shows that the GO record is new. A model may have read the
paper. A feature quota can set its own `min_reference_date` when the feature
is too rare to fill from the main window.

### Modes

- `GOA_TIME_SPLIT`: targets are current-release rows that pass the filters and
  the novelty test. Proteins are sampled with the seed, feature quotas first.
  A reference that adds new annotations to more than `max_proteins_per_reference`
  proteins is treated as high-throughput and its rows are dropped.
- `REVIEW_DERIVED`: targets are the ACCEPT and NEW annotations of
  ai-gene-review reviews (`--reviews ...`), kept only when they too are absent
  from the baseline release. Run agentically, the skill first reviews N
  candidate genes with the normal review workflow, then builds from those
  reviews.

Both modes pin each item's UniProt sequence and sequence version, record
PubMed publication dates, attach the review action when the gene has a review,
grade every target, and draw decoys.

## Deterministic checks

`benchmark check` reruns everything against the pinned sources. A hand-edited or
review-derived benchmark is held to the same tests as a drawn one.

| check | what it tests |
|---|---|
| `schema` | the Benchmark validates (closed LinkML/JSON Schema) |
| `novelty` | no baseline experimental row for the term, a descendant, or an alt_id or obsolete id the current ontology maps onto them; for NOT targets, no baseline NOT row to the term or an ancestor (FAIL) |
| `present_in_current` | the row is in the current release (FAIL for GOA targets) |
| `date_window` | the GAF date is on or after the cutoff (WARN only; see below) |
| `prior_prediction` | the term or a descendant was predicted on the protein at baseline (IBA/PAN-GO, IEA, ISS, ...) |
| `homolog_leakage` | the term or a descendant was experimentally annotated at baseline on a protein in the same PANTHER subfamily (INFO when the protein has no subfamily: not checked) |
| `near_duplicate` | the closest baseline experimental term in the same aspect has Lin similarity at or above the threshold (IC from baseline annotation frequencies; INFO when there is no baseline term to compare) |
| `uniprot_leakage` | the current UniProt entry carries the target in a DR GO line (INFO) or its label in comment text (WARN) |
| `header_leakage` | the protein name shown in FULL conditions shares most of the target label's words |
| `reference_recency` | the earliest supporting paper was published after each condition's model training cutoff |
| `decoy` | decoys neither entail nor are entailed by any current annotation of the protein |
| `feature_label` | a query-derived feature (pseudoenzyme) is supported by the UniProt protein name, not only by comment text |
| `review_agreement` | an ai-gene-review review of the gene keeps (PASS) or contests (WARN) the target |
| `balance` | requested size, aspects and feature quotas met; no single reference supplies more than 25% of targets or targets to more than 10% of items |
| `difficulty` | a recorded difficulty agrees with the grading checks |

Difficulty follows from three of these checks. A target is EASY if
`prior_prediction` or `homolog_leakage` fires, MEDIUM if `near_duplicate`
fires, and HARD otherwise. An item takes the hardest grade among its targets.
The knowledge category follows CAFA, judged on baseline experimental rows
outside the excluded terms: `NO_KNOWLEDGE`, `LIMITED_KNOWLEDGE` (experimental
annotation only in another aspect) and `PARTIAL_KNOWLEDGE`.

## Agentic parts

- **Agent evaluation** (`<id>-agent-evaluation.yaml`, class `AgentEvaluation`):
  an agent reads the finished benchmark and its check report and records
  ambiguous, wrong, trivial or leaked targets and imbalance. Each finding
  should name a deterministic check that would confirm it. These are an
  agent's judgements, not expert review. Say who the evaluator is and whether
  it is independent of the builder.
- **Review-derived build**: see Modes.

## Things the example taught

- **GAF dates are not creation dates.** GO re-stamps the date column. An IPI
  from a 2021 paper carries 20260725 in the 2026-08-05 release. Novelty is
  decided by absence from the baseline release, never by date. `date_window`
  is informational.
- **Evidence codes churn between releases.** Between 2025-06-01 and 2026-08-05
  the human GAF lost about 15,000 IDA rows and gained about 15,000 EXP rows.
  Novelty is therefore keyed on term and qualifier, not evidence code.
- **New to GO is not new knowledge.** In the example window, 10,771 rows on
  4,420 human proteins passed the novelty test (after the high-throughput
  filter). Only 393 rows on 182 proteins rest wholly on papers published since
  2025-06-01, and 10 rows on 6 proteins on papers since 2026-06-01.
- **GO moved its per-species files** to `annotations/gaf/<CODE>-uniprot.gaf.gz`
  in 2026. The loader tries both layouts.
- **Feature labels from UniProt queries are not literature checks.** In draws
  of the example, SMARCA1 matched a pseudoenzyme query only through isoform-2
  text, KLK11 (an active protease) only through the names of its cleavage
  chains ("inactive chain 1"), and WHR1 (formerly STK19) only through an
  AltName. All are recorded with `literature_checked: false`. `feature_label`
  reads only the protein's own names and flags the first two. This is the
  lesson of fs2f's `NAMED_INACTIVE_LABELS.md`.

## Related practice

- **CAFA** (Critical Assessment of Functional Annotation). Prediction is
  followed by a waiting period, and new experimental annotations become the
  targets. Proteins are split into no-knowledge and limited-knowledge targets,
  and in CAFA3 partial knowledge. A target is excluded when a descendant was
  already known. `evaluation/cafa.py` holds the repository's PAN-GO-style
  scorer, and the benchmark reuses its excluded-term defaults.
- **fable-sequence-to-function.** Its test sets are committed exactly as drawn,
  because the build scripts query live services. It has a decoy control
  (substitutions at non-catalytic positions) and shuffled-sequence controls. It
  stratifies by prior homology (no close earlier PDB match). Its "inactive"
  labels were checked against the full text, and two of three checked were
  contradicted. The benchmark follows each of these: it commits the drawn
  benchmark with source checksums, draws decoy terms and supports shuffled
  controls, grades difficulty by prior and homolog knowledge, and does not treat
  UniProt-name labels as literature.
- **"A Society of AI Scientists"** (alphaXiv `2611.society-ai-scientists`, 21 Nov
  2026; only the abstract page loaded, the PDF viewer rendered no text). It is
  an observational study of 936 agents publishing to a shared preprint server,
  not a benchmark paper, so its relevance is low. Three points carry over.
  Text-only agent referees barely separated flawed from corrected papers (11/16
  vs 10/16). Objections run against the uploaded data overturned conclusions
  far more often. LLM ratings are not expert review. The agent evaluation here
  therefore asks each finding to name a deterministic check, and the benchmark,
  its sources and its check report are released together.

## Limits

- The homolog check uses same-species PANTHER subfamilies only. Cross-species
  ortholog knowledge enters through IBA, ISS and ISO rows (`prior_prediction`).
- PANTHER subfamilies, UniProt entries, sequences and feature queries come from
  current UniProt (release recorded), not from the baseline date.
- A decoy is a term the protein is not annotated to, not one it is known to
  lack, so a yes on a decoy is not necessarily wrong.
- `min_reference_date` and `reference_recency` use the PubMed record date. A
  preprint, accepted manuscript or author copy may have been readable, and in a
  model's training data, a year earlier. A preprint-date lookup would tighten
  both.
- Decoys are scored only where a predictor is asked about them. A review is
  never asked about decoys, so the agent-review condition records them as
  missing, and its decoy rate is not comparable with the peptalk conditions.
  Compare conditions on targets, and on decoys only among the peptalk runs.
- Review verdicts count ACCEPT, KEEP_AS_NON_CORE, NEW, TOO_GENERAL and MODIFY
  rows (including MODIFY's replacement terms) and every core-function term
  slot as assertions. REMOVE and MARK_AS_OVER_ANNOTATED count as "no".
- Existing ai-gene-review reviews were written with current GOA in view. Scoring
  them with `--reviews-dir genes` measures agreement, not an AGENT_REVIEW run.
  A real run seeds each review with `run-inputs/baseline-goa/<ACC>-goa.tsv` and
  keeps the agent away from post-cutoff sources.
