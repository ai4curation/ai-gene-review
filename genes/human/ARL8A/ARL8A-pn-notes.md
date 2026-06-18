# ARL8A PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q96BM9
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-03 (PR 1368)
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/ARL8A/ARL8A-ai-review.yaml](ARL8A-ai-review.yaml)
- AIGR review HTML: present - [genes/human/ARL8A/ARL8A-ai-review.html](ARL8A-ai-review.html)
- Gene notes: present - [genes/human/ARL8A/ARL8A-notes.md](ARL8A-notes.md)
- GOA TSV: present - [genes/human/ARL8A/ARL8A-goa.tsv](ARL8A-goa.tsv)
- UniProt record: present - [genes/human/ARL8A/ARL8A-uniprot.txt](ARL8A-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/ARL8A.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/ARL8A.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ARL8A.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ARL8A.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/ARL8A/ARL8A-deep-research-falcon.md](ARL8A-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: ARL8A encodes ADP-ribosylation factor-like protein 8A, an ARF-family small GTPase that associates with lysosomal and late-endosomal membranes in its active GTP-bound state. Together with ARL8B, it organizes endolysosome positioning and microtubule-based motility by engaging BORC-dependent recruitment and effectors such as SKIP/PLEKHM2, PLEKHM1/HOPS, and RUFY3/RUFY4. These interactions support peripheral and juxtanuclear redistribution of lysosomes/endolysosomes, cargo delivery to lysosomes, and specialized neuronal axonal transport of lysosome-related vesicles. ARL8A also has reported tubulin/spindle-midzone associations and chromosome-segregation phenotypes from early GIE studies, but those mitotic observations are secondary to its endolysosomal transport role.
- Existing/core annotation action counts: ACCEPT: 10; KEEP_AS_NON_CORE: 15; MARK_AS_OVER_ANNOTATED: 1; MODIFY: 1; REMOVE: 12

## PN Consistency Summary

- **Consistency:** Consistent, with a deliberate PN-vs-review divergence (below). DR ↔ notes ↔ YAML agree: ARL8A is a lysosomal/endolysosomal small GTPase for lysosome positioning and BORC-kinesin/dynein-coupled transport; most ARL8A-specific conclusions are paralog-inferred from ARL8B but direct ARL8A contribution shown by ARL8B-KO + ARL8A-siRNA (PMID:27851960).
- **PN story / NEW pressure:** PN's projected term **GO:0061906 autophagosome localization (verified real, new_to_goa): review DECLINES.** Evidence supports lysosome/endolysosome positioning and HOPS-mediated cargo delivery, not direct ARL8A-dependent positioning of autophagosomes as the transported organelle. Over-reaches as written. Review instead anchors on GO:0032418 lysosome localization. Conclude: GO:0061906 not yet supported for ARL8A; recorded as suggested question/experiment.
- **Evidence alignment:** PN cites tandfonline/NatComms titles (Arl8 review; BORC; RUFY3/4 = PMID:35314674). Review/notes anchor on PMID:16537643 (ARL8a/b lysosome localization), 25898167 (BORC), 28325809 (PLEKHM1), 35314674 (RUFY3/4). DR added PMID:27851960, 35653304 (cholesterol egress), 37213076 (exosomes, ARL8A/B dKO), 38296963 (DENND6A), 38128568 (BORCS8 disease) statement-only. Strong overlap (RUFY3/4); review broader.
- **Verdict:** Consistent; PN GO:0061906 over-reaches for ARL8A (lysosome vs autophagosome positioning); review correctly declines and uses GO:0032418.

## Full Consistency Review

- **UniProt:** Q96BM9 · **batch:** proteostasis-batch-2026-06-03 (Falcon DR 2026-06-07) · **review status:** COMPLETE
- **PN placement:** 2 rows, ALP. (1) `…Localization of the autophagosome|Movement of autophagosomes along microtubules|HOPS-BORC complex bridging`; (2) `…Autophagosome-lysosome docking|HOPS-BORC interaction mediator`. **PN-node mapping:** localization group + movement/bridging leaves=`mapped`→GO:0061906 autophagosome localization (new_to_goa); docking nodes=`context_only`→GO:0061909; class=`context_only`→GO:0016236.
- **Consistency:** Consistent, with a deliberate PN-vs-review divergence (below). DR ↔ notes ↔ YAML agree: ARL8A is a lysosomal/endolysosomal small GTPase for lysosome positioning and BORC-kinesin/dynein-coupled transport; most ARL8A-specific conclusions are paralog-inferred from ARL8B but direct ARL8A contribution shown by ARL8B-KO + ARL8A-siRNA (PMID:27851960).
- **PN story / NEW pressure:** PN's projected term **GO:0061906 autophagosome localization (verified real, new_to_goa): review DECLINES.** Evidence supports lysosome/endolysosome positioning and HOPS-mediated cargo delivery, not direct ARL8A-dependent positioning of autophagosomes as the transported organelle. Over-reaches as written. Review instead anchors on GO:0032418 lysosome localization. Conclude: GO:0061906 not yet supported for ARL8A; recorded as suggested question/experiment.
- **Mapping strategy:** Mapping flagged `manual_gene_level_review_required`; gene-level review here declines projection to ARL8A. The "autophagosome localization" leaf conflates lysosome positioning with autophagosome positioning — for ARL8A the safe shared target is lysosome localization, not autophagosome localization (PN term is narrower-but-mis-targeted: right process family, wrong cargo organelle).
- **Evidence alignment:** PN cites tandfonline/NatComms titles (Arl8 review; BORC; RUFY3/4 = PMID:35314674). Review/notes anchor on PMID:16537643 (ARL8a/b lysosome localization), 25898167 (BORC), 28325809 (PLEKHM1), 35314674 (RUFY3/4). DR added PMID:27851960, 35653304 (cholesterol egress), 37213076 (exosomes, ARL8A/B dKO), 38296963 (DENND6A), 38128568 (BORCS8 disease) statement-only. Strong overlap (RUFY3/4); review broader.
- **Verdict:** Consistent; PN GO:0061906 over-reaches for ARL8A (lysosome vs autophagosome positioning); review correctly declines and uses GO:0032418.
- **Recommended edits:** none to ARL8A-ai-review.yaml. [MAP] do not propagate GO:0061906 to ARL8A from the autophagosome-localization leaf until direct ARL8A-dependent autophagosome positioning is shown; ARL8A's shared target is lysosome localization.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-03
- review_yaml: genes/human/ARL8A/ARL8A-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Autophagy-Lysosome Pathway | Autophagosome closure maturation and lysosome fusion | Localization of the autophagosome | Movement of autophagosomes along microtubules | HOPS-BORC complex bridging
- UniProt: Q96BM9
- In branches: ALP
- Notes: Small GTPase that regulates lysosome positioning and bridges the HOPS and BORC complexes for autophagosome-lysosome fusion. Also serves as a link to the dynein-dynactin system for vesicles.
- PN references (titles):
    - Arf-like GTPase Arl8: Moving from the periphery to the center of lysosomal biology (tandfonline.com)
    - Full article: BORC coordinates encounter and fusion of lysosomes with autophagosomes (tandfonline.com)
    - RUFY3 and RUFY4 are ARL8 effectors that promote coupling of endolysosomes to dynein-dynactin | Nature Communications
- PN-node mapping records (path + ancestors):
    - [subtype] Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion|Localization of the autophagosome|Movement of autophagosomes along microtubules|HOPS-BORC complex bridging
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0061906 autophagosome localization]
        rationale: This PN subtype denotes the bridging machinery that links HOPS/BORC-like late-endolysosomal transport systems to autophagosome positioning on microtubules. The best current GO target is autophagosome localization.
    - [type] Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion|Localization of the autophagosome|Movement of autophagosomes along microtubules
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0061906 autophagosome localization]
        rationale: This leaf describes a mechanism for positioning autophagosomes. The safe shared GO target is autophagosome localization, not the downstream fusion process.
    - [group] Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion|Localization of the autophagosome
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0061906 autophagosome localization]
        rationale: This group is explicitly about positioning/autophagosome localization in late autophagy. Autophagosome localization is the correct propagation target rather than autophagosome-lysosome fusion.
    - [class] Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion
        status=context_only scope=too_broad_to_propagate GO=[GO:0016236 macroautophagy]
        rationale: This class is a late macroautophagy context, but the subtree mixes docking, fusion, localization, membrane-composition, and unknown late-stage roles. The class-level relation is useful for display while propagation is restricted to narrower mechanism nodes.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## PN row 2: Autophagy-Lysosome Pathway | Autophagosome closure maturation and lysosome fusion | Autophagosome-lysosome docking | HOPS-BORC interaction mediator
