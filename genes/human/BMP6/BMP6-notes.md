# BMP6 review notes

## 2026-10-02: source-based annotation review

BMP6/P22004 is a secreted BMP-family ligand. The review separates its receptor-binding and signaling role from receptor kinase activity, SMAD transcriptional activity, and erythroferrone-mediated ligand sequestration. One core function describes extracellular growth-factor signaling, including hepcidin-dependent systemic iron regulation. Bone, pancreatic, adrenal and vascular responses are recorded as tissue-specific consequences.

The 81 original annotation objects are preserved, including their evidence codes, source references, supporting entities and the cytokine `contributes_to` qualifier. The proposal contains 26 ACCEPT, 36 KEEP_AS_NON_CORE, 2 MODIFY and 17 UNDECIDED decisions. No annotation is added or removed. The two modifications refine supported receptor interactions to the existing GO:0070700 BMP receptor binding term. Their source mouse receptor accessions remain unchanged.

The disease association remains the project snapshot's **Limited** autosomal-dominant susceptibility to iron overload. Established physiological gene function does not establish pathogenicity of every reported allele. No clinical reclassification is made.

## Signaling and ligand complexes

[PMID:31800957](https://pubmed.ncbi.nlm.nih.gov/31800957/) was assessed from primary indexed main Methods/Results and the PubMed figure captions. The normal cached record is citation-only despite the presence of experimental content online. The main Results explicitly describe BMP6 binding to ALK3 and ALK2 as positive controls. Mouse BMPR1A/P36895, ACVR1/P37172 and ERFE/Q6PGN1 remain the source partners. Receptor binding is distinguished from receptor-knockdown effects on hepcidin. The supplementary reagent table, original images and complete supplement were not inspected.

Existing GO-CAMs [BMP6](../../../gocams/66e382fb00001606/66e382fb00001606-src.yaml) and [BMP2/BMP6](../../../gocams/66e382fb00001786/66e382fb00001786-src.yaml) were consulted at their relevant activity nodes. The second model represents BMP6 and BMP2 as parts of a complex contributing cytokine activity. Both connect signaling with iron homeostasis. This supports retaining the complex qualifier and avoids an inference that extracellular location precludes participation in an iron-regulatory process. Recombinant heterodimer activity does not prove obligatory endogenous heterodimer composition. These are curator interpretations, not additional independent experiments.

[PMID:30097509](https://pubmed.ncbi.nlm.nih.gov/30097509/), cached abstract, provides cell-free competition and signaling evidence for ERFE interaction. The two broad ERFE binding annotations are retained outside the core function because the interaction is supported and no defensible more specific BMP6 activity term was established.

For [PMID:7811286](https://pubmed.ncbi.nlm.nih.gov/7811286/), the exact historical BMP6 reagent and heterodimer assay remain inaccessible from the abstract. Correct receptor-binding and heterodimer functions are retained with explicit curator deference and independent corroboration from PMID:31800957. The paper's BMP2/BMP4-focused title is not evidence of misattribution.

[PMID:19366699](https://pubmed.ncbi.nlm.nih.gov/19366699/) contains an explicit BMP6 Smad1/5 response in its cached Discussion. The cache has Abstract and Discussion despite its full-text flag. Earlier indexed primary Methods/Results also identified recombinant human BMP6 treatment of pulmonary artery endothelial cells. Neither reading establishes an independent inspection of all figures or supplementary experiments.

## Tissue-specific responses

[PMID:18436533](https://pubmed.ncbi.nlm.nih.gov/18436533/): cached Methods and selected Results establish recombinant BMP6 treatment of primary human mesenchymal cells, osteoblast markers, mineralization and receptor-dependent signaling. Receptor preferences in this cell type should not be generalized to all tissues.

[PMID:26598555](https://pubmed.ncbi.nlm.nih.gov/26598555/): cached Results and selected Methods describe human BMP6 stimulation of HUVECs, permeability measurements, VE-cadherin internalization and junction changes, with ALK2/SRC perturbation and SMAD/ID1 readouts. BMP6 initiates the response; cellular kinases and adhesion machinery execute the downstream events. Complete supplements were not reviewed.

[PMID:16527843](https://pubmed.ncbi.nlm.nih.gov/16527843/), cached abstract: BMP6 augments angiotensin-II-dependent CYP11B2 expression and aldosterone output in human H295R cells; potassium-induced output is distinguished. [PMID:15516325](https://pubmed.ncbi.nlm.nih.gov/15516325/) reports proliferation and bone-related expression in human periodontal ligament cells, with limited resolution of secretion versus synthesis in the abstract.

[PMID:11865031](https://pubmed.ncbi.nlm.nih.gov/11865031/) uses fetal mouse pancreatic cultures and laminin-1. [PMID:8089189](https://pubmed.ncbi.nlm.nih.gov/8089189/) uses murine BMP6-expressing CHO tumors in mice. [PMID:16798745](https://pubmed.ncbi.nlm.nih.gov/16798745/) measures skeletal effects of systemic BMP6 in ovariectomized rats. These abstract-based assessments preserve experimental species and gain-of-function context.

## Iron regulation and unresolved evidence

[PMID:18326817](https://pubmed.ncbi.nlm.nih.gov/18326817/), cached abstract, supports endogenous BMP6 as an HJV-dependent ligand in hepatoma-derived cells. [PMID:26582087](https://pubmed.ncbi.nlm.nih.gov/26582087/) combines human variant observations with secretion, signaling and hepcidin assays for selected constructs. The other variant cohorts, [PMID:28335084](https://pubmed.ncbi.nlm.nih.gov/28335084/) and [PMID:32464486](https://pubmed.ncbi.nlm.nih.gov/32464486/), are not treated as comprehensive functional validation of all reported alleles.

[PMID:29695288](https://pubmed.ncbi.nlm.nih.gov/29695288/) was also read from the publisher's main scientific text in the preliminary research. Its p.Q118dup localization and secretion results do not independently test every signaling endpoint or other propeptide substitutions. The annotation to intracellular iron homeostasis remains UNDECIDED because the precise evidence-to-process connection needs clarification. The separate PMID:31800957 row retains its curated signaling/hepcidin context; this source-specific difference is deliberate.

[PMID:16886151](https://pubmed.ncbi.nlm.nih.gov/16886151/) supplies an accessible association abstract, insufficient here to resolve a direct immune-response role. Other UNDECIDED rows identify uninspected donor experiments for specific developmental, stimulus-response or localization assertions. They are not claims that those annotations are false. PAINT assertions are assessed as phylogenetic curator judgments, without treating donor count or the target's presence among evidence as circularity.

## Workflow and checks

Normal source files and publication caches were imported unchanged from authenticated fetch outputs. Existing variant caches and family files were preserved. The standard `just deep-research-falcon human BMP6 --fallback perplexity-lite` invocation failed during dependency resolution before either provider ran. No provider-labelled research file was authored manually. These notes and the explicit source-access statements document the manual research instead.

The TMP proposal passed data-model validation, an exact comparison of all 81 non-review annotation objects, and independent source-substring checks for six short excerpts. A distinct annotation and core-function reviewer assessed the decisions and synthesis, verified preservation of the source objects, and corrected nine rat-donor descriptions before canonical application. Normal gene validation, HTML rendering and a scaffolded history record are performed after that review.

## 2026-10-02: first review follow-up

The follow-up retains all 81 source annotation objects and distinguishes two related molecular activities: BMP receptor binding and experimentally demonstrated BMP2/BMP6 heterodimer formation contributing cytokine activity. The latter is a recombinant capability; obligatory endogenous assembly is not established. The review now records 26 ACCEPT, 45 KEEP_AS_NON_CORE, 2 MODIFY, 1 MARK_AS_OVER_ANNOTATED and 7 UNDECIDED decisions. No source annotation is added or removed. This section supersedes the initial action counts and the earlier unresolved assessment of PMID:29695288.

The complete available main text of [PMID:29695288](https://pubmed.ncbi.nlm.nih.gov/29695288/) describes variant genotyping and BMP6 localization/secretion assays. These do not directly measure the annotated intracellular iron-homeostasis response. That source-specific IDA assignment is now marked over-annotated; the established wildtype BMP6–hepcidin function and other iron-regulation annotations remain supported. A benign variant result does not refute wildtype function.

Twelve additional normal publication caches were read. Ten contain abstracts only, including two with PMC identifiers whose full text was not recovered. [PMID:19191909](https://pubmed.ncbi.nlm.nih.gov/19191909/) has an HTML extraction, read through its main Methods, Results and Discussion. [PMID:27647829](https://pubmed.ncbi.nlm.nih.gov/27647829/) has an XML extraction; relevant Methods and BMP6-specific Results were read alongside a previously accessed primary Figure 7 caption. Figure images and complete supplements were not inspected. Source-cache availability is recorded independently of the reading scope.

The macrophage study establishes BMP6-dependent iNOS/TNF-alpha induction in murine RAW264.7 cells with receptor perturbations. Its primary mouse macrophage and human THP-1 confirmation concerns proliferation and receptor expression; the entire mouse cell-line mechanism is not assigned to human cells. The airway study [PMID:12151307](https://pubmed.ncbi.nlm.nih.gov/12151307/) supplies expression/signaling context, not an isolated BMP6 airway perturbation.

The BMP9-titled endothelial paper contains a separate BMP6 experiment: pretreatment enhances adhesion-molecule expression after LPS. Its BMP9-specific receptor, neutrophil-recruitment and in-vivo experiments are kept separate. Likewise, the BMP6 arm of [PMID:20406889](https://pubmed.ncbi.nlm.nih.gov/20406889/) measures increased cell yield in mouse VEGFR2-positive progenitors. Proliferation is retained, while the separate differentiation claim remains unresolved. [PMID:17119124](https://pubmed.ncbi.nlm.nih.gov/17119124/) independently supports BMP6-induced endothelial proliferation and angiogenic responses through Cox2.

For [PMID:17030628](https://pubmed.ncbi.nlm.nih.gov/17030628/), BMP6 stimulation and downstream MSX-dependent repression are distinct experimental layers. The ligand contributes to regulation without itself binding DNA. The observed mouse donor for some transferred regulation terms is [PMID:19252488](https://pubmed.ncbi.nlm.nih.gov/19252488/); that paper's preserved inflammatory hepcidin induction does not establish equal absolute expression or refute every positive BMP6 effect. The new papers are identified as corroboration where they are not the original donor citation.

The organ-development annotations associated with [PMID:16154126](https://pubmed.ncbi.nlm.nih.gov/16154126/) are retained with explicit deference to MGI's Bmp7/Bmp6 complementation curation. The abstract foregrounds BMP4, and neither the exact chimera boundaries nor the organ-specific assay details were independently recovered. This is an access limit, not a wrong-gene finding.

[PMID:9202223](https://pubmed.ncbi.nlm.nih.gov/9202223/) provides functional antisense/rescue evidence that BMP6 participates in a glucocorticoid-induced osteoblast response. The independently located retinoic-acid, magnesium and mechanical-stimulation studies ([PMID:8385738](https://pubmed.ncbi.nlm.nih.gov/8385738/), [PMID:21736832](https://pubmed.ncbi.nlm.nih.gov/21736832/), [PMID:23198877](https://pubmed.ncbi.nlm.nih.gov/23198877/)) document expression changes without resolving the exact historical RGD transfer chains. Those specific annotations remain UNDECIDED. Vesicle localization also remains unresolved; secretory transit neither verifies nor disproves the original location assay.

Supported generic ERFE interactions remain non-core under the standing project instruction to retain correct interactions when no justified more specific replacement describes the assertion. A cofactor or receptor activity is not substituted merely to avoid a generic-binding warning. Source files, qualifiers and original partner accessions remain unchanged.
