# MGAT1 (human, P26572) — gene review notes

## Identity and core enzymology

- HGNC:7044, MGAT1, chromosome 5. Synonyms GGNT1, GLCT1, GLYT1, MGAT; protein name
  "Alpha-1,3-mannosyl-glycoprotein 2-beta-N-acetylglucosaminyltransferase"; common
  enzyme names GnT-I / GlcNAc-TI. EC 2.4.1.101. CAZy family GT13. 445 aa.
- Type II single-pass membrane protein (UniProt P26572): cytoplasmic tail 1-6,
  TM 7-29, lumenal 30-445; active site His289 (proton acceptor); Mn2+-binding
  residue 211; substrate-binding residues 115/142/188/210/320; disulfides 113-143,
  237-303 (by similarity to rabbit P27115).
- Core reaction (UniProt CATALYTIC ACTIVITY, RHEA:11456): transfers GlcNAc from
  UDP-GlcNAc to the alpha-1,3-Man arm of Man5GlcNAc2-Asn-[protein], forming
  beta-1,2-GlcNAc. This is the first committed/gatekeeper step converting
  high-mannose (oligomannose) N-glycans into hybrid and complex N-glycans, creating
  the obligate substrate for downstream MAN2A1/MAN2A2 (alpha-mannosidase II) and
  MGAT2/MGAT4/MGAT5 branching. Cofactor Mn2+ (UniProt COFACTOR).
- Originally cloned by complementation of the N-glycosylation defect of the Lec1 CHO
  mutant; the protein is "the medial Golgi transferase that initiates complex
  N-linked carbohydrate formation" [PMID:1702225 title; abstract: "a human gene
  encoding N-acetylglucosaminyltransferase I (GlcNAc-TI; EC 2.4.1.101) by
  complementation of the glycosylation defect in the Lec1 Chinese hamster ovary (CHO)
  cell mutant ... full-length cDNA encoding human GlcNAc-TI activity. The overall
  features of the cDNA and deduced protein sequence (445 amino acids) are typical of
  other Golgi transferases that are type II transmembrane proteins."].
- Catalytic activity / function re-confirmed in a cell-free glycoenzyme pipeline
  (water-soluble SIMPLEx GTs remodel glycans) [PMID:36280670]; UniProt cites this as
  ECO:0000269 evidence for FUNCTION + CATALYTIC ACTIVITY. The paper's abstract is
  about a general 98-GT pipeline (human-origin GTs, complex-type N-glycan remodeling
  on trastuzumab); MGAT1/GnT-I is one of the enzymes used. Treat the EXP MF
  annotation as curator-verified (full text available in cache) — do NOT REMOVE
  because the abstract is generic.

## Subcellular localization (experimental)

