# pdk-1 (Q9Y1J3) review notes

Deep research: falcon run failed (timeout/connection reset; perplexity fallback unavailable). Review based on cached publications, UniProt and PubMed.

## Key findings
- Necessary and sufficient relay from AGE-1 to AKT [PMID:10364160 "Therefore, pdk-1 activity is both necessary and sufficient to propagate AGE-1 PI3K signals in the DAF-2 insulin receptor-like signaling pathway."]
- [PMID:10364160 "This indicates that the major function of C. elegans PDK1 is to transduce signals from AGE-1 to AKT-1 and AKT-2."]
- Activates SGK-1 [PMID:15068796 "SGK-1 forms a protein complex with the AKT kinases, and is activated by and strictly depends on PDK-1."]
- PH-less PIAK form phosphorylates AKT Thr308 [PMID:11274160 "PIAK phosphorylates mammalian AKT/PKB at the activating Thr(308) residue in the presence of the phosphatidylinositol (PI) 3-kinase inhibitors as well as in the absence of growth factors."]

## Curation decisions
- Core MF is 3-phosphoinositide-dependent protein kinase activity (GO:0004676), proposed as NEW (GOA carries only the parent GO:0004674). An earlier draft declined it on the grounds that UniProt annotates no PH domain; that was wrong. The UniProt entry has no FT DOMAIN line for the PH domain, but cross-references a PDK1-type PH domain (CDD cd01262 PH_PDK1, Gene3D 2.30.29.30, InterPro IPR033931 PDK1-typ_PH, Pfam PF14593, SMART SM00233) [file:worm/pdk-1/pdk-1-uniprot.txt "InterPro; IPR033931; PDK1-typ_PH."], and the PIAK paper defines PIAK by lacking the PH domain that PDK-1 has [PMID:11274160 "PIAK is highly homologous to C. elegans and mammalian PDK 1 with the exception that the novel kinase lacks a phospholipid binding pleckstrin homology domain."]. Comparators: Drosophila Pdk1 review uses GO:0004676 as core MF; human PDPK1 (O15530) has GO:0004676 by IDA (PMID:9368760, QuickGO). The PH-less PIAK form is phospholipid-independent and is covered by the accepted GO:0004674 rows.
- Cellular response to ROS (PMID:28632756) marked over-annotated: the paper assays cadmium-inducible mtl-1 transcription, not ROS.
- ARBA IEA developmental-growth / gross-anatomy / oxygen-compound terms marked over-annotated.
