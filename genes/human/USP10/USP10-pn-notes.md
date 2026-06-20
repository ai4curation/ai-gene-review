# USP10 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q14694
- AIGR review status: COMPLETE
- Review batch: proteostasis-pr-1217 (PR 1217)
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/USP10/USP10-ai-review.yaml](USP10-ai-review.yaml)
- AIGR review HTML: present - [genes/human/USP10/USP10-ai-review.html](USP10-ai-review.html)
- Gene notes: present - [genes/human/USP10/USP10-notes.md](USP10-notes.md)
- GOA TSV: present - [genes/human/USP10/USP10-goa.tsv](USP10-goa.tsv)
- UniProt record: present - [genes/human/USP10/USP10-uniprot.txt](USP10-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/USP10.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/USP10.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/USP10.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/USP10.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: USP10 encodes a ubiquitin-specific cysteine deubiquitinase that removes ubiquitin from selected substrates including p53/TP53, CFTR, Beclin1-complex components, LC3B, and 40S ribosomal proteins. Its direct roles in protein homeostasis include protein deubiquitination, rescue of ubiquitinated stalled 40S ribosomal subunits, and regulation of autophagy/stress-granule signaling through LC3B, Beclin1, and G3BP contexts.
- Existing/core annotation action counts: ACCEPT: 45; KEEP_AS_NON_CORE: 16; MARK_AS_OVER_ANNOTATED: 28; MODIFY: 1

## PN Consistency Summary

- **Consistency:** Consistent across all three branches. Notes, review, and PN agree on a core cysteine-type DUB (GO:0004843) acting on p53, CFTR, LC3B, and 40S ribosomal proteins, with RQC and ATG8 as direct substrate contexts. Review accepts the RQC story strongly (GO:0072344 rescue of stalled cytosolic ribosome, GO:0035520 monoubiquitinated protein deubiquitination, GO:0022626 cytosolic ribosome) and keeps autophagy/LC3B as KEEP_AS_NON_CORE.
- **PN story / NEW pressure:** The RQC group's GO:0006515 (verified real, non-obsolete) is new_to_goa and the dossier rationale notes GO lacks a dedicated ribosome-associated-QC term. The review instead captures RQC via the more specific, already-curatable GO:0072344 + GO:0035520 (both in GOA, IDA-supported). So the function is captured at finer grain than the PN projection; GO:0006515 would be a defensible but broader add. Verdict: already captured (more specifically) — GO:0006515 is broader than the review's RQC terms.
- **Evidence alignment:** PN RQC row has no titled reference; ALP cites PMID:33577797 (USP10 deubiquitinates LC3B) — present in review (non-core autophagy). UPS row cites "19734957/rev". Review's RQC evidence: PMID:31981475, 34348161, 34469731 (40S/iRQC) — richer than PN. Strong overlap on the LC3B paper.
- **Verdict:** Consistent; RQC and ATG8 stories captured (RQC more specifically than the PN's GO:0006515, which is broader). No NEW term needed.

## Full Consistency Review

- **UniProt:** Q14694 · **batch:** proteostasis-pr-1217 · **review status:** COMPLETE
- **PN placement:** TR `Cytosolic translation|Ribosome-associated QC|Deubiquitination`; ALP `…|ATG8 homolog processing, direct|Deubiquitination of ATG8 homologs`; UPS `DUBs and UBL demodifiers|USP|Ataxin-2, C term|other` ; **PN-node mapping:** RQC type→GO:0101005 deubiquitinase activity; RQC group→GO:0006515 protein QC for misfolded/incompletely synthesized proteins (new_to_goa); ALP type→GO:0016579 protein deubiquitination (already_in_goa); UPS group→GO:0101005.
- **Consistency:** Consistent across all three branches. Notes, review, and PN agree on a core cysteine-type DUB (GO:0004843) acting on p53, CFTR, LC3B, and 40S ribosomal proteins, with RQC and ATG8 as direct substrate contexts. Review accepts the RQC story strongly (GO:0072344 rescue of stalled cytosolic ribosome, GO:0035520 monoubiquitinated protein deubiquitination, GO:0022626 cytosolic ribosome) and keeps autophagy/LC3B as KEEP_AS_NON_CORE.
- **PN story / NEW pressure:** The RQC group's GO:0006515 (verified real, non-obsolete) is new_to_goa and the dossier rationale notes GO lacks a dedicated ribosome-associated-QC term. The review instead captures RQC via the more specific, already-curatable GO:0072344 + GO:0035520 (both in GOA, IDA-supported). So the function is captured at finer grain than the PN projection; GO:0006515 would be a defensible but broader add. Verdict: already captured (more specifically) — GO:0006515 is broader than the review's RQC terms.
- **Mapping strategy:** USP10 supports the RQC node well. The PN-projected GO:0006515 is broader than the review's GO:0072344/GO:0035520 — a precedent-style "broader than review" case (cf. TOMM20/HSPA8). MF granularity note: PN projects GO:0101005 deubiquitinase activity while GOA/review use child GO:0004843; entailed_by_goa_closure is correct, no conflict. ALP→GO:0016579 matches.
- **Evidence alignment:** PN RQC row has no titled reference; ALP cites PMID:33577797 (USP10 deubiquitinates LC3B) — present in review (non-core autophagy). UPS row cites "19734957/rev". Review's RQC evidence: PMID:31981475, 34348161, 34469731 (40S/iRQC) — richer than PN. Strong overlap on the LC3B paper.
- **Verdict:** Consistent; RQC and ATG8 stories captured (RQC more specifically than the PN's GO:0006515, which is broader). No NEW term needed.

## PN Dossier Context

- review_batch: proteostasis-pr-1217
- review_yaml: genes/human/USP10/USP10-ai-review.yaml
- PN workbook rows: 3

## PN row 1: Translation | Cytosolic translation | Ribosome-associated QC | Deubiquitination
- UniProt: Q14694
- In branches: TR, ALP, UPS
- PN-node mapping records (path + ancestors):
    - [type] Translation|Cytosolic translation|Ribosome-associated QC|Deubiquitination
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0101005 deubiquitinase activity]
        rationale: This PN RQC type denotes deubiquitinases acting in ribosome-associated quality control. Deubiquitinase activity is the shared molecular-function target.
    - [group] Translation|Cytosolic translation|Ribosome-associated QC
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0006515 protein quality control for misfolded or incompletely synthesized proteins]
        rationale: The PN ribosome-associated quality-control group covers surveillance and disposal of stalled or defective nascent-chain translation products. GO lacks a dedicated ribosome-associated QC term in the local cache, so the broader protein-quality-control process is the best supported target.
    - [class] Translation|Cytosolic translation
        status=context_only scope=too_broad_to_propagate GO=[GO:0002181 cytoplasmic translation]
        rationale: The PN class Cytosolic translation is centered on the cytoplasmic translation apparatus and process, but it also houses supporting machinery such as ribosome biogenesis factors. The GO process term is a useful high-level label for the class, but propagating it to all members would over-annotate genes whose PN placement is through assembly or maturation context rather than core cytoplasmic translation.
    - [branch] Translation
        status=context_only scope=too_broad_to_propagate GO=[GO:0006412 translation]
        rationale: The PN Translation branch is organized around the translation apparatus and immediately associated cotranslational quality-control systems. GO translation is the closest high-level process label, but the PN branch also contains adjacent machinery such as ribosome biogenesis and nascent-chain handling. Keeping this relationship is useful for interpretation, but it is too broad to project safely onto every member.

## PN row 2: Autophagy-Lysosome Pathway | Autophagophore initiation and elongation | ATG8 homolog processing, direct | Deubiquitination of ATG8 homologs
- UniProt: Q14694
- In branches: TR, ALP, UPS
- Notes: Deubiquitinase that removes ubiquitin from LC3, thereby increasing autophagy.
- PN references (titles):
    - The ubiquitin isopeptidase USP10 deubiquitinates LC3B to increase LC3B levels and autophagic activity - ScienceDirect
- PN-node mapping records (path + ancestors):
    - [type] Autophagy-Lysosome Pathway|Autophagophore initiation and elongation|ATG8 homolog processing, direct|Deubiquitination of ATG8 homologs
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0016579 protein deubiquitination]
        rationale: This PN type denotes deubiquitination of ATG8-family proteins within the autophagy pathway. GO does not currently provide an ATG8-specific deubiquitination term, so the defensible target is the broader parent process protein deubiquitination.
    - [group] Autophagy-Lysosome Pathway|Autophagophore initiation and elongation|ATG8 homolog processing, direct
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN taxonomy container. The descendants mix components, regulators, context labels, and mechanistic leaves, so propagation should come only from narrower curated nodes.
    - [class] Autophagy-Lysosome Pathway|Autophagophore initiation and elongation
        status=context_only scope=too_broad_to_propagate GO=[GO:0016236 macroautophagy]
        rationale: This class is a real macroautophagy context, but its descendants include core factors, component buckets, upstream modulators, localization roles, and residual categories. Projecting generic macroautophagy from this ancestor creates TRAPP-like overpropagation, so candidate GO annotations must come from narrower curated nodes.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## PN row 3: Ubiquitin Proteasome System | DUBs and UBL demodifiers | USP | Ataxin-2, C term | other
