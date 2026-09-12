# Phase-1 review — consolidated recommended edits (auto-extracted)

Generated from the per-gene section files in `_sections/`. Tags: **[YAML]** gene-review change · **[MAP]** PN mapping/projection · **[WB]** upstream PN workbook · **[REF]** reference hygiene. Nothing here was applied automatically — staged for curator adjudication.

- genes with **[YAML]** recommendations: **65**
- genes with **[MAP]** recommendations: **148**
- genes with **[REF]** recommendations: **39**
- genes with **[WB]** recommendations: **3**

## Genes with gene-review (YAML) change recommendations

`ATP6V0A1`, `AZI2`, `BCL2L13`, `BNIP3L`, `CALCOCO1`, `CALR3`, `CAND1`, `CCDC47`, `CHIC2`, `CLCN7`, `CLGN`, `CNOT4`, `CSNK1D`, `DCAF10`, `DDA1`, `DDB2`, `DNAJC6`, `DTL`, `EIF5A`, `FAF2`, `FBXL8`, `FBXO16`, `FBXO27`, `FBXO47`, `FBXO8`, `FBXW5`, `GIGYF1`, `GLMN`, `GTPBP2`, `GTPBP6`, `LRSAM1`, `MAP1S`, `MEFV`, `NAA30`, `NAA35`, `NAA38`, `NAA40`, `NBR1`, `NEMF`, `NLRX1`, `NPLOC4`, `NUFIP1`, `P4HA3`, `PPIB`, `RACK1`, `RETREG2`, `RNF166`, `RNF170`, `RNF185`, `RNF41`, `RNF5`, `SEC62`, `SEC63`, `SERPINH1`, `SIAH1`, `STIP1`, `STUB1`, `TCF25`, `TRIM13`, `TRIM16`, `TRIM17`, `TRIM5`, `TXNDC11`, `TXNDC16`, `UBAC2`

## Per-gene tagged recommendations

### AATF
- Verdict:** Subunit contradiction — PN over-reaches (LSU projection on an SSU factor); review correctly rejects pre-60S. **Recommended edits:** [MAP] Do not project GO:0030687 to AATF; re-bucket AATF under an SSU-processome/pre-40S PN node or suppress the pre-60S type mapping for this gene.

### ABCF2
- Verdict:** Consistent (review conservatively rejects the PN RQC projection). **Recommended edits:** [REF] Reconcile UniProt accession — PN dossier/workbook uses A0A090N7X1 but the canonical reviewed entry and review YAML use Q9UG63; update the PN workbook to Q9UG63. [MAP] Keep GO:0006515 non-propagating for ABCF2.

### ABRAXAS2
- Verdict:** Consistent on BRISC; PN DNA-repair projection over-reaches and is correctly declined; review's p53-DDR/IFN NEW terms are sound. **Recommended edits:** [MAP] Do not project GO:0006281 DNA repair to ABRAXAS2; the supported DNA-damage role is GO:0043517 (p53-class DDR signaling), already added in the review.

