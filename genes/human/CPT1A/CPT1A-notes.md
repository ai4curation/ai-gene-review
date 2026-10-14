# CPT1A (P50416) review notes

## Deep research status
`just deep-research human CPT1A --provider falcon` did NOT produce a
`CPT1A-deep-research-falcon.md` file within the polling window (the running
`deep-research-client` process on the machine was for CPT2, a concurrent batch job,
not CPT1A). Review therefore grounded in `CPT1A-uniprot.txt` (UniProt P50416,
entry v221) and cached `publications/PMID_*.md`. No `-deep-research-*.md` file was
fabricated (per policy).

## Verified biology (UniProt P50416 + primary literature)
- RecName: **Carnitine O-palmitoyltransferase 1, liver isoform** (Short CPT1-L);
  AltName CPT I, liver isoform; AltName Carnitine palmitoyltransferase 1A;
  AltName Succinyltransferase CPT1A. EC 2.3.1.21.
- Liver isoform of CPT1. Catalyses the committed, rate-limiting step of long-chain
  fatty-acid import for mitochondrial beta-oxidation: transfer of a long-chain acyl
  group from acyl-CoA to L-carnitine, giving long-chain acylcarnitine + CoA
  (RHEA:12661; (R)-carnitine + hexadecanoyl-CoA = O-hexadecanoyl-(R)-carnitine + CoA).
- Location: **mitochondrion outer membrane**, multi-pass membrane protein
  (TOPO_DOM/TRANSMEM: two TM helices 48-73, 103-122; large C-terminal cytoplasmic
  catalytic domain 123-773). Confirmed EXP in PubMed:11350182, PubMed:14517221.
- Key regulatory point of fatty-acid oxidation; allosterically **inhibited by
  malonyl-CoA** (ACTIVITY REGULATION, PubMed:14517221; N-terminal 1-42 conformational
  switch, PubMed:21990363/PDB 2LE3).
- Deficiency: **CPT1A deficiency (CPT1AD, MIM:255120)** — autosomal recessive
  hypoketotic hypoglycemia; many characterised loss-of-function variants
  (D454G, G709E, G710E, etc.).
- Secondary/moonlighting functions (from UniProt + primary papers):
  - **Lysine succinyltransferase** activity (EC 2.3.1.-; succinyl-CoA + protein Lys),
    e.g. on ENO1, independent of the O-palmitoyltransferase activity
    (PubMed:29425493 — NOT cached).
  - **Scaffold/adaptor**: recruits ER-localized ZDHHC4 to palmitoylate MAVS
    (Cys79) at mitochondria, stabilising/activating MAVS and sustaining the
    type-I IFN response / antitumor immunity; catalytically-dead H473A retains this
    scaffolding activity (PubMed:38016475). This underlies the
    protein-macromolecule adaptor activity (GO:0030674) and positive regulation of
    innate immune response (GO:0045089) IDA annotations.

## Annotation review decisions (summary)
- Core MF GO:0004095 carnitine O-palmitoyltransferase activity: ACCEPT (EXP/IDA/IBA;
  multiple: PMID:11350182 IDA, PMID:7892212 IDA/TAS, PMID:14517221 EXP/IMP,
  PMID:16651524 EXP, PMID:9691089 IMP). Core function.
- CC mitochondrial outer membrane (GO:0005741): ACCEPT (EXP PMID:11350182, IMP
  PMID:14517221, plus ISS/IEA/TAS). This is the specific correct compartment.
- CC mitochondrion (GO:0005739) IBA/IDA/HTP/TAS: less specific than outer membrane;
  KEEP_AS_NON_CORE (redundant parent).
- CC membrane (GO:0016020) HDA PMID:19946888 (NK cell membrane proteome): correct
  but very general and off-context; MARK_AS_OVER_ANNOTATED.
- BP fatty acid beta-oxidation (GO:0006635), carnitine shuttle (GO:0006853),
  long-chain fatty acid metabolic process (GO:0001676), carnitine metabolic process
  (GO:0009437): ACCEPT — directly informed by function; these + fatty acid metabolic
  process (GO:0006631, parent, KEEP_AS_NON_CORE) frame the core process.
- MF acyltransferase activity (GO:0016746) IEA InterPro: correct but general parent
  of GO:0004095; MARK_AS_OVER_ANNOTATED / could MODIFY to GO:0004095.
