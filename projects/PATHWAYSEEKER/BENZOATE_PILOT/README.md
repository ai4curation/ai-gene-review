---
species: []
title: PathwaySeeker Benzoate Pilot
---

# PathwaySeeker Benzoate Pilot

## Source

This pilot imports the public PathwaySeeker example output directly: `matched_metabolites_reactions_all.csv`, `graph_notebook.json`, `ko_to_reactions.csv`, and `proteomics_with_ko.csv`.

Source repository commit used for this run: `ad38526f7877047ed08a645b1c1b2db7190a4696`.

Pilot integration of real PathwaySeeker output for a benzoate/catechol target pathway. The input is the public PathwaySeeker example output from pnnl/PathwaySeeker. The target pathway is the benzoate-to-catechol and catechol ortho-cleavage route used in the first pilot. The integration result is allowed to be negative or partial.

## Target Pathway

| KEGG reaction | Expected step | PathwaySeeker status | Origin |
|---|---|---|---|
| R05621 | benzoate 1,2-dioxygenation | missing |  |
| R00813 | dihydrodiol dehydrogenation to catechol | missing |  |
| R00817 | catechol ortho-cleavage to cis,cis-muconate | missing |  |
| R06989 | muconate cycloisomerization | missing |  |
| R06990 | muconolactone isomerization | missing |  |
| R02991 | 3-oxoadipate enol-lactone hydrolysis | missing |  |

## Real PathwaySeeker Result

The real PathwaySeeker output does not recover the selected benzoate-to-catechol / catechol ortho-cleavage pathway reactions. That is the important result: the integration should record this as absent or partial evidence, not fill the pathway from KEGG.

Observed target-compound coverage:

| Compound | Label | Status | Matched rows | Origin |
|---|---|---|---:|---|
| C00180 | Benzoate | observed | 3 | proteomics |
| C06321 | (1R,6S)-1,6-dihydroxycyclohexa-2,4-diene-1-carboxylate | missing | 0 |  |
| C00090 | Catechol | observed | 1 | proteomics |
| C02480 | cis,cis-Muconate | missing | 0 |  |
| C14610 | (S)-5-oxo-2,5-dihydrofuran-2-acetate | missing | 0 |  |
| C03586 | 3-oxoadipate enol-lactone | missing | 0 |  |
| C00846 | 3-oxoadipate | missing | 0 |  |

The benzoate/catechol neighborhood contains 4 PathwaySeeker reaction(s): `R00815`, `R01295`, `R01421`, `R05590`.

| Reaction | Compound | Role | Origin | Equation |
|---|---|---|---|---|
| R00815 | C00090 | products | proteomics | `C00146 + C00007 + C00005 + C00080 <=> C00090 + C00006 + C00001` |
| R00815 | C00146 | substrates | proteomics | `C00146 + C00007 + C00005 + C00080 <=> C00090 + C00006 + C00001` |
| R01295 | C00156 | products | proteomics | `C00180 + C03024 + C00007 <=> C00156 + C03161 + C00001` |
| R01295 | C00180 | substrates | proteomics | `C00180 + C03024 + C00007 <=> C00156 + C03161 + C00001` |
| R01421 | C00180 | products | proteomics | `C06206 + C00001 <=> C00180 + C00009` |
| R01421 | C06206 | substrates | proteomics | `C06206 + C00001 <=> C00180 + C00009` |
| R05590 | C00180 | products | proteomics | `C09815 + C00001 <=> C00180 + C00014` |
| R05590 | C09815 | substrates | proteomics | `C09815 + C00001 <=> C00180 + C00014` |

## Protein Evidence

