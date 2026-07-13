# NDUFS3 (O75489) review notes

## Identity
- NADH:ubiquinone oxidoreductase core subunit S3 / "30 kDa" subunit / Complex I-30kD (CI-30kD).
- 264 aa precursor; mitochondrial transit peptide 1-36; mature chain 37-264.
- Belongs to the complex I 30 kDa subunit family (UniProt SIMILARITY). Despite the
  historical name "iron-sulfur protein 3 (IP fraction)", NDUFS3 itself does **not** bind
  an Fe-S cluster; it was co-purified in the biochemically-defined IP subfraction of
  complex I. It is a **core, non-cofactor structural subunit of the Q-module** of the
  peripheral (hydrophilic) arm, adjacent to the Fe-S-carrying NDUFS2, near the ubiquinone
  reduction site.

## Verified biology
- **Core subunit of respiratory Complex I (NADH:ubiquinone oxidoreductase).** UniProt:
  "Core subunit of the mitochondrial membrane respiratory chain NADH dehydrogenase
  (Complex I) which catalyzes electron transfer from NADH through the respiratory chain,
  using ubiquinone as an electron acceptor" [UniProt O75489 FUNCTION].
  One of the 7 conserved nuclear-encoded core subunits (14 core subunits total: 7 mtDNA +
  7 nuclear). [PMID:14729820 abstract: "seventh and last subunit of complex I core"].
- **Essential for catalytic activity AND assembly of Complex I** [UniProt: "Essential for
  the catalytic activity and assembly of complex I"; PMID:14729820, PMID:30140060].
- **Disease:** biallelic NDUFS3 variants cause Mitochondrial complex I deficiency nuclear
  type 8 (MC1DN8, MIM:618230), presenting as Leigh syndrome / optic atrophy. Patient
  variants (T145I, R199W, R140W) decrease enzyme activity and impair complex I assembly
  [PMID:14729820; PMID:30140060 "decreased amount of NDUFS3 and complex I assembly"].

## Localization / topology
- Mitochondrial inner membrane, peripheral membrane protein, matrix side [UniProt
  SUBCELLULAR LOCATION; PMID:18826940 topology; PMID:12611891, PMID:17209039].
- Part of the peripheral (matrix-facing) arm; PMID:18826940 shows NDUFS3 present in a
  matrix-soluble subassembly. Mitochondrial matrix (Reactome TAS) is compatible with the
  matrix-side peripheral-arm location but the primary/curated anatomical location is the
  inner membrane (GO:0005743).

## Assembly / entry point
- NDUFS3 is an early nucleation point of the Q-module: tracing tagged NDUFS3 revealed
  stepwise CI assembly and the entry point of mtDNA-encoded subunits [PMID:17209039].
- Interacts with assembly factor NDUFAF3 [PMID:19463981], and is found in subcomplexes
  with NDUFS2, MT-ND1, NDUFA13 [PMID:17209039, PMID:18826940].
- GO:0032981 mitochondrial respiratory chain complex I assembly (IMP, PMID:30140060) is
  well supported.

## Molecular function annotations
- GOA carries both **GO:0008137 NADH dehydrogenase (ubiquinone) activity** as
  `contributes_to` (IMP, PMID:30140060) — the biologically correct framing for a core
  structural subunit contributing to the complex-level catalytic activity — and as
  `enables` (IMP PMID:14729820; NAS PMID:9647766/9878551; IEA). The complex-level
  holoenzyme catalyzes RHEA:29091 / EC 7.1.1.2. NDUFS3 has no independent catalytic
  activity of its own; the `contributes_to GO:0008137` is the appropriate MF core.
- GO:0003954 NADH dehydrogenase activity (IMP) — parent/looser MF; kept as non-core.
- GO:0016651 oxidoreductase activity acting on NAD(P)H (IEA) — broad parent, accept.
- GO:0009055 electron transfer activity (NAS, PMID:9647766) — NDUFS3 does not itself
  carry a redox cofactor; the electron-transfer chemistry is carried by the Fe-S subunits
  and flavin. Over-annotation for this subunit → MARK_AS_OVER_ANNOTATED.

## protein binding (GO:0005515) IPIs
- Many bare `protein binding` IPIs from high-throughput interactome mapping
  (15250827, 19688755, 21310150, 24344204, 27499296, 28514442, 32296183, 32814053,
  33961781, 19822128) plus curated ones (31536960 RAB5IF; 19463981 NDUFAF3). Per curation
  policy bare `protein binding` is uninformative → MARK_AS_OVER_ANNOTATED (not REMOVE).
  Biologically meaningful partners (NDUFS2, NDUFA5, NDUFA8, NDUFAF3, RAB5IF) are captured
  by the complex-membership and assembly annotations.

## Other BP
- GO:0006120 mitochondrial electron transport, NADH to ubiquinone — core BP (IMP
  PMID:14729820, PMID:30140060). ACCEPT.
- GO:1902600 proton transmembrane transport (IEA, GO_REF:0000108 from GO:0008137) —
  complex I pumps protons; valid at complex level, keep as non-core.
- GO:0009060 aerobic respiration; GO:0042776 proton motive force-driven mito ATP synthesis
  (NAS, ComplexPortal PMID:30030361) — complex-level physiological roles; non-core.
- GO:0072593 reactive oxygen species metabolic process (IMP, PMID:16826196) — siRNA
  knockdown of NDUFS3 reduced ROS production in IFN-beta/RA cancer-death model; downstream
  physiological consequence, keep as non-core (not a core molecular role).
- GO:0021762 substantia nigra development (HEP, PMID:22926577) — from a differential
  proteomics survey of substantia nigra in neurodegeneration; expression correlation only,
  no developmental-function evidence → MARK_AS_OVER_ANNOTATED.

## Core functions
- MF: contributes_to GO:0008137 NADH dehydrogenase (ubiquinone) activity (core structural
  subunit contributing to complex-level catalysis).
- BP: directly_involved_in GO:0006120 mitochondrial electron transport, NADH to ubiquinone;
  and GO:0032981 complex I assembly.
- CC: located_in GO:0005743 mitochondrial inner membrane; in_complex GO:0045271
  respiratory chain complex I.
</content>
</invoke>
