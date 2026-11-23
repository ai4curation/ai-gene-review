

## 2026-11-06 Bacillus comparative chemotaxis review

Identity: P39802, primary gene cheW, UniProt BACSU, strain 168, taxon 224308. Current primary names were checked explicitly because historical cheA/cheC/cheD aliases can refer to fliZ/fliP/fliY.

The reviewed accession is the strain 168 reference. The receptor and CheD mechanistic studies explicitly use OI1085-derived chemotactic laboratory strains; these are not relabeled as literal strain 168 assays. Conserved gene identity and curated strain 168 records support the functional synthesis, with no claim of a sequence-verified identical assay construct. PMID25313396 instead uses predominantly strain 3610; these experiments are identified as such.

CheW is a noncatalytic coupling protein that coordinates methyl-accepting chemotaxis receptors with the CheA histidine kinase in Bacillus subtilis. It acts on the cytoplasmic side of receptor signaling complexes. CheV can compensate for part of its coupling function, but the phosphorylatable receiver domain of CheV supplies a separate adaptation mechanism.

- [PMID:8169224 Chemotaxis in Bacillus subtilis requires either of two functionally redundant CheW homologs.] Abstract-only cache; detailed claims limited to available evidence unless publisher full access is explicitly recorded.
- [PMID:11553614 Phosphorylation of the response regulator CheV is required for adaptation to attractants during Bacillus subtilis chemotaxis.] Abstract-only cache; detailed claims limited to available evidence unless publisher full access is explicitly recorded.
- [PMID:1601874 Sequence and characterization of Bacillus subtilis CheW.] Abstract-only cache; detailed claims limited to available evidence unless publisher full access is explicitly recorded.
- [PMID:20864474 Site-specific methylation in Bacillus subtilis chemotaxis: effect of covalent modifications to the chemotaxis receptor McpB.] Full cached text available.

The pristine review text, complete original non-review annotation payloads, inherited proposals and raw SHA-256 hashes are recorded in `.cache/module-audit-logs/chemotaxis-20261106/bacillus-baseline.json`. Every machine annotation is preserved. No raw UniProt or GOA file was edited. The normal default Falcon attempt returned HTTP 403 authorization failure; manual notes are used and no provider report was fabricated.

No NEW biological-process annotation was inferred from necessity alone. New proposals, if any, identify missing experimentally grounded molecular activities. PAINT loss checks were run for all genes carrying IBA and found no lineage loss; donor count and target self-inclusion were not used as weaknesses.

Integration refinement: the newly authored adaptor MF is GO:0030159 signaling receptor complex adaptor activity. PMID8169224 and PMID11553614 explicitly place CheW/CheV coupling between chemoreceptors and CheA, meeting the physical-support definition for a receptor signaling complex. This refines the earlier authored GO:0035591 proposal; there was no machine-seeded adaptor MF to modify. CheV receiver adaptation remains a distinct function.


## 2026-11-06 PR6100 round1 scientific follow-up

All pre-edit rows, original actions and source hashes are frozen in `.cache/module-audit-logs/chemotaxis-20261106/round1-bacillus-baseline.json`. No machine annotation payload or inherited authored proposal payload was changed. Every summary in this gene is now claim-specific.

Removed CheV phosphorylation as support for every CheW row/core. The retained IC adaptor proposal integrates genetic redundancy/complementation (PMID8169224), the explicit receptor–CheA coupling statement (PMID11553614) and the experimentally linked frozen UniProt function. The1994 abstract itself labels its detailed coupling model speculative; it is not presented as direct physical-complex purification. UniProt’s target-specific disruption account identifies aspartate and2-deoxyglucose, improving the substrate-taxis evidence.
