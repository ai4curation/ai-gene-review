---
title: "No Data (ND): what an ND annotation is telling us"
maturity: SCOPING
tags: [PIPELINE]
species: [yeast, SCHPO, DROME, CANAL, worm, DANRE, ARATH, human, mouse]
---

# No Data (ND): what an ND annotation is telling us

**Bottom line:** an ND annotation says that a curator searched the literature
for one GO aspect and found nothing to annotate. That is a statement about
**evidence for this gene product**, not about **knowledge**. The two diverge in
predictable ways. When this project started (2026-10-24), 361 ND rows sat in
237 gene reviews, and the same situation received different actions in different
reviews: for an ND
whose aspect also carried an IBA or ISO, reviews chose `ACCEPT` 36 times,
`REMOVE` 37 times and `KEEP_AS_NON_CORE` 13 times. Only 90 of the 237 genes
had any `knowledge_gaps`, and 62 accepted ND rows (51 genes) had nothing else in
their aspect and still no `BIOLOGY` gap. Current counts are in
[the inventory](NO_DATA/data/nd-summary.md). This project sorts ND rows into a
small set of cases. One rule fixes the action: **an ND that follows the
evidence-code guideline is `ACCEPT`**. It follows the guideline when no
literature on this gene product, in this species, identifies a function in that
aspect. Inferences (IBA, ISO, ISS, IEA) in the same aspect do not change this.
Only one case (a true gap) must also be paired with a `KnowledgeGap`.

## What ND means in GO

Two GO rules define it:

- **GORULE:0000011**, "ND evidence code should be to root nodes only, and no
  terms other than root nodes can have the evidence code ND" (hard filter). So
  an ND is always one of `GO:0003674` molecular_function, `GO:0008150`
  biological_process or `GO:0005575` cellular_component.
- **GORULE:0000054**, "Genes annotated with ND should have no other annotations
  for that aspect" (approved, soft report). Its text reads: "Use of the ND
  evidence code specifically indicates that a curator has looked but not been
  able to find information that supports making an annotation to any term from
  the Molecular Function, Biological Process, or Cellular Component as of the
  annotation date indicated." It adds that ND for one aspect "does not make any
  statement about the availability of knowledge or evidence in the other GO
  aspects."

Three consequences follow, and the cases below rest on them:

1. **ND is per aspect.** An MF ND next to rich BP annotations is the
   `MF_DARK` pattern from [Function Knowledge Gaps](FUNCTION_KNOWLEDGE_GAPS.md).
   It is not a contradiction.
2. **ND is dated.** "As of the annotation date" means an ND can go stale. The
   date is only informative if it records a real search. 108 of the 133 SGD ND
   rows in our corpus carry the same date (2013-08-07). That pattern looks like a
   bulk re-stamp, not 108 separate searches.
3. **ND is about literature for this gene product.** It is silent on
   inference. In practice a MOD's ND often coexists with a GO_Central IBA in
   the same aspect, though GORULE:0000054 reports this pairing. An IBA is not
   literature for the gene, so it does not make the ND wrong.

## The acceptance rule

We reward annotations that follow the evidence-code guidelines, and ND is no
exception. The test for an ND row is:

> Is there literature on **this gene product, in this species**, that would
> support a GO annotation in **this aspect** under the evidence-code guidelines
> (an IDA, IMP, IPI, IGI, IEP or similar that a curator would make)?

- **No** → the ND is correct: `ACCEPT`. This holds whether the aspect is empty
  or already carries IBA, ISO, ISS or IEA rows, and whether or not the function
  is obvious from orthologs.
- **Yes** → the ND is stale or missed (N1): `REMOVE`, and add the term the
  literature supports.

"Literature" means papers that identify a function, not any mention of the
gene. A screen hit, an expression change or a non-physiological in-vitro
reaction that a curator would not annotate leaves the ND correct (see N4).
A bare protein-binding IPI does not count either: it identifies no function,
which is why the protein-binding policy removes it. Papers on orthologs do not
count, however strong. Per CLAUDE.md, an accepted ND needs evidence that the literature was searched:
cite the deep-research file or the reviewer's own search, not the UniProt
`PE` line. The rows converted by the re-action pass below carry no such source
yet, because the pass searched nothing, so they do not earn the
`nd_search_support` credit; the metric therefore counts the searches still to
be recorded.

`ACCEPT` here endorses the annotation as made. It does not make a root term a
core function: `core_functions` never cite an ND row, and the function of an
N2 gene is carried by its informative IBA or ISO rows. `KEEP_AS_NON_CORE` is
not used for ND, and neither is `REMOVE` when an IBA appears in the same
aspect.

