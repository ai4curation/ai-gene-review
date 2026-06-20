# UFC1 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9Y3C8
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07c
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/UFC1/UFC1-ai-review.yaml](UFC1-ai-review.yaml)
- AIGR review HTML: present - [genes/human/UFC1/UFC1-ai-review.html](UFC1-ai-review.html)
- Gene notes: present - [genes/human/UFC1/UFC1-notes.md](UFC1-notes.md)
- GOA TSV: present - [genes/human/UFC1/UFC1-goa.tsv](UFC1-goa.tsv)
- UniProt record: present - [genes/human/UFC1/UFC1-uniprot.txt](UFC1-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/UFC1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/UFC1.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/UFC1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/UFC1.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: UFC1 (Ubiquitin-fold modifier-conjugating enzyme 1) is the E2-like conjugating enzyme of the UFM1 (ufmylation) cascade, a ubiquitin-like protein-conjugation system that proceeds through E1 (UBA5), E2 (UFC1) and E3 (UFL1/DDRGK1/CDK5RAP3) enzymes. UFC1 accepts the activated ubiquitin-fold modifier UFM1 from the E1 enzyme UBA5 and forms a thioester-linked intermediate at its catalytic cysteine (Cys-116), then, in concert with the UFL1-DDRGK1 E3 ligase, transfers UFM1 onto substrate lysines. The principal physiological substrate is the 60S ribosomal protein RPL26/uL24 on endoplasmic-reticulum-bound ribosomes, where ufmylation promotes recycling of post-termination or stalled 60S subunits from SEC61 translocons and supports ribosome-associated quality control. UFMylation more broadly participates in the response to ER stress, reticulophagy (ER-phagy), DNA-damage signaling and innate-immune/interferon signaling. UFC1 is a small (167 aa) cytosolic protein structurally related to ubiquitin-conjugating (E2) enzymes; biallelic loss-of-function variants cause a neurodevelopmental disorder with spasticity and poor growth, underscoring an essential role of ufmylation in brain development.
- Existing/core annotation action counts: ACCEPT: 18; KEEP_AS_NON_CORE: 18; MARK_AS_OVER_ANNOTATED: 1

## PN Consistency Summary

- **Consistency:** Strong. Notes/review/PN agree UFC1 is the UFM1 E2 (accepts UFM1 from UBA5, Cys-116 thioester, works with UFL1/DDRGK1). Review ACCEPTs GO:0061657 (UFM1 conjugating enzyme activity, IDA x4), GO:0071568 (transferase, IBA), GO:0071569; ERphagy/ER-stress KEEP_AS_NON_CORE. extracellular exosome MARK_AS_OVER_ANNOTATED. No contradictions.
- **PN story / NEW pressure:** All PN assertions captured in GOA/review. GO:0006515 (verified) projected new_to_goa via RQC group is broad; UFC1's RQC role is via ufmylation (annotated). Conclusion: **already captured**; GO:0006515 over-reaches as a direct UFC1 term.
- **Evidence alignment:** PN E2 row cites "19452197 / rev" (not in review); review uses cascade/structure PMIDs (15071506, 36121123, 38383789, 37036982 — the last three also in GOA as IDA/IMP for GO:0061657). PN ERphagy row cites the ER-phagy screen (PMID:32160526, in notes). Good thematic overlap; PN's family-review PMID is non-overlapping by design.
- **Verdict:** Consistent and complete; PN E2/UFMylation/ERphagy story fully captured by specific GO:0061657 + GO:0071569. PN's broad GO:0019787 is an ancestor only; GO:0006515 not warranted as a direct add.

## Full Consistency Review

- **UniProt:** Q9Y3C8 · **batch:** proteostasis-batch-2026-06-07c · **review status:** complete (core MF GO:0061657; proposed_new_terms: [])
- **PN placement:** `Translation|Cytosolic translation|Ribosome-associated QC|UFMylation`; `ALP|...|ERphagy|UFMylation of ER proteins`; `UPS|E2 conjugating enzymes|UFMylation|no family designation` ; **PN-node mapping:** UFMylation type→GO:0071569; ERphagy→GO:0061709; E2 group→GO:0019787 (broad UBL transferase activity, entailed_by_goa_closure); RQC group→GO:0006515.
- **Consistency:** Strong. Notes/review/PN agree UFC1 is the UFM1 E2 (accepts UFM1 from UBA5, Cys-116 thioester, works with UFL1/DDRGK1). Review ACCEPTs GO:0061657 (UFM1 conjugating enzyme activity, IDA x4), GO:0071568 (transferase, IBA), GO:0071569; ERphagy/ER-stress KEEP_AS_NON_CORE. extracellular exosome MARK_AS_OVER_ANNOTATED. No contradictions.
- **PN story / NEW pressure:** All PN assertions captured in GOA/review. GO:0006515 (verified) projected new_to_goa via RQC group is broad; UFC1's RQC role is via ufmylation (annotated). Conclusion: **already captured**; GO:0006515 over-reaches as a direct UFC1 term.
- **Mapping strategy:** Specific-vs-broad MF: PN E2-group projects broad GO:0019787 (ubiquitin-like protein transferase activity), explicitly entailed_by_goa_closure of the gene-level specific GO:0061657 — so PN's term is strictly an ancestor (TOMM20/HSPA8 "broader" precedent: keep as context, do not propagate over the specific). Review's GO:0061657 (E2) is the correct gene-level MF. UFC1 does not change the node.
- **Evidence alignment:** PN E2 row cites "19452197 / rev" (not in review); review uses cascade/structure PMIDs (15071506, 36121123, 38383789, 37036982 — the last three also in GOA as IDA/IMP for GO:0061657). PN ERphagy row cites the ER-phagy screen (PMID:32160526, in notes). Good thematic overlap; PN's family-review PMID is non-overlapping by design.
- **Verdict:** Consistent and complete; PN E2/UFMylation/ERphagy story fully captured by specific GO:0061657 + GO:0071569. PN's broad GO:0019787 is an ancestor only; GO:0006515 not warranted as a direct add.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07c
- review_yaml: genes/human/UFC1/UFC1-ai-review.yaml
- PN workbook rows: 3

## PN row 1: Translation | Cytosolic translation | Ribosome-associated QC | UFMylation
- UniProt: Q9Y3C8
- In branches: TR, ALP, UPS
- PN-node mapping records (path + ancestors):
    - [type] Translation|Cytosolic translation|Ribosome-associated QC|UFMylation
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0071569 protein ufmylation]
        rationale: This PN RQC type denotes UFM1 conjugation in ribosome quality control. Protein ufmylation is the shared process target.
    - [group] Translation|Cytosolic translation|Ribosome-associated QC
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0006515 protein quality control for misfolded or incompletely synthesized proteins]
        rationale: The PN ribosome-associated quality-control group covers surveillance and disposal of stalled or defective nascent-chain translation products. GO lacks a dedicated ribosome-associated QC term in the local cache, so the broader protein-quality-control process is the best supported target.
    - [class] Translation|Cytosolic translation
        status=context_only scope=too_broad_to_propagate GO=[GO:0002181 cytoplasmic translation]
        rationale: The PN class Cytosolic translation is centered on the cytoplasmic translation apparatus and process, but it also houses supporting machinery such as ribosome biogenesis factors. The GO process term is a useful high-level label for the class, but propagating it to all members would over-annotate genes whose PN placement is through assembly or maturation context rather than core cytoplasmic translation.
    - [branch] Translation
        status=context_only scope=too_broad_to_propagate GO=[GO:0006412 translation]
        rationale: The PN Translation branch is organized around the translation apparatus and immediately associated cotranslational quality-control systems. GO translation is the closest high-level process label, but the PN branch also contains adjacent machinery such as ribosome biogenesis and nascent-chain handling. Keeping this relationship is useful for interpretation, but it is too broad to project safely onto every member.

