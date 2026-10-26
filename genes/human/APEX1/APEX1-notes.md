# APEX1 notes

## 2026-10-20 ORGANELLES batch 1 (mitochondrion rows)

- GO:0005739 rows: IEA (GO_REF:0000044, SL-0173; UniProt line is by similarity), HTP (PMID:34800366, mitochondrial proteome), IDA (PMID:20231292, MTS mapping). All kept ACCEPT; reasons now record that the direct assays resolve only the organelle.
- Sub-mitochondrial evidence (rule 4), from the Tell/Vascotto group:
  - IMS: [PMID:25956655 "In a previous work, we demonstrated that the majority of APE1 protein accumulates within the IMS"];
    [PMID:25956655 "Presence of PLA signals demonstrated that ectopic APE1 interacted with endogenous Mia40 which is known to be present only in the mitochondria IMS."];
    [PMID:25956655 "Here, we showed that Mia40 is involved in the transport of APE1 into the IMS."]
  - Matrix: [PMID:25956655 "However, a portion of APE1 is further translocated, through a still unidentified mechanism, to the matrix where the mtDNA resides."];
    matrix-restricted MTS-APE1 rescues mtDNA damage and respiration [PMID:33028238 "Remarkably, the phenotype was efficiently rescued in MTS-APE1 clone, where APE1 is present only within the mitochondrial matrix."]
- Outcome: two NEW IC rows, GO:0005758 mitochondrial intermembrane space (main pool) and GO:0005759 mitochondrial matrix (minor pool, where mtBER acts). The earlier fractionation paper behind the "majority in IMS" claim was not read directly, hence IC.
- Note on form: older work proposed an N-terminally truncated (NLS-less) form enters mitochondria; PMID:25956655 states full-length APE1 is present in mitochondria. The IEA row summary keeps the older wording.
- core_functions.locations left at nucleus: the core functions there are written for nuclear BER/redox; mitochondrial BER is real but not yet a separate core function entry.
