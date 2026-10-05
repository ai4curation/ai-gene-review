# CD320 (Q9NPF0) review notes

CD320 antigen = transcobalamin receptor (TCblR), aka 8D6 antigen / FDC-signaling molecule 8D6.
Single-pass type I plasma-membrane glycoprotein (282 aa; signal 1-35, extracellular 36-229,
TM 230-250, cytoplasmic 251-282). Member of the LDLR family: two LDLR class A (LDLR-A) domains
(53-90, 131-168) separated by an EGF/complement-like cysteine-rich region. Non-enzymatic.

## Core biology
- Cell-surface receptor that captures transcobalamin-bound cobalamin (holo-TC / TC-Cbl) from
  plasma and internalizes it by receptor-mediated endocytosis, supplying cobalamin (vitamin B12)
  to cells throughout the body; the only physiologic route for TC-bound Cbl uptake.
  [PMID:18779389 "The transcobalamin (TC, TCII) receptor (TCblR) on the plasma membrane binds TC- cobalamin (Cbl) and internalizes the complex by endocytosis"]
  [PMID:20524213 "TCblR expressed on the plasma membrane binds transcobalamin (TC) saturated with Cbl (holo-TC) and mediates cellular uptake of Cbl"; "The only route for physiologic transport of TC-bound Cbl into cells is via TCblR"]
- Uptake is Ca2+-dependent; each LDLR-A domain binds a central Ca2+ ion.
  [PMID:27411955 "transcobalamin (TC)-bound Cbl is transported into cells by receptor-mediated endocytosis, which requires Ca2+-dependent complex formation of TC with its cognate cell surface receptor CD320"]
  [PMID:27411955 "Both LDLR-A domains contain central Ca2+ ions bound by four conserved acidic residues and two backbone carbonyls in an octahedral coordination"]
- Expression is coupled to cell cycle; highest in actively proliferating cells and upregulated
  in cancer cells (drug-delivery target). [PMID:20524213; PMID:27411955]
- Binds TC with high affinity/specificity (KD ~1.5 nM); does NOT bind haptocorrin. [PMID:27411955]
- Ligand released at endosomal low pH; receptor recycles to plasma membrane. [PMID:27411955; Reactome R-HSA-3000112]

## Disease
- CD320-related transient/mild methylmalonic aciduria (MATR / MMATC; MIM:613646), autosomal
  recessive, detected on newborn screening. Common in-frame p.E88del (loss of Glu88 in LDLR-A1)
  decreases cobalamin-transport function; most patients clinically asymptomatic.
  [PMID:20524213 "identified a homozygous single codon deletion, c.262_264GAG (p.E88del) ... Inserting the codon by site-directed mutagenesis fully restored TCblR function"]
  UniProt DISEASE MATR; variants E88del, R129L, S142G, G220R.

## Immunology (historic first description; likely secondary/over-annotated)
- First cloned as "8D6 antigen" on follicular dendritic cells (FDCs); mAb 8D6 blocks FDC-mediated
  costimulation of germinal-center B-cell growth. [PMID:10727470]
- FDC-SM-8D6 augments plasma-cell generation from CD27+ precursors. [PMID:11418631]
  These immune roles predate the identification of the B12-receptor function and are plausibly
  downstream of proliferation-coupled B12 supply; kept as non-core. The Growth-factor keyword
  (UniProt-KW -> GO:0008083) derives from this 8D6/FDC work but CD320 is a membrane receptor,
  not a secreted growth factor -> not brought in.

## Interactions
- TCN2 (P20062): the physiological ligand; structural + IntAct evidence. [PMID:27411955]
- JAML/AMICA1 (Q86YT9): CD320-JAML pair from a large immune surface-interactome screen; CD320
  facilitates NK-cell activation in that assay. [PMID:35922511] Secondary immune adhesion role.

