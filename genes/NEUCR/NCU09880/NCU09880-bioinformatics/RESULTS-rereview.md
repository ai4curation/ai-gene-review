# NCU09880 (Q7S234) re-review: Sm snRNA-contact triad conservation

Script: `sm_triad_rereview.py` (run with `uv run --script sm_triad_rereview.py`; sequences fetched live from UniProt).

Method: global BLOSUM62 pairwise alignment of Q7S234 to yeast SmG (P40204, PANTHER PTHR10553:SF2, same subfamily as Q7S234)
and human SmG (P62308, PTHR10553:SF26), mapping the SmG residues analysed by structure-guided mutagenesis in PMID:27417296.

Output (2026-10-21):

```
neurospora	Q7S234	length=85
yeast	P40204	length=77
human	P62308	length=76
yeast Arg23 (observed R) -> Q7S234 pos 24: R
yeast Phe35 (observed F) -> Q7S234 pos 36: F
yeast Asn37 (observed N) -> Q7S234 pos 38: N
yeast Arg64 (observed R) -> Q7S234 pos 62: R
human Arg25 (observed R) -> Q7S234 pos 24: R
human Phe37 (observed F) -> Q7S234 pos 36: F
human Asn39 (observed N) -> Q7S234 pos 38: N
human Arg63 (observed R) -> Q7S234 pos 62: R
```

Interpretation: all three uracil-contact triad residues (Phe, Asn, Arg) and the SmE-bridging Arg are conserved in
Q7S234 (Arg24, Phe36, Asn38, Arg62). Q7S234 is a full-length 85-residue SmG (Sm domain 3..75), not a fragment.
