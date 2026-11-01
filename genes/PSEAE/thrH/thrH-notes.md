# thrH annotation-review notes

## 2026-10-26 complete native-function review

All 15 seeded rows reviewed. Raw UniProt/GOA source files and every non-review annotation payload are preserved. No NEW rows were proposed.

PMID:10220164 demonstrates that only the thrB/thrH double mutant is threonine auxotrophic in P. aeruginosa. Its historical title calls ThrH a kinase isozyme, but PMID:14699121 resolves the chemistry: phosphoserine hydrolysis and transfer of phosphate from phosphoserine to homoserine. Normal caches are abstract-only; direct reaction results are explicit in the abstracts, and the curated UniProt CC:CAUTION explicitly rejects a homoserine-kinase interpretation. Current GO0004413 requires ATP, so the original IDA row is MODIFY to the already-existing GO0043899, not a redundant NEW annotation. Serine is a coproduct; ATP and ADP do not belong in this reaction.

SerB rescue requires overexpression in the cited study. Retain direct serine formation as conditional non-core physiological participation, with phosphoserine phosphatase as a supported molecular core; do not claim native indispensability. Magnesium binding has independent target structural/biochemical support, so the questionable ISS donor citation does not invalidate the target claim.

PMID:2251281 explicitly studies E. coli PabB and aminodeoxychorismate lyase; PMID:16605270 characterizes chorismate-utilizing ADCS chemistry. Their ISS folate and aminodeoxychorismate assignments are rejected based on the target's demonstrated HAD-like phosphoserine-phosphatase fold and reactions, not just papers naming a different organism. The transferred PabB enzyme machinery is incompatible with the characterized ThrH-family identity. Record these as miscited sources while retaining independently correct magnesium binding. PMID:14699121 PDB1RKU/1RKV maps to Q9I2Y2. No extra NEW binding/process rows.

## Retrieval and evidence limits

Normal fetch-gene seeded this review. Actual Falcon/default research and perplexity-lite fallback were attempted concurrently with normal fetch-gene-pmids; both providers failed access/authentication and no report was fabricated. The actual fetch-fitness attempt failed because no FEBA source was reachable; no fitness phenotype or file is claimed. Full provider/publication/fitness logs are in .cache/module-audit-logs/threonine-PSEAE-thrH-*.log. Additional references were normally fetched; transient 429 errors were retried serially. UniProt source quotes are curated reaction/function/family statements, including explicitly identified orthology inferences, never names/EC fields, electronic GO lines or GOA evidence.

Original experimental claims are judged holistically with independently established function; an abstract-only cache or title focused on another enzyme is not by itself evidence against the claim. The current QuickGO term definitions were inspected and saved in the audit log. Authored GO0004073 labels use the validator's ontology spelling while seeded labels remain untouched. Record-section backfill, strict schema/reference/term checks, helper history and HTML rendering accompany the review.


## Correction of negated ATP-kinase review (2026-10-25)

The original PMID:14699121 GO:0004413 IDA row has negated:true. Its supported claim is NOT ATP-dependent homoserine kinase, consistent with phosphoserine-donor chemistry and UniProt CC:CAUTION. The prior MODIFY to GO:0043899 mistakenly carried that negation onto the experimentally demonstrated phosphotransferase activity. Corrected to ACCEPT of the original negative assertion; the separate positive GO:0043899 row is unchanged. This supersedes the earlier review decision, not the original annotation or prior history.


## PR #5569 source-specific corrective review (2026-10-26)

The target family/reaction quote did not establish localization. Traced the ancestral IBA node and donor identities; no target loss or phylogenetic error is alleged. Native localization remains UNDECIDED pending independent source resolution; recombinant solubility is not relabeled as native compartment evidence.

Action changes: Row 5 GO:0005737: ACCEPT → UNDECIDED.

All 15 original rows and their non-review payloads were compared against the pre-correction snapshot and remain identical. This update supersedes contradictory earlier review prose; it does not overwrite fetched source files. Focused strict schema, term and source checks and HTML rendering are recorded in the PR follow-up report.


## 2026-10-26 PR #5569 second follow-up

Replaced the shared action-only summaries and catalytic boilerplate with enzyme-specific chemistry and row-specific source assessments. Existing annotation payloads and raw UniProt/GOA files remain unchanged. Distinct experimental, PAINT, domain/rule and homolog-transfer rows now state what each evidence stream establishes. No new biological annotation was proposed.

PMID:14699121 establishes HPLC-detected phosphate transfer from phosphoserine to homoserine, with serine coproduct, alongside hydrolytic phosphoserine phosphatase activity. The original negated ATP-dependent homoserine-kinase row remains ACCEPT. Native double-mutant auxotrophy in PMID:10220164 is distinct from overexpression rescue of serB. The cytoplasmic IBA is now ACCEPT as a qualified ancestral inference: actual PTN000000002 is SOUND in the PTHR43344 family review and has publication-linked cytosolic PSPH donor evidence. No direct target localization assay is claimed.

All 24 current panel reviews remain within the preservation proof (439 rows, including the pre-existing proposal). Focused schema/term/source checks, derived record sections, renders and helper-generated Codex histories accompany the changed genes. No module, tracker, staging, commit or full-repository validation is part of this follow-up.


## 2026-11-01 bacterial native-route audit

Re-examined all 15 existing annotation decisions; no action or original annotation payload changes. ThrH remains a directly characterized alternative homoserine-phosphorylation mechanism, not an ATP kinase and not evidence by itself for a complete PAO1 aspartate-to-threonine route. Native double disruption establishes threonine auxotrophy [PMID:10220164, "threonine auxotrophy is observed only when both thrB and thrH are"], while the later HPLC experiment identifies the phosphoserine donor [PMID:14699121, "homoserine using phosphoserine as the phosphoryl group donor"]. Retain the accepted negative ATP-kinase row and the separate positive phosphotransferase row. The previously traced cytoplasmic IBA and structurally contradicted PabB-like ISS transfers remain as adjudicated. The serB overexpression rescue is conditional and does not establish native indispensability.

Added explicit reference assessments and mined findings for the two primary studies. The new module uses ThrH only as a separately marked step comparator, without substituting it across species. A fresh normal Falcon request failed (provider exit 1); no provider report was authored. The MOD-description command skipped PSEAE because no provider is configured. Existing fetched records and publication caches remain unchanged.
