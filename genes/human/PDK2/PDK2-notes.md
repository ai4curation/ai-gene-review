## Manual review notes

Deep research via `just deep-research-falcon human PDK2 --fallback perplexity-lite`
could not run in this environment: the deep-research client exposed only the
`claude_code` provider, while both `falcon` and the configured Perplexity fallback
failed. I reviewed the seeded GOA rows manually from the UniProt record, the
PANTHER/PAINT cache for PTHR11947, and the cached primary publications.

- Core function: PDK2 is a broadly expressed mitochondrial matrix kinase that
  phosphorylates the E1 alpha subunit of the pyruvate dehydrogenase complex.
  PMID:7499431 identifies PDK2 as one of the human PDK isoenzymes, and
  PMID:16401071/PMID:19833728 place ATP, ADP, dichloroacetate, and lipoyl-domain
  regulation in its catalytic/regulatory dimer.
- PAINT: there are no IRD/IKR losses on the PDK2 lineage. The PTN000236514 PDK
  activity, mitochondrion, pyruvate-flux, and broad glucose-metabolism IBD rows
  are kept.
- Mouse-projection rows for insulin receptor signaling, gluconeogenesis, pH,
  ketone metabolism, nutrient response, and glucose homeostasis were marked as
  over-annotated at the gene-product level. They are organismal consequences of
  PDK-mediated PDC inhibition, not direct pathway steps executed by PDK2.
- The p53 and cigarette-smoke/ROS rows describe upstream transcriptional or
  cancer-cell contexts that change PDK2 expression and PDH phosphorylation. They
  were not kept as direct apoptotic or ROS-response functions of the kinase.
