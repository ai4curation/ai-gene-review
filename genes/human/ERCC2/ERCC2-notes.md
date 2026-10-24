# ERCC2 annotation review notes

## Biological conclusions

The two principal roles are ATP-driven 5′–3′ DNA unwinding during nucleotide-excision repair and structural organization of TFIIH for RNA-polymerase-II transcription initiation. The full-length human evidence distinguishes XPD from XPB motor activity and CDK7 kinase activity. CIA interactions identify XPD as an Fe–S maturation client. The canonical 760-aa and reported 405-aa products remain distinct; no functional equivalence is inferred.

Detailed synthesis is in [ERCC2-deep-research-manual.md](ERCC2-deep-research-manual.md); public original-paper URLs, Methods/Figure locators and database chains are in [ERCC2-source-guide.md](ERCC2-source-guide.md).

## Annotation decisions

All 151 imported contexts have manual decisions: 94 ACCEPT, 25 MODIFY, 21 KEEP_AS_NON_CORE, 10 UNDECIDED and 1 MARK_AS_OVER_ANNOTATED. No new annotation is proposed. The raw acquisition had 152 records; one deterministic context collapse produced 151 seeded review rows. Every imported source object and both natural-product records are preserved.

Broad nuclear, catalytic and transcription annotations are refined consistently across sources. The TFIID assignment is corrected to TFIIH from the original preparation and current definitions. The developmental-expression transfer is over-annotated because the rat source measures expression during organogenesis without establishing XPD-specific developmental work. Hypoxia, MMXD/spindle, oxidative-stress, hair-cell and unresolved target-pair claims retain explicit uncertainty where the supporting source cannot be adjudicated.

Supported generic interactions remain non-core unless an informative functional role is established, in which case they are refined. This follows the [ClinGen Mendelian campaign curation instructions](../../../projects/CLINGEN_MENDELIAN.md#curation-instructions). No new publication quotations are added under the same campaign policy. Incomplete source access is never treated as a wrong-gene or wrong-paralog finding.

## Evidence boundaries

All 68 Reactome contexts trace through forward participant/component links to full-length human P18074 with its own nucleoplasmic compartment. Event surroundings do not give XPD other proteins' catalytic activities. Five PAINT assertions have verified nodes, target ancestry and canonical sequence alignment; the single experimentally studied yeast donor for damaged-DNA binding is legitimate phylogenetic evidence.

The source guide separates complete original access from missing supplementary target records. Fourteen directly cited originals remain incomplete or unavailable; independent primary evidence resolves many shared functions without pretending those originals were inspected. Fifty-eight initial publication caches and five later donor caches remain unchanged. Only sources used by this review are selected for publication.

The canonical product is reconstructed at 760 residues and the alternative product at 405 residues from UniProt's explicit VSP edits. These lengths do not establish stability, expression, localization or activity of the shorter product. Native human preparations, recombinant human proteins in insect/bacterial hosts, and yeast/rat/mouse evidence are identified separately.

## Acquisition and validation

The required Falcon research attempt and Perplexity fallback both failed; no provider report was fabricated. The manual synthesis cites inspected original evidence. Whole-gene schema, term and reference validation passed with 18 advisories: 17 concern supported generic interactions retained under campaign policy, and one recommends directly citing the manual synthesis (the source guide is already cited). The computed status is DRAFT because of those advisories; all 151 annotations are reviewed. The HTML review rendered successfully. Two earlier term-check attempts failed before the normal validator wrappers were restored from the fixed runtime version; the subsequent strict check passed. No source cache was changed.

The transcriptional structural activity is represented by GO:0140378 protein complex scaffold activity. Current GO:0030674 explicitly directs integral complex scaffolds to that term; human TFIIH assembly/reconstitution supports XPD holding the core and CAK together. No specific kinase-substrate recruitment role is inferred.
