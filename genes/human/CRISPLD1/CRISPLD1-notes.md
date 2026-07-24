# CRISPLD1 review notes

## 2026-07-18: setup and evidence acquisition

- `just fetch-gene human CRISPLD1` created the UniProt, GOA, and review-stub files for
  Q9H336. The current GOA has seven annotation groups.
- `just fetch-gene-pmids human CRISPLD1` confirmed the three GOA-linked papers were
  cached. Forced refreshes recovered PMC full text for PMID:21254358 and PMID:23533145.
- The configured deep-research workflow was attempted with Falcon and the
  `perplexity-lite` fallback. Falcon failed with HTTP 402 (Edison payment required),
  and the fallback failed with HTTP 401 (quota exceeded). No provider-named research
  file was created; the evidence synthesis below is manual.
- A manual literature search identified PMID:32146539 as the strongest focused
  functional study, and it was cached with PMC full text.

## Protein identity, architecture, and localization

CRISPLD1 is a reviewed 500-aa precursor with a predicted signal peptide (residues
1-23), an SCP/CAP domain (66-206), and two LCCL domains (289-384 and 390-492)
[file:human/CRISPLD1/CRISPLD1-uniprot.txt, "FT   SIGNAL          1..23";
"FT   DOMAIN          66..206"; "FT   DOMAIN          289..384";
"FT   DOMAIN          390..492"]. UniProt calls the protein secreted
[file:human/CRISPLD1/CRISPLD1-uniprot.txt, "CC   -!- SUBCELLULAR LOCATION: Secreted
{ECO:0000305}."]. This architecture distinguishes CRISPLD1 from the approximately
240-aa, CAP-only GLIPR/CRISP proteins even though all share the broad CAP superfamily.

## Focused functional literature

### Cardiomyocyte calcium cycling (PMID:32146539)

CRISPLD1 expression increases during the transition from pressure-overload hypertrophy
to heart failure in both human myocardium and the analogous mouse model. The focused
functional experiment used CRISPR/Cas9 loss of function in human iPSC-derived
cardiomyocytes. Knockout increased calcium-transient amplitude and rise time and
shortened decay, producing a higher systolic calcium transient
[PMID:32146539, "Compared to WT controls, CRISPLD1-KO-CM show a significant increase
in CaT amplitude (WT mean = 2.8, KO mean = 3.5; Fig. 4b, e), a significant increase in
CaT rise time (WT mean = 169.5 ms, KO mean = 199.0 ms; Fig. 4c, f) and a significant
decrease in CaT decay (WT mean = 603.5 ms, KO mean = 460.8 ms; Fig. 4d, g), pointing
towards higher systolic CaT in KO-CM."]. The authors' evidence-bounded interpretation
is that CRISPLD1 inhibits cardiomyocyte calcium cycling
[PMID:32146539, "This loss-of-function and rescue experiments support the converse
argument, that CRISPLD1 plays an inhibitory role in CM Ca2+ cycling."].

The molecular mechanism remains unresolved. Sequence similarity to the calcium-channel
regulating toxin helothermine motivated the experiment, but the study did not identify
a CRISPLD1 receptor, channel target, or direct binding/catalytic activity. The authors
state that "the detailed underlying molecular mechanisms remain to be investigated in
the future" [PMID:32146539]. Therefore GO:0051481 (negative regulation of cytosolic
calcium ion concentration) is defensible as a new process annotation, whereas
GO:0005246 (calcium channel regulator activity) is not yet justified.

### Craniofacial association (PMID:21254358)

This is a human family genetic-association study, not a CRISPLD1 perturbation study.
It found little evidence for CRISPLD1 variation alone and instead reported statistical
interactions with CRISPLD2 and folate-pathway variants. The full text explicitly says
[PMID:21254358, "We show that only one CRISPLD1 SNP, rs1455809, had marginally altered
transmission (p=0.05) suggesting that variation in CRISPLD1 alone does not play a
significant etiologic role in NSCLP."]. The paper also says that additional validation
and functional studies are required [PMID:21254358, "These results are intriguing and
require both validation and functional studies"]. Developmental expression in mouse
nose/skeleton and zebrafish splanchocranium makes a facial-development relationship
plausible, but the paper does not establish a direct CRISPLD1 mutant phenotype. Thus
GO:0060325 is treated as over-annotated, not as a core function.

### Exosome-enriched proteomes (PMID:19199708 and PMID:23533145)

CRISPLD1 was identified in two independent exosome-enriched human-fluid proteomes:
parotid saliva and expressed prostatic secretions in urine. These HDA observations are
compatible with a secreted protein and are retained as non-core localization context.
They do not demonstrate that CRISPLD1 functions on/in exosomes. Both studies discuss
the limitations of high-throughput vesicle preparations. The prostate study notes that
some detected proteins may also exist in soluble form [PMID:23533145, "some of these
proteins could also exist as a soluble form"], and the parotid study states that highly
abundant extracellular proteins can be incorporated during vesicle formation or arise
from minor contamination [PMID:19199708, "Alternatively, some minor contamination may
have occurred during the isolation procedure of the exosomes."].

## PANTHER/IBA trace

The current CRISPLD1 GOA routes both IBA annotations through PANTHER node
PTN000036124. The local PAINT table shows that extracellular region is supported by
many secreted CAP-family proteins, whereas molecular adaptor activity has a single
seed, mouse Glipr1l1 (MGI:MGI:1916536)
[file:interpro/panther/PTHR31331/PTHR31331-paint.tsv,
"PTHR31331\tPTN000036124\tGO:0060090\tF\tIBD\tfalse\tMGI:MGI:1916536"].

The source GO-CAM places Glipr1l1 molecular adaptor activity at the outer acrosomal
membrane in sperm and connects it to protein localization involved in the acrosome
reaction [file:gocams/62f58d8800005094/62f58d8800005094-src.yaml]. The local family
files show human CRISPLD1 as a 500-aa SF9 CAP-plus-two-LCCL protein, while mouse
Glipr1l1 is a 236-aa CAP-only protein in the much broader PTHR10334 collection
[file:interpro/panther/PTHR31331/PTHR31331-entries.csv,
"Q9H336,Cysteine-rich secretory protein LCCL domain-containing 1,protein,9606,Homo
sapiens,Homo sapiens (Human),CRISPLD1,500,PTHR31331:SF9"]
[file:interpro/panther/PTHR10334/PTHR10334-entries.csv,
"Q9DAG6,GLIPR1-like protein 1,protein,10090,Mus musculus,Mus musculus (Mouse),Glipr1l1,236"].
No CRISPLD1-specific evidence shows it bridging macromolecules. The sole PANTHER seed
for GO:0060090 is therefore biologically specific to a divergent reproductive CAP
paralog and does not support transfer to CRISPLD1; the IBA is removed as a propagation
failure. In contrast, the extracellular-region IBA agrees with the signal peptide,
UniProt secretion statement, and human extracellular-fluid proteomics, and is accepted.

## Curation synthesis

Original GOA actions (seven groups):

1. Extracellular region, IBA: **ACCEPT**.
2. Molecular adaptor activity, IBA: **REMOVE** (single divergent Glipr1l1 seed;
   no CRISPLD1-specific adaptor evidence).
3. Extracellular region, IEA: **ACCEPT**.
4. Face morphogenesis, IEA/ARBA: **MARK_AS_OVER_ANNOTATED**.
5. Extracellular exosome, HDA/PMID:23533145: **KEEP_AS_NON_CORE**.
6. Face morphogenesis, IMP/PMID:21254358: **MARK_AS_OVER_ANNOTATED**.
7. Extracellular exosome, HDA/PMID:19199708: **KEEP_AS_NON_CORE**.

One evidence-supported new annotation is added: GO:0051481, negative regulation of
cytosolic calcium ion concentration, based on the human cardiomyocyte loss-of-function
phenotype in PMID:32146539.

The major remaining knowledge gap is molecular: the extracellular target/receptor,
direct molecular activity, relevant calcium-handling effector, and domain requirements
are unknown. Direct CRISPLD1 protein add-back, channel/current measurements, and
domain-resolved rescue are needed before assigning calcium channel regulator activity.
