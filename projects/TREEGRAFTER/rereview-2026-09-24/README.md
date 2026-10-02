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
  checking, and a composed one passes validation silently. Every `file:` quote
  this audit **added** was checked by hand (`grep -cF` against the cited file);
  the ones it inherited were swept once, with the result recorded below rather
  than left implicit.

This is a known repo-wide blind spot, documented in
[`MISCITATIONS.md`](../../MISCITATIONS.md), [`SPKW.md`](../../SPKW.md) and
[`FUNCTION_KNOWLEDGE_GAPS.md`](../../FUNCTION_KNOWLEDGE_GAPS.md); the SPKW audit
measured ~48% of 550 `file:` quotes non-verbatim while passing validation.

### What the sweep of this audit's changed set found

**`file:` `supporting_text` lives in two different slot classes, and the tools
disagree about which one they read.** Getting this wrong is how the first pass of
this sweep measured only half the set, so the slots come first:

| slot | count here | what checks it |
|---|---|---|
| `*.supported_by[]` (annotation `review`, `core_functions`, `proposed_new_terms`) | 945 | the external `linkml-reference-validator` CLI — but not for `file:`, which is in `skip_prefixes` |
| `references[].findings[].supporting_text` | 261 | `validator.py:117–131`, the repo-local gate — but only for `LITERATURE_PREFIXES`, so not `file:` either |

So **neither slot is gated for `file:`**, and the two code paths cover opposite
halves. The first version of this sweep keyed on `reference_id` and
`supporting_text` appearing in the same mapping, which is true in `supported_by`
and false in `findings` (where the id sits on the parent `- id:`), so it silently
skipped all 261 — **which is the slot the repo-local gate actually reads.**
A future `file:` gate has to name its slot set, or it will measure the wrong half
exactly as this did.

**Re-measured across both: 1206 quotes in 104 reviews, 15 non-verbatim, of which
3 were fixed and 12 were left.**

| | | |
|---|---|---|
| fixed | 3 | `THLAR/TFP` ×2 (`supported_by`), and one on the `PSEPK/retS` `GO:0071474` row this audit relaxed to `UNDECIDED` |
| left, inherited — `supported_by` | 7 | `PSEAI/merA` 1, `PSEPK/groES` 1, `PSEPK/retS` 5 |
| left, inherited — `references[].findings[]` | 5 | `PSEAI/merA` 2, `PSEPK/retS` 2, `SALSP/mcr-4` 1 |

All twelve are non-verbatim, all are byte-identical on `main`, and none sits on a
row this audit moved — so they were reported rather than fixed, to keep the
audit's diff from becoming a cleanup of inherited quote problems. **Do not read
this section as "the changed set is verbatim": it is 12/1206 short, deliberately
and with the genes named.** (`merA` and `groES` carry `no_change` history records
for this reason; their first records say "one", which was true of the
`supported_by`-only sweep that wrote them and is superseded by the figures here.)

Two details that a count of distinct strings hides: `merA`'s quote occupies **two
sites** — `supported_by` and `references[].findings[]`, the same text plus a
period — so occurrences exceed distinct strings; and the compositions are **not**
confined to notes files, which is the tempting generalisation. Of the five
`findings` misses, two are `-notes.md`-sourced (`retS`), two are
`-deep-research.md`-sourced (`merA`) and one comes from a `.tsv`
(`SALSP/mcr-4`, `candidate_new_annotations.tsv`). Deep-research-sourced quotes
are *usually* real copies, markdown emphasis included — spot-checks on `flgG` and
`PP_1084` are verbatim — but `merA` shows the habit is not source-specific.

A naive substring test over-reports, and the way it does so differs **per slot** —
which matters because the breakdown below is the spec a future `file:` gate would
be built against. Raw flags, classified, with each denominator named:

| class | `supported_by` (of 945) | `references[].findings[]` (of 261) | both (of 1206) |
|---|---|---|---|
| UniProt line-wrap artifact | 25 | 2 | 27 |
| marked ` ... ` elision | 2 | 0 | 2 |
| **real composition** | **7** | **5** | **12** |
| raw flags | 34 | 7 | 41 |