## Case taxonomy

The cases are ordered by how often they occur in our corpus and by how much
they matter. Each case answers one question: *if the ND is true, why is there
no data?*

| Case | Short name | Is the ND true? | Knowledge gap? | Proposed action |
|---|---|---|---|---|
| N1 | Stale or missed | No: data exist | No (curation) | `REMOVE`, and add the informative term |
| N2 | Not assayed here, inferable | Yes | No | `ACCEPT` |
| N3 | Existence in question | Yes | Yes, of a special kind (does the product exist?) | `ACCEPT`, defer to MICROPROTEINS |
| N4 | True knowledge gap | Yes | **Yes, `BIOLOGY`**, required | `ACCEPT` and a `KnowledgeGap` |
| N5 | Ontology-blocked | No: literature identifies the function | No (ontology) | `MODIFY` to the term, or a proposed term |
| N6 | Tested and negative | Yes | No (or a narrower gap) | `ACCEPT`, and keep the NOT row |
| N7 | Bookkeeping artifact | Unclear | Decide after reading | Re-check, then reclassify |

### N1 — Stale or missed: data now exist

The ND was true on its date and is no longer true, or the search missed a paper.
GORULE:0000054 already flags the conflict when the new data have been
annotated. When they have not, the review finds the paper and the gap becomes
a curation gap.

- Annotated since: yeast/MDM10 (ND MF dated 2022, yet the gene has an IDA for
  ER–mitochondrion tether activity), mouse/Capsl (a 2024 knockout gives
  IMP evidence for process terms), human/AMTN (hydroxyapatite binding).
- Not yet annotated: ARATH/MLO2 (calcium channel activity, proposed as `NEW`),
  SCHPO/knh4 (a 2021 paper supports a cell-wall process).

**Action:** `REMOVE`. Here REMOVE is used in its normal sense: the claim "no
data exist" is now false. Add the informative term (as `NEW` if it is missing
from GOA). Do not create a knowledge gap. If GOA still has the ND after the
MOD has annotated the aspect, the ND is a candidate `source_defects` report.

### N2 — Not assayed here, but obvious from orthologs

An enzyme, transporter or complex subunit whose direct orthologs are well
characterised and whose function no one has re-assayed in this species. The ND is
true, because nothing was published on *this* gene product. The function is
nonetheless known by any reasonable standard, and IBA, ISO or ISS rows usually
carry it already. This is not a knowledge gap: no wet-lab experiment would tell
us anything new, beyond "confirm it in species X".

Examples: CANAL/LPL1 (phospholipase B, inferred from the *S. cerevisiae*
branch), CANAL/ERG2, CANAL/MON1 and DANRE/gmppb. The inventory signal
`inferable_by_homology` marks 106 rows, and most of them belong to this case.

**Action:** `ACCEPT`. Nothing was published on this gene product in this
species, so the ND follows the guideline. The informative IBA or ISO carries the
function, and is reviewed on its own row. The ND records that the function is
unverified in this species. Do not add a `KnowledgeGap`. `REMOVE` is wrong: 37
reviews removed an ND for this reason alone ("superseded by the IBA"), which
penalises a correct annotation.

**Subcase N2b — the family is known but the specificity is not.** If the
ortholog assignment is ambiguous (paralog-rich family, possible pseudoenzyme,
substrate range that differs between subfamilies), the function is *not*
obvious. yeast/SIA1 (possibly a pseudophosphatase) is the type example. This
subcase belongs in N4 with `dark_aspect: RESIDUAL_SUBGAP` or `MF_DARK`. The
test is the IBA one in `projects/IBA_REVIEW.md`: is the target inside the clade
that inherited the function?

### N3 — Existence in question: microproteins and dubious ORFs

The basic unknown is whether a functional gene product exists at all:
sORF peptides, uORF and alternative-frame products, yeast "dubious" and
"putative" ORFs, and lineage-restricted ORFs without homologs. See
[Microproteins](MICROPROTEINS.md) and the `just fetch-gene --alias` rule for
alternative-ORF folders. Example: human/P3R3URF.

A length filter does **not** identify this case. The inventory's ≤100-aa flag
also catches yeast/SMX2 (an Sm protein) and yeast/COA4, which are canonical,
well-conserved short proteins and fall in N2 or N4. The MICROPROTEINS census
found the same split.

**Action:** `ACCEPT`. Where translation or conservation evidence
exists but function does not, the gene gets a `BIOLOGY` gap whose
`gap_statement` puts the existence question first.

### N4 — True knowledge gap

