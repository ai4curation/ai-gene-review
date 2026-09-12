# PGAP3 (Q96FM1) review notes

## Identity
- Human PGAP3 = Post-GPI Attachment to Proteins factor 3 = PERLD1 = CAB2/hCOS16 = COS16 homolog.
- HGNC:23719; located 17q12 (within the PPP1R1B-STARD3-ERBB2-GRB7 amplicon).
- 320 aa, multi-pass Golgi membrane protein (7 predicted TM helices), N-glycosylated at N40.
- Member of the PGAP3/PER1 (Per1-like, Pfam PF04080 / InterPro IPR007217) family.

## Core biology (from UniProt Q96FM1 + cited papers)
- **GPI-specific phospholipase A2**. Carries out the **first step of GPI fatty-acid remodeling**
  in the Golgi: removes the **unsaturated acyl chain at sn-2 of the inositol phospholipid**
  (phosphatidylinositol) of the mature GPI anchor, generating a lyso-GPI intermediate.
  PGAP2 then reacylates with a saturated (stearic) chain. This remodeling is required for
  GPI-anchored proteins (GPI-APs) to associate with lipid rafts / detergent-resistant membranes.
  - UniProt FUNCTION + CATALYTIC ACTIVITY (Rhea RHEA:83847), EC 3.1.1.-.
  - [PMID:29374258 (PGAP4 paper) intro, "In the Golgi, GPI-APs undergo fatty acid remodeling where
    PGAP3 removes an sn-2-linked unsaturated fatty acid and PGAP2 is involved in reacylation with
    stearic acid, a saturated fatty acid"].
  - Yeast PER1 is the ortholog; human PERLD1/PGAP3 functionally complements per1Δ
    [PMID:17021251 "human PERLD1 is a functional homologue of PER1"; "PER1 is required for the
    production of lyso-GPI, suggesting that Per1p possesses or regulates the GPI-phospholipase A2
    activity"].

## Localization
- Golgi apparatus membrane (GO:0000139): UniProt SUBCELLULAR LOCATION; IDA [PMID:24439110];
  IBA is_active_in; IEA (SubCell SL-0134). HPMRS4 P105R and D305G mutants are ER-retained.
- GO:0031410 cytoplasmic vesicle (IDA, PMID:12460457): from the CAB2/hCOS16 GFP-fusion study
  reporting translocation into vesicles. Peripheral/older assignment; the well-supported steady-state
  location is Golgi. Keep as non-core.

## Disease
- Hyperphosphatasia with impaired intellectual development syndrome 4 (HPMRS4 / Mabry syndrome),
  MIM 615716, autosomal recessive; elevated serum ALP (a GPI-anchored enzyme) [PMID:24439110].

## Interactions (GO:0005515 protein binding, IPI)
- GTF3C3 (Q9Y5Q9) [PMID:32814053, ND interactome Y2H]; TBRG4 (Q969Z0) [PMID:33961781, BioPlex AP-MS].
  Both are large-scale high-throughput screens; neither has an established functional relationship
  to GPI remodeling. Uninformative bare `protein binding` -> MARK_AS_OVER_ANNOTATED (do not REMOVE
  per policy).

## GOA MF term used for core_functions
- GOA carries **GO:0016788 "hydrolase activity, acting on ester bonds"** (both the IBA and the
  IMP MF annotations). Per instructions, use this exact current GOA term as the core molecular_function.
  (A more specific phospholipase A2 term would be biologically apt, but the task requires the exact
  GOA-carried MF term.)

## Quote-verification log (all verbatim substrings confirmed via python `in` check against cached files)
- PMID:29374258: "In the Golgi, GPI-APs undergo fatty acid remodeling where PGAP3 removes an
  sn-2-linked unsaturated fatty acid and PGAP2 is involved in reacylation with stearic acid, a
  saturated fatty acid" (also PGAP3-KO used experimentally in that paper).
- PMID:17021251: wrapped substrings for lyso-GPI/phospholipase A2 and PERLD1 homologue.
- PMID:24439110: "identified mutations in PGAP3, encoding a protein that is involved in GPI-anchor \nmaturation";
  "elevated serum alkaline phosphatase (ALP), a GPI-anchored enzyme"; "functional studies on Chinese
  hamster ovary cell lines"; "the later \nGPI-anchor remodelling steps for normal neuronal development".
- PMID:12460457: "CAB2 translocates into vesicles".
- file:human/PGAP3/PGAP3-uniprot.txt used for FUNCTION/CATALYTIC ACTIVITY/SUBCELLULAR LOCATION quotes.
