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
- Falcon deep research (CG30022-deep-research-falcon.md, arrived after initial commit): CG30022 =
  dEthe1 (58% identity to human ETHE1), predicted N-terminal mitochondrial targeting sequence; a 2011
  thesis reports an EMS P157S allele with reduced complex IV (COX) activity, mirroring sulfide
  inhibition of COX in ETHE1 deficiency; CG30022 is upregulated in tko25t mitochondrial-translation
  mutants. No purified-enzyme or localization data. Sources not cached (thesis); no annotation changes.
- PR #4483 follow-up: checked the six QuickGO rows on the alternative accession Q86PD3 (GO:0050313 IBA/IEA,
  GO:0006749 IBA/IEA, GO:0005739 IBA/IEA). All three terms are already reviewed here on A0ACM8PZC4 (from
  ISS/IEA rows), so no term goes unreviewed; the IBA rows exist only on Q86PD3 and would get the same
  actions (accept sulfur dioxygenase; mitochondrion -> matrix; glutathione metabolism -> sulfide oxidation).
