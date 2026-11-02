# CG3515 evidence notes

Q9VQD1 is the 395-residue PA product of FBgn0031431 (AAF51244/NP_608687), with one protein-coding transcript. Its record contains `DR   InterPro; IPR037867; Swd2/WDR82.`; the family assignment is more diagnostic than generic WD40 repeats. [FlyBase](https://flybase.org/reports/FBgn0031431).

CG3515 is not Wdr82/CG17293 (FBgn0032030, Q9VLN1). The current FlyBase orthology table nevertheless places CG3515 with human WDR82 (7/14 DIOPT methods, best target score but not best reverse score). This is consistent with a diverged paralog and with the curated PAINT chromatin/COMPASS assignment. A paralog distinction warrants keeping direct experimental attribution accurate; it does not alone demonstrate loss of conserved nuclear localization.

[PMID:18838538](https://pubmed.ncbi.nlm.nih.gov/18838538/) establishes that human WDR82 associates with chromatin and Set1 complexes. The cached abstract directly supports that family property; full-text fetching encountered a publisher/browser restriction. The accessible primary search excerpt identifies CG17293 as the closest fly sequence, and is not represented as evidence that CG3515 itself was assayed. Nuclear localization and chromatin/COMPASS roles are accepted as conserved-family inferences. A specific CG3515 RNA-metabolic role remains unresolved; no histone methyltransferase activity is assigned to the WD-repeat subunit itself.

ProtNLM nucleus is CNN: this broad location is supported by nuclear-complex family biology and already occurs in the record. The original location score and donor metadata remain in the frozen prediction JSON.

Research-provider outcome: the default Falcon process timed out after 600 seconds. The configured perplexity-lite fallback returned HTTP 401 (`insufficient_quota`). The original Falcon child subsequently produced a complete report (614.92 seconds), which was inspected. Its CG3515/CG17293 distinction agrees with the identity analysis. It identified the primary comparative Swd2 analysis [PMID:15146080](https://doi.org/10.1261/rna.7090104), now cached as an abstract; the report's exact CG3515 alignment row has not been independently recovered from full text. The primary yeast study establishes dual chromatin and RNA-processing roles, while the present fly review treats chromatin/COMPASS as conserved-family inference and leaves specific RNA processing unresolved. The provider's absence of a direct fly assay does not itself refute the curated phylogenetic inference.

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

Identity: Q9VQD1 is the full-length, sole annotated product (PA, 395 aa) of CG3515 (FBgn0031431). It is not a fragment, isoform or alternative gene model. It is a separate locus from Wdr82 (CG17293, FBgn0032030, Q9VLN1, 317 aa).

Evolutionary placement: UniProt places Q9VQD1 in PANTHER PTHR19861:SF0 (WD REPEAT-CONTAINING PROTEIN 82), the same subfamily as fly Wdr82 and human WDR82 (Q6UXN9), per `interpro/panther/PTHR19861/PTHR19861-entries.csv`. The IBA rows come from PAINT node PTN000458398; Set1C/COMPASS donors include fly Wdr82 (FBgn0032030), human WDR82, both yeasts and Dictyostelium. The family review `interpro/panther/PTHR19861/PTHR19861-review.yaml` uses Q9VQD1 as the SF0 representative, so there is no disagreement about subfamily placement. It does make the somewhat odd choice of representing SF0 by the divergent paralog rather than by Wdr82 or WDR82.

New sequence comparison (`CG3515-bioinformatics/RESULTS-rereview.md`, script `compare_swd2_paralogs_rereview.py`): CG3515 is about 36% identical to fly Wdr82 and 35% to human WDR82, while fly Wdr82 and human WDR82 are 69% identical. CG3515 is therefore a rapidly diverging paralog, with a C-terminal extension of about 80 aa. FlyBase DIOPT lists Wdr82 as its top paralog (9/13 methods). The FlyBase testis-specificity index is 4.91 (scale -2.52 to 5.2), and Bgee reports expression in spermatocytes, so the gene is strongly testis-biased.

Literature: Mohan et al. 2011 [PMID:21875999 "Sequence searches and alignments of these proteins with human and yeast proteins revealed that CG17293 is very closely related to Wdr82"] purified fly Set1/COMPASS from S2 cells with tagged dWdr82 (CG17293). A grep of the cached full text finds no mention of CG3515. All fly Wdr82 functional data (COMPASS, H3K4me3) belong to CG17293. Absence from S2-cell complexes is not evidence of loss for a testis-biased paralog.

Decisions:
- GO:0003682 chromatin binding (IBA): ACCEPT, as a family inference with caveats.
- GO:0048188 Set1C/COMPASS complex (IBA): ACCEPT. The node placement is sound; whether a testis-specific variant complex exists is untested.
- GO:0005634 nucleus (IEA, ARBA): ACCEPT, on the basis of the family placement.
- GO:0016070 RNA metabolic process (IEA, ARBA): changed from UNDECIDED to MARK_AS_OVER_ANNOTATED. PAINT propagated no RNA-processing term from the Swd2/WDR82 node, and the RNA role is a yeast CPF function.

No NEW terms. The description was rewritten to state the paralog relationship and the testis bias.

Relative to review next: fly Wdr82 (CG17293, Q9VLN1), the experimentally characterised SF0 paralog that is the conserved WDR82 ortholog. The repo has no review of it, nor of human WDR82. Module: `modules/dmel_compass_family_complexes.yaml` lists Wdr82 (Q9VLN1), not CG3515.
