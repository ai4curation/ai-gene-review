# RNF25 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q96BH1
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07c
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/RNF25/RNF25-ai-review.yaml](RNF25-ai-review.yaml)
- AIGR review HTML: present - [genes/human/RNF25/RNF25-ai-review.html](RNF25-ai-review.html)
- Gene notes: present - [genes/human/RNF25/RNF25-notes.md](RNF25-notes.md)
- GOA TSV: present - [genes/human/RNF25/RNF25-goa.tsv](RNF25-goa.tsv)
- UniProt record: present - [genes/human/RNF25/RNF25-uniprot.txt](RNF25-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/RNF25.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/RNF25.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/RNF25.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/RNF25.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: RNF25 (RING finger protein 25, originally identified as AO7) is a cytoplasmic RING-H2 E3 ubiquitin-protein ligase that, with an N-terminal RWD domain for E2 recognition, functions in ribosome-associated quality control. It is a core component of the RNF14-RNF25 translation quality control pathway that operates when ribosomes stall and collide during translation. RNF25 catalyzes ubiquitination of the ribosomal protein RPS27A/eS31 in response to ribosome collisions, providing a signal that activates the partner ligase RNF14, and it ubiquitinates additional ribosomal proteins and stalled release factor ETF1/eRF1, marking translation factors on stalled ribosomes for degradation. RNF25 also assembles atypical K6-linked ubiquitin chains that flag formaldehyde-induced RNA-protein crosslinks for translation-coupled resolution. It works with the E2 enzyme UBE2D2 (UbcH5B). Independently of the stalled-ribosome response, RNF25 was originally characterized as a regulator that supports NF-kappaB (RELA/p65)-mediated transcription and can target substrates such as NKD2 for degradation.
- Existing/core annotation action counts: ACCEPT: 25; KEEP_AS_NON_CORE: 11

## PN Consistency Summary

- **Consistency:** Excellent. Deep research, review and PN concur: RING-H2 E3 (RWD for E2 recognition; works with UBE2D2/UbcH5B), the partner ligase of RNF14 in the RNF14-RNF25 pathway — ubiquitinates RPS27A/eS31 on collided ribosomes to activate RNF14, ubiquitinates eRF1/ribosomal proteins, and assembles K6 chains on formaldehyde RNA-protein crosslinks (GO:0160127); legacy AO7/NF-kB(RELA) role kept non-core. PN correctly tags the **catalytic ligase MF**. No contradictions.
- **PN story / NEW pressure:** GO:0061630 (verified real) and GO:0016567 already in GOA + review (IDA PMID:36638793, 26475854, 37651229, 37951215). GO:0006515 (verified real) is new_to_goa; RNF25 genuinely drives stalled-ribosome QC so it is a defensible higher-level ADD, but broader than the review's precise set (GO:0072344, GO:0085020 K6, GO:0160127, GO:0006511). Conclude: ligase MF + ubiquitination already captured; GO:0006515 defensible-but-broader ADD.
- **Evidence alignment:** PN RING row cites "PMID 19489725 / rev" — NOT in the review references. Review RQC/ligase evidence (PMID:36638793, 26475854, 37651229, 37951215/16, 27863242, 12748188) is HIGH/VERIFIED and far richer. Divergence: the single PN-cited RING PMID is uncited in the review (likely an older RING/E3 review; low impact, ligase MF independently well-supported).
- **Verdict:** Fully consistent; PN ligase MF (GO:0061630) and ubiquitination already captured, GO:0006515 a defensible-but-broader ADD. No YAML change needed.

## Full Consistency Review

- **UniProt:** Q96BH1 · **batch:** proteostasis-batch-2026-06-07c · **review status:** COMPLETE (thorough; core RING ligase + RQC, AO7/NF-kB as non-core)
- **PN placement:** 3 rows — `Translation|Cytosolic translation|Ribosome-associated QC|ubiquitination of eEF1A on stalled ribosomes`; `UPS|E3 ubiquitin and UBL ligases|RING|ubiquitin binding domain|RWD`; `UPS|Ubiquitin and UBL binding|E3 ligase|RING / with UBD|RWD`. **PN-node mapping:** RQC-type→mapped GO:0016567 protein ubiquitination (already_in_goa); RQC-group→GO:0006515 (new); RING-group→mapped GO:0061630 ubiquitin protein ligase activity (already_in_goa); UBL-binding E3-group→GO:0061630 (already_in_goa); RING subtype/type no_mapping. Projected: GO:0006515 (new), GO:0016567, GO:0061630×2 (all in GOA).
- **Consistency:** Excellent. Deep research, review and PN concur: RING-H2 E3 (RWD for E2 recognition; works with UBE2D2/UbcH5B), the partner ligase of RNF14 in the RNF14-RNF25 pathway — ubiquitinates RPS27A/eS31 on collided ribosomes to activate RNF14, ubiquitinates eRF1/ribosomal proteins, and assembles K6 chains on formaldehyde RNA-protein crosslinks (GO:0160127); legacy AO7/NF-kB(RELA) role kept non-core. PN correctly tags the **catalytic ligase MF**. No contradictions.
- **PN story / NEW pressure:** GO:0061630 (verified real) and GO:0016567 already in GOA + review (IDA PMID:36638793, 26475854, 37651229, 37951215). GO:0006515 (verified real) is new_to_goa; RNF25 genuinely drives stalled-ribosome QC so it is a defensible higher-level ADD, but broader than the review's precise set (GO:0072344, GO:0085020 K6, GO:0160127, GO:0006511). Conclude: ligase MF + ubiquitination already captured; GO:0006515 defensible-but-broader ADD.
- **Mapping strategy:** Correctly resolves RNF25 as catalytic RING ligase (GO:0061630), distinct from a UBD reader; group-level mapping appropriate, subtype/type no_mapping avoids double-counting. RQC-group→GO:0006515 broader than terms already present. No node change warranted.
- **Evidence alignment:** PN RING row cites "PMID 19489725 / rev" — NOT in the review references. Review RQC/ligase evidence (PMID:36638793, 26475854, 37651229, 37951215/16, 27863242, 12748188) is HIGH/VERIFIED and far richer. Divergence: the single PN-cited RING PMID is uncited in the review (likely an older RING/E3 review; low impact, ligase MF independently well-supported).
- **Verdict:** Fully consistent; PN ligase MF (GO:0061630) and ubiquitination already captured, GO:0006515 a defensible-but-broader ADD. No YAML change needed.
- **Recommended edits:** none required. [REF] (optional) check PN-cited PMID:19489725 (RING row) — absent from review; verify whether it adds RNF25-specific support or is a family review. [MAP] GO:0006515 broader than the exact RQC terms already annotated.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07c
- review_yaml: genes/human/RNF25/RNF25-ai-review.yaml
- PN workbook rows: 3

## PN row 1: Translation | Cytosolic translation | Ribosome-associated QC | ubiquitination of eEF1A on stalled ribosomes
- UniProt: Q96BH1
- In branches: TR, UPS
- PN-node mapping records (path + ancestors):
    - [type] Translation|Cytosolic translation|Ribosome-associated QC|ubiquitination of eEF1A on stalled ribosomes
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0016567 protein ubiquitination]
        rationale: This PN RQC type is a specific ubiquitination bucket for eEF1A on stalled ribosomes. Protein ubiquitination is the shared process target.
    - [group] Translation|Cytosolic translation|Ribosome-associated QC
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0006515 protein quality control for misfolded or incompletely synthesized proteins]
        rationale: The PN ribosome-associated quality-control group covers surveillance and disposal of stalled or defective nascent-chain translation products. GO lacks a dedicated ribosome-associated QC term in the local cache, so the broader protein-quality-control process is the best supported target.
    - [class] Translation|Cytosolic translation
        status=context_only scope=too_broad_to_propagate GO=[GO:0002181 cytoplasmic translation]
        rationale: The PN class Cytosolic translation is centered on the cytoplasmic translation apparatus and process, but it also houses supporting machinery such as ribosome biogenesis factors. The GO process term is a useful high-level label for the class, but propagating it to all members would over-annotate genes whose PN placement is through assembly or maturation context rather than core cytoplasmic translation.
    - [branch] Translation
        status=context_only scope=too_broad_to_propagate GO=[GO:0006412 translation]
        rationale: The PN Translation branch is organized around the translation apparatus and immediately associated cotranslational quality-control systems. GO translation is the closest high-level process label, but the PN branch also contains adjacent machinery such as ribosome biogenesis and nascent-chain handling. Keeping this relationship is useful for interpretation, but it is too broad to project safely onto every member.

