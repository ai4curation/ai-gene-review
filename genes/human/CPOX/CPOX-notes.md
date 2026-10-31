# CPOX (human) — curation notes

UniProt: P36551 (HEM6_HUMAN). Gene: CPOX (syn. CPO, CPX). HGNC:2321. 454 aa precursor.

Deep research note: falcon deep-research was OUT OF CREDITS (HTTP 402) at review time, so
there is no `CPOX-deep-research-falcon.md`. This review is grounded in the UniProt record
(`CPOX-uniprot.txt`), the seeded GOA (`CPOX-goa.tsv`), and the cached publications listed
below.

## Function (well established)

CPOX is the **oxygen-dependent coproporphyrinogen-III oxidase (EC 1.3.3.3)** that catalyses
the **sixth step of heme biosynthesis**: the aerobic oxidative decarboxylation of the
propionate side chains on rings A and B of coproporphyrinogen III to vinyl groups, forming
protoporphyrinogen IX. Reaction (RHEA:18257): coproporphyrinogen III + O2 + 2 H+ ->
protoporphyrinogen IX + 2 CO2 + 2 H2O.

- [PMID:8159699 "Coproporphyrinogen oxidase (EC 1.3.3.3) catalyzes the sixth step in the heme biosynthetic pathway, the oxidation of coproporphyrinogen III to protoporphyrinogen IX"] — cloning + functional expression in E. coli gave a "17-fold increase in coproporphyrinogen activity over endogenous activity" (EXP evidence for MF).
- UniProt FUNCTION: "Catalyzes the aerobic oxidative decarboxylation of propionate groups of rings A and B of coproporphyrinogen-III to yield the vinyl groups in protoporphyrinogen-IX and participates to the sixth step in the heme biosynthetic pathway."
- Human enzyme is uniquely **oxygen-dependent** (aerobic CPO family); anaerobes use HemN (radical-SAM, unrelated).

## Localization

Mitochondrial **intermembrane space**, associated with the inner membrane. Human localization
to the IMS is inferred from the homologous rat enzyme (Reactome; UniProt ISS from Q3B7D0).
- [PMID:8407975 "mammalian coproporphyrinogen oxidase is mitochondrial enzyme"] — activity mainly in mitochondria of transfected cells.
- HPA IDA (GO_REF:0000052) and mitochondrial-proteome MS (PMID:34800366) both place it in mitochondrion.

## Structure / subunit

Functions as a **homodimer**. Crystal structure (PDB 2AEX, 1.58 Å) solved; metal- and
cofactor-independent mechanism.
- [PMID:16176984 "In the biologically active dimer (K(D) = 5 x 10(-7) M), one monomer rotates relative to the second by approximately 40 degrees"] — IDA for protein homodimerization; residues 392–418 (exon 6) needed for dimerization; K404E harderoporphyria mutation impairs 2nd decarboxylation cycle.

## Disease

- **Hereditary coproporphyria (HCP; MIM 121300)** — acute hepatic porphyria; many missense/deletion mutations catalogued (e.g. PMID:9888388, systematic mutation update).
- **Harderoporphyria (HARPO; MIM 618892)** — rare erythropoietic variant; homozygous H327R (PMID:21103937) or K404E (PMID:7757079).

## GOA review summary

Core, strongly supported:
- MF GO:0004109 coproporphyrinogen oxidase activity (EXP/IDA/IBA/IEA/TAS) — ACCEPT.
- BP GO:0006783 heme biosynthetic process (IBA/IEA/TAS) — ACCEPT.
- CC GO:0005758 mitochondrial intermembrane space (ISS/TAS/IEA) — ACCEPT; GO:0005739 mitochondrion (IDA/HTP/TAS) — ACCEPT.

