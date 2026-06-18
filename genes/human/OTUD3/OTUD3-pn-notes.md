# OTUD3 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q5T2D3
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07c
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/OTUD3/OTUD3-ai-review.yaml](OTUD3-ai-review.yaml)
- AIGR review HTML: present - [genes/human/OTUD3/OTUD3-ai-review.html](OTUD3-ai-review.html)
- Gene notes: present - [genes/human/OTUD3/OTUD3-notes.md](OTUD3-notes.md)
- GOA TSV: present - [genes/human/OTUD3/OTUD3-goa.tsv](OTUD3-goa.tsv)
- UniProt record: present - [genes/human/OTUD3/OTUD3-uniprot.txt](OTUD3-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/OTUD3.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/OTUD3.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/OTUD3.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/OTUD3.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: OTUD3 (OTU domain-containing protein 3) is a cysteine-protease deubiquitinase (DUB, EC 3.4.19.12) of the ovarian tumor (OTU) family. Its catalytic OTU domain (active-site nucleophile Cys76, with His182) hydrolyzes isopeptide bonds of ubiquitin chains with a preference for atypical Lys-6 (K6)- and Lys-11 (K11)-linked polyubiquitin, and it also processes heterotypic (mixed/branched) and other homotypic chains; a C-terminal UBA-like domain does not affect catalysis. OTUD3 acts on specific substrates: it deubiquitinates and stabilizes the tumor suppressor PTEN (suppressing PI3K-AKT signaling and tumorigenesis), stabilizes the nuclear receptor PPARD to regulate glucose and lipid metabolism and oxidative phosphorylation in response to nutritional stress (with glucose/fatty-acid-triggered, CBP/CREBBP-dependent acetylation driving its nuclear translocation), and deubiquitinates KPTN to suppress mTORC1 signaling. In ribosome-associated quality control, OTUD3 acts as a negative regulator by deubiquitinating 40S ribosomal proteins RPS10/eS10 and RPS20/uS10, antagonizing ZNF598-mediated 40S ubiquitination. OTUD3 shuttles between the cytoplasm and the nucleus.
- Existing/core annotation action counts: ACCEPT: 32; KEEP_AS_NON_CORE: 5

## PN Consistency Summary

- **Consistency:** Strong. Deep research, review, and PN all agree OTUD3 is an OTU-family Cys-protease DUB (Cys76) with K6/K11 preference; the RQC role (deubiquitinating 40S eS10/uS10, antagonizing ZNF598; PMID:32011234) is captured in description + IDA annotations. No contradictions. Nuance: review/description frame the RQC role as **negative** regulation (a brake on RQC); PN files OTUD3 as an RQC "Deubiquitination" member, which is correct directionally but the PN-group→GO:0006515 "protein quality control" projection slightly overstates OTUD3's role (it antagonizes, not drives, QC).
- **PN story / NEW pressure:** GO:0101005 deubiquitinase activity (verified real) is entailed by the existing GO:0004843 cysteine-type DUB activity already annotated (IDA/IBA/TAS) — already captured, no NEW pressure on MF. GO:0006515 (verified real) is new_to_goa and absent from review; given OTUD3 antagonizes RQC, a positive "involved_in protein QC" assertion over-reaches. Conclude: MF already captured; process term over-reaches as a propagation.
- **Evidence alignment:** PN cites only PMID:23827681 (OTU linkage-specificity); review has it (HIGH/VERIFIED) plus the full substrate literature (26280536 PTEN, 32011234 RQC, 35675826 PPARD, 38288086 KPTN). Review strictly superset; no divergence.
- **Verdict:** Consistent; PN MF already captured, PN RQC-process projection (GO:0006515) over-reaches because OTUD3 is a negative regulator of RQC. No YAML change needed.

## Full Consistency Review

- **UniProt:** Q5T2D3 · **batch:** proteostasis-batch-2026-06-07c · **review status:** COMPLETE (rich, 40 annotations, all ACCEPT/KEEP_AS_NON_CORE)
- **PN placement:** 3 rows — `Translation|Cytosolic translation|Ribosome-associated QC|Deubiquitination`; `UPS|DUBs and UBL demodifiers|OTU|other`; `UPS|Ubiquitin and UBL binding|DUB|OTU|UBA-like (other)`. **PN-node mapping:** RQC-type→mapped GO:0101005 deubiquitinase activity; RQC-group→mapped GO:0006515 protein QC (new_to_goa); UPS OTU/UBL nodes mostly no_mapping/context_only. Projected: GO:0006515 (new), GO:0101005 (entailed).
- **Consistency:** Strong. Deep research, review, and PN all agree OTUD3 is an OTU-family Cys-protease DUB (Cys76) with K6/K11 preference; the RQC role (deubiquitinating 40S eS10/uS10, antagonizing ZNF598; PMID:32011234) is captured in description + IDA annotations. No contradictions. Nuance: review/description frame the RQC role as **negative** regulation (a brake on RQC); PN files OTUD3 as an RQC "Deubiquitination" member, which is correct directionally but the PN-group→GO:0006515 "protein quality control" projection slightly overstates OTUD3's role (it antagonizes, not drives, QC).
- **PN story / NEW pressure:** GO:0101005 deubiquitinase activity (verified real) is entailed by the existing GO:0004843 cysteine-type DUB activity already annotated (IDA/IBA/TAS) — already captured, no NEW pressure on MF. GO:0006515 (verified real) is new_to_goa and absent from review; given OTUD3 antagonizes RQC, a positive "involved_in protein QC" assertion over-reaches. Conclude: MF already captured; process term over-reaches as a propagation.
- **Mapping strategy:** Does not change the node. RQC-type→GO:0101005 redundant with the review's GO:0004843. The group→GO:0006515 propagation is the only divergence and should NOT be projected to OTUD3 (antagonist).
- **Evidence alignment:** PN cites only PMID:23827681 (OTU linkage-specificity); review has it (HIGH/VERIFIED) plus the full substrate literature (26280536 PTEN, 32011234 RQC, 35675826 PPARD, 38288086 KPTN). Review strictly superset; no divergence.
- **Verdict:** Consistent; PN MF already captured, PN RQC-process projection (GO:0006515) over-reaches because OTUD3 is a negative regulator of RQC. No YAML change needed.
- **Recommended edits:** [MAP] Do not propagate GO:0006515 (protein QC) to OTUD3 from the RQC-group node — OTUD3 antagonizes ZNF598-driven 40S ubiquitination (negative RQC regulator), so an `involved_in protein quality control` assertion mis-states direction; flag as do-not-project.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07c
- review_yaml: genes/human/OTUD3/OTUD3-ai-review.yaml
- PN workbook rows: 3

## PN row 1: Translation | Cytosolic translation | Ribosome-associated QC | Deubiquitination
- UniProt: Q5T2D3
- In branches: TR, UPS
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

## PN row 2: Ubiquitin Proteasome System | DUBs and UBL demodifiers | OTU | other
- UniProt: Q5T2D3
- In branches: TR, UPS
- Signature domains: IPR003323
- Auxiliary domains: (none)
- PN references (titles):
    - 23827681
- PN-node mapping records (path + ancestors):
    - [type] Ubiquitin Proteasome System|DUBs and UBL demodifiers|OTU|other
        status=no_mapping scope= GO=[]
        rationale: Reviewed as an OTU-family subtype. Because the family branch includes inactive or ambiguous OTU-like cases, no automatic DUB propagation is made from this subtype.
    - [group] Ubiquitin Proteasome System|DUBs and UBL demodifiers|OTU
        status=context_only scope=too_broad_to_propagate GO=[GO:0101005 deubiquitinase activity]
        rationale: This OTU-family group is DUB-related context, but the subtree includes inactive or ambiguous OTU-like cases. Direct DUB propagation should come from narrower gene-level review rather than this whole family bucket.
    - [class] Ubiquitin Proteasome System|DUBs and UBL demodifiers
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a UPS taxonomy container. Its descendants mix catalytic roles, complex membership, binding domains, regulators, adaptors, and substrate-context labels, so a single propagating GO assertion would overstate the shared biology.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## PN row 3: Ubiquitin Proteasome System | Ubiquitin and UBL binding | DUB | OTU | UBA-like (other)
- UniProt: Q5T2D3
- In branches: TR, UPS
- Signature domains: PMID: 23827681 (likely @ 228-276)
- Auxiliary domains: IPR003323
- PN references (titles):
    - 23827681
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|Ubiquitin and UBL binding|DUB|OTU|UBA-like (other)
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower UBL-binding DUB-domain subdivision. Because this subtree includes noncatalytic or pseudo-DUB cases, active DUB propagation is handled by the DUB-family branch rather than this binding-domain node.
    - [type] Ubiquitin Proteasome System|Ubiquitin and UBL binding|DUB|OTU
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower UBL-binding DUB-domain subdivision. Because this subtree includes noncatalytic or pseudo-DUB cases, active DUB propagation is handled by the DUB-family branch rather than this binding-domain node.
    - [group] Ubiquitin Proteasome System|Ubiquitin and UBL binding|DUB
        status=context_only scope=too_broad_to_propagate GO=[GO:0101005 deubiquitinase activity]
        rationale: This UBL-binding group is DUB-related context, but it includes noncatalytic or pseudo-DUB domain cases such as NPLOC4/USP39-like entries. Active DUB propagation is handled from the DUB-family branch.
    - [class] Ubiquitin Proteasome System|Ubiquitin and UBL binding
        status=context_only scope=too_broad_to_propagate GO=[GO:0140036 ubiquitin-modified protein reader activity]
        rationale: This class records ubiquitin/UBL-reader context, but the subtree mixes ubiquitin, SUMO, UBL-domain, domain-architecture, catalytic, signaling, trafficking, and nucleic-acid process buckets. It is useful context, not a safe direct propagation.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## Projected GO annotations (2)
- GO:0006515 protein quality control for misfolded or incompletely synthesized proteins | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Translation|Cytosolic translation|Ribosome-associated QC
- GO:0101005 deubiquitinase activity | scope=ok_for_propagation_to_go | goa_status=entailed_by_goa_closure | from=Translation|Cytosolic translation|Ribosome-associated QC|Deubiquitination

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
