# ADSL (adenylosuccinate lyase) — review notes

The 2026-09-27 audit below is the current assessment. The earlier notes are retained as history; their GMP/XMP/salvage rejections, blanket propagation claim, and whole-pathway interpretation of “step 2/2” are superseded.

## Prior review (superseded where revised below)

UniProtKB:P30566 (PUR8_HUMAN). HGNC:291. EC 4.3.2.2. Chromosome 22q13.1.
Lyase 1 family, adenylosuccinate lyase subfamily.

Deep research status: falcon provider out of credits (HTTP 402); no
`-deep-research-falcon.md` generated. Review grounded in the cached UniProt
record, the seeded GOA, cached publications (PMID_10888601, 11428554, 16973378,
19405474, 27590927), and the two cached Reactome entries. PMID:19405474 is the
only one with full text available in the cache; the others are abstract-only.

## Core biology

ADSL is a **homotetrameric** cytosolic enzyme that catalyses **two distinct
beta-elimination (fumarate-releasing) reactions** in purine metabolism, both in
the same active site (three subunits contribute residues to each of the four
active sites):

1. **SAICAR lyase** (de novo IMP branch): (S)-2-(5-amino-1-(5-phospho-D-ribosyl)
   imidazole-4-carboxamido)succinate (SAICAR) → AICAR + fumarate.
   Rhea:RHEA:23920 → GO:0070626.
2. **Adenylosuccinate (S-AMP) lyase** (IMP→AMP branch): N6-(1,2-dicarboxyethyl)-
   AMP (SAMP) → AMP + fumarate. Rhea:RHEA:16853 → GO:0004018.

Both activities reside at the same active site; a single competitive inhibitor
(APBADP) blocks both, showing the two substrates occupy the same site
[PMID:19405474 full text].

Key verbatim support:
- UniProt FUNCTION: "Catalyzes two non-sequential steps in de novo AMP synthesis"
  and "converts succinyladenosine monophosphate (SAMP) to AMP and fumarate."
- PMID:19405474: "Adenylosuccinate lyase (EC 4.3.2.2) catalyzes two β-elimination
  reactions in the de novo synthesis of purines: the cleavage of adenylosuccinate
  (SAMP)1 to AMP and fumarate; and the conversion of 5-aminoimidazole-4-
  (N-succinylocarboxamide ribonucleotide) (SAICAR) to 5-aminoimidazole-4-
  carboxamide ribonucleotide (AICAR) and fumarate."
- PMID:19405474: "ASL, a catalyst of key reactions in purine biosynthesis, is
  normally a homotetramer in which three subunits contribute to each of four
  active sites."
- Reactome R-HSA-73800 / R-HSA-73828: "The active form of this enzyme is a
  cytosolic tetramer" and it mediates both reactions in vivo.

## Localization

Cytosol. IDA (HPA immunofluorescence, GO_REF:0000052), TAS (Reactome), IBA. Also
reported to associate with the purinosome (multi-enzyme DNPS complex) under some
metabolic conditions [Reactome R-HSA-73800; PMID:27590927].

## Disease

Adenylosuccinate lyase deficiency (ADSLD; MIM:103050), autosomal recessive.
Accumulation of dephosphorylated substrates SAICA-riboside (SAICAr) and
succinyladenosine (S-Ado); psychomotor/mental retardation, epilepsy, autistic
features. S-Ado/SAICAr ratio in CSF correlates with severity [PMID:10888601].
Many characterised missense variants reduce activity (PMID:19405474 etc).

## Annotation assessment summary

MF (core):
- GO:0004018 SAMP lyase — IDA x3 (PMID:19405474, 16973378) + IBA + IEA → ACCEPT (core).
- GO:0070626 SAICAR lyase — IDA (PMID:27590927) + IBA + IEA → ACCEPT (core).
- GO:0003824 catalytic activity (IEA/InterPro) — too general; MARK_AS_OVER_ANNOTATED
  (parent of the two specific MFs already present).
- GO:0042802 identical protein binding (IDA PMID:16973378; IEA) — homotetramer, so
  self-association is real, but bare-binding term is uninformative vs the enzymatic
  MFs and complex CC → KEEP_AS_NON_CORE (IDA), IEA duplicate KEEP_AS_NON_CORE.

CC (core = cytosol):
- GO:0005829 cytosol — IDA/TAS/IBA → ACCEPT.
- GO:0032991 protein-containing complex (IDA PMID:16973378) — homotetramer =
  protein-containing complex; correct but very general → KEEP_AS_NON_CORE.

