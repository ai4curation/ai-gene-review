# UFD1 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q92890
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07c
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/UFD1/UFD1-ai-review.yaml](UFD1-ai-review.yaml)
- AIGR review HTML: present - [genes/human/UFD1/UFD1-ai-review.html](UFD1-ai-review.html)
- Gene notes: present - [genes/human/UFD1/UFD1-notes.md](UFD1-notes.md)
- GOA TSV: present - [genes/human/UFD1/UFD1-goa.tsv](UFD1-goa.tsv)
- UniProt record: present - [genes/human/UFD1/UFD1-uniprot.txt](UFD1-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/UFD1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/UFD1.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/UFD1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/UFD1.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: UFD1 (Ubiquitin recognition factor in ER-associated degradation protein 1; also UFD1L, ubiquitin fusion degradation protein 1) is an essential ubiquitin-binding cofactor of the AAA+ ATPase VCP/p97. It forms the obligate UFD1-NPL4 heterodimer, the principal substrate-recruiting adaptor of p97, and with VCP constitutes the VCP-NPL4-UFD1 segregase. UFD1 binds (poly)ubiquitin and, together with NPL4, recognizes ubiquitinated substrates and presents them to p97 for ATP-driven extraction and unfolding, after which they are degraded by the proteasome. The complex is central to endoplasmic-reticulum-associated degradation (ERAD), driving retrotranslocation of misfolded proteins from the ER to the cytosol, and participates in many other p97-dependent processes including the cellular response to misfolded proteins, ribosome-associated quality control, spindle disassembly and nuclear-envelope reformation at the end of mitosis, and Golgi membrane reassembly. UFD1 also contributes to a non-canonical p97 function in innate immunity, acting (with NPLOC4/VCP) as a negative regulator of type I interferon production by binding RIG-I (RIGI) and recruiting RNF125 for its degradation, and it couples the ER stress response to cell-cycle control via interaction with USP13. The gene lies within the 3q29 / DiGeorge (22q11)-associated genomic context and is developmentally expressed. UFD1 localizes to the cytosol, ER and nucleus.
- Existing/core annotation action counts: ACCEPT: 31; KEEP_AS_NON_CORE: 27; REMOVE: 1

## PN Consistency Summary

- **Consistency:** Strong. Notes/review/PN agree UFD1 is the p97/VCP ubiquitin-binding cofactor (UFD1-NPL4 heterodimer; ERAD retrotranslocation; also RQC, mitosis, immunity). NOTE: UFD1 is NOT a UFMylation-cascade member despite the name similarity — it is "ubiquitin fusion degradation 1," a p97 adaptor. The review/PN both treat it correctly as a UPS/ERAD/VCP gene; no false UFM1 conflation. Review ACCEPTs GO:0036503, GO:0034098 (8x in GOA), GO:0031593, GO:0030970, GO:0036501 (UFD1-NPL4 complex), GO:0036435 (K48-polyUb binding). No contradictions.
- **PN story / NEW pressure:** Well captured. GO:0036503 (ERAD) and GO:0034098 (complex) are in GOA/review. PN's GO:0097466 (ubiquitin-dependent glycoprotein ERAD pathway; verify before any add) is flagged more_specific_than_existing — UFD1 is a general ERAD adaptor, not glycoprotein-specific, so this projection over-reaches. PN RQC type is correctly no_mapping; review captures RQC via GO:0072344 (NAS) + GO:1990116 as KEEP_AS_NON_CORE. The MF core GO:0031593 (polyubiquitin-modification-dependent protein binding) is annotated. Conclusion: **already captured**; GO:0097466 over-reaches.
- **Evidence alignment:** PN cites PMID:28451587 (SHP motif) and 36736315 (IPR055417 domain) — neither in review YAML (domain/signature citations); review uses UniProt + p97/ERAD literature. Divergence is benign; no shared functional PMID but no conflict.
- **Verdict:** Consistent and complete; correctly handled as a p97/ERAD adaptor (not a UFMylation gene). PN GO:0036503/GO:0034098 match the review; PN's glycoprotein-specific GO:0097466 over-reaches — keep general ERAD.

## Full Consistency Review

- **UniProt:** Q92890 · **batch:** proteostasis-batch-2026-06-07c · **review status:** complete (2 core_functions, both GO:0031593; large protein-binding set triaged)
- **PN placement:** `ER proteostasis|...|ER associated degradation|VCP system for retrotranslocation in ERAD|VCP accessories`; `Translation|...|Ribosome-associated QC|VCP system for RQC`; `UPS|VCP and associated proteins|adaptors|SHP|UT3`; `UPS|Ubiquitin and UBL binding|protein quality control|ERAD cofactor|...UT3` ; **PN-node mapping:** ERAD group→GO:0036503 (exact); SHP/UT3 subtype→GO:0034098 (VCP-NPL4-UFD1 complex); ERAD-cofactor type→GO:0097466 (glycoprotein ERAD, more_specific_than_existing); RQC type→no_mapping.
- **Consistency:** Strong. Notes/review/PN agree UFD1 is the p97/VCP ubiquitin-binding cofactor (UFD1-NPL4 heterodimer; ERAD retrotranslocation; also RQC, mitosis, immunity). NOTE: UFD1 is NOT a UFMylation-cascade member despite the name similarity — it is "ubiquitin fusion degradation 1," a p97 adaptor. The review/PN both treat it correctly as a UPS/ERAD/VCP gene; no false UFM1 conflation. Review ACCEPTs GO:0036503, GO:0034098 (8x in GOA), GO:0031593, GO:0030970, GO:0036501 (UFD1-NPL4 complex), GO:0036435 (K48-polyUb binding). No contradictions.
- **PN story / NEW pressure:** Well captured. GO:0036503 (ERAD) and GO:0034098 (complex) are in GOA/review. PN's GO:0097466 (ubiquitin-dependent glycoprotein ERAD pathway; verify before any add) is flagged more_specific_than_existing — UFD1 is a general ERAD adaptor, not glycoprotein-specific, so this projection over-reaches. PN RQC type is correctly no_mapping; review captures RQC via GO:0072344 (NAS) + GO:1990116 as KEEP_AS_NON_CORE. The MF core GO:0031593 (polyubiquitin-modification-dependent protein binding) is annotated. Conclusion: **already captured**; GO:0097466 over-reaches.
- **Mapping strategy:** PN node is sound: ERAD group→GO:0036503 exact and the SHP/UT3 subtype→GO:0034098 complex are precise and match the review. The only caution is the ERAD-cofactor type→GO:0097466 (glycoprotein-specific) being narrower/skewed vs UFD1's general adaptor role — keep ERAD at GO:0036503, do not propagate the glycoprotein-specific child. UFD1 does not change the node.
- **Evidence alignment:** PN cites PMID:28451587 (SHP motif) and 36736315 (IPR055417 domain) — neither in review YAML (domain/signature citations); review uses UniProt + p97/ERAD literature. Divergence is benign; no shared functional PMID but no conflict.
- **Verdict:** Consistent and complete; correctly handled as a p97/ERAD adaptor (not a UFMylation gene). PN GO:0036503/GO:0034098 match the review; PN's glycoprotein-specific GO:0097466 over-reaches — keep general ERAD.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07c
- review_yaml: genes/human/UFD1/UFD1-ai-review.yaml
- PN workbook rows: 4

## PN row 1: ER proteostasis | Organelle-specific protein degradation | ER associated degradation | VCP system for retrotranslocation in ERAD | VCP accessories
- UniProt: Q92890
- In branches: ER, TR, UPS
- PN-node mapping records (path + ancestors):
    - [subtype] ER proteostasis|Organelle-specific protein degradation|ER associated degradation|VCP system for retrotranslocation in ERAD|VCP accessories
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a single GO class. The member genes span multiple activities, complexes, or contexts, so direct propagation from this node would overstate the shared biology.
    - [type] ER proteostasis|Organelle-specific protein degradation|ER associated degradation|VCP system for retrotranslocation in ERAD
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0036503 ERAD pathway]
        rationale: This PN type captures the VCP/p97-dependent retrotranslocation machinery used in ERAD. It is not a separate process from ERAD, but a core mechanistic subsystem within it.
    - [group] ER proteostasis|Organelle-specific protein degradation|ER associated degradation
        status=mapped scope=exact GO=[GO:0036503 ERAD pathway]
        rationale: The PN group "ER associated degradation" is a direct lexical and biological match to the GO ERAD pathway term. The additional branch and class context disambiguates the source string from any broader degradation language.
    - [class] ER proteostasis|Organelle-specific protein degradation
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a single GO class. The member genes span multiple activities, complexes, or contexts, so direct propagation from this node would overstate the shared biology.
    - [branch] ER proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## PN row 2: Translation | Cytosolic translation | Ribosome-associated QC | VCP system for RQC
