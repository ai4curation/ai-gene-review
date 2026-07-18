# ALDH6A1 (MMSDH) review notes

UniProt: Q02252 (MMSA_HUMAN). Gene: ALDH6A1 (HGNC:7179), synonym MMSDH. 535 aa precursor;
residues 1–33 are a mitochondrial transit peptide; mature chain 34–535. Homo sapiens (NCBITaxon:9606).

## Identity and function

ALDH6A1 encodes **methylmalonate-semialdehyde/malonate-semialdehyde dehydrogenase [acylating],
mitochondrial (MMSDH)**, EC 1.2.1.27. It is an unusual, CoA-dependent member of the aldehyde
dehydrogenase (ALDH) superfamily: unlike most ALDHs it is **acylating**, coupling NAD+-dependent
oxidative decarboxylation of the semialdehyde substrate to CoA thioester formation.

- UniProt RecName: "Methylmalonate-semialdehyde/malonate-semialdehyde dehydrogenase [acylating],
  mitochondrial", `EC=1.2.1.27` [file:human/ALDH6A1/ALDH6A1-uniprot.txt].
- UniProt FUNCTION: "Malonate and methylmalonate semialdehyde dehydrogenase involved in the
  catabolism of valine, thymine, and compounds catabolized by way of beta-alanine, including
  uracil and cytidine." (ECO:0000269|PubMed:23835272) [file:human/ALDH6A1/ALDH6A1-uniprot.txt].

### Catalyzed reactions (UniProt CATALYTIC ACTIVITY blocks)

1. **Malonate semialdehyde branch** (RHEA:76615, ECO:0000250|Q02253):
   3-oxopropanoate + NAD(+) + CoA + H2O = hydrogencarbonate + acetyl-CoA + NADH + H(+).
   This is the malonate-semialdehyde dehydrogenase (acetylating) activity → **GO:0018478**.
2. **Methylmalonate semialdehyde branch** (RHEA:20804, ECO:0000269|PubMed:23835272):
   2-methyl-3-oxopropanoate + NAD(+) + CoA + H2O = propanoyl-CoA + hydrogencarbonate + NADH + H(+).
   This is the methylmalonate-semialdehyde dehydrogenase (acylating, NAD) activity → **GO:0004491**.
   Both (R)- and (S)-2-methyl-3-oxopropanoate stereoisomers are handled (RHEA:76623, RHEA:76627).

Both malonate-SA and methylmalonate-SA activities are genuine, distinct MF facets of the same
enzyme; the human enzyme's methylmalonate-SA activity is directly evidenced (PubMed:23835272),
the malonate-SA (acetylating) activity is by similarity to the rat ortholog Q02253.

### GO:0004491 definition (OLS/go.db, verified)
"Catalysis of the reaction: 2-methyl-3-oxopropanoate + CoA + NAD+ = propanoyl-CoA +
hydrogencarbonate + NADH + H+. Can also use malonate (3-oxopropanoate) as a substrate. The
reaction occurs in two steps with the decarboxylation process preceding CoA-binding. Bicarbonate
rather than CO2 is released as a final product." — matches UniProt.

### GO:0018478 definition (OLS, verified)
"Catalysis of the reaction: 3-oxopropanoate + CoA + NAD(P)+ = acetyl-CoA + CO2 + NAD(P)H." —
matches UniProt malonate-semialdehyde branch. Current, non-obsolete, molecular_function.

## Pathway placement

MMSDH catalyzes the shared **distal step** of two catabolic pathways that converge on
methylmalonate/malonate semialdehyde (PMID:23835272 full text):

- **Valine catabolism**: "Metabolism of valine produces the intermediate (S)-3-hydroxyisobutyric
  acid (HIBA), which is oxidized to (S)-methylmalonic semialdehyde (MMSA) by 3-hydroxyisobutyrate
  dehydrogenase." [PMID:23835272]
- **Thymine catabolism (via β-alanine/aminoisobutyrate)**: "Thymine metabolism generates
  (R)-aminoisobutyric acid (AIBA), which is then deaminated to (R)-methylmalonic semialdehyde."
  [PMID:23835272]
- Both enantiomers of MMSA "are substrates for MMSDH, which catalyzes their oxidative
  decarboxylation to propionyl-CoA" [PMID:23835272].

Reactome R-HSA-70893: "Mitochondrial methylmalonate semialdehyde dehydrogenase (ALDH6A1)
catalyzes the reaction of methylmalonate semialdehyde, NAD+, and CoA to form propionyl-CoA, CO2,
and NADH + H+." Placed within R-HSA-70895 (Branched-chain amino acid catabolism).

Note: the beta-alanine branch (from uracil/cytidine and thymine) yields malonate semialdehyde →
acetyl-CoA, hence the malonate-SA (acetylating) activity GO:0018478 is the MF for that branch.

## Localization

- UniProt SUBCELLULAR LOCATION: "Mitochondrion {ECO:0000305|PubMed:23835272}."
  [file:human/ALDH6A1/ALDH6A1-uniprot.txt]
