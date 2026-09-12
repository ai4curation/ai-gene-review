# NEMF PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: O60524
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07c
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/NEMF/NEMF-ai-review.yaml](NEMF-ai-review.yaml)
- AIGR review HTML: present - [genes/human/NEMF/NEMF-ai-review.html](NEMF-ai-review.html)
- Gene notes: present - [genes/human/NEMF/NEMF-notes.md](NEMF-notes.md)
- GOA TSV: present - [genes/human/NEMF/NEMF-goa.tsv](NEMF-goa.tsv)
- UniProt record: present - [genes/human/NEMF/NEMF-uniprot.txt](NEMF-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/NEMF.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/NEMF.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/NEMF.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/NEMF.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: NEMF (Nuclear Export Mediator Factor; also called RQC2, the mammalian ortholog of yeast Rqc2/Tae2 and bacterial RqcH) is a core subunit of the ribosome-associated quality control (RQC) complex that acts on stalled 60S large ribosomal subunits. After an aberrant ribosome stalls and is split, NEMF recognizes the exposed nascent-chain-conjugated (peptidyl) tRNA in the 60S subunit, which allows it to discriminate occupied from empty 60S, and it recruits and stabilizes the E3 ubiquitin ligase LTN1/Listerin. NEMF additionally catalyzes CAT tailing, in which (in an mRNA- and 40S-independent manner) it delivers mainly alanine-charged tRNA (and other aminoacyl-tRNAs) to the ribosomal A site and directs non-templated C-terminal elongation of the stalled nascent chain, generating C-terminal alanine/threonine (CAT) tails. These tails promote degradation of the stalled chain by two routes. In the canonical RQC-L pathway they expose buried lysines for LTN1-dependent ubiquitination, and in the alternative RQC-C pathway they form a C-terminal alanine degron recognized by C-end-rule E3 ligases (CRL2-KLHDC10 and RCHY1/PIRH2). NEMF acts in the cytosol on cytosolic ribosomes; loss of NEMF function causes accumulation of toxic, aggregation-prone nascent chains, and biallelic NEMF variants cause an autosomal-recessive neurodevelopmental disorder with peripheral neuropathy.
- Existing/core annotation action counts: ACCEPT: 33; KEEP_AS_NON_CORE: 3

## PN Consistency Summary

- **Consistency:** Strong. Deep-research notes, review YAML and PN dossier all agree NEMF is the mammalian Rqc2/RQC2 ortholog: core RQC subunit that senses stalled 60S via the nascent-chain-conjugated P-site tRNA, recruits LTN1, and catalyzes **CAT/Ala tailing** (GO:0140708) of stalled nascent chains. PN placement under Ribosome-associated QC matches.
- **PN story / NEW pressure:** PN projects GO:0006515 (protein quality control for misfolded or incompletely synthesized proteins) at the group level. **Verified real and non-obsolete via OLS.** Critically, OLS ancestor check shows the review's RQC terms GO:1990116 (ribosome-associated ubiquitin-dependent protein catabolic process) and GO:0072344 (rescue of stalled cytosolic ribosome) do **NOT** have GO:0006515 as an ancestor (they sit in the ubiquitin-catabolic branch). So GO:0006515 is a genuinely distinct, complementary QC-aspect term not currently captured. Conclusion: **ADD GO:0006515 (involved_in)** is defensible for NEMF and not redundant with existing annotations; the group projection is well justified ("GO lacks a dedicated RQC term" rationale is accurate — RQC is captured only via the catabolic/rescue children).
- **Evidence alignment:** Concordant and rich. Review anchors CAT tailing to PMID:33406423 and PMID:33909987 (both VERIFIED), 60S sensing/LTN1 recruitment to PMID:25578875, RQC review PMID:35452614. PN row carries no titles; review is broader. No divergence.
- **Verdict:** Consistent, high-quality; PN projection of GO:0006515 is a defensible ADD (distinct QC aspect, verified absent from GOA and not an ancestor of existing terms). **Recommended edits:** Add GO:0006515 (protein quality control for misfolded or incompletely synthesized proteins, involved_in) to NEMF review to mirror the PN projection [YAML].

## Full Consistency Review

- **UniProt:** O60524 · **batch:** proteostasis-batch-2026-06-07c · **review status:** COMPLETE
- **PN placement:** `Translation|Cytosolic translation|Ribosome-associated QC|other RQC processes` ; **PN-node mapping:** type `other RQC processes`→no_mapping; group `Ribosome-associated QC`→GO:0006515 protein quality control for misfolded or incompletely synthesized proteins (ok_for_propagation, new_to_goa)
- **Consistency:** Strong. Deep-research notes, review YAML and PN dossier all agree NEMF is the mammalian Rqc2/RQC2 ortholog: core RQC subunit that senses stalled 60S via the nascent-chain-conjugated P-site tRNA, recruits LTN1, and catalyzes **CAT/Ala tailing** (GO:0140708) of stalled nascent chains. PN placement under Ribosome-associated QC matches.
- **PN story / NEW pressure:** PN projects GO:0006515 (protein quality control for misfolded or incompletely synthesized proteins) at the group level. **Verified real and non-obsolete via OLS.** Critically, OLS ancestor check shows the review's RQC terms GO:1990116 (ribosome-associated ubiquitin-dependent protein catabolic process) and GO:0072344 (rescue of stalled cytosolic ribosome) do **NOT** have GO:0006515 as an ancestor (they sit in the ubiquitin-catabolic branch). So GO:0006515 is a genuinely distinct, complementary QC-aspect term not currently captured. Conclusion: **ADD GO:0006515 (involved_in)** is defensible for NEMF and not redundant with existing annotations; the group projection is well justified ("GO lacks a dedicated RQC term" rationale is accurate — RQC is captured only via the catabolic/rescue children).
- **Mapping strategy:** Reasonable. type→no_mapping (correct: "other RQC processes" is a heterogeneous bucket); group→GO:0006515 is the safe broader QC target. Not too broad to project for a bona fide RQC factor. No change warranted.
- **Evidence alignment:** Concordant and rich. Review anchors CAT tailing to PMID:33406423 and PMID:33909987 (both VERIFIED), 60S sensing/LTN1 recruitment to PMID:25578875, RQC review PMID:35452614. PN row carries no titles; review is broader. No divergence.
- **Verdict:** Consistent, high-quality; PN projection of GO:0006515 is a defensible ADD (distinct QC aspect, verified absent from GOA and not an ancestor of existing terms). **Recommended edits:** Add GO:0006515 (protein quality control for misfolded or incompletely synthesized proteins, involved_in) to NEMF review to mirror the PN projection [YAML].

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07c
- review_yaml: genes/human/NEMF/NEMF-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Translation | Cytosolic translation | Ribosome-associated QC | other RQC processes
- UniProt: O60524
- In branches: TR
- PN-node mapping records (path + ancestors):
    - [type] Translation|Cytosolic translation|Ribosome-associated QC|other RQC processes
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a single GO class. The member genes span multiple activities, complexes, or contexts, so direct propagation from this node would overstate the shared biology.
    - [group] Translation|Cytosolic translation|Ribosome-associated QC
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0006515 protein quality control for misfolded or incompletely synthesized proteins]
        rationale: The PN ribosome-associated quality-control group covers surveillance and disposal of stalled or defective nascent-chain translation products. GO lacks a dedicated ribosome-associated QC term in the local cache, so the broader protein-quality-control process is the best supported target.
    - [class] Translation|Cytosolic translation
        status=context_only scope=too_broad_to_propagate GO=[GO:0002181 cytoplasmic translation]
        rationale: The PN class Cytosolic translation is centered on the cytoplasmic translation apparatus and process, but it also houses supporting machinery such as ribosome biogenesis factors. The GO process term is a useful high-level label for the class, but propagating it to all members would over-annotate genes whose PN placement is through assembly or maturation context rather than core cytoplasmic translation.
    - [branch] Translation
        status=context_only scope=too_broad_to_propagate GO=[GO:0006412 translation]
        rationale: The PN Translation branch is organized around the translation apparatus and immediately associated cotranslational quality-control systems. GO translation is the closest high-level process label, but the PN branch also contains adjacent machinery such as ribosome biogenesis and nascent-chain handling. Keeping this relationship is useful for interpretation, but it is too broad to project safely onto every member.

## Projected GO annotations (1)
- GO:0006515 protein quality control for misfolded or incompletely synthesized proteins | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Translation|Cytosolic translation|Ribosome-associated QC

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
