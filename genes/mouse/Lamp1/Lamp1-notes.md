# Lamp1 (mouse) review notes

## Session 1 (2026-10-28)

- Fetched P11438 (Lamp1, MGI:96745, GeneID 16783); 124 GOA rows, dominated by
  lysosome/late endosome IDA rows from papers using Lamp1 as a marker (MGI).
- No deep-research API available; manual synthesis in `Lamp1-deep-research-manual.md`.
- PMID:22147702 was flagged as "key" by the batch task, but it only uses an anti-rat
  LAMP-1 antibody as a lysosomal marker in rat hepatoma cells
  [PMID:22147702 "Large vacuoles were stained by the antibody against LAMP-1, a major component of the lysosomal membrane"].
  Cited as LOW relevance background.

### Decisions

- Root organelle `lysosome` rows (IDA/ISO/IEA): ACCEPT per projects/ORGANELLES.md;
  lysosomal membrane is already present as a separate row set (ACCEPT).
- `late endosome`, `endosome`, `vesicle`, `cytolytic granule`, `phagocytic vesicle`,
  `cytoplasm`, `membrane`: correct but general for a type I membrane protein -> MODIFY to the
  membrane sub-term the gene already carries.
- Core MF: ion channel inhibitor activity (TMEM175) in lysosomal lumen acidification
  [PMID:37390818 "LAMP-1 and LAMP-2 directly interact with and inhibit the activity of the lysosomal cation channel TMEM175"].
  This is human data; mouse carries it by ISS/ISO. Lamp1-/- mice have normal lysosomal pH
  [PMID:10212251 "Lysosomal properties, such as enzyme activities, lysosomal pH, osmotic stability, density, shape, and subcellular distribution were not changed in comparison with controls"],
  consistent with LAMP-2 redundancy.
- `lysosomal lumen pH elevation` ISO (GO:0035752): direction inverted relative to the
  TMEM175-inhibition biology; human source row no longer in GOA. MODIFY to lysosomal lumen
  acidification + source defect.
- `proton transmembrane transport` ISO: LAMP1 does not transport protons; it inhibits TMEM175.
  MODIFY to GO:0010155 regulation of proton transport (no negative-regulation term exists).
- `autophagic cell death` ISO from rat (RGD IDA PMID:18690537): rat paper used lamp1 as a
  marker in dying oocytes -> REMOVE + RGD source defect.
- `spermatogenesis` TAS (PMID:18689890): testis-EST evolution paper, no Lamp1 statement; KO
  fertile -> REMOVE.
- `cytosol` IEA (GO_REF:0000108 from Golgi-to-lysosome transport): wrong for a luminal/TM
  protein -> REMOVE.
- Bare protein binding (amelogenin, ABCB9) -> REMOVE per policy.
- `phagocytic vesicle` IMP (PMID:22190682, AgBase): location established by imaging; IMP
  code describes Salmonella/Stx6 perturbations -> WRONG_EVIDENCE_CODE CHECK.
