# Curation Notes: Escherichia phage Mu `I` (`Q01267`, Protease I / Scaffold protein Z, Mup32/Mup33)

## Summary of Function
- **Product**: Bifunctional nested gene `I`/`Z` (`Mup32`/`Mup33`) encoding two in-frame protein products via alternative translational initiation (`file:BPMU/I/I-uniprot.txt`):
  1. **Protease I (`gp32` / `gpI`, `Q01267-1`, 361 aa, 38.9 kDa)**: Contains an N-terminal MEROPS peptidase U35 family prohead protease domain (`residues 1-178`, `IPR061919` / `PF10123`) fused in-frame to the C-terminal scaffolding domain. Interacts with portal protein H (`gp29`) to form an early 25S initiator complex (`GO:0019069`) and cleaves the C-terminus of portal protein H (`GO:0008233`, `GO:0019082`) to yield mature procapsids competent for DNA packaging (`GO:0046797`).
  2. **Scaffold protein Z (`gp33` / `gpZ`, `Q01267-2`, 183 aa, `residues 179-361`)**: Initiated from internal `Met179` (confirmed by direct N-terminal protein sequencing of `residues 242-249` in Morgan et al. 2002, `PubMed:11922669`); forms the internal procapsid scaffold (`GO:0046806`) that co-assembles with major capsid protein T (`gp34`) into the immature prohead (`GO:0019069`).

## Annotation Review Decisions
- **ACCEPT**:
  - `GO:0008233` (`peptidase activity`, IEA): Core protease activity of the MEROPS U35 peptidase domain (note: MEROPS family U35 is a prohead protease family of unassigned catalytic type in UniProtKB, so `GO:0008233` is exact).
  - `GO:0030430` (`host cell cytoplasm`, IEA): Site of prohead assembly and maturation.
  - `GO:0046797` (`viral procapsid maturation`, IEA): Core biological process of Protease I.
- **MODIFY**:
  - `GO:0006508` (`proteolysis`, IEA) -> `GO:0019082` (`viral protein processing`): Refines broad proteolysis to specific viral protein processing of the portal vertex.
- **TOO_GENERAL**:
  - `GO:0016787` (`hydrolase activity`, IEA): Entailed by `GO:0008233` (`peptidase activity`).
- **NEW**:
  - `GO:0019082` (`viral protein processing`, `involved_in`), `GO:0019069` (`viral capsid assembly`, `involved_in`), `GO:0046806` (`viral scaffold`, `located_in`).
