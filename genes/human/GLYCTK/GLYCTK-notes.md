# GLYCTK notes

## 2026-10-25 ORGANELLES batch 3 (mitochondrion rows)

Rows: GO:0005739 mitochondrion, IEA GO_REF:0000044 (SL-0173) and HTP PMID:34800366 (MitoCoP; FlyBase). No sub-compartment rows; qualifier located_in.

Checks:
- UniProt: "SUBCELLULAR LOCATION: [Isoform 2]: Cytoplasm. Mitochondrion {ECO:0000269|PubMed:16753811}"; isoform 1 cytoplasm only [file:human/GLYCTK/GLYCTK-uniprot.txt].
- Guo et al. 2006 [PMID:16753811, abstract only]: "Both GLYCTK1 and GLYCTK2 proteins are localized in cytosol, and GLYCTK2 proteins are specifically localized in mitochondria."
- MitoCoP [PMID:34800366, full text cached]: "We classified >8,000 proteins in mitochondrial preparations of human cells and defined a mitochondrial high-confidence proteome of >1,100 proteins (MitoCoP)." The per-protein table is supplementary, not cached.
- Isoform 2 is truncated (VSP_025360 replaces 179-234; VSP_025362 deletes 235-523), so the GFP-mitochondrial form is not the full enzyme. The canonical N-terminus MAAALQVLPRLARAPLHPLLWRGSVARLASS is Arg-rich with no acidic residues, presequence-like; UniProt annotates no transit peptide and no predictor was run, so this is only an observation (a question worth a TargetP/MitoFates run).

Outcome: both rows stay KEEP_AS_NON_CORE, reasons now record the check; quotes replaced with verbatim ones (the old ones were in conf/local_quote_baseline.yaml). Stays at root (no sub-mitochondrial assay, no annotated transit peptide or TM).
