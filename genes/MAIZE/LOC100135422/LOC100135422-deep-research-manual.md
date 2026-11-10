# LOC100135422 (ZmPMP3-1) — manual literature research

No deep-research API was available; this summary was compiled by hand from the cached
publications and PubMed/NCBI queries (2026-10-28).

## Identity

- UniProt A0A804RGV6 (TrEMBL, unreviewed, PE 3), 58 aa, two predicted TM helices (Phobius 7-26, 32-54).
- NCBI GeneID 100135422; RefSeq NM_001114162.2 / NP_001107634.2; B73 v5 gene Zm00001eb417550
  (v4 Zm00001d024778, v3 GRMZM2G015605), chromosome 10.
- Pfam PF01679 (Pmp3), InterPro IPR000612 (PMP3), PROSITE PS01309 (UPF0057),
  PANTHER PTHR21659:SF120 (HYDROPHOBIC PROTEIN LTI6B).
- NCBI other designations include "Hydrophobic protein LTI6B", "Hydrophobic protein RCI2B",
  "early drought induced protein" and "NaCl stress protein1".

## Mapping to ZmPMP3-1 of Fu et al. 2012 (PMID:22348040)

Fu et al. 2012 list ZmPMP3-1 as a 58-aa protein, accession "EU364580", chromosome bin 10.03,
predicted Mr 6390.71, pI 5.54 (Table 1) [PMID:22348040 "a full-length sequence of ZmPMP3-1 (EU364580) encoding a putative hydrophobic protein of 58 amino acids was obtained"].

- GenBank EU364580 resolves to a COX1 (cytochrome oxidase subunit I) fragment, not a PMP3 cDNA.
- GenBank EU364508 ("Zea mays early drought induced protein mRNA", submitted Dec 2007 by
  Liu Y.H., Li H.Y., Wang T.Y., Li Y. — the same group) is one of the mRNAs NCBI links to
  GeneID 100135422; its CDS (ABY71210.1) is identical to A0A804RGV6 except the last residue
  (...KNN vs ...KNT). Adding Asn for Thr (+13 Da) to the B73 sequence (computed Mr 6378.6)
  gives ~6391.6, matching the reported 6390.71.
- Conclusion: ZmPMP3-1 = LOC100135422, and "EU364580" in the paper is a digit transposition of
  EU364508. This is a publication error, not a GO/UniProt record defect.

## Experimental findings for ZmPMP3-1 (PMID:22348040, full text read)

- Localization: ZmPMP3-1-GFP in onion epidermal cells is at the cell periphery and remains with
  the retracted plasma membrane after plasmolysis in 30% sucrose
  [PMID:22348040 "In these cells, the fluorescence was still detected in regions corresponding to the distorted plasma membrane"].
- Expression: induced by NaCl in shoot and root
  [PMID:22348040 "Under salt treatment, ZmPMP3-1 and ZmPMP3-5 were up-regulated in shoot and root"]; also responsive to drought, cold, ABA (family-level statement in abstract).
- Yeast complementation: ZmPMP3-1 (and six of the other seven paralogs) suppressed Na+ and
  hygromycin B sensitivity of a pmp3 deletion strain (YR93-31, Δnha1 Δpmr2 Δpmp3)
  [PMID:22348040 "the expression of the ZmPMP3 genes could suppress the sensitivity of mutant strains to the Na+ and hygromycin B"].
  Membrane potential was not measured directly; it is inferred from hygromycin B sensitivity
  [PMID:22348040 "Hygromycin B is a lipophilic toxic cation, which is taken up according to the membrane potential"].
- Overexpression (35S::ZmPMP3-1 in Arabidopsis Col-0) enhanced growth under salt and increased
  transcripts of ion transporter (NHX1, AVP1, AHA2) and antioxidant genes — indirect, heterologous.
- Authors acknowledge mechanism unknown; PMP3 proteins are probably not transporters
  [PMID:22348040 "due to the small size of these polypeptides, they are likely not ion transporters"].

## Other literature checked

- PMID:33934485 (Luo et al. 2021, GWAS of maize salt tolerance): the "ZmPMP3" validated with an
  EMS mutant is GRMZM2G477325 on chromosome 7 — a paralog, not this gene.
- PMID:37147346 (ZmPMP3g, drought tolerance): a different paralog by name; not assessed for this locus.
- PMID:30537926 (Esi3/RCI2/PMP3 family in Triticeae): family background.
- PMID:39414681: expression of an unspecified maize PMP3 gene after chitosan treatment; not informative.

## Family-level biology

PMP3/RCI2/Esi3 proteins are 50-80 aa two-TM proteolipids. Yeast Pmp3 loss hyperpolarizes the
plasma membrane; plant homologs (AtRCI2A, rice Lti6a/b) complement it. No molecular activity
(channel, transporter, regulator binding partner) has been established for the family.
