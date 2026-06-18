# RACK1 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: P63244
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07c
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/RACK1/RACK1-ai-review.yaml](RACK1-ai-review.yaml)
- AIGR review HTML: present - [genes/human/RACK1/RACK1-ai-review.html](RACK1-ai-review.html)
- Gene notes: present - [genes/human/RACK1/RACK1-notes.md](RACK1-notes.md)
- GOA TSV: present - [genes/human/RACK1/RACK1-goa.tsv](RACK1-goa.tsv)
- UniProt record: present - [genes/human/RACK1/RACK1-uniprot.txt](RACK1-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/RACK1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/RACK1.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/RACK1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/RACK1.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: RACK1 (Receptor for Activated C Kinase 1; formerly GNB2L1) is a highly conserved seven-bladed WD40 beta-propeller protein that is an integral component of the small (40S) ribosomal subunit, where it sits on the head of the subunit near the mRNA exit channel. As a ribosomal protein it contributes to translational control and is a central platform for ribosome-associated quality control (RQC) of stalled and collided ribosomes, promoting regulatory ubiquitylation of a subset of 40S ribosomal proteins together with the E3 ubiquitin ligase ZNF598 to resolve poly(A)-induced and other terminal stalls. Independently of the ribosome, RACK1 is a versatile signaling scaffold whose WD40 propeller mediates interactions with a large set of partners; it binds and stabilizes activated protein kinase C, inhibits Src-family tyrosine kinases, and acts as an adaptor that assembles and regulates diverse signaling complexes affecting cell growth, migration, apoptosis, receptor/channel trafficking and the stability of clients such as HIF1A. RACK1 is predominantly cytosolic and ribosome-associated, with additional context-dependent localizations (plasma membrane, perinuclear region, nucleus, neuronal projections). It is also exploited by numerous viruses and pathogens to remodel translation or subvert host signaling.
- Existing/core annotation action counts: ACCEPT: 25; KEEP_AS_NON_CORE: 110; MARK_AS_OVER_ANNOTATED: 4

## PN Consistency Summary

- **Consistency:** Partial. Review/notes and PN agree strongly on the **40S structural + RQC scaffold** core (integral 40S protein, collision sensing, ZNF598-dependent RPS2/3/20 ubiquitylation, GO:0072344, GO:0016567, GO:0043022). **Two PN rows are absent from the review/notes:** (a) ribosome **biogenesis / pre-40S** placement, and (b) the **ATG5/autophagy** regulator role (PN Notes cite the RACK1-ATG5 paper). GOA confirms NO biogenesis, pre-40S, GO:0042254, GO:0030688, GO:0016236 or ATG terms. So PN asserts two roles the review neither covers nor refutes.
- **PN story / NEW pressure:** GO:0042254 ribosome biogenesis and GO:0030688 preribosome SSU precursor (both verified real) are genuinely new and NOT in review/GOA. RACK1 is incorporated late into pre-40S particles, so a biogenesis/pre-40S association is biologically plausible — but the review's stance is that RACK1's ribosomal role is **structural/translational/RQC**, not assembly. This is a candidate ADD that needs literature support before projection (the review did not assess it). GO:0072344 already captured (IMP+IBA). GO:0006515 broader/redundant with GO:0072344.
- **Evidence alignment:** PN row3 cites the RACK1-ATG5 autophagy paper (title only, no PMID); this paper is absent from the review references entirely. PN biogenesis rows cite nothing. Review RQC evidence (PMID:28132843, 23636399, 25901680) does not overlap PN's cited material. Divergence: autophagy + biogenesis literature uncited in review.
- **Verdict:** Core RQC/40S consistent; PN biogenesis (GO:0042254/GO:0030688) and ATG5-autophagy stories are NOT in the review — candidate ADDs requiring verification, currently over-reaching as auto-projections.

## Full Consistency Review

- **UniProt:** P63244 · **batch:** proteostasis-batch-2026-06-07c · **review status:** COMPLETE (very large, ~80 annotations; core = 40S/RQC scaffold)
- **PN placement:** 3 rows — `Translation|Cytosolic translation|Ribosome biogenesis factor|pre-40S complex`; `…|Ribosome-associated QC|Ribosomal rescue`; `Autophagy-Lysosome Pathway|…|Modulation of ATG5-ATG12-ATG16 complex activity`. **PN-node mapping:** biogenesis-group→mapped GO:0042254 ribosome biogenesis (new_to_goa); pre-40S-type→mapped GO:0030688 preribosome SSU precursor (new_to_goa); rescue-type→GO:0072344 (already_in_goa); RQC-group→GO:0006515 (new); ALP leaf/group no_mapping. Projected: GO:0042254, GO:0030688, GO:0006515 (all new), GO:0072344 (in GOA).
- **Consistency:** Partial. Review/notes and PN agree strongly on the **40S structural + RQC scaffold** core (integral 40S protein, collision sensing, ZNF598-dependent RPS2/3/20 ubiquitylation, GO:0072344, GO:0016567, GO:0043022). **Two PN rows are absent from the review/notes:** (a) ribosome **biogenesis / pre-40S** placement, and (b) the **ATG5/autophagy** regulator role (PN Notes cite the RACK1-ATG5 paper). GOA confirms NO biogenesis, pre-40S, GO:0042254, GO:0030688, GO:0016236 or ATG terms. So PN asserts two roles the review neither covers nor refutes.
- **PN story / NEW pressure:** GO:0042254 ribosome biogenesis and GO:0030688 preribosome SSU precursor (both verified real) are genuinely new and NOT in review/GOA. RACK1 is incorporated late into pre-40S particles, so a biogenesis/pre-40S association is biologically plausible — but the review's stance is that RACK1's ribosomal role is **structural/translational/RQC**, not assembly. This is a candidate ADD that needs literature support before projection (the review did not assess it). GO:0072344 already captured (IMP+IBA). GO:0006515 broader/redundant with GO:0072344.
- **Mapping strategy:** RACK1 is a ribosomal scaffold/collision sensor, not a biogenesis factor by the review's framing; projecting GO:0042254/GO:0030688 from the pre-40S node risks the TRAPP-like/biogenesis over-propagation the dossier itself warns about. Recommend these stay gene-curated, not auto-projected, until verified. RQC-group→GO:0006515 broader than the exact GO:0072344 already present.
- **Evidence alignment:** PN row3 cites the RACK1-ATG5 autophagy paper (title only, no PMID); this paper is absent from the review references entirely. PN biogenesis rows cite nothing. Review RQC evidence (PMID:28132843, 23636399, 25901680) does not overlap PN's cited material. Divergence: autophagy + biogenesis literature uncited in review.
- **Verdict:** Core RQC/40S consistent; PN biogenesis (GO:0042254/GO:0030688) and ATG5-autophagy stories are NOT in the review — candidate ADDs requiring verification, currently over-reaching as auto-projections.
- **Recommended edits:** [YAML] Consider adding a note/annotation on the RACK1-ATG5 autophagy-regulator role (PN-cited) and the pre-40S/biogenesis association if literature supports — both are absent from the current review. [MAP] Do NOT auto-project GO:0042254/GO:0030688 to RACK1 from the biogenesis/pre-40S node without gene-level evidence (RACK1 framed as structural/RQC scaffold, not an assembly factor); GO:0006515 broader than the exact GO:0072344 already present. [REF] RACK1-ATG5 paper (resolve to a PMID) missing from review references.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07c
- review_yaml: genes/human/RACK1/RACK1-ai-review.yaml
- PN workbook rows: 3

## PN row 1: Translation | Cytosolic translation | Ribosome biogenesis factor | pre-40S complex
- UniProt: P63244
- In branches: TR, ALP
- PN-node mapping records (path + ancestors):
    - [type] Translation|Cytosolic translation|Ribosome biogenesis factor|pre-40S complex
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0030688 preribosome, small subunit precursor]
        rationale: This PN type denotes pre-40S particles. The GO preribosome small-subunit precursor term is the direct complex target.
    - [group] Translation|Cytosolic translation|Ribosome biogenesis factor
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0042254 ribosome biogenesis]
        rationale: This PN group collects factors assigned through cytosolic ribosome biogenesis, including SSU-processosome and pre-60S maturation machinery. The full PN path resolves the earlier over-annotation problem: these genes are not being placed by core translational elongation or decoding, but by assembly and maturation of ribosomal subunits. GO ribosome biogenesis is therefore the appropriate propagation target.
    - [class] Translation|Cytosolic translation
        status=context_only scope=too_broad_to_propagate GO=[GO:0002181 cytoplasmic translation]
        rationale: The PN class Cytosolic translation is centered on the cytoplasmic translation apparatus and process, but it also houses supporting machinery such as ribosome biogenesis factors. The GO process term is a useful high-level label for the class, but propagating it to all members would over-annotate genes whose PN placement is through assembly or maturation context rather than core cytoplasmic translation.
    - [branch] Translation
        status=context_only scope=too_broad_to_propagate GO=[GO:0006412 translation]
        rationale: The PN Translation branch is organized around the translation apparatus and immediately associated cotranslational quality-control systems. GO translation is the closest high-level process label, but the PN branch also contains adjacent machinery such as ribosome biogenesis and nascent-chain handling. Keeping this relationship is useful for interpretation, but it is too broad to project safely onto every member.

