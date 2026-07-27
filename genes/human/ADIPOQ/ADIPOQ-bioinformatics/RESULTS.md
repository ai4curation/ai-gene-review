# ADIPOQ (Q15848) — computed evidence for the GO annotation review

All numbers below are produced by `analyze_adipoq.py` and stored in
`results.json`. Re-run with:

```bash
uv run python analyze_adipoq.py            # full run (needs network)
uv run python analyze_adipoq.py --self-test  # break-test the guards
```

The script fails loudly on a missing input and never returns a partial
section. Every paginated query asserts `numberOfHits == len(results)`; where a
reference is too large to paginate honestly the entity count is reported as
**unavailable** rather than estimated from one page.

---

## A. The `fetch-gene` stub under-seeds this gene by 58 rows

| quantity | value |
|---|---|
| GOA TSV data rows | **161** |
| distinct rows (term + evidence + reference + qualifier + WITH/FROM + assigner) | **161** |
| entries the seeder produced | **103** |
| rows lost to collapse | **58** |

There are no duplicate lines in the TSV — the 58-row gap is entirely the known
`GOAValidator.seed_missing_annotations` behaviour, which keys entries on
`(GO id, evidence, reference, negated, qualifier)` and **omits `WITH/FROM`**.
On ADIPOQ that collapses 65 `IPI` rows (one per interaction partner) into a
handful of stubs. The review restores one entry per GOA row; the guard in
`analyze_adipoq.py` asserts `review_yaml_entries == goa_rows_distinct` and
fails otherwise.

## B. Reference-projection test — two bulk imports found

For every `TAS` / `NAS` / `RCA` / `HDA` / `IPI` reference, how many *distinct
entities* does that reference annotate in all of GOA?

| reference | annotations | entities | term we carry | entities on that term |
|---|---|---|---|---|
| PMID:36399478 (MatrisomeDB 2.0) | 285 | 274 | `GO:0140149` | **272**, `TAS`+`IDA`, all `GO_Central` |
| PMID:28675934 (ECM proteomics) | 219 | 135 | `GO:0005201` | **41**, `RCA`, `BHF-UCL` |
| PMID:28675934 | " | " | `GO:0031012` | 135, `HDA`, `BHF-UCL` |
| PMID:27068509 | 188 | 149 | `GO:0005576` | 103, `HDA`, `BHF-UCL` |
| PMID:10095105 (gene structure) | **1** | **1** | `GO:0006091` | 1, `TAS`, `PINC` |
| PMID:12611609 (review article) | 2 | 1 | `GO:0005125`, `GO:0050728` | 1 each, `NAS` |
| PMID:12070119 (PDGF-BB binding) | 11 | 4 | `GO:0005515` etc. | 2 (reciprocal pair) |
| PMID:16622416 (APPL1) | 4 | 4 | `GO:0005515` | 4 |
| PMID:12021245 | 3 | 2 | `GO:0042803`, `GO:0045599` | 1–2 |
| PMID:25910212 | 1021 | 470 | `GO:0005515` | 468 |
| PMID:31515488 | 3269 | — | `GO:0005515` | too large to paginate |
| PMID:32296183 (HuRI) | **85343** | — | `GO:0005515` | too large to paginate |
| PMID:32814053 | 20010 | — | `GO:0005515` | too large to paginate |

**Reading.**

* `GO:0140149` from **PMID:36399478 is a database import**. MatrisomeDB 2.0 is
  a database-update paper; one such reference giving **272 entities** one
  identical cellular-component term is an import, not 272 author statements.
* `GO:0005201` from **PMID:28675934 is a bulk `RCA` block** over 41 entities,
  alongside `GO:0030020`/`GO:0030021`/`GO:0030023` (the collagen
  tensile-strength terms) over 31/8/4 more. The pipeline converted
  matrisome-proteomics *detection* into ECM *structural* roles.
* The `GO:0005576` `HDA` row (PMID:27068509, 103 entities) is the same shape but
  the conclusion is independently true and experimentally established for
  adiponectin, so nothing turns on it.
* **PMID:10095105 is a non-confirmation of the projection hypothesis**: it has
  exactly **one** annotation in all of GOA — ADIPOQ's own `GO:0006091` `TAS`.
  It is not an import; it is a single idiosyncratic annotation, and it must be
  judged on whether the paper supports the term (it is a gene-structure paper:
  *"Organization of the gene for gelatin-binding protein (GBP28)"*).

## C. The `GO:0005515` set is one Y2H screen, counted five ways

| quantity | value |
|---|---|
| IntAct interactions for Q15848 | **286** |
| distinct publications | **7** |
| interactions from PMID:32296183 (HuRI) alone | **171** |
| two-hybrid interactions (all sub-methods) | **196** |
| partners appearing in exactly one publication | **240 of 264** |
| GOA `IPI` rows | 65 |
| distinct `GO:0005515` partners | **61** |
| partners cited as a non-canonical isoform accession | **13** |
| partners resolving to unreviewed (TrEMBL) entries | **0** |

