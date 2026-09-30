# TIRAP (Mal) review notes — human, P58753

## Identity and architecture
- 221 aa; disordered N-terminal region (1-82) and TIR domain (84-213) per UniProt; two intra-domain
  disulfides (C89-C134, C142-C174) seen in crystal structures.
- N-terminal PIP2-binding domain targets TIRAP to the plasma membrane
  [PMID:16751103 "We find that TIRAP contains a phosphatidylinositol 4,5-bisphosphate (PIP2) binding domain, which mediates TIRAP recruitment to the plasma membrane."]
  [PMID:21873236 "MAL associates constitutively with the plasma membrane through a phosphatidylinositol-4,5-bisphosphate (PIP2)-binding motif at the N terminus of the protein"]

## Core function: bridging/sorting adaptor for TLR2 and TLR4 -> MyD88
- [PMID:11544529 "Mal associates with TLR-4. Mal is therefore an adapter in TLR-4 signal transduction."]
- [PMID:16751103 "TIRAP then functions to facilitate MyD88 delivery to activated TLR4 to initiate signal transduction."]
- [PMID:17258210 "We show that the TLR adaptor Mal is critical for linking Myeloid Differentiation primary response protein 88 (MyD88) to TLR2 and TLR4."]
- Mouse KO: [PMID:12447441 "Instead, TIRAP has a crucial role in the MyD88-dependent signalling pathway shared by TLR2 and TLR4."]
  and not needed for TLR3/7/9: [PMID:12447441 "they also show defective response to TLR2 ligands, but not to stimuli that activate TLR3, TLR7 or TLR9."]
- D96N loses MyD88 binding but keeps TLR2/TLR4 binding, and is signaling-dead
  [PMID:19509286 "Moreover, co-immunoprecipitation studies revealed that Mal D96N is unable to interact with MyD88, a prerequisite for downstream signaling to occur."]
- IFN-beta induction by LPS is TIRAP-independent
  [PMID:19509286 "D96N expressing macrophages induced comparable amounts of IFN-β mRNA as WT and Mal-deficient cells."]
  (contrast: [PMID:12062447 "Notably, our investigation revealed a critical function for TIRAP/MAL, a signaling adapter for Toll-like receptor (TLR) 4, in LPS-induced but not dsRNA-induced activation of IRF-3."] — abstract only, overexpression/DN era; not supported by KO data).
- TLR2: S180L loses TLR2 binding and attenuates TLR2 signaling
  [PMID:17322885 "We found that the Mal S180L variant attenuated TLR2 signal transduction."]. Experiments used
  Malp2 (called "TLR2 ligand" in the paper), not a TLR1:TLR2-specific ligand, so the GOA TLR1:TLR2 IDA was
  generalized to GO:0034134.

## Other partners
- RAGE (AGER): direct binding to phosphorylated RAGE tail [PMID:21829704 "Binding of TIRAP but not MyD88 to the cytoplasmic domain of RAGE was confirmed to be direct by an in vitro protein interaction assay using recombinant proteins (data not shown)."]
- PI3K p85alpha after TLR2/6 stimulation [PMID:19574958 "On stimulation of the TLR2/6 heterodimer with diacylated bacterial lipoproteins, Mal directly interacts with the regulatory subunit of phosphoinositide 3-kinase (PI3K), p85alpha, in an inducible fashion."]
- PKCdelta via TIR domain [PMID:17161867 "Truncation mutants of TIRAP/Mal showed that the TIR domain of TIRAP/Mal is responsible for binding."]
- IRAK2 via TIR domain [PMID:11544529 "Mal associates with IRAK-2 by means of its TIR domain."]
- Pathogen mimics: Brucella TcpB [PMID:24275656], HBeAg [PMID:21334391].

## Source tracing for ISS rows (mouse Q99JY1, QuickGO 2026-09-30)
- myeloid cell differentiation <- MGI IMP PMID:11526399 (DC maturation readout) -> over-annotation.
- regulation of IFN-beta production <- BHF IDA PMID:14630816 (not read) -> over-annotation given KO data.
- positive regulation of TLR3 signaling <- BHF IDA PMID:17322885 on mouse; the Khor paper does not test TLR3;
  contradicted by PMID:12447441 and PMID:19509286 -> REMOVE.
- neutrophil chemotaxis <- BHF IMP PMID:18039275 (not read) -> indirect via chemokines -> over-annotation.
- B cell proliferation, IL-12, CXCL1/2 <- mouse KO cytokine/proliferation phenotypes -> non-core.

## Key decisions
- 'positive regulation of TLR2/TLR4 signaling' IMP rows -> MODIFY to pathway membership (TIRAP is a
  component, not a regulator).
- general adaptor MF (GO:0060090, GO:0030674) -> MODIFY to GO:0035591 signaling adaptor activity.
- protein binding: MODIFY to TLR4 binding / RAGE receptor binding / PI3K regulatory subunit binding /
  protein kinase binding / signaling adaptor activity where the paper supports it; REMOVE HT and pathogen rows.
- cell surface IDA (PMID:12447441, abstract-only, no localization data in abstract) -> MODIFY to GO:0031234;
  TIRAP is on the cytoplasmic face, not exposed at the cell surface.
- 3'-UTR mRNA stabilization -> over-annotation (distal consequence).
- GO-CAM index: TIRAP appears in 5 human models with GO:0035591 / GO:0060090 / GO:0030674 and TLR4 or
  TLR1:TLR2 pathways — consistent with the core function chosen.

## Project questions (INNATE_IMMUNITY / TLR batch)
- TIRAP carries only vertebrate TLR-pathway terms (GO:0002224 branch); no GO:0008063 Toll signaling
  conflation. The TLR3 regulation row is the only ligand/receptor-specific term that is wrong.
