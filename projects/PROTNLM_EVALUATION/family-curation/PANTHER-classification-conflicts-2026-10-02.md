# PANTHER classification conflicts observed on 2026-10-02

Eight accession-specific assignments in the official PANTHER 19.0 sequence-classification files disagree with the frozen UniProt records used by these family reviews. All eight official rows agree with the saved upstream membership index and with the unchanged parser. This establishes a source conflict; it does not establish the correct evolutionary placement or a parser defect.

The diagnostic source run was [36943928592, attempt 1](https://github.com/ai4curation/ai-gene-review/actions/runs/36943928592), commit `86ffe004ffe04b167981c081a14c1c526fb24da2`. The five inputs were fetched once each on 2026-10-02 UTC, returned HTTP 200 without redirects, and were reported complete by the reviewed runtime. Source URLs use a mutable `current_release` location; the observed dates and recorded hashes below identify this observation.

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

- **P50613**: [frozen UniProt record](../../../genes/human/CDK7/CDK7-uniprot.txt); 02-SEP-2026, entry version 247. Old label: **CYCLIN-DEPENDENT KINASE 7**. Official sequence-file label: **CYCLIN-DEPENDENT KINASE 7**. Both identifiers resolve in the repository PANTHER ontology. Cached InterPro family metadata was fetched at `2026-06-02T09:17:01.488145` and does not declare a PANTHER release.
- **Q7K5M0**: [frozen UniProt record](../../../genes/DROME/scaf/scaf-uniprot.txt); 02-SEP-2026, entry version 156. Old label: **ELASTASE 2 LIKE**. Official sequence-file label: **FI17609P1-RELATED**. Both identifiers resolve in the repository PANTHER ontology. Cached InterPro family metadata was fetched at `2026-09-10T14:24:52.035828` and does not declare a PANTHER release.
- **Q9W288**: [frozen UniProt record](../../../genes/DROME/NtR/NtR-uniprot.txt); 02-SEP-2026, entry version 167. Old label: **AGAP008648-PA**. Official sequence-file label: **ACETYLCHOLINE RECEPTOR SUBUNIT ALPHA-LIKE 2-RELATED**. Both identifiers resolve in the repository PANTHER ontology. Cached InterPro family metadata was fetched at `2026-09-08T18:20:39.936769` and does not declare a PANTHER release.
- **Q9UTA9**: [frozen UniProt record](../../../genes/SCHPO/SPAC25B8.09/SPAC25B8.09-uniprot.txt); 02-SEP-2026, entry version 125. Old label: **METHYLTRANSFERASE TYPE 11 DOMAIN-CONTAINING PROTEIN**. Official sequence-file label: **METHYLTRANSFERASE TYPE 11 DOMAIN-CONTAINING PROTEIN**. Both identifiers resolve in the repository PANTHER ontology. Cached InterPro family metadata was fetched at `2026-09-10T14:23:07.490598` and does not declare a PANTHER release.
- **A0A8I6ALM9**: [frozen UniProt record](../../../genes/rat/Ptk7/Ptk7-uniprot.txt); 02-SEP-2026, entry version 22. Old label: **INACTIVE TYROSINE-PROTEIN KINASE 7**. Official sequence-file label: **MEGAKARYOCYTE-ASSOCIATED TYROSINE-PROTEIN KINASE**. Both identifiers resolve in the repository PANTHER ontology. Cached InterPro family metadata was fetched at `2026-08-18T17:37:28.556246` and does not declare a PANTHER release.
- **Q9XTP7**: [frozen UniProt record](../../../genes/DROME/jumu/jumu-uniprot.txt); 02-SEP-2026, entry version 216. Old label: **FORKHEAD BOX N1**. Official sequence-file label: **FORKHEAD BOX PROTEIN N4**. Both identifiers resolve in the repository PANTHER ontology. Cached InterPro family metadata was fetched at `2026-09-08T18:05:52.276117` and does not declare a PANTHER release.
- **P36507**: [frozen UniProt record](../../../genes/human/MAP2K2/MAP2K2-uniprot.txt); 02-SEP-2026, entry version 254. Old label: **MITOGEN-ACTIVATED PROTEIN KINASE KINASE 2**. Official sequence-file label: **DUAL SPECIFICITY MITOGEN-ACTIVATED PROTEIN KINASE KINASE 2**. Both identifiers resolve in the repository PANTHER ontology. Cached InterPro family metadata was fetched at `2026-09-08T11:07:39.910858` and does not declare a PANTHER release.
- **F4JLB7**: [frozen UniProt record](../../../genes/ARATH/F4JLB7/F4JLB7-uniprot.txt); 10-JUN-2026, entry version 92. Old label: **OS01G0162200 PROTEIN**. Official sequence-file label: **ROP-INTERACTIVE CRIB MOTIF-CONTAINING PROTEIN 7**. Both identifiers resolve in the repository PANTHER ontology. Cached InterPro family metadata was fetched at `2026-06-18T17:18:28.356454` and does not declare a PANTHER release.

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

The two same-parent cases retain biological comparison groups without numbered subfamily assertions. CDK7 P50613 has cached PAINT seed evidence, including PTN000624096, but no checked SF0/SF375-to-PTN bridge. Horse CDK7 A0A9L0R074 remains in PTHR24056 in its frozen UniProt record and both saved indexes. F4JLB7 has no seed in the cached family PAINT table; its frozen record combines the name RIC7 with a 450-residue LRR sequence (sequence version 1 since 2011). A different subfamily label does not establish a CRIB-effector mechanism or sequence drift.

For the six parent-family conflicts, the original identifier, label, protein identity, and complete biological interpretation are retained in unresolved curator notes outside asserted membership. Remaining independently supported representatives are retained. Existing gene-level experimental conclusions are not reversed: in particular, the rat PTK7 pseudokinase evidence is not replaced by a kinase claim based on the alternate family label. Jumu and human MAP2K2 experiments do not resolve the complete parent-family boundary, so the former universal activity grants are left unresolved.

The family reviews remain **IN_PROGRESS**. This treatment withdraws disputed classification assertions while preserving the evidence; it does not assign replacement families, change PAINT nodes, or declare the source discrepancy solved.

## Verification limits

The compact archive preserves extracted rows, controls, and runner-recorded full-body digests. It proves the authenticated compact bytes and supports local replay of those rows. It does not independently prove the full raw-body hashes or the original PR input bytes. GitHub artifacts may expire; this report retains the finite observed facts and their provenance without requiring the remote artifacts to remain available.
