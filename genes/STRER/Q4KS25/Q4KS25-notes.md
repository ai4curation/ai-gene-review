# Q4KS25 notes

## 2026-11-23

- Started the Strongyloides stercoralis beta-tubulin review after live UniProt
  searches for Strongyloides PTHR11588 members identified `Q4KS25_STRER` as a
  447 aa beta-tubulin with the UniProt species code `STRER`, gene name `btub`,
  EMBL record `AY898942` / `AAY16350.1` and conserved Tubulin/FtsZ GTPase and
  C-terminal tubulin domains.
- `just deep-research-falcon STRER Q4KS25 --fallback perplexity-lite` could not
  produce a deep-research file because this checkout only had `claude_code`
  configured as a deep-research provider; I kept manual notes rather than
  creating a provider-named file by hand.
- `just fetch-gene-pmids STRER Q4KS25` found no PMID references in the seeded
  GOA rows, because all seven rows are electronic mappings to GO_REF records.
  The Q4KS25 UniProt `RN` block cites Melville et al. 2006, so I fetched
  `PMID:16309677` directly.
- `just paint-losses STRER Q4KS25` reported that Q4KS25 is in PANTHER
  `PTHR11588` but not as a leaf of the cached PAINT tree, and found no IRD or
  IKR loss on the gene lineage.
- The Q4KS25 GOA rows are all automated beta-tubulin rows: GTPase activity,
  GTP binding, structural constituent of cytoskeleton, microtubule,
  cytoskeleton, microtubule-based process and microtubule cytoskeleton
  organization. I accepted the core beta-tubulin structural and
  nucleotide-cycle rows, kept microtubule cytoskeleton organization as the
  specific process, and marked the broader cytoskeleton and
  microtubule-based-process rows as too general once microtubule and
  microtubule cytoskeleton organization were asserted.
- The cached Melville et al. paper is abstract-only. The abstract states that
  the authors cloned and sequenced the beta-tubulin genes from S. stercoralis
  and S. ratti, then developed a single-worm beta-tubulin genotyping protocol
  for polymorphisms at codons 167, 198 and 200
  [PMID:16309677 The beta-tubulin genes of two Strongyloides species., "Our
  genotyping test allows the identification of polymorphisms at codons 167,
  198, and 200 in the Strongyloides beta-tubulin gene, thus enabling survey for
  BZ resistant genotypes."]. The abstract connects Q4KS25 to Strongyloides
  benzimidazole-resistance marker surveillance, but it does not assay Q4KS25
  protein for GTPase activity, microtubule polymerization or benzimidazole
  binding.
