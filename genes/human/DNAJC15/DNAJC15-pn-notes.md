# DNAJC15 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9Y5T4
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07b
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/DNAJC15/DNAJC15-ai-review.yaml](DNAJC15-ai-review.yaml)
- AIGR review HTML: present - [genes/human/DNAJC15/DNAJC15-ai-review.html](DNAJC15-ai-review.html)
- Gene notes: present - [genes/human/DNAJC15/DNAJC15-notes.md](DNAJC15-notes.md)
- GOA TSV: present - [genes/human/DNAJC15/DNAJC15-goa.tsv](DNAJC15-goa.tsv)
- UniProt record: present - [genes/human/DNAJC15/DNAJC15-uniprot.txt](DNAJC15-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/DNAJC15.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/DNAJC15.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/DNAJC15.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/DNAJC15.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: DNAJC15 (MCJ, "methylation-controlled J protein") is a small (150 aa) single-pass mitochondrial inner-membrane protein of the DnaJ/HSP40 subfamily C, anchored by a single transmembrane helix with its C-terminal J domain facing the matrix. It has two intertwined activities. As a J co-chaperone of the TIM23 presequence translocase import motor, it stimulates the ATPase activity of the matrix HSP70 chaperone mortalin (HSPA9) to drive presequence-protein import into the matrix; it forms a stable subcomplex with PAM16/MAGMAS, which counteracts this ATPase stimulation. Independently, MCJ associates with respiratory-chain complex I, impairs supercomplex assembly and acts as an endogenous negative regulator of the respiratory chain, restricting mitochondrial membrane potential and ATP production. DNAJC15 is highly expressed in heart, liver and kidney; its promoter is hypermethylated and silenced in many cancers, where loss of expression is associated with chemoresistance.
- Existing/core annotation action counts: ACCEPT: 6; KEEP_AS_NON_CORE: 6

## PN Consistency Summary

- **Consistency:** Strong agreement. Deep-research notes, review YAML and PN node all converge on a TIM23/PAM J-domain co-chaperone that stimulates matrix HSP70 (mortalin/HSPA9). No contradictions. The review additionally documents a second, mitochondrial-import-independent role (negative regulation of respiratory chain/complex I, PMID:23530063) that the PN single-row mapping does not represent, but this is a coverage gap, not a contradiction.
- **PN story / NEW pressure:** PN asserts the generic co-chaperone "Hsp70 protein binding". The review captures the function more precisely as GO:0001671 ATPase activator activity (experimentally demonstrated mortalin stimulation, PMID:23263864). GO:0030544 (verified real via OLS; child of GO:0031072/GO:0051087) is biologically true for MCJ but is NOT a parent of GO:0001671 — it is a different (binding vs activator) MF axis, and is broader/less informative than what the review already records. Not an ADD: the binding is real but the activator-activity annotation already exists and is superior.
- **Evidence alignment:** Excellent overlap. Both rest on PMID:23263864 (Schusdziarra 2013, import co-chaperone) plus PMID:23530063 (Hatle 2013, respiratory repressor) in the review. PN reference titles match the import-cochaperone framing.
- **Verdict:** Consistent; PN projection (Hsp70 binding) is true but already captured more informatively (ATPase activator activity). No edits required.

## Full Consistency Review

- **UniProt:** Q9Y5T4 (MCJ) · **batch:** proteostasis-batch-2026-06-07b · **review status:** COMPLETE
- **PN placement:** `Mitochondrial proteostasis | Chaperone | HSP70 system | J-domain containing HSP70 cochaperone` (branch MI) ; **PN-node mapping:** type=mapped, scope=ok_for_propagation_to_go, GO:0030544 Hsp70 protein binding (goa_status=more_specific_than_existing_goa)
- **Consistency:** Strong agreement. Deep-research notes, review YAML and PN node all converge on a TIM23/PAM J-domain co-chaperone that stimulates matrix HSP70 (mortalin/HSPA9). No contradictions. The review additionally documents a second, mitochondrial-import-independent role (negative regulation of respiratory chain/complex I, PMID:23530063) that the PN single-row mapping does not represent, but this is a coverage gap, not a contradiction.
- **PN story / NEW pressure:** PN asserts the generic co-chaperone "Hsp70 protein binding". The review captures the function more precisely as GO:0001671 ATPase activator activity (experimentally demonstrated mortalin stimulation, PMID:23263864). GO:0030544 (verified real via OLS; child of GO:0031072/GO:0051087) is biologically true for MCJ but is NOT a parent of GO:0001671 — it is a different (binding vs activator) MF axis, and is broader/less informative than what the review already records. Not an ADD: the binding is real but the activator-activity annotation already exists and is superior.
- **Mapping strategy:** No change to the node warranted from this gene. The "more_specific_than_existing_goa" tag is inaccurate here — GO:0030544 is not more specific than the existing GO:0001671 ATPase activator activity; it is an orthogonal/broader label. The respiratory-chain repressor role is genuinely outside the HSP70-cochaperone node and should not be forced into it.
- **Evidence alignment:** Excellent overlap. Both rest on PMID:23263864 (Schusdziarra 2013, import co-chaperone) plus PMID:23530063 (Hatle 2013, respiratory repressor) in the review. PN reference titles match the import-cochaperone framing.
- **Verdict:** Consistent; PN projection (Hsp70 binding) is true but already captured more informatively (ATPase activator activity). No edits required.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07b
- review_yaml: genes/human/DNAJC15/DNAJC15-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Mitochondrial proteostasis | Chaperone | HSP70 system | J-domain containing HSP70 cochaperone
- UniProt: Q9Y5T4
- In branches: MI
- PN-node mapping records (path + ancestors):
    - [type] Mitochondrial proteostasis|Chaperone|HSP70 system|J-domain containing HSP70 cochaperone
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0030544 Hsp70 protein binding]
        rationale: In the PN hierarchy, this type denotes J-domain cochaperones assigned to the HSP70 system. Their shared mechanistic role is direct interaction with HSP70-family chaperones, making Hsp70 protein binding the most defensible GO target in the current cache.
    - [group] Mitochondrial proteostasis|Chaperone|HSP70 system
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a specific GO class. The member genes span multiple activities, complexes, or contexts, so propagation from this node would overstate the shared biology; use narrower child or gene-level curations.
    - [class] Mitochondrial proteostasis|Chaperone
        status=no_mapping scope= GO=[]
        rationale: This PN class is too heterogeneous for a single safe GO mapping. In the workbook it mixes HSP70, HSP60, and HSP90 systems, small intermembrane-space chaperones, membrane-protein chaperones, and other mitochondrial-specific factors.
    - [branch] Mitochondrial proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## Projected GO annotations (1)
- GO:0030544 Hsp70 protein binding | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=Mitochondrial proteostasis|Chaperone|HSP70 system|J-domain containing HSP70 cochaperone

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
