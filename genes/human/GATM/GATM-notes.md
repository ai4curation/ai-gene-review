# GATM (P50440) review notes

Gene: GATM (HGNC:4175), synonym AGAT. UniProt P50440, "Glycine amidinotransferase, mitochondrial".
EC 2.1.4.1. L-arginine:glycine amidinotransferase / transamidinase.

## Core catalytic function

- AGAT catalyzes the committed/rate-limiting step of creatine biosynthesis:
  L-arginine + glycine -> guanidinoacetate (GAA) + L-ornithine (Rhea:13201). GAA is then
  methylated by GAMT to form creatine.
  [PMID:9218780 "L-arginine:glycine amidinotransferase (AT) catalyses the committed step in creatine biosynthesis by formation of guanidinoacetic acid, the immediate precursor of creatine."]
- Catalytic mechanism: ping-pong, catalytic triad Cys-His-Asp; amidino-cysteine covalent
  intermediate at Cys407 (mature numbering). Active site residues His303, Asp254, Asp305, etc.
  [PMID:9218780 "A reaction mechanism with a catalytic triad Cys-His-Asp is proposed on the basis of substrate and product bound states."]
- New fold ("basket") with 5-fold pseudosymmetry of betabeta-alphabeta modules.
  [PMID:9218780 "The structure of AT reveals a new fold with 5-fold pseudosymmetry of circularly arranged betabeta alphabeta-modules."]
- Purified human kidney enzyme: dimer ~89 kDa, subunits ~44 kDa; Km ~2.5 mM for both arginine
  and glycine (UniProt lists Km 2 uM / 3 uM from later work).
  [PMID:3800397 "Human kidney transamidinase is a dimer with a molecular mass of 89,000 Da and subunit masses of 44,000 Da. The Km for arginine and glycine were both 2.5 mM"]
- Mutagenesis + crystallography confirming catalytic residues and mechanism.
  [PMID:9266688] (substrate binding and catalysis; mutagenesis of Asp170, Glu233, Asp254, His303, Asp305, Arg322, Ser355, Cys407, Cys410).

## Substrate promiscuity (moonlighting / side reactions)

- Human GATM also accepts GABA, beta-alanine and taurine as amidino acceptors, producing
  guanidinobutyrate (GBA), guanidinopropionate (GPA) and taurocyamine (TC) respectively, with
  decreasing preference; glycine remains the main substrate.
  [PMID:36543883 "human GATM had the highest activity with glycine, but also GABA, β-alanine and taurine were accepted as substrates with decreasing preference"]
  [PMID:36543883 "In creatine biosynthesis, the intermediate guanidinoacetate is formed from glycine and arginine by mitochondrial glycine amidinotransferase (GATM)"]
  These appear as additional CATALYTIC ACTIVITY entries in UniProt (Rhea 75939/75943/75947).
  This justifies the broader parent MF "amidinotransferase activity" (GO:0015067) as IDA in GOA.

## Localization

- Mitochondrial enzyme; canonical isoform 1 has a cleaved N-terminal mitochondrial transit
  peptide (1-43) and localizes to the mitochondrial intermembrane space / inner-membrane
  intermembrane side. IDA placement in intermembrane space (MGI, PMID:9218780).
  UniProt: "Mitochondrion inner membrane; Peripheral membrane protein; Intermembrane side.
  Note=Probably attached to the outer side of the inner membrane." Isoform 2 = cytoplasmic.
- GOA also has C:mitochondrion (IDA HPA, HTP) - consistent broader location.
- C:extracellular exosome (HDA, PMID:23533145, prostatic-secretion exosome proteomics) is a
  high-throughput proteomics co-purification; not a site of catalytic function. Over-annotation
  / non-core.

## Tissue expression and regulation

- Expressed broadly; highest in kidney; also liver, pancreas (exocrine acinar cells), heart,
  brain, lung, salivary gland, skeletal muscle. HPA group-enriched kidney/liver/pancreas.
  [UniProt TISSUE SPECIFICITY: "highest expression in kidney"]
  [PMID:28844881 "GATM is highly expressed in pancreatic exocrine acinar cells"]
- Feedback repression of AGAT by creatine (classic; not directly in cached abstracts but a
  well-established regulatory feature). Induction: elevated in failing myocardium (PMID:16820567),
  decreased in IUGR placenta (PMID:16125225). Not GO-annotated; record as biology only.

## Disease

