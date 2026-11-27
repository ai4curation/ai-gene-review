# LOC541855 (A0A1D6L7U4; ZmTSAlike) - manual literature research

No deep-research API was available; this summary was compiled manually from cached
publications (publications/PMID_*.md), PubMed searches and NCBI/UniProt records
(searched 2026-10-28).

## Identity

- UniProt A0A1D6L7U4 (TrEMBL), 274 aa, gene model Zm00001eb060880 (B73 v5), chromosome 1,
  NCBI GeneID 541855.
- NCBI Gene names the locus "indole-3-glycerol phosphate lyase 1" (alias igl1,
  GRMZM2G046191, Zm00001d034460), but also lists the designations "tryptophan synthase A
  homolog1" and "tryptophan synthase A-like protein".
- The protein is ZmTSAlike, not IGL:
  - the ZmTSAlike expression primer "CGCATATGGCCAACGGCGGCG" in PMID:18430213 encodes the
    N-terminus MANGG, which is the N-terminus of A0A1D6L7U4
    (file:MAIZE/LOC541855/LOC541855-bioinformatics/RESULTS.md);
  - IGL is a 339-aa protein [PMID:11106389 "The reading frame of Igl encodes a 339-aa
    peptide"], while A0A1D6L7U4 has 274 aa;
  - Igl and TSAlike are adjacent genes [PMID:11106389 "Sequence analyses of the genomic Igl
    clone revealed that Igl and TSAlike are separated by 1.6 kb"], which may explain why
    the NCBI gene record mixes the two names.

## Family and sequence features

- TrpA (tryptophan synthase alpha chain) family: Pfam PF00290, NCBIfam TIGR00262, HAMAP
  MF_00131, PROSITE PS00167, PANTHER PTHR43406.
- The catalytic Glu/Asp pair of TrpA (E. coli E49/D60) is retained as E58/D69. The UniProt
  ACT_SITE feature at position 68 falls on an alanine, an apparent off-by-one placement
  (file:MAIZE/LOC541855/LOC541855-bioinformatics/RESULTS.md).
- No N-terminal plastid transit peptide: ZmTSAlike is 45 aa shorter at the N-terminus than
  ZmTSA [PMID:18430213 "ZmTSAlike, 45 amino acids shorter at the N-terminus, was expected
  to be retained in the cytoplasm"].

## Experimental findings (PMID:18430213, Kriechbaumer et al. 2008, full text)

- Localization: "ZmTSAlike-GFP was localized in the cytosol" (maize mesophyll protoplasts).
- Activity: "No α-activity of recombinant ZmTSAlike was detected in analogous experiments."
  It "remained inactive with IGP as substrate also when the β-subunit was added".
- Complex formation: "No interaction of ZmTSB1 with ZmTSAlike, BX1, or IGL was
  detectable"; ZmTSAlike behaves as a monomer (~30 kD) in gel filtration.
- Native tryptophan synthase complex from leaves contains ZmTSA, and "No peptides
  specific for ZmTSAlike, BX1, or IGL were detected".
- Expression: transcripts in all 16 tissues tested, about 9-fold lower than ZmTSA
  (0.20 vs 1.80 fg/fg GAPDH).
- Authors' conclusion: "it remains unclear, whether ZmTSAlike functions as cytosolic TSA
  isoform. ZmTSAlike might either require specific conditions and modifications or it has
  an unknown function in plant metabolism."

## Earlier description (PMID:11106389, Frey et al. 2000, full text)

- TSAlike was first isolated as a cDNA in the Igl study; it is closer to Arabidopsis TSA
  (70% identity) than to IGL and BX1, and "No deviation from the TSA consensus is found for
  TSAlike."
- TSAlike transcript "is not influenced by volicitin treatment" (unlike Igl).

## Paralogs in maize (context)

- ZmTSA (chromosome 7; plastid; the alpha subunit of the native TS complex), BX1
  (benzoxazinoid indole), IGL (herbivore-induced volatile indole) and ZmTSAlike
  [PMID:18430213 "Four TSA homologs are present: BX1, IGL, ZmTSAlike [17], and ZmTSA (this
  work)."].

## Searches without further hits

PubMed queries for TSAlike / "TSA like" / GRMZM2G046191 / Zm00001d034460 with maize
returned no further gene-specific papers.
