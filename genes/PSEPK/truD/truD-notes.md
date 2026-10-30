# truD (PP_1619, Q88MF2): curation notes

Dashboard gene: DOAB01000105.1_3 (P. putida, tier A), https://gene-annotate-dashboard.kbase.us/review/DOAB01000105.1_3
Filed on Swiss-Prot Q88MF2 (TRUD_PSEPK, KT2440 PP_1619): 351/352 identical (99.7%), no gaps. The exact UniParc entries were deleted (not in a reference proteome).

## Conclusion

PP_1619 is the TruD-family tRNA pseudouridine(13) synthase (EC 5.4.99.27). This is an assignment by orthology; the P. putida protein has never been assayed.

- It is 37.3% identical over 343 aligned residues to E. coli TruD (Q57261). E. coli TruD was purified as the tRNA(Glu) Psi13 synthase, and deleting it loses Psi13, which complementation restores (PMID:12756329).
- **Catalytic Asp conserved.** E. coli Asp80 (in the GXKD motif; D80N/T inactive) corresponds to query Asp81 (GLKD 78-81). Glu31, the proposed general base (PMID:19664587), corresponds to Glu32. The four other annotated E. coli functional residues are also conserved. The analysis is in `truD-bioinformatics/` and BERIL run `20261030T211234Z-trud-identity-catalytic-site`.
- **Substrate range.** Thermus TruD modifies U13 of tRNA(Asp), tRNA(Glu) and tRNA(Gln), and U35 of tRNA(Tyr) (PMID:40138658). Which P. putida tRNAs TruD modifies is unknown.

## Dashboard verdict: supported

- **Corrected annotation:** none needed. Optionally: "tRNA pseudouridine(13) synthase TruD (EC 5.4.99.27); tRNA substrates in P. putida untested."
- **GO terms:**
  - GO:0160150 tRNA pseudouridine(13) synthase activity: **CNN**. It is already in GOA as an IEA.
  - GO:0006400 tRNA modification: **LSP**. GOA already has the descendant GO:0031119 tRNA pseudouridine synthesis.
  - GO:0005737 cytoplasm: **CNN**. GOA has the child term cytosol.
- The call is consistent with the evidence the annotator saw. It also does not over-claim tRNA specificity, and it correctly ignored the PaperBLAST "xylose receptor" homolog at 37.9%, which is an AI-2/XylF blastx artefact.
- The evidence shown contained no TruD biochemistry paper. Tier A therefore rests on domain signatures, not on literature the annotator read.

## Existing GOA for Q88MF2 (9 IEA, no experimental)

- **ACCEPT:** GO:0160150, GO:0031119 and GO:0005829.
- **KEEP_AS_NON_CORE:** GO:0009982, GO:0001522 and GO:0009451.
- **MARK_AS_OVER_ANNOTATED:** GO:0003723 RNA binding, GO:0006396 RNA processing and GO:0140098 catalytic activity, acting on RNA.

## Caveats

- **The only P. putida paper is not about function.** PMID:20398259 names PP_1619 as a "conserved hypothetical protein" with one miniTn5 insertion among phenol-tolerant derivatives of a colR mutant. The downstream gene pcm (PP_1621) had 4 insertions in the same screen, so a polar effect on pcm is plausible. This says nothing about TruD activity.
- **No fitness data for PP_1619.** `just fetch-fitness` failed because no FEBA source was reachable. The dashboard evidence holds only homolog fitness: P. fluorescens 79% (L-malate, -1.4) and Shewanella 40% (various N/C sources, about -3 to -4.6). These are pleiotropic growth defects with no bearing on the molecular function.
- **P33643 is not E. coli TruD.** The brief named P33643, but that accession is E. coli RluD (23S rRNA Psi synthase, catalytic Asp139). E. coli TruD is Q57261. Q57261 was used here.

## Tooling

- **fetch-gene.** `just fetch-gene` failed twice at the OLS NCBITaxon label lookup (read timeout). The YAML stub was seeded by calling `fetch_gene_data` with the label resolved through `ubergraph:`, as was done for yxcA. The stub first landed in `genes/genes/PSEPK/truD/` because of a base_path slip; it was moved into place, and that stray directory was removed.
- **fetch-fitness** failed: no FEBA source was reachable.
- **validate-predictions** also writes `reports/prediction-evidence.json` (the recipe's own report output).
