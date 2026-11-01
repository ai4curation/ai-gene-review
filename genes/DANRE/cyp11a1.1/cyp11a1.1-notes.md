
# cyp11a1.1 source-specific review notes

## 2026-10-25 review

- Fetched with `just fetch-gene DANRE cyp11a1.1 --uniprot-id Q7SYJ6`. Current ZFIN symbol cyp11a1.1 (ZDB-GENE-010306-1), RefSeq NP_694485.2/NM_152953.2, maps to historical cyp11a1/P450scc. Current nomenclature was checked at https://zfin.org/ZDB-GENE-010306-1 and the UniProt REST record; Q7SYJ6 is a full 509-aa protein, not a fragment. The second tandem duplicate is a different locus.
- **Catalytic evidence:** PMID:16437115 describes pregnenolone production, cyp11a1 morphant defects, and cyp11a1 RNA/pregnenolone rescue. Curated RuleBase RU364077 gives conserved cholesterol-cleavage chemistry and inner-membrane topology. Neither an unreviewed DE label nor generic CYP-family membership is used as functional proof.
- **Deployment matters:** PMID:23671259 distinguishes early cyp11a1 expression and primarily gonadal adult expression from the maintained interrenal role of cyp11a2 (current cyp11a1.2). Glucocorticoid biosynthesis, cortisol metabolism and peptide-hormone response remain UNDECIDED for this paralog; no claim of lost cholesterol-cleavage activity is made. This gene is a functional comparator, not a confidently interchangeable interrenal module representative.
- **Developmental phenotype qualification:** the original microtubule/epiboly annotations are retained non-core as pregnenolone-mediated effects, not direct CYP11A microtubule binding. PMID:23955365 identifies CLIP-170 as the pregnenolone effector. PMID:36332486 reports that both homozygous cyp11a1 knockout lines appeared normal despite morphant migration defects. Thus, do not assert unconditional essentiality of this paralog alone.
- PMID:41062373 was fetched as a lead concerning newer Nanog/pregnenolone work, but the cache has no scientific abstract or full text. A press summary and earlier preprint suggest compensation; those were not substituted for the unavailable published primary results or used to assert new functions.
- **Other original sources:** full PMID:28265462 names NM_152953 in ovarian hormone-treatment expression tables/primers; retain the IEP steroid-response context as non-core. Full PMID:31075101 contains heart/vascular morpholino tests but renders the tested gene as cypna1. Construct mapping to the curated cyp11a1.1 record remains unresolved; heart-left/right asymmetry is UNDECIDED, not rejected as wrong gene based on its broad title.
- **Family/PAINT:** PANTHER:PTHR24279:SF3 = CHOLESTEROL SIDE-CHAIN CLEAVAGE ENZYME, MITOCHONDRIAL; parent PTHR24279 = CYTOCHROME P450. Cached IBD PTN001547321 explains inherited process/location terms. Specific tissue uncertainty is not a donor-count criticism, and no unverified tree pruning is proposed.
- No cached GO-CAM role for Q7SYJ6 was identified. The human CYP11A1 model supplies a comparator, not target-specific zebrafish tissue evidence.

### Retrieval and validation provenance

Falcon deep research was attempted for DANRE/cyp11a1.1 with perplexity-lite fallback. Falcon failed authentication (403) and Perplexity returned insufficient_quota (401). No provider research file was fabricated. Manual source-specific findings are recorded here and in reference reviews. Publication caching ran concurrently with research retrieval; initial NCBI 429 failures were retried only for missing records. Existing caches were not force-refreshed except the key abstract-only PMID18403318 and PMID21636783 records needed for source-specific adjudication.

### Reviewed row ledger

1. GO:0004497 (IEA; GO_REF:0000002): MODIFY — The broad P450 oxidoreductase function can be specified as cholesterol side-chain cleavage.
2. GO:0005506 (IEA; GO_REF:0000002): ACCEPT — The CYP11A enzyme uses a catalytic heme iron center.
3. GO:0005739 (ISS; GO_REF:0000024): MODIFY — The mitochondrial location can be refined to the inner membrane.
4. GO:0005743 (IBA; GO_REF:0000033): ACCEPT — Cyp11a1 is assigned to the matrix-facing inner mitochondrial membrane.
5. GO:0005743 (IEA; GO_REF:0000044): ACCEPT — Cyp11a1 is assigned to the matrix-facing inner mitochondrial membrane.
6. GO:0006700 (IBA; GO_REF:0000033): ACCEPT — Pregnenolone synthesis is a directly catalyzed C21-steroid biosynthetic step.
7. GO:0006700 (IMP; PMID:16437115): ACCEPT — Pregnenolone synthesis is a directly catalyzed C21-steroid biosynthetic step.
8. GO:0006704 (IBA; GO_REF:0000033): UNDECIDED — The adrenal-equivalent glucocorticoid role is not resolved for this paralog.
9. GO:0008203 (IBA; GO_REF:0000033): ACCEPT — Cholesterol is directly metabolized by the CYP11A reaction.
10. GO:0008207 (IEA; GO_REF:0000041): MODIFY — C21-steroid metabolism is specifically biosynthetic at this reaction.
11. GO:0008386 (IC; PMID:16437115): ACCEPT — The protein catalyzes cholesterol side-chain cleavage to pregnenolone.
12. GO:0008386 (IEA; GO_REF:0000003): ACCEPT — The protein catalyzes cholesterol side-chain cleavage to pregnenolone.
13. GO:0008386 (ISS; GO_REF:0000024): ACCEPT — The protein catalyzes cholesterol side-chain cleavage to pregnenolone.
14. GO:0016705 (IEA; GO_REF:0000002): MODIFY — The broad P450 oxidoreductase function can be specified as cholesterol side-chain cleavage.
15. GO:0020037 (IEA; GO_REF:0000002): ACCEPT — The CYP11A enzyme uses a catalytic heme iron center.
16. GO:0031116 (IGI; PMID:23955365): KEEP_AS_NON_CORE — Pregnenolone production supports microtubule polymerization during embryonic development.
17. GO:0031116 (IMP; PMID:16437115): KEEP_AS_NON_CORE — Pregnenolone production supports microtubule polymerization during embryonic development.
18. GO:0031116 (IMP; PMID:23955365): KEEP_AS_NON_CORE — Pregnenolone production supports microtubule polymerization during embryonic development.
19. GO:0031966 (IEA; GO_REF:0000044): MODIFY — The mitochondrial location can be refined to the inner membrane.
20. GO:0034650 (IBA; GO_REF:0000033): UNDECIDED — The adrenal-equivalent glucocorticoid role is not resolved for this paralog.
21. GO:0048545 (IEP; PMID:28265462): KEEP_AS_NON_CORE — Ovarian cyp11a1.1 expression responds to steroid treatment.
22. GO:0061371 (IMP; PMID:31075101): UNDECIDED — A heart-asymmetry phenotype is reported, but the source-specific target mapping needs resolution.
23. GO:0071375 (IBA; GO_REF:0000033): UNDECIDED — A peptide-hormone response role remains uncertain for the developmentally specialized paralog.
24. GO:0090504 (IMP; PMID:23671259): KEEP_AS_NON_CORE — The original morpholino study links cyp11a1.1-dependent pregnenolone production to epiboly.

Counts: 5 MODIFY, 10 ACCEPT, 4 UNDECIDED, 5 KEEP_AS_NON_CORE. No NEW annotations were added. All original seeded annotation fields were preserved.
