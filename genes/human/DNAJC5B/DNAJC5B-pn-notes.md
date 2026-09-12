# DNAJC5B PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9UF47
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07b
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/DNAJC5B/DNAJC5B-ai-review.yaml](DNAJC5B-ai-review.yaml)
- AIGR review HTML: present - [genes/human/DNAJC5B/DNAJC5B-ai-review.html](DNAJC5B-ai-review.html)
- Gene notes: present - [genes/human/DNAJC5B/DNAJC5B-notes.md](DNAJC5B-notes.md)
- GOA TSV: present - [genes/human/DNAJC5B/DNAJC5B-goa.tsv](DNAJC5B-goa.tsv)
- UniProt record: present - [genes/human/DNAJC5B/DNAJC5B-uniprot.txt](DNAJC5B-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/DNAJC5B.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/DNAJC5B.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/DNAJC5B.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/DNAJC5B.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: DNAJC5B (cysteine-string protein isoform beta, CSP-beta) is a testis-specific paralog of the synaptic co-chaperone CSPalpha/DNAJC5. Like other cysteine string proteins it has an N-terminal J domain that engages the constitutive HSP70 chaperone HSC70/HSPA8 and a downstream cysteine-string region that can be palmitoylated. CSP-beta interacts with the HSC70-SGTA chaperone complex and is membrane-anchored, associating with the trans-Golgi network; unlike CSPalpha its membrane association does not require palmitoylation. Its physiological role is presumed to be HSP70 co-chaperone activity in a secretory/membrane-trafficking context of the testis, but it is otherwise poorly characterized.
- Existing/core annotation action counts: ACCEPT: 1; KEEP_AS_NON_CORE: 2

## PN Consistency Summary

- **Consistency:** Consistent. Deep research (notes), review and PN converge on DNAJC5B/CSP-beta as a testis-specific CSPalpha paralog (J domain aa 19-84) that interacts with the HSC70-SGTA chaperone complex and targets the trans-Golgi network as a non-palmitoylated CSP (PMID:17034881, Boal et al.). The review's core MF is exactly GO:0030544 Hsp70 protein binding, matching the PN projection. The TGN/secretory-pathway context makes the ER-branch placement reasonable. The HSC70/SGTA interaction is experimentally documented (not just family inference), so GO:0030544 here is better-supported than for the Tdark paralogs DNAJC4/DNAJC5G.
- **PN story / NEW pressure:** GO:0030544 is already the review's core MF → **already captured** (verified real). goa_status=more_specific_than_existing_goa is accurate (GOA had no chaperone-binding MF, only membrane/cytoplasm + one HT protein-binding IPI with TFCP2). The Hsp70-cochaperone assertion is genuine MF (the experimental HSC70-SGTA interaction), not an over-broad holdase claim.
- **Evidence alignment:** PN carries no row references. Review cites PMID:17034881 (HIGH relevance, UNVERIFIED/uncached primary functional paper) and PMID:25416956 (proteome-scale Y2H, TFCP2 HT hit). No divergence from PN.
- **Verdict:** Fully consistent; PN Hsp70-binding story already captured as core MF and experimentally supported via HSC70/SGTA. **Recommended edits:** none required.

## Full Consistency Review

- **UniProt:** Q9UF47 · **batch:** proteostasis-batch-2026-06-07b · **review status:** COMPLETE
- **PN placement:** `ER proteostasis|Chaperone|HSP70 system|J-domain containing HSP70 cochaperone` (branch ER) ; **PN-node mapping:** type → mapped/ok_for_propagation_to_go GO:0030544 Hsp70 protein binding (goa_status=more_specific_than_existing_goa); all ancestor nodes no_mapping.
- **Consistency:** Consistent. Deep research (notes), review and PN converge on DNAJC5B/CSP-beta as a testis-specific CSPalpha paralog (J domain aa 19-84) that interacts with the HSC70-SGTA chaperone complex and targets the trans-Golgi network as a non-palmitoylated CSP (PMID:17034881, Boal et al.). The review's core MF is exactly GO:0030544 Hsp70 protein binding, matching the PN projection. The TGN/secretory-pathway context makes the ER-branch placement reasonable. The HSC70/SGTA interaction is experimentally documented (not just family inference), so GO:0030544 here is better-supported than for the Tdark paralogs DNAJC4/DNAJC5G.
- **PN story / NEW pressure:** GO:0030544 is already the review's core MF → **already captured** (verified real). goa_status=more_specific_than_existing_goa is accurate (GOA had no chaperone-binding MF, only membrane/cytoplasm + one HT protein-binding IPI with TFCP2). The Hsp70-cochaperone assertion is genuine MF (the experimental HSC70-SGTA interaction), not an over-broad holdase claim.
- **Mapping strategy:** No change to the node. GO:0030544 is the correct breadth and is experimentally anchored for this gene.
- **Evidence alignment:** PN carries no row references. Review cites PMID:17034881 (HIGH relevance, UNVERIFIED/uncached primary functional paper) and PMID:25416956 (proteome-scale Y2H, TFCP2 HT hit). No divergence from PN.
- **Verdict:** Fully consistent; PN Hsp70-binding story already captured as core MF and experimentally supported via HSC70/SGTA. **Recommended edits:** none required.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07b
- review_yaml: genes/human/DNAJC5B/DNAJC5B-ai-review.yaml
- PN workbook rows: 1

## PN row 1: ER proteostasis | Chaperone | HSP70 system | J-domain containing HSP70 cochaperone
- UniProt: Q9UF47
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

## Projected GO annotations (1)
- GO:0030544 Hsp70 protein binding | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=ER proteostasis|Chaperone|HSP70 system|J-domain containing HSP70 cochaperone

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
