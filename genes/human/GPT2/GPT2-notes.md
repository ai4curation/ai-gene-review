# Human GPT2 (ALT2) full annotation review

## 2026-10-25 canonical enzyme, isoforms and physiology

Normally seeded human Q8TD30 with alias GPT2. All 11 original rows and both seeded alternative products are preserved; no NEW annotations are added. Current UniProt classifies GPT2 in PTHR11751:SF311, distinct from GPT/ALT1 SF308.

Human recombinant primary PMID:11863375 establishes reversible alanine/2-oxoglutarate transamination. Human variant primary PMID:25758935 tests wild-type and S153R recombinant ALT2, with severe loss of activity in the disease variant; its human protein expressed experimentally must be distinguished from model-organism physiology. Primary PMID:19360321 reports: "ALT1 and 2 possess similar enzymatic activity for alanine and pyruvate but with different Km and kcat values". It separately reports no detectable activity for the tested alternative splice form ALT2_2. The canonical enzyme remains active; a family-level activity should not be interpreted as an assay of every isoform.

Primary PMID:27601654 links human disease variants to biochemical loss of function and uses mouse metabolomics/isotope tracing for alanine production and anaplerosis. Its normal cache is abstract-only; publisher abstract and initial clinical/variant Results were inspected during preliminary research, but no complete supplement or raw tracing dataset is claimed. The corrected publisher/current abstract names p.Arg404* and p.Pro272Leu; older indexed snippets contain different nonsense-variant wording, so no uncertain residue claim is used in the review. Both alanine synthesis and breakdown are legitimate directions of the direct reaction. Brain alanine-production context does not imply the enzyme invariably synthesizes alanine; catalytic direction depends on substrates and physiological state. No extra brain-development or TCA-process NEW is added from necessity/metabolomic evidence alone.

## Localization and cofactor evidence

PMID:19360321 separates human muscle organelles and detects ALT2 in mitochondrial and ER fractions but not cytosol. PMID:27601654 independently supports mitochondrial localization. Neither is represented as a newly inspected matrix-resolution assay. The existing curated Reactome R-HSA-507749/R-HSA-507775 and ortholog matrix assignments are retained conservatively for the soluble mitochondrial enzyme; the finer matrix location is explicitly distinguished from the direct organelle-level evidence. Thus broad mitochondrion is refined to the already asserted matrix without claiming exclusive localization or rewriting the original HTP measurement.

Current UniProt's cofactor feature and Reactome's description of human GPT2 structure PDB3IHJ support PLP. The Reactome summary says the structure is consistent with a homodimer and one PLP per monomer; it is not described as a new peer-reviewed kinetic study. PLP is integrated into the catalytic core. The 2-oxoglutarate metabolic-process row reflects a direct substrate/product, not merely a changed metabolite concentration.

## Access and provenance

Normal Falcon/default and perplexity-lite fallback were attempted with publication caching in parallel. Both provider attempts failed with access/credit errors; no provider output was invented. All reviewed sources were normally cached; rate-limited requests were retried serially. Source files, alternative products and original annotation payloads remain unchanged. Helper-generated codex history, record-section backfill, strict/term validation, rendered HTML and row-preservation proof accompany this complete review.


## Root-organelle policy correction (2026-10-25)

Reassessed all 1 mitochondrion (GO:0005739) rows against their original source scope and independent localization evidence. Changed MODIFY to ACCEPT: CLAUDE.md and projects/ORGANELLES.md explicitly retain a supported root organelle rather than replacing it with a subcompartment. The row-specific reasons distinguish direct localization/proteomics from similarity or phylogenetic inference and preserve source-resolution limits. Existing matrix rows, core locations and other annotations are unchanged; no NEW row was added. This supersedes the earlier matrix-replacement decisions, not their historical records. No inferred granularity failure is retained for a biologically sound IBA.
