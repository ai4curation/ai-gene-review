# VDAC2 manual literature synthesis

Automated deep-research providers were not used for this family review; this synthesis is based on the
cached publications, the UniProtKB record, the existing VDAC1 review in this repository, and the seeded GOA
evidence.

## Core activity and location

VDAC2 is a voltage-dependent anion channel of the mitochondrial outer membrane. Human VDAC2 cDNA was cloned
with HVDAC1 and, after expression in yeast lacking endogenous VDAC, the isolated human protein formed
VDAC-like channels in planar bilayers [PMID:8420959]. Epitope-tagged human VDAC1 and VDAC2 localized
exclusively with mitochondrial markers in COS7 cells and rat astrocytes, arguing that both isoforms are
outer-mitochondrial-membrane beta barrels [PMID:7539795]. UniProtKB summarizes the open state as weakly
anion-selective and records chloride and potassium channel activity, lipid binding, and mitochondrial
outer-membrane localization [file:human/VDAC2/VDAC2-uniprot.txt].

VDAC2 also has a second direct transport activity: as a dimer, it scrambles phospholipids across the
mitochondrial outer membrane. Purified human VDAC2 reconstituted into liposomes translocated both
phosphatidylinositol and phosphatidylcholine analogs, and the paper concluded that human VDAC1 and VDAC2
dimers catalyze rapid transbilayer phospholipid movement independently of channel conduction
[PMID:38065946].

## Lipid binding and apoptosis

Photoactivatable ceramide labeling of isolated mitochondria identified VDAC1 and VDAC2, but not VDAC3 or
TOM40, as mitochondrial ceramide-binding proteins. Molecular dynamics and mutagenesis localized the VDAC2
ceramide-binding site around Glu84; VDAC2 knockout or replacement with the E84Q mutant made cells largely
resistant to ceramide-induced mitochondrial outer-membrane permeabilization and apoptosis, supporting a
direct VDAC2 role in ceramide-triggered MOMP [PMID:31015432].

## Peripheral or lower-confidence contexts

VDAC2 was also identified in a human sperm-head zona-pellucida-binding screen: recombinant ZP2 and ZP3
co-precipitated VDAC2 from human sperm extracts, consistent with an acrosomal/sperm-head pool that is
peripheral relative to the mitochondrial channel [PMID:23355646]. An erythrocyte study detected VDAC
isoforms in mature red-blood-cell membranes and proposed a TSPO2-VDAC complex that influences ZnPPIX uptake
during Plasmodium infection; this supports a minor non-mitochondrial membrane pool but does not change the
core mitochondrial function [PMID:27641616]. VDAC2 appeared in mitochondrial nucleoid fractions in a
proteomic study [PMID:18063578], best treated as a retained peripheral association of an abundant
outer-membrane channel rather than as a nucleoid-specific function.

High-throughput IntAct rows supply many bare `GO:0005515 protein binding` annotations, including large
interaction screens and VDAC self/heteromer interactions. The interactions are not disputed here, but bare
protein binding is uninformative as a GO molecular function and is removed under the project policy.
