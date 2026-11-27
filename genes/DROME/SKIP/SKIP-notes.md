# SKIP (A0A0B4K6C1) review notes

## 2026-10-28

- `just fetch-gene DROME SKIP` resolved A0A0B4K6C1 as expected (FlyBase FBgn0051163,
  GeneID 42601). GOA has 2 rows: cytoplasm (IEA, ARBA/SubCell) and sensory perception of
  smell (IMP, FlyBase, PMID:22530061).
- Read the full text of PMID:22530061 (olfactory gene-trap screen) and PMID:19463952 (Diao
  et al., SKIP3-Shal). No other Drosophila SKIP papers turned up in PubMed.
- Key point: A0A0B4K6C1 is a long SAM1-SH3-SAM2 isoform. The Shal-binding octapeptide is
  unique to the 128-aa SKIP3 product (A0A0B4KH49), see SKIP-bioinformatics/RESULTS.md
  [PMID:19463952 "Shal binding requires these unique C-terminal residues"]. So I did not
  add potassium channel regulator activity or Shal binding to this accession, even though
  these are the best-characterized activities of the gene.
- Cytoplasm: ACCEPT. It agrees with myc-SKIP1 imaging in neuronal soma and processes and
  with the lack of TM segments or signal peptide. The ARBA source is not used as support.
- Added NEW neuronal cell body (IDA, PMID:19463952). This rests on myc-SKIP1, a long isoform
  with the same SAM1-SH3-SAM2 architecture as A0A0B4K6C1, imaged in neurons.
- Sensory perception of smell (IMP): KEEP_AS_NON_CORE. The excision reversion is solid
  genetics, but the EAG is normal, the mechanism is unknown, and the isoforms involved are
  unknown.
- Considered and rejected NEW BP terms (e.g. regulation of potassium ion transmembrane
  transport). The deficiency/rescue data are SKIP3-specific and phenotype-level.
