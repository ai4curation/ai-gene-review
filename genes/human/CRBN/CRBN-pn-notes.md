# CRBN PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q96SW2
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/CRBN/CRBN-ai-review.yaml](CRBN-ai-review.yaml)
- AIGR review HTML: present - [genes/human/CRBN/CRBN-ai-review.html](CRBN-ai-review.html)
- Gene notes: present - [genes/human/CRBN/CRBN-notes.md](CRBN-notes.md)
- GOA TSV: present - [genes/human/CRBN/CRBN-goa.tsv](CRBN-goa.tsv)
- UniProt record: present - [genes/human/CRBN/CRBN-uniprot.txt](CRBN-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/CRBN.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/CRBN.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/CRBN.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/CRBN.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: CRBN (cereblon) is the substrate-recognition subunit of a CRL4 cullin-RING E3 ubiquitin ligase, the DCX/CRL4(CRBN) complex composed of DDB1, CUL4A or CUL4B, RBX1 and CRBN. Through an N-terminal Lon-protease-like domain it binds the adaptor DDB1, and through a C-terminal thalidomide-binding (CULT) domain that coordinates a structural Zn2+ ion it recruits substrate proteins for ubiquitination and subsequent proteasomal degradation. Endogenous substrates include MEIS2, glutamine synthetase (GLUL) and ILF2, and the complex is required for normal limb outgrowth and FGF8 expression in vertebrates. CRBN also regulates neuronal large-conductance Ca2+-activated potassium (BK) channels via interaction with KCNT1, contributing to presynaptic glutamate release, memory and learning; loss-of-function variants cause autosomal recessive intellectual developmental disorder. The CULT domain is the direct molecular target of thalidomide, lenalidomide and pomalidomide (IMiDs) and of newer molecular-glue and PROTAC degraders, which act as molecular glues that reprogram CRBN substrate specificity to recruit neosubstrates such as IKZF1, IKZF3, SALL4, CK1alpha and GSPT1 for degradation. CRBN is expressed widely and most highly in brain, and localizes to cytoplasm, nucleus and peripheral membranes.
- Existing/core annotation action counts: ACCEPT: 14; KEEP_AS_NON_CORE: 10; MARK_AS_OVER_ANNOTATED: 8; NEW: 1

## PN Consistency Summary

- **Consistency:** Consistent and well-judged. Review describes CRBN as the substrate-recognition subunit of CRL4(CRBN) (DDB1/CUL4A or CUL4B/RBX1), with the CULT domain as the IMiD/molecular-glue/neosubstrate-binding module. PN annotation (Cul4 substrate receptor, LON/Yippee/DOC domain family; auxiliary domains IPR003111/IPR004910/IPR004939; ref 17588513) and PN-node mapping align with this exactly.
- **PN story / NEW pressure:** PN projects GO:1990756 ubiquitin-like ligase-substrate adaptor activity (verified real OLS; definition "brings together a ubiquitin-like ligase and its substrate"). This is NOT in the current GOA (grep confirms absence) — GOA's only MF is bare GO:0005515. The review independently proposes the SAME term as a NEW IDA annotation (from PMID:26909574). Perfect convergence. Conclusion: **ADD** GO:1990756 — defensible, verified, and the precise adaptor MF CRBN lacks in GOA.
- **Evidence alignment:** PN cites 17588513 (CRBN-domain/cereblon ref). Review's adaptor-MF evidence is PMID:26909574 (+ PMID:25108355, PMID:20223979). Different but compatible anchors, both establishing the substrate-receptor/adaptor role; high-throughput GO:0005515 PMIDs correctly marked over-annotated. No conflict.
- **Verdict:** Consistent; PN GO:1990756 adaptor mapping verified, matches review's NEW term, and correctly avoids over-broad CRL4 ligase terms. **Recommended edits:** none (PN and review already converge on GO:1990756).

## Full Consistency Review

- **UniProt:** Q96SW2 · **batch:** proteostasis-batch-2026-06-07 · **review status:** COMPLETE
- **PN placement:** `Ubiquitin Proteasome System | E3 ubiquitin and UBL ligases | Cul4A/Cul4B substrate receptor | non-WD40 | LON, Yippee, DOC` ; **PN-node mapping:** group (Cul4A/Cul4B substrate receptor)=mapped, scope=ok_for_propagation_to_go, GO:1990756 ubiquitin-like ligase-substrate adaptor activity; class (E3 ligases)=context_only, scope=too_broad_to_propagate, GO:0061630 ubiquitin protein ligase activity; subtype/type/branch = no_mapping
- **Consistency:** Consistent and well-judged. Review describes CRBN as the substrate-recognition subunit of CRL4(CRBN) (DDB1/CUL4A or CUL4B/RBX1), with the CULT domain as the IMiD/molecular-glue/neosubstrate-binding module. PN annotation (Cul4 substrate receptor, LON/Yippee/DOC domain family; auxiliary domains IPR003111/IPR004910/IPR004939; ref 17588513) and PN-node mapping align with this exactly.
- **PN story / NEW pressure:** PN projects GO:1990756 ubiquitin-like ligase-substrate adaptor activity (verified real OLS; definition "brings together a ubiquitin-like ligase and its substrate"). This is NOT in the current GOA (grep confirms absence) — GOA's only MF is bare GO:0005515. The review independently proposes the SAME term as a NEW IDA annotation (from PMID:26909574). Perfect convergence. Conclusion: **ADD** GO:1990756 — defensible, verified, and the precise adaptor MF CRBN lacks in GOA.
- **Mapping strategy:** Correct, and notably careful re the task's CRBN caution. The PN deliberately avoids over-broad CRL4 ligase terms: it marks the E3-ligase class as context_only / too_broad_to_propagate (GO:0061630 not propagated) and propagates only the substrate-receptor group → GO:1990756 (adaptor, not catalytic ligase). This matches the review, which represents CRBN as adaptor (GO:1990756) + complex membership (GO:0031464/0031465), never as the catalytic ligase. No broadening problem.
- **Evidence alignment:** PN cites 17588513 (CRBN-domain/cereblon ref). Review's adaptor-MF evidence is PMID:26909574 (+ PMID:25108355, PMID:20223979). Different but compatible anchors, both establishing the substrate-receptor/adaptor role; high-throughput GO:0005515 PMIDs correctly marked over-annotated. No conflict.
- **Verdict:** Consistent; PN GO:1990756 adaptor mapping verified, matches review's NEW term, and correctly avoids over-broad CRL4 ligase terms. **Recommended edits:** none (PN and review already converge on GO:1990756).

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07
- review_yaml: genes/human/CRBN/CRBN-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Ubiquitin Proteasome System | E3 ubiquitin and UBL ligases | Cul4A/Cul4B substrate receptor | non-WD40 | LON, Yippee, DOC
- UniProt: Q96SW2
- In branches: UPS
- Signature domains: (none)
- Auxiliary domains: IPR003111, IPR004910, IPR004939
- PN references (titles):
    - 17588513 rev
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul4A/Cul4B substrate receptor|non-WD40|LON, Yippee, DOC
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower substrate-receptor, adaptor, domain, or family subdivision already covered by the curated parent adaptor/receptor mapping. No additional direct GO mapping is needed at this node.
    - [type] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul4A/Cul4B substrate receptor|non-WD40
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower substrate-receptor, adaptor, domain, or family subdivision already covered by the curated parent adaptor/receptor mapping. No additional direct GO mapping is needed at this node.
    - [group] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul4A/Cul4B substrate receptor
        status=mapped scope=ok_for_propagation_to_go GO=[GO:1990756 ubiquitin-like ligase-substrate adaptor activity]
        rationale: This PN group captures substrate receptors/adaptors for cullin/UBL ligase systems. The shared GO molecular-function target is ubiquitin-like ligase-substrate adaptor activity.
    - [class] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases
        status=context_only scope=too_broad_to_propagate GO=[GO:0061630 ubiquitin protein ligase activity]
        rationale: This class is a genuine E3-ligase context, but its descendants include catalytic ligases, cullin scaffolds, substrate receptors, adaptors, cofactors, regulators, and UBL modifier systems. A class-level propagation would over-annotate.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## Projected GO annotations (1)
- GO:1990756 ubiquitin-like ligase-substrate adaptor activity | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul4A/Cul4B substrate receptor

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
