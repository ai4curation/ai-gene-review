# G27 putP review notes

## 2026-11-06 source-grounded review

All eleven seeded rows reviewed. Specific sodium/proline symport, membrane location, sodium binding and proline transport are accepted as G27 conserved-function inferences; broad true terms refine to the supported substrate/coupling/location claims. PMID24358297 uses P12/hpp12_0049, native deletion assays, E. coli WG170 expression and purified C-terminal His6-tagged carrier. It does not establish G27 kinetic constants or exact sequence identity. Results permits Li+ substitution in vitro despite abstract sodium-exclusive phrasing; proton coupling is not inferred. No new catabolic, colonization or osmotic-stress process assertion was manufactured from substrate supply or necessity alone.

Source identity is the frozen G27 UniProt record, not the J99 or P12 assay donor. Seeded payloads/order and raw bytes are retained. Root performed a genuine Falcon attempt before delegation; it failed with HTTP403 (logs `.cache/module-audit-logs/puta-20261106/falcon-HELPG-putP.log` and `attempts.yaml`). No report was fabricated or second attempt made. Manual review used the complete cached primaries and the comparative PutA review.

GO0004657 explicitly requires a quinone; GO0003842 explicitly uses NAD+. G27 PutA retains the former at family-inference strength and the latter from catalytic-domain/homolog evidence. No exact quinone species or G27 membrane face is assumed. PutP evidence is kept separate from PutA regulatory/localization conclusions.

PAINT lineage check was run: this G27 accession is absent from the cached family tree, so target-lineage losses could not be evaluated. This is not recorded as evidence of either a loss or its absence. No evolutionary-loss node was invented.


## 2026-11-06 PR #6150 review follow-up

The UniProt FUNCTION quotation now includes L-proline across the source line wrap, rather than ending at L-. This changes quotation completeness, not the documented G27 family inference versus P12 experimental distinction. [file:HELPG/putP/putP-uniprot.txt, CC:FUNCTION; RuleBase:RU366012.]

The scoped action ledger and ontology checks are in `analysis/module_audits/bacterial_fused_puta_proline_catabolism/round1-action-reversal-ledger.yaml` and `round1-review-response.md`. Original annotation rows and source fields are retained in order.
