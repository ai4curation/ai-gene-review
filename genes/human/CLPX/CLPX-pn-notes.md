# CLPX PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: O76031
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/CLPX/CLPX-ai-review.yaml](CLPX-ai-review.yaml)
- AIGR review HTML: present - [genes/human/CLPX/CLPX-ai-review.html](CLPX-ai-review.html)
- Gene notes: present - [genes/human/CLPX/CLPX-notes.md](CLPX-notes.md)
- GOA TSV: present - [genes/human/CLPX/CLPX-goa.tsv](CLPX-goa.tsv)
- UniProt record: present - [genes/human/CLPX/CLPX-uniprot.txt](CLPX-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/CLPX.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/CLPX.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/CLPX.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/CLPX.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: CLPX is the regulatory AAA+ ATPase/unfoldase subunit of the mitochondrial-matrix ClpXP protease. It is imported into mitochondria via an N-terminal transit peptide, assembles into a homohexameric ring (ATP-dependent), and pairs with two heptameric rings of the CLPP peptidase to form the symmetry-mismatched ClpXP protease. Using energy from ATP binding and hydrolysis, CLPX recognizes specific substrate proteins, unfolds them, and translocates the unfolded polypeptide through its central pore into the CLPP proteolytic chamber for degradation, contributing to mitochondrial protein quality control. Independently of CLPP-coupled degradation, CLPX also acts as a chaperone/unfoldase that remodels and activates δ-aminolevulinate synthase (ALAS) by accelerating incorporation of the pyridoxal 5'-phosphate (PLP) cofactor, thereby stimulating the first, rate-limiting step of heme biosynthesis and supporting erythropoiesis; it also contributes to heme-induced turnover of ALAS, so the balance of activation and degradation tunes ALAS activity. CLPX contains a ClpX-type zinc-binding domain and a P-loop AAA+ ATPase module, and mutations affecting its ATPase activity cause autosomal dominant erythropoietic protoporphyria 2 (EPP2).
- Existing/core annotation action counts: ACCEPT: 18; KEEP_AS_NON_CORE: 9; MARK_AS_OVER_ANNOTATED: 6; NEW: 1

## PN Consistency Summary

- **Consistency:** Consistent on the core. Notes, YAML, and PN agree CLPX is the AAA+ unfoldase subunit of the matrix ClpXP protease (matrix localization, protein catabolism). Both projected GO terms (GO:0005759, GO:0035694) are verified real. One nuance: GO:0035694's GO definition is framed around an intramitochondrial lysosome-like degradation organelle, which is a narrower/atypical concept than ClpXP-mediated soluble-matrix proteolysis; the review instead uses GO:0030163 protein catabolic process + GO:0006508 proteolysis (the GOA term is the non-mitochondrial GO:0030163 IDA).
- **PN story / NEW pressure:** PN's degradation story is already well captured (matrix + protein catabolism). The review's distinctive, well-supported addition is the CLPP-independent chaperone role: GO:0006783 heme biosynthetic process via ALAS activation (action NEW, PMID:25957689, PMID:28874591, EPP2 disease). The PN node does NOT surface this heme/ALAS axis — a PN-side gap rather than a review gap.
- **Evidence alignment:** No PN reference titles were listed for this row, so no title-level overlap to compare; the review is densely cited (PMID:11923310, 16115876, 22710082, 25957689, 28874591). No conflict.
- **Verdict:** Consistent; degradation captured. PN mapping over-specifies the catabolic process (GO:0035694 definitional mismatch) and omits the heme/ALAS chaperone role.

## Full Consistency Review

- **UniProt:** O76031 · **batch:** proteostasis-batch-2026-06-07 · **review status:** COMPLETE
- **PN placement:** `Mitochondrial proteostasis|Organelle-specific protein degradation|Matrix protease` ; **PN-node mapping:** `[group] Matrix protease` → `mapped` GO:0005759 mitochondrial matrix (`already_in_goa_exact`); `[class] Organelle-specific protein degradation` → `mapped` GO:0035694 mitochondrial protein catabolic process (`more_specific_than_existing_goa`); branch unmapped.
- **Consistency:** Consistent on the core. Notes, YAML, and PN agree CLPX is the AAA+ unfoldase subunit of the matrix ClpXP protease (matrix localization, protein catabolism). Both projected GO terms (GO:0005759, GO:0035694) are verified real. One nuance: GO:0035694's GO definition is framed around an intramitochondrial lysosome-like degradation organelle, which is a narrower/atypical concept than ClpXP-mediated soluble-matrix proteolysis; the review instead uses GO:0030163 protein catabolic process + GO:0006508 proteolysis (the GOA term is the non-mitochondrial GO:0030163 IDA).
- **PN story / NEW pressure:** PN's degradation story is already well captured (matrix + protein catabolism). The review's distinctive, well-supported addition is the CLPP-independent chaperone role: GO:0006783 heme biosynthetic process via ALAS activation (action NEW, PMID:25957689, PMID:28874591, EPP2 disease). The PN node does NOT surface this heme/ALAS axis — a PN-side gap rather than a review gap.
- **Mapping strategy:** Largely sound, but the `[class]` projection to GO:0035694 is questionable: its GO definition does not match ClpXP matrix proteolysis well, and the existing GOA term is the broader GO:0030163. Prefer mapping the class to GO:0030163 protein catabolic process (or qualify GO:0035694) to avoid asserting a process the term's definition does not support.
- **Evidence alignment:** No PN reference titles were listed for this row, so no title-level overlap to compare; the review is densely cited (PMID:11923310, 16115876, 22710082, 25957689, 28874591). No conflict.
- **Verdict:** Consistent; degradation captured. PN mapping over-specifies the catabolic process (GO:0035694 definitional mismatch) and omits the heme/ALAS chaperone role.

**Recommended edits:** [MAP] Reconsider `[class]` projection GO:0035694 → use GO:0030163 protein catabolic process (matches GOA + ClpXP biology; GO:0035694's definition is lysosome-like-organelle specific). [MAP] Optionally extend the PN node to reflect CLPX's GO:0006783 heme biosynthesis chaperone role.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07
- review_yaml: genes/human/CLPX/CLPX-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Mitochondrial proteostasis | Organelle-specific protein degradation | Matrix protease
- UniProt: O76031
- In branches: MI
- PN-node mapping records (path + ancestors):
    - [group] Mitochondrial proteostasis|Organelle-specific protein degradation|Matrix protease
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0005759 mitochondrial matrix]
        rationale: This PN group identifies matrix-local protease systems. The source is a compartmental proteostasis bucket, so the mitochondrial matrix cellular-component term is the conservative propagation target.
    - [class] Mitochondrial proteostasis|Organelle-specific protein degradation
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0035694 mitochondrial protein catabolic process]
        rationale: This PN class groups mitochondrial protein-degradation pathways. GO mitochondrial protein catabolic process is the conservative shared target.
    - [branch] Mitochondrial proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## Projected GO annotations (2)
- GO:0035694 mitochondrial protein catabolic process | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=Mitochondrial proteostasis|Organelle-specific protein degradation
- GO:0005759 mitochondrial matrix | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Mitochondrial proteostasis|Organelle-specific protein degradation|Matrix protease

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
