# PN dossier: ANKZF1

- review_batch: proteostasis-batch-2026-06-03
- review_yaml: genes/human/ANKZF1/ANKZF1-ai-review.yaml
- PN workbook rows: 3

## PN row 1: Mitochondrial proteostasis | Organelle-specific protein degradation | Vms pathway
- UniProt: Q9H8Y5
- In branches: MI, TR, UPS
- PN-node mapping records (path + ancestors):
    - [group] Mitochondrial proteostasis|Organelle-specific protein degradation|Vms pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower taxonomy bucket that is already covered by a curated parent mapping or by gene-level annotations. No additional direct GO mapping is appropriate from this node.
    - [class] Mitochondrial proteostasis|Organelle-specific protein degradation
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0035694 mitochondrial protein catabolic process]
        rationale: This PN class groups mitochondrial protein-degradation pathways. GO mitochondrial protein catabolic process is the conservative shared target.
    - [branch] Mitochondrial proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## PN row 2: Translation | Cytosolic translation | Ribosome-associated QC | VCP system for RQC
- UniProt: Q9H8Y5
- In branches: MI, TR, UPS
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

## PN row 3: Ubiquitin Proteasome System | VCP and associated proteins | adaptors | VIM | ankyrin repeats
- UniProt: Q9H8Y5
- In branches: MI, TR, UPS
- Signature domains: PMID: 28451587 (VIM)
- Auxiliary domains: IPR002110
- PN references (titles):
    - 28451587
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|VCP and associated proteins|adaptors|VIM|ankyrin repeats
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a VCP-adaptor motif or architecture subdivision. The label is useful taxonomy but too indirect for direct GO propagation without gene-level evidence.
    - [type] Ubiquitin Proteasome System|VCP and associated proteins|adaptors|VIM
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

## Projected GO annotations (2)
- GO:0035694 mitochondrial protein catabolic process | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Mitochondrial proteostasis|Organelle-specific protein degradation
- GO:0006515 protein quality control for misfolded or incompletely synthesized proteins | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Translation|Cytosolic translation|Ribosome-associated QC
