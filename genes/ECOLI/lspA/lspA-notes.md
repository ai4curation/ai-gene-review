# lspA notes

## 2026-10-02

`just deep-research-falcon ECOLI lspA` could not run in this Orca environment
because `agentapi` was not available on `PATH` and no provider API keys were
configured, so this review uses the cached primary literature from
`just fetch-gene` plus the fetched UniProtKB record.

Manual synthesis:

- LspA/signal peptidase II is a four-transmembrane inner-membrane protease:
  Munoa et al. found that "The lsp gene of Escherichia coli encodes the inner
  membrane enzyme, signal peptidase II (SPase II)" [PMID:1894646].
- Its specific chemistry is cleavage of the signal peptide from
  diacylglyceryl-modified prolipoproteins. Tokunaga et al. characterized
  "Prolipoprotein signal peptidase, a unique endopeptidase which recognizes
  glycyl glyceride cysteine as a cleavage site" and localized the activity to
  the inner cytoplasmic membrane [PMID:6368552].
- GO currently represents the molecular function with `GO:0004190
  aspartic-type endopeptidase activity`. That is accurate but broad; a
  dedicated `lipoprotein signal peptidase activity` child term would capture
  the signal peptidase II substrate and cleavage context.
