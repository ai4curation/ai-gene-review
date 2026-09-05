---
species:
  - PSEPK
title: PathwaySeeker PSEPK Benzoate Real-Omics Pilot
---

# PathwaySeeker PSEPK Benzoate Real-Omics Pilot

## What this pilot is

One-pathway pilot for integrating PathwaySeeker-compatible graph artifacts with AI Gene Review. The real omics input is the public MetaboLights MTBLS1715 processed metabolomics table for P. putida KT2440 grown with [U-13C6]-glucose plus unlabeled benzoate. KEGG supplies reaction topology; it is not counted as omics evidence. AIGR gene reviews supply reviewed gene anchors.

This is a real-data pilot. The experimental evidence in this report is limited to:

- processed MTBLS1715 metabolomics abundance rows for KT2440 samples;
- MTBLS1715 sample metadata showing the carbon source context;
- existing AIGR gene-review files for gene-function anchors.

KEGG reaction records are used only as reaction topology and identifiers. They do not count as experimental omics evidence.

## Source Data

- MetaboLights `MTBLS1715`: https://www.ebi.ac.uk/metabolights/MTBLS1715
- PRIDE `PXD013605`: https://www.ebi.ac.uk/pride/archive/projects/PXD013605
- Publication `PMID:33273114` / DOI `10.1073/pnas.2016380117`: Hierarchical routing in carbon metabolism favors iron-scavenging strategy in iron-deficient soil Pseudomonas species
- Sample carbon-source context: D-Glucose (`C00031`), Benzoate (`C00180`).

The MAF contains 14 measured metabolites across 16 KT2440 glucose-plus-benzoate sample columns. No processed MAF row maps to benzoate, catechol, cis,cis-muconate, muconolactone, or 3-oxoadipate.

The cached PRIDE project metadata documents the matched proteomics accession, but this pilot does not parse raw PRIDE spectra or treat the PRIDE record as a protein-abundance matrix.

## Measured Metabolites

| Metabolite | Source ID | KEGG | FeInt T1 mean | FeLim T1 mean | FeLim T2 mean | FeLim T3 mean | log2 FeLim T1 / FeInt T1 | Mapping |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Gluconate | CHEBI:24265 | C00257 | 2.95e+05 | 1.65e+05 | 1.86e+05 | 66699 | -0.84 | verified_in_cached_kegg_find |
| Glucose 6-phosphate | CHEBI:4170 | C00092 | 85671 | 5.18e+05 | 1.63e+06 | 42720 | 2.60 | verified_in_cached_kegg_find |
| Fructose 6-phosphate | CHEBI:78697 | C00085 | 36776 | 1.33e+05 | 3.08e+05 | 41507 | 1.86 | verified_in_cached_kegg_find |
| 6-phosphogluconic acid | CHEBI:48928 | C00345 | 2.69e+05 | 6.79e+05 | 2.63e+05 | 15035 | 1.34 | verified_in_cached_kegg_find |
| Dihydroxyacetone phosphate | CHEBI:16108 | C00111 | 27777 | 93983 | 2.15e+05 | 2467 | 1.76 | verified_in_cached_kegg_find |
| 3-phosphoglyceric acid | CHEBI:17050 | C00197 | 2.73e+05 | 75659 | 3.47e+05 | 71902 | -1.85 | verified_in_cached_kegg_find |
| Phosphoenolpyruvate | CHEBI:18021 | C00074 | 1.17e+06 | 3.13e+05 | 1.81e+06 | 1.42e+05 | -1.90 | verified_in_cached_kegg_find |
| Pyruvate | CHEBI:15361 | C00022 | 5e+05 | 1.54e+06 | 3.91e+06 | 3.9e+05 | 1.62 | verified_in_cached_kegg_find |
| Aspartic acid | CHEBI:17053 | C00049 | 4.62e+05 | 1.01e+06 | 7.7e+05 | 1.87e+05 | 1.13 | verified_in_cached_kegg_find |
| Malate | CHEBI:25115 | C00149 | 6.8e+05 | 1.07e+06 | 2.28e+06 | 9.88e+05 | 0.65 | verified_in_cached_kegg_find |
| Fumarate | CHEBI:29806 | C00122 | 3.23e+05 | 1.51e+05 | 2.1e+05 | 1.54e+05 | -1.09 | verified_in_cached_kegg_find |
| Succinate | CHEBI:26806 | C00042 | 8.58e+05 | 3.44e+06 | 3.15e+06 | 5.22e+05 | 2.00 | verified_in_cached_kegg_find |
| Alpha-ketoglutaric acid | CHEBI:16810 | C00026 | 2.34e+05 | 3.49e+05 | 9.39e+05 | 37537 | 0.58 | verified_in_cached_kegg_find |
| Citrate | CHEBI:16947 | C00158 | 1.71e+06 | 7.87e+06 | 5.85e+07 | 2.07e+06 | 2.21 | verified_in_cached_kegg_find |

## Central-Carbon Reaction Coverage

