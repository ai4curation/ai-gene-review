# FERMT3 database source guide

The source-keyed [decision table](FERMT3-database-decisions.yaml) preserves all imported fields for the 20 database contexts. Full manual database assessments and four additional paper assessments appear in the review YAML; the six original PMID assessments belong to the direct-review source guide.

| Source | Actual evidence examined | Boundary |
|---|---|---|
| GO_REF:0000120 / GO_REF:0000024 | Q8K1B8 mouse record, matching experimental GO rows, SL-0295; PMID:16876785 original localization Results and Figure 5F | Curated mouse-to-human podosome inference; SL-0295 is not an HPA assay |
| GO_REF:0000107 | Ensembl one-to-one ENSG00000149781–ENSMUSG00000024965; mouse ENSMUSP00000037858 and exact donor GO rows | Gene orthology is verified; no all-splice-product functional claim |
| GO_REF:0000033 | Official PTHR16160 member/labels, seven literal positive IBD joins, actual 144-sequence MSA | Tree request timed out; the [phylogeny record](FERMT3-phylogeny-evidence.yaml) makes no target-to-IBD path claim |
| GO_REF:0000002 | Target IPR037837 and IPR037843 matches and mapping outputs | Domain/family inference evaluated alongside actual signaling evidence |
| GO_REF:0000117 | ARBA00028907, 35 condition sets, GO:0030335 output | Exact target-matching rule branch not reconstructed; separate human-cell evidence supports a bounded migration role |
| Reactome:R-HSA-481007 | Input 481003 → Q86UX7 entity 8862993; output 481033 → entity 8862985 | Literal cargo routes verified; source-specific location evidence remains unresolved |

PMID:16876785 was read in the original author-thesis reprint: Methods and Kindlin-3 localization Results, original pages 3143–3144 and 3148–3150, Figure 5F caption. Mouse cellular context and tagged versus endogenous observations are retained. Figure 6 concerns other kindlins.

PMID:18278053 was read from the author-uploaded original: Results, Methods and Figures 1–4 captions. Its normal cache remains abstract-only. The direct binding experiment uses the F3 domain; original figure pixels and supplements were not independently read.

PMID:19234461 was read as the original article reprinted in the author thesis, original pages 300–305 (PDF pages 166–171): tail-binding, adhesion, arrest and rolling Results, main Methods and figure captions. Supplemental methods/videos and original figure pixels were not independently inspected.

For PMID:23640497, only the indexed original first page and verified metadata/abstract were accessible. The exact FERMT3 table, full Methods and supporting compartment result remain unread after preserved access failures. This limitation is not a claim that the protein was absent from the study.

The independently read human evidence is localized to PMID:19234460 Results and Figure 4 contact-site rescue, and PMID:19234463 Figure 4 migration/adhesion plus the mouse construct clause in Methods. Keep the complete direct-review reference assessments. The [product map](FERMT3-database-product-map.yaml) records sequence boundaries without converting artificial constructs or patient bands into natural products.
