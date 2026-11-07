# PP_3204 curation notes

- UniProt identifies PP_3204 as a cupin type-2 domain protein
  [file:PSEPK/PP_3204/PP_3204-uniprot.txt "InterPro; IPR013096; Cupin_2."].
- KEGG maps PP_3204 to K26182/FdeH and the same unclear R13075 reaction as
  FdeC. The available records do not define whether FdeH is catalytic,
  structural, or otherwise accessory.
- PP_3204 shares 57.6% identity over aligned residue pairs with Hsero_1010 in
  the Herbaspirillum fde locus
  [file:PSEPK/PP_3204/PP_3204-bioinformatics/RESULTS.md "Pairwise identity over aligned residue pairs: 57.6%"].

## 2026-11-06 — late-component participation reassessment

The inherited GO:0046275 proposal is withdrawn and explicitly `retired: true`: cupin membership and similarity to unassayed Hsero_1010 do not establish a particular catalytic or accessory contribution. Locus induction, whole-operon phenotypes and similarity to another unassayed candidate do not establish this product's individual step. Original source fields and row position are preserved; retirement records curator withdrawal, not an upstream GOA disappearance. The former process-only core block is removed, and the unresolved role remains a knowledge gap. The same-role BRADU comparator bll6423 likewise asserts no process annotation. See `analysis/module_audits/bacterial_flavonoid_degradation/round1-source-review.md`.


## 2026-11-07 PR #6140 round-2 review follow-up

The inherited GO:0046275 proposal now uses REMOVE with its existing retired:true flag. This explicitly withdraws a curator-authored proposal, following the documented cysI precedent, rather than making a biological absence claim or reporting disappearance from upstream GOA. Original payload, position and evidence remain present.

See `analysis/module_audits/bacterial_flavonoid_degradation/round2-review-response.md` for source provenance, limits and disposition of all seven review points. Earlier journal entries record superseded judgments and remain unchanged.
