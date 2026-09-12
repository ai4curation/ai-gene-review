# DNAJC17 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9NVM6
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07b
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/DNAJC17/DNAJC17-ai-review.yaml](DNAJC17-ai-review.yaml)
- AIGR review HTML: present - [genes/human/DNAJC17/DNAJC17-ai-review.html](DNAJC17-ai-review.html)
- Gene notes: present - [genes/human/DNAJC17/DNAJC17-notes.md](DNAJC17-notes.md)
- GOA TSV: present - [genes/human/DNAJC17/DNAJC17-goa.tsv](DNAJC17-goa.tsv)
- UniProt record: present - [genes/human/DNAJC17/DNAJC17-uniprot.txt](DNAJC17-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/DNAJC17.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/DNAJC17.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/DNAJC17.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/DNAJC17.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: DNAJC17 is a poorly characterized, predominantly nuclear protein of the DnaJ/HSP40 subfamily C that combines an N-terminal J domain with a C-terminal RNA recognition motif (RRM), separated by a disordered acidic/basic region. The domain architecture marks it as a putative HSP70 co-chaperone with RNA-binding capacity. Convergent evidence (phylogenetic inference from the yeast ortholog Cwc23, an RRM domain with a solved RNA-binding-domain structure, nuclear-speckle localization, and interaction with the U5 snRNP component EFTUD2) implicates DNAJC17 in spliceosome function, most likely spliceosomal complex disassembly. By orthology it has also been suggested to negatively affect PAX8-induced thyroglobulin transcription. It is phosphorylated at Ser-112 and methylated at Lys-264, and its mouse ortholog is essential for viability. Its precise molecular and cellular function in human cells has not been directly established.
- Existing/core annotation action counts: ACCEPT: 4; KEEP_AS_NON_CORE: 7

## PN Consistency Summary

- **Consistency:** Mismatch in emphasis. Deep-research notes and review converge on a nuclear J-domain+RRM protein whose best-supported (convergent IBA + EFTUD2 IPI + nuclear-speckle) function is spliceosome association / spliceosomal complex disassembly (yeast Cwc23 ortholog) plus RNA binding. The PN node frames it solely as an HSP70 co-chaperone. The HSP70-binding role is plausible from the J domain but is NOT demonstrated and NOT the review's core; the review never asserts Hsp70 binding. So PN and review diverge on what the gene principally does.
- **PN story / NEW pressure:** PN proposes GO:0030544 (verified real). There is no existing Hsp70-binding annotation and no direct evidence one exists for DNAJC17; the "more_specific_than_existing_goa" tag is questionable (no existing parent MF in GOA to be more specific than — existing MF terms are RNA binding/nucleic acid binding, a different axis). Family-level inference only; over-reaches as a confident projection.
- **Evidence alignment:** Divergent. Review cites EFTUD2 interactome papers (PMID:35271311 OpenCell, PMID:40205054 cell maps) and the IBA spliceosome-disassembly inference; PN node carries no DNAJC17-specific reference, only the family heuristic. No shared functional paper supports Hsp70 binding.
- **Verdict:** Plausible family inference but over-reaches as confident projection; gene's real function (spliceosome/RNA) sits outside the HSP70-cochaperone node. **Recommended edits:** [MAP] mark DNAJC17's GO:0030544 as family/domain-level inference (no experimental HSP70 binding); correct the "more_specific_than_existing_goa" tag (existing GOA MF is RNA binding, not an HSP70 parent).

## Full Consistency Review

- **UniProt:** Q9NVM6 · **batch:** proteostasis-batch-2026-06-07b · **review status:** COMPLETE
- **PN placement:** `Cytonuclear proteostasis | Chaperone | HSP70 system | J-domain containing HSP70 cochaperone` (branch CY) ; **PN-node mapping:** type=mapped, scope=ok_for_propagation_to_go, GO:0030544 Hsp70 protein binding (goa_status=more_specific_than_existing_goa)
- **Consistency:** Mismatch in emphasis. Deep-research notes and review converge on a nuclear J-domain+RRM protein whose best-supported (convergent IBA + EFTUD2 IPI + nuclear-speckle) function is spliceosome association / spliceosomal complex disassembly (yeast Cwc23 ortholog) plus RNA binding. The PN node frames it solely as an HSP70 co-chaperone. The HSP70-binding role is plausible from the J domain but is NOT demonstrated and NOT the review's core; the review never asserts Hsp70 binding. So PN and review diverge on what the gene principally does.
- **PN story / NEW pressure:** PN proposes GO:0030544 (verified real). There is no existing Hsp70-binding annotation and no direct evidence one exists for DNAJC17; the "more_specific_than_existing_goa" tag is questionable (no existing parent MF in GOA to be more specific than — existing MF terms are RNA binding/nucleic acid binding, a different axis). Family-level inference only; over-reaches as a confident projection.
- **Mapping strategy:** Node heuristic is fine generically, but for DNAJC17 the projection is purely domain-based and the gene's real placement is in the spliceosome (Translation/RNA branch), not captured here. PN-projected Hsp70 binding is orthogonal to (not broader/narrower than) the review's RNA-binding/spliceosome core. Treat as family inference.
- **Evidence alignment:** Divergent. Review cites EFTUD2 interactome papers (PMID:35271311 OpenCell, PMID:40205054 cell maps) and the IBA spliceosome-disassembly inference; PN node carries no DNAJC17-specific reference, only the family heuristic. No shared functional paper supports Hsp70 binding.
- **Verdict:** Plausible family inference but over-reaches as confident projection; gene's real function (spliceosome/RNA) sits outside the HSP70-cochaperone node. **Recommended edits:** [MAP] mark DNAJC17's GO:0030544 as family/domain-level inference (no experimental HSP70 binding); correct the "more_specific_than_existing_goa" tag (existing GOA MF is RNA binding, not an HSP70 parent).

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07b
- review_yaml: genes/human/DNAJC17/DNAJC17-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Cytonuclear proteostasis | Chaperone | HSP70 system | J-domain containing HSP70 cochaperone
- UniProt: Q9NVM6
- In branches: CY
- PN-node mapping records (path + ancestors):
    - [type] Cytonuclear proteostasis|Chaperone|HSP70 system|J-domain containing HSP70 cochaperone
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0030544 Hsp70 protein binding]
        rationale: In the PN hierarchy, this type denotes J-domain cochaperones assigned to the HSP70 system. Their shared mechanistic role is direct interaction with HSP70-family chaperones, making Hsp70 protein binding the most defensible GO target in the current cache.
    - [group] Cytonuclear proteostasis|Chaperone|HSP70 system
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a specific GO class. The member genes span multiple activities, complexes, or contexts, so propagation from this node would overstate the shared biology; use narrower child or gene-level curations.
    - [class] Cytonuclear proteostasis|Chaperone
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a specific GO class. The member genes span multiple activities, complexes, or contexts, so propagation from this node would overstate the shared biology; use narrower child or gene-level curations.
    - [branch] Cytonuclear proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## Projected GO annotations (1)
- GO:0030544 Hsp70 protein binding | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=Cytonuclear proteostasis|Chaperone|HSP70 system|J-domain containing HSP70 cochaperone

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
