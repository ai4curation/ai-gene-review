# OLFML2A horse gene-model comparison (re-review, 2026-10-20)

Script: `compare_sequences_rereview.py` (run with `uv run compare_sequences_rereview.py > RESULTS-rereview.json`).
It fetches sequences live from UniProt REST and NCBI E-utilities, makes a BLOSUM62 global alignment of
each horse product against human Q68BL7, and reports human positions left unpaired. As a crude
signal-peptide proxy it reports the maximum Kyte-Doolittle hydropathy of any 11-residue window in the
first 40 residues. This is not a SignalP prediction. Raw output: `RESULTS-rereview.json`.

## Horse products of the OLFML2A locus

All entries below come from one Ensembl gene, ENSECAG00000023908. The two UniProt entries both cross-reference it.

| Product | Length | N-terminus | max KD (1-40) | Identity to human | Human positions unpaired |
|---|---|---|---|---|---|
| human Q68BL7 (reference) | 652 | MAAAALPPRPLLLLPLVLLLSGRPTRADSKVFGD | 2.93 | - | - |
| UniProtKB:A0A9L0SKW1 (benchmark) | 599 | MDSQVFGDMDQVRMTSEGSD | 0.25 | 91.3% | 2-27, 123-144, 327-328, 360-363 |
| UniProtKB:A0A3Q2LAT7 | 621 | MDSQVFGDMDQVRMTSEGSD | 0.25 | 91.6% | 2-27, 327-328, 360-363 |
| RefSeq:XP_023484611.2 (isoform X1) | 650 | MAAAALPPRPRPLALLLLPLLLLRAGTVRADSKVFGD | 3.13 | 91.3% | 23, 327-328, 360-363 |
| RefSeq:XP_023484612.1 (isoform X2) | 621 | MDSQVFGDMDQVRMTSEGSD | 0.25 | 91.6% | 2-27, 327-328, 360-363 |
| RefSeq:XP_070107868.1 (isoform X3) | 621 | MHPGVFGDMDQVRMTSEGSD | 0.25 | 91.3% | 5-30, 327-328, 360-363 |
| RefSeq:XP_023484613.1 (isoform X4) | 618 | MVFGDMDQVRMTSEGSD | 0.25 | 91.7% | 2-30, 327-328, 360-363 |
| RefSeq:XP_070107869.1 (isoform X5) | 477 | MRHFSEQLKHYENHSAI | 0.59 | 90.1% | 2-171, 327-328, 360-363 |
| mouse Q8BHP7 (comparison) | 681 | MEAAAVLPRYLQLRLLLVLLLLVLLRAGPVWPDSKVF | 3.87 | 83.8% | 327-328 |

## Interpretation

- The horse locus encodes a leader-bearing product. RefSeq isoform X1 (XP_023484611.2, 650 residues)
  starts with a hydrophobic N-terminal segment homologous to the human 1-27 signal peptide (maximum
  hydropathy 3.13, against 2.93 for human), and it pairs with human over all but five positions. It is the
  horse counterpart of canonical human isoform 1.
- The benchmark accession A0A9L0SKW1 is one of several leaderless alternative models of the same gene.
  Its N-terminus MDSQ-VFGD replaces the leader and the human ADSK-VFGD junction (human residues 1-27
  unpaired). The model also lacks the 22-residue segment opposite human 123-144, which every other horse
  model retains. It is therefore a shorter alternative splice/gene model and not the canonical product.
  The leaderless start parallels human isoform 2, which UniProt records as missing residues 1-39.
- The olfactomedin domain is intact in A0A9L0SKW1. The cysteines corresponding to the human 395-582
  disulfide (horse C342 and C529) are both present.
- Unpaired human 327-328 and 360-363 appear in every horse product, so these are species-level
  indels, not features of the benchmark model.
- None of this establishes whether the leaderless horse transcripts are translated, or where their
  products localize.
