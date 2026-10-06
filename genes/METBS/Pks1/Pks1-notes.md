# Pks1 Gene Review Notes

## Key Findings from Literature

### Primary Function
- Polyketide synthase producing anthraquinone-derived conidial pigments [PMID:29958281 "PKS1 is involved in synthesis of an anthraquinone derivative"]
- Essential for UV protection and temperature stress resistance [PMID:29958281 "play[ing] an important role in fungal tolerance to UV radiation and extreme temperatures"]
- Type I non-reducing PKS with modular domain architecture

### Biosynthetic Details
- Produces 1-acetyl-2,4,6,8-tetrahydroxy-9,10-anthraquinone [UniProt annotation]
- Works with EthD (dehydratase) and Mlac1 (laccase) to produce final pigment [PMID:29958281, UniProt]
- Contains SAT, KS, MAT, PT, dual ACP, and TE domains

### Regulation
- Highly expressed during conidiation [PMID:29958281 "PKS1 is highly expressed during conidiation"]
- Regulated by BrlA-AbaA-WetA conidiation pathway [UniProt annotation]
- Controlled by Hog1 and Slt2 MAPK pathways [PMID:29958281]

### Evolutionary Significance  
- Part of duplicated gene cluster that underwent functional diversification [PMID:29958281 "Duplication of a Pks gene cluster and subsequent functional diversification facilitate environmental adaptation"]
- Enhanced adaptive flexibility of Metarhizium species [PMID:29958281]

## GO Annotation Assessment

### Molecular Function
- GO:0016218 (polyketide synthase activity) - CORRECT, primary function
- GO:0004315 (3-oxoacyl-[ACP] synthase) - PARTIAL, represents KS domain activity only
- GO:0004312 (fatty acid synthase) - INCORRECT, produces polyketides not fatty acids
- GO:0016740/GO:0016746 (transferase/acyltransferase) - TOO GENERAL
- GO:0031177 (phosphopantetheine binding) - CORRECT for ACP domains
- GO:0003824 (catalytic activity) - TOO GENERAL

### Biological Process
- GO:0030639 (polyketide biosynthetic process) - CORRECT, should be core
- GO:0046189 (phenol-containing compound biosynthetic process) - CORRECT, anthraquinones are phenolic
- GO:0044550 (secondary metabolite biosynthetic process) - CORRECT but general
- GO:0006633 (fatty acid biosynthetic process) - INCORRECT

### Missing Important Annotations
- Conidial pigmentation process
- Response to UV radiation
- Response to temperature stress
- Fungal-type cell wall organization (pigment deposition)
## Re-review 2026-10-01 (GOA refresh)

- New GOA rows reviewed:
  - GO:0016740 transferase activity (IEA, GO_REF:0000002, InterPro:IPR001227) -> MODIFY
    to GO:0016218 polyketide synthase activity (as for the acyltransferase row).
  - GO:0044550 secondary metabolite biosynthetic process (IEA, GO_REF:0000118 TreeGrafter)
    -> MODIFY to GO:0030639 polyketide biosynthetic process (replaces vanished
    GO_REF:0000120 row for the same term).
- Vanished from current GOA -> `retired: true` (reviews kept): GO:0003824 catalytic
  activity (GO_REF:0000043), GO:0016740 transferase activity (GO_REF:0000120),
  GO:0044550 secondary metabolite biosynthetic process (GO_REF:0000120).
- NEW proposals re-audited against the participation/comparator rules:
  - Dropped GO:0009411 response to UV, GO:0009266 response to temperature stimulus
    (downstream protective effects of the pigment, not processes Pks1 executes) and
    GO:0048315 conidium formation (Pks1 KO strains still form conidia, just red ones).
  - Dropped GO:0046189 phenol-containing compound biosynthetic process (chemical-class
    restatement of the polyketide product; no added information).
  - Replaced GO:0043473 pigmentation with GO:0046148 pigment biosynthetic process (IMP);
    comparator check via QuickGO: conidial pigment PKSs wA (Q03149) and alb1 (Q4WZA8)
    carry GO:0046148 by IMP.
  - Kept GO:0030639 polyketide biosynthetic process (now IMP, PMID:29958281); fixed its
    reason, which wrongly named the product isoflavipucine.
- Removed non-verbatim supporting texts (a quote attributed to Pks1-bioinformatics/
  RESULTS.md and a paraphrased PMID:29958281 finding); core_functions consolidated from
  four entries to two.