The two-hybrid total is logged under **five separate sub-method names** —
`two hybrid array` (66), `validated two hybrid` (65),
`two hybrid prey pooling approach` (57), `two hybrid pooling` (4),
`two hybrid bait and prey pooling approach` (4). These are sub-methods of one
pipeline, which is why UniProt's `NbExp=3` appears on nearly every partner.
There is **no orthogonal biophysical assay** anywhere in the set: no SPR, no
ITC, no co-IP of endogenous protein.

**Topology.** Adiponectin has a cleaved signal peptide (`SIGNAL 1..18`) and its
mature chain is secreted; Y2H requires both partners to reconstitute a
transcription factor in the yeast **nucleus**, which the native protein never
enters. Six partners are additionally annotated to cytosolic/nuclear/
mitochondrial compartments *only* — SGTA, COQ9, HTT, FASN, MRM1, TRIM35 — and
so could not meet secreted adiponectin even if the assay were physiological.
This is a supporting observation, not the main argument: the primary objection
is the assay, which places **every** partner outside its native compartment.

**Negative results from this check, reported explicitly.** All 61 partners
resolve to reviewed Swiss-Prot entries with canonical lengths — no TrEMBL
clones and no partial ORFeome constructs of the sort found on ACRV1. Thirteen
are cited as specific isoform accessions, which is normal for ORFeome-based
screens and is not itself a defect.

**Partners that are *not* screen hits.** `PMID:12070119` (PDGFB, `P01127`) and
`PMID:16622416` (ADIPOR1, `Q96A54`) are directed, hypothesis-led experiments,
and ADIPOR1 carries the reciprocal `GO:0005515` `IPI` back to `Q15848`. They
are judged separately from the 59 screen partners.

## D. All four IBA rows are self-referential and every donor is experimentally grounded

| term | PANTHER node | donor tokens | resolved | with own experimental evidence for the term |
|---|---|---|---|---|
| `GO:0005179` hormone activity | `PTN008559544` | 2 | 2 | **2/2** |
| `GO:0005576` extracellular region | `PTN008355511` | 15 | 15 | **15/15** |
| `GO:0010642` neg. reg. PDGFR signaling | `PTN008559544` | 2 | 2 | **2/2** |
| `GO:0045599` neg. reg. fat cell differentiation | `PTN008559544` | 2 | 2 | **2/2** |

**21 of 21 donor tokens resolved; 21 of 21 carry their own experimental
evidence.** Every row's WITH/FROM includes `UniProtKB:Q15848` itself — these
are **self-referential IBAs**, which record a PAINT curator judging the
function core, and are valid by construction.

