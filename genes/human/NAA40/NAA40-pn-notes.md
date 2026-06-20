# NAA40 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q86UY6
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07c
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/NAA40/NAA40-ai-review.yaml](NAA40-ai-review.yaml)
- AIGR review HTML: present - [genes/human/NAA40/NAA40-ai-review.html](NAA40-ai-review.html)
- Gene notes: present - [genes/human/NAA40/NAA40-notes.md](NAA40-notes.md)
- GOA TSV: present - [genes/human/NAA40/NAA40-goa.tsv](NAA40-goa.tsv)
- UniProt record: present - [genes/human/NAA40/NAA40-uniprot.txt](NAA40-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/NAA40.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/NAA40.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/NAA40.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/NAA40.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: NAA40 (N-alpha-acetyltransferase 40; also NatD/Nat4/Nat11) is a highly substrate-specific N-terminal acetyltransferase that acetylates the free alpha-amino group of the N-terminal serine of histones H4 and H2A (which share an identical Ser-Gly-Arg-Gly N-terminal sequence after initiator-methionine removal), producing N-terminally acetylated H4/H2A (EC 2.3.1.257). Unlike the ribosome-associated NatA/NatB/NatC/NatE complexes, NAA40 is a monomeric enzyme with a narrow, sequence-specific selectivity restricted to these histone N-termini and recognizes the substrate independently of the bulk Nt-acetylation machinery. NAA40-mediated N-terminal acetylation of H4 influences chromatin function and crosstalk with adjacent histone marks (e.g. H4R3 methylation), and NAA40 has reported roles in transcriptional regulation, ribosomal RNA expression, cellular metabolism (including hepatic lipid metabolism), and as a negative regulator of apoptosis. NAA40 localizes mainly to the nucleus with a cytoplasmic pool.
- Existing/core annotation action counts: ACCEPT: 13; KEEP_AS_NON_CORE: 5; MARK_AS_OVER_ANNOTATED: 1

## PN Consistency Summary

- **Consistency:** Partial mismatch. The review and notes correctly describe NAA40/NatD as a **monomeric, histone-specific** N-terminal acetyltransferase acting on the N-terminal Ser of **histones H4/H2A in the nucleus/chromatin** (EC 2.3.1.257), explicitly **not** a ribosome-associated nascent-peptide NAT and recognizing substrate independently of the bulk Nt-acetylation machinery. The PN places it under "N-terminal acetylation of **nascent peptide**" — biologically inaccurate for NAA40 (its substrate is mature chromatin histones, not nascent chains). The PN mapping mitigates this by setting the NatD subtype to no_mapping; only the generic type-level BP propagates.
- **PN story / NEW pressure:** PN projects generic BP GO:0006474 (verified real; absent from NAA40 GOA). GO:0006474 is broad enough to technically cover histone N-terminal acetylation, but the review's histone-specific MFs (GO:0010485, GO:0043998, GO:1990189) are far more precise and already capture the biology; a histone-specific N-terminal acetylation **process** term would be preferable to the generic GO:0006474 if added at all. Conclusion: generic GO:0006474 **over-reaches as the framing** (implies nascent-peptide cotranslational role); the specific histone MF/CC content already in the review is the correct capture.
- **Evidence alignment:** Mostly concordant. Core anchored to PMID:25619998 (NatD H4/H2A specificity; IDA, VERIFIED). Review flags PMID:25732826 as WRONG_IDENTIFIER (resolves to the Naa60 study, not NAA40) — a genuine citation problem the PN row does not surface. PN row carries no titles.
- **Verdict:** Placement biologically off (histone NAT mis-filed under nascent-peptide husbandry); generic GO:0006474 over-reaches relative to the histone-specific terms already present. **Recommended edits:** Re-home NAA40/NatD from "N-terminal acetylation of nascent peptide" to a histone/chromatin PN node, or replace the projected generic GO:0006474 with a histone-N-terminal-acetylation-specific framing [MAP]; do not add generic GO:0006474 to the review (histone-specific MFs suffice) [YAML]; PMID:25732826 already flagged WRONG_IDENTIFIER — candidate for removal/replacement [REF].

## Full Consistency Review

- **UniProt:** Q86UY6 · **batch:** proteostasis-batch-2026-06-07c · **review status:** COMPLETE
- **PN placement:** `Translation|Cytosolic translation|Nascent peptide husbandry|N-terminal acetylation of nascent peptide|NatD, sole component` ; **PN-node mapping:** subtype `NatD, sole component`→no_mapping (correctly suppressed); type→GO:0006474 N-terminal protein amino acid acetylation (ok_for_propagation, new_to_goa)
- **Consistency:** Partial mismatch. The review and notes correctly describe NAA40/NatD as a **monomeric, histone-specific** N-terminal acetyltransferase acting on the N-terminal Ser of **histones H4/H2A in the nucleus/chromatin** (EC 2.3.1.257), explicitly **not** a ribosome-associated nascent-peptide NAT and recognizing substrate independently of the bulk Nt-acetylation machinery. The PN places it under "N-terminal acetylation of **nascent peptide**" — biologically inaccurate for NAA40 (its substrate is mature chromatin histones, not nascent chains). The PN mapping mitigates this by setting the NatD subtype to no_mapping; only the generic type-level BP propagates.
- **PN story / NEW pressure:** PN projects generic BP GO:0006474 (verified real; absent from NAA40 GOA). GO:0006474 is broad enough to technically cover histone N-terminal acetylation, but the review's histone-specific MFs (GO:0010485, GO:0043998, GO:1990189) are far more precise and already capture the biology; a histone-specific N-terminal acetylation **process** term would be preferable to the generic GO:0006474 if added at all. Conclusion: generic GO:0006474 **over-reaches as the framing** (implies nascent-peptide cotranslational role); the specific histone MF/CC content already in the review is the correct capture.
- **Mapping strategy:** The node placement is the concern, not the projected GO per se. NatD does not belong under "nascent peptide husbandry / N-terminal acetylation of nascent peptide" — it is a chromatin/histone modifier. Suppressing the subtype was the right call; consider re-homing NatD to a histone/chromatin PN node, or annotating the type with a histone-specific term rather than the cotranslational-implying generic BP.
- **Evidence alignment:** Mostly concordant. Core anchored to PMID:25619998 (NatD H4/H2A specificity; IDA, VERIFIED). Review flags PMID:25732826 as WRONG_IDENTIFIER (resolves to the Naa60 study, not NAA40) — a genuine citation problem the PN row does not surface. PN row carries no titles.
- **Verdict:** Placement biologically off (histone NAT mis-filed under nascent-peptide husbandry); generic GO:0006474 over-reaches relative to the histone-specific terms already present. **Recommended edits:** Re-home NAA40/NatD from "N-terminal acetylation of nascent peptide" to a histone/chromatin PN node, or replace the projected generic GO:0006474 with a histone-N-terminal-acetylation-specific framing [MAP]; do not add generic GO:0006474 to the review (histone-specific MFs suffice) [YAML]; PMID:25732826 already flagged WRONG_IDENTIFIER — candidate for removal/replacement [REF].

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07c
- review_yaml: genes/human/NAA40/NAA40-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Translation | Cytosolic translation | Nascent peptide husbandry | N-terminal acetylation of nascent peptide | NatD, sole component
- UniProt: Q86UY6
- In branches: TR
- PN-node mapping records (path + ancestors):
    - [subtype] Translation|Cytosolic translation|Nascent peptide husbandry|N-terminal acetylation of nascent peptide|NatD, sole component
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower taxonomy bucket already covered by a curated parent mapping or by gene-level annotations. No additional direct GO mapping is appropriate from this node.
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