BP:
- GO:0006189 'de novo' IMP biosynthetic process (IEA) — ACCEPT core (SAICAR→AICAR
  is step 2/2 of the IMP de novo pathway; UniProt PATHWAY).
- GO:0044208 'de novo' AMP biosynthetic process (IBA + IEA) — ACCEPT core (SAMP→AMP
  is AMP-from-IMP step 2/2; UniProt PATHWAY).
- GO:0006164 purine nucleotide biosynthetic process (IC PMID:10888601) — ACCEPT
  (correct, general parent).
- GO:0006167 AMP biosynthetic process (IDA PMID:11428554; IEA) — ACCEPT/KEEP; the
  IDA in blood cells measures AMP-producing activity.
- GO:0009152 purine ribonucleotide biosynthetic process (IEA InterPro) — ACCEPT
  (correct general parent).
- GO:0044209 AMP salvage (IEA Ensembl, GO_REF:0000107) — MISLEADING. ADSL's AMP
  production (SAMP→AMP) is part of DE NOVO synthesis (and the purine nucleotide
  cycle), not the salvage (hypoxanthine/adenine phosphoribosyltransferase) pathway.
  → MARK_AS_OVER_ANNOTATED (Ensembl ortholog electronic transfer, biologically off).
- GO:0006177 GMP biosynthetic process (IEA Ensembl) — REMOVE. GMP is made from IMP
  by IMPDH + GMPS; ADSL is not on the GMP branch. Wrong IEA ortholog transfer.
- GO:0097294 'de novo' XMP biosynthetic process (IEA Ensembl) — REMOVE. XMP is made
  from IMP by IMPDH; ADSL not involved. Wrong IEA ortholog transfer.
- GO:0009060 aerobic respiration (IEA Ensembl) — REMOVE. ADSL is a cytosolic purine
  biosynthesis enzyme; fumarate release is not participation in aerobic respiration.
  Over-propagated ortholog IEA.
- GO:0001666 response to hypoxia (IEA Ensembl) — REMOVE. No evidence ADSL itself is
  a hypoxia-response effector; electronic ortholog transfer, not supportable.
- GO:0007584 response to nutrient (IEA Ensembl) — REMOVE. Electronic ortholog
  transfer; not supportable for human ADSL.
- GO:0042594 response to starvation (IEA Ensembl) — REMOVE. Same.
- GO:0014850 response to muscle activity (IEA Ensembl) — REMOVE. ADSL is highly
  expressed in muscle and participates in the purine nucleotide cycle there, but
  "response to muscle activity" (a stimulus-response BP) is not a supportable
  molecular role for ADSL from an electronic ortholog transfer. Over-propagation.

The GO_REF:0000107 (Ensembl Compara) block of stimulus/response and off-pathway
biosynthesis terms is the classic over-propagation cluster and is treated as such.


## 2026-09-27 source and pathway audit

### Scope, identity, and baseline

