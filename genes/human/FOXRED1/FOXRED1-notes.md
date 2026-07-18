# FOXRED1 review notes

Gene: **FOXRED1** (FAD-dependent oxidoreductase domain-containing protein 1)
UniProt: Q96CU9 · HGNC:26927 · GeneID 55572 · Chromosome 11 · human (NCBITaxon:9606)

## One-line summary

FOXRED1 is a nuclear-encoded, FAD-dependent oxidoreductase-fold flavoprotein of the
mitochondrial inner membrane that acts as a **complex I-specific assembly factor
(molecular chaperone)** required for the mid-late stages of NADH:ubiquinone
oxidoreductase (respiratory chain complex I) biogenesis. It is **not** a structural
subunit of the mature holoenzyme, and no in-vivo catalytic substrate/reaction has been
defined; its fold and cofactor imply oxidoreductase activity but the specific reaction is
unknown.

## Core biology (grounded)

### Molecular identity / cofactor
- Named "FAD-dependent oxidoreductase domain-containing protein 1"; EC=1.-.-.- (an
  oxidoreductase of undefined sub-subclass). [file:human/FOXRED1/FOXRED1-uniprot.txt
  "RecName: Full=FAD-dependent oxidoreductase domain-containing protein 1"]
- Carries an **FAD** cofactor (by similarity, ECO:0000250). [file:human/FOXRED1/FOXRED1-uniprot.txt
  "Name=FAD; Xref=ChEBI:CHEBI:57692; Evidence={ECO:0000250}"]
- Keywords: FAD; Flavoprotein; Oxidoreductase; Electron transport; Respiratory chain.
  [file:human/FOXRED1/FOXRED1-uniprot.txt]
- Domain architecture (InterPro/Pfam): DAO (PF01266) FAD-dependent oxidoreductase domain;
  FAD/NAD(P)-binding superfamily fold; PANTHER family PTHR13847 "SARCOSINE
  DEHYDROGENASE-RELATED". [file:human/FOXRED1/FOXRED1-uniprot.txt]
- Evolution: Lemire 2015 (PMID:25681241) analyses FOXRED1 as "an FAD-dependent
  oxidoreductase necessary for NADH:ubiquinone oxidoreductase (Complex I) assembly"
  (title; abstract-only, not cached).

