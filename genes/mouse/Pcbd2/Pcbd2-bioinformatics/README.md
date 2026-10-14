# Pcbd2 N-terminal extension: is it a mitochondrial presequence?

Run `just` (or `python3 nterm_mts_analysis.py`) in this directory. Python 3.12
standard library only; no third-party dependencies.

## Why

Mouse Pcbd2 (Q9CZL5, 136 aa) carries ~33 N-terminal residues that mouse Pcbd1
(P61458, 104 aa) does not. GOA has one `located_in mitochondrion` annotation for
Pcbd2 — HDA from PMID:18614015 (MitoCarta) — which UniProt has not adopted; its
SUBCELLULAR LOCATION lists only Cytoplasm and Nucleus. Deciding whether that HDA
is a co-purifying-contaminant artefact or a real second pool turns on whether the
Pcbd2-specific extension could be a cleavable mitochondrial targeting sequence.

## What the script does

Fetches sequences from the UniProt REST API (cached under `data/`) and scores the
first 32 residues of each focus protein against two mouse reference sets built
from UniProt itself:

* **positives** — reviewed mouse proteins with a `TRANSIT` "Mitochondrion"
  feature; the annotated presequence is the scored window.
* **negatives** — reviewed mouse cytosolic (SL-0091) proteins with no transit,
  signal or transmembrane feature; their first 32 residues are the scored window.

Features are the textbook presequence properties — net charge, Arg count, acidic
count, Ser+Thr fraction, and maximum mean hydrophobic moment (Eisenberg
consensus scale, 18-residue window, 100°/residue) — plus Ala fraction as an
explicit **confounder control**, because a low-complexity Ala tract lacks acidic
residues for reasons unrelated to targeting.

No thresholds are asserted. The output is each feature's percentile within both
reference distributions, so the reader can see how presequence-like the extension
is relative to real presequences rather than against an invented cutoff.

## Limits

These are compositional heuristics, not a targeting predictor, and they cannot
demonstrate import or cleavage. No MitoFates/TargetP/DeepLoc run is included
because none is callable without a licence or web upload from this environment;
the script does not pretend otherwise. See `RESULTS.md` for the biological
reading and for what would actually settle the question.

## Outputs

* `results.json` — every number, regenerated on each run
* `data/` — cached UniProt REST responses. These are committed on purpose: they
  pin the exact reference sets the percentiles in `RESULTS.md` were computed
  against, since UniProt query results drift between releases. Pass `--refresh`
  (or `just refresh`) to refetch against current UniProt, which may shift the
  reference distributions slightly.
* `RESULTS.md` — interpretation
