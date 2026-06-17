# PN dossier: ANAPC2

- review_batch: proteostasis-batch-2026-06-03
- review_yaml: genes/human/ANAPC2/ANAPC2-ai-review.yaml
- PN workbook rows: 3

## PN row 1: Ubiquitin Proteasome System | E3 ubiquitin and UBL ligases | Cullin | degenerate, APC sununit
- UniProt: Q9UJX6
- In branches: UPS
- Signature domains: IPR001373, IPR059120
- Auxiliary domains: (none)
- PN references (titles):
    - 16763193
    - 21107322
- PN-node mapping records (path + ancestors):
    - [type] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cullin|degenerate, APC sununit
        status=no_mapping scope= GO=[]
        rationale: Reviewed manually as a UPS source node. No single GO term is appropriate for direct propagation from this PN label without narrower context or gene-level evidence.
    - [group] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cullin
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0160072 ubiquitin ligase complex scaffold activity]
        rationale: This PN group captures cullin or cullin-associated scaffold roles in ubiquitin ligase complexes. The shared GO molecular-function target is ubiquitin ligase complex scaffold activity.
    - [class] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases
        status=context_only scope=too_broad_to_propagate GO=[GO:0061630 ubiquitin protein ligase activity]
        rationale: This class is a genuine E3-ligase context, but its descendants include catalytic ligases, cullin scaffolds, substrate receptors, adaptors, cofactors, regulators, and UBL modifier systems. A class-level propagation would over-annotate.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## PN row 2: Ubiquitin Proteasome System | E3 ubiquitin and UBL ligases | idiosyncratic RING complex | Anaphase Promoting Complex | catalytic / core
- UniProt: Q9UJX6
- In branches: UPS
- Signature domains: (none)
- Auxiliary domains: IPR059120
- PN references (titles):
    - 29167309
    - 16763193
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|idiosyncratic RING complex|Anaphase Promoting Complex|catalytic / core
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower E3-ligase architecture, component, or domain subdivision already covered by the curated parent E3 mapping. No additional direct GO mapping is needed at this node.
    - [type] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|idiosyncratic RING complex|Anaphase Promoting Complex
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0005680 anaphase-promoting complex]
        rationale: In `4.3.11`, APC/C is nested under the idiosyncratic RING-complex branch rather than appearing as a direct group. The GO cellular-component term anaphase-promoting complex remains the appropriate propagation target.
    - [group] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|idiosyncratic RING complex
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0000151 ubiquitin ligase complex]
        rationale: This PN group is an E3 ligase complex bucket. The safest shared GO target is ubiquitin ligase complex membership rather than assigning catalytic activity to every subunit.
    - [class] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases
        status=context_only scope=too_broad_to_propagate GO=[GO:0061630 ubiquitin protein ligase activity]
        rationale: This class is a genuine E3-ligase context, but its descendants include catalytic ligases, cullin scaffolds, substrate receptors, adaptors, cofactors, regulators, and UBL modifier systems. A class-level propagation would over-annotate.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## PN row 3: Ubiquitin Proteasome System | Ubiquitin and UBL binding | E3 ligase complex component | APC / catalytic subunit | idiosyncratic Ub binding / other
- UniProt: Q9UJX6
- In branches: UPS
- Signature domains: PMID: 27259151, PMID: 31350353
- Auxiliary domains: IPR059120
- PN references (titles):
    - 27259151
    - 31350353
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|Ubiquitin and UBL binding|E3 ligase complex component|APC / catalytic subunit|idiosyncratic Ub binding / other
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower enzyme-family, domain, or architecture subdivision already covered by a curated parent enzyme mapping. No additional direct GO mapping is needed at this node.
    - [type] Ubiquitin Proteasome System|Ubiquitin and UBL binding|E3 ligase complex component|APC / catalytic subunit
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower enzyme-family, domain, or architecture subdivision already covered by a curated parent enzyme mapping. No additional direct GO mapping is needed at this node.
    - [group] Ubiquitin Proteasome System|Ubiquitin and UBL binding|E3 ligase complex component
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0000151 ubiquitin ligase complex]
        rationale: This PN group captures E3 ligase complex components. The safe shared GO target is ubiquitin ligase complex membership.
    - [class] Ubiquitin Proteasome System|Ubiquitin and UBL binding
        status=context_only scope=too_broad_to_propagate GO=[GO:0140036 ubiquitin-modified protein reader activity]
        rationale: This class records ubiquitin/UBL-reader context, but the subtree mixes ubiquitin, SUMO, UBL-domain, domain-architecture, catalytic, signaling, trafficking, and nucleic-acid process buckets. It is useful context, not a safe direct propagation.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## Projected GO annotations (4)
- GO:0160072 ubiquitin ligase complex scaffold activity | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cullin
- GO:0000151 ubiquitin ligase complex | scope=ok_for_propagation_to_go | goa_status=entailed_by_goa_closure | from=Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|idiosyncratic RING complex
- GO:0005680 anaphase-promoting complex | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|idiosyncratic RING complex|Anaphase Promoting Complex
- GO:0000151 ubiquitin ligase complex | scope=ok_for_propagation_to_go | goa_status=entailed_by_goa_closure | from=Ubiquitin Proteasome System|Ubiquitin and UBL binding|E3 ligase complex component
