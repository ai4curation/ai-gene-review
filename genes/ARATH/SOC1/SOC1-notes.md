# SOC1 (AGL20, At2g45660; UniProt O64645) curation notes

## 2026-10-05 — finishing review (floral_meristem_identity module)

- GO:0010077 maintenance of inflorescence meristem identity (IGI with BOP1/BOP2, PMID:20626659, abstract-only):
  UNDECIDED -> KEEP_AS_NON_CORE, deferring to the experimental curator (full text not cached); biologically
  consistent because SOC1/AGL24/SVP promote shoot/inflorescence character and are repressed by AP1 in flowers
  [PMID:17428825].
- protein binding IPI with AP1/CAL from PMID:11439126 (AP1/CAL yeast two-hybrid screen; abstract-only):
  UNDECIDED -> MODIFY to GO:0046982, consistent with the independent matrix MADS interaction map [PMID:15805477].
- Three protein binding rows previously MARK_AS_OVER_ANNOTATED: Pin1At (PMID:20129060) and OXS3 (PMID:31540691)
  -> REMOVE (no SOC1-enabled MF follows); Arabidopsis Interactome-1 (PMID:21798944; partners AP1 and FUL)
  -> MODIFY to GO:0046982.
- SOC1 role in the module: integrator that binds and activates the LFY promoter as a SOC1-AGL24 heterodimer [PMID:18466303].


## Autonomous flowering all-member review (2026-10-26)

Independently re-reviewed all 35 original rows, using genuine existing Falcon research only for retrieval leads. Native primary evidence for the core is retained: PMID:18466303 directly resolves SOC1-AGL24 heterodimerization, partner-dependent localization and LFY binding; PMID:18339670 resolves reciprocal SOC1/AGL24 transcriptional regulation and GA context; full PMID:30946745 resolves TFS1 activation and recruitment of REF6/BRM.

The two experimentally supported positive-regulation-of-flower-development rows now remain ACCEPT rather than being replaced by a related phase-transition process that is not their ontological descendant. Broader flower/development regulation is refined to the supported signed process. The core's vegetative-to-reproductive meristem-transition term remains because the primary target/regulatory/genetic evidence supports it; no NEW is manufactured merely to remove a coverage warning. Broad dimerization is refined to the already supported heterodimerization mechanism.

Full PMID:15805477 explicitly places SOC1 in the MADS heterodimer network with floral identity proteins. The original PMID:11439126 abstract foregrounds AP1/SEP3 and does not reveal all SOC1 pairs; it is not treated as proof of wrong-gene attribution. No original SOC1-AGL24 assay is invented for that source. Full PMID:24714165 recovers SOC1 in SAP54-associated material and confirms plant interaction/destabilization; the bare-binding REMOVE is retained strictly as the uninformative-binding exception, not because effector targeting is a false interaction. OXS3 and Pin1At interactions likewise remain biologically real without assigning partner/substrate-modifying activities to SOC1.

Cold and gibberellin expression responses remain valid non-core responses; direct sensing is not required for a response annotation. Cytoplasm is retained as the documented transient-expression localization state, with nuclear accumulation when AGL24 is coexpressed. The exact original genotype details for PMID:20626659 remain unavailable in the local abstract after a normal force-retrieval attempt. The known SOC1 developmental role is retained conservatively with this source-specific limitation, not negated from an abstract omission.

Normal publication caching (`just fetch-gene-pmids ARATH SOC1`) completed. A targeted full-text refresh was interrupted by disk exhaustion before curated writes, then recovered serially after space was freed. Original source files were checked for intact metadata and abstracts; no cache text was edited manually. Existing real provider files were reused rather than fabricated or rewritten. Primary access levels below are those actually cached at final review.

### Per-row audit

Row numbers are zero-based and identify the unchanged original order.

