# BX1 review notes

## 2026-10-28 session

- `just fetch-gene MAIZE BX1` resolved P42390 (Swiss-Prot TRPA_MAIZE, GeneID 542117);
  8 GOA rows, all IBA/IEA. No experimental GO annotations exist for BX1.
- Papers read: PMID:18430213 (full text; Kriechbaumer 2008), PMID:11106389 (full text; Frey
  2000, IGL), abstracts of PMID:9235894, PMID:7766899, PMID:16120446, PMID:33458870,
  PMID:19577780, PMID:21730199, PMID:27538820.
- Literature summary in BX1-deep-research-manual.md (no API deep research available).

## Key points

- BX1 is a TrpA paralog neofunctionalised as a free indole-3-glycerol phosphate lyase
  (EC 4.1.2.8), the first step of benzoxazinoid biosynthesis [PMID:9235894 "Bx1 encodes a
  tryptophan synthase alpha homolog that catalyzes the formation of indole for the
  production of secondary metabolites rather than tryptophan"].
- It does not interact with TSB and is absent from the native TS complex
  [PMID:18430213 "No interaction of ZmTSB1 with ZmTSAlike, BX1, or IGL was detectable."],
  so tryptophan synthase activity (EC 4.2.1.20, IGP + Ser -> Trp) is not a property of
  BX1. The IBA/IEA rows for GO:0004834 and GO:0000162 come from TrpA family membership.
  MODIFY to GO:0033984 and GO:0042432 (indole biosynthetic process) respectively.
- Cytosol IBA comes from E. coli TrpA only; BX1 has a chloroplast transit peptide and
  YFP fusion is chloroplastic (PMID:33458870) -> REMOVE + source defect.
- Chloroplast rows accepted. Added NEW chloroplast stroma (IC): soluble monomeric enzyme
  in leaf extracts, no TM segment, stromal-type transit peptide, and IGP is made by
  plastid IGPS enzymes (PMID:33458870).
- No GO term for benzoxazinoid (DIBOA/DIMBOA) biosynthetic process; proposed as a new term.
  Defence-response terms were NOT proposed: bx1 phenotypes (aphids, fungi, caterpillars)
  are consequences of loss of the metabolite.

## Possible UniProt issues

- UniProt kinetics note says kcat 0.02 s-1 citing PMID:9235894, but PMID:18430213 Table 1
  (citing the same work) gives 2.8 s-1, and PMID:11106389 says IGL kcat 2.3 s-1 is
  "similar for both enzymes". Likely a UniProt error; cannot verify without the 1997 full
  text. Recorded as a CHECK source defect on the lyase row.
- UniProt SUBUNIT says homodimer for the lyase activity (crystal structure); gel filtration
  (PMID:18430213) gives ~30 kD monomers. Crystal packing dimer vs. solution monomer.
- UniProt lists EC 4.2.1.20 (tryptophan synthase) as a catalytic activity without
  evidence; this is contradicted for BX1 by the absence of TSB interaction.
