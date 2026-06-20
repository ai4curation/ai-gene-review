# UBAC2 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q8NBM4
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-11
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/UBAC2/UBAC2-ai-review.yaml](UBAC2-ai-review.yaml)
- AIGR review HTML: missing - genes/human/UBAC2/UBAC2-ai-review.html
- Gene notes: present - [genes/human/UBAC2/UBAC2-notes.md](UBAC2-notes.md)
- GOA TSV: present - [genes/human/UBAC2/UBAC2-goa.tsv](UBAC2-goa.tsv)
- UniProt record: present - [genes/human/UBAC2/UBAC2-uniprot.txt](UBAC2-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/UBAC2.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/UBAC2.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/UBAC2.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/UBAC2.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/UBAC2/UBAC2-deep-research-falcon.md](UBAC2-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: UBAC2 (ubiquitin-associated domain-containing protein 2, also PHGDHL1) is a multi-pass endoplasmic reticulum (ER) membrane protein of the rhomboid superfamily. Its N-terminal region adopts a rhomboid-like fold but is a catalytically inactive pseudoprotease (it lacks the conserved serine-protease catalytic dyad), and its C-terminal cytoplasmic UBA domain binds ubiquitin. UBAC2 acts as an ER-membrane scaffolding/adaptor component rather than an enzyme. It partners the active rhomboid protease RHBDD1 in the ER-associated degradation (ERAD) of membrane substrates, where its UBA domain engages ubiquitinated clients. UBAC2 is also the ER receptor that binds FAF2/UBXD8 and restricts FAF2 trafficking from the ER to lipid droplets, thereby modulating ER-to-cytosol dislocation and lipid-droplet partitioning. Independently, UBAC2 serves as a selective autophagy (ER-phagy/reticulophagy) receptor; a LIR motif in its cytoplasmic domain binds the autophagosomal protein GABARAP, and MARK2-mediated phosphorylation at Ser223 promotes UBAC2 dimerization and GABARAP binding to drive ER-phagy, which in turn restrains ER-stress-induced inflammatory responses. In a complex with LMBR1L and the E3 ubiquitin ligase AMFR, UBAC2 also negatively regulates canonical Wnt/beta-catenin signaling in lymphocytes by promoting degradation of CTNNB1 and the Wnt receptors FZD6 and LRP6.
- Existing/core annotation action counts: ACCEPT: 8; KEEP_AS_NON_CORE: 6; REMOVE: 1

## PN Consistency Summary

- **Consistency:** Excellent. Deep research, review and PN concur that UBAC2 is a **catalytically inactive rhomboid pseudoprotease** (no Ser/His dyad), an ER-membrane scaffold/adaptor — NOT an enzyme. The PN explicitly tags the LMBR1L-GP78-UBAC2 subtype as "noncatalytic / UBA, transmembrane" and assigns the COMPLEX (GO:0000151), not catalytic activity, to the group — exactly matching the review's REMOVE of the IBA serine-type endopeptidase activity (GO:0004252). The PN correctly does NOT project GO:0061630 to UBAC2. No contradictions.
- **PN story / NEW pressure:** PN's only NEW projection is GO:0000151 ubiquitin ligase complex (verified real; NOT in GOA) from the LMBR1L-GP78(AMFR)-UBAC2 idiosyncratic-RING-complex membership (PMID:31073040). UBAC2 is genuinely a non-catalytic subunit of this AMFR/GP78-containing E3 complex, so complex membership is a DEFENSIBLE ADD — and one the review does NOT currently capture (review has the Wnt BP via this complex but no GO:0000151 CC term). Conclude: pseudoprotease/scaffold correctly captured; GO:0000151 a defensible NEW the review missed.
- **Evidence alignment:** Partial. PN complex row cites "31073040" (LMBR1L/Wnt paper) — IS in the review (HIGH/VERIFIED, source of the Wnt + LMBR1L annotations). The ERphagy row carries no PN reference title; the review's ER-phagy evidence (PMID:39284914, HIGH) is gene-specific and richer. Good overlap on the one cited PMID; no divergence.
- **Verdict:** Fully consistent; pseudoprotease status and scaffold role correctly handled by BOTH review (REMOVE GO:0004252) and PN (noncatalytic tag, no GO:0061630). GO:0000151 complex membership is a defensible ADD the review omits.

## Full Consistency Review

- **UniProt:** Q8NBM4 · **batch:** proteostasis-batch-2026-06-11 · **review status:** COMPLETE (thorough; rhomboid PSEUDOprotease, ERAD scaffold + FAF2 ER receptor + ER-phagy receptor + Wnt)
- **PN placement:** 2 rows — `UPS|E3 ubiquitin and UBL ligases|idiosyncratic RING complex|LMBR1L-GP78-UBAC2 complex|noncatalytic / UBA, transmembrane`; `UPS|Ubiquitin and UBL binding|trafficking|ERphagy|UBA`. **PN-node mapping:** LMBR1L-GP78-UBAC2 subtype/type no_mapping (noncatalytic, covered by parent); idiosyncratic-RING-complex group→GO:0000151 ubiquitin ligase complex (new_to_goa); E3-ligase class context_only GO:0061630 (too_broad); ERphagy/UBA-binding rows all no_mapping/context_only (GO:0140036 too_broad). Projected: GO:0000151 (new).
- **Consistency:** Excellent. Deep research, review and PN concur that UBAC2 is a **catalytically inactive rhomboid pseudoprotease** (no Ser/His dyad), an ER-membrane scaffold/adaptor — NOT an enzyme. The PN explicitly tags the LMBR1L-GP78-UBAC2 subtype as "noncatalytic / UBA, transmembrane" and assigns the COMPLEX (GO:0000151), not catalytic activity, to the group — exactly matching the review's REMOVE of the IBA serine-type endopeptidase activity (GO:0004252). The PN correctly does NOT project GO:0061630 to UBAC2. No contradictions.
- **PN story / NEW pressure:** PN's only NEW projection is GO:0000151 ubiquitin ligase complex (verified real; NOT in GOA) from the LMBR1L-GP78(AMFR)-UBAC2 idiosyncratic-RING-complex membership (PMID:31073040). UBAC2 is genuinely a non-catalytic subunit of this AMFR/GP78-containing E3 complex, so complex membership is a DEFENSIBLE ADD — and one the review does NOT currently capture (review has the Wnt BP via this complex but no GO:0000151 CC term). Conclude: pseudoprotease/scaffold correctly captured; GO:0000151 a defensible NEW the review missed.
- **Mapping strategy:** Exemplary. Resolves the pseudoprotease trap (no serine endopeptidase MF — matches prior REMOVE precedent), assigns complex membership not catalysis to the non-catalytic subunit, and conservatively leaves the ERphagy/UBA-binding rows unmapped (avoids over-broad GO:0140036 reader propagation). The ER-phagy biology IS captured at the gene level (review GO:0061709 reticulophagy IMP). No node-status change warranted.
- **Evidence alignment:** Partial. PN complex row cites "31073040" (LMBR1L/Wnt paper) — IS in the review (HIGH/VERIFIED, source of the Wnt + LMBR1L annotations). The ERphagy row carries no PN reference title; the review's ER-phagy evidence (PMID:39284914, HIGH) is gene-specific and richer. Good overlap on the one cited PMID; no divergence.
- **Verdict:** Fully consistent; pseudoprotease status and scaffold role correctly handled by BOTH review (REMOVE GO:0004252) and PN (noncatalytic tag, no GO:0061630). GO:0000151 complex membership is a defensible ADD the review omits.
- **Recommended edits:** [YAML] add GO:0000151 ubiquitin ligase complex (part_of; LMBR1L-AMFR/GP78-UBAC2 complex, PMID:31073040) as a non-core CC — currently absent from the review. [MAP] none — node mapping is correct; complex (not catalytic) target for the non-catalytic subunit is the right call.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-11
- review_yaml: genes/human/UBAC2/UBAC2-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Ubiquitin Proteasome System | E3 ubiquitin and UBL ligases | idiosyncratic RING complex | LMBR1L-GP78-UBAC2 complex | noncatalytic / UBA, transmembrane
- UniProt: Q8NBM4
- In branches: UPS
- Signature domains: (none)
- Auxiliary domains: IPR015940
- PN references (titles):
    - 31073040
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|idiosyncratic RING complex|LMBR1L-GP78-UBAC2 complex|noncatalytic / UBA, transmembrane
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower E3-ligase architecture, component, or domain subdivision already covered by the curated parent E3 mapping. No additional direct GO mapping is needed at this node.
    - [type] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|idiosyncratic RING complex|LMBR1L-GP78-UBAC2 complex
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower E3-ligase architecture, component, or domain subdivision already covered by the curated parent E3 mapping. No additional direct GO mapping is needed at this node.
    - [group] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|idiosyncratic RING complex
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0000151 ubiquitin ligase complex]
        rationale: This PN group is an E3 ligase complex bucket. The safest shared GO target is ubiquitin ligase complex membership rather than assigning catalytic activity to every subunit.
    - [class] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases
        status=context_only scope=too_broad_to_propagate GO=[GO:0061630 ubiquitin protein ligase activity]
        rationale: This class is a genuine E3-ligase context, but its descendants include catalytic ligases, cullin scaffolds, substrate receptors, adaptors, cofactors, regulators, and UBL modifier systems. A class-level propagation would over-annotate.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## PN row 2: Ubiquitin Proteasome System | Ubiquitin and UBL binding | trafficking | ERphagy | UBA