## PN row 2: Ubiquitin Proteasome System | E3 ubiquitin and UBL ligases | RING | ubiquitin binding domain | RWD
- UniProt: Q96BH1
- In branches: TR, UPS
- Signature domains: IPR001841
- Auxiliary domains: IPR006575
- PN references (titles):
    - 19489725 / rev
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|RING|ubiquitin binding domain|RWD
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower E3-ligase architecture, component, or domain subdivision already covered by the curated parent E3 mapping. No additional direct GO mapping is needed at this node.
    - [type] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|RING|ubiquitin binding domain
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower E3-ligase architecture, component, or domain subdivision already covered by the curated parent E3 mapping. No additional direct GO mapping is needed at this node.
    - [group] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|RING
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0061630 ubiquitin protein ligase activity]
        rationale: This PN group is a catalytic ubiquitin E3 ligase bucket. The shared GO molecular-function target is ubiquitin protein ligase activity.
    - [class] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases
        status=context_only scope=too_broad_to_propagate GO=[GO:0061630 ubiquitin protein ligase activity]
        rationale: This class is a genuine E3-ligase context, but its descendants include catalytic ligases, cullin scaffolds, substrate receptors, adaptors, cofactors, regulators, and UBL modifier systems. A class-level propagation would over-annotate.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## PN row 3: Ubiquitin Proteasome System | Ubiquitin and UBL binding | E3 ligase | RING / with UBD | RWD