- UniProt: Q14694
- In branches: TR, ALP, UPS
- Signature domains: IPR028889
- Auxiliary domains: IPR009818
- PN references (titles):
    - 19734957 / rev
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|DUBs and UBL demodifiers|USP|Ataxin-2, C term|other
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower active DUB family/domain subdivision already covered by the curated parent DUB-family mapping. No additional direct GO mapping is needed at this node.
    - [type] Ubiquitin Proteasome System|DUBs and UBL demodifiers|USP|Ataxin-2, C term
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower active DUB family/domain subdivision already covered by the curated parent DUB-family mapping. No additional direct GO mapping is needed at this node.
    - [group] Ubiquitin Proteasome System|DUBs and UBL demodifiers|USP
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0101005 deubiquitinase activity]
        rationale: This PN group is an active deubiquitinase family bucket. The shared molecular-function assertion is deubiquitinase activity.
    - [class] Ubiquitin Proteasome System|DUBs and UBL demodifiers
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a UPS taxonomy container. Its descendants mix catalytic roles, complex membership, binding domains, regulators, adaptors, and substrate-context labels, so a single propagating GO assertion would overstate the shared biology.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## Projected GO annotations (4)
- GO:0006515 protein quality control for misfolded or incompletely synthesized proteins | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Translation|Cytosolic translation|Ribosome-associated QC
- GO:0101005 deubiquitinase activity | scope=ok_for_propagation_to_go | goa_status=entailed_by_goa_closure | from=Translation|Cytosolic translation|Ribosome-associated QC|Deubiquitination
- GO:0016579 protein deubiquitination | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Autophagy-Lysosome Pathway|Autophagophore initiation and elongation|ATG8 homolog processing, direct|Deubiquitination of ATG8 homologs
- GO:0101005 deubiquitinase activity | scope=ok_for_propagation_to_go | goa_status=entailed_by_goa_closure | from=Ubiquitin Proteasome System|DUBs and UBL demodifiers|USP

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
