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

---

# 2026-10-16: Function-level model scores (TIGR02666, MF_01225) and gene context

## Objective

The earlier section left open why NCBIfam TIGR02666 (moaA) and HAMAP MF_01225
do not match Q88LG4 (PP_1969) and Q88K11 (PP_2482). These are the models that
give reviewed KT2440 MoaA Q88E69 its GTP 3',8-cyclase name and EC 4.1.99.22.
This section scores all three KT2440 proteins against both models, finds
where along the model the paralogs lose score, checks whether those positions
are UniProt-annotated ligand positions, and records InterPro member-database
matches and the KEGG genome neighbourhood.

## Inputs and commands

Sequences: Q88E69, Q88LG4, Q88K11; reviewed MoaA from E. coli (P30745),
S. aureus (P69848, the HAMAP FT template), P. aeruginosa moaA1 and moaA2
(Q9HXD6, Q9I3K7); human MOCS1 (Q9NZB8, the MOCS1A-MOCS1B fusion); and KT2440
PqqE (Q88QV8) as a non-MoaA radical-SAM control. Models: NCBIfam TIGR02666.1
and TIGR02668.1 (archaeal MoaA) from hmm_PGAP release 20.0
(https://ftp.ncbi.nlm.nih.gov/hmm/current/), HAMAP profile MF_01225_B
(version 6) and rule MF_01225 (version 30) from hamap.expasy.org. Tools:
HMMER 3.4 and pftools 3.2.12 (Ubuntu packages `hmmer`, `pftools`), pyhmmer 0.12.3.

```
D=<scratch download dir outside the repo>
bash genes/PSEPK/PP_1969/PP_1969-bioinformatics/fetch_inputs.sh $D
# sha256: TIGR02666.1.HMM 11e76cc6...f114e9; TIGR02668.1.HMM f7cedcd8...254;
#         MF_01225_B.prf 7d7dc654...e22; MF_01225.rule.txt fbc3bc2b...27b1e; seqs.fasta 8355322f...f9f9
uv run --no-project --with pyhmmer==0.12.3 python -I \
  genes/PSEPK/PP_1969/PP_1969-bioinformatics/model_scores.py \
  --hmm $D/TIGR02666.1.HMM --hmm $D/TIGR02668.1.HMM \
  --prf $D/MF_01225_B.prf --rule $D/MF_01225.rule.txt --fasta $D/seqs.fasta \
  --ref-uniprot genes/PSEPK/moaA/moaA-uniprot.txt --ref Q88E69 \
  --targets Q88LG4,Q88K11 --canonical Q88E69,P30745,P69848,Q9HXD6,Q9I3K7,Q9NZB8 \
  --outdir genes/PSEPK/PP_1969/PP_1969-bioinformatics/model_scores_out \
  > genes/PSEPK/PP_1969/PP_1969-bioinformatics/model_scores.out
SSL_CERT_FILE=<proxy CA bundle, if behind a TLS proxy> uv run --no-project python -I \
  genes/PSEPK/PP_1969/PP_1969-bioinformatics/context_lookups.py \
  --uniprot Q88E69,Q88LG4,Q88K11,P30745 --loci PP_4597,PP_1969,PP_2482 --flank 6 \
  --outdir genes/PSEPK/PP_1969/PP_1969-bioinformatics/model_scores_out
```

`model_scores.py` runs `hmmsearch --max -E 1000 --domE 1000` and
`pfsearchV3 -f -n -a -o 1` (no heuristic, optimal alignment reported for every
sequence), keeps their native outputs in `model_scores_out/`, reads the
cutoffs from the model headers, and uses pyhmmer to walk the best-domain
alignment column by column. Per-position values are match-state emission
log-odds, log2(e_k(a)/f(a)) against the HMMER background; they ignore
transitions and the null2 correction, so they rank where score is lost but
do not sum to the bit score. The full per-position table is
`model_scores_out/TIGR02666_positions.tsv`. HAMAP rule FT conditions are
evaluated by mapping the rule template (P69848) positions through the
pfsearch alignment.

## Results

### NCBIfam TIGR02666 (moaA, model length 336; TC 284.05, NC 270.95)

| protein | full bits | E-value | domain bits | model span | vs TC | vs NC |
|---|---|---|---|---|---|---|
| Q88E69 (KT2440 moaA) | 375.6 | 8.8e-116 | 375.4 | 1-336 | +91.6 | +104.6 |
| Q88LG4 (PP_1969) | 269.2 | 2e-83 | 269.1 | 1-312 | -14.8 | -1.8 |
| Q88K11 (PP_2482) | 268.1 | 4.6e-83 | 267.9 | 1-313 | -15.9 | -2.9 |
| P30745 (E. coli MoaA) | 370.0 | 4.6e-114 | 369.8 | 1-336 | +86.0 | +99.0 |
| P69848 (S. aureus MoaA) | 402.8 | 4.6e-124 | 402.7 | 2-336 | +118.8 | +131.8 |
| Q9HXD6 (P. aeruginosa moaA1) | 371.1 | 2e-114 | 371.0 | 2-336 | +87.1 | +100.1 |
| Q9I3K7 (P. aeruginosa moaA2) | 374.8 | 1.5e-115 | 374.7 | 1-336 | +90.8 | +103.8 |
| Q9NZB8 (human MOCS1) | 372.6 | 7.3e-115 | 372.1 | 1-321 | +88.6 | +101.6 |
| Q88QV8 (KT2440 PqqE) | 81.0 | 3.6e-26 | 80.6 | 16-220 | -203.0 | -190.0 |

Both paralogs score just below the noise cutoff and about 15-16 bits below the
trusted cutoff. Every reviewed MoaA in the set, including the two
P. aeruginosa paralogs, scores 370-403 bits; the KT2440 paralogs sit about 100
bits below that group and about 190 bits above the PqqE control. They are a
distinct intermediate group, not borderline members of the canonical one.
The archaeal model TIGR02668 matches none of the sequences above its noise
cutoff (281.4); the paralogs score 197.8 and 203.7 there.

### HAMAP MF_01225_B (profile length 327; level 0 cutoff N_SCORE 35.254, level -1 8.5)

| protein | level | normalized score | raw | triggers rule |
|---|---|---|---|---|
| Q88E69 | 0 | 39.916 | 7172 | yes |
| Q88LG4 | -1 | 30.497 | 5240 | no |
| Q88K11 | -1 | 30.560 | 5253 | no |
| P30745 | 0 | 37.985 | 6776 | yes |
| P69848 | 0 | 41.359 | 7468 | yes |
| Q9HXD6 | 0 | 40.501 | 7292 | yes |
| Q9I3K7 | 0 | 41.841 | 7567 | yes |
| Q9NZB8 | 0 | 36.406 | 6452 | yes |
| Q88QV8 | -1 | 10.865 | 1213 | no |

Both paralogs reach only the level -1 (weak) cutoff, about 4.7 normalized
units below the level 0 cutoff that triggers the rule; every reviewed MoaA in
the set passes level 0. The rule's other conditions would be met: their lengths
(337, 322 aa) are inside the Bacteria size range 318-378, and all 14 FT
binding conditions of the Bacteria case (template P69848) are satisfied in
both paralogs, as they are in every canonical MoaA (PqqE fails eight).
So the HAMAP non-match is a profile-score failure only.

### Where the paralogs lose TIGR02666 score

- No missing segment explains it. The best domain covers model positions
  1-312 (Q88LG4) and 1-313 (Q88K11), with 12 deleted match states each, the
  same order as canonical MoaA (6-12). The unaligned model end (313-336,
  consensus `...msqiGG`) corresponds to a divergent C-terminal tail that is
  still present in both paralogs and still ends in Gly-Gly (Q88LG4
  `VAFSGGVTVMKVIGG`, Q88K11 `TFTGSALIMKSVGG`), but does not align to the model.
- The deficit is spread along the whole model. Summed emission log-odds are
  427.6 bits on average for the six canonical MoaA and 329.3 (Q88LG4) and
  321.4 (Q88K11) for the paralogs. The largest window deficits are in the
  N-terminal radical-SAM region (model 1-60: -33.1 and -36.1 bits) and the
  C-terminal twitch region and tail (model 281-336: -26.1 and -27.0 bits),
  with smaller losses through most of the TIM barrel.
- All 17 Q88E69 UniProt binding positions fall on TIGR02666 match states, are
  aligned with posterior probability `*` (>0.95) in all three proteins, and
  carry identical residues with identical emission scores in the paralogs,
  except model 266 (Q88E69 V266, paralogs Leu; 1.17 vs 0.85 bits).
  None of the score loss is at an annotated ligand position.
- Eight model positions are conserved (>= 1 bit) in all six canonical MoaA and
  negative or gapped in both paralogs: model 22/23 (Q88E69 F29, R30; paralogs
  Y, A: the CNYAC positions that break PS01305, one and two residues from
  cluster cysteines C27 and C31), 47 (E52; A/S), 51 (V56; G/A), 73 (R78, Arg
  in all six canonical; Ser in both paralogs, five residues from SAM-binding
  G73), 254 (P254; N), 287 (K287; G) and 314 (H315; unaligned). None is a
  UniProt-annotated ligand position; whether any of them is functionally
  important for GTP binding or catalysis was not established here.

### InterPro member-database matches (InterPro API)

All four proteins match PF04055, PF06463, cd01335, PS51918, SM00729,
SSF102114, G3DSA:3.20.20.70, PANTHER PTHR22960 and the same four SFLD groups
(including SFLDG01383, cyclic pyranopterin phosphate synthase). Matched only
by Q88E69 and E. coli P30745 are NCBIfam TIGR02666 (E 6.7e-109 and 3.5e-107),
HAMAP MF_01225_B, PROSITE PS01305 and CDD cd21117 (the MoaA C-terminal twitch
model; E 5.8e-23 and 5.9e-27). The paralogs therefore lack every
function-level MoaA signature in InterPro, including one (cd21117) not
considered earlier. Table: `model_scores_out/interpro_matches.tsv`.

### Genome neighbourhood (KEGG, +/- 6 loci)

- PP_4597 (moaA): moaB (PP_4600) three genes downstream; no other moa genes in
  the window.
- PP_1969: no molybdenum-cofactor or molybdoenzyme gene in the window
  (neighbours are a TetR-family regulator, a putative lipoprotein,
  DNA polymerase III delta', TatD, aromatic-amino-acid aminotransferase,
  UvrB); two locus numbers (PP_1965, PP_1973) returned no KEGG entry.
- PP_2482: same strand as, and directly downstream of, PP_2477-PP_2481
  (isoquinoline 1-oxidoreductase alpha and beta subunits, K07302/K07303, a
  cytochrome c family protein, a putative xanthine dehydrogenase accessory
  factor, and a protein of unknown function; PP_2481 ends inside PP_2482).
  PP_2483 (K07141, molybdenum cofactor cytidylyltransferase) is adjacent on
  the opposite strand. This is a molybdoenzyme cluster.
- Table: `model_scores_out/kegg_neighbourhood.tsv`.

## Interpretation

The TIGR02666 and MF_01225 non-matches are not explained by a missing
non-catalytic segment. The paralogs lose score across the whole length,
mainly in the N-terminal radical-SAM region and the C-terminal twitch/tail,
at positions that every canonical MoaA in the set conserves, while every
annotated ligand position is retained. Ligand-site conservation is expected
of a MoaA-derived paralog whatever its present substrate, so it cannot by
itself separate a GTP 3',8-cyclase from a diverged MoaA-like enzyme.
The paralogs form a distinct group about 100 bits below every reviewed MoaA,
including the two P. aeruginosa paralogs that both pass the function-level
models.

Gene context differs between the two. PP_2482 sits in a cluster with an
isoquinoline-oxidoreductase-type molybdoenzyme, an XdhC-like accessory factor
and a MocA-like cytidylyltransferase, which ties it to molybdenum-cofactor
use by that enzyme; PP_1969 has no such context. A Moco-related context for
PP_2482 is compatible with a dedicated GTP 3',8-cyclase but does not show
which reaction it catalyses.

## Limits

Single-model scoring plus emission-only position decomposition; no
phylogeny, structure or activity data. The HAMAP result is the profile
score; the rule's Bacteria FT conditions were evaluated through the same
pfsearch alignment. KEGG and InterPro results reflect those services on
2026-10-16.
