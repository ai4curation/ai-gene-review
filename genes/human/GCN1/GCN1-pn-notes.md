# GCN1 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q92616
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07c
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/GCN1/GCN1-ai-review.yaml](GCN1-ai-review.yaml)
- AIGR review HTML: present - [genes/human/GCN1/GCN1-ai-review.html](GCN1-ai-review.html)
- Gene notes: present - [genes/human/GCN1/GCN1-notes.md](GCN1-notes.md)
- GOA TSV: present - [genes/human/GCN1/GCN1-goa.tsv](GCN1-goa.tsv)
- UniProt record: present - [genes/human/GCN1/GCN1-uniprot.txt](GCN1-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/GCN1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/GCN1.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/GCN1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/GCN1.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: GCN1 (stalled ribosome sensor GCN1, formerly GCN1L1) is a very large cytoplasmic HEAT-repeat/alpha-solenoid protein that binds directly to ribosomes and acts as a sentinel for stalled and collided ribosomes. Through its RWD-binding domain it engages RWD-domain proteins and serves two intertwined ribosome-surveillance functions. First, GCN1 activates the eIF2alpha kinase GCN2 (EIF2AK4) on translating ribosomes, stimulating GCN2 to phosphorylate eIF2alpha (EIF2S1) and thereby triggering the integrated stress response and the cellular response to amino-acid starvation (the GCN2-mediated signaling axis conserved from yeast GCN1/GCN20). Second, GCN1 is the collision sensor of the RNF14-RNF25 translation quality-control pathway, where it is required for ubiquitination and degradation of translation factors (eEF1A/eEF1A1, eRF1/ETF1) and ribosomal proteins on stalled ribosomes, including resolution of formaldehyde-induced mRNA RNA-protein crosslinks. GCN1 binding by IMPACT antagonizes GCN2 activation. GCN1 is ribosome/polysome-associated in the cytosol.
- Existing/core annotation action counts: ACCEPT: 23; KEEP_AS_NON_CORE: 6; MARK_AS_OVER_ANNOTATED: 3

## PN Consistency Summary

- **Consistency:** Strong and well-aligned. Deep research, notes, and review all describe GCN1 as the ribosome collision/stall sensor with two roles: (1) activating GCN2/EIF2AK4 → eIF2alpha-P → ISR/amino-acid-starvation response, and (2) acting as the collision sensor of the RNF14-RNF25 RQC pathway that degrades A-site-blocking factors (eEF1A, eRF1). Review ACCEPTs GO:0034198 (aa starvation), GO:0140469 (GCN2-mediated signaling), GO:0072344 (rescue of stalled ribosome ×4), GO:0170011 (stalled ribosome sensor ×4), GO:0043539 (kinase activator), GO:0060090 (adaptor), GO:0160127 (protein-RNA crosslink repair). All four PN rows map onto biology the review independently asserts. No contradictions.
- **PN story / NEW pressure:** PN's projected terms — GO:0006417 (regulation of translation, already_in_goa, KEEP_AS_NON_CORE in review), GO:0140467 (ISR signaling, entailed by closure; review uses the child GO:0140469 GCN2-mediated signaling), GO:0006515 (RQC umbrella, verified real), GO:0016567 (protein ubiquitination) — are all real and biology-consistent. GO:0016567 is the one term GCN1's review does NOT carry: GCN1 enables/promotes eEF1A ubiquitination by recruiting RNF14, but GCN1 is the sensor/scaffold, not itself a ubiquitin transferase, so a direct GO:0016567 on GCN1 over-reaches (the ubiquitination is RNF14's catalytic act; GCN1 is involved_in via GO:0072344/GO:0060090). **Mostly already captured**; GO:0016567 over-reaches for the sensor.
- **Evidence alignment:** PN cites one title — "Ribosome binding protein GCN1 regulates the cell cycle and cell proliferation and is essential for the embryonic development of mice (PLOS Genetics)" — which is NOT among the review's references (the review uses 9234705, 36638793, 37651229, 37951215/6 for the sensor/RQC/ISR roles). Divergence: PN's cited paper covers a developmental/proliferation phenotype not used by the review; the mechanistic ISR/RQC evidence base differs.
- **Verdict:** Highly consistent on core sensor/ISR/RQC biology; PN story already captured (review is more granular: GO:0140469, GO:0072344, GO:0170011). One over-reach. **Recommended edits:** [MAP] qualify the eEF1A-ubiquitination type→GO:0016567 projection — GCN1 promotes (does not catalyze) eEF1A ubiquitination; project as involved_in RQC (GO:0072344) rather than as GCN1's own protein-ubiquitination activity. [REF] consider adding the PN-cited GCN1 developmental PLOS Genetics paper to the review references (currently absent) or noting its relevance is non-core.

## Full Consistency Review

- **UniProt:** Q92616 · **batch:** proteostasis-batch-2026-06-07c · **review status:** COMPLETE
- **PN placement (4 rows):** `PN regulation|Translation regulator|Integrated stress response|EIF2AK4 modulator`; `Translation|...|Ribosome-associated QC|other RQC processes`; `Translation|...|Ribosome-associated QC|ubiquitination of eEF1A on stalled ribosomes`; `Autophagy-Lysosome Pathway|Autophagy gene expression|ATF4 transcriptional program|Nutrient sensing` ; **PN-node mapping:** ISR group=mapped→GO:0140467; Translation-regulator class=mapped→GO:0006417; RQC group=mapped→GO:0006515; eEF1A-ubiq type=mapped→GO:0016567 (protein ubiquitination); ALP class context_only (GO:0010506); several types/branches no_mapping.
- **Consistency:** Strong and well-aligned. Deep research, notes, and review all describe GCN1 as the ribosome collision/stall sensor with two roles: (1) activating GCN2/EIF2AK4 → eIF2alpha-P → ISR/amino-acid-starvation response, and (2) acting as the collision sensor of the RNF14-RNF25 RQC pathway that degrades A-site-blocking factors (eEF1A, eRF1). Review ACCEPTs GO:0034198 (aa starvation), GO:0140469 (GCN2-mediated signaling), GO:0072344 (rescue of stalled ribosome ×4), GO:0170011 (stalled ribosome sensor ×4), GO:0043539 (kinase activator), GO:0060090 (adaptor), GO:0160127 (protein-RNA crosslink repair). All four PN rows map onto biology the review independently asserts. No contradictions.
- **PN story / NEW pressure:** PN's projected terms — GO:0006417 (regulation of translation, already_in_goa, KEEP_AS_NON_CORE in review), GO:0140467 (ISR signaling, entailed by closure; review uses the child GO:0140469 GCN2-mediated signaling), GO:0006515 (RQC umbrella, verified real), GO:0016567 (protein ubiquitination) — are all real and biology-consistent. GO:0016567 is the one term GCN1's review does NOT carry: GCN1 enables/promotes eEF1A ubiquitination by recruiting RNF14, but GCN1 is the sensor/scaffold, not itself a ubiquitin transferase, so a direct GO:0016567 on GCN1 over-reaches (the ubiquitination is RNF14's catalytic act; GCN1 is involved_in via GO:0072344/GO:0060090). **Mostly already captured**; GO:0016567 over-reaches for the sensor.
- **Mapping strategy:** ISR group→GO:0140467 is broader than the review's GO:0140469 (a child) but defensible as the umbrella; not a TOMM20-style rejection. RQC group→GO:0006515 is fine (umbrella over GO:0072344). The eEF1A-ubiquitination type→GO:0016567 should be treated as a process GCN1 enables indirectly, not a direct MF/BP to project as GCN1's own activity.
- **Evidence alignment:** PN cites one title — "Ribosome binding protein GCN1 regulates the cell cycle and cell proliferation and is essential for the embryonic development of mice (PLOS Genetics)" — which is NOT among the review's references (the review uses 9234705, 36638793, 37651229, 37951215/6 for the sensor/RQC/ISR roles). Divergence: PN's cited paper covers a developmental/proliferation phenotype not used by the review; the mechanistic ISR/RQC evidence base differs.
- **Verdict:** Highly consistent on core sensor/ISR/RQC biology; PN story already captured (review is more granular: GO:0140469, GO:0072344, GO:0170011). One over-reach. **Recommended edits:** [MAP] qualify the eEF1A-ubiquitination type→GO:0016567 projection — GCN1 promotes (does not catalyze) eEF1A ubiquitination; project as involved_in RQC (GO:0072344) rather than as GCN1's own protein-ubiquitination activity. [REF] consider adding the PN-cited GCN1 developmental PLOS Genetics paper to the review references (currently absent) or noting its relevance is non-core.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07c
- review_yaml: genes/human/GCN1/GCN1-ai-review.yaml
- PN workbook rows: 4

## PN row 1: PN regulation | Translation regulator | Integrated stress response | EIF2AK4 modulator
- UniProt: Q92616
- In branches: PN, TR, ALP
- PN-node mapping records (path + ancestors):
    - [type] PN regulation|Translation regulator|Integrated stress response|EIF2AK4 modulator
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a contextual PN bucket. The label is useful for curator triage, but no direct GO mapping is appropriate because propagation would add a process, activity, or localization not shared cleanly by all members.
    - [group] PN regulation|Translation regulator|Integrated stress response
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0140467 integrated stress response signaling]
        rationale: This PN path covers translation-regulator components of the integrated stress response, including EIF2S1 phosphorylation control. These genes are participants in integrated stress response signaling, but the PN group is a mechanistic slice of the process rather than a GO-equivalent class.
    - [class] PN regulation|Translation regulator
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0006417 regulation of translation]
        rationale: This PN class is the broad translation-regulatory bucket. GO regulation of translation is the conservative propagation target for the umbrella label.
    - [branch] PN regulation
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## PN row 2: Translation | Cytosolic translation | Ribosome-associated QC | other RQC processes
- UniProt: Q92616
- In branches: PN, TR, ALP
- PN-node mapping records (path + ancestors):
    - [type] Translation|Cytosolic translation|Ribosome-associated QC|other RQC processes
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

## PN row 3: Translation | Cytosolic translation | Ribosome-associated QC | ubiquitination of eEF1A on stalled ribosomes
- UniProt: Q92616
- In branches: PN, TR, ALP
- PN-node mapping records (path + ancestors):
    - [type] Translation|Cytosolic translation|Ribosome-associated QC|ubiquitination of eEF1A on stalled ribosomes
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0016567 protein ubiquitination]
        rationale: This PN RQC type is a specific ubiquitination bucket for eEF1A on stalled ribosomes. Protein ubiquitination is the shared process target.
    - [group] Translation|Cytosolic translation|Ribosome-associated QC
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0006515 protein quality control for misfolded or incompletely synthesized proteins]
        rationale: The PN ribosome-associated quality-control group covers surveillance and disposal of stalled or defective nascent-chain translation products. GO lacks a dedicated ribosome-associated QC term in the local cache, so the broader protein-quality-control process is the best supported target.
    - [class] Translation|Cytosolic translation
        status=context_only scope=too_broad_to_propagate GO=[GO:0002181 cytoplasmic translation]
        rationale: The PN class Cytosolic translation is centered on the cytoplasmic translation apparatus and process, but it also houses supporting machinery such as ribosome biogenesis factors. The GO process term is a useful high-level label for the class, but propagating it to all members would over-annotate genes whose PN placement is through assembly or maturation context rather than core cytoplasmic translation.
    - [branch] Translation
        status=context_only scope=too_broad_to_propagate GO=[GO:0006412 translation]
        rationale: The PN Translation branch is organized around the translation apparatus and immediately associated cotranslational quality-control systems. GO translation is the closest high-level process label, but the PN branch also contains adjacent machinery such as ribosome biogenesis and nascent-chain handling. Keeping this relationship is useful for interpretation, but it is too broad to project safely onto every member.

