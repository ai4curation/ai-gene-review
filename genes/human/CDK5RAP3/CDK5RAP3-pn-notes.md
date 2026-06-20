# CDK5RAP3 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q96JB5
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/CDK5RAP3/CDK5RAP3-ai-review.yaml](CDK5RAP3-ai-review.yaml)
- AIGR review HTML: present - [genes/human/CDK5RAP3/CDK5RAP3-ai-review.html](CDK5RAP3-ai-review.html)
- Gene notes: present - [genes/human/CDK5RAP3/CDK5RAP3-notes.md](CDK5RAP3-notes.md)
- GOA TSV: present - [genes/human/CDK5RAP3/CDK5RAP3-goa.tsv](CDK5RAP3-goa.tsv)
- UniProt record: present - [genes/human/CDK5RAP3/CDK5RAP3-uniprot.txt](CDK5RAP3-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/CDK5RAP3.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/CDK5RAP3.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/CDK5RAP3.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/CDK5RAP3.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: CDK5RAP3 (also known as C53, LZAP, IC53) is a 506-residue protein that, despite its name, is not a kinase and has no known catalytic activity. Its principal, well-established function is as a substrate adaptor/recruiter within the UFM1 ribosome E3 ligase (UREL) complex, a heterotrimer composed of the UFM1 E3 ligase UFL1, the ER-anchoring adaptor DDRGK1/UFBP1, and CDK5RAP3. This complex catalyzes UFMylation (covalent attachment of the ubiquitin-like modifier UFM1) of substrate proteins at the cytoplasmic surface of the endoplasmic reticulum. CDK5RAP3 directs the ligase to mono-UFMylate ribosomal protein RPL26/uL24 on the 60S subunit of ER-associated ribosomes; within reconstituted systems it constrains UFL1 activity to achieve this precise substrate selection. Through its RPL10a-binding domain it docks the complex onto the 60S subunit, and the UREL complex wraps around the 60S as a C-shaped clamp to promote release and recycling of 60S subunits from the SEC61 translocon following normal termination or ribosome stalling during co-translational translocation (ER ribosome-associated quality control). The complex also mediates UFM1-dependent reticulophagy (ER-phagy) in response to ER stress, in part through ufmylation of CYB5R3, and CDK5RAP3 binds ATG8-family proteins and UFM1 through shuffled ATG8-interacting motifs. UFMylation-dependent functions underlie its requirement for liver development and erythroid differentiation. CDK5RAP3 localizes to the ER membrane, cytosol, nucleus, centrosome and microtubules/cytoskeleton. A separate, older body of literature describes CDK5RAP3/LZAP/C53 as a putative tumor suppressor modulating NF-kappaB (RelA) signaling, ARF/MDM2/p53 regulation, the mitotic G2/M DNA-damage checkpoint (antagonizing CHEK1), p38 MAPK activity, cell invasion and apoptosis-associated nuclear envelope rupture; these roles derive mainly from overexpression/knockdown studies and are less firmly established than the UFMylation adaptor function.
- Existing/core annotation action counts: ACCEPT: 37; KEEP_AS_NON_CORE: 36; MARK_AS_OVER_ANNOTATED: 16

## PN Consistency Summary

- **Consistency:** Excellent multi-branch consistency. Deep-research, review, and all three PN rows converge on CDK5RAP3 as the substrate adaptor of the UFM1 ribosome E3 ligase (UREL: UFL1/DDRGK1/CDK5RAP3) that mono-UFMylates RPL26 on ER 60S ribosomes (ER-RQC, 60S recycling) and drives ER-phagy. Review carries GO:1990756 (adaptor MF, multiple IDA), GO:0071569 (ufmylation), GO:0072344/GO:0032790 (ribosome rescue/disassembly), GO:0140501 (reticulophagy). Older LZAP/C53 NF-kB, ARF/p53, G2/M-checkpoint roles correctly KEEP_AS_NON_CORE. No contradictions across the three PN branches.
- **PN story / NEW pressure:** Mostly already captured, one defensible ADD. (a) GO:0071569 ufmylation, GO:0061709 reticulophagy — both already in review (the review uses GO:0140501 *positive regulation of* reticulophagy; GO:0061709 reticulophagy is the parent process, consistent). (b) The RQC group projects GO:0006515 (protein quality control for misfolded/incompletely synthesized proteins) flagged new_to_goa — this captures the ER-RQC role and is defensible/ADD-able, though the review already encodes the same biology more specifically via GO:0072344 rescue of stalled cytosolic ribosome + GO:0032790 ribosome disassembly, so GO:0006515 would be a broader sibling. No NEW term invention needed; all terms verified pre-existing.
- **Evidence alignment:** PN cites 36121123 (non-canonical scaffold E3 / UFMylation — in review, core IDA), plus ERphagy review titles (Stephani/C53 reticulophagy = PMID:32851973, in review). Good overlap with review's UREL evidence (36121123, 37595036, 38383785, 38383789, 36543799). PN and review are well-aligned on sources.
- **Verdict:** Consistent across TR/ALP/UPS; mapping sound. GO:0006515 (RQC group) is broader than the review's specific terms but defensible as an umbrella.

## Full Consistency Review

- **UniProt:** Q96JB5 (C53, LZAP, IC53) · **batch:** proteostasis-batch-2026-06-07 · **review status:** COMPLETE (very large annotation set reviewed)
- **PN placement:** THREE rows across TR/ALP/UPS — (1) `Translation|Cytosolic translation|Ribosome-associated QC|UFMylation`; (2) `ALP|Autophagy substrate selection|Selective autophagy receptor|ERphagy`; (3) `UPS|E3 ubiquitin and UBL ligases|UBL modifier cofactors|UFMylation cofactor` ; **PN-node mapping:** RQC-UFMylation type → GO:0071569 protein ufmylation; RQC group → GO:0006515 protein QC; ERphagy type → GO:0061709 reticulophagy; UPS UFMylation-cofactor type+group → no_mapping.
- **Consistency:** Excellent multi-branch consistency. Deep-research, review, and all three PN rows converge on CDK5RAP3 as the substrate adaptor of the UFM1 ribosome E3 ligase (UREL: UFL1/DDRGK1/CDK5RAP3) that mono-UFMylates RPL26 on ER 60S ribosomes (ER-RQC, 60S recycling) and drives ER-phagy. Review carries GO:1990756 (adaptor MF, multiple IDA), GO:0071569 (ufmylation), GO:0072344/GO:0032790 (ribosome rescue/disassembly), GO:0140501 (reticulophagy). Older LZAP/C53 NF-kB, ARF/p53, G2/M-checkpoint roles correctly KEEP_AS_NON_CORE. No contradictions across the three PN branches.
- **PN story / NEW pressure:** Mostly already captured, one defensible ADD. (a) GO:0071569 ufmylation, GO:0061709 reticulophagy — both already in review (the review uses GO:0140501 *positive regulation of* reticulophagy; GO:0061709 reticulophagy is the parent process, consistent). (b) The RQC group projects GO:0006515 (protein quality control for misfolded/incompletely synthesized proteins) flagged new_to_goa — this captures the ER-RQC role and is defensible/ADD-able, though the review already encodes the same biology more specifically via GO:0072344 rescue of stalled cytosolic ribosome + GO:0032790 ribosome disassembly, so GO:0006515 would be a broader sibling. No NEW term invention needed; all terms verified pre-existing.
- **Mapping strategy:** Sound. UFMylation type → GO:0071569 and ERphagy type → GO:0061709 are precise. The UPS "UFMylation cofactor" node correctly no_mapping (CDK5RAP3 is a UBL-system adaptor, not a ubiquitin E3 — avoids mis-projecting GO:0061630). The RQC-group GO:0006515 is broader than the review's specific ribosome-rescue terms; acceptable as a group umbrella but flag it as broader-than-review (do not let it displace the specific GO:0072344/GO:0032790).
- **Evidence alignment:** PN cites 36121123 (non-canonical scaffold E3 / UFMylation — in review, core IDA), plus ERphagy review titles (Stephani/C53 reticulophagy = PMID:32851973, in review). Good overlap with review's UREL evidence (36121123, 37595036, 38383785, 38383789, 36543799). PN and review are well-aligned on sources.
- **Verdict:** Consistent across TR/ALP/UPS; mapping sound. GO:0006515 (RQC group) is broader than the review's specific terms but defensible as an umbrella.
- **Recommended edits:** None required; optionally note GO:0006515 is a broader sibling of the review's GO:0072344/GO:0032790 and should not displace them. [MAP]

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07
- review_yaml: genes/human/CDK5RAP3/CDK5RAP3-ai-review.yaml
- PN workbook rows: 3

## PN row 1: Translation | Cytosolic translation | Ribosome-associated QC | UFMylation
- UniProt: Q96JB5
- In branches: TR, ALP, UPS
- PN-node mapping records (path + ancestors):
    - [type] Translation|Cytosolic translation|Ribosome-associated QC|UFMylation
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0071569 protein ufmylation]
        rationale: This PN RQC type denotes UFM1 conjugation in ribosome quality control. Protein ufmylation is the shared process target.
    - [group] Translation|Cytosolic translation|Ribosome-associated QC
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0006515 protein quality control for misfolded or incompletely synthesized proteins]
        rationale: The PN ribosome-associated quality-control group covers surveillance and disposal of stalled or defective nascent-chain translation products. GO lacks a dedicated ribosome-associated QC term in the local cache, so the broader protein-quality-control process is the best supported target.
    - [class] Translation|Cytosolic translation
        status=context_only scope=too_broad_to_propagate GO=[GO:0002181 cytoplasmic translation]
        rationale: The PN class Cytosolic translation is centered on the cytoplasmic translation apparatus and process, but it also houses supporting machinery such as ribosome biogenesis factors. The GO process term is a useful high-level label for the class, but propagating it to all members would over-annotate genes whose PN placement is through assembly or maturation context rather than core cytoplasmic translation.
    - [branch] Translation
        status=context_only scope=too_broad_to_propagate GO=[GO:0006412 translation]
        rationale: The PN Translation branch is organized around the translation apparatus and immediately associated cotranslational quality-control systems. GO translation is the closest high-level process label, but the PN branch also contains adjacent machinery such as ribosome biogenesis and nascent-chain handling. Keeping this relationship is useful for interpretation, but it is too broad to project safely onto every member.

