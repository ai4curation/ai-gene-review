# PPP1R13B notes

- Manual research substituted for automated deep research because no configured
  deep-research provider keys were available in this child checkout.
- Core function: ASPP1 binds p53-family transcription factors and stimulates
  apoptosis-selective transcription of pro-apoptotic target genes
  [PMID:11684014; PMID:14729977].
- The 76 `GO:0005515 protein binding` rows stay as 76 distinct entries, one per
  GOA row and WITH/FROM interactor. They are removed only because GO:0005515 is
  an uninformative bare binding term.
- `GO:0045786 negative regulation of cell cycle`, `GO:0048471 perinuclear
  region of cytoplasm` and `GO:0005912 adherens junction` look like
  over-propagation from ASPP2 or invertebrate ASPP biology. I did not find a
  direct PPP1R13B paper supporting these as ASPP1 locations or processes.
- `GO:0008157 protein phosphatase 1 binding` is proposed for the direct PP1CA
  row from PMID:21998301 because it is the informative molecular-function
  replacement for bare `GO:0005515 protein binding`. This should not be
  broadened to protein phosphatase 1 regulator activity without evidence that
  full-length ASPP1 acts as a PP1 regulatory subunit in vivo; UniProt explicitly
  notes that the PPP1R13B name reflects similarity to a PP1-binding protein.
