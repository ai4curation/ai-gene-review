# Ortholog identity: Delta H vs M. marburgensis MvhADG/HdrABC subunits

Script: `ortholog_identity.py` (run with `uv run python genes/METTH/hdrA/hdrA-bioinformatics/ortholog_identity.py`).
Sequences fetched from the UniProt REST API on 2026-11-07. Global alignment, BLOSUM62,
gap open -10, extend -0.5 (Biopython PairwiseAligner).

Output:

```
HdrA: O27434 (659 aa) vs Q50756 (659 aa): 639/658 aligned identical = 97.1%; 97.0% of shorter sequence
HdrB: O27907 (302 aa) vs Q50755 (302 aa): 286/302 aligned identical = 94.7%; 94.7% of shorter sequence
  Q50755 C153 -> O27907 C153
  Q50755 C193 -> O27907 C193
  Q50755 C194 -> O27907 C194
  Q50755 C234 -> O27907 C234
MvhA: Q50783 (472 aa) vs P60227 (472 aa): 460/472 aligned identical = 97.5%; 97.5% of shorter sequence
```

Interpretation: the three Delta H subunits are 95-98% identical over their full length
to the M. marburgensis (strain Marburg) proteins whose complex was purified and assayed
(PMID:8119281, PMID:21262829). The four C-terminal CCG-domain cysteines shown by
mutagenesis to ligate the [4Fe-4S] cluster of M. marburgensis HdrB (PMID:17929940) are
conserved at the same positions in O27907. Transfer of the ortholog biochemistry to the
Delta H proteins is therefore well founded.
