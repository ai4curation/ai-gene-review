# MAP3K20 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9NYL2
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07c
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/MAP3K20/MAP3K20-ai-review.yaml](MAP3K20-ai-review.yaml)
- AIGR review HTML: present - [genes/human/MAP3K20/MAP3K20-ai-review.html](MAP3K20-ai-review.html)
- Gene notes: present - [genes/human/MAP3K20/MAP3K20-notes.md](MAP3K20-notes.md)
- GOA TSV: present - [genes/human/MAP3K20/MAP3K20-goa.tsv](MAP3K20-goa.tsv)
- UniProt record: present - [genes/human/MAP3K20/MAP3K20-uniprot.txt](MAP3K20-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/MAP3K20.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/MAP3K20.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/MAP3K20.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/MAP3K20.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: MAP3K20 (ZAK; also MLK7/MRK) is a stress-activated mitogen-activated protein kinase kinase kinase (MAP3K) of the MLK family. As a serine/threonine protein kinase it phosphorylates the MAP2Ks MKK4/MKK7 (activating JNK) and MKK3/MKK6 (activating p38), driving stress-activated MAPK (JNK and p38) signaling that can promote programmed cell death. The principal isoform ZAKalpha is the proximal sensor of the ribotoxic stress response and directly binds the ribosome by inserting its flexible C-terminus into the intersubunit space (contacting helix 14 of 18S rRNA), acting as a sentinel for colliding ribosomes. Ribosome collisions trigger MAP3K20 autophosphorylation and activation; depending on collision severity it either activates the JNK/p38 cascade to promote cell death or activates EIF2AK4/GCN2 to engage the integrated stress response. ZAKalpha also drives the UV-B-induced NLRP1 inflammasome and pyroptosis by phosphorylating NLRP1. A shorter isoform, ZAKbeta, lacks the ribosome-binding C-terminus and does not sense collisions. MAP3K20 localizes mainly to the cytoplasm/cytosol (with reported nuclear pools and histone H3 Ser-28 kinase activity). It has additional reported roles in DNA-damage checkpoint signaling and cardiac stress responses. Biallelic variants cause split-foot malformation with mesoaxial polydactyly (SFMMP) and centronuclear myopathy 6 (CNM6).
- Existing/core annotation action counts: ACCEPT: 61; KEEP_AS_NON_CORE: 21; MARK_AS_OVER_ANNOTATED: 4

## PN Consistency Summary

- **Consistency:** Consistent. Deep research, review, and PN agree MAP3K20/ZAKalpha is the ribotoxic-stress-response kinase — the proximal sensor of ribosome collisions (binds ribosome / helix 14 of 18S rRNA, autophosphorylates) that routes signals to JNK/p38 (cell death) or GCN2 (ISR). PN deliberately places it in "other RQC processes" with type=no_mapping (sensor/signaling, not a core ubiquitination/rescue effector), which matches the review framing exactly. No contradiction.
- **PN story / NEW pressure:** Subtle. PN maps only the GROUP node GO:0006515 (protein quality control) — broad. MAP3K20 is a ribotoxic-stress SENSOR/SIGNALING kinase, not a protein-QC catabolic effector, so GO:0006515 over-attributes a QC-disposal process to it. The review's rich, accurate captures are GO:0043022 ribosome binding (IDA), GO:0070181 small ribosomal subunit rRNA binding (IDA), GO:0051403 stress-activated MAPK cascade, GO:0140469 GCN2-mediated signaling, GO:0070269 pyroptosis. There is no missing term — the ribotoxic-stress/collision-sensing role is well annotated. Conclusion: **already captured**; PN group GO:0006515 over-reaches for a sensor kinase.
- **Evidence alignment:** PN lists no reference titles. Review anchors on PMID:32289254 (ZAKalpha sensor domains / 18S helix-14), PMID:32610081 (collisions → cell fate, p38/JNK vs GCN2), PMID:35857590 (NLRP1 inflammasome/pyroptosis), plus the classical MRK/ZAK kinase papers. No citation conflict; PN carries no PMIDs.
- **Verdict:** Consistent; ribotoxic-stress sensor role already well captured — PN group GO:0006515 over-reaches for a signaling kinase. **Recommended edits:** treat group-node GO:0006515 as context-only for MAP3K20 (do not propagate the protein-QC catabolic process to a sensor/signaling kinase) [MAP]; no YAML changes needed.

## Full Consistency Review

- **UniProt:** Q9NYL2 (ZAK/MLK7/MRK) · **batch:** proteostasis-batch-2026-06-07c · **review status:** COMPLETE
- **PN placement:** `Translation|Cytosolic translation|Ribosome-associated QC|other RQC processes` ; **PN-node mapping:** type `other RQC processes`=no_mapping; group `Ribosome-associated QC`=mapped→GO:0006515 protein quality control (new_to_goa); class/branch=context_only.
- **Consistency:** Consistent. Deep research, review, and PN agree MAP3K20/ZAKalpha is the ribotoxic-stress-response kinase — the proximal sensor of ribosome collisions (binds ribosome / helix 14 of 18S rRNA, autophosphorylates) that routes signals to JNK/p38 (cell death) or GCN2 (ISR). PN deliberately places it in "other RQC processes" with type=no_mapping (sensor/signaling, not a core ubiquitination/rescue effector), which matches the review framing exactly. No contradiction.
- **PN story / NEW pressure:** Subtle. PN maps only the GROUP node GO:0006515 (protein quality control) — broad. MAP3K20 is a ribotoxic-stress SENSOR/SIGNALING kinase, not a protein-QC catabolic effector, so GO:0006515 over-attributes a QC-disposal process to it. The review's rich, accurate captures are GO:0043022 ribosome binding (IDA), GO:0070181 small ribosomal subunit rRNA binding (IDA), GO:0051403 stress-activated MAPK cascade, GO:0140469 GCN2-mediated signaling, GO:0070269 pyroptosis. There is no missing term — the ribotoxic-stress/collision-sensing role is well annotated. Conclusion: **already captured**; PN group GO:0006515 over-reaches for a sensor kinase.
- **Mapping strategy:** Correct that the type node ("other RQC processes") is no_mapping. The group-level GO:0006515 should be treated as context_only for MAP3K20 — it is a heterogeneous QC umbrella and MAP3K20's role is upstream sensing/signaling, not nascent-chain disposal. Distinguishing broad GO:0006515 from MAP3K20's specific ribosome-binding/stress-cascade terms is exactly the branch-guidance concern.
- **Evidence alignment:** PN lists no reference titles. Review anchors on PMID:32289254 (ZAKalpha sensor domains / 18S helix-14), PMID:32610081 (collisions → cell fate, p38/JNK vs GCN2), PMID:35857590 (NLRP1 inflammasome/pyroptosis), plus the classical MRK/ZAK kinase papers. No citation conflict; PN carries no PMIDs.
- **Verdict:** Consistent; ribotoxic-stress sensor role already well captured — PN group GO:0006515 over-reaches for a signaling kinase. **Recommended edits:** treat group-node GO:0006515 as context-only for MAP3K20 (do not propagate the protein-QC catabolic process to a sensor/signaling kinase) [MAP]; no YAML changes needed.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07c
- review_yaml: genes/human/MAP3K20/MAP3K20-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Translation | Cytosolic translation | Ribosome-associated QC | other RQC processes
- UniProt: Q9NYL2
- In branches: TR
- PN-node mapping records (path + ancestors):
    - [type] Translation|Cytosolic translation|Ribosome-associated QC|other RQC processes
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a single GO class. The member genes span multiple activities, complexes, or contexts, so direct propagation from this node would overstate the shared biology.
    - [group] Translation|Cytosolic translation|Ribosome-associated QC
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0006515 protein quality control for misfolded or incompletely synthesized proteins]
        rationale: The PN ribosome-associated quality-control group covers surveillance and disposal of stalled or defective nascent-chain translation products. GO lacks a dedicated ribosome-associated QC term in the local cache, so the broader protein-quality-control process is the best supported target.
    - [class] Translation|Cytosolic translation
        status=context_only scope=too_broad_to_propagate GO=[GO:0002181 cytoplasmic translation]
        rationale: The PN class Cytosolic translation is centered on the cytoplasmic translation apparatus and process, but it also houses supporting machinery such as ribosome biogenesis factors. The GO process term is a useful high-level label for the class, but propagating it to all members would over-annotate genes whose PN placement is through assembly or maturation context rather than core cytoplasmic translation.
    - [branch] Translation
        status=context_only scope=too_broad_to_propagate GO=[GO:0006412 translation]
        rationale: The PN Translation branch is organized around the translation apparatus and immediately associated cotranslational quality-control systems. GO translation is the closest high-level process label, but the PN branch also contains adjacent machinery such as ribosome biogenesis and nascent-chain handling. Keeping this relationship is useful for interpretation, but it is too broad to project safely onto every member.

## Projected GO annotations (1)
- GO:0006515 protein quality control for misfolded or incompletely synthesized proteins | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Translation|Cytosolic translation|Ribosome-associated QC

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
