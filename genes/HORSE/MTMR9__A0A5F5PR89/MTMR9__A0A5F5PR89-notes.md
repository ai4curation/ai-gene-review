# MTMR9 (horse, A0A5F5PR89) notes

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

### Identity of this entry

- A0A5F5PR89 is the 549-aa product of Ensembl transcript ENSECAT00000074905 (gene ENSECAG00000014120,
  VGNC:20431 MTMR9). It is unreviewed (TrEMBL); there is no Swiss-Prot horse MTMR9.
- Other horse products of the same gene: A0A9L0T3C1 (507 aa; lacks the segment equivalent to human 98-139)
  and F7CCR9 (553 aa; Ensembl canonical and the gene's member in the PANTHER tree, but its divergent last exon
  truncates the C-terminal coiled coil). See `genes/HORSE/MTMR9/MTMR9-bioinformatics/RESULTS-rereview.md`
  (read only, not modified): A0A5F5PR89 is 98.0% identical to human Q96QG7 with no missing segments.
- Folder named `MTMR9__A0A5F5PR89` following the `<HOST>__<ACC>` convention, because `genes/HORSE/MTMR9/`
  already holds the A0A9L0T3C1 review. Fetched with
  `just fetch-gene HORSE A0A5F5PR89 --alias MTMR9__A0A5F5PR89`.

### Deep research

`just deep-research-falcon HORSE MTMR9__A0A5F5PR89 --fallback perplexity-lite` failed on 2026-10-20: falcon
returned "Edison API request failed: Failed to authenticate", and perplexity-lite returned HTTP 401
(insufficient quota). No deep-research file was produced. A web search found no horse-specific functional
study of MTMR9 (only reagent and database pages). I used the cached primary papers and the human review
(`genes/human/MTMR9/`) as the literature base.

### Evolutionary grounding

- PANTHER: horse record maps to PTHR10807:SF56 (MYOTUBULARIN-RELATED PROTEIN 9), the same subfamily as human
  Q96QG7, mouse Q9Z2D0 and bovine A7MB43. This is the subfamily of the experimentally characterised proteins,
  so subfamily-level functions (partner activation) transfer.
- PAINT (`interpro/panther/PTHR10807/PTHR10807-paint.tsv`):
  - PTN002246859 (MTMR9 clade, taxon 6072 Eumetazoa) carries IBD GO:0019903 protein phosphatase binding and
    GO:0010507 negative regulation of autophagy, both seeded by human Q96QG7.
  - PTN000743854 (deep node) carries GO:0005737 cytoplasm.
  - Human MTMR9 also receives GO:0046856 phosphatidylinositol dephosphorylation from PTN008506586.
  - A0A5F5PR89 is not a tree leaf and has no IBA rows; F7CCR9 is the horse leaf.
- New analysis `MTMR9__A0A5F5PR89-bioinformatics/compare_to_human.py` -> `RESULTS.md`:
  - 98.0% identity, no gaps, 11 substitutions, none in the active-site loop or the coiled coil.
  - PH-GRAM 97.9%, phosphatase-like domain 97.6%, coiled coil (human 508-542) 100%.
  - HCX5R loop `HGTEGTDST` identical to human. The catalytic Cys and Arg are therefore replaced, as in
    human and mouse (`genes/human/MTMR9/MTMR9-bioinformatics/RESULTS-rereview.md`), so horse MTMR9 is
    predicted to be catalytically inactive, like its orthologs.

### Experimental evidence (all non-horse)

- Human: MTMR6-MTMR9 heteromer; MTMR9 raises MTMR6 3-phosphatase activity up to 6-fold and stabilizes it
  [PMID:19038970 "MTMR9 increased the 3-phosphatase activity of MTMR6 up to 6-fold"].
- Human: MTMR9 sets MTMR6 versus MTMR8 substrate preference; MTMR8-MTMR9 lowers PI3P and inhibits autophagy
  [PMID:22647598 "Complex formation between the active myotubularins and MTMR9 increases their catalytic
  activity and alters their substrate specificity"].
- Human: MTMR8-MTMR9 heteromer and cytoplasmic/perinuclear localization [PMID:16787938].
- Mouse: Mtmr9 binds Mtmr7 via its coiled coil and raises its Ins(1,3)P2 phosphatase activity
  [PMID:12890864].
- Mouse/human: MTMR6 and MTMR9 required for late macropinocytosis; ruffle localization [PMID:24591580].

### Decisions

- The 5 GOA rows are all IEA (ARBA or SubCell mappings of ARBA location lines):
  - cytosol: ACCEPT.
  - ER, perinuclear region, ruffle membrane: KEEP_AS_NON_CORE.
  - enzyme regulator activity: MODIFY to GO:0019211 phosphatase activator activity.
  - Support for each row comes from the human experimental data plus the subfamily and sequence grounding,
    not from the ARBA rules.
- NEW (ISS from human): GO:0019902 phosphatase binding, GO:0060304 regulation of phosphatidylinositol
  dephosphorylation, and GO:0050821 protein stabilization. MTMR9 itself does the work in each case, as the
  binding and activating subunit.
- Not proposed:
  - GO:0010507 negative regulation of autophagy is placed by PAINT but is a downstream cell-level
    consequence. The human review kept it only as non-core, and it is not proposed for this IEA-only horse
    entry.
  - Apoptosis and macropinocytosis rest on cultured-cell necessity or over-expression evidence and are not
    proposed.
  - GO:0046856 phosphatidylinositol dephosphorylation is not proposed, because MTMR9 is catalytically dead.
    The regulation term captures its role.
- Nothing in this review is experimentally established in horse; every function is inferred from human and
  mouse orthologs in the same PANTHER subfamily.
