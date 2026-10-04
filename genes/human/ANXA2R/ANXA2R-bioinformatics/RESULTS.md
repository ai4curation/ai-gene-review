# ANXA2R ortholog check (PANTHER PTHR38820)

Script: `panther_orthologs.py` (UniProt REST query `xref:panther-PTHR38820`, run 2026-10-04).

Purpose: test the statement in PMID:23640736 that "AXIIR gene is peculiar to human".

Output (abridged):

```
UniProt entries in PTHR38820: 92
distinct organisms: 57
Q3ZCQ2	Homo sapiens (Human)	ANXA2R AX2R C5orf39	193
A0A286YE39	Mus musculus (Mouse)	Anxa2r1 Anxa2r2	190
K7DGJ4	Pan troglodytes (Chimpanzee)	ANXA2R	193
G3UKB0	Loxodonta africana (African elephant)	ANXA2R	178
non-mammalian organisms: []
```

Conclusion: ANXA2R family members are present in 57 organisms, all mammals in this query, including mouse Anxa2r. The gene is mammal-specific, not human-specific. This fits PTHR38820 having no PAINT annotations: there are no experimentally characterised members outside human to seed an ancestral node.