- BP positive regulation of innate immune response (GO:0045089) IDA + MF
  protein-macromolecule adaptor activity (GO:0030674) IDA (PMID:38016475): ACCEPT
  as real but non-core moonlighting scaffold function (MAVS/ZDHHC4). Kept out of
  core_functions location claims (mito outer surface vs ER contact unresolved).
- Ensembl GO_REF:0000107 rat-ortholog IEA physiology terms (response to hypoxia,
  glucose metabolic process, triglyceride metabolic process, response to nutrient,
  response to xenobiotic, response to nutrient levels, eating behavior, response to
  alkaloid, response to ethanol, regulation of insulin secretion, cellular response
  to fatty acid, liver regeneration, response to tetrachloromethane, identical
  protein binding, positive regulation of fatty acid beta-oxidation, regulation of
  fatty acid oxidation): mostly downstream physiology / rat-transferred; kept as
  KEEP_AS_NON_CORE or MARK_AS_OVER_ANNOTATED individually. `identical protein
  binding` is uninformative -> MARK_AS_OVER_ANNOTATED. `positive regulation of fatty
  acid beta-oxidation` (a positive-regulation term for the enzyme itself) is
  arguably a self-referential over-call -> MARK_AS_OVER_ANNOTATED; the plain
  `regulation of fatty acid oxidation` retained NON_CORE (malonyl-CoA is CPT1's
  own regulator, not CPT1 regulating others).
- GO:0006006 glucose metabolic process / GO:0001678 intracellular glucose
  homeostasis (ISS from mouse): indirect physiology, KEEP_AS_NON_CORE.
- GO:0030855 epithelial cell differentiation IEP PMID:21492153 (Caco-2 proteomics,
  CPT1A up on differentiation): correlative only; MARK_AS_OVER_ANNOTATED.

## core_functions
1. MF GO:0004095 carnitine O-palmitoyltransferase activity; directly involved in
   fatty acid beta-oxidation (GO:0006635), carnitine shuttle (GO:0006853),
   long-chain fatty acid metabolic process (GO:0001676); located in mitochondrial
   outer membrane (GO:0005741).
</content>
</invoke>


## 2026-10-12 — source-resolved reassessment

The earlier journal above is retained verbatim. The following assessment supersedes its blanket objections to response annotations, positive self-association, broad membrane detections and the CPT1A immune function. It also supersedes the earlier claim that the 2023 adaptor mechanism was verified as catalytically independent. Full original Methods for that paper were not recovered here.

### Activities and products

