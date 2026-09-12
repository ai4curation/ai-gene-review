# RNF5 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q99942
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-11
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/RNF5/RNF5-ai-review.yaml](RNF5-ai-review.yaml)
- AIGR review HTML: missing - genes/human/RNF5/RNF5-ai-review.html
- Gene notes: present - [genes/human/RNF5/RNF5-notes.md](RNF5-notes.md)
- GOA TSV: present - [genes/human/RNF5/RNF5-goa.tsv](RNF5-goa.tsv)
- UniProt record: present - [genes/human/RNF5/RNF5-uniprot.txt](RNF5-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/RNF5.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/RNF5.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/RNF5.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/RNF5.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/RNF5/RNF5-deep-research-falcon.md](RNF5-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: RNF5 (RMA1, NG2/G16) is a small (180 aa) tail-anchored RING-type E3 ubiquitin-protein ligase (EC 2.3.2.27) embedded in the endoplasmic reticulum membrane via two C-terminal transmembrane helices, with an N-terminal cytosolic C3HC4 RING domain (catalytic Cys-42) that recruits ubiquitin-charged E2 enzymes (notably the UBE2D/UbcH5 family and UBE2N/Ubc13). RNF5 is one of the founding mammalian ER-anchored ERAD ubiquitin ligases. Together with the E2 UBE2J1/Ubc6e and Derlin-1 it recognizes folding defects in membrane proteins co-translationally and assembles K48-linked polyubiquitin chains that commit misfolded clients such as CFTR and the disease-associated CFTR-deltaF508 mutant to retrotranslocation and proteasomal degradation; it functions partly redundantly with its close paralog RNF185, with which it forms an E3 ligase module central to CFTR degradation. Beyond canonical ERAD, RNF5 has documented ligase-dependent regulatory roles that use distinct chain topologies and substrates. It builds non-degradative K63-linked chains on the ERAD adaptor JKAMP/JAMP to limit its recruitment of proteasome and p97/VCP components; it ubiquitinates and degrades the innate-immune adaptor STING1/MITA at mitochondria to dampen antiviral type I interferon responses; it controls basal autophagy by regulating the stability of a membrane pool of the cysteine protease ATG4B; and it ubiquitinates paxillin to influence cell motility. RNF5 is widely expressed, and although localized predominantly to membranes (with reported plasma-membrane and mitochondrial-membrane pools), its ER-membrane localization underlies its core ERAD ligase function.
- Existing/core annotation action counts: ACCEPT: 31; KEEP_AS_NON_CORE: 28; REMOVE: 3

## PN Consistency Summary

- **Consistency:** Excellent. Deep research, review and PN concur on the core: ER-membrane RING E3 (Cys-42), ERAD of CFTR/ΔF508 (K48), partly redundant with RNF185; plus the non-core ATG4B/autophagy, STING1/MITA antiviral (K48, mitochondria), JAMP (K63), and paxillin/motility roles. The PN ATG4 row's note ("controls stability of ATG4B") and its reference (PMID:23093945, ATG4B/RNF5 PLOS paper) match the review's GO:0061630 EXP annotation on PMID:23093945. No contradictions.
- **PN story / NEW pressure:** GO:0061630 + GO:0036503 already in GOA and ACCEPTed (multiple EXP/IMP/IGI). GO:2000785 regulation of autophagosome assembly (verified real, OLS) is new_to_goa — RNF5 genuinely limits basal autophagy via ATG4B stability, so this is a DEFENSIBLE ADD, though it is a regulatory framing of a role the review treats as non-core moonlighting (the review captures ATG4B only as substrate-directed ligase activity, no autophagy-process term). Conclude: ligase MF + ERAD already captured; GO:2000785 defensible NEW (non-core).
- **Evidence alignment:** Strong overlap. PN ATG4 row PMID:23093945 = review's autophagy annotation. PN RING row cites "19489725 / rev" (Kaneko/RING-family review) — NOT in the review's reference list (review uses gene-specific EXP papers instead); low impact since ligase MF is independently well-supported.
- **Verdict:** Fully consistent; PN ligase/ERAD already captured, GO:2000785 a defensible (non-core) NEW autophagy-regulation term. No YAML change required.

## Full Consistency Review

- **UniProt:** Q99942 · **batch:** proteostasis-batch-2026-06-11 · **review status:** COMPLETE (very thorough; tail-anchored ER RING E3, ERAD core + STING/ATG4B/paxillin moonlighting)
- **PN placement:** 3 rows — `ER proteostasis|...|ER associated degradation|Cytosolic handling of ERAD substrates|ERAD-associated RING E3 ligase`; `ALP|Autophagophore initiation and elongation|...|Modulation of ATG4 activity`; `UPS|E3 ubiquitin and UBL ligases|RING|with transmembrane domain|ER, mitochondria, cell membrane`. **PN-node mapping:** ERAD-RING-E3 subtype→GO:0061630 (in_goa); ERAD type/group→GO:0036503 (in_goa); ATG4-modulation subtype→GO:2000785 regulation of autophagosome assembly (new_to_goa); RING group→GO:0061630 (in_goa). Projected: GO:0036503×2, GO:0061630×2 (all in GOA), GO:2000785 (new).
- **Consistency:** Excellent. Deep research, review and PN concur on the core: ER-membrane RING E3 (Cys-42), ERAD of CFTR/ΔF508 (K48), partly redundant with RNF185; plus the non-core ATG4B/autophagy, STING1/MITA antiviral (K48, mitochondria), JAMP (K63), and paxillin/motility roles. The PN ATG4 row's note ("controls stability of ATG4B") and its reference (PMID:23093945, ATG4B/RNF5 PLOS paper) match the review's GO:0061630 EXP annotation on PMID:23093945. No contradictions.
- **PN story / NEW pressure:** GO:0061630 + GO:0036503 already in GOA and ACCEPTed (multiple EXP/IMP/IGI). GO:2000785 regulation of autophagosome assembly (verified real, OLS) is new_to_goa — RNF5 genuinely limits basal autophagy via ATG4B stability, so this is a DEFENSIBLE ADD, though it is a regulatory framing of a role the review treats as non-core moonlighting (the review captures ATG4B only as substrate-directed ligase activity, no autophagy-process term). Conclude: ligase MF + ERAD already captured; GO:2000785 defensible NEW (non-core).
- **Mapping strategy:** Correct. Catalytic RING E3 → GO:0061630 at subtype/group; ERAD pathway at type/group; subtype-with-TM no_mapping avoids double-counting. ATG4-modulation leaf → GO:2000785 is appropriately conservative (regulation, not core autophagy). No node-status change warranted.
- **Evidence alignment:** Strong overlap. PN ATG4 row PMID:23093945 = review's autophagy annotation. PN RING row cites "19489725 / rev" (Kaneko/RING-family review) — NOT in the review's reference list (review uses gene-specific EXP papers instead); low impact since ligase MF is independently well-supported.
- **Verdict:** Fully consistent; PN ligase/ERAD already captured, GO:2000785 a defensible (non-core) NEW autophagy-regulation term. No YAML change required.
- **Recommended edits:** none required. [YAML] (optional) consider adding GO:2000785 regulation of autophagosome assembly (IMP/IDA, PMID:23093945) as a non-core BP to mirror the PN projection. [REF] PN-cited PMID:19489725 (RING row) absent from review — verify it is a family review, not gene-specific.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-11
- review_yaml: genes/human/RNF5/RNF5-ai-review.yaml
- PN workbook rows: 3

## PN row 1: ER proteostasis | Organelle-specific protein degradation | ER associated degradation | Cytosolic handling of ERAD substrates | ERAD-associated RING E3 ligase
- UniProt: Q99942
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

## PN row 2: Autophagy-Lysosome Pathway | Autophagophore initiation and elongation | ATG8 homolog processing, upstream | Preparation of ATG8 homologs for lipidation | Modulation of ATG4 activity
- UniProt: Q99942
- In branches: ER, ALP, UPS
- Notes: Annotated by homology with mouse. Regulates basal levels of autophagy by controlling the stability of ATG4B
- PN references (titles):
    - Regulation of ATG4B Stability by RNF5 Limits Basal Levels of Autophagy and Influences Susceptibility to Bacterial Infection (plos.org)
- PN-node mapping records (path + ancestors):
    - [subtype] Autophagy-Lysosome Pathway|Autophagophore initiation and elongation|ATG8 homolog processing, upstream|Preparation of ATG8 homologs for lipidation|Modulation of ATG4 activity
        status=mapped scope=ok_for_propagation_to_go GO=[GO:2000785 regulation of autophagosome assembly]
        rationale: This PN leaf denotes factors that alter ATG4 function upstream of ATG8 processing. The cleanest GO-level consequence captured in the current ontology is regulation of autophagosome assembly.
    - [type] Autophagy-Lysosome Pathway|Autophagophore initiation and elongation|ATG8 homolog processing, upstream|Preparation of ATG8 homologs for lipidation
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a contextual PN role. The label is useful for curator triage, but by itself does not support a universal GO assertion for all member genes beyond curated ancestor or child mappings.
    - [group] Autophagy-Lysosome Pathway|Autophagophore initiation and elongation|ATG8 homolog processing, upstream
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN taxonomy container. The descendants mix components, regulators, context labels, and mechanistic leaves, so propagation should come only from narrower curated nodes.
    - [class] Autophagy-Lysosome Pathway|Autophagophore initiation and elongation
        status=context_only scope=too_broad_to_propagate GO=[GO:0016236 macroautophagy]
        rationale: This class is a real macroautophagy context, but its descendants include core factors, component buckets, upstream modulators, localization roles, and residual categories. Projecting generic macroautophagy from this ancestor creates TRAPP-like overpropagation, so candidate GO annotations must come from narrower curated nodes.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## PN row 3: Ubiquitin Proteasome System | E3 ubiquitin and UBL ligases | RING | with transmembrane domain | ER, mitochondria, cell membrane
- UniProt: Q99942
- In branches: ER, ALP, UPS
- Signature domains: IPR001841
- Auxiliary domains: (none)
- PN references (titles):
    - 19489725 / rev
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|RING|with transmembrane domain|ER, mitochondria, cell membrane
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

## Projected GO annotations (5)
- GO:0036503 ERAD pathway | scope=exact | goa_status=already_in_goa_exact | from=ER proteostasis|Organelle-specific protein degradation|ER associated degradation
- GO:0036503 ERAD pathway | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=ER proteostasis|Organelle-specific protein degradation|ER associated degradation|Cytosolic handling of ERAD substrates
- GO:0061630 ubiquitin protein ligase activity | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=ER proteostasis|Organelle-specific protein degradation|ER associated degradation|Cytosolic handling of ERAD substrates|ERAD-associated RING E3 ligase
- GO:2000785 regulation of autophagosome assembly | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Autophagy-Lysosome Pathway|Autophagophore initiation and elongation|ATG8 homolog processing, upstream|Preparation of ATG8 homologs for lipidation|Modulation of ATG4 activity
- GO:0061630 ubiquitin protein ligase activity | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|RING

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
