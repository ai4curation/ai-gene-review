# RUVBL1 notes

## 2026-11-22 RUVBL family review

Deep research did not leave a usable archived `RUVBL1-deep-research-*.md` provider file in this checkout, so this pass used the seeded UniProt/GOA files, cached publications, the existing INO80/SRCAP/TIP60 module reviews, and the existing GO-CAM index.

Curated RUVBL1 as one half of the essential RUVBL1-RUVBL2 AAA+ ATPase ring. The highest-confidence conserved functions are the ring's structural and ATP-hydrolyzing roles in INO80 chromatin remodeling, SRCAP/SWR1 H2A.Z exchange, metazoan NuA4/TIP60/p400, and the R2TP/PAQosome co-chaperone used for box C/D snoRNP and other quaternary client assembly. No production GO-CAM indexed locally contains RUVBL1 or RUVBL2, while `modules/ino80_complex.yaml`, `modules/srcap_h2az_deposition.yaml`, and `modules/tip60_p400_complex.yaml` already model the main chromatin modules.

Decision points:

- Removed all bare `GO:0005515` protein binding rows under the project protein-binding policy. Many of the interactions are plausible, but a generic binding row does not name the RUVBL1 activity; the useful signal is captured by complex membership where the interaction supports INO80, SRCAP, TIP60/p400, or R2TP/PAQosome.
- Kept ATP binding and ATP hydrolysis as core molecular activities, backed by biochemical and cryo-EM evidence for human RUVBL1/RUVBL2 heterohexamers.
- Accepted INO80, Swr1/SRCAP, NuA4/TIP60, R2TP, RPAP3/R2TP/prefoldin-like, and broader protein-folding chaperone complex rows where they describe a stable RUVBL-ring assembly.
- Treated DNA helicase and ATP-dependent DNA-acting activity as over-annotations: RUVBL proteins are AAA+ ATPases named after bacterial RuvB, but the assembled human TIP48/TIP49 complex lacked detectable DNA helicase or branch-migration activity in later direct assays.
- Kept telomerase, DNA replication, DNA repair, Wnt signaling, TBP binding, cytosol/cytoplasm, and broad transcriptional outcomes as non-core contextual roles rather than expanding them with process `NEW` rows.
- Marked membrane, centrosome, ciliary basal body, dynein axonemal particle, MLL1 complex, ribonucleoprotein complex, Cajal-body telomerase RNA localization, spermatogenesis, embryonic development, and cell-cycle rows as over-annotations when they looked too specific, too phenotypic, or disconnected from a direct RUVBL1/RUVBL2 assembly.
