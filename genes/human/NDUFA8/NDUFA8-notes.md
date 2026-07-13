# NDUFA8 (P51970) review notes

Human gene: **NDUFA8** (HGNC:7692), a.k.a. Complex I-19kD / CI-PGIV / NADH-ubiquinone
oxidoreductase 19 kDa subunit. UniProt P51970, 172 aa (mature 2-172; initiator Met removed).

## Core biology (from UniProt P51970)

- **Accessory (supernumerary) subunit** of mitochondrial respiratory Complex I
  (NADH:ubiquinone oxidoreductase), **not involved in catalysis**.
  [file:human/NDUFA8/NDUFA8-uniprot.txt "Accessory subunit of the mitochondrial membrane respiratory"]
  [file:human/NDUFA8/NDUFA8-uniprot.txt "that is believed not to be" / "involved in catalysis"]
- Complex I is composed of 45 different subunits; the 14 conserved core subunits carry
  out catalysis (electron transfer NADH -> ubiquinone, coupled to proton pumping); the
  ~31 accessory subunits (including NDUFA8) are structural/assembly/stability roles.
  [file:human/NDUFA8/NDUFA8-uniprot.txt "Complex I is composed of 45 different subunits"]
- **Twin CX9C protein**: contains four C-X9-C motifs forming a helix-coil-helix (CHCH)
  fold with two pairs of intramolecular disulfide bonds (36-66, 46-56, 78-110, 88-100).
  [file:human/NDUFA8/NDUFA8-uniprot.txt "Contains four C-X9-C motifs"]
  This is the hallmark of the MIA40/CHCHD4 disulfide-relay import substrate class.
- **Localization**: mitochondrial inner membrane (peripheral membrane protein), facing
  the **intermembrane space (IMS)**. NDUFB7 and NDUFA8 sit at the IMS surface of Complex I.
  [file:human/NDUFA8/NDUFA8-uniprot.txt "Mitochondrion inner membrane" / "Mitochondrion intermembrane space"]
  [PMID:21310150 "NDUFB7 and NDUFA8 are located at the intermembrane surface of complex I"]
  [PMID:21310150 "the inter-membrane space localization of three Cx(9)C-containing subunits in human: NDUFS5, NDUFB7 and NDUFA8"]
  [PMID:21310150 "We propose these subunits stabilize the membrane domain of complex I"]

## Key references (cached publications)

- **PMID:9860297** (Triepels 1998, Hum Genet) — cDNA cloning of NDUFA8; 172 aa, ~20.1 kDa;
  maps to chr 9; highest mRNA in heart/skeletal muscle; conserved cysteine motif; bovine
  ortholog = PGIV. Abstract-only in cache. [PMID:9860297 "Both human and bovine NDUFA8 contain a conserved cysteine motif"]
- **PMID:9878551** (Loeffen 1998, BBRC) — cDNAs of 8 nuclear-encoded Complex I subunits;
  general Complex I function statement. Abstract-only.
- **PMID:12611891** (Murray 2003, JBC) — immunopurification + MS identification of human
  Complex I subunit composition (NDUFA8 among 42 polypeptides). Basis for part_of CI (IDA).
- **PMID:21310150** (Szklarczyk 2011, FEBS Lett) — establishes IMS-surface localization of
  NDUFB7 and NDUFA8; probable intramolecular disulfide bonds; proposes membrane-arm
  stabilization role. Abstract-only but abstract itself supports the localization claims.
- **PMID:23676665** (Fischer 2013, Mol Biol Cell) — MIA40/ALR oxidative-folding import
  pathway in mammalian IMS (CX9C substrates). Full text available; NDUFA8 disulfide bonds
  attributed here (ECO:0000305). Supports mitochondrion localization.
- **PMID:27626371** (Stroud 2016, Nature) — CRISPR knockout of each Complex I accessory
  subunit; accessory subunits integral for assembly and function; loss of a subunit
  destabilizes its structural module. Basis for FUNCTION and part_of CI. Abstract-only.
