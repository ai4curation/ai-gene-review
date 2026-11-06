# fliF curation notes

- Q88ET4 is the KT2440 integral-membrane FliF family protein that forms the flagellar MS ring. [file:PSEPK/fliF/fliF-uniprot.txt, "The M ring is integral to the inner membrane of the cell"]
- Native *Salmonella* structural work establishes that the FliF MS ring is the motor core and an assembly template; this supports conserved structural molecule activity but does not directly establish KT2440 ring stoichiometry. [PMID:34244518, "The bacterial flagellar MS ring is a transmembrane complex acting as the core of the flagellar motor and template for flagellar assembly."]
- KT2440 work shows that FlhF targets early flagellar components to the pole, providing species-level context for MS-ring positioning without directly assaying FliF. [PMID:39709681, "FlhF determines the polar position of the flagella by targeting early flagellar components to the cell pole"]
- The OpenScientist report found no direct KT2440 `fliF` knockout or native basal-body structure, so detailed mechanistic claims remain orthology-based. [file:PSEPK/fliF/fliF-deep-research-openscientist.md]
- The review uses `contributes_to` for proton motive force-driven motor activity because FliF is a structural rotor subunit, not an independently active motor.


## 2026-11-06 comparative flagellar audit

Reviewed every existing annotation and the biological summary/core functions. Original annotation payloads, including historical NEW proposals, are preserved. Family/domain evidence supports conserved structural assignments; comparative Salmonella or other bacterial assays are not presented as KT2440 experiments. Exact subunit counts and interaction geometries are not transferred as target measurements.

GO:0003774 explicitly includes electrochemical-gradient-driven flagellar rotation. Rotor/switch structural roles are distinguished from autonomous torque generation. The C-ring/MS-ring CC terms were verified against ontology ancestry and remain valid substructure locations.

The available genuine provider report was consulted. Primary/comparative evidence and target family membership now support row decisions directly; the resulting advisory that no row cites the provider is accepted rather than adding a weaker citation solely to suppress it.


## 2026-11-06 PR6138 round-1 clarification

Confirmed through the official QuickGO API that GO0140605 is an is_a descendant of GO0003774 and that the latter definition explicitly includes flagellar rotation and electrochemical proton-gradient energy. Retained the motor refinement and clarified MS-ring structural contribution and comparative evidence; the obsolete wrong-kind-of-motor rationale was not restored.

Ontology definitions and ancestor URLs, primary-source scope and reviewer disagreements are recorded in `analysis/module_audits/bacterial_flagellar_assembly_export/round1-consultation.md`.
