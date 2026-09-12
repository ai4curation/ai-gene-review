# AZI2 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9H6S1
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-14
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/AZI2/AZI2-ai-review.yaml](AZI2-ai-review.yaml)
- AIGR review HTML: missing - genes/human/AZI2/AZI2-ai-review.html
- Gene notes: present - [genes/human/AZI2/AZI2-notes.md](AZI2-notes.md)
- GOA TSV: present - [genes/human/AZI2/AZI2-goa.tsv](AZI2-goa.tsv)
- UniProt record: present - [genes/human/AZI2/AZI2-uniprot.txt](AZI2-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/AZI2.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/AZI2.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/AZI2.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/AZI2.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: AZI2 (5-azacytidine-induced protein 2), better known as NAP1 (NAK-associated protein 1; also TBKBP2, TILP), is a cytoplasmic adapter protein that binds and positively regulates the IkappaB kinase (IKK)-related serine/threonine kinases TBK1 (NAK) and IKBKE (IKKepsilon). The protein has an N-terminal homodimerization region and two coiled-coil segments, and a C-terminal TBK1/IKBKE-binding domain (the Pfam TBD module, residues ~216-257) shared with the related adapters TANK and TBKBP1/SINTBAD. By binding TBK1, NAP1 promotes TBK1 activation and oligomerization and thereby couples upstream innate-immune signals to TBK1 kinase output. NAP1 functions as a shared adaptor in type I interferon induction downstream of both the endosomal Toll-like receptor 3 (via the TRIF/TICAM1 adaptor) and the cytoplasmic RIG-I/MDA5 RNA-sensing pathway, driving IRF3 activation and IFN-beta production, and it also potentiates NF-kappaB activation, including TBK1-dependent phosphorylation of the p65/RELA subunit. NAP1 is a constituent of the TBK1-IKKepsilon-NAP1 complex. Structurally, its N-terminal region binds the SKICH domains of the selective-autophagy cargo receptors NDP52/CALCOCO2 and TAX1BP1, allowing NAP1 (with its paralog SINTBAD) to bridge these receptors to TBK1 and recruit/ activate TBK1 at autophagic cargo. NAP1 is itself a phosphoprotein and is subject to TRIM38-mediated K48-linked polyubiquitination and degradation.
- Existing/core annotation action counts: ACCEPT: 5; KEEP_AS_NON_CORE: 8

## PN Consistency Summary

- **Consistency:** Mostly consistent, with one framing mismatch. The review, notes and UniProt all cast NAP1 as a cytoplasmic TBK1/IKBKE adaptor and positive regulator (PMID:14560022), a shared antiviral type-I-IFN adaptor (PMID:17142768), and — structurally — a TBK1-recruiting adaptor for the autophagy cargo receptors NDP52/CALCOCO2 and TAX1BP1 (PMID:30459273). The PN row is keyed off exactly that NDP52/TAX1BP1-bridging literature ("recruiting the ULK complex"; CALCOCO2 in PN Notes). So the PN's xenophagy placement and the review's structural-adaptor finding agree on the underlying biology. The mismatch is in altitude/role: PN places AZI2 under "Autophagy receptor **regulation**" and projects the xenophagy **process** onto it, whereas the review treats autophagy as a peripheral structural role and assigns no autophagy term at all.
- **PN story / NEW pressure:** PN asserts a xenophagy role absent from GOA (confirmed: AZI2 GOA has no autophagy term). GO:0098792 xenophagy is verified real. But NAP1 is a TBK1-recruiting **adaptor/regulator**, not itself a cargo receptor or a demonstrated xenophagy effector in human cells — evidence is structural (bridges receptors to TBK1) rather than a loss-of-function xenophagy phenotype. Conclusion: a direct `involved_in xenophagy` over-reaches; `GO:1904415 regulation of xenophagy` (verified real) or leaving it as the TBK1-adaptor capture is more defensible than the bare process projection.
- **Evidence alignment:** Partial. PN titles are the NDP52/CALCOCO2 ULK/TBK1 recruitment papers; the review's autophagy anchor is the NAP1-SKICH structural paper PMID:30459273 (HIGH relevance) plus the TBK1/IFN refs. The specific NDP52-ULK papers named in the PN dossier are not cited by PMID in the review.
- **Verdict:** Consistent biology, but PN xenophagy projection over-reaches for a TBK1-adaptor/regulator. **Recommended edits:** [MAP] downgrade AZI2's contribution to the Xenophagy node from `xenophagy` (GO:0098792, involved_in) to `regulation of xenophagy` (GO:1904415) — AZI2 is a TBK1-recruiting adaptor, not a cargo receptor. [YAML] optionally add GO:1904415 regulation of xenophagy (involved_in) supported by PMID:30459273 to reflect the NDP52/TAX1BP1-TBK1 bridging role; do not add bare GO:0098792.

## Full Consistency Review

- **UniProt:** Q9H6S1 (NAP1/TBKBP2) · **batch:** proteostasis-batch-2026-06-14 · **review status:** COMPLETE
- **PN placement:** `ALP|Autophagy substrate selection|Autophagy receptor regulation|Xenophagy` (1 row) ; **PN-node mapping:** Xenophagy type → mapped/ok_for_propagation_to_go GO:0098792 xenophagy (goa_status=new_to_goa); all ancestors (group/class/branch) = no_mapping.
- **Consistency:** Mostly consistent, with one framing mismatch. The review, notes and UniProt all cast NAP1 as a cytoplasmic TBK1/IKBKE adaptor and positive regulator (PMID:14560022), a shared antiviral type-I-IFN adaptor (PMID:17142768), and — structurally — a TBK1-recruiting adaptor for the autophagy cargo receptors NDP52/CALCOCO2 and TAX1BP1 (PMID:30459273). The PN row is keyed off exactly that NDP52/TAX1BP1-bridging literature ("recruiting the ULK complex"; CALCOCO2 in PN Notes). So the PN's xenophagy placement and the review's structural-adaptor finding agree on the underlying biology. The mismatch is in altitude/role: PN places AZI2 under "Autophagy receptor **regulation**" and projects the xenophagy **process** onto it, whereas the review treats autophagy as a peripheral structural role and assigns no autophagy term at all.
- **PN story / NEW pressure:** PN asserts a xenophagy role absent from GOA (confirmed: AZI2 GOA has no autophagy term). GO:0098792 xenophagy is verified real. But NAP1 is a TBK1-recruiting **adaptor/regulator**, not itself a cargo receptor or a demonstrated xenophagy effector in human cells — evidence is structural (bridges receptors to TBK1) rather than a loss-of-function xenophagy phenotype. Conclusion: a direct `involved_in xenophagy` over-reaches; `GO:1904415 regulation of xenophagy` (verified real) or leaving it as the TBK1-adaptor capture is more defensible than the bare process projection.
- **Mapping strategy:** Node need not change for this gene, but the projection is too strong: AZI2 supports the xenophagy node only as a TBK1-recruiting regulator. Prefer the regulation-of-xenophagy framing over `xenophagy` for this member.
- **Evidence alignment:** Partial. PN titles are the NDP52/CALCOCO2 ULK/TBK1 recruitment papers; the review's autophagy anchor is the NAP1-SKICH structural paper PMID:30459273 (HIGH relevance) plus the TBK1/IFN refs. The specific NDP52-ULK papers named in the PN dossier are not cited by PMID in the review.
- **Verdict:** Consistent biology, but PN xenophagy projection over-reaches for a TBK1-adaptor/regulator. **Recommended edits:** [MAP] downgrade AZI2's contribution to the Xenophagy node from `xenophagy` (GO:0098792, involved_in) to `regulation of xenophagy` (GO:1904415) — AZI2 is a TBK1-recruiting adaptor, not a cargo receptor. [YAML] optionally add GO:1904415 regulation of xenophagy (involved_in) supported by PMID:30459273 to reflect the NDP52/TAX1BP1-TBK1 bridging role; do not add bare GO:0098792.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-14
- review_yaml: genes/human/AZI2/AZI2-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Autophagy-Lysosome Pathway | Autophagy substrate selection | Autophagy receptor regulation | Xenophagy
- UniProt: Q9H6S1
- In branches: ALP
- Notes: Adapter protein for TBK1 complex, essential for xenophagy. Binds to CALCOCO2.
- PN references (titles):
    - The Cargo Receptor NDP52 Initiates Selective Autophagy by Recruiting the ULK Complex to Cytosol-Invading Bacteria - ScienceDirect
    - Full article: CALCOCO2/NDP52 initiates selective autophagy through recruitment of ULK and TBK1 kinase complexes (tandfonline.com)
- PN-node mapping records (path + ancestors):
    - [type] Autophagy-Lysosome Pathway|Autophagy substrate selection|Autophagy receptor regulation|Xenophagy
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0098792 xenophagy]
        rationale: This PN type groups receptor-regulatory factors assigned to xenophagy. The source category sits inside the xenophagy mechanism rather than being equivalent to the full process.
    - [group] Autophagy-Lysosome Pathway|Autophagy substrate selection|Autophagy receptor regulation
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN taxonomy container. The descendants mix components, regulators, context labels, and mechanistic leaves, so propagation should come only from narrower curated nodes.
    - [class] Autophagy-Lysosome Pathway|Autophagy substrate selection
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad substrate-selection container. GO has useful targets for specific receptor, cargo-adaptor, and selective-autophagy leaves, but this class mixes marking, recognition, receptor regulation, and unknown roles and should not propagate as one term.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## Projected GO annotations (1)
- GO:0098792 xenophagy | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Autophagy-Lysosome Pathway|Autophagy substrate selection|Autophagy receptor regulation|Xenophagy

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
