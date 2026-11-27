# PRKDC (DNA-PKcs, P78527) curation notes

No deep-research provider was available for this review; these notes were assembled
manually from the UniProt record, the cached publications in `publications/`, Reactome
entries in `reactome/`, and a Europe PMC search. Quotes are verbatim from the cached files.

## Identity and architecture

- 4128-aa PIKK-family Ser/Thr kinase; HEAT-repeat N-terminal solenoid (double ring),
  FAT, PI3K/PI4K catalytic and FATC domains (UniProt P78527; PANTHER PTHR11139:SF68).
- "DNA-PKcs is a serine/threonine protein kinase comprising a single polypeptide chain of
  4,128 amino acids and belonging to the phosphatidylinositol-3-OH kinase (PI(3)K)-related
  protein family" [PMID:20023628].
- Protein kinase, not lipid kinase: "DNA-PK phosphorylates proteins but has no detectable
  activity toward lipids" [PMID:7671312].

## Core: catalytic subunit of DNA-PK in classical NHEJ and V(D)J recombination

- Holoenzyme: "DNA-PKcs, KU70, KU80 and DNA duplex form a 650-kDa heterotetramer with
  1:1:1:1 stoichiometry" and "KU70/80 and DNA coordinately induce conformational changes of
  DNA-PKcs and allosterically stimulate its kinase activity" [PMID:28840859].
- Activated structures 3.2-3.7 A; activation "loosens DNA-end binding" [PMID:33385326].
- Long-range synaptic complex with LigIV/XRCC4/XLF; trans-autophosphorylation drives
  transition to short-range complex [PMID:33854234]; NHEJ supercomplex structures and
  mutational validation [PMID:34352203].
- Kinase activity required for DSB rejoining and V(D)J: kinase-dead constructs "fail to
  complement the DNA DSB or V(D)J recombination defects of DNA-PKcs mutant cells"
  [PMID:10207111].
- T2609 autophosphorylation required: "Ku-dependent phosphorylation of DNA-PKcs at Thr2609
  is required for the repair of DSBs by NHEJ" [PMID:12231622]; PP5 dephosphorylates
  [PMID:14734805].
- Artemis activation in V(D)J hairpin opening: "Upon complex formation, DNA-PKcs
  phosphorylates Artemis, and Artemis acquires endonucleolytic activity on 5' and 3'
  overhangs, as well as hairpins" [PMID:11955432]; Reactome R-HSA-5687183.
- Human disease: RS-SCID (IMD26). L3062R patient: mutation "caused insufficient Artemis
  activation" [PMID:19075392]; compound het patient with SCID plus severe neurological
  phenotype [PMID:23722905].
- DNA-PKcs is not essential in human HCT116 cells but its loss gives "profound
  proliferation and genomic stability deficits" [PMID:18710952] (abstract only).

## Substrates / signalling outputs (non-core, many contexts)

- H2AX S139 (nucleosomal, acetylation-enhanced) [PMID:14627815]; hypertonic gamma-H2AX
  [PMID:16046194].
- LIG4 T650 [PMID:15194694]; RPA2 S4/S8 (G2/M checkpoint delay) [PMID:21731742];
  ASF1A S192 (DNA-PKcs-dependent) [PMID:29478807]; fumarase T236 (in vitro) [PMID:26237645];
  GOLPH3 (Golgi dispersal after damage) [PMID:24485452]; USF-1 (FAS promoter, insulin)
  [PMID:19303849]; NR4A3/NOR1 (SMC proliferation) [PMID:25852083]; PARP1 T594
  [PMID:35460603]; cGAS (T68/S213) [PMID:33273464].
- AKT S473: purified as a membrane-fraction S473 kinase [PMID:15262962]; DNA-PKcs-SIN1
  (mTORC2) association in UVB-induced S473 phosphorylation [PMID:24365180].
  mTORC2 is the predominant S473 kinase in most contexts, so this is context-dependent.

## Innate immunity -- conflicting directions

- Positive: "we identify DNA-dependent protein kinase (DNA-PK) as a DNA sensor that
  activates innate immunity" [PMID:23251783]; HDP-RNP with HEXIM1/NEAT1 needed for
  cGAS-STING-IRF3 [PMID:28712728].
- Negative: "DNA-PK phosphorylates cGAS and suppresses its enzymatic activity"
  [PMID:33273464]; DNA-PK phosphorylates PARP1 which then PARylates cGAS [PMID:35460603].
- Both are curated (activation of innate immune response; negative regulation of
  cGAS/STING). Kept both as non-core; the direction is cell-type/context dependent.

## Ribosome biogenesis (non-core, Ku-dependent)

- "DNA-PK has RNA-dependent, cNHEJ-independent functions during ribosome biogenesis that
  require the kinase activity of DNA-PKcs and its phosphorylation at the T2609 cluster";
  U3 snoRNA activates DNA-PK; nucleolar, co-purifies with SSU processome [PMID:32103174].
  Northern blots show accumulation of 21S and 12S precursors.
- Nucleolar localization also in [PMID:27829214] (immunostaining and fractionation).

## Efferocytosis-induced macrophage proliferation (module context)

- PMID:34784501 (mouse macrophages): AC-derived oligonucleotides from DNase II
  activate "a DNA-PKcs-mTORC2/Rictor pathway that increases Myc"; siRNA evidence;
  direct oligonucleotide binding not shown. This is one context of DNA-PKcs as a
  DNA-end/oligonucleotide-activated kinase upstream of AKT; not used to add GO terms here.

## Decisions summary

- Core MF: DNA-dependent protein kinase activity (GO:0004677) / protein Ser/Thr kinase.
- Core BP: NHEJ (GO:0006303), immunoglobulin V(D)J recombination (GO:0033152).
- Core CC: DNA-PK complex, NHEJ complex, DNA-PK-Lig4 complex, nucleus.
- Generic protein binding rows removed per policy (Ku, Artemis etc. captured by complex
  and kinase terms).
- G1 checkpoint IMP (PMID:21731742) modified to G2 checkpoint: full text says
  "DNA-PK-dependent RPA2 phosphorylation at S4, S8 appeared to function in the G2/M
  checkpoint".
- Alternative NHEJ (TAS) removed: GO definition requires independence from V(D)J
  recombination factors, of which DNA-PKcs is one.
- Mouse ISS/IEA haematopoiesis-related regulation terms (erythrocyte, platelet, HSC
  differentiation, lymphocyte differentiation, translation) judged over-annotations:
  downstream phenotypes of rRNA-processing or V(D)J defects.
- NEW: site of double-strand break (GO:0035861): phospho-T2609 DNA-PKcs colocalizes with
  gamma-H2AX and 53BP1 foci [PMID:12231622].