Reasonable but broader / peripheral:
- GO:0006779 porphyrin-containing compound biosynthetic process — broader parent of heme biosynthesis; KEEP_AS_NON_CORE.
- GO:0006785 heme B biosynthetic process (IDA from PMID:7987309) — heme b IS the product of this pathway; the cited paper is gene-organization/exon-6 skipping, an odd choice for a heme-b IDA, but the biology is correct; KEEP (heme b is the specific heme made via protoporphyrin IX). Keep as accurate downstream process; not the most direct term (protoporphyrinogen IX biosynthesis is more direct) — MARK non-core.
- GO:0005737 cytoplasm (IBA is_active_in) — IMS is the accurate compartment; cytoplasm is too broad/imprecise for this mito-IMS enzyme; MARK_AS_OVER_ANNOTATED.
- GO:0005743 mitochondrial inner membrane (IEA/Ensembl ortholog) — CPO is IMS-associated with inner membrane; plausible but the primary curated location is IMS; KEEP_AS_NON_CORE.
- GO:0016020 membrane (IEA/Ensembl) — uninformative broad CC; MARK_AS_OVER_ANNOTATED.

Ortholog-transferred stress/metal responses (all IEA from rat/mouse ortholog via Ensembl,
GO_REF:0000107) — response to iron ion, lead ion, insecticide, arsenic, methylmercury. These
are electronic transfers of environmental/toxicant response phenotypes from the rodent
ortholog; they are peripheral and not demonstrated for human CPOX; KEEP_AS_NON_CORE
(they are plausible ortholog transfers, not clearly wrong, so not REMOVE).

- GO:0042802 identical protein binding (IEA/Ensembl) — CPO is a homodimer, so identical
  protein binding is biologically true; but "identical protein binding" is a weak binding
  term. There is a directly supported, more informative IDA term GO:0042803 protein
  homodimerization activity from PMID:16176984. MODIFY GO:0042802 -> GO:0042803.
- GO:0042803 protein homodimerization activity (IDA PMID:16176984) — ACCEPT (directly shown
  by crystallography/AUC). Non-core relative to catalysis but well supported.


## 2026-10-12 — source reconciliation and functional reassessment

The assessment below supersedes the earlier action rationale where it differs; the historical journal above is retained. The two products remain distinct. The canonical precursor is 454 residues, with the official mature chain at 111–454. The 287-residue alternative product replaces canonical residues 272–287 and deletes 288–454. Its sequence is exactly reconstructable from the two UniProt VSP records, but equivalent import, dimerization and catalytic activity are not established.

### Catalysis and pathway scope