## GOA term choices (current labels verified against local go.db)
- GO:0038024 cargo receptor activity (MF) — core
- GO:0031419 cobalamin binding (MF) — core (binds Cbl via the TC-Cbl complex)
- GO:0015889 cobalamin transport (BP) — core
- GO:0006898 receptor-mediated endocytosis (BP) — core mechanism
- GO:0005886 plasma membrane (CC) — core location
- GO:0005509 calcium ion binding (MF) — accept (structural, LDLR-A Ca2+ sites)
- GO:0005783 endoplasmic reticulum — LIFEdb GFP overexpression artifact; over-annotated
- GO:0016020 membrane — accept but generic (subsumed by plasma membrane)
- GO:0005515 protein binding — uninformative; TCN2 IPI captured by cargo-receptor/cobalamin-binding MF; JAML IPI is a secondary immune interaction
</content>


## 2026-10-05 reassessment (supersedes historical interpretations above)

The original journal is preserved verbatim above. The reassessment below supersedes the earlier cobalamin-binding core claim, the unsupported ER-artifact explanation, and mechanistic interpretations linking the immune phenotypes or JAML association to a particular pathway. The current evidence and remaining uncertainties are recorded here.

## Scope and source provenance

This review reassesses the existing human CD320 review for the ClinGen Mendelian campaign. The frozen inventory identifies HGNC:16692, reviewed UniProt Q9NPF0 and the autosomal recessive, Definitive association with transcobalamin receptor defect (MONDO:0013341). It does not authorize a new clinical severity classification. The 282-residue protein and two recorded UniProt products are preserved. No isoform-specific activity is inferred for Q9NPF0-2.

The immutable GOA contains 23 rows representing 22 distinct assertions. The duplicate TCN2-binding assertion differs only in date and assigning source. Normal `seed-goa --no-fetch-titles` restored missing supporting-entity lists on six annotations in temporary storage, adding no annotations. All source IDs, evidence codes, qualifiers and ordered partners remain intact. Existing sources and the cobalamin module are protected; this review does not edit the module or generated source caches.

The normal deep-research recipe was attempted with falcon and the perplexity-lite fallback. Both stopped at dependency resolution because the pinned deep-research-client 0.2.7rc1 was unavailable in the offline environment. No provider report was produced or authored manually. The research here uses existing publications and selected original online text, with access limits below.

## Nutrient uptake and ligand specificity

