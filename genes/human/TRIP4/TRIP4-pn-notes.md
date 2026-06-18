# TRIP4 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q15650
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07c
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/TRIP4/TRIP4-ai-review.yaml](TRIP4-ai-review.yaml)
- AIGR review HTML: present - [genes/human/TRIP4/TRIP4-ai-review.html](TRIP4-ai-review.html)
- Gene notes: present - [genes/human/TRIP4/TRIP4-notes.md](TRIP4-notes.md)
- GOA TSV: present - [genes/human/TRIP4/TRIP4-goa.tsv](TRIP4-goa.tsv)
- UniProt record: present - [genes/human/TRIP4/TRIP4-uniprot.txt](TRIP4-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/TRIP4.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/TRIP4.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/TRIP4.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/TRIP4.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: TRIP4 (Activating Signal Cointegrator 1, ASC-1; thyroid receptor-interacting protein 4) is a C4-type zinc-finger protein that functions in two distinct contexts. As a subunit of the ASC-1 / RQC-trigger (RQT) complex (with ASCC1, ASCC2 and the ASCC3 helicase), it acts in ribosome-associated quality control, where the complex recognizes K63-polyubiquitinated collided ribosomes and drives splitting/disassembly of the collided (disome) ribosomes so that the obstructing nascent chain can be targeted for degradation. Separately, TRIP4 acts as a nuclear transcriptional coactivator/cointegrator; through its zinc-finger transactivation domain it binds nuclear receptors (thyroid hormone receptor, estrogen receptor ESR1, androgen receptor), basal transcription factors (TBP, TFIIA), and coactivators (SRC-1/NCOA1, CBP/EP300), and potentiates nuclear-receptor-, SRF-, AP-1- and NF-kappaB-mediated transcription. Its coactivator activity is regulated by UFM1 modification (ufmylation); ligand-bound nuclear receptors displace the UFM1 protease UFSP2 from TRIP4, allowing ufmylation that promotes recruitment of EP300/NCOA1 and assembly of an active coactivator complex. TRIP4 is predominantly nuclear (cytoplasmic under serum deprivation; colocalizes with NEK6 at the centrosome). Biallelic loss-of-function variants in TRIP4 cause severe congenital neuromuscular disease (spinal muscular atrophy with congenital bone fractures, SMABF1; and congenital muscular dystrophy, Davignon-Chauveau type).
- Existing/core annotation action counts: ACCEPT: 39; KEEP_AS_NON_CORE: 8; MARK_AS_OVER_ANNOTATED: 1

## PN Consistency Summary

- **Consistency:** Strong. Notes, review and PN all describe the dual ASC-1/RQT (RQC) + nuclear coactivator roles. Review ACCEPTs GO:0072344 (5x in GOA, IDA/IBA) and the RQT-complex/ribosome-disassembly terms; core_functions name GO:0072344 + GO:0003713. No contradictions. The UPS row maps to no_mapping (correct — taxonomy only).
- **PN story / NEW pressure:** PN's RQC role is already richly captured in GOA/review (GO:0072344, GO:0180022 RQC-trigger complex, GO:0032790 ribosome disassembly, GO:1990116). The PN group-level GO:0006515 (verified real; PQC for misfolded/incompletely synthesized proteins) is projected new_to_goa but is a broad QC umbrella; for TRIP4 the more specific GO:1990116 (already annotated) is the better representation. Conclusion: **already captured**; GO:0006515 over-reaches relative to existing specific terms.
- **Evidence alignment:** PN cites only PMID:36627279 (yeast RQT4 analogy, "/rev"); not in the review YAML, but the review relies on direct human RQT papers (PMID:32579943, 36302773). Divergence is benign — PN row is a family/analogy citation.
- **Verdict:** Consistent; PN RQC story already captured by specific GO terms. GO:0006515 is broader than TRIP4's annotated GO:1990116 — keep as propagation-context only, do not add.

## Full Consistency Review

- **UniProt:** Q15650 · **batch:** proteostasis-batch-2026-06-07c · **review status:** complete (all annotations actioned; 2 core_functions)
- **PN placement:** `Translation|Cytosolic translation|Ribosome-associated QC|Ribosomal rescue` (also a UPS "idiosyncratic Ub binding / other" taxonomy row) ; **PN-node mapping:** type=mapped scope=ok_for_propagation_to_go GO:0072344 (rescue of stalled cytosolic ribosome); group=mapped GO:0006515.
- **Consistency:** Strong. Notes, review and PN all describe the dual ASC-1/RQT (RQC) + nuclear coactivator roles. Review ACCEPTs GO:0072344 (5x in GOA, IDA/IBA) and the RQT-complex/ribosome-disassembly terms; core_functions name GO:0072344 + GO:0003713. No contradictions. The UPS row maps to no_mapping (correct — taxonomy only).
- **PN story / NEW pressure:** PN's RQC role is already richly captured in GOA/review (GO:0072344, GO:0180022 RQC-trigger complex, GO:0032790 ribosome disassembly, GO:1990116). The PN group-level GO:0006515 (verified real; PQC for misfolded/incompletely synthesized proteins) is projected new_to_goa but is a broad QC umbrella; for TRIP4 the more specific GO:1990116 (already annotated) is the better representation. Conclusion: **already captured**; GO:0006515 over-reaches relative to existing specific terms.
- **Mapping strategy:** TRIP4 does not change the node. The "Ribosomal rescue" subtype→GO:0072344 mapping is exact and well supported here; the parent group→GO:0006515 is broader than what TRIP4 (and GO) actually uses (GO:1990116), so it should stay context/propagation-only, not displace the specific terms.
- **Evidence alignment:** PN cites only PMID:36627279 (yeast RQT4 analogy, "/rev"); not in the review YAML, but the review relies on direct human RQT papers (PMID:32579943, 36302773). Divergence is benign — PN row is a family/analogy citation.
- **Verdict:** Consistent; PN RQC story already captured by specific GO terms. GO:0006515 is broader than TRIP4's annotated GO:1990116 — keep as propagation-context only, do not add.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07c
- review_yaml: genes/human/TRIP4/TRIP4-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Translation | Cytosolic translation | Ribosome-associated QC | Ribosomal rescue
- UniProt: Q15650
- In branches: TR, UPS
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

## PN row 2: Ubiquitin Proteasome System | Ubiquitin and UBL binding | translation | ribosome QC & transcriptional activation | idiosyncratic Ub binding / other
- UniProt: Q15650
- In branches: TR, UPS
- Signature domains: by analogy with yeast RQT4 (PMID: 36627279)
- Auxiliary domains: (none)
- PN references (titles):
    - 36627279
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|Ubiquitin and UBL binding|translation|ribosome QC & transcriptional activation|idiosyncratic Ub binding / other
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a family, domain, architecture, or residual subdivision. The label is useful for PN taxonomy navigation but is not itself a GO annotation target; any functional assertion should come from a curated parent role or gene-level evidence.
    - [type] Ubiquitin Proteasome System|Ubiquitin and UBL binding|translation|ribosome QC & transcriptional activation
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a UPS taxonomy container. Its descendants mix catalytic roles, complex membership, binding domains, regulators, adaptors, and substrate-context labels, so a single propagating GO assertion would overstate the shared biology.
    - [group] Ubiquitin Proteasome System|Ubiquitin and UBL binding|translation
        status=context_only scope=too_broad_to_propagate GO=[GO:0006412 translation]
        rationale: This PN group captures ubiquitin/UBL-binding factors assigned to translation-related contexts. The relationship to translation is real, but the group mixes heterogeneous subcontexts including repression, nascent-peptide binding, ribosome maturation, and ribosome-quality- control-adjacent roles.
    - [class] Ubiquitin Proteasome System|Ubiquitin and UBL binding
        status=context_only scope=too_broad_to_propagate GO=[GO:0140036 ubiquitin-modified protein reader activity]
        rationale: This class records ubiquitin/UBL-reader context, but the subtree mixes ubiquitin, SUMO, UBL-domain, domain-architecture, catalytic, signaling, trafficking, and nucleic-acid process buckets. It is useful context, not a safe direct propagation.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## Projected GO annotations (2)
- GO:0006515 protein quality control for misfolded or incompletely synthesized proteins | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Translation|Cytosolic translation|Ribosome-associated QC
- GO:0072344 rescue of stalled cytosolic ribosome | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Translation|Cytosolic translation|Ribosome-associated QC|Ribosomal rescue

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
