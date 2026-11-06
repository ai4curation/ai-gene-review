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


## 2026-11-06 taxonomic module audit

Restored both regulation-of-chemotaxis rows to ACCEPT: GO regulation does not require an external pathway component. Retained the motor C-ring association in core locations and clarified that it is transient. GO:0009433 is an anatomical component rather than a member of the protein-containing-complex branch, so the initial proposed move to in_complex was not appropriate. Changed the three acetylation claims to UNDECIDED: self-catalysis would count as work, but the original 2006 full text was not recovered and the catalytic/native contribution remains unresolved. Retained the family-supported rejection of histidine phosphatase over-propagation.

Reviewed all existing rows, references and core functions. Current PAINT-loss checks found no IRD or IKR on this target lineage. A normal Falcon research attempt failed with HTTP 403 authentication; no provider report was fabricated or overwritten. Existing source payloads, raw files and inherited NEW rows are preserved; no new annotation rows were added. Comparative scope was checked against the full text of PMID33684668: the E. coli ligand-response direction and optional adaptation/termination components are not universal.

PMID20398208 full text was read at https://onlinelibrary.wiley.com/doi/full/10.1111/j.1365-2958.2010.07148.x; the normal publication cache remains abstract-only. Its experiments acetylate CheY chemically, and its discussion distinguishes those experiments from the earlier self-acetylation claim. PMID16630631 full text remained inaccessible after normal refetch and publisher attempts. The review therefore makes no definitive catalytic inference from that abstract alone.

### Reassessment of the PAINT histidine-phosphatase claim

GO:0101006 is now UNDECIDED, superseding the earlier REMOVE. Receiving phosphate on Asp57 does not exclude net hydrolysis of a donor phosphohistidine after intrinsic CheY dephosphorylation. PMID2832069 describes CheA dephosphorylation by CheY; PMID7623663 (normally fetched, abstract-only) directly reports intrinsic CheY autohydrolysis. No target-specific loss or PAINT IRD/IKR was found. Removed the categorical plant-only source defect and marked the propagation interpretation unresolved. The family TOO_DEEP judgement has been reported to the module owner for reassessment; family files are outside this agent scope. The response-regulator core remains unchanged.

## PR 6100 round 1 follow-up — 2026-11-06

Items 8 and 15: the three acetylation rows now apply MARK_AS_OVER_ANNOTATED to reported in-vitro self-acetylation of unknown native relevance. The 2006 abstract establishes a reported self-reaction; missing full text limits reassessment of catalytic controls, not acknowledgment of that observation. The 2010 paper chemically modifies CheY as substrate and does not independently show participation. Gene-level actions remain consistent across the two same-term process rows without conflating their experiments. No native acetylation flux or resolved catalytic mechanism is claimed.

The GO:0101006 IBA remains UNDECIDED and the family node UNRESOLVED. E. coli CheY is a motor-directed signal carrier whose Asp-phosphate is hydrolyzed; Sinorhizobium CheY1 is a dedicated phosphate sink. PMID:22194454 states that CheY1 "serves as a sink for surplus phosphoryl groups from CheA-P." That biological asymmetry strengthens the net-reaction framing for CheY1 without establishing a target-specific loss in E. coli. Source-label-only summaries were replaced with biological conclusions.
