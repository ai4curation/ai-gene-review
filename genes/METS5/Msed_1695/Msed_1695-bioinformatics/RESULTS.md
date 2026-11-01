# Msed_1695 (A4YHE8) paralog assignment: results

Analyses run 2026-10-15. Sequences, family memberships and neighbour annotations were
fetched live from UniProt REST; nothing is hardcoded.

## 1. Cdv ESCRT-III family members in M. sedula DSM 5348 (UniProt REST query)

| Accession | Locus | Length | NCBIfam / InterPro family |
|---|---|---|---|
| A4YHC4 | Msed_1671 | 270 | NF041008 / IPR053654 (CdvB) |
| A4YHE8 | Msed_1695 | 221 | NF041005 cell_div_CdvB1_B2 / IPR053492, IPR005024 |
| A4YIR6 | Msed_2179 | 211 | NF041005 cell_div_CdvB1_B2 / IPR053492 |
| A4YI57 | Msed_1969 | 165 | NF041009 / IPR053658 (CdvB3) |

Only A4YHE8 is also matched by IPR005024 (Snf7 family, Pfam PF03357), which is why it
is the only M. sedula Cdv protein that carries the InterPro2GO vacuolar transport row.

## 2. Pairwise global alignment (paralog_assignment.py; BLOSUM62, gap -10/-0.5)

Output in `paralog_assignment_output.tsv`.

- Msed_1695 vs Saci_1416 CdvB2: 64.8% identity; vs Saci_0451 CdvB1: 60.5%;
  vs Saci_1373 CdvB: 31.9%; vs Saci_1601 CdvB3: 26.7%.
- Msed_2179 vs Saci_0451 CdvB1: 61.1%; vs Saci_1416 CdvB2: 57.0%.
- Best S. acidocaldarius hit: Msed_1695 -> Saci_1416 CdvB2; Msed_2179 -> Saci_0451 CdvB1;
  Msed_1671 -> Saci_1373 CdvB; Msed_1969 -> Saci_1601 CdvB3 (reciprocal best-hit pairs).
- The sequence margin between B1 and B2 is small (CdvB1 and CdvB2 are close paralogs,
  65.0% identical to each other in S. acidocaldarius), so identity alone is not decisive.

## 3. Conserved gene neighbourhood (synteny.py, +/-3 loci)

Output in `synteny_output.txt`.

- Msed_1695 neighbourhood shares 5 arCOGs with the Saci_1416 (cdvB2) neighbourhood
  (arCOG01111 PEP synthase, arCOG01434 threonine synthase, arCOG01671 UbiD-family
  decarboxylase, arCOG04213 inositol-1-phosphate synthase, arCOG07220 conserved protein)
  and 0 with the Saci_0451 (cdvB1) neighbourhood.
- Msed_2179 neighbourhood shares 4 arCOGs with Saci_0451 (cdvB1) (arCOG01887 TrpRS,
  arCOG01947, arCOG03358, arCOG04273) and 0 with Saci_1416.

## Conclusion

Msed_1695 is the CdvB2 ortholog of M. sedula: it is in the CdvB1/B2 family
(NF041005), is the reciprocal best hit of S. acidocaldarius CdvB2 (Saci_1416), and lies
in the conserved cdvB2 gene neighbourhood. The other CdvB1/B2-family protein, Msed_2179,
is the CdvB1 ortholog, consistent with its independent designation as M. sedula CdvB1
in the literature (PMID:35238034).
