# pro3 (SPAPYUG7.05, UniProt Q9P7Y7) notes

## Identity
- PomBase pro3 = pyrroline-5-carboxylate reductase (P5CR, EC 1.5.1.2), ortholog of S. cerevisiae PRO3. [UniProt:Q9P7Y7 "Reaction=L-proline + NADP(+) = (S)-1-pyrroline-5-carboxylate + NADPH +"]
- PANTHER PTHR11645:SF0; InterPro IPR000304.

## Evidence
- No S. pombe-specific enzymology or mutant phenotype in GOA/cached literature; annotations are IBA/IEA plus ORFeome cytosol (HDA, PMID:16823372).
- Indirect S. pombe evidence for P5C reduction to proline from arginine: arginine label enters all proline in an arginase/OAT-dependent manner (PMID:20460254), and pro3 is the only P5CR gene, so this flux must pass through pro3.
- PomBase GO-CAM 678073a900003902: pro3 GO:0004735 in cytosol, part of GO:0055129 L-proline biosynthetic process; no causal edges connect it to car2 or put1.

## Curation points
- All 5 GOA rows correct. Core MF GO:0004735, BP L-proline biosynthetic process, cytosol (as yeast PRO3).
- Not proposing GO:0006527 as NEW: no S. pombe GOA row exists, and the arginine-to-proline flux is covered by the module.


## 2026-10-26 systematic arginase-pathway audit

Reviewed every one of the 5 original annotations and all core functions using the review and annotation-reviewer workflows. Machine payloads, row order, evidence codes, qualifiers, source identifiers and WITH/FROM values were preserved. No NEW rows were added.

Conserved P5CR architecture and PAINT support the catalytic and biosynthetic assignments; the target HDA supports cytosol. NADH/NADPH use is described as curated comparative chemistry rather than a purified S. pombe turnover experiment. Native isotope incorporation into proline supports an upstream arginase/OAT route but does not isolate Pro3 as a measured individual step. No new arginine-catabolism annotation was manufactured from pathway completeness. The description/core explicitly separate direct native labeling from family inference.

Normal publication caching passed. Genuine Falcon research with Perplexity-lite fallback was attempted for this gene; authentication/quota errors prevented a report. Manual source review is recorded here, with no fabricated provider-named research file. Abstract-only and bibliographic-only access are distinguished from full text; unknown target supplementary details are not treated as a contradiction. Logs are under `.cache/module-audit-logs/arginase-SCHPO-pro3-*`.

The initial focused validation passed. Record sections are backfilled, and final schema/term/reference validation, rendering and helper-history checks are recorded in the same log directory. Actions: ACCEPT 5.
