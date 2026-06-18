# NAA30 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q147X3
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07c
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/NAA30/NAA30-ai-review.yaml](NAA30-ai-review.yaml)
- AIGR review HTML: present - [genes/human/NAA30/NAA30-ai-review.html](NAA30-ai-review.html)
- Gene notes: present - [genes/human/NAA30/NAA30-notes.md](NAA30-notes.md)
- GOA TSV: present - [genes/human/NAA30/NAA30-goa.tsv](NAA30-goa.tsv)
- UniProt record: present - [genes/human/NAA30/NAA30-uniprot.txt](NAA30-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/NAA30.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/NAA30.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/NAA30.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/NAA30.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: NAA30 (N-alpha-acetyltransferase 30; also hMak3, NAT12) is the catalytic subunit of the human NatC N-terminal acetyltransferase complex (NatC = NAA30 + NAA35 + NAA38). It is a GNAT-fold acetyltransferase (MAK3 subfamily, EC 2.3.1.256) that co-translationally transfers an acetyl group from acetyl-CoA to the alpha-amino group of N-terminal methionine residues retained in front of bulky/hydrophobic residues (Met-Leu, Met-Ile, Met-Phe, Met-Trp, Met-Tyr). NatC associates with ribosomes and acts on nascent polypeptides; this N-terminal acetylation can shield proteins from N-degron-mediated ubiquitination and degradation. NAA30 activity is required for the lysosomal localization of the small GTPase ARL8B (a NatC substrate), and depletion of NatC subunits triggers p53-dependent apoptosis. NAA30 is predominantly cytoplasmic (ribosome-associated) with some reported nuclear localization.
- Existing/core annotation action counts: ACCEPT: 14; KEEP_AS_NON_CORE: 6; MARK_AS_OVER_ANNOTATED: 1; NEW: 1

## PN Consistency Summary

- **Consistency:** Strong. Deep-research notes, review YAML and PN dossier all agree NAA30 is the **catalytic** subunit of NatC (=NAA30+NAA35+NAA38, hMak3/hMak10/hMak31), co-translational Nt-acetylation of retained Met before bulky/hydrophobic residues, ribosome-associated. PN-node mapping (NatC complex CC; Nt-acetylation BP) matches the review's MF/CC content. No contradictions.
- **PN story / NEW pressure:** PN projects the **BP** GO:0006474 (N-terminal protein amino acid acetylation) — verified real and non-obsolete via OLS; confirmed absent from NAA30 GOA (grep). The review captures the **MF** (GO:0004596, GO:0120518) and **CC** (GO:0031417) but has no BP for the acetylation *process*. GO:0006474 is the BP aspect, not a parent of the MF terms, so it is genuinely complementary. Conclusion: **ADD** GO:0006474 (involved_in) is defensible and would round out MF/BP/CC; not an over-reach for the catalytic subunit.
- **Evidence alignment:** Concordant. PN row carries no reference titles; review/notes anchor to PMID:19398576 (NatC characterization, hMak3 catalytic; IDA GO:0004596/GO:0031417) and PMID:37891180 (Nt-acetylation shields from degradation). Both VERIFIED in the YAML reference_review. No divergence.
- **Verdict:** Consistent and high-quality. Optional ADD of BP GO:0006474 to the review to mirror the PN projection. **Recommended edits:** Add existing/new BP annotation GO:0006474 (N-terminal protein amino acid acetylation, involved_in) to NAA30 review [YAML].

## Full Consistency Review

- **UniProt:** Q147X3 · **batch:** proteostasis-batch-2026-06-07c · **review status:** COMPLETE
- **PN placement:** `Translation|Cytosolic translation|Nascent peptide husbandry|N-terminal acetylation of nascent peptide|NatC complex component` ; **PN-node mapping:** subtype mapped→GO:0031417 NatC complex (ok_for_propagation); type mapped→GO:0006474 N-terminal protein amino acid acetylation (ok_for_propagation, new_to_goa)
- **Consistency:** Strong. Deep-research notes, review YAML and PN dossier all agree NAA30 is the **catalytic** subunit of NatC (=NAA30+NAA35+NAA38, hMak3/hMak10/hMak31), co-translational Nt-acetylation of retained Met before bulky/hydrophobic residues, ribosome-associated. PN-node mapping (NatC complex CC; Nt-acetylation BP) matches the review's MF/CC content. No contradictions.
- **PN story / NEW pressure:** PN projects the **BP** GO:0006474 (N-terminal protein amino acid acetylation) — verified real and non-obsolete via OLS; confirmed absent from NAA30 GOA (grep). The review captures the **MF** (GO:0004596, GO:0120518) and **CC** (GO:0031417) but has no BP for the acetylation *process*. GO:0006474 is the BP aspect, not a parent of the MF terms, so it is genuinely complementary. Conclusion: **ADD** GO:0006474 (involved_in) is defensible and would round out MF/BP/CC; not an over-reach for the catalytic subunit.
- **Mapping strategy:** Sound for the catalytic subunit. Subtype→NatC complex (exact CC) and type→Nt-acetylation BP are both appropriate and not too broad (NAA30 directly performs the catalysis). No change to node mapping warranted.
- **Evidence alignment:** Concordant. PN row carries no reference titles; review/notes anchor to PMID:19398576 (NatC characterization, hMak3 catalytic; IDA GO:0004596/GO:0031417) and PMID:37891180 (Nt-acetylation shields from degradation). Both VERIFIED in the YAML reference_review. No divergence.
- **Verdict:** Consistent and high-quality. Optional ADD of BP GO:0006474 to the review to mirror the PN projection. **Recommended edits:** Add existing/new BP annotation GO:0006474 (N-terminal protein amino acid acetylation, involved_in) to NAA30 review [YAML].
- **2026-06-18 follow-up:** Implemented the YAML edit: added GO:0006474 N-terminal protein amino acid acetylation as a NEW BP recommendation and added it to the catalytic NatC core function.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07c
- review_yaml: genes/human/NAA30/NAA30-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Translation | Cytosolic translation | Nascent peptide husbandry | N-terminal acetylation of nascent peptide | NatC complex component
- UniProt: Q147X3
- In branches: TR
- PN-node mapping records (path + ancestors):
    - [subtype] Translation|Cytosolic translation|Nascent peptide husbandry|N-terminal acetylation of nascent peptide|NatC complex component
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0031417 NatC complex]
        rationale: Exact cellular-component match: members are subunits of the NatC N-terminal acetyltransferase complex. Complements the parent BP mapping with the complex-membership CC term.
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
- GO:0006474 N-terminal protein amino acid acetylation | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Translation|Cytosolic translation|Nascent peptide husbandry|N-terminal acetylation of nascent peptide

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