- UniProt: Q8NBM4
- In branches: UPS
- Signature domains: IPR015940
- Auxiliary domains: (none)
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|Ubiquitin and UBL binding|trafficking|ERphagy|UBA
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a selective-autophagy or trafficking subdivision under a UPS binding context. The autophagy context is real, but this node is too indirect for automatic GO propagation.
    - [type] Ubiquitin Proteasome System|Ubiquitin and UBL binding|trafficking|ERphagy
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a UPS taxonomy container. Its descendants mix catalytic roles, complex membership, binding domains, regulators, adaptors, and substrate-context labels, so a single propagating GO assertion would overstate the shared biology.
    - [group] Ubiquitin Proteasome System|Ubiquitin and UBL binding|trafficking
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a UPS taxonomy container. Its descendants mix catalytic roles, complex membership, binding domains, regulators, adaptors, and substrate-context labels, so a single propagating GO assertion would overstate the shared biology.
    - [class] Ubiquitin Proteasome System|Ubiquitin and UBL binding
        status=context_only scope=too_broad_to_propagate GO=[GO:0140036 ubiquitin-modified protein reader activity]
        rationale: This class records ubiquitin/UBL-reader context, but the subtree mixes ubiquitin, SUMO, UBL-domain, domain-architecture, catalytic, signaling, trafficking, and nucleic-acid process buckets. It is useful context, not a safe direct propagation.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## Projected GO annotations (1)
- GO:0000151 ubiquitin ligase complex | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|idiosyncratic RING complex

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
