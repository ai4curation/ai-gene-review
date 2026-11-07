# lspA (Bacillus subtilis 168, Q45479) curation notes

Added as the monoderm exemplar of the LspA step in `modules/bacterial_lipoprotein_maturation.yaml`.

- Provider deep research could not run: `just deep-research-falcon BACSU lspA` failed with a 403 authentication error
  (2026-11-02), the only configured provider key, and no MOD description provider exists for BACSU. The review relies on the
  UniProt record and two cached primary papers, both abstract-only in the cache.
- Cloned by complementing an E. coli lsp(ts) mutant; activity shown by pulse labelling in E. coli
  [PMID:9141696 "Activity of the B. subtilis SPase II was demonstrated by a pulse-labelling experiment in E. coli."].
- Mutagenesis of 15 conserved residues; Asp-102 and Asp-129 proposed as catalytic, making SPase II an aspartic protease;
  non-essential in B. subtilis [PMID:10497172 "which, unlike SPase II of Escherichia coli, is not essential for viability"].
- Decisions follow the E. coli and P. putida lspA reviews: generic endopeptidase (IBA) and proteolysis/membrane (InterPro IEA)
  are refined to aspartic-type endopeptidase activity, lipoprotein biosynthetic process and plasma membrane.
- 2026-11-02 retry: `just deep-research BACSU lspA --provider perplexity` failed with "Provider 'perplexity' not available.
  Available: falcon, openscientist, claude_code" (no Perplexity key in this environment). No provider-named deep-research
  file exists for this gene.
- An lspA-null strain is viable but impaired at temperature extremes and accumulates lipid-modified PrsA precursor
  [PMID:9880550 "Cells lacking SPase II accumulated lipid-modified precursor and mature-like forms of PrsA"].


## 2026-11-07 source and ontology audit

Reviewed all original rows, references and core activity. Original annotation payloads/order and historical NEW actions are preserved; no row was added or retired. See `analysis/module_audits/bacterial_lipoprotein_maturation/ecoli-bacsu-consultation/evidence.md` for the complete source/construct and ontology rationale. All genuine Falcon attempts returned authentication HTTP403; manual synthesis is recorded here without creating provider output. Final PAINT lineage inspection reported no IRD/IKR loss; initial cold-cache download races were retried sequentially and logged. Protected publication/provider/raw files remain unchanged.

Current GO:0009003 signal peptidase activity is active and supplies the substrate-directed core genus; GO:0004190 remains a correct mechanistic assertion. Generic endopeptidase refines to both; proteolysis refines to protein processing. The specific proposal retains only lipidated-prolipoprotein/Cys context. Bacillus downstream LhaT acetylation prevents an inference that all products remain diacylated.


## PR 6184 source adjudication, 2026-11-07

The lipoprotein signal peptidase proposal now uses GO:0009003 as its substrate-defined parent, matching the PSEPK proposal. GO:0004190 describes the independent aspartic catalytic mechanism and remains valid; no corresponding original annotation or core activity was removed or changed.
