# GNAT1 (human, UniProtKB:P11488) review notes

Journal of what was read and what was decided. Quotes are verbatim from the cached file
named in the bracket. No deep-research report existed when this was started (see the last
section for whether one arrived).

## 1. What the gene product is

GNAT1 encodes the alpha subunit of rod transducin (Gt), the heterotrimeric G protein that
couples photoactivated rhodopsin to the rod cGMP phosphodiesterase PDE6.

- UniProt record (`GNAT1-uniprot.txt`, P11488, 350 aa). The FUNCTION comment is mostly
  "By similarity" to bovine GNAT1 (P04695); the one statement with a publication tag on the
  human protein is "Essential for normal RHO-mediated light perception in retinal rod
  photoreceptors (PubMed:22190596)".
- Catalytic activity (GTP + H2O = GDP + phosphate), Mg(2+) cofactor, RGS9 as GAP, the
  heterotrimer GNAT1/GNB1/GNGT1, the RHO and PDE6 interactions and all GTP/Mg binding
  residues are tagged `ECO:0000250|UniProtKB:P04695`, i.e. transferred from the bovine
  protein. Human-specific experimental statements are: N-myristoyl glycine at Gly-2 and
  the UNC119 interaction (PubMed:21642972), phosphotyrosine 142 by SRC (PubMed:11032890),
  tissue specificity (PubMed:1614872, PubMed:22190596) and the three disease variants
  (G38D, D129G, Q200E).
- Subcellular location in UniProt: photoreceptor outer segment membrane, lipid-anchor;
  photoreceptor inner segment (by similarity to mouse P20612); "Localizes mainly in the
  outer segment in the dark-adapted state, whereas is translocated to the inner part of
  the photoreceptors in the light-adapted state."
- Family: G-alpha family, G(i/o/t/z) subfamily. PANTHER PTHR10218 (GTP-BINDING PROTEIN
  ALPHA SUBUNIT), subfamily PTHR10218:SF67 (names read from `interpro/panther/panther.obo`).

## 2. GOA-cited publications (all five are abstract-only in the cache)

