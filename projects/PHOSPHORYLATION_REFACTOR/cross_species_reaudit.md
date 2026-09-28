---
title: "PHOSPHORYLATION_REFACTOR cross-species re-audit"
species: [DROME, DANRE, ARATH, rat]
sidecars:
  current_goa:
    - current-goa-2026-09-28.tsv
---

# Cross-Species Re-Audit

## 2026-09-28

This re-audit revisits the fly, zebrafish, Arabidopsis and rat query-level
findings that were added on 2026-01-19. Those sections predated full
`GENE-ai-review.yaml` curation for these species, and the original query
counted at least one `NOT` annotation as though it were a positive assertion.
The dated `current-goa-2026-09-28.tsv` sidecar records total fetched GOA rows,
positive protein-phosphorylation rows, negated protein-phosphorylation rows and
the related GOA rows used to make the calls below.

Rules used here:

- Keep `NOT|...` rows out of the error set. They say the gene product lacks the
  activity or process.
- Count only current positive rows to `GO:0006468 protein phosphorylation`,
  `GO:0046777 protein autophosphorylation`, or a protein-specific descendant
  such as `GO:0018108 peptidyl-tyrosine phosphorylation`.
- Treat `GO:0046834 lipid phosphorylation`, `GO:0008887 glycerate kinase
  activity`, arginine kinase activity, and PI4K molecular-function rows as
  substrate-correct unless they also have a positive protein-phosphorylation
  process row.
- Do not turn a row into `REMOVE` merely because the protein has no GOA
  `GO:0004672 protein kinase activity` parent; several plant receptor-like
  kinases were caught by ID mismatches or lagging MF coverage and are real
  protein kinases.

The main project counts should therefore treat fly/ZFIN/TAIR/RGD as a
row-level triage, not as completed gene reviews.

## FlyBase

| Gene | Current GOA row | Current call | Rationale |
|------|-----------------|--------------|-----------|
| DROME/Mulk | No positive protein-phosphorylation BP row; IDA `GO:0046834 lipid phosphorylation` from PMID:22069480 | False positive | Mulk currently carries ceramide/acylglycerol kinase molecular functions and a lipid-phosphorylation process row. That is not a protein-phosphorylation error. |
| DROME/rdgA | No positive protein-phosphorylation BP row; TAS `GO:0046834 lipid phosphorylation` from PMID:11707492 | False positive | rdgA is a diacylglycerol kinase. The only phosphorylation process hit in current GOA is lipid phosphorylation. |
| DROME/Argk1 | No positive protein-phosphorylation BP row | Stale hit | Current GOA has arginine kinase molecular-function rows, but no `GO:0006468` or `GO:0046777` biological-process row. |
| DROME/Dref | ISS `GO:0006468 protein phosphorylation` and `GO:0046777 protein autophosphorylation` from GO_REF:0000024, `WITH/FROM` human CAMKK2 | Remove | Dref is a BED-domain transcription factor rather than a kinase; the positive protein-phosphorylation rows are old ISS transfers from human CAMKK2, not a FlyBase or PAINT assertion. |
| DROME/CG9886 (`Glyctk`) | ISS `GO:0006468 protein phosphorylation` from GO_REF:0000024, `WITH/FROM` human GLYCTK | Remove | CG9886 is glycerate kinase, EC 2.7.1.31, and current GOA already has `GO:0008887 glycerate kinase activity`. The propagated human GLYCTK `GO:0006468` row is the same wrong-substrate error seen in mammals. |

## Zebrafish

| Gene | Current GOA row | Current call | Rationale |
|------|-----------------|--------------|-----------|
| DANRE/glyctk | ISS `GO:0006468 protein phosphorylation` from GO_REF:0000024, `WITH/FROM` human GLYCTK | Remove | Zebrafish glyctk is glycerate kinase, EC 2.7.1.31, and current GOA already has `GO:0008887 glycerate kinase activity`. The protein-phosphorylation row should not have propagated from human GLYCTK. |

## Arabidopsis

