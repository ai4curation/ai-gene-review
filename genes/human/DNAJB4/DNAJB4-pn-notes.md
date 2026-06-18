# DNAJB4 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9UDY4
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07b
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/DNAJB4/DNAJB4-ai-review.yaml](DNAJB4-ai-review.yaml)
- AIGR review HTML: present - [genes/human/DNAJB4/DNAJB4-ai-review.html](DNAJB4-ai-review.html)
- Gene notes: present - [genes/human/DNAJB4/DNAJB4-notes.md](DNAJB4-notes.md)
- GOA TSV: present - [genes/human/DNAJB4/DNAJB4-goa.tsv](DNAJB4-goa.tsv)
- UniProt record: present - [genes/human/DNAJB4/DNAJB4-uniprot.txt](DNAJB4-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/DNAJB4.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/DNAJB4.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/DNAJB4.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/DNAJB4.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: DNAJB4 (HLJ1, "human liver DnaJ-like protein"; also DNAJW) is a cytosolic HSP40/J-domain co-chaperone of the DNAJB subfamily and a paralog of DNAJB1. Through its N-terminal J domain it stimulates the ATPase activity of HSP70 (HSPA1A/HSPA1B), binding misfolded client proteins and delivering them to HSP70 to drive their folding, refolding and disaggregation. It is a homodimer, is heat-inducible, and is broadly expressed with high levels in striated muscle, where it localizes to the sarcomeric Z-disc and contributes to myofibril/Z-disc proteostasis. Biallelic loss-of-function variants in DNAJB4 cause an autosomal recessive congenital myopathy with early respiratory failure (CMYO21), reflecting its role as a muscle chaperone. It also interacts with the mu-opioid receptor (OPRM1) C-terminal tail and with aggregation-prone clients such as huntingtin and ataxin-1.
- Existing/core annotation action counts: ACCEPT: 11; KEEP_AS_NON_CORE: 12; MARK_AS_OVER_ANNOTATED: 1

## PN Consistency Summary

- **Consistency:** Strong agreement. Notes, review YAML and PN annotation all describe a cytosolic class-B HSP40 that stimulates HSP70 (HSPA1A/B) ATPase and delivers misfolded clients. No contradictions; PN "J-domain HSP70 cochaperone" type matches the gene's verified core MF.
- **PN story / NEW pressure:** PN asserts direct HSP70 interaction. This is already captured experimentally: GO:0001671 ATPase activator activity (IDA, PMID:24318877, ACCEPT/core) and GO:0051087 protein-folding chaperone binding (IPI PMID:21231916, ACCEPT/core). The PN-projected GO:0030544 "Hsp70 protein binding" (verified real via OLS) is a child of GO:0051087 — i.e. it would be a *more specific* refinement, not a missing function. No NEW-term pressure; the muscle/Z-disc role (GO:0030018 IDA) is also well captured. Verdict: already captured (GO:0030544 is a defensible specialization).
- **Evidence alignment:** PN reference titles overlap the review's core PMIDs (21231916 HSP70 machine; 24318877 NEF/ATPase; 36264506 myopathy/Z-disc). No divergence.
- **Verdict:** CONSISTENT — PN GO:0030544 is a defensible narrower specialization of the gene's experimentally-supported GO:0051087/GO:0001671 HSP70-cochaperone MF; node mapping correct.

## Full Consistency Review

- **UniProt:** Q9UDY4 (HLJ1/DNAJW) · **batch:** proteostasis-batch-2026-06-07b · **review status:** COMPLETE
- **PN placement:** `Cytonuclear proteostasis|Chaperone|HSP70 system|J-domain containing HSP70 cochaperone` (branch CY) ; **PN-node mapping:** type=mapped, scope=ok_for_propagation_to_go, GO:0030544 Hsp70 protein binding (parent group/class/branch = no_mapping)
- **Consistency:** Strong agreement. Notes, review YAML and PN annotation all describe a cytosolic class-B HSP40 that stimulates HSP70 (HSPA1A/B) ATPase and delivers misfolded clients. No contradictions; PN "J-domain HSP70 cochaperone" type matches the gene's verified core MF.
- **PN story / NEW pressure:** PN asserts direct HSP70 interaction. This is already captured experimentally: GO:0001671 ATPase activator activity (IDA, PMID:24318877, ACCEPT/core) and GO:0051087 protein-folding chaperone binding (IPI PMID:21231916, ACCEPT/core). The PN-projected GO:0030544 "Hsp70 protein binding" (verified real via OLS) is a child of GO:0051087 — i.e. it would be a *more specific* refinement, not a missing function. No NEW-term pressure; the muscle/Z-disc role (GO:0030018 IDA) is also well captured. Verdict: already captured (GO:0030544 is a defensible specialization).
- **Mapping strategy:** Node already mapped to GO:0030544 (correct, narrower than the gene's GO:0051087). Status/scope appropriate — DNAJB4 has direct IPI HSP70-binding evidence, so it genuinely supports the type-level mapping rather than over-reaching. Parent no_mapping decisions are sound.
- **Evidence alignment:** PN reference titles overlap the review's core PMIDs (21231916 HSP70 machine; 24318877 NEF/ATPase; 36264506 myopathy/Z-disc). No divergence.
- **Verdict:** CONSISTENT — PN GO:0030544 is a defensible narrower specialization of the gene's experimentally-supported GO:0051087/GO:0001671 HSP70-cochaperone MF; node mapping correct.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07b
- review_yaml: genes/human/DNAJB4/DNAJB4-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Cytonuclear proteostasis | Chaperone | HSP70 system | J-domain containing HSP70 cochaperone
- UniProt: Q9UDY4
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
