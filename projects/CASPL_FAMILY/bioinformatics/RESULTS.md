---
title: "CASP-like (CASPL) orthology / phylogeny analysis — poplar vs Arabidopsis"
species: [ARATH, POPTR]
---

# CASP-like (CASPL) orthology / phylogeny analysis — poplar vs Arabidopsis

## Purpose

The 20 *Populus trichocarpa* CASP-like (CASPL) gene reviews are largely uncharacterized
proteins. For five of them the review text transfers functional hypotheses from
**characterized Arabidopsis orthologs** in the same Roppolo subfamily
(CASPL1B/1D → aquaporin PIP2;1 / suberized endodermis, [PMID:30767240]; CASPL4C →
cold tolerance / growth, [PMID:26399665]). This analysis tests, with sequence data, whether
those orthology assignments are real — i.e. whether a poplar CASPL with a given subfamily
code is actually most similar to the Arabidopsis protein(s) carrying that code.

## Method (reproducible)

`orthology_analysis.py` uses **only** Biopython (no external aligners), so it runs anywhere:

1. `data/caspl.fasta` — 54 sequences fetched from UniProt: all 20 reviewed poplar CASPLs +
   all 34 reviewed Arabidopsis CASPLs (the Golgi golgin "Protein CASP", Q9LS42, is excluded —
   it is not a Casparian-strip CASPL).
2. All-vs-all global pairwise alignment (`Bio.Align.PairwiseAligner`, BLOSUM62, gap −11/−1);
   percent identity = identical / aligned columns.
3. Cross-species **reciprocal best hits (RBH)** between poplar and Arabidopsis = putative
   ortholog pairs.
4. For each poplar protein: is its best Arabidopsis hit in the same **group** (leading digit
   of the code, e.g. `1B1` → group 1) and the same **exact code**?
5. Neighbour-joining tree (`results/caspl_nj_tree.nwk`).

Regenerate:

```bash
cd projects/CASPL_FAMILY/bioinformatics
uv run orthology_analysis.py
```

Outputs: `results/rbh_orthology.tsv`, `results/summary.json`, `results/caspl_nj_tree.nwk`.

## Results

54 sequences (20 POPTR, 34 ARATH).

**Group-level orthology is robust:** for **all 20** poplar CASPLs the single best Arabidopsis
hit falls in the **same Roppolo group** (`same_group = True` for every row below). 12 of 20 are
full reciprocal best hits; 8 of those match the **exact** subfamily code.

```
POPTR      ->ARATH       %id   RBH  grp  code
1B1        1B2          57.4 False True False
1B2        1B2          59.8  True True  True
1C1        1C1          37.5 False True  True
1C2        1C1          62.8  True True False
1C3        1C1          49.4 False True False
1D1        1D1          51.5  True True  True
1E1        1E1          50.3  True True  True
1F1        1F1          33.7 False True  True
1F2        1F1          34.3  True True False
1F3        1E2          29.3 False True False
2A2        2A1          50.9  True True False
2B1        2B2          69.3 False True False
2B2        2B2          69.8  True True  True
2C1        2C1          48.9  True True  True
2D1        2D1          44.7  True True  True
3A1        3A1          42.7 False True  True
3A2        3A2          44.3  True True  True
4C1        4C1          66.0 False True  True
4C2        4C1          68.0  True True False
4D1        4D1          46.0  True True  True
```

### What this means for the functional transfers

- **CASPL1B / 1D (suberization / PIP2;1 aquaporin hypothesis).**
  PtCASPL1B2 ↔ AtCASPL1B2 (59.8 %, RBH, exact code) and PtCASPL1D1 ↔ AtCASPL1D1 (51.5 %, RBH,
  exact code) are clean orthologs. PtCASPL1B1's top Arabidopsis hit is AtCASPL1B2 (57.4 %), not
  AtCASPL1B1 — but [PMID:30767240] characterized **both** AtCASPL1B1 *and* AtCASPL1B2 (and 1D1/1D2)
  as PIP2;1-interacting, suberized-endodermis proteins, so the transfer holds at the
  **1B/1D-subgroup** level. Conclusion: the suberization / aquaporin hypothesis is appropriately
  attributed to the poplar 1B/1D genes, with the caveat that exact 1:1 orthology is blurred by
  independent within-group duplications.

- **CASPL4C (cold tolerance / growth hypothesis).**
  Arabidopsis has a single group-4C gene (AtCASPL4C1); poplar has two (PtCASPL4C1, PtCASPL4C2)
  from a poplar-specific duplication. Both are top-hit to AtCASPL4C1 (66 % and 68 %), i.e. they
  are **co-orthologs** of the characterized AtCASPL4C1. Conclusion: transferring the
  AtCASPL4C1 cold/growth hypothesis to **both** PtCASPL4C1 and PtCASPL4C2 is justified.

### Caveats

- Pairwise %identity + RBH is a lightweight orthology proxy, not a full phylogeny with bootstrap
  support; the NJ tree (`caspl_nj_tree.nwk`) is provided for inspection but branch support was not
  computed (no external ML tree builder available in this environment).
- The Roppolo letter-number codes (e.g. 1B1 vs 1B2) denote fine subfamily sub-clades, not strict
  1:1 orthology across species; this is exactly why group-level (not exact-code) transfer is the
  correct granularity, as the data confirm.
- This analysis is **functional-hypothesis support only** — it does not by itself justify adding
  experimental GO annotations to the poplar genes (those remain IEA plasma-membrane).
