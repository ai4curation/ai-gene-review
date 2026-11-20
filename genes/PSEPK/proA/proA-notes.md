# proA (Q88DL4) — Pseudomonas putida KT2440 gamma-glutamyl phosphate reductase

## Summary

proA (PP_4811) encodes the reviewed cytoplasmic gamma-glutamyl phosphate
reductase (glutamate-5-semialdehyde dehydrogenase, EC 1.2.1.41), the second
enzyme of the glutamate-to-P5C branch of L-proline biosynthesis
[file:PSEPK/proA/proA-uniprot.txt "Catalyzes the NADPH-dependent reduction of L-glutamate 5-"].
The product cyclizes non-enzymatically
[file:PSEPK/proA/proA-uniprot.txt "The product spontaneously undergoes cyclization to form 1-pyrroline-5-carboxylate."].

- Pathway: [file:PSEPK/proA/proA-uniprot.txt "PATHWAY: Amino-acid biosynthesis; L-proline biosynthesis"]
- Localization: [file:PSEPK/proA/proA-uniprot.txt "SUBCELLULAR LOCATION: Cytoplasm"]
- PANTHER: PTHR11063 (GLUTAMATE SEMIALDEHYDE DEHYDROGENASE), subfamily SF8.
  SF8 also contains bifunctional animal P5C synthases; Q88DL4 is a
  monofunctional ProA-type enzyme (no amino-acid-kinase domain), so the
  glutamate 5-kinase step belongs to the separate ProB (Q88Q07).

## Provenance and search

- No gene-level deep-research provider file exists for Q88DL4 and no provider
  API keys were available in this session (2026-11-02). The review rests on the
  reviewed UniProt record, the PTHR11063 PAINT slice and the experimentally
  grounded E. coli ProA ortholog (genes/ECOLI/proA). No Q88DL4-specific
  experimental publications are cached.
- All GOA rows are electronic (GO_REF:0000120, GO_REF:0000002). Generic
  oxidoreductase activity was refined to GO:0004350; NADP binding kept as a
  non-core cofactor-binding subfunction, consistent with E. coli proA and yeast PRO2.


## 2026-11-07 evidence re-audit

All original annotation payloads and row order are preserved. No NEW annotation was added. The catalytic reaction and proline-biosynthetic participation remain supported. KT2440 chemistry and localization are conserved-role inferences supported by curated HAMAP, not newly identified target assays.

The normal Falcon research attempt failed with HTTP 403 authentication/access error; no provider report was fabricated. Manual source review used the protected existing caches and normally fetched new publications.

PMID:39514317 (full text) challenges required ProA–ProB channeling: heterologous kinase replacements and overexpressed alternative reductases support E. coli growth; failed crosslinking alone is not universal proof of no interaction. ProA is reduced glutamyl-phosphate chemistry; spontaneous GSA cyclization supplies P5C. The computed GP half-life and diffusion times are calculations, not intracellular measurements. Native-locus monomeric-GFP fusions show dispersed cytoplasmic localization. Expression/purification used engineered BL21 derivatives, while growth experiments used K-12 BW25113 derivatives. No matched-protein complex requirement is imposed.

NADP binding includes both NADP+ and NADPH under the verified current GO definition and directly supports ProA catalysis; it is not peripheral simply because the catalytic term is more informative.

Existing abstract-only primary caches were not refreshed. Curated experimental annotations remain supported where independent evidence agrees; no target-table detail was invented. Complete validation, ontology snapshots and preservation proof are in the member-review audit and ignored existing-review logs.


## 2026-11-08 — consistent inferred cytosolic ProA location

Refine cytoplasm to cytosol using the same evidential standard as BACSU: curated HAMAP MF_00412 compartment/family support, soluble reductase architecture without annotated signal peptide or transmembrane segment, and comparative native-locus monomeric-GFP imaging of E. coli ProA (PMID:39514317). This is an inference for Pseudomonas putida KT2440, not a direct localization experiment. Protein association does not exclude cytosol. Original annotation payloads and raw records are unchanged.


## 2026-11-08 — reference target wording

Corrected the copied organism name in the PMID:39514317 findings and reference-review note to Pseudomonas putida. The experiment remains E. coli microscopy used comparatively; no target-strain assay or new biological claim is asserted.
