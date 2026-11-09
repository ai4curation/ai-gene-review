# mtrA2 (O27134, MTH_1062): alignment to membrane MtrA

Command (from this folder):

    uv run python analyze_mtrA2.py > analysis_output.txt

Sequences and UniProt TRANSMEM features are fetched live from the UniProt REST
API. Alignments are semi-global (BLOSUM62, gap open -10, extend -0.5, free end
gaps). Hydropathy is Kyte-Doolittle, 19-residue window (classic TM threshold
about 1.6). Full output, including the alignments, is in `analysis_output.txt`.

## (a) The C-terminal membrane anchor is absent from mtrA2

| Pair | Identity | Last residue of partner aligned to O27134 | Partner residues beyond the end of O27134 | Partner TRANSMEM residues aligned to O27134 |
|---|---|---|---|---|
| O27134 vs O27227 (mtrA1, 238 aa) | 109/180 = 60.6% | 180 | 58 | 0/19 (TM 219-237) |
| O27134 vs P80184 (MtrA strain Marburg, 238 aa) | 110/180 = 61.1% | 180 | 58 | 0/19 (TM 219-237) |
| O27134 vs Q58261 (MtrA M. jannaschii, 241 aa) | 102/178 = 57.3% | 180 | 61 | 0/21 (TM 221-241) |
| O27134 vs E3GZ46 (membrane MtrA M. fervidus, 237 aa) | 112/175 = 64.0% | 175 | 62 | 0/19 (TM 218-236) |
| O27134 vs E3GWY7 (cytoplasmic MtrA homologue M. fervidus, 167 aa) | 109/167 = 65.3% | 167 | 0 | (no TRANSMEM) |

mtrA2 aligns to the first ~180 residues of membrane MtrA, the soluble
cobamide domain, and ends there. The juxtamembrane segment and the C-terminal
transmembrane helix (the last ~58-62 residues of each membrane MtrA) have no
counterpart in mtrA2. At 183 aa, mtrA2 falls in the "cytoplasmic MtrA
homologue" class of PMID:27324530 (below 215 aa).

## (b) The UniProt TRANSMEM on O27134 lies inside the soluble domain

- O27134 has one TRANSMEM, 102-118 (`DLETGRIIGATGAIPYI`), evidence
  `ECO:0000255|HAMAP-Rule:MF_01093`. Its mean KD hydropathy is 0.49, well
  below the TM threshold, and it contains three charged residues (D, E, R).
- The most hydrophobic 19-residue window anywhere in O27134 scores 1.29
  (residues 64-82). The membrane MtrA anchors score 2.05-2.21 (O27227
  219-237: 2.15; Q58261 222-240: 2.21; E3GZ46 218-236: 2.05).
- O27134 102-118 aligns to residues 99-115 of O27227 and P80184, a segment in
  the middle of the cobamide domain that is not a TRANSMEM in any membrane MtrA.
  It contains the residue equivalent to Ile111 of the M. fervidus structure
  (O27134 Ile115; see (c)), which belongs to the meander segment after
  helix alpha3 of the Rossmann-like fold (PMID:27324530).
- The 167-aa M. fervidus cytoplasmic homologue E3GWY7, which also matches
  MF_01093, carries no TRANSMEM.

## (c) The cobamide-ligand histidine is conserved

| Literature residue | P80184 (strain Marburg MtrA) | E3GWY7 (M. fervidus homologue) | O27134 |
|---|---|---|---|
| His84 (lower axial cobalt ligand) | H84 | H84 | His87 |
| Glu54 (H-bond to His84 ND1) | E54 | E54 | Glu57 |
| Ile111 (backbone N fixes Glu54) | A111 | I111 | Ile115 |

The cobalt ligand His and its Glu partner are conserved in mtrA2, offset by +3
because of a three-residue N-terminal extension. This agrees with the UniProt
BINDING feature at position 87. The Ile111 numbering in PMID:27324530 matches the
M. fervidus homologue (E3GWY7), not the strain Marburg MtrA (Ala111).

## Caveats

- Hydropathy is a simple screen, not a topology predictor. The conclusion that
  mtrA2 has no TM helix rests on the agreement of hydropathy, the alignment and
  the length class of the cytoplasmic homologues.
- E3GWY7 is the M. fervidus MtrA entry below 215 aa. Its identity to the
  M. fervidus membrane MtrA (E3GZ46) is 94.6% by `pairwise_identity.py` in
  `../../mtrA1/mtrA1-bioinformatics/`, against the 97% given in PMID:27324530.
  The residue numbering matches the structure paper, but the analysis does not
  establish that E3GWY7 is the exact construct that was crystallised.
- Conservation of the ligand His predicts cobamide binding. It says nothing
  about what methyl-transfer partner, if any, mtrA2 has.

## HAMAP rule MF_01093

`hamap_MF_01093.txt` is the rule as downloaded on 2026-11-09
(`curl -sS https://hamap.expasy.org/rule/MF_01093.txt -o hamap_MF_01093.txt`,
rule version 33). It lists `Size: 183-262` and `Duplicate: in METRM, METTH, METTM`,
so the 183-aa paralog is deliberately inside the rule's scope. The rule asserts
the cell membrane location, the single-pass topology (with a TM prediction
triggered on the sequence), EC 7.2.1.4 and the eight-subunit complex with no
case that excludes the anchorless cytoplasmic homologues.
