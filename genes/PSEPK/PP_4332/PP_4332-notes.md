# PP_4332 notes

## Curation session 2026-11-03

Deep research attempts: `just deep-research PSEPK PP_4332 --provider perplexity` failed ("Provider 'perplexity' not available"); `just mod-description-deep-research PSEPK PP_4332` skipped (no MOD provider configured for PSEPK). No provider deep-research file exists for this gene; review based on the UniProt record, cached publications and the project synthesis `projects/P_PUTIDA/deep-research/PSEPK__bacterial_chemotaxis_signal_transduction__ppu02030-deep-research-openscientist.md`.

TrEMBL entry Q88EX0 (PE 4). Single CheW domain; CheW subfamily (IPR039315; PANTHER PTHR22617:SF23). Adjacent paralog PP_4333 (CheW domain protein) unresolved.
- E. coli CheW (P0A964): [PMID:11923283 "Because CheW can bind to CheA and to Tar, it is thought to serve as an adapter protein in this complex."], [PMID:11923283 "mutations which eliminate CheW binding to Tar (V36M) or to CheA (G57D) result in a complete inability to form active ternary complexes"].
- [PMID:21606342 "Bacterial chemoreceptors, histidine kinase CheA, and coupling protein CheW form clusters of chemotaxis signaling complexes."]

Decisions: cytosol ACCEPT; chemotaxis ACCEPT; signal transduction MODIFY -> GO:0000160; NEW GO:0060090 molecular adaptor activity, ISS with UniProtKB:P0A964, ref PMID:11923283 (module MF supported). No KT2440 PP_4332 mutant data in cache.
Gene symbol kept as PP_4332 (UniProt gives no gene name).


## Taxon/module audit, 2026-11-06

PP_4332 is a single CheW-domain protein in the flagellar region. E. coli binding/reconstitution anchors the adaptor mechanism; it is not a KT2440 PP_4332 experiment. Adjacent PP_4333 is another CheW-domain protein and these sources do not establish which adaptor is exclusive or whether both participate. Retain inherited ISS adaptor NEW row, with this uncertainty in core/reason; no new annotation is proposed.

Source anchor: [PMID:11923283 "Because CheW can bind to CheA and to Tar, it is thought to serve as an adapter protein in this complex."]

All existing annotations were reassessed. Machine annotation fields, inherited NEW rows, UniProt/GOA files and provider reports were preserved. No new annotation rows were added; unchanged actions reflect retained biological judgments, not skipped review. Existing provider/manual research was consulted; this focused audit creates no provider-authored report. Current ontology definitions and primary literature take precedence over module completeness.


## 2026-11-06 — receptor-complex adaptor refinement

The inherited authored GO:0060090 NEW proposal is replaced with GO:0030159 signaling receptor complex adaptor activity, matching the independently reviewed E. coli CheW function. The exact original row is archived in analysis/module_audits/bacterial_chemotaxis_signal_transduction/PP_4332-authored-proposal-refinement.yaml. GO:0060090 is absent from frozen GOA, so the refinement cannot be represented as a machine GOA MODIFY row. All machine rows and raw sources are unchanged. This introduces no additional annotation count and does not assert a PP_4332-specific experiment. The E. coli receptor/CheA binding evidence and CheW-family assignment support the narrower inferred role, while adjacent PP_4333 remains an unresolved potential partner.
