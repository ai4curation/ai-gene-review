# AGL (Glycogen debranching enzyme, GDE) — review notes

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
