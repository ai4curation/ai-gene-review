# AIRE manual deep research fallback

## Provenance

Falcon deep research was attempted with:

```bash
just deep-research-falcon human AIRE --fallback perplexity-lite
```

Falcon timed out after 600 seconds. The configured `perplexity-lite` fallback then failed with a Perplexity API 401 quota error, so no provider-generated deep research file was created. This manual fallback summarizes the cached publications, UniProt-derived context, and PN projection report used for the review.

## Functional Synthesis

AIRE is a thymic self-tolerance regulator. Human disease genetics and mechanistic studies support AIRE as a nuclear transcriptional/chromatin regulator rather than a general immune effector. Dominant PHD1 mutations suppress gene expression driven by wild-type AIRE and are associated with organ-specific autoimmunity [PMID:26084028 "These missense PHD1 mutations suppressed gene expression driven by wild-type AIRE in a dominant-negative manner"]. The broader disease role is thymic T cell tolerance induction and autoimmunity prevention [PMID:19302042 "Aire plays an important role in T cell tolerance induction in the thymus"; PMID:26084028 "The autoimmune regulator (AIRE) gene is crucial for establishing central immunological tolerance and preventing autoimmunity."].

AIRE's core molecular features are chromatin engagement, histone H3 recognition, DNA binding, transcriptional activation, and oligomerization. PHD1 selectively binds histone H3 and preferentially recognizes non-methylated H3K4 [PMID:18292755 "AIRE selectively interacts with histone H3 through its first plant homeodomain (PHD) finger"; PMID:18292755 "preferentially binds to non-methylated H3K4 (H3K4me0)"]. Structural work confirms an extensive AIRE PHD1-H3 interface [PMID:19446523 "The structure reveals a detailed network of interactions between the protein and the amino-terminal residues of histone H3"]. AIRE oligomers bind A/T-rich DNA motifs [PMID:11533054 "AIRE dimers and tetramers, but not the monomers, can bind to G-doublets with the ATTGGTTA motif and the TTATTA-box."] and activate promoter/reporter expression [PMID:11274163 "AIRE can activate the interferon beta minimal promoter in a transfection assay"; PMID:18292755 "in vivo AIRE binds to and activates promoters containing low levels of H3K4me3"].

Cellular localization is primarily nuclear, with nuclear dot/nuclear-body-like localization and some cytoplasmic or microtubule-associated signal [PMID:11274163 "At the cellular level, AIRE is located in microtubular structures of the cytoskeleton and in discrete nuclear dots resembling ND10 nuclear bodies."; PMID:14974083 "Most of the mutations altered the nucleus-cytoplasm distribution of AIRE and disturbed its association with nuclear dots and cytoplasmic filaments."].

## PN Projection Assessment

The Proteostasis PN projection report assigns AIRE a candidate `GO:0061630 ubiquitin protein ligase activity` annotation from the path `Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|RING variant|PHD|other` [file:projects/PROTEOSTASIS/reports/pn_projection/pn_projected_annotations.tsv]. This was not added as a new GO annotation. The projection is based on a UPS domain/family bucket, while the direct AIRE literature supports a PHD histone-reader/transcriptional regulator. The current evidence does not demonstrate direct ubiquitin transfer or intrinsic E3 ligase activity for AIRE.

## GO Review Implications

- Accept histone binding, chromatin binding, sequence-specific transcription regulatory region DNA binding, positive regulation of RNA polymerase II transcription, nuclear/nuclear-body localization, central tolerance induction, and negative thymic T cell selection.
- Keep cytoplasmic localization, oligomerization, peripheral tolerance, thymic epithelial morphogenesis, thymocyte migration, chemokine-production regulation, and zinc ion binding as non-core or supporting features.
- Mark generic protein binding, immune response, and humoral immune response as over-annotated where they obscure the more specific AIRE mechanism.
- Remove automated translation-regulator annotations because the available evidence supports transcription/chromatin regulation rather than translation regulation.
- Do not add `GO:0061630 ubiquitin protein ligase activity` without direct biochemical or cellular ubiquitination evidence.
