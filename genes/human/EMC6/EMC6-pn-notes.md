# EMC6 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9BV81
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-11
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/EMC6/EMC6-ai-review.yaml](EMC6-ai-review.yaml)
- AIGR review HTML: missing - genes/human/EMC6/EMC6-ai-review.html
- Gene notes: present - [genes/human/EMC6/EMC6-notes.md](EMC6-notes.md)
- GOA TSV: present - [genes/human/EMC6/EMC6-goa.tsv](EMC6-goa.tsv)
- UniProt record: present - [genes/human/EMC6/EMC6-uniprot.txt](EMC6-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/EMC6.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/EMC6.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/EMC6.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/EMC6.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/EMC6/EMC6-deep-research-falcon.md](EMC6-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: EMC6 (ER membrane protein complex subunit 6; also TMEM93) is a small (110 aa) polytopic ER membrane protein with three transmembrane helices and an N-cytoplasmic/C-lumenal topology. It is a constitutive subunit of the ER membrane protein complex (EMC), a conserved ~9-subunit transmembrane-domain insertase and membrane-protein chaperone of the endoplasmic reticulum. Within the complex, EMC6 packs against the catalytic insertase subunit EMC3 (a member of the YidC/Oxa1/Get1 insertase superfamily) to form the hydrophilic membrane vestibule through which substrate transmembrane domains are inserted. The EMC enables the energy-independent insertion of newly synthesized membrane proteins into the ER membrane, with a preference for transmembrane domains that are weakly hydrophobic or contain destabilizing charged or aromatic residues. It mediates post-translational insertion of tail-anchored proteins and cotranslational insertion and topogenesis of multipass membrane proteins, including setting the N-exo topology of the first transmembrane domain of G protein-coupled receptors. Mutations of EMC6 residues at the cytoplasmic/TM1 boundary (Asp-27, Thr-31) impair client insertion without disrupting complex assembly, demonstrating a direct contribution of EMC6 to the insertase reaction. EMC6 localizes to the ER membrane and is broadly expressed.
- Existing/core annotation action counts: ACCEPT: 19; KEEP_AS_NON_CORE: 11; MARK_AS_OVER_ANNOTATED: 1

## PN Consistency Summary

- **Consistency:** Consistent, and the two-branch placement is well-handled on both sides. EMC6 is the catalytic-core subunit pairing with EMC3 in the vestibule (D27/T31 mutagenesis separates insertion from assembly → GO:0032977 core). Separately, the single 2013 study (PMID:23182941: RAB5A/BECN1 interaction, DFCP1/omegasome colocalization, autophagosome-formation defect) underlies GOA's GO:0000045 (autophagosome assembly, IMP+IBA) and GO:1903349 (omegasome membrane, IDA) — all KEEP_AS_NON_CORE in the review, matching PN's judgment that the autophagy role is context, likely indirect via client biogenesis. No contradictions.
- **PN story / NEW pressure:** Row 2 is the only place PN asserts a role beyond the EMC insertase story (BECN1-mediated recruitment of PI3K complex to the autophagophore nucleation site). This is partially captured in GOA (autophagosome assembly, omegasome membrane) and in the review (BECN1/RAB5A protein-binding, omegasome). PN correctly does NOT claim EMC6 is a PI3K-complex member (GO:0035032 marked too_broad/context_only). No defensible NEW GO term — the existing autophagosome-assembly term covers the asserted role and is already present. Conclusion: already captured (and appropriately non-core).
- **Evidence alignment:** Good overlap on EMC papers (PMID:22119785, PMID:29242231, PMID:32439656, PMID:34918864). Row2's PN reference is a non-PMID review ("Membrane Trafficking in Autophagy - ScienceDirect"); the review instead anchors the autophagy role to the primary PMID:23182941, a stronger citation. Slight divergence: PN row-2 evidence is a secondary review whereas the gene review uses the primary experimental paper.
- **Verdict:** Consistent across both branches; autophagy/PI3K role correctly captured as non-core and correctly NOT projected as complex membership; PN adds no NEW pressure; row1 projected group/class terms broader than review.

## Full Consistency Review

- **UniProt:** Q9BV81 (TMEM93) · **batch:** proteostasis-batch-2026-06-11 · **review status:** COMPLETE (thorough; all annotations including autophagy block adjudicated)
- **PN placement:** Row 1 `ER proteostasis | Protein transport | Transmembrane protein import | EMC complex component`; Row 2 `Autophagy-Lysosome Pathway | Autophagophore initiation and elongation | Class 3 PI3K complex 1, direct | Localization of class 3 PI3K complex 1` (branches ER + ALP). **PN-node mapping:** row1 type→GO:0072546 EMC complex (already_in_goa_exact), group→GO:0044743, class→GO:0015031; row2 entirely context_only/too_broad_to_propagate (GO:0035032 PI3K III; GO:0016236 macroautophagy) — projects NOTHING.
- **Consistency:** Consistent, and the two-branch placement is well-handled on both sides. EMC6 is the catalytic-core subunit pairing with EMC3 in the vestibule (D27/T31 mutagenesis separates insertion from assembly → GO:0032977 core). Separately, the single 2013 study (PMID:23182941: RAB5A/BECN1 interaction, DFCP1/omegasome colocalization, autophagosome-formation defect) underlies GOA's GO:0000045 (autophagosome assembly, IMP+IBA) and GO:1903349 (omegasome membrane, IDA) — all KEEP_AS_NON_CORE in the review, matching PN's judgment that the autophagy role is context, likely indirect via client biogenesis. No contradictions.
- **PN story / NEW pressure:** Row 2 is the only place PN asserts a role beyond the EMC insertase story (BECN1-mediated recruitment of PI3K complex to the autophagophore nucleation site). This is partially captured in GOA (autophagosome assembly, omegasome membrane) and in the review (BECN1/RAB5A protein-binding, omegasome). PN correctly does NOT claim EMC6 is a PI3K-complex member (GO:0035032 marked too_broad/context_only). No defensible NEW GO term — the existing autophagosome-assembly term covers the asserted role and is already present. Conclusion: already captured (and appropriately non-core).
- **Mapping strategy:** EMC6 does not change either node. Row1 type→GO:0072546 exact/correct; projected group/class (GO:0044743, GO:0015031) broader than review's specific insertion terms (broader-ancestor pattern, cf. TOMM20/HSPA8/RAB7A). Row2 correctly projects nothing — EMC6 is a BECN1 interactor/regulator, not a class-III PI3K complex component, so withholding GO:0035032 membership is the right call (avoids a false complex-membership assertion).
- **Evidence alignment:** Good overlap on EMC papers (PMID:22119785, PMID:29242231, PMID:32439656, PMID:34918864). Row2's PN reference is a non-PMID review ("Membrane Trafficking in Autophagy - ScienceDirect"); the review instead anchors the autophagy role to the primary PMID:23182941, a stronger citation. Slight divergence: PN row-2 evidence is a secondary review whereas the gene review uses the primary experimental paper.
- **Verdict:** Consistent across both branches; autophagy/PI3K role correctly captured as non-core and correctly NOT projected as complex membership; PN adds no NEW pressure; row1 projected group/class terms broader than review.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-11
- review_yaml: genes/human/EMC6/EMC6-ai-review.yaml
- PN workbook rows: 2

## PN row 1: ER proteostasis | Protein transport | Transmembrane protein import | EMC complex component
- UniProt: Q9BV81
- In branches: ER, ALP
- PN-node mapping records (path + ancestors):
    - [type] ER proteostasis|Protein transport|Transmembrane protein import|EMC complex component
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0072546 EMC complex]
        rationale: This PN type denotes ER membrane protein complex components. The GO EMC complex cellular-component term is the direct target.
    - [group] ER proteostasis|Protein transport|Transmembrane protein import
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0044743 protein transmembrane import into intracellular organelle]
        rationale: This PN group covers ER transmembrane-protein insertion/import systems such as EMC- and PAT-related pathways. The local GO cache does not expose an ER-specific matching term, so the broader intracellular-organelle transmembrane-import process is the best supported propagation target.
    - [class] ER proteostasis|Protein transport
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0015031 protein transport]
        rationale: The PN ER Protein transport class groups ER-targeting and ER-insertion pathways. GO protein transport is the appropriate propagation target, while the source class remains ER-specific and broader than any single GO transport subtype.
    - [branch] ER proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## PN row 2: Autophagy-Lysosome Pathway | Autophagophore initiation and elongation | Class 3 PI3K complex 1, direct | Localization of class 3 PI3K complex 1
