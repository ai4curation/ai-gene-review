# ABRAXAS2 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q15018
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-03 (PR 1329)
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/ABRAXAS2/ABRAXAS2-ai-review.yaml](ABRAXAS2-ai-review.yaml)
- AIGR review HTML: present - [genes/human/ABRAXAS2/ABRAXAS2-ai-review.html](ABRAXAS2-ai-review.html)
- Gene notes: present - [genes/human/ABRAXAS2/ABRAXAS2-notes.md](ABRAXAS2-notes.md)
- GOA TSV: present - [genes/human/ABRAXAS2/ABRAXAS2-goa.tsv](ABRAXAS2-goa.tsv)
- UniProt record: present - [genes/human/ABRAXAS2/ABRAXAS2-uniprot.txt](ABRAXAS2-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/ABRAXAS2.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/ABRAXAS2.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ABRAXAS2.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ABRAXAS2.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/ABRAXAS2/ABRAXAS2-deep-research-falcon.md](ABRAXAS2-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: ABRAXAS2 encodes Abraxas 2/ABRO1, a noncatalytic MPN-domain scaffold subunit of the BRISC K63-linked deubiquitinating complex. Together with BRCC3/BRCC36, BABAM1/MERIT40, and BABAM2/BRE, ABRAXAS2 helps assemble and localize BRISC in the cytoplasm and nucleus, where the complex removes K63-linked ubiquitin chains from substrates involved in immune receptor signaling and mitotic spindle organization. ABRAXAS2 also provides the BRISC-specific interface for SHMT2-dependent regulation and targeting, and it can translocate to the nucleus during cellular stress to influence p53-dependent DNA-damage signaling. Unlike ABRAXAS1, ABRAXAS2 lacks the BRCA1-interacting C-terminal phospho-motif and is not a canonical BRCA1-A DNA-repair adaptor.
- Existing/core annotation action counts: ACCEPT: 35; KEEP_AS_NON_CORE: 1; MARK_AS_OVER_ANNOTATED: 2; MODIFY: 3; NEW: 2; REMOVE: 6

## PN Consistency Summary

- **Consistency:** Deep-research notes, review YAML, and PN-node BRISC mapping all agree ABRAXAS2 (=ABRO1/FAM175B) is a **noncatalytic BRISC scaffold/adaptor**, not a catalytic JAMM DUB. **Partial contradiction at the DNA-repair node:** the PN row-2 group projects broad GO:0006281 DNA repair, but the review and notes explicitly argue ABRO1 lacks the BRCA1-interacting motif and does NOT join BRCA1-A/DNA-repair sites (PMID:21282113), so direct DNA-repair propagation is rejected.
- **PN story / NEW pressure:** BRISC complex membership is already captured (GO:0070552, IDA/IPI/NAS in GOA). The DNA-repair claim over-reaches for this paralog. The review instead adds well-supported NEW terms the PN node does not surface: **GO:0043517** positive regulation of DNA damage response, signal transduction by p53 class mediator (OLS-verified real; PMID:25283148, ABRO1 stabilizes p53 via USP7) and **GO:0060340** positive regulation of type I interferon-mediated signaling (PMID:24075985/31142841, BRISC-SHMT2/IFNAR1), plus NuMA spindle-assembly terms. Conclusion: BRISC = already captured; DNA repair = PN over-reaches; p53-DDR signaling = legitimate ADD already done in review.
- **Evidence alignment:** PN row references (PMID:36473924, 19261749) overlap the review's BRISC/polyubiquitin-binding evidence (PMID:19261749 used, marked over-annotated as BRCA1-A-specific). Review extends far beyond PN refs (PMID:21282113, 20656690, 24075985, 25283148, 26195665, 31142841, 31253574) — divergence is enrichment, not conflict.
- **Verdict:** Consistent on BRISC; PN DNA-repair projection over-reaches and is correctly declined; review's p53-DDR/IFN NEW terms are sound. **Recommended edits:** [MAP] Do not project GO:0006281 DNA repair to ABRAXAS2; the supported DNA-damage role is GO:0043517 (p53-class DDR signaling), already added in the review.

## Full Consistency Review

- **UniProt:** Q15018 · **batch:** proteostasis-batch-2026-06-03 · **review status:** COMPLETE
- **PN placement:** `Ubiquitin Proteasome System|DUBs and UBL demodifiers|BRISC complex|noncatalytic|JAMM / MPN / ubiquitin binding` (row 1) and `...|Ubiquitin and UBL binding|DNA repair|BRISC complex component|...` (row 2) ; **PN-node mapping:** group/type `BRISC complex`=mapped→**GO:0070552 BRISC complex** (already_in_goa_exact); group `...|DNA repair`=mapped→**GO:0006281 DNA repair** (new_to_goa); class `Ubiquitin and UBL binding`=context_only (too_broad).
- **Consistency:** Deep-research notes, review YAML, and PN-node BRISC mapping all agree ABRAXAS2 (=ABRO1/FAM175B) is a **noncatalytic BRISC scaffold/adaptor**, not a catalytic JAMM DUB. **Partial contradiction at the DNA-repair node:** the PN row-2 group projects broad GO:0006281 DNA repair, but the review and notes explicitly argue ABRO1 lacks the BRCA1-interacting motif and does NOT join BRCA1-A/DNA-repair sites (PMID:21282113), so direct DNA-repair propagation is rejected.
- **PN story / NEW pressure:** BRISC complex membership is already captured (GO:0070552, IDA/IPI/NAS in GOA). The DNA-repair claim over-reaches for this paralog. The review instead adds well-supported NEW terms the PN node does not surface: **GO:0043517** positive regulation of DNA damage response, signal transduction by p53 class mediator (OLS-verified real; PMID:25283148, ABRO1 stabilizes p53 via USP7) and **GO:0060340** positive regulation of type I interferon-mediated signaling (PMID:24075985/31142841, BRISC-SHMT2/IFNAR1), plus NuMA spindle-assembly terms. Conclusion: BRISC = already captured; DNA repair = PN over-reaches; p53-DDR signaling = legitimate ADD already done in review.
- **Mapping strategy:** The BRISC node mapping is correct and stable. The `...|DNA repair` group node should **not** propagate GO:0006281 to ABRAXAS2 — the p53-class mediator is a paralog-specific signaling role, not direct repair. This mirrors the precedent of suppressing an over-broad projected term for a specific gene.
- **Evidence alignment:** PN row references (PMID:36473924, 19261749) overlap the review's BRISC/polyubiquitin-binding evidence (PMID:19261749 used, marked over-annotated as BRCA1-A-specific). Review extends far beyond PN refs (PMID:21282113, 20656690, 24075985, 25283148, 26195665, 31142841, 31253574) — divergence is enrichment, not conflict.
- **Verdict:** Consistent on BRISC; PN DNA-repair projection over-reaches and is correctly declined; review's p53-DDR/IFN NEW terms are sound. **Recommended edits:** [MAP] Do not project GO:0006281 DNA repair to ABRAXAS2; the supported DNA-damage role is GO:0043517 (p53-class DDR signaling), already added in the review.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-03
- review_yaml: genes/human/ABRAXAS2/ABRAXAS2-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Ubiquitin Proteasome System | DUBs and UBL demodifiers | BRISC complex | noncatalytic | JAMM / MPN / ubiquitin binding
- UniProt: Q15018
- In branches: UPS
- Signature domains: (none)
- Auxiliary domains: IPR037518
- PN references (titles):
    - 36473924
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|DUBs and UBL demodifiers|BRISC complex|noncatalytic|JAMM / MPN / ubiquitin binding
        status=no_mapping scope= GO=[]
        rationale: Reviewed manually as a UPS source node. No single GO term is appropriate for direct propagation from this PN label without narrower context or gene-level evidence.
    - [type] Ubiquitin Proteasome System|DUBs and UBL demodifiers|BRISC complex|noncatalytic
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0070552 BRISC complex]
        rationale: This PN type covers noncatalytic BRISC subunits, so complex membership is the safe propagation target rather than catalytic DUB activity.
    - [group] Ubiquitin Proteasome System|DUBs and UBL demodifiers|BRISC complex
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0070552 BRISC complex]
        rationale: This PN group denotes BRISC complex members. The matching GO cellular-component term is BRISC complex.
    - [class] Ubiquitin Proteasome System|DUBs and UBL demodifiers
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a UPS taxonomy container. Its descendants mix catalytic roles, complex membership, binding domains, regulators, adaptors, and substrate-context labels, so a single propagating GO assertion would overstate the shared biology.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## PN row 2: Ubiquitin Proteasome System | Ubiquitin and UBL binding | DNA repair | BRISC complex component | idiosyncratic Ub binding / MPN
- UniProt: Q15018
- In branches: UPS
- Signature domains: PMID: 19261749 (IPR037518)
- Auxiliary domains: (none)
- PN references (titles):
    - 19261749
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|Ubiquitin and UBL binding|DNA repair|BRISC complex component|idiosyncratic Ub binding / MPN
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a family, domain, architecture, or residual subdivision. The label is useful for PN taxonomy navigation but is not itself a GO annotation target; any functional assertion should come from a curated parent role or gene-level evidence.
    - [type] Ubiquitin Proteasome System|Ubiquitin and UBL binding|DNA repair|BRISC complex component
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a UPS taxonomy container. Its descendants mix catalytic roles, complex membership, binding domains, regulators, adaptors, and substrate-context labels, so a single propagating GO assertion would overstate the shared biology.
    - [group] Ubiquitin Proteasome System|Ubiquitin and UBL binding|DNA repair
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0006281 DNA repair]
        rationale: This PN group captures ubiquitin/UBL-binding factors assigned to DNA repair contexts. The group is context-defined rather than GO-equivalent, but propagation to DNA repair is appropriate.
    - [class] Ubiquitin Proteasome System|Ubiquitin and UBL binding
        status=context_only scope=too_broad_to_propagate GO=[GO:0140036 ubiquitin-modified protein reader activity]
        rationale: This class records ubiquitin/UBL-reader context, but the subtree mixes ubiquitin, SUMO, UBL-domain, domain-architecture, catalytic, signaling, trafficking, and nucleic-acid process buckets. It is useful context, not a safe direct propagation.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## Projected GO annotations (3)
- GO:0070552 BRISC complex | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Ubiquitin Proteasome System|DUBs and UBL demodifiers|BRISC complex
- GO:0070552 BRISC complex | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Ubiquitin Proteasome System|DUBs and UBL demodifiers|BRISC complex|noncatalytic
- GO:0006281 DNA repair | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Ubiquitin Proteasome System|Ubiquitin and UBL binding|DNA repair

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
