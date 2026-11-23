# eutD: Salmonella Typhimurium LT2 evidence notes

2026-11-06 annotation-reviewer curation. Target P41790, taxon99287, is the LT2 reference protein. The pristine27-row four-gene baseline and eight raw hashes were frozen before curation in `.cache/module-audit-logs/ethanolamine-20261106/salmonella/seed-baseline.json`. Every original non-review annotation field is retained.

Default Falcon was attempted normally once for this gene and returned authentication HTTP403. No provider report was created or fabricated; these notes document manual primary-source work.

EutD is a phosphate acetyltransferase of the Salmonella Typhimurium LT2 ethanolamine-utilization system. It reversibly interconverts acetyl-CoA plus inorganic phosphate and acetyl phosphate plus free CoA. In the catabolic direction, this supplies acetyl phosphate to acetate kinase and regenerates CoA for acetaldehyde oxidation. Genetic evidence places its function in the ethanolamine microcompartment and links its physiological importance to compartmentalized cofactor recycling.

- [PMID:14996820] Direct EutD phosphotransacetylase study; HPLC/MS identifies acetyl-CoA in the reverse reaction. Cached abstract only; later full-text26448059 independently tests forward coupling.

- [PMID:26448059] Direct LT2-derived JE6583 recombinant EutQ kinase assays and EutD-coupled chemistry; His6 purification tag was cleaved. Physiological phenotype is conditional on anoxic ethanolamine/tetrathionate growth. Local ATP-consumer coupling is a hypothesis.

- [PMID:23585538] LT2 genetic cofactor-recycling model; not direct purified EutG kinetics. The historical prediction that EutBC lies outside the compartment is superseded by later localization evidence. Cache abstract-only; supporting quotations here are from that cached abstract.

- [PMID:16291677] Condition-dependent Salmonella growth evidence, including reduced-oxygen and glutathione bypass of EutA requirement. Does not demonstrate universal dispensability of compartments or accessory enzymes.

Core synthesis: Reversible phosphate acetyltransferase activity converts acetyl-CoA plus phosphate to acetyl phosphate plus CoA in the catabolic direction, feeding acetate kinase and recycling CoA. Compartment assignment is supported by genetic physiology rather than a direct native EutD localization assay.

Ontology decisions: broad catalytic terms are refined only to supported reaction terms; bacterial microcompartment is refined to the ethanolamine-specific organelle. The broad energy-process claim is retained as distinct physiological context, not falsely treated as an ancestor of the ethanolamine process. No new biological-process term is proposed. Existing ethanolamine-catabolism rows describe enzyme, cofactor-recycling or structural participation, not deletion necessity alone. The added molecular-function proposal, where present, is separately distinguished from all seed rows.

Limits: strain 14028s operon evidence and E. coli purified reactivase evidence are labeled as such. The LT2 protein identity comes from the frozen UniProt record; primary studies are mapped by explicitly named strain and gene/construct, not title alone. No generic protein-binding proposal, unsupported metal-specific EutQ claim, or ATP-folding annotation is added.


Final evidence boundary: LT2 reference;14996820 is the curated direct EutD phosphotransacetylase source.26448059 uses EutD in reversible coupled EutQ/EutP assays. 2004 product confirmation is acetyl-CoA formation in the reverse direction.2016 coupled assays support forward CoA liberation. Compartment localization is physiological inference, not a direct EutD image from41032589.

Verified frozen membership: PTHR43356:SF1. All existing rows remain; added rows: none.
