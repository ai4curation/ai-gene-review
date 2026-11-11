# cec-10 (Q9N4L7) versus the fungal SBF/MBF family: domain and alignment check

Script: `align_vs_swi6_family.py` (raw output in `results.txt`). Sequences from UniProt REST, domain
matches from the InterPro API, Smith-Waterman local alignment (BLOSUM62, gap -11/-1), significance by
a Z-score against 100 composition-preserving shuffles of each subject.

## Domain architecture

CEC-10 InterPro matches: chromodomain (IPR000953, residues 48-110; SMART SM00298; PROSITE PS50013),
one ankyrin repeat (IPR002110, 520-552) inside an ankyrin-repeat superfamily region (IPR036770, 451-589),
and the family-level signature PTHR43828 / IPR051642 "Regulatory protein SWI6-like" spanning 17-793.

CEC-10 has no KilA-N / APSES-type HTH DNA-binding domain (IPR003163, IPR018004, PF04383). All four
DNA-binding fungal members tested (S. pombe Res2 and Res1, S. cerevisiae Mbp1 and Swi4) carry this
domain at their N terminus. CEC-10 also lacks the Swi6 N-terminal domain (PF18530) found in budding
yeast Swi6. The N-terminal chromodomain of CEC-10 is absent from every fungal member tested.

## Pairwise similarity

| Subject | Z-score | CEC-10 region aligned | Identity |
|---|---:|---|---|
| Swi6 (P09959) | 1.9 | 488-559 (ankyrin region) | 30% over 71 |
| Cdc10 (P01129) | 2.5 | 265-453 | 23% over 179 |
| Res2 (P41412, a seed of PTN000917496) | 2.9 | 207-266 | 32% over 60 |
| Res1 (P33520) | 2.1 | 522-563 (ankyrin) | 31% over 42 |
| Mbp1 (P39678) | 5.5 | 120-581 | 26% over 420 |
| Swi4 (P25302) | 3.6 | 138-346 | 25% over 207 |

Pairwise similarity between CEC-10 and the fungal SBF/MBF subunits is weak (Z 1.9-5.5, roughly
23-32% identity over short or low-complexity stretches). Much of it falls in the long disordered,
compositionally biased middle region of CEC-10 (141-381). No alignment covers a fungal DNA-binding
domain. CEC-10 is in PTHR43828 because the family HMM matches over its whole length, most likely
driven by the ankyrin-repeat region and the region C-terminal to it. Pairwise alignment gives no
evidence that CEC-10 is an ortholog of any MBF or SBF subunit.

## Interpretation (limits)

These are pairwise checks, not a phylogeny; the PANTHER tree itself was not re-inferred. The result
supports the narrower claim needed for the review: CEC-10 lacks the DNA-binding module that defines the
MBF/SBF DNA-binding subunits, and it carries an animal-type chromodomain that no fungal member has.
The InterPro API also lists 48 metazoan PTHR43828 members, mostly from cnidarians and molluscs, with
CEC-10 the only Caenorhabditis entry. Whether these are relics of an ancestral ankyrin-repeat lineage
or independent acquisitions was not determined.