- Golgi apparatus membrane; medial Golgi. BiFC in live cells shows GnTI (MGAT1) forms
  Golgi-localized homodimers and a functionally relevant medial-Golgi heterodimer
  with GnTII (MGAT2); signal "detected only in the Golgi membranes of live cells"
  [PMID:20378551 "the BiFC signal with GnTI was detected only in the Golgi membranes
  of live cells"; "the medial Golgi enzymes GnTI and GnTII also assemble into
  Golgi-localized homodimers in live cells"]. UniProt SUBCELLULAR LOCATION cites
  PMID:20378551 for Golgi apparatus membrane.
- UniProt also lists "Cytoplasm, perinuclear region" from PMID:30983867, where
  MGAT1 co-localizes with BRI3 isoform 1 at the perinuclear region. The perinuclear
  signal is consistent with the (peri-Golgi) location of a Golgi enzyme; the
  IEA "perinuclear region of cytoplasm" (GO:0048471) annotation derives from this.

## Protein interactions

- Interacts with MGAT4D (GnT1IP) — UniProt SUBUNIT (by similarity to P27808); GnT1IP-L
  inhibits MGAT1 in the Golgi via its lumenal domain (regulatory; spermatogenic
  context) [Falcon: huang2015 = PMID:26371591 eLife, NOT in cache → notes only].
- Interacts with BRI3 (ITM2C/BRI3 isoforms 1>2) by Y2H + co-IP + colocalization
  [PMID:30983867 "MGAT1 ... were confirmed as interaction partners by using
  cotransformation in yeast cells and coimmunoprecipitation from mammalian cell
  lines"; "intense colocalization of BRI3 with MGAT1, especially in the perinuclear
  area"]. This is the basis of the IPI GO:0005515 "protein binding". BRI3 is a poorly
  characterized lysosomal/TNF-pathway protein; the interaction has no established
  link to MGAT1 catalytic function → generic protein binding, over-annotation.
- Forms homo- and hetero-dimers/multi-enzyme assemblies with other Golgi
  N-glycosyltransferases (MGAT2, GalT, SiaT) and, per Falcon, with MAN2A2 and
  SLC35A3 (UDP-GlcNAc transporter) [PMID:20378551 for GnTI-GnTII; Falcon:
  khoderagha2019 = PMID:30659329 CMLS, NOT in cache → notes only].

## Physiology / biological process (mostly via substrate glycans — non-core)

- Mgat1-null mouse is embryonic lethal (~E9.5-10.5) with neural-tube defects; Lec1
  CHO mutant lacks GnT-I activity (gatekeeper of complex N-glycans). Indispensable
  for complex N-glycan synthesis. [Falcon synthesis; classic Stanley/Ioffe-Stanley
  and Metzler results — not in our cache, recorded here as background.]
- Falcon-cited downstream/pleiotropic roles (T-cell development/beta-selection/Treg,
  dendritic-cell CD8 activation, zebrafish development, TNBC CD73 immune evasion,
  AD glycomics, lactate/Treg "mitochondrial MGAT1"): these are consequences of
  altered N-glycan structures on substrate glycoproteins, not direct MGAT1 molecular
  functions. None are in our publications cache (no fetchable cached PMID), so they
  are recorded as notes/background only and not used as supporting_text. They do not
  warrant direct GO process annotations for MGAT1.

## Reactome

- R-HSA-964768 "Addition of GlcNAc to the glycan on the A arm": "This is the first
  committed step in the synthesis of complex and hybrid N-glycans" — TAS basis for
  the MGAT1 MF and the ERGIC membrane location.
- R-HSA-9683648/9694656 "Spike trimer glycoside chains are extended": "The
  N-acetylglucosaminyltransferase called GlcNAc-TI (MGAT1) adds a GlcNAc residue in
  the core of some high-mannose chains" — viral (SARS-CoV) spike N-glycan maturation;
  basis of TAS acetylglucosaminyltransferase activity and "viral protein processing".
- R-HSA-9683686/9694548 "Maturation of spike protein": viral spike N-glycosylation
  pathway; basis of TAS GO:0019082 "viral protein processing". This is the same
  housekeeping N-glycan-maturation activity applied to a viral glycoprotein substrate
  — keep as non-core (it is not a dedicated antiviral/viral function of MGAT1).

## Annotation strategy summary

- Core MF: GO:0003827 (specific GlcNAc-TI activity) — collapse the generic
  GO:0008375 "acetylglucosaminyltransferase activity" onto this. Mn2+ binding
  (GO:0030145) is a genuine experimentally supported cofactor MF.
- Core BP: GO:0006487 protein N-linked glycosylation (specifically the
  oligomannose->hybrid/complex committed step). GO:0009101 glycoprotein biosynthetic
  process is an over-general InterPro parent.
- Core CC: GO:0000139 Golgi membrane (IDA). GO:0005794 Golgi apparatus (IBA) accept.
  GO:0033116 ERGIC membrane (Reactome TAS) keep-as-non-core. GO:0048471 perinuclear
  region keep-as-non-core (peri-Golgi). Exosome/extracellular vesicle/membrane HDA
  proteomics hits = over-annotation (secretory-pathway carryover, not function).
- Generic GO:0005515 protein binding (BRI3 Y2H) → over-annotated per guidelines.
- viral protein processing (GO:0019082) Reactome TAS → keep-as-non-core (substrate
  application of the housekeeping activity).

## Falcon integration (2026-06-21)

Falcon report read in full; it is well-organized and its core-vs-pleiotropic framing
matches GO best practice. Used / rejected:

- USED (concordant, anchored to verifiable sources): GT13 / type II Golgi membrane
  enzyme; UDP-GlcNAc donor + Mn2+ cofactor; gatekeeper first committed step
  (Man5GlcNAc2 alpha-1,3 arm); medial-Golgi multi-enzyme assemblies; explicit
  "core enzymatic function vs indirect substrate-mediated phenotype" annotation
  principle; caution against cytosol/nucleus/mitochondrion CC and against
  immune-evasion/apoptosis/inflammation BP. These are independently supported by
  UniProt P26572, PMID:1702225, PMID:20378551, and Reactome R-HSA-964768.
- REJECTED / DOWNGRADED TO NOTES (no fetchable cached PMID; could not verify
  verbatim, and CLAUDE.md forbids citing them as supporting_text):
  - huang2015 GnT1IP-L inhibition (cited as eLife 2015; resolves to PMID:26371591,
    not in cache) — recorded as background for the MGAT4D interaction only.
  - khoderagha2019 multi-enzyme/SLC35A3 assemblies (CMLS; PMID:30659329, not in
    cache) — background only.
  - vicente2023 / blomberg2025 / chi2025 / zhou2024 / tang2023 / hall2023 immune,
    cancer, AD, "mitochondrial MGAT1" claims — all downstream/substrate-mediated or
    single-context emerging claims, none in cache; not used for annotation. The
    Falcon report itself flags these as annotation-risk, which I agree with.
  - Several Falcon "page" citation tokens (e.g. liu2026 bioRxiv preprint) are
    preprints/low-citation and not load-bearing here.
- DATING NOTE: Falcon assigns PMID:1702225 to 1990 (correct PNAS year); the cached
  record header says 1990. UniProt RN[1] lists the PNAS 87:9948-9952(1990). Fine.
- The Falcon report is added to references as a file: reference with relevance MEDIUM,
  used only to anchor the core-vs-pleiotropic synthesis; all substantive claims are
  cited to primary papers / UniProt / Reactome.