- PMID:8673138 (Dryja 1996, Nougaret G38D). Human genetics. [PMID:8673138 "the alpha
  subunit of rod transducin the G-protein that couples rhodopsin to cGMP-phosphodiesterase
  in the phototransduction cascade"]. Night blindness with normal cone vision:
  [PMID:8673138 "Patients with congenital stationary night blindness enjoy normal daytime
  vision, which is mediated by cone photoreceptors"]. Supports visual perception (TAS) and
  the generic signal transduction (NAS) rows.
- PMID:17584859 (Szabo 2007, Q200E). Human family plus modelling and a trypsin protection
  assay. [PMID:17584859 "the evolutionarily highly conserved Switch 2 region of
  alpha-transducin, a domain that has an important role in binding and hydrolyzing GTP"];
  [PMID:17584859 "the p.Gln200Glu mutant exhibits impaired GTPase activity, and thereby
  leads to constitutive activation of phototransduction"]. The abstract also records that
  the Nougaret protein [PMID:17584859 "produces an alpha-transducin that is unable to
  activate its downstream effector molecule in vitro"]. The GTPase row from this paper is
  NAS (an author statement), the phototransduction and detection-of-light rows are IMP
  (the dominant mutant phenotype). Full text not read.
- PMID:22190596 (Naeem 2012, recessive D129G). [PMID:22190596 "a missense mutation in
  GNAT1, p.D129G, was identified, which segregated within the family, consistent with an
  autosomal recessive mode of inheritance"]; expression: [PMID:22190596 "Gnat1 is expressed
  at approximately postnatal day (P)7 and is predominantly expressed in the retina"].
  Supports visual perception IMP.
- PMID:2534964 (Lerea 1989). The abstract is about cone transducin alpha (Tc alpha, now
  GNAT2) immunolabelling in human cones; for the rod protein it says only [PMID:2534964
  "cDNA clones corresponding to human rod and cone transducin alpha subunit (Tr alpha and
  Tc alpha) genes were isolated"]. GOA carries two IDA rows from this paper on GNAT1
  (photoreceptor outer segment, photoreceptor inner segment). The abstract does not show a
  rod-alpha localization experiment, and the full text is not in the cache, so I cannot
  see what the curator saw. The locations themselves are independently established for
  rod transducin (section 4). Not treated as a wrong-gene defect: a title that foregrounds
  the paralog is not evidence of one.
- PMID:7822269 (Wedegaertner 1995, review). [PMID:7822269 "G protein alpha subunits and
  beta gamma dimers are covalently modified by lipids"]. Source of the NAS `membrane` row.

## 3. Reactome entries cited by GOA

- R-HSA-2485182 (Gt-GTP dissociates): [Reactome:R-HSA-2485182 "Transducin activation is
  the first amplifying step in visual transduction. Many findings came from bovine
  experiments"]. Disc-membrane location.
- R-HSA-2584246 (GNAT1-GTP hydrolyses its bound GTP): [Reactome:R-HSA-2584246 "Active Gt
  alpha (GNAT-GTP) can be inactivated by a slow, intrinsic GTPase activity that hydrolyses
  GTP to GDP"]; [Reactome:R-HSA-2584246 "Shutoff of Gt is the rate-limiting step in the
  recovery of the single photon response of rods"]. GTPase activity TAS and disc membrane.
- R-HSA-74059 (PDE6 hydrolyses cGMP): [Reactome:R-HSA-74059 "activated transducin
  (GNAT1-GTP) sustains PDE6 activation allowing it to hydrolyze cGMP at a rate limited only
  by diffusional access to substrate"].
- R-HSA-2534087 (NMT1/2 myristoylate GNAT1) and R-HSA-2534096 (METAP1/2 remove the
  initiator Met; the event name says "demethylates", the text describes Met removal). These
  are the two `cytosol` TAS rows: co-translational processing of the nascent chain, not a
  place where transducin works.
- R-HSA-420883, R-HSA-8982637, R-HSA-8982640 ("Opsins act as GEFs for G alpha-t" etc.).
  These three belong to the generic "G alpha (i) signalling events"/opsin events and are
  drawn at the plasma membrane; they give the three `plasma membrane` TAS rows. Their text
  itself says the protein is in rods: [Reactome:R-HSA-420883 "alpha-1 chain (expressed in
  rods by GNAT1)"]. In rods rhodopsin and transducin sit on the disc membranes, which are
  sealed off from the plasma membrane (GO:0120202 definition, read in QuickGO), so
  `plasma membrane` is the compartment the generic Reactome drawing uses, not the rod one.
- R-HSA-2514859 (inactivation, recovery and regulation of the phototransduction cascade):
  pathway-level TAS for `regulation of opsin-mediated signaling pathway`.

## 4. Donor annotations behind the ISS/IEA/IBA rows (QuickGO, queried 2026-11)

Bovine GNAT1 P04695: acyl binding IDA PMID:9498812; G protein activity IMP PMID:16469737,
IDA PMID:31300275, IMP PMID:33007200; GTP binding IMP PMID:11024022 and IDA PMID:9498812;
GDP binding IMP PMID:11024022 and IDA PMID:2538446; protein kinase binding IDA
PMID:11032890; response to light stimulus IDA PMID:17507570; negative regulation of
cyclic-nucleotide phosphodiesterase activity IDA PMID:2538446; transducin-mediated opsin
signaling pathway IDA PMID:31300275 and IMP PMID:33007200; photoreceptor outer segment
membrane IDA PMID:9498812; heterotrimeric G-protein complex IDA PMID:31300275 and
PMID:8552184; membrane EXP PMID:23303210 and PMID:28655769.

Mouse Gnat1 P20612: GTPase activity IDA PMID:17881533; G-protein beta/gamma-subunit
complex binding IDA PMID:17881533; photoreceptor connecting cilium IDA PMID:17881533;
photoreceptor outer segment IDA (PMID:18367617, 20592197, 29410614, 31696965);
photoreceptor inner segment IDA PMID:31696965; phototransduction IMP PMID:11095744.

Rat Gnat1 D3ZSS5: bitter-taste detection IDA PMID:7596440; GTP binding IDA PMID:7596440;
cGMP catabolic process IDA PMID:7878085; response to light intensity IDA PMID:11931744;
G protein-coupled opsin signaling pathway IMP PMID:11931744; outer segment, inner segment,
neuronal cell body and heterotrimeric G-protein complex IDA PMID:11931744; apical plasma
membrane IDA PMID:17495045.

Chicken GNAT1 Q9DG28 (AgBase): response to light stimulus IDA PMID:10854264; membrane IDA
PMID:10854264.

## 5. PAINT

`just paint-losses human GNAT1`: "No IRD or IKR loss on this gene's lineage."
`interpro/panther/PTHR10218/PTHR10218-paint.tsv`:
- root node PTN000026392 (Eukaryota): cytoplasm, heterotrimeric G-protein complex, G
  protein activity, adenylate cyclase-modulating GPCR signaling pathway (GO:0007188). The
  only losses recorded for GO:0007188 are two fungal nodes (PTN000812114, PTN000812123);
  nothing removes it from the transducin clade.
- transducin-alpha-1 node PTN002566486 (Euteleostomi): photoreceptor outer segment,
  phototransduction visible light, detection of light stimulus involved in visual
  perception. Human GNAT1 is itself one of the seeds, which is expected.
- the bitter-taste term GO:0001580 has an IBD at PTN002566474, the cone transducin
  (GNAT2) node, seeded by rat Gnat2 (RGD:1309514). It is not placed on the GNAT1 node, so
  the bitter-taste row on human GNAT1 is the Ensembl transfer from rat Gnat1 only.
- No FamilyReview exists for PTHR10218 (folder has entries, metadata and paint.tsv only).

## 6. The role others give GNAT1

- GO-CAM gomodel:6918f23700000035 (dim light signalling by RHO via transducin): GNAT1
  enables G protein activity (GO:0003925), occurs in rod photoreceptor disc membrane
  (GO:0120202) of retinal rod cell, part of transducin-mediated opsin signaling pathway
  (GO:0141190), itself part of visual perception. RHO G protein-coupled photoreceptor
  activity has GNAT1 as input and directly positively regulates the GNAT1 activity; GNAT1
  directly negatively regulates the PDE6G enzyme inhibitor activity.
- Module `modules/visual_phototransduction.yaml`: rod transducin heterotrimer
  (GNAT1/GNB1/GNGT1) G protein activity, target PDE6G, process GO:0141190, location
  GO:0120202.
- Possible defect in the GO-CAM, not in this gene's GOA: the evidence on the GNAT1 ->
  PDE6G causal edge is keyed to PMID:33762731, whose cached title is "Structural insights
  into the lipid and ligand regulation of serotonin receptors." The transducin-PDE6
  structure paper is PMID:33007200 (title confirmed by esummary: "Structure of the Visual
  Signaling Complex between Transducin and Phosphodiesterase 6"). The RHO -> GNAT1 edge is
  TAS to PMID:31097585, an opsin 3 / melanocyte paper. I cannot edit the GO-CAM review;
  reported to the coordinator.

## 7. Papers fetched and read for this review

Abstract-only unless marked full text. Species is stated for each because almost none of
the biochemistry is on the human protein.

Activation, effector and deactivation (bovine)
- PMID:31300275 (Gao 2019, full text). Cryo-EM of light-activated bovine rhodopsin with
  transducin (native bovine Gbeta1gamma1 and a recombinant GalphaT carrying 18 Galpha-i1
  residues). [PMID:31300275 "activates the G-protein transducin (GT) by catalyzing GDP-GTP
  exchange on its α subunit (GαT)"]. This is the IDA behind bovine G protein activity,
  heterotrimer membership and GO:0141190.
- PMID:33007200 (Gao 2020, full text). Cryo-EM of native bovine PDE6 with GTP-bound
  recombinant GalphaT (GTPase-defective R174C/Q200L, same chimeric backbone).
  [PMID:33007200 "The structure reveals two GαT·GTP subunits engaging the PDE6
  hetero-tetramer at both the PDE6 catalytic core and the PDEγ subunits, driving extensive
  rearrangements to relieve all inhibitory constraints on enzyme catalysis"]. Effector is
  PDE6, via the gamma subunits. Deactivation: [PMID:33007200 "The RGS9 complex involved in
  deactivating GTP-bound GαT is attached to the membrane by the RGS9 anchor protein (R9AP)"].
- PMID:16469737 (Majumdar 2006). Chimeric alpha-T* with R174C or Q200L: [PMID:16469737
  "both the alpha(T)*(R174C) and alpha(T)*(Q200L) mutants exhibited severely compromised
  GTPase activity"] yet [PMID:16469737 "both stimulated effector activity in the absence
  of rhodopsin and Gbetagamma"]. Gln-200 is the residue changed in the human Q200E family.
- PMID:2538446 (Kroll 1989). Source of the bovine IDA rows for GDP binding and for
  "negative regulation of cyclic-nucleotide phosphodiesterase activity". The experiment:
  [PMID:2538446 "the addition of the pure alpha T.GDP species to the trypsin-treated PDE
  (tPDE) results in a significant (90-100%) inhibition of the enzyme activity"]. The same
  abstract records the activating role: [PMID:2538446 "alpha T.GTP gamma S] which elicits
  a marked stimulation of the native enzyme activity"]. So the "negative regulation" row
  is an in vitro effect of the GDP-bound form on protease-activated PDE; the physiological
  relation of GTP-bound transducin to PDE6 is activation. GO has no live positive
  counterpart: GO:0051343 (positive regulation of cyclic-nucleotide phosphodiesterase
  activity) is obsolete in QuickGO; GO:0051344 is still live.
- PMID:8552184 (Lambright 1996). Crystal structure of the transducin heterotrimer
  (bovine; chimeric alpha). [PMID:8552184 "The structure of a heterotrimeric G protein
  reveals the mechanism of the nucleotide-dependent engagement of the alpha and beta gamma
  subunits that regulates their interaction with receptor and effector molecules"].
- PMID:11024022 (Natochin 2000, AGS3; donor of bovine GTP/GDP binding IMP): fetch failed,
  not read.

Lipid anchor and membrane attachment
- PMID:9498812 (Neubert and Hurley 1998, bovine). [PMID:9498812 "The N-terminal glycine
  of transducin alpha subunits is acylated by lauroyl (C12:0), myristoyl (C14:0),
  (cis-delta5)-tetradecaenoyl (C14:1) or (cis,cis-delta5,delta8)-tetradecadienoyl (C14:2)
  fatty acyl groups"]. This is covalent N-acylation of transducin alpha, and it is the only
  source of the `acyl binding` row. GO:0005488 binding is defined in QuickGO as "The
  selective, non-covalent, often stoichiometric, interaction of a molecule with one or more
  specific sites on another molecule", so a covalently attached acyl chain is not acyl
  binding by the modified protein.
- PMID:17881533 (Kerov 2007, mouse transgenic G2A). [PMID:17881533 "In contrast to native
  G alpha(t), which resides in the outer segments of dark-adapted rods, G alpha(t)G2A was
  found predominantly in the inner compartments of the photoreceptor cells"];
  [PMID:17881533 "N-acylation is critical for correct compartmentalization of transducin
  and controls the rate of its deactivation"]. MGI takes GTPase activity IDA, G-beta/gamma
  binding IDA and connecting cilium IDA from the full text, which I could not read.
- PMID:21642972 (Zhang 2011, full text). UNC119 binds the acylated N terminus of transducin
  alpha; pulldowns from bovine retina, a lauroylated bovine N-terminal peptide
  (2-GAGASAEEKH-11, identical in human GNAT1 residues 2-11), mouse Unc119 knockout.
  [PMID:21642972 "UNC119 bound Tα-GTP, inhibiting its GTPase activity, thereby providing a
  stable UNC119-Tα-GTP complex capable of diffusing from the inner segment back to the
  outer segment after light-induced translocation"]. UniProt's "myristoylation at Gly-2"
  for the human protein rests on this peptide work.

Localization and light-driven translocation
- PMID:11931744 (Sokolov 2002, rat). [PMID:11931744 "Up to 90% of transducin translocates
  from rod outer segments to other cellular compartments on the time scale of tens of
  minutes"]; [PMID:11931744 "The reduction in the transducin content of the rod outer
  segments is accompanied by a corresponding reduction in the amplification of the rod
  photoresponse"]. RGD takes outer segment, inner segment, neuronal cell body, response to
  light intensity (IDA) and G protein-coupled opsin signaling (IMP) from this paper.
- PMID:17507570 (Rosenzweig 2007; mouse/other, donor of bovine "response to light
  stimulus" IDA). [PMID:17507570 "In darkness, transducin is sequestered within the
  membrane-enriched outer segments of the rod cell. In light, it disperses throughout the
  entire neuron"]; [PMID:17507570 "When rod transducin is stimulated, its subunits
  dissociate, leave outer segment membranes, and equilibrate throughout the cell"].
- PMID:31696965 (Chaya 2019, mouse). Cul3-Klhl18 and Unc119 modulate rod transducin alpha
  translocation; source of the mouse inner segment IDA.
- PMID:11095744 (Calvert 2000, mouse Gnat1 knockout). [PMID:11095744 "Rod-driven components
  were absent from the electroretinogram, whereas cone-driven components were retained"];
  [PMID:11095744 "These results indicate that most if not all rods use a single transducin
  type in phototransduction"].
- PMID:1614872 (Fong 1992, human gene). [PMID:1614872 "the gene is transcribed by rod
  photoreceptors into two species of mRNA, 1.3 kb and 2.4 kb in size"].

Taste and other non-visual sites
- PMID:7596440 (Ruiz-Avila 1995, rat and bovine material). [PMID:7596440 "rod transducin
  is also present in vertebrate taste cells, where it specifically activates a
  phosphodiesterase isolated from taste tissue"]; [PMID:7596440 "the bitter compound
  denatonium in the presence of taste-cell membranes activates transducin but not Gi"].
  The conclusion is stated as a suggestion: [PMID:7596440 "These results suggest that rod
  transducin transduces bitter taste"]. This is the rat IDA behind the Ensembl bitter-taste
  row; it is about rod transducin itself (not gustducin), in vitro with taste membranes.
- PMID:7878085 (McLaughlin 1994, rat taste tissue cloning). Donor of rat "cGMP catabolic
  process" IDA. The abstract shows cloning and expression only: [PMID:7878085 "alpha i-3,
  alpha 14, alpha s, and alpha t-rod are more highly expressed in taste tissue than in the
  surrounding nonsensory tissue"], and a proposal: [PMID:7878085 "We propose that gustducin
  and transducin regulate phosphodiesterase activity in taste cells"].
- PMID:17495045 (Mace 2007, rat jejunum). Donor of rat "apical plasma membrane" IDA. The
  abstract speaks of "transducin" without saying rod or cone alpha: [PMID:17495045 "T1Rs
  are colocalized with each other and with alpha-gustducin, transducin or phospholipase C
  beta2 to different extents"]. Enterocyte/brush-cell staining, full text not read.
- PMID:10854264 (Kasahara 2000, chicken pineal). [PMID:10854264 "the pineal Gt(1)alpha is
  activated in a light-dependent manner in the presence of GTPgammaS"]. Donor of the AgBase
  ISS rows (response to light stimulus, membrane).

Other
- PMID:11032890 (Bell 2000, bovine ROS; rat retina in vivo). [PMID:11032890 "Several
  tyrosine-phosphorylated proteins, including Src, coimmunoprecipitated with Talpha"];
  site mapped [PMID:11032890 "to Tyr(142) in the helical domain of Talpha"]. Donor of
  "protein kinase binding". The functional consequence is not established:
  [PMID:11032890 "Talpha was also tyrosine-phosphorylated in vivo in rat retina, but this
  phosphorylation was not affected by light"].

## 8. Ontology checks (QuickGO)

- GO:0003925 G protein activity is_a GO:0003924 GTPase activity (ancestor list read).
- GO:0141190 definition names transducin, PDE and CNG-channel closure; it is the specific
  pathway term for this gene.
- GO:0120202 rod photoreceptor disc membrane: the discs are separated from the ciliary and
  plasma membrane.
