# PN dossier: UFSP1

- review_batch: proteostasis-batch-2026-06-07c
- review_yaml: genes/human/UFSP1/UFSP1-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Translation | Cytosolic translation | Ribosome-associated QC | UFMylation
- UniProt: Q6NVU6
- In branches: TR, UPS
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

## PN row 2: Ubiquitin Proteasome System | DUBs and UBL demodifiers | UFSP | deUFMylase
- UniProt: Q6NVU6
- In branches: TR, UPS
- Signature domains: IPR012462
- Auxiliary domains: (none)
- PN references (titles):
    - 29476094
- PN-node mapping records (path + ancestors):
    - [type] Ubiquitin Proteasome System|DUBs and UBL demodifiers|UFSP|deUFMylase
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0071567 deUFMylase activity]
        rationale: This PN type is the explicit deUFMylase bucket under UFSP proteins. The matching GO molecular-function term is deUFMylase activity.
    - [group] Ubiquitin Proteasome System|DUBs and UBL demodifiers|UFSP
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0071567 deUFMylase activity]
        rationale: This PN group captures UFSP-family deUFMylases. The matching GO molecular-function term is deUFMylase activity.
    - [class] Ubiquitin Proteasome System|DUBs and UBL demodifiers
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a UPS taxonomy container. Its descendants mix catalytic roles, complex membership, binding domains, regulators, adaptors, and substrate-context labels, so a single propagating GO assertion would overstate the shared biology.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## Projected GO annotations (4)
- GO:0006515 protein quality control for misfolded or incompletely synthesized proteins | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Translation|Cytosolic translation|Ribosome-associated QC
- GO:0071569 protein ufmylation | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Translation|Cytosolic translation|Ribosome-associated QC|UFMylation
- GO:0071567 deUFMylase activity | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Ubiquitin Proteasome System|DUBs and UBL demodifiers|UFSP
- GO:0071567 deUFMylase activity | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Ubiquitin Proteasome System|DUBs and UBL demodifiers|UFSP|deUFMylase
