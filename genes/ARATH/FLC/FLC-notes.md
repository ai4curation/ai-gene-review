

## Autonomous flowering all-member review (2026-10-26)

Re-reviewed all 30 original rows against primary evidence. Existing genuine Falcon/Perplexity reports were used as literature leads only; they are not independent evidence. The biological description and core now distinguish FLC protein activity from epigenetic regulation of its locus. Primary PMID:16623882 places FLC on the FT **first intron** and SOC1 promoter, and detects a multimeric complex with multiple FLC polypeptides; PMID:16600915 resolves leaf signaling versus meristem competence. Neither source justifies describing both binding sites as promoters or assigning FLC all activities of the machinery silencing the FLC locus.

A key correction is the positive-transcription row. PMID:21464308 states: "Five genes showed decreased expression in the mutant, indicating that FLC binding can result in either transcriptional repression or activation." The full PMC article was inspected online and identifies SMZ/TOE3 among these targets; its normally retrieved local cache is currently abstract-only, and the force retrieval retry returned HTTP429. The quote in the review comes from the intact cached abstract, not a fabricated full-text extract. The result directly defeats the previous assumption that a floral repressor must exclusively repress transcription. The inhibitory FT/SOC1 mechanism remains supported.

Protein binding was evaluated by partner and experiment: FLC-SVP MADS association is refined; the multiplex screen and FLZ13/regulatory interactions remain recorded without inferring a new activity from mere binding. Thermal clock effects are retained as non-core, while vernalization response remains a legitimate response claim. The generic differentiation mapping is refined to the experimentally supported inhibitory flowering role rather than removed just for breadth. Unsupported proposed terms for MADS assembly and silencing of the FLC locus were retired: existing activity terms cover the former, and being the locus silenced does not make the FLC protein the silencing enzyme. No annotation rows were added or removed.

Normal publication caching (`just fetch-gene-pmids ARATH FLC`) completed. A targeted full-text refresh was interrupted by disk exhaustion before curated writes, then recovered serially after space was freed. Original source files were checked for intact metadata and abstracts; no cache text was edited manually. Existing real provider files were reused rather than fabricated or rewritten. Primary access levels below are those actually cached at final review.

### Per-row audit

Row numbers are zero-based and identify the unchanged original order.