[PMID:18779389](https://pubmed.ncbi.nlm.nih.gov/18779389/) identifies the human placental receptor by peptide sequencing and connects it to CD320. The locally cached abstract is supplemented by selected original [Methods and Results](https://pmc.ncbi.nlm.nih.gov/articles/PMC2614632/): binding assays use radiolabeled cobalamin already carried by transcobalamin; receptor antibodies inhibit binding and uptake; human HEK293 transfection increases uptake. A mouse ES-cell allele experiment is separately supporting evidence. The entire online paper and figure pixels were not inspected; a later PMC request encountered a browser challenge.

[PMID:15652495](https://pubmed.ncbi.nlm.nih.gov/15652495/) is the earlier receptor-characterization study. Its abstract is available, but the full 2005 methods were not accessed. It precedes definitive gene identification and distinguishes a functional 58-kDa receptor candidate from a competing preparation. The 2009 paper supplies the gene identification that makes the older functional evidence interpretable.

[PMID:27411955](https://pubmed.ncbi.nlm.nih.gov/27411955/) provides the human TC-CD320 ectodomain structure, calcium coordination and ligand-affinity measurements. Selected cached Results, Discussion, expression/purification and binding methods were inspected. Human constructs were expressed in insect cells; these are not intact-cell transport measurements. Receptor contacts lie on transcobalamin, whereas the vitamin is carried within transcobalamin. Acidic pH lowers affinity in vitro; this is consistent with ligand release during uptake but does not directly demonstrate receptor recycling in cells.

The existing experimental cobalamin-binding assertion is retained as UNDECIDED. The inspected assays establish binding of the carrier-vitamin complex; direct receptor-vitamin contact and the intended ontology scope remain unresolved. Official QuickGO/OLS term API access failed. The local ontology cache confirms the term label but lacks its definition. No assertion of an experimental error or demonstrated absence of free-vitamin binding is made. A separate cobalamin-binding core entry would overstate what was established, so the synthesis has one cargo-receptor core function. Calcium coordination is a well-supported receptor structural feature, not a separate calcium-signaling function.

## Human variant evidence

[PMID:20524213](https://pubmed.ncbi.nlm.nih.gov/20524213/) reports reduced holo-transcobalamin uptake in patient fibroblasts and rescue after restoring the deleted codon in the patient cDNA. Selected original Methods and Results were read. The early patient series does not justify a broad prediction of lifelong clinical severity. The later purified deletion-mutant ectodomain retained high ligand affinity (PMID:27411955), so cellular uptake impairment cannot simply be equated with complete failure of carrier binding. Regulation, trafficking and assay context remain mechanistic questions.

## Immune contexts and localization

[PMID:10727470](https://pubmed.ncbi.nlm.nih.gov/10727470/) establishes the original 8D6/CD320 molecule using human FDC/HK cells, antibody staining and expression cloning. The cached abstract and selected Methods/Results support B-cell costimulation under CD40 and cytokine stimulation. Antibody controls and transfected COS cocultures strengthen the observation. These two existing process annotations are kept as non-core; neither an intrinsic growth-factor activity nor a resolved downstream mechanism is inferred. [PMID:11418631](https://pubmed.ncbi.nlm.nih.gov/11418631/) provides complementary 8D6/B-cell differentiation evidence, but only its cached abstract was available.

[PMID:35922511](https://pubmed.ncbi.nlm.nih.gov/35922511/) uses recombinant extracellular-protein screening and mixed-leukocyte phenotyping. The GOA row and immutable UniProt entry identify JAML as the CD320 partner. The target-specific supplementary pair record was not independently inspected; the curated association is retained with that limit. Soluble-CD320 phenotypes do not establish a JAML-specific signaling pathway. The official [2024 correction](https://www.nature.com/articles/s41586-024-07928-6) concerns a figure label, a concentration unit and missing single-cell dataset references, without retracting the interaction study.

[PMID:19946888](https://pubmed.ncbi.nlm.nih.gov/19946888/) describes membrane proteomics in the human NK-like YTS line. Its abstract was read; its target-specific table was not. The broad experimental membrane assignment is retained as non-core without converting that fractionation into a more precise experiment. By contrast, the broad ARBA membrane prediction can be refined using independent target-specific evidence. This deliberate distinction accounts for the validator's inconsistent-action advisory.

The [LIFEdb GO reference](https://geneontology.org/GO_REF/0000054.html) describes microscopic curation of GFP-fusion localization. The CD320-specific image and construct were not obtained. The ER assertion therefore remains UNDECIDED. Secretory transit or a fusion artifact must not be treated as demonstrated explanations without inspecting that record.

The four cached Reactome summaries were read. They support carrier capture, uptake and pathway location, without making CD320 an intracellular cobalamin-processing enzyme. The local GO-CAM index search found no CD320/Q9NPF0 entry; no absence-based new annotation is proposed.

## Decisions and validation

All 22 source assertions were reassessed: 13 ACCEPT, three MODIFY, four KEEP_AS_NON_CORE and two UNDECIDED. There are no NEW assertions, 17 reference assessments, two preserved protein products and one core function. The three refinements specify plasma membrane, receptor-mediated endocytosis and cargo receptor activity. The generic JAML interaction remains non-core under the project's standing treatment of supported associations.

Temporary normal validation passes with two advisories: the generic protein-binding association and the deliberate evidence-specific action difference for membrane. DRAFT follows these advisory conditions; it is distinct from the two unresolved biological/source questions. Whole independent scientific review and canonical application remain subsequent steps.
