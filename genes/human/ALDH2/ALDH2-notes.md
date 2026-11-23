# ALDH2 (P05091) — curation notes

Reviewer: Claude (AI-assisted). Date: 2026-11-04.

## Provenance of this review

No `ALDH2-deep-research-*.md` file exists for this gene and deep-research providers were
not available in this session (no API keys), so **no deep research file was generated** and
none is cited. The review was built from:

- `ALDH2-uniprot.txt` (UniProtKB P05091, reviewed entry) — CC FUNCTION, CATALYTIC ACTIVITY,
  BIOPHYSICOCHEMICAL PROPERTIES, PATHWAY, SUBUNIT, SUBCELLULAR LOCATION, POLYMORPHISM,
  DISEASE and FT blocks.
- The cached publications for every PMID in `ALDH2-goa.tsv`
  (`publications/PMID_*.md`): 12693930, 16440063, 16956664, 19056867, 19506075, 20062057,
  22339434, 25413692, 27521998, 34800366, 39075523, 4015840, 4065146.
- Three further PMIDs cited by UniProt that bear directly on contested rows, fetched with
  `just fetch-pmids-from-file`: 33355142 (AMeD syndrome / formaldehyde), 22988236 (GTN
  denitration crystallography), 10631996 (ALDH2 3D structure, abstract only — PMC blocks
  full text).
- The cached Reactome entries for the six TAS rows (`reactome/R-HSA-71723.md`,
  `R-HSA-380608.md`, `R-HSA-9838035.md`, `R-HSA-9838081.md`, `R-HSA-9838093.md`,
  `R-HSA-9838289.md`).
- `interpro/panther/PTHR11699/` (family review, `PTHR11699-paint.tsv`) for the three IBA
  rows, and `just paint-losses human ALDH2` (no IRD/IKR on this lineage).

Literature search note: the GOA PMID set plus UniProt's own citation list was treated as
the search frontier; no additional literature search tool was available offline, so claims
not traceable to one of the sources above were not asserted.

## Biology

ALDH2 is the mitochondrial, NAD+-dependent, low-Km aldehyde dehydrogenase. It is a
homotetramer of 517-residue precursors whose N-terminal 17 residues are a cleaved
mitochondrial transit peptide [file:human/ALDH2/ALDH2-uniprot.txt, "TRANSIT         1..17"],
giving a soluble matrix enzyme. Catalysis runs through the canonical ALDH dyad: Cys319
(precursor numbering; Cys302 in the mature-protein numbering used in the enzymology
literature) attacks the aldehyde carbonyl, hydride goes to NAD+, and Glu285 (Glu268 mature)
activates the hydrolytic water [PMID:19506075, "Although the C302S mutation led to >90% loss
of all enzyme activities, the E268Q mutant exhibited virtually unaffected rates of GTN
denitration despite low dehydrogenase and esterase activities."].

Substrate scope and affinity (UniProt kinetics block): acetaldehyde KM 0.02 µM, propanal
0.5 µM, 4-HNE 0.9 µM (pH 7.4), acrolein 1.1 µM, malondialdehyde 26 µM, nitroglycerin
8.7 µM. ALDH2 is the highest-efficiency human isoform for the lipid-peroxidation aldehydes
acrolein, 4-HNE and malondialdehyde and also the most easily inactivated by them
[PMID:22339434]. It oxidises DOPAL (the MAO product of dopamine) to DOPAC, a step inhibited
by 4-HNE [PMID:16956664]. It has weak but physiologically consequential formaldehyde
activity: ALDH2 E504K plus biallelic ADH5 loss causes AMeD syndrome, and wild-type ALDH2
cDNA rescues formaldehyde-induced DNA damage in patient cells [PMID:33355142].

Pharmacology: ALDH2 denitrates nitroglycerin to 1,2-glyceryl dinitrate and nitrite and also
reduces it to NO, via a thionitrate adduct on the catalytic cysteine
[PMID:22988236; PMID:19506075]. The E504K (ALDH2*2) variant, which nearly abolishes activity,
both causes acetaldehyde accumulation/flushing and abolishes clinical nitroglycerin efficacy
[PMID:16440063]. Two further loss-of-function variants (R101G, R114W) were characterised in
2024 [PMID:39075523].

## Judgement calls recorded in the review

- **Substrate-specific IEA rows from by-similarity Rhea/EC mappings.** Retinal
  (GO:0001758), succinate-semialdehyde (GO:0004777) and 4-aminobutanal (GO:0019145) rows
  trace to UniProt CATALYTIC ACTIVITY blocks whose only evidence is `ECO:0000250` (by
  similarity to rodent ALDH2 P20000 / mouse P47738), and human has dedicated enzymes for
  each reaction (the ALDH1A family, ALDH5A1, ALDH9A1). Marked over-annotated, not removed:
  a broad-specificity ALDH plausibly turns these substrates over in vitro, but the claim is
  not grounded on this protein.
- **Esterase activity (GO:0106435).** Real and measured on p-nitrophenyl acetate, but
  UniProt itself says the physiological relevance is unclear, so this is in vitro activity
  of unknown relevance → `MARK_AS_OVER_ANNOTATED`, per the promiscuous-activity tiers.
- **Nitroglycerin reductase has no GO MF term.** The only specific term,
  `GO:0018547 nitroglycerin reductase activity`, was obsoleted ("there was no evidence that
  this specific reaction exists"), although UniProt records the reaction with
  `ECO:0000269` evidence (RHEA:80159, RHEA:80155). The GOA rows therefore sit on the EC
  1.7.1.- parent `GO:0046857`, which is accepted here; the gap is raised as a
  `suggested_questions` entry rather than as a new term, since GO's obsoletion was a
  deliberate decision.
- **Exosome (GO:0070062).** A urinary-exosome proteomics hit for a mitochondrial matrix
  enzyme; kept but flagged as over-annotated.
- **Mitochondrion/mitochondrial matrix rows.** Under the root-organelle policy, the
  mitochondrion rows are kept and the matrix sub-compartment is added rather than
  substituted; the matrix claim is independently supported (cleaved transit peptide, a
  soluble tetramer, Reactome R-HSA-71723, and the Ensembl-Compara matrix IEA), so no
  `NEW` IC row was needed. The four CLPXP/LONP1 TAS rows are substrate-role rows in
  Reactome: their location claim (matrix) is right, which is all the GO row asserts.
