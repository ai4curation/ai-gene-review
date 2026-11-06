# FUCA1 notes

Deep research (`just deep-research-falcon human FUCA1`) timed out after 600 s ("All providers failed"),
so the literature work was done manually with PubMed and the cached `publications/` files.

## Function
- Lysosomal tissue alpha-L-fucosidase (GH29, EC 3.2.1.51). Knockout evidence: [PMID:27491075 "Homozygous knockout mice completely lack α-L-fucosidase activity in all tested organs leading to highly elevated amounts of the core-fucosylated glycoasparagine Fuc(α1,6)-GlcNAc(β1-N)-Asn"].
- Order of steps with AGA: [PMID:27491075 "It is known that α1,6-(core)-fucosylation sterically inhibits the lysosomal aspartyl-glucosaminidase (AGA; EC 3.5.1.26)"] -> FUCA1 acts before AGA on glycoasparagines.
- Substrate classes: [PMID:39796208 "This enzyme is responsible for breaking down fucose-containing glycoproteins, glycolipids, and oligosaccharides within the lysosome"].
- Patient cells: [PMID:4074382 "Studies on fibroblasts from patients with less than 5% of normal alpha-L-fucosidase activity (fucosidosis) showed 8 of 11 patients synthesized no detectable alpha-fucosidase protein"]; partial secretion [PMID:1873910 "only 25%-30% of control enzyme was secreted with the remainder retained intracellularly"].

## Annotation notes
- IDA PMID:19666478 is a FUCA2-focused paper, but the full text states "we prepared and characterized human FUCA1 and FUCA2", so the IDA rows are accepted.
- HuRI protein-binding rows (CIB1, MED10, UBQLN2) removed as uninformative.
- Added NEW glycoprotein catabolic process (GO:0006516), which is also the term the dismech Fucosidosis entry marks as DECREASED.
- Module: `modules/lysosomal_glycoprotein_degradation.yaml` (created in the same session).


## Evidence reassessment on 2026-11-01

Re-review of the existing complete human FUCA1 record retains the lysosomal fucosidase core and distinguishes mouse storage experiments from human biochemical evidence. The actual PAINT node is a deep ancestor, not a guessed metazoan clade. HuRI construct interactions remain positive non-core observations. Broad carbohydrate and lysosomal-location terms are refined through actual typed ancestry.

The original urine extension was absent from the inherited review and is preserved in full for restoration. The separately authored glycoprotein-catabolism human IMP row uses mouse evidence and is retained historically, with its quotations, rather than carried forward as a human experiment. The existing catalytic core still describes this biology. The original EPS-urine supplementary table now directly identifies FUCA1, resolving the target-access gap. Its annotation is retained as non-core preparation-level detection, with pooled-sample and possible contamination limits detailed in [the source guide](FUCA1-source-guide.md).

The source guide distinguishes the selected original-paper readings, cached availability and unresolved biological limits. No provider job was retried.

Native acquisition preserved the existing GOA, UniProt, 26-row review and 14 sources; the missing PAINT slice was acquired using the retained cache. The approved reassessment retains all 25 original contexts, restores the urine scope and archives the prior authored NEW row with all three supporting quotations. The full inherited review and all 29 quotation associations remain in the evidence map. Validation and a new EDIT history are recorded after execution.

## Validation outcomes on 2026-11-01

Default schema, ontology, reference and best-practice validation passed, together with strict GOA reconciliation of all 25 original annotations. The native status audit confirms DRAFT with five advisories: three retained positive protein-binding contexts, an unused inherited research file, and glycoprotein catabolism represented in the catalytic core without a new experimental annotation. The source-specific evidence and existing quotations remain unchanged; no annotation was added merely to suppress an advisory.


## Review clarification on 2026-11-01

Both GO:0005764 lysosome annotations are restored to ACCEPT under the root-organelle policy, alongside the existing lumen annotation. Cytoplasm remains TOO_GENERAL because the supported organellar location supplies greater specificity, not because the broad compartment is false. The three positive HuRI binding contexts remain non-core under the standing campaign instruction; no new interaction-derived activity is inferred.

One new IC GO:0006516 annotation is proposed from human fucosidase catalysis and its lysosomal substrate context. Human FUCA1 was characterized in [PMID:19666478](https://pubmed.ncbi.nlm.nih.gov/19666478/), and the [human Reactome reaction](https://reactome.org/content/detail/R-HSA-5693807) identifies it as the enzyme removing fucose from N-glycoprotein. FUCA1 performs a step of degradation. Human patient fibroblast activity supports identity; [PMID:27491075](https://pubmed.ncbi.nlm.nih.gov/27491075/) remains mouse storage evidence. The old human IMP assertion and its quotations stay retired in the archive. Positive same-role MAN2B1/GLB1 annotations, term ancestry and the absence of a local FUCA1 GO-CAM entry were checked; this adds distinct process coverage without duplicating an existing process ancestor or descendant. The core description again states the AGA-dependent sequence of degradation, and the FUCA2 compensation question is restored as an unresolved hypothesis.

The [source guide](FUCA1-source-guide.md#review-clarification-process-inference-and-original-source-locators) now supplies the precise original article/table locators for PMID:9741689, PMID:19056867 and PMID:23533145. PMID:9741689 and PMID:19056867 were read through accessible selected originals despite abstract-only normal caches. PMID:23533145 has cached main text; its supplementary workbook was independently recovered and read. The literal QuickGO urine-extension object and its normalized mapping are indexed in the public evidence file; the TSV itself has no extension column. Reference correctness remains scoped to what was actually read and supports the annotation. Unrelated unread sections are not used as evidence.

All 25 original annotations, source fields and the urine scope are retained; the IC row is separately authored. All 29 inherited quotation associations remain preserved, with 26 active and three historical, and no new quotation is added. The earlier journal entries record prior decisions and are retained unchanged. The reviewed amendment has been applied; actual validation outcomes follow.

## Follow-up validation outcomes on 2026-11-01

Default schema, ontology, reference and best-practice validation passed, as did strict GOA reconciliation of all 25 originals with one separately authored IC annotation. The native status audit confirms DRAFT with four advisories: three supported generic-binding contexts retained under the campaign instruction and the unused inherited research file. All 15 normal sources and all 29 inherited quotation associations remain exact (26 active and three historical); no new quotation was added.
