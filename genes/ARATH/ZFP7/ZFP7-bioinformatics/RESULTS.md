# ZFP7 (Q39266) bioinformatics

Reproducible with `python3 motifs.py` (standard library only; reads `../ZFP7-uniprot.txt`).
Output is saved in `motifs-output.tsv`.

## Sequence motifs

- Length 209 aa, one C2H2 zinc finger at 61-81 (CNYCRRKFYSSQALGGHQNAH), matching
  the UniProt PROSITE feature 59..81.
- The plant Q-type QALGGH motif lies inside the finger at 72-77.
- Two LxLxL EAR-like matches: LDLKL at 35-39 and LTLRL at 205-209 (C-terminal).
  No DLNxxP EAR motif.

These features place ZFP7 among the single-finger Q-type (C1-1i) C2H2 zinc-finger
proteins of plants, and the C-terminal LxLxL is consistent with, but does not prove,
transcriptional repression activity. The motif scan is a pattern match only.

## Phylogenetic placement (from existing family files, not recomputed here)

`interpro/panther/PTHR47593/PTHR47593-paint.tsv` lists two PAINT nodes that ZFP7 descends
from: PTN009184003 (GO:0005634 nucleus and GO:0000976 transcription cis-regulatory region
binding, seeded by ZFP7, ZFP4, KNU and ZFP3 among others) and PTN008158895 (GO:0009788
negative regulation of abscisic acid-activated signaling pathway, seeded by ZFP7 and ZFP4).
The PANTHER 19 tree analysis in
`genes/SOYBN/C6T1A2/C6T1A2-bioinformatics/RESULTS-rereview.md` places ZFP7 in PTHR45730
(SF104), while UniProt's PANTHER cross-reference gives PTHR47593:SF8.
