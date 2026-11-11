# C6F010 notes

## 2026-10-28 initial review

- fetch-gene first failed on an OLS NCBITaxon lookup (404); a re-run completed and
  created the stub. UniProt id is C6F010 (no switch). GOA: 6 IEA rows.
- Identity: C6F010 = ZmrbohD variant alpha [PMID:19592501 "A 2972 bp ZmrbohD
  transcript was also cloned, which had an ORF of 2799 nucleotides, encoding a
  protein of 932 amino acids"]; GeneID 100136880 (rbohD, Zm00001d052653).
- PMID:20693409 (key paper) was read in full: expression-only evidence (BR induces
  ZmrbohA-D transcripts; ZmMPK5 and apoplastic H2O2 needed for the late phase).
  It does not justify any process annotation for this protein.
- Nat Genet 2024 ZmRBOH4 (PMID:38238629) is probably this gene (closest to AtRBOHD;
  NCBI designation "respiratory burst oxidase4") but no locus id is given; kept
  as a suggested question, not used to add NEW process terms.
- Annotation decisions follow the maize rbohC review: peroxidase and the derived
  cellular oxidant detoxification rows are removed (wrong InterPro2GO mapping of
  IPR013623), oxidoreductase rows MODIFY to GO:0106292, membrane MODIFY to plasma
  membrane, calcium ion binding kept as non-core.
- Bioinformatics: C6F010-bioinformatics/RESULTS.md (closest Arabidopsis homologue
  RBOHD, 67.4%; heme His ligands intact).
