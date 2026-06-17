# PN dossier: UBA5

- review_batch: proteostasis-batch-2026-06-07c
- review_yaml: genes/human/UBA5/UBA5-ai-review.yaml
- PN workbook rows: 3

## PN row 1: Translation | Cytosolic translation | Ribosome-associated QC | UFMylation
- UniProt: Q9GZZ9
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

## PN row 2: Autophagy-Lysosome Pathway | Autophagy substrate selection | Marking substrates for selective autophagy | ERphagy | UFMylation of ER proteins
- UniProt: Q9GZZ9
- In branches: TR, ALP, UPS
- Notes: E1-type protein that catalyzes UFMylation. Knockdown of UFL1 decreased DDRGK1 levels and inhibits ER-phagy.UFL1 UFMylates RPN1 and RPL26 to target ER sheets for degradation.
- PN references (titles):
    - A Genome-wide ER-phagy Screen Highlights Key Roles of Mitochondrial Metabolism and ER-Resident UFMylation - ScienceDirect
- PN-node mapping records (path + ancestors):
    - [subtype] Autophagy-Lysosome Pathway|Autophagy substrate selection|Marking substrates for selective autophagy|ERphagy|UFMylation of ER proteins
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0061709 reticulophagy]
        rationale: This PN subtype captures a specific ER-cargo marking mechanism used in ERphagy. Because GO uses reticulophagy for ER autophagy, this subtype can propagate to reticulophagy.
    - [type] Autophagy-Lysosome Pathway|Autophagy substrate selection|Marking substrates for selective autophagy|ERphagy
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0061709 reticulophagy]
        rationale: The PN ERphagy marking category captures factors that mark ER cargo for selective autophagic turnover. GO uses reticulophagy for this pathway, so propagation to reticulophagy is appropriate.
    - [group] Autophagy-Lysosome Pathway|Autophagy substrate selection|Marking substrates for selective autophagy
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN taxonomy container. The descendants mix components, regulators, context labels, and mechanistic leaves, so propagation should come only from narrower curated nodes.
    - [class] Autophagy-Lysosome Pathway|Autophagy substrate selection
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad substrate-selection container. GO has useful targets for specific receptor, cargo-adaptor, and selective-autophagy leaves, but this class mixes marking, recognition, receptor regulation, and unknown roles and should not propagate as one term.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## PN row 3: Ubiquitin Proteasome System | E1 activating enzymes | activation of UFM1
- UniProt: Q9GZZ9
- In branches: TR, ALP, UPS
- Signature domains: IPR000594
- Auxiliary domains: (none)
- PN-node mapping records (path + ancestors):
    - [group] Ubiquitin Proteasome System|E1 activating enzymes|activation of UFM1
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0008641 ubiquitin-like modifier activating enzyme activity]
        rationale: This PN group represents E1 activation of the UFM1 modifier family. The generic GO activating enzyme activity term is the safest propagation target.
    - [class] Ubiquitin Proteasome System|E1 activating enzymes
        status=context_only scope=too_broad_to_propagate GO=[GO:0008641 ubiquitin-like modifier activating enzyme activity]
        rationale: This class is a real ubiquitin-like modifier E1 context, but it spans ubiquitin, SUMO, NEDD8, UFM1, URM1, ISG15, FAT10, and autophagy modifiers. Propagation is safer from the curated child groups.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## Projected GO annotations (5)
- GO:0006515 protein quality control for misfolded or incompletely synthesized proteins | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Translation|Cytosolic translation|Ribosome-associated QC
- GO:0071569 protein ufmylation | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Translation|Cytosolic translation|Ribosome-associated QC|UFMylation
- GO:0061709 reticulophagy | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Autophagy-Lysosome Pathway|Autophagy substrate selection|Marking substrates for selective autophagy|ERphagy
- GO:0061709 reticulophagy | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Autophagy-Lysosome Pathway|Autophagy substrate selection|Marking substrates for selective autophagy|ERphagy|UFMylation of ER proteins
- GO:0008641 ubiquitin-like modifier activating enzyme activity | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Ubiquitin Proteasome System|E1 activating enzymes|activation of UFM1
