# Pairwise comparison of the Actinomortierella ambigua SUCLG2-type beta subunit (A0A9P6TY68)

Analysis: `scs_beta_comparison.py`, run with `uv run --script scs_beta_comparison.py` on 2026-11-18.
Output: `results.yaml` (all numbers below).
Sequences and annotations are fetched from UniProt at run time.

## What was done

- Inventory of the succinyl-CoA synthetase subunits of the organism: every UniProt entry of taxon 1343610 with a PANTHER PTHR11815 (beta) or PTHR11117 (alpha) cross-reference.
- Pairwise global alignments of A0A9P6TY68 (409 residues, sequence version 1) with ten reference beta subunits and with the second beta subunit of the same organism. Settings: BLOSUM62, gap open -10, gap extend -0.5, end gaps free. Identity is the number of identical residues over the columns in which both sequences have a residue.
- Residue correspondences read from the same alignments.
- Comparison of the N-terminus with the two closest ortholog models, read from the same alignments.

This is not a phylogenetic analysis. No tree was built that contains A0A9P6TY68.

## Results

### 1. The organism has one alpha subunit and two beta subunits

| Accession | Gene | Length | PANTHER | HAMAP profiles |
|---|---|---|---|---|
| A0A9P6PU00 | SUCLG1 | 327 | PTHR11117:SF2 | MF_01988 |
| A0A9P6Q632 | TCA9 | 439 | PTHR11815:SF1 | MF_00558, MF_03220 |
| A0A9P6TY68 | SUCLG2 | 409 | PTHR11815:SF10 | MF_00558 |

Actinomortierella ambigua has three succinyl-CoA synthetase entries in UniProt: one alpha subunit (A0A9P6PU00) and two beta subunits (A0A9P6TY68 and A0A9P6Q632).
The gene names are those given by the submitter.
A0A9P6Q632 matches the HAMAP profile of ATP-specific eukaryotic beta subunits (MF_03220); A0A9P6TY68 matches only the general beta-subunit profile (MF_00558).

### 2. A0A9P6TY68 is closest to the Mortierellomycota genes that group with SUCLG2

| Compared with | Identity | Aligned columns |
|---|---|---|
| Linnemannia elongata A0A197JV50 | 80.3% | 402 |
| Lobosporangium transversale A0A1Y2H5W1 | 78.5% | 409 |
| Monosiga brevicollis A9UVA2 | 62.8% | 395 |
| human SUCLG2 Q96I99 | 56.9% | 406 |
| pig SUCLG2 P53590 | 56.6% | 408 |
| Dictyostelium discoideum scsB Q869S7 | 55.3% | 407 |
| Actinomortierella ambigua TCA9 A0A9P6Q632 (same organism) | 52.5% | 408 |
| human SUCLA2 Q9P2R7 | 49.8% | 404 |
| Blastocystis SCSb B3FHP0 | 46.5% | 404 |
| E. coli SucC P0A836 | 45.7% | 387 |
| S. cerevisiae LSC2 P53312 | 44.6% | 406 |

A0A9P6TY68 is 80.3% identical to Linnemannia elongata A0A197JV50 and 78.5% identical to Lobosporangium transversale A0A1Y2H5W1, the two Mortierellomycota Gln20 genes that group with human SUCLG2 in the trees of `genes/yeast/LSC2/LSC2-bioinformatics`.
A0A9P6TY68 is more similar to human SUCLG2 (56.9%) than to the second beta subunit of its own genome, A0A9P6Q632 (52.5%), and more similar to human SUCLG2 than to human SUCLA2 (49.8%).
Pairwise identity is not a tree. The LSC2 analysis shows that identity alone can fail to separate the two lineages (LSC2 is 46.3% identical to SUCLA2 and 45.1% to SUCLG2). The assignment of A0A9P6TY68 to the SUCLG2-type lineage therefore rests on its close similarity to two genes whose placement was tested, and on the TreeGrafter placement recorded in its GO annotations, not on a tree of its own.