## PN row 2: Autophagy-Lysosome Pathway | Autophagy substrate selection | Selective autophagy receptor | ERphagy
- UniProt: Q96JB5
- In branches: TR, ALP, UPS
- Notes: Receptor for selective autophagy. Binds to ATG8 and ubiquitinated or degron-contaning substrates. Active in ERphagy
- PN references (titles):
    - Regulatory events controlling ER-phagy - ScienceDirect
    - Full article: C53 is a cross-kingdom conserved reticulophagy receptor that bridges the gap betweenselective autophagy and ribosome stalling at the endoplasmic reticulum (tandfonline.com)
- PN-node mapping records (path + ancestors):
    - [type] Autophagy-Lysosome Pathway|Autophagy substrate selection|Selective autophagy receptor|ERphagy
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0061709 reticulophagy]
        rationale: The PN uses the community label ERphagy for selective autophagy of the endoplasmic reticulum, while GO uses the synonym reticulophagy. Receptor members of this PN category are suitable for propagation to the GO reticulophagy process.
    - [group] Autophagy-Lysosome Pathway|Autophagy substrate selection|Selective autophagy receptor
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN taxonomy container. The descendants mix components, regulators, context labels, and mechanistic leaves, so propagation should come only from narrower curated nodes.
    - [class] Autophagy-Lysosome Pathway|Autophagy substrate selection
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad substrate-selection container. GO has useful targets for specific receptor, cargo-adaptor, and selective-autophagy leaves, but this class mixes marking, recognition, receptor regulation, and unknown roles and should not propagate as one term.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## PN row 3: Ubiquitin Proteasome System | E3 ubiquitin and UBL ligases | UBL modifier cofactors | UFMylation cofactor
- UniProt: Q96JB5
- In branches: TR, ALP, UPS
- Signature domains: (none)
- Auxiliary domains: IPR008491
- PN references (titles):
    - 36121123
