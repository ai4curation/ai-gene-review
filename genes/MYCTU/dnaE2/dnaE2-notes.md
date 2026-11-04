# dnaE2 / Rv3370c (P9WNT5) curation notes

- No provider deep research is available for this gene; no `-deep-research-*.md` file was
  generated in this session. The review rests on four cached publications (PMID:20615954
  full text; PMID:12705867, PMID:12029045, PMID:18799471 abstract-only) and UniProt.
- DnaE2 is the catalytic component: active-site substitution phenocopies deletion.
  [PMID:20615954, "Point mutations in the DnaE2 active site eliminated induced mutagenesis and damage tolerance, reproducing the dnaE2 deletion phenotype."]
- It is not the replicative polymerase, which is why GO:0006260 is over-annotation; UniProt's
  curated FUNCTION line says so explicitly, citing PubMed:12705867.
  [file:MYCTU/dnaE2/dnaE2-uniprot.txt, "CC       polymerase. Does not appear to be essential for chromosomal"]
- PHP exonuclease residues are absent in DnaE2 but retained in DnaE1, which is the argument
  against GO:0008408.
  [PMID:20615954, "The corresponding domain of Mtb DnaE1 retains all amino acids associated with exonuclease activity ( 34 – 36 ), whereas key residues are absent in DnaE2."]
- In vivo significance: DnaE2-dependent mutagenesis contributes to drug resistance.
  [PMID:12705867, "and can contribute directly to the emergence of drug resistance in vivo"]
- Induction: LexA-regulated, up-regulated by all forms of DNA damage; delayed (24 h)
  induction after subinhibitory ciprofloxacin.
  [PMID:18799471, "induction of lexA and recA after 4 h and of dnaE2 after 24 h of subinhibitory"]
- Note on PMID:12029045: it calls dnaE2 "a component of DNA polymerase III", which reflects
  2002 knowledge and is superseded; recorded in that reference's reference_review.
- Evidence-code issue: the two MTBBASE rows from PMID:20615954 are coded IDA for
  mutant-phenotype data (IMP). Recorded once as a source_defect on the GO:0042276 row.
