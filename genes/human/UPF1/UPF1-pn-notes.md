# UPF1 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q92900
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07c
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/UPF1/UPF1-ai-review.yaml](UPF1-ai-review.yaml)
- AIGR review HTML: present - [genes/human/UPF1/UPF1-ai-review.html](UPF1-ai-review.html)
- Gene notes: present - [genes/human/UPF1/UPF1-notes.md](UPF1-notes.md)
- GOA TSV: present - [genes/human/UPF1/UPF1-goa.tsv](UPF1-goa.tsv)
- UniProt record: present - [genes/human/UPF1/UPF1-uniprot.txt](UPF1-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/UPF1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/UPF1.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/UPF1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/UPF1.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: UPF1 (regulator of nonsense transcripts 1; RENT1) is the central ATP-dependent RNA helicase and ATPase of the nonsense-mediated mRNA decay (NMD) pathway. A superfamily-1 (SF1) helicase with an N-terminal cysteine-histidine-rich (CH) zinc-binding regulatory domain, UPF1 is recruited to mRNAs at translation termination, where release factors (eRF1/eRF3) and the SMG1 kinase complex assemble the transient SURF complex. In EJC-dependent NMD the adaptor UPF2 bridges UPF1 to UPF3 and the downstream exon-junction complex, forming the UPF1-UPF2-UPF3 surveillance complex; UPF1 is then phosphorylated by SMG1 and the phospho-form is recognized by SMG5/SMG6/SMG7 to recruit decay enzymes and PP2A. UPF1 ATPase/helicase activity remodels and disassembles target mRNPs, committing premature-termination-codon-containing and certain long-3'UTR or staufen-bound transcripts to degradation, and also mediates replication-dependent histone mRNA decay at the end of S phase. UPF1 acts mainly on cytoplasmic translating mRNAs (with a smaller nuclear pool), concentrates in P-bodies in its hyperphosphorylated state, and has additional reported moonlighting roles at telomeres and in DNA replication; it can unwind both RNA and DNA in vitro.
- Existing/core annotation action counts: ACCEPT: 41; KEEP_AS_NON_CORE: 78; MARK_AS_OVER_ANNOTATED: 1

## PN Consistency Summary

- **Consistency:** Mostly consistent on the gene's biology — deep-research/notes, review YAML and GOA all agree UPF1 is the central ATP-dependent SF1 RNA helicase/ATPase of NMD (core MF GO:0003724; core BP GO:0000184). But there is a framing tension with the PN-node mapping (see below): the review never frames UPF1 as a translation-termination factor; it is recruited *at* termination but its function is mRNA surveillance/decay, not polypeptide release.
- **PN story / NEW pressure:** The PN "modulation of termination" story IS reflected in GOA — UPF1 carries GO:0006449 *regulation of translational termination* (verified real; 2 records, ECO:0000315/0000303), which the dossier correctly cites as `supported_by_goa_regulation`. This is the defensible frame and is already captured. No NEW term needed; UPF1's core (RNA helicase, NMD, ATPase) is fully annotated.
- **Evidence alignment:** PN row carries no reference titles; the review is heavily evidenced (NMD: PMID:26255671 TAS, GO:0000184 IEA; helicase: PMID:21419344, 26138914, 30218034 IDA; complex GO:0170010). No divergence to reconcile — PN provides no competing citations.
- **Verdict:** Gene biology consistent; PN group→GO:0006415 (translational termination) over-reaches — UPF1's termination link is regulatory (GO:0006449), already in GOA.

## Full Consistency Review

- **UniProt:** Q92900 · **batch:** proteostasis-batch-2026-06-07c · **review status:** COMPLETE
- **PN placement:** `Translation|Cytosolic translation|Translation termination|Modulation of termination` ; **PN-node mapping:** type (Modulation of termination) `no_mapping`; group (Translation termination) `mapped, ok_for_propagation` → GO:0006415 translational termination; class/branch `context_only, too_broad`. Projected: GO:0006415 (goa_status=supported_by_goa_regulation).
- **Consistency:** Mostly consistent on the gene's biology — deep-research/notes, review YAML and GOA all agree UPF1 is the central ATP-dependent SF1 RNA helicase/ATPase of NMD (core MF GO:0003724; core BP GO:0000184). But there is a framing tension with the PN-node mapping (see below): the review never frames UPF1 as a translation-termination factor; it is recruited *at* termination but its function is mRNA surveillance/decay, not polypeptide release.
- **PN story / NEW pressure:** The PN "modulation of termination" story IS reflected in GOA — UPF1 carries GO:0006449 *regulation of translational termination* (verified real; 2 records, ECO:0000315/0000303), which the dossier correctly cites as `supported_by_goa_regulation`. This is the defensible frame and is already captured. No NEW term needed; UPF1's core (RNA helicase, NMD, ATPase) is fully annotated.
- **Mapping strategy:** The GROUP projection onto GO:0006415 *translational termination* (verified: "release of a polypeptide chain from the ribosome … in response to a termination codon") is the wrong/over-broad term for UPF1 — UPF1 does not catalyze peptide release. UPF1 already has the precise GO:0006449 (regulation of termination) and GO:0000184 (NMD). The type-level `no_mapping` for "Modulation of termination" is correct; the group-level GO:0006415 projection should be GO:0006449, not GO:0006415, for UPF1 (precedent: TOMM20/HSPA8/RAB7A broader-term rejections).
- **Evidence alignment:** PN row carries no reference titles; the review is heavily evidenced (NMD: PMID:26255671 TAS, GO:0000184 IEA; helicase: PMID:21419344, 26138914, 30218034 IDA; complex GO:0170010). No divergence to reconcile — PN provides no competing citations.
- **Verdict:** Gene biology consistent; PN group→GO:0006415 (translational termination) over-reaches — UPF1's termination link is regulatory (GO:0006449), already in GOA.

**Recommended edits:** [MAP] for UPF1, replace/avoid the group projection GO:0006415 (translational termination, = peptide release) with GO:0006449 (regulation of translational termination), which is already in UPF1 GOA and is the accurate frame; UPF1's core remains NMD (GO:0000184) + RNA helicase (GO:0003724).

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07c
- review_yaml: genes/human/UPF1/UPF1-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Translation | Cytosolic translation | Translation termination | Modulation of termination
- UniProt: Q92900
- In branches: TR
- PN-node mapping records (path + ancestors):
    - [type] Translation|Cytosolic translation|Translation termination|Modulation of termination
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a contextual PN bucket. The label is useful for curator triage, but no direct GO mapping is appropriate because propagation would add a process, activity, or localization not shared cleanly by all members.
    - [group] Translation|Cytosolic translation|Translation termination
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0006415 translational termination]
        rationale: This PN group denotes cytosolic translation termination and release factors. Translational termination is the shared process target.
    - [class] Translation|Cytosolic translation
        status=context_only scope=too_broad_to_propagate GO=[GO:0002181 cytoplasmic translation]
        rationale: The PN class Cytosolic translation is centered on the cytoplasmic translation apparatus and process, but it also houses supporting machinery such as ribosome biogenesis factors. The GO process term is a useful high-level label for the class, but propagating it to all members would over-annotate genes whose PN placement is through assembly or maturation context rather than core cytoplasmic translation.
    - [branch] Translation
        status=context_only scope=too_broad_to_propagate GO=[GO:0006412 translation]
        rationale: The PN Translation branch is organized around the translation apparatus and immediately associated cotranslational quality-control systems. GO translation is the closest high-level process label, but the PN branch also contains adjacent machinery such as ribosome biogenesis and nascent-chain handling. Keeping this relationship is useful for interpretation, but it is too broad to project safely onto every member.

## Projected GO annotations (1)
- GO:0006415 translational termination | scope=ok_for_propagation_to_go | goa_status=supported_by_goa_regulation | from=Translation|Cytosolic translation|Translation termination

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
