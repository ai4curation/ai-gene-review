# SLC25A20 (CACT / mitochondrial carnitine-acylcarnitine carrier) review notes

UniProtKB: O43772 (MCAT_HUMAN). HGNC:1421. Gene MIM 613698; disease MIM 212138 (CACTD).

## Deep research status
`just deep-research-falcon human O43772 --alias SLC25A20` failed with a Python
version error in `scripts/deep_research_wrapper.py` (`dict | None` union syntax
under an older interpreter: `TypeError: unsupported operand type(s) for |: 'type'
and 'NoneType'`). This is an environment/tooling bug, not a data-availability
issue, and a retry produces the same failure. Per project policy I did NOT
fabricate a `-deep-research-*.md`. Review is grounded in the UniProt record,
seeded GOA, cached publications (`publications/PMID_*.md`), Reactome caches, and
the dismech disorder KB entry for CACT deficiency.

## Core biology (verified)
- CACT is the mitochondrial INNER-membrane carnitine/acylcarnitine antiporter; it
  couples the two CPT reactions of the carnitine shuttle. CPT1 (outer membrane)
  makes long-chain acylcarnitine from acyl-CoA + carnitine; CACT imports the
  acylcarnitine into the matrix in exchange (antiport) for exporting free
  L-carnitine; CPT2 (matrix face of inner membrane) regenerates acyl-CoA for
  beta-oxidation. [Reactome R-HSA-200425 carnitine shuttle; R-HSA-200424 exchange
  of acylcarnitine and carnitine across the IMM]
- Mechanism: electroneutral antiport via ping-pong mechanism over a range of acyl
  chain lengths (acetyl- to long-chain O-acyl-carnitine); also catalyzes
  lower-rate uniport of free carnitine. [UniProt FUNCTION; PubMed:12892634,
  18307102, 20347717]
- Belongs to mitochondrial carrier family (TC 2.A.29; SLC25). 6 TM helices, 3
  Solcar repeats. Multi-pass IMM protein. [UniProt features]

## Key references
- PMID:9399886 (EXP for GO:0005476): cloned human CAC cDNA; "The
  carnitine-acylcarnitine carrier (CAC) catalyzes the translocation of long-chain
  fatty acids across the inner mitochondrial membrane." Identified a homozygous C
  insertion causing frameshift in a CAC-deficient infant (first CACTD mutation).
  Abstract-only in cache; Reactome assigned the MF EXP annotation from this paper.
- PMID:32814053 (IPI protein binding): Y2H neurodegenerative-disease interactome;
  IntAct records SLC25A20-LAMP2 (P13473-2) interaction (UniProt INTERACTION line).
  Bare "protein binding" — uninformative; MARK_AS_OVER_ANNOTATED per curation
  policy (not REMOVE; it is an experimental IPI).
- PMID:34800366 (HTP mitochondrion): MitoCoP high-confidence human mitochondrial
  proteome (>1,100 proteins); SLC25A20 among them.
- PMID:20833797 (HDA mitochondrion): phosphoproteome of isolated human muscle
  mitochondria (inner-membrane solute carriers included).

## Disorder KB (dismech Carnitine-Acylcarnitine_Translocase_Deficiency.yaml)
"CACT is a mitochondrial inner membrane transporter that facilitates the exchange
of long-chain acylcarnitines for free carnitine across the inner mitochondrial
membrane, a critical step in the carnitine shuttle required for long-chain fatty
acid beta-oxidation." Severe neonatal form: hypoketotic hypoglycemia,
hyperammonemia, cardiac arrhythmia, cardiomyopathy, hepatic dysfunction, ~65%
mortality (cardiac). GeneReviews: "Carnitine-acylcarnitine translocase (CACT) is a
critical component of the carnitine shuttle, which facilitates the transfer of
long-chain fatty acylcarnitines across the inner mitochondrial membrane."

## Annotation dispositions
- GO:0005476 antiporter MF (EXP PMID:9399886; TAS Reactome) — ACCEPT, core.
- GO:0015227 O-acyl-L-carnitine transporter MF (IBA, ISS) — ACCEPT (broader
  parent capturing same activity; the antiport term is the precise one).
- GO:0006853 carnitine shuttle BP (IEA, TAS) — ACCEPT, core process.
- GO:1902616 O-acyl-L-carnitine transmembrane transport BP (IEA) — ACCEPT.
- GO:1902603 carnitine transmembrane transport BP (IBA, ISS) — ACCEPT (uniport of
  free carnitine + carnitine leg of antiport).
- GO:0006839 mitochondrial transport BP (IBA) — ACCEPT (broad but correct parent).
- GO:0005743 mitochondrial inner membrane CC (IEA, TAS x2) — ACCEPT, core location.
- GO:0005740 mitochondrial envelope CC (IBA) — ACCEPT (correct broader CC; IMM is
  more precise).
- GO:0005739 mitochondrion CC (IDA HPA, HTP, HDA) — ACCEPT (correct, less precise).
- GO:0005515 protein binding MF (IPI PMID:32814053) — MARK_AS_OVER_ANNOTATED
  (uninformative bare protein binding; keep, do not treat as core MF).
