# LOC542106 review notes

## 2026-10-28 session

- fetch-gene resolved K7WCD1 (TrEMBL, GeneID 542106, Zm00001eb391800), as expected;
  GOA file keyed to K7WCD1 with a single row (GO:0005576 extracellular region, IEA
  InterPro2GO).
- Gene identity: NCBI Gene 542106 "lo1 pI allergen homolog 1", aliases EXPB1B, EXPB9,
  GRMZM2G072886 (NCBI E-utilities). K7WCD1 is 264/269 identical to EXPB1/Zea m 1d
  (P58738 = AAO45608), own pairwise comparison; differences A20V, Y116F, I149L, Y191F,
  V251I.
- PMID:17225858 (full text read): Mu insertion is in "EXPB1 (GenBank Accession
  AY197353)"; AY197353 encodes P58738, not K7WCD1. The paper explicitly notes
  "additional genes highly similar to EXPB1 (>98.8% nucleotide sequence identity) also
  code for the same isoform" - LOC542106 is such a gene. So: background/paralog
  evidence; phenotype (reduced pollen competitive ability) not attributable to this
  locus and not a basis for a NEW process term.
- Activity evidence (wall extension of grass walls, GAX binding, no hydrolysis) is on
  native Zea m 1d purified from pollen [PMID:12913162, PMID:16984999, PMID:27729469];
  given near-identity, transferred as ISS.
- Decisions:
  - GO:0005576 extracellular region -> MODIFY to GO:0009505 plant-type cell wall
    (OAK: GO:0009505 is_a GO:0005618 cell wall, part_of/is_a chain to GO:0005576).
    Two lines: Zea m 1d binds grass cell walls (PMID:16984999, PMID:27729469); signal
    peptide + CBD-like domain 2. Same choice as genes/MAIZE/LOC541904 (EXPA1).
  - NEW GO:0009828 plant-type cell wall loosening (ISS from P58738/Zea m 1d). The gene
    product itself does the work (it is the wall-loosening agent), so it passes the
    "who performs the step" test; comparator: P58738 carries GO:0009828 by IDA.
  - Not added: pollen tube growth / pollination terms (phenotype only, and on a
    paralog allele).
- No GO MF term exists for nonenzymatic wall loosening (GO:0009936 expansin obsolete);
  core function uses proposed_molecular_function as in LOC541904.
