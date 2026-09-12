# FBXO40 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9UH90
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-13
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/FBXO40/FBXO40-ai-review.yaml](FBXO40-ai-review.yaml)
- AIGR review HTML: missing - genes/human/FBXO40/FBXO40-ai-review.html
- Gene notes: missing - genes/human/FBXO40/FBXO40-notes.md
- GOA TSV: present - [genes/human/FBXO40/FBXO40-goa.tsv](FBXO40-goa.tsv)
- UniProt record: present - [genes/human/FBXO40/FBXO40-uniprot.txt](FBXO40-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/FBXO40.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/FBXO40.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/FBXO40.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/FBXO40.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/FBXO40/FBXO40-deep-research-falcon.md](FBXO40-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: FBXO40 (F-box only protein 40; "muscle disease-related protein") is a 709-residue FBXO-class F-box protein that serves as the substrate-recognition subunit of a cullin-RING SCF (SKP1-CUL1-RBX1-F-box) E3 ubiquitin ligase complex. Like other F-box proteins, it docks onto the SCF scaffold through its C-terminal F-box domain (interacting with SKP1/CUL1) while presenting an N-terminal substrate-binding module; FBXO40 carries a TRAF-type zinc finger and is not itself the catalytic RING subunit (catalysis is provided by RBX1, which recruits the ubiquitin-charged E2). FBXO40 expression is restricted essentially to heart and skeletal muscle, appears postnatally during muscle development, and is upregulated in denervation-induced (but not starvation-induced) muscle atrophy and reduced in Limb-girdle muscular dystrophy muscle. Its best-supported direct substrate is insulin receptor substrate 1 (IRS1): the SCF(FBXO40) complex (with co-precipitating SKP1, CUL1 and RBX1) ubiquitinates recombinant IRS1 in vitro in a manner enhanced by IGF1R-dependent IRS1 tyrosine phosphorylation, targeting IRS1 for proteasomal degradation and thereby attenuating the IGF-1/insulin -> IRS1 -> PI3K/AKT anabolic signaling axis in skeletal muscle. Loss of Fbxo40 increases IRS1 protein abundance (without changing Irs1 mRNA), prolongs IRS1 half-life, and produces myotube and whole-muscle hypertrophy in mice (and increased muscle mass in knockout pigs), a phenotype that is IRS1-dependent. FBXO40 transcription is induced by inflammatory STAT3 signaling (e.g. downstream of IL-6), linking it to catabolic insulin-resistance states. The protein localizes to the cytoplasm/cytosol.
- Existing/core annotation action counts: ACCEPT: 5; KEEP_AS_NON_CORE: 13; MODIFY: 1; NEW: 1

## PN Consistency Summary

- **Consistency:** Consistent and the best-characterized of the set. Deep research (Falcon, anchored on Shi et al. 2011 PMID:22033112), review YAML, and PN mapping agree: muscle-restricted SCF substrate receptor whose validated substrate is IRS1, limiting IGF-1/insulin->IRS1->PI3K/AKT signaling. Review applies the KEY F-box PATTERN cleanly: MODIFY of the IEA catalytic GO:0061630 (ubiquitin protein ligase activity) -> GO:1990756 adaptor activity. No internal contradictions.
- **PN story / NEW pressure:** PN asserts only the generic adaptor role, but FBXO40 has a real substrate-specific BP NOT in GOA. Review adds NEW GO:0046627 "negative regulation of insulin receptor signaling pathway" (OLS-verified real). Defensible: SCF-FBXO40 ubiquitinates IRS1, Fbxo40 loss stabilizes IRS1 and causes IRS1-dependent muscle hypertrophy. Honestly recorded as ISO (mouse ortholog; PMID:22033112 NOT in cache — confirmed). Conclusion: **ADD** GO:0046627 (already in the review). MF/CC otherwise captured.
- **Evidence alignment:** PN cites only "15340381 / rev." Review uses PMID:17928169 (muscle-specific expression, VERIFIED), PMID:22033112 (IRS1, UNVERIFIED/ISO), PMID:34445249 (NAS), Falcon, Reactome. Substantial divergence: review carries the substrate-level primary literature PN lacks.
- **Verdict:** Consistent; correct F-box MODIFY pattern; defensible verified NEW BP (GO:0046627). ACCEPT review. **Recommended edits:** none required; optionally [REF] upgrade PMID:22033112 to VERIFIED if full text read.

## Full Consistency Review

- **UniProt:** Q9UH90 · **batch:** proteostasis-batch-2026-06-13 · **review status:** COMPLETE
- **PN placement:** `UPS|E3 ubiquitin and UBL ligases|Cul1 substrate receptor|F-box|TRAF-type ZnF` ; **PN-node mapping:** F-box subtype/type = no_mapping; group = mapped, ok_for_propagation_to_go, GO:1990756; class = context_only/too_broad (GO:0061630).
- **Consistency:** Consistent and the best-characterized of the set. Deep research (Falcon, anchored on Shi et al. 2011 PMID:22033112), review YAML, and PN mapping agree: muscle-restricted SCF substrate receptor whose validated substrate is IRS1, limiting IGF-1/insulin->IRS1->PI3K/AKT signaling. Review applies the KEY F-box PATTERN cleanly: MODIFY of the IEA catalytic GO:0061630 (ubiquitin protein ligase activity) -> GO:1990756 adaptor activity. No internal contradictions.
- **PN story / NEW pressure:** PN asserts only the generic adaptor role, but FBXO40 has a real substrate-specific BP NOT in GOA. Review adds NEW GO:0046627 "negative regulation of insulin receptor signaling pathway" (OLS-verified real). Defensible: SCF-FBXO40 ubiquitinates IRS1, Fbxo40 loss stabilizes IRS1 and causes IRS1-dependent muscle hypertrophy. Honestly recorded as ISO (mouse ortholog; PMID:22033112 NOT in cache — confirmed). Conclusion: **ADD** GO:0046627 (already in the review). MF/CC otherwise captured.
- **Mapping strategy:** Gene does not change the node. GO:1990756 matches; node-level scope correct. The FBXO40-specific GO:0046627 lives in the review as a NEW substrate-specific term, appropriately not propagated to the shared PN node (too specific for the group). Catalytic-ligase IEA correctly demoted per pattern.
- **Evidence alignment:** PN cites only "15340381 / rev." Review uses PMID:17928169 (muscle-specific expression, VERIFIED), PMID:22033112 (IRS1, UNVERIFIED/ISO), PMID:34445249 (NAS), Falcon, Reactome. Substantial divergence: review carries the substrate-level primary literature PN lacks.
- **Verdict:** Consistent; correct F-box MODIFY pattern; defensible verified NEW BP (GO:0046627). ACCEPT review. **Recommended edits:** none required; optionally [REF] upgrade PMID:22033112 to VERIFIED if full text read.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-13
- review_yaml: genes/human/FBXO40/FBXO40-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Ubiquitin Proteasome System | E3 ubiquitin and UBL ligases | Cul1 substrate receptor | F-box | TRAF-type ZnF
- UniProt: Q9UH90
- In branches: UPS
- Signature domains: IPR001810
- Auxiliary domains: IPR001293
- PN references (titles):
    - 15340381 / rev
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul1 substrate receptor|F-box|TRAF-type ZnF
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
