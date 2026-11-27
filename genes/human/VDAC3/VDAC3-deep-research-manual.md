# VDAC3 manual literature synthesis

Automated deep-research providers were not used for this family review; this synthesis is based on the
cached publications, the UniProtKB record, the existing VDAC1 review in this repository, and the seeded GOA
evidence.

## Core activity and location

VDAC3 is the third mammalian voltage-dependent anion channel isoform. The original human VDAC3 paper cloned
a cDNA corresponding to mouse MVDAC3 and reported wide tissue expression with the highest signal in testis
[PMID:9781040]. Later electrophysiology showed that purified human and mouse VDAC3 form stable,
high-conductance, voltage-gated channels similar to VDAC1 and weakly selective for anions; VDAC3 therefore
shares the outer-membrane metabolite/ion-channel activity of the family while retaining distinctive
regulation by cytosolic tubulin and alpha-synuclein [PMID:31935282].

GOA also carries several mitochondrial outer-membrane rows from PAINT, InterPro/UniProt, VDAC1 similarity,
and Reactome PINK1/PRKN mitophagy events. No PAINT IRD or IKR currently blocks the VDAC3 lineage. These
rows agree with the VDAC family role as mitochondrial beta-barrel channels.

## Peripheral contexts

Mouse Vdac3 has a sperm-specific role in male fertility and mitochondrial sheath formation, and UniProtKB
summarizes this as an orthology-supported process for human VDAC3 [file:human/VDAC3/VDAC3-uniprot.txt].
Because the current human GOA rows are ISS from mouse rather than direct human reproductive evidence, the
spermatogenesis and sperm mitochondrial sheath assembly rows are retained as non-core.

Several rows are broader or less well supported. The 1998 VDAC3 cloning abstract says the family is
believed to control adenine nucleotide movement across the outer membrane, but `GO:0015853 adenine
transport` names transport of the free base adenine, not ATP, ADP, or AMP [PMID:9781040]. High-throughput
nuclear and exosome localizations are treated as over-annotations of an abundant mitochondrial membrane
protein. VDAC3 interacts with VDAC1 and VDAC2 in high-throughput datasets, but the seeded annotations are
bare `GO:0005515 protein binding` and are removed under the project policy.
