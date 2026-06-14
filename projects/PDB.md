# PDB: Deposited Structures as Functional-Insight Evidence

## Goal

Many genes in this review pipeline have experimentally solved 3D structures deposited in
the [Protein Data Bank](https://www.rcsb.org/). A structure is not just a picture: when it
captures a **bound ligand, cofactor, catalytic metal, or partner macromolecule**, it is
direct, experimental evidence for molecular function, binding, and complex membership — the
very things GO annotation review hinges on.

This project (1) inventories what is deposited across the whole pipeline, and (2) prioritizes
the structures most likely to *change or strengthen* a gene's functional annotation, so that
structure-informed review effort goes where it pays off.

## What "functional insight" means here

A deposited structure is most valuable for review when **what is bound in it** tells us
something the current annotations do not. The prioritization therefore combines two axes:

1. **Structure richness** — what the structure actually contains:
   - bound **cofactor / catalytic metal** (FAD, NAD(P), PQQ, F430, Fe–S clusters, heme, Zn, …)
     → strongest single clue to catalytic mechanism / molecular function
   - bound **substrate / product / inhibitor ligand** → active-site and specificity evidence
   - **complex** (≥2 protein entities, or bound nucleic acid) → interaction & CC evidence
   - high **sequence coverage** (full-length vs a short peptide fragment in a partner's structure)

2. **Annotation sparsity** — a structure adds the most where we currently know the least.
   Genes whose GO annotations are **electronic-only (IEA/IBA)** with *no experimental
   molecular-function term* are upweighted: here a ligand-bound structure (plus literature)
   can ground a specific, experiment-grade MF annotation that today rests only on inference.

The two are multiplied: `richness × sparsity`. An apo structure of an already
well-annotated protein scores low; a cofactor-bound, full-length structure of an IEA-only
enzyme scores high.

## What is deposited (pipeline-wide inventory)

Computed offline from the cached UniProt records (`*-uniprot.txt`, `DR PDB` cross-references):

| Metric | Count |
|--------|------:|
| Genes with ≥1 deposited PDB structure | **949** / 2529 |
| Total deposited PDB entries | **13,415** |
| Genes with a structure but **no experimental GO at all** | 73 |
| Genes with a structure but **no experimental molecular-function GO** | 115 |

Top organisms by genes-with-structure: human (588), yeast (65), ARATH (53), BPT4 (32),
mouse (30), ECOLI (23), PSEPK (19), SCHPO (17), worm (17), rat (15).

Full inventory: `pdb-bioinformatics/data/pdb_inventory.tsv` (per entry) and
`pdb_gene_summary.tsv` (per gene).

## Prioritized candidates (first pass)

The 115 genes with a structure but no experimental MF GO were enriched with RCSB metadata
(bound ligands, entity counts, titles). Of the 105 that resolved:

- **42** have a structure with a bound **cofactor / catalytic metal**
- **69** have a structure with a meaningful (non-buffer) **ligand**
- **40** are captured in a **complex**; 6 with bound **nucleic acid**
- 23 are apo with no partner (lower structural-insight yield)

These are **IEA-only** enzymes/proteins whose function is structurally (and often
biochemically) characterized but whose GO annotations have not been promoted beyond
electronic inference — the sweet spot for structure-grounded review.

| # | Gene | Organism | UniProt | n PDB | cofactor | ligand | complex | cofactors/ligands |
|---|------|----------|---------|------:|:--------:|:------:|:-------:|-------------------|
| 1 | rpsD | PSEAE | O52759 | 6 | ✓ | ✓ | ✓ | GDP,ZN |
| 2 | psaC | CHLRE | Q00914 | 17 | ✓ | ✓ | ✓ | FES,SF4 |
| 3 | secA | BACSU | P28366 | 18 | ✓ | ✓ | ✓ | ADP |
| 4 | (DsrAB) | DESVH | P07598 | 12 | ✓ | ✓ | ✓ | FE2,HEC,SF4,ZN |
| 5 | mcrA | METAC | Q8THH1 | 4 | ✓ | ✓ | ✓ | COB,F430,FE,SAM,SF4 |
| 6 | wac | BPT4 | P10104 | 117 | ✓ | ✓ | ✓ | ZN |
| 7 | rbcL | 9POAL | P0C512 | 3 | ✓ | ✓ | ✓ | NDP (RuBisCO) |
| 8 | algK | PSEPK | Q88NC7 | 1 | ✓ | ✓ | ✓ | NI |
| 9 | mxaI | METEA | P14775 | 3 | ✓ | ✓ | ✓ | PQQ |
| 10 | fae | METEA | Q9FA38 | 11 |  | ✓ | ✓ | H4MPT,DCP,CA,MG |
| 12 | cbh1 | HYPJE | P62694 | 48 | ✓ | ✓ |  | (cellobiohydrolase) |
| 13 | pqqB | PSEPK | Q88QV5 | 8 | ✓ | ✓ |  | CU,MN,ZN |
| 16 | merA | PSEAI | P00392 | 6 | ✓ | ✓ |  | FAD,NADP |
| 17 | mtdA | METEA | P55818 | 5 | ✓ | ✓ |  | NADP |
| 18 | pcaF | PSEPK | Q88N39 | 4 | ✓ | ✓ |  | COA |
| 23 | mdh | METEA | Q84FY8 | 2 | ✓ | ✓ |  | NAD |
| 25 | xoxF1 | METEA | C5B120 | 2 | ✓ | ✓ |  | PQQ |

Full ranked list: `pdb-bioinformatics/data/pdb_gene_enriched.tsv`.

Patterns worth noting: a cluster of **methylotrophy / PQQ-dependent dehydrogenases**
(METEA `mxaI`, `xoxF1`, `mdh`, `mtdA`, `fae`, PSEPK `pedH`, `pqqB`) and **redox cofactor
enzymes** (`merA` FAD/NADP, `psaC`/`mcrA`/`pqqE` Fe–S, DsrAB heme/siroheme) — these have
diagnostic cofactors visible in their structures, making them low-effort, high-yield review
targets.

## Reproduce

```bash
# 1. offline inventory from cached UniProt + GOA (no network)
python3 projects/pdb-bioinformatics/inventory_pdb.py

# 2. RCSB enrichment of the prioritized (no-exp-MF) candidate genes (network)
python3 projects/pdb-bioinformatics/enrich_rcsb.py
```

See `pdb-bioinformatics/RESULTS.md` for method detail, caveats, and the full output schema.

## Caveats

- The "no experimental MF GO" flag is computed from the cached `*-goa.tsv`. It flags genes
  whose GO is electronic-only **in our snapshot**; some are well-characterized in the
  literature. That is the point — the structure + literature can justify promoting the
  annotation, not that the function is unknown.
- A bound ligand is a *clue*, not proof: crystallization additives are filtered out, but a
  flagged ligand still needs reviewer judgment (substrate vs adventitious binder).
- UniProt `DR PDB` residue ranges drive the coverage metric; a gene present only as a short
  peptide in a partner's structure scores low coverage, correctly.

## Next steps

- [ ] Run full gene reviews on the top cofactor-bound candidates (start: `mcrA`, `merA`,
      the METEA PQQ-dehydrogenase cluster), citing the PDB entry + bound cofactor as MF evidence.
- [ ] Extend enrichment beyond the no-exp-MF set to genes with **contested** function
      (cross-reference `CONTESTED_FUNCTION.md`) where a structure could adjudicate.
- [ ] For complexes (≥2 protein entities), map partners to UniProt to support CC / complex
      membership annotations.
- [ ] Consider adding a PDB-evidence field to the review schema (per `ALPHAFOLD.md` action items).
