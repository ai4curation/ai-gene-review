---
title: "Endosome to Plasma Membrane Protein Transport (GO:0099638) — Obsoletion & Merge into Endocytic Recycling"
maturity: SCOPING
tags: [OBSOLETION]
species:
  - human
  - mouse
  - SCHPO
genes:
  - LMTK3
  - RAB7A
  - SORL1
  - ATP6AP1
  - ALDH7A1
  - vas2
  - AP1S1
  - AP1S3
  - AP2S1
  - AP3S1
  - AP4S1
---

# Endosome to Plasma Membrane Protein Transport (GO:0099638) — Obsoletion & Merge into Endocytic Recycling

## Overview

A four-term GO obsoletion merges the **`GO:0099638` endosome to plasma membrane
protein transport** branch into the **`GO:0032456` endocytic recycling** branch.
Every obsoleted term has a direct `replaced_by`, and every replacement is a
**generalisation**, so no annotation is invalidated:

| obsoleted | replaced_by |
|---|---|
| GO:0099638 endosome to plasma membrane protein transport | GO:0032456 endocytic recycling |
| GO:1905749 regulation of endosome to plasma membrane protein transport | GO:2001135 regulation of endocytic recycling |
| GO:1905750 negative regulation of endosome to plasma membrane protein transport | GO:2001136 negative regulation of endocytic recycling |
| GO:1905751 positive regulation of endosome to plasma membrane protein transport | GO:2001137 positive regulation of endocytic recycling |

The stated reason is that GO:0099638 duplicated GO:0032456, differing only by a
protein-cargo restriction that GO:0032456's logical definition does not carry;
the reasoner already classified GO:0099638 underneath it. The three regulation
children follow necessarily.

**This is not settled.** See "Status" below — the obsoletion PR merged on
2026-09-19 and the ontology thread reopened the same morning with a request to
reverse it. Nothing in this repo should be edited yet.

## Upstream tickets

- Annotation tracker: [geneontology/go-annotation#6557](https://github.com/geneontology/go-annotation/issues/6557)
  — *"Review annotations to GO:0099638 endosome to plasma membrane protein
  transport & regulation children"* (OPEN, opened 2026-09-18; labels
  `annotation review`, `reg_ann_to_list_of_terms`). Impacted groups: UniProt 14,
  MGI 8, PomBase 7, SGD 3, FlyBase 2, RGD 1, TAIR 1. The issue notes that
  **no InterPro2GO, UniProt-Keyword or UniRule mapping** targets any of the four
  terms, so there is no KW2GO/ARBA follow-on.
