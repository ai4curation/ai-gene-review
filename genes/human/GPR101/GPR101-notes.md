# GPR101 notes

## 2026-06-02

PITA context: GPR101 corresponds to PITA2 / X-linked acrogigantism. UniProt describes PITA2 as "a growth hormone-secreting benign neoplasm" and ties excess growth hormone before epiphyseal closure to gigantism [file:human/GPR101/GPR101-uniprot.txt "PITA2 is a growth hormone-secreting benign neoplasm"].

Deep research status: `just deep-research-falcon human GPR101 --fallback perplexity-lite` timed out on Falcon after 600 seconds, and the fallback failed with a Perplexity quota error. I proceeded using fetched UniProt, GOA, and cached publications.

Functional summary: GPR101 is best reviewed as an orphan class A GPCR. UniProt states "FUNCTION: Orphan receptor" and "SUBCELLULAR LOCATION: Cell membrane; Multi-pass membrane protein" [file:human/GPR101/GPR101-uniprot.txt "FUNCTION: Orphan receptor."; file:human/GPR101/GPR101-uniprot.txt "SUBCELLULAR LOCATION: Cell membrane; Multi-pass membrane protein."]. The GPCR activity and plasma membrane annotations are therefore accepted. The IBA "adrenergic receptor signaling" term was modified to the broader non-adrenergic GPCR adenylate cyclase term because GPR101 is not an adrenergic receptor.

Evidence cautions: The HuRI protein-binding annotation is high-throughput context, not a functional statement; the source describes a reference map with "52,569 verified PPIs involving 8,275 proteins" [PMID:32296183 "contains 52,569 verified PPIs involving 8,275 proteins"]. The SNX/PX-FERM source supports broad receptor-cargo trafficking, noting "RTKs, integrins, GPCRs" as putative cargo classes [PMID:23382219 "These proteins include RTKs, integrins, GPCRs"], but does not by itself establish GPR101 core function.

