# ABRAXAS1 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q6UWZ7
- AIGR review status: DRAFT
- Review batch: proteostasis-batch-2026-06-03 (PR 1327)
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/ABRAXAS1/ABRAXAS1-ai-review.yaml](ABRAXAS1-ai-review.yaml)
- AIGR review HTML: present - [genes/human/ABRAXAS1/ABRAXAS1-ai-review.html](ABRAXAS1-ai-review.html)
- Gene notes: present - [genes/human/ABRAXAS1/ABRAXAS1-notes.md](ABRAXAS1-notes.md)
- GOA TSV: present - [genes/human/ABRAXAS1/ABRAXAS1-goa.tsv](ABRAXAS1-goa.tsv)
- UniProt record: present - [genes/human/ABRAXAS1/ABRAXAS1-uniprot.txt](ABRAXAS1-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/ABRAXAS1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/ABRAXAS1.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ABRAXAS1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ABRAXAS1.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/ABRAXAS1/ABRAXAS1-deep-research-falcon.md](ABRAXAS1-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: ABRAXAS1 encodes a nuclear BRCA1-A complex subunit that acts as a scaffold linking BRCA1, UIMC1/RAP80, BRCC3/BRCC36, BABAM proteins, and ubiquitin-dependent DNA damage-site signaling. The protein contains an MPN-like domain, binds polyubiquitin as part of the BRCA1-A/RAP80 complex, and supports BRCA1 recruitment, DNA double-strand break repair, K63-ubiquitin signal editing by BRCC36, and G2/M DNA damage checkpoint responses.
- Existing/core annotation action counts: ACCEPT: 30; KEEP_AS_NON_CORE: 4; MARK_AS_OVER_ANNOTATED: 11; MODIFY: 2; REMOVE: 3

## PN Consistency Summary

- **Consistency:** Consistent on the core: deep-research/notes, review, and PN all converge on ABRAXAS1 as a nuclear BRCA1-A/RAP80 scaffold + polyubiquitin-reader (MPN-like) in DNA damage response. Review accepts GO:0070531 BRCA1-A complex (core), GO:0031593 polyubiquitin-dependent binding, GO:0006302 DSB repair, GO:0045739 positive regulation of DNA repair, GO:0007095 G2 checkpoint. One nuance: the PN group projects GO:0000151 "ubiquitin ligase complex," but the review prefers the more specific GO:0070531 and explicitly calls GO:0000151 "more precise than the PN-projected generic ubiquitin-ligase-complex bucket." Note ABRAXAS1 is a scaffold/DUB-support subunit, **not** an E3 catalytic ligase — so the RING/ligase framing is a placement convenience, not a function claim (review is careful here). No hard contradiction.
- **PN story / NEW pressure:** PN's DNA-repair + ubiquitin-binding + BRCA1-A story is fully captured (GO:0006281 entailed by accepted GO:0006302; GO:0070531 present; GO:0031593 present). All PN-projected terms verified real. Conclusion: **already captured**; the only over-reach is the generic ligase-complex bucket, which the review supersedes with GO:0070531.
- **Evidence alignment:** Good overlap. PN reference titles cite PMID:17525340 (row 1) and PMID:19261749 (row 2 signature domain, IPR037518/MPN) — both are central review references (17525340 = ACCEPT-supporting for nucleus/checkpoint/DSB; 19261749 = NBA1/BRCA1-A + polyubiquitin binding). PN and review cite the same anchor papers.
- **Verdict:** Consistent; PN captured (review uses more specific complex term, correctly avoids E3-catalytic over-claim). Status is DRAFT. No substantive edits warranted (optional: finalize DRAFT→COMPLETE after the open RNA-binding and SSA/MMEJ negative-regulation questions are settled).

## Full Consistency Review

- **UniProt:** Q6UWZ7 · **batch:** proteostasis-batch-2026-06-03 · **review status:** DRAFT
- **PN placement (2 rows):** `UPS|E3 ubiquitin and UBL ligases|idiosyncratic RING complex|BRCA1-A complex|ubiquitin binding` AND `UPS|Ubiquitin and UBL binding|DNA repair|BRCA1-A complex component|idiosyncratic Ub binding / MPN` ; **PN-node mapping:** type `BRCA1-A complex`=mapped→GO:0070531 (already_in_goa_exact); group `idiosyncratic RING complex`=mapped→GO:0000151 ubiquitin ligase complex (new_to_goa); group `...|DNA repair`=mapped→GO:0006281 DNA repair (entailed_by_goa_closure); class `E3...ligases`/`Ub and UBL binding`=context_only; branch UPS=no_mapping.
- **Consistency:** Consistent on the core: deep-research/notes, review, and PN all converge on ABRAXAS1 as a nuclear BRCA1-A/RAP80 scaffold + polyubiquitin-reader (MPN-like) in DNA damage response. Review accepts GO:0070531 BRCA1-A complex (core), GO:0031593 polyubiquitin-dependent binding, GO:0006302 DSB repair, GO:0045739 positive regulation of DNA repair, GO:0007095 G2 checkpoint. One nuance: the PN group projects GO:0000151 "ubiquitin ligase complex," but the review prefers the more specific GO:0070531 and explicitly calls GO:0000151 "more precise than the PN-projected generic ubiquitin-ligase-complex bucket." Note ABRAXAS1 is a scaffold/DUB-support subunit, **not** an E3 catalytic ligase — so the RING/ligase framing is a placement convenience, not a function claim (review is careful here). No hard contradiction.
- **PN story / NEW pressure:** PN's DNA-repair + ubiquitin-binding + BRCA1-A story is fully captured (GO:0006281 entailed by accepted GO:0006302; GO:0070531 present; GO:0031593 present). All PN-projected terms verified real. Conclusion: **already captured**; the only over-reach is the generic ligase-complex bucket, which the review supersedes with GO:0070531.
- **Mapping strategy:** Group node GO:0000151 should be treated as non-propagating to ABRAXAS1 (review holds the narrower, child term GO:0070531). The DNA-repair group→GO:0006281 is already entailed. Type node GO:0070531 is correct. No new propagation needed.
- **Evidence alignment:** Good overlap. PN reference titles cite PMID:17525340 (row 1) and PMID:19261749 (row 2 signature domain, IPR037518/MPN) — both are central review references (17525340 = ACCEPT-supporting for nucleus/checkpoint/DSB; 19261749 = NBA1/BRCA1-A + polyubiquitin binding). PN and review cite the same anchor papers.
- **Verdict:** Consistent; PN captured (review uses more specific complex term, correctly avoids E3-catalytic over-claim). Status is DRAFT. No substantive edits warranted (optional: finalize DRAFT→COMPLETE after the open RNA-binding and SSA/MMEJ negative-regulation questions are settled).

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-03
- review_yaml: genes/human/ABRAXAS1/ABRAXAS1-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Ubiquitin Proteasome System | E3 ubiquitin and UBL ligases | idiosyncratic RING complex | BRCA1-A complex | ubiquitin binding
- UniProt: Q6UWZ7
- In branches: UPS
- Signature domains: (none)
- Auxiliary domains: PMID: 19261749 (IPR037518)
- PN references (titles):
    - 17525340
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|idiosyncratic RING complex|BRCA1-A complex|ubiquitin binding
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower E3-ligase architecture, component, or domain subdivision already covered by the curated parent E3 mapping. No additional direct GO mapping is needed at this node.
    - [type] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|idiosyncratic RING complex|BRCA1-A complex
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0070531 BRCA1-A complex]
        rationale: This PN type denotes BRCA1-A complex members. The matching GO cellular-component term is BRCA1-A complex.
    - [group] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|idiosyncratic RING complex
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0000151 ubiquitin ligase complex]
        rationale: This PN group is an E3 ligase complex bucket. The safest shared GO target is ubiquitin ligase complex membership rather than assigning catalytic activity to every subunit.
    - [class] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases
        status=context_only scope=too_broad_to_propagate GO=[GO:0061630 ubiquitin protein ligase activity]
        rationale: This class is a genuine E3-ligase context, but its descendants include catalytic ligases, cullin scaffolds, substrate receptors, adaptors, cofactors, regulators, and UBL modifier systems. A class-level propagation would over-annotate.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## PN row 2: Ubiquitin Proteasome System | Ubiquitin and UBL binding | DNA repair | BRCA1-A complex component | idiosyncratic Ub binding / MPN
- UniProt: Q6UWZ7
- In branches: UPS
- Signature domains: PMID: 19261749 (IPR037518)
- Auxiliary domains: (none)
- PN references (titles):
    - 19261749
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|Ubiquitin and UBL binding|DNA repair|BRCA1-A complex component|idiosyncratic Ub binding / MPN
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a family, domain, architecture, or residual subdivision. The label is useful for PN taxonomy navigation but is not itself a GO annotation target; any functional assertion should come from a curated parent role or gene-level evidence.
    - [type] Ubiquitin Proteasome System|Ubiquitin and UBL binding|DNA repair|BRCA1-A complex component
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
- GO:0000151 ubiquitin ligase complex | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|idiosyncratic RING complex
- GO:0070531 BRCA1-A complex | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|idiosyncratic RING complex|BRCA1-A complex
- GO:0006281 DNA repair | scope=ok_for_propagation_to_go | goa_status=entailed_by_goa_closure | from=Ubiquitin Proteasome System|Ubiquitin and UBL binding|DNA repair

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
