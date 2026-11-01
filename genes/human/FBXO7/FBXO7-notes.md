# FBXO7 notes

## 2026-10-25 ORGANELLES batch 3 (mitochondrion rows)

Rows: GO:0005739 IEA (GO_REF:0000120; UniProt SL-0173 plus mouse Q3U7U3), IDA
(PMID:26310625, ParkinsonsUK-UCL) and IDA (PMID:23933751, UniProt). No sub-compartment rows.

Checks:
- [PMID:23933751 "endogenous Fbxo7 levels were found to decrease steadily in the cytosolic fraction and increase concurrently in the mitochondrial fractions"]
  (HEK293T and SH-SY5Y, CCCP time course). Full text cached.
- Predicted MTS: [PMID:23933751 "In silico analysis of the primary sequence of the Fbxo7 protein suggested that it may possess such an MTS at the N-terminus of isoform 1, and this prediction depended on two critical residues (Arg-2 and Arg-6)"];
  the R2/R6 mutant does not reach the mitochondrial fraction. No cleavage, import or
  protease-protection assay.
- [PMID:26310625 "Upon stress, the endogenous WT FBXO7 gets up-regulated, concentrates into mitochondria and forms FBXO7 aggregates in mitochondria."] (abstract only).
- UniProt: [file:human/FBXO7/FBXO7-uniprot.txt "Relocates from the cytosol to depolarized mitochondria (PubMed:23933751)."]; no TM. Not in MitoCarta3.0.

Outcome: all three rows stay ACCEPT (the core mitophagy function's location), reasons record
the check. Stay at root: the PINK1/Parkin role points to the cytosolic face of the outer
membrane, the aggregation paper says "into mitochondria", and no assay separates them.