The canonical activity is transfer of a long-chain acyl group from acyl-CoA to carnitine. CPT1A performs this chemical step of the carnitine shuttle at the outer mitochondrial membrane; it does not itself perform the exchange reaction or the repeated oxidation-cycle chemistry. The current beta-oxidation definition nevertheless covers the overall pathway, so its existing pathway annotations remain positive. The original [human enzyme study](https://doi.org/10.1074/jbc.M310130200) uses full-length human CPT1A expressed in yeast; the [foundational cloning paper](https://pubmed.ncbi.nlm.nih.gov/7892212/) instead measures endogenous human fibroblast CPT activity. Neither is a comparison of the two complete human products. The CPT1C-focused [2006 paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC1564279/) includes a genuine positive CPT1A activity control, but its HEK293T host must not be mistaken for proof of a human activity insert.

Both official products were reconstructed from sequence records: 773 residues for P50416-1 and 756 for P50416-2. VSP_012167 replaces residues 746–773 with an 11-residue alternative tail. Both retain the two annotated membrane segments and shared catalytic-region residues, but the C-terminal difference lies within the catalytic-domain region. In [PMID:21990363](https://pubmed.ncbi.nlm.nih.gov/21990363/), the human isoform-2 template supplied only the Met1–Lys42 NMR peptide; the full-length functional assays used rat CPT1A in Pichia. Sequence compatibility and a shared peptide do not establish equal full-length activity.

A second molecular activity is supported by the actual [2018 lysine-succinylation paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC5826573/). Main Methods and Results distinguish endogenous depletion and cell proteomics from purified ENO1 plus succinyl-CoA assays. No-enzyme and no-succinyl-CoA controls, H473A, substrate-site variants, and G710E separation from carnitine transfer support a distinct peptide-lysine succinyltransferase activity. The broader proteomic list is not a list of individually proven direct substrates. Extended supplementary Methods were not recovered, so their purification details remain outside the read scope. GO:0106076 is represented in a separate molecular-function core without manufacturing a new biological-process annotation. The broad InterPro acyltransferase row is refined to both specific activities, explicitly distinguishing canonical family evidence from the independent succinylation experiments.

The third molecular activity is the reported CPT1A adaptor that recruits ZDHHC4 to MAVS. The complete [PMID:38016475 abstract](https://pubmed.ncbi.nlm.nih.gov/38016475/) and existing [human GO-CAM](https://www.geneontology.org/gocam/65bc474400000029) support this defined recruitment role and positive innate-immune regulation. ZDHHC4, not CPT1A, performs MAVS palmitoylation. The original full Methods remain unavailable despite bounded recovery attempts; neither H473A independence nor a purified binary interface is claimed. No NEW row is needed because the adaptor and immune-process annotations already exist.

### Ortholog evidence and response terms

The actual PTHR22589 tree places the official human sequence below PTN001097100. Four current IBDs lie on that path and no loss record lies on it. A separate CPT1C loss branch is outside the human CPT1A path. The human target's presence among experimental descendant sources is legitimate. Current ARBA predicates were checked against the official FunFam identifiers and taxonomy: matching branches are 15 for ARBA00028692, 0 for ARBA00087538 and 11 for ARBA00088384. These are present-day applicability checks, not reconstructed historical curator or rule runs. An unmerged family-review proposal was not imported.

The rat evidence is heterogeneous and remains source-specific. Response terms can include expression changes; a measured change is not invalid merely because CPT1A is not the stimulus receptor. Actual rat hepatocyte, high-fat/myriocin and alcohol/alirocumab Methods and Results support their stated response scopes. Other rat papers remain abstract-only, with their positive source assertions and access limits retained. Liver regeneration remains UNDECIDED because the available source resolves lipid physiology but not regrowth of damaged or removed liver. The mouse intracellular-glucose-homeostasis premise also remains unresolved. GO-CAM 69ea894900000564 preserves the same mouse ISS context; this is acknowledged rather than treated as a new direct experiment.

The original [INS1E experiment](https://doi.org/10.1042/bj3640219) used sequence-verified full-length rat liver CPT1, increased activity and palmitate oxidation, and measured glucose-stimulated insulin secretion with inhibitor and rescue controls. Its abstract states, “These results provide further evidence that CPT I activity regulates insulin secretion in the beta-cell.” The actual indexed Methods and Results were read, with gaps identified in the evidence ledger. This supports a context-dependent non-core role rather than a blanket rejection as an unspecified downstream effect.

The [rat oligomerization study](https://pmc.ncbi.nlm.nih.gov/articles/PMC2652319/) provides positive self-association evidence: “There was minimal self-association of the sequence corresponding to TM1 but significant self-association of TM2 in TOXCAT.” Native and recombinant assays support trimers and hexamers with preparation-dependent proportions. They do not establish a human homodimer or prove the proposed channel mechanism.

### Localization and differentiation

HPA mitochondrial immunofluorescence and the original [MitoCoP workbook](https://pmc.ncbi.nlm.nih.gov/articles/PMC8664129/) support mitochondrial localization at their actual resolution. CPT1A is protein group 4917, sheet `(A) All protein groups`, row 264, and gene row 239 of `(B) MitoCoP (1,134 genes)`. P50416 and P50416-2 are grouped. The membrane category is blank, integral percentage is NaN and carbonate extraction has only one valid ratio; sonication has four. The inherited outer-membrane annotation column does not independently establish topology. Broad membrane detection in the NK-cell paper is retained with curator deference because that full target table remains unavailable and membrane association is independently correct.

The authentic [Caco-2 paper](https://doi.org/10.1111/j.1440-169X.2011.01258.x) does identify P50416 in Table 1, with a 4.02-fold increase between the assayed differentiation states. CPT1A was not among the seven selected immunoblot/qPCR confirmations. The observation is real; the read Methods and Results do not resolve its functional contribution to acquiring epithelial specialization. UNDECIDED therefore reflects unclear participation, not an inaccessible article or a wrong-target allegation.

Reactome's structured reaction-to-catalyst-to-P50416 path supports the outer membrane and carnitine shuttle. The R-HSA-200406 narrative's first sentence says inner membrane, conflicting with its structured location and primary evidence. The original text is preserved, and substrate compartments are not assigned wholesale to the enzyme.

### Source continuity

The [source evidence index](CPT1A-source-evidence.yaml) records all 53 historical assertions, all 52 current source objects, current donor records, typed ontology evidence, product reconstruction and exact primary-access boundaries. Thirty inherited WITH/FROM omissions remain visible rather than being falsely recast as historical complete records. One historical source occurrence is retired because it is absent from the fresh source set; its carnitine-shuttle biology remains ACCEPT. Retirement is bookkeeping about source presence, not a biological REMOVE. The journal prefix and all machine-fetched sources remain unchanged.


## 2026-10-12 — source-specific follow-up

The earlier journal, including its pre-existing tool markup, remains an unchanged historical prefix. This entry supersedes the preceding two-replacement InterPro assessment and the positive dispositions for glucose metabolism and regulation of fatty-acid oxidation. The InterPro row now refines only to carnitine O-palmitoyltransferase. The independently demonstrated peptide-lysine succinyltransferase activity remains in the second core, with its own experimental source; no redundant NEW assertion is added beneath an existing acyltransferase ancestor.

The rat studies show real changes in oxidation flux and neurohepatic glucose production. They do not yet resolve the specific participation-versus-regulation interpretation of the two oxidation-regulation transfers or CPT1A's own participation in the glucose chemical pathway. Those three assertions are now UNDECIDED, preserving the positive observations and the distinct access limits. Intracellular glucose homeostasis remains a separate unresolved claim about steady-state glucose within a cell, with an unreconstructed historical mouse premise. These judgments do not treat a downstream physiological response as false merely because it is non-core. The earlier assertion that catalytic rate control alone settles a GO regulation annotation is withdrawn.

The membrane HDA row now refines to mitochondrial outer membrane on independent target topology and enzyme evidence. The unrecovered NK-cell target table is not represented as resolving that finer site. Broad mitochondrial HPA and MitoCoP measurements retain their actual assay resolution. Beta-oxidation remains supported by performed shuttle chemistry, human biochemical evidence and curated pathway placement; the definition's CoA-addition clause is not itself a statement about carnitine transfer. The reported MAVS adaptor activity remains a distinct molecular activity, with uncertain generality outside the studied context and with the unrecovered full Methods limitation explicit.

### Portable original-source anchors

The following short excerpts are from externally recovered originals, not from rewritten publication caches. The existing cache quotes remain unchanged.

- [PMID:14517221, original author-laboratory PDF](https://tonglab.biology.columbia.edu/Research/crat_cpt.pdf), human construct Methods, page 50429: “containing the full-length human CPT1A cDNA”. This identifies the human insert expressed in yeast.
- [PMID:7892212, original PMC scan](https://pmc.ncbi.nlm.nih.gov/articles/PMC42407/), fibroblast assay Results, page 1988, item (iv): “fibroblast homogenates were assayed for CPT I activity”. The human fibroblast assay is distinct from yeast expression of human enzyme.
- [PMID:11988095, original indexed author upload](https://www.researchgate.net/publication/11382320_Adenovirus-mediated_overexpression_of_liver_carnitine_palmitoyltransferase_I_in_INS1E_cells_effects_on_cell_metabolism_and_insulin_secretion), Discussion, page 225: “CPT I controls the fatty acid oxidation ﬂux directly.” This is the authors' flux interpretation, not an independently demonstrated regulatory mechanism separate from the catalytic entry step. The actual Methods use rat liver CPT1 in INS1E cells.
- [PMID:21492153, original publisher Table 1](https://onlinelibrary.wiley.com/doi/10.1111/j.1440-169X.2011.01258.x), CPT1A/P50416 row: “Carnitine O-palmitoyltransferase 1, liver isoform”. The row's fold-change value is 4.02. It measures differentiation-associated expression, not a resolved CPT1A differentiation mechanism.

The [MitoCoP source](https://pmc.ncbi.nlm.nih.gov/articles/PMC8664129/) is PMID:34800366, not the Caco-2 PMID:21492153. Its original Supplementary Data 1 workbook and complete A264/B239 target rows are separately identified in the source-evidence index. A blank category, NaN integral percentage and one valid carbonate ratio do not establish integral topology; the grouped product identifiers do not separate the two human products. The source index is a manually assembled evidence record with deterministic literal projections, not an independent experiment or a claimed one-command generator. Raw sections retain their original evidence; the follow-up assessments are separated below them.
