# TTC28 notes

## 2026-05-29 - PROTEOSTASIS PN HSP90-cochaperone pass

- PN places TTC28 under `Cytonuclear proteostasis > Chaperone > HSP90 system > HSP90 cochaperone > TPR domain containing`, which would currently propagate `GO:0051879 Hsp90 protein binding`.
- The existing local review and UniProt-supported biology instead point to TTC28/TPRBK as a large TPR mitotic scaffold that localizes to centrosomes, spindle poles, spindle midzone, and midbody, and interacts with AURKB during mitosis and cytokinesis [PMID:23036704 "TPRBK binds to Aurora B"; PMID:23036704 "essential for the formation and integrity of the midbody"].
- The newer CMA paper supports a proteostasis-adjacent role, but it is HSPA8-mediated substrate biology rather than HSP90 cochaperone activity. TTC28 TPR domains bind the HSPA8 C-terminal PTIEEVD motif, and TTC28 is degraded through CMA/microautophagy [PMID:39630868 "TTC28 directly interacts with HSPA8"; PMID:39630868 "TTC28 is not only an HSPA8-mediated CMA/microautophagy substrate"].
- Working curation conclusion: do not propagate `GO:0051879 Hsp90 protein binding` to TTC28 from the PN HSP90-cochaperone bucket. If a gene-level binding annotation is pursued, the supported chaperone partner is HSPA8/HSC70, while the stronger core function remains mitotic scaffold/AURKB-associated cell-division biology.
