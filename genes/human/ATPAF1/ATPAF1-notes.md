# ATPAF1 notes

## 2026-10-05 review (PAINT, affinage)

- F1 assembly chaperone (Atp11 homolog) [PMID:11410595 "Here we report the isolation of the cDNAs and the characterization of the human genes for Atp11p and Atp12p and show that the human proteins function like their yeast counterparts."].
- Mouse knockout [PMID:34375736 "Western blots and Blue-Native electrophoresis (BN-PAGE) demonstrated a decreased F1 content and ATP synthase dimers in the Atpaf1-KO heart."].
- Accepted: complex-stabilizing activity, F1/ATP synthase assembly and mitochondrion. The inner-membrane rows (IEA and mouse ISS) are non-core, because the mouse basis is IF colocalization only.
- Four ATP5F1B IPI rows (chaperone-client) removed under policy. The stub collapses two PMID:11410595 GOA rows into one entry.

## 2026-10-05 revision (reviewer round 1)

- Removed "(yeast two-hybrid)" from the PMID:11410595 IPI summary: the cached abstract states no assay.
- The inner-membrane rows now say the mouse donor's basis is not traced; UniProt's "Peripheral membrane protein" (by similarity) is quoted, and the Q811I0 source_status is UNRESOLVED.
- GO:0140777 now also cites the HEK293 co-IP of endogenous F1 beta with ATPAF1 (PMID:34375736). GO:0065003 is worded as a general ancestor, not core. PMID:12965202 relevance raised to MEDIUM. The holdase/chaperone MF (GO:0044183) is raised as a question. Label casing is fixed (builder used str.capitalize).
