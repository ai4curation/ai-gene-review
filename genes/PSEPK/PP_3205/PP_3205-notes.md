# PP_3205 curation notes

- UniProt identifies PP_3205 as a fumarylacetoacetate-hydrolase-family protein
  [file:PSEPK/PP_3205/PP_3205-uniprot.txt "Fumarylacetoacetate hydrolase family protein"].
- KEGG maps PP_3205 to K26185/FdeI and two unclear reactions: R13078 is drawn
  as decarboxylation, while R13079 eliminates water. Neither has direct assay
  support for PP_3205 or Hsero_1011.
- PP_3205 shares 62.3% identity over aligned residue pairs with Hsero_1011
  [file:PSEPK/PP_3205/PP_3205-bioinformatics/RESULTS.md "Pairwise identity over aligned residue pairs: 62.3%"].
- OpenScientist completed after the review was drafted and independently
  recovered K26185/FdeI while stating that no direct PP_3205 characterization
  exists [file:PSEPK/PP_3205/PP_3205-deep-research-openscientist.md "No direct
  experimental characterization of PP_3205 exists."]. Its localization,
  regulation, metal, and catalytic-motif claims remain unverified and were not
  converted into annotations.

## 2026-11-06 — late-component participation reassessment

The inherited GO:0046275 proposal is withdrawn and explicitly `retired: true`: the FAH fold and similarity to unassayed Hsero_1011 do not establish either proposed R13078/R13079 transformation. Locus induction, whole-operon phenotypes and similarity to another unassayed candidate do not establish this product's individual step. Original source fields and row position are preserved; retirement records curator withdrawal, not an upstream GOA disappearance. The former process-only core block is removed, and the unresolved role remains a knowledge gap. The same-role BRADU comparator bll6422 likewise asserts no process annotation. See `analysis/module_audits/bacterial_flavonoid_degradation/round1-source-review.md`.


## 2026-11-07 PR #6140 round-2 review follow-up

The inherited GO:0046275 proposal now uses REMOVE with its existing retired:true flag. This explicitly withdraws a curator-authored proposal, following the documented cysI precedent, rather than making a biological absence claim or reporting disappearance from upstream GOA. Original payload, position and evidence remain present.

See `analysis/module_audits/bacterial_flavonoid_degradation/round2-review-response.md` for source provenance, limits and disposition of all seven review points. Earlier journal entries record superseded judgments and remain unchanged.
