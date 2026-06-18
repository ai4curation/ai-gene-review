# DNAJC10 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q8IXB1
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07b
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/DNAJC10/DNAJC10-ai-review.yaml](DNAJC10-ai-review.yaml)
- AIGR review HTML: present - [genes/human/DNAJC10/DNAJC10-ai-review.html](DNAJC10-ai-review.html)
- Gene notes: present - [genes/human/DNAJC10/DNAJC10-notes.md](DNAJC10-notes.md)
- GOA TSV: present - [genes/human/DNAJC10/DNAJC10-goa.tsv](DNAJC10-goa.tsv)
- UniProt record: present - [genes/human/DNAJC10/DNAJC10-uniprot.txt](DNAJC10-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/DNAJC10.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/DNAJC10.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/DNAJC10.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/DNAJC10.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: DNAJC10 (also called ERdj5 or macrothioredoxin) is an endoplasmic reticulum (ER)-lumenal protein that is both a J-domain co-chaperone and a thioredoxin-family disulfide reductase. It has an N-terminal J domain (with an HPD motif) followed by six thioredoxin-fold domains, four of which carry redox-active CXXC motifs and constitute its reductase active sites. As an enzyme (EC 1.8.4.2), it binds substrate proteins and catalyzes the reduction and removal of improper (non-native) disulfide bonds. Through its J domain it binds the ER Hsp70 chaperone BiP/HSPA5 in an ATP-dependent manner and stimulates its ATPase activity; this BiP interaction is required for DNAJC10 function in both protein folding and degradation. DNAJC10 supports ER protein quality control in two ways. In ER-associated degradation (ERAD) it reduces disulfides in misfolded glycoproteins recognized by EDEM1 to enable their retrotranslocation and degradation, and during productive folding it reduces obligatory non-native disulfides to allow correct maturation of clients such as the LDL receptor. Its expression is induced by ER stress, and it can modulate ER-stress (UPR/apoptotic) signaling.
- Existing/core annotation action counts: ACCEPT: 28; KEEP_AS_NON_CORE: 5; MARK_AS_OVER_ANNOTATED: 1

## PN Consistency Summary

- **Consistency:** Row1 is fully consistent — review and notes confirm J-domain binding of BiP/HSPA5 and GO:0030544 is in GOA (`already_in_goa_exact` is correct). Row2 contains a mechanistic contradiction: PN files ERdj5 under "Protein disulfide isomerases" and projects GO:0003756 (PDI = isomerase activity), but the review, notes, UniProt (RecName "ER disulfide reductase"), and literature (PMID:23769672, PMID:37739037) establish ERdj5 as a disulfide **reductase** (GO:0015035, EC 1.8.4.2), not an isomerase. The review correctly annotates reductase activity and never asserts GO:0003756.
- **PN story / NEW pressure:** GO:0003756 is a verified real term but sits in the isomerase branch (GO:0016853 → GO:0016864 transposing S-S bonds), whereas GO:0015035 is in the oxidoreductase branch (GO:0016491). They are mechanistically distinct. ERdj5 removes/reduces non-native disulfides; it does not rearrange them. Projecting GO:0003756 onto DNAJC10 over-reaches and is the wrong activity. The correct, already-captured term is GO:0015035 (IDA, in GOA).
- **Evidence alignment:** PN row carries no titles; review evidence (PMID:12411443, 18400946, 23769672, 37739037 — all verified) uniformly supports reductase + BiP co-chaperone, none supports isomerase activity. Divergence is in the PN group label, not the literature.
- **Verdict:** Row1 consistent/captured; Row2 over-reaches (PDI isomerase ≠ ERdj5 reductase). **Recommended edits:** [MAP] retarget DNAJC10 row2 from GO:0003756 (PDI activity) to GO:0015035 (protein-disulfide reductase activity), or exclude ERdj5 from the "Protein disulfide isomerases" PN group as a reductase exception.

## Full Consistency Review

- **UniProt:** Q8IXB1 (ERdj5) · **batch:** proteostasis-batch-2026-06-07b · **review status:** COMPLETE
- **PN placement:** row1 `ER proteostasis|Chaperone|HSP70 system|J-domain containing HSP70 cochaperone` (GO:0030544); row2 `ER proteostasis|Folding enzyme|Protein disulfide isomerases` (group=mapped GO:0003756 protein disulfide isomerase activity, `new_to_goa`)
- **Consistency:** Row1 is fully consistent — review and notes confirm J-domain binding of BiP/HSPA5 and GO:0030544 is in GOA (`already_in_goa_exact` is correct). Row2 contains a mechanistic contradiction: PN files ERdj5 under "Protein disulfide isomerases" and projects GO:0003756 (PDI = isomerase activity), but the review, notes, UniProt (RecName "ER disulfide reductase"), and literature (PMID:23769672, PMID:37739037) establish ERdj5 as a disulfide **reductase** (GO:0015035, EC 1.8.4.2), not an isomerase. The review correctly annotates reductase activity and never asserts GO:0003756.
- **PN story / NEW pressure:** GO:0003756 is a verified real term but sits in the isomerase branch (GO:0016853 → GO:0016864 transposing S-S bonds), whereas GO:0015035 is in the oxidoreductase branch (GO:0016491). They are mechanistically distinct. ERdj5 removes/reduces non-native disulfides; it does not rearrange them. Projecting GO:0003756 onto DNAJC10 over-reaches and is the wrong activity. The correct, already-captured term is GO:0015035 (IDA, in GOA).
- **Mapping strategy:** Row2 group mapping should be reconsidered for ERdj5 — the "Protein disulfide isomerases" PN group conflates reductases with isomerases. For DNAJC10 specifically the propagated term should be GO:0015035 (protein-disulfide reductase activity), not GO:0003756.
- **Evidence alignment:** PN row carries no titles; review evidence (PMID:12411443, 18400946, 23769672, 37739037 — all verified) uniformly supports reductase + BiP co-chaperone, none supports isomerase activity. Divergence is in the PN group label, not the literature.
- **Verdict:** Row1 consistent/captured; Row2 over-reaches (PDI isomerase ≠ ERdj5 reductase). **Recommended edits:** [MAP] retarget DNAJC10 row2 from GO:0003756 (PDI activity) to GO:0015035 (protein-disulfide reductase activity), or exclude ERdj5 from the "Protein disulfide isomerases" PN group as a reductase exception.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07b
- review_yaml: genes/human/DNAJC10/DNAJC10-ai-review.yaml
- PN workbook rows: 2

## PN row 1: ER proteostasis | Chaperone | HSP70 system | J-domain containing HSP70 cochaperone
- UniProt: Q8IXB1
- In branches: ER
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

## PN row 2: ER proteostasis | Folding enzyme | Protein disulfide isomerases
- UniProt: Q8IXB1
- In branches: ER
- PN-node mapping records (path + ancestors):
    - [group] ER proteostasis|Folding enzyme|Protein disulfide isomerases
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0003756 protein disulfide isomerase activity]
        rationale: This PN group captures the canonical ER protein-disulfide-isomerase folding enzymes. GO protein disulfide isomerase activity is the cleanest propagation target for the catalytically active family members.
    - [class] ER proteostasis|Folding enzyme
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a single GO class. The member genes span multiple activities, complexes, or contexts, so direct propagation from this node would overstate the shared biology.
    - [branch] ER proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## Projected GO annotations (2)
- GO:0030544 Hsp70 protein binding | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=ER proteostasis|Chaperone|HSP70 system|J-domain containing HSP70 cochaperone
- GO:0003756 protein disulfide isomerase activity | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=ER proteostasis|Folding enzyme|Protein disulfide isomerases

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