Coverage status is computed from non-common reaction participants after removing water, ATP/ADP, redox cofactors, oxygen, phosphate, CO2, CoA, quinone/ubiquinone, and protons.

| Reaction | Step | AIGR genes | Coverage | Detail | Equation |
| --- | --- | --- | --- | --- | --- |
| R06620 | PQQ-dependent glucose dehydrogenase context | gcd | sample_context_only | measured=-; sample_context=C00031; unmeasured=C00198 | `C00031 + C00399 <=> C00198 + C00390` |
| R01519 | gluconolactone hydrolysis to gluconate |  | measured_partial | measured=C00257; sample_context=-; unmeasured=C00198 | `C00198 + C00001 <=> C00257` |
| R01737 | gluconate kinase to 6-phosphogluconate |  | measured_complete | measured=C00257,C00345; sample_context=-; unmeasured=- | `C00002 + C00257 <=> C00008 + C00345` |
| R00835 | glucose-6-phosphate dehydrogenase | zwf | measured_partial | measured=C00092; sample_context=-; unmeasured=C01236 | `C00092 + C00006 <=> C01236 + C00005 + C00080` |
| R02035 | 6-phosphogluconolactone hydrolysis |  | measured_partial | measured=C00345; sample_context=-; unmeasured=C01236 | `C01236 + C00001 <=> C00345` |
| R02036 | phosphogluconate dehydratase | edd | measured_partial | measured=C00345; sample_context=-; unmeasured=C04442 | `C00345 <=> C04442 + C00001` |
| R05605 | KDPG aldolase | eda | measured_partial | measured=C00022; sample_context=-; unmeasured=C00118,C04442 | `C04442 <=> C00118 + C00022` |
| R00771 | glucose-6-phosphate isomerase |  | measured_complete | measured=C00085,C00092; sample_context=-; unmeasured=- | `C00092 <=> C00085` |
| R00200 | pyruvate kinase / PEP-pyruvate interconversion |  | measured_complete | measured=C00022,C00074; sample_context=-; unmeasured=- | `C00002 + C00022 <=> C00008 + C00074` |
| R01325 | citrate aconitase step |  | measured_partial | measured=C00158; sample_context=-; unmeasured=C00417 | `C00158 <=> C00417 + C00001` |
| R00342 | malate dehydrogenase |  | measured_partial | measured=C00149; sample_context=-; unmeasured=C00036 | `C00149 + C00003 <=> C00036 + C00004 + C00080` |
| R00355 | aspartate aminotransferase / oxaloacetate surrogate context |  | measured_partial | measured=C00026,C00049; sample_context=-; unmeasured=C00025,C00036 | `C00049 + C00026 <=> C00036 + C00025` |
| R01082 | fumarase |  | measured_complete | measured=C00122,C00149; sample_context=-; unmeasured=- | `C00149 <=> C00122 + C00001` |
| R02164 | succinate dehydrogenase |  | measured_complete | measured=C00042,C00122; sample_context=-; unmeasured=- | `C15602 + C00042 <=> C15603 + C00122` |

## Aromatic Branch Coverage Check

No aromatic-ring-cleavage intermediates are present as measured compounds in the processed MAF. Benzoate is present only as a sample carbon-source context.

| Reaction | Step | AIGR genes | Coverage | Detail | Equation |
| --- | --- | --- | --- | --- | --- |
| R05621 | benzoate 1,2-dioxygenation | benA, benB, benC | sample_context_only | measured=-; sample_context=C00180; unmeasured=C06321 | `C00180 + C00004 + C00080 + C00007 <=> C06321 + C00003` |
| R00813 | dihydrodiol dehydrogenation to catechol | benD | kegg_topology_only | measured=-; sample_context=-; unmeasured=C00090,C06321 | `C06321 + C00003 <=> C00090 + C00004 + C00011 + C00080` |
| R00817 | catechol 1,2-dioxygenation | catA | kegg_topology_only | measured=-; sample_context=-; unmeasured=C00090,C02480 | `C00090 + C00007 <=> C02480` |
| R06989 | muconate cycloisomerization | catB | kegg_topology_only | measured=-; sample_context=-; unmeasured=C02480,C14610 | `C02480 <=> C14610` |
| R06990 | muconolactone isomerization | catC | kegg_topology_only | measured=-; sample_context=-; unmeasured=C03586,C14610 | `C14610 <=> C03586` |
| R02991 | 3-oxoadipate enol-lactone hydrolysis | pcaD | kegg_topology_only | measured=-; sample_context=-; unmeasured=C00846,C03586 | `C03586 + C00001 <=> C00846` |

## AIGR Gene Anchors

