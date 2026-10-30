# drkA (Q54H46; rk1, vsk1; DDB_G0289791) notes

## Identity and architecture
- 642 aa; signal peptide 1-23, extracellular 24-322, TM 323-343, cytoplasmic 344-642 with protein kinase domain 374-627 (UniProt features, predicted). ATP loop 380-388, K401, proton acceptor D497. N-glycosylation sites predicted in ectodomain.
- TKL group, DRK family receptor kinase [PMID:16596165 "The other three receptor kinases in the TKL group are unstudied, and are from the DRK family"]; rk1 and rk2 share a Dictyostelium-specific extracellular domain [PMID:16596165 "rk1 and rk2 have closely related extracellular domains that are unique to Dictyostelium"].

## Function (Saga et al. 2019; abstract only in cache)
- Candidate STATa kinase identified by homology to tyrosine-selective TKLs (Pyk2/Pyk3 are STATc kinases) [PMID:31002205 "we identified DrkA, a member of the TKL family and the Dictyostelium receptor-like kinase (DRK) subfamily, as a candidate STATa kinase"].
- Expression almost exclusively in pstA cells [PMID:31002205 "The drkA gene is almost exclusively expressed in prestalk A (pstA) cells, where STATa is activated"].
- Over-expression increases STATa phosphorylation but is toxic [PMID:31002205 "Transient over-expression of DrkA increased STATa phosphorylation"].
- Autophosphorylates on Tyr and Thr; phosphorylates STATa Tyr702 in vitro, SH2-dependent [PMID:31002205 "recombinant DrkA protein is auto-phosphorylated on tyrosine and threonine residues"].

## Curation reasoning
- Core MF: protein tyrosine kinase activity (IDA). Ser/Thr: Thr autophosphorylation only -> non-core; serine kinase (Rhea) unsupported -> over-annotated.
- Cytoplasm IBA: PANTHER node dominated by soluble TKLs; DrkA is a predicted type I TM protein -> over-annotated.
- Root CC ND removed (membrane IEA present).
- No NEW terms: localization (plasma membrane vs vesicle) not experimentally established; "vsk1"/"vesicle-associated" name has no traceable primary evidence found.

## Deep research
- `just deep-research-falcon DICDI drkA --fallback perplexity-lite` was run (2026-10-05) but produced no output file (falcon and perplexity-lite fallback both yielded nothing; log not retained). Review is based on cached publications (PMID:31002205 abstract, PMID:16596165 full text), UniProt and web search.
