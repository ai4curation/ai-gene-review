# MRP1 (MAIZE, Q6Y3I1) curation notes

## 2026-10-28 session

- fetch-gene resolved Q6Y3I1 (GeneID 100037760, EMBL AAO72316.1) as asked. GOA: 6
  IEA rows (nucleotide binding, ATP binding, membrane, ATP hydrolysis activity,
  transmembrane transport, ABC-type transporter activity).
- Literature: cloning paper (PMID:14557075, abstract only) and three
  transcript-induction papers (PMID:22792398 and PMID:23144728 full text;
  PMID:29870861 abstract only). All experimental data are RT-PCR induction by
  herbicides, safeners and pro-oxidants. Most "ZmMRP1" PubMed hits are the
  unrelated transfer-cell MYB TF ZmMRP-1.
- Motif scan (MRP1-bioinformatics/RESULTS.md): NBD2 consensus Walker B ILVLDE,
  NBD1 degenerate VYLLDD, canonical NBD1 signature MSGGQ: typical ABCC.
- Decisions: all MF/CC/BP IEA rows are domain-level claims consistent with a
  full-size ABCC transporter. Nucleotide binding -> TOO_GENERAL (ATP binding kept).
  Membrane kept: no localization data; plant ABCCs are mostly tonoplast but some
  are plasma membrane, so I did not add vacuolar membrane (only one, family-level,
  line of evidence).
- No NEW terms: induction by xenobiotics is expression evidence ("response to"
  terms describe regulation of the gene), and glutathione-conjugate transport has
  never been assayed for this protein.
- UniProt ARBA FUNCTION text (phytic acid) is a family transfer from lpa1/MRP4-type
  orthologs; MRP1 is in PANTHER SF108 (ABCC8-like), not the lpa1 subfamily. Not used
  as support; flagged as a question.
- Verified via UniProt REST (2026-10-28): ZmMRP4/LPA1 (A7KVC2) is PANTHER
  PTHR24223:SF189 "ABC TRANSPORTER C FAMILY MEMBER 5"; MRP1 (Q6Y3I1) is
  PTHR24223:SF108 "ABC TRANSPORTER C FAMILY MEMBER 8" (panther.obo). The ARBA phytic
  acid FUNCTION text therefore comes from a different ABCC subfamily; recorded as a
  CHECK source_defect for UniProt on the transmembrane transport row.
