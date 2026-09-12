---
title: "PDB inventory & prioritization — results"
---
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

   The inventory also reads each gene's `*-ai-review.yaml` and flags **contested catalytic
   MF**: a molecular-function term whose label denotes catalytic activity (`…ase activity`,
   `catalytic activity`, kinase/transferase/hydrolase/…, excluding `binding`) and whose review
   `action` is `REMOVE` or `MARK_AS_OVER_ANNOTATED`. Plus an `is_eukaryote` flag.

2. **Candidate selection (union of three cuts, tagged in `candidate_reason`).**
   - `dark_mf` — `exp_mf == 0` (no experimental MF GO): a structure grounds a first MF.
   - `euk` — eukaryotic **and** `exp_mf <= 2`: broadens beyond the prokaryote-dominated dark
     set so eukaryotic proteins aren't lost; structure sharpens an IEA term / pins complex.
   - `contested` — ≥1 contested catalytic MF (above): structure adjudicates the disputed
     activity. 278 genes total (union of the three cuts). To bound RCSB calls, ≤15 entries are queried per gene (the
     rollup only needs "does *any* deposited structure carry feature X").

3. **Enrichment (network).** For each candidate's PDB entries, query the RCSB Data API for
   `struct.title`, the **primary-citation PMID/DOI/year**, protein/nucleic-acid entity counts,
   and non-polymer (ligand) chem-comp ids. Filter ligands against a buffer/cryo blocklist
   (`HOH`, `GOL`, `EDO`, PEGs, `SO4`, `ACT`, halides, …) so that "meaningful ligand" ≈
   substrate/product/cofactor/inhibitor. A curated `RICH` set (FAD, NAD(P), PQQ, F430, Fe–S,
   heme, transition metals, nucleotides, …) marks cofactor-grade ligands.

4. **Score.** Per gene:
   `score = 3·(any cofactor) + 2·(any ligand) + 2·(any complex) + 1.5·(bound nucleic acid)
            + 1·(coverage≥0.8)`, then `×1.5` if the gene has **zero** experimental GO of any
   aspect (sparsity multiplier).

## Headline numbers

- 949 / 2529 genes have ≥1 deposited PDB structure; 13,415 entries total; 815 eukaryotic.
- Candidate union = 278 genes: `dark_mf` 114, `euk` 100, `contested` (catalytic MF) 130
  (overlapping). 1,361 PDB entries queried (≤15/gene).
- The strict `dark_mf` cut (102 resolved): 40 with a bound cofactor/metal, 66 with a
  meaningful ligand, 36 in a complex, 6 with bound nucleic acid, 23 apo/no-partner.
- `contested` catalytic cases split into **over-general parent terms** (cofactor present →
  pick the specific child) vs **genuinely-wrong specifics** (structure/cofactor refutes the
  call, e.g. HEN1 PPIase→SAH-methyltransferase; CASP3 aspartic→cysteine protease).

## Output schema

`pdb_inventory.tsv` — one row per deposited entry: organism, gene, uniprot, length, pdb_id,
method, resolution_A, chains, coverage_frac.

`pdb_gene_summary.tsv` — one row per gene: is_eukaryote, n_pdb, methods, best_resolution_A,
max_coverage_frac, exp_mf/exp_bp/exp_cc/exp_total, any_experimental, n_contested_cat_mf,
contested_cat_mf (term|label|action list).

`pdb_enriched.tsv` — one row per candidate entry: title, pmid, doi, year, n_protein,
n_nucleic, ligands_all, ligands_meaningful, n_meaningful, has_cofactor, is_complex.

`pdb_gene_enriched.tsv` — one row per candidate gene, ranked by priority_score, with
candidate_reason, n_pdb / n_pdb_sampled, pdb_with_cofactor / pdb_with_ligand /
pdb_with_complex / has_nucleic_acid, deduplicated cofactor & ligand lists, contested_cat_mf,
and up to 3 representative structure_papers (ligand/cofactor-bearing, newest first).

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
- The `contested` cut is keyword-based on the GO **label** (catalytic roots, excluding
  "binding") cross-referenced with the GOA aspect; it can include over-general parents that
  were merely marked over-annotated (not pseudo-enzymes). The `contested_cat_mf` field gives
  the exact term/action so each case can be triaged. Verify the disputed-term mapping before
  acting.
- Per-gene enrichment is capped at 15 entries (`CAP`), so `pdb_with_*` counts are over the
  sampled entries, not all deposited entries; `n_pdb` (true total) and `n_pdb_sampled` are
  both reported. Raise `CAP` to enrich exhaustively.
- `structure_papers` are RCSB **per-entry** primary citations and are frequently peripheral
  (inhibitor/methods) papers, not the definitive structure/function paper — verify per
  `STRUCTURE_PAPERS.md` before citing.
