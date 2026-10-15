# Results: ligand-binding residue conservation in KT2440 MoaA paralogs

## Objective

Test whether the two unreviewed KT2440 MoaA-family paralogs, Q88LG4 (PP_1969) and
Q88K11 (PP_2482), retain the substrate (GTP), S-adenosyl-L-methionine and
[4Fe-4S]-cluster binding residues of reviewed KT2440 MoaA Q88E69 (PP_4597). The
earlier comparison in `genes/PSEPK/moaA/moaA-bioinformatics/RESULTS.md` recorded
motif presence, InterPro split and pairwise identity but did not map individual
ligand-binding positions. This analysis was run during re-review of the
TreeGrafter GO:0061798 rows after a blinded OpenScientist run, to check the run's
active-site claims independently.

## Methods

`map_moaA_sites.py` parses the FT BINDING lines (with ligand names) from the
repository UniProt flat file of Q88E69, aligns Q88E69 globally (Biopython
PairwiseAligner, BLOSUM62, gap open -10, extend -0.5) to Q88K11, Q88LG4 and
reviewed E. coli MoaA P30745 (`P30745_Ecoli_MoaA.fasta`, downloaded from the
UniProt REST API), and reports the aligned residue at each annotated binding
position. It also scans each sequence with the PROSITE PS01305
(MOAA_NIFB_PQQE) pattern copied from the ExPASy PROSITE entry. Raw output is in
`map_moaA_sites.out`. Command:

```
uv run --no-project --with biopython python -I \
  genes/PSEPK/PP_1969/PP_1969-bioinformatics/map_moaA_sites.py \
  genes/PSEPK/moaA/moaA-uniprot.txt genes/PSEPK/PP_2482/PP_2482-uniprot.txt \
  genes/PSEPK/PP_1969/PP_1969-uniprot.txt \
  genes/PSEPK/PP_1969/PP_1969-bioinformatics/P30745_Ecoli_MoaA.fasta
```

## Findings

- All 17 UniProt-annotated binding positions of Q88E69 (seven GTP-binding
  positions, i.e. four single residues plus the 265..267 span; four SAM-binding residues; and the six
  cysteines of the two [4Fe-4S] clusters) align to identical residues in Q88LG4 and
  Q88K11, except Q88E69 V266, which is Leu in both paralogs. E. coli MoaA P30745
  also carries Leu at that position (L263), so the paralogs match the
  experimentally characterized E. coli enzyme there.
- Mapped positions: Q88LG4 R29, C36, C40, Y42, C43, R79, G83, T109, S133, K169,
  M203, C268, C271, R273, L274, R275, C285; Q88K11 R14, C21, C25, Y27, C28, R64,
  G68, T94, S118, K154, M188, C253, C256, R258, L259, R260, C270.
- The PROSITE PS01305 pattern matches Q88E69 and E. coli MoaA but not the two
  paralogs. Both paralogs read `CNYAC` where the pattern requires
  `C-[NDP]-[LIVMF]-[DNQRS]-C`; the two failing positions lie between the first
  and second cluster cysteines and are not among the annotated ligand residues.
  The failure of the signature therefore reflects substitutions at non-ligand
  positions inside an intact CxxxCxxC motif.
- Global identities with this scoring scheme: Q88LG4 vs E. coli MoaA 37.11%,
  Q88E69 vs E. coli MoaA 36.92%, Q88K11 vs E. coli MoaA 33.54%; Q88K11 vs Q88LG4
  66.15%. The two paralogs are about as similar to characterized E. coli MoaA as
  the reviewed KT2440 MoaA is.

## Interpretation

The divergence of PP_1969 and PP_2482 from canonical KT2440 MoaA does not touch the
annotated GTP-, SAM- or cluster-binding residues. Retaining the full GTP-binding
set argues against a change of substrate, which was the main open question in the
earlier comparison. The missing MoaA-specific database records (NCBIfam TIGR02666,
HAMAP MF_01225, PROSITE PS01305, InterPro IPR013483/IPR000385) are consistent with
overall sequence divergence; for PS01305 the cause is identified above. The reason
TIGR02666 and HAMAP MF_01225 do not match was not examined here.

## Limits

Pairwise alignment to one reference, not a phylogeny or a structure-based
alignment. Conservation of binding residues supports, but does not demonstrate,
GTP 3',8'-cyclase activity; no PP_1969 or PP_2482 assay exists. The analysis says
nothing about which paralog carries molybdenum-cofactor flux in vivo.
