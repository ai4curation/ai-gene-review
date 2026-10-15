# Ratn1 — curation notes (ALLERGENS backlog, mammalian inhalant cohort)

Rat n 1 = major urinary protein; secreted pheromone-binding lipocalin (major rat allergen). Same curation as Mus m 1 incl. IDA extracellular (PMID:6886376) ACCEPT; metabolic ISS cluster over-annotated.

## Re-review 2026-10-10

GOA refresh (commit a3cf70b6d): no new rows and no retired rows. There is no deep-research file; this re-audit used the UniProt entry (P02761, alpha-2u-globulin / major urinary protein) and the cached source papers for the mouse MUP1 (P11588) donor annotations. PMID:19258313 and PMID:19336396 (both full text) and PMID:6643987 were fetched for this.

Action changes:
- Insulin receptor activity (ISS from mouse MUP1): MARK_AS_OVER_ANNOTATED -> REMOVE. A secreted lipocalin has no receptor architecture, and the donor paper found no effect on insulin receptor phosphorylation [PMID:19258313 "Therefore, it is unlikely that MUP1 inhibits the hepatic gluconeogenic program by increasing insulin sensitivity in the liver."]. The mouse IDA annotation to GO:0005009 from this paper looks like a donor-side error worth reporting upstream.
- Insulin receptor signaling pathway (IEA, GO_REF:0000108, derived from the MF row): MARK_AS_OVER_ANNOTATED -> REMOVE, because the MF it is derived from is removed.
- Small molecule binding (IEA, InterPro): MARK_AS_OVER_ANNOTATED -> MODIFY to pheromone binding (GO:0005550). The term is a correct but generic parent, not an overreach.
- Metabolic ISS cluster (15 BP rows, e.g. energy reserve metabolism, glucose homeostasis, heat generation, locomotor rhythm, negative regulation of gluconeogenesis) and negative regulation of DNA-templated transcription: still MARK_AS_OVER_ANNOTATED. Each now names its donor paper and quotes the evidence, which is pharmacological elevation of circulating recombinant MUP1 in diabetic mice [PMID:19336396 "Chronic elevation of circulating MUP-1 in db/db mice, using an osmotic pump-based protein delivery system, increased energy expenditure and locomotor activity"].
- Cytosol (IEA, ISS): stays KEEP_AS_NON_CORE. The reason was corrected: UniProt places a processed 15.5 kDa form in the cytosol, probably after endocytic uptake from urine ("It is probably taken up from the urinary lumen by endocytosis."). The earlier text called this a "biosynthetic route", which is not correct for a secreted protein.
- Nucleus (ISS) stays MARK_AS_OVER_ANNOTATED; extracellular region (IDA, PMID:6886376) stays ACCEPT and now quotes the urine detection.
- Status DRAFT -> COMPLETE.

Open questions:
- Rat and mouse MUPs form species-specific gene clusters. Should ISS transfers from mouse MUP1 to rat P02761 be made at all?
- Is the mouse MUP1 GO:0005009 insulin receptor activity IDA (PMID:19258313) a curation error? The paper's own data argue against it.
