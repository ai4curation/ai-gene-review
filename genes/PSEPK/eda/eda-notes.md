# eda Gene Review Notes

## Core identity

- `eda` in *Pseudomonas putida* KT2440 is UniProt `Q88P29` / locus tag `PP_1024` and is annotated as `2-dehydro-3-deoxy-phosphogluconate aldolase` with `EC=4.1.2.14` [file:PSEPK/eda/eda-uniprot.txt "RecName: Full=2-dehydro-3-deoxy-phosphogluconate aldolase"; file:PSEPK/eda/eda-uniprot.txt "GN   OrderedLocusNames=PP_1024"; file:PSEPK/eda/eda-uniprot.txt "DE            EC=4.1.2.14"].
- UniProt gives the catalytic reaction as cleavage of `2-dehydro-3-deoxy-6-phospho-D-gluconate` to `D-glyceraldehyde 3-phosphate + pyruvate`, which is the canonical KDPG aldolase reaction [file:PSEPK/eda/eda-uniprot.txt "Reaction=2-dehydro-3-deoxy-6-phospho-D-gluconate = D-glyceraldehyde 3-phosphate + pyruvate"].
- UniProt places the enzyme in `2-dehydro-3-deoxy-D-gluconate degradation` step `2/2`, consistent with the terminal carbon-splitting step of the Entner-Doudoroff route [file:PSEPK/eda/eda-uniprot.txt "PATHWAY: Carbohydrate acid metabolism; 2-dehydro-3-deoxy-D-gluconate degradation; D-glyceraldehyde 3-phosphate and pyruvate from 2-dehydro-3-deoxy-D-gluconate: step 2/2"].

## Family / structure

- The protein is a member of the `KHG/KDPG aldolase family` and is predicted to form a `homotrimer` [file:PSEPK/eda/eda-uniprot.txt "SUBUNIT: Homotrimer."; file:PSEPK/eda/eda-uniprot.txt "SIMILARITY: Belongs to the KHG/KDPG aldolase family."].
- GOA for `Q88P29` currently contains only two molecular function annotations: the specific aldolase term `GO:0008675` and the broad parent `GO:0016829 lyase activity` [file:PSEPK/eda/eda-goa.tsv "GO:0008675"; file:PSEPK/eda/eda-goa.tsv "GO:0016829"].

## Curation take

- `GO:0008675 2-dehydro-3-deoxy-phosphogluconate aldolase activity` should be retained as the core molecular function because it matches the named catalytic activity and reaction chemistry [file:PSEPK/eda/eda-uniprot.txt "RecName: Full=2-dehydro-3-deoxy-phosphogluconate aldolase"; file:PSEPK/eda/eda-uniprot.txt "Reaction=2-dehydro-3-deoxy-6-phospho-D-gluconate = D-glyceraldehyde 3-phosphate + pyruvate"].
- `GO:0016829 lyase activity` is accurate but too generic to represent the evolved core function on its own; it should be retained only as non-core [file:PSEPK/eda/eda-uniprot.txt "KW   Lyase"].
- A missing process-level annotation is involvement in the `Entner-Doudoroff pathway through 6-phosphogluconate (GO:0009255)`, supported by the explicit UniProt pathway statement [file:PSEPK/eda/eda-uniprot.txt "PATHWAY: Carbohydrate acid metabolism; 2-dehydro-3-deoxy-D-gluconate degradation; D-glyceraldehyde 3-phosphate and pyruvate from 2-dehydro-3-deoxy-D-gluconate: step 2/2"].

## Context

- The KT2440 genome paper is useful for strain/background provenance but does not itself establish `eda` biochemistry beyond the genome context [PMID:12534463 "Sequence analysis of the 6.18 Mb genome of strain KT2440 reveals diverse transport and metabolic systems."].
