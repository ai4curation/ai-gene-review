# CG14662 (Q9VN74) sequence features and family placement (re-review, 2026-10-21)

Script: `sequence_features_rereview.py` (reads `../CG14662-uniprot.txt`; run with `python3 sequence_features_rereview.py`).

## Script output (verbatim)

```
length 550
hydrophobic windows (start,end,max_KD): [(28, 54, 2.48), (418, 448, 2.4)]
N-glyc sequons (N position): [64, 77, 98, 116, 129, 143, 391]
{'region': '1-28', 'len': 28, 'ST_frac': 0.11, 'C_count': 0, 'KR': 9, 'DE': 4}
{'region': '51-290', 'len': 240, 'ST_frac': 0.15, 'C_count': 3, 'KR': 15, 'DE': 29}
{'region': '291-336', 'len': 46, 'ST_frac': 0.48, 'C_count': 0, 'KR': 2, 'DE': 5}
{'region': '337-420', 'len': 84, 'ST_frac': 0.24, 'C_count': 10, 'KR': 3, 'DE': 13}
{'region': '448-550', 'len': 103, 'ST_frac': 0.11, 'C_count': 2, 'KR': 13, 'DE': 14}
LxxLxLxxN/C motifs: [(220, 'LEQLLLRNC')]
tyrosine motifs YxxL/I/V/F in C-terminal tail: [(475, 'YEQV'), (546, 'YEEL')]
```

## Interpretation

- Two hydrophobic segments (Kyte-Doolittle windows 28-54 and 418-448) coincide with the two Phobius
  transmembrane calls in UniProt (29-50, 421-447).
- The first hydrophobic segment is preceded by a 28-residue N-terminus carrying 9 Lys/Arg. A cleavable
  signal peptide normally starts within a few residues of the initiator Met; a long, positively charged
  N-terminal extension before the hydrophobic core instead fits an uncleaved signal anchor with the
  N-terminus in the cytosol (positive-inside rule). Dolan et al. 2007 (PMID:17868438) called it a signal
  sequence ("SS, 6LRR, TM"). Both readings put residues ~51-420 on the luminal/extracellular side; they
  differ only on whether the protein is single-pass (cleaved SS) or two-pass (signal anchor + TM).
- The luminal/extracellular segment carries all seven N-glycosylation sequons (64-391), consistent with
  that orientation; none is in the C-terminal tail.
- Domain order in that segment: an LRR-superfamily region (CATH 3.80.10.10 / IPR032675, residues 35-282;
  Dolan counts 6 LRRs, only one strict LxxLxLxxN/C match, so the repeats are degenerate), a Ser/Thr-rich
  disordered stretch (291-336, 48% S+T; mucin-like stalk candidate, MobiDB-lite disordered 296-332), and
  a cysteine-rich segment (337-420, 10 Cys) immediately before the second TM.
- The 103-residue C-terminal tail (448-550) is predicted cytosolic and contains two YxxΦ motifs
  (YEQV 475, YEEL 546), a sequence pattern often used for endocytic sorting; this is a motif match only.
- No catalytic domain, TIR domain or other signalling domain is present. Absence of a TIR domain means
  the protein lacks the defining intracellular module of Toll/Toll-like receptors.

## Family placement and orthology

- InterPro (API query 2026-10-21) reports a PANTHER match PTHR24365 (TOLL-LIKE RECEPTOR) to subfamily
  PTHR24365:SF541 "PROTEIN TOLL-RELATED" over residues 190-452 with model score 0.032. Q9VN74 is NOT in
  the PANTHER 19.0 fruit-fly classification file (.cache/panther/PTHR19.0_fruit_fly), whose SF541
  members are Tl (P08953) and Tehao (Q9VJX9). The match is weak, partial (it covers neither the
  N-terminal LRR half nor a TIR domain, which Q9VN74 lacks) and not part of PANTHER's own
  classification, so it is not treated as evidence of Toll-receptor ancestry or function.
- Dolan et al. 2007 classified CG14662 as an LRR_Only singleton (no subfamily partner at their
  clustering cutoffs in human, mouse, fly or worm).
- OrthoDB (query by FBgn0037291, 2026-10-21) places the gene in a single orthogroup of 63 genes in 62
  species, all in Brachycera (Drosophila, Tephritidae, Sarcophagidae, Lauxaniidae and others); the group
  is identical at every level from Eukaryota down to Brachycera, i.e. no ortholog outside higher Diptera
  was found. No member of the group is experimentally characterized.
