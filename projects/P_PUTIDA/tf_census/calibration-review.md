# KT2440 TF calibration evidence review

Date: 2026-11-05. All 20 selected accessions received a scoped evidence assessment. That pass did not change gene-review YAML. The machine-readable assessments, citations, access limitations and follow-ups are in [calibration-assessments.yaml](calibration-assessments.yaml).

Follow-up, 2026-11-08: the [first full-review batch](../batches/tf_carbon_utilization_01.md) covers BenR, HexR, PtxS and CbrB, with supported regulatory relationships and explicit pathway context. The other 16 cases retain their scoped-assessment status; they have not received full GO re-review in this workstream. Per-case `full_go_review` fields distinguish that subsequent work from the original assessment.

## What this pass resolves

- CbrB/AlgB and GacA/uvrY joins are supported by locus-specific primary literature. CbrB promoter experiments include KT2442, so derivative-strain provenance must remain explicit.
- PP_3765 is TurB in KT2440 literature; MvaT is family-oriented source wording.
- PP_3832 is the post-transcriptional regulator RsmE. It is distinct from the methyltransferase named rsmE at PP_4985. The rsmA/KsgA control at PP_0401 is likewise distinct from regulatory RsmA at PP_4472.
- The three unnamed TetR/LysR candidates remain inferred candidates with unknown targets, signs and ligands. PvdS remains an architecture-supported sigma-factor case with target-specific experimental support unverified in this pass.
- XylR P06519 stays outside the native KT2440 reference census.

These identity findings draw on [KT2440 CbrB/GacA locus evidence](https://pmc.ncbi.nlm.nih.gov/articles/PMC7580535/), [TurB nomenclature](https://doi.org/10.1186/s12866-017-1091-6), and [Rsm protein nomenclature](https://doi.org/10.1128/AEM.01724-16).

## Calibration outcomes

| Case | Accession | Assessed role | Evidence status |
|---|---|---|---|
| BenR | Q88I42 | DNA-binding transcriptional activator | SUPPORTED |
| cbrB | Q88DX2 | Transcriptional response regulator | SUPPORTED |
| gacA | Q88FJ6 | Transcriptional response regulator | SUPPORTED |
| fleQ | Q88ET0 | DNA-binding AAA+ transcriptional regulator | SUPPORTED |
| ada | Q88PZ2 | Multifunctional DNA-repair enzyme and transcriptional activator | SUPPORTED |
| hexR | Q88P32 | DNA-binding transcriptional repressor | SUPPORTED |
| ptxS | Q88HH7 | DNA-binding transcriptional repressor | SUPPORTED |
| lexA2 | P59479 | DNA-binding transcriptional repressor | SUPPORTED |
| PP_2597 | Q88JQ2 | DNA-binding TF-family candidate | INFERRED |
| PP_4754 | Q88DR9 | DNA-binding TF-family candidate | INFERRED |
| PP_4660 | Q88E08 | DNA-binding TF-family candidate | INFERRED |
| rpoS | Q88ME8 | Sigma factor | SUPPORTED |
| pvdS | Q88F55 | Alternative ECF sigma-factor candidate | INFERRED |
| hfq | Q88DD3 | Post-transcriptional RNA regulator | SUPPORTED |
| csrA | Q88G93 | Post-transcriptional CsrA/Rsm regulator | SUPPORTED |
| cheY | Q88EW2 | Non-transcriptional chemotaxis response regulator | INFERRED |
| flgM | Q88EQ8 | Anti-sigma accessory regulator | SUPPORTED |
| MvaT | Q88GF9 | Nucleoid-associated H-NS-family regulator | SUPPORTED |
| rsmA | Q88QT6 | rRNA methyltransferase negative control | INFERRED |
| xylR | P06519 | Plasmid-borne DNA-binding transcriptional activator | SUPPORTED_OUT_OF_SCOPE |

## Evidence boundaries and follow-ups

BenR has promoter-response evidence, but this pass did not verify its description’s specific direct benzoate-binding claim. GacA has system-level expression evidence; direct DNA edges remain unresolved. HexR’s SIS effector-site assignment should retain the qualification in the primary abstract. FleQ and PtxS have explicit ligand-binding assays described in their primary abstracts. Ada preserves both repair and regulatory roles, while covalent modification must not be represented as ordinary ligand binding.

The BenR literature includes KT2442 experiments; earlier BenR studies require their own strain checks and must not silently become KT2440 experiments. The older BenR iModulon report also needs a catA-II versus catA-I check before treating every cat-gene association as indirect. The exact promoter/operon boundaries remain a follow-up.

Sigma factors, Hfq/RsmE, CheY, FlgM and TurB retain their separate roles. RNA binding, anti-sigma action and motor signaling do not become sequence-specific DNA regulation because downstream transcription changes. The [2026 sigma-factor study](https://doi.org/10.1186/s13036-026-00769-z) is an update lead; its target tables were not extracted here.

Missing full text is stated per case. Abstract-only evidence was used only for claims explicitly reported there, and never to declare an experimental annotation wrong. Primary studies were consulted where accessible; no complete systematic literature search, sequence verification, gene validator run or genome-coordinate transfer was performed.

## Importer assessment

The [repaired importer results](imodulon/calibration-results.md) cover all 20 accessions. All 84 published modules passed independent checks against named matrix columns, measured weights and source-specific thresholds. FleQ retains both assigned modules; gene membership is reported separately from regulator assignment. BenR has 10 published members, correcting the historical 13-gene cutoff list. No module membership, ICA weight, overlap score or regulator label was used to manufacture direct targets, regulatory signs or effectors.

## Next GO-review actions

Use the per-case follow-up lists for subsequent annotation reviews. Add primary references where existing reviews depend only on provider notes; preserve KT2442 and plasmid context; verify target-specific binding before claiming direct regulation; keep unknowns explicit for the unnamed family candidates. Full review validation and any GO changes are separate work.
