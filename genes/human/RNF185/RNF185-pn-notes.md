# RNF185 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q96GF1
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-11
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/RNF185/RNF185-ai-review.yaml](RNF185-ai-review.yaml)
- AIGR review HTML: missing - genes/human/RNF185/RNF185-ai-review.html
- Gene notes: present - [genes/human/RNF185/RNF185-notes.md](RNF185-notes.md)
- GOA TSV: present - [genes/human/RNF185/RNF185-goa.tsv](RNF185-goa.tsv)
- UniProt record: present - [genes/human/RNF185/RNF185-uniprot.txt](RNF185-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/RNF185.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/RNF185.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/RNF185.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/RNF185.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/RNF185/RNF185-deep-research-falcon.md](RNF185-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: RNF185 is a small (192 aa) membrane-anchored RING-type E3 ubiquitin-protein ligase (EC 2.3.2.27) and a close paralog of RNF5/RMA1 in the RNF5/RNF185-like family. It has a cytoplasmic N-terminal C3HC4 RING domain (catalytic Cys-39; the RING domain is responsible for ligase activity) and two C-terminal transmembrane helices that anchor it in membranes. RNF185 is an ER-membrane-resident ERAD ubiquitin ligase: it mediates the cotranslational ubiquitination and proteasomal degradation of the misfolded membrane protein CFTR (including CFTR-deltaF508), and it functions partly redundantly with RNF5 as an E3 ligase module that is central to CFTR degradation. Its expression is induced by the unfolded protein response and ER stress, and it protects cells from ER stress-induced apoptosis; it preferentially partners with the ER-associated E2 enzymes UBE2J1 and UBE2J2. Beyond canonical ERAD, RNF185 has documented ligase-dependent regulatory roles that use distinct ubiquitin chain topologies. At the mitochondrial outer membrane it builds K63-linked chains on the Bcl-2 family protein BNIP1 to promote selective mitochondrial autophagy via the autophagy receptor p62, and it builds non-degradative K27-linked chains on the DNA sensor cGAS (CGAS) at Lys-173/Lys-384 to enhance its enzymatic activity and the cGAS-STING innate antiviral response. RNF185 is ubiquitously expressed; its core function is as an ER-membrane ERAD ubiquitin ligase.
- Existing/core annotation action counts: ACCEPT: 32; KEEP_AS_NON_CORE: 23; REMOVE: 3

## PN Consistency Summary

- **Consistency:** Excellent. Deep research, review and PN concur: ER RING E3 (Cys-39), CFTR/ΔF508 ERAD redundant with RNF5; non-core BNIP1 K63 mitophagy (PMID:21931693), cGAS K27/antiviral (PMID:28273161), and the RNF185/Membralin/TMUB1-2 ER-membrane ligase complex. PN row 4 reference "32738194" verified via PubMed = van de Weijer et al. 2020 Mol Cell "Quality Control of ER Membrane Proteins by the RNF185/Membralin Ubiquitin Ligase Complex" ([DOI](https://doi.org/10.1016/j.molcel.2020.07.009)) — the same complex the review cites via PMID:39353943 (Tapasin/Membralin). No contradictions.
- **PN story / NEW pressure:** GO:0061630 + GO:0036503 already in GOA/review. GO:0000423 mitophagy (verified real) is new_to_goa — RNF185's BNIP1 role supports selective mitochondrial autophagy, a DEFENSIBLE ADD (review captures it only as BNIP1-substrate ligase activity + K63, no mitophagy BP term). GO:0000151 ubiquitin ligase complex (verified real, NOT in GOA) is well-grounded by the Membralin complex (PMID:32738194/39353943) — DEFENSIBLE ADD; review has GO:0044877 (complex binding) but no complex CC term. Conclude: catalytic/ERAD captured; GO:0000423 and GO:0000151 both defensible NEW.
- **Evidence alignment:** Strong. PN mitophagy row PMID:21931693 = review BNIP1 annotation; PN membralin PMID:32738194 = review's Membralin/Tapasin literature (PMID:39353943, also van de Weijer). PN RING row "19489725 / rev" not in review (family review; low impact).
- **Verdict:** Fully consistent; ligase MF + ERAD already captured, GO:0000423 mitophagy and GO:0000151 ubiquitin ligase complex both defensible NEW (non-core). No YAML change strictly required.

## Full Consistency Review

- **UniProt:** Q96GF1 · **batch:** proteostasis-batch-2026-06-11 · **review status:** COMPLETE (very thorough; ER RING E3, ERAD/CFTR core + BNIP1 mitophagy, cGAS/K27, Membralin/Tapasin)
- **PN placement:** 4 rows — `ER proteostasis|...|ERAD|...|ERAD-associated RING E3 ligase`; `ALP|Autophagy substrate selection|Autophagy receptor regulation|Mitophagy`; `UPS|...|RING|with transmembrane domain|ER, mitochondria`; `UPS|...|idiosyncratic RING complex|membralin complex|catalytic / RING, transmembrane`. **PN-node mapping:** ERAD-RING subtype→GO:0061630 (in_goa); ERAD type/group→GO:0036503 (in_goa); Mitophagy type→GO:0000423 mitophagy (new_to_goa); RING group→GO:0061630 (in_goa); membralin-complex group→GO:0000151 ubiquitin ligase complex (new_to_goa). Projected: GO:0036503×2, GO:0061630×2 (in GOA), GO:0000423 (new), GO:0000151 (new).
- **Consistency:** Excellent. Deep research, review and PN concur: ER RING E3 (Cys-39), CFTR/ΔF508 ERAD redundant with RNF5; non-core BNIP1 K63 mitophagy (PMID:21931693), cGAS K27/antiviral (PMID:28273161), and the RNF185/Membralin/TMUB1-2 ER-membrane ligase complex. PN row 4 reference "32738194" verified via PubMed = van de Weijer et al. 2020 Mol Cell "Quality Control of ER Membrane Proteins by the RNF185/Membralin Ubiquitin Ligase Complex" ([DOI](https://doi.org/10.1016/j.molcel.2020.07.009)) — the same complex the review cites via PMID:39353943 (Tapasin/Membralin). No contradictions.
- **PN story / NEW pressure:** GO:0061630 + GO:0036503 already in GOA/review. GO:0000423 mitophagy (verified real) is new_to_goa — RNF185's BNIP1 role supports selective mitochondrial autophagy, a DEFENSIBLE ADD (review captures it only as BNIP1-substrate ligase activity + K63, no mitophagy BP term). GO:0000151 ubiquitin ligase complex (verified real, NOT in GOA) is well-grounded by the Membralin complex (PMID:32738194/39353943) — DEFENSIBLE ADD; review has GO:0044877 (complex binding) but no complex CC term. Conclude: catalytic/ERAD captured; GO:0000423 and GO:0000151 both defensible NEW.
- **Mapping strategy:** Correct and conservative. Membralin-complex group→GO:0000151 (complex membership, not catalytic activity to every subunit) is sound; consider the more specific child GO:0000835 ER ubiquitin ligase complex (verified in OLS) given the ER-membrane context. Mitophagy via receptor-regulation framing → GO:0000423 appropriate. No node-status change warranted.
- **Evidence alignment:** Strong. PN mitophagy row PMID:21931693 = review BNIP1 annotation; PN membralin PMID:32738194 = review's Membralin/Tapasin literature (PMID:39353943, also van de Weijer). PN RING row "19489725 / rev" not in review (family review; low impact).
- **Verdict:** Fully consistent; ligase MF + ERAD already captured, GO:0000423 mitophagy and GO:0000151 ubiquitin ligase complex both defensible NEW (non-core). No YAML change strictly required.
- **Recommended edits:** [YAML] (optional) add GO:0000151 ubiquitin ligase complex (or child GO:0000835 ER ubiquitin ligase complex; part_of, PMID:32738194) and GO:0000423 mitophagy (involved_in, PMID:21931693) as non-core annotations to mirror the PN projections. [MAP] consider GO:0000835 ER ubiquitin ligase complex as a more precise target for the membralin-complex node.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-11
- review_yaml: genes/human/RNF185/RNF185-ai-review.yaml
- PN workbook rows: 4

## PN row 1: ER proteostasis | Organelle-specific protein degradation | ER associated degradation | Cytosolic handling of ERAD substrates | ERAD-associated RING E3 ligase
- UniProt: Q96GF1
- In branches: ER, ALP, UPS
- PN-node mapping records (path + ancestors):
    - [subtype] ER proteostasis|Organelle-specific protein degradation|ER associated degradation|Cytosolic handling of ERAD substrates|ERAD-associated RING E3 ligase
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0061630 ubiquitin protein ligase activity]
        rationale: This PN subtype denotes ERAD-associated RING E3 ligases. Ubiquitin protein ligase activity is the appropriate shared catalytic target.
    - [type] ER proteostasis|Organelle-specific protein degradation|ER associated degradation|Cytosolic handling of ERAD substrates
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0036503 ERAD pathway]
        rationale: This PN type covers the cytosolic processing steps that receive ERAD substrates after retrotranslocation. These activities remain part of the ERAD pathway, but the source category is a specific mechanistic slice.
    - [group] ER proteostasis|Organelle-specific protein degradation|ER associated degradation
        status=mapped scope=exact GO=[GO:0036503 ERAD pathway]
        rationale: The PN group "ER associated degradation" is a direct lexical and biological match to the GO ERAD pathway term. The additional branch and class context disambiguates the source string from any broader degradation language.
    - [class] ER proteostasis|Organelle-specific protein degradation
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a single GO class. The member genes span multiple activities, complexes, or contexts, so direct propagation from this node would overstate the shared biology.
    - [branch] ER proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## PN row 2: Autophagy-Lysosome Pathway | Autophagy substrate selection | Autophagy receptor regulation | Mitophagy
- UniProt: Q96GF1
- In branches: ER, ALP, UPS
- Notes: Mitochondrial ubiquitin E3 ligase that regulates selective mitochondrial autophagy via interaction with BNIP1.
- PN references (titles):
    - RNF185, a Novel Mitochondrial Ubiquitin E3 Ligase, Regulates Autophagy through Interaction with BNIP1 (plos.org)
- PN-node mapping records (path + ancestors):
    - [type] Autophagy-Lysosome Pathway|Autophagy substrate selection|Autophagy receptor regulation|Mitophagy
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0000423 mitophagy]
        rationale: The PN receptor-regulation type for mitophagy captures factors that tune receptor activity within the mitophagy pathway. This supports propagation to mitophagy while preserving that the source is a regulatory sub-role.
    - [group] Autophagy-Lysosome Pathway|Autophagy substrate selection|Autophagy receptor regulation
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN taxonomy container. The descendants mix components, regulators, context labels, and mechanistic leaves, so propagation should come only from narrower curated nodes.
    - [class] Autophagy-Lysosome Pathway|Autophagy substrate selection
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad substrate-selection container. GO has useful targets for specific receptor, cargo-adaptor, and selective-autophagy leaves, but this class mixes marking, recognition, receptor regulation, and unknown roles and should not propagate as one term.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## PN row 3: Ubiquitin Proteasome System | E3 ubiquitin and UBL ligases | RING | with transmembrane domain | ER, mitochondria
- UniProt: Q96GF1
- In branches: ER, ALP, UPS
- Signature domains: IPR001841
- Auxiliary domains: (none)
- PN references (titles):
    - 19489725 / rev
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|RING|with transmembrane domain|ER, mitochondria
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower E3-ligase architecture, component, or domain subdivision already covered by the curated parent E3 mapping. No additional direct GO mapping is needed at this node.
    - [type] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|RING|with transmembrane domain
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

## PN row 4: Ubiquitin Proteasome System | E3 ubiquitin and UBL ligases | idiosyncratic RING complex | membralin complex | catalytic / RING, transmembrane
- UniProt: Q96GF1
- In branches: ER, ALP, UPS
- Signature domains: (none)
- Auxiliary domains: IPR001841
- PN references (titles):
    - 32738194
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|idiosyncratic RING complex|membralin complex|catalytic / RING, transmembrane
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower E3-ligase architecture, component, or domain subdivision already covered by the curated parent E3 mapping. No additional direct GO mapping is needed at this node.
    - [type] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|idiosyncratic RING complex|membralin complex
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower E3-ligase architecture, component, or domain subdivision already covered by the curated parent E3 mapping. No additional direct GO mapping is needed at this node.
    - [group] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|idiosyncratic RING complex
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0000151 ubiquitin ligase complex]
        rationale: This PN group is an E3 ligase complex bucket. The safest shared GO target is ubiquitin ligase complex membership rather than assigning catalytic activity to every subunit.
    - [class] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases
        status=context_only scope=too_broad_to_propagate GO=[GO:0061630 ubiquitin protein ligase activity]
        rationale: This class is a genuine E3-ligase context, but its descendants include catalytic ligases, cullin scaffolds, substrate receptors, adaptors, cofactors, regulators, and UBL modifier systems. A class-level propagation would over-annotate.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## Projected GO annotations (6)
- GO:0036503 ERAD pathway | scope=exact | goa_status=already_in_goa_exact | from=ER proteostasis|Organelle-specific protein degradation|ER associated degradation
- GO:0036503 ERAD pathway | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=ER proteostasis|Organelle-specific protein degradation|ER associated degradation|Cytosolic handling of ERAD substrates
- GO:0061630 ubiquitin protein ligase activity | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=ER proteostasis|Organelle-specific protein degradation|ER associated degradation|Cytosolic handling of ERAD substrates|ERAD-associated RING E3 ligase
- GO:0000423 mitophagy | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Autophagy-Lysosome Pathway|Autophagy substrate selection|Autophagy receptor regulation|Mitophagy
- GO:0061630 ubiquitin protein ligase activity | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|RING
- GO:0000151 ubiquitin ligase complex | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|idiosyncratic RING complex

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
