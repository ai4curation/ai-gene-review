# CSNK2B PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: P67870
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/CSNK2B/CSNK2B-ai-review.yaml](CSNK2B-ai-review.yaml)
- AIGR review HTML: present - [genes/human/CSNK2B/CSNK2B-ai-review.html](CSNK2B-ai-review.html)
- Gene notes: present - [genes/human/CSNK2B/CSNK2B-notes.md](CSNK2B-notes.md)
- GOA TSV: present - [genes/human/CSNK2B/CSNK2B-goa.tsv](CSNK2B-goa.tsv)
- UniProt record: present - [genes/human/CSNK2B/CSNK2B-uniprot.txt](CSNK2B-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/CSNK2B.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/CSNK2B.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/CSNK2B.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/CSNK2B.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: CSNK2B (casein kinase II subunit beta, CK2beta) is the non-catalytic regulatory subunit of protein kinase CK2 (casein kinase 2), a constitutively active, highly pleiotropic acidophilic serine/threonine kinase. The CK2 holoenzyme is a heterotetramer in which a CSNK2B beta dimer bridges two catalytic alpha subunits (CSNK2A1 and/or CSNK2A2); the beta subunits form a stable zinc-finger-mediated dimer that links the two catalytic subunits, which make no direct contact with each other. CSNK2B has no catalytic activity of its own. Within the holoenzyme it docks and stabilizes the catalytic subunits, raises basal catalytic activity, modulates substrate specificity and selectivity, and can recruit specific substrates and partners (e.g. via its C-terminal region and its KSSR protein-interaction pocket). CK2 phosphorylates hundreds of substrates bearing acidic residues C-terminal to the phosphoacceptor (consensus S/T-X-X-D/E), influencing transcription, translation, cell cycle, DNA repair, Wnt and other signaling, circadian rhythm, and apoptosis (its major recognized role being to counteract apoptosis). CSNK2B also has activities reported to be partly independent of CK2 catalysis, including negative regulation of cell proliferation and adaptor/scaffolding roles. It localizes predominantly to the nucleus and cytoplasm. In humans, de novo loss-of-function and missense variants cause Poirier-Bienvenu neurodevelopmental syndrome (POBINDS), an autosomal dominant disorder of seizures and intellectual disability, consistent with haploinsufficiency.
- Existing/core annotation action counts: ACCEPT: 33; KEEP_AS_NON_CORE: 23; MARK_AS_OVER_ANNOTATED: 39; MODIFY: 1

## PN Consistency Summary

- **Consistency:** ROW-1 CONFLICT. The review and notes characterize CSNK2B exclusively as the CK2 regulatory beta subunit (kinase regulator / adaptor / holoenzyme), nuclear+cytosolic, with NO ribosome-biogenesis or SSU-processome role. CSNK2B-goa.tsv has no GO:0042254/GO:0032040. The "UTP-C complex" is a **yeast** SSU-processome subcomplex (yeast Utp-C contains CK2); human CSNK2B SSU-processome membership is not established — PubMed returns zero hits for CSNK2B+UTP-C+processome. So row-1 is a likely yeast-orthology over-projection. Row-2 (CK2 phosphorylates ATG16L1 to promote ATG5-ATG12 binding) is biologically real but the review only captures it indirectly (kinase-regulator pleiotropy); no autophagy annotation.
- **PN story / NEW pressure:** Row-1 over-reaches: projecting GO:0042254 "ribosome biogenesis" + GO:0032040 "small-subunit processome" (both verified real) onto human CSNK2B is not supported by human evidence and conflicts with the review's holoenzyme-centric core. Row-2 ATG16L1 phosphorylation is a defensible kinase-substrate role but is correctly left no_mapping (a regulatory, member-specific role, not a shared GO assertion).
- **Evidence alignment:** Row-1 lists no PN references (no human paper supports it). Row-2 PN cites a CSNK2/ATG16L1 cardiomyocyte paper + an autophagy-enzyme review (titles only, not PMIDs) — neither is in the review. Review's substrate/interactome PMIDs do not overlap the PN rows.
- **Verdict:** ROW-1 OVER-REACHES (yeast UTP-C orthology); ROW-2 acceptably no_mapping. **Recommended edits:** [MAP] downgrade row-1 SSU-processome/ribosome-biogenesis projection (GO:0032040/GO:0042254) to context_only/no_mapping for human CSNK2B pending human evidence; [WB] human CSNK2B SSU-processome membership unverified (PubMed: 0 hits).

## Full Consistency Review

- **UniProt:** P67870 · **batch:** proteostasis-batch-2026-06-07 · **review status:** COMPLETE
- **PN placement:** row1 `Translation|Cytosolic translation|Ribosome biogenesis factor|SSU processosome|UTP-C complex`; row2 `ALP|Autophagophore initiation and elongation|...|Modulation of ATG5-ATG12-ATG16 complex assembly` ; **PN-node mapping:** row1 SSU-processome type→GO:0032040 (more_specific_than_existing); RibBiogenesis group→GO:0042254 (new_to_goa). row2 entirely no_mapping (ALP class context_only→GO:0016236).
- **Consistency:** ROW-1 CONFLICT. The review and notes characterize CSNK2B exclusively as the CK2 regulatory beta subunit (kinase regulator / adaptor / holoenzyme), nuclear+cytosolic, with NO ribosome-biogenesis or SSU-processome role. CSNK2B-goa.tsv has no GO:0042254/GO:0032040. The "UTP-C complex" is a **yeast** SSU-processome subcomplex (yeast Utp-C contains CK2); human CSNK2B SSU-processome membership is not established — PubMed returns zero hits for CSNK2B+UTP-C+processome. So row-1 is a likely yeast-orthology over-projection. Row-2 (CK2 phosphorylates ATG16L1 to promote ATG5-ATG12 binding) is biologically real but the review only captures it indirectly (kinase-regulator pleiotropy); no autophagy annotation.
- **PN story / NEW pressure:** Row-1 over-reaches: projecting GO:0042254 "ribosome biogenesis" + GO:0032040 "small-subunit processome" (both verified real) onto human CSNK2B is not supported by human evidence and conflicts with the review's holoenzyme-centric core. Row-2 ATG16L1 phosphorylation is a defensible kinase-substrate role but is correctly left no_mapping (a regulatory, member-specific role, not a shared GO assertion).
- **Mapping strategy:** Row-1 mapping should be reconsidered — analogous to the rejected TOMM20/HSPA8/RAB7A "too broad / orthology-driven" cases, GO:0042254/GO:0032040 over-annotate human CSNK2B. Row-2 ALP handling (all no_mapping / context_only) is appropriately conservative.
- **Evidence alignment:** Row-1 lists no PN references (no human paper supports it). Row-2 PN cites a CSNK2/ATG16L1 cardiomyocyte paper + an autophagy-enzyme review (titles only, not PMIDs) — neither is in the review. Review's substrate/interactome PMIDs do not overlap the PN rows.
- **Verdict:** ROW-1 OVER-REACHES (yeast UTP-C orthology); ROW-2 acceptably no_mapping. **Recommended edits:** [MAP] downgrade row-1 SSU-processome/ribosome-biogenesis projection (GO:0032040/GO:0042254) to context_only/no_mapping for human CSNK2B pending human evidence; [WB] human CSNK2B SSU-processome membership unverified (PubMed: 0 hits).

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07
- review_yaml: genes/human/CSNK2B/CSNK2B-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Translation | Cytosolic translation | Ribosome biogenesis factor | SSU processosome | UTP-C complex
- UniProt: P67870
- In branches: TR, ALP
- PN-node mapping records (path + ancestors):
    - [subtype] Translation|Cytosolic translation|Ribosome biogenesis factor|SSU processosome|UTP-C complex
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower taxonomy bucket already covered by a curated parent mapping or by gene-level annotations. No additional direct GO mapping is appropriate from this node.
    - [type] Translation|Cytosolic translation|Ribosome biogenesis factor|SSU processosome
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0032040 small-subunit processome]
        rationale: This PN type denotes SSU processosome factors. The GO small-subunit processome term is the direct complex target.
    - [group] Translation|Cytosolic translation|Ribosome biogenesis factor
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0042254 ribosome biogenesis]
        rationale: This PN group collects factors assigned through cytosolic ribosome biogenesis, including SSU-processosome and pre-60S maturation machinery. The full PN path resolves the earlier over-annotation problem: these genes are not being placed by core translational elongation or decoding, but by assembly and maturation of ribosomal subunits. GO ribosome biogenesis is therefore the appropriate propagation target.
    - [class] Translation|Cytosolic translation
        status=context_only scope=too_broad_to_propagate GO=[GO:0002181 cytoplasmic translation]
        rationale: The PN class Cytosolic translation is centered on the cytoplasmic translation apparatus and process, but it also houses supporting machinery such as ribosome biogenesis factors. The GO process term is a useful high-level label for the class, but propagating it to all members would over-annotate genes whose PN placement is through assembly or maturation context rather than core cytoplasmic translation.
    - [branch] Translation
        status=context_only scope=too_broad_to_propagate GO=[GO:0006412 translation]
        rationale: The PN Translation branch is organized around the translation apparatus and immediately associated cotranslational quality-control systems. GO translation is the closest high-level process label, but the PN branch also contains adjacent machinery such as ribosome biogenesis and nascent-chain handling. Keeping this relationship is useful for interpretation, but it is too broad to project safely onto every member.

