# Naked mole-rat Cd44 (A0AAX6R0R7): isoform architecture and hyaluronan-binding site

## Question

Two things about the naked mole-rat (NMR) CD44 reference protein could not be settled
from the UniProt record alone:

1. The TrEMBL entry A0AAX6R0R7 is 701 aa and carries **no** `ALTERNATIVE PRODUCTS` or
   `VAR_SEQ` annotation, so the record itself says nothing about which CD44 splice form
   the RefSeq gene model XP_012930388.1 represents. CD44 is one of the most heavily
   alternatively spliced genes in the genome (human P16070 has 19 annotated isoforms),
   and the distinction between the short *standard* form (CD44s) and the long
   *variant-exon-containing* forms (CD44v) matters for several GO annotations.
2. The entry carries a `CAUTION` from the Link-domain ProRule:
   `Lacks conserved residue(s) required for the propagation of feature annotation`
   (PROSITE-ProRule PRU00323). Read carelessly this could be taken to mean the
   hyaluronan-binding module is degenerate, which would undercut
   `GO:0005540 hyaluronic acid binding` — the gene's core molecular function.

## Method

`cd44_isoform_architecture.py` performs a global Needleman-Wunsch alignment (BLOSUM62,
gap open -11, extend -1, Biopython `PairwiseAligner`) of A0AAX6R0R7 against human
P16070-1 (742 aa, the full variant-exon-containing canonical form), then maps
UniProt-annotated human landmark positions through the alignment. Landmarks are read
from the two UniProt flat files, not assumed:

| Landmark | Human P16070 | Source |
|---|---|---|
| Link domain | 32–120 | `FT DOMAIN` (PROSITE PS50963) |
| Link-region disulfide cysteines | 28, 53, 77, 97, 118, 129 | `FT DISULFID 28..129, 53..118, 77..97` |
| Hyaluronan-contact residues | 41, 78, 79, 105 | `FT BINDING /ligand="hyaluronan"` |
| Stem region | 224–649 | `FT REGION /note="Stem"` |
| Alternatively spliced insert | 223–535 | `VSP_022797` "Missing (in isoform 11)" |
| Transmembrane helix | 650–670 | `FT TRANSMEM` |

The variant-exon test is: if the NMR protein were a *standard* CD44s form, human
residues 223–535 (the segment removed in the short human isoform 11 / CD44R2) would
have no aligned counterpart. Sequences are fetched from the UniProt REST API and
cached beside the script; results are written to `cd44_isoform_architecture.json`.

Reproduce with:

```
uv run --with biopython python cd44_isoform_architecture.py
```

## Results

```
human_length                              742
hetga_length                              701
percent_identity_over_aligned            77.3
human_link_domain_32_120_aligned        89/89
human_TM_650_670_aligned                21/21
human_variant_insert_223_535_aligned   270/313  (86.3%)
percent_identity_link_domain_32_120      92.1
percent_identity_variant_insert_223_535  74.1
percent_identity_cytoplasmic_tail        97.2
hetga_ectodomain_len_after_signal         588
human_ectodomain_len_after_signal         629
```

Residue-level correspondence:

| Human landmark | NMR counterpart |
|---|---|
| R41 (hyaluronan) | R43 |
| R78 (hyaluronan) | R80 |
| Y79 (hyaluronan) | Y81 |
| Y105 (hyaluronan) | Y107 |
| C28 / C129 (disulfide) | C30 / C132 |
| C53 / C118 (disulfide) | C55 / C120 |
| C77 / C97 (disulfide) | C79 / C99 |

## Interpretation

**1. The reference protein is a variant-exon-containing (CD44v-like) gene model, not
CD44s.** 86% of the human alternatively spliced insert (223–535) has an aligned NMR
counterpart, and the NMR ectodomain is 588 residues against 629 for the full-length
human canonical form. A standard CD44s model would be several hundred residues shorter.
This is a statement about the RefSeq gene model that UniProt happens to have selected as
the reference protein for this gene; it is **not** evidence about which splice forms NMR
tissues actually express, which no cached study reports. The variant region is also the
least conserved part of the protein (74.1% identity), as expected for a mucin-like,
heavily O-glycosylated stem.

**2. The hyaluronan-binding module is intact.** All four UniProt-annotated
hyaluronan-contact residues of human CD44 and all six cysteines forming the three
Link-region disulfides have direct counterparts in the NMR sequence, and the Link domain
is 92.1% identical to human — the most conserved region of the ectodomain. The PRU00323
`CAUTION` is a feature-*propagation* flag (the rule declines to auto-transfer its
`DISULFID` features when its profile-position conditions are not met); it is not a
finding that the hyaluronan-binding site is degenerate, and the residues that matter are
present.

**3. The cytoplasmic tail is the single most conserved region (97.2% identity).** That
is the segment through which CD44 couples to ERM proteins and to NF2/merlin, the
interaction through which naked mole-rat hyaluronan signalling arrests proliferation
(PMID:23783513).

## Limitations

This is a sequence-architecture analysis of one predicted gene model against one human
reference sequence. It establishes that the residues required for hyaluronan binding are
present; it does **not** measure binding, and it says nothing about affinity, about the
splice repertoire expressed in NMR tissue, or about post-translational modification
(glycosylation state gates CD44 hyaluronan binding and is not addressed here).
