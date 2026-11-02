# EIP9/SDJ1 J-domain HPD motif check

Script: `jdomain_hpd_check.py` (stdlib Python; fetches UniProt REST JSON). Raw output: `hpd_check_output.tsv`.

Question: does the J domain of EIP9/SDJ1 (Q9FMF3, At5g64360) retain the HPD tripeptide that canonical
J-domain proteins use to stimulate Hsp70 ATPase activity?

| Accession | Protein (PANTHER subfamily) | J domain | HPD in J domain |
|---|---|---|---|
| Q9FMF3 | EIP9/SDJ1 (PTHR45496:SF19) | 79-144 | No (LLNPSVNR in place of the HPD loop) |
| Q9ZU99 | SDJ2 (PTHR45496:SF1) | 71-139 | Yes (position 103) |
| Q0WQM3 | SDJ3 (PTHR45496:SF10) | 81-146 | No (LLNPSRNR) |
| Q9SZ59 | ADMETOS (PTHR45496:SF32) | none annotated | n/a |
| P08622 | E. coli DnaJ (positive control) | 3-72 | Yes (position 33) |

Interpretation: EIP9/SDJ1 lacks the HPD motif within its J domain (the corresponding loop reads NPS),
as does SDJ3, while SDJ2 retains it. Loss of HPD in J-domain proteins is generally associated with loss
of the ability to stimulate Hsp70 ATPase activity, so a canonical Hsp70 co-chaperone (J-domain protein)
activity should not be assumed for EIP9/SDJ1 from domain membership alone. This is a sequence-motif
observation only; no biochemical test of Hsp70 stimulation by SDJ1 has been reported in the literature
reviewed.