### 3. Residue correspondences

| Reference residue | Residue of A0A9P6TY68 | Note |
|---|---|---|
| E. coli SucC Pro20 | Gln34 | position 20 of the mature subunit |
| pig SUCLG2 Gln58 | Gln34 | UniProt GTP binding site of P53590 |
| human SUCLG2 Gln57 | Gln34 | |
| E. coli SucC Lys46 | Lys60 | ATP site of the HAMAP rule |
| E. coli SucC Glu107 | Glu128 | ATP site of the HAMAP rule |
| E. coli SucC Asn199 | Asn220 | Mg site of the HAMAP rule |
| E. coli SucC Asp213 | Asp234 | Mg site of the HAMAP rule |
| E. coli SucC Asn264 | Asn285 | substrate site of the HAMAP rule |
| E. coli SucC Gly321-Ile322-Val323 | Gly342-Ile343-Ala344 | substrate motif of the HAMAP rule |

Gln34 of A0A9P6TY68 aligns with Pro20 of E. coli SucC, Gln58 of pig SUCLG2 (P53590) and Gln57 of human SUCLG2 (Q96I99).
The residues that the UniProt record lists as ATP, magnesium and substrate sites (Lys60, Glu128, Asn220, Asp234, Asn285) are identical to the aligned residues of E. coli SucC.
The third residue of the substrate motif is Ala344, where E. coli SucC has Val323. This may be the residue behind the UniProt caution that the entry lacks a conserved residue required for feature propagation; UniProt does not say which residue failed, so this is a reading of the alignment.

### 4. N-terminus

Met1 of E. coli SucC aligns with Leu15 of A0A9P6TY68, so the gene model has 14 residues (MPIQRGIVASQVRF) ahead of the conserved core.
The 14 residues contain two basic residues (Arg5, Arg13) and no acidic residue.
No targeting-sequence predictor was run, and the start codon of the gene model has not been checked against transcript data.

Comparison with the two closest ortholog models, read from the same pairwise alignments (`n_terminal_comparison_with_orthologs` in `results.yaml`):

| Ortholog model | Length | Residues ahead of the residue aligned with Leu15 of A0A9P6TY68 | Arg + Lys | Asp + Glu |
|---|---|---|---|---|
| Linnemannia elongata A0A197JV50 | 402 | 7 (MASQVRH) | 1 | 0 |
| Lobosporangium transversale A0A1Y2H5W1 | 439 | 40 (MLRHAFKQRVPTIGMARPLLVQRQLPTLAAKAFVASQVRF) | 7 | 0 |

Residues 9 to 13 of A0A9P6TY68 (ASQVR) are identical in both ortholog models, and only residues 1 to 8 (MPIQRGIV) are specific to this model.
The Linnemannia model starts one residue before that shared motif, so its seven-residue difference in length from A0A9P6TY68 lies entirely at the N-terminus.
Lobosporangium transversale A0A1Y2H5W1 has 40 residues ahead of the residue aligned with Leu15, with seven basic residues and no acidic residue, of which the last seven (VASQVRF) are identical to residues 8 to 14 of A0A9P6TY68.
The three models therefore disagree on the start. The 14 residues of A0A9P6TY68 are not a model-specific extension of presequence length: five of them (9 to 13) are identical in both ortholog models and seven (8 to 14) in the Lobosporangium model, and a long basic leader of the kind expected of a mitochondrial presequence is present only in the Lobosporangium model. A truncated or mis-called start in A0A9P6TY68 (and in the Linnemannia model) is the simpler reading; it was not tested against genomic or transcript sequence.

## Limitations

- Pairwise alignments only; no tree, no bootstrap.
- The sequence is an unreviewed gene model from a draft whole-genome shotgun assembly.
- Residue correspondences come from one alignment per pair with one set of gap penalties.
- Nothing here measures enzyme activity or nucleotide specificity.