| Row | Term | Original evidence/source | Final action | Primary or curated support |
| --- | --- | --- | --- | --- |
| 0 | GO:0006357 regulation of transcription by RNA polymerase II | IBA GO_REF:0000033 | ACCEPT | PMID:16623882, PMID:16600915 |
| 1 | GO:0009910 negative regulation of flower development | IBA GO_REF:0000033 | ACCEPT | PMID:16600915 |
| 2 | GO:0000978 RNA polymerase II cis-regulatory region sequence-specific DNA binding | IBA GO_REF:0000033 | ACCEPT | PMID:16623882, PMID:16600915 |
| 3 | GO:0000981 DNA-binding transcription factor activity, RNA polymerase II-specific | IBA GO_REF:0000033 | ACCEPT | PMID:16623882, PMID:16600915 |
| 4 | GO:0000977 RNA polymerase II transcription regulatory region sequence-specific DNA binding | IEA GO_REF:0000002 | ACCEPT | PMID:16623882, PMID:16600915 |
| 5 | GO:0003677 DNA binding | IEA GO_REF:0000120 | MODIFY | PMID:16623882, PMID:16600915 |
| 6 | GO:0003700 DNA-binding transcription factor activity | IEA GO_REF:0000002 | MODIFY | PMID:16623882, PMID:16600915 |
| 7 | GO:0005634 nucleus | IEA GO_REF:0000120 | ACCEPT | PMID:16623882, file:ARATH/FLC/FLC-uniprot.txt |
| 8 | GO:0006355 regulation of DNA-templated transcription | IEA GO_REF:0000002 | MODIFY | PMID:16623882, PMID:16600915 |
| 9 | GO:0009908 flower development | IEA GO_REF:0000043 | MODIFY | PMID:16623882, PMID:16600915 |
| 10 | GO:0009909 regulation of flower development | IEA GO_REF:0000117 | MODIFY | PMID:16623882, PMID:16600915 |
| 11 | GO:0030154 cell differentiation | IEA GO_REF:0000043 | MODIFY | PMID:16600915 |
| 12 | GO:0045944 positive regulation of transcription by RNA polymerase II | IEA GO_REF:0000002 | ACCEPT | PMID:21464308 |
| 13 | GO:0046983 protein dimerization activity | IEA GO_REF:0000002 | ACCEPT | PMID:16623882, PMID:19011118 |
| 14 | GO:0005515 protein binding | IPI PMID:19011118 | MODIFY | PMID:19011118 |
| 15 | GO:0005515 protein binding | IPI PMID:28650476 | REMOVE | PMID:28650476 |
| 16 | GO:0005515 protein binding | IPI PMID:38053494 | REMOVE | PMID:38053494 |
| 17 | GO:0009266 response to temperature stimulus | IDA PMID:25267112 | KEEP_AS_NON_CORE | PMID:25267112 |
| 18 | GO:2000028 regulation of photoperiodism, flowering | IMP PMID:25267112 | ACCEPT | PMID:16600915 |
| 19 | GO:0000976 transcription cis-regulatory region binding | IPI PMID:30356219 | MODIFY | PMID:16623882 |
| 20 | GO:0032991 protein-containing complex | IDA PMID:16623882 | ACCEPT | PMID:16623882 |
| 21 | GO:0005515 protein binding | IPI PMID:30946745 | REMOVE | PMID:30946745 |
| 22 | GO:0003700 DNA-binding transcription factor activity | IDA PMID:16600915 | MODIFY | PMID:16623882, PMID:16600915 |
| 23 | GO:0003700 DNA-binding transcription factor activity | ISS PMID:12837945 | MODIFY | PMID:16623882, PMID:16600915 |
| 24 | GO:0009266 response to temperature stimulus | IMP PMID:16473970 | KEEP_AS_NON_CORE | PMID:16473970 |
| 25 | GO:0009910 negative regulation of flower development | IMP PMID:12114624 | ACCEPT | PMID:12114624, PMID:16600915 |
| 26 | GO:0010048 vernalization response | IEP PMID:15734903 | ACCEPT | PMID:10716723 |
| 27 | GO:0042752 regulation of circadian rhythm | IMP PMID:16473970 | KEEP_AS_NON_CORE | PMID:16473970 |
| 28 | GO:0003700 DNA-binding transcription factor activity | TAS PMID:10716723 | MODIFY | PMID:16623882, PMID:16600915 |
| 29 | GO:0003700 DNA-binding transcription factor activity | ISS PMID:11118137 | MODIFY | PMID:16623882, PMID:16600915 |

The original annotation payloads, including any NOT/contributes-to fields, were preserved. Existing annotations judged here are not cited as their own evidence. Provider-only warning suppression is not a reason to reintroduce provider prose as biological support.

### Final local primary-source access

| Source | Normal cache access |
| --- | --- |
| PMID:10716723 | Abstract only |
| PMID:11118137 | Abstract only |
| PMID:12114624 | Abstract only |
| PMID:12837945 | Abstract only |
| PMID:15734903 | Full text |
| PMID:16473970 | Full text |
| PMID:16600915 | Full text |
| PMID:16623882 | Abstract only |
| PMID:19011118 | Full text |
| PMID:25267112 | Abstract only |
| PMID:28650476 | Full text |
| PMID:30356219 | Abstract only |
| PMID:30946745 | Full text |
| PMID:38053494 | Abstract only |
| PMID:21464308 | Abstract only |

All cited primary caches were inspected at the stated access level; source-specific limits remain explicit in the review.
