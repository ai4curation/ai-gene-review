# Results

## Objective

Assess whether sequence evidence is sufficient to treat PP_2482 and PP_1969 as
equivalent to the reviewed KT2440 MoaA protein (PP_4597/Q88E69), and use the same
workflow as a control on the three KT2440 MobA-like proteins.

## Methods

`analyze_sequences.py` parsed repository-fetched UniProt flat files, or retrieved
the two explicit reviewed E. coli control accessions from the UniProt REST API.
It recorded sequence length, InterPro/PANTHER cross-references, requested motif
positions, current KEGG gene-to-orthology links, and global pairwise amino-acid
identity. KEGG links were retrieved from the KEGG REST API using the gene IDs
in the UniProt records. The global aligner used a match score of 1, mismatch
score of 0, gap-open score of -1, and gap-extension score of -0.1. Identity is
matches divided by positions at which both aligned sequences contain an amino
acid.

## MoaA-Family Findings

- All three KT2440 proteins have comparable lengths (322-337 aa), the canonical
  radical-SAM `CxxxCxxC` pattern near the N terminus, and two detected `CxxC`
  patterns. These features support radical-SAM/MoaA-like family membership but
  do not establish the same physiological substrate or pathway contribution.
- The reviewed MoaA sequence Q88E69 is the only one of the three with the
  MoaA-specific InterPro entries IPR013483 and IPR000385 in its UniProt record.
  All three share broader MoaA-like/radical-SAM entries and PTHR22960.
- Q88E69 is 36.25% identical to Q88K11 (PP_2482) and 37.85% identical to Q88LG4
  (PP_1969) over aligned residue pairs. Q88K11 and Q88LG4 are 66.15% identical
  to one another. This pattern supports a closer relationship between the two
  unreviewed candidates than either has to canonical moaA, and does not support
  assuming that all three are interchangeable copies.

The sequence analysis therefore supports keeping PP_2482 and PP_1969 as
MoaA-family candidates while reserving the unqualified GTP 3',8'-cyclase role
for Q88E69 unless gene-specific biochemical, genetic, or stronger phylogenetic
evidence resolves the paralogs.

## MobA-Like Control Findings

- The reviewed KT2440 MobA Q88HA3 is 34.59% identical to reviewed E. coli MobA
  P32173 and 30.99% identical to E. coli MocA Q46810.
- PP_2483 is more similar to the E. coli MobA control (39.29%) than to the E. coli
  MocA control (28.49%), whereas PP_4230 is more similar to MocA (39.62%) than to
  MobA (28.74%). PP_2483 and PP_4230 are 48.13% identical to one another.
- The generated KEGG link table maps both PP_2483 and PP_4230 to K07141. It maps
  the reviewed E. coli controls to distinct MobA (K03752) and MocA (K07141)
  orthologies, respectively.
- These modest identities are not sufficient by themselves to assign nucleotide
  specificity. PTHR43777:SF1 also contains reviewed proteins with non-MocA names,
  so family membership alone is not decisive. Independently of this sequence
  analysis, however, KEGG assigns both PP_2483 and PP_4230 to K07141
  (molybdenum-cofactor cytidylyltransferase), and both occur in
  molybdoenzyme-associated neighborhoods. The concordant orthology, subfamily,
  and neighborhood evidence supports a predicted MocA assignment while leaving
  CTP specificity and client delivery to direct experimental testing.

## Limits

This is a small, targeted sequence comparison, not a phylogenetic reconstruction
or activity assay. Motif presence and pairwise identity can test an equivalence
claim but cannot establish pathway necessity, substrate specificity, or in vivo
redundancy.

## Reproducibility Checklist

- [x] The analysis script accepts all inputs, motifs, and output paths as command-line arguments.
- [x] The same script was tested on a second, independently specified MobA-like input set.
- [x] Both analyses completed successfully with the pinned Biopython dependency.
- [x] Direct feature, KEGG-orthology, and pairwise-identity results are stored as TSV files in this directory.
- [x] Conclusions above are limited to the generated results and their stated provenance.