- UniProt: Q92890
- In branches: ER, TR, UPS
- PN-node mapping records (path + ancestors):
    - [type] Translation|Cytosolic translation|Ribosome-associated QC|VCP system for RQC
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a single GO class. The member genes span multiple activities, complexes, or contexts, so direct propagation from this node would overstate the shared biology.
    - [group] Translation|Cytosolic translation|Ribosome-associated QC
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0006515 protein quality control for misfolded or incompletely synthesized proteins]
        rationale: The PN ribosome-associated quality-control group covers surveillance and disposal of stalled or defective nascent-chain translation products. GO lacks a dedicated ribosome-associated QC term in the local cache, so the broader protein-quality-control process is the best supported target.
    - [class] Translation|Cytosolic translation
        status=context_only scope=too_broad_to_propagate GO=[GO:0002181 cytoplasmic translation]
        rationale: The PN class Cytosolic translation is centered on the cytoplasmic translation apparatus and process, but it also houses supporting machinery such as ribosome biogenesis factors. The GO process term is a useful high-level label for the class, but propagating it to all members would over-annotate genes whose PN placement is through assembly or maturation context rather than core cytoplasmic translation.
    - [branch] Translation
        status=context_only scope=too_broad_to_propagate GO=[GO:0006412 translation]
        rationale: The PN Translation branch is organized around the translation apparatus and immediately associated cotranslational quality-control systems. GO translation is the closest high-level process label, but the PN branch also contains adjacent machinery such as ribosome biogenesis and nascent-chain handling. Keeping this relationship is useful for interpretation, but it is too broad to project safely onto every member.

