# PP_4332 notes

## Curation session 2026-11-03

Deep research attempts: `just deep-research PSEPK PP_4332 --provider perplexity` failed ("Provider 'perplexity' not available"); `just mod-description-deep-research PSEPK PP_4332` skipped (no MOD provider configured for PSEPK). No provider deep-research file exists for this gene; review based on the UniProt record, cached publications and the project synthesis `projects/P_PUTIDA/deep-research/PSEPK__bacterial_chemotaxis_signal_transduction__ppu02030-deep-research-openscientist.md`.

TrEMBL entry Q88EX0 (PE 4). Single CheW domain; CheW subfamily (IPR039315; PANTHER PTHR22617:SF23). Adjacent paralog PP_4333 (CheW domain protein) unresolved.
- E. coli CheW (P0A964): [PMID:11923283 "Because CheW can bind to CheA and to Tar, it is thought to serve as an adapter protein in this complex."], [PMID:11923283 "mutations which eliminate CheW binding to Tar (V36M) or to CheA (G57D) result in a complete inability to form active ternary complexes"].
- [PMID:21606342 "Bacterial chemoreceptors, histidine kinase CheA, and coupling protein CheW form clusters of chemotaxis signaling complexes."]

Decisions: cytosol ACCEPT; chemotaxis ACCEPT; signal transduction MODIFY -> GO:0000160; NEW GO:0060090 molecular adaptor activity, ISS with UniProtKB:P0A964, ref PMID:11923283 (module MF supported). No KT2440 PP_4332 mutant data in cache.
Gene symbol kept as PP_4332 (UniProt gives no gene name).
