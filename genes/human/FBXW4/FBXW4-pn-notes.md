# FBXW4 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: P57775
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-13
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/FBXW4/FBXW4-ai-review.yaml](FBXW4-ai-review.yaml)
- AIGR review HTML: missing - genes/human/FBXW4/FBXW4-ai-review.html
- Gene notes: missing - genes/human/FBXW4/FBXW4-notes.md
- GOA TSV: present - [genes/human/FBXW4/FBXW4-goa.tsv](FBXW4-goa.tsv)
- UniProt record: present - [genes/human/FBXW4/FBXW4-uniprot.txt](FBXW4-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/FBXW4.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/FBXW4.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/FBXW4.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/FBXW4.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/FBXW4/FBXW4-deep-research-falcon.md](FBXW4-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: FBXW4 (dactylin; SHFM3) is a member of the F-box/WD40 (FBXW) family of proteins. Its 412-residue product contains an N-terminal F-box motif (approximately residues 25-71) and a C-terminal beta-propeller built from roughly six WD40 repeats. F-box proteins function as the interchangeable substrate-recognition subunits of SCF (SKP1-CUL1-F-box)-type cullin-RING E3 ubiquitin ligase complexes: the F-box motif docks the protein onto SKP1/CUL1, while the WD40 propeller recognizes (typically phosphorylated) substrate proteins and presents them for ubiquitination by the RBX1-bound E2, committing them to proteasomal degradation. Affinity-purification studies confirm that FBXW4 assembles, in an F-box-dependent manner, with the canonical SCF core subunits SKP1, CUL1 and RBX1 and with COP9 signalosome subunits (which deneddylate and regulate cullin-RING ligases), and that FBXW4 associates with ubiquitinated cellular proteins in a manner enhanced by proteasome inhibition - establishing it as a bona fide SCF substrate receptor engaged in ubiquitin-dependent turnover. Its physiological substrates, however, remain undefined. FBXW4 is broadly expressed (including brain, kidney, lung and liver) and is recurrently mutated, deleted, or under-expressed across human cancers, suggesting a candidate tumor-suppressor role. The human gene maps to chromosome 10q24.3 within the critical region for split-hand/foot malformation type 3 (SHFM3), and the orthologous gene is disrupted in the mouse dactylaplasia (Dac) mutant, which fails to maintain the apical ectodermal ridge and truncates the autopod. SHFM3 is most often associated with tandem/discontinuous genomic duplications at 10q24 that perturb a shared cis-regulatory neighborhood and alter expression of FBXW4 and several neighboring genes (e.g. BTRC, POLL, LBX1) rather than with coding mutations in FBXW4 itself, so FBXW4's precise contribution to limb development and its physiological ubiquitination substrates remain incompletely defined.
- Existing/core annotation action counts: ACCEPT: 6; KEEP_AS_NON_CORE: 16

## PN Consistency Summary

- **Consistency:** Row1 consistent — review treats FBXW4 (dactylin/SHFM3) as an SCF substrate receptor (GO:0019005 IBA/NAS ACCEPT, GO:0031146 ACCEPT, proposed_new_terms GO:1990756) with substrates UNDEFINED; deep research (Lockwood 2013) confirms F-box-dependent SKP1/CUL1/RBX1 + COP9 assembly and MG132-dependent association with ubiquitinated proteins. **Row2 INCONSISTENT/over-reach:** the PN "idiosyncratic Ub binding | E3 ligase" node projects GO:0061630 (catalytic ubiquitin protein **ligase** activity). PMID:21070969 (Pashkova 2010, Mol Cell, [DOI](https://doi.org/10.1016/j.molcel.2010.10.018)) — per PubMed, "WD40 repeat propellers define a ubiquitin-**binding** domain that regulates turnover of F box proteins" — describes the WD40 propeller as a ubiquitin-BINDING module promoting F-box **auto-ubiquitination/turnover**, NOT ligase catalysis. F-box proteins are non-catalytic receptors (catalysis is RBX1 RING). Both the paper's content and the F-box pattern contradict GO:0061630.
- **PN story / NEW pressure:** Row1 ADD GO:1990756 (verified real, new_to_goa) — defensible, already proposed by review. Row2 GO:0061630 over-reaches twice (wrong activity type AND wrong paper interpretation). If anything, PMID:21070969 supports GO:0043130 ubiquitin binding (verified real; molecular function), not ligase activity. Limb-development role (SHFM3, dactylaplasia) is correctly KEEP_AS_NON_CORE / positional, not a molecular function.
- **Evidence alignment:** Row1 PN cites PMID:15340381 (family review). Review uses PMID:10405324/PMID:10471509 (SHFM3/dactylaplasia, HIGH), PMID:10945468, plus falcon (Lockwood 2013). Row2 PN's PMID:21070969 is NOT in the review and its claim (Ub-binding) is mischaracterized by the GO:0061630 mapping.
- **Verdict:** Row1 CONSISTENT (ADD GO:1990756). Row2 PN node OVER-REACHES. **Recommended edits:** [MAP] change Row2 group `Ubiquitin and UBL binding|E3 ligase` projection for FBXW4 from GO:0061630 ubiquitin protein ligase activity to GO:0043130 ubiquitin binding, or set no_mapping — PMID:21070969 documents WD40 ubiquitin BINDING (regulating F-box turnover), not catalytic ligase activity; F-box proteins are non-catalytic.

## Full Consistency Review

- **UniProt:** P57775 · **batch:** proteostasis-batch-2026-06-13 · **review status:** COMPLETE
- **PN placement (2 rows):** Row1 `UPS|E3 ubiquitin and UBL ligases|Cul1 substrate receptor|F-box|WD40` (PMID:15340381); Row2 `UPS|Ubiquitin and UBL binding|E3 ligase|CUL1 receptor|idiosyncratic Ub binding / WD40` (PMID:21070969). **PN-node mapping:** Row1 group=mapped GO:1990756; Row2 group=mapped GO:0061630 ubiquitin protein ligase activity (new_to_goa); both class nodes context_only/too_broad.
- **Consistency:** Row1 consistent — review treats FBXW4 (dactylin/SHFM3) as an SCF substrate receptor (GO:0019005 IBA/NAS ACCEPT, GO:0031146 ACCEPT, proposed_new_terms GO:1990756) with substrates UNDEFINED; deep research (Lockwood 2013) confirms F-box-dependent SKP1/CUL1/RBX1 + COP9 assembly and MG132-dependent association with ubiquitinated proteins. **Row2 INCONSISTENT/over-reach:** the PN "idiosyncratic Ub binding | E3 ligase" node projects GO:0061630 (catalytic ubiquitin protein **ligase** activity). PMID:21070969 (Pashkova 2010, Mol Cell, [DOI](https://doi.org/10.1016/j.molcel.2010.10.018)) — per PubMed, "WD40 repeat propellers define a ubiquitin-**binding** domain that regulates turnover of F box proteins" — describes the WD40 propeller as a ubiquitin-BINDING module promoting F-box **auto-ubiquitination/turnover**, NOT ligase catalysis. F-box proteins are non-catalytic receptors (catalysis is RBX1 RING). Both the paper's content and the F-box pattern contradict GO:0061630.
- **PN story / NEW pressure:** Row1 ADD GO:1990756 (verified real, new_to_goa) — defensible, already proposed by review. Row2 GO:0061630 over-reaches twice (wrong activity type AND wrong paper interpretation). If anything, PMID:21070969 supports GO:0043130 ubiquitin binding (verified real; molecular function), not ligase activity. Limb-development role (SHFM3, dactylaplasia) is correctly KEEP_AS_NON_CORE / positional, not a molecular function.
- **Mapping strategy:** Row1 correct. **Row2 mapping is wrong:** GO:0061630 should not be projected to F-box receptors from this Ub-binding paper. Recommend the Row2 node project GO:0043130 ubiquitin binding (if at all) or no_mapping — analogous to FBXW7's IBA ubiquitin-binding which the curator marked over-annotated.
- **Evidence alignment:** Row1 PN cites PMID:15340381 (family review). Review uses PMID:10405324/PMID:10471509 (SHFM3/dactylaplasia, HIGH), PMID:10945468, plus falcon (Lockwood 2013). Row2 PN's PMID:21070969 is NOT in the review and its claim (Ub-binding) is mischaracterized by the GO:0061630 mapping.
- **Verdict:** Row1 CONSISTENT (ADD GO:1990756). Row2 PN node OVER-REACHES. **Recommended edits:** [MAP] change Row2 group `Ubiquitin and UBL binding|E3 ligase` projection for FBXW4 from GO:0061630 ubiquitin protein ligase activity to GO:0043130 ubiquitin binding, or set no_mapping — PMID:21070969 documents WD40 ubiquitin BINDING (regulating F-box turnover), not catalytic ligase activity; F-box proteins are non-catalytic.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-13
- review_yaml: genes/human/FBXW4/FBXW4-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Ubiquitin Proteasome System | E3 ubiquitin and UBL ligases | Cul1 substrate receptor | F-box | WD40
- UniProt: P57775
- In branches: UPS
- Signature domains: IPR001810
- Auxiliary domains: IPR001680
- PN references (titles):
    - 15340381 / rev
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul1 substrate receptor|F-box|WD40
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

## PN row 2: Ubiquitin Proteasome System | Ubiquitin and UBL binding | E3 ligase | CUL1 receptor | idiosyncratic Ub binding / WD40
- UniProt: P57775
- In branches: UPS
- Signature domains: PMID: 21070969 (IPR001680)
- Auxiliary domains: IPR001810
- PN references (titles):
    - 21070969
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|Ubiquitin and UBL binding|E3 ligase|CUL1 receptor|idiosyncratic Ub binding / WD40
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower enzyme-family, domain, or architecture subdivision already covered by a curated parent enzyme mapping. No additional direct GO mapping is needed at this node.
    - [type] Ubiquitin Proteasome System|Ubiquitin and UBL binding|E3 ligase|CUL1 receptor
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower enzyme-family, domain, or architecture subdivision already covered by a curated parent enzyme mapping. No additional direct GO mapping is needed at this node.
    - [group] Ubiquitin Proteasome System|Ubiquitin and UBL binding|E3 ligase
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0061630 ubiquitin protein ligase activity]
        rationale: This PN group captures ubiquitin/UBL-binding factors that are E3 ligases. The shared molecular-function target is ubiquitin protein ligase activity.
    - [class] Ubiquitin Proteasome System|Ubiquitin and UBL binding
        status=context_only scope=too_broad_to_propagate GO=[GO:0140036 ubiquitin-modified protein reader activity]
        rationale: This class records ubiquitin/UBL-reader context, but the subtree mixes ubiquitin, SUMO, UBL-domain, domain-architecture, catalytic, signaling, trafficking, and nucleic-acid process buckets. It is useful context, not a safe direct propagation.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## Projected GO annotations (2)
- GO:1990756 ubiquitin-like ligase-substrate adaptor activity | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul1 substrate receptor
- GO:0061630 ubiquitin protein ligase activity | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Ubiquitin Proteasome System|Ubiquitin and UBL binding|E3 ligase

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