| Row | Term | Original evidence/source | Final action | Primary or curated support |
| --- | --- | --- | --- | --- |
| 0 | GO:0009409 response to cold | IEP PMID:16507079 | KEEP_AS_NON_CORE | PMID:16507079 |
| 1 | GO:0009908 flower development | TAS PMID:10995392 | MODIFY | PMID:11123798, PMID:18466303 |
| 2 | GO:0009911 positive regulation of flower development | IMP PMID:10834834 | ACCEPT | PMID:11123798, PMID:18466303 |
| 3 | GO:0009911 positive regulation of flower development | IMP PMID:11123798 | ACCEPT | PMID:11123798, PMID:18466303 |
| 4 | GO:0010077 maintenance of inflorescence meristem identity | IGI PMID:20626659 | KEEP_AS_NON_CORE | PMID:20626659 |
| 5 | GO:0000977 RNA polymerase II transcription regulatory region sequence-specific DNA binding | IEA GO_REF:0000002 | ACCEPT | PMID:18466303, file:interpro/panther/PTHR48019/PTHR48019-metadata.yaml |
| 6 | GO:0000978 RNA polymerase II cis-regulatory region sequence-specific DNA binding | IBA GO_REF:0000033 | ACCEPT | PMID:30946745, PMID:18466303 |
| 7 | GO:0000981 DNA-binding transcription factor activity, RNA polymerase II-specific | IPI PMID:30946745 | ACCEPT | PMID:30946745, file:ARATH/SOC1/SOC1-deep-research-falcon.md |
| 8 | GO:0003677 DNA binding | IEA GO_REF:0000002 | MODIFY | PMID:18466303 |
| 9 | GO:0003700 DNA-binding transcription factor activity | IEA GO_REF:0000002 | MODIFY | file:ARATH/SOC1/SOC1-uniprot.txt |
| 10 | GO:0003700 DNA-binding transcription factor activity | TAS PMID:10995392 | MODIFY | PMID:10995392 |
| 11 | GO:0003700 DNA-binding transcription factor activity | ISS PMID:11118137 | MODIFY | PMID:11118137 |
| 12 | GO:0003700 DNA-binding transcription factor activity | ISS PMID:11123798 | MODIFY | PMID:11123798 |
| 13 | GO:0003700 DNA-binding transcription factor activity | ISS PMID:12837945 | MODIFY | PMID:12837945 |
| 14 | GO:0005515 protein binding | IPI PMID:11439126 | MODIFY | PMID:15805477, PMID:18466303 |
| 15 | GO:0005515 protein binding | IPI PMID:15805477 | MODIFY | PMID:15805477, PMID:18466303 |
| 16 | GO:0005515 protein binding | IPI PMID:18466303 | MODIFY | PMID:18466303 |
| 17 | GO:0005515 protein binding | IPI PMID:20129060 | REMOVE | PMID:20129060 |
| 18 | GO:0005515 protein binding | IPI PMID:21798944 | MODIFY | PMID:15805477, PMID:18466303 |
| 19 | GO:0005515 protein binding | IPI PMID:24714165 | REMOVE | PMID:24714165 |
| 20 | GO:0005515 protein binding | IPI PMID:31540691 | REMOVE | PMID:31540691 |
| 21 | GO:0046983 protein dimerization activity | IEA GO_REF:0000002 | MODIFY | PMID:18466303 |
| 22 | GO:0006355 regulation of DNA-templated transcription | IEA GO_REF:0000002 | MODIFY | file:ARATH/SOC1/SOC1-uniprot.txt |
| 23 | GO:0006357 regulation of transcription by RNA polymerase II | IBA GO_REF:0000033 | ACCEPT | PMID:30946745 |
| 24 | GO:0009739 response to gibberellin | IEP PMID:18466303 | KEEP_AS_NON_CORE | PMID:18339670 |
| 25 | GO:0045893 positive regulation of DNA-templated transcription | IEP PMID:18339670 | MODIFY | PMID:18339670 |
| 26 | GO:0045944 positive regulation of transcription by RNA polymerase II | IEA GO_REF:0000002 | ACCEPT | file:ARATH/SOC1/SOC1-uniprot.txt, PMID:30946745 |
| 27 | GO:0050793 regulation of developmental process | IEA GO_REF:0000117 | MODIFY | PMID:11123798, PMID:18466303 |
| 28 | GO:0005634 nucleus | IEA GO_REF:0000002 | ACCEPT | PMID:18466303 |
| 29 | GO:0005634 nucleus | IEA GO_REF:0000044 | ACCEPT | file:ARATH/SOC1/SOC1-uniprot.txt |
| 30 | GO:0005634 nucleus | ISM GO_REF:0000122 | ACCEPT | PMID:18466303 |
| 31 | GO:0005634 nucleus | IDA PMID:18466303 | ACCEPT | PMID:18466303 |
| 32 | GO:0005634 nucleus | IDA PMID:31540691 | ACCEPT | file:ARATH/SOC1/SOC1-uniprot.txt, PMID:31540691 |
| 33 | GO:0005737 cytoplasm | IEA GO_REF:0000044 | KEEP_AS_NON_CORE | PMID:18466303 |
| 34 | GO:0005737 cytoplasm | IDA PMID:18466303 | KEEP_AS_NON_CORE | PMID:18466303 |

