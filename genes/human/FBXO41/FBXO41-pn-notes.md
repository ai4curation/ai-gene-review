# FBXO41 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q8TF61
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-13
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/FBXO41/FBXO41-ai-review.yaml](FBXO41-ai-review.yaml)
- AIGR review HTML: missing - genes/human/FBXO41/FBXO41-ai-review.html
- Gene notes: missing - genes/human/FBXO41/FBXO41-notes.md
- GOA TSV: present - [genes/human/FBXO41/FBXO41-goa.tsv](FBXO41-goa.tsv)
- UniProt record: present - [genes/human/FBXO41/FBXO41-uniprot.txt](FBXO41-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/FBXO41.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/FBXO41.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/FBXO41.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/FBXO41.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/FBXO41/FBXO41-deep-research-falcon.md](FBXO41-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: FBXO41 (F-box only protein 41; KIAA1940) is a brain/neuron-enriched member of the FBXO family of F-box proteins. F-box proteins serve as the substrate-recognition (receptor/adaptor) subunits of SCF (SKP1-CUL1-RBX1-F-box) Cullin-RING E3 ubiquitin ligase complexes: the F-box motif docks the protein onto the SKP1-CUL1 scaffold, while a separate substrate-binding region recruits target proteins for poly-ubiquitination, committing them to proteasomal degradation. FBXO41 carries a C-terminal F-box domain together with an N-terminal C2H2 zinc-finger-like region, a long predicted coiled-coil, and extensive intrinsically disordered/low-complexity regions, and by sequence similarity is predicted to assemble into an SCF complex through direct interaction with SKP1 and CUL1. FBXO41 is a neuron-specific/CNS-enriched protein (expressed from early embryogenesis, abundant postnatally in cerebellum and hippocampus; not detected in astrocytes or oligodendrocytes). It is cytoplasmic and excluded from the nucleus, with a prominent centrosomal/pericentriolar pool: in neurons FBXO41 localizes adjacent to centriole markers and co-fractionates with centrosomes, and this targeting requires both its coiled-coil and F-box domains. Functionally, increased centrosomal/centriolar accumulation of FBXO41 promotes disassembly/shortening of neuronal primary cilia and thereby modulates the cilium-dependent Sonic hedgehog (Shh) pathway; this cilia disassembly activity depends on actin-cytoskeleton remodeling and, in mitotic contexts, on Aurora A kinase. F-box deletion or an F-box point mutation (W577A) abolishes SKP1/CUL1 binding, and a centrosome-localized F-box mutant fails to drive cilia shortening, indicating that FBXO41's biological activity is coupled to SCF/CRL assembly. In vivo, loss of Fbxo41 in mice causes cerebellar granule neuron migration defects, an ataxia-like phenotype and cerebellar neurodegeneration. Its direct, broadly validated ubiquitination substrate repertoire remains unestablished; a less-replicated (thesis-level) model proposes an FBXO41-CUL7 complex mediating non-proteolytic K63-linked ubiquitination of neurofilament medium (NFM) to promote axon growth, alongside proposed interactions with DISC1 and NDEL1. A rare homozygous human variant (p.Arg317Gln) has been reported segregating with a neurologic phenotype, and FBXO41 shows altered DNA methylation in 22q11.2 deletion syndrome.
- Existing/core annotation action counts: ACCEPT: 1; KEEP_AS_NON_CORE: 13; NEW: 2

## PN Consistency Summary

- **Consistency:** Consistent. Deep research (Falcon) and review YAML agree on a neuron-specific SCF F-box protein with a centrosomal pool driving cilia disassembly and cerebellar granule-neuron migration. Both primary studies (PMID:31160656, PMID:26063905) are cached full-text and the review correctly states they were read in full (verified: full_text_available=true). PN dossier (generic F-box adaptor) is narrower than the rich review biology but not contradictory. Note: PN/UniProt put the auxiliary domain as LRR, whereas the review describes an N-terminal C2H2 zinc-finger + coiled-coil (not LRR) — a minor domain-annotation divergence, not a functional contradiction.
- **PN story / NEW pressure:** PN asserts only the generic adaptor role. Review adds two verified NEW terms by ISO from mouse/rat: GO:0061523 cilium disassembly (OLS-verified) and GO:0001764 neuron migration — both directly assayed in the read full texts. Defensible. Conclusion: **ADD** GO:0061523 + GO:0001764 (present in review). Core SCF adaptor MF (GO:1990756) already captured; no validated ubiquitination substrate (CUL7/NFM is thesis-level, held preliminary — appropriate).
- **Evidence alignment:** PN cites only "15340381 / rev." Review anchors on PMID:31160656 and PMID:26063905 (both HIGH/VERIFIED, full text) plus GO_REF:0000107, PMID:34445249, Falcon, Reactome. Strong divergence: review carries the experimental primaries PN lacks.
- **Verdict:** Consistent; well-evidenced verified NEW terms. ACCEPT review. **Recommended edits:** none for YAML; optionally [MAP] note FBXO41 auxiliary domain may be C2H2/coiled-coil rather than LRR in the PN workbook.

## Full Consistency Review

- **UniProt:** Q8TF61 · **batch:** proteostasis-batch-2026-06-13 · **review status:** COMPLETE
- **PN placement:** `UPS|E3 ubiquitin and UBL ligases|Cul1 substrate receptor|F-box|LRR` ; **PN-node mapping:** F-box subtype/type = no_mapping; group = mapped, ok_for_propagation_to_go, GO:1990756; class = context_only/too_broad (GO:0061630).
- **Consistency:** Consistent. Deep research (Falcon) and review YAML agree on a neuron-specific SCF F-box protein with a centrosomal pool driving cilia disassembly and cerebellar granule-neuron migration. Both primary studies (PMID:31160656, PMID:26063905) are cached full-text and the review correctly states they were read in full (verified: full_text_available=true). PN dossier (generic F-box adaptor) is narrower than the rich review biology but not contradictory. Note: PN/UniProt put the auxiliary domain as LRR, whereas the review describes an N-terminal C2H2 zinc-finger + coiled-coil (not LRR) — a minor domain-annotation divergence, not a functional contradiction.
- **PN story / NEW pressure:** PN asserts only the generic adaptor role. Review adds two verified NEW terms by ISO from mouse/rat: GO:0061523 cilium disassembly (OLS-verified) and GO:0001764 neuron migration — both directly assayed in the read full texts. Defensible. Conclusion: **ADD** GO:0061523 + GO:0001764 (present in review). Core SCF adaptor MF (GO:1990756) already captured; no validated ubiquitination substrate (CUL7/NFM is thesis-level, held preliminary — appropriate).
- **Mapping strategy:** Gene does not change the shared node. GO:1990756 matches; the neuron-specific cilia/migration terms are correctly kept in the review (substrate/process-specific) rather than propagated to the broad PN group node.
- **Evidence alignment:** PN cites only "15340381 / rev." Review anchors on PMID:31160656 and PMID:26063905 (both HIGH/VERIFIED, full text) plus GO_REF:0000107, PMID:34445249, Falcon, Reactome. Strong divergence: review carries the experimental primaries PN lacks.
- **Verdict:** Consistent; well-evidenced verified NEW terms. ACCEPT review. **Recommended edits:** none for YAML; optionally [MAP] note FBXO41 auxiliary domain may be C2H2/coiled-coil rather than LRR in the PN workbook.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-13
- review_yaml: genes/human/FBXO41/FBXO41-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Ubiquitin Proteasome System | E3 ubiquitin and UBL ligases | Cul1 substrate receptor | F-box | LRR
- UniProt: Q8TF61
- In branches: UPS
- Signature domains: IPR001810
- Auxiliary domains: IPR032675
- PN references (titles):
    - 15340381 / rev
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul1 substrate receptor|F-box|LRR
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower substrate-receptor, adaptor, domain, or family subdivision already covered by the curated parent adaptor/receptor mapping. No additional direct GO mapping is needed at this node.
    - [type] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul1 substrate receptor|F-box
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower substrate-receptor, adaptor, domain, or family subdivision already covered by the curated parent adaptor/receptor mapping. No additional direct GO mapping is needed at this node.
    - [group] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul1 substrate receptor
        status=mapped scope=ok_for_propagation_to_go GO=[GO:1990756 ubiquitin-like ligase-substrate adaptor activity]
        rationale: This PN group captures substrate receptors/adaptors for cullin/UBL ligase systems. The shared GO molecular-function target is ubiquitin-like ligase-substrate adaptor activity.
    - [class] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases
        status=context_only scope=too_broad_to_propagate GO=[GO:0061630 ubiquitin protein ligase activity]
        rationale: This class is a genuine E3-ligase context, but its descendants include catalytic ligases, cullin scaffolds, substrate receptors, adaptors, cofactors, regulators, and UBL modifier systems. A class-level propagation would over-annotate.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## Projected GO annotations (1)
- GO:1990756 ubiquitin-like ligase-substrate adaptor activity | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul1 substrate receptor

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
