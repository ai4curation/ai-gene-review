# HNF4G (Q14541) review notes

Deep research was not attempted after the same `claude_code: success Not
logged in` provider failure seen for the preceding HNF1B review. This compact
review is grounded in UniProt, the sibling HNF4A review, PTHR24083 PAINT, and
the three HNF4G GOA-cited publications.

- `just paint-losses human HNF4G` reported no IRD or IKR loss on the human
  lineage.
- PTHR24083 is broad: HNF4G sits in the HNF4/NR2A clade below
  `PTN000638895`, while the HNF4A/HNF4G positive regulation assertion is at
  `PTN000639196`.
- The direct HNF4G molecular evidence supports sequence-specific cis-regulatory
  DNA binding and transcriptional activation: HNF4G recognizes the DD4/AKR1C4
  regulatory regions in HepG2 cells [PMID:12220531], and activates a HAS2
  promoter/enhancer reporter in bladder cancer cells [PMID:23896584].
- Cytosol and nucleoplasm rows were left undecided because the local cache does
  not expose the HPA or Reactome evidence needed to verify those granular
  locations. HNF4G is kept at the directly supported nucleus term.
- The root `cell differentiation` IBA was left undecided because it needs
  family-level source-node review; the InterPro intracellular receptor signaling
  inference was marked as over-annotated because the local HNF4G evidence
  supports an orphan nuclear receptor transcription factor, not a ligand-driven
  receptor-signaling pathway.
