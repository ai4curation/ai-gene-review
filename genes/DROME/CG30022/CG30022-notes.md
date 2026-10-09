# CG30022 notes

- 2026-10-09: Initial review of CG30022 (FBgn0050022), fly ETHE1 ortholog (persulfide dioxygenase).
- Accession: `just fetch-gene DROME CG30022` resolved to Q86PD3 (6 GOA rows); the expected accession
  A0ACM8PZC4 has 9 GOA rows (superset incl. FlyBase ISS rows), so the review uses A0ACM8PZC4
  (fetched with `--alias CG30022`). UniProt gives Name=CG9026 on A0ACM8PZC4 with Dmel\CG30022 as a
  synonym; gene_symbol set to the FlyBase symbol CG30022.
- No fly publications; all annotations ISS (human ETHE1 O95571) or IEA.
- Decisions: sulfur dioxygenase and sulfide oxidation accepted by orthology; mitochondrion ->
  mitochondrial matrix; glutathione metabolic process -> sulfide oxidation; iron ion binding ->
  ferrous iron binding; nucleoplasm (from early human HSCO overexpression data) over-annotated.
