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
  over-annotated for the parasite ortholog: the direct evidence for BMA-BEN-1 is
  the conserved beta-tubulin sequence, not a Brugia sensory or egg-laying
  circuit assay.
- PubMed search for Brugia/filarial beta-tubulin and benzimidazoles found
  in vivo and in vitro Brugia flubendazole/oxfendazole efficacy papers and one
  B. malayi beta-tubulin docking paper, but no primary experiment assigning
  this exact B. malayi isotype as the sensitive benzimidazole target. I kept
  the direct core function to the conserved beta-tubulin structural role and
  recorded the Brugia benzimidazole-isotype assignment as a residual knowledge
  gap.
