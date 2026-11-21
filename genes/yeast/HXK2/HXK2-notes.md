# HXK2 notes (P04807, YGL253W)

- Hexokinase PII, EC 2.7.1.1, main hexokinase on glucose [UniProt:P04807 "Reaction=a D-hexose + ATP = a D-hexose 6-phosphate + ADP + H(+);"]; long-term glucose repression requires Hxk2 [PMID:8917466 "long-term repression specifically requires Hxk2 on glucose and either Hxk1 or Hxk2 on fructose"].
- Nuclear pool: [PMID:9563516 "the HXK2 gene product, isoenzyme PII of hexokinase, is located in both the nucleus and the cytoplasm"]; proposed transcriptional role [PMID:11311123 "nuclear localization of Hxk2p is necessary for glucose-induced repression signalling of the HXK1 and GLK1 genes"].
- Contested: [PMID:37196001 "we find that Hxk2 is largely excluded from the nucleus under glucose-replete conditions but is retained in the nucleus under glucose-limiting conditions"] and [PMID:37196001 "RNAseq analyses of the yeast transcriptome dispels the idea that Hxk2 moonlights as a transcriptional regulator of glucose repression"].
- p53 heterologous model: mitochondrial association, apoptosis resistance via NADPH [PMID:31862471 "Enhanced association of HXK2 with the mitochondria"] — indirect.

Decisions: regulation of transcription by glucose UNDECIDED (disputed); nucleus rows KEEP_AS_NON_CORE; cell size HMP, apoptosis IMP, mitochondrial membrane IMP MARK_AS_OVER_ANNOTATED; same IEA/RCA treatment as HXK1.

## QA pass (2026-11-19)

- Regulation of transcription by glucose (IDA PMID:11311123): UNDECIDED -> MARK_AS_OVER_ANNOTATED. Lesko et al. full text: wild-type vs hxk2 deletion RNA-seq in high and low glucose [PMID:37196001 "However, we find that glucose repression is largely unaffected by hxk2Δ, suggesting that the small number of genes whose transcription changes in hxk2Δ cells are not representative of a global loss of glucose repression."]. A few genes (HXK1, SUC2) do change, so not REMOVE.
- IBA intracellular glucose homeostasis and IBA cytoplasmic side of mitochondrial outer membrane: same donor inspection as HXK1 (sensor-type Gck/HKDC1/AtHXK1 donors; anchor-bearing HK2/M4FD55 donors; yeast N-terminus MVHLGPKKPQARKGSMADVP has no anchor). propagation_review added.
- Generic parents -> TOO_GENERAL.