- **Wrap artifacts.** The quote *is* present, split across `CC` continuation
  lines — `secD`'s `Part of the essential Sec protein translocation apparatus`
  straddles `secD-uniprot.txt:47–48`. A gate must unwrap `CC`/`DR` continuations.
  The findings slot's two are **`PSEPK/infC:128`** (the IF-3 30S-binding
  sentence, straddling `infC-uniprot.txt:29–31`) and **`PSEPK/mraY:191`** (the
  phospho-MurNAc-pentapeptide transfer, straddling `mraY-uniprot.txt:32–34` —
  the quote begins at `transfers`, the last word of `:32`). Both are under a
  `- id: file:…-uniprot.txt` parent in `references[].findings[]`, and both return
  `grep -cF` **0** against their source while matching once the `CC`
  continuations are unwrapped. Named because they are the evidence for the rate
  difference below, and the one row in this table `grep` could not otherwise
  check.

  *(Earlier revisions of this line cited `infC:182` and `mraY:192` with a
  two-line span. `infC:182` was wrong twice over — it is a
  `core_functions[].supported_by` quote, not a findings one, and its shorter text
  is verbatim at count 1, so it is not an artifact at all. Both locators had been
  derived by grepping for the quote text separately from the pass that classified
  it, which matched a different occurrence; they are now read from the files.)*
  **But do not size that work from the `supported_by` rate**: it is 25/34 (74%)
  there and 2/7 (29%) in the findings slot, because the two slots cut quotes
  differently — findings-slot quotes are short and tend to stop *at* a wrap
  boundary rather than run across one (`flgG:106` ends exactly where
  `flgG-uniprot.txt:45` ends, which is why it passes). The same slot asymmetry
  that made the first sweep measure half the corpus also makes its artifact rate
  non-transferable.
- **Marked elisions.** `zwf` joins two fragments with a literal ` ... `, visible
  to a reader. Both are in `supported_by`; the findings slot has none. A gate has
  to decide whether that is a supported convention.
- **The slot set**, per the table above: `supported_by[]` *and*
  `references[].findings[]`. The two existing code paths each read one, so a gate
  inheriting either one's scope measures half the corpus.
- **Test the passes, not only the flags.** Every round of PR #3165 audited the
  quotes this sweep *reported*; a classifier checked only on its output can be
  wrong in the direction nobody looks. Round 14 sampled two quotes it had
  *cleared* (`NICAT/NaPMT1.1`, neither previously named) and both are verbatim at
  count 1. A gate needs that check in its own tests, or a silent false-negative
  rate stays invisible.

The difference between a marked and a silent elision is why only some of these
read as quotes at all: `zwf` shows the join; `merA` performs the same operation
invisibly, fusing two clauses three sentences apart and changing `when` to
`When`; `groES` splices across two source sentences. **Silent splices are the
class that needs the gate**; marked elisions are a convention question.

Two independent measurements of the same blind spot now exist — ~48% of 550
(SPKW) and 12/1206 ≈ 1.0% (here, both slots) — which differ by corpus, not by
method. Every rate in this section carries its denominator in the same sentence,
deliberately: three findings running on PR #3165 were "the measurement is sound,
the sentence around it is wider than the measurement" (166-vs-165, 7/945,
945-of-1206), and naming the scope at the point of use is the one habit that
would have caught all three.

One more thing a gate would have to settle: `file:` references use **three**
different base conventions, and under `reference_base_dir: genes` only one
resolves.

| form | example | resolves to | ok? |
|---|---|---|---|
| `genes`-relative | `file:PSEPK/accD/accD-uniprot.txt` | `genes/PSEPK/…` | ✅ |
| repo-root-relative | `file:interpro/panther/…/*-paint.tsv` | `genes/interpro/…` | ❌ |
| repo-root incl. `genes/` | `file:genes/SALSP/mcr-4/mcr-4-uniprot.txt` | `genes/genes/SALSP/…` | ❌ |

The second is what the PAINT citations here and dozens of existing reviews use;
the third appears in **50 reviews** repo-wide (`SALSP/mcr-4` uses it at ten sites,
alongside `file:projects/…` paths). So a gate cannot pick one base and treat the
others as the error case — it has to recognise all three. Nothing breaks today
only because `file` is skipped entirely, which means two of the three forms have
never been resolvable by any tool, only by a human with `grep`. This is
pre-existing convention drift, not something this audit introduced.

So: when reading a rationale here, treat a `file:` quote as a reviewer's
transcription rather than a gated fact.

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
