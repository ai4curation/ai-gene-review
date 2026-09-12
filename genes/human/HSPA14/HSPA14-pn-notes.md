# HSPA14 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q0VDF9
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07b
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/HSPA14/HSPA14-ai-review.yaml](HSPA14-ai-review.yaml)
- AIGR review HTML: present - [genes/human/HSPA14/HSPA14-ai-review.html](HSPA14-ai-review.html)
- Gene notes: present - [genes/human/HSPA14/HSPA14-notes.md](HSPA14-notes.md)
- GOA TSV: present - [genes/human/HSPA14/HSPA14-goa.tsv](HSPA14-goa.tsv)
- UniProt record: present - [genes/human/HSPA14/HSPA14-uniprot.txt](HSPA14-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/HSPA14.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/HSPA14.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/HSPA14.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/HSPA14.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: HSPA14 (Heat shock 70 kDa protein 14, also called HSP70L1 / HSP70-like protein 1) is an atypical, divergent member of the HSP70 family and the Hsp70/DnaK-type subunit of the mammalian ribosome-associated complex (RAC). RAC is a stable cytosolic heterodimer of HSPA14 and the Hsp40/DnaJ-type co-chaperone DNAJC2 (MPP11) that docks at the ribosomal exit tunnel, where it engages emerging nascent polypeptide chains and assists their co-translational ('de novo') folding. Within RAC, HSPA14 provides the nucleotide-binding/substrate-binding HSP70 module while DNAJC2 stimulates its ATPase activity; the complex couples the chaperone cycle to ongoing translation rather than acting as an autonomous stress-induced refoldase. HSPA14 is cytosolic and ribosome-associated, and has additionally been described as an immunoadjuvant capable of activating antigen-presenting cells.
- Existing/core annotation action counts: ACCEPT: 13; KEEP_AS_NON_CORE: 3; MARK_AS_OVER_ANNOTATED: 3; MODIFY: 4

## PN Consistency Summary

- **Consistency:** Notes ↔ review ↔ PN RAC row converge — HSPA14 is the atypical Hsp70/DnaK subunit of RAC (heterodimer with DNAJC2/MPP11) acting cotranslationally at the ribosomal exit tunnel; ATPase stimulated by DNAJC2 (PMID:16002468). Notes flag (per MS1) that HSPA14, like yeast Ssz1p, may not be an autonomous foldase — its nucleotide cycle largely serves to stimulate the downstream ribosome-bound HSP70. The cotranslational-folding story is fully and consistently captured.
- **PN story / NEW pressure:** The RAC/cotranslational story is ALREADY captured: review ACCEPTs GO:0051083 'de novo' cotranslational protein folding (TAS) and GO:0101031 protein folding chaperone complex; PN's GO:0051083 is correctly flagged already_in_goa_exact. The HSP70-type GO:0140662 ATP-dependent protein folding chaperone projection is the softer of the two atypical-HSP70 cases: the review itself uses GO:0044183 protein folding chaperone (parent, ACCEPT) as a core MF and MARK_AS_OVER_ANNOTATED only the stress-refolding GO:0042026. So GO:0140662 (ATP-dependent foldase child) is debatable — defensible as RAC engages nascent chains ATP-dependently, but borderline given HSPA14's Ssz1p-like atypia (uncertain intrinsic foldase activity).
- **Evidence alignment:** PN rows carry no reference titles; the review's central PMID:16002468 (MPP11/Hsp70L1 form mammalian RAC) underpins both the GO:0051083 and complex annotations — convergent with the PN RAC subtype projection.
- **Verdict:** RAC/cotranslational-folding projection sound and already captured; HSP70-type GO:0140662 is borderline-defensible (atypical Ssz1p-like HSP70) but should carry the caveat. **Recommended edits:** [MAP] keep GO:0051083 for the RAC subtype (already covered); for the HSP70-type GO:0140662 projection, scope to co-translational folding and note HSPA14's Ssz1p-like atypia (intrinsic foldase activity uncertain) rather than asserting canonical ATP-dependent refolding.

## Full Consistency Review

- **UniProt:** Q0VDF9 (HSP70L1) · **batch:** proteostasis-batch-2026-06-07b · **review status:** COMPLETE
- **PN placement:** two rows — `Cytonuclear proteostasis|Chaperone|HSP70 system|HSP70` (type) and `Translation|Cytosolic translation|Nascent peptide husbandry|Nascent peptide chaperoning|RAC component` (subtype) ; **PN-node mapping:** HSP70 type → mapped/ok GO:0140662 ATP-dependent protein folding chaperone (more_specific_than_existing_goa); RAC subtype + parent type → mapped/ok GO:0051083 'de novo' cotranslational protein folding (already_in_goa_exact); Translation class/branch → context_only/too_broad (GO:0002181 / GO:0006412).
- **Consistency:** Notes ↔ review ↔ PN RAC row converge — HSPA14 is the atypical Hsp70/DnaK subunit of RAC (heterodimer with DNAJC2/MPP11) acting cotranslationally at the ribosomal exit tunnel; ATPase stimulated by DNAJC2 (PMID:16002468). Notes flag (per MS1) that HSPA14, like yeast Ssz1p, may not be an autonomous foldase — its nucleotide cycle largely serves to stimulate the downstream ribosome-bound HSP70. The cotranslational-folding story is fully and consistently captured.
- **PN story / NEW pressure:** The RAC/cotranslational story is ALREADY captured: review ACCEPTs GO:0051083 'de novo' cotranslational protein folding (TAS) and GO:0101031 protein folding chaperone complex; PN's GO:0051083 is correctly flagged already_in_goa_exact. The HSP70-type GO:0140662 ATP-dependent protein folding chaperone projection is the softer of the two atypical-HSP70 cases: the review itself uses GO:0044183 protein folding chaperone (parent, ACCEPT) as a core MF and MARK_AS_OVER_ANNOTATED only the stress-refolding GO:0042026. So GO:0140662 (ATP-dependent foldase child) is debatable — defensible as RAC engages nascent chains ATP-dependently, but borderline given HSPA14's Ssz1p-like atypia (uncertain intrinsic foldase activity).
- **Mapping strategy:** RAC subtype → GO:0051083 needs no change (exact, already in GOA/review). HSP70-type GO:0140662: narrower than the review's accepted GO:0044183; acceptable but flag the Ssz1p-atypia caveat — if propagated, it should be co-translational-folding-scoped, not stress-refolding. Not a clear-cut rejection like HSPA13.
- **Evidence alignment:** PN rows carry no reference titles; the review's central PMID:16002468 (MPP11/Hsp70L1 form mammalian RAC) underpins both the GO:0051083 and complex annotations — convergent with the PN RAC subtype projection.
- **Verdict:** RAC/cotranslational-folding projection sound and already captured; HSP70-type GO:0140662 is borderline-defensible (atypical Ssz1p-like HSP70) but should carry the caveat. **Recommended edits:** [MAP] keep GO:0051083 for the RAC subtype (already covered); for the HSP70-type GO:0140662 projection, scope to co-translational folding and note HSPA14's Ssz1p-like atypia (intrinsic foldase activity uncertain) rather than asserting canonical ATP-dependent refolding.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07b
- review_yaml: genes/human/HSPA14/HSPA14-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Cytonuclear proteostasis | Chaperone | HSP70 system | HSP70
- UniProt: Q0VDF9
- In branches: CY, TR
- PN-node mapping records (path + ancestors):
    - [type] Cytonuclear proteostasis|Chaperone|HSP70 system|HSP70
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0140662 ATP-dependent protein folding chaperone]
        rationale: In the PN hierarchy, the type label HSP70 within the chaperone/HSP70-system context denotes canonical HSP70 chaperones. Propagation to the GO molecular function ATP-dependent protein folding chaperone is appropriate for curation, but the PN family label is not itself a strict GO-equivalent class.
    - [group] Cytonuclear proteostasis|Chaperone|HSP70 system
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a specific GO class. The member genes span multiple activities, complexes, or contexts, so propagation from this node would overstate the shared biology; use narrower child or gene-level curations.
    - [class] Cytonuclear proteostasis|Chaperone
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a specific GO class. The member genes span multiple activities, complexes, or contexts, so propagation from this node would overstate the shared biology; use narrower child or gene-level curations.
    - [branch] Cytonuclear proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## PN row 2: Translation | Cytosolic translation | Nascent peptide husbandry | Nascent peptide chaperoning | RAC component
