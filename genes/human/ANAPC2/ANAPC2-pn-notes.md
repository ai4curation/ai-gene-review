# ANAPC2 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9UJX6
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-03 (PR 1367)
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/ANAPC2/ANAPC2-ai-review.yaml](ANAPC2-ai-review.yaml)
- AIGR review HTML: present - [genes/human/ANAPC2/ANAPC2-ai-review.html](ANAPC2-ai-review.html)
- Gene notes: present - [genes/human/ANAPC2/ANAPC2-notes.md](ANAPC2-notes.md)
- GOA TSV: present - [genes/human/ANAPC2/ANAPC2-goa.tsv](ANAPC2-goa.tsv)
- UniProt record: present - [genes/human/ANAPC2/ANAPC2-uniprot.txt](ANAPC2-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/ANAPC2.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/ANAPC2.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ANAPC2.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ANAPC2.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/ANAPC2/ANAPC2-deep-research-falcon.md](ANAPC2-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: ANAPC2 encodes anaphase-promoting complex subunit 2, the cullin-like scaffold of the APC/C catalytic module. In the APC/C E3 ubiquitin ligase, ANAPC2 works with the RING subunit ANAPC11 and ubiquitin-conjugating enzymes to ubiquitinate cell-cycle substrates, promoting ordered proteasomal degradation during mitotic progression and mitotic exit. Structural and biochemical studies place ANAPC2 in the APC/C catalytic platform, and APC/C activity is regulated by coactivators, phosphorylation, checkpoint inhibitors, and substrate adaptors in nuclear and cytosolic cell-cycle contexts.
- Existing/core annotation action counts: ACCEPT: 15; KEEP_AS_NON_CORE: 40; MARK_AS_OVER_ANNOTATED: 8; MODIFY: 1; NEW: 1

## PN Consistency Summary

- **Consistency:** Fully consistent. DR ↔ notes ↔ YAML ↔ PN all converge: ANAPC2 is the cullin-like scaffold subunit of the APC/C catalytic module (Apc2-Apc11). No contradiction.
- **PN story / NEW pressure:** PN projects three terms; review handles each correctly. GO:0005680 already_in_goa → ACCEPT (IBA). GO:0000151 entailed via GO:0005680/GO:0031461 → correctly NOT added. **GO:0160072 ubiquitin ligase complex scaffold activity (verified real, new_to_goa): review ADDS as `action: NEW`** (IC, PMID:26083744) only after gene-level scrutiny of structural literature (Apc2-Apc11 catalytic module; PMID:11739784 minimal module, 16364912). Defensible — APC2 is a degenerate cullin scaffold. Conclude: ADD (GO:0160072), others already captured/entailed.
- **Evidence alignment:** PN cites PMID:16763193, 21107322, 29167309, 27259151, 31350353. Review uses overlapping structural set (16364912, 26083744, 11739784, 18485873, 29033132) plus DR additions PMID:37735619 (TR cryo-EM E2 docking), 39567505 (APC2 Zn module), 36548081 (DEPTOR substrate) as statement-only. Good overlap on APC/C catalytic-module structure; review enriches with newer cryo-EM.
- **Verdict:** Consistent; GO:0160072 NEW warranted and matches PN (new_to_goa). GO:0005680 ACCEPT, GO:0000151 correctly entailed. No over-reach.

## Full Consistency Review

- **UniProt:** Q9UJX6 (APC2) · **batch:** proteostasis-batch-2026-06-03 (Falcon DR 2026-06-07) · **review status:** COMPLETE
- **PN placement:** 3 rows, UPS. (1) `…Cullin|degenerate, APC sununit`; (2) `…idiosyncratic RING complex|Anaphase Promoting Complex|catalytic / core`; (3) `…Ubiquitin and UBL binding|E3 ligase complex component|APC / catalytic subunit`. **PN-node mapping:** Cullin group=`mapped`→GO:0160072 scaffold activity (new_to_goa); APC type=`mapped`→GO:0005680 anaphase-promoting complex (already_in_goa_exact); RING-complex/E3-component groups=`mapped`→GO:0000151 ubiquitin ligase complex (entailed_by_goa_closure).
- **Consistency:** Fully consistent. DR ↔ notes ↔ YAML ↔ PN all converge: ANAPC2 is the cullin-like scaffold subunit of the APC/C catalytic module (Apc2-Apc11). No contradiction.
- **PN story / NEW pressure:** PN projects three terms; review handles each correctly. GO:0005680 already_in_goa → ACCEPT (IBA). GO:0000151 entailed via GO:0005680/GO:0031461 → correctly NOT added. **GO:0160072 ubiquitin ligase complex scaffold activity (verified real, new_to_goa): review ADDS as `action: NEW`** (IC, PMID:26083744) only after gene-level scrutiny of structural literature (Apc2-Apc11 catalytic module; PMID:11739784 minimal module, 16364912). Defensible — APC2 is a degenerate cullin scaffold. Conclude: ADD (GO:0160072), others already captured/entailed.
- **Mapping strategy:** ANAPC2 supports, rather than changes, the node mappings. The Cullin-group scaffold projection is precisely the term gene-level review accepts; APC and ligase-complex memberships are appropriately already-in/entailed. Scopes (ok_for_propagation) correct; no broader/narrower mismatch.
- **Evidence alignment:** PN cites PMID:16763193, 21107322, 29167309, 27259151, 31350353. Review uses overlapping structural set (16364912, 26083744, 11739784, 18485873, 29033132) plus DR additions PMID:37735619 (TR cryo-EM E2 docking), 39567505 (APC2 Zn module), 36548081 (DEPTOR substrate) as statement-only. Good overlap on APC/C catalytic-module structure; review enriches with newer cryo-EM.
- **Verdict:** Consistent; GO:0160072 NEW warranted and matches PN (new_to_goa). GO:0005680 ACCEPT, GO:0000151 correctly entailed. No over-reach.
- **Recommended edits:** none to ANAPC2-ai-review.yaml; PN mappings sound as-is.

## PN Dossier Context

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

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
