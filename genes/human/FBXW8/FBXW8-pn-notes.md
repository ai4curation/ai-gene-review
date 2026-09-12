# FBXW8 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q8N3Y1
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-13
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/FBXW8/FBXW8-ai-review.yaml](FBXW8-ai-review.yaml)
- AIGR review HTML: missing - genes/human/FBXW8/FBXW8-ai-review.html
- Gene notes: missing - genes/human/FBXW8/FBXW8-notes.md
- GOA TSV: present - [genes/human/FBXW8/FBXW8-goa.tsv](FBXW8-goa.tsv)
- UniProt record: present - [genes/human/FBXW8/FBXW8-uniprot.txt](FBXW8-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/FBXW8.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/FBXW8.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/FBXW8.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/FBXW8.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/FBXW8/FBXW8-deep-research-falcon.md](FBXW8-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: FBXW8 (FBW8, FBX29) is an F-box/WD40-repeat protein that serves as the substrate-recognition subunit of a distinctive vertebrate-specific cullin-RING ubiquitin ligase. Unlike most F-box proteins, which assemble into the canonical SCF (SKP1-CUL1) ligase, FBXW8 is the exclusive F-box partner of CUL7, forming the CUL7-RING(FBXW8) (CRL7(FBXW8)) complex composed of CUL7, SKP1, RBX1 and FBXW8. Structural and biochemical work shows that CUL7 binds FBXW8 through an unusual F-box-independent mode and that, within CRL7(FBXW8), the RBX1 RING domain is held in an orientation incompatible with charging E2~ubiquitin/E2~NEDD8; the complex therefore lacks intrinsic catalytic activity and instead acts as a substrate receptor that couples, via SKP1-FBXW8, to a separately neddylated CUL1-RBX1 catalytic module that performs ubiquitin transfer. As an adaptor, FBXW8 selects substrates for polyubiquitination and proteasomal degradation. Documented substrates include insulin receptor substrate 1 (IRS1), recognized after S6-kinase phosphorylation in an mTOR-dependent manner (linking FBXW8 to insulin/IGF-1 signaling and cellular senescence); the Golgi stacking protein GORASP1/GRASP65, whose degradation, together with the scaffold OBSL1 that localizes CUL7(FBXW8) to the Golgi, controls Golgi morphology and dendrite patterning in neurons; the Ste20-family kinase MAP4K1/HPK1, recognized when autophosphorylated; phosphorylated cyclin D1 (CCND1), recognized after ERK/MAPK-dependent Thr286 phosphorylation and degraded in the cytoplasm during S phase; the chromatin-associated MRFAP1, degraded around anaphase-telophase; and adipose triglyceride lipase (ATGL/PNPLA2), K48-polyubiquitinated by a Golgi-localized CUL7-FBXW8 complex to restrain lipolysis. FBXW8 carries a polybasic N-terminal region that binds Golgi phosphatidylinositol 4-phosphate (PtdIns4P), coupling intracellular glucose status to recruitment of the CUL7-FBXW8 ligase to the Golgi. FBXW8 is also an associated component of the CUL7-OBSL1-CCDC8 "3M complex" implicated in microtubule and genome integrity and growth (3M syndrome), and is required in mouse models for placental development and fetal growth. FBXW8 is a cytoplasmic protein that also localizes to the perinuclear region and Golgi apparatus.
- Existing/core annotation action counts: ACCEPT: 40; KEEP_AS_NON_CORE: 18

## PN Consistency Summary

- **Consistency:** Rows 1–2 fully consistent and unusually well grounded. FBXW8 is the exclusive CUL7 F-box partner; review has GO:1990756 (IDA x4, ACCEPT — already in GOA), GO:0031467 Cul7-RING complex (IDA), GO:0019005 SCF KEEP_AS_NON_CORE (reflecting the PMID:35982156 finding that CRL7(FBXW8) is catalytically coupled to CUL1-RBX1), validated substrates IRS1/HPK1/cyclin D1/GORASP1/ATGL. Row2 Cul7 receptor matches GO:0031467; the dossier's own note that CRL7(FBXW8) "lacks intrinsic catalytic activity" reinforces the receptor-not-catalyst pattern. **Row3 INCONSISTENT:** PN projects GO:0061630 ubiquitin protein **ligase** activity from PMID:21070969 (Pashkova 2010, [DOI](https://doi.org/10.1016/j.molcel.2010.10.018)) — a ubiquitin-**binding** WD40 paper about F-box auto-turnover — contradicting both the paper and the structurally-demonstrated non-catalytic nature of FBXW8.
- **PN story / NEW pressure:** Rows 1–2 GO:1990756 already in GOA (IDA) — no new pressure, correctly already_in_goa_exact. Row3 GO:0061630 over-reaches (catalytic term for a structurally non-catalytic receptor; wrong paper interpretation). Both terms verified real via OLS. No defensible NEW catalytic term; the only Ub-binding-derived candidate would be GO:0043130 ubiquitin binding, and FBXW8 has no specific evidence even for that.
- **Evidence alignment:** Rows 1–2 PN cites PMID:15340381 (family review) and PMID:35982156 (CRL7 structure — also a HIGH-relevance review reference, good overlap). Review adds gene-specific PMID:17205132 (cyclin D1), PMID:18498745 (IRS1), PMID:24362026 (HPK1), PMID:21572988 (GORASP1/Golgi). Row3 PMID:21070969 is NOT in the review and is mischaracterized by GO:0061630.
- **Verdict:** Rows 1–2 CONSISTENT (GO:1990756 already in GOA, both CUL1+CUL7 contexts validated); Row3 PN node OVER-REACHES. **Recommended edits:** [MAP] change Row3 `Ubiquitin and UBL binding|E3 ligase` projection for FBXW8 from GO:0061630 ubiquitin protein ligase activity to GO:0043130 ubiquitin binding or no_mapping — PMID:21070969 = WD40 ubiquitin BINDING / F-box auto-turnover, not ligase catalysis; structure (PMID:35982156) shows FBXW8 is non-catalytic.

## Full Consistency Review

- **UniProt:** Q8N3Y1 · **batch:** proteostasis-batch-2026-06-13 · **review status:** COMPLETE (high quality)
- **PN placement (3 rows):** Row1 `UPS|...|Cul1 substrate receptor|F-box|WD40`; Row2 `UPS|...|Cul7 substrate receptor|F-box, noncanonical contact|WD40` (PMID:35982156); Row3 `UPS|Ubiquitin and UBL binding|E3 ligase|CUL1 receptor|idiosyncratic Ub binding / WD40` (PMID:21070969). **PN-node mapping:** Row1 group=mapped GO:1990756 (already_in_goa_exact); Row2 group=mapped GO:1990756 (already_in_goa_exact); Row3 group=mapped GO:0061630 (new_to_goa); class nodes context_only/too_broad.
- **Consistency:** Rows 1–2 fully consistent and unusually well grounded. FBXW8 is the exclusive CUL7 F-box partner; review has GO:1990756 (IDA x4, ACCEPT — already in GOA), GO:0031467 Cul7-RING complex (IDA), GO:0019005 SCF KEEP_AS_NON_CORE (reflecting the PMID:35982156 finding that CRL7(FBXW8) is catalytically coupled to CUL1-RBX1), validated substrates IRS1/HPK1/cyclin D1/GORASP1/ATGL. Row2 Cul7 receptor matches GO:0031467; the dossier's own note that CRL7(FBXW8) "lacks intrinsic catalytic activity" reinforces the receptor-not-catalyst pattern. **Row3 INCONSISTENT:** PN projects GO:0061630 ubiquitin protein **ligase** activity from PMID:21070969 (Pashkova 2010, [DOI](https://doi.org/10.1016/j.molcel.2010.10.018)) — a ubiquitin-**binding** WD40 paper about F-box auto-turnover — contradicting both the paper and the structurally-demonstrated non-catalytic nature of FBXW8.
- **PN story / NEW pressure:** Rows 1–2 GO:1990756 already in GOA (IDA) — no new pressure, correctly already_in_goa_exact. Row3 GO:0061630 over-reaches (catalytic term for a structurally non-catalytic receptor; wrong paper interpretation). Both terms verified real via OLS. No defensible NEW catalytic term; the only Ub-binding-derived candidate would be GO:0043130 ubiquitin binding, and FBXW8 has no specific evidence even for that.
- **Mapping strategy:** Rows 1–2 correct (GO:1990756 matches review core MF for both CUL1-coupled and CUL7 contexts; not broader/narrower). **Row3 mapping wrong:** GO:0061630 should be GO:0043130 ubiquitin binding or no_mapping. The Cul1 vs Cul7 distinction is handled well; the genuine error is the Ub-binding→ligase miscast.
- **Evidence alignment:** Rows 1–2 PN cites PMID:15340381 (family review) and PMID:35982156 (CRL7 structure — also a HIGH-relevance review reference, good overlap). Review adds gene-specific PMID:17205132 (cyclin D1), PMID:18498745 (IRS1), PMID:24362026 (HPK1), PMID:21572988 (GORASP1/Golgi). Row3 PMID:21070969 is NOT in the review and is mischaracterized by GO:0061630.
- **Verdict:** Rows 1–2 CONSISTENT (GO:1990756 already in GOA, both CUL1+CUL7 contexts validated); Row3 PN node OVER-REACHES. **Recommended edits:** [MAP] change Row3 `Ubiquitin and UBL binding|E3 ligase` projection for FBXW8 from GO:0061630 ubiquitin protein ligase activity to GO:0043130 ubiquitin binding or no_mapping — PMID:21070969 = WD40 ubiquitin BINDING / F-box auto-turnover, not ligase catalysis; structure (PMID:35982156) shows FBXW8 is non-catalytic.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-13
- review_yaml: genes/human/FBXW8/FBXW8-ai-review.yaml
- PN workbook rows: 3

## PN row 1: Ubiquitin Proteasome System | E3 ubiquitin and UBL ligases | Cul1 substrate receptor | F-box | WD40
- UniProt: Q8N3Y1
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

## PN row 2: Ubiquitin Proteasome System | E3 ubiquitin and UBL ligases | Cul7 substrate receptor | F-box, noncanonical contact | WD40
- UniProt: Q8N3Y1
- In branches: UPS
- Signature domains: (none)
- Auxiliary domains: IPR001680
- PN references (titles):
    - 35982156
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul7 substrate receptor|F-box, noncanonical contact|WD40
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower substrate-receptor, adaptor, domain, or family subdivision already covered by the curated parent adaptor/receptor mapping. No additional direct GO mapping is needed at this node.
    - [type] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul7 substrate receptor|F-box, noncanonical contact
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower substrate-receptor, adaptor, domain, or family subdivision already covered by the curated parent adaptor/receptor mapping. No additional direct GO mapping is needed at this node.
    - [group] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul7 substrate receptor
        status=mapped scope=ok_for_propagation_to_go GO=[GO:1990756 ubiquitin-like ligase-substrate adaptor activity]
        rationale: This PN group captures substrate receptors/adaptors for cullin/UBL ligase systems. The shared GO molecular-function target is ubiquitin-like ligase-substrate adaptor activity.
    - [class] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases
        status=context_only scope=too_broad_to_propagate GO=[GO:0061630 ubiquitin protein ligase activity]
        rationale: This class is a genuine E3-ligase context, but its descendants include catalytic ligases, cullin scaffolds, substrate receptors, adaptors, cofactors, regulators, and UBL modifier systems. A class-level propagation would over-annotate.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## PN row 3: Ubiquitin Proteasome System | Ubiquitin and UBL binding | E3 ligase | CUL1 receptor | idiosyncratic Ub binding / WD40
- UniProt: Q8N3Y1
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

## Projected GO annotations (3)
- GO:1990756 ubiquitin-like ligase-substrate adaptor activity | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul1 substrate receptor
- GO:1990756 ubiquitin-like ligase-substrate adaptor activity | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul7 substrate receptor
- GO:0061630 ubiquitin protein ligase activity | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Ubiquitin Proteasome System|Ubiquitin and UBL binding|E3 ligase

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
