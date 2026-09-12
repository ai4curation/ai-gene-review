# HSPB8 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9UJY1
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07b
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/HSPB8/HSPB8-ai-review.yaml](HSPB8-ai-review.yaml)
- AIGR review HTML: present - [genes/human/HSPB8/HSPB8-ai-review.html](HSPB8-ai-review.html)
- Gene notes: present - [genes/human/HSPB8/HSPB8-notes.md](HSPB8-notes.md)
- GOA TSV: present - [genes/human/HSPB8/HSPB8-goa.tsv](HSPB8-goa.tsv)
- UniProt record: present - [genes/human/HSPB8/HSPB8-uniprot.txt](HSPB8-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/HSPB8.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/HSPB8.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/HSPB8.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/HSPB8.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: HSPB8 (heat shock protein beta-8, also called HSP22, H11 kinase, E2IG1 or alpha-crystallin C chain) is a member of the small heat shock protein (sHSP / HSP20, alpha-crystallin domain) family, predominantly expressed in skeletal muscle and heart. It is an ATP-independent molecular chaperone (holdase) that binds aggregation-prone and stress-destabilized client proteins. Its central role is in chaperone-assisted selective autophagy (CASA), where together with the co-chaperone BAG3, the Hsp70 chaperones HSPA8/HSC70 and HSPA1A, and the ubiquitin ligase STUB1/CHIP, HSPB8 routes damaged clients (e.g. filamin and polyglutamine-expanded proteins) for autophagic degradation via p62/SQSTM1, a process essential for maintenance of the muscle Z-disk under mechanical stress. HSPB8 forms homodimers and hetero-oligomers with other small HSPs (HSPB1, HSPB2, HSPB7) and DNAJB6. Despite an early report of protein kinase activity, recombinant HSPB8 lacks detectable kinase activity. It localizes to the cytoplasm and nucleus and translocates to nuclear foci during heat shock. Dominant variants (notably at the K141 hot spot) cause distal hereditary motor neuropathy, Charcot-Marie-Tooth disease type 2L, and myofibrillar/rimmed-vacuole myopathy.
- Existing/core annotation action counts: ACCEPT: 18; KEEP_AS_NON_CORE: 13; MODIFY: 4

## PN Consistency Summary

- **Consistency:** Best-evidenced of the six and fully consistent across notes ↔ review ↔ PN CASA row. HSPB8/HSP22 is an ATP-independent holdase (PMID:14985082) and the sHSP of the CASA complex with BAG3/HSPA8/STUB1 driving aggrephagy of polyQ/filamin (PMID:18006506, 20060297). The PN CASA row even cites matching CASA papers. Mitochondrial row is unsupported (HSPB8 documented in cytoplasm/nucleus, not mitochondria).
- **PN story / NEW pressure:** The CASA/aggrephagy story is ALREADY captured: review has GO:1905337 positive regulation of aggrephagy (IMP) and GO:0034620 cellular response to unfolded protein; GOA carries GO:1905337. PN's GO:0035973 aggrephagy is the parent process and is correctly flagged supported_by_goa_regulation — already captured. The sHSP GO:0044183 projection is the same foldase-vs-holdase over-reach as the other sHSPs (HSPB8 is a holdase per PMID:14985082; GOA has no folding-chaperone MF, core MF is GO:0051082 unfolded protein binding + GO:0051087 protein-folding chaperone binding for the BAG3 interaction).
- **Evidence alignment:** Strong overlap — PN CASA-row titles (CASA complex dynamics; HspB8 promotes autophagic removal in ALS; HSPB8-BAG3-HSP70 stress-granule surveillance) align with the review's CASA PMIDs (18006506, 20060297). No divergence on the autophagy story.
- **Verdict:** CASA/aggrephagy projection sound and already captured; sHSP foldase MF over-reaches, mito row unsupported. **Recommended edits:** [MAP] retarget sHSP GO:0044183 → GO:0140309 / GO:0051082 on Q9UJY1; [MAP] do not project a mitochondrial chaperone term onto HSPB8 (no mito localization). CASA row needs no change.

## Full Consistency Review

- **UniProt:** Q9UJY1 · **batch:** proteostasis-batch-2026-06-07b · **review status:** COMPLETE
- **PN placement:** three rows — `Cytonuclear proteostasis|...|small HSP` (type), `Mitochondrial proteostasis|Chaperone|small HSP` (group), and `Autophagy-Lysosome Pathway|...|Chaperone assisted selective autophagy|CASA complex component` (subtype) ; **PN-node mapping:** sHSP nodes → mapped/ok GO:0044183 protein folding chaperone (new_to_goa); CASA subtype → mapped/ok GO:0035973 aggrephagy (supported_by_goa_regulation).
- **Consistency:** Best-evidenced of the six and fully consistent across notes ↔ review ↔ PN CASA row. HSPB8/HSP22 is an ATP-independent holdase (PMID:14985082) and the sHSP of the CASA complex with BAG3/HSPA8/STUB1 driving aggrephagy of polyQ/filamin (PMID:18006506, 20060297). The PN CASA row even cites matching CASA papers. Mitochondrial row is unsupported (HSPB8 documented in cytoplasm/nucleus, not mitochondria).
- **PN story / NEW pressure:** The CASA/aggrephagy story is ALREADY captured: review has GO:1905337 positive regulation of aggrephagy (IMP) and GO:0034620 cellular response to unfolded protein; GOA carries GO:1905337. PN's GO:0035973 aggrephagy is the parent process and is correctly flagged supported_by_goa_regulation — already captured. The sHSP GO:0044183 projection is the same foldase-vs-holdase over-reach as the other sHSPs (HSPB8 is a holdase per PMID:14985082; GOA has no folding-chaperone MF, core MF is GO:0051082 unfolded protein binding + GO:0051087 protein-folding chaperone binding for the BAG3 interaction).
- **Mapping strategy:** CASA subtype → GO:0035973 needs no change (already covered by stronger GO:1905337 in review/GOA). The sHSP GO:0044183 target is the wrong MF (foldase) for this holdase; prefer GO:0140309 holdase / GO:0051082. Drop the mitochondrial-row chaperone projection.
- **Evidence alignment:** Strong overlap — PN CASA-row titles (CASA complex dynamics; HspB8 promotes autophagic removal in ALS; HSPB8-BAG3-HSP70 stress-granule surveillance) align with the review's CASA PMIDs (18006506, 20060297). No divergence on the autophagy story.
- **Verdict:** CASA/aggrephagy projection sound and already captured; sHSP foldase MF over-reaches, mito row unsupported. **Recommended edits:** [MAP] retarget sHSP GO:0044183 → GO:0140309 / GO:0051082 on Q9UJY1; [MAP] do not project a mitochondrial chaperone term onto HSPB8 (no mito localization). CASA row needs no change.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07b
- review_yaml: genes/human/HSPB8/HSPB8-ai-review.yaml
- PN workbook rows: 3

## PN row 1: Cytonuclear proteostasis | Chaperone | small HSP system | small HSP
- UniProt: Q9UJY1
- In branches: CY, MI, ALP
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
- UniProt: Q9UJY1
- In branches: CY, MI, ALP
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

## PN row 3: Autophagy-Lysosome Pathway | Autophagy substrate selection | Selective autophagy receptor | Chaperone assisted selective autophagy | CASA complex component
- UniProt: Q9UJY1
- In branches: CY, MI, ALP
- Notes: Small heat shock protein. Participates in chaperone-assisted selective autophagy by forming the CASA complex (HSPA8, BAG3, HSPB8, and STUB1) that delivers ubiquitinated substrates to the to the autophagosome
- PN references (titles):
    - Full article: The chaperone-assisted selective autophagy complex dynamics and dysfunctions (tandfonline.com)
    - small heat shock protein B8 (HspB8) promotes autophagic removal of misfolded proteins involved in amyotrophic lateral sclerosis (ALS) | Human Molecular Genetics | Oxford Academic (oup.com)
    - A Surveillance Function of the HSPB8-BAG3-HSP70 Chaperone Complex Ensures Stress Granule Integrity and Dynamism - ScienceDirect
- PN-node mapping records (path + ancestors):
    - [subtype] Autophagy-Lysosome Pathway|Autophagy substrate selection|Selective autophagy receptor|Chaperone assisted selective autophagy|CASA complex component
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0035973 aggrephagy]
        rationale: The PN CASA subtype covers BAG3-HSPB8-HSP70-system machinery that directs damaged or aggregation-prone substrates into selective autophagic clearance. GO lacks a dedicated CASA term in the current cache, and this subtype includes chaperones and cofactors beyond pure cargo adaptors, so aggrephagy is the closest available process target.
    - [type] Autophagy-Lysosome Pathway|Autophagy substrate selection|Selective autophagy receptor|Chaperone assisted selective autophagy
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a contextual PN role. The label is useful for curator triage, but by itself does not support a universal GO assertion for all member genes beyond curated ancestor or child mappings.
    - [group] Autophagy-Lysosome Pathway|Autophagy substrate selection|Selective autophagy receptor
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN taxonomy container. The descendants mix components, regulators, context labels, and mechanistic leaves, so propagation should come only from narrower curated nodes.
    - [class] Autophagy-Lysosome Pathway|Autophagy substrate selection
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad substrate-selection container. GO has useful targets for specific receptor, cargo-adaptor, and selective-autophagy leaves, but this class mixes marking, recognition, receptor regulation, and unknown roles and should not propagate as one term.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## Projected GO annotations (3)
- GO:0044183 protein folding chaperone | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Cytonuclear proteostasis|Chaperone|small HSP system|small HSP
- GO:0044183 protein folding chaperone | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Mitochondrial proteostasis|Chaperone|small HSP
- GO:0035973 aggrephagy | scope=ok_for_propagation_to_go | goa_status=supported_by_goa_regulation | from=Autophagy-Lysosome Pathway|Autophagy substrate selection|Selective autophagy receptor|Chaperone assisted selective autophagy|CASA complex component

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