`MGI:` and `RGD:` tokens are rejected by QuickGO's `geneProductId` with HTTP
400, so they are resolved through UniProt's `xref:mgi-` / `xref:rgd-` indexes
(bare numeric id — a query containing MGI's inner colon returns 400) and the
fallback route is recorded per token in `results.json`. `MGI:MGI:106675`
resolves to `Q60994` `ADIPO_MOUSE`, the true mouse ortholog.

### PAINT node placement is correct here — hypothesis not confirmed

The campaign's node-placement hypothesis (a term attached to the wrong node)
was tested in both directions and **did not confirm**:

* `PTN008559544` reaches **exactly one human gene, ADIPOQ** — verified against
  all 82 human `GO:0005179` IBA rows, all 3 `GO:0045599` rows and the single
  human `GO:0010642` IBA row, each query fully paginated. An ortholog-specific
  node carrying ortholog-specific terms is correct placement.
* `PTN008355511` reaches **ADIPOQ, C1QA, C1QB, C1QC, C1QTNF2, C1QTNF5,
  C1QTNF7, C1QTNF9 and C1QTNF9B** and gives them `GO:0005576 extracellular
  region`. For a clade mixing complement C1q chains with the CTRP adipokines,
  the generic extracellular term *is* the LCA — refining it would mean picking
  one donor's compartment over another's.

Neither a misplaced term nor a mis-clustered member was found.

## F. Ontology relations the review's prose asserts, fetched and checked

Regulation is not subsumption in GO, and — less obviously — the **activity**
branch is not under the **binding** branch. Both traps were live in this
review's first draft. Every relation the prose depends on is now fetched,
recorded in `results.json` under `term_relations`, and asserted:

| child | ancestor | prose claims | GO says |
|---|---|---|---|
| `GO:0005179` hormone activity | `GO:0048018` receptor ligand activity | IS | IS |
| `GO:0005179` | `GO:0140677` molecular function activator activity | IS | IS |
| `GO:0005179` | `GO:0005102` signaling receptor binding | **is NOT** | **is NOT** |
| `GO:0048018` | `GO:0005102` | **is NOT** | **is NOT** |
| `GO:0005125` cytokine activity | `GO:0048018` | IS | IS |
| `GO:0042803` homodimerization | `GO:0042802` identical protein binding | IS | IS |
| `GO:0006635` beta-oxidation | `GO:0019395` fatty acid oxidation | IS | IS |
| `GO:0046321` pos. reg. FA oxidation | `GO:0019395` | is NOT | is NOT |
| `GO:0090336` pos. reg. brown fat diff. | `GO:0050873` | is NOT | is NOT |
| `GO:0010906` reg. glucose metabolism | `GO:0006006` | is NOT | is NOT |

**The correction this check was written for.** The first draft of the
`GO:0005102` rows argued that the term was merely the coarser grain of
`GO:0005179`, "which is a descendant of GO:0048018 receptor ligand activity,
which is a descendant of this term". The last clause is false. `GO:0048018`
sits under `GO:0140677 molecular function activator activity` →
`GO:0098772 molecular function regulator activity`, in the activity branch;
`GO:0005102` is a binding term under `GO:0005515`. Neither subsumes the other,
so the two rows are **not** redundant — they state different things (that
adiponectin physically engages a receptor, and that engaging it activates the
receptor), which strengthens the ACCEPT rather than weakening it.

Queries are `is_a,part_of` ancestor closures from QuickGO. The guard fails if
any observed membership disagrees with what the prose claims, and fails loudly
rather than vacuously if the assertion list is empty.

## E. The two cold-thermogenesis terms are a 2 x 2 citation cross-product

`GO:0120162` (**positive** regulation of cold-induced thermogenesis) and
`GO:0120163` (**negative** regulation of cold-induced thermogenesis) are
logical opposites. GOA cites **both terms to both** of the same two references:

| | PMID:24531262 | PMID:26166748 |
|---|---|---|
| `GO:0120162` positive | ISS | ISS |
| `GO:0120163` negative | ISS | ISS |

All four rows are `ISS` from `UniProtKB:Q60994`, all assigned by `YuBioLab`.
The detector reports `is_full_cross_product: true`.

This is a defect **independent of what the papers say** — the same evidence
cannot support a proposition and its negation. Reading the two abstracts
resolves which pairing is which:

* **PMID:24531262** (Diabetologia 2014) — *"Adiponectin reduces thermogenesis by
  inhibiting brown adipose tissue activation in mice"*; `Adipoq-/-` mice have
  **higher** core body temperature and **more** UCP1. Supports the **negative**
  term only.
* **PMID:26166748** (Cell Metab 2015) — *"Adiponectin Enhances Cold-Induced
  Browning of Subcutaneous Adipose Tissue"*; the thermogenic program is
  **impaired** in adiponectin-knockout mice. Supports the **positive** term
  only.

So two of the four rows are mis-paired with their reference
(`GO:0120162`/PMID:24531262 and `GO:0120163`/PMID:26166748), while the
remaining two are each correct. The underlying biological disagreement between
the two labs is genuine and unresolved; the annotation defect is separate from
it and is fixable without adjudicating the science.

---

## Summary of what each check decided

| check | outcome | verdicts it drives |
|---|---|---|
| A | 58 collapsed rows restored | coverage of all 161 rows |
| B | 2 bulk imports (272-entity and 41-entity) | `GO:0140149`, `GO:0005201` |
| B | 1 non-confirmation (PMID:10095105 is a singleton) | `GO:0006091` judged on content |
| C | 1 Y2H screen, 5 sub-method labels, 0 orthogonal assays | 59 `GO:0005515` rows |
| C | 2 directed experiments separated out | PDGFB, ADIPOR1 rows |
| D | 21/21 donors experimentally grounded, all self-referential | 4 IBA rows accepted |
| D | node placement correct — hypothesis not confirmed | no PAINT recommendation |
| E | full 2x2 cross-product | `GO:0120162`, `GO:0120163` |

## Limitations

* This check-set matches computable structure (counts, ids, compartments). It
  cannot tell whether a well-formed annotation is *biologically* apt; those
  judgements are argued in `ADIPOQ-ai-review.yaml` and `ADIPOQ-notes.md`.
* The projection test is unavailable for the three largest interactome
  references (85343, 20010 and 3269 annotations). Their screen-artifact status
  rests on the IntAct method census in section C, not on an entity count.
* Section C's compartment call uses UniProt `SUBCELLULAR LOCATION` plus signal-
  peptide/transmembrane features. For multipass membrane partners it does not
  distinguish which loop faces which side, so the six-partner
  "cytosol-only" figure is a floor, not a total.
