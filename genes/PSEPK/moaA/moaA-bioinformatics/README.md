# PSEPK MoCo paralog sequence analysis

This analysis compares the three KT2440 MoaA-family proteins and separately
exercises the same workflow on the MobA-like nucleotide-transferase candidates.
It reports sequence identity, selected sequence motifs, the family/database
cross-references present in authoritative UniProt flat files, and current KEGG
gene-to-orthology links retrieved from the KEGG REST API. It does not infer
physiological equivalence from similarity alone.

Run the complete workflow from this directory:

```bash
just all
```

The MoaA inputs are repository-fetched UniProt records. The MobA-like control
also retrieves the explicit reviewed E. coli MobA (P32173) and MocA (Q46810)
records from the UniProt REST API. KEGG identifiers in those records are looked
up through `rest.kegg.jp`. Dependencies are pinned in `pyproject.toml`.
