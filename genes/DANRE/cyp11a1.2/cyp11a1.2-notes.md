
# cyp11a1.2 source-specific review notes

## 2026-10-25 review

- Fetched with `just fetch-gene DANRE cyp11a1.2 --uniprot-id A0A8M9Q8E0`. Current ZFIN symbol cyp11a1.2 (ZDB-GENE-130911-1), RefSeq XP_691817.1, maps to historical cyp11a2. Current nomenclature was verified at https://zfin.org/ZDB-GENE-130911-1 and UniProt REST; the accession is a full 512-aa protein, not a fragment.
- PMID:23671259 identifies the paralog expressed after formation of the interrenal primordium and in adult interrenal/gonadal tissues. Its morphant phenotype is rescued by pregnenolone. Stable CRISPR mutants in PMID:31693487 show profound glucocorticoid and androgen deficiency, independently establishing interrenal and gonadal steroidogenic function. This is the preferred zebrafish representative for conserved interrenal cholesterol entry.
- Curated RuleBase RU364077 supplies the exact cholesterol-to-pregnenolone reaction and inner-membrane localization; localization/cofactor assignments remain comparative rather than direct microscopy or metal-occupancy measurements. Catalytic family does not establish tissue expression; primary paralog studies do.
- Cortisol metabolism is refined to the existing cortisol biosynthesis term. Shared upstream catalysis genuinely participates in the pathway. The positive-regulation-of-steroid-biosynthesis row is refined to steroid hormone biosynthesis: loss of a biosynthetic enzyme is not by itself evidence of a separate regulator.
- Spermatogenesis is KEEP_AS_NON_CORE. PMID:34932120 independently finds ovarian/testicular abnormalities and shows mutant spermatogonial stem cells differentiating in wild-type hosts. This supports a steroidogenic tissue environment rather than a cell-autonomous enzyme role in germ-cell differentiation.
- The peptide-hormone-response context is retained non-core as the steroidogenic effector in the HPI axis, with no peptide-binding or signal-transducer function inferred. The target studies establish steroid output and feedback, not a direct ligand-binding assay.
- PANTHER:PTHR24279:SF3 has official label CHOLESTEROL SIDE-CHAIN CLEAVAGE ENZYME, MITOCHONDRIAL; broad parent PTHR24279 is CYTOCHROME P450. Cached IBD PTN001547321 supports inherited annotations; refinement does not reject its ancestral placement.
- No cached GO-CAM role for A0A8M9Q8E0 was identified. Human pathway evidence is not relabeled as zebrafish tissue evidence. No assertion of mammalian aldosterone synthesis or universal vertebrate adrenal anatomy follows from this shared entry reaction.

### Retrieval and validation provenance

Falcon deep research was attempted for DANRE/cyp11a1.2 with perplexity-lite fallback. Falcon failed authentication (403) and Perplexity returned insufficient_quota (401). No provider research file was fabricated. Manual source-specific findings are recorded here and in reference reviews. Publication caching ran concurrently with research retrieval; initial NCBI 429 failures were retried only for missing records. Existing caches were not force-refreshed except the key abstract-only PMID18403318 and PMID21636783 records needed for source-specific adjudication.

### Reviewed row ledger

1. GO:0004497 (IEA; GO_REF:0000002): MODIFY — The broad P450 oxidoreductase function can be specified as cholesterol side-chain cleavage.
2. GO:0005506 (IEA; GO_REF:0000002): ACCEPT — The CYP11A enzyme uses a catalytic heme iron center.
3. GO:0005743 (IBA; GO_REF:0000033): ACCEPT — Cyp11a1 is assigned to the matrix-facing inner mitochondrial membrane.
4. GO:0005743 (IEA; GO_REF:0000044): ACCEPT — Cyp11a1 is assigned to the matrix-facing inner mitochondrial membrane.
5. GO:0006694 (IMP; PMID:23671259): MODIFY — The enzyme directly supplies steroid hormone precursor synthesis.
6. GO:0006700 (IBA; GO_REF:0000033): ACCEPT — Pregnenolone synthesis is a directly catalyzed C21-steroid biosynthetic step.
7. GO:0006704 (IBA; GO_REF:0000033): ACCEPT — Cyp11a1.2 supplies the entry reaction for interrenal glucocorticoid synthesis.
8. GO:0007283 (IMP; PMID:31693487): KEEP_AS_NON_CORE — Loss of cyp11a1.2 disrupts spermatogenesis through the gonadal steroidogenic environment.
9. GO:0008203 (IBA; GO_REF:0000033): ACCEPT — Cholesterol is directly metabolized by the CYP11A reaction.
10. GO:0008207 (IEA; GO_REF:0000041): MODIFY — C21-steroid metabolism is specifically biosynthetic at this reaction.
11. GO:0008386 (IEA; GO_REF:0000003): ACCEPT — The protein catalyzes cholesterol side-chain cleavage to pregnenolone.
12. GO:0016705 (IEA; GO_REF:0000002): MODIFY — The broad P450 oxidoreductase function can be specified as cholesterol side-chain cleavage.
13. GO:0020037 (IEA; GO_REF:0000002): ACCEPT — The CYP11A enzyme uses a catalytic heme iron center.
14. GO:0031966 (IEA; GO_REF:0000044): MODIFY — The mitochondrial location can be refined to the inner membrane.
15. GO:0034650 (IBA; GO_REF:0000033): MODIFY — The supported cortisol role is biosynthetic.
16. GO:0034651 (IMP; PMID:23671259): ACCEPT — Cyp11a1.2 supplies the entry reaction for interrenal glucocorticoid synthesis.
17. GO:0071375 (IBA; GO_REF:0000033): KEEP_AS_NON_CORE — Cyp11a1.2 is a steroidogenic effector within the hormone-regulated interrenal axis.
18. GO:0090031 (IMP; PMID:31693487): MODIFY — The mutant phenotype establishes steroid hormone biosynthesis rather than a separate positive regulator.

Counts: 7 MODIFY, 9 ACCEPT, 2 KEEP_AS_NON_CORE. No NEW annotations were added. All original seeded annotation fields were preserved.
