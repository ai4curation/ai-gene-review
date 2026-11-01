# mak-2 re-review notes

## 2026-11-01 PTHR24055 fungal PR-MAPK review

- `mak-2` encodes the Neurospora terminal ERK-type MAP kinase of the
  `NRC-1` -> `MEK-2` -> `MAK-2` cascade. PMID:15075265 showed that MAK-2
  contains the conserved MAPK TEY activation motif, that `mak-2` mutants fail
  vegetative hyphal fusion and are female sterile, and that MAK-2
  phosphorylation during early colony development depends on the upstream
  MAPKKK NRC-1.
- PMID:19884508 provided the key direct functional/localization experiment:
  functional MAK-2-GFP is cytoplasmic/nuclear in isolated germlings and
  oscillates to cortical complexes at interacting conidial anastomosis tube
  tips, while an analog-sensitive MAK-2 variant showed that MAK-2 kinase
  activity is required for chemotropic interactions and for the alternating
  MAK-2/SO oscillation.
- PMID:23028357 and PMID:25412208 establish MAK-2 as part of a scaffolded
  PR-like MAPK module. HYM1 helps organize NRC-1, MEK-2, and MAK-2, while
  HAM-5 scaffolds the MAK-2 MAPK complex and is needed to localize MEK-2 and
  MAK-2 to oscillatory puncta during germling and hyphal fusion.
- The `PANTHER:PTN000622075` IBDs are broad PTHR24055 MAPK-family transfers
  for Ser/Thr kinase chemistry and active nucleus/cytoplasm compartments. They
  are safe for MAK-2; the catalytic parent is simply less informative than the
  exact imported `GO:0004707 MAP kinase activity` row.
- The `PANTHER:PTN001172087` IBD is seeded by S. cerevisiae Fus3 and S. pombe
  Spk1, and it does identify the inherited fungal Fus3/Spk1-type MAPK clade.
  `GO:0071507 pheromone response MAPK cascade` is scoped too narrowly for
  Neurospora MAK-2, however: the direct Neurospora evidence supports a
  homologous NRC-1/MEK-2/MAK-2 MAPK cascade for self-signaling, chemotropic
  germling/hyphal fusion, and sexual development, not a pheromone-GPCR
  conjugation cascade. I changed that row to `MODIFY` with `GO:0000165 MAPK
  cascade` as the replacement.
- I searched for 2024-2026 Neurospora `mak-2` papers. PMID:34899653,
  PMID:39283084, and PMID:41915693 extend MAK-2/PR-MAPK biology into
  protoperithecium development, VE-1-dependent sexual development, and the
  SO/EOP-1 pre-fusion oscillator. They reinforce the same core pathway rather
  than changing any of the 12 seeded GOA row decisions.
- `just deep-research-falcon NEUCR mak-2` failed in this environment because
  `agentapi` was not found in `PATH` and the Falcon provider was unavailable.
  I therefore used this manual notes file and `mak-2-deep-research-manual.md`
  rather than creating a provider-named deep-research file.
