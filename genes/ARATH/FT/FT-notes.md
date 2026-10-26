

## Autonomous flowering all-member review (2026-10-26)

Re-reviewed all 20 original rows and independently assessed the two inherited NEW molecular-function proposals. Real existing provider reports were used only to locate primary evidence. The old phosphatidylethanolamine-binding core quoted TFL1 antagonism and did not support its lipid claim. Direct primary PMID:24698997 reports no PE binding signal even at increased PE loading, specific PC binding, and liposome confirmation; PMID:31726375 provides structural modeling plus experimentally tested binding-site mutations. The original ISS PE row is therefore MODIFY to GO:0031210 phosphatidylcholine binding, preserving the original term/evidence/reference payload. The PC core uses those experiments. This is a ligand correction, not a new redundant lipid annotation; the PEBP family name is not experimental evidence of PE affinity.

The two inherited NEWs remain: PMID:16099979 establishes FT interaction with FD, and PMID:16099980 establishes AP1 activation by the FT-FD complex. GO:0140297 records specific partner recognition; GO:0003713 records the transcriptional coactivator effect. Live QuickGO ancestry checks show neither is an ancestor/descendant of the other. These are MF proposals, not process claims inferred from necessity or cargo transport. FT performs the coactivation step through its DNA-binding partner; it is not itself assigned DNA binding. No additional NEW row was created.

Full PMID:22529749 explicitly reports FT:RFP/FTIP1:GFP colocalization at ER connected to the nuclear envelope in transiently transformed N. benthamiana leaf epidermis. The ER term is retained KEEP_AS_NON_CORE with that assay boundary; the observation is not rejected merely because FT transcriptional action is nuclear. Cytoplasmic and nuclear locations remain supported. The source establishes FTIP1-mediated export, with FT as cargo/signal; neither FT transport activity nor a membrane-spanning FT topology is invented. The inherited proposed term for phloem protein transport was removed because FT is transported, and complex-assembly proposals were retired in favor of demonstrated coactivation and an explicit native-composition question.

Grafting/movement evidence comes from PMID:17446353, not the separately retracted FT-mRNA transport paper. Primary PMID:21737277 independently establishes the guard-cell stomatal function, which remains non-core. Meristem determinacy is supported by the genotype/tissue-expression/grafting comparisons in PMID:30943325 rather than inferred merely from flowering time.

Normal publication caching (`just fetch-gene-pmids ARATH FT`) completed. A targeted full-text refresh was interrupted by disk exhaustion before curated writes, then recovered serially after space was freed. Original source files were checked for intact metadata and abstracts; no cache text was edited manually. Existing real provider files were reused rather than fabricated or rewritten. Primary access levels below are those actually cached at final review.

### Per-row audit

Row numbers are zero-based and identify the unchanged original order.

| Row | Term | Original evidence/source | Final action | Primary or curated support |
| --- | --- | --- | --- | --- |
| 0 | GO:0005634 nucleus | IEA GO_REF:0000044 | ACCEPT | file:ARATH/FT/FT-uniprot.txt, PMID:22529749 |
| 1 | GO:0005737 cytoplasm | IEA GO_REF:0000044 | ACCEPT | file:ARATH/FT/FT-uniprot.txt |
| 2 | GO:0005783 endoplasmic reticulum | IEA GO_REF:0000044 | KEEP_AS_NON_CORE | PMID:22529749 |
| 3 | GO:0009908 flower development | IEA GO_REF:0000043 | MODIFY | PMID:16099979 |
| 4 | GO:0030154 cell differentiation | IEA GO_REF:0000043 | MODIFY | PMID:16099979 |
| 5 | GO:0005515 protein binding | IPI PMID:16099979 | REMOVE | PMID:16099979 |
| 6 | GO:0005515 protein binding | IPI PMID:17189287 | REMOVE | PMID:17189287 |
| 7 | GO:0005515 protein binding | IPI PMID:19656342 | REMOVE | PMID:19656342 |
| 8 | GO:0005515 protein binding | IPI PMID:29259105 | REMOVE | file:ARATH/FT/FT-uniprot.txt |
| 9 | GO:0010022 meristem determinacy | IGI PMID:30943325 | ACCEPT | PMID:30943325 |
| 10 | GO:0005515 protein binding | IPI PMID:22529749 | REMOVE | PMID:22529749 |
| 11 | GO:0010119 regulation of stomatal movement | IMP PMID:21737277 | KEEP_AS_NON_CORE | PMID:21737277 |
| 12 | GO:0009909 regulation of flower development | IGI PMID:20626659 | MODIFY | PMID:16099979 |
| 13 | GO:0005515 protein binding | IPI PMID:16099980 | REMOVE | PMID:16099980 |
| 14 | GO:0005634 nucleus | IDA PMID:16099979 | ACCEPT | file:ARATH/FT/FT-uniprot.txt, PMID:22529749 |
| 15 | GO:0005737 cytoplasm | IDA PMID:16099979 | ACCEPT | file:ARATH/FT/FT-uniprot.txt |
| 16 | GO:0048573 photoperiodism, flowering | IEP PMID:17446353 | ACCEPT | PMID:17446353 |
| 17 | GO:0008429 phosphatidylethanolamine binding | ISS PMID:10583961 | MODIFY | PMID:24698997, PMID:31726375 |
| 18 | GO:0009911 positive regulation of flower development | IMP PMID:10583960 | ACCEPT | PMID:10583960, PMID:16099979 |
| 19 | GO:0009911 positive regulation of flower development | IMP PMID:10583961 | ACCEPT | PMID:10583961, PMID:16099980 |
| 20 | GO:0140297 DNA-binding transcription factor binding | IPI PMID:16099979 | NEW | PMID:16099979, file:ARATH/FT/FT-uniprot.txt |
| 21 | GO:0003713 transcription coactivator activity | IPI PMID:16099980 | NEW | PMID:16099980, PMID:16099979 |

The original annotation payloads, including any NOT/contributes-to fields, were preserved. Existing annotations judged here are not cited as their own evidence. Provider-only warning suppression is not a reason to reintroduce provider prose as biological support.

### Final local primary-source access

| Source | Normal cache access |
| --- | --- |
| PMID:10583960 | Abstract only |
| PMID:10583961 | Abstract only |
| PMID:16099979 | Abstract only |
| PMID:16099980 | Abstract only |
| PMID:17189287 | Abstract only |
| PMID:17446353 | Abstract only |
| PMID:19656342 | Abstract only |
| PMID:20626659 | Abstract only |
| PMID:21737277 | Abstract only |
| PMID:22529749 | Full text |
| PMID:29259105 | Full text |
| PMID:30943325 | Abstract only |
| PMID:24698997 | Full text |
| PMID:31726375 | Full text |

All cited primary caches were inspected at the stated access level; source-specific limits remain explicit in the review.