Nobody knows. The review has read the literature and the deep research and
confirms that no experiment, and no defensible inference, assigns a term in this
aspect. **Action:** `ACCEPT`. Only this case should be coupled to
`knowledge_gaps`. The coupling should be mandatory:

| ND aspect | Required `KnowledgeGap.dark_aspect` |
|---|---|
| MF | `MF_DARK` (or `WHOLLY_DARK`) |
| BP | `BP_DARK` (or `WHOLLY_DARK`) |
| CC | `CC_DARK` (or `WHOLLY_DARK`) |
| all three | `WHOLLY_DARK` |

The gap also has `gap_kind: [BIOLOGY]` and a `provenance` quote showing that the
unknown is real. Reading the existing reviews turns up recurring sub-flavours.
They are worth recording in `gap_statement` because each points to a different
experiment:

- **Orphan:** no homologs to infer from (SCHPO/tam10).
- **Phenotype only:** screen hits or knockout phenotypes, with no mechanism. This
  is necessity evidence, which per CLAUDE.md is not participation
  (yeast/IRC24, an increased-Rad52-foci deletion phenotype from a screen).
- **Non-physiological activity only:** an in-vitro activity whose biological
  role is unclear (yeast/NRE1, benzil reduction). Typically MF is known and BP
  is dark.
- **Partners only:** binding partners are known but no activity is
  (DANRE/samsn1b, worm/abu-1, ARATH/CASPL4C1).

### N5 — Ontology-blocked: the function is known but GO cannot say it

Structural or accessory subunits whose function is "be part of machine X" often
get an MF ND because no MF term fits, even though literature on the gene
identifies its role. Under the acceptance rule that literature makes the ND
incorrect. That accounted for about 64% of the conserved
"MF-dark" genes in the Function Knowledge Gaps triage (worked example:
human/POLE4). No ND row in the corpus is classified N5 yet. DROME/Vps53 looks
like one, but the tethering literature behind it is on human EARP, so under the
rule its ND is N2 and the tethering activity sits on its own inferred row.

**Action:** `MODIFY` to the expressible term (a `contributes_to` complex
activity or a `structural constituent` term). If none exists, MODIFY to an
`NTR` and add a matching `proposed_new_terms` entry. Per CLAUDE.md, an
ONTOLOGY-only `knowledge_gaps` entry is not allowed.

### N6 — Tested and negative

The function people expected was tested and ruled out. **Action:** `ACCEPT`:
a negative result identifies no function. The ND then sits next to a `NOT`
row, as for SCHPO/alo1: the positive ISO to D-arabinono-lactone
biosynthesis was withdrawn and PomBase now carries `NOT` IGC for that process. The
ND is honest, but the aspect is not empty: the NOT row is information. If an
alternative function is plausible but unknown, record an N4 gap with the
negative result as its `boundary`.

### N7 — Bookkeeping artifact

The ND reflects how the record was handled, not a search. Signs:

- bulk dates (above);
- paralog asymmetry, where one paralog has the ND and its sibling does not "only
  because of how the two records were processed" (DANRE/samsn1b against
  samsn1a);
- an ND older than the gene's earliest relevant paper.

These are not a separate biological category. Re-check the ND and reclassify it
into N1–N6, then record the provenance issue in the notes.

### Considered and folded in

- **Contested function** ([Function Knowledge Gaps](FUNCTION_KNOWLEDGE_GAPS.md),
  "fourth kind"): conflicting data are still data, so a contested gene
  should not carry an ND for that aspect. If it does, treat the ND as N1.
- **Inaccessible literature:** that is `UNDECIDED` on the *other* rows, not a
  property of the ND.

## Current state of the corpus

From [the inventory](NO_DATA/data/nd-summary.md)
(`uv run python projects/NO_DATA/scripts/nd_inventory.py`), regenerated with
each change to this project; on 2026-10-31 it counted 427 ND rows in 268 reviews. A bare protein-binding
IPI is not counted as experimental (it identifies no function).

| Provisional signal | ND rows | Likely case(s) |
|---|---:|---|
| `aspect_empty` (nothing else in the aspect) | 216 | N4, N3, some N1 (missed) |
| `inferable_by_homology` (IBA/ISO/ISS present, no experimental) | 118 | N2, N2b→N4 |
| `electronic_or_author_only` (incl. bare protein-binding IPIs) | 52 | N2 or N4, needs reading |
| `short_orf/*` (≤100 aa) | 34 | N3, or canonical short proteins |
| `coexists_with_experimental` | 7 | N1 |