- Cerebral creatine deficiency syndrome 3 (CCDS3 / AGAT deficiency, MIM:612718): autosomal
  recessive; intellectual disability/developmental delay, speech delay, severe brain creatine
  depletion; many develop myopathy. Treatable with oral creatine.
  [PMID:26490222 "Arginine:glycine aminotransferase (AGAT) (GATM) deficiency is an autosomal recessive inborn error of creative synthesis."]
  [PMID:26490222 "15 patients diagnosed between 16 months and 25 years of life had intellectual disability/developmental delay (IDD). 8 patients also had myopathy/proximal muscle weakness."]
  [PMID:27233232 "Clinical features include intellectual disability, hypotonia, and myopathy."]
  Many loss-of-activity missense variants characterized in PMID:27233232 (IDA glycine
  amidinotransferase activity supported by variant assays).
- Fanconi renotubular syndrome 1 (FRTS1, MIM:134600): autosomal DOMINANT; a distinct,
  gain-of-toxicity mechanism - specific GATM missense variants (e.g. P320S, T336A/I, P341L)
  cause GATM protein AGGREGATION in mitochondria, abnormal/elongated mitochondria, ROS,
  NLRP3 inflammasome activation, proximal tubulopathy and progressive kidney failure
  (PMID:29654216). This is a toxic-aggregation gain of function, NOT loss of catalytic activity.

## GO annotation assessment summary

Core:
- MF: glycine amidinotransferase activity (GO:0015068) - EXP/IDA, multiple papers. ACCEPT (core).
- BP: creatine biosynthetic process (GO:0006601) - IDA/IBA. ACCEPT (core).
- CC: mitochondrial intermembrane space (GO:0005758) - IDA. ACCEPT (core location).

Supporting/peripheral:
- amidinotransferase activity (GO:0015067) parent MF - ACCEPT as accurate parent (promiscuous
  side activities). Keep.
- mitochondrial inner membrane (GO:0005743) IEA SubCell - ACCEPT/keep (UniProt subcellular).
- mitochondrion (GO:0005739) IDA/HTP - ACCEPT (broader true location).
- cytoplasm (GO:0005737) IEA SubCell - reflects cytoplasmic isoform 2; KEEP_AS_NON_CORE.
- positive regulation of cold-induced thermogenesis (GO:0120162) ISS/IEA from mouse Adipo-Gatm
  KO (PMID:28844881) - real mouse phenotype but a tissue/context-specific downstream consequence
  of creatine synthesis, not a core human function. KEEP_AS_NON_CORE.
- learning or memory (GO:0007611) IMP CAFA (PMID:26490222) - downstream of brain creatine
  depletion; over-reach from a clinical ID phenotype. MARK_AS_OVER_ANNOTATED.
- muscle atrophy (GO:0014889) IMP CAFA (PMID:26490222) - downstream myopathy consequence;
  over-annotation. MARK_AS_OVER_ANNOTATED.
- extracellular exosome (GO:0070062) HDA (PMID:23533145) - HTP co-purification; over-annotation.
- protein binding (GO:0005515) IPI x13 (PMID:32814053) - uninformative; this is the
  Haenig/neurodegeneration interactome map. MARK_AS_OVER_ANNOTATED (avoid bare protein binding).
- acts_upstream_of_or_within creatine biosynthetic process (GO:0006601) IDA - same as core BP,
  weaker qualifier; ACCEPT.

References to cite: 9218780, 3800397, 9266688, 36543883, 27233232, 26490222, 28844881,
23533145, 32814053, 34800366, plus GO_REFs and Reactome already in stub.

## QA re-review 2026-07-23 (conservative)

Re-validated `GATM-ai-review.yaml`: `ai-gene-review validate` returns "✓ Valid", no
warnings. Audited all 25 annotations plus core_functions. No changes made — the review is
biologically and curatorially sound.

Checks performed:
- `protein binding` (GO:0005515, IPI, PMID:32814053) is correctly `MARK_AS_OVER_ANNOTATED`,
  not ACCEPT (bare protein binding from an HT interactome; no defined GATM complex). OK.
- All 10 cited PMIDs are cached; every `supporting_text` verifies as a verbatim
  (whitespace-normalized) substring of its cached publication. Labels match GOA terms.
- No action/reason contradictions found; MARK_AS_OVER_ANNOTATED / KEEP_AS_NON_CORE reasons
  each give positive justification (learning-or-memory & muscle-atrophy are distal disease
  consequences; cold-induced thermogenesis is tissue/context-specific mouse phenotype;
  extracellular exosome is HT co-purification).
- core_functions ids are all in the correct GO aspect: GO:0015068 & GO:0015067 (MF),
  GO:0006601 (BP, directly_involved_in), GO:0005758 (CC, locations). Core glycine
  amidinotransferase activity → creatine biosynthesis in the mitochondrial IMS is captured
  as core and not over-generalized; the parent GO:0015067 as a second core_function is
  justified by the experimentally documented promiscuity (PMID:36543883).