## PN row 2: Autophagy-Lysosome Pathway | Autophagy substrate selection | Marking substrates for selective autophagy | ERphagy | UFMylation of ER proteins
- UniProt: Q9Y3C8
- In branches: TR, ALP, UPS
- Notes: E2-type protein that catalyzes UFMylation. Knockdown of UFL1 decreased DDRGK1 levels and inhibits ER-phagy.UFL1 UFMylates RPN1 and RPL26 to target ER sheets for degradation.
- PN references (titles):
    - A Genome-wide ER-phagy Screen Highlights Key Roles of Mitochondrial Metabolism and ER-Resident UFMylation - ScienceDirect
- PN-node mapping records (path + ancestors):
    - [subtype] Autophagy-Lysosome Pathway|Autophagy substrate selection|Marking substrates for selective autophagy|ERphagy|UFMylation of ER proteins
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0061709 reticulophagy]
        rationale: This PN subtype captures a specific ER-cargo marking mechanism used in ERphagy. Because GO uses reticulophagy for ER autophagy, this subtype can propagate to reticulophagy.
    - [type] Autophagy-Lysosome Pathway|Autophagy substrate selection|Marking substrates for selective autophagy|ERphagy
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0061709 reticulophagy]
        rationale: The PN ERphagy marking category captures factors that mark ER cargo for selective autophagic turnover. GO uses reticulophagy for this pathway, so propagation to reticulophagy is appropriate.
    - [group] Autophagy-Lysosome Pathway|Autophagy substrate selection|Marking substrates for selective autophagy
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN taxonomy container. The descendants mix components, regulators, context labels, and mechanistic leaves, so propagation should come only from narrower curated nodes.
    - [class] Autophagy-Lysosome Pathway|Autophagy substrate selection
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad substrate-selection container. GO has useful targets for specific receptor, cargo-adaptor, and selective-autophagy leaves, but this class mixes marking, recognition, receptor regulation, and unknown roles and should not propagate as one term.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## PN row 3: Ubiquitin Proteasome System | E2 conjugating enzymes | UFMylation | no family designation
- UniProt: Q9Y3C8
- In branches: TR, ALP, UPS
- Signature domains: IPR014806
- Auxiliary domains: (none)
- PN references (titles):
    - 19452197 / rev
