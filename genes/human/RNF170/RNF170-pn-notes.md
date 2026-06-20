# RNF170 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q96K19
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-11
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/RNF170/RNF170-ai-review.yaml](RNF170-ai-review.yaml)
- AIGR review HTML: missing - genes/human/RNF170/RNF170-ai-review.html
- Gene notes: present - [genes/human/RNF170/RNF170-notes.md](RNF170-notes.md)
- GOA TSV: present - [genes/human/RNF170/RNF170-goa.tsv](RNF170-goa.tsv)
- UniProt record: present - [genes/human/RNF170/RNF170-uniprot.txt](RNF170-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/RNF170.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/RNF170.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/RNF170.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/RNF170.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/RNF170/RNF170-deep-research-falcon.md](RNF170-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: RNF170 is a multi-pass endoplasmic reticulum membrane RING-type E3 ubiquitin-protein ligase (EC 2.3.2.27, 258 aa) with three transmembrane helices and a large cytoplasmic loop carrying a C3HC4 RING domain (catalytic Cys-102/His-104). Its defining function is in ER-associated degradation (ERAD) of the inositol 1,4,5-trisphosphate receptor (ITPR1/IP3R): RNF170 is essential for stimulus-induced ubiquitination and degradation of activated ITPR1 and also contributes to ITPR1 turnover in resting cells, thereby controlling IP3R abundance and ER calcium-release signaling. To do this it is constitutively associated with the ERLIN1/ERLIN2 (SPFH-domain) complex, which recognizes activated IP3R and recruits RNF170 to ubiquitinate it. RNF170 also has a secondary, ligase-dependent immune-regulatory role: it binds Toll-like receptor 3 (TLR3) and builds K48-linked polyubiquitin chains on Lys-766 in the TLR3 TIR domain to drive its proteasomal degradation, selectively dampening TLR3-triggered innate immune responses. RNF170 is broadly expressed (including spinal cord); loss-of-function and RING-region missense variants cause autosomal dominant sensory ataxia (SNAX1) and autosomal recessive hereditary spastic paraplegia (SPG85), linking its ER ubiquitin-ligase activity to neuronal homeostasis. Its core localization and site of action is the ER membrane.
- Existing/core annotation action counts: ACCEPT: 5; KEEP_AS_NON_CORE: 4; NEW: 1

## PN Consistency Summary

- **Consistency:** Excellent and notably aligned on the NEW pressure. Deep research, review and PN all foreground the **IP3R/ITPR1 ERAD with the ERLIN1/ERLIN2 complex** (PMID:21610068, verified via PubMed [DOI](https://doi.org/10.1074/jbc.M111.251983)) as the defining function that is currently ABSENT from the GOA — the review marks GO:0036503 ERAD pathway as action `NEW` for exactly this reason, matching the dossier `goa_status=new_to_goa` for GO:0036503. GOA confirmed to lack GO:0036503 and GO:0000151. No contradictions.
- **PN story / NEW pressure:** GO:0036503 ERAD pathway (verified real) is genuinely new_to_goa here — the review already proposes adding it (NEW) plus a substrate-specific child term "inositol 1,4,5-trisphosphate receptor catabolic process via the ERAD pathway" (proposed_new_terms, parent GO:0036503). PN's GO:0036503 projection = ADD, fully concordant. GO:0000151 ubiquitin ligase complex (verified real, NOT in GOA) is grounded by the constitutive ERLIN1/2 association — DEFENSIBLE ADD; the review does NOT currently capture complex membership (no GO:0000151). Conclude: ERAD ADD strongly justified (review agrees); GO:0000151 a defensible ADD the review missed.
- **Evidence alignment:** Strong. PN ERLIN row cites "1610068" (truncated PMID = 21610068, the Lu et al. founding IP3R-ERAD paper) and "41481136" (UNVERIFIABLE — does not resolve as a PMID; likely a typo/garbled ID). Review's IP3R-ERAD evidence (PMID:21610068, 31636353, 38782601) is richer; the SNAX1/SPG85 genetics tie ligase activity to disease. PN RING row "19489725 / rev" not in review (family review).
- **Verdict:** Fully consistent and mutually reinforcing on the IP3R-ERAD NEW story; review already proposes the ERAD ADD. GO:0000151 complex membership is a defensible addition the review omits.

## Full Consistency Review

- **UniProt:** Q96K19 · **batch:** proteostasis-batch-2026-06-11 · **review status:** COMPLETE (thorough; multi-pass ER RING E3, IP3R-ERAD core + TLR3, ERLIN complex, SPG85/SNAX1 disease)
- **PN placement:** 3 rows — `ER proteostasis|...|ERAD|...|ERAD-associated RING E3 ligase`; `UPS|...|RING|with transmembrane domain|ER`; `UPS|...|idiosyncratic RING complex|RNF170 / ERLIN complex|catalytic / RING, transmembrane`. **PN-node mapping:** ERAD-RING subtype→GO:0061630 (in_goa); ERAD type→GO:0036503 (new_to_goa); ERAD group→GO:0036503 exact (new_to_goa); RING group→GO:0061630 (in_goa); RNF170/ERLIN-complex group→GO:0000151 ubiquitin ligase complex (new_to_goa). Projected: GO:0036503×2 (new), GO:0061630×2 (in GOA), GO:0000151 (new).
- **Consistency:** Excellent and notably aligned on the NEW pressure. Deep research, review and PN all foreground the **IP3R/ITPR1 ERAD with the ERLIN1/ERLIN2 complex** (PMID:21610068, verified via PubMed [DOI](https://doi.org/10.1074/jbc.M111.251983)) as the defining function that is currently ABSENT from the GOA — the review marks GO:0036503 ERAD pathway as action `NEW` for exactly this reason, matching the dossier `goa_status=new_to_goa` for GO:0036503. GOA confirmed to lack GO:0036503 and GO:0000151. No contradictions.
- **PN story / NEW pressure:** GO:0036503 ERAD pathway (verified real) is genuinely new_to_goa here — the review already proposes adding it (NEW) plus a substrate-specific child term "inositol 1,4,5-trisphosphate receptor catabolic process via the ERAD pathway" (proposed_new_terms, parent GO:0036503). PN's GO:0036503 projection = ADD, fully concordant. GO:0000151 ubiquitin ligase complex (verified real, NOT in GOA) is grounded by the constitutive ERLIN1/2 association — DEFENSIBLE ADD; the review does NOT currently capture complex membership (no GO:0000151). Conclude: ERAD ADD strongly justified (review agrees); GO:0000151 a defensible ADD the review missed.
- **Mapping strategy:** Correct. Catalytic RING → GO:0061630; ERAD group/type → GO:0036503 (exact); ERLIN-complex group → GO:0000151 (membership, conservative). The ERLIN/RNF170 module is ER-membrane, so child GO:0000835 ER ubiquitin ligase complex (verified in OLS) would be more precise. No node-status change warranted.
- **Evidence alignment:** Strong. PN ERLIN row cites "1610068" (truncated PMID = 21610068, the Lu et al. founding IP3R-ERAD paper) and "41481136" (UNVERIFIABLE — does not resolve as a PMID; likely a typo/garbled ID). Review's IP3R-ERAD evidence (PMID:21610068, 31636353, 38782601) is richer; the SNAX1/SPG85 genetics tie ligase activity to disease. PN RING row "19489725 / rev" not in review (family review).
- **Verdict:** Fully consistent and mutually reinforcing on the IP3R-ERAD NEW story; review already proposes the ERAD ADD. GO:0000151 complex membership is a defensible addition the review omits.
- **Recommended edits:** [YAML] add GO:0000151 ubiquitin ligase complex (or child GO:0000835 ER ubiquitin ligase complex; part_of, PMID:21610068/38782601 ERLIN1/2 association) as a non-core CC — currently absent from the review. [REF] verify PN row-3 reference "41481136" — does not resolve as a valid PMID (likely garbled); confirm intended citation.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-11
- review_yaml: genes/human/RNF170/RNF170-ai-review.yaml
- PN workbook rows: 3

## PN row 1: ER proteostasis | Organelle-specific protein degradation | ER associated degradation | Cytosolic handling of ERAD substrates | ERAD-associated RING E3 ligase
- UniProt: Q96K19
- In branches: ER, UPS
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

## PN row 2: Ubiquitin Proteasome System | E3 ubiquitin and UBL ligases | RING | with transmembrane domain | ER
- UniProt: Q96K19
- In branches: ER, UPS
- Signature domains: IPR001841
- Auxiliary domains: (none)
- PN references (titles):
    - 19489725 / rev
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|RING|with transmembrane domain|ER
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

## PN row 3: Ubiquitin Proteasome System | E3 ubiquitin and UBL ligases | idiosyncratic RING complex | RNF170 / ERLIN complex | catalytic / RING, transmembrane
- UniProt: Q96K19
- In branches: ER, UPS
- Signature domains: (none)
- Auxiliary domains: IPR001841
- PN references (titles):
    - 1610068
    - 41481136
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|idiosyncratic RING complex|RNF170 / ERLIN complex|catalytic / RING, transmembrane
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower E3-ligase architecture, component, or domain subdivision already covered by the curated parent E3 mapping. No additional direct GO mapping is needed at this node.
    - [type] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|idiosyncratic RING complex|RNF170 / ERLIN complex
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

## Projected GO annotations (5)
- GO:0036503 ERAD pathway | scope=exact | goa_status=new_to_goa | from=ER proteostasis|Organelle-specific protein degradation|ER associated degradation
- GO:0036503 ERAD pathway | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=ER proteostasis|Organelle-specific protein degradation|ER associated degradation|Cytosolic handling of ERAD substrates
- GO:0061630 ubiquitin protein ligase activity | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=ER proteostasis|Organelle-specific protein degradation|ER associated degradation|Cytosolic handling of ERAD substrates|ERAD-associated RING E3 ligase
- GO:0061630 ubiquitin protein ligase activity | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|RING
- GO:0000151 ubiquitin ligase complex | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|idiosyncratic RING complex

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
