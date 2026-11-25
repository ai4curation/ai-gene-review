# KRIT1 evidence notes

[PMID:21633110](https://pubmed.ncbi.nlm.nih.gov/21633110/), DOI [10.1091/mbc.E11-02-0157](https://doi.org/10.1091/mbc.E11-02-0157), directly establishes GTP-dependent Rap1 effector binding and junctional recruitment. [PMID:17916086](https://pubmed.ncbi.nlm.nih.gov/17916086/) supports microtubule/PIP2 interactions. [PMID:23317506](https://pubmed.ncbi.nlm.nih.gov/23317506/) gives the ICAP1 competition structure, and [PMID:20332120](https://pubmed.ncbi.nlm.nih.gov/20332120/) links CCM1 to VE-cadherin/Par polarity organization. These supply the molecular scaffold mechanism, independently of the Falcon synthesis. The early PMID:9285558 two-hybrid speculation that KRIT1 might regulate Krev-1 does not establish GEF/GAP catalysis; use the directly demonstrated small-GTPase binding function.

[PMID:20616044](https://pubmed.ncbi.nlm.nih.gov/20616044/) reports inhibition of endothelial proliferation, apoptosis, migration, lumen formation and sprouting. The same biology supports the broad horse developmental-process GOA rows, but does not establish spermatogenic piRNA production. ROS/FOXO1/SOD2 effects in [PMID:20668652](https://pubmed.ncbi.nlm.nih.gov/20668652/) are regulatory phenotypes rather than intrinsic redox catalysis.

The horse record is719 aa and aligns at 98.5% identity across 719 paired residues to736 aa human KRIT1. The N-terminal interaction motifs and C-terminal FERM scaffold are retained; see the full alignment for the internal 17 aa gap. The initial horse search returned studies mentioning conserved KRIT1 structures but no horse-specific functional assay. Human Falcon research is complete; no separate horse Edison was selected.

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

Deep research: `just deep-research-falcon HORSE KRIT1 --fallback perplexity-lite` failed on 2026-10-20. Falcon returned "Failed to authenticate", and perplexity-lite returned HTTP 401 for insufficient quota. No horse deep-research file was created. I used the cached primary papers and the human falcon report (`genes/human/KRIT1/KRIT1-deep-research-falcon.md`) as background.

### Identity: A0A9L0SR44 is a non-canonical alternative product of horse KRIT1

- The UniProt search `gene:KRIT1 AND organism_id:9796` returns three unreviewed entries, all on Ensembl gene ENSECAG00000016850:
  - A0A3Q2GZV2, 736 aa (ENSECAT00000036518)
  - A0A3Q2LAF1, 727 aa (ENSECAT00000063479)
  - A0A9L0SR44, 719 aa (ENSECAT00000146800), the benchmark entry
- The Ensembl canonical transcript is ENSECAT00000118392 (753 aa). There is no reviewed horse entry.
- PAINT IBA rows (plasma membrane, negative regulation of angiogenesis, regulation of establishment of cell polarity, cell redox homeostasis) are present on A0A3Q2GZV2 only. That is consistent with A0A3Q2GZV2 being the gene-centric representative and A0A9L0SR44 being an alternative product.
- New analysis, `KRIT1-bioinformatics/compare_sequences_rereview.py` → `RESULTS-rereview.md`:
  - A0A9L0SR44 vs A0A3Q2GZV2: 716/719 identical, with one 17-residue gap.
  - A0A3Q2GZV2 vs human O00522: 726/736 identical, with no gaps.
  - A0A9L0SR44 lacks the residues equivalent to human 715-731 (`AGLVIKLLIKLNGQLMP` in horse A0A3Q2GZV2). It ends in a divergent `TKKQS` instead of `TERNS`.
- The missing segment holds Leu717 and Leu721. These residues form the HEG1-binding groove at the FERM F1/F3 interface. In human KRIT1, the L717,721A mutant is well folded but fails to target to EC junctions [PMID:23007647 "Although well folded and expressed, KRIT1(L717,721A) failed to target to EC junctions"].
- The Rap1 interface is retained, including Arg452 and the 430-452 region [PMID:21633110 "KRIT1 is an authentic Rap1-specific effector that binds strongly to the effector loop of active Rap1A"]. So are the N-terminal NPxY motifs, the ankyrin repeats and FERM F1/F2.
- Interpretation: this product most likely comes from an alternative 3' splice or terminal exon, unless it is a gene-model artefact. No transcript evidence was checked. If it is expressed, it is predicted to bind Rap1 without HEG1-dependent anchoring at junctions.
- The earlier RESULTS.md feature-correspondence table is empty, because O00522 has no ACT_SITE/BINDING-type features. The earlier review did not identify the C-terminal difference. I left RESULTS.md unchanged.

### Evolutionary grounding

- A0A9L0SR44, A0A3Q2GZV2 and human O00522 are all in PANTHER PTHR13283:SF11 (KREV INTERACTION TRAPPED PROTEIN 1). FRMD8 is in a different subfamily of the same family. No FRMD8-specific functions (iRhom/ADAM17) are transferred.
- The relevant PAINT nodes are:
  - PTN002665063 (KRIT1 clade): microtubule binding, regulation of establishment of cell polarity, cell redox homeostasis, and anterior/posterior axis specification. The axis term comes from a zebrafish donor and is a downstream phenotype, so it is not used here.
  - PTN002665064: negative regulation of angiogenesis.
  - PTN004412369 (deep node, KRIT1 + FRMD8 + worm): plasma membrane.

### Decisions

| Term | Action | Reason |
|---|---|---|
| cytoskeleton | MODIFY → GO:0015630 microtubule cytoskeleton | The evidence is microtubule-specific [PMID:17916086] |
| plasma membrane | ACCEPT | PIP2 binding and Rap1-dependent membrane recruitment; the Rap1 interface is retained |
| anchoring junction | UNDECIDED | Correct for the canonical product (would refine to cell-cell junction), but this product lacks the L717/L721 HEG1 anchoring residues |
| negative regulation of developmental process; regulation of multicellular organismal development | MODIFY → GO:0016525 negative regulation of angiogenesis | The descendant term is directly supported [PMID:20616044] and IBA'd to the clade. The previous review had KEEP_AS_NON_CORE while arguing the terms were general, which conflicts with the MODIFY rule. |
| small GTPase binding; microtubule binding | NEW | Direct molecular activities with experimental evidence for human KRIT1, transferred within SF11 |

- No new process terms are proposed. Cardiovascular-development and CCM phenotypes are organismal consequences.

### Relative to review next

The relative is horse A0A3Q2GZV2, the full-length 736-aa product of the same gene. It carries the PAINT IBAs. If curated, it would live at `genes/HORSE/KRIT1__A0A3Q2GZV2`, and it has no review in the repo. Human KRIT1 (O00522, `genes/human/KRIT1`) has every row reviewed, though its status is IN_PROGRESS.

### Family file

`interpro/panther/PTHR13283/PTHR13283-review.yaml` places A0A9L0SR44 in SF11, which agrees with UniProt. However, the SF11 `description` copies the family-level KRIT1-vs-FRMD8 coherence text, and so describes FRMD8 inside the KRIT1 subfamily. A0A9L0SR44 is also listed as the representative, although it is an alternative C-terminal product; A0A3Q2GZV2 would be a better horse representative. I did not edit the family file.

No KRIT1/CCM module exists in `modules/`. `modules/dmel_stripak_complex.yaml` covers only Ccm3/PDCD10. KRIT1 does not appear in `gocams/index.tsv`.

## 2026-10-21 — NEW rows withdrawn from the alternative gene model (PR #5303 review)

The re-review had proposed NEW rows (GO:0008017) on this benchmark accession because GOA propagates the
gene's annotations, including PAINT IBA rows, to one representative product per gene and not to
alternative transcript models. The same terms are already annotated in GOA on the canonical horse
product of this gene (KRIT1__A0A3Q2GZV2, reviewed in `genes/HORSE/KRIT1__A0A3Q2GZV2/`). Filling that propagation
convention on a second product of the same gene is not a curation gap, so the rows were withdrawn
for consistency across the cohort. The gene-level function is unchanged and is recorded on the
canonical product's review; this file's description and core functions still describe it.
