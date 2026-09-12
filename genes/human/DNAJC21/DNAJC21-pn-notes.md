# DNAJC21 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q5F1R6
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07b
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/DNAJC21/DNAJC21-ai-review.yaml](DNAJC21-ai-review.yaml)
- AIGR review HTML: present - [genes/human/DNAJC21/DNAJC21-ai-review.html](DNAJC21-ai-review.html)
- Gene notes: present - [genes/human/DNAJC21/DNAJC21-notes.md](DNAJC21-notes.md)
- GOA TSV: present - [genes/human/DNAJC21/DNAJC21-goa.tsv](DNAJC21-goa.tsv)
- UniProt record: present - [genes/human/DNAJC21/DNAJC21-uniprot.txt](DNAJC21-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/DNAJC21.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/DNAJC21.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/DNAJC21.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/DNAJC21.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: DNAJC21 (DnaJ homolog subfamily C member 21; also DNAJA5) is a J-domain co-chaperone of the HSP70 system that functions in ribosome biogenesis, specifically in the maturation of the large (60S) ribosomal subunit. It contains an N-terminal J-domain and two C2H2 zinc fingers within an otherwise disordered C-terminal region. DNAJC21 localizes to the cytoplasm, the nucleus and especially the nucleolus, associates with precursor 45S rRNA, and works with the HSP70 chaperone HSPA8 and the cofactors PA2G4 (a 60S nuclear-export factor) and ZNF622 to drive late nucleolar rRNA biogenesis and cytoplasmic maturation/recycling of the 60S subunit. It is the human counterpart of the yeast 60S-maturation factor Jjj1/Zuo1-like J-protein. Biallelic loss-of-function variants cause a cancer-prone bone marrow failure syndrome (BMFS3, Shwachman-Diamond-like), establishing DNAJC21 as a ribosomopathy gene.
- Existing/core annotation action counts: ACCEPT: 9; KEEP_AS_NON_CORE: 5; MARK_AS_OVER_ANNOTATED: 1

## PN Consistency Summary

- **Consistency:** Strong agreement, and the two-row PN placement is the right call. Notes, review and PN all describe a J-domain co-chaperone of HSPA8 that drives 60S ribosomal-subunit maturation (PMID:27346687), binds precursor 45S rRNA, and causes ribosomopathy BMFS3. No contradictions. PN's dual chaperone+ribosome-biogenesis framing matches the review's two core functions (chaperone binding; RNA binding) better than a single HSP70-cochaperone row would.
- **PN story / NEW pressure:** PN proposes three terms, all verified real (OLS): GO:0030544 Hsp70 protein binding, GO:0042254 ribosome biogenesis, GO:0030687 preribosome large subunit precursor. GOA confirms ribosome biogenesis and pre-60S are genuinely ABSENT from existing annotations (goa.tsv has only RNA binding, nucleolus, ribosome NAS, protein folding NAS). Both GO:0042254 and GO:0030687 are well-supported ADDs (PMID:27346687 establishes the conserved 60S-maturation role). GO:0030544: HSPA8 binding is documented (review uses the parent GO:0051087 protein-folding chaperone binding as core MF); GO:0030544 is the verified more-specific child, so here the "more_specific" tag IS accurate.
- **Evidence alignment:** Excellent. Both rest on PMID:27346687 (Tummala 2016, VERIFIED) for 60S maturation, plus PMID:22658674 (RNA-interactome) for RNA binding. PN row-2 reference titles align with the ribosome-biogenesis story.
- **Verdict:** Consistent and exemplary; the two ribosome-biogenesis ADDs (GO:0042254, GO:0030687) are well-supported and genuinely new to GOA, and GO:0030544 is correctly the more-specific HSP70-binding child. No edits required.

## Full Consistency Review

- **UniProt:** Q5F1R6 (DNAJA5) · **batch:** proteostasis-batch-2026-06-07b · **review status:** COMPLETE
- **PN placement:** Two rows — (1) `Cytonuclear proteostasis | Chaperone | HSP70 system | J-domain containing HSP70 cochaperone` (CY); (2) `Translation | Cytosolic translation | Ribosome biogenesis factor | pre-60S complex | non 5S RNP complex` (TR) ; **PN-node mapping:** row1 type=mapped GO:0030544 Hsp70 protein binding (more_specific_than_existing_goa); row2 type(pre-60S)=mapped GO:0030687 preribosome large subunit precursor (new_to_goa), group(ribosome biogenesis factor)=mapped GO:0042254 ribosome biogenesis (new_to_goa); subtype/class/branch no_mapping or context_only.
- **Consistency:** Strong agreement, and the two-row PN placement is the right call. Notes, review and PN all describe a J-domain co-chaperone of HSPA8 that drives 60S ribosomal-subunit maturation (PMID:27346687), binds precursor 45S rRNA, and causes ribosomopathy BMFS3. No contradictions. PN's dual chaperone+ribosome-biogenesis framing matches the review's two core functions (chaperone binding; RNA binding) better than a single HSP70-cochaperone row would.
- **PN story / NEW pressure:** PN proposes three terms, all verified real (OLS): GO:0030544 Hsp70 protein binding, GO:0042254 ribosome biogenesis, GO:0030687 preribosome large subunit precursor. GOA confirms ribosome biogenesis and pre-60S are genuinely ABSENT from existing annotations (goa.tsv has only RNA binding, nucleolus, ribosome NAS, protein folding NAS). Both GO:0042254 and GO:0030687 are well-supported ADDs (PMID:27346687 establishes the conserved 60S-maturation role). GO:0030544: HSPA8 binding is documented (review uses the parent GO:0051087 protein-folding chaperone binding as core MF); GO:0030544 is the verified more-specific child, so here the "more_specific" tag IS accurate.
- **Mapping strategy:** This gene materially improves the node coverage by adding the ribosome-biogenesis arm. status/scope are appropriate (pre-60S → preribosome large-subunit precursor is the direct complex target; group → ribosome biogenesis is the safe process target; branch/class kept context_only as too broad — consistent with the TOMM20/HSPA8/RAB7A "reject broader" precedent). PN-projected terms are appropriately specific, not over-broad.
- **Evidence alignment:** Excellent. Both rest on PMID:27346687 (Tummala 2016, VERIFIED) for 60S maturation, plus PMID:22658674 (RNA-interactome) for RNA binding. PN row-2 reference titles align with the ribosome-biogenesis story.
- **Verdict:** Consistent and exemplary; the two ribosome-biogenesis ADDs (GO:0042254, GO:0030687) are well-supported and genuinely new to GOA, and GO:0030544 is correctly the more-specific HSP70-binding child. No edits required.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07b
- review_yaml: genes/human/DNAJC21/DNAJC21-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Cytonuclear proteostasis | Chaperone | HSP70 system | J-domain containing HSP70 cochaperone
- UniProt: Q5F1R6
- In branches: CY, TR
- PN-node mapping records (path + ancestors):
    - [type] Cytonuclear proteostasis|Chaperone|HSP70 system|J-domain containing HSP70 cochaperone
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0030544 Hsp70 protein binding]
        rationale: In the PN hierarchy, this type denotes J-domain cochaperones assigned to the HSP70 system. Their shared mechanistic role is direct interaction with HSP70-family chaperones, making Hsp70 protein binding the most defensible GO target in the current cache.
    - [group] Cytonuclear proteostasis|Chaperone|HSP70 system
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a specific GO class. The member genes span multiple activities, complexes, or contexts, so propagation from this node would overstate the shared biology; use narrower child or gene-level curations.
    - [class] Cytonuclear proteostasis|Chaperone
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a specific GO class. The member genes span multiple activities, complexes, or contexts, so propagation from this node would overstate the shared biology; use narrower child or gene-level curations.
    - [branch] Cytonuclear proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## PN row 2: Translation | Cytosolic translation | Ribosome biogenesis factor | pre-60S complex | non 5S RNP complex
