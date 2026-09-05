# ADGRV1 (Q8WXG9) annotation review notes

Gene: ADGRV1 / GPR98 / VLGR1 / MASS1 / USH2C. HGNC:17416. Human, NCBITaxon:9606.
Largest known GPCR / cell surface protein (full-length VLGR1b ~6,307 aa).

## Core biology (wild-type focus)

- Adhesion GPCR (family B / LNB-7TM). Huge ectodomain: 35 Calx-beta (Ca-exchanger beta)
  repeats, EAR/EPTP repeats, pentraxin-like domain; GAIN domain with GPS autoproteolysis
  site cleaving into extracellular alpha subunit + membrane 7TM beta subunit.
  [PMID:11606593 "The longest gene product, VLGR1b, is 6307 amino acids ... a much larger
  ectodomain containing 35 calcium exchanger beta repeats and a pentraxin homology domain."]
  [PMID:14740321 "All LNB 7TM members, including VLGR1, have a G-protein-coupled proteolysis
  site (GPS)"]

- Calx-beta repeats bind calcium in vitro (overlay assays with isolated repeats).
  [PMID:10976914 "Bacterial fusion proteins containing two or four repeats specifically bind
  45Ca in overlay experiments; binding is competed poorly by Mg2+ but competed well by
  neomycin, Al3+, and Gd3+."] -> supports GO:0005509 IDA.

- Cell-surface expression demonstrated by biotinylation of recombinant protein.
  [PMID:10976914 "the recombinant protein is expressed on the surface of transfected
  mammalian cells."] -> GO:0009986 cell surface IDA, GO:0005886 plasma membrane.

## USH2 complex / ankle links (hearing)

- ADGRV1 is the transmembrane core of the USH2 quaternary complex (USH2A + GPR98 + WHRN +
  PDZD7). WHRN & PDZD7 both required for complex; PDZD7 prefers GPR98, WHRN prefers USH2A;
  WHRN-PDZD7 heterodimer bridges USH2A-GPR98. [PMID:25406310 "both WHRN and PDZD7 are
  required for the complex formation with USH2A and GPR98. In this USH2 quaternary complex,
  WHRN prefers to bind to USH2A, whereas PDZD7 prefers to bind to GPR98."]
- Colocalize at ankle-link region of developing hair bundle. [PMID:25406310 "In hair cells,
  proteins encoded by the four genes are colocalized at the ankle link region of the
  mechanosensitive structure, the hair bundle, during development"]
- ADGRV1 ectodomain forms the ankle links themselves (transient in mammalian cochlea).
  -> GO:0002141 ankle link (part_of), GO:0002142 ankle link complex, GO:1990696 USH2 complex,
  GO:0032420 stereocilium, GO:0060171 stereocilium membrane, GO:0060122 stereocilium
  organization, GO:0050910 detection of mechanical stimulus (acts_upstream_of_or_within).

- Whirlin directly associates with VLGR1b (basis of IPI GO:0005515 PMID:16434480). Mediated
  by whirlin PDZ domains binding GPR98 C-terminal PDZ-binding motif -> MODIFY to GO:0030165
  PDZ domain binding. [PMID:16434480 "whirlin directly associates with USH2A isoform b and
  VLGR1b"]
- PDZD7 PDZ2 binds GPR98 PDZ-binding motif (IPI GO:0005515 PMID:20440071) -> MODIFY to
  GO:0030165. [PMID:20440071 "it is mediated by the PDZ2 domain of PDZD7 and the PDZ-binding
  motif of GPR98."]

## Photoreceptor periciliary complex (vision)

- ADGRV1, usherin, whirlin form periciliary membrane complex at apical inner segment around
  connecting cilium. Pdzd7 knockdown reduces Gpr98 at connecting cilium. [PMID:20440071
  "reduced Gpr98 localization in the region of the photoreceptor connecting cilium"]
  -> GO:0001917 photoreceptor inner segment, GO:1990075 periciliary membrane compartment.
- USH2C -> progressive RP = photoreceptor maintenance. [PMID:15671307 "USH2C and USH2A
  manifest photoreceptor disease with rod- and cone-mediated visual losses and thinning of
  the outer nuclear layer."] -> GO:0045494 photoreceptor cell maintenance (ACCEPT), and the
  GO:0048496 "maintenance of animal organ identity" IMP is a contorted mapping -> MODIFY to
  GO:0045494.

## Signaling

- UniProt (by similarity to mouse Q8VHN7): couples to Gai (GNAI1/2/3), Gaq (GNAQ), Gas
  (GNAS), inhibiting adenylate cyclase and cAMP. Cleaved beta subunit constitutively inhibits
  AC more strongly than full-length. -> GO:0004930 GPCR activity (ACCEPT, multiple evidences),
  GO:0001965 G-alpha-subunit binding (ACCEPT), GO:0007186 GPCR signaling pathway (ACCEPT).
- GO:0010855 adenylate cyclase INHIBITOR ACTIVITY is mechanistically wrong: inhibition is
  indirect via Gi, ADGRV1 does not bind AC. -> MODIFY to GO:0007193 (AC-inhibiting GPCR
  signaling pathway). Applies to both IBA and ISS copies.

## Pleiotropic / non-core

- Ca-dependent PKA/PKC activation regulating MAG ubiquitination / myelination (auditory
  pathway) -> GO:0071277 cellular response to calcium (KEEP_AS_NON_CORE), GO:0031647
  regulation of protein stability (KEEP_AS_NON_CORE). UniProt by-similarity.
- Bone metabolism -> GO:0030501 positive regulation of bone mineralization (KEEP_AS_NON_CORE),
  UniProt by-similarity, mouse.
- Seizures: mouse mass1/Frings audiogenic seizures; human MASS1 S2652X in one febrile/afebrile
  seizure family (incomplete penetrance). [PMID:12402266] -> GO:0050877 nervous system process
  IMP (KEEP_AS_NON_CORE).
- Developmental CNS expression (ventricular zone). [PMID:11606593 "Strong expression in the
  ventricular zone, home of neural progenitor cells ... suggests a fundamental role for VLGR1
  in the development of the central nervous system."] -> GO:0007399 nervous system development
  NAS (KEEP_AS_NON_CORE).

## Over-annotations flagged

- GO:0005737 cytoplasm (IBA is_active_in; IEA located_in) -> MARK_AS_OVER_ANNOTATED (plasma
  membrane / stereocilium receptor). The IDA cytoplasm (PMID:16434480) -> UNDECIDED (abstract
  only cache; full-text evidence not verifiable, membrane/ciliary localizations described).
- GO:0098609 cell-cell adhesion (NAS PMID:11606593) -> MARK_AS_OVER_ANNOTATED: based on 2002
  sponge-aggregation-factor sequence-similarity speculation. [PMID:11606593 "Similar repeats
  are found in the extracellular aggregation factor of marine sponges, which mediates
  species-specific cell aggregation."] ADGRV1's real adhesion is intracellular membrane links
  (ankle links between stereocilia of one cell; periciliary membrane links), not cell-cell.
- GO:0050793 regulation of developmental process (ARBA) -> MARK_AS_OVER_ANNOTATED (vague).
- Root/general terms MODIFY to specific: GO:0007154 cell communication -> GO:0007186;
  GO:0032991 complex -> GO:1990696 USH2 complex; GO:0048513 animal organ development ->
  GO:0048839 inner ear development.

## Notes on evidence access

- Full text cached (full_text_available: true): PMID:14740321, PMID:20440071, PMID:23382219,
  PMID:25406310.
- Abstract-only cache: 10976914, 11606593, 12402266, 15203201, 15671307, 16434480, 19056867.
  Did not REMOVE any experimental annotation on abstract-level doubt (per policy); used
  UNDECIDED for the one experimental (IDA) annotation whose specific evidence I could not
  verify (GO:0005737 cytoplasm, PMID:16434480).
- PMID:23382219 (SNX17/27/31 PX-FERM): cached text does not name GPR98/ADGRV1; the GO:0043235
  IDA rests on screen/SI data I cannot inspect -> KEEP_AS_NON_CORE, deferring to curator.
