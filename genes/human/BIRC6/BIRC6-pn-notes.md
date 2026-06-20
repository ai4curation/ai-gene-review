# BIRC6 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: priority-only PN rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9NR09
- AIGR review status: COMPLETE
- Priority category: contextual_autophagy
- Local AIGR project status: local_review_complete_not_phase1
- Related project: ER_PHAGY.md

## Source Files Checked

- AIGR review YAML: present - [genes/human/BIRC6/BIRC6-ai-review.yaml](BIRC6-ai-review.yaml)
- AIGR review HTML: present - [genes/human/BIRC6/BIRC6-ai-review.html](BIRC6-ai-review.html)
- Gene notes: present - [genes/human/BIRC6/BIRC6-notes.md](BIRC6-notes.md)
- GOA TSV: present - [genes/human/BIRC6/BIRC6-goa.tsv](BIRC6-goa.tsv)
- UniProt record: present - [genes/human/BIRC6/BIRC6-uniprot.txt](BIRC6-uniprot.txt)
- PROTEOSTASIS priority table: [projects/PROTEOSTASIS/priority_genes.tsv](../../../projects/PROTEOSTASIS/priority_genes.tsv)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)
- PN mapping file: [projects/PROTEOSTASIS/mappings/ubiquitin_proteasome_system.yaml](../../../projects/PROTEOSTASIS/mappings/ubiquitin_proteasome_system.yaml)

### Deep Research Files

- [genes/human/BIRC6/BIRC6-deep-research-falcon.md](BIRC6-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: BIRC6 (also known as BRUCE or Apollon) is a giant (~528 kDa) dual-function E2 ubiquitin-conjugating enzyme and E3 ubiquitin-protein ligase (EC 2.3.2.24) belonging to the inhibitor of apoptosis (IAP) protein family. It contains an N-terminal BIR (baculovirus IAP repeat) domain that mediates caspase binding and inhibition, and a C-terminal UBC (ubiquitin-conjugating enzyme) domain that confers chimeric E2/E3 ubiquitin ligase activity. BIRC6 functions as an antiparallel homodimer with a central substrate-binding cavity. Its primary molecular functions are (1) ubiquitination of pro-apoptotic factors (caspases-3, -7, -9, Smac/DIABLO, HtrA2) to inhibit apoptosis, (2) mono-ubiquitination of LC3 at K51 to suppress autophagy (in cooperation with E1 enzyme UBA6), and (3) regulation of cytokinesis by localizing to the midbody ring and coordinating vesicular targeting during abscission. BIRC6 exhibits cell cycle-dependent localization, concentrating at the trans-Golgi network and endosomes in interphase and relocating to spindle poles, the midzone, and the midbody during cell division. Smac/DIABLO antagonizes BIRC6 by competing for substrate binding sites. BIRC6 is itself regulated by RNF41/Nrdp1-mediated ubiquitination and proteasomal degradation, by deubiquitination via USP8, and by caspase-mediated cleavage.
- Existing/core annotation action counts: ACCEPT: 34; KEEP_AS_NON_CORE: 3; MODIFY: 2; REMOVE: 7

## PN Consistency Summary

- **Consistency:** Priority-only record; no phase-1 dossier section exists yet. Local review status is `local_review_complete_not_phase1`. PN placement: ALP > Autophagosome-lysosome docking > Lysosome-autophagosome SNARE complex regulator; UPS > E2-E3 chimera; UPS > with intrinsic E2 > BIR repeat. Main issue: PN assigns a specific ALP role beyond the already-known UPS and autophagy-suppression context
- **PN story / NEW pressure:** Current projection rows: GO:0061630 ubiquitin protein ligase activity (more_specific_than_existing_goa); GO:0061631 ubiquitin conjugating enzyme activity (already_in_goa_exact).
- **Mapping strategy:** Audit the specific autophagy assertion separately from established UPS biology; do not let the broad autophagy context override the reviewed core functions.
- **Verdict:** Create boundary/phase1 dossier and audit whether docking/fusion belongs as a secondary function

## Priority Review Context

- Category: contextual_autophagy
- PN annotations: ALP > Autophagosome-lysosome docking > Lysosome-autophagosome SNARE complex regulator; UPS > E2-E3 chimera; UPS > with intrinsic E2 > BIR repeat
- Why interesting: PN assigns a specific ALP role beyond the already-known UPS and autophagy-suppression context
- Suggested next step: Create boundary/phase1 dossier and audit whether docking/fusion belongs as a secondary function
- Related project: ER_PHAGY.md

## PN Projection Rows

- GO:0061630 ubiquitin protein ligase activity - more_specific_than_existing_goa; scope=ok_for_propagation_to_go; mapping=ubiquitin_proteasome_system.yaml; PN=Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|E3 with intrinsic E2|BIR repeat
- GO:0061631 ubiquitin conjugating enzyme activity - already_in_goa_exact; scope=ok_for_propagation_to_go; mapping=ubiquitin_proteasome_system.yaml; PN=Ubiquitin Proteasome System|E2 conjugating enzymes|ubiquitination|Family 14|E2-E3 chimera

## PN Dossier Context

No phase-1 dossier exists for this priority-only gene. This note preserves the current PROTEOSTASIS boundary or exception decision and should be superseded by a dossier section if the gene is promoted into a full phase-1 batch.

## Note

This file is generated from the current PROTEOSTASIS priority table, PN projection outputs, and local gene-review artifacts. Edit those source records rather than this generated note when correcting the underlying curation.
