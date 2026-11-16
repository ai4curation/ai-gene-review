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

(filled in below as each is read)