- Left alone (conservative): all EXP/IDA/IMP experimental annotations retained per their
  authors; no REMOVE issued; no existing-annotation term ids rewritten.
</content>


## Evidence reassessment — 2026-11-04

The preceding journal is preserved verbatim as historical work. The current assessment reviews all 37 original contexts, including the thirteen distinct interaction partners that were previously summarized by one stored row. Current decisions and selected source locators are in the [source guide](GATM-source-guide.md).

GATM performs the entry reaction of creatine synthesis. Purified human kidney enzyme supports dimer formation [PMID:3800397 "transamidinase is a dimer"]. Broader acceptor activity is retained within one catalytic synthesis, with the experimental readout and limits stated in the current reference assessment rather than treating side reactions as established physiological programs.

The natural products and engineered proteins are distinguished in the current product descriptions. The older journal's “mature numbering” for Cys407 should be read as canonical precursor numbering. A missing targeting segment does not by itself establish cytoplasmic localization, and a changed catalytic region does not establish measured inactivity.

The primary clinical paper includes actual cognitive assessments and biopsy atrophy. Learning or memory is therefore retained as a contextual function; atrophy remains a consequence of deficiency rather than a process performed by GATM. The thermogenesis interpretation separates the cold endpoint from the adrenergic rescue experiment and uses the verified directional erratum.

Original target tables support the interaction and urinary-vesicle observations. Four binding partners permit informative class refinements; nine positive pairs remain uninformative generic binding assertions. The MitoCoP record includes GATM through literature rather than a new target proteomics measurement. These distinctions preserve positive observations without assigning unmeasured mechanisms.

All fifteen inherited quote associations remain historical and traceable through the preserved review and Git locators. The three newly selected literal anchors are short and centralized; repeated quotations are not needed for source-linked support. Genuine native refresh matched all 37 contexts and three products without reseeding. All 35 source records are now present, including 14 missing-only acquisitions and 21 unchanged sources. Reference titles and the three short anchors match exactly. A genuine EDIT record documents this update. Default validation and strict GOA matching passed with zero annotation advisories; native status computation sets COMPLETE. The initial report-only status mismatch is retained as a diagnostic. All 35 source bytes and the ontology cache remain unchanged.


## 2026-11-04 — Review follow-up

Formal cognitive testing is retained as a genuine AGAT-deficiency phenotype, while the learning/memory assertion is marked over-annotated because precursor synthesis does not itself perform information processing. Cytoplasm remains non-core with the explicit product-2 database context and its unresolved experimental basis. The broad enzyme parents are refined to the established glycine reaction; wider in-vitro acceptor chemistry remains documented.

Short exact cache excerpts now accompany the experimental claims. The four binding refinements cite the actual partner records as well as the interaction paper, without assigning partner activities or claiming orthogonal validation. The positive urinary-vesicle identification supports the non-core location independently of any extracellular enzymatic role. The description restores catalytic mechanism, expression and both recessive deficiency and dominant renal aggregation disease. See the [source guide](GATM-source-guide.md) for selected-source access and the [review](GATM-ai-review.yaml) for the evidence-linked reasons. All existing normal source bytes, original contexts, product sequences and previous journal text are preserved.

Native amendment outcome: Default validation, strict GOA matching, computed-status audit, genuine EDIT history validation and private rendering pass. Computed review status remains COMPLETE, with zero annotation advisories. The only diagnostic is a dependency deprecation notice. All 35 normal source objects and the ontology cache remain unchanged.


## 2026-11-04: measured secondary acceptor breadth

The experimental broad amidinotransferase annotation is retained as non-core to keep its measured non-glycine chemistry machine-readable. This supersedes the prior refinement of that IDA row; the family-based refinement and single physiological core remain ([PMID:36543883](https://pubmed.ncbi.nlm.nih.gov/36543883/), [source guide](GATM-source-guide.md)).

The native result is DRAFT with one retained consistency advisory; the source-specific activity distinction is intentional. The [source guide](GATM-source-guide.md) records the checked outcome.


## 2026-11-04: broad activity retained across both source contexts

Independent human acceptor assays make the broad amidinotransferase term informative beyond glycine-specific catalysis. Both existing parent assertions are now non-core; this supersedes the earlier InterPro refinement and its source-specific action distinction. The family mapping alone does not establish the complete substrate range, and the single physiological core is unchanged ([PMID:36543883](https://pubmed.ncbi.nlm.nih.gov/36543883/), [source guide](GATM-source-guide.md)).