- PN-node mapping records (path + ancestors):
    - [type] Ubiquitin Proteasome System|E2 conjugating enzymes|UFMylation|no family designation
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower E2 family or architecture subdivision already covered by the curated parent E2 mapping. No additional direct GO mapping is needed at this node.
    - [group] Ubiquitin Proteasome System|E2 conjugating enzymes|UFMylation
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0019787 ubiquitin-like protein transferase activity]
        rationale: This PN group is a UBL-conjugating E2 bucket. The safest shared molecular-function target is ubiquitin-like protein transferase activity.
    - [class] Ubiquitin Proteasome System|E2 conjugating enzymes
        status=context_only scope=too_broad_to_propagate GO=[GO:0019787 ubiquitin-like protein transferase activity]
        rationale: This class is a real E2/UBL transferase context, but it includes ubiquitin, SUMO, NEDD8, UFMylation, ATGylation, dual-use, and inactive buckets. Propagation is restricted to narrower curated children.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## Projected GO annotations (5)
- GO:0006515 protein quality control for misfolded or incompletely synthesized proteins | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Translation|Cytosolic translation|Ribosome-associated QC
- GO:0071569 protein ufmylation | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Translation|Cytosolic translation|Ribosome-associated QC|UFMylation
- GO:0061709 reticulophagy | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Autophagy-Lysosome Pathway|Autophagy substrate selection|Marking substrates for selective autophagy|ERphagy
- GO:0061709 reticulophagy | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Autophagy-Lysosome Pathway|Autophagy substrate selection|Marking substrates for selective autophagy|ERphagy|UFMylation of ER proteins
- GO:0019787 ubiquitin-like protein transferase activity | scope=ok_for_propagation_to_go | goa_status=entailed_by_goa_closure | from=Ubiquitin Proteasome System|E2 conjugating enzymes|UFMylation

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
