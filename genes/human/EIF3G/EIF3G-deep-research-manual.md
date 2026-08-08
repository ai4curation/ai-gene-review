# Manual deep research: human EIF3G

## Why this file exists

Falcon deep research failed with HTTP 402 and the Perplexity-lite fallback failed with HTTP 401 on 2026-07-18. This manual synthesis is based on the reviewed UniProt record, the complete GOA seed, cached primary publications, and local GO term metadata. It is intentionally not named for a provider.

## Functional synthesis

EIF3G is a conserved RNA-binding subunit of the cytosolic eIF3 complex. It contains a C-terminal RRM and directly binds RNA in vitro. In human cells, EIF3G is one of four eIF3 subunits that directly crosslink to a restricted set of mRNAs, with contacts enriched in 5-prime UTRs. EIF3G participates structurally in the eIF3(a:b:i:g) module adjacent to the mRNA entry/decoding region.

Human reconstitution provides an important constraint: an EIF3 complex lacking EIF3G and EIF3I retained basal activity on beta-globin mRNA, and EIF3G knockdown did not reduce bulk translation. EIF3G should therefore not be described as an independently catalytic or universally rate-limiting initiation factor. The strongest model is that EIF3G contributes an RNA-contacting, transcript-selective regulatory surface within eIF3, while the holo-complex supplies general translation-initiation-factor activity.

## Primary evidence

- [PMID:9822659] Direct biochemical RNA binding: "Northwestern blotting shows that eIF3-p44 binds 18 S rRNA and beta-globin mRNA."
- [PMID:9973622] Independent recombinant-protein result: "The purified protein binds RNA in agreement with the presence of a putative RNA binding motif in the deduced amino acid sequence."
- [PMID:17581632] Functional boundary: "It was striking that two evolutionarily conserved subunits, eIF3g and eIF3i, were not essential for eIF3 activity."
- [PMID:17581632] Likely selective role: "Thus, these two subunits might be involved in translational control of specific mRNAs or in particular cellular conditions."
- [PMID:18599441] Architecture: "In our network, it interacts directly with the other RNA recognition motif (RRM)-containing subunit eIF3g."
- [PMID:25849773] Direct cellular RNA contacts: "After RNase digestion, separation of crosslinked eIF3–RNA complexes by denaturing gel electrophoresis demonstrated that four of the thirteen subunits crosslink directly to RNA"
- [PMID:25849773] Target scale: "eIF3a, b, d, and g crosslinking to 328, 264, 356, and 352 transcripts, respectively"
- [PMID:27462815] Direct c-JUN-UTR contact: "the four eIF3 RNA-binding subunits, eIF3a, b, d, and g, provide RNase protection to internally 32P-labeled c-Jun 5' UTR RNA upon UV254-induced crosslinking"
- [PMID:17094969] Apoptosis-linked interaction: "The direct interaction between AIF and eIF3g was confirmed in a GST pull-down assay and also verified by the results of co-immunoprecipitation and confocal microscopy studies."
- [PMID:23804756] Histone-mRNA machinery connection: "We confirmed the binding of SLIP1 to DBP5 and eIF3g by pull-down assays"
- [PMID:24396066] Nutrient-regulated Paip1 connection: "the interaction of PABP-interacting protein 1 (Paip1) with PABP and eukaryotic translation initiation factor 3 (eIF3; via the eIF3g subunit) further stimulates translation."
- [PMID:21347434] Holo-eIF3 viral context: "exogenous eIF3 specifically stimulated synthesis of the BM2fluc reinitiation product with all of the mRNAs tested"

## Curation implications

The core molecular function is mRNA binding (GO:0003729), while translation initiation factor activity is contributed in the eIF3 complex. General translational initiation and initiation-complex assembly remain valid biological-process annotations. Generic protein binding annotations are uninformative and should be marked over-annotated, not interpreted as separate molecular activities. Viral termination-reinitiation and AIFM1-dependent translational inhibition are context-specific rather than core.
