# NAA38 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9BRA0
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07c
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/NAA38/NAA38-ai-review.yaml](NAA38-ai-review.yaml)
- AIGR review HTML: present - [genes/human/NAA38/NAA38-ai-review.html](NAA38-ai-review.html)
- Gene notes: present - [genes/human/NAA38/NAA38-notes.md](NAA38-notes.md)
- GOA TSV: present - [genes/human/NAA38/NAA38-goa.tsv](NAA38-goa.tsv)
- UniProt record: present - [genes/human/NAA38/NAA38-uniprot.txt](NAA38-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/NAA38.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/NAA38.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/NAA38.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/NAA38.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: NAA38 (N-alpha-acetyltransferase 38; also LSMD1, MAK31) is a small Sm-like (LSm-fold) non-catalytic auxiliary subunit of the human NatC N-terminal acetyltransferase complex (NatC = NAA30 catalytic + NAA35 + NAA38). It does not catalyze acetyl transfer but is a structural component of NatC, which co-translationally acetylates the alpha-amino group of N-terminal methionine residues retained in front of bulky/hydrophobic residues; this modification shields substrates from N-degron-mediated ubiquitination and degradation. NAA38 is predominantly cytoplasmic (ribosome-associated) with some nuclear localization. Loss of NatC subunits triggers p53-dependent apoptosis.
- Existing/core annotation action counts: ACCEPT: 7; KEEP_AS_NON_CORE: 8; MARK_AS_OVER_ANNOTATED: 1; NEW: 1

## PN Consistency Summary

- **Consistency:** Strong. All sources agree NAA38 (LSMD1/MAK31) is the small Sm-like (LSm-fold) **non-catalytic auxiliary** subunit of NatC; correctly no catalytic MF. PN-node mapping matches.
- **PN story / NEW pressure:** PN projects BP GO:0006474 (verified real; confirmed absent from NAA38 GOA). As with NAA35, an `involved_in` BP for the auxiliary subunit of the acetylating complex is defensible and complements the CC-only core. Conclusion: **ADD GO:0006474 (involved_in)** reasonable; catalytic MF must NOT be added. Separately, the review correctly flags the family-level GO:0003723 (RNA binding, from the Sm-like signature) as MARK_AS_OVER_ANNOTATED — consistent with the PN treatment as a NatC subunit, not an RNA-binding protein. Not an over-reach.
- **Evidence alignment:** Concordant. Review/notes anchor to PMID:19398576 (NatC; hMak31; IDA GO:0031417, IMP GO:0043066) and PMID:37891180. PN row carries no titles. No divergence.
- **Verdict:** Consistent, high-quality. Same minor notes-vs-YAML mismatch as NAA35: notes say HT protein-binding PMID:25416956/PMID:32814053 should be MARK_AS_OVER_ANNOTATED, YAML uses KEEP_AS_NON_CORE. **Recommended edits:** Add BP GO:0006474 (involved_in, auxiliary subunit) to NAA38 review [YAML]; optionally reconcile PMID:25416956 / PMID:32814053 protein-binding actions with notes [YAML].

## Full Consistency Review

- **UniProt:** Q9BRA0 · **batch:** proteostasis-batch-2026-06-07c · **review status:** COMPLETE
- **PN placement:** `Translation|Cytosolic translation|Nascent peptide husbandry|N-terminal acetylation of nascent peptide|NatC complex component` ; **PN-node mapping:** subtype mapped→GO:0031417 NatC complex (ok_for_propagation); type mapped→GO:0006474 N-terminal protein amino acid acetylation (ok_for_propagation, new_to_goa)
- **Consistency:** Strong. All sources agree NAA38 (LSMD1/MAK31) is the small Sm-like (LSm-fold) **non-catalytic auxiliary** subunit of NatC; correctly no catalytic MF. PN-node mapping matches.
- **PN story / NEW pressure:** PN projects BP GO:0006474 (verified real; confirmed absent from NAA38 GOA). As with NAA35, an `involved_in` BP for the auxiliary subunit of the acetylating complex is defensible and complements the CC-only core. Conclusion: **ADD GO:0006474 (involved_in)** reasonable; catalytic MF must NOT be added. Separately, the review correctly flags the family-level GO:0003723 (RNA binding, from the Sm-like signature) as MARK_AS_OVER_ANNOTATED — consistent with the PN treatment as a NatC subunit, not an RNA-binding protein. Not an over-reach.
- **Mapping strategy:** Correct. Subtype→NatC complex exact CC; BP at type level. No node-mapping change warranted.
- **Evidence alignment:** Concordant. Review/notes anchor to PMID:19398576 (NatC; hMak31; IDA GO:0031417, IMP GO:0043066) and PMID:37891180. PN row carries no titles. No divergence.
- **Verdict:** Consistent, high-quality. Same minor notes-vs-YAML mismatch as NAA35: notes say HT protein-binding PMID:25416956/PMID:32814053 should be MARK_AS_OVER_ANNOTATED, YAML uses KEEP_AS_NON_CORE. **Recommended edits:** Add BP GO:0006474 (involved_in, auxiliary subunit) to NAA38 review [YAML]; optionally reconcile PMID:25416956 / PMID:32814053 protein-binding actions with notes [YAML].
- **2026-06-18 follow-up:** Implemented the high-confidence YAML edit: added GO:0006474 N-terminal protein amino acid acetylation as a NEW BP recommendation and core process for the NatC auxiliary subunit. The optional protein-binding action-style reconciliation remains separate.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07c
- review_yaml: genes/human/NAA38/NAA38-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Translation | Cytosolic translation | Nascent peptide husbandry | N-terminal acetylation of nascent peptide | NatC complex component
- UniProt: Q9BRA0
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