The integrated core is oxygen-dependent coproporphyrinogen oxidase activity in heme-B biosynthesis, principally in the mitochondrial intermembrane space. CPOX performs the oxidative decarboxylations itself; an upstream catalytic step belongs to the pathway and is not merely a consumed substrate. The original human-expression paper reports “a 17-fold increase in coproporphyrinogen activity over endogenous activity” ([PMID:8159699](https://pmc.ncbi.nlm.nih.gov/articles/PMC43507/), Results and Table 1). Its historical putative-mature GST construct and uncertain initiation site must not be equated to the full current precursor. Human solution and structural work supports the homodimer ([PMID:16176984](https://pmc.ncbi.nlm.nih.gov/articles/PMC1224704/)); its radical/carbanion mechanism is proposed, not settled.

The heme-B IDA from PMID:7987309 is retained with explicit curator deference and independent catalytic support. Its abstract describes gene structure and exon skipping; the full original was not recovered. That access limit does not establish miscitation. The old proposed GO:0006782 addition is withdrawn because the actual current ontology marks it obsolete. Broad ancestral heme biosynthesis and conservative electronic pathway mappings remain valid, while the source-specific human-expression process can be refined to heme B. The existing GO-CAM already models human CPOX as an enzyme in that pathway.

The new mouse-derived heme-A assertion remains UNDECIDED. Actual indexed Methods and Results of [PMID:8407975](https://pubmed.ncbi.nlm.nih.gov/8407975/) establish bovine purification and mouse MCPO-1 expression in COS-1 cells, with protoporphyrinogen formation and mitochondrial activity. They do not resolve the heme-A-specific curation premise. This is uncertainty about pathway specificity, not a claim that lack of a heme-A assay disproves upstream participation. The authors also did not directly test the recombinant enzyme's intermembrane-space localization.

### Compartments and physiological context

The earlier cytoplasm over-annotation rationale was too restrictive: the current term includes organelles. The actual PAINT ancestral assertion is on the human tree path, and the human aligned sequence matches the canonical sequence exactly. A target-level refinement to intermembrane space adds precision without declaring the node wrong or asserting exclusive localization.

The original rat fractionation paper describes “a fraction loosely bound to the inner membrane” ([PMID:31872](https://pmc.ncbi.nlm.nih.gov/articles/PMC1186208/), abstract and Results/Tables 1–4, pp. 97–100). All six original scanned pages were read, with Table 3/4 pixels checked. Salt/alkaline release and sonication support peripheral association; proposed substrate transfer to PPOX is a model. This does not assert integral topology. Human MitoCoP classifies the CPOX group as soluble under its specific extraction conditions, which can coexist with the rat peripheral-association result.

The mouse membrane transfer has positive target evidence: original [PMID:20080761](https://pmc.ncbi.nlm.nih.gov/articles/PMC2818953/), Table 1, explicitly lists P36552 CPOX in Atg7-null erythrocyte membrane preparations. The full main Results, Discussion and Methods were read. This supports contextual fraction detection, not a CPOX-mediated autophagy mechanism or plasma-membrane topology.

Authentic MitoCoP Table S1 identifies CPOX in `(A) All protein groups`, row 262, and `(B) MitoCoP (1,134 genes)`, row 237 ([PMID:34800366](https://pmc.ncbi.nlm.nih.gov/articles/PMC8664129/)). Subtractive class 1, spatial cluster 1 and importomics class 1 support mitochondrial localization. The group contains P36551, P36551-2 and two unreviewed accessions, so it does not resolve individual products. Inherited compartment-annotation columns are distinguished from measured enrichment and extraction results. Official HPA immunofluorescence metadata also supports the principal mitochondrial location, with antibody/cell-line differences retained.

Rat iron, lead, insecticide, arsenic and methylmercury source records are retained as non-core exposure-associated enzyme responses. Current response definitions include changes in enzyme activity. Actual lead-paper Methods/Results/Discussion were read; the other complete abstracts and literal donor records support their narrower scope. Insecticide effects concern the diazinon/isodiazinon condition; the stabilized-diazinon control differs. Metal effects differ between kidney and liver. These are not direct human experiments or evidence for a dedicated sensing/detoxification mechanism ([PMID:2289051](https://pubmed.ncbi.nlm.nih.gov/2289051/), [PMID:656697](https://pmc.ncbi.nlm.nih.gov/articles/PMC1668043/), [PMID:6626236](https://pubmed.ncbi.nlm.nih.gov/6626236/), [PMID:2916235](https://pubmed.ncbi.nlm.nih.gov/2916235/)).

### Lens evidence and unresolved structure

The current mouse donor for structural constituent of eye lens is an IMP assertion citing [PMID:12470976](https://pubmed.ncbi.nlm.nih.gov/12470976/). Only its complete abstract was accessible after bounded publisher attempts; it maps the Nakano cataract locus and modifiers. The later original [PMID:23631845](https://soar-ir.repo.nii.ac.jp/record/3707/files/Hereditary_cataract_Nakano_mouse.pdf) establishes Cpox R380L, reduced catalytic activity, porphyrin accumulation and wildtype-Cpox transgene rescue. Its authors state: “The mechanisms by which impairment of CPOX leads to lens opacity in the NCT are elusive.” The complete main Methods, Results and Discussion were read from the author manuscript. Those positive findings do not yet distinguish a structural moonlighting role from metabolic protection of lens transparency. The human structural-function transfer remains UNDECIDED, without denying the mouse physiology or alleging a wrong gene.

### Source provenance

The historical 26 assertion objects are preserved. Twenty-five match current sources uniquely, with 15 historical WITH/FROM omissions left untouched. Five newly seeded source assertions are added verbatim. The old GO_REF:0000044 intermembrane-space row is marked retired only because the current source grouping uses combined IEA; its biological judgment remains positive. The union therefore has 31 rows, 30 active. Complete current objects, literal donor records, product reconstructions, actual PAINT paths, rule predicates, original table projections and access limits are in [the source evidence](CPOX-source-evidence.yaml). No new biological assertion is proposed. All previous reference identities and findings are retained.

## 2026-10-12 — Source-specific evidence clarification

The human catalytic evidence has distinct experimental scopes. [PMID:8159699](https://pmc.ncbi.nlm.nih.gov/articles/PMC43507/), original Methods and Table 1, compares human putative-mature cDNA expression with controls; [PMID:9888388](https://pubmed.ncbi.nlm.nih.gov/9888388/) reports functional loss after expression of selected human disease variants in its accessible abstract. The separate PMID:7987309 IDA remains supported by curator deference and independent catalysis; its original assay sections remain unavailable. Current PAINT ancestry, ARBA predicates, InterPro signatures, EC classification and RHEA reaction mapping are distinguished in their own source comments.

The porphyrin-containing-compound biosynthesis annotation remains ACCEPT: it is a correct broader description of the same central pathway reaction. A more specific heme-B term in the compact core does not convert its existing ancestor annotation into a peripheral function. The retired intermembrane-space row retains a positive biological judgment because retirement concerns the replaced source grouping, not a loss of that compartment.

The exact original mouse [Table 1](https://pmc.ncbi.nlm.nih.gov/articles/PMC2818953/#T1) identifies P36552 among mitochondrial proteins in Atg7-null erythrocyte ghosts. That target row is absent from the normal cached article text and is now exposed as literal cells with the original HTML hash in [the source evidence](CPOX-source-evidence.yaml). It is fraction-detection evidence, not a membrane-attachment discriminator: retained mitochondrial material can account for the ghost result. The separate rat [PMID:31872](https://pmc.ncbi.nlm.nih.gov/articles/PMC1186208/), pp. 99–100, alkaline/salt release and sonication, provides positive peripheral inner-membrane-association evidence. Intermembrane space and the membrane bilayer are distinct compartments.

Human MitoCoP evidence remains inspectable as the original Table S1 full headers and CPOX group rows A262/B237 in the source evidence, linked to [the primary article and supplementary workbook](https://pmc.ncbi.nlm.nih.gov/articles/PMC8664129/#appsec1). The group contains multiple accessions and does not identify an isoform-specific function. HPA evidence comes from the [official CPOX XML](https://www.proteinatlas.org/ENSG00000080819.xml): the supported principal mitochondrial annotation and antibody/cell-line differences are metadata reads, not a new image interpretation.

The preceding heme-A UNDECIDED assessment is superseded by KEEP_AS_NON_CORE. The [complete exact-term QuickGO query](https://www.ebi.ac.uk/QuickGO/services/annotation/search?goId=GO%3A0006784&goUsage=exact&taxonId=9606%2C10090%2C10116&taxonUsage=exact&limit=200&page=1), captured 2026-10-12, contains 73 human/mouse/rat records, including experimental mouse annotations for Alad, Hmbs, Uros, Urod, Ppox, Fech, Alas1 and Cpox. These are observations of current annotation practice, not new reads of each comparator paper. They resolve the proposed terminal-enzyme-only interpretation of the pathway. The actual mouse activity experiment in [PMID:8407975](https://pubmed.ncbi.nlm.nih.gov/8407975/) establishes upstream chemical work; it does not measure heme A or make CPOX a terminal heme-A synthase. The single core remains heme-B biosynthesis.

Lens structural activity remains UNDECIDED. The current donor is real, but the original 2002 full text remains unavailable. Later hypomorphic enzyme activity, porphyrin accumulation and transgene rescue establish a lens phenotype; they do not distinguish metabolic protection from a second structural function. The membrane annotation remains non-core using the separately evidenced rat association, not an assumption that the mouse ghost experiment alone demonstrates attachment. The rat authors also report failure to retain binding on isolated membranes (PMID:31872, Discussion, p. 102), so the biochemical context is retained explicitly.