The signals come from GOA alone and are only for triage. As in Function
Knowledge Gaps, the case is decided by reading the literature, not by a pattern
in the annotations. Actions are currently inconsistent within each signal (see
the signal × action table in the summary). One example is the 4 `NEW` ND rows
(SCHPO/tam10 ×2, human/P3R3URF, MYCTU/Rv0898c), where reviewers used `NEW`
ND to *assert* a gap. ND is the contributing group's statement about its own
search, so we cannot meaningfully propose one. These rows should become
`knowledge_gaps` entries.

## Coupling to knowledge gaps (implemented)

1. **Schema.** `review.nd_case` (`NoDataCaseEnum`: `STALE`, `INFERABLE`,
   `EXISTENCE`, `TRUE_GAP`, `ONTOLOGY_BLOCKED`, `NEGATIVE`) records why an ND
   row has no data. Bookkeeping artifacts (N7) are re-checked and given one of
   these values. The `ACCEPT` description now says what ACCEPT means on an ND
   row.
2. **Validation** (`nd_policy`, best-practice warnings):
   - `KEEP_AS_NON_CORE`, `MARK_AS_OVER_ANNOTATED` or `TOO_GENERAL` on an ND;
   - `REMOVE` or `MODIFY` on an ND without `nd_case` `STALE` or
     `ONTOLOGY_BLOCKED`, which catches removal "because an IBA exists";
   - `ACCEPT` with `nd_case` `STALE` or `ONTOLOGY_BLOCKED`, or with
     `proposed_replacement_terms`;
   - `NEW` on an ND row (record a `knowledge_gaps` entry instead);
   - `nd_case` `TRUE_GAP` or `EXISTENCE` without a `BIOLOGY` gap whose
     `dark_aspect` matches the ND aspect (`MF_DARK`, `BP_DARK` or `CC_DARK`,
     or `WHOLLY_DARK`), on the row, the gene or a core function;
   - `nd_case` on a non-ND row;
   - `ACCEPT` without evidence that the literature was searched: the row must
     cite a publication (PMID, DOI, PMC) or the deep-research file. The UniProt
     record, or its protein-existence (`PE`) line, is not a search. On
     2026-11-01 this flags 208 of 311 accepted ND rows in 147 reviews; 197 of
     them cite nothing, mostly rows the re-action pass converted.
3. **Compliance** (`qc_config.yaml`, the evidence-code × action rule table):
   `nd_search_support` credits an `ACCEPT`ed ND that gives a reason and cites
   a source for the literature search (e.g. the deep-research file). The pass
   adds no such citation itself: the credit is for a search a reviewer records,
   so the rows the pass converted score 0 until one is.
   `nd_stale_support` credits a `REMOVE`d or `MODIFY`d ND only for a PMID/DOI
   quote from the literature that makes it stale.
4. **Upstream (to do).** N1 rows where the MOD has already annotated the aspect
   are GORULE:0000054 conflicts. They can go to `source_defects` and on to the
   per-resource reports. N7 bulk-date clusters are a question for the MOD,
   not a defect.

## Re-action pass

The decisions are in [`data/nd-decisions.yaml`](NO_DATA/data/nd-decisions.yaml),
one entry per ND row the pass changed, and
`scripts/apply_acceptance_rule.py` applies them. They were made by reading each
row and the review's other rows in the same aspect (2026-10-24, extended on
2026-10-26 to reviews merged from main, and re-checked on 2026-10-31 after
review), **not by a new literature search**, and the generated text says so.
The script restores each row as it was before the pass, then edits only that
row's review block, so it can be re-run. The pre-pass rows are read from git,
so re-running needs those commits to be reachable; after a squash merge it can
no longer restore them.

- **66 rows keep `REMOVE`/`MODIFY` with `nd_case: STALE`**: the review cites
  literature on this gene product in this species (e.g. yeast/MDM10,
  mouse/Capsl, ARATH/MLO2, DANRE/elna, human/ARL15, mouse/Rtl5).
