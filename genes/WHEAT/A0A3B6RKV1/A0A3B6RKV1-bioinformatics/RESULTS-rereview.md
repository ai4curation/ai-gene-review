# A0A3B6RKV1 vs Arabidopsis JMJ22 and human JMJD8 (re-review, 2026-10-20)

Script: `compare_to_jmj22.py` (run: `uv run --no-project --with biopython --with requests python compare_to_jmj22.py`).
Raw output: `compare_to_jmj22.out`. UniProt records used for comparison are saved as
`Q67XX3-JMJ22-uniprot.txt` and `Q96S16-JMJD8-uniprot.txt` (fetched 2026-10-20).

## Phylogenetic placement

- A0A3B6RKV1, Arabidopsis JMJ22 (Q67XX3, At5g06550) and human JMJD8 (Q96S16) are all
  classified in PANTHER PTHR12480:SF21 ("JMJC DOMAIN-CONTAINING PROTEIN 8").
- Arabidopsis JMJ20 (Q67ZB6, At5g63080), the redundant partner of JMJ22 in the seed
  germination study, is in a different subfamily, PTHR12480:SF6 (JMJD4 subfamily), per
  UniProt PANTHER cross-references. JMJ20 is therefore a paralog, not the ortholog.
- SF21 is the JMJD8 subfamily, not the JMJD6 subfamily (JMJD6 is PTHR12480:SF32).

## Pairwise global alignment (BLOSUM62, gap -10/-0.5)

| Comparison | Aligned columns | Identical | % identity |
|---|---|---|---|
| A0A3B6RKV1 vs AtJMJ22 | 494 | 309 | 62.6 |
| A0A3B6RKV1 vs HsJMJD8 | 243 | 90 | 37.0 |

- AtJMJ22 F-box 80-126 maps to wheat 89-135 (46.8% identity).
- AtJMJ22 JmjC 279-439 maps to wheat 285-445 (77.0% identity).
- AtJMJ22 Fe(II) ligands H324, D326, H407 map to wheat H330, D332, H413 (all conserved).
  (An earlier statement in the review that the third ligand was His362 was incorrect.)
- Human JMJD8 (264 aa) lacks the N-terminal region and F-box; the F-box/JmjC architecture
  is plant-branch specific within SF21.

## Interpretation

Same-subfamily membership, shared F-box + JmjC architecture, near-collinear alignment and
conservation of the Fe(II)-binding HxD...H triad make AtJMJ22 the closest experimentally
characterised relative. The conserved triad supports a catalytically competent Fe(II)/2OG
oxygenase. Substrate identity (H4R3me2) for the wheat protein is not tested.
