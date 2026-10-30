# LOC541855 notes (A0A1D6L7U4)

## 2026-10-28 initial review

- Confirmed fetched accession A0A1D6L7U4 (GeneID 541855, Zm00001eb060880). GOA has 8 rows,
  all IBA/IEA.
- Identified the protein as ZmTSAlike (primer N-terminus MANGG; 274 aa vs 339 aa IGL)
  [PMID:18430213; PMID:11106389 "The reading frame of Igl encodes a 339-aa peptide"].
  NCBI Gene/RefSeq call it igl1, which appears to be a naming conflation of two adjacent
  genes [PMID:11106389 "Igl and TSAlike are separated by 1.6 kb"].
- Key data [PMID:18430213]: cytosolic GFP fusion ("ZmTSAlike-GFP was localized in the
  cytosol"); no IGP cleavage alone or with ZmTSB1; no complex with ZmTSB1; absent from the
  native TS complex.
- Catalytic E58/D69 retained (bioinformatics/RESULTS.md); UniProt ACT_SITE 68 is on Ala68,
  apparently off by one.
- Decisions: chloroplast rows REMOVE (contradicted by GFP and lack of transit peptide);
  tryptophan synthase activity rows REMOVE (no activity with TSB1, no complex, and TSB is
  plastidic); IGP lyase activity and Trp biosynthesis rows MARK_AS_OVER_ANNOTATED (not
  detected, but the authors leave a cytosolic or conditional role open and catalytic
  residues are present); cytosol IBA ACCEPT, plus a NEW IDA cytosol row from the GFP data.
- No MF is established; core_functions records only the cytosolic TrpA-family protein of
  unknown function.
