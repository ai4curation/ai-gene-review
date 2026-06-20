# MAN1B1 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9UKM7
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-11
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/MAN1B1/MAN1B1-ai-review.yaml](MAN1B1-ai-review.yaml)
- AIGR review HTML: missing - genes/human/MAN1B1/MAN1B1-ai-review.html
- Gene notes: present - [genes/human/MAN1B1/MAN1B1-notes.md](MAN1B1-notes.md)
- GOA TSV: present - [genes/human/MAN1B1/MAN1B1-goa.tsv](MAN1B1-goa.tsv)
- UniProt record: present - [genes/human/MAN1B1/MAN1B1-uniprot.txt](MAN1B1-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/MAN1B1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/MAN1B1.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/MAN1B1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/MAN1B1.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/MAN1B1/MAN1B1-deep-research-falcon.md](MAN1B1-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: MAN1B1 (ER alpha-1,2-mannosidase I, ERManI, ERMan1) is a calcium-dependent, type II single-pass endoplasmic reticulum membrane glycosidase of glycoside hydrolase family 47 (GH47, EC 3.2.1.113) that trims terminal alpha-1,2-linked mannose residues from N-linked oligosaccharides. At low enzyme concentration it removes a single mannose from Man9GlcNAc2 to generate Man8GlcNAc2 isomer B, the first committed mannose-trimming step of N-glycan maturation; at the high local concentrations found in the ER-derived quality control compartment (ERQC) it excises additional alpha-1,2-mannoses to yield Man5-6GlcNAc2. This trimming removes misfolded glycoproteins from the calnexin/reglucosylation folding cycle and generates the demannosylated signal that commits them to ER-associated degradation (ERAD), where the trimmed glycan is recognized by downstream lectins (e.g. OS-9/XTP3-B) and delivered to the HRD1 ubiquitin-ligase machinery. ERManI thus functions as a key "mannose timer" in glycoprotein quality control. It is widely expressed, resides in the ER membrane and concentrates in mobile ER-like quality control vesicles that converge on the pericentriolar ERQC. Biallelic loss-of-function variants cause an autosomal-recessive congenital disorder of glycosylation with intellectual disability (Rafiq syndrome / MAN1B1-CDG).
- Existing/core annotation action counts: ACCEPT: 47; KEEP_AS_NON_CORE: 5; MARK_AS_OVER_ANNOTATED: 8

## PN Consistency Summary

- **Consistency:** Deep research ↔ review ↔ PN annotation are fully consistent. MAN1B1 is correctly framed as a *catalytic* GH47 alpha-1,2-mannosidase (EC 3.2.1.113), not a lectin — matching the PN "Mannose trimming" subtype. The PN subtype→GO:1904382 is well aligned with the review's accepted GO:1904380 (ER mannose trimming) + GO:0036503 (ERAD).
- **PN story / NEW pressure:** No NEW pressure for the catalytic role — already richly captured. One genuinely under-annotated function surfaced by Falcon and incorporated into the review (PMID:32958677): a catalysis-independent, cytoplasmic-tail-dependent ERAD function of misfolded alpha1-antitrypsin, glycan-independent. This is not represented by any existing GO term and is the only defensible NEW direction, but it is single-paper and the review correctly left it as a finding rather than a new term. Conclude: catalytic role already captured; tail-dependent role = future candidate, not yet actionable.
- **Evidence alignment:** PN dossier carries no reference titles (mapping-only); review evidence is extensive and PubMed-verified (PMID:10409699, 10521544, 18003979, 21062743, 22160784, 25411339, 15713668). No divergence.
- **Verdict:** Review excellent and PN-consistent; subtype mapping correct. Flag the group-level GO:0006487 projection as a closure error (catalytic trimmer ≠ N-glycosylation installer).

## Full Consistency Review

- **UniProt:** Q9UKM7 (ER alpha-1,2-mannosidase I / ERManI) · **batch:** proteostasis-batch-2026-06-11 · **review status:** COMPLETE, very thorough (60+ annotations reviewed; rich notes + Falcon).
- **PN placement:** `ER proteostasis|Glycoproteostasis|N-glycosylation system|N-glycan processing|Mannose trimming` ; **PN-node mapping:** subtype mapped→GO:1904382 (mannose trimming in glycoprotein ERAD, ok_for_propagation, more_specific_than_existing_goa); group "N-glycosylation system" mapped→GO:0006487 (protein N-linked glycosylation, entailed_by_goa_closure); type/class/branch no_mapping.
- **Consistency:** Deep research ↔ review ↔ PN annotation are fully consistent. MAN1B1 is correctly framed as a *catalytic* GH47 alpha-1,2-mannosidase (EC 3.2.1.113), not a lectin — matching the PN "Mannose trimming" subtype. The PN subtype→GO:1904382 is well aligned with the review's accepted GO:1904380 (ER mannose trimming) + GO:0036503 (ERAD).
- **PN story / NEW pressure:** No NEW pressure for the catalytic role — already richly captured. One genuinely under-annotated function surfaced by Falcon and incorporated into the review (PMID:32958677): a catalysis-independent, cytoplasmic-tail-dependent ERAD function of misfolded alpha1-antitrypsin, glycan-independent. This is not represented by any existing GO term and is the only defensible NEW direction, but it is single-paper and the review correctly left it as a finding rather than a new term. Conclude: catalytic role already captured; tail-dependent role = future candidate, not yet actionable.
- **Mapping strategy:** Subtype→GO:1904382 is sound (correctly narrower/specific). **Group→GO:0006487 (protein N-linked glycosylation) is mis-entailed for MAN1B1.** Verified via OLS: MAN1B1's GO:0140277 (ER N-glycan trimming) ancestors run through GO:0006491 "N-glycan processing" → glycoprotein *biosynthetic* process — GO:0006487 (the glycan *attachment* step) is a sibling, NOT an ancestor. So the `entailed_by_goa_closure` flag is wrong; MAN1B1 processes/trims N-glycans, it does not install them.
- **Evidence alignment:** PN dossier carries no reference titles (mapping-only); review evidence is extensive and PubMed-verified (PMID:10409699, 10521544, 18003979, 21062743, 22160784, 25411339, 15713668). No divergence.
- **Verdict:** Review excellent and PN-consistent; subtype mapping correct. Flag the group-level GO:0006487 projection as a closure error (catalytic trimmer ≠ N-glycosylation installer).
**Recommended edits:** [MAP] Correct MAN1B1's group projection of GO:0006487 — mark goa_status as NOT entailed_by_goa_closure (GO:0140277/GO:1904380 do not subsume GO:0006487); MAN1B1 is an N-glycan-processing enzyme, not an N-linked-glycosylation (attachment) enzyme.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-11
- review_yaml: genes/human/MAN1B1/MAN1B1-ai-review.yaml
- PN workbook rows: 1

## PN row 1: ER proteostasis | Glycoproteostasis | N-glycosylation system | N-glycan processing | Mannose trimming
- UniProt: Q9UKM7
- In branches: ER
- PN-node mapping records (path + ancestors):
    - [subtype] ER proteostasis|Glycoproteostasis|N-glycosylation system|N-glycan processing|Mannose trimming
        status=mapped scope=ok_for_propagation_to_go GO=[GO:1904382 mannose trimming involved in glycoprotein ERAD pathway]
        rationale: Within the ER proteostasis branch, this PN subtype denotes mannose trimming used in glycoprotein quality control and ERAD triage. That is close enough for propagation to the GO mannose-trimming-in-ERAD process, but the PN subtype is framed as a proteostasis step rather than a formal GO process class.
    - [type] ER proteostasis|Glycoproteostasis|N-glycosylation system|N-glycan processing
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a single GO class. The member genes span multiple activities, complexes, or contexts, so direct propagation from this node would overstate the shared biology.
    - [group] ER proteostasis|Glycoproteostasis|N-glycosylation system
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0006487 protein N-linked glycosylation]
        rationale: This PN group captures the ER N-glycosylation machinery that installs and processes N-linked glycans during proteostasis. GO protein N-linked glycosylation is the best current propagation target in the local cache.
    - [class] ER proteostasis|Glycoproteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a single GO class. The member genes span multiple activities, complexes, or contexts, so direct propagation from this node would overstate the shared biology.
    - [branch] ER proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## Projected GO annotations (2)
- GO:0006487 protein N-linked glycosylation | scope=ok_for_propagation_to_go | goa_status=entailed_by_goa_closure | from=ER proteostasis|Glycoproteostasis|N-glycosylation system
- GO:1904382 mannose trimming involved in glycoprotein ERAD pathway | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=ER proteostasis|Glycoproteostasis|N-glycosylation system|N-glycan processing|Mannose trimming

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