### ABTB1
- Verdict:** Consistent; PN substrate-adaptor activity correctly held back (no substrate), review adds verified CRL3 complex + cullin-binding terms. **Recommended edits:** [MAP] Keep GO:1990756 non-propagating for ABTB1 pending substrate evidence (review's GO:0031463/GO:0097602 are the correct landing terms). Optional [REF]: consider adding PMID:15071497 / PMID:23912815 (PN-cited Cul3 reviews) to the review references for completeness.

### ABTB3
- Verdict:** PN Cul3-adaptor projection over-reaches (domain-only, contradicted by synaptic-function evidence); review correctly rejects GO:1990756. **Recommended edits:** [MAP] Suppress GO:1990756 projection for ABTB3 (no CUL3/CRL3/substrate evidence); retain the group mapping for genes with direct support (e.g. ABTB2).

### ADRB2
- Verdict:** PN direct-lipophagy projection over-reaches; review correctly retains positive-regulation-of-lipophagy and declines GO:0061724 (RAB7 is the direct factor). **Recommended edits:** [MAP] Keep ADRB2 mapping at GO:1904504 positive regulation of lipophagy; do not propagate direct GO:0061724 lipophagy.

### AFG3L2
- Verdict:** Consistent; PN GO:0035694 correctly adopted as NEW; PN matrix (GO:0005759) projection correctly overruled at gene level. **Recommended edits:** none required. Optional [MAP]: flag mitochondrial-proteostasis "Matrix protease" group GO:0005759 as too specific for inner-membrane matrix-facing proteases (consider GO:0005743 or no_mapping).

### AGK
- Verdict:** Consistent; PN TIM22 (GO:0042721) adopted; PN class GO:0015031 protein transport too broad — review's GO:0045039 is the correct narrower call. **Recommended edits:** none required. Optional [MAP]: confirm class-level GO:0015031 stays gene-gated in favor of compartment-specific insertion/import terms.

### AGR2
- Verdict:** Consistent; PN GO:0003756 projection validated and added via MODIFY; only nuance is the pseudo-PDI catalysis debate (review mitigates via mixed-disulfide evidence). **Recommended edits:** none required; [REF] optionally note in review that AGR2 is a non-canonical CXXS PDI-family member (catalytic isomerase activity debated) to pre-empt over-reading GO:0003756.

### AGR3
- Verdict:** PN PDI projection (GO:0003756) over-reaches for AGR3; correctly overruled — best-supported role is Ca-dependent ciliary beat regulation. **Recommended edits:** none to YAML. [MAP]: flag ER-proteostasis "Protein disulfide isomerases" group GO:0003756 as requiring gene-level catalytic gating; AGR3 (DCYQS, no CXXC) should be excluded/`no_mapping`.

### AHCTF1
- Verdict:** Consistent; PN nuclear pore (GO:0005643) adopted; PN class GO:0015031 protein transport over-reaches for an NPC-assembly factor — review's GO:0051292 + GO:0003682 are the correct calls. **Recommended edits:** none required. [MAP]: flag class-level GO:0015031 for the Nuclear proteostasis|Protein transport node as too broad for structural NPC-assembly factors; consider gene-gating. [WB]: optionally reconsider AHCTF1's inclusion in the PN source list (assembly factor, weak proteostasis link).

### AHR
- Verdict:** PN UPS/CUL4-adaptor projection (GO:1990756) over-reaches; correctly NOT propagated to AHR (left as open question). Core TF/nuclear-receptor function fully captured. **Recommended edits:** none to YAML. [MAP]: keep AHR/ARNT/TBL3 and PAS subtypes `no_mapping`; gate the Cul4A/Cul4B substrate-adaptor group GO:1990756 behind per-gene review (AHR is the cautionary case). [REF]: optionally fetch/verify PN PMID:17392787 & 28416634 to substantiate or retire the AHR UPS placement.

### AIP
- Verdict:** Consistent; PN PPIase (GO:0003755) projection correctly overruled with direct biochemical evidence; cochaperone role captured more specifically as GO:0051879. **Recommended edits:** none required. Optional [MAP]: note FKBP-type PPIase group GO:0003755 over-projects to catalytically-dead members (AIP); flag for gene-level gating.

### AIPL1
- Recommended edits:** [MAP] Flag GO:0003755 PPIase as a known false-positive for AIPL1 in the PPIase group/type mapping notes (gene-level exclusion), so the FKBP-type propagation does not re-assert PPIase activity on AIPL1.

### AIRE
- Recommended edits:** [MAP] Mark AIRE (and other PHD-"other" members) as a gene-level exception to the RING-variant→GO:0061630 propagation, or downgrade that subtree to context_only, since PHD-reader members are not demonstrated catalytic E3s. [REF] Adjudicate PMID:14734522 and PMID:15150263 (the PN E3 references) — fetch full text and record a reference_review before any E3 verdict.

### AKIRIN1
- Recommended edits:** [MAP] Split the `adaptors|Akirin` type so GO:0070628 proteasome binding propagates to AKIRIN2 only; mark AKIRIN1 as no_mapping (nuclear transcription cofactor, no proteasome-binding evidence).

### AMBRA1
- Recommended edits:** [MAP] Downgrade the CMA-enhancer *type*→GO:1904716 to context_only (or mark AMBRA1 a gene-level exclusion) so positive-CMA is not auto-projected without LAMP2A/HSPA8 substrate-uptake evidence, consistent with the review's withholding.

### ANKFY1
- Recommended edits:** none to ANKFY1-ai-review.yaml. [MAP] exclude ANKFY1 from the Cul3-substrate-receptor GO:1990756 projection (no CUL3/adaptor evidence; function is Rab5/PI3P endosomal + ATG2A autophagy). Consider re-homing ANKFY1's proteostasis placement to ALP.

### ANKZF1
- Recommended edits:** none to ANKZF1-ai-review.yaml. [MAP] do not propagate GO:0035694 from the mito "Organelle-specific protein degradation" class to ANKZF1 (Vms-pathway leaf is no_mapping; gene-level evidence is RQC/stress-translocation, not mito proteolysis).

### ARF1
- Recommended edits:** none to ARF1-ai-review.yaml. [MAP] flag PN "COPI coating and uncoating" subtype to not project GO:0030126 (CC membership) to regulatory GTPases such as ARF1; restrict to coatomer subunits.

### ARL8A
- Recommended edits:** none to ARL8A-ai-review.yaml. [MAP] do not propagate GO:0061906 to ARL8A from the autophagosome-localization leaf until direct ARL8A-dependent autophagosome positioning is shown; ARL8A's shared target is lysosome localization.

### ARL8B
- Recommended edits:** none to ARL8B-ai-review.yaml (it already flags both issues). [MAP] do not propagate GO:0061906 to ARL8B (autophagy role captured by GO:0061909). [REF] PN/curators: correct GO:0007059 origin reference PMID:14871887 → PMID:15331635 (GIE/ARL8 study).

### ARNT
- Verdict:** PN UPS adaptor projection over-reaches and is correctly rejected in-review. **Recommended edits:** exempt ARNT from GO:1990756 group propagation at the mapping layer [MAP].

### ATP23
- Verdict:** MOSTLY CONSISTENT — IMS location good; class-level *catabolic* projection mis-flavored for an assembly/processing peptidase. **Recommended edits:** [MAP] mark GO:0035694 class projection as not_for_propagation to ATP23 (gene is processing/assembly, not catabolism); review's GO:0034982 is the correct process term.

### ATP6V0A1
- Recommended edits:** [YAML] Consider aligning the GO:0046610 NEW-row evidence code between ATP6V0A1 (IC) and ATP6V0C (TAS) for consistency across the V0 PN refinements (low priority; both are defensible).

### ATP6V0A4
- Verdict:** PN LYSOSOMAL PROJECTION OVER-REACHES for a4 (renal-apical, not lysosomal); review correctly declined. **Recommended edits:** [MAP] flag GO:0046610 + GO:0007042 leaf/type projections as not_for_propagation to ATP6V0A4 (no a4-specific lysosomal evidence; isoform is apical-PM targeted); keep GO:0033179 (V0 domain, already in GOA).

### ATP6V1A
- Verdict:** Consistent / ADD GO:0046612 (verified) as more-specific CC; no contradictions. **Recommended edits:** [MAP] align subtype complex target GO:0033176 → GO:0046611 (lysosomal V-ATPase complex, already ACCEPTed in review) for specificity.

### ATP6V1B1
- Mapping strategy:** The shared V-ATPase node maps to lysosomal terms generically, but B1 is a tissue-restricted plasma-membrane isoform — analogous to the TOMM20/HSPA8/RAB7A "too broad" precedent. **[MAP]** flag B1 as an exception to lysosomal projection (scope=too_broad/wrong_compartment for this isoform); the generic vacuolar V1 term (GO:0000221, already in review) is the safe target.
- Verdict:** OVER-REACH — PN lysosomal projection (GO:0046612/GO:0007042) is wrong-compartment for this apical-plasma-membrane kidney isoform. **Recommended edits:** [MAP] exempt ATP6V1B1 from lysosomal-acidification/lysosomal-V1 projection; restrict to vacuolar V1 domain + plasma-membrane/renal acid-secretion terms already in the review.

### ATP6V1D
- Verdict:** Consistent / ADD GO:0046612 (verified) as more-specific CC; review exceeds PN scope (cilia) without conflict. **Recommended edits:** [MAP] align subtype complex target GO:0033176 → GO:0046611 (lysosomal V-ATPase complex, already ACCEPTed for D).

### ATP6V1E1
- Verdict:** Consistent / ADD GO:0007042 + GO:0046612 (verified, new to E1 GOA); review also makes an unrelated REMOVE for a mis-attributed citation. **Recommended edits:** [MAP] consider subtype complex GO:0033176 → GO:0046611 (already ACCEPTed for E1) for specificity.

### ATP6V1E2
- Mapping strategy:** Like B1/G3, E2 is a tissue-restricted isoform whose specialized compartment is not the lysosome (TOMM20/HSPA8/RAB7A "too broad" precedent applies). **[MAP]** flag E2 as an exception to lysosomal projection; safe target is the generic catalytic/V1 complex term (GO:0033178, already in review). Acrosome remains non-core/IEA.
- Verdict:** OVER-REACH — PN lysosomal projection wrong-compartment for this testis/acrosome isoform (and acrosome itself is IEA-only). **Recommended edits:** [MAP] exempt ATP6V1E2 from lysosomal-acidification/lysosomal-V1 projection; restrict to vacuolar/catalytic V1 complex terms; keep acrosome as non-core.

### ATP6V1G2
- Mapping strategy:** Tissue-restricted neuronal isoform; lysosomal projection is over-broad (TOMM20/HSPA8/RAB7A precedent). **[MAP]** flag G2 as an exception — its acidification specialization is synaptic-vesicle (GO:0097401), not lysosomal; safe complex target is GO:0000221/GO:0016471 (already in review).
- Verdict:** OVER-REACH — PN lysosomal projection wrong-compartment for this brain/synaptic-vesicle isoform; correct acidification term (GO:0097401) already present. **Recommended edits:** [MAP] exempt ATP6V1G2 from lysosomal-acidification/lysosomal-V1 projection; route to synaptic-vesicle acidification + vacuolar V1 complex terms already in the review.

### ATP6V1G3
- Mapping strategy:** Tissue-restricted plasma-membrane isoform; lysosomal projection over-broad (TOMM20/HSPA8/RAB7A precedent). **[MAP]** flag G3 as an exception — safe targets are vacuolar V1 domain/complex (GO:0000221/GO:0016471) + plasma-membrane acid-secretion context already in the review; the specific G3-a-subunit ATPase-binding (GO:0051117) is the mechanistically informative core, not lysosomal acidification.
- Verdict:** OVER-REACH — PN lysosomal projection wrong-compartment for this apical-plasma-membrane kidney isoform. **Recommended edits:** [MAP] exempt ATP6V1G3 from lysosomal-acidification/lysosomal-V1 projection; restrict to vacuolar V1 complex + plasma-membrane/renal acid-secretion terms already in the review.

### AZI2
- Verdict:** Consistent biology, but PN xenophagy projection over-reaches for a TBK1-adaptor/regulator. **Recommended edits:** [MAP] downgrade AZI2's contribution to the Xenophagy node from `xenophagy` (GO:0098792, involved_in) to `regulation of xenophagy` (GO:1904415) — AZI2 is a TBK1-recruiting adaptor, not a cargo receptor. [YAML] optionally add GO:1904415 regulation of xenophagy (involved_in) supported by PMID:30459273 to reflect the NDP52/TAX1BP1-TBK1 bridging role; do not add bare GO:0098792.

### BAG2
- Verdict:** NEF classification sound and already captured; the UPS "adaptor → proteasome binding" projection is unsupported for BAG2. **Recommended edits:** [MAP] do not project GO:0070628 proteasome binding onto O95816 (BAG2 binds HSP70 and CHIP, not the proteasome); its UPS role is already covered by GO:0031625 / GO:0031397 in the review.

### BCL2L13
- Verdict:** Consistent; mitophagy process correctly added (note it is already IEA in UniProt GOA). Key finding: the review's proposed NEW "mitophagy receptor activity" duplicates existing **GO:0140580**. **Recommended edits:** [YAML][REF] replace the BCL2L13 proposed_new_term with existing GO:0140580 mitochondrion autophagosome adaptor activity (add as core MF, supported by PMID:26146385); [MAP] note GO:0000423 is already UniProt-IEA, so goa_status is closer to "already_in_goa" than "new_to_goa".

### BNIP3L
- Verdict:** Consistent; mitophagy process already captured. Key finding: the review's proposed NEW "mitophagy receptor activity" term duplicates the existing **GO:0140580**. **Recommended edits:** [YAML][REF] replace the BNIP3L proposed_new_term "mitophagy receptor activity" with the existing GO:0140580 mitochondrion autophagosome adaptor activity (add as core MF, supported by PMID:20200478).

### CACUL1
- Recommended edits:** Suppress/except the Cullin-group GO:0160072 projection for CACUL1; mark the node mapping as not-inherited for this degenerate member. [MAP]

### CACYBP
- Verdict:** Domain-based misclassification — CACYBP is a Siah1 E3-ligase adaptor / S100A6-binding protein, not a demonstrated HSP90 cochaperone; Hsp90-binding projection is unsupported. **Recommended edits:** [MAP] remove/flag GO:0051879 projection onto Q9HB71 and reconsider the HSP90-cochaperone placement; the gene's shared MF is better represented by molecular adaptor activity (GO:0060090) / ubiquitin protein ligase binding, already in the review.

### CALCOCO1
- Recommended edits:** [YAML] Add GO:0061709 reticulophagy (BP, involved_in) to CALCOCO1 existing/core annotations — currently new_to_goa and the validated core process. [YAML] Replace `proposed_new_terms` "reticulophagy/Golgiphagy receptor activity" with existing GO:0160247 autophagy cargo adaptor activity (and GO:0038024 cargo receptor activity) as the molecular_function for the core receptor role. [REF] Add the EMBO J "CALCOCO1 acts with VAMP-associated proteins to mediate ER-phagy" PMID (named in PN dossier) to the review references.

### CALR
- Verdict:** OVER-REACHES — reject projected GO:0006487 for CALR (true lectin-chaperone function already captured). **Recommended edits:** [MAP] do not propagate GO:0006487 to CALR; re-map the shared "Lectin chaperone" type node to a binding/chaperone term (GO:0030246 / GO:0036503), covering CALR+CANX together.

### CALR3
- Recommended edits:** [MAP] Do not propagate GO:0006487 to CALR3; remap `N-glycosylation system` group to a folding/glycoprotein-QC term or leave chaperone members unmapped. [MAP] Reconsider the `Lectin chaperone` leaf for CALR3 (documented lectin-independent). [YAML] No glycosylation annotation for CALR3.

### CAMLG
- Verdict:** GET-pathway placement sound and already captured by a more specific gene-level term; PPIase classification is a misassignment — CAML binds cyclophilin B but is not a PPIase. **Recommended edits:** [MAP] flag CAMLG as a non-member of the PN "Peptidyl-prolyl isomerases / Cyclophilin type" node, or block GO:0003755 projection onto P49069 (binds cyclophilin, no isomerase activity).

### CAND1
- Verdict:** Consistent and the strongest ADD case of the six — GO:1990757 (real) is a defensible new MF for CAND1, matching both PN and the review's positive-regulator framing. **Recommended edits:** [YAML] consider adding GO:1990757 ubiquitin ligase activator activity to CAND1 existing/core (currently only proposed as a bespoke new term); [REF] confirm PN reference 23453757 and add to the review if it supports the activator role.

### CAND2
- Verdict:** Substantively consistent; PN activator mapping (GO:1990757) over-reaches and conflicts with the review's non-catalytic/context-inhibitory exchange-factor framing. Prefer review's GO:0097602 + GO:0010265. **Recommended edits:** [MAP] downgrade CAND2 type/subtype GO:1990757 mapping toward exchange-factor/cullin-binding (GO:0097602) or context_only, rather than "activator". [REF] add PMID:40011427 to CAND2 review `references` (currently only cited via falcon report).

### CANX
- Verdict:** OVER-REACHES — projected GO:0006487 mis-assigns an enzymatic process to a lectin chaperone; reject for CANX (true function already captured). **Recommended edits:** [MAP] do not propagate GO:0006487 to CANX; re-map the "Lectin chaperone" type node to a binding/chaperone term (e.g. GO:0030246 carbohydrate binding / GO:0036503 ERAD pathway).

### CCDC47
- Verdict:** Consistent; PN adds the precise complex term. **Recommended edits:** [YAML] ADD GO:0160005 PAT complex (part_of, IPI/IDA, PMID:32814900/PMID:36261522) to CCDC47 existing_annotations and core_functions.in_complex — it is the exact, more-specific complex vs the review's GO:0160064. [MAP] keep GO:0044743/GO:0015031 as context-only (broader than review's GO:0160063/GO:0045048).

