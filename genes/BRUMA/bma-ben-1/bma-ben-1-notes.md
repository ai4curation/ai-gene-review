# bma-ben-1 notes

## 2026-11-22

- Started the first parasite review in the beta-tubulin/benzimidazole lane with
  `BRUMA/bma-ben-1`, UniProt `A0A1U7F2B2`. The current UniProt record names the
  gene `bma-ben-1`, maps it to WormBase `Bm4733` / `WBGene00224994`, and lists
  the expected beta-tubulin InterPro signatures.
- `bma-ben-1` has nine GOA rows. Seven are automated beta-tubulin rows for
  GTPase activity, GTP binding, structural constituent of cytoskeleton,
  microtubule, cytoskeleton, microtubule-based process and microtubule
  cytoskeleton organization. These mirror the accepted or too-general calls in
  the merged `worm/ben-1` review and are supported by the local UniProt domain
  architecture plus the complete PTHR11588 family review.
- The two EnsemblMetazoa behavior rows, chemosensory behavior and egg-laying
  behavior, are transferred from the C. elegans `ben-1` product. I marked both
  over-annotated for this parasite beta-tubulin: the direct evidence for
  BMA-BEN-1 is the conserved beta-tubulin sequence, not a Brugia sensory or
  egg-laying circuit assay.
- PubMed searches for Brugia or filarial beta-tubulin papers in the
  flubendazole/oxfendazole/benzimidazole literature found efficacy papers
  reporting activity against Brugia or filarial systems (PMID:42545617,
  PMID:38362501, PMID:37440891, PMID:30650084, PMID:27733308, PMID:27145083),
  plus papers on Litomosoides oxfendazole activity or B. malayi beta-tubulin
  docking (PMID:42013151, PMID:41244930). None of these search hits was a
  primary Brugia loss-of-function, allele-swap or resistance-mapping experiment
  assigning the Bm4733 beta-tubulin isotype as the sensitive benzimidazole
  target, so I kept the direct core function to the conserved beta-tubulin
  structural role and recorded the Brugia benzimidazole-isotype assignment as a
  residual knowledge gap.
