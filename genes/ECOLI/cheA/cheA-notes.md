# cheA (E. coli K-12, P07363) review notes

## 2026-11-03: initial full review

### Deep research attempts
- `just deep-research ECOLI cheA --provider perplexity` failed: "Provider 'perplexity' not available. Available: falcon, openscientist, claude_code". No deep-research file was written.
- `just mod-description-deep-research ECOLI cheA` was skipped: "no MOD provider configured for organism 'ECOLI'".
- So the review rests on the cached publications, the UniProt record and GO term definitions (local GO via oaklib).

### Publications added to the cache
- PMID:2068106 (McNally & Matsumura 1991, CheA/CheW complex) and PMID:8456299 (Maddock & Shapiro 1993, polar location), both via `just fetch-pmid`. Both are abstract-only.
- PMID:3280143, PMID:2832069 and PMID:1326408 were already cached.

### Key evidence
- Autophosphorylation and phosphotransfer: [PMID:3280143 "We show that in vitro the CheA protein becomes autophosphorylated in the presence of ATP. In addition, the phosphate group on CheA can be rapidly transferred to CheB, a protein involved in adaptation to stimuli, or to CheY, a protein involved in the excitation response."]
- Kinetic preference for cognate response regulators: [PMID:16176121 "At 1 h, CheA shows phosphotransfer to seven response regulators, including CheY and CheB (Figure 4E), but at 10 s we detect only phosphorylation of CheY and CheB (Figure 4F)."] This paper is mostly about Caulobacter, but its full text profiles E. coli CheA.
- Receptor coupling via CheW: [PMID:1326408 "CheW physically links the kinase to the receptor"]. [PMID:1326408 "Such binding greatly modulates the kinase activity of CheA."]
- Polar arrays at the inner membrane: [PMID:8456299 "The transduction of the chemotaxis signal is initiated by a chemoreceptor-CheW-CheA ternary complex at the inner membrane. These ternary complexes aggregate predominantly at the cell poles."]
- CheA(S) binds CheZ: [PMID:19502407 "CheA-short interacts with CheZ to localize CheZ to cell poles."]

### Decisions
- GO:0000155 phosphorelay sensor kinase activity (IBA, IDA, IEA): MODIFY to GO:0004673. In current GO, GO:0000155 is the MORE specific term. It is_a GO:0004673 protein histidine kinase activity and also is_a GO:0140299 molecular sensor activity. Its definition requires the kinase to act "in response to detection of an extracellular signal". CheA does not detect signals itself; chemoreceptors do. The PAINT node PTN000504218 is placed soundly, and only the sensor part of the term is wrong for CheA. I recorded a GO_CENTRAL source_defect (WRONG_TERM, CHECK, SUSPECTED) and a suggested question about the node term.
- The module MF GO:0004673 protein histidine kinase activity is supported. It is the core_functions MF, and both of its GOA rows are ACCEPTed.
- Protein binding: rows with screen data or phosphotransfer substrates are REMOVEd. The CheZ structural rows are MODIFYed to GO:0019903 protein phosphatase binding (CheA(S)-specific). The Tar nanodisc binding row is MODIFYed to GO:0005102 signaling receptor binding.
- Plasma membrane: MODIFY to GO:0009898 cytoplasmic side of plasma membrane, because CheA is a peripheral protein held through the receptors. Cytoplasm is ACCEPTed because no descendant of cytoplasm is better supported.
- NEW: GO:0060187 cell pole, IDA PMID:8456299.
- Swimming motility (GO:0071977): MODIFY to GO:1902021, because swim plates measure chemotaxis and not the ability to swim.
- GO:0031400 (in vitro inhibition of acetylation): MARK_AS_OVER_ANNOTATED.
- GO:0007165 and GO:0035556: MODIFY to GO:0000160.


## 2026-11-06 taxonomic module audit

Refined both cytoplasm rows to cytosol using explicit fractionation of both CheA products in PMID334749; the core array-associated catalytic function is unchanged. Retained the carefully qualified histidine kinase versus direct sensor distinction, CheA-S recruitment function and inherited NEW cell-pole assertion.

Reviewed all existing rows, references and core functions. Current PAINT-loss checks found no IRD or IKR on this target lineage. A normal Falcon research attempt failed with HTTP 403 authentication; no provider report was fabricated or overwritten. Existing source payloads, raw files and inherited NEW rows are preserved; no new annotation rows were added. Comparative scope was checked against the full text of PMID33684668: the E. coli ligand-response direction and optional adaptation/termination components are not universal.

### Coordinated correction of the sensor-kinase interpretation

The current QuickGO GO:0000155 definition requires autophosphorylation in response to signal detection, not direct ligand binding by the kinase. Receptor-controlled CheA fits that definition. The three sensor-kinase rows are therefore ACCEPT, the broad kinase and phosphorus-transferase rows are refined to GO:0000155, and the core uses that more specific MF. Removed the earlier suspected source defect and question based on the unsupported direct-binding requirement. This supersedes the sensor judgement above and agrees with the independently assessed KT2440 CheA review. PMID1326408 directly reports receptor ligand control of kinase activity, complementing the histidine phosphotransfer assays in PMID3280143.
