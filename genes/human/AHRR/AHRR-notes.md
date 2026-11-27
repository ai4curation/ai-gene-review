# AHRR notes

## 2026-11-26

- Seed/family: AHRR is UniProtKB:A9YTQ3, HGNC:AHRR, in PANTHER `PTHR10649:SF3`.
  The two human reviewed family members are AHRR and the already reviewed AHR
  (`P35869`, `PTHR10649:SF9`).
- Deep research: `just deep-research-falcon human AHRR --fallback
  perplexity-lite` could not run in this environment because the configured
  `deep-research-client` provider list only exposed `claude_code`. The review
  was therefore based on the Swiss-Prot record, GOA, Reactome caches, PAINT, and
  cached PMIDs from the AHRR UniProt record.
- Core function: human AHRRdelta8 is the active predominant human repressor
  isoform. It represses AHR-dependent transactivation, binds ARNT, and binds
  xenobiotic response elements at target promoters including CYP1A1
  [PMID:19380484; PMID:17890447]. The shorter AHRR715 isoform is much less
  active and does not form a comparable ARNT complex.
- Localization: AHRR is a nucleocytoplasmic shuttle with both an NLS and NES.
  Its NLS is dominant, so it is predominantly nuclear, but ARNT can carry the
  NLS-deletion mutant into the nucleus and thereby supports a cytoplasmic
  AHRR:ARNT assembly pool [PMID:17980155].
- PAINT: `PTN004180845` is sound for the shared bHLH-PAS transcriptional
  regulator terms: `GO:0005634`, `GO:0000976`, and `GO:0006357`. The same root
  node over-propagates `GO:0004879` nuclear receptor activity and `GO:0034751`
  aryl hydrocarbon receptor complex to the AHRR branch. AHR contains a PAS-B
  ligand-binding domain, whereas AHRR lacks it; AHRR forms a distinct AHRR:ARNT
  repressor complex instead of an AHR-containing receptor complex. The PANTHER
  tree cache identifies `PANTHER:PTN002579384` as the smallest AHRR/SF3 node
  below `PTN004180845`, so both rows should gain an IRD at
  `PANTHER:PTN002579384`.
- Existing IRDs: `PANTHER:PTN008502945` is in the fish AHR-like SF9 branch,
  below the AHR SF9 clade and not on the human AHRR lineage, so it does not
  prune the AHRR IBA rows.
- GO-CAM/module decision: `gocams/index.tsv` contains human AHR in production
  model `62f58d8800001680`, but no AHRR activity. The existing efferocytosis
  anti-inflammatory module also uses AHR SF9 only. AHRR is a feedback regulator
  of the broader AHR/ARNT/CYP/TIPARP transcriptional pathway; an AHR/AHRR-only
  module would omit ARNT and the target-gene context, so this PR adds no module
  or GO-CAM review.