### CCDC50
- Verdict:** CONSISTENT conclusion (GO:0160247 ADD agreed by both); evidence sources diverge. **Recommended edits:** [REF] add the CCDC50/NLRP3 autophagic-degradation EMBO reports paper to the review references and as supporting_text for the proposed GO:0160247 receptor MF.

### CDK5RAP3
- Recommended edits:** None required; optionally note GO:0006515 is a broader sibling of the review's GO:0072344/GO:0032790 and should not displace them. [MAP]

### CGRRF1
- Recommended edits:** Suppress/flag the RING-group GO:0061630 projection for CGRRF1 (unproven catalytic activity; one in vitro assay negative); if retained, mark as homology-only/unverified rather than ok_for_propagation. [MAP]

### CHIC2
- Verdict:** UNDER-CAPTURED by review — PN ADD is justified. **Recommended edits:** [YAML] add PMID:40796662 to references and add a NEW/proposed annotation GO:0000151 (part_of, "STUB1-CHIC2 complex") and an adapter/molecular-function note; [REF] flag that the review's "function undefined" framing is now superseded by the STUB1-CHIC2 adapter finding.

### CLCN7
- Recommended edits:** [YAML] Add an `existing_annotations`/`proposed_new_terms` entry or `core_functions.directly_involved_in` for GO:0007042 lysosomal lumen acidification (involved_in, supported_by PMID:18449189), framed as contributory.

### CLGN
- Recommended edits:** [MAP] Do not propagate GO:0006487 from `N-glycosylation system` to lectin-chaperone members (CLGN); remap the group to a folding/glycoprotein-QC term or leave lectin chaperones unmapped. [YAML] No glycosylation annotation should be added to CLGN.

