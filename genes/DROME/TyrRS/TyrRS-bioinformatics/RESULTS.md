# TyrRS (Q9VV60) vs human YARS1 (P54577): motif comparison

Script: `compare_motifs.py` (run with `uv run --with biopython python compare_motifs.py`).
Sequences downloaded from UniProt REST on 2026-10-20 (`Q9VV60.fasta`, `P54577.fasta`).

Both proteins are members of PANTHER subfamily PTHR11586:SF43 (TYROSINE--TRNA LIGASE, CYTOPLASMIC),
per UniProt DR lines and `interpro/panther/PTHR11586/PTHR11586-entries.csv`.

Output (BLOSUM62 global alignment, gap open -10, extend -0.5):

```
human length 528, fly length 525
aligned pairs 522, identical 355, identity over aligned 0.680
HIGH-like (class I signature region): human PHVAYF at 48-53; fly PHVAYF at 47
KMSSS (class I signature): human KMSSS at 222-226; fly KMSSS at 221
ELR tripeptide (mini-TyrRS cytokine motif): human LELR at 90-93; fly LELR at 89
lysine-rich region (reported NLS): human KKKLKKA at 242-248; fly KKKLKKA at 241
```

Interpretation: the fly protein is full length relative to human YARS1 (525 vs 528 aa), 68% identical
over the aligned length, and retains the class-I catalytic signature regions, the ELR tripeptide of the
mini-TyrRS N-terminal module, and the lysine-rich segment that in human TyrRS lies in the region
reported to mediate nuclear entry. Motif retention is consistent with, but does not demonstrate,
conservation of the noncanonical human activities (cytokine signalling, nuclear translocation).