- **PMID:28844695** (Guo 2017, Cell) — cryo-EM megacomplex I2III2IV2; assigns individual
  CI subunits. Basis for ComplexPortal CI membership / inner-membrane localization.
- **PMID:30030361** (Signes & Fernandez-Vizarra 2018, Essays Biochem) — review of OXPHOS
  complex/supercomplex assembly. ComplexPortal NAS source for aerobic respiration and
  proton-motive-force ATP synthesis (complex/pathway-level, not NDUFA8's own MF).
- **PMID:34800366** (Morgenstern 2021, Cell Rep) — high-confidence human mitochondrial
  proteome (HTP); NDUFA8 among mitochondrial proteins. Basis for mitochondrion (HTP).

## Interaction annotations (bare protein binding, GO:0005515 IPI)

- **PMID:21310150** with UniProtKB:O75489 (NDUFS3) — IntAct; NDUFA8-NDUFS3 co-purify as
  Complex I neighbors. Consistent with UniProt INTERACTION (P51970;O75489 NDUFS3 NbExp=5).
- **PMID:27499296** (Floyd 2016, Mol Cell) with UniProtKB:O75489 (NDUFS3) — mitochondrial
  AE-MS interaction map; NDUFA8-NDUFS3 in the CI interactome (supplementary data; abstract
  does not name NDUFA8 but the study is a mitochondrial interactome and IntAct extracted
  the pair). Bare protein binding, uninformative -> MARK_AS_OVER_ANNOTATED.
- **PMID:32814053** (Haenig 2020, Cell Rep) with UniProtKB:G5E9A7 (DMWD) and Q7Z699
  (SPRED1) — neurodegenerative-disease Y2H interactome; NDUFA8-DMWD and NDUFA8-SPRED1 in
  the UniProt INTERACTION block. These are large-scale Y2H hits, not functional MFs.
  Bare protein binding -> MARK_AS_OVER_ANNOTATED.

## Mis-citation flag

- **PMID:23209302** ("KIF14 negatively regulates Rap1a-Radil signaling during breast
  cancer progression"; Ahmed 2012, J Cell Biol) is the reference behind the MGI
  `protein-containing complex binding` (GO:0044877) IDA. **This paper is about KIF14/Radil/
  Rap1a breast-cancer signaling and does not concern NDUFA8 or Complex I at all** (full
  text read; no mention of NDUFA8, NDUFS3, or mitochondrial Complex I). This looks like a
  wrong-paper citation. Per policy, an experimental (IDA) annotation is not removed:
  MARK_AS_OVER_ANNOTATED, with a WRONG_IDENTIFIER note in reference_review. The concept
  "NDUFA8 is part of a protein complex" is nonetheless biologically true (it is a Complex I
  subunit), but GO:0044877 is redundant with the specific part_of GO:0045271 membership.

## Disease

- **MC1DN37** (mitochondrial complex I deficiency, nuclear type 37; MIM:619272), autosomal
  recessive. Biallelic NDUFA8 variants: R47C (PMID:32385911) and R98L (PMID:33153867)
  reduce CI activity / CI assembly (variant papers NOT in cache; from UniProt DISEASE/VARIANT
  FT). Confirms NDUFA8 is required for a functional Complex I.

## Curation summary / core function

- Honest molecular function = **GO:0005198 structural molecule activity** (non-catalytic
  structural subunit), **contributes_to** the complex-level **GO:0008137 NADH dehydrogenase
  (ubiquinone) activity**.
- part_of **GO:0045271 respiratory chain complex I**; locations mitochondrial inner membrane
  (IMS-facing) GO:0005743 / GO:0005758.
- Core BP: **GO:0006120 mitochondrial electron transport, NADH to ubiquinone** and
  **GO:0032981 mitochondrial respiratory chain complex I assembly** (subunit loss impairs
  assembly, PMID:27626371).
- Direct NADH-dehydrogenase/oxidoreductase MF (GO:0008137 enables) and proton-transport BP
  (GO:1902600, GO:0042776) are complex/pathway-level over-annotations for this non-catalytic
  subunit -> MARK_AS_OVER_ANNOTATED.
