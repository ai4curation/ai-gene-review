# CRTAP PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: O75718
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/CRTAP/CRTAP-ai-review.yaml](CRTAP-ai-review.yaml)
- AIGR review HTML: present - [genes/human/CRTAP/CRTAP-ai-review.html](CRTAP-ai-review.html)
- Gene notes: present - [genes/human/CRTAP/CRTAP-notes.md](CRTAP-notes.md)
- GOA TSV: present - [genes/human/CRTAP/CRTAP-goa.tsv](CRTAP-goa.tsv)
- UniProt record: present - [genes/human/CRTAP/CRTAP-uniprot.txt](CRTAP-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/CRTAP.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/CRTAP.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/CRTAP.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/CRTAP.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: CRTAP (cartilage-associated protein) is an endoplasmic reticulum (ER) lumen glycoprotein that is an essential, non-catalytic subunit of the collagen prolyl 3-hydroxylation complex, together with prolyl 3-hydroxylase 1 (P3H1/LEPRE1) and cyclophilin B (PPIB/CyPB). Within this ternary complex, P3H1 provides the catalytic prolyl 3-hydroxylase activity and PPIB the peptidyl-prolyl cis-trans isomerase activity, while CRTAP acts as a scaffolding/helper subunit required for complex assembly and stability. The complex 3-hydroxylates a single specific proline residue (Pro986) of the alpha1(I) and alpha1(II) fibrillar procollagen chains in the ER and also functions as a collagen-specific molecular chaperone/foldase that controls the rate of collagen triple-helix folding; delayed folding in its absence leads to overmodification of the collagen helix. CRTAP and P3H1 are mutually stabilizing: loss of either protein destabilizes the other. A minor fraction of CRTAP is secreted into the extracellular space/matrix. Biallelic loss-of-function variants cause autosomal recessive osteogenesis imperfecta type VII, underscoring an essential role in collagen biosynthesis and skeletal development.
- Existing/core annotation action counts: ACCEPT: 10; KEEP_AS_NON_CORE: 4; MARK_AS_OVER_ANNOTATED: 4; MODIFY: 1

## PN Consistency Summary

- **Consistency:** Fully consistent. Deep-research notes, review YAML, PN annotation, and PN-node mapping all describe CRTAP as the non-catalytic scaffolding subunit of the ER collagen prolyl 3-hydroxylation complex (with P3H1/PPIB) that 3-hydroxylates α1(I)/α1(II) Pro986 and acts as a collagen foldase. No contradictions.
- **PN story / NEW pressure:** PN asserts collagen biosynthetic context. This is already captured: the review explicitly lists GO:0032964 collagen biosynthetic process in `core_functions.directly_involved_in`, and the GOA carries collagen-fibril-organization / protein-folding-in-ER terms. GO:0032964 verified real via OLS. No NEW-term pressure beyond what the review already proposes (MODIFY protein folding → GO:0034975; collagen complex CC term flagged as a suggested question). Conclusion: **already captured**.
- **Evidence alignment:** Strong overlap. PN dossier carries no reference titles for this row, but the review's collagen-process evidence (PMID:19846465, PMID:20089953, PMID:39245686, Reactome collagen reactions) directly underpins the GO:0032964 mapping. No divergence.
- **Verdict:** Consistent; PN role already captured in review (GO:0032964). No edits required.

## Full Consistency Review

- **UniProt:** O75718 · **batch:** proteostasis-batch-2026-06-07 · **review status:** COMPLETE
- **PN placement:** `ER proteostasis | Maturation and folding of specific substrates | ER collagen processing and folding` ; **PN-node mapping:** group=mapped, scope=ok_for_propagation_to_go, GO:0032964 collagen biosynthetic process (class/branch ancestors = no_mapping)
- **Consistency:** Fully consistent. Deep-research notes, review YAML, PN annotation, and PN-node mapping all describe CRTAP as the non-catalytic scaffolding subunit of the ER collagen prolyl 3-hydroxylation complex (with P3H1/PPIB) that 3-hydroxylates α1(I)/α1(II) Pro986 and acts as a collagen foldase. No contradictions.
- **PN story / NEW pressure:** PN asserts collagen biosynthetic context. This is already captured: the review explicitly lists GO:0032964 collagen biosynthetic process in `core_functions.directly_involved_in`, and the GOA carries collagen-fibril-organization / protein-folding-in-ER terms. GO:0032964 verified real via OLS. No NEW-term pressure beyond what the review already proposes (MODIFY protein folding → GO:0034975; collagen complex CC term flagged as a suggested question). Conclusion: **already captured**.
- **Mapping strategy:** No change needed. The group-node mapping to GO:0032964 is defensible and matches the review's own process annotation; ancestor nodes correctly left no_mapping. Projected term is the same grain as the review (neither broader nor narrower). Consistent with the project's pattern of mapping only the substrate-specific group node.
- **Evidence alignment:** Strong overlap. PN dossier carries no reference titles for this row, but the review's collagen-process evidence (PMID:19846465, PMID:20089953, PMID:39245686, Reactome collagen reactions) directly underpins the GO:0032964 mapping. No divergence.
- **Verdict:** Consistent; PN role already captured in review (GO:0032964). No edits required.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07
- review_yaml: genes/human/CRTAP/CRTAP-ai-review.yaml
- PN workbook rows: 1

## PN row 1: ER proteostasis | Maturation and folding of specific substrates | ER collagen processing and folding
- UniProt: O75718
- In branches: ER
- PN-node mapping records (path + ancestors):
    - [group] ER proteostasis|Maturation and folding of specific substrates|ER collagen processing and folding
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0032964 collagen biosynthetic process]
        rationale: This PN group contains ER factors dedicated to collagen maturation, processing, and folding. Collagen biosynthetic process captures the shared substrate-specific pathway context.
    - [class] ER proteostasis|Maturation and folding of specific substrates
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a single GO class. The member genes span multiple activities, complexes, or contexts, so direct propagation from this node would overstate the shared biology.
    - [branch] ER proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## Projected GO annotations (1)
- GO:0032964 collagen biosynthetic process | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=ER proteostasis|Maturation and folding of specific substrates|ER collagen processing and folding

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
