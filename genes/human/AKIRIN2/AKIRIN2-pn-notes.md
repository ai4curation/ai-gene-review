# AKIRIN2 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q53H80
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-03 (PR 1361)
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/AKIRIN2/AKIRIN2-ai-review.yaml](AKIRIN2-ai-review.yaml)
- AIGR review HTML: present - [genes/human/AKIRIN2/AKIRIN2-ai-review.html](AKIRIN2-ai-review.html)
- Gene notes: present - [genes/human/AKIRIN2/AKIRIN2-notes.md](AKIRIN2-notes.md)
- GOA TSV: present - [genes/human/AKIRIN2/AKIRIN2-goa.tsv](AKIRIN2-goa.tsv)
- UniProt record: present - [genes/human/AKIRIN2/AKIRIN2-uniprot.txt](AKIRIN2-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/AKIRIN2.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/AKIRIN2.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/AKIRIN2.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/AKIRIN2.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/AKIRIN2/AKIRIN2-deep-research-falcon.md](AKIRIN2-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: AKIRIN2 encodes a conserved, predominantly nuclear akirin-family adaptor protein. In vertebrate cells, AKIRIN2 homodimers bind assembled proteasomes and the import receptor IPO9 to promote proteasome import into the nucleus, supporting nuclear protein degradation. Akirin proteins also act as nuclear transcriptional coregulators downstream of NF-kappaB and chromatin-remodeling machinery, linking conserved immune and developmental gene-expression programs to a small, domain-poor adaptor protein.
- Existing/core annotation action counts: ACCEPT: 16; KEEP_AS_NON_CORE: 17; MARK_AS_OVER_ANNOTATED: 9; MODIFY: 1; NEW: 1

## PN Consistency Summary

- **Consistency:** Fully consistent across all four layers. Deep research (falcon), review, PN annotation, and PN-node mapping all agree AKIRIN2 is the proteasome-import adaptor: homodimers bridge assembled 20S proteasomes to importin IPO9 for nuclear import (PMID:34711951). Review adopts the PN projection as **action NEW GO:0070628**, plus GO:0030674 adaptor activity, GO:0006606, GO:0031144, GO:0071630 — a coherent proteostasis core.
- **PN story / NEW pressure:** PN asserts proteasome binding not in GOA; GOA confirms only GO:0031144 and GO:0071630 are present (GO:0070628 genuinely new_to_goa). GO:0070628 verified real and **directly supported** by primary biochemistry. Verdict: ADD — well justified; this is the model case the Akirin bucket was built for.
- **Evidence alignment:** Strong overlap. PN reference 34711951 = the central review reference PMID:34711951. Review additionally MARK_AS_OVER_ANNOTATED the many high-throughput protein-binding rows (PMID:16189514, 28514442, 31515488, 32296183, 33961781, 40205054) — consistent triage, no conflict.
- **Verdict:** Consistent and well-supported; GO:0070628 ADD confirmed (already realized as NEW in review).

## Full Consistency Review

- **UniProt:** Q53H80 · **batch:** proteostasis-batch-2026-06-03 · **review status:** COMPLETE
- **PN placement:** `Ubiquitin Proteasome System|Proteasome and associated proteins|adaptors|Akirin` ; **PN-node mapping:** Akirin *type* no_mapping; *group* (adaptors) mapped→GO:0070628 (proteasome binding, propagate); class context_only→GO:0000502. Projection: **GO:0070628 new_to_goa**.
- **Consistency:** Fully consistent across all four layers. Deep research (falcon), review, PN annotation, and PN-node mapping all agree AKIRIN2 is the proteasome-import adaptor: homodimers bridge assembled 20S proteasomes to importin IPO9 for nuclear import (PMID:34711951). Review adopts the PN projection as **action NEW GO:0070628**, plus GO:0030674 adaptor activity, GO:0006606, GO:0031144, GO:0071630 — a coherent proteostasis core.
- **PN story / NEW pressure:** PN asserts proteasome binding not in GOA; GOA confirms only GO:0031144 and GO:0071630 are present (GO:0070628 genuinely new_to_goa). GO:0070628 verified real and **directly supported** by primary biochemistry. Verdict: ADD — well justified; this is the model case the Akirin bucket was built for.
- **Mapping strategy:** No change to the node for AKIRIN2; the adaptors→GO:0070628 mapping is exactly right here. (The only caveat is shared with AKIRIN1: the Akirin *type* lumps both paralogs, and the proteasome activity is AKIRIN2-specific — see AKIRIN1 recommendation to split. AKIRIN2 keeps the mapping.) PN-projected GO:0070628 is appropriately specific (neither broader nor narrower than the review's core MF).
- **Evidence alignment:** Strong overlap. PN reference 34711951 = the central review reference PMID:34711951. Review additionally MARK_AS_OVER_ANNOTATED the many high-throughput protein-binding rows (PMID:16189514, 28514442, 31515488, 32296183, 33961781, 40205054) — consistent triage, no conflict.
- **Verdict:** Consistent and well-supported; GO:0070628 ADD confirmed (already realized as NEW in review).
- **Recommended edits:** None for AKIRIN2 (mapping and review aligned). (Cross-ref: the AKIRIN1 split recommendation keeps GO:0070628 on AKIRIN2 only.)

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-03
- review_yaml: genes/human/AKIRIN2/AKIRIN2-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Ubiquitin Proteasome System | Proteasome and associated proteins | adaptors | Akirin
- UniProt: Q53H80
- In branches: UPS
- Signature domains: IPR024132
- Auxiliary domains: (none)
- PN references (titles):
    - 34711951
- PN-node mapping records (path + ancestors):
    - [type] Ubiquitin Proteasome System|Proteasome and associated proteins|adaptors|Akirin
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower proteasome component, chaperone, adaptor, domain, or isoform subdivision already covered by a curated parent proteasome mapping. No additional direct GO mapping is needed at this node.
    - [group] Ubiquitin Proteasome System|Proteasome and associated proteins|adaptors
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0070628 proteasome binding]
        rationale: This PN group captures proteasome adaptors and shuttle factors. Proteasome binding is the safe shared molecular-function target.
    - [class] Ubiquitin Proteasome System|Proteasome and associated proteins
        status=context_only scope=too_broad_to_propagate GO=[GO:0000502 proteasome complex]
        rationale: This class records the proteasome branch context, but descendants include core and regulatory particle subunits, activators, assembly chaperones, adaptors, DUBs, E3 ligases, enzymes, and transcriptional regulators. Propagation should come from narrower nodes.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## Projected GO annotations (1)
- GO:0070628 proteasome binding | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Ubiquitin Proteasome System|Proteasome and associated proteins|adaptors

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
