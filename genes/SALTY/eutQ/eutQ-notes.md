# eutQ: Salmonella Typhimurium LT2 evidence notes

2026-11-06 annotation-reviewer curation. Target Q9ZFV5, taxon99287, is the LT2 reference protein. The pristine27-row four-gene baseline and eight raw hashes were frozen before curation in `.cache/module-audit-logs/ethanolamine-20261106/salmonella/seed-baseline.json`. Every original non-review annotation field is retained.

Default Falcon was attempted normally once for this gene and returned authentication HTTP403. No provider report was created or fabricated; these notes document manual primary-source work.

EutQ is a bifunctional component of the Salmonella Typhimurium LT2 ethanolamine microcompartment. Its cupin-like C-terminal domain supports reversible acetate kinase activity, providing ATP from acetyl phosphate and ADP in the catabolic direction. Its N-terminal helices connect shell proteins with encapsulated cargo enzymes and support assembly of the organelle. The N-terminal assembly architecture is distinct from that of shorter Gram-positive EutQ proteins.

- [PMID:26448059] Direct LT2-derived JE6583 recombinant EutQ kinase assays and EutD-coupled chemistry; His6 purification tag was cleaved. Physiological phenotype is conditional on anoxic ethanolamine/tetrathionate growth. Local ATP-consumer coupling is a hypothesis.

- [PMID:27063436] Recombinant Eut-protein assembly in E. coli; distinguished from the later native LT2 localization/assembly experiments.

- [PMID:41032589] Direct LT2 fluorescent localization, scarless deletion, domain mapping and shell/cargo interaction studies. N-terminal assembly role is not transferable without evidence to Gram-positive EutQ lacking the first three helices. ATP delivery to EutA/EutT remains proposed.

Core synthesis: Reversible acetate kinase activity of the LT2 cupin-like C-terminal region generates ATP and acetate from ADP and acetyl phosphate. Direct coupled assays support pathway chemistry; dedicated delivery of this ATP to EutA or EutT remains a hypothesis.

Ontology decisions: broad catalytic terms are refined only to supported reaction terms; bacterial microcompartment is refined to the ethanolamine-specific organelle. The broad energy-process claim is retained as distinct physiological context, not falsely treated as an ancestor of the ethanolamine process. No new biological-process term is proposed. Existing ethanolamine-catabolism rows describe enzyme, cofactor-recycling or structural participation, not deletion necessity alone. The added molecular-function proposal, where present, is separately distinguished from all seed rows.

Limits: strain 14028s operon evidence and E. coli purified reactivase evidence are labeled as such. The LT2 protein identity comes from the frozen UniProt record; primary studies are mapped by explicitly named strain and gene/construct, not title alone. No generic protein-binding proposal, unsupported metal-specific EutQ claim, or ATP-folding annotation is added.


Full-text refinement: PMID27063436 is not confined to its recombinant E. coli title. It also assays native LT2 EutQ deletion strain TT24802. C-terminal His6-tagged EutQ pulls down EutM whereas the N-terminal tag interferes, independently supporting an N-terminal interaction role. The original IPI row is retained.


Final evidence boundary: 26448059 PCR-amplified eutQ from LT2-derived JE6583; pEUT112 carried cleavable N-terminal His6, removed by rTEV.41032589 maps full-length229-aa LT2 EutQ, its1–99 N terminus and100–229 cupin domain.27063436 combines LT2 TT24802 deletion with recombinant E. coli C2566 and tag-orientation-sensitive pull-downs. ATP supply specifically to EutA/EutT is proposed, not demonstrated channeling. EutQ kinase was EDTA-insensitive. Gram-positive homologs lack the first three N-terminal helices, precluding wholesale assembly-role transfer.

Verified frozen membership: PTHR36169:SF1. All existing rows remain; added rows: GO:0140378.
