# DNAJC11 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9NVH1
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07b
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/DNAJC11/DNAJC11-ai-review.yaml](DNAJC11-ai-review.yaml)
- AIGR review HTML: present - [genes/human/DNAJC11/DNAJC11-ai-review.html](DNAJC11-ai-review.html)
- Gene notes: present - [genes/human/DNAJC11/DNAJC11-notes.md](DNAJC11-notes.md)
- GOA TSV: present - [genes/human/DNAJC11/DNAJC11-goa.tsv](DNAJC11-goa.tsv)
- UniProt record: present - [genes/human/DNAJC11/DNAJC11-uniprot.txt](DNAJC11-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/DNAJC11.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/DNAJC11.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/DNAJC11.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/DNAJC11.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: DNAJC11 is a mitochondrial protein of the DnaJ/Hsp40 (DNAJC) family with an N-terminal J domain and a C-terminal family-specific beta-barrel/coiled-coil region. Its full-length isoform is a peripheral protein of the mitochondrial outer membrane, and it is a component of the mitochondrial intermembrane space bridging (MIB) complex that links the inner-membrane MICOS (mitochondrial contact site and cristae organizing system) complex with the outer-membrane SAM (sorting and assembly machinery) complex. Through these associations DNAJC11 is required for proper mitochondrial inner-membrane organization and the formation of cristae and cristae junctions. In mice, a hypomorphic splicing mutation in DnaJC11 causes motor neuron pathology with cristae disorganization, muscle weakness, lymphoid abnormalities and early lethality, establishing a link between DNAJC11 and neuromuscular disease.
- Existing/core annotation action counts: ACCEPT: 11; KEEP_AS_NON_CORE: 5

## PN Consistency Summary

- **Consistency:** Contradiction. PN classifies DNAJC11 as a J-domain HSP70 co-chaperone and projects GO:0030544 Hsp70 binding. The review and notes explicitly state the opposite: DNAJC11's role is **structural** (MIB/MICOS/SAM, cristae organization); "no demonstrated HSP70 ATPase stimulation" and "DNAJC11's MF is not well-defined as a co-chaperone." The review deliberately assigns NO molecular-function/Hsp70-binding term and frames the gene around GO:0140275 (MIB complex), GO:0042407 (cristae formation), GO:0007007. GOA contains no GO:0030544 or even GO:0031072.
- **PN story / NEW pressure:** PN asserts an HSP70-cochaperone role that is NOT in GOA and NOT supported by literature. This is the classic over-broad J-domain holdase/cochaperone inference flagged in the task. There is no defensible NEW Hsp70-binding term here; the gene's verified biology (cristae/MIB) is already captured. The PN `goa_status=more_specific_than_existing_goa` is also factually wrong — GOA lacks the parent GO:0031072, so it could at best be `new_to_goa`, but the assertion itself is unsupported.
- **Evidence alignment:** PN row carries no titles; review anchors on PMID:25111180, 25997101, 26477565 (all verified, MIB/cristae). None supports Hsp70 binding. Full divergence from the PN cochaperone framing.
- **Verdict:** PN over-reaches — DNAJC11 is a structural MIB/cristae protein, not a demonstrated HSP70 cochaperone. **Recommended edits:** [MAP] remove/exempt DNAJC11 from GO:0030544 propagation under the "J-domain containing HSP70 cochaperone" type; its propagating terms are GO:0140275 / GO:0042407.

## Full Consistency Review

- **UniProt:** Q9NVH1 · **batch:** proteostasis-batch-2026-06-07b · **review status:** COMPLETE
- **PN placement:** `Mitochondrial proteostasis|Chaperone|HSP70 system|J-domain containing HSP70 cochaperone` ; **PN-node mapping:** type=mapped, scope=ok_for_propagation_to_go, GO:0030544 Hsp70 protein binding (group/class/branch = no_mapping)
- **Consistency:** Contradiction. PN classifies DNAJC11 as a J-domain HSP70 co-chaperone and projects GO:0030544 Hsp70 binding. The review and notes explicitly state the opposite: DNAJC11's role is **structural** (MIB/MICOS/SAM, cristae organization); "no demonstrated HSP70 ATPase stimulation" and "DNAJC11's MF is not well-defined as a co-chaperone." The review deliberately assigns NO molecular-function/Hsp70-binding term and frames the gene around GO:0140275 (MIB complex), GO:0042407 (cristae formation), GO:0007007. GOA contains no GO:0030544 or even GO:0031072.
- **PN story / NEW pressure:** PN asserts an HSP70-cochaperone role that is NOT in GOA and NOT supported by literature. This is the classic over-broad J-domain holdase/cochaperone inference flagged in the task. There is no defensible NEW Hsp70-binding term here; the gene's verified biology (cristae/MIB) is already captured. The PN `goa_status=more_specific_than_existing_goa` is also factually wrong — GOA lacks the parent GO:0031072, so it could at best be `new_to_goa`, but the assertion itself is unsupported.
- **Mapping strategy:** DNAJC11 should be treated as an exception to the J-domain-cochaperone type mapping (like the structural/non-canonical cases). Propagating GO:0030544 to DNAJC11 would assert an undemonstrated function. The node mapping is fine for genuine cochaperones but mis-includes DNAJC11.
- **Evidence alignment:** PN row carries no titles; review anchors on PMID:25111180, 25997101, 26477565 (all verified, MIB/cristae). None supports Hsp70 binding. Full divergence from the PN cochaperone framing.
- **Verdict:** PN over-reaches — DNAJC11 is a structural MIB/cristae protein, not a demonstrated HSP70 cochaperone. **Recommended edits:** [MAP] remove/exempt DNAJC11 from GO:0030544 propagation under the "J-domain containing HSP70 cochaperone" type; its propagating terms are GO:0140275 / GO:0042407.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07b
- review_yaml: genes/human/DNAJC11/DNAJC11-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Mitochondrial proteostasis | Chaperone | HSP70 system | J-domain containing HSP70 cochaperone
- UniProt: Q9NVH1
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
