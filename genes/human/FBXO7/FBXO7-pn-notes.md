# FBXO7 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9Y3I1
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-13
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/FBXO7/FBXO7-ai-review.yaml](FBXO7-ai-review.yaml)
- AIGR review HTML: missing - genes/human/FBXO7/FBXO7-ai-review.html
- Gene notes: missing - genes/human/FBXO7/FBXO7-notes.md
- GOA TSV: present - [genes/human/FBXO7/FBXO7-goa.tsv](FBXO7-goa.tsv)
- UniProt record: present - [genes/human/FBXO7/FBXO7-uniprot.txt](FBXO7-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/FBXO7.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/FBXO7.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/FBXO7.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/FBXO7.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/FBXO7/FBXO7-deep-research-falcon.md](FBXO7-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: FBXO7 (also called FBX7; PARK15) is the substrate-recognition (F-box) component of an SCF (SKP1-CUL1-RBX1-F-box) E3 ubiquitin-protein ligase complex, SCF(FBXO7). As an F-box protein it acts as a ligase-substrate adaptor: it recruits substrates and bridges them, via its F-box domain binding to SKP1, to the catalytic cullin-RING core (RBX1), and is not itself the catalytic ubiquitin transferase. The protein has a modular architecture comprising an N-terminal ubiquitin-like (Ubl) region that mediates binding to the E3 ligase PRKN/Parkin, a CDK6-interaction region, an FP (Fbxo7/PI31) dimerization domain that mediates homodimerization and interaction with the proteasome inhibitor PSMF1/PI31, the F-box domain, and a C-terminal proline-rich region that serves as a substrate-binding module. SCF(FBXO7) ubiquitination is not exclusively degradative: it can build K48-linked chains that target substrates for proteasomal degradation or K63-linked chains with non-proteolytic signaling/assembly outcomes, depending on substrate and context. Documented SCF(FBXO7) substrates include the cell-cycle regulator DLGAP5/HURP, the inhibitor-of-apoptosis protein BIRC2/cIAP1, TRAF2 and the NF-kappa-B cofactor UXT isoform 2 (whose degradation inhibits NF-kappa-B signaling), the NAD+-dependent deacetylase SIRT7 (K48- linked polyubiquitination promoting H2O2-induced cell death), the kinase GSK3-beta and the mitochondrial import receptor TOMM20 (modified in part with non-degradative chains), and, in tumor-suppressor contexts, the mitochondrial-fission factor INF2 and the arginine methyltransferase PRMT1 (K48-linked polyubiquitination coupling FBXO7 to control of mitochondrial division and serine biosynthesis, respectively). Beyond canonical SCF activity, FBXO7 has SCF-independent roles: it relocates from the cytosol to depolarized mitochondria downstream of PINK1 and promotes PRKN/Parkin recruitment and mitofusin ubiquitination to drive selective autophagy of damaged mitochondria (mitophagy); it associates with the proteasome and regulates proteasome assembly/activity through PSMF1/PI31; and it activates cyclin D/CDK6 complexes to promote cell-cycle progression, with proto-oncogenic transforming activity. FBXO7 protein stability is itself controlled by the deubiquitinase USP7. FBXO7 is predominantly cytoplasmic/cytosolic with a minor nuclear pool. Recessive loss-of-function and missense mutations (e.g. T22M, R378G, R498X) cause early-onset autosomal recessive parkinsonian-pyramidal syndrome (Parkinson disease 15, PARK15).
- Existing/core annotation action counts: ACCEPT: 41; KEEP_AS_NON_CORE: 50; MODIFY: 1

## PN Consistency Summary

- **Consistency:** Fully consistent across the SPECIAL CASE roles. Falcon DR, review YAML, and all three PN rows converge: FBXO7 is (a) an SCF substrate receptor (GO:1990756, ACCEPT, already in GOA), (b) a PINK1/PRKN-pathway mitophagy regulator (PARK15), and (c) a PSMF1/PI31 proteasome regulator via the FP domain; plus CDK6/cyclin-D activation. No contradictions.
- **PN story / NEW pressure:** No new term pressure. GO:1990756 already in GOA (PN flags already_in_goa_exact) and accepted. The mitophagy role: PN projects GO:0000423 mitophagy (verified real) but self-flags more_specific_than_existing_goa; the review more accurately uses the regulator terms **GO:1903599 (positive regulation of autophagy of mitochondrion) and GO:1901526 (positive regulation of mitophagy), both verified real, ACCEPT** — FBXO7 facilitates/regulates mitophagy rather than being core autophagy machinery. Review also adds SCF-independent GO:0030674 protein-macromolecule adaptor activity for the mitophagy and PI31 roles. Conclude: all roles already captured; PN mitophagy term is appropriately broader and acknowledged as such.
- **Evidence alignment:** PN cites the FBXO7/Parkin mitophagy paper (Burchell et al., Nat Neurosci — PMID:23933751) for row 1 and "15340381 / rev" for row 3. Review uses PMID:23933751 (mitophagy IBA/IDA support), the FP-domain/PI31 structural work (PMID:16782869-class, GO:0046982), CDK6 interaction studies, plus Falcon DR. Good overlap on the mitophagy primary reference; review enriches with proteasome/CDK6 literature.
- **Verdict:** Consistent across all three PN rows; GO:1990756 already in GOA, mitophagy handled via more specific regulator terms (GO:1903599/GO:1901526). No over-reach; PI31/CDK6/NF-kB roles appropriately placed.

## Full Consistency Review

- **UniProt:** Q9Y3I1 (FBXO7/PARK15) · **batch:** proteostasis-batch-2026-06-13 (Falcon DR) · **review status:** COMPLETE
- **PN placement:** 3 rows, ALP+UPS. (1) `ALP|Autophagy substrate selection|…|Mitophagy|PINK/PRKN pathway`; (2) `UPS|Ubiquitin and UBL proteins|UBL domain|E3 ligases|CUL1 receptor / F-box`; (3) `UPS|E3 ubiquitin and UBL ligases|Cul1 substrate receptor|F-box|PI31, UBL`. **PN-node mapping:** mitophagy type=`mapped`/ok→GO:0000423 (more_specific_than_existing_goa); UBL-domain CUL1-receptor subtype + Cul1-receptor group both=`mapped`/ok→GO:1990756 (already_in_goa_exact); UBL-domain class/group/type held context_only (too_broad)→GO:0061630/0043130/0019787.
- **Consistency:** Fully consistent across the SPECIAL CASE roles. Falcon DR, review YAML, and all three PN rows converge: FBXO7 is (a) an SCF substrate receptor (GO:1990756, ACCEPT, already in GOA), (b) a PINK1/PRKN-pathway mitophagy regulator (PARK15), and (c) a PSMF1/PI31 proteasome regulator via the FP domain; plus CDK6/cyclin-D activation. No contradictions.
- **PN story / NEW pressure:** No new term pressure. GO:1990756 already in GOA (PN flags already_in_goa_exact) and accepted. The mitophagy role: PN projects GO:0000423 mitophagy (verified real) but self-flags more_specific_than_existing_goa; the review more accurately uses the regulator terms **GO:1903599 (positive regulation of autophagy of mitochondrion) and GO:1901526 (positive regulation of mitophagy), both verified real, ACCEPT** — FBXO7 facilitates/regulates mitophagy rather than being core autophagy machinery. Review also adds SCF-independent GO:0030674 protein-macromolecule adaptor activity for the mitophagy and PI31 roles. Conclude: all roles already captured; PN mitophagy term is appropriately broader and acknowledged as such.
- **Mapping strategy:** Gene supports the multi-branch node design. KEY PATTERN holds for the UPS rows (F-box receptor → GO:1990756; catalytic GO:0061630 held too_broad at class). For the ALP row, the PN process term GO:0000423 is broader than the review's regulator terms — consistent with the TOMM20/HSPA8/RAB7A precedent that the broader process term should not over-claim; PN's more_specific_than_existing_goa flag captures this correctly. Scopes sound.
- **Evidence alignment:** PN cites the FBXO7/Parkin mitophagy paper (Burchell et al., Nat Neurosci — PMID:23933751) for row 1 and "15340381 / rev" for row 3. Review uses PMID:23933751 (mitophagy IBA/IDA support), the FP-domain/PI31 structural work (PMID:16782869-class, GO:0046982), CDK6 interaction studies, plus Falcon DR. Good overlap on the mitophagy primary reference; review enriches with proteasome/CDK6 literature.
- **Verdict:** Consistent across all three PN rows; GO:1990756 already in GOA, mitophagy handled via more specific regulator terms (GO:1903599/GO:1901526). No over-reach; PI31/CDK6/NF-kB roles appropriately placed.
- **Recommended edits:** none to FBXO7-ai-review.yaml; PN mappings sound (mitophagy more_specific_than_existing_goa flag is the correct treatment).

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-13
- review_yaml: genes/human/FBXO7/FBXO7-ai-review.yaml
- PN workbook rows: 3

## PN row 1: Autophagy-Lysosome Pathway | Autophagy substrate selection | Substrate selectivity regulator for selective autophagy | Mitophagy | PINK/PRKN pathway
- UniProt: Q9Y3I1
- In branches: ALP, UPS
- Notes: F-box only protein, component of SCF E3 ubiquitin ligase complex. Interacts with PINK1 and PRKN. Involved in translocation of PRKN to mitochondria. FBXO7 interacts with PINK1 and facilitate the translocation of Parkin/PINK1 translocation to the mitochondria.
- PN references (titles):
    - The Parkinson's disease–linked proteins Fbxo7 and Parkin interact to mediate mitophagy | Nature Neuroscience
- PN-node mapping records (path + ancestors):
    - [subtype] Autophagy-Lysosome Pathway|Autophagy substrate selection|Substrate selectivity regulator for selective autophagy|Mitophagy|PINK/PRKN pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a contextual PN role. The label is useful for curator triage, but by itself does not support a universal GO assertion for all member genes beyond curated ancestor or child mappings.
    - [type] Autophagy-Lysosome Pathway|Autophagy substrate selection|Substrate selectivity regulator for selective autophagy|Mitophagy
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0000423 mitophagy]
        rationale: This PN type groups substrate-selectivity regulators assigned to mitophagy. Those factors participate in mitophagy, but the PN category is more specific than the full process term.
    - [group] Autophagy-Lysosome Pathway|Autophagy substrate selection|Substrate selectivity regulator for selective autophagy
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN taxonomy container. The descendants mix components, regulators, context labels, and mechanistic leaves, so propagation should come only from narrower curated nodes.
    - [class] Autophagy-Lysosome Pathway|Autophagy substrate selection
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad substrate-selection container. GO has useful targets for specific receptor, cargo-adaptor, and selective-autophagy leaves, but this class mixes marking, recognition, receptor regulation, and unknown roles and should not propagate as one term.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## PN row 2: Ubiquitin Proteasome System | Ubiquitin and UBL proteins | UBL domain | E3 ligases | CUL1 receptor / F-box
- UniProt: Q9Y3I1
- In branches: ALP, UPS
- Signature domains: (IPR029071)
- Auxiliary domains: IPR001810, IPR021625
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|Ubiquitin and UBL proteins|UBL domain|E3 ligases|CUL1 receptor / F-box
        status=mapped scope=ok_for_propagation_to_go GO=[GO:1990756 ubiquitin-like ligase-substrate adaptor activity]
        rationale: This PN subtype identifies a UBL-domain F-box/CUL1 receptor role. The safe shared molecular function is ubiquitin-like ligase-substrate adaptor activity rather than catalytic E3 activity.
    - [type] Ubiquitin Proteasome System|Ubiquitin and UBL proteins|UBL domain|E3 ligases
        status=context_only scope=too_broad_to_propagate GO=[GO:0061630 ubiquitin protein ligase activity]
        rationale: This UBL-domain type is an E3-ligase context, but descendants include catalytic E3s as well as cullin receptor/adaptor components. Direct propagation is restricted to narrower subtypes.
    - [group] Ubiquitin Proteasome System|Ubiquitin and UBL proteins|UBL domain
        status=context_only scope=too_broad_to_propagate GO=[GO:0043130 ubiquitin binding]
        rationale: This group records UBL-domain protein context, but descendants include enzymes, adaptors, chaperone-related proteins, non-enzymatic proteins, and nucleic-acid factors. Propagation is restricted to narrower nodes.
    - [class] Ubiquitin Proteasome System|Ubiquitin and UBL proteins
        status=context_only scope=too_broad_to_propagate GO=[GO:0019787 ubiquitin-like protein transferase activity]
        rationale: This class groups ubiquitin, UBL modifiers, UBX/UBL-domain proteins, and UBL-containing enzymes. The branch is UPS-relevant but too mixed to propagate as a single GO annotation.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## PN row 3: Ubiquitin Proteasome System | E3 ubiquitin and UBL ligases | Cul1 substrate receptor | F-box | PI31, UBL
- UniProt: Q9Y3I1
- In branches: ALP, UPS
- Signature domains: IPR001810
- Auxiliary domains: IPR021625, (IPR029071)
- PN references (titles):
    - 15340381 / rev
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul1 substrate receptor|F-box|PI31, UBL
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

## Projected GO annotations (3)
- GO:0000423 mitophagy | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=Autophagy-Lysosome Pathway|Autophagy substrate selection|Substrate selectivity regulator for selective autophagy|Mitophagy
- GO:1990756 ubiquitin-like ligase-substrate adaptor activity | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Ubiquitin Proteasome System|Ubiquitin and UBL proteins|UBL domain|E3 ligases|CUL1 receptor / F-box
- GO:1990756 ubiquitin-like ligase-substrate adaptor activity | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul1 substrate receptor

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