| Gene | Current GOA row | Current call | Rationale |
|------|-----------------|--------------|-----------|
| ARATH/CRY2 | Negated `GO:0016301 kinase activity` and `GO:0046777 protein autophosphorylation`, both PMID:17073458 | False positive | This is the important qualifier bug: the rows are negated and are already accepted in `genes/ARATH/CRY2/CRY2-ai-review.yaml`. They should never be counted as incorrect positive phosphorylation annotations. |
| ARATH/TOPP4 | IPI `GO:0006468 protein phosphorylation` from PMID:26704640, with PIF5 | Remove | TOPP4 is a type 1 protein phosphatase. The cited abstract says TOPP4 interacts with PIF5 and dephosphorylates it, so the gene acts on the opposite side of the phosphorylation cycle. |
| ARATH/CDC25 | IDA `GO:0006468 protein phosphorylation` from PMID:15336525 | Remove | PMID:15336525 characterizes Arath;CDC25 as a dual-specificity tyrosine phosphatase, and current GOA also has `GO:0004725 protein tyrosine phosphatase activity`. |
| ARATH/PWD | No positive protein-phosphorylation BP row | Stale hit | Current fetched GOA no longer has a protein autophosphorylation row for PWD. |
| ARATH/CKB2 | No positive protein-phosphorylation BP row | Stale hit | Current fetched GOA no longer has a protein-phosphorylation row for the CK2 beta regulatory subunit. |
| ARATH/RIN4 | IDA `GO:0006468 protein phosphorylation` from PMID:11955429 | Remove | RIN4 is the immune regulator whose phosphorylation is induced by AvrRpm1 and AvrB; the cached abstract describes phosphorylation of RIN4, not phosphorylation by RIN4. |
| ARATH/ATPI4K_ALPHA (`PI4KA1`) | IDA `GO:0006468 protein phosphorylation` from PMID:9712908 | Modify | PI4KA1 is phosphatidylinositol 4-kinase alpha 1, EC 2.7.1.67. The PMID:9712908-linked evidence supports PI4K activity and phosphoinositide binding, not phosphorylation of protein substrates. |
| ARATH/PI4KG7 | IDA `GO:0046777 protein autophosphorylation` from PMID:17880284 | Keep | This was mislabeled as a lipid-kinase error in January. The PMID:17880284 abstract says AtPI4Kgamma7 undergoes autophosphorylation and phosphorylates Ser/Thr protein substrates. |
| ARATH/AAK1 (`FER`) | IDA `GO:0046777 protein autophosphorylation` from PMID:17673660 | Keep | AAK1 resolves to FERONIA, a receptor-like protein kinase; the same PMID also supports an IDA `GO:0004672 protein kinase activity` row in current GOA. |
| ARATH/LecRK-I.5 | IDA `GO:0006468 protein phosphorylation` from PMID:32345768 | Keep | P2K2/LecRK-I.5 is a receptor-like protein kinase, and the PMID:32345768 abstract says P2K2 and P2K1 cross-phosphorylate after extracellular ATP treatment. |
| ARATH/LecRK-I.8 | IDA `GO:0046777 protein autophosphorylation` from PMID:28722654 | Keep | The full text of PMID:28722654 reports "strong autophosphorylation activity" by the LecRK-I.8 kinase domain. |

## Rat

| Gene | Current GOA row | Current call | Rationale |
|------|-----------------|--------------|-----------|
| rat/Gas6 | ISS `GO:0006468 protein phosphorylation` from GO_REF:0000024, `WITH/FROM` human GAS6 | Modify | This is the same TAM-receptor ligand pattern as mouse Gas6. The ligand activates receptor tyrosine kinases and downstream ERK/PI3K signaling; it does not catalyze the phosphorylation reaction. |
| rat/Glyctk | ISS `GO:0006468 protein phosphorylation` from GO_REF:0000024, `WITH/FROM` human GLYCTK | Remove | Glyctk is a small-molecule glycerate kinase, and current GOA already has multiple `GO:0008887 glycerate kinase activity` rows. |
| rat/Ilf3 | ISS `GO:0006468 protein phosphorylation` from GO_REF:0000024, `WITH/FROM` mouse Ilf3 | Remove | Human ILF3 has the corresponding IDA row reviewed as a substrate error: ILF3/NFAR is phosphorylated by PKR rather than being a kinase. |
| rat/Pdgfb | ISS `GO:0006468 protein phosphorylation` and `GO:0018108 peptidyl-tyrosine phosphorylation` from GO_REF:0000024, `WITH/FROM` human PDGFB | Modify | These mirror the human PDGFB rows, which should be replaced with `GO:0048008 platelet-derived growth factor receptor signaling pathway`; PDGFB is the secreted ligand, not the receptor tyrosine kinase. |
| rat/Prrt1 | ISS `GO:0006468 protein phosphorylation` from GO_REF:0000024, `WITH/FROM` mouse Prrt1 | Remove | The human PRRT1 review rejected this same assertion: PRRT1/SynDIG4 affects basal GRIA1 phosphorylation indirectly as an AMPAR auxiliary subunit and has no kinase domain. |
| rat/Ywhaz | ISS `GO:0006468 protein phosphorylation` from GO_REF:0000024, `WITH/FROM` human YWHAZ | Modify | The human YWHAZ review recasts this as regulation of phosphorylation. 14-3-3 zeta binds phosphoserine clients and modulates kinase pathways but is not itself the kinase. |
| rat/Ppp3cb | ISS `GO:0006468 protein phosphorylation` from GO_REF:0000024, `WITH/FROM` human PPP3CB | Remove | Ppp3cb is the calcineurin catalytic subunit, a calcium/calmodulin-dependent protein phosphatase. The positive protein-phosphorylation row is the opposite reaction. |
| rat/Grm5 | IDA `GO:0006468 protein phosphorylation` from PMID:15758184 | Remove | PMID:15758184 supports mGluR5-dependent ERK1/2 phosphorylation through Homer1b/c. The same current GOA file already has `GO:0043410 positive regulation of MAPK cascade` for this reference. |
| rat/Pick1 | IDA `GO:0006468 protein phosphorylation` from PMID:11237868 | Modify | The PMID:11237868 abstract says rPICK1 modulates PKC phosphorylation of TIS21 through binding; PICK1 is the PDZ scaffold, not PKC. |
| rat/Thy1 | IDA `GO:0046777 protein autophosphorylation` from PMID:19723805 | Remove | Thy-1 is a GPI-anchored ligand. The full text says "FAK autophosphorylation on Y397 is triggered by Thy-1" downstream of integrin and syndecan-4 engagement in astrocytes. |
