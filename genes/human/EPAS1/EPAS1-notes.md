# EPAS1 manual review notes

`just deep-research-perplexity-lite human EPAS1` could not run in this
environment because the Perplexity provider was unavailable (`Available:
claude_code` only; `agentapi` was not on `PATH`). I therefore used the cached
UniProt, GOA, Reactome and publication files rather than creating a fake
provider deep-research file.

EPAS1 encodes HIF-2alpha, an oxygen-regulated bHLH-PAS HIF alpha subunit. The
founding EPAS1 paper cloned the gene, showed that EPAS1 binds and activates an
erythropoietin HRE reporter, and showed that EPAS1 forms an ARNT-containing
heterodimer before target-gene transcriptional activation [PMID:9000051, "EPAS1
forms a heterodimeric complex with the aryl hydrocarbon nuclear transporter"].
Direct HIF-2alpha/ARNT PAS-B structural work supports this heterodimeric
interface [PMID:16181639, "mutations in the solvent-exposed beta-sheet surface
of the HIF-2alpha domain not only disrupt this interaction"].

Endogenous HIF-2alpha ChIP-seq in human cells shows chromatin occupancy at
HIF-1beta-positive sites during hypoxia [PMID:30429208, "Here, we report on the
pan-genomic distribution of isoform-specific HIF binding in response to
hypoxia"], while Reactome records EPAS1-containing HIF complexes in nuclear
target-gene binding and CBP/p300 recruitment events. The Reactome and UniProt
cytosolic rows describe oxygen-regulated HIF-alpha hydroxylation, VHL binding,
ubiquitination, and proteasomal degradation; I treated those as non-core
trafficking/turnover locations rather than as the chromatin-bound core
transcription-factor activity.

The mouse adipocyte paper supports a real tissue-specific Epas1 role in BAT
thermogenesis during obesity, with UCP1 loss and a VEGF-rescuable BAT phenotype
[PMID:26572826, "VEGF treatment reversed the enhanced weight of obese BAT due
to adipocyte HIF2alpha deficiency"]. I therefore kept the cold-induced
thermogenesis rows as non-core. In contrast, the neddylation paper is
abstract-only in the cache and the abstract names HIF1A, VHL, DCNL1 and CUL2
but not EPAS1/HIF-2alpha, so the EPAS1 protein-neddylation rows need the full
text before they can be decided.
