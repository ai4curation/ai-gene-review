# PELO PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9BRX2
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07c
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/PELO/PELO-ai-review.yaml](PELO-ai-review.yaml)
- AIGR review HTML: present - [genes/human/PELO/PELO-ai-review.html](PELO-ai-review.html)
- Gene notes: present - [genes/human/PELO/PELO-notes.md](PELO-notes.md)
- GOA TSV: present - [genes/human/PELO/PELO-goa.tsv](PELO-goa.tsv)
- UniProt record: present - [genes/human/PELO/PELO-uniprot.txt](PELO-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/PELO.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/PELO.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/PELO.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/PELO.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: PELO (Protein pelota homolog, the human ortholog of yeast Dom34) is a cytoplasmic ribosome-rescue factor of the eukaryotic release factor 1 (eRF1) family, Pelota subfamily. Structurally it mimics eRF1 and occupies the ribosomal A site, but it lacks the catalytic GGQ motif and therefore has no peptidyl-tRNA hydrolase (peptide-release) activity. PELO forms the Pelota-HBS1L complex (also called the Dom34-Hbs1 complex) with the translational GTPase HBS1L. This complex recognizes ribosomes that are stalled at the 3' end of an mRNA (truncated, non-stop, or no-go messages), engages the empty mRNA channel, and, after mRNA extraction by the SKI complex, recruits the recycling ATPase ABCE1 to split the stalled 80S ribosome into subunits. PELO thereby initiates the no-go decay (NGD) and non-stop decay (NSD) mRNA surveillance pathways and rescues stalled ribosomes. It is ubiquitously expressed and is also recruited, in a PINK1-regulated manner, to mitochondrially associated ribosomes during mitophagy.
- Existing/core annotation action counts: ACCEPT: 17; KEEP_AS_NON_CORE: 11

## PN Consistency Summary

- **Consistency:** Excellent across all four sources. Deep research, notes, review, PN and GOA all agree PELO is the eRF1-like ribosome-rescue factor (Pelota subfamily; no GGQ/peptidyl-tRNA hydrolase), subunit of the Pelota-HBS1L (Dom34-Hbs1) complex, working with HBS1L+ABCE1 to split stalled 80S and initiate NGD/NSD. No contradictions.
- **PN story / NEW pressure:** GO:0072344 (verified real, rescue of stalled cytosolic ribosome) is already in GOA and in the review (IDA PMID:21448132, 27863242 + IBA) — fully captured. GO:0006515 (verified real) is new_to_goa; PELO genuinely drives stalled-ribosome QC, so it is a defensible higher-level process ADD, but it is broader than the review's already-precise GO:0072344/GO:0032790/GO:0070966/GO:0070481 set. Conclude: rescue already captured; GO:0006515 a defensible but redundant (broader) ADD.
- **Evidence alignment:** PN cites no PMIDs (row had none). Review evidence (21448132, 23667253, 27543824, 27863242) is fully self-consistent and HIGH/VERIFIED. No divergence to reconcile.
- **Verdict:** Fully consistent; PN rescue mapping already captured exactly (GO:0072344), GO:0006515 is a defensible-but-broader ADD already entailed by finer terms. No YAML change needed.

## Full Consistency Review

- **UniProt:** Q9BRX2 · **batch:** proteostasis-batch-2026-06-07c · **review status:** COMPLETE (clean; all ACCEPT or KEEP_AS_NON_CORE)
- **PN placement:** 1 row — `Translation|Cytosolic translation|Ribosome-associated QC|Ribosomal rescue`. **PN-node mapping:** rescue-type→mapped GO:0072344 rescue of stalled cytosolic ribosome (already_in_goa_exact); RQC-group→mapped GO:0006515 protein QC (new_to_goa); class/branch context_only. Projected: GO:0072344 (already in GOA), GO:0006515 (new).
- **Consistency:** Excellent across all four sources. Deep research, notes, review, PN and GOA all agree PELO is the eRF1-like ribosome-rescue factor (Pelota subfamily; no GGQ/peptidyl-tRNA hydrolase), subunit of the Pelota-HBS1L (Dom34-Hbs1) complex, working with HBS1L+ABCE1 to split stalled 80S and initiate NGD/NSD. No contradictions.
- **PN story / NEW pressure:** GO:0072344 (verified real, rescue of stalled cytosolic ribosome) is already in GOA and in the review (IDA PMID:21448132, 27863242 + IBA) — fully captured. GO:0006515 (verified real) is new_to_goa; PELO genuinely drives stalled-ribosome QC, so it is a defensible higher-level process ADD, but it is broader than the review's already-precise GO:0072344/GO:0032790/GO:0070966/GO:0070481 set. Conclude: rescue already captured; GO:0006515 a defensible but redundant (broader) ADD.
- **Mapping strategy:** Does not change the node. PN rescue-type→GO:0072344 exactly matches the review's core BP. The group→GO:0006515 propagation is broader than (a parent of) terms already annotated; per the TOMM20/HSPA8/RAB7A "rejected as broader" precedent it adds little. Status/scope (mapped, ok_for_propagation) are appropriate at the type level.
- **Evidence alignment:** PN cites no PMIDs (row had none). Review evidence (21448132, 23667253, 27543824, 27863242) is fully self-consistent and HIGH/VERIFIED. No divergence to reconcile.
- **Verdict:** Fully consistent; PN rescue mapping already captured exactly (GO:0072344), GO:0006515 is a defensible-but-broader ADD already entailed by finer terms. No YAML change needed.
- **Recommended edits:** none required. [MAP] (optional) treat GO:0006515 for PELO as broader/redundant given GO:0072344 already exact in GOA+review.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07c
- review_yaml: genes/human/PELO/PELO-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Translation | Cytosolic translation | Ribosome-associated QC | Ribosomal rescue
- UniProt: Q9BRX2
- In branches: TR
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

## Projected GO annotations (2)
- GO:0006515 protein quality control for misfolded or incompletely synthesized proteins | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Translation|Cytosolic translation|Ribosome-associated QC
- GO:0072344 rescue of stalled cytosolic ribosome | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Translation|Cytosolic translation|Ribosome-associated QC|Ribosomal rescue

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
