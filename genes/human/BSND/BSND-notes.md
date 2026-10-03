# BSND curation notes

## 2026-10-03 — barttin channel-regulator review

The reviewed human UniProt record is Q8WZ55 (secondary accession Q6NT28), BSND/BART, HGNC:16512, 320 amino acids. The imported record contains no named alternative-products section and the 52-object seed has no `alternative_products` slot. The frameshift caution on BC069510 is not a named functional isoform. Partner accessions with isoform suffixes remain partner identifiers; they are not converted into BSND isoform annotations.

The normal source run 37117972985 at immutable commit `944f6386ed0a51d64c91daf95b372b625afe22cb` produced the complete 52-row GOA projection. ROOT imported three primary files, two absent publication caches and one Reactome cache after authenticated artifact recovery. The two pre-existing publication variants were retained unchanged. The PANTHER exports remain quarantined. No source file was rewritten during this review.

### Molecular mechanism and annotation decisions

Barttin is an accessory regulator of ClC-Ka/ClC-Kb channels. The [2002 primary abstract](https://pubmed.ncbi.nlm.nih.gov/12111250/) reports channel coexpression, altered currents, increased surface abundance and co-immunoprecipitation. These observations support both association and a functional regulatory role. They do not demonstrate that barttin supplies the conducting pore, or a purified binary interaction. The two targeted generic-binding rows are refined to chloride channel regulator activity, overlapping an already annotated function rather than manufacturing a new annotation.

The two chloride-channel annotations already have `contributes_to`. They are retained on that complex-subunit interpretation. The two general complex annotations are refined to chloride channel complex. Official GO defines [GO:0017081](https://amigo.geneontology.org/amigo/term/GO:0017081) by channel binding and modulation and [GO:0034707](https://amigo.geneontology.org/amigo/term/GO:0034707) by chloride passage through the assembled complex. A single core connects the own regulator activity, contribution to channel activity and [chloride transmembrane transport](https://amigo.geneontology.org/amigo/term/GO:1902476). This specific process subsumes the broad transport ancestor in the synthesis. No NEW annotation, independent pore activity, exact complex stoichiometry or separate chaperone activity is asserted.

The inner-ear physiological role is retained as non-core sensory context. The [official abstract of PMID:11734858](https://pubmed.ncbi.nlm.nih.gov/11734858/) independently describes ClC-K/barttin heteromers in renal and inner-ear basolateral membranes. It was read as external context; it is not yet a normal cached YAML reference or quoted support. The YAML hearing rationale cites the imported curated UniProt record and does not claim an independent audit of the original mouse inference.

### Localization discrepancy resolved from primary text

The normal cache for [PMID:18776122](https://pmc.ncbi.nlm.nih.gov/articles/PMC2615720/) is abstract-only despite its PMCID. Its abstract calls WT insertion preferentially apical. In contrast, the accessible official indexed Results and Figure 5 caption explicitly place WT predominantly basolaterally and describe increased apical/equalized distribution with E88X. Selected Methods identify human barttin/ClC-K constructs, polarized MDCK filter cultures, confocal localization and sided surface biotinylation. The basolateral IDA assertion is therefore accepted. This is human protein in a model epithelium, not direct native-human kidney imaging. Direct PMC opening returned a challenge; the successful indexed passages and consultation are saved in `tmp/BSND-localization-consultation/`. No figure images or complete-paper access are claimed, and the canonical cache remains unchanged.

### Interaction-screen boundaries and reference access

The 26 HuRI and five neurodegeneration-map rows retain their exact source partner accessions and remain UNDECIDED. The canonical HuRI entry includes an XML-derived body, but the BSND-specific pair records and validation tables were not inspected. The other map is abstract-only. UniProt interaction listings corroborate that these are curated reported edges; they do not independently establish each original screen result or its physiological function. No wrong-gene accusation, partner-function transfer or removal for low informativeness is made. The standing [project curation instruction](../../../projects/CLINGEN_MENDELIAN.md#curation-instructions) retains supported correct generic binding as KEEP_AS_NON_CORE when a specific replacement is not established; unresolved evidence remains UNDECIDED.

All four canonical publication abstracts, the complete UniProt record and complete Reactome entry were read. Reactome includes CLCN1/2 as well as CLCNKA/B; only its BSND-associated channel passage informs this review. Other channels' oligomeric properties are not transferred. GO method references remain machine-sourced; no complete PAINT tree or ortholog-donor audit is claimed, and the human target appearing among PAINT evidence is not treated as circular. The local GO-CAM index search returned no BSND/Q8WZ55 hit; no NEW inference depends on that absence.

### Research and review record

The standard Falcon research attempt with perplexity-lite fallback failed DNS and produced no provider output. Its filtered, credential-safe outcome is saved in `tmp/BSND-scientific-proposal/provider-attempt-assessment.json`; these notes are manual research and are not provider-branded output. All 52 decisions were authored in TMP, preserving every machine annotation field and all ten original reference identities. One UniProt file reference was added. Four canonical-cache-exact quote entries total 20 words from PMID:12111250 and eight from PMID:18776122, counting repeats. Bloc supplied a bounded localization/core consultation; ROOT remains the independent final science reviewer.

All 52 annotations have been assessed, with 31 explicit UNDECIDED screen assertions. Normal full candidate validation including terms, references and GOA completed with zero curation warnings or errors. The final review status is COMPLETE under the repository no-PENDING/no-warning rule; it does not resolve those evidence limits. The external pkg_resources deprecation message is a tooling advisory. Independent science approval and canonical application follow separately.

## 2026-10-03 — canonical application

The independently reviewed candidate was applied after checking the exact seeded preimage. Normal canonical validation passed without errors or curation warnings, and the standard codex/gpt-6 CREATE history was scaffolded and validated. COMPLETE records assessment of all 52 assertions; 31 source-specific screen edges remain UNDECIDED. The original source fields, raw GOA and UniProt records, normal publication caches, Reactome entry and quarantined family exports were preserved. Earlier candidate-stage statements above describe the prior stage and are superseded by this application entry.

## 2026-10-03 — first published-review follow-up

This entry supersedes the earlier current-state statements about 31 unresolved screen annotations and uncached mechanism references. It preserves the earlier notes as a dated record. All 52 machine source objects remain intact, including each interaction partner, evidence code and qualifier. The present judgments are 16 ACCEPT, 32 KEEP_AS_NON_CORE and four MODIFY, with no NEW annotation. The four pre-existing refinements and their source partners remain unchanged.

### Screen evidence and the standing curation instruction

The 26 HuRI and five neurodegeneration-map binding assertions are retained as non-core reported experimental interactions. Each exact partner accession was joined to the normal UniProt/IntAct record; all have three reported experiments except ARFIP1, which has five. These are experiment counts, not independent publications. The original publication reference and the in-repository UniProt source now support every row. No generic binding is removed merely for being uninformative: the standing [project curation instruction](../../../projects/CLINGEN_MENDELIAN.md#curation-instructions) applies.

The [HuRI source](https://pmc.ncbi.nlm.nih.gov/articles/PMC7169983/) describes multiple Y2H implementations, pairwise retesting and sequence confirmation. Its dataset-level orthogonal validation does not establish individual orthogonal validation for each BSND edge. The normal XML-derived body was inspected, but its supplementary target records were not. The [neurodegeneration-map primary manuscript](https://pub.dzne.de/record/153392/files/DZNE-2020-01389.pdf) was accessible through indexed Results on pages 2–3 describing Y2H screening/retesting and integration of prior binary interactions. Opening the complete PDF exceeded the web size limit; the normal cache remains abstract-only. Neither an individual supplementary pair nor an image was independently inspected. Source-specific curator deference, with these explicit limits, supports retention; absence of an independent native-context assay is not treated as grounds for rejection. Native biological roles and precise constructs remain open questions.

### Localization conflict recorded without rewriting the source

The basolateral IDA row remains ACCEPT. Its supporting evidence now includes the normal UniProt localization statement. The specific apical-WT sentence in the [PMID:18776122 abstract](https://pmc.ncbi.nlm.nih.gov/articles/PMC2615720/) is recorded as a DISPUTED finding because the same paper's inspected Results/Figure 5 caption and the curated UniProt statement distinguish basolateral WT from altered E88X sorting. This is an internal abstract/body discrepancy, not a retraction, published correction, or invalidation of the whole paper. Human constructs in polarized MDCK cells remain distinct from native human tissue imaging; no supplementary-image inspection is claimed.

### Mechanism references now available in normal caches

One ordinary hosted fetch at run37121579647 produced the six requested references. The authenticated artifact and ROOT's exclusive import preserved existing source bytes. The normal caches contain five abstracts and one longer HTML extraction. Reference reviews state those actual limits.

- [PMID:11734858](https://pubmed.ncbi.nlm.nih.gov/11734858/) directly connects the ClC-K/barttin complex to basolateral renal and inner-ear epithelia and potassium recycling. It now supports the hearing-context row and core; the original mouse donor record has not been independently reconstructed.
- [PMID:12574213](https://pubmed.ncbi.nlm.nih.gov/12574213/) is a clinical G47R case with mild renal presentation and congenital deafness. Its suggested severity explanation is not presented as a direct functional assay.
- [PMID:16849430](https://pmc.ncbi.nlm.nih.gov/articles/PMC1544099/) separates trafficking, conductance and gating using human barttin with rat ClC-K1 or human ClC-Kb in tsA201/MDCKII cells. The complete extracted Results, Discussion and Methods were read. Figures and Table 1 lack their image/data display in this extraction. Rat channel behavior is not automatically attributed to human channels.
- [PMID:19646679](https://pubmed.ncbi.nlm.nih.gov/19646679/) reports I12T-associated deafness and trafficking impairment with retained channel function; only its abstract was recovered.
- [PMID:20538786](https://pubmed.ncbi.nlm.nih.gov/20538786/) supports cooperative/common-gate modulation with explicit rat ClC-K1 versus human ClC-Ka boundaries; only the abstract was recovered.
- [PMID:26013830](https://pubmed.ncbi.nlm.nih.gov/26013830/) supports C54/C56 palmitoylation-dependent activation. Its abstract separates reduced active channel number from membrane insertion and single-channel properties. Barttin is the modified accessory subunit, not a palmitoyltransferase.

The single core retains its own chloride-channel regulator activity and contribution to chloride-channel activity. Added mechanism detail does not turn barttin into the pore or add a separate catalytic function. The existing broad chloride-transport annotations remain supported; the core uses the more specific chloride transmembrane transport term rather than duplicating ancestor and child. Distinct CLCNKA/CLCNKB partners justify preserving the two source-specific regulator refinements despite overlap with an existing regulator annotation. Short quotations were checked against canonical caches and complete clauses replaced the earlier fragmentary anchors.

### Review and validation outcome

All 52 source assertions have been assessed. Normal full validation, including references, ontology terms and GOA coverage, passed with 31 expected generic-binding policy warnings and no errors. The review status is DRAFT because those intentional warnings remain; this does not relabel the retained evidence as unresolved. Ten short quotation entries are exact canonical substrings, with at most 19 words from any one publication after counting repeats. Independent follow-up review and canonical application are recorded separately. The earlier COMPLETE/31-UNDECIDED state above is historical.

## 2026-10-03 — first follow-up applied

The independently reviewed follow-up was applied after exact preimage checks. Normal candidate and canonical validation passed with 31 intentional generic-binding policy warnings and no errors; DRAFT is the current review status. All 52 source assertions are assessed (16 ACCEPT, 32 KEEP_AS_NON_CORE, four MODIFY), with the source-specific access limits retained. The standard codex/gpt-6 EDIT history was scaffolded and validated. Six normal reference caches were imported separately before this application; this application preserved all source caches and prior histories. Earlier status and access statements remain historical.