The original annotation payloads, including any NOT/contributes-to fields, were preserved. Existing annotations judged here are not cited as their own evidence. Provider-only warning suppression is not a reason to reintroduce provider prose as biological support.

### Final local primary-source access

| Source | Normal cache access |
| --- | --- |
| PMID:10834834 | Abstract only |
| PMID:10995392 | Abstract only |
| PMID:11118137 | Abstract only |
| PMID:11123798 | Abstract only |
| PMID:11439126 | Abstract only |
| PMID:12837945 | Abstract only |
| PMID:15805477 | Full text |
| PMID:16507079 | Abstract only |
| PMID:18339670 | Abstract only |
| PMID:18466303 | Abstract only |
| PMID:20129060 | Abstract only |
| PMID:20626659 | Abstract only |
| PMID:21798944 | Full text |
| PMID:24714165 | Full text |
| PMID:30946745 | Full text |
| PMID:31540691 | Abstract only |

All cited primary caches were inspected at the stated access level; source-specific limits remain explicit in the review.

## PR #5574 evidence-preservation follow-up (2026-10-26)

Compared the review with `origin/main` and restored the reference-level findings after reading the cached publications at their stated access levels. The comparison contains 25 findings across 24 references (including the two distinct findings for PMID:18339670). Each reference now retains a source-specific finding; 17 primary-publication findings carry matched source quotations. The original-reference evidence for PMID:10834834, PMID:10995392 and PMID:21798944 is restored alongside the complementary independent evidence.

PMID:10834834 directly identifies SOC1 as an early CONSTANS target required for CO-mediated flowering promotion. PMID:10995392 identifies the dominant FRI suppressor and overexpression rescue of late flowering. PMID:11123798 independently reports late-flowering agl20 mutants and constitutive-expression effects. The two positive-regulation ACCEPT reasons now distinguish those genetic results. The flower-development MODIFY remains unchanged biologically, but its reason explicitly describes a lateral correction to SOC1's positive regulatory role, not a descendant refinement. This supersedes the shorthand "refined" wording for that particular term pair in the earlier audit note.

Full PMID:21798944 documents the binary yeast two-hybrid screen, but the cached main text does not independently expose the exact SOC1-AP1/FUL pairs. Its restored quotation therefore establishes the original assay context; the curated pair assignment and the independent SOC1 MADS interaction studies remain explicitly separate. Similarly, the abstract of PMID:11439126 does not resolve every SOC1 partner. Neither limit justifies erasing the original reference or overturning the supported heterodimerization action.

Restored all four expert-tagged questions, rewording the cold/GA and meristem questions to retain valid response annotations and ask about specific contexts rather than presuppose removal. The complex-composition and root-development questions remain open; they do not manufacture new functions. The two newer native-partner/localization questions are retained, for six questions total. The genuine Falcon report remains a discovery source. The PANTHER metadata's generated description is explicitly marked `llm: true` and `checked: false`; its biological paragraph was removed from direct support for DNA binding, which already has direct SOC1 promoter-binding evidence. Its classification context is retained as a qualified reference finding.

All 35 original annotation payloads and all 35 actions are unchanged. No new annotations, source-cache edits or provider reports were introduced. The source-support table above describes the earlier audit; the additional original-reference quotations documented here supplement its rows 1, 2, 10 and 18.