- **108 rows changed to `ACCEPT`**: 48 `REMOVE` (mostly "superseded by the
  IBA"), 30 `KEEP_AS_NON_CORE`, 25 `MODIFY` to an inferred term, 4
  `TOO_GENERAL` and 1 `MARK_AS_OVER_ANNOTATED`. Each gets a reason that names
  the earlier action and says the judgement came from the review's own
  content. The earlier summary is kept unless it argued for the replacement
  (every converted `MODIFY`) or said the ND was obsolete; those 69 summaries
  are replaced with a neutral one. `nd_case` is `TRUE_GAP` where the review has a
  matching `BIOLOGY` gap, `INFERABLE` where a retained inferred row covers the
  aspect, and unset otherwise.
- **Quotes.** A converted row loses its earlier `supported_by`: those quotes
  argued for the earlier action (a replacement term, or that the ND was
  obsolete), so none of them supports the `ACCEPT`, and none should earn the
  `nd_search_support` credit. A converted `MODIFY` also loses its
  `proposed_replacement_terms`: if the review already has a row for the term,
  nothing more is needed; if not (`new_row` in the table), the term becomes its
  own `NEW` row carrying the earlier quotes. A `NEW` row inherits the earlier
  reasoning only when the `MODIFY` proposed that one term, and never its
  sentences about the ND row or the earlier action. 14 `NEW` rows were made this way,
  e.g. DROME/Vps50, Vps51, Vps53 `contributes_to` vesicle membrane tethering
  and mouse/Sdhaf2 protein folding chaperone.
- **Judgement calls (agreed 2026-10-24, now in CLAUDE.md).** Bare
  protein-binding IPIs do not count as literature that identifies a function
  (yeast/CRT10, human/TIMM21 stay `ACCEPT`), and neither do papers on orthologs
  (yeast/COQ4, whose decarboxylase paper is not on yeast; DROME/Tango5, from
  human VMP1). `NAS` and Reactome `TAS` rows on the gene count (DROME/Kpc1,
  human/TAT). Background statements in a same-species paper do not count
  (SCHPO/apc2, mouse/Rtl3), nor does necessity without an activity
  (DANRE/lhfpl5b).
- **Same-species data that cannot be assigned to a paralog** (mouse/Rtl8c:
  the mouse UBQLN2-RTL8 interaction does not resolve Rtl8a, Rtl8b or Rtl8c) is
  not literature on this gene product. The ND stays and the inferred terms rest
  on the human ortholog (`ISO`).
- **Re-check on 2026-10-31.** Three earlier `ACCEPT` calls were reversed to
  `STALE`: human/ASNSD1 MF (the review refines the human IPIs to PDZ domain
  binding) and yeast/THI11 and THI12 MF (PMID:12777485 shows in yeast that each
  paralog alone supports HMP formation). The pass then also read each review's
  `core_functions`, where same-species evidence often sits: four more rows
  became `STALE` (yeast/FSH3 MF, activity-based proteomics; yeast/KDX1 BP and
  CC, Mlp1 at the FKS2 promoter; yeast/PTM1 CC, Golgi immunoisolation), and
  each of the other 50 accepted rows whose core functions cite a paper has a
  `note` saying why that paper does not make the ND stale (another species,
  another aspect, or background). The script reports any accepted row with
  such a citation and no `note`.
- **Left alone:** 4 `UNDECIDED` rows, and 4 `NEW` ND rows (SCHPO/tam10 ×2,
  MYCTU/Rv0898c, human/P3R3URF), which need knowledge gaps written by
  reading before the row can go.

**Not yet swept (as of `04e2ffa3e`).** Reviews merged from main after the last
pass carry 42 ND rows that `nd_policy` flags: 37 `MODIFY` rows in 13 mouse
keratin-associated protein reviews (Krtap3-2 to Krtap29-1), whose reasons rest
on family-level literature; human/CDKAL1 BP; ARATH/PGR3; and rat Actl7a, Aph1a
and Pik3c2a. They are waiting for a decision.

## Plan

- [x] Inventory script and summary ([data](NO_DATA/data/nd-summary.md))
- [x] Agree on the action per case: guideline-conformant ND is `ACCEPT`
- [x] Add `nd_case` to the schema, `nd_policy` warnings, ND compliance rules
- [x] Re-action pass (above)
- [ ] Decide the 42 unswept rows from main (above)
- [ ] Classify the 217 `ACCEPT` rows with no `nd_case` by reading (counted in
      the inventory's `nd_case` table); gap-less `aspect_empty` rows are
      expected to be N4 and gain `BIOLOGY` gaps
- [ ] Replace the 4 `NEW` ND rows with `knowledge_gaps` entries
- [ ] N1 upstream report from `source_defects`

## Open questions

- **N2 against GORULE:0000054.** The rule reports an ND next to an IBA. This
  project accepts both, by decision (2026-10-24), because the ND correctly says
  that no literature exists for this species. Raising it with GO as a
  clarification of the rule is still to do.
- **Is N3 a kind of knowledge gap or its own kind?** An existence question
  could justify a new `KnowledgeGapAspectEnum` value (e.g. `EXISTENCE_DARK`)
  rather than overloading `WHOLLY_DARK`.
