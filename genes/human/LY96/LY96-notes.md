# LY96 (MD-2) review notes

UniProt Q9Y6Y9, lymphocyte antigen 96 / myeloid differentiation protein 2. 160 aa,
signal peptide 1-18, ML (MD-2-related lipid-recognition) domain, no transmembrane
segment. Isoform 2 lacks residues 38-68.

## Deep research status

The background deep-research job finished (exit 0) but produced
`LY96-deep-research-asta.md` (Asta corpus retrieval), not a Falcon report. Its 20
retrieved papers are generic bioinformatics/database papers unrelated to MD-2
(IgAN subtyping, CRONOS, LIPID MAPS, etc.), so it contributed nothing to this
review. The review was built from the UniProt record, the cached GOA publications
(all 14 cached; several abstract-only) and the cached Reactome entries.

## Biology, with provenance

- Discovery: MD-2 is needed for TLR4 to respond to LPS.
  [PMID:10359581 "Here, we report that a novel molecule, MD-2, is requisite for LPS signaling of TLR4."]
  [PMID:10359581 "MD-2 is physically associated with TLR4 on the cell surface and confers responsiveness to LPS."]
  MD-2 reaches the surface only with TLR4:
  [PMID:10359581 "These results are consistent with membrane anchoring of MD-2 via physical association with TLR4."]
- Secreted protein, disulfide-linked oligomers, soluble MD-2 is active:
  [PMID:11593030 "MD-2 contains a leader sequence but lacks a transmembrane domain, and we asked whether it is secreted into the medium as an active protein."]
  [PMID:11593030 "We conclude that normal and transfected cells secrete a soluble form of MD-2 that binds with high affinity to TLR4 and that could play a role in regulating responses to LPS and other pathogen-derived substances in vivo."]
- Two separable surfaces: TLR4-binding (C95-C105 region) and LPS-responsiveness (basic/aromatic region).
  [PMID:14607928 "MD-2 binding to TLR4 was dependent on Cys(95) and Cys(105), which might form an intramolecular disulfide bond."]
  [PMID:14607928 "Thus, our data indicate that MD-2 interaction with TLR4 is necessary but not sufficient for cellular response to LPS."]
- LPS is crosslinked to MD-2 and TLR4 in the CD14-containing complex:
  [PMID:11274165 "Thus, LPS binds directly to each of the members of the tripartite LPS receptor complex."]
- Structures: MD-2 binds the concave face of TLR4 ectodomain; ligand sits in MD-2's hydrophobic pocket.
  [PMID:17803912 "MD-2 binds to the concave surface of the N-terminal and central domains."]
  [PMID:17803912 "The interaction with Eritoran is mediated by a hydrophobic internal pocket in MD-2."]
  [PMID:19252480 "LPS interacts with a large hydrophobic pocket in MD-2 and directly bridges the two components of the multimer."]
  [PMID:22532668 "TLR4 alone does not directly bind LPS and requires the coreceptor MD-2"]
  [PMID:22532668 "MD-2 has a unique hydrophobic cavity that directly binds to lipid A, the active center of LPS."]
  [PMID:22532668 "Human MD-2 binds lipid IVa in an antagonistic manner completely differently from the way mouse MD-2 does."]
- Not involved in LTA sensing via TLR2 (at least for the LTA preparations tested):
  [PMID:12594207 "Additional transfection with MD-2 did not affect stimulation of these cells by LTA."]
- Other ligands of the MD-2 pocket: morphine
  [PMID:22474354 "We demonstrate that morphine binds to an accessory protein of Toll-like receptor 4 (TLR4), myeloid differentiation protein 2 (MD-2), thereby inducing TLR4 oligomerization and triggering proinflammation."];
  heme (Reactome R-HSA-9707594); HMGB1 binds the TLR4/MD-2 complex [PMID:20547845].
- Der p 2 (house dust mite allergen) is an MD-2 structural/functional mimic and co-IPs with MD-2
  [PMID:19060881 "Direct association of Der p 2-HA and MD-2-FLAG was shown by co-immunoprecipitation in cell lysates using antibodies to HA and FLAG"].

## Which receptor MF belongs to MD-2 vs TLR4

- The recognition step (binding lipid A) is performed by MD-2's pocket; TLR4 alone does not
  bind LPS [PMID:22532668]. The one exposed acyl chain and the phosphates contact TLR4 and
  drive the 2:2:2 dimerisation [PMID:19252480].
- Transmembrane transmission and TIR-domain signalling belong to TLR4 alone; MD-2 has no
  transmembrane or cytoplasmic part.
- So: MD-2 directly *enables* LPS binding (GO:0001530) and coreceptor activity (GO:0015026 —
  "combining with an extracellular messenger, and in cooperation with a nearby primary
  receptor, initiating a change in cell activity" fits MD-2 exactly), and *contributes to*
  GO:0001875 LPS immune receptor activity, which is a property of the TLR4-MD-2 heterodimer.
  The existing `enables` GO:0001875 rows (IBA + IDA PMID:19252480) are accepted: MD-2 is the
  ligand-binding subunit of a two-chain receptor and does the recognition half of the work;
  in core_functions it is recorded as contributes_to.
- Process: detection of lipopolysaccharide (GO:0032497) is a direct participation — MD-2
  performs the detection step. TLR4 signalling pathway: MD-2 is part of the receptor that
  initiates it.

## Annotation decisions (summary)

- protein binding IPI rows with TLR4 partner -> MODIFY to GO:0035662 Toll-like receptor 4 binding.
- protein binding with Der p 2, LCN2, MESD -> REMOVE (uninformative; xeno allergen mimic / HuRI Y2H).
- cellular defense response (TAS) -> MODIFY to innate immune response.
- cell surface receptor signaling pathway (TAS) -> MODIFY to toll-like receptor 4 signaling pathway.
- positive regulation of LPS-mediated signaling (IBA) -> KEEP_AS_NON_CORE: MD-2 is a receptor
  subunit rather than a regulator, though soluble MD-2 does set cell responsiveness.
- positive regulation of TNF production -> KEEP_AS_NON_CORE (downstream output).
- endosome membrane (Reactome) -> KEEP_AS_NON_CORE (TLR4-MD-2 internalised for TRAM/TRIF branch).
- No NEW annotations.
