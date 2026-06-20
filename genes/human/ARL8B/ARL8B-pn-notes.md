# ARL8B PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9NVJ2
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-03 (PR 1369)
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/ARL8B/ARL8B-ai-review.yaml](ARL8B-ai-review.yaml)
- AIGR review HTML: present - [genes/human/ARL8B/ARL8B-ai-review.html](ARL8B-ai-review.html)
- Gene notes: present - [genes/human/ARL8B/ARL8B-notes.md](ARL8B-notes.md)
- GOA TSV: present - [genes/human/ARL8B/ARL8B-goa.tsv](ARL8B-goa.tsv)
- UniProt record: present - [genes/human/ARL8B/ARL8B-uniprot.txt](ARL8B-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/ARL8B.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/ARL8B.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ARL8B.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ARL8B.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/ARL8B/ARL8B-deep-research-falcon.md](ARL8B-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: ARL8B is a conserved Arf-like small GTPase that associates with lysosomal and endolysosomal membranes in its active GTP-bound state. Through effector interactions with BORC, PLEKHM2/SKIP-kinesin, PLEKHM1/HOPS, VPS41, and RUFY proteins, it coordinates lysosome positioning, endolysosomal cargo delivery, and lysosome fusion or exocytosis in contexts including autophagic cargo degradation, phagosome maturation, antigen presentation, cytolytic granule polarization, plasma membrane repair, and beta-coronavirus egress.
- Existing/core annotation action counts: ACCEPT: 39; KEEP_AS_NON_CORE: 27; MARK_AS_OVER_ANNOTATED: 12

## PN Consistency Summary

- **Consistency:** Consistent, with deliberate PN-vs-review divergence on GO:0061906. DR ↔ notes ↔ YAML agree: ARL8B is the better-characterized paralog — lysosomal small GTPase recruiting SKIP/PLEKHM2-kinesin (anterograde), HOPS/VPS41 (fusion), RUFY3/4 and DENND6A/Rab34/RILP (retrograde).
- **PN story / NEW pressure:** PN's projected term **GO:0061906 autophagosome localization (verified real, new_to_goa): review DECLINES** — ARL8B drives lysosome positioning and autophagosome-lysosome fusion/cargo delivery, not direct positioning of autophagosomes as cargo. The autophagy role IS already captured by the existing **GO:0061909 autophagosome-lysosome fusion (IMP, PMID:28325809) which the review ACCEPTs.** So the genuine autophagy story is already in GOA via fusion, and GO:0061906 over-reaches. Conclude: already-captured (fusion) + GO:0061906 not supported.
- **Evidence alignment:** PN cites the same three titles as ARL8A (Arl8 review; BORC; RUFY3/4=PMID:35314674). Review anchors PMID:16537643, 25898167 (BORC), 22172677 (SKIP/kinesin), 21802320 (VPS41/HOPS), 28325809 (PLEKHM1/fusion), 35314674 (RUFY3/4); DR added PMID:38296963 (DENND6A), 38128568 (BORCS8). **REF ISSUE flagged in review:** seeded GO:0007059 chromosome segregation cites PMID:14871887 (a Drosophila Topors paper, wrong gene) — review retains term as non-core (supported by GIE PMID:15331635) and flags the mismatch with a reference_review + suggested correction.
- **Verdict:** Consistent; PN GO:0061906 over-reaches; autophagy role already captured via GO:0061909 (ACCEPTed). REF mismatch (PMID:14871887) correctly flagged, not removed.

## Full Consistency Review

- **UniProt:** Q9NVJ2 · **batch:** proteostasis-batch-2026-06-03 (Falcon DR 2026-06-07) · **review status:** COMPLETE
- **PN placement:** 2 rows, ALP (identical structure to ARL8A). (1) `…Localization of the autophagosome|Movement of autophagosomes along microtubules|HOPS-BORC complex bridging`; (2) `…Autophagosome-lysosome docking|HOPS-BORC interaction mediator`. **PN-node mapping:** localization group + movement/bridging leaves=`mapped`→GO:0061906 autophagosome localization (new_to_goa); docking nodes=`context_only`→GO:0061909; class=`context_only`→GO:0016236.
- **Consistency:** Consistent, with deliberate PN-vs-review divergence on GO:0061906. DR ↔ notes ↔ YAML agree: ARL8B is the better-characterized paralog — lysosomal small GTPase recruiting SKIP/PLEKHM2-kinesin (anterograde), HOPS/VPS41 (fusion), RUFY3/4 and DENND6A/Rab34/RILP (retrograde).
- **PN story / NEW pressure:** PN's projected term **GO:0061906 autophagosome localization (verified real, new_to_goa): review DECLINES** — ARL8B drives lysosome positioning and autophagosome-lysosome fusion/cargo delivery, not direct positioning of autophagosomes as cargo. The autophagy role IS already captured by the existing **GO:0061909 autophagosome-lysosome fusion (IMP, PMID:28325809) which the review ACCEPTs.** So the genuine autophagy story is already in GOA via fusion, and GO:0061906 over-reaches. Conclude: already-captured (fusion) + GO:0061906 not supported.
- **Mapping strategy:** Same as ARL8A — mapping flagged `manual_gene_level_review_required`; gene-level review declines GO:0061906 projection. Right process family, wrong cargo organelle; shared target should remain lysosome localization (GO:0032418) / existing fusion term.
- **Evidence alignment:** PN cites the same three titles as ARL8A (Arl8 review; BORC; RUFY3/4=PMID:35314674). Review anchors PMID:16537643, 25898167 (BORC), 22172677 (SKIP/kinesin), 21802320 (VPS41/HOPS), 28325809 (PLEKHM1/fusion), 35314674 (RUFY3/4); DR added PMID:38296963 (DENND6A), 38128568 (BORCS8). **REF ISSUE flagged in review:** seeded GO:0007059 chromosome segregation cites PMID:14871887 (a Drosophila Topors paper, wrong gene) — review retains term as non-core (supported by GIE PMID:15331635) and flags the mismatch with a reference_review + suggested correction.
- **Verdict:** Consistent; PN GO:0061906 over-reaches; autophagy role already captured via GO:0061909 (ACCEPTed). REF mismatch (PMID:14871887) correctly flagged, not removed.
- **Recommended edits:** none to ARL8B-ai-review.yaml (it already flags both issues). [MAP] do not propagate GO:0061906 to ARL8B (autophagy role captured by GO:0061909). [REF] PN/curators: correct GO:0007059 origin reference PMID:14871887 → PMID:15331635 (GIE/ARL8 study).

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-03
- review_yaml: genes/human/ARL8B/ARL8B-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Autophagy-Lysosome Pathway | Autophagosome closure maturation and lysosome fusion | Localization of the autophagosome | Movement of autophagosomes along microtubules | HOPS-BORC complex bridging
- UniProt: Q9NVJ2
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
- UniProt: Q9NVJ2
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