- UniProt: Q0VDF9
- In branches: CY, TR
- PN-node mapping records (path + ancestors):
    - [subtype] Translation|Cytosolic translation|Nascent peptide husbandry|Nascent peptide chaperoning|RAC component
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0051083 'de novo' cotranslational protein folding]
        rationale: The ribosome-associated complex is a cotranslational chaperone system for emerging nascent chains. The PN subtype is a specific component class within this mechanism, so propagation to GO 'de novo' cotranslational protein folding is justified but not exact.
    - [type] Translation|Cytosolic translation|Nascent peptide husbandry|Nascent peptide chaperoning
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0051083 'de novo' cotranslational protein folding]
        rationale: This PN type denotes cotranslational chaperoning of nascent peptides. The GO de novo cotranslational protein folding term is the shared process target.
    - [group] Translation|Cytosolic translation|Nascent peptide husbandry
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a single GO class. The member genes span multiple activities, complexes, or contexts, so direct propagation from this node would overstate the shared biology.
    - [class] Translation|Cytosolic translation
        status=context_only scope=too_broad_to_propagate GO=[GO:0002181 cytoplasmic translation]
        rationale: The PN class Cytosolic translation is centered on the cytoplasmic translation apparatus and process, but it also houses supporting machinery such as ribosome biogenesis factors. The GO process term is a useful high-level label for the class, but propagating it to all members would over-annotate genes whose PN placement is through assembly or maturation context rather than core cytoplasmic translation.
    - [branch] Translation
        status=context_only scope=too_broad_to_propagate GO=[GO:0006412 translation]
        rationale: The PN Translation branch is organized around the translation apparatus and immediately associated cotranslational quality-control systems. GO translation is the closest high-level process label, but the PN branch also contains adjacent machinery such as ribosome biogenesis and nascent-chain handling. Keeping this relationship is useful for interpretation, but it is too broad to project safely onto every member.

## Projected GO annotations (3)
- GO:0140662 ATP-dependent protein folding chaperone | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=Cytonuclear proteostasis|Chaperone|HSP70 system|HSP70
- GO:0051083 'de novo' cotranslational protein folding | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Translation|Cytosolic translation|Nascent peptide husbandry|Nascent peptide chaperoning
- GO:0051083 'de novo' cotranslational protein folding | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Translation|Cytosolic translation|Nascent peptide husbandry|Nascent peptide chaperoning|RAC component

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
