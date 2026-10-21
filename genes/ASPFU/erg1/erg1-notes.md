# erg1 (ASPFU, UniProt E9R5G2) notes

## Deep research

- The falcon/perplexity-lite deep-research recipe was attempted for `ASPFU erg1` and failed because this worktree has no `agentapi` and no provider API key. No provider-named deep-research file was created.

## Manual literature and database notes

- UniProt E9R5G2 is the reviewed Af293 Erg1 record for `AFUA_5G07780`; it places the protein in PANTHER `PTHR10835:SF0`, the squalene monooxygenase subfamily, and gives the reaction `squalene + reduced [NADPH--hemoprotein reductase] + O2 = (S)-2,3-epoxysqualene + oxidized [NADPH--hemoprotein reductase] + H2O + H(+)` by similarity to S. cerevisiae Erg1.
- Liu et al. 2004 is the best direct A. fumigatus primary paper for the gene identity: multicopy `ERG1` conferred terbinafine resistance, and "DNA sequence analysis identified the gene responsible for TRB resistance as the A. fumigatus squalene epoxidase gene (ERG1), which encodes the target enzyme of TRB." [PMID:15215099].
- UniProt cites Ferreira et al. 2005 for the `erg1` gene name and pathway annotation. The local cache is abstract-only; the abstract supports broad pathway context, including that "About 20 genes are involved in the A. fumigatus ergosterol biosynthesis pathway." [PMID:16110826].
- Rocha et al. 2006 showed target-site resistance with an engineered A. fumigatus allele: "The equivalent mutation was engineered into the ergA gene of Aspergillus fumigatus, resulting in an F389L substitution that also conferred resistance to this pathogenic mold." [PMID:16801438]. This confirms Erg1/ErgA as the allylamine target but does not add a distinct GO annotation beyond squalene monooxygenase activity.
- Alcazar-Fuoli et al. 2008 measured the sterol composition of A. fumigatus strains and ergosterol-pathway mutants; the local cache is abstract-only and does not directly assay `erg1` [PMID:18191972].
- Liebl et al. 2023 used conditional `erg1` strains and terbinafine treatment to validate an isoprenoid GC-MS assay; decreased `erg1` expression and terbinafine treatment both increased squalene [PMID:37504756 "The decreased expression of erg1 as well as terbinafine treatment led to an increased squalene content."].
- PANTHER `PTHR10835` puts E9R5G2 in `PTHR10835:SF0` and the family review assesses the relevant PAINT nodes as sound: `PTN000089417` supports squalene monooxygenase activity and endoplasmic reticulum, while fungal node `PTN000851137` supports ergosterol biosynthetic process.

## Curation decisions

- Accepted all squalene monooxygenase activity, ER/ER membrane, ergosterol biosynthesis, and sterol biosynthesis rows. The three IBA rows follow the PTHR10835 family review and cite the exact PAINT IBD lines.
- Modified generic `membrane` to `endoplasmic reticulum membrane`.
- Modified ARBA `sterol metabolic process` to fungal `ergosterol biosynthetic process`.
- Kept `flavin adenine dinucleotide binding` as non-core because it is a conserved cofactor interaction supporting the monooxygenase reaction.
