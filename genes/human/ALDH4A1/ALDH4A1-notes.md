# ALDH4A1 (P30038) review notes

Gene: ALDH4A1 (aka ALDH4, P5CDH). Human. UniProt P30038. 563 aa precursor;
N-terminal mitochondrial transit peptide (residues 1-24), mature chain 25-563.

## Core identity and function

ALDH4A1 is the **mitochondrial NAD+-dependent delta-1-pyrroline-5-carboxylate
dehydrogenase (P5CDH)**, an aldehyde dehydrogenase (ALDH superfamily, ALDH4
family). It catalyzes the **second (final) step of proline catabolism**:
oxidation of L-glutamate-5-semialdehyde (glutamate gamma-semialdehyde, GSA,
in spontaneous equilibrium with its cyclic tautomer delta-1-pyrroline-5-carboxylate,
P5C) to L-glutamate, using NAD+.

- EC 1.2.1.88 [file:human/ALDH4A1/ALDH4A1-uniprot.txt "EC=1.2.1.88"].
- Reaction [file:human/ALDH4A1/ALDH4A1-uniprot.txt
  "Reaction=L-glutamate 5-semialdehyde + NAD(+) + H2O = L-glutamate + NADH"].
- Function statement [file:human/ALDH4A1/ALDH4A1-uniprot.txt
  "Irreversible conversion of delta-1-pyrroline-5-carboxylate"] "(P5C), derived
  either from proline or ornithine, to glutamate. This is a necessary step in the
  pathway interconnecting the urea and tricarboxylic acid cycles."
- Pathway [file:human/ALDH4A1/ALDH4A1-uniprot.txt
  "Amino-acid degradation; L-proline degradation into L-"] "glutamate;
  L-glutamate from L-proline: step 2/2."
- Location [file:human/ALDH4A1/ALDH4A1-uniprot.txt "Mitochondrion matrix."].
- Homodimer [file:human/ALDH4A1/ALDH4A1-uniprot.txt "Homodimer."].

