# USP8 notes

## 2026-06-02

PITA context: USP8 corresponds to PITA4 / ACTH-producing corticotroph adenoma/Cushing disease. Pediatric Cushing disease work concluded that "Somatic USP8 gene mutations are a common cause of pediatric CD" and that mutations decrease EGFR degradation, leading to increased POMC and ACTH production [PMID:28505279 "Somatic USP8 gene mutations are a common cause of pediatric CD"; PMID:28505279 "decreased EGFR degradation, which in turn leads to increased POMC expression and ACTH production"].

Deep research status: `just deep-research-falcon human USP8 --fallback perplexity-lite` timed out on Falcon after 600 seconds, and the fallback failed with a Perplexity quota error. I proceeded using fetched UniProt, GOA, Reactome-derived references, and cached publications.

Functional summary: USP8/UBPY is a cysteine-type deubiquitinase. UniProt summarizes it as a "Hydrolase that can remove conjugated ubiquitin from proteins" [file:human/USP8/USP8-uniprot.txt "Hydrolase that can remove conjugated ubiquitin from proteins"]. The endosomal UBPY paper states "UBPY is a ubiquitin-specific protease" and that UBPY function is essential for growth factor receptor down-regulation [PMID:16520378 "UBPY is a ubiquitin-specific protease"; PMID:16520378 "UBPY function is essential for growth factor receptor down-regulation"]. The MIT-domain paper supports endosomal targeting: "essential for its localization to endosomes" [PMID:17711858 "essential for its localization to endosomes"].

Annotation decisions: I accepted deubiquitinase, protein deubiquitination, cytosol/cytoplasm, early endosome/endosome membrane, and endosome organization annotations as core or directly supportive. I kept cytokinesis/midbody, Wnt/FZD, BACE1, postsynaptic, and acrosomal contexts as non-core. Generic high-throughput `protein binding`, cadherin binding, dexamethasone response, and amyloid fibril formation were marked as over-annotated because they are indirect or too generic relative to the deubiquitinase/endosomal cargo-sorting mechanism.

