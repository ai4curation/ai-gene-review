# NAA15 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9BXJ9
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07c
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/NAA15/NAA15-ai-review.yaml](NAA15-ai-review.yaml)
- AIGR review HTML: present - [genes/human/NAA15/NAA15-ai-review.html](NAA15-ai-review.html)
- Gene notes: present - [genes/human/NAA15/NAA15-notes.md](NAA15-notes.md)
- GOA TSV: present - [genes/human/NAA15/NAA15-goa.tsv](NAA15-goa.tsv)
- UniProt record: present - [genes/human/NAA15/NAA15-uniprot.txt](NAA15-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/NAA15.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/NAA15.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/NAA15.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/NAA15.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: NAA15 (N-alpha-acetyltransferase 15, NatA auxiliary subunit; also NARG1, NATH, Tubedown-1) is the large, non-catalytic auxiliary subunit of the NatA N-terminal acetyltransferase complex. It dimerizes with the catalytic subunit NAA10, where its TPR-repeat-rich solenoid wraps around NAA10, anchoring the complex to the ribosome near the exit tunnel and orienting nascent polypeptide N-termini for co-translational acetylation. NAA15 itself has no acetyltransferase catalytic activity; rather it activates and confers ribosomal targeting and substrate specificity on NAA10, and is required for NatA-type N-terminal acetylation in vivo. It also serves as the scaffold for the NatA-associated factors HYPK and NAA50 (forming NatE). NAA15 is predominantly cytoplasmic with a nuclear pool, and a nuclear NAA15-containing complex with the Ku70/Ku80 (XRCC6/ XRCC5) heterodimer has been reported to up-regulate transcription from the osteocalcin promoter. NAA15 (as Tubedown-1) has additional reported roles in endothelial/retinal vascular biology, and NAA15 variants are associated with neurodevelopmental and congenital heart phenotypes.
- Existing/core annotation action counts: ACCEPT: 14; KEEP_AS_NON_CORE: 19; MARK_AS_OVER_ANNOTATED: 3

## PN Consistency Summary

- **Consistency:** Agreement on identity and complex: review (notes, deep-research) and PN agree NAA15 is the **auxiliary, non-catalytic** NatA subunit — NatA complex (GO:0031415, IBA/IPI/IDA accepted) and ribosome anchoring (GO:0043022 IDA accepted) and activator activity (GO:0010698 IBA accepted). The review is careful that NAA15 is NOT catalytic (it MARK_AS_OVER_ANNOTATED'd the bare GO:0016407 acetyltransferase activity contributes_to). One tension: the PN projects the **BP** GO:0006474 (the acetylation *process*) onto NAA15; the review captures the auxiliary contribution via the activator MF (GO:0010698) and ribosome binding, not via a process term — but NAA15 "involved_in N-terminal acetylation" is defensible as process participation, so this is a soft, not hard, divergence.
- **PN story / NEW pressure:** No NEW pressure. NatA membership and the activator/ribosome-anchoring functions are fully captured. The PN GO:0006474 process projection is **broader/less specific** than the review's precise non-catalytic MF framing and risks implying catalytic involvement.
- **Evidence alignment:** PN row carries no reference titles. Review anchors on PMID:15496142, 19480662, 25489052 (VERIFIED, NatA structure/complex) plus the moonlighting Ku70/Ku80 osteocalcin role (PMID:12145306, kept non-core). No conflict.
- **Verdict:** Consistent on complex/auxiliary identity; non-catalytic role correctly emphasized. No edits required. Caveat: prefer the activator MF (GO:0010698) over the catalytic-flavored BP GO:0006474 when describing NAA15's contribution.

## Full Consistency Review

- **UniProt:** Q9BXJ9 · **batch:** proteostasis-batch-2026-06-07c · **review status:** COMPLETE
- **PN placement:** `Translation|Cytosolic translation|Nascent peptide husbandry|N-terminal acetylation of nascent peptide|NatA/NatE complex component` (TR only). **PN-node mapping:** subtype→GO:0031415 NatA complex (mapped, CC); type→GO:0006474 N-terminal protein amino acid acetylation (mapped, BP); group no_mapping; class/branch context_only.
- **Consistency:** Agreement on identity and complex: review (notes, deep-research) and PN agree NAA15 is the **auxiliary, non-catalytic** NatA subunit — NatA complex (GO:0031415, IBA/IPI/IDA accepted) and ribosome anchoring (GO:0043022 IDA accepted) and activator activity (GO:0010698 IBA accepted). The review is careful that NAA15 is NOT catalytic (it MARK_AS_OVER_ANNOTATED'd the bare GO:0016407 acetyltransferase activity contributes_to). One tension: the PN projects the **BP** GO:0006474 (the acetylation *process*) onto NAA15; the review captures the auxiliary contribution via the activator MF (GO:0010698) and ribosome binding, not via a process term — but NAA15 "involved_in N-terminal acetylation" is defensible as process participation, so this is a soft, not hard, divergence.
- **PN story / NEW pressure:** No NEW pressure. NatA membership and the activator/ribosome-anchoring functions are fully captured. The PN GO:0006474 process projection is **broader/less specific** than the review's precise non-catalytic MF framing and risks implying catalytic involvement.
- **Mapping strategy:** GO:0031415 NatA complex (CC) projection is exact and appropriate for NAA15 — this is the right shared term for both NAA10 and NAA15 at the complex-component subtype. The BP GO:0006474 node mapping is fine at the *type* node generically, but at gene level for an auxiliary subunit it over-reaches toward catalysis; the activator MF is the more honest gene-level term.
- **Evidence alignment:** PN row carries no reference titles. Review anchors on PMID:15496142, 19480662, 25489052 (VERIFIED, NatA structure/complex) plus the moonlighting Ku70/Ku80 osteocalcin role (PMID:12145306, kept non-core). No conflict.
- **Verdict:** Consistent on complex/auxiliary identity; non-catalytic role correctly emphasized. No edits required. Caveat: prefer the activator MF (GO:0010698) over the catalytic-flavored BP GO:0006474 when describing NAA15's contribution.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07c
- review_yaml: genes/human/NAA15/NAA15-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Translation | Cytosolic translation | Nascent peptide husbandry | N-terminal acetylation of nascent peptide | NatA/NatE complex component
- UniProt: Q9BXJ9
- In branches: TR
- PN-node mapping records (path + ancestors):
    - [subtype] Translation|Cytosolic translation|Nascent peptide husbandry|N-terminal acetylation of nascent peptide|NatA/NatE complex component
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0031415 NatA complex]
        rationale: This subtype is an exact cellular-component match: members are subunits of the NatA N-terminal acetyltransferase complex. The parent maps the BP (GO:0006474 N-terminal protein amino acid acetylation); this node adds the complementary, non-redundant complex-membership CC term.
    - [type] Translation|Cytosolic translation|Nascent peptide husbandry|N-terminal acetylation of nascent peptide
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0006474 N-terminal protein amino acid acetylation]
        rationale: This PN type denotes N-terminal acetyltransferase machinery acting on nascent peptides. The GO N-terminal acetylation process is the direct target.
    - [group] Translation|Cytosolic translation|Nascent peptide husbandry
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a single GO class. The member genes span multiple activities, complexes, or contexts, so direct propagation from this node would overstate the shared biology.
    - [class] Translation|Cytosolic translation
        status=context_only scope=too_broad_to_propagate GO=[GO:0002181 cytoplasmic translation]
        rationale: The PN class Cytosolic translation is centered on the cytoplasmic translation apparatus and process, but it also houses supporting machinery such as ribosome biogenesis factors. The GO process term is a useful high-level label for the class, but propagating it to all members would over-annotate genes whose PN placement is through assembly or maturation context rather than core cytoplasmic translation.
    - [branch] Translation
        status=context_only scope=too_broad_to_propagate GO=[GO:0006412 translation]
        rationale: The PN Translation branch is organized around the translation apparatus and immediately associated cotranslational quality-control systems. GO translation is the closest high-level process label, but the PN branch also contains adjacent machinery such as ribosome biogenesis and nascent-chain handling. Keeping this relationship is useful for interpretation, but it is too broad to project safely onto every member.

## Projected GO annotations (1)
- GO:0006474 N-terminal protein amino acid acetylation | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=Translation|Cytosolic translation|Nascent peptide husbandry|N-terminal acetylation of nascent peptide

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