The substrate P5C/GSA is generated from proline by proline dehydrogenase (PRODH),
and from ornithine by ornithine aminotransferase; thus P5CDH sits at the node
interconnecting the urea and TCA cycles (glutamate is fed into central metabolism)
[PMID:22516612 "GSA is the hydrolysis product of Δ1-pyrroline-5-carboxylate (P5C),
which is generated from proline by proline dehydrogenase (PRODH)"; "GSA is also
produced from ornithine by ornithine aminotransferase"].

Cloning/characterization: two full-length human P5CDh cDNAs encode a 563-residue
protein; expression in P5CDh-deficient yeast confers P5CDH activity and growth on
proline [PMID:8621661 "a mitochondrial matrix NAD(+)-dependent dehydrogenase,
catalyzes the second step of the proline degradation pathway"; "Both conferred
measurable P5CDh activity and the ability to grow on proline as a sole nitrogen
source"]. (Note: this 1996 paper used the older EC 1.5.1.12; current EC is 1.2.1.88.)

## Dual substrate specificity: hydroxyproline catabolism

Human P5CDH is **also the second enzyme of hydroxyproline (4-Hyp) catabolism**.
By analogy to proline, trans-4-hydroxy-L-proline is oxidized to
1-pyrroline-3-hydroxy-5-carboxylate (3OH-P5C) by hydroxyproline oxidase; the
nonenzymatic hydrolysis product 4-hydroxyglutamate semialdehyde (OH-GSA) is then
oxidized by P5CDH to 4-erythro-hydroxy-L-glutamate (OH-Glu)
[PMID:22516612 "P5CDH is also the second enzyme of hydroxyproline catabolism in
humans"; "which is oxidized to 4-erythro-hydroxy-L-glutamate (OH-Glu) by P5CDH"].
The GO term GO:0003842 explicitly covers this dual activity ("The activity can also
oxidize other 1-pyrrolines, e.g. oxidation of 3-hydroxy-1-pyrroline-5-carboxylate to
4-hydroxyglutamate") per its OLS definition.

PMID:21998747 (Riedel et al. 2011) is primarily about HOGA1 (4-hydroxy-2-oxoglutarate
aldolase), the terminal enzyme of the 4-Hyp pathway, but its Figure 1 / pathway
description places 1P5CDH as the second of four mitochondrial 4-Hyp-degrading enzymes
[PMID:21998747 "the step-wise action of four mitochondrial enzymes: hydroxyproline
oxidase (HPOX), Δ1-pyrroline-5-carboxylate dehydrogenase (1P5CDH), aspartate
aminotransferase (AspAT), and 4-hydroxy-2-oxoglutarate aldolase (HOGA"]. This supports
GO:0019470 (trans-4-hydroxy-L-proline catabolic process) TAS for ALDH4A1.

## Structure and mechanism

First human P5CDH crystal structure solved by Srivastava et al. 2012 (PMID:22516612).
Classic ALDH fold: N-terminal NAD+-binding (Rossmann-like) domain, C-terminal
catalytic domain furnishing the essential cysteine nucleophile Cys348 and
substrate-binding Ser349, plus an oligomerization domain. Homodimer (domain-swapped),
~122 kDa in solution [PMID:22516612 "This domain furnishes the essential cysteine
nucleophile (Cys348) and several residues that bind GSA, including Ser349";
"The molar mass is estimated to be 122 kDa"]. Kinetics: Km(NAD+)=100 uM,
Km(L-P5C)=32 uM, kcat=10 s-1 for wild-type HsP5CDH.

Mechanism (general ALDH): nucleophilic attack by conserved Cys on the aldehyde C to
form a hemithioacetal, hydride transfer to NAD+ giving a thioacyl intermediate and
NADH, then hydrolysis to the carboxylic acid product.

## Disease: type II hyperprolinemia (HYRPRO2)

Autosomal recessive; deficiency of P5CDH causes accumulation of P5C and proline
[file:human/ALDH4A1/ALDH4A1-uniprot.txt "Hyperprolinemia 2 (HYRPRO2)"; PMID:22516612
"Type II hyperprolinemia is an autosomal recessive disorder caused by a deficiency
in Δ(1)-pyrroline-5-carboxylate dehydrogenase (P5CDH; also known as ALDH4A1)"].
The disease mutation S352L abolishes catalytic activity and eliminates NAD+ binding
by inducing an ~8 Å rearrangement of the catalytic loop [PMID:22516612 "Mutation of
Ser352 to Leu is shown to abolish catalytic activity and eliminate NAD(+) binding"].
S352L and variant P16L were originally reported by Geraghty et al. 1998
(PubMed:9700195; not in local publications cache).

## Localization evidence

- Mitochondrion matrix (UniProt subcellular location, and TAS from Reactome + Hu 1996)
  [file:human/ALDH4A1/ALDH4A1-uniprot.txt "Mitochondrion matrix."].
- Mitochondrion IDA from HPA (immunofluorescence, GO_REF:0000052).
- Mitochondrion HTP from PMID:34800366 (quantitative high-confidence human
  mitochondrial proteome). Abstract-only in cache; consistent with all other evidence.
All localization evidence is mutually consistent; mitochondrial matrix is the specific,
authoritative location.

## Protein interactions

- Homodimer / identical protein binding (GO:0042802), IPI PMID:22516612 (self;
  With/From UniProtKB:P30038) — supported by the structural + AUC data showing a dimer.
- protein binding (GO:0005515), IPI PMID:32814053 with UniProtKB:Q09028 (RBBP4).
  PMID:32814053 is a large-scale Y2H neurodegenerative-disease interactome map
  (abstract-only in cache; does not describe ALDH4A1 specifically). UniProt records the
  RBBP4 interaction [file:human/ALDH4A1/ALDH4A1-uniprot.txt
  "P30038; Q09028: RBBP4"]. Bare "protein binding" is uninformative and this is a
  single high-throughput Y2H hit with no known biological role for ALDH4A1; keep as
  non-core.

## Annotations to watch (over-annotation / generality)

- GO:0016491 oxidoreductase activity (IEA, InterPro): correct but a very general
  parent of the specific catalytic term; over-annotation relative to GO:0003842.
- GO:0004029 aldehyde dehydrogenase (NAD+) activity (IDA, CACAO from PMID:4015840):
  a more general ALDH-family MF. PMID:4015840 (Hopkinson et al. 1985) is a biochemical-
  genetic survey of ALDH isozymes; its abstract discusses ALDH1/ALDH2/ALDH3 and does
  not mention ALDH4/P5CDH. Full text unavailable in cache; cannot verify it assays
  ALDH4A1. Per policy (experimental IDA, do not REMOVE), keep the correct-but-general
  GO:0004029 as non-core and defer to the curator; the specific activity GO:0003842 is
  the core MF.
- GO:0005739 mitochondrion (IDA/HTP): correct but less specific than the
  mitochondrial matrix (GO:0005759) location.

## Core function summary

1. MF: L-glutamate gamma-semialdehyde / 1-pyrroline-5-carboxylate dehydrogenase
   activity, NAD+-dependent (GO:0003842, EC 1.2.1.88).
2. BP: L-proline catabolic process to L-glutamate (GO:0006562) — 2nd/final step.
3. BP: trans-4-hydroxy-L-proline catabolic process (GO:0019470) — dual substrate.
4. CC: mitochondrial matrix (GO:0005759).
</content>
</invoke>