- UniProt: Q96BM9
- In branches: ALP
- Notes: Small GTPase that regulates lysosome positioning and bridges the HOPS and BORC complexes for autophagosome-lysosome fusion. Also serves as a link to the dynein-dynactin system for vesicles.
- PN references (titles):
    - Arf-like GTPase Arl8: Moving from the periphery to the center of lysosomal biology (tandfonline.com)
    - Full article: BORC coordinates encounter and fusion of lysosomes with autophagosomes (tandfonline.com)
    - RUFY3 and RUFY4 are ARL8 effectors that promote coupling of endolysosomes to dynein-dynactin | Nature Communications
- PN-node mapping records (path + ancestors):
    - [type] Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion|Autophagosome-lysosome docking|HOPS-BORC interaction mediator
        status=context_only scope=too_broad_to_propagate GO=[GO:0061909 autophagosome-lysosome fusion]
        rationale: Reviewed as an interaction-mediator bucket in autophagosome-lysosome docking. The relation to fusion is contextual and should not project generic fusion to all members.
    - [group] Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion|Autophagosome-lysosome docking
        status=context_only scope=too_broad_to_propagate GO=[GO:0061909 autophagosome-lysosome fusion]
        rationale: Reviewed as an autophagosome-lysosome docking context. The subtree mixes component buckets and modulators, so generic fusion propagation should come only from narrower reviewed mechanism leaves.
    - [class] Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion
        status=context_only scope=too_broad_to_propagate GO=[GO:0016236 macroautophagy]
        rationale: This class is a late macroautophagy context, but the subtree mixes docking, fusion, localization, membrane-composition, and unknown late-stage roles. The class-level relation is useful for display while propagation is restricted to narrower mechanism nodes.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## Projected GO annotations (3)
- GO:0061906 autophagosome localization | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion|Localization of the autophagosome
- GO:0061906 autophagosome localization | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion|Localization of the autophagosome|Movement of autophagosomes along microtubules
- GO:0061906 autophagosome localization | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion|Localization of the autophagosome|Movement of autophagosomes along microtubules|HOPS-BORC complex bridging

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
