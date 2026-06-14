# PDB inventory & prioritization — results

Bioinformatics backing for `../PDB.md`. All scripts use the Python standard library only
(no third-party deps); `inventory_pdb.py` is fully offline, `enrich_rcsb.py` needs network
access to `https://data.rcsb.org/graphql`.

## Pipeline

```
inventory_pdb.py   cached *-uniprot.txt (DR PDB) + *-goa.tsv  ->  data/pdb_inventory.tsv
                                                                  data/pdb_gene_summary.tsv
enrich_rcsb.py     RCSB GraphQL for no-exp-MF candidate genes  ->  data/pdb_enriched.tsv
                                                                  data/pdb_gene_enriched.tsv
```

## Method

1. **Inventory (offline).** Parse every `genes/*/*/*-uniprot.txt` for `DR PDB` cross-
   references → PDB id, method, resolution, chain/residue ranges. Coverage = fraction of the
   protein length (UniProt `SQ` line) spanned by the union of residue ranges. Parse the
   sibling `*-goa.tsv` to count **experimental** GO annotations (evidence codes
   EXP/IDA/IPI/IMP/IGI/IEP) by aspect.

2. **Candidate selection.** Genes with `exp_mf == 0` (no experimental molecular-function GO)
   but ≥1 structure — these are where a structure most plausibly upgrades the annotation.

3. **Enrichment (network).** For each candidate's PDB entries, query the RCSB Data API for
   `struct.title`, protein/nucleic-acid entity counts, and non-polymer (ligand) chem-comp
   ids. Filter ligands against a buffer/cryo blocklist (`HOH`, `GOL`, `EDO`, PEGs, `SO4`,
   `ACT`, halides, …) so that "meaningful ligand" ≈ substrate/product/cofactor/inhibitor.
   A curated `RICH` set (FAD, NAD(P), PQQ, F430, Fe–S, heme, transition metals, nucleotides,
   …) marks cofactor-grade ligands.

4. **Score.** Per gene:
   `score = 3·(any cofactor) + 2·(any ligand) + 2·(any complex) + 1.5·(bound nucleic acid)
            + 1·(coverage≥0.8)`, then `×1.5` if the gene has **zero** experimental GO of any
   aspect (sparsity multiplier).

## Headline numbers

- 949 / 2529 genes have ≥1 deposited PDB structure; 13,415 entries total.
- 115 of those genes lack any experimental MF GO (105 resolved in RCSB enrichment):
  42 with a bound cofactor/metal, 69 with a meaningful ligand, 40 in a complex,
  6 with bound nucleic acid, 23 apo/no-partner.

## Output schema

`pdb_inventory.tsv` — one row per deposited entry: organism, gene, uniprot, length, pdb_id,
method, resolution_A, chains, coverage_frac.

`pdb_gene_summary.tsv` — one row per gene: n_pdb, methods, best_resolution_A,
max_coverage_frac, exp_mf/exp_bp/exp_cc/exp_total, any_experimental.

`pdb_enriched.tsv` — one row per candidate entry: title, n_protein, n_nucleic, ligands_all,
ligands_meaningful, n_meaningful, has_cofactor, is_complex.

`pdb_gene_enriched.tsv` — one row per candidate gene, ranked by priority_score, with
pdb_with_cofactor / pdb_with_ligand / pdb_with_complex / has_nucleic_acid and the
deduplicated cofactor & ligand lists.

## Caveats

- "No experimental MF GO" reflects the cached GOA snapshot, not literature reality; several
  top hits (mcrA, merA, RuBisCO) are textbook enzymes whose GOA is simply IEA-only. The
  structure + literature justifies promoting the annotation.
- Ligand flags are clues, not proof; reviewer judgment still distinguishes a genuine
  substrate/cofactor from an adventitious binder.
- RCSB ligand lists are per-entry; the per-gene rollup reports whether *any* deposited
  structure carries each feature.
- A few candidate PDB ids did not resolve in the GraphQL response (obsolete/superseded ids);
  they appear with blank enrichment rather than being dropped from the inventory.