### CLPX
- Recommended edits:** [MAP] Reconsider `[class]` projection GO:0035694 → use GO:0030163 protein catabolic process (matches GOA + ClpXP biology; GO:0035694's definition is lysosome-like-organelle specific). [MAP] Optionally extend the PN node to reflect CLPX's GO:0006783 heme biosynthesis chaperone role.

### CNOT4
- Verdict:** CONSISTENT — defensible ADD of GO:0006515 (protein QC) to capture the RQC role. **Recommended edits:** [YAML] consider adding GO:0006515 (involved_in, from PMID:29861391 ABCE1/co-translational QC) as a proposed_new_term or NEW annotation to align with the PN RQC projection.

### CNPY3
- Recommended edits:** [MAP] Correct goa_status for GO:0051879 on the CNPY3 row from `more_specific_than_existing_goa` to `new_to_goa` (no Hsp90-binding annotation exists in CNPY3 GOA). (Review already proposes GO:0051879 + the full chaperone/TLR NEW set; no YAML change needed.)

### CSNK1D
- Verdict:** UNDER-CAPTURED autophagy role; PN ADD (GO:0000045) plausible but PMID-unverified. **Recommended edits:** [REF] resolve the PN row's title-only citations to PMIDs and confirm human (not just yeast Hrr25) evidence; [YAML] if confirmed, add GO:0000045 (involved_in) and reframe the SEC23/COPII annotations to note an autophagosome-membrane-input role alongside secretion.

### CSNK2B
- Verdict:** ROW-1 OVER-REACHES (yeast UTP-C orthology); ROW-2 acceptably no_mapping. **Recommended edits:** [MAP] downgrade row-1 SSU-processome/ribosome-biogenesis projection (GO:0032040/GO:0042254) to context_only/no_mapping for human CSNK2B pending human evidence; [WB] human CSNK2B SSU-processome membership unverified (PubMed: 0 hits).

### CWC27
- Verdict:** Inconsistent — PN propagates positive GO:0003755 PPIase activity onto a curated dead pseudo-enzyme that GOA annotates as NOT|GO:0003755. **Recommended edits:** [MAP] exclude CWC27 from the cyclophilin-type GO:0003755 propagation (CWC27 is a catalytically inactive pseudo-PPIase; GOA = NOT|GO:0003755, PMID:20676357); represent CWC27 via its scaffold/spliceosome role instead.

### CYB5R4
- Verdict:** Inconsistent — PN HSP90-cochaperone placement / GO:0051879 over-reaches and is unsupported by the review. **Recommended edits:** [MAP] exclude CYB5R4 from GO:0051879 Hsp90 protein binding propagation (CS/p23 domain is structural-homology only; no Hsp90-binding evidence); flag the PN "HSP90 cochaperone" classification as domain-based, not functional. [REF] none.

### DCAF10
- Recommended edits:** Add GO:1990756 (ubiquitin-like ligase-substrate adaptor activity) as the molecular_function on DCAF10's core_function, inferred by homology/DCAF-family membership. [YAML]

### DDA1
- Verdict:** Consistent; GO:0160072 (scaffold) is a defensible-but-borderline add vs the review's GO:0005198. **Recommended edits:** [YAML] optionally add GO:0160072 to DDA1 core MF (or reconcile GO:0005198 vs GO:0160072) to align the review with the PN scaffold projection.

### DDB1
- Verdict:** Biology consistent but PN MF mapping mis-categorized. **Recommended edits:** [MAP] retarget DDB1 "Cullin adaptor" node from GO:1990756 to GO:0160072 (scaffold), matching the review's accepted MF and existing GOA.

### DDB2
- Verdict:** Consistent; PN GO:1990756 (receptor) is correctly categorized and a defensible add. **Recommended edits:** [YAML] consider adding GO:1990756 to DDB2 as the explicit DCAF substrate-receptor MF (complements existing GO:0004842 contributes_to), aligning with the PN projection.

### DDRGK1
- Verdict:** Consistent and high quality; only the broad GO:0006515 RQC projection over-reaches relative to existing specific GOA terms. **Recommended edits:** [MAP] drop/downgrade GO:0006515 projection for DDRGK1 (specific RQC terms GO:0072344/GO:0032790 already in GOA and reviewed).

### DENR
- Verdict:** Mapping mismatch — PN "translation termination" + GO:0006415 contradicts DENR's reinitiation/recycling biology (already in GOA as GO:0002188). **Recommended edits:** [MAP] do not project GO:0006415 to DENR; reclassify the PN node as translation reinitiation/40S recycling (GO:0002188 already in GOA).

### DNAJB13
- Recommended edits:** [MAP] Exclude DNAJB13 from the `J-domain containing HSP70 cochaperone` GO:0030544 projection (catalytically-divergent, no HSP70-binding evidence; function is structural radial-spoke). [MAP] Re-examine its ER-branch placement (protein is axonemal, not ER-resident).

### DNAJC10
- Verdict:** Row1 consistent/captured; Row2 over-reaches (PDI isomerase ≠ ERdj5 reductase). **Recommended edits:** [MAP] retarget DNAJC10 row2 from GO:0003756 (PDI activity) to GO:0015035 (protein-disulfide reductase activity), or exclude ERdj5 from the "Protein disulfide isomerases" PN group as a reductase exception.

### DNAJC11
- Verdict:** PN over-reaches — DNAJC11 is a structural MIB/cristae protein, not a demonstrated HSP70 cochaperone. **Recommended edits:** [MAP] remove/exempt DNAJC11 from GO:0030544 propagation under the "J-domain containing HSP70 cochaperone" type; its propagating terms are GO:0140275 / GO:0042407.

### DNAJC12
- Verdict:** Consistent; PN GO:0030544 defensible and already realized in the review. **Recommended edits:** [MAP] (minor) correct DNAJC12 projected `goa_status` from `more_specific_than_existing_goa` to `new_to_goa` (GOA lacks the GO:0031072 parent).

### DNAJC13
- Verdict:** Cochaperone identity consistent; GO:0030544 defensible but inferred. **Recommended edits:** [MAP] (minor) correct DNAJC13 projected `goa_status` to `new_to_goa`; optionally co-propagate GO:0001671 (ATPase activator activity) to match the review's core MF.

### DNAJC14
- Verdict:** PN over-reaches — Hsp70 binding unverified; DNAJC14's supported function is GPCR ER export. **Recommended edits:** [MAP] do not propagate GO:0030544 to DNAJC14 (mark cochaperone MF unverified); retain GO:0050780 / GO:0001664 as the gene-level MF.

### DNAJC16
- Verdict:** Over-reaches for this gene — Hsp70 binding is domain-inferred only, no HSP70 partner shown; flag as family-level inference, not new_to_goa. **Recommended edits:** [MAP] downgrade DNAJC16's GO:0030544 projection from new_to_goa confident annotation to family/ISS-level inference (no experimental HSP70 binding); note the established function (autophagosome-size regulation) lies outside this HSP70-cochaperone node.

### DNAJC17
- Verdict:** Plausible family inference but over-reaches as confident projection; gene's real function (spliceosome/RNA) sits outside the HSP70-cochaperone node. **Recommended edits:** [MAP] mark DNAJC17's GO:0030544 as family/domain-level inference (no experimental HSP70 binding); correct the "more_specific_than_existing_goa" tag (existing GOA MF is RNA binding, not an HSP70 parent).

### DNAJC22
- Verdict:** Consistent family-level inference; GO:0030544 is a defensible more-specific candidate but unverified experimentally — flag as ISS/family inference rather than confident new annotation. **Recommended edits:** [MAP] retain GO:0030544 for DNAJC22 but mark as family/domain-level inference (no experimental HSP70 binding; Wurst-orthology basis only).

### DNAJC27
- Verdict:** Consistent core review; PN placement over-emphasizes the J-domain. GO:0030544 is a defensible inferred ADD but **not core**. **Recommended edits:** [MAP] change goa_status from more_specific_than_existing_goa to new_to_goa (no existing chaperone-binding GOA term to refine).

### DNAJC28
- Verdict:** Consistent on function (uncharacterized J-protein); GO:0030544 defensible inferred ADD. **Recommended edits:** [MAP] change goa_status to new_to_goa; [MAP] reconcile ER vs mitochondrial branch placement (review predicts mitochondrial targeting).

### DNAJC30
- Verdict:** Over-reach. GO:0030544 projection is unsupported for DNAJC30 (a complex-I repair / ATP-synthase auxiliary factor). **Recommended edits:** [MAP] do not propagate GO:0030544 to DNAJC30 (family-level over-inference; gene-level GO:0051082 + GO:0019899 already capture its biology); [MAP] if retained, downgrade goa_status to new_to_goa and mark as IBA/family-inferred only.

### DNAJC4
- Verdict:** Family-level J-co-chaperone call sound; GO:0030544 is a defensible-but-unverified ADD; mitochondrial placement and the GO:0030544-vs-GO:0051082 MF mismatch need reconciling. **Recommended edits:** [MAP] reconcile Hsp70 protein binding (GO:0030544) projection with the review's GO:0051082 unfolded protein binding — both are family-level/unverified; prefer GO:0030544 only if asserted as predicted, not experimental. [MAP][WB] verify the Mitochondrial-branch assignment — no mitochondrial localization evidence appears in the review or notes.

### DNAJC5
- Verdict:** Fully consistent; PN Hsp70-binding story already captured as core MF (GO:0030544). **Recommended edits:** none required; optionally [MAP] note that CSPalpha is the prototypical *synaptic/secretory-vesicle* CSP, so the ER-branch placement is an umbrella rather than its primary compartment.

### DNAJC5G
- Verdict:** Family-level call sound; GO:0030544 is a defensible-but-unverified ADD; harmonize MF term with the CSP family. **Recommended edits:** [MAP] reconcile the GO:0030544 (PN) vs GO:0051082 (review) MF choice across the CSP paralogs — for consistency with DNAJC5/DNAJC5B, GO:0030544 Hsp70 protein binding is preferable, asserted as predicted/family-level (not experimental).

### DNAJC6
- Verdict:** Consistent and well-supported; PN's GO:0030544 is a defensible more-specific ADD over the review/GOA's GO:0031072. **Recommended edits:** [YAML][MAP] consider replacing/supplementing GO:0031072 heat shock protein binding with the more specific GO:0030544 Hsp70 protein binding in the review core MF (auxilin's documented partner is HSPA8/HSC70), aligning with the PN projection.

### DNAJC7
- Verdict:** Fully consistent; row2 already captured, row1 GO:0030544 a defensible-but-secondary more-specific ADD. **Recommended edits:** [MAP] note that for DNAJC7 the broader GO:0031072 (joint HSP70/HSP90 binding) is the better umbrella than the HSP70-only GO:0030544; consider also projecting the well-supported GO:0001671 ATPase activator activity (review core MF, in GOA) from the J-domain node.

### DRG2
- Verdict:** GTPase biology is solid, but the PN RQC placement and GO:0006515 projection are unsupported for DRG2. **Recommended edits:** [MAP] do not project GO:0006515 (protein QC) to DRG2 — no RQC/surveillance evidence; GTPase activity (GO:0003924) is the supported core.

### DTL
- Verdict:** Consistent; PN GO:1990756 is correctly categorized and a defensible more-specific add over the review's GO:0030674. **Recommended edits:** [YAML] optionally add/swap GO:1990756 as the DCAF substrate-receptor MF (more specific than GO:0030674), aligning with the PN projection.

### EEF2K
- Verdict:** Clear mis-mapping — EEF2K is the eEF2 kinase, not a translation elongation factor; GO:0003746 should not be projected. **Recommended edits:** [MAP] remove GO:0003746 projection for EEF2K; if a shared process is wanted use GO:0045900 negative regulation of translational elongation. Core MF GO:0004686 already in GOA.

### EIF2D
- Verdict:** Mapping mismatch — PN "translation termination" + GO:0006415 contradicts EIF2D's initiation/recycling biology already in GOA. **Recommended edits:** [MAP] do not project GO:0006415 to EIF2D; reclassify PN node toward reinitiation/40S recycling (GO:0001731 / GO:0032790 already in GOA).

### EIF3J
- Verdict:** Initiation placement consistent and correct; RQC-group GO:0006515 projection over-reaches (EIF3J is a recycling accessory, not a protein-QC factor). **Recommended edits:** [MAP] drop GO:0006515 projection for EIF3J (or substitute GO:0032790 ribosome disassembly if a recycling term is wanted).

### EIF4E2
- Verdict:** Biology consistent; one node-level contradiction (PN GO:0016281 vs review REMOVE). RQC story already captured more precisely. **Recommended edits:** [MAP] flag the EIF4E2 "eIF4F complex" type→GO:0016281 projection as inappropriate (4EHP cannot bind eIF4G / is not an eIF4F component — see review REMOVE of GO:0016281); do not propagate GO:0016281 to O60573.

### EIF5A
- Verdict:** Consistent; elongation core fully captured. GO:0006515 RQC umbrella is defensible but mildly over-reaching for a general elongation factor and is absent from the review. **Recommended edits:** [MAP] treat the EIF5A RQC-group→GO:0006515 projection as low-confidence (eIF5A is an elongation factor with a supportive RQC-cofactor role, not a dedicated surveillance factor); optionally [YAML] consider adding eIF5A's RQC-cofactor role only if curator deems UniProt's CAT-tailing statement annotation-worthy.

### ERLIN1
- Recommended edits:** [MAP] Replace/qualify the GO:0000151 group projection with GO:0000835 "ER ubiquitin ligase complex" (CC) for the ERLIN/RNF170 assembly, noting ERLINs are non-catalytic BAND 7 subunits. [YAML, optional] Consider adding MF GO:0160072 "ubiquitin ligase complex scaffold activity" to core_functions for the adaptor role.

### ERLIN2
- Recommended edits:** [MAP] Replace/qualify the GO:0000151 group projection with GO:0000835 "ER ubiquitin ligase complex" (CC), noting ERLINs are non-catalytic BAND 7 subunits. [YAML, optional] Consider adding MF GO:0160072 "ubiquitin ligase complex scaffold activity" to core_functions.

### ERO1A
- Verdict:** Consistent at the (corrected) gene/type level; GO:0016971 validated and captured. The lingering **group-level GO:0003756 projection over-reaches** and should not land on ERO1A. **Recommended edits:** [MAP] suppress/override the GO:0003756 projection for ERO1A (and ERO1B) so the PDI-reoxidation oxidase children inherit only GO:0016971, not the parent isomerase term (matches the already-corrected type node and the review's oxidase-vs-isomerase distinction).

### ERO1B
- Verdict:** Consistent at the (corrected) gene/type level; GO:0016971 validated and captured. The **group-level GO:0003756 projection over-reaches** and should not land on ERO1B (same fix as ERO1A). **Recommended edits:** [MAP] suppress/override the GO:0003756 projection for ERO1B so PDI-reoxidation oxidase children inherit only GO:0016971 (consistent with the corrected type node and the review's explicit oxidase-not-isomerase / not-reductase stance).

### ERP27
- Verdict:** **Contradiction** — PN projects GO:0003756 (new_to_goa) onto a gene whose review explicitly NEGATES that exact term (no CXXC, catalytically inactive). PN over-reaches; review is correct. **Recommended edits:** [MAP] remove/suppress the GO:0003756 projection for ERP27 (it is a non-catalytic PDI-family member; the term is correctly a NOT annotation). If a positive mapping is wanted, target GO:0051082 unfolded protein binding and/or GO:0051087 protein-folding chaperone binding (both OLS-real, both already in the review's core_functions).

### ERP29
- Verdict:** OVER-REACHES / CONTRADICTED — reject projected GO:0003756 for ERP29; the gene is a non-catalytic PDI member whose function is already captured by GO:0051087. **Recommended edits:** [MAP] do not propagate GO:0003756 to ERP29 (it carries a curated NOT for this term); exclude non-catalytic PDI-family members from the group's isomerase projection or re-map ERP29 to GO:0051087 protein-folding chaperone binding.

### FAF2
- Recommended edits:** [YAML] (optional) add GO:0035694 mitochondrial protein catabolic process (involved_in; mitoTAD/mito membrane-protein extraction, PMID:41258083) as a non-core BP to mirror the PN projection. [REF] PN-cited PMID:18438607 (UBX row) absent from review — verify whether gene-specific or a UBX-family review.

### FBXL16
- Verdict:** CONSISTENT-WITH-CAVEATS / ACCEPT degradative mapping. **Flag: non-canonical F-box (no detectable CUL1).** Proposed stabilizer term is candidate/unverified. **Recommended edits:** none to YAML [no change]; [MAP] annotate node that FBXL16 is non-canonical (SKP1+ / CUL1-negative) so GO:1990756 propagation is treated as tentative for this member.

### FBXL3
- Verdict:** CONSISTENT / ACCEPT mapping. No edits required; the MODIFY→GO:1990756 pattern is correctly applied. Optional [REF]: PN-row reference PMID:15340381 not reflected in review (placeholder only).

### FBXL8
- Verdict:** MAPPING CONSISTENT but YAML gap. **Recommended edits:** [YAML] add `GO:1990756` as `action: NEW` in FBXL8 existing_annotations (mirror FBXL7/FBXL12) so the PN-projected adaptor MF is materialized; [MAP] consider noting the non-canonical (no-LRR) status on the F-box|LRR subtype for FBXL8.

### FBXO10
- Recommended edits:** none to FBXO10-ai-review.yaml. [MAP] none — node mapping and review concur.

### FBXO15
- Recommended edits:** none to FBXO15-ai-review.yaml. [MAP] none — node mapping and review concur.

### FBXO16
- Recommended edits:** [YAML] consider adding GO:1990756 as a NEW MF `existing_annotation` (currently FBXO16 carries no MF annotation; the adaptor activity lives only in core_functions) — mirrors the explicit NEW done for FBXO15. [MAP] none.

### FBXO17
- Recommended edits:** none to FBXO17-ai-review.yaml (ERAD MARK_AS_OVER_ANNOTATED and NEW carbohydrate-binding are sound). [MAP] for the FBA subfamily, prefer GO:0030246 (lectin) as the informative MF at gene level rather than propagating the generic GO:1990756; do not propagate ERAD (GO:0036503) from the FBA node to FBXO17.

### FBXO2
- Recommended edits:** none to FBXO2-ai-review.yaml. [MAP] Optionally annotate FBA-lectin F-box subfamily nodes so carbohydrate binding (GO:0030246) is recognized as their distinguishing MF alongside the generic GO:1990756.

### FBXO21
- Recommended edits:** none to FBXO21-ai-review.yaml. [MAP] none — node mapping and review concur.

### FBXO27
- Recommended edits:** [YAML] In FBXO27-ai-review.yaml, replace the `proposed_new_terms` "lysophagy" entry with a reference to existing **GO:0062093 lysophagy** (verified real), and set core_function #3 `directly_involved_in` to GO:0062093 (more specific than GO:0016236 macroautophagy). [YAML] Optionally MODIFY the ERAD IBA (GO:0036503) toward **GO:0097466 ubiquitin-dependent glycoprotein ERAD pathway** if retained.

### FBXO40
- Verdict:** Consistent; correct F-box MODIFY pattern; defensible verified NEW BP (GO:0046627). ACCEPT review. **Recommended edits:** none required; optionally [REF] upgrade PMID:22033112 to VERIFIED if full text read.

### FBXO41
- Verdict:** Consistent; well-evidenced verified NEW terms. ACCEPT review. **Recommended edits:** none for YAML; optionally [MAP] note FBXO41 auxiliary domain may be C2H2/coiled-coil rather than LRR in the PN workbook.

### FBXO43
- Verdict:** Review correct; PN node mis-files FBXO43 and over-reaches with GO:1990756. **Recommended edits:** [MAP] exclude FBXO43/EMI2 from the GO:1990756 substrate-adaptor projection and flag as non-canonical F-box / APC/C inhibitor (core MF GO:1990948), mirroring FBXO5/EMI1.

### FBXO47
- Verdict:** Consistent at MF label; meiotic biology appropriately added (GO:0007129) with honest UNDECIDED on SCF catabolism. ACCEPT review. **Recommended edits:** none required; optionally [REF] verify Hua 2019 / Guan 2022 / Ma 2024 PMIDs and [YAML] convert the label-only bouquet term to a real GO ID if one exists (e.g. via OLS) before promotion.

### FBXO5
- Recommended edits:** none to FBXO5-ai-review.yaml (review is correct). [MAP] Flag FBXO5/EMI1 as a non-canonical F-box (APC/C inhibitor) so GO:1990756 is NOT propagated to it; its core MF is GO:1990948 ubiquitin ligase inhibitor activity.

### FBXO6
- Recommended edits:** none to FBXO6-ai-review.yaml. [MAP] As for FBXO2, FBA-lectin subfamily nodes could carry GO:0030246 as the distinguishing MF in addition to GO:1990756.

### FBXO8
- Recommended edits:** [YAML] consider adding GO:1990756 as a NEW `existing_annotation` (MF) to make the adaptor activity an explicit annotation, not only a `core_functions` entry (FBXO8 currently has no curated SCF-adaptor MF in GOA; the only MF is the IEA GEF term, kept non-core). [MAP] none.

### FBXW4
- Verdict:** Row1 CONSISTENT (ADD GO:1990756). Row2 PN node OVER-REACHES. **Recommended edits:** [MAP] change Row2 group `Ubiquitin and UBL binding|E3 ligase` projection for FBXW4 from GO:0061630 ubiquitin protein ligase activity to GO:0043130 ubiquitin binding, or set no_mapping — PMID:21070969 documents WD40 ubiquitin BINDING (regulating F-box turnover), not catalytic ligase activity; F-box proteins are non-catalytic.

### FBXW5
- Verdict:** MOSTLY CONSISTENT; one substrate gap. **Recommended edits:** [YAML] Note the PN ALP SEC23B/autophagy axis in FBXW5 notes/description and assess the eLife "ULK1-FBXW5-SEC23B nexus" paper; if it supports a direct SCF(FBXW5)→SEC23B degradation event, consider adding it as a substrate (and a regulation-of-autophagy non-core process) — verify the PMID first. [REF] add the eLife SEC23B reference.

### FBXW7
- Verdict:** Rows 1–2 CONSISTENT; Row3 PN node OVER-REACHES (contradicts the review's own over-annotation call). **Recommended edits:** [MAP] change Row3 `Ubiquitin and UBL binding|E3 ligase` projection for FBXW7 from GO:0061630 ubiquitin protein ligase activity to GO:0043130 ubiquitin binding or no_mapping — PMID:21070969 = WD40 ubiquitin BINDING controlling F-box auto-turnover, not catalytic ligase; the FBXW7 review already marks ubiquitin binding as over-annotated.

### FBXW8
- Verdict:** Rows 1–2 CONSISTENT (GO:1990756 already in GOA, both CUL1+CUL7 contexts validated); Row3 PN node OVER-REACHES. **Recommended edits:** [MAP] change Row3 `Ubiquitin and UBL binding|E3 ligase` projection for FBXW8 from GO:0061630 ubiquitin protein ligase activity to GO:0043130 ubiquitin binding or no_mapping — PMID:21070969 = WD40 ubiquitin BINDING / F-box auto-turnover, not ligase catalysis; structure (PMID:35982156) shows FBXW8 is non-catalytic.

### FKBP5
- Verdict:** Consistent on core; PN's autophagy role is documented but intentionally non-propagating, so no required edit. **Recommended edits:** none required; optionally note the FKBP5-autophagy/BECN1 paper in notes/references for completeness [REF]. Do not propagate GO:0035032/GO:0016236 (regulator, too broad) [MAP].

### FKBP8
- Verdict:** Consistent; all PN molecular roles captured; only nuance is mitophagy process (GO:0000423) vs regulation (GO:1901524) granularity. **Recommended edits:** [MAP] optionally retarget the Mitophagy-receptor leaf projection from GO:0000423 to GO:1901524 regulation of mitophagy to match FKBP8's experimental (IDA) evidence and the review.

### FKBPL
- Verdict:** Consistent; PN GO:0051879 projection validated and added as the core MF; subtype-level PPIase correctly withheld. **Recommended edits:** none required; [REF] optionally add PMID:15664193 (Jascur et al., WISp39/HSP90/p21) as an explicit reference entry in the review YAML to anchor the GO:0051879 core function (currently it is only in notes, with the YAML core_function relying on UniProt text).

### GCN1
- Verdict:** Highly consistent on core sensor/ISR/RQC biology; PN story already captured (review is more granular: GO:0140469, GO:0072344, GO:0170011). One over-reach. **Recommended edits:** [MAP] qualify the eEF1A-ubiquitination type→GO:0016567 projection — GCN1 promotes (does not catalyze) eEF1A ubiquitination; project as involved_in RQC (GO:0072344) rather than as GCN1's own protein-ubiquitination activity. [REF] consider adding the PN-cited GCN1 developmental PLOS Genetics paper to the review references (currently absent) or noting its relevance is non-core.

### GIGYF1
- Verdict:** Fully consistent; PN RQC story already captured more precisely (GO:0045947 + NEW GO:0008190). GO:0006515 is a defensible umbrella, not an over-reach. **Recommended edits:** [YAML] for paralog consistency, consider whether GIGYF1 warrants GO:0072344 (rescue of stalled cytosolic ribosome) as GIGYF2's review carries it — the underlying PMID:33053355/RQC evidence is shared (curator judgment; optional).

### GLMN
- Verdict:** Fully consistent; PN inhibitor mapping (GO:1904667) is well-aligned with the review (GO:0055105) — no over-reach, no missing-NEW pressure on the core function. **Recommended edits:** [YAML] optional — anchor the proposed "negative regulation of cIAP-mediated inflammasome activation" term to the now-existing GO:0141086 (verify scope) as the closest existing parent/match. No mapping change required.

### GTPBP1
- Verdict:** Biology consistent; PN's GO:0072344 "Ribosomal rescue" mapping over-reaches vs the review's surveillance/decay framing (GO:0071025 present in GOA; GO:0072344 absent). **Recommended edits:** [MAP] do not project GO:0072344 (rescue of stalled cytosolic ribosome) onto GTPBP1 — its evidenced role is mRNA surveillance/exosomal decay (GO:0071025/GO:0061014), not ribosome rescue; reclassify the PN row from "Ribosomal rescue" to "other RQC processes" (RQC-group→GO:0006515 still applies). [REF] PMID:30108131 supports surveillance, not rescue — note the interpretive divergence.

### GTPBP2
- Verdict:** Consistent; PN rescue story is real NEW pressure (GOA lacks a correct BP). **Recommended edits:** add GO:0072344 rescue of stalled cytosolic ribosome to `proposed_new_terms` (or as a NEW annotation) [YAML]; consider adding Ishimura 2014 Science to `references` for the PELO-rescue/neurodegeneration evidence [REF].

### GTPBP6
- Verdict:** Mostly consistent on biogenesis (already captured, review narrower); row-2 stalled-ribosome-rescue projection over-reaches vs the recycling evidence. **Recommended edits:** keep GO:7770016 as context-only / do not propagate to GTPBP6 unless stalled-ribosome evidence is found [MAP]; optionally add a mitochondrial-ribosome-recycling process annotation (anchored to PMID:34135319 dual-role) to capture row 2 accurately [YAML].

### HBS1L
- Verdict:** Fully consistent; PN rescue story already captured (more specifically) — no NEW pressure. **Recommended edits:** none warranted; treat group-node GO:0006515 as context-only/entailed for HBS1L (do not add as a separate annotation) [MAP].

### HSPA13
- Verdict:** Atypical HSP70; PN's GO:0140662 foldase projection is contradicted by the truncated SBD and peptide-independent ATPase — over-reaches. **Recommended edits:** [MAP] do not project GO:0140662 ATP-dependent protein folding chaperone (nor GO:0044183) onto P48723 (PMID:8131751 truncated peptide-binding domain, peptide-independent ATPase); its evidenced MFs are GO:0016887 ATP hydrolysis activity and GO:0032182 ubiquitin-like protein binding.

### HSPA14
- Verdict:** RAC/cotranslational-folding projection sound and already captured; HSP70-type GO:0140662 is borderline-defensible (atypical Ssz1p-like HSP70) but should carry the caveat. **Recommended edits:** [MAP] keep GO:0051083 for the RAC subtype (already covered); for the HSP70-type GO:0140662 projection, scope to co-translational folding and note HSPA14's Ssz1p-like atypia (intrinsic foldase activity uncertain) rather than asserting canonical ATP-dependent refolding.

### HSPB3
- Verdict:** sHSP placement sound but PN MF target mischaracterizes holdases as foldases; mito row unsupported. **Recommended edits:** [MAP] retarget GO:0044183 → GO:0140309 unfolded protein holdase activity (or GO:0051082) for sHSP nodes on Q12988; [MAP] do not project a mitochondrial chaperone term onto HSPB3 (no mitochondrial localization evidence).

### HSPB7
- Verdict:** sHSP membership correct but the GO:0044183 foldase projection is contradicted by direct evidence; over-reaches. **Recommended edits:** [MAP] do not project GO:0044183 protein folding chaperone onto Q9UBY9 (HSPB7 demonstrably does not refold; PMID:19464326); if a shared sHSP MF is desired use GO:0140309 unfolded protein holdase activity / GO:0051082 unfolded protein binding, and mark HSPB7 a non-canonical exception.

### HSPB8
- Verdict:** CASA/aggrephagy projection sound and already captured; sHSP foldase MF over-reaches, mito row unsupported. **Recommended edits:** [MAP] retarget sHSP GO:0044183 → GO:0140309 / GO:0051082 on Q9UJY1; [MAP] do not project a mitochondrial chaperone term onto HSPB8 (no mito localization). CASA row needs no change.

### HSPB9
- Verdict:** sHSP placement defensible by homology but the GO:0044183 foldase projection over-reaches (wrong activity class + no demonstrated chaperone activity). **Recommended edits:** [MAP] do not project GO:0044183 (foldase) onto Q9BQS6; if the sHSP node propagates an MF use GO:0140309 / GO:0051082 as inference, and note HSPB9's only experimental MF is GO:0045503 dynein light chain binding.

### HYPK
- Verdict:** Mostly consistent; PN's catalytic N-terminal-acetylation projection over-reaches for a NatA-modulator. **Recommended edits:** treat node GO:0006474 as context-only for HYPK (do not propagate the catalytic process term); keep the review's GO:0010699 inhibitor activity + GO:0031415 NatA complex as the accurate captures [MAP].

### LMAN1
- Recommended edits:** [MAP] Do not propagate GO:0006487 (protein N-linked glycosylation) to LMAN1 from the "N-glycosylation system" group — LMAN1 binds/transports high-mannose glycoproteins, it does not perform N-linked glycosylation; flag the group node as over-broad (mixes installers/processors/readers).

### LMAN1L
- Recommended edits:** [MAP] Suppress GO:0006487 (protein N-linked glycosylation) propagation to LMAN1L — predicted lectin/cargo receptor, no N-glycosylation activity, and transcript-level-only evidence; do not introduce a new biosynthesis annotation on an uncharacterized paralog.

### LMAN2
- Recommended edits:** [MAP] Do not propagate GO:0006487 (protein N-linked glycosylation) to LMAN2/VIP36 — it is a high-mannose glycan-reading sorting receptor (transport/retrograde QC), not an N-linked-glycosylation enzyme; flag the "N-glycosylation system" group node as over-broad.

### LMAN2L
- Recommended edits:** [MAP] Do not propagate GO:0006487 (protein N-linked glycosylation) to LMAN2L/VIPL — it is an ER-resident high-mannose lectin / ER-export regulator, not an N-glycosylation enzyme; flag the "N-glycosylation system" group node as over-broad (and a poor fit for a non-cycling ER resident).

### LRSAM1
- Recommended edits:** [YAML] add GO:0098792 xenophagy (BP, involved_in) — the base process is absent though GO:1904417 (its positive-regulation child) is already accepted as core; cite PMID:23245322.

### LTN1
- Verdict:** Fully consistent; PN story already captured (review more specific) — no NEW pressure. **Recommended edits:** none required for terms; treat group-node GO:0006515 as context-only/entailed (LTN1 has the specific GO:1990116) [MAP]; optionally add PMID:19489725 (PN row-2 reference) to `references` if it supports the Listerin RQC/neurodegeneration role [REF].

### MAN1B1
- Recommended edits:** [MAP] Correct MAN1B1's group projection of GO:0006487 — mark goa_status as NOT entailed_by_goa_closure (GO:0140277/GO:1904380 do not subsume GO:0006487); MAN1B1 is an N-glycan-processing enzyme, not an N-linked-glycosylation (attachment) enzyme.

### MAP1S
- Recommended edits:** [YAML] Add `GO:0000423` mitophagy (involved_in) supported_by PMID:21262964 (LRPPRC/Parkin link; defective-mitochondria accumulation) and `GO:0035973` aggrephagy (involved_in) supported_by the PN-cited tandfonline/Cancer Research MAP1S-autophagy papers — fetch and add those PMIDs to `references` first (verify the tandfonline "MAP1S enhances autophagy to suppress tumorigenesis" PMID and the AACR Cancer Research PMID before citing). [MAP] No mapping-status change needed; both type→GO propagations are correct.

### MAP3K20
- Verdict:** Consistent; ribotoxic-stress sensor role already well captured — PN group GO:0006515 over-reaches for a signaling kinase. **Recommended edits:** treat group-node GO:0006515 as context-only for MAP3K20 (do not propagate the protein-QC catabolic process to a sensor/signaling kinase) [MAP]; no YAML changes needed.

### MEFV
- Recommended edits:** [YAML] consider adding GO:0160247 autophagy cargo adaptor activity (MF) for the TRIM20 precision-autophagy receptor role (PMID:26347139) — currently captured only as non-core positive-regulation-of-autophagy. [MAP] annotate the RING-group node (or a ringless-TRIM exclusion) so GO:0061630 does NOT auto-propagate to "Pyrin, ringless, SPRY" members lacking a functional RING; the review's over-annotation flag on GO:0061630 should be honored by the mapping.

### MKRN2
- Verdict:** Over-reach on the RQC branch (paralog inheritance from MKRN1). E3-ligase placement consistent. **Recommended edits:** [MAP] do not project GO:0006515 / GO:1990116 onto MKRN2 from the RQC node — no human-experimental RQC evidence; flag MKRN2's RQC-node membership as paralogy-driven (PARALOG_OVERANNOTATION) pending the suggested iCLIP/ribosome-profiling experiment.

### NAA30
- Verdict:** Consistent and high-quality. Optional ADD of BP GO:0006474 to the review to mirror the PN projection. **Recommended edits:** Add existing/new BP annotation GO:0006474 (N-terminal protein amino acid acetylation, involved_in) to NAA30 review [YAML].

### NAA35
- Verdict:** Consistent, high-quality. Internal note vs YAML mismatch: notes say PMID:32296183 (TRIM7) protein-binding should be MARK_AS_OVER_ANNOTATED, but YAML uses KEEP_AS_NON_CORE (minor, defensible either way). **Recommended edits:** Add BP GO:0006474 (involved_in, auxiliary subunit of the acetylating complex) to NAA35 review [YAML]; optionally reconcile PMID:32296183 action with notes (KEEP_AS_NON_CORE vs MARK_AS_OVER_ANNOTATED) [YAML].

### NAA38
- Verdict:** Consistent, high-quality. Same minor notes-vs-YAML mismatch as NAA35: notes say HT protein-binding PMID:25416956/PMID:32814053 should be MARK_AS_OVER_ANNOTATED, YAML uses KEEP_AS_NON_CORE. **Recommended edits:** Add BP GO:0006474 (involved_in, auxiliary subunit) to NAA38 review [YAML]; optionally reconcile PMID:25416956 / PMID:32814053 protein-binding actions with notes [YAML].

### NAA40
- Verdict:** Placement biologically off (histone NAT mis-filed under nascent-peptide husbandry); generic GO:0006474 over-reaches relative to the histone-specific terms already present. **Recommended edits:** Re-home NAA40/NatD from "N-terminal acetylation of nascent peptide" to a histone/chromatin PN node, or replace the projected generic GO:0006474 with a histone-N-terminal-acetylation-specific framing [MAP]; do not add generic GO:0006474 to the review (histone-specific MFs suffice) [YAML]; PMID:25732826 already flagged WRONG_IDENTIFIER — candidate for removal/replacement [REF].

### NBR1
- Verdict:** CONSISTENT and convergent — review already adds GO:0160247 NEW. Minor: consider adding GO:0000425 pexophagy BP to match PN projection. **Recommended edits:** consider [YAML] add existing/new GO:0000425 pexophagy (involved_in) to NBR1 review to mirror PN projection and SQSTM1 co-receptor evidence.

### NEMF
- Verdict:** Consistent, high-quality; PN projection of GO:0006515 is a defensible ADD (distinct QC aspect, verified absent from GOA and not an ancestor of existing terms). **Recommended edits:** Add GO:0006515 (protein quality control for misfolded or incompletely synthesized proteins, involved_in) to NEMF review to mirror the PN projection [YAML].

### NLRX1
- Recommended edits:** [REF/WB] obtain and assess the PN-cited "Listeria hijacks host mitophagy through a novel mitophagy receptor" (Nat Immunol) — it is absent from the review; it is the sole basis for the NLRX1 LIR/mitophagy-receptor claim and for GO:0000423. [YAML] if verified, add GO:0000423 mitophagy (and reconcile with the review's existing GO:0010508 proposed_new_term, which currently frames the autophagy role generically via TUFM rather than as mitophagy).

### NPLOC4
- Verdict:** Consistent, high-quality; core captured, DUB correctly suppressed, one ComplexPortal mis-citation already flagged. **Recommended edits:** Optionally add GO:0006515 (involved_in, non-core) to mirror the RQC-group projection [YAML]; PMID:39329031 already flagged WRONG_IDENTIFIER on GO:0034098/GO:0043161/GO:1904949 — replace with a correct p97 complex reference [REF].

### NUFIP1
- Verdict:** Consistent; ribophagy ADD already implemented in review; only the proposed bespoke MF term over-reaches. **Recommended edits:** [YAML] drop the `proposed_new_terms` "ribophagy receptor activity" entry — the existing GO:0034517 ribophagy (BP) + GO:0160247 autophagy cargo adaptor activity (MF), both already in the review's core_functions, fully capture the role (mirrors the BNIP3L/CALCOCO1 "use existing terms, don't mint new" precedent).

### OPTN
- Verdict:** CONSISTENT on mitophagy/xenophagy (review more specific); PN aggrephagy (GO:0035973) over-reaches / likely group-note carryover. **Recommended edits:** [MAP] reconsider OPTN membership in the Aggrephagy receptor leaf (GO:0035973 new_to_goa) — unsupported by OPTN-specific evidence; demote to context or drop.

### OTUD3
- Recommended edits:** [MAP] Do not propagate GO:0006515 (protein QC) to OTUD3 from the RQC-group node — OTUD3 antagonizes ZNF598-driven 40S ubiquitination (negative RQC regulator), so an `involved_in protein quality control` assertion mis-states direction; flag as do-not-project.

### P4HA3
- Recommended edits:** [YAML] Consider adding a peptidyl-proline-hydroxylation / collagen-biosynthetic-process entry to P4HA3 proposed_new_terms (GO:0018401 / GO:0032964) for parity with P4HA1/P4HA2 and to match the PN projection.

### P4HB
- Verdict:** Consistent; PDI core validated; collagen role real but already captured via finer P4H-complex terms, making GO:0032964 a broader optional addition. **Recommended edits:** [MAP] consider downgrading the ER-collagen-processing leaf projection (GO:0032964) to context/non-propagating for P4HB (it acts as the non-catalytic structural beta-subunit; the review's GO:0004656 contributes_to + GO:0016222 part_of are the more accurate, already-present representation).

### PELO
- Recommended edits:** none required. [MAP] (optional) treat GO:0006515 for PELO as broader/redundant given GO:0072344 already exact in GOA+review.

### PPIB
- Verdict:** CONSISTENT — GO:0003755 already captured (correct); GO:0032964 is a sound NEW addition. **Recommended edits:** [YAML] consider adding GO:0032964 collagen biosynthetic process (involved_in) to PPIB existing/proposed terms, supported by PMID:39245686 + OI9 genetics, to align the review with the defensible PN projection.

### RACK1
- Recommended edits:** [YAML] Consider adding a note/annotation on the RACK1-ATG5 autophagy-regulator role (PN-cited) and the pre-40S/biogenesis association if literature supports — both are absent from the current review. [MAP] Do NOT auto-project GO:0042254/GO:0030688 to RACK1 from the biogenesis/pre-40S node without gene-level evidence (RACK1 framed as structural/RQC scaffold, not an assembly factor); GO:0006515 broader than the exact GO:0072344 already present. [REF] RACK1-ATG5 paper (resolve to a PMID) missing from review references.

### RETREG2
- Recommended edits:** [YAML] add GO:0061709 reticulophagy (BP, involved_in; the specific process for this ER-phagy receptor) — currently absent; more precise than the accepted generic GO:0061753. Cite PMID:26040720/PMID:34338405.

### RNF14
- Recommended edits:** none required. [REF] (optional) check PN-cited PMID:17367545 (RBR row) — absent from review; verify whether it adds RNF14-specific support or is a family review. [MAP] GO:0006515 broader than the exact RQC terms already annotated.

### RNF166
- Recommended edits:** [YAML] none required for the PN story — the review already proposes GO:0098792 xenophagy (NEW). Optionally [REF] check PN row3's PMID:17990982 (UIM characterization), absent from the review, if a UIM ubiquitin-reader MF is desired.

### RNF170
- Recommended edits:** [YAML] add GO:0000151 ubiquitin ligase complex (or child GO:0000835 ER ubiquitin ligase complex; part_of, PMID:21610068/38782601 ERLIN1/2 association) as a non-core CC — currently absent from the review. [REF] verify PN row-3 reference "41481136" — does not resolve as a valid PMID (likely garbled); confirm intended citation.

### RNF185
- Recommended edits:** [YAML] (optional) add GO:0000151 ubiquitin ligase complex (or child GO:0000835 ER ubiquitin ligase complex; part_of, PMID:32738194) and GO:0000423 mitophagy (involved_in, PMID:21931693) as non-core annotations to mirror the PN projections. [MAP] consider GO:0000835 ER ubiquitin ligase complex as a more precise target for the membralin-complex node.

### RNF25
- Recommended edits:** none required. [REF] (optional) check PN-cited PMID:19489725 (RING row) — absent from review; verify whether it adds RNF25-specific support or is a family review. [MAP] GO:0006515 broader than the exact RQC terms already annotated.

### RNF41
- Recommended edits:** [REF/WB] obtain/assess the PN-cited CLEC16A-RNF41-USP8 beta-cell mitophagy paper (and UniProt's PMID:24949970 late-mitophagy citation) — both absent from the review; they are the basis for GO:0000423. [YAML] if verified, add GO:0000423 mitophagy (regulation-of-mitophagy may fit better given RNF41's late/fusion-stage role) — currently the mitophagy role is mentioned in `description` but unannotated and uncited.

### RNF5
- Recommended edits:** none required. [YAML] (optional) consider adding GO:2000785 regulation of autophagosome assembly (IMP/IDA, PMID:23093945) as a non-core BP to mirror the PN projection. [REF] PN-cited PMID:19489725 (RING row) absent from review — verify it is a family review, not gene-specific.

### SEC11A
- Recommended edits:** [MAP] At the "ER signal peptidase" node, annotate that catalytic subunits SEC11A/SEC11C additionally project signal peptidase MF (GO:0009003 / GO:0004252), distinct from accessory subunits — so the node does not flatten catalytic vs accessory members.

### SEC11C
- Recommended edits:** [MAP] Same node-level note as SEC11A: flag that catalytic subunits SEC11A/SEC11C project signal peptidase MF (GO:0009003 / GO:0004252) distinct from the non-catalytic SPCS subunits.

### SEC62
- Recommended edits:** [YAML] Add GO:0005784 Sec61 translocon complex (part_of/located_in, translocon-associated) to SEC62 existing_annotations/core_functions, matching the PN-projected term and the verified GO definition (TRAP-inclusive).

### SEC63
- Recommended edits:** [YAML] Add MF GO:0030544 Hsp70 protein binding (enables; J-domain stimulation of BiP/HSPA5) to SEC63 existing_annotations + core_functions, supported by H132/HPD mutagenesis and PMID:29719251/36459117. [YAML] Optionally add GO:0005784 Sec61 translocon complex CC to mirror the PN node.

### SERPINH1
- Verdict:** Consistent and high-quality. **Recommended edits:** optionally add GO:0032964 collagen biosynthetic process (KEEP_AS_NON_CORE) to align with PN, since it captures HSP47's ER-upstream role better than the existing GO:0030199 fibril-organization term [YAML]; otherwise no change.

### SGTA
- Verdict:** Consistent; PN adds breadth only, no new defensible term. **Recommended edits:** none required; treat GO:0015031 and GO:0031072 as broader-than-review and do not propagate (gene-level GO:0006620/GO:0071816/GO:0051879 already finer) [MAP].

### SIAH1
- Recommended edits:** [YAML] Add a mitophagy annotation `GO:0000423` (NEW, qualifier involved_in) for the PINK1-SIAH1-SNCAIP PRKN-independent pathway, supported_by the Szargel et al. 2016 HMG paper — first fetch/verify the PMID (Szargel HMG 2016; cache currently lacks it) and add it to `references`; mark UNDECIDED→NEW only after full-text confirmation. [REF] Keep the existing PMID:11863358 WRONG_IDENTIFIER flag (no change); optionally re-anchor the zinc IDA's primary support note to PMID:16085652.

### SPCS1
- Recommended edits:** [MAP] At the "ER signal peptidase" class, prefer GO:0006465 signal peptide processing over GO:0015031 protein transport as the BP projection for accessory subunits (SPCS1/2), reflecting that SPCS1 acts downstream of ER targeting (matches review MODIFY of GO:0045047→GO:0006465).

### SPCS2
- Recommended edits:** [MAP] At the "ER signal peptidase" class, prefer GO:0006465 signal peptide processing over GO:0015031 protein transport as the BP projection for accessory subunits (SPCS1/2). Optionally [REF] note PMID:39565596 (Spc2/SPCS2 substrate-selection) supports a substrate-selectivity contribution beyond bare membership.

### STIP1
- Verdict:** Consistent on the chaperone core but review under-covers the ALP/CMA story PN documents. **Recommended edits:** consider adding GO:0061684 / GO:0061740 / GO:0061738 as KEEP_AS_NON_CORE pending full-text verification of HOP-specific evidence [YAML]; cite the CMA review [REF]. Do not add GO:0031072 (broader, already entailed) [MAP].

### STUB1
- Verdict:** Consistent and high-quality; one warranted addition (aggrephagy). **Recommended edits:** add GO:0035973 aggrephagy as KEEP_AS_NON_CORE supported by CASA literature [YAML]; optionally cite PMID:40796662 / CASA review in references [REF].

### TANK
- Verdict:** OVER-REACH — PN projects GO:0000423 mitophagy (new_to_goa) onto TANK with no support in review/notes; TANK is an indirect regulatory scaffold of TBK1. **Recommended edits:** [MAP] drop/demote TANK's "Autophagy receptor regulation|Mitophagy"→GO:0000423 projection (indirect, single-paper, regulatory-subunit role) — at most a regulation-of-mitophagy context, not a direct mitophagy annotation; do not add to the review without TANK-specific evidence.

### TBK1
- Verdict:** CONSISTENT on biology; PN's bare GO:0000423 mitophagy projection is scope drift for a regulator — review's positive-regulation terms are better. **Recommended edits:** [MAP] for TBK1 the "Autophagy receptor regulation|Mitophagy" node should project a regulation term (GO:1901526 positive regulation of mitophagy, verified real) rather than the bare process GO:0000423; do not add GO:0000423 involved_in to the kinase review.

### TCF25
- Recommended edits:** none required. [YAML] (optional) GO:0006515 protein quality control for misfolded or incompletely synthesized proteins could be added as an `involved_in` process term to better surface TCF25's RQC role (currently only catabolic/regulation/complex terms present); supported by PMID:30244831.

### TRIM13
- Verdict:** Consistent; ERAD/RING already captured; reticulophagy ADD warranted (regulatory framing preferable). **Recommended edits:** [YAML] add GO:0061709 reticulophagy (or GO:0140500 regulation of reticulophagy, matching the regulatory evidence) involved_in, supported by PMID:22178386 — currently new_to_goa and more specific than the existing GO:0016239.

### TRIM16
- Verdict:** Consistent; lysophagy ADD warranted; RING-less caveat correctly handled. **Recommended edits:** [MAP] fix the Lysophagy node rationale — GO:0062093 lysophagy exists; add it as the process target alongside GO:0160247. [YAML] upgrade the review's NEW GO:0030674 adaptor MF to the more specific GO:0160247 autophagy cargo adaptor activity, and add GO:0062093 lysophagy (involved_in, PMID:27693506) as the specific process. [YAML] retain GO:0061630 only as the atypical B-box autoubiquitination capture (do not assert RING catalytic ligase function).

### TRIM17
- Verdict:** Consistent; cargo-adaptor MF upgrade warranted; RING ligase already captured. **Recommended edits:** [YAML] upgrade the GO:0030674 adaptor MF to the more specific GO:0160247 autophagy cargo adaptor activity (supported by PMID:27562068/25127057), scoped to midbody autophagy. [REF] consider adding PMID:22023800 (MCL1/ZWINT, neuronal apoptosis) to references to support the core MCL1-degradation function.

### TRIM5
- Verdict:** Consistent; xenophagy ADD warranted; RING ligase already captured. **Recommended edits:** [YAML] add GO:0098792 xenophagy (involved_in, supported by PMID:25127057) as a more-specific child of the existing autophagy annotation. [YAML] optionally upgrade the GO:0030674 adaptor MF to the more specific GO:0160247 autophagy cargo adaptor activity for the capsid-receptor role.

### TXNDC11
- Recommended edits:** [MAP] Flag TXNDC11 in the "Protein disulfide isomerases" group as a non-canonical reductase: do not propagate GO:0003756 to it; project GO:0015035 protein-disulfide reductase activity instead. [YAML] Optionally tighten the TXNDC11 proposed_new_terms to GO:0097466 (ubiquitin-dependent glycoprotein ERAD pathway) as the precise BP, and drop the GO:0003756 alternative wording in favor of GO:0015035.

### TXNDC16
- Recommended edits:** [MAP] Exclude TXNDC16 (Q9P2K2) from the GO:0003756 protein disulfide isomerase activity projection (redox-inactive PDI-family member, no CXXC) — flag as member-level exception under the "Protein disulfide isomerases" group, do NOT project to GOA. [YAML] none required (review correctly omits a catalytic MF).

### UBAC2
- Recommended edits:** [YAML] add GO:0000151 ubiquitin ligase complex (part_of; LMBR1L-AMFR/GP78-UBAC2 complex, PMID:31073040) as a non-core CC — currently absent from the review. [MAP] none — node mapping is correct; complex (not catalytic) target for the non-catalytic subunit is the right call.

### UFSP1
- Recommended edits:** [MAP] do not project group-level GO:0006515 (PQC for misfolded/incompletely synthesized proteins) onto UFSP1 — UFSP1 is a cytosolic UFM1-maturation/deUFMylase enzyme, not a ribosome-associated misfolded-protein QC factor (contrast UFSP2/RPL26).

### UFSP2
- Recommended edits:** [MAP] the RQC-group GO:0006515 projection is acceptable for UFSP2 but redundant/broader than the review's existing GO:0072344 (rescue of stalled cytosolic ribosome) and GO:0032790 (ribosome disassembly); prefer those narrower IDA-supported terms when representing UFSP2's RQC role.

### UPF1
- Recommended edits:** [MAP] for UPF1, replace/avoid the group projection GO:0006415 (translational termination, = peptide release) with GO:0006449 (regulation of translational termination), which is already in UPF1 GOA and is the accurate frame; UPF1's core remains NMD (GO:0000184) + RNA helicase (GO:0003724).

### UPF2
- Recommended edits:** [MAP] do NOT project GO:0006415 (translational termination) onto UPF2 — it is an NMD adaptor recruited downstream of termination, not a peptide-release factor; the type-level `no_mapping` should win. UPF2 is already correctly anchored on GO:0000184 (NMD).

### UPF3A
- Recommended edits:** [MAP] do NOT project GO:0006415 (translational termination) onto UPF3A; UPF3A is a partial NMD antagonist (negated GO:0000184; GO:2000623 negative regulation of NMD; GO:0140311 sequestering). The type-level `no_mapping` should win, and any node-level frame must respect its negative/antagonist directionality.

### UPF3B
- Recommended edits:** [MAP] do NOT project GO:0006415 (translational termination) onto UPF3B — it is an EJC/NMD adaptor acting downstream of termination, already correctly anchored on GO:0000184 and GO:2000624 (positive regulation of NMD). Type-level `no_mapping` should win.
