# LOC732842 (K7TTR0) review notes

## Session log (2026-10-28)

- `just fetch-gene MAIZE LOC732842` resolved K7TTR0 directly (GeneID 732842; GOA keyed to
  K7TTR0, 6 rows). No accession switch.
- Identified as orp1/TSB1 via NCBI Gene (see deep-research-manual) and 99.7% identity to
  Swiss-Prot P43283 (bioinformatics/RESULTS.md).
- Key paper PMID:18430213 read in full: recombinant ZmTSB1 (= this protein) has the
  beta-reaction alone (Table 1), forms beta2 homodimers, and forms an alpha2beta2 complex with
  ZmTSA that performs the overall reaction [PMID:18430213 "These results are consistent with
  formation of a ZmTSA2ZmTSB12 heterotetramer."]
- Decisions mirror the sibling review LOC732803 (TSB2) for consistency: IBA/IEA tryptophan
  biosynthesis ACCEPT; contributes_to GO:0004834 ACCEPT; IEA enables GO:0004834 ACCEPT with a
  WRONG_QUALIFIER source defect; cytoplasm IBA MODIFY to chloroplast; chloroplast IEA ACCEPT;
  NEW GO:0052684 (beta-reaction). Unlike TSB2, TSB1 has direct recombinant enzyme data, so the
  NEW row is IDA.
- Not added: protein homodimerization activity (beta2 dimers seen by gel filtration) -- true
  but peripheral and not needed to describe function; no complex CC term exists in GO for
  tryptophan synthase.
- Curation gap: GO has no CC term for the tryptophan synthase alpha2beta2 complex (recorded as
  suggested question).
