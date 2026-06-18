# DNAJC19 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q96DA6
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07b
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/DNAJC19/DNAJC19-ai-review.yaml](DNAJC19-ai-review.yaml)
- AIGR review HTML: present - [genes/human/DNAJC19/DNAJC19-ai-review.html](DNAJC19-ai-review.html)
- Gene notes: present - [genes/human/DNAJC19/DNAJC19-notes.md](DNAJC19-notes.md)
- GOA TSV: present - [genes/human/DNAJC19/DNAJC19-goa.tsv](DNAJC19-goa.tsv)
- UniProt record: present - [genes/human/DNAJC19/DNAJC19-uniprot.txt](DNAJC19-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/DNAJC19.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/DNAJC19.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/DNAJC19.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/DNAJC19.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: DNAJC19 (TIM14/TIMM14; DnaJ homolog subfamily C member 19) is a J-domain co-chaperone of the mitochondrial inner membrane. It is a single-pass inner-membrane protein with a short intermembrane-space N-terminus, one transmembrane helix, and a matrix-facing J-domain. As the J-protein of the presequence translocase-associated import motor (PAM), it stimulates the ATPase activity of matrix mitochondrial HSP70 (mortalin/HSPA9) to drive ATP-dependent translocation of presequence-bearing precursor proteins from the TIM23 channel into the matrix. It forms a regulatory heterodimeric subcomplex with PAM16/Magmas (TIMM16), which restrains its HSP70-stimulating activity, and is tethered to the TIM23 translocase. DNAJC19 also associates with the prohibitin complex via PHB2 and has been implicated in cardiolipin remodeling. Biallelic loss-of-function variants cause dilated cardiomyopathy with ataxia (DCMA) syndrome / 3-methylglutaconic aciduria type 5.
- Existing/core annotation action counts: ACCEPT: 10; KEEP_AS_NON_CORE: 12

## PN Consistency Summary

- **Consistency:** Strong agreement. Notes, review and PN node all describe the prototypical TIM23/PAM J-protein that stimulates matrix HSP70 (mortalin/HSPA9). Experimentally established for the human protein (PMID:20053669: ~70% ATPase stimulation in the Magmas:DnaJC19 complex; PMID:19564938). No contradictions. This is the best-supported member of the six (vs DNAJC15's PAM18-orthologue role; correctly distinguished as the genuine TIM23-associated import J-protein).
- **PN story / NEW pressure:** PN proposes GO:0030544 Hsp70 protein binding (verified real). The binding is genuine (DNAJC19 directly engages/stimulates mortalin), but the review already records the stronger, more informative GO:0001671 ATPase activator activity (experimentally supported). GO:0030544 is NOT a parent of GO:0001671 — it is the binding axis, broader/less informative than the existing activator-activity annotation. Not an ADD; the function is already captured better.
- **Evidence alignment:** Excellent overlap on the import-motor biology. Review anchors on PMID:20053669 and PMID:19564938 (both VERIFIED) plus the DCMA disease paper PMID:16055927 (UNVERIFIED, uncached). PN reference titles align with the J-domain/Hsp70-stimulation framing.
- **Verdict:** Consistent and well-supported; PN's Hsp70-binding projection is true but already captured more informatively (ATPase activator activity). No edits required.

## Full Consistency Review

- **UniProt:** Q96DA6 (TIM14/TIMM14) · **batch:** proteostasis-batch-2026-06-07b · **review status:** COMPLETE
- **PN placement:** `Mitochondrial proteostasis | Chaperone | HSP70 system | J-domain containing HSP70 cochaperone` (branch MI) ; **PN-node mapping:** type=mapped, scope=ok_for_propagation_to_go, GO:0030544 Hsp70 protein binding (goa_status=more_specific_than_existing_goa)
- **Consistency:** Strong agreement. Notes, review and PN node all describe the prototypical TIM23/PAM J-protein that stimulates matrix HSP70 (mortalin/HSPA9). Experimentally established for the human protein (PMID:20053669: ~70% ATPase stimulation in the Magmas:DnaJC19 complex; PMID:19564938). No contradictions. This is the best-supported member of the six (vs DNAJC15's PAM18-orthologue role; correctly distinguished as the genuine TIM23-associated import J-protein).
- **PN story / NEW pressure:** PN proposes GO:0030544 Hsp70 protein binding (verified real). The binding is genuine (DNAJC19 directly engages/stimulates mortalin), but the review already records the stronger, more informative GO:0001671 ATPase activator activity (experimentally supported). GO:0030544 is NOT a parent of GO:0001671 — it is the binding axis, broader/less informative than the existing activator-activity annotation. Not an ADD; the function is already captured better.
- **Mapping strategy:** No node change warranted. As with DNAJC15, "more_specific_than_existing_goa" is inaccurate — GO:0030544 is not more specific than the existing GO:0001671 ATPase activator activity. The secondary cardiolipin/prohibitin role (ISS, GO:1900208) sits outside this node and is correctly non-core in the review.
- **Evidence alignment:** Excellent overlap on the import-motor biology. Review anchors on PMID:20053669 and PMID:19564938 (both VERIFIED) plus the DCMA disease paper PMID:16055927 (UNVERIFIED, uncached). PN reference titles align with the J-domain/Hsp70-stimulation framing.
- **Verdict:** Consistent and well-supported; PN's Hsp70-binding projection is true but already captured more informatively (ATPase activator activity). No edits required.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07b
- review_yaml: genes/human/DNAJC19/DNAJC19-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Mitochondrial proteostasis | Chaperone | HSP70 system | J-domain containing HSP70 cochaperone
- UniProt: Q96DA6
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
