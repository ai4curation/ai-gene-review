# Donkey TNFRSF1A canonical product (A0A8C4MD74) vs human TNFR1 (P19438)

Script: `compare_sequences.py` (PEP 723; run with `uv run --script compare_sequences.py > results.json`).
Sequences and human features are fetched live from the UniProt REST API. Alignments are global,
BLOSUM62, gap open -10, extend -0.5. Feature positions below are human UniProt coordinates, with the
aligned donkey span in brackets. Raw output, including the formatted alignment, is in `results.json`.

## Relationship

- A0A8C4MD74 (453 aa) is the product of the Ensembl canonical transcript ENSEAST00005025834 of donkey
  gene ENSEASG00005016176 (TNFRSF1A, chromosome 22). UniProt maps it to PANTHER PTHR46861:SF1, the
  same subfamily as human P19438 and mouse P25118. PTHR46861 (TNFRSF1A) has a single subfamily; the
  PAINT IBD node PTN002930098 (taxon Euteleostomi) carries TNF receptor activity, TNF binding,
  signaling receptor complex, membrane raft and inflammatory response, and donkey lies inside it.
- Identity over aligned positions: human P19438 0.761 (448 positions); mouse P25118 0.666;
  horse A0A5F5Q204 0.982 (the horse model differs mainly by an N-terminal extension).

## Feature coverage vs human P19438

- Signal peptide 1-29: 100% covered, 72% identical [donkey 1-29].
- CRD1 43-82 (contains the pre-ligand assembly domain): 100% covered, 88% identical [43-82].
- CRD2 83-125: 100% covered, 91% identical [83-125].
- CRD3 126-166: 100% covered, 80% identical [126-169; 3-residue insertion].
- CRD4 167-196: 100% covered, 73% identical [170-199].
- All 24 human extracellular cysteines (positions 22-211) are conserved.
- Transmembrane helix 212-232: 100% covered, 86% identical [215-235].
- N-SMase activation domain 338-348: 91% covered, 73% identical [338-347].
- Death domain 356-441: 100% covered, 88% identical [354-439].

## Interpretation

A0A8C4MD74 encodes a complete TNFR1: signal peptide, four cysteine-rich domains with every
disulfide-forming cysteine of the human receptor, a single transmembrane helix and a cytoplasmic death
domain. The UniProt CAUTION line ("Lacks conserved residue(s) required for the propagation of feature
annotation", PROSITE-ProRule PRU00206) reflects the PROSITE repeat model calling only two of the four
CRDs; it is not borne out by the cysteine count. Nothing here tests whether the donkey protein binds TNF
or signals: no experimental data on donkey TNFR1 were found, so all functional statements rest on 1:1
orthology (PTHR46861:SF1, PAINT node PTN002930098) and on the conservation reported above.
