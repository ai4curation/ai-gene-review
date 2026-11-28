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
- The direct HPA cytosol row is marked as over-annotated because the rest of the
  cached evidence supports a soluble nuclear transcription factor; the HPA and
  Reactome nucleoplasm rows are accepted as consistent with nuclear receptor
  transcriptional complexes.
- The root `cell differentiation` IBA is kept as a broad, non-core NR2A/HNF4
  output, and the InterPro intracellular receptor signaling inference is also
  kept as non-core because the local HNF4G evidence supports an orphan nuclear
  receptor transcription factor with a constitutively fatty-acid-bound ligand
  binding domain.
