# HSPB3 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q12988
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07b
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/HSPB3/HSPB3-ai-review.yaml](HSPB3-ai-review.yaml)
- AIGR review HTML: present - [genes/human/HSPB3/HSPB3-ai-review.html](HSPB3-ai-review.html)
- Gene notes: present - [genes/human/HSPB3/HSPB3-notes.md](HSPB3-notes.md)
- GOA TSV: present - [genes/human/HSPB3/HSPB3-goa.tsv](HSPB3-goa.tsv)
- UniProt record: present - [genes/human/HSPB3/HSPB3-uniprot.txt](HSPB3-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/HSPB3.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/HSPB3.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/HSPB3.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/HSPB3.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: HSPB3 (heat shock protein beta-3, also called HSP17 or HSPL27) is a member of the small heat shock protein (sHSP / HSP20, alpha-crystallin domain) family. It is the most divergent of the human small HSPs, possessing a unique N-terminal domain and essentially lacking the C-terminal extension found in other family members, while retaining the conserved alpha-crystallin domain. Like other small HSPs it is an ATP-independent molecular chaperone that binds partially unfolded client proteins and holds them in a folding-competent state, and it has been reported to inhibit actin polymerization. HSPB3 forms a hetero-oligomeric complex with its partner small HSP HSPB2 (MKBP). It is expressed predominantly in striated and smooth muscle (heart, skeletal muscle, tongue), localizes to the cytoplasm and nucleus, and translocates to nuclear foci during heat shock. Dominant missense variants in HSPB3 cause autosomal dominant distal hereditary motor neuronopathy.
- Existing/core annotation action counts: ACCEPT: 7; KEEP_AS_NON_CORE: 2; NEW: 1

## PN Consistency Summary

- **Consistency:** Notes ↔ review fully consistent — HSPB3 is the most divergent human sHSP (HSP20/alpha-crystallin family), an ATP-independent holdase partnering HSPB2 in muscle, cytoplasm+nucleus, R7S causes HMND4 (PMID:9858786, 8972725, 20142617, 19464326). The PN mitochondrial row is questionable: neither review, notes, UniProt nor GOA places HSPB3 in mitochondria (documented compartments are cytoplasm/nucleus), so the "Mitochondrial proteostasis" placement is a PN-internal contradiction with the evidence.
- **PN story / NEW pressure:** GOA has NO molecular-function annotation for HSPB3 (only GO:0006986 response to unfolded protein, TAS). PN projects GO:0044183 protein folding chaperone as new_to_goa. Verified real, but its OLS definition is a foldase ("binds an unfolded protein **to fold it**... do not confuse with unfolded protein holdase activity"). HSPB3 is a holdase, not a foldase. The review's core MF is GO:0051082 unfolded protein binding (holdase); the precise term is GO:0140309 unfolded protein holdase activity (verified real). So an MF gap exists, but GO:0044183 over-reaches the wrong way.
- **Evidence alignment:** PN rows carry no reference titles for HSPB3; review PMIDs (9858786, 8972725, 20142617, 19464326) are sHSP-identity/localization/disease papers — no divergence, just no overlap to compare.
- **Verdict:** sHSP placement sound but PN MF target mischaracterizes holdases as foldases; mito row unsupported. **Recommended edits:** [MAP] retarget GO:0044183 → GO:0140309 unfolded protein holdase activity (or GO:0051082) for sHSP nodes on Q12988; [MAP] do not project a mitochondrial chaperone term onto HSPB3 (no mitochondrial localization evidence).

## Full Consistency Review

- **UniProt:** Q12988 · **batch:** proteostasis-batch-2026-06-07b · **review status:** COMPLETE
- **PN placement:** two rows — `Cytonuclear proteostasis|Chaperone|small HSP system|small HSP` (type) and `Mitochondrial proteostasis|Chaperone|small HSP` (group) ; **PN-node mapping:** both sHSP nodes → mapped/ok_for_propagation_to_go GO:0044183 protein folding chaperone (new_to_goa); class/branch nodes no_mapping.
- **Consistency:** Notes ↔ review fully consistent — HSPB3 is the most divergent human sHSP (HSP20/alpha-crystallin family), an ATP-independent holdase partnering HSPB2 in muscle, cytoplasm+nucleus, R7S causes HMND4 (PMID:9858786, 8972725, 20142617, 19464326). The PN mitochondrial row is questionable: neither review, notes, UniProt nor GOA places HSPB3 in mitochondria (documented compartments are cytoplasm/nucleus), so the "Mitochondrial proteostasis" placement is a PN-internal contradiction with the evidence.
- **PN story / NEW pressure:** GOA has NO molecular-function annotation for HSPB3 (only GO:0006986 response to unfolded protein, TAS). PN projects GO:0044183 protein folding chaperone as new_to_goa. Verified real, but its OLS definition is a foldase ("binds an unfolded protein **to fold it**... do not confuse with unfolded protein holdase activity"). HSPB3 is a holdase, not a foldase. The review's core MF is GO:0051082 unfolded protein binding (holdase); the precise term is GO:0140309 unfolded protein holdase activity (verified real). So an MF gap exists, but GO:0044183 over-reaches the wrong way.
- **Mapping strategy:** Keep status=mapped but the target is wrong for sHSPs. GO:0044183 (foldase) is broader/different from the holdase activity sHSPs actually have. Prefer GO:0140309 unfolded protein holdase activity (or GO:0051082). Drop or re-scope the mitochondrial-row projection (no mito evidence for HSPB3).
- **Evidence alignment:** PN rows carry no reference titles for HSPB3; review PMIDs (9858786, 8972725, 20142617, 19464326) are sHSP-identity/localization/disease papers — no divergence, just no overlap to compare.
- **Verdict:** sHSP placement sound but PN MF target mischaracterizes holdases as foldases; mito row unsupported. **Recommended edits:** [MAP] retarget GO:0044183 → GO:0140309 unfolded protein holdase activity (or GO:0051082) for sHSP nodes on Q12988; [MAP] do not project a mitochondrial chaperone term onto HSPB3 (no mitochondrial localization evidence).

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07b
- review_yaml: genes/human/HSPB3/HSPB3-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Cytonuclear proteostasis | Chaperone | small HSP system | small HSP
- UniProt: Q12988
- In branches: CY, MI
- PN-node mapping records (path + ancestors):
    - [type] Cytonuclear proteostasis|Chaperone|small HSP system|small HSP
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0044183 protein folding chaperone]
        rationale: This PN type denotes small heat-shock chaperones. Protein folding chaperone is the appropriate shared molecular-function term.
    - [group] Cytonuclear proteostasis|Chaperone|small HSP system
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower taxonomy bucket that is already covered by a curated parent mapping or by gene-level annotations. No additional direct GO mapping is appropriate from this node.
    - [class] Cytonuclear proteostasis|Chaperone
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a specific GO class. The member genes span multiple activities, complexes, or contexts, so propagation from this node would overstate the shared biology; use narrower child or gene-level curations.
    - [branch] Cytonuclear proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## PN row 2: Mitochondrial proteostasis | Chaperone | small HSP
- UniProt: Q12988
- In branches: CY, MI
- PN-node mapping records (path + ancestors):
    - [group] Mitochondrial proteostasis|Chaperone|small HSP
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0044183 protein folding chaperone]
        rationale: This PN group denotes mitochondrial small heat-shock chaperones. Protein folding chaperone is the appropriate shared molecular-function term.
    - [class] Mitochondrial proteostasis|Chaperone
        status=no_mapping scope= GO=[]
        rationale: This PN class is too heterogeneous for a single safe GO mapping. In the workbook it mixes HSP70, HSP60, and HSP90 systems, small intermembrane-space chaperones, membrane-protein chaperones, and other mitochondrial-specific factors.
    - [branch] Mitochondrial proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## Projected GO annotations (2)
- GO:0044183 protein folding chaperone | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Cytonuclear proteostasis|Chaperone|small HSP system|small HSP
- GO:0044183 protein folding chaperone | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Mitochondrial proteostasis|Chaperone|small HSP

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
