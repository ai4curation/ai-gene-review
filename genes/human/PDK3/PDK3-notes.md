## Manual review notes

Deep research via `just deep-research-falcon human PDK3 --fallback perplexity-lite`
could not run in this environment: the deep-research client exposed only the
`claude_code` provider, while both `falcon` and the configured Perplexity fallback
failed. I reviewed the seeded GOA rows manually from the UniProt record, the
PANTHER/PAINT cache for PTHR11947, and the cached primary publications.

- Core function: PDK3 phosphorylates serine sites on human pyruvate dehydrogenase
  E1 alpha. PMID:11486000 assayed site specificity across all four mammalian PDKs,
  while PMID:15861126 solved PDK3 bound to the inner lipoyl domain of the human
  PDC core and explains L2-dependent stimulation of the enzyme.
- PAINT: there are no IRD/IKR losses on the PDK3 lineage. The PTN000236514 rows
  are sound for this isoform.
- PDK3 is a transcriptional output of PPARbeta/delta, HIF1A, and butyrate-linked
  fatty-acid response contexts. Those papers are useful biological context, but
  the mature PDK3 protein does not transduce PPAR or HIF1 signaling; it carries
  out the downstream mitochondrial PDH phosphorylation reaction.
- The melanoma ROS row from PMID:22865452 was kept only as a non-core metabolic
  consequence: PDK3 knockdown pushes the cells toward mitochondrial oxidation and
  raises mitochondrial ROS.
