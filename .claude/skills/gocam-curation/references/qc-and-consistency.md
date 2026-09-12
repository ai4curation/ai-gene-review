# Verdict, QC flags, consistency & checklist

These controlled vocabularies are the schema enums used in a
`GoCamActivityReview`. Fill them per activity.

## Verdict — `GoCamClaimVerdictEnum`

Overall best-practice/evidence verdict for the activity (the forensic
claim-validation scale):

- **OK** — well supported and best-practice-compliant (correct MF specificity,
  correct `has input`/causal usage, adequate evidence).
- **UNCERTAIN** — defensible but imprecise or under-supported; needs a caveat.
- **WRONG** — contradicts the evidence or breaks a hard rule (binding-as-function,
  reversed causality, etc.).

No "probably fine" — every activity gets an explicit verdict, ideally with a
verbatim quote-back in `supporting_text`.

## QC flags — `GoCamQcFlagEnum`

Record every specific issue observed (multivalued):

| Flag | Meaning | Detail |
|---|---|---|
| `BINDING_AS_FUNCTION` | bare binding MF, no consequence | molecular-function.md |
| `GENERIC_MF` | generic term where a child applies | molecular-function.md |
| `HAS_INPUT_MISUSE` | wrong `has input` filler | has-input.md |
| `DIRECT_VS_INDIRECT_CAUSAL` | directness wrong for the mechanism | causal-relations.md |
| `INCORRECT_DIRECTIONALITY` | reversed subject→object edge | causal-relations.md |
| `MISSING_LOCATION` | no `occurs_in` | — |
| `MISSING_PROCESS` | not tied to a process via `part_of` | — |
| `ORPHAN_ACTIVITY` | no causal edges | causal-relations.md |
| `MISSING_EVIDENCE` | no ECO code / reference | — |
| `COMPLEX_SUBUNIT_REPRESENTATION` | wrong subunit/complex attribution | complexes.md |

## Consistency with the gene review — `GoCamConsistencyEnum`

How the activity relates to the gene's `genes/**/<gene>-ai-review.yaml` (join on
`gene_product` via `gocams/index.tsv`):

- `CONSISTENT` — matches an accepted core function in the review.
- `MORE_SPECIFIC` / `MORE_GENERAL` — a clean subsumption either way.
- `RELATED` — same area, neither match nor clean subsumption.
- `CONFLICT` — the review **removed / negated / over-annotated** this function.
- `NOT_IN_REVIEW` — function not represented in the review (a candidate gap).
- `NO_GENE_REVIEW` — no review exists yet for this gene product.

`CONFLICT` and `NOT_IN_REVIEW` are the signals worth surfacing.

## Pre-finalize checklist

- [ ] MF is the most specific correct term (not generic, not bare binding).
- [ ] `has input` names the substrate/target-gene/effector/cargo — not a ligand or raw DNA.
- [ ] Causal edges are direct/indirect as the mechanism warrants, pointing subject→object.
- [ ] `occurs_in` and `part_of` present where known.
- [ ] Every activity/edge has an ECO code + reference; claims have verbatim support.
- [ ] Complex activities attributed to the right subunit(s).
- [ ] `verdict`, any `qc_flags`, and `consistency` recorded for every activity.