- Ontology ticket: [geneontology/go-ontology#31237](https://github.com/geneontology/go-ontology/issues/31237)
  — *"Term merge: GO:0032456 endocytic recycling and GO:0099638 endosome to
  plasma membrane protein transport"* (OPEN, opened 2025-12-18).
- Obsoletion PR: [go-ontology#32639](https://github.com/geneontology/go-ontology/pull/32639),
  **MERGED 2026-09-19T00:01Z**.
- Superseded PR: [go-ontology#32631](https://github.com/geneontology/go-ontology/pull/32631)
  (CLOSED, not merged) — would have kept both terms and instead broadened
  GO:0032456's *text* definition to match its cargo-agnostic logical definition.

### Status: merged upstream, and contested the same day

Worth reading the ontology thread before acting, because the decision has
already reversed once and is being questioned again:

1. **2026-09-18** — an analysis posted to the ticket argued *against* the merge:
   GO:0099638 is an inferred **child**, not a duplicate, and carries parentage
   GO:0032456 lacks (`protein localization to plasma membrane`, `establishment
   of protein localization to plasma membrane`, `intracellular protein
   transport`). It cited `GO:0006893 Golgi to plasma membrane transport` /
   `GO:0043001 Golgi to plasma membrane protein transport` as a structurally
   identical pair that is *not* merged. PR #32631 implemented that position.
2. **2026-09-18** — Pascale Gaudet countered that the single-child pattern is
   itself suspicious: if no sibling for non-protein cargo can be justified, the
   child should merge up. Val Wood agreed the two concepts are safe to merge
   *given current definitions and usage*, and added that she is not troubled by
   losing the protein-localization parentage because she expects those terms to
   be obsoleted eventually anyway.
3. **2026-09-19T00:01Z** — PR #32639 merged; the obsoletion is in `go-edit.obo`.
4. **2026-09-19, hours later** — Val Wood asked to **de-merge and make the two
   terms siblings**, on the grounds that neither subsumes the other: endosome-to-PM
   routes exist that are not recycling (MVBs fusing with the plasma membrane to
   release intraluminal vesicles), and "endocytic recycling", properly defined,
   would also include the inbound internalization step. Ruth Lovering asked in
   the same thread what becomes of UCL's two IDA annotations to
   `GO:0099639 neurotransmitter receptor transport, endosome to plasma membrane`;
   Val Wood's answer was that GO:0099638 should be kept so that GO:0099639 can
   stay under it.

So the live question is not "how do we apply this merge" but "does the merge
survive". **All eight terms are still active in the released ontology** (OLS,
checked 2026-09-19), so nothing in this repo is broken today.

## Terms verified (OLS, 2026-09-19 — all eight active, all `biological_process`)

| GO id | Label | Definition (abridged) |
|---|---|---|
| GO:0099638 | endosome to plasma membrane protein transport | "The directed movement of proteins from the endosome to the plasma membrane in transport vesicles." |
| GO:0032456 | endocytic recycling | "The directed movement of membrane-bounded vesicles from endosomes back to the plasma membrane, a trafficking pathway that promotes the recycling of internalized transmembrane proteins." |
| GO:1905749 | regulation of endosome to plasma membrane protein transport | modulates frequency/rate/extent of GO:0099638 |
| GO:2001135 | regulation of endocytic recycling | modulates frequency/rate/extent of GO:0032456 |
| GO:1905750 | negative regulation of endosome to plasma membrane protein transport | — |
| GO:2001136 | negative regulation of endocytic recycling | — |
| GO:1905751 | positive regulation of endosome to plasma membrane protein transport | — |
| GO:2001137 | positive regulation of endocytic recycling | — |

Note that GO:0032456's released definition is still the **protein-restricted**
one quoted above — the broadening in PR #32631 was never merged. If the merge
stands, the surviving term's text definition and its cargo-agnostic logical
definition remain out of step, which is the mismatch that started the ticket.

## Annotation footprint (QuickGO, 2026-09-19)

| term | exact annotations | evidence split |
|---|---|---|
| GO:0099638 | **939** | IEA 717, IBA 163, ISS 20, IMP 19, ISO 12, IDA 8 |
| GO:1905749 | **0** | — (a regulation term with no direct annotations at all) |
| GO:1905750 | **45** | IBA 26, IEA 9, ISS 6, ISO 2, IMP 2 |
| GO:1905751 | **86** | IEA 75, IMP 5, ISO 4, ISS 2 |

GO:0099638's `assignedBy` split is Ensembl 359, EnsemblFungi 334, GO_Central
166, UniProt 27, EnsemblMetazoa 24, RGD 10, PomBase 7, MGI 6, SGD 3, FlyBase 2,
TAIR 1 — i.e. **roughly 76% of the footprint is Ensembl/EnsemblFungi orthology
projection** that regenerates from the MOD seeds each release and needs no
individual attention.

The two regulation terms have disjoint, single-seed fan-outs:

- **GO:1905750** is mostly a *plant* IBA cloud (26 rows across *Brassica*,
  *Medicago*, *Populus*, *Glycine*, *Prunus*, *Vitis*, …) seeded by the two
  *Arabidopsis* SHOU4/SHOU4L IMPs (PMID:30245104), plus a separate ALDH7A1
  ortholog ISS/ISO set (8 rows, all citing `P49419-2` as WITH/FROM).
- **GO:1905751**'s manual content is exactly the five IMPs the upstream issue
  lists: human AKAP5, mouse `Commd1`, rat `Zdhhc2`, and *C. elegans* `arf-6` and
  `cnt-1`.

### Two of the 36 experimental rows are invisible to QuickGO

The upstream issue lists **36 EXP annotations**. QuickGO returns **27** EXP-code
rows for GO:0099638 (against the issue's 28) and **2** IMPs for GO:1905750
(against the issue's 3). The two missing rows were chased down individually and
**both exist in the GO release** — they are retrievable from
`api.geneontology.org` but not from QuickGO:

| row | present in GO release | QuickGO |
|---|---|---|
| mouse `Mfsd8` · GO:0099638 · IMP · PMID:30301600 (MGI) | yes — `MGI:MGI:1919425` returns it among 81 associations | absent; QuickGO has 73 rows for Q8BH31, none of them GO:0099638, and **zero rows citing PMID:30301600 at all** |
| human ALDH7A1 · GO:1905750 · IDA · PMID:31492851 (UniProt) | yes — `UniProtKB:P49419` returns it among 76 associations | absent; QuickGO has 48 rows for P49419 and 6 rows citing PMID:31492851, none of them this one |

The cause was not determined here (it is not an isoform-visibility artefact in
the `Mfsd8` case, since the reference returns nothing at all). **The consequence
for this repo is concrete**: `GENE-goa.tsv` files are fetched from the QuickGO
API, so a review built from one can silently lack rows the GO release carries —
see the ALDH7A1 entry under "Tier 3" below, where exactly this happened. Both
discrepancies are worth reporting upstream, independently of the obsoletion.

## Impact on this repo

Eleven reviews reference one of the four terms. **None of them also carries the
corresponding replacement term**, so this is a clean re-terming everywhere — no
review will end up with a redundant ancestor/descendant pair.

### Tier 1 — one review breaks strict validation, and it is a `NEW` proposal

`genes/human/LMTK3/LMTK3-ai-review.yaml` is the only file with `core_functions`
exposure. It uses **GO:1905750** twice:

- as an `existing_annotations` row (IMP, PMID:28294115, with an `RO:0002233
  has input` extension naming EPHA2) whose action is **`NEW`** — i.e. this repo
  is *proposing to add* an annotation to a term that is being retired;
- as `core_functions[].directly_involved_in`, which **is** bound to
  `GOBiologicalProcessEnum` in the schema (`gene_review.yaml:1513-1520`,
  `obligation_level: REQUIRED`), alongside `molecular_function`, `locations` and
  `in_complex`.

`just validate human LMTK3` passes today (checked 2026-09-19). It should be
expected to fail on the `core_functions` entry once the obsoletion reaches the
ontology release used for validation. The fix is a one-for-one swap to
**GO:2001136 negative regulation of endocytic recycling**; the underlying
biology (LMTK3 phosphorylating RAB11FIP1/RCP Ser435 to divert EPHA2 into a
slower RAB14 route, reducing its return to the surface) is unaffected, and the
`NEW` action and its `has input` extension carry over unchanged.

### Tier 2 — `existing_annotations` rows, no `core_functions` exposure

| Review | Term | Ev | Reference | Current action |
|---|---|---|---|---|
| `genes/human/RAB7A` | GO:0099638 | IMP | PMID:33147445 | KEEP_AS_NON_CORE |
| `genes/human/SORL1` | GO:0099638 | IEA | GO_REF:0000107 | ACCEPT ("core recycling route") |
| `genes/human/ATP6AP1` | GO:0099638 ×2 | IEA, ISS | GO_REF:0000107, GO_REF:0000024 | KEEP_AS_NON_CORE ×2 |
| `genes/SCHPO/vas2` | GO:0099638 | IDA | PMID:19624755 | ACCEPT |
| `genes/mouse/Rab7` | GO:0099638 ×2 | ISO, ISS | GO_REF:0000119, GO_REF:0000024 | KEEP_AS_NON_CORE ×2 |

Two of these are rows the upstream issue is asking MODs to review directly:
**human RAB7A** (UniProt's IMP, PMID:33147445) and **SCHPO/vas2** (one of
PomBase's seven, PMID:19624755). PomBase is flagged in the upstream table with
"**no automatic replacement**", so the seven fission-yeast rows — `apl2`,
`apl4`, `apm1` ×2, `chc1`, `vas2`, `ypt3` — are the ones most likely to change
shape rather than just change id. Only `vas2` has a review here.

**SORL1 is the interesting one.** It already carries `GO:2001137 positive
regulation of endocytic recycling` (IMP, PMID:22621900, `ACCEPT`, and promoted
into `core_functions[].directly_involved_in`) *alongside* the GO:0099638 IEA.
After the merge it would hold both `GO:0032456` and its positive-regulation
child — which is not redundant (regulating a process is not the same as doing
it), but the two review rows currently justify themselves in nearly identical
prose ("core recycling route" / "core recycling-promoting activity") and should
be reconciled into one story when they are re-termed. Mouse `Sorl1` is also in
the upstream EXP list (IDA, PMID:27322061) and is the subject of a cached GO-CAM
(below); there is no `genes/mouse/Sorl1` review here.

### Tier 3 — a row that never made it into the review

`genes/human/ALDH7A1/ALDH7A1-ai-review.yaml` does **not** mention GO:1905750,
because `ALDH7A1-goa.tsv` (fetched 2025-10-27) does not contain it — the
QuickGO gap documented above. The GO release does carry
`ALDH7A1 · GO:1905750 · IDA · PMID:31492851`, and the review already discusses
that paper (for the Golgi-membrane and plasma-membrane localizations it *did*
receive, treated as "stress-induced membrane recruitment ... real but
non-core"). So there is a genuine missing annotation here, on a term that is
being obsoleted, and the review's existing reasoning about PMID:31492851 is the
right place to decide whether `GO:2001136` belongs. Eight ortholog ISS/ISO rows
(zebrafish, rat, mouse, bovine, *Xenopus*, …) hang off this one human
annotation.

### Tier 4 — prose mentions only, non-blocking

Five AP-complex sigma-subunit reviews cite GO:0099638 inside IBA
`source_status` commentary, all describing the same donor — *S. pombe* `vas2`
(PomBase:SPAP27G11.06c / Q9P7N2) "carries GO:0042147 and GO:0099638 by IDA
(PMID:19624755)": `genes/human/AP1S1`, `genes/human/AP1S3`,
`genes/human/AP2S1`, `genes/human/AP3S1`, `genes/human/AP4S1`. AP1S1 also
carries it in a `reference_review.review_notes` for PMID:19624755. These go
stale rather than invalid; reword when the donor's own annotation is re-termed.

`projects/DELIVEROME.md` lists GO:0099638 in a route table ("Recycling to
surface") and needs the same one-line swap.

### Tier 5 — cached GO-CAM models

Two production models use GO:0099638 as a `part_of` biological-process context.
Neither has a `-review.yaml` yet, and both are read-only caches that will be
refreshed upstream:

| Model | Title | Where |
|---|---|---|
| `gocams/62f58d8800001119/` | Insulin receptor recycling (Mouse) | on the mouse `Sorl1` activity (MGI:MGI:1202296), the PMID:27322061 IDA from the upstream list; also in `gocams/index.tsv` |
| `gocams/69729a3800001528/` | CD36 transport to the plasma membrane for muscle regeneration (Human) | a `part_of` context in the model built on PMID:38198890 — the same paper as UniProt's mouse `Stx11` IMP in the upstream list |

## The LMTK family is the reason to want this merge

Three LMTK paralogs already have reviews here, and each landed on a *different*
term in the same small corner of the ontology:

| Gene | Term | Ev | Action | In `core_functions`? |
|---|---|---|---|---|
| LMTK1 | GO:2001135 regulation of endocytic recycling | ISO (PMID:24672056) | NEW | yes (`directly_involved_in`) |
| LMTK2 | GO:0032456 endocytic recycling | IBA + IMP (PMID:18029400) | ACCEPT | — |
| LMTK3 | GO:1905750 neg. reg. of endosome to PM protein transport | IMP (PMID:28294115) | NEW | yes (`directly_involved_in`) |

LMTK2's review additionally contains a `MODIFY` whose
`proposed_replacement_terms` is GO:0032456 (replacing a wrong-destination late-endosome
term). So this repo has independently converged on the `GO:0032456` /
`GO:2001135` family for two of the three paralogs, and picked the branch being
obsoleted for the third — for no biological reason, only because that is where
the cargo-specific term happened to sit. Post-merge the three paralogs read as
one coherent family: the process, its regulation, and its negative regulation.
That is a point worth making on the upstream ticket in favour of the merge,
against the de-merge request.

## Scope

- **Organisms with reviews here**: human (LMTK3, RAB7A, SORL1, ATP6AP1,
  ALDH7A1, AP1S1, AP1S3, AP2S1, AP3S1, AP4S1), mouse (`Rab7`), *S. pombe*
  (`vas2`).
- **Organisms in the upstream EXP list without reviews here**: *D. melanogaster*
  (`Vps26`, `Vps35`, `Rab35`), *S. cerevisiae* (`CDC48`, `IST1`, `NPL4`),
  *A. thaliana* (`BRO1`, `SHOU4`, `SHOU4L`), *C. elegans* (`arf-6`, `cnt-1`),
  rat (`Snx27`, `Zdhhc2`), and most of the mouse set. Note that
  `genes/human/VCP` and `genes/human/NPLOC4` exist and are the orthologs of the
  SGD `CDC48`/`NPL4` rows, but neither carries any of the four terms.
- **GO branch**: BP only. A four-term obsoletion with direct `replaced_by` on
  every term, every replacement a generalisation.
- **Type of fix in this repo's vocabulary**: `MODIFY` with
  `proposed_replacement_terms`, or a plain id+label swap where the row's action
  and reasoning are unchanged. **Not `REMOVE`** — no annotation is invalidated,
  which is the whole point of a replaced obsoletion. For LMTK3's `NEW` row, the
  proposal simply re-points to GO:2001136.
- **Not in scope**: the surviving descendants `GO:0099639 neurotransmitter
  receptor transport, endosome to plasma membrane`, `GO:0098887` and
  `GO:0099152`, which reparent automatically and are unused in this repo. Also
  out of scope: the `GO:0006893` / `GO:0043001` Golgi-to-PM pair, which has the
  identical general/protein-specific structure and is *not* being merged — if
  the GO:0099638 merge stands, that pair becomes the obvious next question.

## Candidate genes for initial review

Confirm accessions with `just fetch-gene <organism> <gene>` before starting.

### Tier 1 — do first when the obsoletion lands

1. **LMTK3** (human, Q96Q04) — `genes/human/LMTK3/`. The only strict-validation
   breakage, and the only `NEW` proposal pointing at a doomed term. Swap
   GO:1905750 → GO:2001136 in both the `existing_annotations` row and
   `core_functions[].directly_involved_in`, then re-run `just validate human
   LMTK3`. Worth doing together with **LMTK1** and **LMTK2** so the family reads
   consistently.

### Tier 2 — re-term plus a prose reconciliation

2. **SORL1** (human, Q92673) — `genes/human/SORL1/`. Resolve the
   GO:0099638 (IEA, ACCEPT) row against the GO:2001137 (IMP, ACCEPT,
   `core_functions`) row it will now sit beside. The IMP is the stronger of the
   two and already carries the biology; decide whether the IEA row adds anything
   once it is `GO:0032456`.
3. **ALDH7A1** (human, P49419) — `genes/human/ALDH7A1/`. Re-fetch and check
   whether the GO:1905750 IDA appears; if it still does not, add it manually
   from the GO release rather than leaving the review silently short a row. The
   review's existing PMID:31492851 reasoning ("stress-induced membrane
   recruitment ... non-core") is the natural anchor for the judgement.

### Tier 3 — single-row swaps, low risk

4. **RAB7A** (human, P51149) — `genes/human/RAB7A/`. One IMP row, already
   `KEEP_AS_NON_CORE` with reasoning ("primary RAB7A function is degradative
   trafficking rather than recycling") that survives the re-terming verbatim.
   Pairs with `genes/mouse/Rab7` (two rows, same treatment).
5. **ATP6AP1** (human, Q15904) — `genes/human/ATP6AP1/`. Two rows, both
   `KEEP_AS_NON_CORE`, both electronic/ISS. Mouse `Atp6ap1` is also in the
   upstream EXP list (IMP, PMID:22467241) but has no review here.
6. **`vas2`** (*S. pombe*, Q9P7N2) — `genes/SCHPO/vas2/`. The repo's only member
   of the seven PomBase rows flagged "no automatic replacement". Watch what
   PomBase does before swapping the id — this is the one case where the fix may
   not be a generalisation.

### Tier 4 — follow-on cleanup

7. The five AP-sigma reviews (`AP1S1`, `AP1S3`, `AP2S1`, `AP3S1`, `AP4S1`) and
   `projects/DELIVEROME.md` — prose-only mentions of GO:0099638, all describing
   the `vas2` donor. Do these after `vas2` itself is settled.

## Proposed approach

1. **Do not edit anything yet.** The obsoletion is merged in `go-edit.obo` but
   absent from the released ontology, and the ontology thread reopened on
   2026-09-19 with a de-merge request from Val Wood plus an unanswered question
   from UCL about `GO:0099639`. Premature edits would swap valid terms for
   terms that may be reverted.
2. **Watch two signals**: (a) whether GO:0099638 turns obsolete in OLS/QuickGO,
   and (b) whether go-ontology#31237 is closed as merged or the de-merge
   proceeds. The second determines whether this project is a re-terming exercise
   or a no-op.
3. **When it lands**, LMTK3 first (validation), then SORL1 and ALDH7A1 (which
   need judgement, not just a swap), then the mechanical single-row swaps.
4. **Independently of the obsoletion**, report the two QuickGO-invisible rows
   (mouse `Mfsd8`, human ALDH7A1) upstream, and add the ALDH7A1 row to its
   review. That gap is a data-freshness problem in this repo's own fetch path
   and is worth fixing whichever way the ticket goes.
5. **Consider commenting on go-ontology#31237** with the LMTK-family observation
   above — three paralogs, one biology, three terms, two of which are already on
   the surviving side of the merge.

## Open questions

- Does the merge survive? Val Wood's objection is that neither term subsumes the
  other — MVB fusion with the plasma membrane is endosome-to-PM transport that
  is not recycling, and a properly defined "endocytic recycling" would include
  the inbound internalization step that GO:0099638 excludes. If that view wins,
  the two become siblings and this project closes unused.
- If the merge stands, what happens to `GO:0099639 neurotransmitter receptor
  transport, endosome to plasma membrane` (UCL's two IDAs)? The upstream issue
  says it reparents automatically under GO:0032456; Val Wood's counter-proposal
  is to keep GO:0099638 *specifically* so GO:0099639 has a home. Unresolved in
  the thread as of 2026-09-19.
- Why did the Ensembl/EnsemblFungi projection (693 of 939 rows) not already
  collapse onto GO:0032456, given that GO:0099638 has been an inferred child of
  it all along? Worth understanding before assuming the fan-out clears itself.
- Should `GO:0006893 Golgi to plasma membrane transport` /
  `GO:0043001 Golgi to plasma membrane protein transport` follow? The pair has
  the same differentiae and the same general/protein-specific relationship.
  Merging one pair and not the other is the incoherence the (closed) PR #32631
  raised, and nobody in the thread answered it.
- Is the QuickGO/GO-release discrepancy systematic? Two of 36 rows were affected
  here. If the rate holds across the corpus, a non-trivial number of
  `GENE-goa.tsv` files are missing experimental rows.
