# A2FPI7 KilA-N family context (2026-10-21)

Script: `kilan_context.py` (run with `uv run python kilan_context.py`); raw output in
`kilan_context_output.json`. All numbers below come from that output (live InterPro and
UniProt REST queries on 2026-10-21); nothing is hardcoded.

## Domain and family matches of A2FPI7 (129 aa)

| Signature | Span | Score |
|---|---|---|
| Pfam PF04383 (KilA-N) | 24-126 | 1.5e-21 |
| SMART SM01252 (KilA-N) | 28-127 | 7e-32 |
| PROSITE PS51301 (KILA_N) | 19-124 | profile |
| PANTHER PTHR48135:SF1 | 71-127 | 4.5e-05 |

The KilA-N domain spans essentially the whole protein (19-127 of 129), so A2FPI7 is a
stand-alone KilA-N module with no additional domain. The PANTHER match is weak and covers
only the C-terminal half of the domain.

## PANTHER family PTHR48135 ("FAMILY NOT NAMED"; SF1 "KILA-N DOMAIN-CONTAINING PROTEIN")

- 1667 UniProt members in total: 1374 Eukaryota, 252 Bacteria, 41 Viruses, 0 Archaea.
- 1308 of the 1667 members are from the T. vaginalis G3 proteome (UP000001542).
- The T. vaginalis proteome contains 1227 Pfam PF04383 (KilA-N) proteins; length
  min 49, median 244, max 462 aa; 147 are 150 aa or shorter.

So the family is a bacterial/phage KilA-N lineage with a massive lineage-specific expansion
in T. vaginalis. None of the reviewed, experimentally characterised KilA-N/APSES proteins
(S. cerevisiae Mbp1/Swi4 and S. pombe Res1/Res2/Cdc10 in PTHR43828; StuA/Efg1/Sok2/Phd1 in
PTHR47792; poxvirus p28 in PTHR11224) belongs to PTHR48135. The phage P1 KilA protein
(P19653), the namesake of the domain, has no PANTHER assignment and no experimental
function beyond a lethality/plasmid-establishment phenotype.

## Pairwise local alignment (BLOSUM62, gap -11/-1; z vs 200 shuffled targets)

Note: in the printed Biopython alignments the row labelled `target` is A2FPI7 (first
sequence) and `query` is the comparator.

| Comparator | Score | Aligned pairs | Identity | z |
|---|---|---|---|---|
| Phage P1 KilA (P19653) | 58 | 71 (A2FPI7 40-113) | 22.5% | 7.42 |
| S. cerevisiae Mbp1 residues 1-124 (P39678, APSES DNA-binding domain) | 33 | 13 | 53.8% | 1.25 |

A2FPI7 has clear pairwise similarity to the phage KilA KilA-N region but no pairwise-
detectable similarity to the Mbp1 APSES domain; the relationship to APSES exists only at
the superfamily/profile level (Iyer et al. 2002, PMID:11897024).

## Interpretation

- A2FPI7 is a member of a T. vaginalis-expanded, phage/bacteria-derived KilA-N lineage,
  not an ortholog of any characterised fungal APSES transcription factor.
- DNA binding is a domain-level (superfamily fold) inference; no member of PTHR48135 has
  experimental evidence of DNA binding or of any other molecular function.
- Subfamily-specific functions of APSES factors (MCB/SCB promoter recognition, G1/S
  transcription, morphogenesis) must not be transferred.