## PN row 2: Translation | Cytosolic translation | Ribosome-associated QC | Ribosomal rescue
- UniProt: P63244
- In branches: TR, ALP
- PN-node mapping records (path + ancestors):
    - [type] Translation|Cytosolic translation|Ribosome-associated QC|Ribosomal rescue
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0072344 rescue of stalled cytosolic ribosome]
        rationale: This PN RQC type denotes rescue of stalled cytosolic ribosomes. The matching GO process term is the direct target.
    - [group] Translation|Cytosolic translation|Ribosome-associated QC
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0006515 protein quality control for misfolded or incompletely synthesized proteins]
        rationale: The PN ribosome-associated quality-control group covers surveillance and disposal of stalled or defective nascent-chain translation products. GO lacks a dedicated ribosome-associated QC term in the local cache, so the broader protein-quality-control process is the best supported target.
    - [class] Translation|Cytosolic translation
        status=context_only scope=too_broad_to_propagate GO=[GO:0002181 cytoplasmic translation]
        rationale: The PN class Cytosolic translation is centered on the cytoplasmic translation apparatus and process, but it also houses supporting machinery such as ribosome biogenesis factors. The GO process term is a useful high-level label for the class, but propagating it to all members would over-annotate genes whose PN placement is through assembly or maturation context rather than core cytoplasmic translation.
    - [branch] Translation
        status=context_only scope=too_broad_to_propagate GO=[GO:0006412 translation]
        rationale: The PN Translation branch is organized around the translation apparatus and immediately associated cotranslational quality-control systems. GO translation is the closest high-level process label, but the PN branch also contains adjacent machinery such as ribosome biogenesis and nascent-chain handling. Keeping this relationship is useful for interpretation, but it is too broad to project safely onto every member.

