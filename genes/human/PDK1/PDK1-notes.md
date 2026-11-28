## Manual review notes

Deep research via `just deep-research-falcon human PDK1 --fallback perplexity-lite`
could not run in this environment: the deep-research client exposed only the
`claude_code` provider, while both `falcon` and the configured Perplexity fallback
failed. I reviewed the seeded GOA rows manually from the UniProt record, the
PANTHER/PAINT cache for PTHR11947, and the cached primary publications.

- Core function: PDK1 is a mitochondrial matrix protein serine kinase that
  phosphorylates PDHA1 in the pyruvate dehydrogenase complex, inhibiting
  oxidative decarboxylation of pyruvate to acetyl-CoA. PMID:22195962 states that
  PDHK1 negatively regulates PDHA1 by phosphorylating it; PMID:17683942 provides
  structural support for human PDK1 as a PDK isoform.
- PAINT: there are no IRD/IKR losses on the PDK1 lineage. The PTN000236514 IBD
  rows for PDK activity, mitochondrion, regulation of pyruvate decarboxylation to
  acetyl-CoA, and regulation of glucose metabolism are consistent with human
  PDK1.
- Rows citing PMID:9427642 and PMID:9637919 are PDPK1/3-phosphoinositide-
  dependent protein kinase 1 alias collisions, not rows about Q15118. PMID:17110931
  is the same alias collision through IntAct. PMID:21763680 experimentally studies
  PDK3 control by HIF1A and cites PDK1 only as background.
- All bare GO:0005515 rows were removed under the current generic protein-binding
  policy. The PGK1-PDHK1 physical interaction in PMID:26942675 remains represented
  by the accepted PDK activity and regulation rows.
