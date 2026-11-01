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
