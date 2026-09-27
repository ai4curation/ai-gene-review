# GRB2 (human, P62993) curation notes

## Identity and domain architecture

- 217-aa, ~25 kDa, non-catalytic adaptor: N-SH3 - SH2 - C-SH3; GRB2/sem-5/DRK family
  [file:human/GRB2/GRB2-uniprot.txt "Non-enzymatic adapter protein that plays a pivotal role in precisely regulated signaling cascades from cell surface receptors to cellular responses"].
- Isoform 2 (GRB3-3) lacks part of the SH2 domain, does not bind phosphorylated EGFR and acts as a dominant negative (UniProt isoform 2 FUNCTION).

## Core molecular functions (with provenance)

1. **SH2 phosphotyrosine recognition (GO:0001784).**
   - EGFR: [PMID:7518560 "Grb2 binds directly to the EGFR at Y-1068, to a lesser extent at Y-1086, and indirectly at Y-1173"].
   - IRS-1 / Shc: [PMID:8491186 "mediated by the binding of the SH2 domain of GRB2 to phosphotyrosines on both IRS-1 and Shc"]; IRS-1 pY895 [PMID:7504175 "the SH2 domain in GRB2 and the amino-terminal SH2 domain in SHPTP2 (Syp) specifically bind to Tyr(P)-895 and Tyr(P)-1172, respectively"].
   - BCR pY177 [PMID:8112292 "the Grb2 SH2 domain bound Bcr-Abl through recognition of a tyrosine phosphorylation site within the amino-terminal bcr-encoded sequence"].
   - FAK pY925 [PMID:7597091 "tyrosine-phosphorylated pp125FAK directly interacts with the SH2 domain of Grb2"]; SHP2 pY584 [PMID:8959326 "mutation of tyrosine 584, but not tyrosine 546, to phenylalanine totally abolished the binding of Grb2 to SHP-2"].
   - Specificity pY-x-N [PMID:8663178 "the SH2 domain of the adapter protein Grb2 predominantly selected beads with the sequence Y*ENDP"].
2. **SOS adaptor (GO:0005091).** [PMID:8386805 "Cellular Grb2 appears to form a complex with a guanine-nucleotide-exchange factor for Ras, which binds to the ligand-activated EGF receptor, allowing the tyrosine kinase to modulate Ras activity"]; simultaneous SH2/SH3 occupancy [PMID:7527391 "Saturation of the SH2 domain of Grb2 with the EGFR phosphopeptide was found not to affect its subsequent binding to the Sos peptide"].
3. **RTK adaptor bridging other effectors (GO:0005068).** PI3K-C2beta [PMID:11533253 "Using immobilized, phosphorylated EGF receptor, recombinant PI3K-C2beta was only purified in the presence of Grb2"]; Cbl [PMID:23799367 "The ubiquitination threshold is mechanistically determined by the cooperative recruitment of the E3 ligase Cbl, in complex with Grb2, to the EGFR"]; HPK1 [PMID:9346925 "induced recruitment of the Grb2.HPK1 complex to the autophosphorylated EGF receptor and to the Shc docking protein"]; Tom1L1 [PMID:19798056 "resulting in transient interaction of Tom1L1 with the activated EGFR bridged by Grb2 and Shc"].
4. **Immune signalosome adaptor (GO:0030674; TCR signalling).** [PMID:25870599 "Our data demonstrate that the ability of GRB2 to facilitate protein clusters is equally important in regulating TCR-mediated functions as its capacity to recruit effector proteins"]; THEMIS/SHP1 [PMID:25535246 "SHP1 and THEMIS engage with the N-SH3 and C-SH3 domains of GRB2, respectively, a configuration that allows GRB2-SH2 to recruit the complex onto LAT"].
5. **SH3 proline-rich recognition (GO:0070064).** GAREM1 [PMID:19509291 "the proline-rich motifs of GAREM are recognized by the N- and C-terminal SH3 domains of Grb2"]; Spry2 [PMID:16893902 "This PXXPXR motif binds directly to the N-terminal Src homology domain 3 of Grb2"]; Dab2 [PMID:9569023 "These data indicate that Dab2 binds to the SH3 domains of Grb2 via its C-terminal proline-rich sequences"].

## Other biology (non-core)

- Homodimer; dimeric GRB2 restrains basal FGFR2 [PMID:22726438 "Dimeric Grb2 binds to the C termini of two FGFR2 molecules"]; GAB1 binds GRB2 dimer [PMID:22536782 "whereas Grb2 exists in a monomer-dimer equilibrium"].
- Nuclear GRB2 in miRNA biogenesis [PMID:37328606 "The N-terminal SH3 domain of GRB2 is recruited to the PAZ domain of AGO2 forming a ternary complex containing GRB2, AGO2 and DICER1"].
- Autophagy/BECN1 association [PMID:38182563 "GRB2 co-immunoprecipitated with BECN1 in several breast cancer cell lines"].
- NK cytotoxicity via DAP10 [PMID:16582911 "For full calcium release and cytotoxicity to occur, both Grb2-Vav1 and p85 had to bind to DAP10"].
- EGFR endocytosis [PMID:14985334 "Thus, CALM is the second protein besides Grb2 that appears to play a specific role in EGFR endocytosis"].

