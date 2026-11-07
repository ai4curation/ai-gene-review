# cheY (E. coli K-12, P0AE67) review notes

## 2026-11-03 session

### Setup / provenance
- `just fetch-gene-pmids ECOLI cheY`: all 30 GOA PMIDs cached (PMID:6089173 newly fetched).
- `just deep-research ECOLI cheY --provider perplexity` failed: "Provider 'perplexity' not available. Available: falcon, openscientist, claude_code" (no API keys). No deep-research file exists; review is based on the cached publications and the UniProt record.
- `just mod-description-deep-research ECOLI cheY`: skipped, "no MOD provider configured for organism 'ECOLI'".
- `just paint-losses ECOLI cheY`: "No IRD or IKR loss on this gene's lineage."
- Full text cached only for PMID:16176121, PMID:20161720, PMID:21496648, PMID:29184123; others abstract-only.

### Key evidence
- Phosphotransfer from CheA: [PMID:3280143 "the phosphate group on CheA can be rapidly transferred to CheB, a protein involved in adaptation to stimuli, or to CheY, a protein involved in the excitation response."]
- Asp57 phosphoacceptor: [PMID:2404281 "consistent with the hypothesis that Asp-57 is the normal site of acyl phosphate formation."]
- Specific kinetic preference of CheA: [PMID:16176121 "at 10 s we detect only phosphorylation of CheY and CheB (Figure 4F)."]
- Output at FliM: [PMID:8415608 "the primary docking site is FliM, that the extent of CheY binding to FliM is dependent upon the phosphorylation level of CheY"]
- Phosphorylation boosts motor activity >100x: [PMID:1737035 "this activity is increased by at least 2 orders of magnitude by phosphorylation."]
- Loss of function: [PMID:353036 "Mutants defective in cheA, cheW, cheX, or cheY function swam smoothly, with little or no tumbling"]
- Autoacetylation: [PMID:16630631 "we demonstrated that one of these means is autoacetylation, with AcCoA serving as an acetyl donor and with a rate similar to that of Acs-mediated acetylation."]

### Decisions (48 rows)
- GO:0000156 phosphorelay response regulator activity (IBA + 3 IDA): ACCEPT; the module MF for CheY is supported and is the core MF in both core_functions.
- GO:0000160 (IBA, IDA, IEA): ACCEPT. GO:0006935 chemotaxis (2 IMP, NAS): ACCEPT. GO:1902021 (6 rows): ACCEPT.
- GO:0005515 protein binding (13 IPI): CheZ partner rows (4) REMOVE: CheY-P is the phosphatase's substrate, the activity belongs to CheZ. Y2H benchmark (PMID:19834901) REMOVE. CheA docking rows (7578071, 9437425, 9636149, 21642453) MODIFY to GO:0043424 protein histidine kinase binding. Phosphotransfer rows (16176121, 20161720 xeno CheA3) and FliM rows (12232047, 8415608) MODIFY to GO:0000156.
- Cytoplasm (IDA, IEA): MODIFY to cytosol (GO:0005829, carried by IBA + IDA fractionation, both ACCEPT).
- Signal transduction (IDA): TOO_GENERAL (GO:0000160 accepted).
- Flagellum (NAS): MODIFY to C ring; C ring and rotor complex: KEEP_AS_NON_CORE (CheY-P is a dynamic visitor of the switch).
- Regulation of chemotaxis (2): MODIFY to chemotaxis (CheY is part of the pathway, not a modulator of it).
- Swimming motility (2): MODIFY to GO:1902021 (cheY mutants still swim).
- Aerotaxis, thermotaxis: KEEP_AS_NON_CORE. Mg2+ binding: KEEP_AS_NON_CORE (cofactor).
- Acetyltransferase activity + internal peptidyl-lysine acetylation (2): MARK_AS_OVER_ANNOTATED (self-modification of unclear in vivo relevance; the IMP row from PMID:20398208 has CheY only as the substrate).
- GO:0101006 protein histidine phosphatase activity (IBA): REMOVE. PTN001981629 has ARR22 (AT3G04280) as its only donor; CheY is an Asp phosphoacceptor. Recorded a source_defect (GO_CENTRAL, CHECK) and a propagation_review. This agrees with the orchestrator's family-review judgement that the term is placed too deep.

### Consistency with genes/PSEPK/cheY
- Both reviews ACCEPT GO:0000160 and use GO:0000156 plus chemotaxis as the core. PSEPK has no cytosol row and so ACCEPTs cytoplasm. Here a supported cytosol row exists, so cytoplasm is MODIFIED to cytosol, following the brief.