- UniProt: Q9BV81
- In branches: ER, ALP
- Notes: Transmembrane ER protein that localizes to omegasomes and interacts with BECN1 to recruit PI3K complex to autophagophore nucleation site.
- PN references (titles):
    - Membrane Trafficking in Autophagy - ScienceDirect
- PN-node mapping records (path + ancestors):
    - [type] Autophagy-Lysosome Pathway|Autophagophore initiation and elongation|Class 3 PI3K complex 1, direct|Localization of class 3 PI3K complex 1
        status=context_only scope=too_broad_to_propagate GO=[GO:0035032 phosphatidylinositol 3-kinase complex, class III]
        rationale: Reviewed as a class-III PI3K complex context or regulator bucket. This node is useful for curator interpretation, but it should not project cellular-component membership; only explicit complex-component leaves propagate to GO complex terms.
    - [group] Autophagy-Lysosome Pathway|Autophagophore initiation and elongation|Class 3 PI3K complex 1, direct
        status=context_only scope=too_broad_to_propagate GO=[GO:0035032 phosphatidylinositol 3-kinase complex, class III]
        rationale: Reviewed as a class-III PI3K complex context or regulator bucket. This node is useful for curator interpretation, but it should not project cellular-component membership; only explicit complex-component leaves propagate to GO complex terms.
    - [class] Autophagy-Lysosome Pathway|Autophagophore initiation and elongation
        status=context_only scope=too_broad_to_propagate GO=[GO:0016236 macroautophagy]
        rationale: This class is a real macroautophagy context, but its descendants include core factors, component buckets, upstream modulators, localization roles, and residual categories. Projecting generic macroautophagy from this ancestor creates TRAPP-like overpropagation, so candidate GO annotations must come from narrower curated nodes.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## Projected GO annotations (3)
- GO:0015031 protein transport | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=ER proteostasis|Protein transport
- GO:0044743 protein transmembrane import into intracellular organelle | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=ER proteostasis|Protein transport|Transmembrane protein import
- GO:0072546 EMC complex | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=ER proteostasis|Protein transport|Transmembrane protein import|EMC complex component

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
