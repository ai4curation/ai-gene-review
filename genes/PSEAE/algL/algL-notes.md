# algL primary-source review notes

## Review session 2026-10-25

Applied review and annotation-reviewer instructions. Verified current UniProt accession, PAO1 organism (NCBITaxon:208964) and gene symbol before normal `just fetch-gene`. Preserved every source annotation field, including evidence, qualifier, supporting entities and reference; only review decisions were added. No GO-CAM index entry was found for this accession. All PMID quotes refer to the normal publication cache; no cached source, GOA or UniProt file was hand-edited. Abstract-only sources were not treated as complete papers. No unsupported NEW process rows were added.

The actual default-provider attempts `just deep-research-falcon PSEAE algL --fallback perplexity-lite` failed: Edison/Falcon HTTP403 and fallback HTTP401 insufficient quota. These notes record manual primary-source research and are not a provider report. `just fetch-fitness PSEAE algL` could not retrieve a local/remote FEBA result and did not establish an organism mapping/result; no fitness phenotype is claimed. Source and provider attempts were performed alongside publication caching. UniProt family/domain memberships are classification evidence, not DE/GO/ARBA predictions used as proof of chemistry.

AlgL is a periplasmic alginate/mannuronan lyase, not a chain-extension enzyme. PMID23215237 full text demonstrates beta-elimination, preferential non-acetylated substrates and cleavage adjacent to M or G; the poly(beta-D-mannuronate) lyase term does not assert exclusive substrate specificity. Broad lyase terms are refined to this already-present specific activity.

PMID34990713 full text directly examines PAO1-derived inducible production strains, accumulation of periplasmic alginate, viability, purified-enzyme mutants and interactions. AlgL does not detectably associate with the secretion machinery. Its catalytic clearance of mislocalized alginate supports envelope homeostasis. Requirement is conditional: AlgU/T-regulon expression, including the mucA22 background, can compensate. Historical PMID8550492 production phenotypes are retained as real observations but do not establish direct participation in chain biosynthesis; the biosynthesis claim is over-annotated rather than dismissed as wrong-gene evidence. UniProt's older possible secretion-complex interpretation cites PMID16177314 and is qualified by the later direct study.

PMID8370530 is abstract-only in cache, with no full text successfully obtained. Its experimental threonine-deaminase row remains UNDECIDED; no removal based on an abstract foregrounding lyase. This is the sole unresolved row. Specific family support: IPR022859 Alginate_lyase, IPR008397, PF05426 and HAMAP MF_00557; no UniProt PANTHER entry.

## Sources checked

- [PMID:23215237] Functional characterization of AlgL, an alginate lyase from Pseudomonas aeruginosa.: Direct P. aeruginosa catalytic characterization; cleavage is possible adjacent to mannuronate or guluronate, not exclusive mannuronate specificity.
- [PMID:8370530] Sequence of the algL gene of Pseudomonas aeruginosa and purification of its alginate lyase product.: Cached abstract supports lyase and localization; full text was not obtained to adjudicate the unexpected experimental threonine deaminase row. That row remains UNDECIDED.
- [PMID:8550492] Alginate synthesis in Pseudomonas aeruginosa: the role of AlgL (alginate lyase) and AlgX.: Historical genetic necessity is interpreted alongside the direct homeostasis and genetic-background dependence in PMID34990713, not dismissed as a curation error.
- [PMID:34990713] The Pseudomonas aeruginosa homeostasis enzyme AlgL clears the periplasmic space of accumulated alginate during polymer biosynthesis.: Direct PAO1-derived strain work, structural and biochemical assays, accumulation measurements and interaction tests distinguish homeostasis from a stable secretion-complex component.
