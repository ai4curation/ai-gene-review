# AGL (Glycogen debranching enzyme, GDE) — review notes

> Historical notes below are preserved as an audit trail. The 2026-09-27 audit at
> the end supersedes their action recommendations and the claims that AGL is
> exclusively monomeric, that inclusions are mutant-only, that SR/granule locations
> are artifacts, and that carbohydrate binding is functionally uninformative.

UniProtKB: P35573 (GDE_HUMAN); HGNC:321; gene AGL (syn. GDE); 1532 aa, ~174.8 kDa.

## Core biology

AGL is the cytosolic **glycogen debranching enzyme**, a single ~175 kDa polypeptide that is
**bifunctional / multifunctional**, carrying two independent catalytic activities on one chain
(UniProt: "Multifunctional enzyme acting as 1,4-alpha-D-glucan:1,4-alpha-D-glucan 4-alpha-D-glycosyltransferase
and amylo-1,6-glucosidase in glycogen degradation"):

- **4-alpha-glucanotransferase (EC 2.4.1.25)** = GO:0004134 — "Transfers a segment of a (1->4)-alpha-D-glucan
  to a new position in an acceptor, which may be glucose or a (1->4)-alpha-D-glucan." (UniProt CATALYTIC ACTIVITY)
- **Amylo-alpha-1,6-glucosidase (EC 3.2.1.33)** = GO:0004135 — "Hydrolysis of (1->6)-alpha-D-glucosidic branch
  linkages in glycogen phosphorylase limit dextrin." (UniProt CATALYTIC ACTIVITY)

Mechanism: works with glycogen phosphorylase to fully degrade glycogen branches. Phosphorylase stalls ~4
glucose residues from an alpha-1,6 branch point (leaving a "limit dextrin"). AGL's transferase moves a
maltotriose unit (3 glucoses) to a nearby non-reducing 1,4-end, exposing the single alpha-1,6-linked glucose,
which the glucosidase then hydrolyses to release **free glucose**. Reactome models these as two cytoplasmic
steps: R-HSA-71552 (transferase) and R-HSA-71593 (glucosidase releasing alpha-D-glucose).

**Localization:** cytoplasm/cytosol (UniProt SUBCELLULAR LOCATION "Cytoplasm {ECO:0000269|PubMed:17908927}";
IDA GO:0005737 from PMID:17908927; IDA GO:0005829 cytosol from HPA). "Under glycogenolytic conditions
localizes to the nucleus" — PMID:17908927 shows ~90% of transfected cells show partial nuclear staining for
AGL after 4 h glycogen depletion. HPA also reports nucleoplasm/nuclear body IDA. Nuclear localization is
condition-dependent and not the site of the core catalytic function.

**Family / domains:** glycogen debranching enzyme family; CAZy GH13 + GH133; InterPro IPR006421
(Glycogen_debranch_met), IPR010401 (AGL/Gdb1). Cryo-EM structure PDB 8ZEQ (full length). Predicted active
site residues 526, 529, 627 (ECO:0000250).

## Disease

Deficiency causes **Glycogen storage disease type III (GSD III; Cori disease / Forbes disease)**, MIM:232400 —
accumulation of abnormal glycogen with **short outer chains** (limit-dextrin-like). Clinically: hepatomegaly,
hypoglycemia, short stature, variable myopathy, cardiomyopathy. Subtypes: IIIa (liver + muscle), IIIb (liver
only); rare IIIc/IIId reflect selective loss of glucosidase or transferase activity respectively (UniProt
DISEASE). GSD III patients often lack detectable debrancher protein (PMID:2961257 immunoblots: "the antiserum
detected no cross-reactive material in any of the liver or muscle samples from patients with Type III glycogen
storage disease").

## Key references (verified against cached publications)

- **PMID:2961257** (Chen et al. 1987, Am J Hum Genet) — purification of debranching enzyme (single ~160 kDa
  band), antibody characterization, immunoblots of GSD III. Abstract-only cache. GOA cites this (EXP, via
  Reactome) for both MF activities GO:0004134 and GO:0004135. This paper is a purification/immunochemistry
  study; the enzymatic activities are foundational and consistent with the assay. ACCEPT both.
- **PMID:1374391** (Yang et al. 1992, JBC) — cDNA cloning of human muscle debranching enzyme; "an important
  step toward defining the structure-function relationship of this multifunctional enzyme." GOA cites it
  (TAS, PINC) for GO:0043033 "isoamylase complex" part_of. AGL is a **monomer** (UniProt SUBUNIT: "Monomer.")
  and the mammalian debranching enzyme is a single bifunctional polypeptide, NOT a member of the bacterial/
  plant isoamylase multi-subunit complex. GO:0043033 is a legacy/dubious CC — MARK_AS_OVER_ANNOTATED
  (do not REMOVE an experimental/TAS curated by a database; but flag as over-annotation; abstract does not
  mention any complex).
- **PMID:17908927** (Cheng et al. 2007, Genes Dev) — AGL ubiquitination in Lafora/Cori disease. Verbatim:
  "AGL is cytoplasmic whereas Malin is predominately nuclear"; "after depletion of glycogen stores for 4 h,
  approximately 90% of transfected cells exhibit partial nuclear staining for AGL"; "the E3 ubiquitin ligase
  Malin interacts with and promotes the ubiquitination of AGL"; "the G1448R genetic variant of AGL is unable
  to bind to glycogen." GOA cites for GO:0005737 cytoplasm (IDA — ACCEPT) and GO:0005515 protein binding
  (IPI with NHLRC1/malin Q6VVB1 — MARK_AS_OVER_ANNOTATED, bare protein binding).
- **PMID:24837458** (Jiang et al. 2014, Biosci Rep) — STBD1 CBM20. Full text available. Verbatim: "co-
  immunoprecipitation experiments demonstrated that HA–STBD1 could bind to FLAG-tagged Laforin, GBE1 and GDE";
  "STBD1 WT ... could all bind to endogenous GDE, Laforin and GS"; "co-expression of HA–STBD1 with FLAG–GDE
  caused a targeting of GDE to the ER compartment as well." GOA cites for GO:0005515 protein binding
  (IPI with STBD1 O95210 — MARK_AS_OVER_ANNOTATED, bare protein binding). Note: this is the STBD1 partner;
  the interaction with GDE is real but "protein binding" is uninformative.

## Annotation decisions summary

Core (ACCEPT): GO:0004134 (IBA, IEA, EXP), GO:0004135 (IBA, IEA, EXP), GO:0005980 glycogen catabolic process
(IBA, TAS-Reactome; IEA accepted), GO:0005829 cytosol (IDA-HPA, TAS-Reactome), GO:0005737 cytoplasm (IDA
PMID:17908927; IEA accepted).

Binding-related (MARK_AS_OVER_ANNOTATED, per policy for bare protein binding / uninformative):
GO:0005515 protein binding (both IPIs), GO:0031593 polyubiquitin modification-dependent protein binding (IEA),
GO:0030246 carbohydrate binding (IEA), GO:0030247 polysaccharide binding (IEA — glycogen-binding is real via
the CBM but these are uninformative relative to the catalytic MFs; the substrate binding is captured by the
enzymatic activities and glycogen catabolic process).

CC over-annotations from Reactome "Neutrophil degranulation" reaction propagation (AGL appears in neutrophil
degranulation cargo lists): GO:0005576 extracellular region (x2 TAS), GO:0034774 secretory granule lumen,
GO:1904813 ficolin-1-rich granule lumen — MARK_AS_OVER_ANNOTATED; AGL is a cytosolic enzyme, not a secreted/
granule-lumen protein. These are artifacts of the neutrophil-degranulation proteomics dataset.

Nuclear CC (condition-dependent, non-core): GO:0005634 nucleus (IEA), GO:0005654 nucleoplasm (IDA-HPA),
GO:0016604 nuclear body (IDA-HPA) — KEEP_AS_NON_CORE; AGL relocates to nucleus during glycogenolysis
(PMID:17908927) but core function is cytosolic.

Other CC IEA: GO:0016529 sarcoplasmic reticulum (IEA-Ensembl from rat/mouse ortholog), GO:0016234 inclusion
body (IEA-Ensembl) — MARK_AS_OVER_ANNOTATED (inclusion body relates to aggresome formation of the unstable
G1448R mutant, not WT function); sarcoplasmic reticulum is an ortholog-transfer artifact not supported for
human WT.

BP IEA: GO:0005975 carbohydrate metabolic process (IEA-InterPro) — ACCEPT (correct, broad parent).
GO:0005978 glycogen biosynthetic process (IEA-InterPro/KW) — REMOVE: AGL is a **catabolic/degradation** enzyme,
not biosynthetic; this is a demonstrably wrong IEA (InterPro2GO mapping of a debranching signature to
biosynthesis). Directionally contradicted by the enzyme's role in glycogen breakdown.
GO:0007584 response to nutrient, GO:0009725 response to hormone, GO:0051384 response to glucocorticoid — all
IEA-Ensembl from rat/mouse ortholog; plausible (AGL is regulated by fasting/refeeding, PMID:17908927 "Refeeding
mice ... causes a reduction in hepatic AGL levels") but not core molecular function — KEEP_AS_NON_CORE.

## 2026-09-27 source-specific audit

All 35 seeded annotations were reviewed. Final actions: **16 ACCEPT, 4
KEEP_AS_NON_CORE, 2 MODIFY, 3 REMOVE, 10 UNDECIDED**, with no NEW annotations.
Two catalytic core functions are retained. All annotation source fields, the 14
original reference id/title pairs, alternative products, GOA and UniProt records
are preserved. COMPLETE records completion of the annotation audit; publication
must remain **DRAFT** pending the missing machine caches listed below.

### Identity and baseline

[NCBI Gene 178](https://www.ncbi.nlm.nih.gov/gene/178) verifies the approved human
symbol AGL, synonym GDE, HGNC:321, ENSG00000162688 and UniProt P35573. Before edits,
all five local gene-file byte-derived Git blob hashes matched the GitHub main
contents endpoint. Parent's latest known main commit was
62134e998e0e4fbda34cc79564fb081e8dbbd951; a separate main-commit request failed
after the successful file checks. Baseline status was INITIALIZED despite 35
previously adjudicated rows, 14 references, two cores and no prior NEW rows.
Open-PR searches for AGL, GDE and "glycogen debranching" returned no matches.

Baseline blobs: YAML 933c62f1d56478dccdbde85acbab1d07b024670d;
notes f6c13fbd81e2ef8138be9d504671bd570501c43c;
HTML f9bf15ab79061c7c925fac8683cb415dc9e06f96;
GOA 0b454697517371bb994944da031bf0158e06656f;
UniProt 5d5b9a5a8c53264e7ad1868b56e129af5adb38d1.

### Research execution and cache boundaries

The review and annotation-reviewer skills were applied. This lane is the delegated
annotation-reviewer consultation. Publication caching and the default Falcon
research launch ran concurrently. An initial offline dependency-resolution attempt
failed; the corrected network-enabled launch used the supported per-process
UV_TOOL_DIR=/tmp/aigr-uv-tools, UV_TOOL_BIN_DIR=/tmp/aigr-uv-bin and
UV_CACHE_DIR=/tmp/aigr-uv-cache with a 1200-second timeout and perplexity-lite
fallback. Both providers then failed while resolving deep-research-client from
PyPI because DNS was unavailable. Neither provider produced a report. No manual
text was named as provider output. Logs: /tmp/AGL-provider.log and
/tmp/AGL-provider-network.log. Manual primary-source research is documented here.

Normal gene-publication caching found all four original PMIDs already cached
(1374391, 17908927, 24837458, 2961257). Added references 6449198 and 23650620 also
already have normal caches. Normal fetch-pmid for **40593796, 15180797, 120213 and
1413626** failed DNS for all four (/tmp/AGL-additional-cache.log). These remain
required; external web access does not replace machine caching. Original Reactome
references **R-HSA-70221, R-HSA-71552 and R-HSA-71593** also lack local caches;
the existing Reactome ETL fetch failed DNS (/tmp/AGL-reactome-cache.log). Their
live pages were independently read. Existing caches were not overwritten.

Local full_text_unavailable flags remain true for absent or abstract-only PMID
records, including papers whose main text was recovered externally. The cached
2961257 "Full Text" heading repeats the abstract and is not complete article
access. The 6449198 cache contains citation metadata but no abstract. The 24837458
cache contains the actual Methods, Results, figures and Discussion and was read.

### Human catalysis, binding and oligomerization

[PMID:40593796](https://pubmed.ncbi.nlm.nih.gov/40593796/), Guan et al.,
*Molecular architecture and catalytic mechanism of human glycogen debranching
enzyme*, Nat Commun 16:5962 (2025),
[original PMC article](https://pmc.ncbi.nlm.nih.gov/articles/PMC12219210/),
DOI 10.1038/s41467-025-61077-6, was verified on PubMed and read through indexed
primary Results, Figures 2–5 and Methods. Direct PMC open presented CAPTCHA;
queries combining PMC12219210 with the relevant section names recovered the
actual original text, not a generated summary.

The study purified human P35573 expressed in HEK293F cells, measured separate GT
and GC activities, and tested glycogen affinity using ConA-immobilized glycogen.
Methods, Glycogen binding assay: "The binding capability of glycogen and hsGDE
was assayed via pull-down assay". This supports both existing carbohydrate-binding
rows being refined to GO:2001069, independently of the inaccessible rat binding
paper. Figure 5/Results also reports protein "existing in both monomeric and
dimeric forms". The previous monomer-only argument is withdrawn; assembly alone
does not establish GO:0043033 isoamylase-complex membership. ATP/pH-dependent
assembly observations do not establish an ATPase annotation.

Both core functions now cite the exact reaction statements in the immutable
UniProt record, rather than disease or protein-abundance snippets. The modern
human catalytic assays corroborate these established functions. The prior
suggested mutagenesis of a guessed shared active-site triad is replaced with a
question about the functional consequences of assembly. No residue-specific
annotation or unsupported new process is added.

[PMID:2961257](https://pubmed.ncbi.nlm.nih.gov/2961257/) was independently verified.
The purified enzyme was porcine; human liver inhibition and human tissue
immunoblots establish related target evidence. Its abstract-only status does not
justify overturning known catalytic EXP annotations, which have independent human
support. Protein loss in patients is not substituted for a direct reaction assay.

[PMID:1374391](https://pubmed.ncbi.nlm.nih.gov/1374391/) verifies human-muscle cDNA
cloning, with porcine peptides used to establish clone identity. The original full
body was not recovered; specific isoamylase-complex support remains UNDECIDED.

### Mouse Agl: full source and species boundaries

[PMID:17908927](https://pubmed.ncbi.nlm.nih.gov/17908927/), Cheng et al. (2007),
DOI 10.1101/gad.1553207, was read in full via the
[original author-uploaded article](https://www.researchgate.net/publication/5935979_A_role_for_AGL_ubiquitination_in_the_glycogen_storage_disorders_of_Lafora_and_Cori's_disease).
The cache itself remains abstract-only. Methods, Plasmids identifies mouse-liver
Agl cDNA. HepG2 and 293T are human host cells, not proof that the tagged protein is
human. COS experiments likewise use this construct.

Figure 1 compares WT, carbohydrate-binding deletion and G1448R using amylose resin
and glycogen-enriched fractions. Figure 2 includes WT inclusions under MG132,
although mutants aggregate more frequently. Figure 3 shows conditional nuclear
redistribution in HepG2. Figures 1F/4 and denaturing-IP Methods establish covalent
ubiquitination of Agl; the Results specify "analyzed for covalently linked
ubiquitin". This is the reason to remove the propagated polyubiquitin-dependent
protein-binding MF, rather than an assumption about missing ubiquitin-binding
domains. The malin interaction itself is retained as biology; the separate generic
protein-binding row is removed for lack of informative MF specificity.

Figure 5 concerns adult mouse liver during fasting/refeeding and primary mouse
hepatocytes exposed to defined glucose, serum, glucagon and insulin conditions.
These results do not establish the precise rat biogenic-amine annotations or a
universal human response. Figure 6/discussion leaves a proposed connection to
glycogen repletion/branching unresolved rather than demonstrating a biosynthetic
step.

### STBD1 association and human imaging

The cached full [PMID:24837458](https://pubmed.ncbi.nlm.nih.gov/24837458/),
DOI 10.1042/BSR20140053, uses GDE constructs traced to the prior mouse-Agl paper
and endogenous mouse liver lysate for GST pull-down. Co-IP/pull-down support an
association with STBD1, but are not a purified two-component demonstration of
direct human binding. Tagged GDE can redistribute with overexpressed STBD1 to an
ER-associated compartment. The regulated association measured in Figure 6 is GS;
it is not transferred to GDE. The generic binding row becomes REMOVE without
denying the observed association or asserting a new AGL adapter function.

The live [Human Protein Atlas AGL subcellular page](https://www.proteinatlas.org/ENSG00000162688-AGL/subcellular)
lists supported nucleoplasm as a main location and supported nuclear bodies and
cytosol as additional locations, with antibodies HPA028498/HPA054340. Cytosol is
core. Nuclear observations are NON_CORE because their biochemical role is not
established; this does not imply that HPA used starvation or glycogen-depleting
treatments. Source compartment resolution is preserved.

### Rat donor tracing and access limits

The [MGI Agl ortholog GO evidence view](https://www.informatics.jax.org/homology/GOGraph/Agl)
links the seeded mouse and rat Compara donors to their experiments. Rat
ENSRNOP00000052593/D4AEH9 is the source for SR, carbohydrate binding and three
response terms; mouse ENSMUSP00000044012/F8VPN4 is the source for nucleus,
cytosol, inclusion body, polysaccharide binding and ubiquitin-dependent binding.

| Donor reference | Source evidence recovered | Decision boundary |
| --- | --- | --- |
| [PMID:15180797](https://pubmed.ncbi.nlm.nih.gov/15180797/) | PubMed abstract: rat skeletal-muscle SR fractions contain enzyme protein/activity; association changes with glycogen depletion. | Positive association is real evidence; full-source controls/human transfer remain UNDECIDED. Peripheral association need not imply an integral SR protein. |
| [PMID:6449198](https://pubmed.ncbi.nlm.nih.gov/6449198/) | PubMed metadata and MGI rat carbohydrate-binding IDA; no abstract/full paper recovered. | Original donor assay remains unresolved. Independent human 40593796 supports the glycogen-binding refinement. |
| [PMID:1413626](https://pubmed.ncbi.nlm.nih.gov/1413626/) | PubMed abstract: biogenic-amine effects on glycogen degradation in isolated rat hepatocytes. | Exact nutrient/hormone annotation scope and human transfer remain UNDECIDED without the full study. |
| [PMID:120213](https://pubmed.ncbi.nlm.nih.gov/120213/) | PubMed English abstract: fetal rat liver, pituitary/adrenal manipulations, cortisol repression and growth-hormone induction of enzyme activity. | Full French article unavailable; developmental and tissue restrictions prevent generalizing the glucocorticoid row to human without further review. |

### Granule and extracellular annotations

Live [R-HSA-6798748](https://reactome.org/content/detail/R-HSA-6798748) contains
AGL in both [secretory-granule input set R-HSA-6800970](https://reactome.org/content/detail/R-HSA-6800970)
and [extracellular output set R-HSA-6806526](https://reactome.org/content/detail/R-HSA-6806526).
Likewise [R-HSA-6800434](https://reactome.org/content/detail/R-HSA-6800434)
contains AGL in [ficolin-rich input set R-HSA-6800431](https://reactome.org/content/detail/R-HSA-6800431)
and [extracellular output set R-HSA-6806481](https://reactome.org/content/detail/R-HSA-6806481).
These are verified modeled participants, not accidental mentions in a pathway.

[PMID:23650620](https://pubmed.ncbi.nlm.nih.gov/23650620/), Rørvig et al. (2013),
was recovered as [full original publisher text](https://jlb.onlinelibrary.wiley.com/doi/10.1189/jlb.1212619)
and the Methods, Results and Discussion were read. The experiment fractionates
fresh human neutrophils by nitrogen cavitation/Percoll, pools marker-defined
fractions, and identifies proteins by MS. The discussion cautions that additional
localization/mobilization experiments are needed for inferred compartments.
The AGL-level supplement, jlb0711-sup-0001.zip, could not be retrieved through the
publisher link. Thus the exact luminal topology and secretion evidence remain
UNDECIDED. The previous categorical contamination/artifact claims are withdrawn;
the known cytosolic catalytic pool cannot exclude additional locations.

### Ontology and propagation checks

[AmiGO GO:2001069](https://amigo.geneontology.org/amigo/term/GO:2001069) was read
live: definition **"Binding to glycogen."**, with is_a GO:0030247 polysaccharide
binding, under GO:0030246 carbohydrate binding. This is a same-category ligand
refinement, not binding-to-catalysis substitution. The catalytic cores already
cover glycogen breakdown, so no NEW process or redundant binding row is created.

[ZFIN GO:0031593](https://zfin.org/GO%3A0031593) gives **"Binding to a protein upon
poly-ubiquitination of the target protein."** The local OAK GO database independently
agrees and places it under modification-dependent protein binding. Covalent
modification of Agl itself in a denaturing assay does not establish that function.

Local OAK (`sqlite:obo:go`) was also queried for GO:0043033, GO:0019156 and
GO:0005978. Isoamylase complex is a catalytic complex with a capable_of link to
GO:0019156 isoamylase activity; the substrate definition includes glycogen,
amylopectin and beta-limit dextrins. This is not interchangeable solely by enzyme
nickname with AGL's phosphorylase-limit-dextrin glucosidase activity. The live
[AmiGO isoamylase-activity neighborhood](https://amigo.geneontology.org/amigo/term/GO:0019156)
also exposes the complex link. Direct complex-page access failed; no claim of a
plant-only taxon restriction is made.

GO:0005978 covers formation of glycogen. InterPro:IPR006421 is the metazoan
debranching-enzyme family, not a verified plant-isoamylase contamination. The
mapping's biosynthetic rationale was not recovered. Existing human catalytic work
and pathway models establish breakdown; they do not alone disprove an additional
biosynthetic contribution. This row becomes UNDECIDED pending source evidence.

PAINT cache interpro/panther/PTHR10569/PTHR10569-paint.tsv places both catalytic
terms and glycogen catabolism at PTN000060165. All three IBA annotations remain
ACCEPT with PTN-only source_entities and source-specific comments. Human target
evidence in the descendant set is expected, not circular.

The GO-CAM index has no human P35573 hit. Mouse Agl (MGI:MGI:1924809) appears in
five cached models: 623d156d00000699, 623d156d00000752, 623d156d00000939,
65f3ae5c00002208 and 65f3ae5c00002270. Each contains the two Agl catalytic
activities in cytosolic glycogen catabolism. These were read as curator pathway
models, without treating absence of biosynthesis as proof that no such role is
possible. The live human [transferase event R-HSA-71552](https://reactome.org/content/detail/R-HSA-71552)
and [glucosidase event R-HSA-71593](https://reactome.org/content/detail/R-HSA-71593)
likewise identify AGL [cytosol] as the catalyst in glycogenolysis.

### Validation and follow-up

Gene/schema/reference validation, authored-term validation, source-field equality,
rendering and scaffolded history validation are recorded in the final handoff
manifest. No source cache or provider file was hand-authored. Four missing PMID
caches and three missing Reactome caches remain explicit retrieval tasks before a
fully cached ready review. Unresolved source judgments remain visible in the YAML.
