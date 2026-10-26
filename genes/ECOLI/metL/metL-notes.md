# metL annotation-review notes

## 2026-10-26 complete native-function review

All 20 seeded rows reviewed. Raw UniProt/GOA source files and every non-review annotation payload are preserved. No NEW rows were proposed.

MetL is the methionine-repressible aspartokinase II/homoserine dehydrogenase II. PMID:4889171 is bibliographic-only in the normal cache; its title explicitly identifies purification of one homogeneous bifunctional protein. Accept the well-established reactions using independently curated UniProt reactions and the genetic assignments in PMID:4148765; do not manufacture assay details from the title. The kinase supplies the DAP branch as well as homoserine pathways, but no NEW lysine process row was added. Methionine repression of synthesis is distinct from direct end-product allostery; PMID:17012784 full-text introduction explicitly distinguishes MetL from ThrA and LysC.

As for ThrA, the curated NAD(H) reaction is an orthology inference from Q9SA18, not a measured cofactor-preference result for this target. Current GO0004412 is NADP specific and does not replace the NAD-specific GO0004022 claim. Retain that existing activity and NAD binding as non-core with explicit inference limits. The two core functions reflect the separate kinase and NADP-dependent homoserine dehydrogenase domains; cofactors are integrated, not free-standing cores.

## Retrieval and evidence limits

Normal fetch-gene seeded this review. Actual Falcon/default research and perplexity-lite fallback were attempted concurrently with normal fetch-gene-pmids; both providers failed access/authentication and no report was fabricated. The actual fetch-fitness attempt failed because no FEBA source was reachable; no fitness phenotype or file is claimed. Full provider/publication/fitness logs are in .cache/module-audit-logs/threonine-ECOLI-metL-*.log. Additional references were normally fetched; transient 429 errors were retried serially. UniProt source quotes are curated reaction/function/family statements, including explicitly identified orthology inferences, never names/EC fields, electronic GO lines or GOA evidence.

Original experimental claims are judged holistically with independently established function; an abstract-only cache or title focused on another enzyme is not by itself evidence against the claim. The current QuickGO term definitions were inspected and saved in the audit log. Authored GO0004073 labels use the validator's ontology spelling while seeded labels remain untouched. Record-section backfill, strict schema/reference/term checks, helper history and HTML rendering accompany the review.


Assembly source conflict: current UniProt says homotetramer, whereas the introduction of full PMID:17012784 cites a native solution dimer for AK-HDH II. No oligomer count is asserted in this review core; resolution requires the original Dautry-Varsat1977 experiment rather than transferring ThrA stoichiometry.
