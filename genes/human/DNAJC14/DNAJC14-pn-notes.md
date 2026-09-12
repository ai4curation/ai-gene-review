# DNAJC14 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q6Y2X3
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07b
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/DNAJC14/DNAJC14-ai-review.yaml](DNAJC14-ai-review.yaml)
- AIGR review HTML: present - [genes/human/DNAJC14/DNAJC14-ai-review.html](DNAJC14-ai-review.html)
- Gene notes: present - [genes/human/DNAJC14/DNAJC14-notes.md](DNAJC14-notes.md)
- GOA TSV: present - [genes/human/DNAJC14/DNAJC14-goa.tsv](DNAJC14-goa.tsv)
- UniProt record: present - [genes/human/DNAJC14/DNAJC14-uniprot.txt](DNAJC14-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/DNAJC14.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/DNAJC14.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/DNAJC14.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/DNAJC14.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: DNAJC14 (DRIP78, "dopamine receptor-interacting protein of 78 kDa"; also HDJ3/hDj-3) is a multi-pass endoplasmic reticulum membrane protein of the DnaJ/HSP40 subfamily C. It contains a cytoplasmically oriented J domain and a family-defining Jiv (Jiv90) domain, and acts as an ER-resident co-chaperone that regulates the export of client membrane proteins from the ER to the cell surface. Its best-characterized client is the dopamine D1 receptor (DRD1), which it binds via an FxxxFxxxF ER-export motif through its C-terminal domain, controlling DRD1 maturation and delivery to the plasma membrane; it has been implicated more broadly in G-protein-coupled receptor trafficking. The Jiv domain is also a host factor exploited during flavivirus/pestivirus RNA replication. DNAJC14 is highly expressed in pancreas and is also expressed in brain, lung, liver, skeletal muscle and kidney.
- Existing/core annotation action counts: ACCEPT: 4; KEEP_AS_NON_CORE: 3

## PN Consistency Summary

- **Consistency:** Tension. PN projects GO:0030544 (Hsp70 binding) as the cochaperone MF. The review and notes describe DNAJC14 as a multi-pass ER-membrane J-protein whose documented function is GPCR ER-export chaperoning (binds DRD1 via FxxxFxxxF motif); the review's core MF is GO:0050780 (dopamine receptor binding) / GO:0001664 (GPCR binding). The review explicitly states the J-domain HSP70-cochaperone activity is **inferred but the functional readout is GPCR ER export** and there is no cached experimental human paper for a direct HSP70 interaction. GOA contains no GO:0030544 or GO:0031072. So PN's Hsp70-binding claim is unverified for this gene.
- **PN story / NEW pressure:** GO:0030544 is verified real but, for DNAJC14, asserts an HSP70 interaction that is neither in GOA nor experimentally cited — the review even lists "does DNAJC14 recruit an ER HSP70" as an open suggested_question. This is over-broad J-domain inference. The gene's actual, supported biology (dopamine/GPCR receptor binding, ER export) is captured (GO:0050780, GO:0001664). No defensible NEW Hsp70 term; the cochaperone MF here is speculative.
- **Evidence alignment:** PN carries no titles; review evidence is UniProt (by similarity) + IBA/IEA for DRD1/GPCR binding (PMID:11331877 cited in notes, not GOA; PMID:19946888 only for membrane). No paper supports direct Hsp70 binding. Divergence from PN cochaperone framing.
- **Verdict:** PN over-reaches — Hsp70 binding unverified; DNAJC14's supported function is GPCR ER export. **Recommended edits:** [MAP] do not propagate GO:0030544 to DNAJC14 (mark cochaperone MF unverified); retain GO:0050780 / GO:0001664 as the gene-level MF.

## Full Consistency Review

- **UniProt:** Q6Y2X3 (DRIP78) · **batch:** proteostasis-batch-2026-06-07b · **review status:** COMPLETE
- **PN placement:** `ER proteostasis|Chaperone|HSP70 system|J-domain containing HSP70 cochaperone` ; **PN-node mapping:** type=mapped, scope=ok_for_propagation_to_go, GO:0030544 Hsp70 protein binding (group/class/branch = no_mapping)
- **Consistency:** Tension. PN projects GO:0030544 (Hsp70 binding) as the cochaperone MF. The review and notes describe DNAJC14 as a multi-pass ER-membrane J-protein whose documented function is GPCR ER-export chaperoning (binds DRD1 via FxxxFxxxF motif); the review's core MF is GO:0050780 (dopamine receptor binding) / GO:0001664 (GPCR binding). The review explicitly states the J-domain HSP70-cochaperone activity is **inferred but the functional readout is GPCR ER export** and there is no cached experimental human paper for a direct HSP70 interaction. GOA contains no GO:0030544 or GO:0031072. So PN's Hsp70-binding claim is unverified for this gene.
- **PN story / NEW pressure:** GO:0030544 is verified real but, for DNAJC14, asserts an HSP70 interaction that is neither in GOA nor experimentally cited — the review even lists "does DNAJC14 recruit an ER HSP70" as an open suggested_question. This is over-broad J-domain inference. The gene's actual, supported biology (dopamine/GPCR receptor binding, ER export) is captured (GO:0050780, GO:0001664). No defensible NEW Hsp70 term; the cochaperone MF here is speculative.
- **Mapping strategy:** Propagating GO:0030544 to DNAJC14 over-states the evidence (parallel to DNAJC11/DNAJC13 but weaker still — no demonstrated ATPase activator role either). Better to leave DNAJC14's propagating MF as its receptor-binding / ER-export terms and treat the HSP70-cochaperone assignment as unverified.
- **Evidence alignment:** PN carries no titles; review evidence is UniProt (by similarity) + IBA/IEA for DRD1/GPCR binding (PMID:11331877 cited in notes, not GOA; PMID:19946888 only for membrane). No paper supports direct Hsp70 binding. Divergence from PN cochaperone framing.
- **Verdict:** PN over-reaches — Hsp70 binding unverified; DNAJC14's supported function is GPCR ER export. **Recommended edits:** [MAP] do not propagate GO:0030544 to DNAJC14 (mark cochaperone MF unverified); retain GO:0050780 / GO:0001664 as the gene-level MF.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07b
- review_yaml: genes/human/DNAJC14/DNAJC14-ai-review.yaml
- PN workbook rows: 1

## PN row 1: ER proteostasis | Chaperone | HSP70 system | J-domain containing HSP70 cochaperone
- UniProt: Q6Y2X3
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
