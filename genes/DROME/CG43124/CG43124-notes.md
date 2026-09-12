# CG43124 / SPH249 review notes

## Finding

The released ProtNLM2 serine-type endopeptidase prediction for A0A0B4K7P3 is a supported pseudoenzyme-overannotation case. The exact current protein replaces two essential trypsin catalytic residues. The main GOA already contains explicit negative peptidase assertions, and these remain negative in the review.

## Identity and evidence provenance

[FlyBase FBgn0262587](https://flybase.org/reports/FBgn0262587) lists one transcript and one 245-residue protein, CG43124-PA / FBpp0293647 / A0A0B4K7P3 / NP_001247345. The downloaded report states "There is only one protein coding transcript and one polypeptide associated with this gene" and connects SPH249 to Cao and Jiang (2018). This is not an unresolved accession or isoform case. The current UniProt sequence is version 1 (2015-04-01); a separate prediction-time input sequence was not supplied by the release API.

[PMID:30367934](https://pubmed.ncbi.nlm.nih.gov/30367934/), Cao and Jiang, *Building a platform for predicting functions of serine protease-related proteins in Drosophila melanogaster and other insects*, DOI [10.1016/j.ibmb.2018.10.006](https://doi.org/10.1016/j.ibmb.2018.10.006), is cached with full text. Its methods state: "The SP-related sequences in each species were divided into SPs or SPHs based on the presence or absence of the His-Asp-Ser catalytic triad" (line wrapping normalized here). The exact SPH249 supplemental-table row was not accessible and is not represented as independently read. The study is a sequence/family analysis, not an experimental activity assay on CG43124.

The target UniProt PROSITE caution is a useful lead but does not by itself identify the missing chemistry. The [reproducible analysis](CG43124-bioinformatics/RESULTS.md) independently maps catalytic His/Asp to Ser69/Asn112 within a significant Pfam match. The third triad position is not reliably mapped, and no precise third-site defect is asserted. A successful active-trypsin control verifies that the mapping procedure recovers the triad when present.

The source ProtNLM2 record and all model metadata are preserved in `CG43124-protnlm-source.json`. The activity prediction score is 0.98; the reported phmmer donor is Q90WD8, Bufo japonicus ovochymase-2, score 52.1. The trypsin fold supports homology, but donor catalytic activity cannot override target catalytic substitutions. The source also predicts secretion and the name Trypsin; this sidecar covers the benchmark GO hypothesis. ARBA's family/CLIP assertion and generated review prose are not used as biological validation.

## Main annotation decisions

All eight seeded GOA rows are reviewed. Both `negated: true` rows (serine-type endopeptidase and peptidase activities) are accepted as negative statements, supported by the reproduced catalytic-residue analysis. A positive prediction matching the GO identifier of a negative annotation is a contradiction, not annotation agreement or CNN.

The extracellular IBA is supported by the sequence's N-terminal signal peptide and absence of evidence against the ancestral transfer. The innate-immune IBA is retained as a curated phylogenetic process inference; no argument is made from donor counts. Loss of protease catalysis does not abolish possible noncatalytic immune function. A native molecular activity is not invented to fill `core_functions.molecular_function`.

The generic InterPro-to-proteolysis IEA is marked overannotated. An inactive homolog could participate as a protease-cascade cofactor, but neither the fold nor the broad immune IBA establishes that specific process mechanism. This distinction avoids equating absence of catalytic activity with impossibility of process participation. Component and process ND root placeholders are removed in favor of retained informative annotations; the MF uncertainty marker is kept as non-core.

## Research status and limitations

Falcon deep research was launched with perplexity-lite fallback concurrently with publication caching. The direct findings above are grounded in the cached primary methods, downloaded database identity/features and reproducible sequence analysis, independent of provider output. No direct CG43124 biochemical inactivity, binding-partner or infection-challenge experiment was identified in these sources.

Falcon completed successfully in 406 seconds; its report and artifact are retained. It found no exact-gene functional experiment and gives useful family background, but it did not inspect the target catalytic residues or its signal peptide and does not cite the 2018 family study supporting the existing IKR. It also carries forward a CLIP-subfamily label supplied from ARBA; no independently identified clip domain is demonstrated for this short protein. Consequently its generalized uncertainty does not outweigh the reproduced His/Asp substitutions or target-specific secretion feature. The native mechanism remains open. The validator advisory about not citing the deep-research report in annotations is intentionally retained: decisive annotation support is cited to the underlying primary methods, target record and explicit analysis instead of this uncomputed family survey.