- Transit peptide 1..33 "/note=Mitochondrion" — targets the protein to the matrix.
- Reactome R-HSA-70893 places the reaction in the mitochondrial matrix (GO:0005759 TAS).
- HPA IDA (GO_REF:0000052) and MitoCarta HTP (PMID:34800366) confirm mitochondrial localization.
  PMID:23835272 notes "The only variants seen in the MitoCarta database ... both occurred in
  ALDH6A1", i.e. ALDH6A1 is a well-supported mitochondrial protein.
- Matrix (GO:0005759) is the most specific and correct compartment; plain "mitochondrion"
  (GO:0005739) annotations are correct but less specific.

## Subunit / structure

UniProt SUBUNIT: "Homotetramer." (by similarity to Q02253). Cryo-EM structures 8XXQ, 9IZU–9IZX
exist. Catalytic nucleophile Cys317 (ACT_SITE). Multiple NAD(+)-binding residues (BINDING 183,
185, 209, 212, 213, 262, 417; ECO:0000250|UniProtKB:P42412) support **NAD binding (GO:0051287)**
as a molecular function facet.

## Disease

UniProt DISEASE: Methylmalonate semialdehyde dehydrogenase deficiency (MMSDHD) [MIM:614105]:
"A metabolic disorder characterized by elevated beta-alanine, 3-hydroxypropionic acid, and both
isomers of 3-amino and 3-hydroxyisobutyric acids in urine organic acids."
(ECO:0000269|PubMed:10947204, PubMed:23835272) [file:human/ALDH6A1/ALDH6A1-uniprot.txt].

PMID:23835272 (Marcadier et al. 2013, Orphanet J Rare Dis, FULL TEXT available) is the key
functional/clinical paper and the source of the BHF-UCL IMP annotations:
- Reports the 4th molecularly confirmed MMSDH deficiency case, compound heterozygous
  p.Tyr172His / p.Arg535Cys in ALDH6A1.
- "Subsequent MMSDH enzyme assay demonstrated reduced activity in patient fibroblasts, measuring
  2.5 standard deviations below the mean" — i.e., direct enzyme-activity link between ALDH6A1
  genotype and MMSDH catalytic function. "Measured activity was 36 pmol/(min.mg protein) (normal
  range 51–184; mean 117; standard deviation ±33)."
- "MMSDH deficiency is an extremely rare, autosomal recessive disorder of valine and thymine
  metabolism." — supports both L-valine catabolic process (GO:0006574) and thymine catabolic
  process (GO:0006210) IMP annotations.

## Original cloning

PMID:1527093 (Kedishvili et al. 1992, JBC; abstract-only, full_text_available: false): cloned rat
and human MMSDH cDNA; "MMSDH clearly belongs to a superfamily of aldehyde dehydrogenases".
Provides the NAS mitochondrion annotation ("PCR was used to obtain the sequence of the 32 amino
acids corresponding to the mitochondrial entry peptide"). Human-clone identity confirmed.

## Annotation review decisions (summary)

- **GO:0004491 MMSDH (acylating, NAD) activity** — CORE MF. Multiple lines (IMP PMID:23835272,
  IBA, ISS, TAS Reactome, IEA). ACCEPT the experimental (IMP) and IBA; KEEP the redundant
  computational ones as non-core / accept.
- **GO:0018478 malonate-semialdehyde dehydrogenase (acetylating) activity** — CORE MF, NOT in GOA
  but strongly supported by the UniProt malonate-SA CATALYTIC ACTIVITY block; proposed in
  core_functions (β-alanine/uracil branch → acetyl-CoA).
- **GO:0051287 NAD binding** — CORE MF facet (7 BINDING residues in UniProt); added to
  core_functions.
- **GO:0006574 L-valine catabolic process** — CORE BP. ACCEPT (IMP + IBA).
- **GO:0006210 thymine catabolic process** — CORE BP. ACCEPT (IMP + IBA).
- **GO:0009083 branched-chain amino acid catabolic process** — TAS Reactome; correct but a
  higher-level parent of the valine-catabolism annotation. KEEP (ACCEPT) as a valid, broader BP.
- **GO:0005759 mitochondrial matrix** — CORE CC, most specific location. ACCEPT (TAS Reactome).
- **GO:0005739 mitochondrion** — correct but less specific than matrix (4 copies: IBA, IEA, IDA,
  HTP, NAS). ACCEPT the experimental IDA; keep the others (accurate parent term).
- **GO:0016491 oxidoreductase activity** — IEA InterPro; correct but far too general vs GO:0004491.
  MARK_AS_OVER_ANNOTATED (parent-of-specific-MF); could MODIFY to GO:0004491 but that term is
  already annotated.
- **GO:0003723 RNA binding** — HDA, PMID:22658674 (mRNA interactome capture, HeLa). A
  high-throughput proteome-wide RNA-crosslinking screen; MMSDH is a metabolic enzyme of the ALDH
  family with no established moonlighting RNA-regulatory role. Classic "enzyme caught in
  interactome capture" over-annotation. Experimental (HDA) so NOT REMOVE →
  MARK_AS_OVER_ANNOTATED.

## Core functions (final)

MF: GO:0004491 (methylmalonate-semialdehyde dehydrogenase, acylating NAD activity),
GO:0018478 (malonate-semialdehyde dehydrogenase, acetylating activity),
GO:0051287 (NAD binding).
BP: GO:0006574 (L-valine catabolic process), GO:0006210 (thymine catabolic process).
CC: GO:0005759 (mitochondrial matrix).
