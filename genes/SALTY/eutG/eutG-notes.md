# eutG: Salmonella Typhimurium LT2 evidence notes

2026-11-06 annotation-reviewer curation. Target P41795, taxon99287, is the LT2 reference protein. The pristine27-row four-gene baseline and eight raw hashes were frozen before curation in `.cache/module-audit-logs/ethanolamine-20261106/salmonella/seed-baseline.json`. Every original non-review annotation field is retained.

Default Falcon was attempted normally once for this gene and returned authentication HTTP403. No provider report was created or fabricated; these notes document manual primary-source work.

EutG is an iron-family alcohol dehydrogenase associated with the ethanolamine microcompartment of Salmonella Typhimurium LT2. It is assigned the reduction of acetaldehyde to ethanol with oxidation of NADH, providing a route for NAD+ recycling during ethanolamine catabolism. This catalytic assignment is supported by enzyme-family conservation and physiological evidence; purified LT2 substrate/cofactor kinetics have not been established in the sources examined. Its requirement for growth depends on medium and compartment integrity.

- [PMID:23585538] LT2 genetic cofactor-recycling model; not direct purified EutG kinetics. The historical prediction that EutBC lies outside the compartment is superseded by later localization evidence. Cache abstract-only; supporting quotations here are from that cached abstract.

- [PMID:41032589] Direct LT2 fluorescent localization, scarless deletion, domain mapping and shell/cargo interaction studies. N-terminal assembly role is not transferable without evidence to Gram-positive EutQ lacking the first three helices. ATP delivery to EutA/EutT remains proposed.

- [PMID:7868611] Operon study of strain 14028s, not an exact LT2 assay. EutG alcohol-dehydrogenase assignment derives from sequence comparison and genetics rather than purified reaction kinetics.

- [PMID:16291677] Condition-dependent Salmonella growth evidence, including reduced-oxygen and glutathione bypass of EutA requirement. Does not demonstrate universal dispensability of compartments or accessory enzymes.

Core synthesis: Inferred NAD-dependent acetaldehyde reduction to ethanol regenerates NAD+ in the LT2 ethanolamine compartment. The family-supported reaction is reversible; physiological direction and cofactor recycling are supported by genetics, whereas purified target kinetics remain unresolved.

Ontology decisions: broad catalytic terms are refined only to supported reaction terms; bacterial microcompartment is refined to the ethanolamine-specific organelle. The broad energy-process claim is retained as distinct physiological context, not falsely treated as an ancestor of the ethanolamine process. No new biological-process term is proposed. Existing ethanolamine-catabolism rows describe enzyme, cofactor-recycling or structural participation, not deletion necessity alone. The added molecular-function proposal, where present, is separately distinguished from all seed rows.

Limits: strain 14028s operon evidence and E. coli purified reactivase evidence are labeled as such. The LT2 protein identity comes from the frozen UniProt record; primary studies are mapped by explicitly named strain and gene/construct, not title alone. No generic protein-binding proposal, unsupported metal-specific EutQ claim, or ATP-folding annotation is added.


Final evidence boundary: LT2 reference; PMID7868611 is strain 14028s comparative sequence/genetics, whereas23585538 is LT2 physiology and41032589 uses LT2 fluorescent cargo fusions. No purified LT2 EutG kinetics, metal preference, or measured native flux partition established. Compartmental NAD recycling remains a genetically supported physiological model; modern imaging confirms cargo localization.

Verified frozen membership: PTHR11496:SF94. All existing rows remain; added rows: none.
