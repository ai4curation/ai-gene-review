

## 2026-11-06 Bacillus comparative chemotaxis review

Identity: P24072, primary gene cheY, UniProt BACSU, strain 168, taxon 224308. Current primary names were checked explicitly because historical cheA/cheC/cheD aliases can refer to fliZ/fliP/fliY.

The reviewed accession is the strain 168 reference. The receptor and CheD mechanistic studies explicitly use OI1085-derived chemotactic laboratory strains; these are not relabeled as literal strain 168 assays. Conserved gene identity and curated strain 168 records support the functional synthesis, with no claim of a sequence-verified identical assay construct. PMID25313396 instead uses predominantly strain 3610; these experiments are identified as such.

CheY is the soluble response regulator connecting the Bacillus subtilis chemotaxis kinase CheA to the flagellar switch. Phosphorylation at Asp54 promotes switch interactions and counterclockwise rotation associated with smooth swimming. CheY-P also contributes to CheC-CheD feedback at receptors and is dephosphorylated by the native phosphatases FliY and CheC. Its response to attractant differs in sign from that of Escherichia coli CheY.

- [PMID:8369293 Purification and characterization of Bacillus subtilis CheY.] Abstract-only cache; detailed claims limited to available evidence unless publisher full access is explicitly recorded.
- [PMID:12920116 Bacillus subtilis hydrolyzes CheY-P at the location of its action, the flagellar switch.] Abstract-only cache; detailed claims limited to available evidence unless publisher full access is explicitly recorded.
- [PMID:12094812 Activation of the CheA kinase by asparagine in Bacillus subtilis chemotaxis.] Abstract-only cache; detailed claims limited to available evidence unless publisher full access is explicitly recorded.
- [PMID:25313396 FlgM is secreted by the flagellar export apparatus in Bacillus subtilis.] Abstract-only cache; detailed claims limited to available evidence unless publisher full access is explicitly recorded.

The pristine review text, complete original non-review annotation payloads, inherited proposals and raw SHA-256 hashes are recorded in `.cache/module-audit-logs/chemotaxis-20261106/bacillus-baseline.json`. Every machine annotation is preserved. No raw UniProt or GOA file was edited. The normal default Falcon attempt returned HTTP 403 authorization failure; manual notes are used and no provider report was fabricated.

No NEW biological-process annotation was inferred from necessity alone. New proposals, if any, identify missing experimentally grounded molecular activities. PAINT loss checks were run for all genes carrying IBA and found no lineage loss; donor count and target self-inclusion were not used as weaknesses.

GO:0101006 remains UNDECIDED: PTHR43228 root PTN001981629 carries the assertion from ARR22; there is no lineage IRD/IKR. Receiver phosphotransfer plus hydrolysis may remove histidine phosphate indirectly, so the familiar receiver mechanism does not establish a loss. A catalytic-turnover assay and the intended GO convention are needed.


## 2026-11-07 — PR #6100 review 5812414716, C2

The question whether net phosphate drainage through the CheY receiver cycle warrants GO:0101006 is a curation/ontology convention question, not a wet-lab knowledge gap. It remains unresolved alongside the unchanged UNDECIDED row and PAINT assessment; no source defect or activity loss is asserted. The former CURATION/ONTOLOGY-only knowledge_gaps entry has therefore moved here. Its assay component is retained separately as a suggested experiment: quantify CheA-P transfer, CheY-P decay and phosphate release under multiple-turnover conditions. Such kinetics can establish reaction behavior but do not alone decide GO convention. The full old entry is archived in the additive follow-up before.json.

Original convention question: Whether Bacillus CheY should carry protein histidine phosphatase activity for net phosphate drainage through its receiver cycle remains unresolved.
