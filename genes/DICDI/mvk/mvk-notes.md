# mvk (Dictyostelium discoideum) review notes

## 2026-11-18 manual review

UniProt Q86AG7 (KIME_DICDI), dictyBase DDB_G0272018, 390 residues, PANTHER PTHR43290:SF2. PE 1
only because peptides were seen by mass spectrometry (unpublished UniProt submission); there is no
published enzymology of the Dictyostelium protein. No deep-research provider keys are configured
here, so no provider file was generated.

### Literature searches (Europe PMC and web, 2026-11-18)

- `Dictyostelium AND ("mevalonate kinase" OR "diphosphomevalonate decarboxylase" OR "mevalonate
  diphosphate decarboxylase" OR "mevalonate pyrophosphate decarboxylase")`: no paper characterises
  the Dictyostelium enzyme. The relevant hit is Nuttall et al. 2012 on peroxisomal FDP synthase
  (PMID:22849378).
- `Dictyostelium AND ("DDB_G0272018" OR "DDB_G0278607")`: 0 hits.
- `Dictyostelium AND (sterol OR isoprenoid) AND biosynthesis AND (cycloartenol OR mevalonate)` and
  `Dictyostelium AND cycloartenol`: sterol chemistry (Nes et al. 1990, PMID:11607106) and the
  cycloartenol synthase cDNA (Godzina et al. 2000, PMID:10783001); Europe PMC also indexes two
  University of Sheffield PhD theses on peroxisomes and sterol synthesis in Dictyostelium (2014,
  open; 2017, restricted).
- Web search for the 2014 thesis title found the open PDF on White Rose eTheses (Alkuwayti 2014,
  supervisor E. H. Hettema), cited here as
  `url:https://etheses.whiterose.ac.uk/id/eprint/7085/2/full%20thesis%20final%20Em.pdf`.

### Evidence

- Localization (thesis, unrefereed): N- and C-terminal GFP fusions of DdMVK expressed in amoebae are
  cytosolic, despite a putative N-terminal PTS2 (KIILFGEHA) [thesis "Fluorescence in amoebae
  transformed with either of the two constructs was in the cytosol"; "Hence, it appears that the
  putative PTS2 does not direct DdMVK to the peroxisomes."]. In the same work PMK (via a C-terminal
  PTS1, -PKL) and FDP synthase are peroxisomal, HMG-CoA reductase is in the ER, and MVK, MVD,
  HMGS isozyme A and IDI are cytosolic. FDP synthase was published as peroxisomal (PTS2-dependent)
  [PMID:22849378 "A fusion protein between FDPS and GFP (green fluorescent protein) was found, in
  D. discoideum, to localize to peroxisomes"].
- These are overexpressed fusions without endogenous-protein confirmation, but two fusion
  orientations agree, and cytosolic MVK matches human MVK, whose cytosolic location was shown for
  the endogenous protein [PMID:14730012 "We exclusively found a cytosolic localisation of both
  endogenous human MK"].
- Sterols: Dictyostelium makes dictyosterol by way of cycloartenol, a plant-like route [PMID:11607106
  "the stereochemical outcome of squalene oxide cyclization leads to the production of cycloartenol
  rather than lanosterol"]; [PMID:10783001 "Presented here is the first cycloartenol synthase gene
  identified from a protist, the cellular slime mold Dictyostelium discoideum."].
- Function assignment is by orthology to human and rat MVK (UniProt FUNCTION, CATALYTIC ACTIVITY,
  COFACTOR and binding sites are all ECO:0000250), NCBIfam TIGR00549 and PANTHER SF2.

### PANTHER / PAINT

- Leaf PTN000825295, ancestors PTN008680402 (root) > PTN000048555 > PTN002457434 > PTN000048556 >
  PTN000825261 > PTN000825294. PTN000825261 also holds PTN000048557 (fungi and animals), so the
  Dictyostelium enzyme sits in the eukaryotic mevalonate kinase clade.
- PTN000048555 carries the IBDs for GO:0004496, GO:0019287 and GO:0005829. The IRD PTN002214956
  (GO:0004496, GO:0019287; taxon Eukaryota) is the plant glucuronokinase branch (PTHR43290:SF1,
  44 leaves), not on this lineage. `just paint-losses DICDI mvk` reports no loss.
- The sterol end-product IBDs are lineage-specific: cholesterol at PTN000825262 (animals) and
  ergosterol at PTN000825284 (fungi). Dictyostelium mvk receives neither, which is correct, since it
  makes neither sterol. No sterol process row is proposed here; the Dicty mvd review modifies its
  UniPathway cholesterol row to sterol biosynthesis.

### Decisions

- Accept all four GO:0004496 rows, both GO:0019287 rows, cytosol IBA and GO:0008299.
- ATP binding (IEA, ISS) and magnesium ion binding (ISS): KEEP_AS_NON_CORE (substrate and cofactor
  binding inherent to the kinase reaction).
- Cytoplasm (IEA): TOO_GENERAL. Cytoplasm includes peroxisomes, which is exactly the alternative in
  question for this pathway in Dictyostelium; cytosol is accepted.
- Phosphorylation (IC, dictyBase): KEEP_AS_NON_CORE. True (the enzyme phosphorylates mevalonate),
  but generic; no mevalonate-specific phosphorylation process term exists.
- Knowledge gap: how cytosolic MVK and MVD connect to peroxisomal PMK and FDPS.
