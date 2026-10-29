# put2 (SPBC24C6.04, UniProt O74766) notes

## Identity and naming
- PomBase symbol put2; UniProt has NO gene name for O74766 (ORF SPBC24C6.04 only), so it had to be fetched by accession.
- Probable P5C dehydrogenase (EC 1.2.1.88), ortholog of S. cerevisiae PUT2 (P07275); PANTHER PTHR42862 (not the human ALDH4A1 family PTHR14516). [UniProt:O74766 "RecName: Full=Probable delta-1-pyrroline-5-carboxylate dehydrogenase;"]

## Evidence
- Only sequence-based: [UniProt:O74766 "Reaction=L-glutamate 5-semialdehyde + NAD(+) + H2O = L-glutamate + NADH"]; pathway step 2/2 of proline degradation to glutamate.
- UniProt gives no subcellular location. The N-terminus (MSQFAEFKLPAIKNEPPKHY...) does not look like a classical amphipathic, Arg-rich presequence, unlike S. cerevisiae PUT2. Mitochondrial matrix rests on the PAINT IBA (from SGD PUT2) and the PomBase GO-CAM (mitochondrial matrix). Worth confirming experimentally.
- PomBase GO-CAM 678073a900003902: put2 GO:0003842 in mitochondrial matrix, part of GO:0006562.

## Curation points
- oxidoreductase activity (InterPro2GO) is uninformative -> MODIFY to GO:0003842.
- The yeast PUT2 review is still a PENDING stub, so no ortholog core_functions to align with.


## 2026-10-26 systematic arginase-pathway audit

Reviewed every one of the 6 original annotations and all core functions using the review and annotation-reviewer workflows. Machine payloads, row order, evidence codes, qualifiers, source identifiers and WITH/FROM values were preserved. No NEW rows were added.

P5CDH/ALDH architecture supports NAD-dependent glutamate-semialdehyde oxidation during proline degradation. Matrix localization is a PAINT assignment whose direct budding-yeast grounding is PMID:3025596; database absence or visual lack of an obvious presequence is not demonstrated loss of targeting. The donor source is explicitly comparative. Removed name-only quotations and outdated review-workflow commentary. The description/core no longer claim a directly demonstrated obligatory arginine shuttle in pombe; target localization and pathway-flux tests remain useful.

Normal publication caching passed. Genuine Falcon research with Perplexity-lite fallback was attempted for this gene; authentication/quota errors prevented a report. Manual source review is recorded here, with no fabricated provider-named research file. Abstract-only and bibliographic-only access are distinguished from full text; unknown target supplementary details are not treated as a contradiction. Logs are under `.cache/module-audit-logs/arginase-SCHPO-put2-*`.

The initial focused validation passed. Record sections are backfilled, and final schema/term/reference validation, rendering and helper-history checks are recorded in the same log directory. Actions: ACCEPT 5, MODIFY 1.

The local ontology cache may warn on the older GO:0003842 label without NAD+. Live QuickGO was checked and confirms the preserved current NAD+-specific label; raw annotation IDs/labels were not rewritten to silence the stale cache.
