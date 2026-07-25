# CYP8B1 (human) — gene review notes

UniProt: Q9UNU6 (CP8B1_HUMAN), 501 aa, gene HGNC:2653. EC 1.14.14.139.
Product name: 7-alpha-hydroxycholest-4-en-3-one 12-alpha-hydroxylase (sterol 12-alpha-hydroxylase, CYPVIIIB1, cytochrome P450 8B1). Synonym CYP12.

## Core biology (grounded)

CYP8B1 is a hepatic, microsomal (ER-membrane) heme-thiolate cytochrome P450 that is the
branch-point enzyme of the classic (neutral) bile-acid synthesis pathway. It
12-alpha-hydroxylates 7-alpha-hydroxy-4-cholesten-3-one and related C27 intermediates,
committing flux toward cholic acid rather than chenodeoxycholic acid, thereby setting the
cholic-acid : CDCA ratio and the hydrophobicity/solubility properties of the bile-acid pool.

- Sterol 12-alpha-hydroxylase, controls the CA:CDCA balance
  [PMID:10051404 "Sterol 12alpha-hydroxylase (CYP8B1) is a hepatic cytochrome P-450 that controls"]
  [PMID:10051404 "the ratio of cholic acid over chenodeoxycholic acid in bile and thus controls"]
  (the sentence continues "the solubility of cholesterol").
- UniProt FUNCTION: "Sterol 12-alpha-hydroxylase involved in primary bile acid"
  biosynthesis by catalyzing "the 12alpha-hydroxylation of key" intermediates
  [file:human/CYP8B1/CYP8B1-uniprot.txt].
- Monooxygenase / P450 chemistry: "Functions as a monooxygenase, inserting one atom"
  "of molecular oxygen into substrates while reducing the second to water,"
  "using electrons supplied by NADPH via cytochrome P450 reductase (CPR)"
  [file:human/CYP8B1/CYP8B1-uniprot.txt].
- Controls bile-acid pool / lipid absorption: "Controls biliary balance of cholic acid and"
  chenodeoxycholic acid, thereby regulating intestinal absorption of dietary lipids
  [file:human/CYP8B1/CYP8B1-uniprot.txt].

## Catalytic activity (UniProt, EC 1.14.14.139)

Four documented reactions, all RHEA-xref'd in the UniProt entry:
- 7alpha-hydroxycholest-4-en-3-one -> 7alpha,12alpha-dihydroxycholest-4-en-3-one
  (RHEA:46752; ECO:0000269|PubMed:10051404, PubMed:39214664) — classic-pathway branch step.
- 5beta-cholestane-3alpha,7alpha-diol -> 5beta-cholestane-3alpha,7alpha,12alpha-triol
  (RHEA:15261; by similarity to O02766).
- (25R)-3alpha,7alpha-dihydroxy-5beta-cholestan-26-oate (DHCA) ->
  (25R)-3alpha,7alpha,12alpha-trihydroxy-5beta-cholestan-26-oate (THCA)
  (RHEA:82331; ECO:0000269|PubMed:39214664) — C27 bile-acid 12alpha-hydroxylation.
- chenodeoxycholate -> cholate (RHEA:65700; ECO:0000269|PubMed:30465713).

GO:0008397 (sterol 12-alpha-hydroxylase activity) is xref'd to EC:1.14.14.139 and to
RHEA:46752/65700/15261 — exact match to the UniProt catalytic reactions. Confirmed via
go.db that GO:0008397 is in the molecular_function branch, is_a monooxygenase activity
(GO:0004497) -> oxidoreductase acting on paired donors with O2 (GO:0016705).

## Experimental support for the enzyme activity

- PMID:30465713 (Fan et al. 2019, IDA): CYP8B1 converts CDCA to CA and the C4 precursor to
  the CA intermediate. Abstract-only cache. "The human cytochrome P450 enzyme CYP8B1 is a
  crucial regulator of the balance of" CA and CDCA; "In this study we demonstrate that
  CYP8B1 can also convert" CDCA to CA; C4 precursor "to 7α,12α-dihydroxycholest-4-en-3-one,
  which is an intermediate" of CA biosynthesis. Also identified CYP8B1 inhibitors
  (aminobenzotriazole, exemestane, ketoconazole, letrozole) — pharmacology, not core.
