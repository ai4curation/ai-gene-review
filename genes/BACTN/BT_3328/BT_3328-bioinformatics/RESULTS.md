# BT_3328 bioinformatics

## Purpose

Check that the KBase Dark Protein Atlas query `CAKXSP010000006.1_105` (an
environmental *Bacteroides thetaiotaomicron* assembly, annotated by eggNOG and
InterPro only as "Domain of unknown function (DUF4955)") is the same gene as
UniProt Q8A2H7 (BT_3328, BtCDH, the founding member of polysaccharide lyase
family PL29), and record the sequence features used in the review.

## Method

`align.py` makes a global BLOSUM62 alignment (Biopython PairwiseAligner, gap
open -10, extend -0.5) of the UniProt sequence in `../BT_3328-uniprot.txt`
against the query sequence `CAKXSP010000006.1_105.fasta`, taken from the
dashboard's review page. Output is in `align_output.txt`.

```
uv run python align.py ../BT_3328-uniprot.txt CAKXSP010000006.1_105.fasta
```

## Results

- Both sequences are 868 aa. The alignment has no gaps; 858 of 868 positions
  are identical (98.8% identity). The 10 differences are conservative or
  surface substitutions scattered along the chain:
  T170A L233F P321L I397V A541V S567A D675N A705T G779S V823M.
- The N-terminus `MKKVISIICITLLVALYSCDERDDL` carries a lipoprotein signal peptide
  with lipobox `LYSC` and Cys19 as the predicted lipidated residue, as in the
  UniProt LIPID feature at position 19 (PROSITE PS51257). The residues after
  Cys19 are acidic (`DERDD`), the pattern of the *Bacteroides* lipoprotein
  export signal that sends lipoproteins to the cell surface.
- InterProScan on the query (KBase run) finds Pfam PF16378 (DUF4988) at
  25-199 and PF16315 (DUF4955) at 716-867 (E = 2.8e-69). These are the only
  domain annotations; neither Pfam entry is linked to a function.

## Conclusion

The query is an allele of BT_3328 from another *B. thetaiotaomicron* strain,
so the experimental characterisation of BT_3328 applies directly to it.
DeepTMHMM in the KBase run classified the protein as soluble and secreted
(signal peptide 1-18). That reading was re-tested directly (below): DeepTMHMM
is right about the signal peptide and simply cannot resolve its type, so the
label is under-resolved rather than wrong. The "soluble" gloss drawn from it
does not hold.

## Re-testing the topology call (2026-11-11)

Both sequences were re-run on current DTU predictors through BioLib, outside the
KBase pipeline. Run record: `projects/hackathon/runs/20261111T071416Z-deeptmhmm-signalp6-bt3328`
(raw outputs under `out/data/<tool>/<sequence>/`, summary in `out/results.json`).

| Tool | BioLib app | CAKXSP010000006.1_105 | Q8A2H7 |
|---|---|---|---|
| DeepTMHMM 1.0 | `DTU/DeepTMHMM:1.0.57` | class `SP`; `S` 1-18, `O` 19-868 | identical |
| SignalP 6.0 (slow, organism other) | `DTU/SignalP-6:0.0.56` | `LIPO` (Sec/SPII), p = 1.000021 reported, CS 18-19 Pr 0.9973 | identical |

Two things follow.

- **The KBase call is reproducible.** DeepTMHMM 1.0 returns exactly what the
  dashboard showed: a signal peptide over residues 1-18 and the rest of the chain
  outside. The dashboard backend was not misconfigured.
- **DeepTMHMM cannot resolve the signal-peptide type.** Its label alphabet has a
  single `S` state for signal peptide (the 3-line format is over `SIOPMB`), so a
  Sec/SPI signal peptide and a Sec/SPII lipoprotein signal peptide both come back
  as `SP`. SignalP 6.0, which scores the classes separately, calls this one
  `LIPO` (Sec/SPII) essentially to the exclusion of everything else, cleaving
  between residues 18 and 19 and so leaving Cys19 as the lipidated N-terminal
  residue of the mature protein. That is the lipobox read independently.

So DeepTMHMM's own output is correct and consistent with a surface lipoprotein. What
does not survive is the interpretation layered on it in the dashboard's topology
panel, that the mature protein is therefore soluble: a lipoprotein is lipid-anchored
rather than soluble, even though it is not membrane-embedded either.

### DeepTMHMM2

A DeepTMHMM2 preprint exists (doi:10.64898/2026.08.24.746435; re-entrant regions,
interfacial helices and localisation over 17 membrane types) and `DTU/DeepTMHMM2`
is published on BioLib, so it was attempted here. It is not usable through
`pybiolib`: arguments do reach the `dtm2` CLI and it runs on the supplied FASTA,
but the app's only retrievable output is a report generated from a built-in
`CLV3_ARATH` example regardless of input, and the real per-sequence files stay in
the container. `--override_command` is refused by the app. The run records both
attempts with `input_sequence_found_in_output: false` so they cannot be mistaken
for results about this protein. Its membrane-type head would be worth having here,
and needs either the web GUI or a local install.
