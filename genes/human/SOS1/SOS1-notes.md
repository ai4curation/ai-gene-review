# SOS1 (human, Q07889) curation notes

## Identity and architecture

- Son of sevenless homolog 1, 1333 aa; PANTHER PTHR23113:SF168 (SON OF SEVENLESS HOMOLOG 1) in the PTHR23113 RasGEF family. Domains: N-terminal tandem histone fold (~1-198), DH (200-390), PH (444-548), REM / N-terminal Ras-GEF (597-741), CDC25-homology Ras-GEF (780-1019), C-terminal proline-rich tail (1020-1333) [file:human/SOS1/SOS1-uniprot.txt; file:human/SOS1/SOS1-deep-research-falcon.md].
- Paralog SOS2 (Q07890), reviewed in genes/human/SOS2 — term choices kept consistent (GO:0005085 for GEF, GO:0017124 for SH3-partner rows, REMOVE histone-fold heterodimerization IEA).
- GO:0005088 "Ras guanyl-nucleotide exchange factor activity" no longer resolves in the local GO build (merged into GO:0005085), so GO:0005085 is used for both Ras and Rac exchange.

## Molecular function

- Ras GEF: [PMID:8493579 "This hSos1 domain specifically stimulated guanine nucleotide exchange on mammalian Ras proteins in vitro."] [PMID:8493579 "Thus hSos1 is a guanine nucleotide exchange factor for Ras."]
- Mechanism (structure of H-Ras:Sos): [PMID:9690470 "the insertion into Ras of an alpha-helix from Sos results in the displacement of the Switch 1 region of Ras, opening up the nucleotide-binding site"].
- Allosteric Ras-GTP site (positive feedback): [PMID:12628188 "a highly conserved Ras binding site on SOS that is located distal to the active site and is specific for Ras.GTP"]; [PMID:15507210 "the DH-PH unit blocks the allosteric binding site for Ras and suppresses the activity of SOS"]; [PMID:18454158 "The activity of the SOS catalytic unit (SOS(cat)) is up to 500-fold higher when Ras is on membranes compared to rates in solution, because the allosteric Ras site anchors SOS(cat) to the membrane."]; [PMID:20133692 "the histone domain plays a dual role in occluding the allosteric site and in stabilizing the autoinhibitory conformation of the DH-PH unit"].
- Autoinhibition by N and C termini: [PMID:9447984 "both the amino and the carboxyl terminus domains of Sos are involved in the negative regulation of its catalytic activity"].
- Rac GEF (DH-PH; context dependent): [PMID:9438849 "the DH domain of Sos stimulated guanine nucleotide exchange on Rac but not Cdc42 in vitro and in vivo"]; [PMID:11777939 "Grb2 and E3b1 bind through their SH3 domains to the same binding site on Sos-1, thus determining the formation of either a Sos-1-Grb2 (S/G) or a Sos-1-E3b1-Eps8 (S/E/E8) complex, endowed with Ras- and Rac-specific GEF activities, respectively"]; [PMID:16520382 "p66shc, an adaptor protein that promotes oxidative stress, increases the rac1-specific GEF activity of sos1, resulting in rac1 activation"]. Deep research cautions that in vivo Rac catalysis is less secure than Ras exchange.
- SH3-ligand (proline-rich tail): [PMID:8493579 "This interaction was mediated by the carboxyl-terminal domain of hSos1 and the Src homology 3 (SH3) domains of GRB2."]; [PMID:19323566 "the Grb2-Sos1 interaction is mediated through the combinatorial binding of nSH3 and cSH3 domains of Grb2 to various sites containing PXpsiPXR motifs within Sos1"]; [PMID:14679214 "The proline-rich Sos peptide retrieved only SH3 domain containing proteins as specific binding partners."]. Other SH3 partners: NCK1/NCK2 [PMID:10206341 "We found that exclusively the third (C-terminal) SH3 domain of Nck has the ability to bind to Sos."], Tks5/SH3PXD2A [PMID:19464300], HCK, CRK, PLCG1, PIK3R1, PACSIN3, SNX9, nebulin, UBASH3A (screens).
- Multivalent condensate component with pLAT/GRB2 [PMID:27056844 "pLAT, Grb2, and Sos1 all colocalized within clusters, and clusters did not form if either Grb2 or Sos1 was omitted"].
- HD region binds CSN3/COPS3, regulating SOS1 stability [PMID:30631038].

## Location

- Cytosolic when inactive; recruited by GRB2 to activated RTKs at the cytoplasmic face of the plasma membrane [PMID:16520382 "The translocation of the grb2–sos1 complex from the cytosol to the membrane upon RTK activation allows the presentation of sos1 to ras"].

## Process

- Core: Ras protein signal transduction downstream of RTKs (EGFR, PDGFR, FGFR, KIT, FLT3, MET, ERBB2/4, insulin/IGF1R, TRK), and immunoreceptors (TCR/LAT, BCR/BLNK, FCERI) — all Reactome events place GRB2:SOS1 as the Ras exchanger.
- Rac signalling via EPS8/ABI1 tricomplex (non-canonical, secondary).
- Disease: Noonan syndrome 4 (gain of function; mutations cluster in autoinhibitory interfaces) [PMID:17143282 "SOS1 mutations cluster at codons encoding residues implicated in the maintenance of SOS1 in its autoinhibited form."], [PMID:17143285 "Noonan syndrome-associated SOS1 mutations are hypermorphs encoding products that enhance RAS and ERK activation."]; hereditary gingival fibromatosis 1 (C-terminal frameshift) [PMID:11868160].

## Curation decisions (summary)

- 56 GO:0005515 IPI rows: SH3-domain partners -> MODIFY to GO:0017124 SH3 domain binding (as for SOS2); HRAS allosteric-site papers -> MODIFY to GO:0031267 small GTPase binding; HRAS catalytic-site papers -> MODIFY to GO:0005085; EGFR, SHC1 (indirect via GRB2) and COPS3 -> REMOVE (uninformative; interaction not disputed).
- GO:0005096 GTPase activator activity (TAS, PMID:9790532) -> MODIFY to GO:0005085: the DH domain is a Rho-family GEF, not a GAP.
- GO:0046982 heterodimerization (histone-fold InterPro2GO) -> REMOVE (intramolecular tandem histone fold).
- GO:1905360 GTPase complex (IPI, SOS1:RAS) -> MARK_AS_OVER_ANNOTATED: the SOS1:RAS complex is a transient enzyme-substrate intermediate with nucleotide-free Ras, not a complex with GTPase activity.
- EXP GEF rows citing PMID:1371879, PMID:16483568 (a review), PMID:7731718 do not assay SOS1 in their abstracts; ACCEPT on the function (well established) and flag the references.
- PMID:23027131 (Wnt4/Ras) and PMID:9054499 (oncogenic Ras senescence) abstracts do not mention SOS1; experimental annotations not removed. Transcription regulation and both proliferation rows MARK_AS_OVER_ANNOTATED (downstream outcomes of Ras-ERK signalling; not removed).
- 126 Reactome cytosol TAS rows accepted (cytosolic pool; events are GRB2:SOS1 recruitment, Ras exchange, or signalosome events that carry SOS1 as a complex member).
- PMID:19593445 (known batch miscitation) does not occur in SOS1 GOA.
