# LtaS1 / YfnI (UniProtKB:Q797B3) notes

## Identity
- UniProt Q797B3 = LTAS1_BACSU, gene `ltaS1`, synonym `yfnI`, locus BSU07260.
- In the primary literature this protein is **YfnI**: a bona-fide
  polyglycerolphosphate LTA synthase whose expression is controlled by the ECF
  sigma factor **SigM** [PMID:17434969 "... yfnI ... responsive to ... the
  stress-responsive extracytoplasmic function sigma factor, SigM"].
- It hydrolyses PG Mn2+-dependently in vitro and, in the absence of LtaS2,
  makes LTA of increased chain length [PMID:21255105 "B. subtilis strains
  expressing YfnI in the absence of LtaS(BS) produced LTA of retarded mobility,
  presumably caused by an increase in chain length"]. Unlike yflE, yfnI cannot
  restore S. aureus growth after ltaS depletion (UniProt MISCELLANEOUS; PMID:17483484).
- Cleaved by signal peptidases SipT/SipV; a genuine SPase I substrate
  [PMID:11544192 "only the processing of the polytopic membrane protein YfnI was
  strongly inhibited in Spase I mutants"]; processed domain secreted
  SecA/Ffh-dependently [PMID:10658653].

## CMMMech cross-reference (data/records/thulium.yaml) — do NOT edit CMMMech
Same swap as the LtaS2 entry (do not edit CMMMech):
1. CMMMech labels Q797B3 "LtaS1 / **YflE**"; UniProt/literature have
   Q797B3 = ltaS1 = **yfnI**. The yfnI/yflE synonyms are reversed between
   Q797B3 and O34952 in CMMMech.
2. CMMMech gives locus "BSU07690" for Q797B3; UniProt: Q797B3 = **BSU07260**
   (BSU07690 matches neither paralogue).
3. CMMMech asserts **EC 2.7.8.40** for all four; that EC is an unrelated
   Aeromonas O-antigen phosphotransferase. UniProt assigns **EC 2.7.8.-**.

The accession→record identity (Q797B3 = LtaS1) is correct; only the synonym,
locus, and EC fields are in error.
