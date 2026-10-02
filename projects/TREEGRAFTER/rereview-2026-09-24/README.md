# TreeGrafter rejection re-review, 2026-09-24

This audit re-examines every TreeGrafter annotation (`IEA` / `GO_REF:0000118`)
whose gene review currently records `action: REMOVE` or
`action: MARK_AS_OVER_ANNOTATED`. The question for each row is whether that
rejection stands on stated biological grounds, or whether it should be relaxed
to `ACCEPT`, `KEEP_AS_NON_CORE`, `MODIFY`, or `UNDECIDED`.

Genes whose rejected rows were already re-assessed in the
[2026-09-20 audit](../rereview-2026-09-20/) (`status: reviewed`) are excluded
here; those decisions stand as recorded there.

Scope is the flagged rows only (`scope: treegrafter_rejections`), not a
full-gene re-review. Other annotations in the same gene are not re-adjudicated
unless a decision on a flagged row logically requires it (for example, a
`MODIFY` whose replacement term is already carried by another row).

## Decision rules

Taken from `CLAUDE.md` and the 2026-09-20 audit README:

1. **`REMOVE` needs positive contrary evidence.** It is appropriate for an
   electronic propagation that is demonstrably wrong: reaction chemistry or
   substrate that the target cannot perform, a domain architecture the target
   lacks, lost catalytic residues, a pathway absent from the organism, or a
   direct experimental contradiction. "Family-level propagation" or "no
   target-specific assay" is not, on its own, grounds for `REMOVE`; the absence
   of a target experiment does not refute a supported phylogenetic inference.
2. **Broad but true terms are not over-annotations.** `cytoplasm` or `cytosol`
   on a soluble bacterial enzyme is correct; redundancy with a more specific
   sibling does not make it wrong. Such rows go to `ACCEPT` (or
   `KEEP_AS_NON_CORE` when the location is real but peripheral). A generic
   location that is *incompatible* with the protein (e.g. `cytosol` on an
   integral membrane transporter with no soluble pool) can stay rejected.
3. **Too-coarse terms are `MODIFY`, not `REMOVE`.** When the propagated term
   is a true ancestor of the gene's real activity, or a sibling that names the
   right chemistry with the wrong specificity, use `MODIFY` with a
   `proposed_replacement_terms` entry, or `ACCEPT` when the specific term is
   already carried by another row and the ancestor is simply true.
4. **`MARK_AS_OVER_ANNOTATED`** is for terms that are not false but attribute
   more than the evidence supports (e.g. a whole-pathway process term on a
   single enzyme whose product could feed that pathway). When even that is
   uncertain, prefer `UNDECIDED` over asserting a rejection.
5. **Verify the term definition** (QuickGO
   `https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:NNNNNNN`) and
   the target's own evidence: `*-uniprot.txt` (catalytic activity, domains,
   InterPro/PANTHER cross-references), `*-goa.tsv` (other evidence for the same
   or related term), the notes and cached deep-research files, and cached
   publications. Do not invent evidence, PMIDs, or term ids.

## Record format

One batch YAML per reviewer batch (`batch-NN.yaml`), top-level `date`, `scope`,
and `genes`. Each gene entry records `gene`, `gene_file`, `status`
(`reviewed`), `scope: treegrafter_rejections`, `outcome`, and an `annotations`
list with `term_id`, `term_label`, `evidence_type`, `original_reference_id`,
`previous_action`, `action`, `outcome` (`retained` when action unchanged,
`changed` otherwise), and a `rationale` written from the evidence considered.
When the review file was edited, the gene also gets an append-only history
record scaffolded with `just new-history`.

**The two `outcome` fields mean different things, and the gene-level one is
defined here because the first pass left it implicit.** Both describe
adjudication, not file edits:

- annotation-level `outcome`: `retained` when `previous_action == action`,
  `changed` otherwise.
- gene-level `outcome`: `changed` when **any** of the gene's annotations
  changed action, `confirmed` when none did.

So a gene whose actions all stand is `confirmed` even if its `reason` prose was
rewritten — strengthening a rationale is not a change of adjudication, and the
history record is what records the edit. The first pass applied this field
inconsistently (some entries tracked the file rather than the decision); PR
#3165 settled on the definition above and brought every entry into line with
it. `check_outcomes.py` enforces it, so the next audit inherits a rule rather
than re-inferring one. `summarize.py` reads only the annotation-level field, so
the gene-level value is documentary.

## What the verbatim check does and does not cover

This audit's rules lean on `supporting_text` being a verbatim substring of its
source, and round 3 caught a quote composed to fit a term exactly that way. The
check is **not symmetric across reference types**, and the asymmetry is worth
stating because it is easy to mistake a passing `just validate` for a verified
quote:

- **`PMID:` / `DOI:` quotes are gated.** `validate_reference_finding_supporting_text`
  runs on `LITERATURE_PREFIXES` only, and a non-verbatim snippet fails.
- **`file:` quotes are not gated at all.** `conf/reference_validator_config.yaml`
  lists `file` in `skip_prefixes`, so `file:` references are exempt from snippet
  checking. Every `file:` quote in this audit is **hand-verified** (by `grep -cF`
  against the cited file), not machine-checked, and a composed one passes
  validation silently.

This is a known repo-wide blind spot, documented in
[`MISCITATIONS.md`](../../MISCITATIONS.md), [`SPKW.md`](../../SPKW.md) and
[`FUNCTION_KNOWLEDGE_GAPS.md`](../../FUNCTION_KNOWLEDGE_GAPS.md); the SPKW audit
measured ~48% of `file:` quotes non-verbatim while passing validation. Two
instances surfaced inside this audit's own changed set (PR #3165 round 10:
`THLAR/TFP`, both `file:` quotes, plus one on the `PSEPK/retS` row this audit
relaxed) and were fixed by substring swap. So: when reading a rationale here,
treat a `file:` quote as a reviewer's transcription rather than a gated fact.

## What the counts count

`192`, `117` and `75` are counts of **recorded rows**, and the gene figures need
the same care, because one protein in this audit has two records. `PSEPK/aroQ`
and `PSEPK/aroQ-III` were two reviews of the same protein (Q88IJ6), which this
audit merged; the record for the merged-away folder stays (records are
append-only) and declares `merged_into`, so its single `GO:0019631` row is
recorded twice but was adjudicated once. The live state is therefore:

| figure | value | meaning |
|---|---|---|
| `recorded_rows` | 192 | annotation rows across the ten batch records |
| `distinct_adjudications` | 191 | rows on entries not marked `merged_into` |
| `gene_entries` | 166 | `- gene:` entries across the records |
| `proteins` | 165 | entries not marked `merged_into` |

`summarize.py` derives all four from `merged_into` rather than from a hand
adjustment, and `check_outcomes.py` checks a merged entry's action against the
surviving twin instead of skipping it. The transition table and the
`117 stand / 75 relaxed` split are row counts, so they include the `aroQ` pair
once each.

A gene entry's `gene` label mirrors its folder name under `genes/<ORG>/`,
accession suffix included where the folder carries one (`PSEPK/dapF__Q88CF3`,
`PSEPK/dapA__Q88NH2`). The suffix is the disambiguator the folder layout
already uses; two of these labels would otherwise collide.

`summary.tsv` is generated from the batch files by `summarize.py`.
