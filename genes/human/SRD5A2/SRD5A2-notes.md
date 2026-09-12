# SRD5A2 (human) review notes
<!-- propagation_review corrected: root_cause=PROPAGATION_BAD; failure_modes are enum values not objects -->


UniProt: P31213 (S5A2_HUMAN). Steroid 5-alpha-reductase type 2 / 3-oxo-5-alpha-steroid
4-dehydrogenase 2. EC 1.3.1.22. 254 aa, ER/microsomal multi-pass membrane protein.

Deep research: falcon provider OUT OF CREDITS (HTTP 402) at time of review — no
`SRD5A2-deep-research-falcon.md` generated. Review grounded in UniProt (`SRD5A2-uniprot.txt`),
the seeded GOA (`SRD5A2-goa.tsv`), and cached publications.

## Core biology (verified)

- **Molecular function**: NADPH-dependent, irreversible stereospecific reduction of the
  Delta-4,5 double bond of 3-oxo-Delta4 steroids -> 5alpha-dihydro-3-oxo products
  [file:human/SRD5A2/SRD5A2-uniprot.txt "Catalyzes the irreversible stereospecific reduction of the delta 4,5 bond ... of various 3-oxo steroids ... producing their 5alpha dihydro-3-oxo forms"].
  Prototype reaction testosterone -> 5alpha-dihydrotestosterone (DHT), the most potent androgen
  [PMID:10898110 "catalyses the irreversible conversion of testosterone to dihydrotestosterone (DHT), the most active androgen in the prostate, with NADPH as its cofactor"].
  Also reduces progesterone and other 3-oxo-Delta4 steroids [UniProt CATALYTIC ACTIVITY blocks:
  5alpha-pregnane-3,20-dione + NADP+ = progesterone + NADPH + H+, RHEA:21952].
- **GO MF terms in GOA**: GO:0003865 (3-oxo-5-alpha-steroid 4-dehydrogenase activity),
  GO:0047751 (3-oxo-5-alpha-steroid 4-dehydrogenase (NADP+) activity, EC 1.3.1.22),
  GO:0047045 (testosterone dehydrogenase (NADP+) activity). All three are correct facets
  of the same enzymatic activity. Chose GO:0003865 as the primary core MF (matches the
  named enzyme and the IBA/EXP/IDA consensus).
- **Biological process**: androgen/testosterone biosynthesis and androgen metabolism;
  DHT is required for male external genitalia development. Core BP terms: GO:0006702
  androgen biosynthetic process, GO:0061370 testosterone biosynthetic process (IDA),
  GO:0008209 androgen metabolic process (IDA).
- **Localization**: ER membrane / microsome membrane, multi-pass membrane protein
  [file:human/SRD5A2/SRD5A2-uniprot.txt "Endoplasmic reticulum membrane"; 4 predicted TM helices].
  GO:0005789 endoplasmic reticulum membrane.
- **Disease / pharmacology**: loss-of-function variants cause 5alpha-reductase-2 deficiency
  (pseudovaginal perineoscrotal hypospadias, PPSH; 46,XY DSD). Target of finasteride and
  dutasteride (BPH, androgenetic alopecia) — see UniProt DrugBank xrefs and Reactome
  R-HSA-9705794.

## Annotation adjudication summary

- ACCEPT (core): the enzymatic MF terms (GO:0003865, GO:0047751, GO:0047045), androgen/
  testosterone biosynthesis & androgen metabolism BP (GO:0006702, GO:0061370, GO:0008209),
  ER membrane CC (GO:0005789), and steroid metabolic process (GO:0008202).
- ACCEPT/KEEP_AS_NON_CORE: male gonad development (GO:0008584, IMP/IBA/IEA) — supported by
  the human deficiency phenotype but developmental/downstream of the core enzymatic role.
- MARK_AS_OVER_ANNOTATED: bare `protein binding` IPIs (GO:0005515 x2/3) from high-throughput
  interactome maps (HuRI PMID:32296183; BioPlex PMID:33961781) — uninformative, no functional
  MF captured (per curation guideline to avoid `protein binding`).
- The large block of Ensembl-orthology (GO_REF:0000107, IEA from rat P31214) transferred
  developmental/response/xenobiotic terms (hippocampus/hypothalamus/bone development, response
  to FSH/testosterone/steroid/peptide-hormone/nutrient, xenobiotic/dioxin/phthalate/biphenyl
  metabolism, neuronal cell body, cell body fiber): these are rodent-CNS/toxicology inferences
  not reflecting the core human enzyme function — KEEP_AS_NON_CORE where plausibly conserved,
  MARK_AS_OVER_ANNOTATED for the xenobiotic/CNS-specific ones.
- GO:0007267 cell-cell signaling (TAS, PMID:1944596) — over-general/miscast; the paper is
  about the enzyme's role in androgen action and DSD, not cell-cell signaling. MARK_AS_OVER_ANNOTATED.
- GO:0006706 steroid catabolic process (IEA) — the reaction is a reductive activation, not
  catabolism per se; MARK_AS_OVER_ANNOTATED.
- Broad IEA MF (GO:0016627 oxidoreductase acting on CH-CH; GO:0006629 lipid metabolic process):
  correct-but-general parents; KEEP as non-core / accept as broader.