- UniProt: Q96BH1
- In branches: TR, UPS
- Signature domains: IPR006575
- Auxiliary domains: IPR001841
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|Ubiquitin and UBL binding|E3 ligase|RING / with UBD|RWD
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower enzyme-family, domain, or architecture subdivision already covered by a curated parent enzyme mapping. No additional direct GO mapping is needed at this node.
    - [type] Ubiquitin Proteasome System|Ubiquitin and UBL binding|E3 ligase|RING / with UBD
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower enzyme-family, domain, or architecture subdivision already covered by a curated parent enzyme mapping. No additional direct GO mapping is needed at this node.
    - [group] Ubiquitin Proteasome System|Ubiquitin and UBL binding|E3 ligase
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0061630 ubiquitin protein ligase activity]
        rationale: This PN group captures ubiquitin/UBL-binding factors that are E3 ligases. The shared molecular-function target is ubiquitin protein ligase activity.
    - [class] Ubiquitin Proteasome System|Ubiquitin and UBL binding
        status=context_only scope=too_broad_to_propagate GO=[GO:0140036 ubiquitin-modified protein reader activity]
        rationale: This class records ubiquitin/UBL-reader context, but the subtree mixes ubiquitin, SUMO, UBL-domain, domain-architecture, catalytic, signaling, trafficking, and nucleic-acid process buckets. It is useful context, not a safe direct propagation.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## Projected GO annotations (4)
- GO:0006515 protein quality control for misfolded or incompletely synthesized proteins | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Translation|Cytosolic translation|Ribosome-associated QC
- GO:0016567 protein ubiquitination | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Translation|Cytosolic translation|Ribosome-associated QC|ubiquitination of eEF1A on stalled ribosomes
- GO:0061630 ubiquitin protein ligase activity | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|RING
- GO:0061630 ubiquitin protein ligase activity | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Ubiquitin Proteasome System|Ubiquitin and UBL binding|E3 ligase

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