- PN-node mapping records (path + ancestors):
    - [type] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|UBL modifier cofactors|UFMylation cofactor
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a UPS taxonomy container. Its descendants mix catalytic roles, complex membership, binding domains, regulators, adaptors, and substrate-context labels, so a single propagating GO assertion would overstate the shared biology.
    - [group] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|UBL modifier cofactors
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a UPS taxonomy container. Its descendants mix catalytic roles, complex membership, binding domains, regulators, adaptors, and substrate-context labels, so a single propagating GO assertion would overstate the shared biology.
    - [class] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases
        status=context_only scope=too_broad_to_propagate GO=[GO:0061630 ubiquitin protein ligase activity]
        rationale: This class is a genuine E3-ligase context, but its descendants include catalytic ligases, cullin scaffolds, substrate receptors, adaptors, cofactors, regulators, and UBL modifier systems. A class-level propagation would over-annotate.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## Projected GO annotations (3)
- GO:0006515 protein quality control for misfolded or incompletely synthesized proteins | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Translation|Cytosolic translation|Ribosome-associated QC
- GO:0071569 protein ufmylation | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Translation|Cytosolic translation|Ribosome-associated QC|UFMylation
- GO:0061709 reticulophagy | scope=ok_for_propagation_to_go | goa_status=supported_by_goa_regulation | from=Autophagy-Lysosome Pathway|Autophagy substrate selection|Selective autophagy receptor|ERphagy

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
