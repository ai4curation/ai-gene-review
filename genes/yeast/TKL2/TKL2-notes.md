# TKL2 notes (P33315, YBR117C)

- Second transketolase, 71% identical to Tkl1 [PMID:7916691 "The deduced protein sequence of TKL2 demonstrates 71% identity with TKL1"].
- tkl2 alone: no phenotype, no activity loss [PMID:7916691 "Deletion of TKL2 alone does not lead to a significant phenotype, and transketolase activity is not reduced in these mutants."].
- Functional when overexpressed [PMID:7916691 "Overexpression of TKL2 on a multi-copy plasmid in a tkl1 background showed that TKL2 is functionally expressed: transketolase enzyme activity was detectable in the transformants"]; rescues tkl1 tkl2 aromatic requirement [PMID:7916691 "In addition, transformation of the tkl1 tkl2 double mutant with the TKL2 plasmid can compensate the growth defect on a medium without aromatic amino acids."].
- Very low abundance [UniProt:P33315 "Present with 149 molecules/cell in log phase SD medium."]; interacts with Tkl1 (IntAct, NbExp=4) [UniProt:P33315].
- Localization: Huh GFP cytoplasm + nucleus (PMID:14562095).

Decisions: ACCEPT activity (incl. ISS, backed by overexpression assay), PPP, non-oxidative branch, cytoplasm/cytosol; KEEP_AS_NON_CORE nucleus; REMOVE 3x protein binding.
Module note: YeastCyc links TKL2 to only the S7P+GAP <-> R5P+X5P reaction, but TKL1 to both; Tkl2 should catalyse both transketolase reactions.
