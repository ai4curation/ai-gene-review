# DDB2 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q92466
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-13
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/DDB2/DDB2-ai-review.yaml](DDB2-ai-review.yaml)
- AIGR review HTML: missing - genes/human/DDB2/DDB2-ai-review.html
- Gene notes: missing - genes/human/DDB2/DDB2-notes.md
- GOA TSV: present - [genes/human/DDB2/DDB2-goa.tsv](DDB2-goa.tsv)
- UniProt record: present - [genes/human/DDB2/DDB2-uniprot.txt](DDB2-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/DDB2.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/DDB2.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/DDB2.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/DDB2.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/DDB2/DDB2-deep-research-falcon.md](DDB2-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: DDB2 (DNA damage-binding protein 2, the p48 subunit of UV-DDB; XPE factor) is a nuclear protein built from an N-terminal helix-loop-helix that docks onto DDB1 and a seven-bladed WD40 beta-propeller that engages DNA. With DDB1 it forms the UV-damaged DNA-binding (UV-DDB) heterodimer, the UV-lesion sensor of global-genome nucleotide excision repair (GG-NER), which directly recognizes UV-induced photolesions, preferentially cyclobutane pyrimidine dimers (CPDs) and 6-4 photoproducts (6-4PPs), as well as apurinic/abasic (AP) sites and short mismatches. The propeller flips the damaged bases into a binding pocket and kinks the duplex by roughly 40 degrees with local strand separation. By binding CPDs that are otherwise poorly recognized, DDB2 recruits and hands off the lesion to the XPC-RAD23B complex to initiate downstream NER. DDB2 also acts as the substrate-recognition receptor (a DCAF) of a CUL4-RING E3 ubiquitin ligase, CRL4(DDB2) (DDB1-CUL4A/CUL4B-RBX1), assembling on chromatin at sites of UV damage. This ligase ubiquitinates chromatin histones (notably H2A, and H3/H4), ubiquitinates XPC to modulate its DNA binding, and autoubiquitinates DDB2 itself to trigger its turnover; these ubiquitination events help remodel and open damaged nucleosomes and hand the lesion to XPC. DDB2 activity is tightly coupled to its modification state: monoubiquitination is compatible with damage binding, whereas polyubiquitination abolishes damaged-DNA binding and promotes proteasomal degradation, and XPC (assisted by centrin-2) competitively suppresses DDB2 ubiquitination to stabilize it for repeated rounds of repair. The ligase is regulated by NEDD8 conjugation and by the COP9 signalosome, and DDB2 protein levels are controlled by ubiquitination/deubiquitination (e.g., USP24, USP44), by PARP1-dependent stabilization, and by p53, which induces DDB2 expression. Loss-of-function mutations in DDB2 cause xeroderma pigmentosum complementation group E (XP-E), with UV sensitivity and skin-cancer predisposition.
- Existing/core annotation action counts: ACCEPT: 55; KEEP_AS_NON_CORE: 26

## PN Consistency Summary

- **Consistency:** Consistent on the substrate-receptor (DCAF) identity. Deep research, review and PN all describe DDB2 as the WD40 substrate-recognition receptor of CRL4(DDB2), plus the UV-DDB lesion sensor. Minor divergence in MF choice (see below). No biological contradiction.
- **PN story / NEW pressure:** PN projects GO:1990756 (substrate-adaptor MF) as new_to_goa — and indeed GOA has no GO:1990756 (it has GO:0004842 contributes_to and GO:0003684 damaged-DNA binding; confirmed in goa.tsv). GO:1990756 is real (OLS) and biologically appropriate for DDB2 as a DCAF receptor. Verdict: ADD is defensible. The review instead represents the receptor MF as GO:0004842 (ubiquitin-protein transferase, contributes_to) and the sensor MF as GO:0003684; it does NOT propose GO:1990756.
- **Evidence alignment:** PN row lists no references; the review is richly evidenced (PMID:12732143 ligase activity IDA; 16473935 H2A ubiquitination; 22334663 CUL4B complex; 19109893 UV-DDB structure; etc.), all marked VERIFIED. No conflict; PN simply under-cites.
- **Verdict:** Consistent; PN GO:1990756 (receptor) is correctly categorized and a defensible add. **Recommended edits:** [YAML] consider adding GO:1990756 to DDB2 as the explicit DCAF substrate-receptor MF (complements existing GO:0004842 contributes_to), aligning with the PN projection.

## Full Consistency Review

- **UniProt:** Q92466 · **batch:** proteostasis-batch-2026-06-13 · **review status:** COMPLETE
- **PN placement:** `UPS|E3 ubiquitin and UBL ligases|Cul4A/Cul4B substrate receptor|WD40|other` ; **PN-node mapping:** group "Cul4A/Cul4B substrate receptor"=mapped, ok_for_propagation, GO:1990756 (substrate-adaptor MF); subtype/type=no_mapping; projected GO:1990756 goa_status=new_to_goa.
- **Consistency:** Consistent on the substrate-receptor (DCAF) identity. Deep research, review and PN all describe DDB2 as the WD40 substrate-recognition receptor of CRL4(DDB2), plus the UV-DDB lesion sensor. Minor divergence in MF choice (see below). No biological contradiction.
- **PN story / NEW pressure:** PN projects GO:1990756 (substrate-adaptor MF) as new_to_goa — and indeed GOA has no GO:1990756 (it has GO:0004842 contributes_to and GO:0003684 damaged-DNA binding; confirmed in goa.tsv). GO:1990756 is real (OLS) and biologically appropriate for DDB2 as a DCAF receptor. Verdict: ADD is defensible. The review instead represents the receptor MF as GO:0004842 (ubiquitin-protein transferase, contributes_to) and the sensor MF as GO:0003684; it does NOT propose GO:1990756.
- **Mapping strategy:** Correct category (substrate receptor → GO:1990756), unlike DDB1. DDB2 is genuinely the DCAF receptor of CRL4(DDB2), so GO:1990756 is well placed and narrower than the generic existing terms. Node status/scope fine.
- **Evidence alignment:** PN row lists no references; the review is richly evidenced (PMID:12732143 ligase activity IDA; 16473935 H2A ubiquitination; 22334663 CUL4B complex; 19109893 UV-DDB structure; etc.), all marked VERIFIED. No conflict; PN simply under-cites.
- **Verdict:** Consistent; PN GO:1990756 (receptor) is correctly categorized and a defensible add. **Recommended edits:** [YAML] consider adding GO:1990756 to DDB2 as the explicit DCAF substrate-receptor MF (complements existing GO:0004842 contributes_to), aligning with the PN projection.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-13
- review_yaml: genes/human/DDB2/DDB2-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Ubiquitin Proteasome System | E3 ubiquitin and UBL ligases | Cul4A/Cul4B substrate receptor | WD40 | other
- UniProt: Q92466
- In branches: UPS
- Signature domains: (none)
- Auxiliary domains: IPR001680
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul4A/Cul4B substrate receptor|WD40|other
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower substrate-receptor, adaptor, domain, or family subdivision already covered by the curated parent adaptor/receptor mapping. No additional direct GO mapping is needed at this node.
    - [type] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul4A/Cul4B substrate receptor|WD40
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
