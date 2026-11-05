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
