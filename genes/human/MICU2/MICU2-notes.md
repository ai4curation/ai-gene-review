# MICU2 notes

## Deep research

- `just fetch-gene human MICU2` and `just fetch-gene-pmids human MICU2` had already succeeded before this review.
- `just deep-research-falcon human MICU2 --fallback perplexity-lite` failed because the Falcon and Perplexity providers were unavailable. No provider-named `MICU2-deep-research-*.md` file was created.
- Manual review therefore used the seeded GOA rows, UniProt Q8IYU8, the cached MICU2 publications, the mitochondrial calcium uniporter module, PAINT lineage-loss output, and the current GO-CAM under `gocams/65d7e4ac00001363/`.

## Evidence synthesis

- MICU2 is a mitochondrial calcium uniporter regulatory subunit, not a Ca2+-conducting pore. The pore is MCU/EMRE; MICU2 acts from the intermembrane-space side of the inner membrane as the MICU1-MICU2 EF-hand dimer [PMID:32494073, "the uniporter complex (uniplex) contains four core components"; PMID:24560927, "MICU2 forms an obligate heterodimer with MICU1 located in the mitochondrial intermembrane space"].
- MICU2's most direct molecular functions are Ca2+ sensing and MICU1 heterodimerization. Ca2+ binding to the MICU1-MICU2 dimer controls the transition between a resting, gatekept uniporter and a high-Ca2+ conducting state [PMID:28615291, "We reconstitute the MICU1-MICU2 heterodimer"; PMID:24560927, "MICU1-MICU2 heterodimers act as the MCU gatekeeper"].
- At low Ca2+, MICU2 is best described as the inhibitory/gatekeeping partner that suppresses constitutive MCU activity and protects against matrix Ca2+ overload. MICU1 is the principal pore-occluding and stimulatory partner in the structural studies [PMID:26903221, "MICU2 behaves as a pure inhibitor of MCU at low cytosolic [Ca(2+)]"; PMID:32494073, "MICU1 uses its K/R ring to seal the MCU pore"].
- I did not propose `GO:0019855` calcium channel inhibitor activity for MICU2 because the direct human holocomplex structures assign physical pore occlusion to MICU1 rather than MICU2; MICU2 contributes to the low-Ca2+ inhibited state through EF-hand sensor activity and MICU1-MICU2 dimer formation.
- The PAINT rows on calcium ion binding, calcium import into the mitochondrion, mitochondrial calcium ion homeostasis, and uniplex complex are acceptable for human MICU2. `uv run python -m ai_gene_review.validation.gene_paint_losses human MICU2` reported `No IRD or IKR loss on this gene's lineage.`
- Parent `GO:0006851` mitochondrial calcium ion transmembrane transport and `GO:0034704` calcium channel complex rows were kept at their own source granularity rather than using other rows to force a more specific import or uniplex term. Bare `GO:0005515` protein binding from MICU1 interaction papers was changed to the specific heterodimerization function when the paper actually assayed MICU1-MICU2 dimerization.
- The BioPlex 3.0 and 2025 multimodal cell-map rows are left as removals of the uninformative bare protein-binding term. They are not treated as false MICU1-MICU2 interactions.

## GO-CAM context

- The GO-CAM model in `gocams/65d7e4ac00001363/` represents the activated, high-Ca2+ branch in which Ca2+ sensing by MICU1/MICU2 positively regulates MCU-mediated mitochondrial Ca2+ import.
- That branch is defensible as a partial model, but the GO-CAM does not separately model the low-Ca2+ gatekeeping branch where MICU2 restrains MCU activity. For the gene review, the Ensembl-transferred `GO:0051561` positive regulation of mitochondrial calcium ion concentration row is therefore kept as a non-core high-Ca2+ arm rather than accepted as MICU2's dominant sign.
