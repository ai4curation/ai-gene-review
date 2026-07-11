# CERS1 (ceramide synthase 1 / LASS1 / UOG1) — review notes

UniProtKB: P27544. HGNC:14253. Gene on chr19; bicistronic with GDF1.

## Core biology (grounded in UniProt P27544 + cached publications)

CERS1 is the C18-specific ceramide synthase. It catalyzes N-acylation of a sphingoid
long-chain base (sphinganine in de novo synthesis; sphingosine in the salvage pathway)
using acyl-CoA, forming dihydroceramide / ceramide. It is highly selective for
stearoyl-CoA (C18:0-CoA), producing C18-(dihydro)ceramide.

- Enzyme / MF: sphingosine N-acyltransferase activity (GO:0050291). EC 2.3.1.24 and the
  newer sphingoid-base N-stearoyltransferase EC 2.3.1.299. UniProt P27544 CATALYTIC
  ACTIVITY lists RHEA reactions incl. sphinganine + octadecanoyl-CoA ->
  N-(octadecanoyl)-sphinganine (RHEA:36547) and sphing-4-enine + fatty acyl-CoA
  (RHEA:23768).
  - "N-acylation of a sphingoid long-chain base by a family of ceramide synthases (CerS),
    each of which displays a high specificity towards acyl CoAs of different chain lengths"
    [PMID:17977534].
  - "Overproduction of Lass1 increased C18:0-ceramide levels preferentially" [PMID:15823095].
  - "elevated ceramide synthase activity when stearoyl-CoA but not palmitoyl-CoA was used
    as substrate" [PMID:12105227].
  - Human LAG1 homologues rescue yeast lag1/lac1 and "restore acyl-CoA-dependent ceramide
    and sphingolipid biosynthesis" [PMID:12869556].

- BP: ceramide biosynthetic process (GO:0046513) — de novo synthesis of C18-(dihydro)ceramide;
  sphingolipid biosynthetic process (GO:0030148). CerS1 acts as one of six mammalian
  ceramide synthases in de novo sphingolipid biosynthesis [PMID:29632068, PMID:19800881].

- Localization: endoplasmic reticulum membrane (GO:0005789), multi-pass membrane protein.
  UniProt SUBCELLULAR LOCATION "Endoplasmic reticulum membrane {PubMed:24782409}". UOG1
  "localized to the endoplasmic reticulum" [PMID:12105227]. 6 predicted TM helices; TLC
  domain (97-311). N-terminus luminal, C-terminus cytosolic [PMID:15823095].

## Tissue / physiology
- Brain (Purkinje/cerebellum) and skeletal muscle enriched; C18-ceramide. HPA: tissue
  enriched (brain).
- Skeletal-muscle role in glucose metabolism / insulin sensitivity; protects from
  diet-induced obesity (FGF21-dependent) — By similarity to mouse P27545.

## Disease
- Epilepsy, progressive myoclonic 8 (EPM8) [MIM:616230], autosomal recessive; homozygous
  H183Q reduces C18-ceramide with impaired ceramide synthase activity [PMID:24782409];
  additional EPM8 variants [PMID:33798445]. "impairment of ceramide biosynthesis underlies
  neurodegeneration in humans."

## Signaling / stress (context, largely non-core)
- CerS1/C18-ceramide induces lethal mitophagy (tumor suppressor); H183A catalytic-dead
  abolishes it — endogenous C18-ceramide anchors LC3B-II to mitochondria [PMID:22922758].
- CerS1/C18-ceramide represses hTERT promoter via Sp3/HDAC1 deacetylation [PMID:17548428].
- Stress (UV, DTT, cisplatin, doxorubicin) drives specific proteasome-dependent ER->Golgi
  translocation of CerS1 and cleavage; p38-MAPK activation; cisplatin sensitization
  [PMID:17699106, PMID:19800881].

## Annotation-review stance
- MF sphingosine N-acyltransferase activity (GO:0050291), BP ceramide biosynthetic process
  (GO:0046513) / sphingolipid biosynthetic process (GO:0030148), CC ER membrane
  (GO:0005789) = CORE. ACCEPT experimental + IBA + curated IEA of these.
- IEA "membrane" (GO:0016020) redundant-general vs ER membrane -> MARK_AS_OVER_ANNOTATED.
- Ensembl ortholog-projected mouse/rat phenotypic BPs (negative regulation of cardiac
  muscle hypertrophy GO:0010614; negative regulation of glucose import GO:0046325;
  acyltransferase-other-than-amino-acyl GO:0016747) -> KEEP_AS_NON_CORE (downstream/indirect
  or too general) rather than REMOVE (they are experimentally-anchored ortholog transfers,
  and the metabolic phenotypes match UniProt By-similarity text).
- Stress/response and mitophagy/hTERT single-study downstream BPs -> KEEP_AS_NON_CORE
  (real but not the enzyme's core molecular role).
- 2-hydroxy activity paper [PMID:18541923] and sphingomyelin-biosynthesis IDA
  [PMID:29632068] are correctly-attributed experimental annotations -> ACCEPT / KEEP.

## Verbatim quote provenance verified via grep against cached files (line-bound substrings).
