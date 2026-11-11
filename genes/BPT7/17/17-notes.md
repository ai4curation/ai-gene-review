# Bacteriophage T7 Gene 17 (Tail Fiber Protein gp17) — Curation Notes

## Overview
Bacteriophage T7 gene *17* (`P03748`, 553 aa, ~61.6 kDa) encodes the tail fiber protein gp17 [PMID:6864790]. Six homotrimers of gp17 (18 monomers per virion) attach to the head-proximal interface of the gp11-gp12 tail complex [PMID:22645347, PMID:23306440].

## Structural and Biochemical Functions
- **Homotrimeric Tail Fiber Assembly**: Each tail fiber is a homotrimer of gp17 (`GO:0042802`, `identical protein binding`; `GO:0098024`, `virus tail, fiber`) with an N-terminal tail-attachment domain (residues 1–149), a central coiled-coil/triple-β-helix shaft, and a C-terminal receptor-binding tip domain (residues 465–553) [PMID:8528255, PMID:22645347, PMID:23306440].
- **Host Lipopolysaccharide Recognition and Reversible Attachment**: In mature virions, the six fibers are folded back against the capsid and dynamically sample extended conformations; reversible binding of the C-terminal tip domains to the inner core heptose region of *Escherichia coli* rough lipopolysaccharide (LPS) orients the virion on the cell surface (`GO:0098671`, `adhesion receptor-mediated virion attachment to host cell`) prior to irreversible tail nozzle binding and DNA ejection [PMID:22645347, PMID:23306440].

## GO Annotation Review
- **Accept**: `GO:0042802` (`identical protein binding`, `IPI` from `PMID:22645347` and `PMID:8528255`), `GO:0098024` (`virus tail, fiber`, `IDA` from `PMID:22645347` and `IEA`), and `GO:0098671` (`adhesion receptor-mediated virion attachment to host cell`).
- **Modify**: Refine `GO:0019062` (`virion attachment to host cell`) and `GO:0046718` (`symbiont entry into host cell`) to `GO:0098671` (`adhesion receptor-mediated virion attachment to host cell`); refine `GO:0098015` (`virus tail`) to `GO:0098024` (`virus tail, fiber`).
