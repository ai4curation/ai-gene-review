# eutA: Salmonella Typhimurium LT2 evidence notes

2026-11-06 annotation-reviewer curation. Target Q9ZFV2, taxon99287, is the LT2 reference protein. The pristine27-row four-gene baseline and eight raw hashes were frozen before curation in `.cache/module-audit-logs/ethanolamine-20261106/salmonella/seed-baseline.json`. Every original non-review annotation field is retained.

Default Falcon was attempted normally once for this gene and returned authentication HTTP403. No provider report was created or fabricated; these notes document manual primary-source work.

EutA is the ethanolamine ammonia-lyase reactivase of Salmonella Typhimurium LT2. It associates with the cognate EutBC enzyme and is assigned ATP-dependent exchange of damaged or inactive bound cobalamin for intact adenosylcobalamin, restoring lyase activity after inactivation. EutA associates with ethanolamine microcompartments. Its physiological requirement depends on conditions that affect lyase inactivation and can be bypassed under particular growth conditions.

- [PMID:35785499] LT2 localization, cognate EutA/EutBC complementation, copurification and crosslinking. Immunogold establishes association; lumen placement is inferred. Aggregation prevented strong enzymatic/kinetic analysis.

- [PMID:15466038] Purified E. coli EutA cofactor-exchange reactivation, not a direct SALTY assay. Used as explicit homolog evidence together with LT2 primary interaction and genetic studies. Cached abstract only.

- [PMID:16291677] Condition-dependent Salmonella growth evidence, including reduced-oxygen and glutathione bypass of EutA requirement. Does not demonstrate universal dispensability of compartments or accessory enzymes.

Core synthesis: Reactivates cognate ethanolamine ammonia-lyase by ATP-dependent exchange of inactive bound cobalamin for intact adenosylcobalamin. E. coli biochemistry supports this mechanistic assignment to LT2, whose EutA directly associates with EutBC and Eut metabolosomes. Reactivation is needed after inactivation, not after every catalytic turnover.

Ontology decisions: broad catalytic terms are refined only to supported reaction terms; bacterial microcompartment is refined to the ethanolamine-specific organelle. The broad energy-process claim is retained as distinct physiological context, not falsely treated as an ancestor of the ethanolamine process. No new biological-process term is proposed. Existing ethanolamine-catabolism rows describe enzyme, cofactor-recycling or structural participation, not deletion necessity alone. The added molecular-function proposal, where present, is separately distinguished from all seed rows.

Limits: strain 14028s operon evidence and E. coli purified reactivase evidence are labeled as such. The LT2 protein identity comes from the frozen UniProt record; primary studies are mapped by explicitly named strain and gene/construct, not title alone. No generic protein-binding proposal, unsupported metal-specific EutQ claim, or ATP-folding annotation is added.


Construct boundary: PMID35785499 calls SeEutA 468 amino acids, while the frozen Q9ZFV2 sequence has 467. Its crosslinked peptides YEFIKR at 39–44 and QGGLKEVELK at 60–69 match exactly. LT2/JE6583 plus these sequence anchors support gene identity, but the one-residue length/terminal-construct discrepancy remains unresolved; no start-site correction or residue insertion is inferred.


Final evidence boundary: LT2/JE6583 in35785499; current467-aa sequence exactly matches reported crosslinked peptides39–44 YEFIKR and60–69 QGGLKEVELK. Paper prose gives468 aa, leaving a one-residue construct-length discrepancy.15466038 is purified E. coli EutA, not SALTY. LT2 binding/localization and cognate complementation support homolog transfer of reactivation chemistry. Lumen placement is inferred. Aggregation limited LT2 enzyme kinetics; no exact whole-construct identity or autonomous ATP-folding is asserted. EutA is conditional after lyase inactivation, not mandatory for every turnover.

Verified frozen membership: PTHR32432:SF13. All existing rows remain; added rows: GO:0008047.
