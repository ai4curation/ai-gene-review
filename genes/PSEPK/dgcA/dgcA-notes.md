# dgcA curation notes

- Q88R24 is the soluble flavoprotein component of the Pseudomonas DgcAB system. The `OxRdtase_FMN_N` fold name alone does not establish FMN binding.
- The characterized DgcA-like Q1QYW1 enzyme carries noncovalently bound FAD [PMID:32631860, "a monomer of 79 kDa with a noncovalently bound flavin adenine dinucleotide"].
- Pseudomonas genetics and isotope tracing support DgcAB-dependent conversion of dimethylglycine to sarcosine. [PMID:17951379, "conversion of DMG to sarcosine."]
- UniProt's `EC 1.5.8.-` assignment implies a flavin acceptor, while the
  pathway model uses the more specific ferredoxin-linked `EC 1.5.7.3` reaction
  and places DgcB before ETF. GO:0047865 is retained as the best available
  substrate-specific term, with a new ferredoxin-linked child term proposed to
  capture the acceptor distinction.
