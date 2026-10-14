# CFAP221 functional review

## 2026-10-10 — substantive ClinGen campaign review

This review retains the 25 normally seeded assertions and all four UniProt alternative products. The normal source contains 26 GOA records: two cytoplasm ISS records differ only in annotation date and project to one identical review object. No source row was manually deleted. The original UniProt/GOA bytes and every seeded source field are preserved.

The review follows the [published campaign instruction](https://github.com/ai4curation/ai-gene-review/blob/5b6c5bc6df4d274e22094cd1a65a6901664a56e5/projects/CLINGEN_MENDELIAN.md#curation-instructions). The approved campaign binding instruction governs supported generic binding; this gene already has a specific calmodulin-binding MF. No NEW annotation, process or molecular activity is proposed.

### Calmodulin binding and ciliary movement

The load-bearing biochemical source is [PMID:20421426](https://doi.org/10.1083/jcb.200912009), Figure 2 and the cloning/gel-overlay Methods. The mammalian constructs were made from mouse testis cDNA, not human cDNA. A bacterial mouse Pcdp1 fragment spanning residues 447–530 binds calmodulin in high calcium; the predicted C-terminal IQ region does not. Algal FAP221 fragments and binding-site mutants establish the corresponding interaction. This supports the existing mouse and Chlamydomonas ortholog transfers without inventing a direct assay of each human product.

That study perturbs FAP74 rather than FAP221. FAP221 still assembles into those algal axonemes, but its calmodulin association and other complex components are disturbed. The motility and C1d phenotypes therefore describe the complex context. They do not show that CFAP221 is a dynein motor, an ATPase, or the sole determinant of the entire C1d structure. The exact molecular link between calcium-dependent binding and beat regulation remains a question.

[PMID:31636325](https://doi.org/10.1038/s10038-019-0686-1) provides direct human airway evidence. Full Results and Figure 2 describe cilia that are present and vigorously beating, with no obvious routine TEM defect, but a significantly abnormal circular waveform. The frequency difference is not significant (p = 0.16). Consequently the original cilium-assembly IMP is refined to cilium movement, preserving its source fields. Predominantly axonemal localization is reported in differentiated human airway cells; the main text describes Supplementary Figure 2C, whose image pixels were not independently inspected.

### Assembly varies with context

[PMID:18039845](https://doi.org/10.1128/MCB.00354-07), full Methods/Results and Figures 2–4, demonstrates absent mature sperm flagella and occasional abortive tails in mouse loss-of-function, rescued by a BAC carrying Pcdp1. Mouse airway cilia remain present and ultrastructurally ordinary but beat more slowly. The same paper directly stains human respiratory and ependymal cilia in Figure 7; its cytoplasmic staining caveat in mutant mice is retained.

[PMID:32704025](https://pubmed.ncbi.nlm.nih.gov/32704025/) adds mouse genetic interaction evidence involving Cfap221, Cfap54 and Spef2. Selected Results and Discussion distinguish intact airway cilia from aborted sperm flagellar maturation. Double-mutant phenotypes are not attributed exclusively to CFAP221. The inherited and broad electronic assembly annotations are retained as non-core with this developmental scope; they do not assert that human airway ciliogenesis always requires CFAP221. PAINT node PTN002507401 is preserved, with historical node reconstruction explicitly unresolved.

[PMID:40250778](https://doi.org/10.1016/j.bbadis.2025.167855) independently reports altered airway beating and reduced bead transport in a human patient, while sperm motility and much sperm morphology remain within normal ranges. Selected full Methods 2.4–2.11 and Results 3.2–3.4 were read in the [authentic author-uploaded article](https://www.researchgate.net/publication/390865523_A_novel_pathogenic_variant_of_CFAP221_is_a_cause_of_a_mild_form_of_primary_ciliary_dyskinesia). The normal cache remains abstract-only; this does not mean full text was unavailable to the review. Planarian homolog RNAi is a separate supporting model. The CFAP221 antibody was nonspecific in that paper's IF experiment; absent protein was assessed by immunoblot. This assay-specific limitation does not invalidate distinct HPA or earlier antibody experiments.

### Localization provenance

The exact mouse A9Q751 manchette donor is grounded in [PMID:29690537](https://pubmed.ncbi.nlm.nih.gov/29690537/), full Results Section 2.4/Figure 8A. Pcdp1 is directly stained in mouse elongating spermatids in a Spag17-perturbation study. This supports location, not a claim that CFAP221 itself carries out intramanchette transport.

The [current HPA target record](https://www.proteinatlas.org/ENSG00000163075-CFAP221/subcellular) supplies four exact imaging mappings. HPA042501 in human sperm maps connecting piece and flagellar centriole to GO:0120212 and GO:0005814. HPA054164 in serum-starved hTERT-RPE1 cells maps primary cilium and its tip to GO:0005929 and GO:0097542. Both assays are marked approved by HPA. The selected images were visually inspected; their source labels are retained rather than treating image resolution alone as proof of suborganelle architecture. These localizations are non-core because their particular molecular functions remain unestablished.

[CFAP221-source-evidence.json](CFAP221-source-evidence.json) contains the exact source objects, donor identities and selected GOA assertions, HPA antibody/cell/GO mappings, official ontology/family data, and source URLs and hashes. It is a literal provenance extract, not a custom functional prediction. Shared database and literature provenance is not independent replication. The external author-article receipt and the unmodified normal cache are distinguished.

### Research and validation scope

Normal fetch produced the authentic seed, UniProt, GOA, family and publication files. The genuine default Falcon attempt timed out at 90 seconds; the explicit Perplexity-lite fallback returned quota HTTP 401. No provider report was created or replaced with authored prose. Manual primary research continued.

All supporting-text excerpts are short exact cache substrings; repeated anchors count toward the aggregate limit of 25 newly authored words per source. This notes file adds no primary-text quotation. There was no pre-existing gene journal to preserve. Normal computed status describes the annotation artifact; campaign completion still requires the approved-head, successful-check and merge gate.

Normal validation and rendering pass. Two action-consistency advisories are retained intentionally: the HPA primary-cilium location has a different functional scope from the motile-cilium literature, and the source-specific human movement refinement differs from the retained mouse-supported assembly assertions. Neither advisory changes the source fields or requires flattening the experimental contexts into one action.
