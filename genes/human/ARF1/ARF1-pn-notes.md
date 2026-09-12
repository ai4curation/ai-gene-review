# ARF1 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: P84077
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-03 (PR 1364)
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/ARF1/ARF1-ai-review.yaml](ARF1-ai-review.yaml)
- AIGR review HTML: present - [genes/human/ARF1/ARF1-ai-review.html](ARF1-ai-review.html)
- Gene notes: present - [genes/human/ARF1/ARF1-notes.md](ARF1-notes.md)
- GOA TSV: present - [genes/human/ARF1/ARF1-goa.tsv](ARF1-goa.tsv)
- UniProt record: present - [genes/human/ARF1/ARF1-uniprot.txt](ARF1-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/ARF1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/ARF1.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ARF1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ARF1.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/ARF1/ARF1-deep-research-falcon.md](ARF1-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: ARF1 encodes ADP-ribosylation factor 1, a myristoylated class I ARF-family small GTPase that cycles between cytosolic GDP-bound and membrane-associated GTP-bound states. Active ARF1 acts mainly on Golgi and trans-Golgi network membranes, where it recruits and regulates coat/adaptor and lipid-transfer machinery for vesicle budding, coat disassembly, intra-Golgi traffic, Golgi-to-ER retrograde transport, TGN-to-endosomal/plasma-membrane routes, and glycosphingolipid export. Its major cellular role is regulation of membrane trafficking through the secretory and endomembrane systems rather than serving as a structural coat subunit.
- Existing/core annotation action counts: ACCEPT: 40; KEEP_AS_NON_CORE: 15; MARK_AS_OVER_ANNOTATED: 18; NEW: 1; REMOVE: 1

## PN Consistency Summary

- **Consistency:** Fully consistent across DR, notes, review YAML, and PN. The notes explicitly walk all three projected terms. No contradiction.
- **PN story / NEW pressure:** PN asserts retrograde Golgi-to-ER transport + COPI coat handling. Review ADDS GO:0006890 (verified real; `action: NEW`, TAS, Reactome:R-HSA-6811434) — defensible, matches PN type-node projection. GO:0015031 already captured (entailed via GO:0006886 IBA). **GO:0030126 COPI vesicle coat: PN subtype over-reaches** — ARF1 is a regulatory GTPase that recruits/releases coat, not a coatomer subunit; review correctly REJECTS adding it (mirrors the TOMM20/RAB7A "wrong-bucket" precedent — a CC membership term projected onto a regulator).
- **Evidence alignment:** PN row carried no PMIDs; review/notes anchor on PMID:8253837 (ARF GTP cycle), PMID:10102276 (ARF1-ARFGAP-coatomer), Reactome:R-HSA-6811434. Falcon DR added PMID:37914730 (cGAS-STING), 37400497 (FA/mito), 36269825 (AP-1:Arf1 coat) as statement-only, non-core. No divergence.
- **Verdict:** Consistent; GO:0006890 NEW is warranted and matches PN. PN GO:0030126 over-reaches for ARF1 (regulator vs coat subunit) and review correctly declines.

## Full Consistency Review

- **UniProt:** P84077 · **batch:** proteostasis-batch-2026-06-03 (Falcon DR 2026-06-07) · **review status:** COMPLETE
- **PN placement:** 1 row, ER. `ER proteostasis|Protein transport|ER-Golgi trafficking|Retrograde transport|COPI coating and uncoating`. **PN-node mapping:** subtype=`mapped`→GO:0030126 COPI vesicle coat (more_specific); type (Retrograde transport)=`mapped`→GO:0006890 retrograde Golgi-to-ER transport (more_specific); group (ER-Golgi trafficking)=`no_mapping`; class (Protein transport)=`mapped`→GO:0015031 (entailed_by_goa_closure); branch=`no_mapping`.
- **Consistency:** Fully consistent across DR, notes, review YAML, and PN. The notes explicitly walk all three projected terms. No contradiction.
- **PN story / NEW pressure:** PN asserts retrograde Golgi-to-ER transport + COPI coat handling. Review ADDS GO:0006890 (verified real; `action: NEW`, TAS, Reactome:R-HSA-6811434) — defensible, matches PN type-node projection. GO:0015031 already captured (entailed via GO:0006886 IBA). **GO:0030126 COPI vesicle coat: PN subtype over-reaches** — ARF1 is a regulatory GTPase that recruits/releases coat, not a coatomer subunit; review correctly REJECTS adding it (mirrors the TOMM20/RAB7A "wrong-bucket" precedent — a CC membership term projected onto a regulator).
- **Mapping strategy:** ARF1 does not change the node mapping. The retrograde-transport (GO:0006890) and protein-transport (GO:0015031) projections are right. The COPI-coat subtype (GO:0030126) is sound for coatomer members but should not project to ARF1; review files this as a suggested question (distinguish structural coatomer from regulatory GTPases).
- **Evidence alignment:** PN row carried no PMIDs; review/notes anchor on PMID:8253837 (ARF GTP cycle), PMID:10102276 (ARF1-ARFGAP-coatomer), Reactome:R-HSA-6811434. Falcon DR added PMID:37914730 (cGAS-STING), 37400497 (FA/mito), 36269825 (AP-1:Arf1 coat) as statement-only, non-core. No divergence.
- **Verdict:** Consistent; GO:0006890 NEW is warranted and matches PN. PN GO:0030126 over-reaches for ARF1 (regulator vs coat subunit) and review correctly declines.
- **Recommended edits:** none to ARF1-ai-review.yaml. [MAP] flag PN "COPI coating and uncoating" subtype to not project GO:0030126 (CC membership) to regulatory GTPases such as ARF1; restrict to coatomer subunits.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-03
- review_yaml: genes/human/ARF1/ARF1-ai-review.yaml
- PN workbook rows: 1

## PN row 1: ER proteostasis | Protein transport | ER-Golgi trafficking | Retrograde transport | COPI coating and uncoating
- UniProt: P84077
- In branches: ER
- PN-node mapping records (path + ancestors):
    - [subtype] ER proteostasis|Protein transport|ER-Golgi trafficking|Retrograde transport|COPI coating and uncoating
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0030126 COPI vesicle coat]
        rationale: This PN subtype is a COPI coat handling bucket in retrograde ER-Golgi transport. COPI vesicle coat is the appropriate shared cellular-component target.
    - [type] ER proteostasis|Protein transport|ER-Golgi trafficking|Retrograde transport
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0006890 retrograde vesicle-mediated transport, Golgi to endoplasmic reticulum]
        rationale: In `4.3.11`, the earlier retrograde-transport bucket has been folded into ER-Golgi trafficking and now specifically denotes COPI/KDEL-style retrograde trafficking from Golgi back to ER. The correct GO target is therefore retrograde vesicle-mediated transport, Golgi to endoplasmic reticulum rather than ER-to-cytosol retrotranslocation.
    - [group] ER proteostasis|Protein transport|ER-Golgi trafficking
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a single GO class. The member genes span multiple activities, complexes, or contexts, so direct propagation from this node would overstate the shared biology.
    - [class] ER proteostasis|Protein transport
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0015031 protein transport]
        rationale: The PN ER Protein transport class groups ER-targeting and ER-insertion pathways. GO protein transport is the appropriate propagation target, while the source class remains ER-specific and broader than any single GO transport subtype.
    - [branch] ER proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## Projected GO annotations (3)
- GO:0015031 protein transport | scope=ok_for_propagation_to_go | goa_status=entailed_by_goa_closure | from=ER proteostasis|Protein transport
- GO:0006890 retrograde vesicle-mediated transport, Golgi to endoplasmic reticulum | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=ER proteostasis|Protein transport|ER-Golgi trafficking|Retrograde transport
- GO:0030126 COPI vesicle coat | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=ER proteostasis|Protein transport|ER-Golgi trafficking|Retrograde transport|COPI coating and uncoating

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
