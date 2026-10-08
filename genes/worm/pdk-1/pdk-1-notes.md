# pdk-1 (Q9Y1J3) review notes

Deep research: falcon run failed (timeout/connection reset; perplexity fallback unavailable). Review based on cached publications, UniProt and PubMed.

## Key findings
- Necessary and sufficient relay from AGE-1 to AKT [PMID:10364160 "Therefore, pdk-1 activity is both necessary and sufficient to propagate AGE-1 PI3K signals in the DAF-2 insulin receptor-like signaling pathway."]
- [PMID:10364160 "This indicates that the major function of C. elegans PDK1 is to transduce signals from AGE-1 to AKT-1 and AKT-2."]
- Activates SGK-1 [PMID:15068796 "SGK-1 forms a protein complex with the AKT kinases, and is activated by and strictly depends on PDK-1."]
- PH-less PIAK form phosphorylates AKT Thr308 [PMID:11274160 "PIAK phosphorylates mammalian AKT/PKB at the activating Thr(308) residue in the presence of the phosphatidylinositol (PI) 3-kinase inhibitors as well as in the absence of growth factors."]

## Curation decisions
- Core MF kept as protein serine/threonine kinase activity (GO:0004674). GO:0004676 (3-phosphoinositide-dependent protein kinase activity) not proposed because UniProt annotates no PH domain on this entry and the PIAK form is phospholipid-independent.
- Cellular response to ROS (PMID:28632756) marked over-annotated: the paper assays cadmium-inducible mtl-1 transcription, not ROS.
- ARBA IEA developmental-growth / gross-anatomy / oxygen-compound terms marked over-annotated.
