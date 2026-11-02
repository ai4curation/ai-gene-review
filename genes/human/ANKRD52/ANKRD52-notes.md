# ANKRD52 notes

- PP6-ARS-C. It co-purifies with PP6 through PPP6R1 [PMID:18186651, abstract]. Unlike ANKRD28 and ANKRD44, it is not needed for PP6 in mitosis [PMID:21187329].
- Key function [PMID:28114302, full text; genome-wide CRISPR screen]: ANKRD52-PPP6C dephosphorylates AGO2 S824-S834 after CSNK1A1 phosphorylation. ANKRD52 knockout accumulates phospho-AGO2 and derepresses miRNA targets. Tumour inactivation blunts IFN-gamma signaling via miR-155/SOCS1 [PMID:34853298]. ANKRD52-PP6 also dephosphorylates PAK1 [PMID:33096142, abstract; not cited]. No separate GO term is drawn from these.
- GOA had only 3 × PPP6R1 IPI → REMOVE (complex co-membership).
- NEW terms:
  - GO:0008287 (IDA, PMID:18186651).
  - GO:0019888 (IMP, PMID:28114302; substrate-level readout).
  - GO:2000637 positive regulation of miRNA-mediated gene silencing (IMP; participation, since ANKRD52 is a subunit of the AGO2 phosphatase).
  - GO:0005737 cytoplasm (HDA; OpenCell cytoplasmic_3, from ANKRD52-bioinformatics/opencell_localization.py).
- PTHR24166 (SF52) has PAINT nodes that do not reach ANKRD52 (PAN-GO 0). The family files are already on main from the ANKRD29 review.