## PN row 2: Autophagy-Lysosome Pathway | Autophagophore initiation and elongation | ATG8 homolog processing, upstream | Preparation of ATG8 homologs for lipidation | Modulation of ATG5-ATG12-ATG16 complex assembly
- UniProt: P67870
- In branches: TR, ALP
- Notes: Member of Casein kinase II complex. Phosphorylates ATG16L1 to increase it's affinity for ATG5-ATG12.
- PN references (titles):
    - Full article: ATG16L1 phosphorylation is oppositely regulated by CSNK2/casein kinase 2 and PPP1/protein phosphatase 1 which determines the fate of cardiomyocytes during hypoxia/reoxygenation (tandfonline.com)
    - Regulation of Autophagy Enzymes by Nutrient Signaling - ScienceDirect
- PN-node mapping records (path + ancestors):
    - [subtype] Autophagy-Lysosome Pathway|Autophagophore initiation and elongation|ATG8 homolog processing, upstream|Preparation of ATG8 homologs for lipidation|Modulation of ATG5-ATG12-ATG16 complex assembly
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a contextual PN role. The label is useful for curator triage, but by itself does not support a universal GO assertion for all member genes beyond curated ancestor or child mappings.
    - [type] Autophagy-Lysosome Pathway|Autophagophore initiation and elongation|ATG8 homolog processing, upstream|Preparation of ATG8 homologs for lipidation
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a contextual PN role. The label is useful for curator triage, but by itself does not support a universal GO assertion for all member genes beyond curated ancestor or child mappings.
    - [group] Autophagy-Lysosome Pathway|Autophagophore initiation and elongation|ATG8 homolog processing, upstream
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN taxonomy container. The descendants mix components, regulators, context labels, and mechanistic leaves, so propagation should come only from narrower curated nodes.
    - [class] Autophagy-Lysosome Pathway|Autophagophore initiation and elongation
        status=context_only scope=too_broad_to_propagate GO=[GO:0016236 macroautophagy]
        rationale: This class is a real macroautophagy context, but its descendants include core factors, component buckets, upstream modulators, localization roles, and residual categories. Projecting generic macroautophagy from this ancestor creates TRAPP-like overpropagation, so candidate GO annotations must come from narrower curated nodes.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## Projected GO annotations (2)
- GO:0042254 ribosome biogenesis | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Translation|Cytosolic translation|Ribosome biogenesis factor
- GO:0032040 small-subunit processome | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=Translation|Cytosolic translation|Ribosome biogenesis factor|SSU processosome

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
