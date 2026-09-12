# PN dossier: GCN1

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