| Gene | UniProt | Review status | Core reviewed terms | Review file |
| --- | --- | --- | --- | --- |
| gcd | Q88MX4 | DRAFT | quinoprotein glucose dehydrogenase activity; glucose catabolic process; pyrroloquinoline quinone binding | genes/PSEPK/gcd/gcd-ai-review.yaml |
| glk | Q88P42 | COMPLETE | glucokinase activity; glucose 6-phosphate metabolic process; glycolytic process via Entner-Doudoroff Pathway; cytosol | genes/PSEPK/glk/glk-ai-review.yaml |
| zwf | Q88C32 | DRAFT | glucose-6-phosphate dehydrogenase activity; cytosol | genes/PSEPK/zwf/zwf-ai-review.yaml |
| edd | Q88P43 | DRAFT | phosphogluconate dehydratase activity; Entner-Doudoroff pathway through 6-phosphogluconate | genes/PSEPK/edd/edd-ai-review.yaml |
| eda | Q88P29 | DRAFT | 2-dehydro-3-deoxy-phosphogluconate aldolase activity; Entner-Doudoroff pathway through 6-phosphogluconate | genes/PSEPK/eda/eda-ai-review.yaml |
| benA | Q88I40 | COMPLETE | benzoate 1,2-dioxygenase activity; benzoate catabolic process via hydroxylation; benzoate catabolic process | genes/PSEPK/bena/bena-ai-review.yaml |
| benB | Q88I39 | DRAFT | benzoate 1,2-dioxygenase activity; benzoate catabolic process via hydroxylation | genes/PSEPK/benB/benB-ai-review.yaml |
| benC | Q88I38 | DRAFT | ferredoxin-NAD+ reductase activity; benzoate 1,2-dioxygenase activity; benzoate catabolic process via hydroxylation | genes/PSEPK/benC/benC-ai-review.yaml |
| benD | Q88I37 | COMPLETE | 1,6-dihydroxycyclohexa-2,4-diene-1-carboxylate dehydrogenase activity; benzoate catabolic process via hydroxylation | genes/PSEPK/benD/benD-ai-review.yaml |
| catA | Q88GK8 | DRAFT | catechol 1,2-dioxygenase activity; catechol-containing compound catabolic process; beta-ketoadipate pathway | genes/PSEPK/catA/catA-ai-review.yaml |
| catB | Q88GK6 | COMPLETE | muconate cycloisomerase activity; beta-ketoadipate pathway | genes/PSEPK/catB/catB-ai-review.yaml |
| catC | Q88GK7 | DRAFT | muconolactone delta-isomerase activity; catechol catabolic process, ortho-cleavage | genes/PSEPK/catC/catC-ai-review.yaml |
| pcaD | Q88N36 | DRAFT | 3-oxoadipate enol-lactonase activity; beta-ketoadipate pathway | genes/PSEPK/pcaD/pcaD-ai-review.yaml |

## Generated PathwaySeeker Artifacts

- `metabolomics_with_C_numbers.csv`: MAF-derived metabolite table with KEGG C numbers and cached lookup provenance.
- `metabolite_condition_summary.csv`: condition-level abundance summary for the 16 KT2440 glucose-plus-benzoate samples.
- `reaction_to_compounds_from_metabolomics.csv`: PathwaySeeker-compatible reaction/compound/role rows for the selected pathway reactions; the origin column separates measured metabolites from sample context and unmeasured topology.
- `matched_metabolites_reactions_all.csv`: final merged reaction/compound table for this pilot; origins distinguish metabolomics, sample metadata, and KEGG topology.
- `pathwayseeker_matched_reactions.csv`: AIGR-facing copy of the matched reaction table.
- `pathwayseeker_reaction_coverage.csv`: central-carbon plus aromatic-branch coverage table.
- `pathwayseeker_graph_subset.json`: graph JSON with compound, reaction, and reviewed-gene nodes; AIGR anchors appear here as `aigr_review` edges.
- `source_metadata.json`: source-file checksums.

The graph subset has 59 nodes and 55 edges.

## Integration Decision

This is suitable for an AIGR pilot as pathway-context evidence, not as direct evidence to create or accept enzymatic GO annotations.

Specific implications:

- The real metabolomics supports central-carbon coverage around gluconate, glucose-6-phosphate, 6-phosphogluconate, pyruvate/PEP, and TCA nodes during glucose-plus-benzoate growth.
- The aromatic benzoate-to-catechol branch is not directly observed in the processed metabolomics table; its reviewed genes should stay supported by literature/review evidence, not by this MAF.
- `gcd`, `zwf`, `edd`, and `eda` can be linked as reviewed anchors to the pathway graph, but the graph edge itself should be tagged as context unless both protein abundance and metabolite evidence are present.
- A proteomics-enabled second pass needs a parsed KT2440 protein-abundance table from PXD013605 or supplementary data with stable locus/UniProt mapping.

## Reproduce

```bash
.venv/bin/python scripts/pathwayseeker_psepk_benzoate_real_pilot.py projects/PATHWAYSEEKER/PSEPK_BENZOATE_REAL/manifest.yaml
.venv/bin/ai-gene-review render-projects projects/PATHWAYSEEKER/PSEPK_BENZOATE_REAL/README.md -o projects/PATHWAYSEEKER/PSEPK_BENZOATE_REAL
```
