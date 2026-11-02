# put1 (SPCC70.03c, UniProt O74524) notes

## Identity and naming
- PomBase symbol put1; UniProt has NO gene name for O74524 (only ORF SPCC70.03c; DR PomBase line shows "-"), so `just fetch-gene SCHPO put1` failed and the entry had to be fetched by accession.
- Probable proline dehydrogenase, mitochondrial (EC 1.5.5.2), ortholog of S. cerevisiae PUT1 (P09368). PANTHER PTHR13914:SF0. [UniProt:O74524 "RecName: Full=Probable proline dehydrogenase, mitochondrial;"]

## Evidence
- Only sequence-based: [UniProt:O74524 "Reaction=L-proline + a quinone = (S)-1-pyrroline-5-carboxylate + a"], FAD cofactor, predicted mitochondrial transit peptide (ECO:0000255).
- No S. pombe experimental data in GOA; no cached publications.
- PomBase GO-CAM 678073a900003902: put1 GO:0004657 in mitochondrial matrix, part of GO:0006562.

## Curation points
- Mitochondrial matrix ISS from PUT1: PRODHs are inner-membrane-associated (ubiquinone acceptor); keep as non-core, same as yeast PUT1 review. Core location: mitochondrion.


## 2026-10-26 systematic arginase-pathway audit

Reviewed every one of the 8 original annotations and all core functions using the review and annotation-reviewer workflows. Machine payloads, row order, evidence codes, qualifiers, source identifiers and WITH/FROM values were preserved. No NEW rows were added.

The PRODH domain, curated reaction/cofactor notes and PAINT support FAD-dependent proline oxidation with a quinone acceptor. Mitochondrial location and matrix ISS are comparative assignments, not new direct S. pombe fractionation. An inferred core location is not automatically peripheral because target-specific experiments are absent. Removed a protein-name quotation, retaining curated functional/location support. The description no longer claims that a budding-yeast-style obligatory proline shuttle has been demonstrated in all fungi or specifically in pombe. No new arginine-catabolism assertion was added.

Normal publication caching passed. Genuine Falcon research with Perplexity-lite fallback was attempted for this gene; authentication/quota errors prevented a report. Manual source review is recorded here, with no fabricated provider-named research file. Abstract-only and bibliographic-only access are distinguished from full text; unknown target supplementary details are not treated as a contradiction. Logs are under `.cache/module-audit-logs/arginase-SCHPO-put1-*`.

The initial focused validation passed. Record sections are backfilled, and final schema/term/reference validation, rendering and helper-history checks are recorded in the same log directory. Actions: ACCEPT 8.
