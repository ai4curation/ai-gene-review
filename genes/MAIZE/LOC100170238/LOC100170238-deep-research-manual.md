# LOC100170238 (ZmTSA, tryptophan synthase alpha subunit) - manual literature research

No deep-research API was available; this summary was compiled manually from cached
publications (publications/PMID_18430213.md, publications/PMID_31090986.md), the
NCBI Gene record for GeneID 100170238, and the UniProt entry A0A804Q7I2.

## Identity

- UniProt A0A804Q7I2 (TrEMBL, 319 aa), B73 gene Zm00001eb301540 (v5),
  Zm00001d018969 / GRMZM5G841619 (older assemblies), chromosome 7; GeneID 100170238.
- NCBI Gene names this locus "tryptophan synthase alpha" with alias TSA and
  designations "indole-3-glycerol phosphate lyase" and "tryptophan synthase alpha
  subunit1"; the GeneRIF for the gene is PMID:31090986.
- Kriechbaumer et al. 2008 named the gene ZmTSA: "ZmTSA is located on chromosome 7
  (contig AC191027, GeneBank). A full-length ZmTSA cDNA clone was isolated
  [GenBank:EU334442]." [PMID:18430213]
- Sequence check: the ZmTSA peptides identified by MS in the native leaf TS complex
  (GTTFEDVISMVK, TLEEAASPEEGLK, AALP, ALR; PMID:18430213 Table 2) are all present in
  A0A804Q7I2, and the reverse GFP-fusion primer GGCAATGCGGCCTTCAGG is the reverse
  complement of the codons for the C-terminus ...LKAALP. The ZmTSAlike expression
  primer (start M-A-N-G-G) does not match. Conclusion: LOC100170238 = ZmTSA, not
  ZmTSAlike, BX1 or IGL.

## Domain / family

- TrpA family (Pfam PF00290, NCBIfam TIGR00262, HAMAP MF_00131, PROSITE PS00167);
  PANTHER PTHR43406:SF1 "tryptophan synthase alpha chain, chloroplastic". Two
  predicted proton-acceptor active sites (PROSITE-ProRule PRU10120) at positions 103
  and 113 of the precursor.
- N-terminal ~50 residues are Ala/Arg/Ser-rich, a plastid transit peptide; TargetP
  and iPSORT predicted plastid localization [PMID:18430213].

## Function

- Plastid localization: "In case of ZmTSA GFP fluorescence coincided with the
  chlorophyll autofluorescence of the chloroplasts (Figure 2A–C), demonstrating
  plastidic localization of ZmTSA." [PMID:18430213]
- Own (alpha) activity: "A low, but clearly detectable IGP turnover (Kcat = 0.006
  s-1) was observed (Table 1)." Km(IGP) 458 uM alone, 52 uM with ZmTSB1
  [PMID:18430213].
- Complex formation: "These results are consistent with formation of a
  ZmTSA2ZmTSB12 heterotetramer." "Heteromerisation with ZmTSB1 resulted in a
  32-fold increase of the catalytic efficiency of ZmTSA." The ZmTSA+ZmTSB1 mixture
  performs the full alpha-beta reaction (IGP + serine to Trp; kcat 0.45 s-1)
  [PMID:18430213].
- In planta: a ~160 kD leaf fraction has alpha, beta and alpha-beta activity, and
  "ZmTSA was conclusively identified as component of a maize TS complex"; no
  ZmTSAlike, BX1 or IGL peptides were found in it [PMID:18430213].
- Monomeric (free) alpha activity in leaf extracts is due to BX1, not ZmTSA ("In
  extracts of bx1 mutants this activity was not present") [PMID:18430213].
- Allosteric dependence on TrpB: "Here, a zmTrpA enzyme is activated by zmTrpB1 in
  the canonical TS whereas a zmBX1 enzyme displays a high IGP lyase activity without
  an interaction partner." zmTrpA is a monomer on its own (native MS); loop 6
  substitutions from BX1 raise its stand-alone kcat up to 520-fold [PMID:31090986].
  The authors propose zmTrpA as the progenitor of BX1 (and by extension IGL).
- Expression: transcripts in all 16 tissues tested; ZmTSA is ~9-fold more abundant
  than ZmTSAlike [PMID:18430213].

## Genetics

- No zmtsa mutant has been described in the papers above. Tryptophan auxotrophy is
  known for the tsb double mutant orp1 orp2 (ZmTSB1/ZmTSB2) and, in Arabidopsis, for
  trp3 (AtTSA1) [as reviewed in PMID:18430213].

## Interpretation

ZmTSA is the housekeeping alpha subunit of plastid tryptophan synthase. It has an
intrinsic but weak indole-3-glycerol-phosphate lyase (alpha-reaction) activity that is
strongly stimulated by assembly with ZmTSB1/2 into an alpha2beta2 complex, which
performs the overall tryptophan synthase reaction; the tryptophan synthase activity is
thus a complex activity to which ZmTSA contributes.