All 30 seeded annotations, 13 original references, two core functions, and the
cached UniProt record were audited. The starting document was INITIALIZED with
30 prior decisions and no NEW rows. Its five gene files matched main
`62134e998e0e4fbda34cc79564fb081e8dbbd951` byte for byte before editing. The
review YAML base blob was `ee68b5cccadfbdfee8322b3240660e0092fbc8ec`.
An open-PR ADSL-symbol query had no matches. Three name/alias-search matches
(#2498, #2516, #3147) were checked by their actual file lists; none touched ADSL.

The [NCBI human record](https://www.ncbi.nlm.nih.gov/gene/158) confirms ADSL,
HGNC:291, and aliases ASL, AMPS and ASASE. Historical “ASL” in the enzyme papers
means adenylosuccinate lyase, while ASL is also the current symbol of the distinct
argininosuccinate lyase gene. The current review retains human UniProt P30566
and the supplied alternative-product records unchanged.

Final actions: **23 ACCEPT, 3 KEEP_AS_NON_CORE, 4 UNDECIDED; 0 NEW**. All 30
source-field objects are unchanged; only their review judgments were revised.
The two cores describe the AMP-forming and SAICAR-cleaving reactions. No new
process annotations were manufactured from disease phenotypes or pathway gaps.

### Reaction and evidence resolution

Human ADSL cleaves SAMP to AMP and fumarate, and SAICAR to AICAR and fumarate.
The SAICAR reaction lies in the shared pathway constructing IMP, upstream of
both adenine and guanine nucleotides. UniProt's “step 2/2” is the **CAIR-to-AICAR
segment**, not the whole de novo IMP pathway. Its separate AMP-from-IMP segment
also has two steps. These local pathway counts do not define the scope of the
corresponding GO processes.

[PMID:19405474](https://pubmed.ncbi.nlm.nih.gov/19405474/) was read in the full
cached article: Methods measures SAMP loss at 282 nm; Figure 3/Table 1 report
AMP-direction kinetics; Figure 6 and the oligomeric-state results connect
assembly defects with activity. K246E has severe oligomerization/activity
impairment. This article experimentally assays SAMP, while its introduction
summarizes SAICAR chemistry. The review does not call that introductory
statement a second substrate-kinetics experiment. The active tetramer has four
active sites, each assembled from three subunits.

[PMID:10888601](https://pubmed.ncbi.nlm.nih.gov/10888601/) provides human
full-length/alternative-transcript and disease-mutant evidence, including
proportional decreases against both substrates; its cache is abstract-only.
[PMID:16973378](https://pubmed.ncbi.nlm.nih.gov/16973378/) reports recombinant
human enzyme kinetics and analytical-ultracentrifugation tetramer mass; E. coli
is the expression host. The functional complex term is accepted at its original
broad resolution, and the two identical-protein-binding rows remain non-core
assembly properties.

[PMID:11428554](https://pubmed.ncbi.nlm.nih.gov/11428554/) supports blood-cell
ADSL activity and AMP-maintenance context. [PMID:27590927](https://pubmed.ncbi.nlm.nih.gov/27590927/)
combines recombinant-enzyme substrate preparation with CRISPR-edited HeLa
cells and metabolite/purinosome measurements. Both caches remain abstract-only.
Their experimentally curated annotations describe established ADSL chemistry
and are accepted with curator deference; knockout substrate accumulation is
not mislabeled as a purified-enzyme IDA assay.

Both cached Reactome events, R-HSA-73800 and R-HSA-73828, explicitly identify
ADSL as the cytosolic catalyst. The [current HPA subcellular page](https://www.proteinatlas.org/ENSG00000239900-ADSL/subcellular)
reports enhanced cytosolic localization with HPA000525 in A-431, U-251MG and
U2OS, including siRNA validation. No more specific compartment is substituted.

### Literal GO scope, PAINT, and GO-CAM donor audit

The live [GO:0006177 definition](https://www.informatics.jax.org/vocab/gene_ontology/GO%3A0006177)
covers “The chemical reactions and pathways resulting in the formation of GMP,
guanosine monophosphate.” It does not restrict membership to IMPDH and GMPS.
[GO:0097294](https://amigo.geneontology.org/amigo/term/GO%3A0097294) covers XMP
formation “from simpler precursors.” ADSL performs the SAICAR cleavage in that
larger biosynthetic sequence; it is not assigned either terminal enzyme activity.

[GO:0044209](https://amigo.geneontology.org/amigo/term/GO%3A0044209) covers AMP
formation from its derivatives without de novo synthesis. Its parents include
AMP biosynthesis and purine ribonucleotide salvage. The definition's examples
of precursors do not restrict the process to APRT or adenosine kinase. Salvaged
purines can reach IMP through HPRT and then AMP through ADSS and ADSL. The
ADSL reaction performs chemical work in that route.

All four IBA rows were checked against the cached PTHR43172 PAINT table.
Their IBD node is **PTN000154581**. Structured source entries use that node
only; human ADSL among the descendant experimental sources supports inherited
function and is not circular evidence. The broad catalytic-activity and
purine-ribonucleotide-biosynthesis InterPro mappings are valid at their original
family-level resolution.

Compara donors were traced to mouse UniProt P54822 / ENSMUSP00000023043 for
the three pathway rows, and rat UniProt A0A8I5ZTN5 / ENSRNOP00000081561 for
the response/respiration and homomeric-binding rows. The six indexed mouse
Adsl GO-CAM activities (MGI:103202) were read, including their substrate and
output connections:

- `60ad85f700003015`, activity `60ad85f700003072`: SAICAR lyase in GMP
  biosynthesis, before ATIC and the IMPDH/GMPS branch.
- `60d5209a00001406`, activity `60d5209a00001482`: SAICAR lyase in de novo
  XMP biosynthesis, before ATIC and IMPDH.
- `60897d8500000531`, activity `60897d8500001245`: SAMP lyase in AMP salvage,
  after HPRT and adenylosuccinate synthetase.
- `60ff660000001341`, activity `60ff660000001352`: AMP salvage from adenosine,
  through ADA, PNP, HPRT and ADSS to ADSL.
- `60ad85f700002694` and `60ad85f700002947`: additional de novo AMP and IMP
  contexts consistent with the two ADSL reactions.

The cached models are under `gocams/<model>/<model>-src.yaml`; they were read
without modification. No direct human P30566 index hit was found. The human
judgments rely on conserved, directly established chemistry as well as the
mouse curator's explicit process modeling.

[PMID:6480832](https://www.jci.org/articles/view/111553), present in the donor
models, is a mouse pharmacological muscle study of disrupted purine nucleotide
cycling. Its accessible abstract is **not** a GMP/XMP flux experiment. The
pathway judgments therefore use the model's reaction sequence together with
human chemistry, rather than overstating that paper's experiment.
[PMID:25681585](https://pmc.ncbi.nlm.nih.gov/articles/PMC4405794/) was recovered
through indexed original Methods/Results/Discussion. Its mouse cardiac HIF-1alpha
and hadacidin experiments support a cycling/salvage context; the induced
regulatory enzymes include AMPD and HPRT, not an established induction of ADSL.

The full cached [PMID:29079593](https://haematologica.org/article/view/8359),
including Figures 5 and 7, provides human/mouse erythrocyte salvage-enzyme and
isotope evidence. PubMed and the publisher identifier were independently
verified. The major hypoxic effect was decreased purine deamination. Aspartate
label in fumarate has alternative metabolic explanations, and these results
are not described as an ADSL-specific knockout or proof of enhanced ADSL flux.

### Rat physiology and source-access limits

The prior blanket removal of response annotations is superseded by an audit of
the actual donor studies. A metabolic enzyme can participate in physiological
responses; cytosolic location alone does not settle the annotation.

- **Hypoxia, UNDECIDED:** the rat NCBI Gene 315150 link identifies
  [PMID:8887278](https://pubmed.ncbi.nlm.nih.gov/8887278/). The abstract studies
  renal cortical/medullary cytosol under simulated normoxic and hypoxic
  conditions. Full methods and the ADSL-specific response scope remain
  unavailable, so exact transfer to human ADSL is unresolved.
- **Nutrient response, UNDECIDED:** the donor link identifies
  [PMID:7128902](https://pubmed.ncbi.nlm.nih.gov/7128902/), comparing purified
  hepatic enzyme from chow-fed and low-riboflavin-diet rats. The abstract gives
  biochemical differences and a cautious link to refeeding. Full experimental
  scope is unavailable; the independent starvation study does not resolve
  every feature of this source.
- **Aerobic respiration and muscle activity, UNDECIDED:**
  [PMID:3777158](https://pubmed.ncbi.nlm.nih.gov/3777158/) reports AICAriboside
  treatment and stimulated rat muscle, motivating an anaplerotic contribution
  of the purine nucleotide cycle. It is the traced respiration source. The
  muscle-response donor carries experimental expression/activity evidence,
  but its exact source assertion was not fully resolved. The accessible
  abstract's stimulation-associated lyase/synthetase changes support a
  connection without settling full assay controls or conserved human process
  participation. This is not a claim that ADSL is a respiratory-chain subunit.
- **Starvation, KEEP_AS_NON_CORE:** [PMID:690130](https://pubmed.ncbi.nlm.nih.gov/690130/)
  was recovered as an [indexed original article copy](https://www.researchgate.net/publication/22452438_Effect_of_diet_on_adenylosuccinase_activity_in_various_organs_of_rat_and_chicken).
  Methods, Results, Tables I–V and Figure 1 were read. Prolonged starvation
  lowers rat hepatic/splenic activity; refeeding restores hepatic activity.
  Brain, kidney and muscle differ, and chicken liver responds in the opposite
  direction. The existing mammalian transfer is retained as a bounded
  physiological context, with no claim that human tissue responses were
  directly measured or that this regulation is universal across species.
- **Homomeric binding, KEEP_AS_NON_CORE:**
  [PMID:3689310](https://pubmed.ncbi.nlm.nih.gov/3689310/) independently reports
  rat native/subunit masses and both substrate activities in its abstract.
  Human tetrameric structure is supported by the original human source; this
  rat source is corroboration, not a substitute for the human experiment.

Human hypoxia studies are relevant follow-up evidence, not replacements for
unread rat assays. Externally indexed Results/Figure 4 of
[PMID:32439803](https://pmc.ncbi.nlm.nih.gov/articles/PMC7363121/) show endogenous
ADSL proximity during hypoxic purinosome assembly, without a corresponding
increase in de novo purine synthesis. Proximity is not direct binding or flux.
[PMID:40033100](https://www.nature.com/articles/s41556-025-01627-8) reports
hypoxia-linked ADSL phosphorylation and local fumarate inhibition of STING in
breast cancer. Its identifier and abstract were verified, but the main article
is subscription-restricted. The specialized mechanism remains a follow-up
lead; no new immune-response annotation or third core was added.

### Research attempt, cache gate, and verification

The required genuine Falcon launch (`--timeout 1200 --fallback perplexity-lite`)
ran with supported temporary UV tool/cache directories in parallel with normal
publication caching. Both providers failed before research because PyPI
`deep-research-client` dependency resolution encountered DNS errors. Neither
produced a report. This is a new failure distinct from the earlier 402 recorded
in the historical notes; no provider file was authored manually.

The five original publications were already cached and left unchanged. The
additional existing cache for PMID:29079593 was read unchanged. Normal
`fetch-pmid` batches for **6480832, 25681585, 3777158, 690130, 3689310,
32439803, 40033100, 8887278, and 7128902** completed with DNS failures and
cached **0/9**. These are required publication-cache gaps: the review must
remain **DRAFT** until fetched normally. Primary identifiers and external
reading are recorded above independently of this machine-cache requirement.
No citation was removed to conceal a missing cache, and no cache was fabricated.
Local `full_text_unavailable` flags remain true for absent/abstract-only caches,
including papers whose full original text was recovered externally.

All original source fields, reference identifiers/titles, alternative products,
and machine-generated gene source files are preserved. The handoff manifest
records validation results, generated history, file hashes, and the explicit
cache gate. No Git, remote PR, shared-project, or source-cache edits were made.

## 2026-09-27 review-status correction

Set the YAML status to DRAFT under the literal GeneReviewStatusEnum, which
reserves COMPLETE for reviews without validation warnings. The already documented
source-cache warnings remain unresolved. All biological judgments, source
assertions, reference assessments and core functions are unchanged. This status
label correction does not imply that source retrieval or automated review has
subsequently succeeded.


## 2026-09-27 PR evidence-scope follow-up

The root catalytic MF is refined to both measured substrate-specific lyase
activities (GO:0004018 and GO:0070626), preserving both reactions. This is based
on the human assays, not a blanket rule that all broad annotations are non-core.
Human tetramer formation is now ACCEPT on both self-association rows and integrated
into the two enzyme cores: each catalytic site receives residues from three subunits
[PMID:19405474]. The broad complex CC remains compatible with that functional assembly.

The rat aerobic-respiration transfer is now MARK_AS_OVER_ANNOTATED. The
[primary rat abstract](https://pubmed.ncbi.nlm.nih.gov/3777158/) proposes that the
purine nucleotide cycle supplies citric-acid-cycle intermediates. The
[live GO definition and parents](https://amigo.geneontology.org/amigo/term/GO:0009060)
describe oxygen-coupled respiratory energy release. The issue is whether the
purine-cycle reaction is itself in that pathway, not whether ADSL must be a
respiratory-chain protein or every participant must perform redox chemistry.
Supplying intermediates supports a metabolic connection without demonstrating
this pathway assignment. The rat phenotype is not denied; full specificity controls
remain inaccessible, and no replacement regulation term is invented. Independent
peer review supported this scope correction and prompted the explicit non-redox caveat.

The reviewer questioned the species of PMID:6480832, but the
[primary PubMed abstract](https://pubmed.ncbi.nlm.nih.gov/6480832/) explicitly reports
28 AICAriboside-treated mice and 22 saline controls. That source is correctly mouse;
the later PMID:3777158 study is rat. Reference notes now name exact primary verification
routes for all nine missing caches, distinguishing abstract versus full-section access.
VERIFIED means inspected identifier/content, not a successful normal cache fetch.
The missing-source requirements remain unchanged. Four IBA source comments are now
term-specific, and the blood-cell AMP row uses measured activity plus independent
reaction support instead of an aim-only quotation. All 30 source assertions and 23
reference identities, downloaded sources and published history remain unchanged.

Peer review also distinguished the dual-substrate assays reported in PMID:10888601 from the reaction descriptions in PMID:19405474, whose measured kinetics concern adenylosuccinate. The two relevant review rows now cite the measured dual-substrate result.
