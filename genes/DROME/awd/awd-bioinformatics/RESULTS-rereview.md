# awd re-review: which initiation codon makes the native enzyme?

Analysis date: 2026-10-20. This supplements, and does not replace, RESULTS.md.

## Question

A0A0B4LHX6 (FlyBase awd-PC/awd-PD, 168 aa) differs from reviewed P08879 (awd-PE, 153 aa) only by a
15-residue N-terminal extension, MLGTILAFFSVISAT; the P08879 sequence begins at target residue 16.
UniProt flags the 168-residue translation (AAF57188.3) as an erroneous initiation. The extension is
67% hydrophobic, and UniProt's automatic SignalP feature predicts a signal peptide at 1-17 of the
168-residue product. Does the biochemistry of the purified fly enzyme say which form is made?

## Method

`mass_rereview.py` reads both frozen UniProt JSON records and computes Biopython 1.85 average masses
for six candidate mature forms. It then compares them with the electrospray mass of purified fly
NDPK recorded in the P08879 MASS SPECTROMETRY comment (17082.3 +/- 0.6 Da, acetylated; PMID:12099695).

```
uv run --no-project --with biopython==1.85 python mass_rereview.py \
  ../awd-uniprot-source.json ../awd-reference-P08879-uniprot.json 17082.3 results-rereview/mass.json
```

## Results (results-rereview/mass.json)

| Candidate form | Average mass (Da) | Delta vs observed |
|---|---|---|
| P08879 1-153 unprocessed | 17169.7 | +87.4 |
| P08879 2-153, Met removed | 17038.5 | -43.8 |
| P08879 2-153, Met removed + N-acetyl | 17080.5 | -1.8 |
| A0A0B4LHX6 1-168 unprocessed | 18722.6 | +1640.3 |
| A0A0B4LHX6 2-168, Met removed + N-acetyl | 18633.4 | +1551.1 |
| A0A0B4LHX6 18-168, after predicted signal peptide | 16967.4 | -114.9 |

## Interpretation

Only the form that starts at the P08879 initiator methionine, with Met1 removed and Ala2 acetylated,
fits the measured mass. That matches the abstract of PMID:12099695, which reports a 152-residue mature
enzyme with N-acetylated Ala2. Neither the full 168-residue product nor a signal-peptide-processed form
of it fits. The bulk enzyme purified from flies is therefore translated from the downstream methionine
(target Met16). This does not exclude a minor 168-residue product, but no experiment we have found
detects one. The SignalP prediction is an automatic call on a translation that UniProt regards as an
initiation error, so it is not evidence of secretion. Delta values depend on the average-mass table used,
so agreement within about 2 Da is the expected precision.
