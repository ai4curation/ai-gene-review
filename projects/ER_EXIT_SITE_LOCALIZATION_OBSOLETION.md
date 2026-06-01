# Protein Localization to ER Exit Site — Obsoletion

## Overview

A GO obsoletion proposal will obsolete the biological-process term
`GO:0070973 protein localization to endoplasmic reticulum exit site`
(defined as "A process in which a protein is transported to, or maintained in, a
location at an endoplasmic reticulum exit site"). The upstream rationale
(ValWood, go-ontology#19122) is that the term **says nothing about the process
itself and conflates several distinct biological roles** — it has been used for
COPII coat assembly factors, anterograde ER→Golgi transport cargo, regulators of
that transport, and ER quality-control proteins. Because the existing
annotations sit in **different pathway contexts**, a single blanket
`replaced_by` cannot be applied; each annotation needs an individually chosen
process term.

This term sits alongside the related "protein exit from endoplasmic reticulum"
family (`GO:0032527` and its regulation children `GO:0070861/0070862/0070863`,
plus `GO:1904211`) that the same ontology ticket proposes to obsolete; that
sibling set is reviewed in go-annotation#6172. GO:0070973 was added to the same
ticket because it has the same conflation problem.

## Upstream tickets

- Annotation tracker: [geneontology/go-annotation#6434](https://github.com/geneontology/go-annotation/issues/6434)
- Ontology ticket (obsoletion): [geneontology/go-ontology#19122](https://github.com/geneontology/go-ontology/issues/19122) (OPEN; labels: obsoletion, ready, vesicle-mediated-transport) — originally "obsoletion 'protein exit from endoplasmic reticulum'", with GO:0070973 added in the Jan/May 2026 discussion.
- Sibling "protein exit from ER" annotation review: [geneontology/go-annotation#6172](https://github.com/geneontology/go-annotation/issues/6172)

## Obsoletion plan (per upstream)

There is **no single `replaced_by`**. The proposed per-annotation remapping
(ValWood, go-annotation/go-ontology#19122 comment, 2026-05-21) is:

| Accession | Symbol | Source | Organism | Proposed action |
|---|---|---|---|---|
| O15027 | SEC16A | UniProt | Human | → `GO:0048208` COPII vesicle coat assembly (syn. "COPII vesicle coating") |
| P34643 | sec-16A.1 | WB | *C. elegans* | → `GO:0048208` COPII vesicle coat assembly |
| P48415 | SEC16 | SGD | *S. cerevisiae* | → `GO:0048208` COPII vesicle coat assembly |
| Q5JRA6 | MIA3 | UniProt | Human | → `GO:0006888` ER to Golgi vesicle-mediated transport |
| Q5S007 | LRRK2 | UniProt | Human | → `GO:0060628` regulation of ER to Golgi vesicle-mediated transport |
| Q5S006 | Lrrk2 | UniProt | Mouse | **delete** — redundant; already carries `GO:0060628` from the same paper (PMID:25201882) |
| Q57WC1 | Tb03.28C22.610 | GeneDB | *T. brucei* | **delete** — already carries `GO:0006888` ER to Golgi vesicle-mediated transport |
| Q61334 | Bcap29 | MGI | Mouse | → ER quality control, likely `GO:0034976` response to endoplasmic reticulum stress (or descendant) |
| Q61335 | Bcap31 | MGI | Mouse | → ER quality control, likely `GO:0034976` response to endoplasmic reticulum stress (or descendant) |
| Q92538 | GBF1 | UniProt | Human | → vesicle-mediated transport or a descendant |

ValWood notes that for the forward (ER-export) direction generally,
**`GO:0090114` COPII-coated vesicle budding** (synonym "ER exit") is often the
best replacement, since it is the COPII vesicle that drives exit from the ER.

Term labels verified in OLS on 2026-05-29:

- `GO:0070973` (`protein localization to endoplasmic reticulum exit site`) — live BP, slated for obsoletion. No children.
- `GO:0048208` (`COPII vesicle coat assembly`) — live; renamed from "COPII vesicle coating" (go-ontology PR #32013).
- `GO:0090114` (`COPII-coated vesicle budding`) — live; synonym "ER exit".
- `GO:0006888` (`endoplasmic reticulum to Golgi vesicle-mediated transport`) — live.
- `GO:0060628` (`regulation of ER to Golgi vesicle-mediated transport`) — live.
- `GO:0034976` (`response to endoplasmic reticulum stress`) — live.

## Affected experimental / curated annotations

Retrieved from the QuickGO annotation API on 2026-05-29 (`goId=GO:0070973`,
restricted to the named accessions). The curated (non-IEA) records:

| # | Source | Accession | Symbol | Organism | Evidence | Qualifier | Reference |
|---|---|---|---|---|---|---|---|
| 1 | UniProt | O15027 | SEC16A | Human | IMP | involved_in | PMID:28442536 |
| 2 | WB | P34643 | sec-16A.1 | *C. elegans* | IMP | involved_in | PMID:21478858 |
| 3 | SGD | P48415 | SEC16 | *S. cerevisiae* | IMP | involved_in | PMID:22675024 |
| 4 | GeneDB | Q57WC1 | Tb03.28C22.610 | *T. brucei* | IMP | acts_upstream_of_or_within | PMID:24612401 |
| 5 | UniProt | Q5JRA6 | MIA3 | Human | IMP | involved_in | PMID:28442536 |
| 6 | UniProt | Q5S006 | Lrrk2 | Mouse | IMP | involved_in | PMID:25201882 |
| 7 | UniProt | Q5S007 | LRRK2 | Human | IMP | involved_in | PMID:25201882 |
| 8 | MGI | Q61334 | Bcap29 | Mouse | IGI | acts_upstream_of_or_within | PMID:15187134 |
| 9 | MGI | Q61335 | Bcap31 | Mouse | IGI | acts_upstream_of_or_within | PMID:15187134 |
| 10 | UniProt | Q92538 | GBF1 | Human | IMP | involved_in | PMID:17956946 |

The upstream group tally is GeneDB 1, MGI 2, SGD 1, WB 1, ~UniProt 7~ (the
UniProt portion is struck through in the issue, i.e. already handled by UniProt).
The minor count difference vs. the 10 rows above (UniProt tally of 7 vs. 5
distinct UniProt rows here) is likely spreadsheet rows for annotation extensions
or duplicates; flagged for the curator's awareness.

On top of these curated records, GO:0070973 currently carries **~14,414 total
annotations** (QuickGO, 2026-05-29), overwhelmingly IEA (TreeGrafter
`GO_REF:0000118`; UniProt `GO_REF:0000104/0000120`) and IBA (`GO_REF:0000033`).
These will be retired/redirected automatically once the term is obsoleted, but
the volume shows how far a handful of curated annotations has propagated.

## Why a blanket `replaced_by` does not work

The curated annotations fall into biologically distinct classes:

- **COPII coat-assembly scaffolds** — SEC16A / SEC16 / sec-16A.1 organize ER
  exit sites and template the COPII coat. The right MF/BP is COPII vesicle
  coat assembly (`GO:0048208`), not a "localization" term.
- **Anterograde transport cargo/machinery** — MIA3/TANGO1 (`GO:0006888`),
  GBF1 (general vesicle-mediated transport). These are about the transport step
  itself.
- **Regulators of transport** — LRRK2 regulates Sec16A at ER exit sites
  (`GO:0060628`, regulation of ER→Golgi transport). The mouse ortholog
  annotation is redundant with an existing regulation annotation from the same
  paper and should be deleted.
- **ER quality control** — mouse Bcap29/Bcap31 (BAP29/BAP31) act upstream of ER
  export as translocon-associated sorting/QC chaperones; the upstream
  recommendation is an ER-stress / quality-control term (`GO:0034976`), not an
  ER-exit-site localization.
- **Already-redundant** — the *T. brucei* GeneDB annotation already has
  `GO:0006888` and should simply be deleted.

## Mappings to review

- `GO:0070973` **unirule2go** `UniRule:UR001349783` > protein localization to
  endoplasmic reticulum exit site. This UniRule mapping must be retargeted or
  removed when the term is obsoleted (otherwise the large IEA tail re-propagates).

## Impact on this repo

Two affected gene products already have `*-ai-review.yaml` files that annotate
`GO:0070973` (verified 2026-05-29):

| Gene | Path | Relation to affected set | Current handling of GO:0070973 | Action when obsoletion lands |
|---|---|---|---|---|
| LRRK2 (human, Q5S007) | `genes/human/LRRK2` | Directly affected (row 7) | Two annotations — IEA (`GO_REF:0000120`) and IMP (PMID:25201882) — both `ACCEPT` with summary "LRRK2 regulates Sec16A at ER exit sites" | **MODIFY** → `GO:0060628` regulation of ER to Golgi vesicle-mediated transport, matching the upstream Q5S007 plan |
| BCAP31 (human, Q61335 is the mouse ortholog) | `genes/human/BCAP31` | Ortholog of affected mouse Bcap31 (row 9); the human record's GO:0070973 is an IBA over-propagation | IBA already `MARK_AS_OVER_ANNOTATED` per go-annotation#6385 (over-propagation from PANTHER PTN000294723; core role is ER QC / translocon chaperone) | No change needed — already flagged; obsoletion removes the IBA. The curated mouse Bcap29/Bcap31 records remap to `GO:0034976`, consistent with the existing "ER quality control" rationale |

The human LRRK2 review will need a `MODIFY` pass once the obsoletion lands; the
human BCAP31 review is already aligned with the upstream direction.

## Scope

- **GO branch:** Biological Process (single-term obsoletion, no `replaced_by`).
- **Organisms:** Human, mouse, *S. cerevisiae*, *C. elegans*, *T. brucei*
  (curated set); plus the large IEA/IBA tail across all eukaryotes.
- **Gene set:** COPII coat scaffolds (SEC16A/SEC16/sec-16A.1), anterograde
  transport machinery (MIA3, GBF1), the transport regulator LRRK2, and the ER
  quality-control proteins BAP29/BAP31.
- **Type of fix:** Curation hygiene / refactor. The biology of each gene is well
  established; the work is splitting one over-loaded "localization" term into the
  correct process terms per annotation.

## Candidate genes for initial review

Listed in priority order. The first two already have reviews here and would be
directly exercised by the obsoletion.

1. **LRRK2 (human, Q5S007)** — already reviewed; needs a `MODIFY` of GO:0070973 →
   `GO:0060628` (regulation of ER→Golgi transport). Highest-value, lowest-effort.
2. **BCAP31 (human)** — already reviewed and `MARK_AS_OVER_ANNOTATED`; confirm
   alignment once obsoletion lands.
3. **SEC16A (human, O15027)** — clean COPII coat-assembly case → `GO:0048208`;
   not yet in this repo. A good positive control for the COPII-coating remap.
4. **MIA3 / TANGO1 (human, Q5JRA6)** — anterograde transport of bulky cargo →
   `GO:0006888`; not yet in this repo.
5. **GBF1 (human, Q92538)** — Arf-GEF at the ER-Golgi interface → vesicle-mediated
   transport; not yet in this repo.
6. **SEC16 (yeast, P48415)** — canonical ER-exit-site organizer; cross-check
   against the human SEC16A handling.

## Proposed approach

1. **Track the obsoletion.** go-ontology#19122 is OPEN and labeled "ready"; the
   replacement terms already exist in GO (`GO:0048208`, `GO:0090114`,
   `GO:0006888`, `GO:0060628`, `GO:0034976`), so no NTR blocks this — unlike the
   mitochondrion-targeting-sequence-binding case.
2. **Pre-stage the LRRK2 MODIFY** (GO:0070973 → `GO:0060628`) so the repo review
   is ready the moment the term is obsoleted. Both LRRK2 GO:0070973 annotations
   (IEA and IMP) should move together.
3. **Confirm BCAP31** stays `MARK_AS_OVER_ANNOTATED`; the curated mouse
   Bcap29/Bcap31 remap to `GO:0034976` is consistent with the human review.
4. **Optionally seed SEC16A / MIA3 / GBF1 reviews** as the clean COPII / secretory
   cases, since they exercise the three main replacement terms.
5. **Flag the UniRule mapping** (`UR001349783`) for retargeting/removal to stop
   IEA re-propagation after obsoletion.

## Priority

Low–medium. Only ~10 curated annotations, replacement terms already exist, and
the two repo-resident genes (LRRK2, BCAP31) are already reviewed — LRRK2 just
needs a one-line MODIFY and BCAP31 is already aligned. No curator group is
blocked waiting on AI Gene Review. The large IEA/IBA tail (driven by the
UniRule mapping) makes the cleanup more impactful than the small curated count
suggests.

## Status

- 2026-05-29 — Project file created. Tracking go-annotation#6434 and
  go-ontology#19122 (OPEN, "ready"). The 10 curated annotations were retrieved
  from QuickGO and reconciled against ValWood's per-annotation remapping plan and
  the upstream group tally. All five replacement terms (`GO:0048208`,
  `GO:0090114`, `GO:0006888`, `GO:0060628`, `GO:0034976`) confirmed live in OLS,
  so no NTR is blocking. Two existing repo reviews touch GO:0070973: human LRRK2
  (needs MODIFY → `GO:0060628`) and human BCAP31 (already
  `MARK_AS_OVER_ANNOTATED` per go-annotation#6385). One UniRule mapping
  (`UR001349783`) needs retargeting/removal.