- PMID:39214664 (Wang et al. 2024, IDA): recombinant + microsomal CYP8B1 12alpha-hydroxylates
  DHCA -> THCA (C27) and C4. "Sterol 12α-hydroxylase (CYP8B1) is the unique P450 enzyme with
  sterol" 12-oxidation activity; "both microsomal and recombinant CYP8B1 enzymes catalyze the
  12α-hydroxylation of" DHCA and C4; substrate titration gives type I heme binding
  ("Soret peak (type I binding)."); KM 1.9 uM for C4, kcat 2.6 min-1 (UniProt kinetics).
- PMID:10051404 (Gåfvels et al. 1999, TAS/primary): cloned human+mouse CYP8B1, intronless
  P450 gene, liver-specific; COS-cell expression gave "enzymatic activity for the"
  12alpha-hydroxylase. First to establish CA:CDCA ratio control. Abstract-only cache.

## Localization / cofactor

- ER membrane, single-pass; also microsome membrane [file:human/CYP8B1/CYP8B1-uniprot.txt,
  "SUBCELLULAR LOCATION: Endoplasmic reticulum membrane"]. Reactome R-HSA-192157 also states
  the enzyme is "associated with the endoplasmic reticulum membrane".
- Heme cofactor (ChEBI:30413), axial Fe-binding residue at position 440 ("axial binding
  residue"); iron ion binding is intrinsic to the P450 heme-thiolate center.
- N-terminal TRANSMEM 1..21 (the single-pass ER anchor).
- Pathway: "Lipid metabolism; bile acid biosynthesis." [file:human/CYP8B1/CYP8B1-uniprot.txt].
- Tissue: liver ("TISSUE SPECIFICITY: Liver.", ECO:0000269|PubMed:10051404); HPA "Tissue
  enriched (liver)".

## Annotation review reasoning (summary)

Core, well-supported:
- MF sterol 12-alpha-hydroxylase activity (GO:0008397): multiple IDA (PMID:30465713,
  PMID:39214664) + IBA + TAS + ISS. ACCEPT the experimental ones; keep the rest as valid
  (redundant) support.
- BP bile acid biosynthetic process (GO:0006699): IDA (PMID:30465713, PMID:39214664) + TAS
  (Reactome) + ISS + IEA (UniPathway). ACCEPT.
- CC endoplasmic reticulum membrane (GO:0005789): ISS/IEA/TAS. ACCEPT.
- MF heme binding (GO:0020037) and iron ion binding (GO:0005506): intrinsic to the P450
  heme-thiolate center; IEA/InterPro. ACCEPT.

Correct-but-general (parents of the specific activity/process); keep as non-core or
over-annotated rather than remove:
- MF monooxygenase activity (GO:0004497), MF oxidoreductase acting on paired donors...
  (GO:0016705): true parents of GO:0008397. Over-annotation relative to the specific MF.
- BP lipid metabolic process (GO:0006629), BP monocarboxylic acid biosynthetic process
  (GO:0072330): ARBA IEA parents of bile acid biosynthesis. Over-annotated / non-core.
- BP sterol metabolic process (GO:0016125): TAS Reactome parent-ish; non-core.

Weakly-supported / peripheral:
- MF oxygen binding (GO:0019825): old TAS/ProtInc (PMID:10051404, PINC). O2 is a co-substrate
  of the monooxygenase reaction, but "oxygen binding" (a carrier-type MF) is not the enzyme's
  informative function. The cited abstract does not describe O2-binding assays. MARK_AS_OVER_ANNOTATED.
- BP response to nutrient levels (GO:0031667): rat-ortholog IEA/Ensembl. CYP8B1 mRNA is induced
  by starvation in mouse [PMID:10051404 "a potent induction of CYP8B1 mRNA was observed upon
  starvation of mice"], so a regulatory response is plausible; keep as non-core.
- BP response to cholesterol (GO:0070723): rat-ortholog IEA/Ensembl; plausible (cholesterol/
  bile-acid feedback) but not directly evidenced here; non-core.
- BP positive regulation of intestinal cholesterol absorption (GO:0045797): ISS from mouse
  O88962. Cyp8b1-KO mouse work supports a role in shaping the bile-acid pool that drives
  intestinal lipid/cholesterol absorption; UniProt says CYP8B1 controls "intestinal absorption
  of dietary lipids". This is a downstream physiological consequence, not CYP8B1's molecular
  function; keep as non-core.

No experimental (IDA/IMP/IPI/IGI/EXP) annotation is removed. No bare "protein binding"
annotation present. Only IEA candidates considered for REMOVE, but the IEA terms here are all
true parents/plausible, so none removed.
