# AKT1 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: P31749
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-03 (PR 1362)
- Batch change status: modified

## Source Files Checked

- AIGR review YAML: present - [genes/human/AKT1/AKT1-ai-review.yaml](AKT1-ai-review.yaml)
- AIGR review HTML: present - [genes/human/AKT1/AKT1-ai-review.html](AKT1-ai-review.html)
- Gene notes: present - [genes/human/AKT1/AKT1-notes.md](AKT1-notes.md)
- GOA TSV: present - [genes/human/AKT1/AKT1-goa.tsv](AKT1-goa.tsv)
- UniProt record: present - [genes/human/AKT1/AKT1-uniprot.txt](AKT1-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/AKT1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/AKT1.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/AKT1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/AKT1.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/AKT1/AKT1-deep-research-falcon.md](AKT1-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: AKT1 encodes RAC-alpha serine/threonine-protein kinase, a central AGC-family kinase in PI3K-AKT signaling. Its core function is phosphoinositide-regulated protein serine/threonine phosphorylation downstream of growth factor, insulin, and other receptor inputs, with broad downstream effects on mTOR signaling, metabolism, survival, growth, and migration.
- Existing/core annotation action counts: ACCEPT: 208; KEEP_AS_NON_CORE: 131; MARK_AS_OVER_ANNOTATED: 97; MODIFY: 7; NEW: 1; REMOVE: 2

## PN Consistency Summary

- **Consistency:** Consistent across layers. Deep research (falcon) frames AKT1 as the PI3K-AKT Ser/Thr kinase; PN notes capture TSC2, GFAP/LAMP2, FOXO1/3, and LAMP2A-multimerization CMA inhibition. Review adopts only the CMA-inhibitor projection (**action NEW GO:1904715**, IMP, PMID:26118642) and keeps TSC/FOXO/autophagy roles as non-core kinase outputs. No contradiction.
- **PN story / NEW pressure:** PN asserts directional CMA inhibition not specifically in GOA (GOA has only broad GO:0010507 negative regulation of autophagy). GO:1904715 verified real (child of GO:0010507 + GO:1904714); GOA confirms it is genuinely more-specific/new. Direct support from lysosomal mTORC2/PHLPP1/Akt CMA assays (PMID:26118642). Verdict: ADD — defensible refinement of the existing broad term.
- **Evidence alignment:** Good overlap. PN reference titles (Lysosomal mTORC2/PHLPP1/Akt = PMID:26118642; Akt/FoxO; TSC2-Akt) map onto review references PMID:26118642, 12172553, FOXO PMIDs. CMA-collapse and CMA-motif papers cited in PN are background, not load-bearing for the GO:1904715 call.
- **Verdict:** Consistent; GO:1904715 ADD confirmed (realized as NEW in review). TSC/FOXO correctly kept as non-core.

## Full Consistency Review

- **UniProt:** P31749 · **batch:** proteostasis-batch-2026-06-03 · **review status:** COMPLETE
- **PN placement:** three ALP rows — mTORC1-upstream/insulin/TSC-deactivator; FOXO transcriptional-program modulator; and `Chaperone-mediated autophagy|...|CMA inhibitor|Modulator of LAMP2A multimerization` ; **PN-node mapping:** TSC and FOXO subtrees no_mapping / context_only (too_broad, GO:0010506); CMA-inhibitor *type* mapped→GO:1904715 (negative regulation of CMA, propagate). Projection: **GO:1904715 more_specific_than_existing_goa**.
- **Consistency:** Consistent across layers. Deep research (falcon) frames AKT1 as the PI3K-AKT Ser/Thr kinase; PN notes capture TSC2, GFAP/LAMP2, FOXO1/3, and LAMP2A-multimerization CMA inhibition. Review adopts only the CMA-inhibitor projection (**action NEW GO:1904715**, IMP, PMID:26118642) and keeps TSC/FOXO/autophagy roles as non-core kinase outputs. No contradiction.
- **PN story / NEW pressure:** PN asserts directional CMA inhibition not specifically in GOA (GOA has only broad GO:0010507 negative regulation of autophagy). GO:1904715 verified real (child of GO:0010507 + GO:1904714); GOA confirms it is genuinely more-specific/new. Direct support from lysosomal mTORC2/PHLPP1/Akt CMA assays (PMID:26118642). Verdict: ADD — defensible refinement of the existing broad term.
- **Mapping strategy:** No node change. The mapping correctly restricts propagation to the CMA-**inhibitor type** (directional GO:1904715) rather than projecting the class-level GO:0061684 chaperone-mediated autophagy (which would wrongly make AKT1 a direct CMA participant). The LAMP2A-multimerization subtype stays no_mapping/contextual — appropriate. PN-projected term is correctly scoped (narrower than class, not over-broad).
- **Evidence alignment:** Good overlap. PN reference titles (Lysosomal mTORC2/PHLPP1/Akt = PMID:26118642; Akt/FoxO; TSC2-Akt) map onto review references PMID:26118642, 12172553, FOXO PMIDs. CMA-collapse and CMA-motif papers cited in PN are background, not load-bearing for the GO:1904715 call.
- **Verdict:** Consistent; GO:1904715 ADD confirmed (realized as NEW in review). TSC/FOXO correctly kept as non-core.
- **Recommended edits:** None warranted.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-03
- review_yaml: genes/human/AKT1/AKT1-ai-review.yaml
- PN workbook rows: 3

## PN row 1: Autophagy-Lysosome Pathway | Pre-initiation autophagy signaling | mTORC1 pathway, upstream | Insulin signaling pathway | TSC complex deactivator
- UniProt: P31749
- In branches: ALP
- Notes: Inhibits TSC1-TSC2 complex by phosphorylating TSC2. Also phosphorylates GFAP to prevent it from interacting with and stabilizing the LAMP2 translocation pore in chaperone-mediated autophagy. AKT1 also phosphorylates FOXO1 and FOXO3 which prevents their nuclear translocation and the transcription of autophagy-related genes by FOXO1 and FOXO3. Also inhibits chaperone-mediated autophagy by modulating LAMP2A multimerization.
- PN references (titles):
    - p53 Regulation of the IGF-1/AKT/mTOR Pathways and the Endosomal Compartment (cshlp.org)
    - Lysosomal mTORC2/PHLPP1/Akt Regulate Chaperone-Mediated Autophagy - ScienceDirect
    - Nuclear Trapping of the Forkhead Transcription Factor FoxO1 via Sirt-dependent Deacetylation Promotes Expression of Glucogenetic Genes* - Journal of Biological Chemistry (jbc.org)
    - Akt Promotes Cell Survival by Phosphorylating and Inhibiting a Forkhead Transcription Factor - ScienceDirect
    - Chaperone-mediated autophagy prevents collapse of the neuronal metastable proteome - ScienceDirect
    - Proteome-wide analysis of chaperone-mediated autophagy targeting motifs | PLOS Biology
- PN-node mapping records (path + ancestors):
    - [subtype] Autophagy-Lysosome Pathway|Pre-initiation autophagy signaling|mTORC1 pathway, upstream|Insulin signaling pathway|TSC complex deactivator
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a contextual PN role. The label is useful for curator triage, but by itself does not support a universal GO assertion for all member genes beyond curated ancestor or child mappings.
    - [type] Autophagy-Lysosome Pathway|Pre-initiation autophagy signaling|mTORC1 pathway, upstream|Insulin signaling pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a contextual PN role. The label is useful for curator triage, but by itself does not support a universal GO assertion for all member genes beyond curated ancestor or child mappings.
    - [group] Autophagy-Lysosome Pathway|Pre-initiation autophagy signaling|mTORC1 pathway, upstream
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN taxonomy container. The descendants mix components, regulators, context labels, and mechanistic leaves, so propagation should come only from narrower curated nodes.
    - [class] Autophagy-Lysosome Pathway|Pre-initiation autophagy signaling
        status=context_only scope=too_broad_to_propagate GO=[GO:0010506 regulation of autophagy]
        rationale: This class organizes upstream signaling inputs to autophagy initiation. Because the subtree contains generic insulin, AMPK, mTORC1, nutrient-sensing, and miscellaneous signaling components, class-level propagation to regulation of autophagy would over-annotate many genes.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## PN row 2: Autophagy-Lysosome Pathway | Autophagy gene expression | FOXO transcriptional program | Modulator of FOXO1 and FOXO3 activity
- UniProt: P31749
- In branches: ALP
- Notes: Inhibits TSC1-TSC2 complex by phosphorylating TSC2. Also phosphorylates GFAP to prevent it from interacting with and stabilizing the LAMP2 translocation pore in chaperone-mediated autophagy. AKT1 also phosphorylates FOXO1 and FOXO3 which prevents their nuclear translocation and the transcription of autophagy-related genes by FOXO1 and FOXO3. Also inhibits chaperone-mediated autophagy by modulating LAMP2A multimerization.
- PN references (titles):
    - p53 Regulation of the IGF-1/AKT/mTOR Pathways and the Endosomal Compartment (cshlp.org)
    - Lysosomal mTORC2/PHLPP1/Akt Regulate Chaperone-Mediated Autophagy - ScienceDirect
    - Nuclear Trapping of the Forkhead Transcription Factor FoxO1 via Sirt-dependent Deacetylation Promotes Expression of Glucogenetic Genes* - Journal of Biological Chemistry (jbc.org)
    - Akt Promotes Cell Survival by Phosphorylating and Inhibiting a Forkhead Transcription Factor - ScienceDirect
    - Chaperone-mediated autophagy prevents collapse of the neuronal metastable proteome - ScienceDirect
    - Proteome-wide analysis of chaperone-mediated autophagy targeting motifs | PLOS Biology
- PN-node mapping records (path + ancestors):
    - [type] Autophagy-Lysosome Pathway|Autophagy gene expression|FOXO transcriptional program|Modulator of FOXO1 and FOXO3 activity
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a contextual PN role. The label is useful for curator triage, but by itself does not support a universal GO assertion for all member genes beyond curated ancestor or child mappings.
    - [group] Autophagy-Lysosome Pathway|Autophagy gene expression|FOXO transcriptional program
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN taxonomy container. The descendants mix components, regulators, context labels, and mechanistic leaves, so propagation should come only from narrower curated nodes.
    - [class] Autophagy-Lysosome Pathway|Autophagy gene expression
        status=context_only scope=too_broad_to_propagate GO=[GO:0010506 regulation of autophagy]
        rationale: This class records autophagy-linked gene-expression programs, but many nodes are transcription program names or upstream modulators rather than direct GO regulation assertions. It is kept as context only; transcription factor or cofactor activities are mapped at narrower nodes.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## PN row 3: Autophagy-Lysosome Pathway | Chaperone-mediated autophagy | Lysosomal modulator of chaperone-mediated autophagy | Chaperone-mediated autophagy inhibitor | Modulator of LAMP2A multimerization
- UniProt: P31749
- In branches: ALP
- Notes: Inhibits TSC1-TSC2 complex by phosphorylating TSC2. Also phosphorylates GFAP to prevent it from interacting with and stabilizing the LAMP2 translocation pore in chaperone-mediated autophagy. AKT1 also phosphorylates FOXO1 and FOXO3 which prevents their nuclear translocation and the transcription of autophagy-related genes by FOXO1 and FOXO3. Also inhibits chaperone-mediated autophagy by modulating LAMP2A multimerization.
- PN references (titles):
    - p53 Regulation of the IGF-1/AKT/mTOR Pathways and the Endosomal Compartment (cshlp.org)
    - Lysosomal mTORC2/PHLPP1/Akt Regulate Chaperone-Mediated Autophagy - ScienceDirect
    - Nuclear Trapping of the Forkhead Transcription Factor FoxO1 via Sirt-dependent Deacetylation Promotes Expression of Glucogenetic Genes* - Journal of Biological Chemistry (jbc.org)
    - Akt Promotes Cell Survival by Phosphorylating and Inhibiting a Forkhead Transcription Factor - ScienceDirect
    - Chaperone-mediated autophagy prevents collapse of the neuronal metastable proteome - ScienceDirect
    - Proteome-wide analysis of chaperone-mediated autophagy targeting motifs | PLOS Biology
- PN-node mapping records (path + ancestors):
    - [subtype] Autophagy-Lysosome Pathway|Chaperone-mediated autophagy|Lysosomal modulator of chaperone-mediated autophagy|Chaperone-mediated autophagy inhibitor|Modulator of LAMP2A multimerization
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a contextual PN role. The label is useful for curator triage, but by itself does not support a universal GO assertion for all member genes beyond curated ancestor or child mappings.
    - [type] Autophagy-Lysosome Pathway|Chaperone-mediated autophagy|Lysosomal modulator of chaperone-mediated autophagy|Chaperone-mediated autophagy inhibitor
        status=mapped scope=ok_for_propagation_to_go GO=[GO:1904715 negative regulation of chaperone-mediated autophagy]
        rationale: This PN type explicitly records inhibitory roles for CMA. The directional GO regulation term is more accurate than projecting direct participation in CMA from the class ancestor.
    - [group] Autophagy-Lysosome Pathway|Chaperone-mediated autophagy|Lysosomal modulator of chaperone-mediated autophagy
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN taxonomy container. The descendants mix components, regulators, context labels, and mechanistic leaves, so propagation should come only from narrower curated nodes.
    - [class] Autophagy-Lysosome Pathway|Chaperone-mediated autophagy
        status=context_only scope=too_broad_to_propagate GO=[GO:0061684 chaperone-mediated autophagy]
        rationale: The class label matches the GO CMA process, but the subtree includes both effectors and positive or negative modulators. The relation is retained as context so modulators are not projected as direct CMA participants unless a narrower node supports it.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## Projected GO annotations (1)
- GO:1904715 negative regulation of chaperone-mediated autophagy | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=Autophagy-Lysosome Pathway|Chaperone-mediated autophagy|Lysosomal modulator of chaperone-mediated autophagy|Chaperone-mediated autophagy inhibitor

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
