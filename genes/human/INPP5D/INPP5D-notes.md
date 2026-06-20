# INPP5D curation notes

## 2026-06-19

- Deep-research attempt with `just deep-research-falcon human INPP5D --fallback perplexity-lite` timed out after 180 seconds with no generated research artifact, so this manual review uses cached UniProt, GOA, Reactome, PANTHER family, and publication evidence.
- INPP5D encodes SHIP1, a hematopoietic SH2-domain inositol/phosphatidylinositol 5-phosphatase. UniProt summarizes its core biochemical role as hydrolysis of the 5-phosphate of PtdIns(3,4,5)P3 to PtdIns(3,4)P2, thereby negatively regulating PI3K pathways in immune and hematopoietic cells.
- The original SIP/SHIP work supports PtdIns(3,4,5)P3 and Ins(1,3,4,5)P4 5-phosphatase activity and association with Shc/Grb2 signaling complexes after B-cell activation [PMID:8723348 "The SIP proteins hydrolyzed phosphatidylinositol"]. This is core evidence for PIP3/IP4 phosphatase activity and immune-receptor signaling context.
- Independent cloning of hp51CN/SHIP supports Ins(1,3,4,5)P4 and PtdIns(3,4,5)P3 hydrolysis, but not Ins(1,4,5)P3 in that assay [PMID:8769125 "PtdIns(3,4,5)P3 hydrolyzing activity"]. I accepted the current IP3 5-phosphatase annotation because the current UniProt record has newer enzymology support, but the core function remains PIP3/IP4 5-phosphatase activity.
- The 2000 phospholipid-specific 5-phosphatase study is not primarily about INPP5D, but its abstract explicitly notes that SHIP also hydrolyzes PtdIns(4,5)P2 under assay conditions [PMID:10764818 "SHIP, a 5-phosphatase previously characterized"].
- SHIP1 recruitment to phosphorylated inhibitory motifs is part of the core mechanism by which it attenuates immune receptor signaling. TIGIT recruits Grb2 and SHIP1 and SHIP1 silencing abolishes TIGIT/PVR-mediated killing inhibition [PMID:23154388 "SHIP1 silencing can dramatically abolish TIGIT/PVR-mediated killing inhibition"].
- B-cell and Fc-receptor inhibitory contexts support SHIP1 phosphotyrosine-motif recognition. FCRL3 coligation inhibits BCR signaling and its ITIM-like motif recruits SHIP [PMID:19843936 "SHIP with the ITIM-like motif at 662"]. Human FcgammaRIIb P-ITIM peptide also binds SHIP in lysates [PMID:10382761 "P-ITIM peptide bindes SHP-2 and SHIP"].
- Additional immune checkpoint/receptor papers support phosphotyrosine-dependent recruitment but generic `protein binding` is too broad. I modified several of these to `phosphotyrosine residue binding` rather than accepting generic protein binding.
- Some protein-binding annotations are over-annotations or unclear. CIN85/SODD and proteome-scale interactome papers are not core SHIP1 functions; the CD300a/IRp60 mast-cell paper is abstract-only and does not name SHIP1, so I left that annotation UNDECIDED. The NKG2A paper explicitly states NKG2A phospho-ITIMs associate with SHP-1/SHP-2 "but not with the polyinositol phosphatase SHIP", so that protein-binding annotation was removed [PMID:9485206 "but not with the polyinositol phosphatase SHIP"].
- The Reactome `phosphatidylinositol biosynthetic process` and `phosphatidylinositol-3,4,5-trisphosphate 3-phosphatase activity` annotations do not describe INPP5D's 5-phosphatase chemistry. I marked these MODIFY to phosphatidylinositol dephosphorylation or PtdIns(3,4,5)P3 5-phosphatase activity.
- Immune differentiation and effector-process annotations such as B-cell differentiation, neutrophil differentiation, osteoclast/bone resorption, TCR signaling, and NK cytotoxicity are plausible or experimentally supported outcomes of SHIP1 immune signaling but are secondary to the core catalytic mechanism.

## 2026-06-20 Second-Pass Review Notes

Second-pass audit confirmed the existing action calls and reference-review
coverage. No YAML changes were needed in this pass.

The REMOVE action for the NKG2A protein-binding annotation remains appropriate:
the cached PMID:9485206 abstract explicitly reports association with SHP-1/SHP-2
but not SHIP, directly contradicting an INPP5D/SHIP1 interaction. This is a
genuine evidence contradiction, not a case of incomplete curator evidence.

The two remaining UNDECIDED protein-binding annotations remain appropriate. For
PMID:9148918 and PMID:16339535, the cached abstracts do not expose
SHIP1-specific evidence even though the GO annotations are experimental. Per
project policy, these should not be removed without full-text review.

The core function remains SHIP1-mediated PtdIns(3,4,5)P3 and soluble inositol
polyphosphate 5-phosphatase activity, recruited by phosphotyrosine motifs to
immune-receptor signaling complexes. Alzheimer relevance should be represented
through microglial phosphoinositide signaling thresholds and receptor-proximal
immune regulation, not as a generic disease-progression function.
