# DNAJB11 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9UBS4
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07b
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/DNAJB11/DNAJB11-ai-review.yaml](DNAJB11-ai-review.yaml)
- AIGR review HTML: present - [genes/human/DNAJB11/DNAJB11-ai-review.html](DNAJB11-ai-review.html)
- Gene notes: present - [genes/human/DNAJB11/DNAJB11-notes.md](DNAJB11-notes.md)
- GOA TSV: present - [genes/human/DNAJB11/DNAJB11-goa.tsv](DNAJB11-goa.tsv)
- UniProt record: present - [genes/human/DNAJB11/DNAJB11-uniprot.txt](DNAJB11-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/DNAJB11.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/DNAJB11.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/DNAJB11.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/DNAJB11.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: DNAJB11 (ERdj3, also HEDJ/ERj3p/ABBP-2) is a soluble, glycosylated, ER-lumenal HSP40/J-domain co-chaperone and the principal J-protein partner of the ER HSP70 chaperone BiP (HSPA5). Through its N-terminal J domain it binds and stimulates the ATPase activity of BiP, and through a cysteine-rich substrate-binding domain it binds unfolded and misfolded peptides directly; it recruits BiP to substrates and then dissociates as BiP engages, promoting proper folding, maturation, trafficking and ERAD-targeted degradation of secretory and membrane proteins. It is a stress (UPR)-inducible component of a large ER chaperone complex (with HSPA5, HSP90B1, HYOU1, PDIA proteins, SDF2L1, UGGT1 and others) and is required for the maturation and trafficking of polycystin-1 (PKD1). Monoallelic loss-of-function variants in DNAJB11 cause an atypical autosomal-dominant polycystic kidney disease (PKD6).
- Existing/core annotation action counts: ACCEPT: 14; KEEP_AS_NON_CORE: 10; MARK_AS_OVER_ANNOTATED: 4

## PN Consistency Summary

- **Consistency:** Strong agreement on the core. Notes/YAML describe a soluble ER-lumenal BiP (HSPA5) co-chaperone that stimulates BiP ATPase (GO:0032781 IDA PMID:20335166) and binds misfolded substrates directly via a Cys-rich domain (GO:0051787 IDA PMID:28597544; GO:0140309 holdase IEA). The PN HSP70-cochaperone type fits BiP partnership. One subtlety: the PN type uses GO:0030544 "Hsp70 protein binding," but DNAJB11's partner is the ER HSP70 BiP — biologically Hsp70-family, so consistent. The row2 "secreted during ER stress" PN note aligns with the minor secreted pool the review flags but downgrades; review marks orthology-projected extracellular (GO:0005576) as over-annotated for the *core* compartment — a defensible nuance, not a contradiction.
- **PN story / NEW pressure:** PN's HSP70-binding assertion is captured (GO:0051787 misfolded protein binding ACCEPT/core; GO:0140309 holdase ACCEPT; core_functions also assert GO:0001671 ATPase activator). Genuine direct-substrate/holdase MF distinguishes ERdj3 from members lacking such data. PN-projected GO:0030544 (verified real) is narrower than the BiP-binding evidence; already captured. No NEW-term pressure (disease/PKD1 maturation = GO:0051604 IMP, captured).
- **Evidence alignment:** Review's BiP-mechanism PMIDs (18923428, 20335166, 28597544) and disease PMID:29706351 are the substantive set; PN supplies path/title-level context only. No conflict.
- **Verdict:** CONSISTENT — strong direct evidence; GO:0030544 a sound narrower specialization of the verified BiP-cochaperone/holdase MF.

## Full Consistency Review

- **UniProt:** Q9UBS4 (ERdj3/HEDJ) · **batch:** proteostasis-batch-2026-06-07b · **review status:** COMPLETE
- **PN placement:** row1 `ER proteostasis|Chaperone|HSP70 system|J-domain containing HSP70 cochaperone` (mapped→GO:0030544); row2 `Extracellular proteostasis|Chaperone|Primarily intracellular, secreted during ER stress` (no_mapping) (branches ER, EX)
- **Consistency:** Strong agreement on the core. Notes/YAML describe a soluble ER-lumenal BiP (HSPA5) co-chaperone that stimulates BiP ATPase (GO:0032781 IDA PMID:20335166) and binds misfolded substrates directly via a Cys-rich domain (GO:0051787 IDA PMID:28597544; GO:0140309 holdase IEA). The PN HSP70-cochaperone type fits BiP partnership. One subtlety: the PN type uses GO:0030544 "Hsp70 protein binding," but DNAJB11's partner is the ER HSP70 BiP — biologically Hsp70-family, so consistent. The row2 "secreted during ER stress" PN note aligns with the minor secreted pool the review flags but downgrades; review marks orthology-projected extracellular (GO:0005576) as over-annotated for the *core* compartment — a defensible nuance, not a contradiction.
- **PN story / NEW pressure:** PN's HSP70-binding assertion is captured (GO:0051787 misfolded protein binding ACCEPT/core; GO:0140309 holdase ACCEPT; core_functions also assert GO:0001671 ATPase activator). Genuine direct-substrate/holdase MF distinguishes ERdj3 from members lacking such data. PN-projected GO:0030544 (verified real) is narrower than the BiP-binding evidence; already captured. No NEW-term pressure (disease/PKD1 maturation = GO:0051604 IMP, captured).
- **Mapping strategy:** GO:0030544 mapping is defensible; ERdj3 has direct BiP-interaction and ATPase-stimulation evidence, so the type-level mapping does NOT over-reach. Row2 extracellular no_mapping is correct.
- **Evidence alignment:** Review's BiP-mechanism PMIDs (18923428, 20335166, 28597544) and disease PMID:29706351 are the substantive set; PN supplies path/title-level context only. No conflict.
- **Verdict:** CONSISTENT — strong direct evidence; GO:0030544 a sound narrower specialization of the verified BiP-cochaperone/holdase MF.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07b
- review_yaml: genes/human/DNAJB11/DNAJB11-ai-review.yaml
- PN workbook rows: 2

## PN row 1: ER proteostasis | Chaperone | HSP70 system | J-domain containing HSP70 cochaperone
- UniProt: Q9UBS4
- In branches: ER, EX
- PN-node mapping records (path + ancestors):
    - [type] ER proteostasis|Chaperone|HSP70 system|J-domain containing HSP70 cochaperone
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0030544 Hsp70 protein binding]
        rationale: In the PN hierarchy, this type denotes J-domain cochaperones assigned to the HSP70 system. Their shared mechanistic role is direct interaction with HSP70-family chaperones, making Hsp70 protein binding the most defensible GO target in the current cache.
    - [group] ER proteostasis|Chaperone|HSP70 system
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a single GO class. The member genes span multiple activities, complexes, or contexts, so direct propagation from this node would overstate the shared biology.
    - [class] ER proteostasis|Chaperone
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a single GO class. The member genes span multiple activities, complexes, or contexts, so direct propagation from this node would overstate the shared biology.
    - [branch] ER proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## PN row 2: Extracellular proteostasis | Chaperone | Primarily intracellular, secreted during ER stress
- UniProt: Q9UBS4
- In branches: ER, EX
- PN-node mapping records (path + ancestors):
    - [group] Extracellular proteostasis|Chaperone|Primarily intracellular, secreted during ER stress
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a contextual PN bucket. The label is useful for curator triage, but no direct GO mapping is appropriate because propagation would add a process, activity, or localization not shared cleanly by all members.
    - [class] Extracellular proteostasis|Chaperone
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a specific GO class. The member genes span multiple activities, complexes, or contexts, so propagation from this node would overstate the shared biology; use narrower child or gene-level curations.
    - [branch] Extracellular proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## Projected GO annotations (1)
- GO:0030544 Hsp70 protein binding | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=ER proteostasis|Chaperone|HSP70 system|J-domain containing HSP70 cochaperone

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
