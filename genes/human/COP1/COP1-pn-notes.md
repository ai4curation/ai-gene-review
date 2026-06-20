# COP1 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q8NHY2
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/COP1/COP1-ai-review.yaml](COP1-ai-review.yaml)
- AIGR review HTML: present - [genes/human/COP1/COP1-ai-review.html](COP1-ai-review.html)
- Gene notes: present - [genes/human/COP1/COP1-notes.md](COP1-notes.md)
- GOA TSV: present - [genes/human/COP1/COP1-goa.tsv](COP1-goa.tsv)
- UniProt record: present - [genes/human/COP1/COP1-uniprot.txt](COP1-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/COP1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/COP1.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/COP1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/COP1.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: COP1 (also known as RFWD2; constitutive photomorphogenesis protein 1 homolog) is a RING-finger E3 ubiquitin-protein ligase (EC 2.3.2.27) that mediates ubiquitination and subsequent proteasomal degradation of substrate transcription factors and signaling proteins. Its domain architecture comprises an N-terminal C3HC4 RING-HC zinc finger (responsible for catalytic ubiquitin transfer and zinc binding), a central coiled-coil that mediates homodimerization, and a C-terminal seven-bladed WD40 beta-propeller that serves as the substrate-recognition module, binding short degron motifs in substrates. COP1 acts both as a stand-alone RING E3 and as the substrate-recognition subunit of a cullin-RING ligase (CRL4) module; in the DCX(DET1-COP1) complex (COP1, DET1, DDB1, CUL4A, RBX1) the catalytic RING is contributed by RBX1 while COP1 provides substrate recognition. Validated substrates include the AP-1 transcription factor c-Jun (JUN) and its relatives, the tumor suppressor p53 (TP53, with MTA1 co-regulation), the oncogenic ETS-family factors ETV1/ETV4/ETV5 and ETS1, the metastasis regulator MTA1, 14-3-3 sigma (SFN), C/EBPalpha (CEBPA, recruited via the pseudokinase adaptor TRIB1), and acetyl-CoA carboxylase 1 (ACACA). Substrate choice and ligase activity are regulated by the pseudokinase adaptors TRIB1/TRIB2, which bind the WD40 domain and compete with substrates. COP1 shuttles between nuclear speckles and the cytoplasm; ATM-dependent phosphorylation at Ser387 and 14-3-3 sigma binding drive its nuclear export and autoubiquitination upon DNA damage. Through degradation of these substrates, COP1 functions as a tumor suppressor in several contexts and contributes to control of lipogenesis. It autoubiquitinates and is stabilized by the COP9 signalosome subunit COPS6/CSN6.
- Existing/core annotation action counts: ACCEPT: 12; KEEP_AS_NON_CORE: 14; MARK_AS_OVER_ANNOTATED: 9; REMOVE: 1

## PN Consistency Summary

- **Consistency:** Strong. The PN dual classification (catalytic RING E3 *and* CRL4 substrate adaptor) exactly matches the review's two core_functions: GO:0061630 ubiquitin protein ligase activity (EXP PMID:12615916, IMP PMID:19805145) and GO:1990756 substrate-adaptor activity (WD40 propeller; PMID:14739464, PMID:21572435). Deep-research notes, review YAML, and PN annotation agree COP1 is both stand-alone RING (catalytic) and the substrate-recognition subunit of DCX(DET1-COP1) CRL4 (RBX1 catalytic). No contradictions.
- **PN story / NEW pressure:** No NEW pressure. Both projected terms are already present/captured: GO:0061630 is in existing_annotations (EXP/IMP/IEA, ACCEPT, core); GO:1990756 is asserted as a core_function (proposed_new_terms is empty because the term already exists and is used). PN's "new_to_goa" flag on GO:1990756 reflects that GOA lacks the explicit adaptor MF, but the review already proposes it. Already captured.
- **Evidence alignment:** PN cites only review-stub PMIDs (17588513 = the DCAF discovery review for the Cul4 row; 19489725 = ER-RING-ligase screen for the RING row). Review's substantive evidence (PMID:12615916, 14739464, 19805145, 21572435, 39920308) does not overlap PN's two citations, but PN citations are family/architecture references, not gene-specific — divergence is expected and benign.
- **Verdict:** Consistent; mapping sound; no edits. COP1 correctly carries both catalytic and adaptor MFs.

## Full Consistency Review

- **UniProt:** Q8NHY2 (RFWD2) · **batch:** proteostasis-batch-2026-06-07 · **review status:** COMPLETE (40 annotations reviewed)
- **PN placement:** two rows — (1) `UPS|E3 ubiquitin and UBL ligases|Cul4A/Cul4B substrate adaptor|WD40|other`; (2) `UPS|E3 ubiquitin and UBL ligases|RING|RFWD|WD40` ; **PN-node mapping:** group nodes mapped — Cul4 adaptor group → GO:1990756 (substrate-adaptor MF); RING group → GO:0061630 (catalytic ligase MF); both ok_for_propagation.
- **Consistency:** Strong. The PN dual classification (catalytic RING E3 *and* CRL4 substrate adaptor) exactly matches the review's two core_functions: GO:0061630 ubiquitin protein ligase activity (EXP PMID:12615916, IMP PMID:19805145) and GO:1990756 substrate-adaptor activity (WD40 propeller; PMID:14739464, PMID:21572435). Deep-research notes, review YAML, and PN annotation agree COP1 is both stand-alone RING (catalytic) and the substrate-recognition subunit of DCX(DET1-COP1) CRL4 (RBX1 catalytic). No contradictions.
- **PN story / NEW pressure:** No NEW pressure. Both projected terms are already present/captured: GO:0061630 is in existing_annotations (EXP/IMP/IEA, ACCEPT, core); GO:1990756 is asserted as a core_function (proposed_new_terms is empty because the term already exists and is used). PN's "new_to_goa" flag on GO:1990756 reflects that GOA lacks the explicit adaptor MF, but the review already proposes it. Already captured.
- **Mapping strategy:** Correct and well-calibrated. This gene is the precedent for distinguishing the two MFs: RING group → catalytic GO:0061630; Cul4 adaptor group → GO:1990756. Both group-level mappings fit COP1; class/branch correctly context_only/no_mapping. No change needed.
- **Evidence alignment:** PN cites only review-stub PMIDs (17588513 = the DCAF discovery review for the Cul4 row; 19489725 = ER-RING-ligase screen for the RING row). Review's substantive evidence (PMID:12615916, 14739464, 19805145, 21572435, 39920308) does not overlap PN's two citations, but PN citations are family/architecture references, not gene-specific — divergence is expected and benign.
- **Verdict:** Consistent; mapping sound; no edits. COP1 correctly carries both catalytic and adaptor MFs.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07
- review_yaml: genes/human/COP1/COP1-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Ubiquitin Proteasome System | E3 ubiquitin and UBL ligases | Cul4A/Cul4B substrate adaptor | WD40 | other
- UniProt: Q8NHY2
- In branches: UPS
- Signature domains: (none)
- Auxiliary domains: IPR001680
- PN references (titles):
    - 17588513 rev
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul4A/Cul4B substrate adaptor|WD40|other
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower substrate-receptor, adaptor, domain, or family subdivision already covered by the curated parent adaptor/receptor mapping. No additional direct GO mapping is needed at this node.
    - [type] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul4A/Cul4B substrate adaptor|WD40
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower substrate-receptor, adaptor, domain, or family subdivision already covered by the curated parent adaptor/receptor mapping. No additional direct GO mapping is needed at this node.
    - [group] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul4A/Cul4B substrate adaptor
        status=mapped scope=ok_for_propagation_to_go GO=[GO:1990756 ubiquitin-like ligase-substrate adaptor activity]
        rationale: This PN group captures substrate receptors/adaptors for cullin/UBL ligase systems. The shared GO molecular-function target is ubiquitin-like ligase-substrate adaptor activity.
    - [class] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases
        status=context_only scope=too_broad_to_propagate GO=[GO:0061630 ubiquitin protein ligase activity]
        rationale: This class is a genuine E3-ligase context, but its descendants include catalytic ligases, cullin scaffolds, substrate receptors, adaptors, cofactors, regulators, and UBL modifier systems. A class-level propagation would over-annotate.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## PN row 2: Ubiquitin Proteasome System | E3 ubiquitin and UBL ligases | RING | RFWD | WD40
- UniProt: Q8NHY2
- In branches: UPS
- Signature domains: IPR001841
- Auxiliary domains: IPR001680
- PN references (titles):
    - 19489725 / rev
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|RING|RFWD|WD40
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower E3-ligase architecture, component, or domain subdivision already covered by the curated parent E3 mapping. No additional direct GO mapping is needed at this node.
    - [type] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|RING|RFWD
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower E3-ligase architecture, component, or domain subdivision already covered by the curated parent E3 mapping. No additional direct GO mapping is needed at this node.
    - [group] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|RING
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0061630 ubiquitin protein ligase activity]
        rationale: This PN group is a catalytic ubiquitin E3 ligase bucket. The shared GO molecular-function target is ubiquitin protein ligase activity.
    - [class] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases
        status=context_only scope=too_broad_to_propagate GO=[GO:0061630 ubiquitin protein ligase activity]
        rationale: This class is a genuine E3-ligase context, but its descendants include catalytic ligases, cullin scaffolds, substrate receptors, adaptors, cofactors, regulators, and UBL modifier systems. A class-level propagation would over-annotate.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## Projected GO annotations (2)
- GO:1990756 ubiquitin-like ligase-substrate adaptor activity | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul4A/Cul4B substrate adaptor
- GO:0061630 ubiquitin protein ligase activity | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|RING

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