## PN row 4: Autophagy-Lysosome Pathway | Autophagy gene expression | ATF4 transcriptional program | Nutrient sensing
- UniProt: Q92616
- In branches: PN, TR, ALP
- Notes: Forms a complex with EIF2AK4 to facilitate delivery of uncharged tRNAs to the tRNA binding domain of EIF2AK4 during starvation thereby promoting its activation
- PN references (titles):
    - Ribosome binding protein GCN1 regulates the cell cycle and cell proliferation and is essential for the embryonic development of mice | PLOS Genetics
- PN-node mapping records (path + ancestors):
    - [type] Autophagy-Lysosome Pathway|Autophagy gene expression|ATF4 transcriptional program|Nutrient sensing
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a contextual PN role. The label is useful for curator triage, but by itself does not support a universal GO assertion for all member genes beyond curated ancestor or child mappings.
    - [group] Autophagy-Lysosome Pathway|Autophagy gene expression|ATF4 transcriptional program
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN taxonomy container. The descendants mix components, regulators, context labels, and mechanistic leaves, so propagation should come only from narrower curated nodes.
    - [class] Autophagy-Lysosome Pathway|Autophagy gene expression
        status=context_only scope=too_broad_to_propagate GO=[GO:0010506 regulation of autophagy]
        rationale: This class records autophagy-linked gene-expression programs, but many nodes are transcription program names or upstream modulators rather than direct GO regulation assertions. It is kept as context only; transcription factor or cofactor activities are mapped at narrower nodes.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## Projected GO annotations (5)
- GO:0006417 regulation of translation | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=PN regulation|Translation regulator
- GO:0140467 integrated stress response signaling | scope=ok_for_propagation_to_go | goa_status=entailed_by_goa_closure | from=PN regulation|Translation regulator|Integrated stress response
- GO:0006515 protein quality control for misfolded or incompletely synthesized proteins | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Translation|Cytosolic translation|Ribosome-associated QC
- GO:0006515 protein quality control for misfolded or incompletely synthesized proteins | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Translation|Cytosolic translation|Ribosome-associated QC
- GO:0016567 protein ubiquitination | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Translation|Cytosolic translation|Ribosome-associated QC|ubiquitination of eEF1A on stalled ribosomes

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