## PN row 3: Autophagy-Lysosome Pathway | Autophagophore initiation and elongation | ATG8 homolog processing, upstream | Preparation of ATG8 homologs for lipidation | Modulation of ATG5-ATG12-ATG16 complex activity
- UniProt: P63244
- In branches: TR, ALP
- Notes: RACK1 interacts with ATG5. Importantly, classical autophagy inducers (starvation or mammalian target of rapamycin blockage) stimulated RACK1-ATG5 interaction. Knockdown of RACK1 or prevention of its binding to ATG5 using mutagenesis blocked autophagy activation. RACK1 may recruit other proteins to the phagophore membrane.
- PN references (titles):
    - RACK1 Is an Interaction Partner of ATG5 and a Novel Regulator of Autophagy - ScienceDirect
- PN-node mapping records (path + ancestors):
    - [subtype] Autophagy-Lysosome Pathway|Autophagophore initiation and elongation|ATG8 homolog processing, upstream|Preparation of ATG8 homologs for lipidation|Modulation of ATG5-ATG12-ATG16 complex activity
        status=no_mapping scope= GO=[]
        rationale: This PN leaf is a regulator bucket rather than a shared gene function or shared process participation class. The current gene set is too heterogeneous for a single defensible GO target.
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

## Projected GO annotations (4)
- GO:0042254 ribosome biogenesis | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Translation|Cytosolic translation|Ribosome biogenesis factor
- GO:0030688 preribosome, small subunit precursor | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Translation|Cytosolic translation|Ribosome biogenesis factor|pre-40S complex
- GO:0006515 protein quality control for misfolded or incompletely synthesized proteins | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Translation|Cytosolic translation|Ribosome-associated QC
- GO:0072344 rescue of stalled cytosolic ribosome | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Translation|Cytosolic translation|Ribosome-associated QC|Ribosomal rescue

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