- UniProt: Q5F1R6
- In branches: CY, TR
- PN-node mapping records (path + ancestors):
    - [subtype] Translation|Cytosolic translation|Ribosome biogenesis factor|pre-60S complex|non 5S RNP complex
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower taxonomy bucket already covered by a curated parent mapping or by gene-level annotations. No additional direct GO mapping is appropriate from this node.
    - [type] Translation|Cytosolic translation|Ribosome biogenesis factor|pre-60S complex
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0030687 preribosome, large subunit precursor]
        rationale: This PN type denotes pre-60S particles. The GO preribosome large-subunit precursor term is the direct complex target.
    - [group] Translation|Cytosolic translation|Ribosome biogenesis factor
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0042254 ribosome biogenesis]
        rationale: This PN group collects factors assigned through cytosolic ribosome biogenesis, including SSU-processosome and pre-60S maturation machinery. The full PN path resolves the earlier over-annotation problem: these genes are not being placed by core translational elongation or decoding, but by assembly and maturation of ribosomal subunits. GO ribosome biogenesis is therefore the appropriate propagation target.
    - [class] Translation|Cytosolic translation
        status=context_only scope=too_broad_to_propagate GO=[GO:0002181 cytoplasmic translation]
        rationale: The PN class Cytosolic translation is centered on the cytoplasmic translation apparatus and process, but it also houses supporting machinery such as ribosome biogenesis factors. The GO process term is a useful high-level label for the class, but propagating it to all members would over-annotate genes whose PN placement is through assembly or maturation context rather than core cytoplasmic translation.
    - [branch] Translation
        status=context_only scope=too_broad_to_propagate GO=[GO:0006412 translation]
        rationale: The PN Translation branch is organized around the translation apparatus and immediately associated cotranslational quality-control systems. GO translation is the closest high-level process label, but the PN branch also contains adjacent machinery such as ribosome biogenesis and nascent-chain handling. Keeping this relationship is useful for interpretation, but it is too broad to project safely onto every member.

## Projected GO annotations (3)
- GO:0030544 Hsp70 protein binding | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=Cytonuclear proteostasis|Chaperone|HSP70 system|J-domain containing HSP70 cochaperone
- GO:0042254 ribosome biogenesis | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Translation|Cytosolic translation|Ribosome biogenesis factor
- GO:0030687 preribosome, large subunit precursor | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Translation|Cytosolic translation|Ribosome biogenesis factor|pre-60S complex

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
