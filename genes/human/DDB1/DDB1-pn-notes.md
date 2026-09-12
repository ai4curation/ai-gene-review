# DDB1 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q16531
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-13
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/DDB1/DDB1-ai-review.yaml](DDB1-ai-review.yaml)
- AIGR review HTML: missing - genes/human/DDB1/DDB1-ai-review.html
- Gene notes: missing - genes/human/DDB1/DDB1-notes.md
- GOA TSV: present - [genes/human/DDB1/DDB1-goa.tsv](DDB1-goa.tsv)
- UniProt record: present - [genes/human/DDB1/DDB1-uniprot.txt](DDB1-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/DDB1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/DDB1.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/DDB1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/DDB1.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/DDB1/DDB1-deep-research-falcon.md](DDB1-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: DDB1 (DNA damage-binding protein 1; p127, UV-DDB1, XAP-1) is a large (1140 aa) WD40 beta-propeller protein built from three seven-bladed beta-propeller domains (BPA, BPB and BPC) that serves as the central adaptor of CUL4-RING E3 ubiquitin ligases (CRL4). Its BPB propeller docks onto the N-terminus of the cullin scaffold CUL4A or CUL4B (assembled with the RING protein RBX1/ROC1), while a cleft between the BPA and BPC propellers, together with a helix-loop-helix (H-box) surface, captures a large family of interchangeable substrate-receptor subunits known as DCAFs (DDB1- and CUL4-associated factors), most of which engage DDB1 through a conserved WDxR motif on their own WD40 propeller. DDB1 itself is not catalytic and is not the direct nucleic-acid-binding subunit; by interchanging DCAF receptors it confers substrate specificity on numerous distinct DCX (DDB1-CUL4-X-box) ligase complexes that ubiquitinate and target their substrates for proteasomal degradation, and cullin-RING ligases as a class account for roughly a fifth of regulated proteasomal protein turnover. Systematic interactome studies (BioID/AP-MS/pulse-SILAC) indicate that only a minority of candidate WD40 proteins are bona fide DDB1/CUL4 receptors under any given condition, so DDB1's functional output is strongly context- and stimulus-dependent and is largely encoded by which DCAF is conditionally recruited. Structurally, DDB1's BPB propeller binds the CUL4 N-terminus while the BPA-BPC double-propeller cleft (with an H-box helical surface) captures receptors and viral hijackers; receptors that are intrinsically disordered (e.g. AMBRA1) become stabilized upon DDB1 engagement. With its dedicated receptor DDB2, DDB1 forms the UV-DDB complex that recognizes UV-induced photolesions (cyclobutane pyrimidine dimers and 6-4 photoproducts), apurinic sites and mismatches in chromatin and initiates global-genome nucleotide excision repair, in part by ubiquitinating histones (H2A, H3, H4) and XPC at damage sites; in a noncanonical capacity UV-DDB also stimulates base-excision-repair enzymes (e.g. OGG1, MUTYH, APE1 and the glycosylase SMUG1), promoting turnover of oxidative DNA lesions. With the DCAF ERCC8/CSA, DDB1-CUL4 contributes to transcription-coupled repair by ubiquitinating stalled RNA polymerase II and CSB/ERCC6. Other DDB1-CUL4 complexes regulate DNA replication licensing (CDT1, p21 via DTL/CDT2), cell-cycle progression through the DCAF AMBRA1 (which directs ubiquitination of cyclin D/cyclin D1), the circadian clock (CRY1), histone methylation, and many additional substrates. DDB1 is predominantly cytoplasmic at steady state and translocates to the nucleus after UV irradiation, accumulating at sites of DNA damage; the two cullin scaffolds it uses show partitioning tendencies (CUL4B largely nuclear, CUL4A more cytoplasmic) so that DDB1-containing CRL4 assemblies can act in distinct compartments depending on scaffold usage. It is a frequent target of viral hijacking (e.g. paramyxovirus V, HBV HBx, HIV Vpr/Vpx, HCMV proteins), which redirect CRL4 toward host antiviral or restriction factors; during influenza A virus infection the CRL4 interactome is rewired and DDB1 (with DCAF11/DCAF12L1) participates in non-degradative polyubiquitination of the viral polymerase subunit PB2. DDB1 is also the platform exploited by thalidomide/lenalidomide molecular-glue degraders acting through the DCAF cereblon (CRBN) and, more broadly, is an actionable induced-proximity node for targeted protein degradation, with surface residues such as Arg928 (a validated molecular-glue hotspot, e.g. in CDK12-cyclin K degrader ternary complexes) and Cys173 (engaged by covalent DDB1 recruiters) used to direct CRL4-dependent degradation of clinically relevant proteins including BRD4 and the androgen receptor. Monoallelic de novo DDB1 missense variants cause a recessive-DNA-repair-related neurodevelopmental syndrome (WHIKERS).
- Existing/core annotation action counts: ACCEPT: 91; KEEP_AS_NON_CORE: 121; MARK_AS_OVER_ANNOTATED: 3; REMOVE: 1

## PN Consistency Summary

- **Consistency:** Mostly consistent on biology (central CRL4 adaptor/scaffold; UV-DDB NER; AMBRA1/BECN1 K63 ubiquitination role appears in the description), but a **mapping-category contradiction**: the review correctly classifies DDB1 as a SCAFFOLD and uses GO:0160072 (ubiquitin ligase complex scaffold activity) + GO:0030674 as its core MF, whereas the PN "Cullin adaptor" node maps it to GO:1990756 (substrate-adaptor activity). Those are different MF categories.
- **PN story / NEW pressure:** PN projects GO:1990756 as "more_specific_than_existing_goa," but DDB1's GOA ALREADY contains the correct GO:0160072 (scaffold, IDA) and GO:0030674 (both verified real via OLS); the review ACCEPTs GO:0160072 as core. GO:1990756 (defn: brings ligase together with its SUBSTRATE; F-box/BTB proteins) is biologically wrong for DDB1 — DDB1 bridges CUL4 to DCAF receptors (scaffold), it is not the substrate receptor. Verdict: over-reaches / already captured by the better GO:0160072.
- **Evidence alignment:** Partial. PN UPS refs 19337321 / 19276361 (DCAF-discovery papers) are not individually in the review reference list, though the review cites the cognate DCAF/CUL4-DDB1 framework (PMID:16949367 and many complex-membership PMIDs). PN ALP ref (AMBRA1 review, tandfonline) is not in the review references; the AMBRA1-CRL4-BECN1 story is in the description but not anchored to that PMID.
- **Verdict:** Biology consistent but PN MF mapping mis-categorized. **Recommended edits:** [MAP] retarget DDB1 "Cullin adaptor" node from GO:1990756 to GO:0160072 (scaffold), matching the review's accepted MF and existing GOA.

## Full Consistency Review

- **UniProt:** Q16531 · **batch:** proteostasis-batch-2026-06-13 · **review status:** COMPLETE
- **PN placement:** two rows — (1) `ALP|Autophagophore initiation and elongation|Class 3 PI3K complex 1, direct|Modulator of class 3 PI3K complex 1 activity|Modulator of BECN1 ubiquitination` (all context_only, too_broad: GO:0035032 / GO:0016236); (2) `UPS|E3 ubiquitin and UBL ligases|Cullin adaptor|DDB1` ; **PN-node mapping (UPS):** group "Cullin adaptor"=mapped, ok_for_propagation, **GO:1990756** (substrate-adaptor MF); projected goa_status=more_specific_than_existing_goa.
- **Consistency:** Mostly consistent on biology (central CRL4 adaptor/scaffold; UV-DDB NER; AMBRA1/BECN1 K63 ubiquitination role appears in the description), but a **mapping-category contradiction**: the review correctly classifies DDB1 as a SCAFFOLD and uses GO:0160072 (ubiquitin ligase complex scaffold activity) + GO:0030674 as its core MF, whereas the PN "Cullin adaptor" node maps it to GO:1990756 (substrate-adaptor activity). Those are different MF categories.
- **PN story / NEW pressure:** PN projects GO:1990756 as "more_specific_than_existing_goa," but DDB1's GOA ALREADY contains the correct GO:0160072 (scaffold, IDA) and GO:0030674 (both verified real via OLS); the review ACCEPTs GO:0160072 as core. GO:1990756 (defn: brings ligase together with its SUBSTRATE; F-box/BTB proteins) is biologically wrong for DDB1 — DDB1 bridges CUL4 to DCAF receptors (scaffold), it is not the substrate receptor. Verdict: over-reaches / already captured by the better GO:0160072.
- **Mapping strategy:** This gene SHOULD change the node. DDB1 is the scaffold that the DCAF receptors dock onto; GO:1990756 is the receptor MF. Recommend the "Cullin adaptor"/DDB1 node target GO:0160072, not GO:1990756 (parallels the DDA1 "receptor scaffold" node which correctly uses GO:0160072).
- **Evidence alignment:** Partial. PN UPS refs 19337321 / 19276361 (DCAF-discovery papers) are not individually in the review reference list, though the review cites the cognate DCAF/CUL4-DDB1 framework (PMID:16949367 and many complex-membership PMIDs). PN ALP ref (AMBRA1 review, tandfonline) is not in the review references; the AMBRA1-CRL4-BECN1 story is in the description but not anchored to that PMID.
- **Verdict:** Biology consistent but PN MF mapping mis-categorized. **Recommended edits:** [MAP] retarget DDB1 "Cullin adaptor" node from GO:1990756 to GO:0160072 (scaffold), matching the review's accepted MF and existing GOA.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-13
- review_yaml: genes/human/DDB1/DDB1-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Autophagy-Lysosome Pathway | Autophagophore initiation and elongation | Class 3 PI3K complex 1, direct | Modulator of class 3 PI3K complex 1 activity | Modulator of BECN1 ubiquitination
- UniProt: Q16531
- In branches: ALP, UPS
- Notes: CUL4A/B-DDB1-AMBRA1 complex mediates K63 ubiquitination of BECN1, increasing activity of VPS34
- PN references (titles):
    - Full article: Connecting autophagy: AMBRA1 and its network of regulation (tandfonline.com)
- PN-node mapping records (path + ancestors):
    - [subtype] Autophagy-Lysosome Pathway|Autophagophore initiation and elongation|Class 3 PI3K complex 1, direct|Modulator of class 3 PI3K complex 1 activity|Modulator of BECN1 ubiquitination
        status=context_only scope=too_broad_to_propagate GO=[GO:0035032 phosphatidylinositol 3-kinase complex, class III]
        rationale: Reviewed as a class-III PI3K complex context or regulator bucket. This node is useful for curator interpretation, but it should not project cellular-component membership; only explicit complex-component leaves propagate to GO complex terms.
    - [type] Autophagy-Lysosome Pathway|Autophagophore initiation and elongation|Class 3 PI3K complex 1, direct|Modulator of class 3 PI3K complex 1 activity
        status=context_only scope=too_broad_to_propagate GO=[GO:0035032 phosphatidylinositol 3-kinase complex, class III]
        rationale: Reviewed as a class-III PI3K complex context or regulator bucket. This node is useful for curator interpretation, but it should not project cellular-component membership; only explicit complex-component leaves propagate to GO complex terms.
    - [group] Autophagy-Lysosome Pathway|Autophagophore initiation and elongation|Class 3 PI3K complex 1, direct
        status=context_only scope=too_broad_to_propagate GO=[GO:0035032 phosphatidylinositol 3-kinase complex, class III]
        rationale: Reviewed as a class-III PI3K complex context or regulator bucket. This node is useful for curator interpretation, but it should not project cellular-component membership; only explicit complex-component leaves propagate to GO complex terms.
    - [class] Autophagy-Lysosome Pathway|Autophagophore initiation and elongation
        status=context_only scope=too_broad_to_propagate GO=[GO:0016236 macroautophagy]
        rationale: This class is a real macroautophagy context, but its descendants include core factors, component buckets, upstream modulators, localization roles, and residual categories. Projecting generic macroautophagy from this ancestor creates TRAPP-like overpropagation, so candidate GO annotations must come from narrower curated nodes.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## PN row 2: Ubiquitin Proteasome System | E3 ubiquitin and UBL ligases | Cullin adaptor | DDB1
- UniProt: Q16531
- In branches: ALP, UPS
- Signature domains: (none)
- Auxiliary domains: IPR015943
- PN references (titles):
    - 19337321
    - 19276361
- PN-node mapping records (path + ancestors):
    - [type] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cullin adaptor|DDB1
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower substrate-receptor, adaptor, domain, or family subdivision already covered by the curated parent adaptor/receptor mapping. No additional direct GO mapping is needed at this node.
    - [group] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cullin adaptor
        status=mapped scope=ok_for_propagation_to_go GO=[GO:1990756 ubiquitin-like ligase-substrate adaptor activity]
        rationale: This PN group captures substrate receptors/adaptors for cullin/UBL ligase systems. The shared GO molecular-function target is ubiquitin-like ligase-substrate adaptor activity.
    - [class] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases
        status=context_only scope=too_broad_to_propagate GO=[GO:0061630 ubiquitin protein ligase activity]
        rationale: This class is a genuine E3-ligase context, but its descendants include catalytic ligases, cullin scaffolds, substrate receptors, adaptors, cofactors, regulators, and UBL modifier systems. A class-level propagation would over-annotate.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## Projected GO annotations (1)
- GO:1990756 ubiquitin-like ligase-substrate adaptor activity | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cullin adaptor

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