## PN row 3: Ubiquitin Proteasome System | VCP and associated proteins | adaptors | SHP | UT3
- UniProt: Q92890
- In branches: ER, TR, UPS
- Signature domains: PMID: 28451587 (SHP)
- Auxiliary domains: IPR042299
- PN references (titles):
    - 28451587
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|VCP and associated proteins|adaptors|SHP|UT3
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0034098 VCP-NPL4-UFD1 AAA ATPase complex]
        rationale: This PN subtype identifies UFD1 in the canonical VCP-NPL4-UFD1 adaptor complex. The matching GO cellular-component term is VCP-NPL4-UFD1 AAA ATPase complex.
    - [type] Ubiquitin Proteasome System|VCP and associated proteins|adaptors|SHP
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a VCP-adaptor motif or architecture subdivision. The label is useful taxonomy but too indirect for direct GO propagation without gene-level evidence.
    - [group] Ubiquitin Proteasome System|VCP and associated proteins|adaptors
        status=context_only scope=too_broad_to_propagate GO=[GO:0034098 VCP-NPL4-UFD1 AAA ATPase complex]
        rationale: This PN group records VCP adaptor context, but it mixes UBX, SHP, VIM, VBM, membrane, and other adaptor classes. Direct propagation should come only from narrower complex-specific nodes or gene-level review.
    - [class] Ubiquitin Proteasome System|VCP and associated proteins
        status=context_only scope=too_broad_to_propagate GO=[GO:0043335 protein unfolding]
        rationale: This class records the VCP segregase branch context, but descendants include VCP, substrate adaptors, DUBs, E3 ligases, channels, and unrelated associated enzymes. Direct propagation is restricted to narrower nodes.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## PN row 4: Ubiquitin Proteasome System | Ubiquitin and UBL binding | protein quality control | ERAD cofactor | idiosyncratic Ub binding / UT3
- UniProt: Q92890
- In branches: ER, TR, UPS
- Signature domains: PMID: 36736315 (IPR055417)
- Auxiliary domains: (none)
- PN references (titles):
    - 36736315
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|Ubiquitin and UBL binding|protein quality control|ERAD cofactor|idiosyncratic Ub binding / UT3
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a family, domain, architecture, or residual subdivision. The label is useful for PN taxonomy navigation but is not itself a GO annotation target; any functional assertion should come from a curated parent role or gene-level evidence.
    - [type] Ubiquitin Proteasome System|Ubiquitin and UBL binding|protein quality control|ERAD cofactor
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0097466 ubiquitin-dependent glycoprotein ERAD pathway]
        rationale: This PN type groups ubiquitin/UBL-binding factors that act as ERAD cofactors in protein-quality-control contexts. The best available GO target in the local cache is ubiquitin-dependent glycoprotein ERAD pathway, used here at propagation scope.
    - [group] Ubiquitin Proteasome System|Ubiquitin and UBL binding|protein quality control
        status=context_only scope=too_broad_to_propagate GO=[GO:0043161 proteasome-mediated ubiquitin-dependent protein catabolic process]
        rationale: This PN group is a protein-quality-control context bucket, but its descendants include ERAD cofactors, HSP70 cochaperone context, stalled-chain recognition, and other mixed roles. Direct propagation should come from narrower nodes such as ERAD cofactor.
    - [class] Ubiquitin Proteasome System|Ubiquitin and UBL binding
        status=context_only scope=too_broad_to_propagate GO=[GO:0140036 ubiquitin-modified protein reader activity]
        rationale: This class records ubiquitin/UBL-reader context, but the subtree mixes ubiquitin, SUMO, UBL-domain, domain-architecture, catalytic, signaling, trafficking, and nucleic-acid process buckets. It is useful context, not a safe direct propagation.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## Projected GO annotations (5)
- GO:0036503 ERAD pathway | scope=exact | goa_status=already_in_goa_exact | from=ER proteostasis|Organelle-specific protein degradation|ER associated degradation
- GO:0036503 ERAD pathway | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=ER proteostasis|Organelle-specific protein degradation|ER associated degradation|VCP system for retrotranslocation in ERAD
- GO:0006515 protein quality control for misfolded or incompletely synthesized proteins | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Translation|Cytosolic translation|Ribosome-associated QC
- GO:0034098 VCP-NPL4-UFD1 AAA ATPase complex | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Ubiquitin Proteasome System|VCP and associated proteins|adaptors|SHP|UT3
- GO:0097466 ubiquitin-dependent glycoprotein ERAD pathway | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=Ubiquitin Proteasome System|Ubiquitin and UBL binding|protein quality control|ERAD cofactor

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