### Function: complex I assembly factor
- Required for assembly of the mitochondrial membrane respiratory chain NADH dehydrogenase
  (complex I). [file:human/FOXRED1/FOXRED1-uniprot.txt "Required for the assembly of the
  mitochondrial membrane"]
- Acts at **mid-late stages** of complex I assembly. [file:human/FOXRED1/FOXRED1-uniprot.txt
  "Involved in mid-late stages of complex I assembly"]
- Formosa et al. 2015 (PMID:25678554, IMP; abstract-only): "we demonstrate that FOXRED1 is
  involved in mid-late stages of complex I assembly." In FOXRED1-null HEK293T cells, complex
  I drops to ~10%, complex I activity is reduced, and cells cannot grow on galactose. An
  ~815 kDa late-stage intermediate forms transiently but, without FOXRED1, breaks down to an
  ~475 kDa complex instead of maturing. FOXRED1 co-immunoprecipitates with a number of
  complex I subunits. [PMID_25678554 abstract: "FOXRED1 is involved in mid-late stages of
  complex I assembly"; "Cells lacking FOXRED1 had ∼10% complex I levels, reduced complex I
  activity, and were unable to grow on galactose media"; "FOXRED1 was found to
  co-immunoprecipitate with a number of complex I subunits"]
- Fassone et al. 2010 (PMID:20858599, disease/knockdown): FOXRED1 is described as a
  "complex I-specific molecular chaperone"; silencing in human fibroblasts reduced complex I
  steady-state levels and activity, and lentiviral FOXRED1 rescued the deficiency in patient
  fibroblasts. [PMID_20858599 abstract: "Silencing of FOXRED1 in human fibroblasts resulted
  in reduced complex I steady-state levels and activity, while lentiviral-mediated FOXRED1
  transgene expression rescued complex I deficiency in the patient fibroblasts"; "is now
  shown to be a complex I-specific molecular chaperone"]

### Subunit / association
- Associates with components of the mitochondrial respiratory chain complex I (SUBUNIT,
  ECO:0000269|PubMed:25678554). [file:human/FOXRED1/FOXRED1-uniprot.txt "Associates with
  components of the mitochondrial respiratory"]
- This association reflects transient interaction with assembly intermediates, not
  membership of the mature holoenzyme (the 44-subunit complex I does not include FOXRED1).

### Localization
- Mitochondrion inner membrane (EXP/IDA, PMID:20858599, PMID:25678554).
  [file:human/FOXRED1/FOXRED1-uniprot.txt "SUBCELLULAR LOCATION: Mitochondrion inner membrane"]
- Predicted single-pass membrane protein (one TM helix, residues 62-82, ECO:0000255), though
  one report places it on the matrix face without a TM region. [file:human/FOXRED1/FOXRED1-uniprot.txt
  "Single-pass"; "associated with the matrix face of the mitochondrial inner membrane"]
- HTP mitochondrial proteome (PMID:34800366) confirms mitochondrial localization (general).

### Disease
- Biallelic FOXRED1 variants cause **mitochondrial complex I deficiency, nuclear type 19
  (MC1DN19; MIM:618241)**, autosomal recessive; infantile-onset encephalomyopathy / Leigh-like
  phenotypes. [file:human/FOXRED1/FOXRED1-uniprot.txt "Mitochondrial complex I deficiency,
  nuclear type 19 (MC1DN19)"]
- Disease variants: p.R352W (Fassone 2010, PMID:20858599), p.N430S and 232-486 del (Calvo
  2010, PMID:20818383). Formosa 2015 characterized R352W/N430S as hypomorphic in vitro; over-
  expressing patient-mutant FOXRED1 could still rescue complex I assembly. [file:...uniprot.txt]

## Annotation review reasoning

- **MF GO:0016491 oxidoreductase activity (IEA UniProtKB-KW)** — ACCEPT. Grounded in the FAD
  cofactor + oxidoreductase fold + EC 1.-.-.-. This is the level of MF specificity the evidence
  supports; do NOT specialize to a substrate reaction (none demonstrated in vivo), and do NOT
  assign NADH dehydrogenase activity GO:0008137 (FOXRED1 is not a catalytic holoenzyme subunit).
- **BP GO:0032981 mitochondrial respiratory chain complex I assembly** — ACCEPT (both the IMP
  from PMID:25678554 and the IBA). This is the core biological process.
- **CC mitochondrion / mitochondrial inner membrane** — ACCEPT experimental (IDA/EXP) and the
  SubCell IEA; general mitochondrion terms are correct but less specific than inner membrane.
- **CC cytoplasm (IBA, is_active_in)** — KEEP_AS_NON_CORE / general. The IBA "cytoplasm" is a
  broad ancestor localization from the phylogenetic pipeline; the informative and experimentally
  supported localization is the mitochondrial inner membrane. Not wrong (mitochondrion is within
  cytoplasm) but uninformative for this gene.
- **FAD binding GO:0050660** — proposed as a NEW core-function MF, grounded in the UniProt
  COFACTOR (FAD) line and Flavoprotein/FAD keywords. Not currently in GOA.

## Core functions (planned)
1. FAD-dependent oxidoreductase activity (GO:0016491), FAD-binding flavoprotein (GO:0050660),
   at the mitochondrial inner membrane — undefined in-vivo substrate.
2. Complex I assembly factor: directly_involved_in mitochondrial respiratory chain complex I
   assembly (GO:0032981) at the mitochondrial inner membrane.

## Open questions / knowledge gaps
- What is FOXRED1's actual enzymatic reaction and physiological substrate (EC sub-subclass)?
  Is its oxidoreductase activity even required for the chaperone function, or is it a
  fold-retaining scaffold?
- Which specific complex I subunit(s)/intermediate does FOXRED1 act on at the mid-late
  (~815 kDa → mature) transition?

## Provenance conventions
- `file:human/FOXRED1/FOXRED1-uniprot.txt` quotes are verbatim single-line substrings of the
  UniProt flat file (CC-prefixed lines cannot be spanned across two lines).
- PMID quotes are verbatim substrings of the cached abstracts in publications/PMID_*.md.
