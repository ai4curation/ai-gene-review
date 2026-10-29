# TINCR (A0A2R8Y7D0) review notes

## 2026-10-08 — MICROPROTEINS Tier 2 review (claude-code)

### Identity
- HGNC TINCR (HGNC:14607), formerly LINC00036 / PLAC2; long annotated as the lncRNA
  "terminal differentiation-induced ncRNA". UniProt A0A2R8Y7D0 (Swiss-Prot, PE1), 87 aa,
  a single ubiquitin-like (beta-grasp) domain (PS50053, 14-83) with a C-terminal
  SUMO-interacting motif (79-83). MANE Select NM_001396408.1 now carries the CDS, so the
  ORF is the main ORF of the TINCR transcript (not an alt-ORF of another host gene); the
  folder name follows the HGNC symbol.
- Crystal structure PDB 7MRJ (res 2-87) from PMID:36899004.
- Names in the literature: TUBL (Nita 2021), pTINCR (Boix 2022), TINCR microprotein
  (Morgado-Palacin 2023).

### Existence
- Stratum corneum proteomics [PMID:32012357 "Here, we report the presence of an evolutionarily
  conserved open reading frame in TINCR and the identification of peptides derived from this
  open reading frame in the proteome of human stratum corneum"].
- Endogenous FLAG knock-in mice and targeted proteomics [PMID:34351912 "whose expression was
  confirmed by the generation of mice harboring a FLAG epitope tag sequence in the endogenous
  open reading frame as well as by targeted proteomics"].

### Function evidence
- Proliferation (Nita 2021, PMID:34351912): overexpression in NHEKs increased S phase; ORF
  frameshift (1-bp del, RNA structure preserved) abolishes the effect in mouse primary
  keratinocytes [PMID:34351912 "Expression of WT or SM forms of TINCR resulted in a marked
  increase in the percentage of cells in S phase of the cell cycle, whereas expression of
  WT_del or SM_del forms had no such effect"]. Human NHEK siRNA knockdown decreased S phase.
  Frameshift mice: delayed wound closure [PMID:34351912 "Tubl–/–mice manifested delayed wound
  closure from days 4 to 10 postinjury compared with WT control animals"]. Nita found that
  two of three siRNAs did not affect involucrin induction, i.e. no differentiation effect.
- Differentiation (Boix 2022, PMID:36369429): start-codon KO HaCaT/MCF7 cells fail to
  differentiate; pTINCR binds SUMO1/2/3 non-covalently via its SIM (GST pull-down) and
  co-IPs with CDC42, increases CDC42 SUMOylation and GTP-CDC42; SIM mutant inactive
  [PMID:36369429 "GST-pull down assays confirmed that pTINCR binds to SUMO1 and SUMO2/3 in a
  non-covalent manner and that the interaction is lost in the pTINCR-SIMmut"]. In tumour /
  epithelial lines pTINCR *decreases* proliferation [PMID:36369429 "In addition, pTINCR
  reinforces cell-to-cell junctions and decreases proliferation."].
- Tumour suppressor in SCC (Morgado-Palacin 2023, PMID:36899004): TP53/UV-induced; Tincr KO
  mice get more UVB SCC.
- So the direction of the proliferation effect differs between normal keratinocytes (Nita,
  pro-proliferative) and transformed epithelial cells (Boix, Morgado-Palacin, anti-
  proliferative). Neither group explains the discrepancy; mechanism of the Nita effect is
  unknown.

### Localization
- Endogenous: nucleus and cell-cell junctions in HaCaT/MCF7 [PMID:36369429 "Endogenous pTINCR
  microprotein was detected in these cell lines localized mainly in the nucleus and at the
  cell-to-cell junctions"]. Overexpressed FLAG-TUBL: cytoplasm in HeLa [PMID:34351912
  "Immunofluorescence microscopic analysis revealed that FLAG epitope–tagged TUBL was diffusely
  distributed throughout the cytoplasm when expressed in HeLa cells"]. IHC in SCC is cytoplasmic.

### Decisions
- Locations: all accepted (nucleus, cytoplasm, anchoring junction).
- Keratinocyte proliferation IMP: kept as non-core (context-dependent; opposite direction in
  transformed cells; molecular route unknown).
- Wound healing ISS (from mouse A0A1B0GRQ3 frameshift mice): non-core.
- NEW: SUMO binding GO:0032183 (direct, SIM-dependent, PMID:36369429); positive regulation of
  epithelial cell differentiation GO:0030858 (start-codon KO + rescue; it is the pTINCR
  protein that acts, via CDC42). Did not propose small GTPase binding as an MF (co-IP only;
  direct binding not shown) nor protein sumoylation regulation (mechanism unknown: TINCR is
  not an E3; it may act as a SUMO-loaded adaptor).
