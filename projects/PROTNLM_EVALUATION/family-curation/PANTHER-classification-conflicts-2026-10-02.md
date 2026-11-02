---
autolink_gene_symbols: false
---

# PANTHER classification conflicts observed on 2026-10-02

Eight accession-specific assignments in the official PANTHER 19.0 sequence-classification files disagree with the frozen UniProt records used by these family reviews. All eight official rows agree with the saved upstream membership index and with the unchanged parser. This establishes a source conflict; it does not establish the correct evolutionary placement or a parser defect.

The diagnostic source run was [36943928592, attempt 1](https://github.com/ai4curation/ai-gene-review/actions/runs/36943928592), commit `86ffe004ffe04b167981c081a14c1c526fb24da2`. The five inputs were fetched once each on 2026-10-02 UTC, returned HTTP 200 without redirects, and were reported complete by the reviewed runtime. Source URLs use a mutable `current_release` location; the observed dates and recorded hashes below identify this observation.

## What changed and why

The reviews now encode five officially corroborated numbered subfamilies and retain the two horse placements with explicit frozen-source provenance. An exact horse-file NO_MATCH and the whale's unavailable named input are different observations, but neither is a positive contradictory assignment. NtR has a positive cross-parent conflict and remains outside structured membership while its channel-function question is restored as UNRESOLVED. Broad FOXN transcription-factor, CDK/CDKL phosphorylation and methyltransferase functions are inferred from the mechanisms and biological anchors; no member-count threshold is imposed. The systematic MAPKK source divergence and the LRR proteins' unresolved signaling mechanisms remain specific limits. All eight reviews remain IN_PROGRESS.

## Exact assignment comparison

Rows are one-based physical line numbers in each complete organism file; the assignment is column 4. Each target had exactly one whole-token `UniProtKB=` match in its organism file. The cached UniProt assignments are historical source observations, not replacements chosen by this assessment.

| Accession | Organism / row | Frozen UniProt assignment | Official sequence-file assignment | Parent conflict |
|---|---|---|---|---|
| P50613 | human / 4071 | PTHR24056:SF0 | PTHR24056:SF375 | No; subfamily only |
| Q7K5M0 | fruit_fly / 3669 | PTHR24250:SF27 | PTHR24260:SF145 | Yes |
| Q9W288 | fruit_fly / 1707 | PTHR36695:SF12 | PTHR18945:SF430 | Yes |
| Q9UTA9 | fission_yeast / 1845 | PTHR44942:SF4 | PTHR42912:SF95 | Yes |
| A0A8I6ALM9 | rat / 10310 | PTHR45080:SF21 | PTHR24418:SF399 | Yes |
| Q9XTP7 | fruit_fly / 8165 | PTHR46721:SF3 | PTHR13962:SF17 | Yes |
| P36507 | human / 16642 | PTHR47448:SF3 | PTHR48013:SF8 | Yes |
| F4JLB7 | arabidopsis / 15922 | PTHR48004:SF58 | PTHR48004:SF38 | No; subfamily only |

## Frozen source evidence and labels

- **P50613**: [frozen UniProt record](https://github.com/ai4curation/ai-gene-review/blob/e82261ba811dadbb944cd3770e7fdd2889ec69a4/genes/human/CDK7/CDK7-uniprot.txt); 02-SEP-2026, entry version 247. Old label: **CYCLIN-DEPENDENT KINASE 7**. Official sequence-file label: **CYCLIN-DEPENDENT KINASE 7**. Both identifiers resolve in the repository PANTHER ontology. Cached InterPro family metadata was fetched at `2026-06-02T09:17:01.488145` and does not declare a PANTHER release.
- **Q7K5M0**: [frozen UniProt record](https://github.com/ai4curation/ai-gene-review/blob/e82261ba811dadbb944cd3770e7fdd2889ec69a4/genes/DROME/scaf/scaf-uniprot.txt); 02-SEP-2026, entry version 156. Old label: **ELASTASE 2 LIKE**. Official sequence-file label: **FI17609P1-RELATED**. Both identifiers resolve in the repository PANTHER ontology. Cached InterPro family metadata was fetched at `2026-09-10T14:24:52.035828` and does not declare a PANTHER release.
- **Q9W288**: [frozen UniProt record](https://github.com/ai4curation/ai-gene-review/blob/e82261ba811dadbb944cd3770e7fdd2889ec69a4/genes/DROME/NtR/NtR-uniprot.txt); 02-SEP-2026, entry version 167. Old label: **AGAP008648-PA**. Official sequence-file label: **ACETYLCHOLINE RECEPTOR SUBUNIT ALPHA-LIKE 2-RELATED**. Both identifiers resolve in the repository PANTHER ontology. Cached InterPro family metadata was fetched at `2026-09-08T18:20:39.936769` and does not declare a PANTHER release.
- **Q9UTA9**: [frozen UniProt record](https://github.com/ai4curation/ai-gene-review/blob/e82261ba811dadbb944cd3770e7fdd2889ec69a4/genes/SCHPO/SPAC25B8.09/SPAC25B8.09-uniprot.txt); 02-SEP-2026, entry version 125. Old label: **METHYLTRANSFERASE TYPE 11 DOMAIN-CONTAINING PROTEIN**. Official sequence-file label: **METHYLTRANSFERASE TYPE 11 DOMAIN-CONTAINING PROTEIN**. Both identifiers resolve in the repository PANTHER ontology. Cached InterPro family metadata was fetched at `2026-09-10T14:23:07.490598` and does not declare a PANTHER release.
- **A0A8I6ALM9**: [frozen UniProt record](https://github.com/ai4curation/ai-gene-review/blob/e82261ba811dadbb944cd3770e7fdd2889ec69a4/genes/rat/Ptk7/Ptk7-uniprot.txt); 02-SEP-2026, entry version 22. Old label: **INACTIVE TYROSINE-PROTEIN KINASE 7**. Official sequence-file label: **MEGAKARYOCYTE-ASSOCIATED TYROSINE-PROTEIN KINASE**. Both identifiers resolve in the repository PANTHER ontology. Cached InterPro family metadata was fetched at `2026-08-18T17:37:28.556246` and does not declare a PANTHER release.
- **Q9XTP7**: [frozen UniProt record](https://github.com/ai4curation/ai-gene-review/blob/e82261ba811dadbb944cd3770e7fdd2889ec69a4/genes/DROME/jumu/jumu-uniprot.txt); 02-SEP-2026, entry version 216. Old label: **FORKHEAD BOX N1**. Official sequence-file label: **FORKHEAD BOX PROTEIN N4**. Both identifiers resolve in the repository PANTHER ontology. Cached InterPro family metadata was fetched at `2026-09-08T18:05:52.276117` and does not declare a PANTHER release.
- **P36507**: [frozen UniProt record](https://github.com/ai4curation/ai-gene-review/blob/e82261ba811dadbb944cd3770e7fdd2889ec69a4/genes/human/MAP2K2/MAP2K2-uniprot.txt); 02-SEP-2026, entry version 254. Old label: **MITOGEN-ACTIVATED PROTEIN KINASE KINASE 2**. Official sequence-file label: **DUAL SPECIFICITY MITOGEN-ACTIVATED PROTEIN KINASE KINASE 2**. Both identifiers resolve in the repository PANTHER ontology. Cached InterPro family metadata was fetched at `2026-09-08T11:07:39.910858` and does not declare a PANTHER release.
- **F4JLB7**: [frozen UniProt record](https://github.com/ai4curation/ai-gene-review/blob/e82261ba811dadbb944cd3770e7fdd2889ec69a4/genes/ARATH/F4JLB7/F4JLB7-uniprot.txt); 10-JUN-2026, entry version 92. Old label: **OS01G0162200 PROTEIN**. Official sequence-file label: **ROP-INTERACTIVE CRIB MOTIF-CONTAINING PROTEIN 7**. Both identifiers resolve in the repository PANTHER ontology. Cached InterPro family metadata was fetched at `2026-06-18T17:18:28.356454` and does not declare a PANTHER release.

## Official input observations

The following byte counts and SHA256 values were computed by the reviewed runner from each complete body. They have **not** been independently recomputed locally from the full raw artifact.

- [PTHR19.0_human](https://data.pantherdb.org/ftp/sequence_classifications/current_release/PANTHER_Sequence_Classification_files/PTHR19.0_human): observed `2026-10-02T00:17:00.558183+00:00`; HTTP Last-Modified `Thu, 20 Jun 2024 19:04:44 GMT`; 23680957 bytes; SHA256 `0635357eeae76cb6dce8ce498f20e7ad5e101fe5a81717003c97acb2ed009b32`.
- [PTHR19.0_fruit_fly](https://data.pantherdb.org/ftp/sequence_classifications/current_release/PANTHER_Sequence_Classification_files/PTHR19.0_fruit_fly): observed `2026-10-02T00:17:00.955509+00:00`; HTTP Last-Modified `Thu, 20 Jun 2024 19:04:42 GMT`; 10818190 bytes; SHA256 `10499c654f7d9dd8e7e2635605114c972d58df36ee3a5ef488e23333c773cd26`.
- [PTHR19.0_fission_yeast](https://data.pantherdb.org/ftp/sequence_classifications/current_release/PANTHER_Sequence_Classification_files/PTHR19.0_fission_yeast): observed `2026-10-02T00:17:01.773021+00:00`; HTTP Last-Modified `Thu, 20 Jun 2024 19:04:42 GMT`; 5113463 bytes; SHA256 `09d5fe2be1e169931419a5bf68213260e44d9ce8efe7fd90883ed47459ee1986`.
- [PTHR19.0_rat](https://data.pantherdb.org/ftp/sequence_classifications/current_release/PANTHER_Sequence_Classification_files/PTHR19.0_rat): observed `2026-10-02T00:17:02.137013+00:00`; HTTP Last-Modified `Thu, 20 Jun 2024 19:04:48 GMT`; 24863242 bytes; SHA256 `e2e04e284124bc5a669869ce2e4c1dd6629fc9079a0b9f0afef665b64cd3c8bf`.
- [PTHR19.0_arabidopsis](https://data.pantherdb.org/ftp/sequence_classifications/current_release/PANTHER_Sequence_Classification_files/PTHR19.0_arabidopsis): observed `2026-10-02T00:17:02.504668+00:00`; HTTP Last-Modified `Thu, 20 Jun 2024 19:04:37 GMT`; 16152084 bytes; SHA256 `309a44c6e1b8664b866ba97b5abe9fce2f9d25ecffc177cd300c0b8a3b9139fa`.

## Artifact and parser provenance

- Compact audit artifact: `11201891369`, 26,345 bytes, SHA256 `9861e63fc8279e570e57ad56d639c36edafeac62809ee9867681a27175707136`. Its exact nine JSON members and ZIP bytes were authenticated after [transport run 36947404317, attempt 1](https://github.com/ai4curation/ai-gene-review/actions/runs/36947404317), commit `fd4395f9616d18867c75d679e82575813b51648e`.
- Retained full raw artifact: `11201776799`, 12,703,276 bytes, GitHub-reported SHA256 `1a952c2fd9f73774c5d578abb02b61144392b7844c8118ee86fc56b85409ffdd`. Its upload binding was checked against the source run metadata. Its ZIP or full source bodies were not downloaded in this compact inspection.
- Parser: `src/ai_gene_review/etl/panther_families.py`, SHA256 `ad4162a45d021da97433b3d3b98e858ea97d16265dedc1c0e61598d89b7cc10a`. The reviewed parser reads column 4; local replay on the eight extracted rows reproduced every runner result.
- Saved tested upstream index: Git blob `10b3f4f14c3326e8fc2d298255e0238785bb28d9`, SHA256 `280574a7675e13e1f7ebd8eebfb8d6088ebac0178fd4b66c98b24460d4135d8b`. The local workspace index was older and retained the UniProt-derived assignments; it was separately compared, not called the current upstream index.
- The upstream index introduction was commit `7a995278183338fcd461234f89ffd74bd7378753` ([PR #3821](https://github.com/ai4curation/ai-gene-review/pull/3821)). Its original complete input bodies were not recovered. These observations reproduce its eight assignments, not a byte-identical historical generation run.

## Release and biological interpretation

The parser constant, generated `panther.obo` header, and official sequence-file names all declare **19.0**. The sequence responses were last modified on 2024-06-20. Later UniProt entry dates and PAINT assertion dates do not establish a different PANTHER release. The InterPro fetch metadata does not name a release; the exact HMM input bytes used to generate the ontology were not recovered. Different HMM-scoring and tree-placement methods remain a possible explanation, not a demonstrated cause for these eight cases.

Human CDK7 and F4JLB7 retain unnumbered functional groups because both classification observations support their respective parents; no numbered subfamily is selected. CDK7 P50613 has cached PAINT seed evidence, including PTN000624096, but no checked SF0/SF375-to-PTN bridge. Horse CDK7 A0A9L0R074 retains a source-bounded PTHR24056:SF0 descriptor from its frozen UniProt record and both saved indexes; the official-file NO_MATCH is not a contradictory placement. The human-horse sequence comparison does not resolve the human subfamily number. F4JLB7 has no seed in the cached family PAINT table; its frozen record combines the name RIC7 with a 450-residue LRR sequence (sequence version 1 since 2011). A different subfamily label does not establish a CRIB-effector mechanism or sequence drift.

For the six positive parent-family conflicts, the original identifier, label, protein identity and biological interpretation remain in comparative notes outside asserted membership. Existing gene-level experimental conclusions are not reversed: rat PTK7 pseudokinase evidence is not replaced by a kinase claim from the alternate label. FOXN DNA-binding transcription-factor activity is inferred from the conserved mechanism and independently corroborated FOXN1/FOXN4 representatives, not from the disputed Jumu placement. The systematic MAPKK source divergence leaves the numbered-family boundary unresolved even though the compared proteins retain positive MAPKK biology.

The family reviews remain **IN_PROGRESS**. This treatment withdraws disputed classification assertions while preserving the evidence; it does not assign replacement families, change PAINT nodes, or declare the source discrepancy solved.

## Functional evidence and coverage limits

A family-wide function is an inference from a conserved mechanism and appropriate biological anchors; it does not require enumerating every member. Cached reviewed-entry counts and metadata protein totals describe retrieval coverage, not an automatic reason to withhold that inference. FOXN1/FOXN4 domain and transcription-factor evidence, including independently corroborated in-family representatives, supports COHERENT and FAMILY_WIDE GO:0003700. Different developmental programs do not establish loss of DNA-binding transcription-factor activity. PTHR47448 instead remains UNKNOWN with GO:0004708 UNRESOLVED because its cached MAPKK inventory and all six independently inspected characterized MAPKK rows systematically use different parent families. That is a family-boundary problem, not a count threshold, a negative MAPKK claim or evidence that different pathway partners abolish catalysis.

Rat PTK7 A0A8I6ALM9 supplies a stronger functional asymmetry than an unexplained label disagreement. Its seven-Ig-domain receptor architecture and conservation of human PTK7 occluded-pocket landmarks support pseudokinase biology and make an active MATK-like interpretation implausible. Rat ATP binding or structure was not directly measured in the alignment analysis. This biological evidence does not identify a replacement evolutionary parent or establish that a surprising family label alone is erroneous.

The rat and mouse PRSS54 representatives form one inactive orthologous group at PTHR24250:SF45, not independent losses of catalysis; human PRSS54 remains a cross-parent comparison. PTHR36695 retains GO:0005230 as an investigated UNRESOLVED question with its prior source excerpts. NtR channel architecture and uncertain ligand/selectivity remain comparative evidence. NtR is not reintroduced as an unnumbered representative because its actual official row positively conflicts with the asserted parent; a validator that skips unnumbered membership does not make that parent assertion defensible.

## Retained comparator classification boundary

The second bounded audit inspected 17 exact accessions in nine complete official PANTHER 19.0 organism files. Fifteen had one whole-token match each; their column-4 assignments agree with the unchanged runner parser and local replay. Horse CDK7 A0A9L0R074 and MAP2K2 A0A9L0SHX8 had no exact match in the complete horse file. This supplies neither independent corroboration nor a contradictory assignment. Both horses retain explicitly source-bounded numbered descriptors from their frozen UniProt records and both saved indexes, with the complete biological comparisons and unresolved release/mapping discrepancy documented. No replacement accession is inferred.

The directory has no whale-named sequence-classification file. Blue-whale A0A8B8WEG2 therefore retains its explicitly sourced frozen placement without an independently inspected additional official row. This unavailability is not a search of every organism file or evidence of global accession absence.

The table reports the source row’s own column-5 family and column-6 subfamily labels verbatim; it does not derive them from the cached ontology or treat them as independent functional experiments.

| Accession / gene | Organism / physical row | Column 4 assignment | Column 5 family label | Column 6 subfamily label |
|---|---|---|---|---|
| Q13308 / PTK7 | human / 1097 | PTHR45080:SF21 | CONTACTIN 5 | INACTIVE TYROSINE-PROTEIN KINASE 7 |
| Q6PEW0 / PRSS54 | human / 17811 | PTHR24256:SF545 | TRYPTASE-RELATED | INACTIVE SERINE PROTEASE 54 |
| O15353 / FOXN1 | human / 10325 | PTHR46721:SF1 | FORKHEAD BOX PROTEIN N1 | FORKHEAD BOX PROTEIN N1 |
| Q02750 / MAP2K1 | human / 819 | PTHR48013:SF5 | DUAL SPECIFICITY MITOGEN-ACTIVATED PROTEIN KINASE KINASE 5-RELATED | DUAL SPECIFICITY MITOGEN-ACTIVATED PROTEIN KINASE KINASE 1 |
| Q6AY28 / Prss54 | rat / 11924 | PTHR24250:SF45 | CHYMOTRYPSIN-RELATED | INACTIVE SERINE PROTEASE 54 |
| Q7M756 / Prss54 | mouse / 6727 | PTHR24250:SF45 | CHYMOTRYPSIN-RELATED | INACTIVE SERINE PROTEASE 54 |
| Q61575 / Foxn1 | mouse / 13834 | PTHR46721:SF1 | FORKHEAD BOX PROTEIN N1 | FORKHEAD BOX PROTEIN N1 |
| Q8K3Q3 / Foxn4 | mouse / 13348 | PTHR13962:SF17 | FORKHEAD BOX PROTEIN N3-LIKE PROTEIN-RELATED | FORKHEAD BOX PROTEIN N4 |
| P31938 / Map2k1 | mouse / 11043 | PTHR48013:SF5 | DUAL SPECIFICITY MITOGEN-ACTIVATED PROTEIN KINASE KINASE 5-RELATED | DUAL SPECIFICITY MITOGEN-ACTIVATED PROTEIN KINASE KINASE 1 |
| P32643 / TMT1 | budding_yeast / 855 | PTHR44942:SF4 | METHYLTRANSF_11 DOMAIN-CONTAINING PROTEIN | METHYLTRANSFERASE TYPE 11 DOMAIN-CONTAINING PROTEIN |
| Q7RYZ6 / mek-1 | neurospora / 658 | PTHR48013:SF6 | DUAL SPECIFICITY MITOGEN-ACTIVATED PROTEIN KINASE KINASE 5-RELATED | MAP KINASE KINASE MKK1_SSP32-RELATED |
| A0A9L0SHX8 | horse / no match | NO_MATCH | — | — |
| A0A9L0R074 | horse / no match | NO_MATCH | — | — |
| P10506 / byr1 | fission_yeast / 2450 | PTHR48013:SF9 | DUAL SPECIFICITY MITOGEN-ACTIVATED PROTEIN KINASE KINASE 5-RELATED | DUAL SPECIFICITY MITOGEN-ACTIVATED PROTEIN KINASE KINASE 5 |
| Q9Y884 / pek1 | fission_yeast / 224 | PTHR48013:SF6 | DUAL SPECIFICITY MITOGEN-ACTIVATED PROTEIN KINASE KINASE 5-RELATED | MAP KINASE KINASE MKK1_SSP32-RELATED |
| A2BGM5 / foxn4 | zebrafish / 14235 | PTHR13962:SF17 | FORKHEAD BOX PROTEIN N3-LIKE PROTEIN-RELATED | FORKHEAD BOX PROTEIN N4 |
| Q3BJS1 / foxn4 | x_laevis / 16025 | PTHR46721:SF2 | FORKHEAD BOX PROTEIN N1 | FORKHEAD BOX PROTEIN N4 |

Five corroborated numbered subfamilies are now represented in the structured reviews: human PTK7 at PTHR45080:SF21; human/mouse FOXN1 at PTHR46721:SF1; Xenopus Foxn4 at PTHR46721:SF2; rat/mouse Prss54 at PTHR24250:SF45; and budding-yeast Tmt1 at PTHR44942:SF4. Their labels are the official names, checked against the ontology. Human PRSS54, mouse/zebrafish Foxn4 and the other positive cross-parent conflicts remain comparative evidence. Classification corroboration and biological mechanism remain separate lines of support.

The MAPKK discrepancy is systematic across the inspected characterized comparators: human MAP2K2 and MAP2K1, mouse Map2k1, Neurospora mek-1 and fission-yeast byr1/pek1 all have official PTHR48013 rows, whereas the cached reviewed-protein inventory consistently uses PTHR47448. Those six positively conflicting targets are not asserted as PTHR47448 members. Horse MAP2K2 retains its historical-source SF3 descriptor because NO_MATCH is not a positive conflict, but cannot independently reconcile the two family boundaries. This predicts a broader mixed-provenance issue worth investigating; it does not prove that every unexamined row follows the split or justify mechanically repointing a family.

### Comparator source and artifact provenance

The source run was [36956025748, attempt 1](https://github.com/ai4curation/ai-gene-review/actions/runs/36956025748), commit `f2af8cb01e88988204fad252eabc1daf375165b9`. All nine primary requests used the explicit `/19.0/` directory, made one attempt, returned HTTP 200 without redirects, and were reported complete. The human, rat and fission-yeast recorded body hashes equal those reported for audit 1, despite its different URL prefix. This is agreement between authenticated runner records, not an independent local full-body hash calculation.

- [PTHR19.0_human](https://data.pantherdb.org/ftp/sequence_classifications/19.0/PANTHER_Sequence_Classification_files/PTHR19.0_human): observed `2026-10-02T02:33:00.775615+00:00`; HTTP Last-Modified `Thu, 20 Jun 2024 19:04:44 GMT`; 23680957 bytes; runner-recorded SHA256 `0635357eeae76cb6dce8ce498f20e7ad5e101fe5a81717003c97acb2ed009b32`.
- [PTHR19.0_rat](https://data.pantherdb.org/ftp/sequence_classifications/19.0/PANTHER_Sequence_Classification_files/PTHR19.0_rat): observed `2026-10-02T02:33:01.312814+00:00`; HTTP Last-Modified `Thu, 20 Jun 2024 19:04:48 GMT`; 24863242 bytes; runner-recorded SHA256 `e2e04e284124bc5a669869ce2e4c1dd6629fc9079a0b9f0afef665b64cd3c8bf`.
- [PTHR19.0_mouse](https://data.pantherdb.org/ftp/sequence_classifications/19.0/PANTHER_Sequence_Classification_files/PTHR19.0_mouse): observed `2026-10-02T02:33:01.693308+00:00`; HTTP Last-Modified `Thu, 20 Jun 2024 19:04:45 GMT`; 24577495 bytes; runner-recorded SHA256 `c5bce735c86e8b672e19380740b0d6392aa2416eeffea1e878c8ecedef4c0de2`.
- [PTHR19.0_budding_yeast](https://data.pantherdb.org/ftp/sequence_classifications/19.0/PANTHER_Sequence_Classification_files/PTHR19.0_budding_yeast): observed `2026-10-02T02:33:02.093298+00:00`; HTTP Last-Modified `Thu, 20 Jun 2024 19:04:38 GMT`; 5567875 bytes; runner-recorded SHA256 `3a0afdfecc3db36656921905d3f58cf81d00eba12b32f16069594c1cb061ecdd`.
- [PTHR19.0_neurospora](https://data.pantherdb.org/ftp/sequence_classifications/19.0/PANTHER_Sequence_Classification_files/PTHR19.0_neurospora): observed `2026-10-02T02:33:02.443969+00:00`; HTTP Last-Modified `Thu, 20 Jun 2024 19:04:46 GMT`; 6364727 bytes; runner-recorded SHA256 `d1ac2a94dc068f835cf759502fbc3ed0537cc612927f62d544fa5adb37856994`.
- [PTHR19.0_horse](https://data.pantherdb.org/ftp/sequence_classifications/19.0/PANTHER_Sequence_Classification_files/PTHR19.0_horse): observed `2026-10-02T02:33:02.711751+00:00`; HTTP Last-Modified `Thu, 20 Jun 2024 19:04:44 GMT`; 23187565 bytes; runner-recorded SHA256 `6c9e1734cc8517f64799dc799d7b04bca27fb7de948005f52329c270aa6c4b73`.
- [PTHR19.0_fission_yeast](https://data.pantherdb.org/ftp/sequence_classifications/19.0/PANTHER_Sequence_Classification_files/PTHR19.0_fission_yeast): observed `2026-10-02T02:33:03.181241+00:00`; HTTP Last-Modified `Thu, 20 Jun 2024 19:04:42 GMT`; 5113463 bytes; runner-recorded SHA256 `09d5fe2be1e169931419a5bf68213260e44d9ce8efe7fd90883ed47459ee1986`.
- [PTHR19.0_zebrafish](https://data.pantherdb.org/ftp/sequence_classifications/19.0/PANTHER_Sequence_Classification_files/PTHR19.0_zebrafish): observed `2026-10-02T02:33:03.541775+00:00`; HTTP Last-Modified `Thu, 20 Jun 2024 19:04:52 GMT`; 29261042 bytes; runner-recorded SHA256 `52b46e3f3f0433765076b402058b8a483a1e81f39a2062a772428e6951b2c080`.
- [PTHR19.0_x_laevis](https://data.pantherdb.org/ftp/sequence_classifications/19.0/PANTHER_Sequence_Classification_files/PTHR19.0_x_laevis): observed `2026-10-02T02:33:04.001059+00:00`; HTTP Last-Modified `Thu, 20 Jun 2024 19:04:52 GMT`; 38935436 bytes; runner-recorded SHA256 `66f95fd45d793b63708ffb606d84a7abe81d7dd955474aace7d8fa6e4bc47c72`.

- Compact artifact `11205408249`: 42,630 bytes, SHA256 `7df7b0367d5d10dc5be4c919adc9af3a89ea3e057ba788fc4b067eaa0d926931`; exactly 13 JSON members. Authenticated through [transport run 36959870242, attempt 1](https://github.com/ai4curation/ai-gene-review/actions/runs/36959870242), commit `03bcb0dd29f4df50bac3b6f208feb9c3b2397a01`.
- Full raw artifact `11205483252`: 28,015,349 bytes, GitHub-reported SHA256 `02dd57b19df880678e39c1474ce97defedee674da331e6cbe4b31c5a57de528e`. Its upload binding was checked; its ZIP and complete source bodies were not downloaded in this compact inspection.
- The unchanged parser is the same SHA256 `ad4162a45d021da97433b3d3b98e858ea97d16265dedc1c0e61598d89b7cc10a` used in audit 1. All 15 extracted matches were replayed locally. The two whole-file NO_MATCH outcomes are authenticated results of the reviewed bounded runner, not independent local scans of the complete raw horse file.
The flat membership index combines official sequence-file and fallback UniProt classifications without a per-row provenance column. A passing validator does not prove that an unnumbered group's parent membership was checked. Positive cross-parent conflicts remain outside structured membership. Human CDK7 and F4JLB7 retain unnumbered groups supported by both parent observations; the two horses retain numbered historical-source descriptors with explicit official NO_MATCH bounds, just as the whale retains its frozen-source descriptor with a distinct missing-input limitation. No validator, index schema or source classification is changed here.

The family notes now use compact source-observation tables and current comparative biological prose. Links to the exact prior revision preserve the complete earlier representation; original source files, residue/sequence findings, references and append-only history remain unchanged.

PTHR24056 is coherent for broad protein phosphorylation across the CDK/CDKL kinase mechanism; its cyclin-dependent qualifier remains unresolved specifically because the current sources do not establish cyclin dependence for the named CDKL branches. CDK5 p35/p39 regulation is not a negative GO:0004693 claim. PTHR44942 supports broad methyltransferase activity through the family classification and direct in-family Tmt1 chemistry; acceptor specificity and physiological pathways are not generalized, and generated InterPro prose is not independent experimental evidence. PTHR48004 remains UNKNOWN because LRR recognition architecture does not establish a shared ligand, intrinsic catalytic reaction or partner-dependent phosphorylation mechanism. These are case-specific biological judgments, independent of metadata counts.

The official rat row 10310 itself records PTHR24418:SF399, the family label TYROSINE-PROTEIN KINASE, the subfamily label MEGAKARYOCYTE-ASSOCIATED TYROSINE-PROTEIN KINASE and the protein-class field non-receptor tyrosine protein kinase. The MATK-like functional discrepancy therefore cannot be explained solely by pairing the identifier with the cached OBO label. Its classification cause remains unresolved.

## Verification limits

The compact archive preserves extracted rows, controls, and runner-recorded full-body digests. It proves the authenticated compact bytes and supports local replay of those rows. It does not independently prove the full raw-body hashes or the original PR input bytes. GitHub artifacts may expire; this report retains the finite observed facts and their provenance without requiring the remote artifacts to remain available.