## Curation decisions and rationale

### GO:0005515 protein binding (564 rows; 162 papers; 207 partners)

Partners were resolved via UniProt REST. Decision was made per (paper, partner) after reading
each cached abstract (full text where needed):

- **High-throughput studies** (HuRI, HI-II-14, BioPlex 2/3, cell maps, MAPK Y2H, liver Y2H,
  ND network, SRM GRB2 dynamics PMID:21706016, PATS SH3 peptide arrays PMID:17474147, etc.)
  -> REMOVE. No binding mode or GRB2 activity is resolved per pair. Reason text notes when the
  partner is a known phosphotyrosine or SH3 partner and where the informative MF is captured.
- **Small-scale, phosphotyrosine/SH2-dependent** (EGFR, Shc, IRS-1, LAT, LAT2, LAX, BLNK,
  Kit, Axl, EphB1, SHP2, FAK, BCR, PTPalpha, PLD2, G6f, FCRL6, magicin pY64, TSPAN2 pY124)
  -> MODIFY to GO:0001784 phosphotyrosine residue binding.
- **Small-scale, SH3/proline-rich motif mapped** (GAREM1, Spry2, Dab2, GAB1 RXXK, HD-PTP,
  srGAP3, REPS2, ADAM15, 5-LO, WASP, HCV NS5A, p66Shc CH2 PPLP, Sos peptides in NMR/ITC)
  -> MODIFY to GO:0070064 proline-rich region binding. GO:0017124 SH3 domain binding is the
  reverse direction (it describes the ligand, not GRB2) and is not used. (The mouse Grb2
  review REMOVEd its SH3-ligand rows; here, where the motif is mapped, the informative MF is
  proposed instead. GO:0070064 is used for other SH3 proteins in human GOA, e.g. ABL1, BAIAP2, ITSN1.)
- **SOS with adaptor evidence** (Grb2-Sos bridging to phosphopeptides/receptors, Ras coupling)
  -> MODIFY to GO:0005091.
- **GRB2 bridging an effector to an activated RTK** (PI3K-C2beta, Gab2, Tom1L1, Cbl, HPK1,
  EGFR-Cbl mediator) -> MODIFY to GO:0005068.
- **GRB2 bridging in LAT signalosome** (THEMIS, SHP1; PTP1B-IRS-1 complex) -> MODIFY to GO:0030674.
- Everything else (co-IP without mapping, GRB2 as comparator in papers about Nck/Grap/Gads,
  abstracts not describing the GRB2 measurement) -> REMOVE with the standard caveat that removal
  does not mean the interaction is false.
- Special cases: PMID:9175774 (Shc peptide binds GRB2 SH2 *regardless* of phosphorylation) ->
  REMOVE rather than GO:0001784; PMID:16696976 (GRB2 N-SH3 inactive on dynamin endocytosis) -> REMOVE;
  PMID:9788432 WITH/FROM is MAP4K5/KHS, which the abstract says binds exclusively Crk proteins -> REMOVE;
  PMID:21725282 WITH/FROM is PTPRT but abstract concerns RPTPalpha -> REMOVE (noted).

### Other notable calls

- GO:0045953 negative regulation of NK cell mediated cytotoxicity (IDA PMID:25870599) -> REMOVE:
  the full text (cached) is about CD4+ T cells and contains no NK or cytotoxicity data; GRB2 is a
  positive requirement in NKG2D-DAP10 cytotoxicity (PMID:16582911).
- GO:0017124 SH3 domain binding (IDA PMID:19509291) -> MODIFY to GO:0070064 (direction reversed).
- GO:0042802 identical protein binding -> MODIFY to GO:0042803 homodimerization for PMID:22536782
  and PMID:22726438; over-annotated for the SILAC pulldown (PMID:12577067).
- GO:0008180 COP9 signalosome (IBA/IDA/IEA) -> MARK_AS_OVER_ANNOTATED, consistent with mouse Grb2.
- GO:0007165 signal transduction IBA -> MODIFY to GO:0007265, consistent with mouse Grb2.
- GO:0003723 RNA binding (HDA) and extracellular exosome (HDA) -> MARK_AS_OVER_ANNOTATED.
- NEW: GO:0050852 T cell receptor signaling pathway (PMID:25870599). Participation: GRB2 is the
  adaptor that cross-links pLAT to effectors. Comparator: LAT and LCP2/SLP-76 carry GO:0050852 in GOA.
- 305 Reactome cytosol TAS rows and 8 plasma membrane TAS rows -> ACCEPT (correct locations).
