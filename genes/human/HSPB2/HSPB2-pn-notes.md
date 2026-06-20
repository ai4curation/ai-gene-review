# HSPB2 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q16082
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07b
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/HSPB2/HSPB2-ai-review.yaml](HSPB2-ai-review.yaml)
- AIGR review HTML: present - [genes/human/HSPB2/HSPB2-ai-review.html](HSPB2-ai-review.html)
- Gene notes: present - [genes/human/HSPB2/HSPB2-notes.md](HSPB2-notes.md)
- GOA TSV: present - [genes/human/HSPB2/HSPB2-goa.tsv](HSPB2-goa.tsv)
- UniProt record: present - [genes/human/HSPB2/HSPB2-uniprot.txt](HSPB2-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/HSPB2.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/HSPB2.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/HSPB2.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/HSPB2.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: HSPB2 (heat shock protein beta-2; also MKBP, "DMPK-binding protein") is an ATP-independent small heat-shock protein (sHSP) of the alpha-crystallin/HSP20 family, expressed preferentially in skeletal and cardiac muscle. Like other sHSPs it acts as a holdase chaperone, binding non-native/destabilized client proteins through its alpha-crystallin domain to prevent their aggregation under stress, holding them for downstream ATP-dependent refolding. HSPB2 forms its own oligomeric complex in muscle cytosol, distinct from the alphaB-crystallin (CRYAB)/HSP27 complex, and is notable for binding and activating the myotonic dystrophy protein kinase (DMPK), enhancing its kinase activity and protecting it from heat-induced inactivation. It localizes to the cytoplasm (Z-membrane of myofibrils and the neuromuscular junction) and to nuclear foci. HSPB2 is not strongly heat-inducible but participates in the muscle stress response and is cardioprotective during ischemia, helping maintain ATP levels.
- Existing/core annotation action counts: ACCEPT: 9; KEEP_AS_NON_CORE: 8; MODIFY: 3; REMOVE: 1

## PN Consistency Summary

- **Consistency:** Largely consistent. Deep research, notes, and review YAML agree HSPB2 is an ATP-independent small HSP (alpha-crystallin/HSP20) holdase (core MF GO:0051082 unfolded protein binding; validated client GAPDH, PMID:26465331) and a DMPK kinase activator (core MF GO:0008047, PMID:9490724). PN "small HSP" placement matches. The CY+MI dual branch fits HSPB2's cytosolic muscle oligomers plus a cardiac mitochondrial-leaning interactome (PMID:26465331). No contradiction; note review REMOVES GO:0005212 (eye-lens crystallin) as an erroneous family transfer — a good catch the PN small-HSP node does not propagate.
- **PN story / NEW pressure:** PN asserts GO:0044183 protein folding chaperone (verified real). GOA lacks GO:0044183 (new_to_goa correct). GO:0044183 sits on the chaperone-ACTIVITY branch, sibling to the review's GO:0051082 (on the binding branch) — neither is ancestor of the other; both are defensible for a sHSP holdase. GO:0044183 is broader/coarser than the review's holdase-specific framing but not wrong. Reasonable ADD; not over-reaching for a bona fide sHSP.
- **Evidence alignment:** PN rows no titles; review anchors on PMID:9490724 (MKBP/DMPK, TAS) and PMID:26465331 (cardiac interactome/GAPDH client) — both VERIFIED. No conflict.
- **Verdict:** Consistent. GO:0044183 is a defensible new_to_goa ADD (broader sibling of review's GO:0051082, both valid for a sHSP holdase). DMPK-activator and lens-removal are gene-specific calls outside the PN family mapping.

## Full Consistency Review

- **UniProt:** Q16082 (MKBP) · **batch:** proteostasis-batch-2026-06-07b · **review status:** COMPLETE
- **PN placement:** two rows — `Cytonuclear proteostasis|Chaperone|small HSP system|small HSP` (type=mapped) and `Mitochondrial proteostasis|Chaperone|small HSP` (group=mapped); **PN-node mapping:** both → GO:0044183 protein folding chaperone, scope=ok_for_propagation_to_go, projected new_to_goa; class/branch=no_mapping.
- **Consistency:** Largely consistent. Deep research, notes, and review YAML agree HSPB2 is an ATP-independent small HSP (alpha-crystallin/HSP20) holdase (core MF GO:0051082 unfolded protein binding; validated client GAPDH, PMID:26465331) and a DMPK kinase activator (core MF GO:0008047, PMID:9490724). PN "small HSP" placement matches. The CY+MI dual branch fits HSPB2's cytosolic muscle oligomers plus a cardiac mitochondrial-leaning interactome (PMID:26465331). No contradiction; note review REMOVES GO:0005212 (eye-lens crystallin) as an erroneous family transfer — a good catch the PN small-HSP node does not propagate.
- **PN story / NEW pressure:** PN asserts GO:0044183 protein folding chaperone (verified real). GOA lacks GO:0044183 (new_to_goa correct). GO:0044183 sits on the chaperone-ACTIVITY branch, sibling to the review's GO:0051082 (on the binding branch) — neither is ancestor of the other; both are defensible for a sHSP holdase. GO:0044183 is broader/coarser than the review's holdase-specific framing but not wrong. Reasonable ADD; not over-reaching for a bona fide sHSP.
- **Mapping strategy:** Node status unchanged. Projection accurate (term absent from GOA). GO:0044183 is appropriately generic for the "small HSP" type; the review's GO:0051082 + holdase (GO:0140309 territory) is the more precise gene-level call. Minor altitude divergence only.
- **Evidence alignment:** PN rows no titles; review anchors on PMID:9490724 (MKBP/DMPK, TAS) and PMID:26465331 (cardiac interactome/GAPDH client) — both VERIFIED. No conflict.
- **Verdict:** Consistent. GO:0044183 is a defensible new_to_goa ADD (broader sibling of review's GO:0051082, both valid for a sHSP holdase). DMPK-activator and lens-removal are gene-specific calls outside the PN family mapping.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07b
- review_yaml: genes/human/HSPB2/HSPB2-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Cytonuclear proteostasis | Chaperone | small HSP system | small HSP
- UniProt: Q16082
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
- UniProt: Q16082
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
