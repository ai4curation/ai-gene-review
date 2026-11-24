# GCN5 notes

Falcon deep research supports the existing core interpretation of GCN5 as the catalytic lysine acetyltransferase subunit of yeast SAGA/ADA chromatin coactivator complexes: "Purified recombinant and native Gcn5-containing complexes catalyze acetyl-CoA-dependent histone acetylation, and loss or catalytic mutation of Gcn5 abolishes nucleosomal HAT activity" [file:yeast/GCN5/GCN5-deep-research-falcon.md].

The main substrate-specific evidence remains histone H3 acetylation, with Falcon summarizing that "ADA/Gcn5 acetylates multiple H3 lysines with strong preference for H3K14 and detectable activity on H3K9, K18, K23, K27, and K36" [file:yeast/GCN5/GCN5-deep-research-falcon.md].

Falcon also supports retaining the histone crotonyltransferase annotation as a genuine catalytic activity: "Purified Gcn5-Ada2-Ada3 (ADA) crotonylates histone H3 in vitro at K9, K14, K18, K23, and K27" [file:yeast/GCN5/GCN5-deep-research-falcon.md].

Generic `protein binding`, broad `DNA-templated transcription`, cytoplasmic/mitochondrial localization, and stress-response phenotypes should remain non-core or removed where the current YAML already marks them that way, because Falcon frames the best-supported function as nuclear chromatin coactivation through histone acylation rather than generic interaction or pleiotropic phenotype terms [file:yeast/GCN5/GCN5-deep-research-falcon.md].

## Source-defect re-review (2026-11-10)

An independent re-review of this gene's wrong-gene / wrong-reference source defects changed the following; where earlier notes above say otherwise, this section supersedes them.

- GO:0061733 / PMID:18250157: defect retyped (evidence depth: FULL_TEXT). The live GO_Central row has has_input human CDK9 (P50750), so the paper is the intended one and the enzyme entity is wrong - WRONG_GENE_PRODUCT, not WRONG_REFERENCE. PMC full text - human cells, siRNA to endogenous GCN5 in U2OS, catalytic mutant Y260A/F261A, numbering that fits truncated human GCN5 (KAT2A Tyr621/Phe622, offset 361; sequences checked) and not yeast Gcn5 (Tyr220/Phe221; 260-261 = Tyr-Leu). REPOINT to UniProtKB:Q92830 (KAT2A, synonym GCN5, verified), cause SYMBOL_COLLISION. ACCEPT kept because the term is true of yeast Gcn5 on yeast evidence (reason says so).
- GO:0061733 / PMID:28426094: defect retyped (evidence depth: FULL_TEXT). Same pattern (has_input human CDK9; companion rows on human SIRT7/CDK9 made the same day). Cached full text is a human HEK293T study using Flag-GCN5 and never mentions yeast, but does not state the species of the Flag-GCN5 construct, so PROBABLE. Retyped to WRONG_GENE_PRODUCT, REPOINT to UniProtKB:Q92830, cause SYMBOL_COLLISION.
