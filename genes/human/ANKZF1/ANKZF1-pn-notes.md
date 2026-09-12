# ANKZF1 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9H8Y5
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-03 (PR 1365)
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/ANKZF1/ANKZF1-ai-review.yaml](ANKZF1-ai-review.yaml)
- AIGR review HTML: present - [genes/human/ANKZF1/ANKZF1-ai-review.html](ANKZF1-ai-review.html)
- Gene notes: present - [genes/human/ANKZF1/ANKZF1-notes.md](ANKZF1-notes.md)
- GOA TSV: present - [genes/human/ANKZF1/ANKZF1-goa.tsv](ANKZF1-goa.tsv)
- UniProt record: present - [genes/human/ANKZF1/ANKZF1-uniprot.txt](ANKZF1-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/ANKZF1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/ANKZF1.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ANKZF1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ANKZF1.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/ANKZF1/ANKZF1-deep-research-falcon.md](ANKZF1-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: ANKZF1 is a cytosolic tRNA endonuclease in the ribosome-associated quality-control pathway. It acts after stalled-ribosome splitting on 60S ribosome-nascent-chain complexes, cleaving the terminal 3'-CCA region of P-site peptidyl-tRNA to release incomplete nascent polypeptides for degradation and to generate tRNA repair intermediates that can be recycled. ANKZF1 also binds VCP/p97 and has a stress-responsive mitochondrial context, translocating to mitochondria under oxidative stress and supporting mitochondrial integrity.
- Existing/core annotation action counts: ACCEPT: 12; KEEP_AS_NON_CORE: 1; MARK_AS_OVER_ANNOTATED: 2; MODIFY: 6; REMOVE: 1

## PN Consistency Summary

- **Consistency:** Mostly consistent, with one deliberate PN-vs-review divergence (see below). DR ↔ notes ↔ YAML agree: ANKZF1 is a cytosolic RQC tRNA endonuclease (acceptor-arm/3'-CCA cleavage on 60S RQC), VCP/VIM cofactor.
- **PN story / NEW pressure:** PN projects two ok_for_propagation terms. GO:0006515 (already_in_goa) — review ACCEPTs (multiple IDA, PMID:29632312/30244831). **GO:0035694 mitochondrial protein catabolic process (PN new_to_goa, verified real): review DECLINES.** Notes find no direct human evidence ANKZF1 catalyzes mito protein catabolism; mito link is stress translocation/RQC-of-OMM-mRNAs (PMID:28302725, 38388640), not catabolism. Conclude: GO:0035694 over-reaches for this gene → already-captured story is RQC (GO:0006515); mito-catabolism not supported.
- **Evidence alignment:** PN row-3 cites PMID:28451587 (VIM); review/DR use PMID:21896481 (Stapf VIM definition) instead — both VIM-defining, complementary. Strong overlap on RQC PMIDs (29632312, 30244831, 31011209, 32075755). MF refined: RNA-endonuclease/GO:0140101 MODIFY→GO:0004549 tRNA-specific ribonuclease (verified real). ERAD IBA (GO:0036503) REMOVEd as Vms1/Cdc48 over-projection.
- **Verdict:** Consistent; GO:0006515 ACCEPT matches PN. PN GO:0035694 over-reaches for ANKZF1; review correctly declines (no human mito-catabolism evidence).

## Full Consistency Review

- **UniProt:** Q9H8Y5 · **batch:** proteostasis-batch-2026-06-03 (Falcon DR 2026-06-07) · **review status:** COMPLETE
- **PN placement:** 3 rows, MI/TR/UPS. (1) `Mitochondrial proteostasis|Organelle-specific protein degradation|Vms pathway`; (2) `Translation|Cytosolic translation|Ribosome-associated QC|VCP system for RQC`; (3) `UPS|VCP and associated proteins|adaptors|VIM|ankyrin repeats`. **PN-node mapping:** mito class=`mapped`→GO:0035694 mito protein catabolic (new_to_goa); RQC group=`mapped`→GO:0006515 protein QC (already_in_goa_exact); VCP-adaptor nodes=`no_mapping`/`context_only` (GO:0034098, GO:0043335).
- **Consistency:** Mostly consistent, with one deliberate PN-vs-review divergence (see below). DR ↔ notes ↔ YAML agree: ANKZF1 is a cytosolic RQC tRNA endonuclease (acceptor-arm/3'-CCA cleavage on 60S RQC), VCP/VIM cofactor.
- **PN story / NEW pressure:** PN projects two ok_for_propagation terms. GO:0006515 (already_in_goa) — review ACCEPTs (multiple IDA, PMID:29632312/30244831). **GO:0035694 mitochondrial protein catabolic process (PN new_to_goa, verified real): review DECLINES.** Notes find no direct human evidence ANKZF1 catalyzes mito protein catabolism; mito link is stress translocation/RQC-of-OMM-mRNAs (PMID:28302725, 38388640), not catabolism. Conclude: GO:0035694 over-reaches for this gene → already-captured story is RQC (GO:0006515); mito-catabolism not supported.
- **Mapping strategy:** GO:0035694 derives from a broad parent class (Organelle-specific protein degradation), while the Vms-pathway child itself is `no_mapping`; the mapping audit flagged it `manual_gene_level_review_required`. Gene-level review here rejects propagation to ANKZF1 — node mapping should not project GO:0035694 onto ANKZF1.
- **Evidence alignment:** PN row-3 cites PMID:28451587 (VIM); review/DR use PMID:21896481 (Stapf VIM definition) instead — both VIM-defining, complementary. Strong overlap on RQC PMIDs (29632312, 30244831, 31011209, 32075755). MF refined: RNA-endonuclease/GO:0140101 MODIFY→GO:0004549 tRNA-specific ribonuclease (verified real). ERAD IBA (GO:0036503) REMOVEd as Vms1/Cdc48 over-projection.
- **Verdict:** Consistent; GO:0006515 ACCEPT matches PN. PN GO:0035694 over-reaches for ANKZF1; review correctly declines (no human mito-catabolism evidence).
- **Recommended edits:** none to ANKZF1-ai-review.yaml. [MAP] do not propagate GO:0035694 from the mito "Organelle-specific protein degradation" class to ANKZF1 (Vms-pathway leaf is no_mapping; gene-level evidence is RQC/stress-translocation, not mito proteolysis).

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-03
- review_yaml: genes/human/ANKZF1/ANKZF1-ai-review.yaml
- PN workbook rows: 3

## PN row 1: Mitochondrial proteostasis | Organelle-specific protein degradation | Vms pathway
- UniProt: Q9H8Y5
- In branches: MI, TR, UPS
- PN-node mapping records (path + ancestors):
    - [group] Mitochondrial proteostasis|Organelle-specific protein degradation|Vms pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower taxonomy bucket that is already covered by a curated parent mapping or by gene-level annotations. No additional direct GO mapping is appropriate from this node.
    - [class] Mitochondrial proteostasis|Organelle-specific protein degradation
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0035694 mitochondrial protein catabolic process]
        rationale: This PN class groups mitochondrial protein-degradation pathways. GO mitochondrial protein catabolic process is the conservative shared target.
    - [branch] Mitochondrial proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## PN row 2: Translation | Cytosolic translation | Ribosome-associated QC | VCP system for RQC
- UniProt: Q9H8Y5
- In branches: MI, TR, UPS
- PN-node mapping records (path + ancestors):
    - [type] Translation|Cytosolic translation|Ribosome-associated QC|VCP system for RQC
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a single GO class. The member genes span multiple activities, complexes, or contexts, so direct propagation from this node would overstate the shared biology.
    - [group] Translation|Cytosolic translation|Ribosome-associated QC
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0006515 protein quality control for misfolded or incompletely synthesized proteins]
        rationale: The PN ribosome-associated quality-control group covers surveillance and disposal of stalled or defective nascent-chain translation products. GO lacks a dedicated ribosome-associated QC term in the local cache, so the broader protein-quality-control process is the best supported target.
    - [class] Translation|Cytosolic translation
        status=context_only scope=too_broad_to_propagate GO=[GO:0002181 cytoplasmic translation]
        rationale: The PN class Cytosolic translation is centered on the cytoplasmic translation apparatus and process, but it also houses supporting machinery such as ribosome biogenesis factors. The GO process term is a useful high-level label for the class, but propagating it to all members would over-annotate genes whose PN placement is through assembly or maturation context rather than core cytoplasmic translation.
    - [branch] Translation
        status=context_only scope=too_broad_to_propagate GO=[GO:0006412 translation]
        rationale: The PN Translation branch is organized around the translation apparatus and immediately associated cotranslational quality-control systems. GO translation is the closest high-level process label, but the PN branch also contains adjacent machinery such as ribosome biogenesis and nascent-chain handling. Keeping this relationship is useful for interpretation, but it is too broad to project safely onto every member.

## PN row 3: Ubiquitin Proteasome System | VCP and associated proteins | adaptors | VIM | ankyrin repeats
- UniProt: Q9H8Y5
- In branches: MI, TR, UPS
- Signature domains: PMID: 28451587 (VIM)
- Auxiliary domains: IPR002110
- PN references (titles):
    - 28451587
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|VCP and associated proteins|adaptors|VIM|ankyrin repeats
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a VCP-adaptor motif or architecture subdivision. The label is useful taxonomy but too indirect for direct GO propagation without gene-level evidence.
    - [type] Ubiquitin Proteasome System|VCP and associated proteins|adaptors|VIM
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a VCP-adaptor motif or architecture subdivision. The label is useful taxonomy but too indirect for direct GO propagation without gene-level evidence.
    - [group] Ubiquitin Proteasome System|VCP and associated proteins|adaptors
        status=context_only scope=too_broad_to_propagate GO=[GO:0034098 VCP-NPL4-UFD1 AAA ATPase complex]
        rationale: This PN group records VCP adaptor context, but it mixes UBX, SHP, VIM, VBM, membrane, and other adaptor classes. Direct propagation should come only from narrower complex-specific nodes or gene-level review.
    - [class] Ubiquitin Proteasome System|VCP and associated proteins
        status=context_only scope=too_broad_to_propagate GO=[GO:0043335 protein unfolding]
        rationale: This class records the VCP segregase branch context, but descendants include VCP, substrate adaptors, DUBs, E3 ligases, channels, and unrelated associated enzymes. Direct propagation is restricted to narrower nodes.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## Projected GO annotations (2)
- GO:0035694 mitochondrial protein catabolic process | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Mitochondrial proteostasis|Organelle-specific protein degradation
- GO:0006515 protein quality control for misfolded or incompletely synthesized proteins | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Translation|Cytosolic translation|Ribosome-associated QC

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
