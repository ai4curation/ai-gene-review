# metL annotation-review notes

## 2026-10-26 complete native-function review

All 20 seeded rows reviewed. Raw UniProt/GOA source files and every non-review annotation payload are preserved. No NEW rows were proposed.

MetL is the methionine-repressible aspartokinase II/homoserine dehydrogenase II. PMID:4889171 is bibliographic-only in the normal cache; its title explicitly identifies purification of one homogeneous bifunctional protein. Accept the well-established reactions using independently curated UniProt reactions and the genetic assignments in PMID:4148765; do not manufacture assay details from the title. The kinase supplies the DAP branch as well as homoserine pathways, but no NEW lysine process row was added. Methionine repression of synthesis is distinct from direct end-product allostery; PMID:17012784 full-text introduction explicitly distinguishes MetL from ThrA and LysC.

As for ThrA, the curated NAD(H) reaction is an orthology inference from Q9SA18, not a measured cofactor-preference result for this target. Current GO0004412 is NADP specific and does not replace the NAD-specific GO0004022 claim. Retain that existing activity and NAD binding as non-core with explicit inference limits. The two core functions reflect the separate kinase and NADP-dependent homoserine dehydrogenase domains; cofactors are integrated, not free-standing cores.

## Retrieval and evidence limits

Normal fetch-gene seeded this review. Actual Falcon/default research and perplexity-lite fallback were attempted concurrently with normal fetch-gene-pmids; both providers failed access/authentication and no report was fabricated. The actual fetch-fitness attempt failed because no FEBA source was reachable; no fitness phenotype or file is claimed. Full provider/publication/fitness logs are in .cache/module-audit-logs/threonine-ECOLI-metL-*.log. Additional references were normally fetched; transient 429 errors were retried serially. UniProt source quotes are curated reaction/function/family statements, including explicitly identified orthology inferences, never names/EC fields, electronic GO lines or GOA evidence.

Original experimental claims are judged holistically with independently established function; an abstract-only cache or title focused on another enzyme is not by itself evidence against the claim. The current QuickGO term definitions were inspected and saved in the audit log. Authored GO0004073 labels use the validator's ontology spelling while seeded labels remain untouched. Record-section backfill, strict schema/reference/term checks, helper history and HTML rendering accompany the review.


Assembly source conflict: current UniProt says homotetramer, whereas the introduction of full PMID:17012784 cites a native solution dimer for AK-HDH II. No oligomer count is asserted in this review core; resolution requires the original Dautry-Varsat1977 experiment rather than transferring ThrA stoichiometry.


## PR #5569 source-specific corrective review (2026-10-26)

Live QuickGO definitions checked on 2026-10-26: GO:0004022 explicitly uses NAD+; GO:0004412 explicitly uses NADP+. Homoserine is a primary alcohol, so its NAD-dependent oxidation fits GO:0004022 without implying ethanol metabolism or substrate promiscuity. Both can refine their common broad oxidoreductase ancestor. Retain the NAD-dependent catalytic capacity as core across all four enzymes, while distinguishing directly measured yeast kinetics from conserved inference in other targets. Missing native cofactor comparisons limit claims about physiological preference, not the biological centrality of the supported homoserine reaction. Earlier fungal MODIFY to GO:0004412 erased the cofactor distinction and is superseded. Sources: https://www.ebi.ac.uk/QuickGO/term/GO:0004022 and https://www.ebi.ac.uk/QuickGO/term/GO:0004412 .

Replaced genetic-map-only support for biosynthetic processes with the curated UniProt CC:PATHWAY statements identifying MetL steps 1 and 3. PMID:4148765 is not treated as biochemical pathway evidence.

Action changes: the existing NAD-dependent alcohol-dehydrogenase and NAD+ binding assertions change from KEEP_AS_NON_CORE to ACCEPT, because both describe integral catalytic properties of the homoserine reaction. Evidence limitations are recorded separately from core status.

All 20 original rows and their non-review payloads were compared against the pre-correction snapshot and remain identical. This update supersedes contradictory earlier review prose; it does not overwrite fetched source files. Focused strict schema, term and source checks and HTML rendering are recorded in the PR follow-up report.


## 2026-10-26 PR #5569 second follow-up

Replaced the shared action-only summaries and catalytic boilerplate with enzyme-specific chemistry and row-specific source assessments. Existing annotation payloads and raw UniProt/GOA files remain unchanged. Distinct experimental, PAINT, domain/rule and homolog-transfer rows now state what each evidence stream establishes. No new biological annotation was proposed.

The N-terminal ATP-dependent kinase and C-terminal homoserine dehydrogenase are distinguished. PMID:4889171 is retained as the legacy purification citation, but its title-only accessible record is not expanded into invented kinetic or oligomer details. Curated target pathway/reaction statements supply independent support. NAD-dependent GO:0004022 remains ACCEPT and is not replaced by the NADP-specific sibling. Plant donor chemistry does not transfer chloroplast localization or allosteric regulation.

All 24 current panel reviews remain within the preservation proof (439 rows, including the pre-existing proposal). Focused schema/term/source checks, derived record sections, renders and helper-generated Codex histories accompany the changed genes. No module, tracker, staging, commit or full-repository validation is part of this follow-up.
