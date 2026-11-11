# Mtmr4 (rat) - manual literature research

No deep-research provider was available; this summary was compiled by hand from
cached publications (`publications/PMID_*.md`) and PubMed searches
(`MTMR4[Title] OR "myotubularin-related protein 4"[Title]`, 12 hits, plus
targeted searches for MTMR3/MTMR4 heteromers and abscission). Almost all functional
work is on human MTMR4 (Q9NYA4) or mouse cells; the only rat-specific paper is
PMID:19125695.

## Identity and domain architecture

- Rat Mtmr4 (RGD:1310306, GeneID 287607) is an unreviewed TrEMBL entry, A0A8I6A3Q2,
  1191 aa, PE 3. It has a PH-GRAM domain, a myotubularin phosphatase domain
  (153-570, PROSITE PS51339) with the catalytic Cys407 in HCSDGWDRT, a coiled-coil
  region, and a C-terminal FYVE zinc finger (1110-1170) (`Mtmr4-uniprot.txt`;
  `Mtmr4-bioinformatics/RESULTS.md`).
- Human MTMR4 was first described as FYVE-DSP2, a FYVE-domain dual-specificity
  phosphatase on chromosome 17 [PMID:11302699 "both FYVE-DSP1 and FYVE-DSP2
  efficiently and specifically dephosphorylated phosphotidylinositol 3-phosphate"].

## Catalytic activity

- Myotubularins are 3-phosphatases for PtdIns3P and PtdIns(3,5)P2 [PMID:16787938
  "The myotubularins are a large family of lipid phosphatases with specificity
  towards PtdIns3P and PtdIns(3,5)P(2)"]. All active MTMs including MTMR4 reduce
  endosomal PtdIns3P on overexpression [PMID:16787938 "All active MTMs we have tested
  (MTM1, MTMR2-MTMR4) reduce endosomal PtdIns3P levels upon overexpression"].
- MTMR4 knockdown or catalytic-dead C407A increases PtdIns3P-positive endosomes
  [PMID:20736309 "In cells with MTMR4 knockdown, or following expression of the
  catalytically inactive MTMR4, MTMR4(C407A), the number of PtdIns(3)P-decorated
  endosomes significantly increased"].
- MTMR4/MTMR3 double knockout macrophages accumulate PtdIns3P puncta
  [PMID:30944173 "DKO cells exhibited enlarged cytosolic puncta positive for PtdIns3P"].
- Protein substrate: one lab reports MTMR4 dephosphorylates the C-terminal SXS
  serines of R-Smads, requiring Cys407 [PMID:20061380 "attenuates TGFbeta signaling by
  reducing the phosphorylation level of R-Smads in early endosomes"; PMID:23150675
  "preferentially associated with and dephosphorylated the activated R-Smads in
  cytoplasm"]. No phosphotyrosine protein substrate has been reported; the PTP
  (EC 3.1.3.48) annotation comes from the generic PTP active-site signature.

## Localisation

- Unique among myotubularins in localising to endosomes, via its FYVE domain
  [PMID:16787938 "Subcellular localisation studies reveal a unique distribution of
  MTMR4 to endosomal structures"].
- Early and Rab11/Sec15 recycling endosomes [PMID:20736309 "localizes to early
  endosomes and also to Rab11- and Sec15-positive recycling endosomes"].
- Late endosomes, with Nedd4 [PMID:19125695 "hMTMR4 (human MTMR4) and Nedd4
  co-immunoprecipitated and co-localized to late endosomes"]; late endosomes and
  autophagosomes in A549 cells [PMID:29962048 "MTMR4 was localized mainly in late
  endosomes and autophagosomes"].
- Phagosomes [PMID:31543504 "was dynamically recruited to phagosomes of macrophages
  during phagocytosis"] and Salmonella-containing vacuole [PMID:27625994 "GFP-tagged
  MTMR4 is recruited to the SCV"].

## Processes

- Endosomal sorting/recycling: overexpression delays transferrin exit from early
  endosomes; knockdown alone has no recycling phenotype [PMID:20736309].
- EGFR trafficking: only MTMR4 affects EGFR degradation, requiring FYVE domain
  [PMID:16787938].
- TGF-beta and BMP signalling attenuation by R-Smad dephosphorylation
  [PMID:20061380; PMID:23150675].
- Phagosome PtdIns3P turnover and phagosome maturation [PMID:31543504 "MTMR4
  regulates PtdIns(3)P degradation in macrophages and thereby controls phagocytosis
  and phagosomal maturation"].
- Autophagy/endolysosomal integrity and TFEB nuclear translocation [PMID:29962048].
- Abscission: MTMR3/MTMR4 heterodimer bridges PLK1 and CEP55; MTMR4 binds CEP55 via
  a GPPXXXY motif [PMID:25659891 "myotubularin-related protein 4 interacts with CEP55
  through a short GPPXXXY motif"]. Rat Mtmr4 has GPPSLEY at residue 5.
- STING trafficking / innate immune response to DNA [PMID:30944173], cardiac ion
  channel degradation as an LQTS modifier [PMID:32173736; PMID:42128250].

## Rat-specific evidence

- PMID:19125695 (full text): MTMR4 is a Nedd4 substrate; in rat gastrocnemius 30 d
  after tibial nerve transection, MTMR4 protein falls about 90% while Nedd4 doubles
  ["MTMR4 decreases approx. 90% with a 2-fold increase in Nedd4 expression"]. This is
  expression (protein level) evidence only; no function of MTMR4 in muscle adaptation
  was tested.
