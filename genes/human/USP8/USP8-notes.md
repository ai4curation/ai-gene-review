# USP8 notes

## 2026-06-02

PITA context: USP8 corresponds to PITA4 / ACTH-producing corticotroph adenoma/Cushing disease. Pediatric Cushing disease work concluded that "Somatic USP8 gene mutations are a common cause of pediatric CD" and that mutations decrease EGFR degradation, leading to increased POMC and ACTH production [PMID:28505279 "Somatic USP8 gene mutations are a common cause of pediatric CD"; PMID:28505279 "decreased EGFR degradation, which in turn leads to increased POMC expression and ACTH production"].

Deep research status: `just deep-research-falcon human USP8 --fallback perplexity-lite` timed out on Falcon after 600 seconds, and the fallback failed with a Perplexity quota error. I proceeded using fetched UniProt, GOA, Reactome-derived references, and cached publications.

Functional summary: USP8/UBPY is a cysteine-type deubiquitinase. UniProt summarizes it as a "Hydrolase that can remove conjugated ubiquitin from proteins" [file:human/USP8/USP8-uniprot.txt "Hydrolase that can remove conjugated ubiquitin from proteins"]. The endosomal UBPY paper states "UBPY is a ubiquitin-specific protease" and that UBPY function is essential for growth factor receptor down-regulation [PMID:16520378 "UBPY is a ubiquitin-specific protease"; PMID:16520378 "UBPY function is essential for growth factor receptor down-regulation"]. The MIT-domain paper supports endosomal targeting: "essential for its localization to endosomes" [PMID:17711858 "essential for its localization to endosomes"].

Annotation decisions: I accepted deubiquitinase, protein deubiquitination, cytosol/cytoplasm, early endosome/endosome membrane, and endosome organization annotations as core or directly supportive. I kept cytokinesis/midbody, Wnt/FZD, BACE1, postsynaptic, and acrosomal contexts as non-core. Generic high-throughput `protein binding`, cadherin binding, dexamethasone response, and amyloid fibril formation were marked as over-annotated because they are indirect or too generic relative to the deubiquitinase/endosomal cargo-sorting mechanism.


## Paired horse benchmark evidence review

The human reference supplies mechanistic evidence for the corresponding selected horse protein; the human conclusion alone is not validation of the horse sequence. The exact horse comparison is in `genes/HORSE/USP8/USP8-bioinformatics/RESULTS.md`. Research reports are source leads; annotation decisions cite the underlying publication or experimentally supported UniProt passages. Unresolved source-specific results retain UNDECIDED.

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

Scope: full re-review of all 83 existing annotation rows, description and core functions for human USP8 (P40818), the paired human reference for the HORSE40 benchmark. ProtNLM2 output was not opened or used.

Identity: P40818 is the reviewed, canonical human USP8 entry (1118 aa; isoform 1 displayed). It is not a fragment or alternative gene model. It carries the full domain set: MIT (33-116), rhodanese (195-313), SH3-binding motif (405-413), the Ser718 14-3-3 motif region, and the USP catalytic domain (777-1109) with the catalytic Cys786 mutated in PMID:16520378 [file:human/USP8/USP8-uniprot.txt "FUNCTION, SUBCELLULAR LOCATION, AND MUTAGENESIS OF CYS-786."].

Evolutionary grounding: PANTHER PTHR21646:SF27 (UBIQUITIN CARBOXYL-TERMINAL HYDROLASE 8) contains human USP8 and mouse Usp8 (Q80U87) (interpro/panther/PTHR21646/PTHR21646-entries.csv). PAINT places GO:0004843 at the deep node PTN002538135 (USP family, many experimental donors including P40818), cytosol and midbody at PTN008371010 (donors MGI:1934029 mouse Usp8 and P40818), and Wnt potentiation at PTN002728602 (donors fly FBgn0038862 and P40818). The family review (PTHR21646-review.yaml) places USP8 in SF27 as its reference protein; no disagreement about subfamily placement. No module in modules/ contains USP8 (a grep hit in tca_cycle.yaml is S. pombe Q9USP8, unrelated).

Changes made:
- GO:0005515 protein binding rows brought into line with the protein-binding policy (MARK_AS_OVER_ANNOTATED / KEEP_AS_NON_CORE are not permitted). Rows whose partner is a 14-3-3 protein (YWHAZ, YWHAE, SFN; PMIDs 15161933, 15778465, 28514442, 33961781, 35271311, 36931259) -> MODIFY to GO:0071889 14-3-3 protein binding, grounded in the Ser718 phospho-motif [file:human/USP8/USP8-uniprot.txt "Phosphorylation of Ser-718 is essential for interaction with YWHAE"; file:human/USP8/USP8-deep-research-falcon.md "Ser718 phosphorylation permits 14-3-3 binding, which stabilizes autoinhibition."]. CHMP1A/CHMP1B/CHMP4C (MIT-domain ESCRT-III), NBR1, HIF1A/EPAS1 (substrate) and BIRC6 (substrate) rows -> REMOVE; no informative MF term for the USP8 side exists (searched OLS for ESCRT-III complex binding: none), and the functional consequences are already captured by localization and deubiquitinase rows.
- GO:0004843 IDA from PMID:18728397 (USP39 paper): previously UNDECIDED with a claimed PMID mismatch. That reasoning overruled an experimental annotation from an abstract-only cache. Changed to ACCEPT deferring to the curator: the claim is independently established and consistent with the other eight GO:0004843 rows.
- Added reference_review entries for the key primary references.
- Added a second core function: 14-3-3 protein binding as the phospho-regulated autoinhibition mechanism (Cushing disease hotspot).
- Other actions re-examined and retained: deubiquitinase, K48/K63 activities, endosome/early endosome/endosome membrane/cytosol as core; midbody/cytokinesis, Wnt, BACE1/lysosomal catabolism, plasma membrane, nucleus, synaptic and acrosome contexts as non-core; dexamethasone response, amyloid fibril formation and HDA cadherin binding as over-annotations; TAS cysteine-type endopeptidase -> MODIFY to deubiquitinase. No NEW terms proposed (cilium assembly from PMID:24378640 is downstream of HIF1A stabilisation and fails the participation test).

Relative to review next: mouse Usp8 (Q80U87, MGI:1934029), ortholog in the same PANTHER subfamily SF27 and a PAINT donor for the cytosol/midbody node; extensive knockout and acrosome biogenesis data. No genes/mouse/Usp8 review exists in the repo.
