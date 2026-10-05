# ASB7 notes

- Substrates: SUV39H1 [PMID:40440427 "ASB7 is recruited to heterochromatin by HP1 and promotes SUV39H1 degradation."] and DDA3/PSRC1 (PMID:27697924). Degron structure: PMID:39039081.
- GO:0120261 (IBA and IDA) is changed (MODIFY) to GO:0120262, since ASB7 is a negative regulator of H3K9me3.
- The spindle phenotype (DDA3) gets no new process annotation: GOA already has CUL5-complex and ubiquitination annotations for the curator-backed DDA3 IDA, so the review keeps those while avoiding de novo spindle-organization process expansion.
- IBA nodes: PTN009082291 (taxon:7711) and PTN000651678, both seeded by ASB7 itself. PTN000651678 comes from the GOA WITH/FROM column but its PANTHER tree is not cached locally, so its taxonomic placement is intentionally not asserted in the review.
- Affinage also reported ASB7-CUL5 ubiquitination of ATF2 at lysine 383 with downstream HDAC6/ITGB2 effects on lung metastasis (PMID:42086529, High confidence) and ASB7 knockdown disrupting mouse-oocyte spindle assembly and cytoskeletal organization (PMID:33251222, Medium confidence). Neither PMID is cached under `publications/`, so these claims were recorded as unverified provider findings rather than used for GO annotation decisions.
