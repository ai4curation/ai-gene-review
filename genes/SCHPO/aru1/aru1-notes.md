# aru1 (SPAC3H1.07, UniProt Q10066) notes

## Identity and naming
- PomBase aru1 = second arginase, 87.9% identical to car1; named car3 in PMID:20435771 [PMID:20435771 "In fission yeast, the open-reading frame car3 + ( SPAC3H1.07 ) encodes a protein that exhibits high homology with arginase Car1 (87.9% identity and 93.5% similarity)."]. Both are budding-yeast CAR1 orthologs (lineage-specific duplication).

## Function
- Car3/aru1 activity constitutive, not iron-regulated; in car1Δ extracts arginase activity remains [PMID:20435771 "As predicted from the constitutive expression of car3 + (Fig. 4D ), Car3 activity assayed in car1Δ cell lysates was not affected by the cellular iron status"]; aru1 appears to be the most expressed/active arginase [PMID:20435771 "since car3 + appeared to be the most expressed and active arginase"].
- SILAC arginine conversion: aru1 is the major arginase [PMID:20460254 "This suggests that Aru1 is the major arginase in fission yeast."]; car1Δ aru1Δ abolishes conversion (PMID:20460254, PMID:26075619).
- Mn2+ cofactor by similarity [UniProt:Q10066].

## Location
- Cytosol and nucleus (ORFeome HDA PMID:16823372); PomBase GO-CAM 678073a900003902 cytosol, part of urea cycle.

## Curation points
- Same treatment as car1: urea cycle (IBA, IEA) MODIFY to L-arginine catabolic process.


## 2026-10-26 systematic arginase-pathway audit

Reviewed every one of the 18 original annotations and all core functions using the review and annotation-reviewer workflows. Machine payloads, row order, evidence codes, qualifiers, source identifiers and WITH/FROM values were preserved. No NEW rows were added.

Aru1 is the SPAC3H1.07 product called Car3 in PMID:20435771. Native enzymatic and isotope studies (PMID:20435771/20460254/26075619) establish a genuine arginase contribution alongside Car1. Its relative dominance and iron-insensitive expression/activity are bounded to tested conditions. Compensatory Car1 induction complicates interpretation of single-mutant activities. Existing urea-cycle terms are retained as contextual network participation, not as a metazoan detoxification claim or a measurement of net cycle flux. No experimental yeast metal stoichiometry is automatically transplanted to this paralog; its Mn assignment is a conserved/curated property.

Normal publication caching passed. Genuine Falcon research with Perplexity-lite fallback was attempted for this gene; authentication/quota errors prevented a report. Manual source review is recorded here, with no fabricated provider-named research file. Abstract-only and bibliographic-only access are distinguished from full text; unknown target supplementary details are not treated as a contradiction. Logs are under `.cache/module-audit-logs/arginase-SCHPO-aru1-*`.

The initial focused validation passed. Record sections are backfilled, and final schema/term/reference validation, rendering and helper-history checks are recorded in the same log directory. Actions: ACCEPT 10, KEEP_AS_NON_CORE 3, MODIFY 5.