| Reaction | KO | Protein ID | Description | AgitWOAO mean | AgitWAO mean | StatWOAO mean | StatWAO mean |
|---|---|---|---|---:|---:|---:|---:|
| R00815 | K03380 | `jgi|Trave1|123403|e_gw1.6.1722.1` | E1.14.13.7; phenol 2-monooxygenase (NADPH) [EC:1.14.13.7] |  | 24.468 |  |  |
| R00815 | K03380 | `jgi|Trave1|47634|gm1.6518_g` | E1.14.13.7; phenol 2-monooxygenase (NADPH) [EC:1.14.13.7] |  |  |  | 29.765 |
| R00815 | K03380 | `jgi|Trave1|47635|gm1.6519_g` | E1.14.13.7; phenol 2-monooxygenase (NADPH) [EC:1.14.13.7] |  |  |  | 29.63 |
| R00815 | K03380 | `jgi|Trave1|58730|estExt_fgenesh1_pm.C_6_t10263` | E1.14.13.7; phenol 2-monooxygenase (NADPH) [EC:1.14.13.7] | 36.927 | 37.103 | 35.791 | 33.502 |
| R01295 | K07824 | `jgi|Trave1|129211|e_gw1.9.1568.1` | CYP53A1; benzoate 4-monooxygenase [EC:1.14.14.92] | 34.098 | 34.595 | 34.612 | 32.964 |
| R01421 | K01512 | `jgi|Trave1|132453|e_gw1.11.1338.1` | acyP; acylphosphatase [EC:3.6.1.7] | 31.193 | 31.826 | 31.211 | 32.28 |
| R05590 | K01426 | `jgi|Trave1|133552|e_gw1.12.147.1` | E3.5.1.4, amiE; amidase [EC:3.5.1.4] | 29.613 | 28.895 |  |  |
| R05590 | K01426 | `jgi|Trave1|160039|estExt_Genewise1Plus.C_1_t80118` | E3.5.1.4, amiE; amidase [EC:3.5.1.4] | 30.68 | 32.305 | 31.603 | 31.333 |
| R05590 | K01426 | `jgi|Trave1|161547|estExt_Genewise1Plus.C_2_t40498` | E3.5.1.4, amiE; amidase [EC:3.5.1.4] | 32.647 | 31.807 | 31.902 |  |
| R05590 | K01426 | `jgi|Trave1|25794|fgenesh1_kg.1_#_615_#_isotig05103` | E3.5.1.4, amiE; amidase [EC:3.5.1.4] | 31.964 | 33.475 | 33.501 | 31.97 |
| R05590 | K01426 | `jgi|Trave1|52365|gm1.11249_g` | E3.5.1.4, amiE; amidase [EC:3.5.1.4] |  | 29.656 |  |  |

## Graph Subset

The extracted real PathwaySeeker graph subset has 6 nodes and 4 edges.

## Integration Implications

- A real PathwaySeeker import must distinguish exact target-pathway reactions from looser compound-neighborhood reactions. Compound adjacency alone should not seed GO annotations.
- Missing target reactions are meaningful evidence. The importer should record absent or partial pathway support instead of backfilling from KEGG modules.
- The public example data uses JGI Trave1 protein identifiers and KO-derived proteomics evidence, so it cannot directly update the P. putida KT2440 gene reviews without an organism-specific protein mapping.
- Proteomics-only PathwaySeeker hits should be represented as pathway evidence or prediction candidates, not accepted GO annotations, unless literature or curated review support is added.

## Generated Artifacts

- `pathwayseeker_reaction_coverage.csv`
- `pathwayseeker_matched_reactions.csv`
- `pathwayseeker_protein_evidence.csv`
- `pathwayseeker_graph_subset.json`
- `source_metadata.json`

## Reproduce

```bash
git clone https://github.com/pnnl/PathwaySeeker.git /tmp/PathwaySeeker
git -C /tmp/PathwaySeeker checkout ad38526f7877047ed08a645b1c1b2db7190a4696
uv run python scripts/pathwayseeker_pilot_report.py projects/PATHWAYSEEKER/BENZOATE_PILOT/manifest.yaml --pathwayseeker-output /tmp/PathwaySeeker/output --pathwayseeker-root /tmp/PathwaySeeker --output projects/PATHWAYSEEKER/BENZOATE_PILOT/README.md --artifact-dir projects/PATHWAYSEEKER/BENZOATE_PILOT
uv run ai-gene-review render-projects projects/PATHWAYSEEKER/BENZOATE_PILOT/README.md -o projects/PATHWAYSEEKER/BENZOATE_PILOT
```
