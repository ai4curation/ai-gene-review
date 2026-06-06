# Tier-2 re-review + the machinery discriminator

The Tier-2 queue (a core `ACCEPT` call on a hub-aligned BP/CC term) is large
(291). To make it actionable, `flag_candidates.py` now (1) ranks it by each
readout class's empirical any-downgrade rate from our own aligned crosstab, and
(2) adds a **machinery discriminator** developed during this re-review.

## What the VIABILITY queue taught us

The highest-priority class is `VIABILITY_PROLIFERATION` (74% of aligned
annotations get downgraded). Re-reviewing its 18 candidates against each gene's
own molecular function:

**Machinery — correctly core, KEEP** (the gene's MF acts directly on the cycle):

| gene | proliferation term | core MF |
|---|---|---|
| CDK1 | G2/M transition | cyclin-dependent kinase |
| CDKN1C | neg. reg. epithelial cell prolif. | CDK inhibitor |
| MYC, Sox2 | G1/S transition; stem-cell maintenance | proliferation-driving TF |
| RB1, TP53/Trp53 | G1/S, G2/M checkpoint | cell-cycle checkpoint |
| Mtor | positive regulation of cell growth | growth-signaling kinase |
| AM1 | meiotic cell cycle | maize meiosis regulator |
| cdc15 | cell division site | mitotic-exit-network |

**Indirect — proliferation is downstream of signaling, NON-CORE candidate**
(the gene's MF is a *secreted signaling ligand*):

| gene | term | core MF |
|---|---|---|
| IL21 | positive regulation of T cell proliferation | cytokine activity |
| PDGFB | positive regulation of glomerular mesangial cell prolif. | growth factor activity |
| VEGFA | positive regulation of endothelial cell prolif. | growth factor activity |
| Sirt2 | positive regulation of cell division | NAD⁺-dependent deacetylase |

The flag alone could not separate these — CDK1 and PDGFB look identical (both
`ACCEPT` BP proliferation aligned to a viability readout). **The discriminator
is the gene's own MF**: a signaling-ligand MF means any cellular process it
drives is downstream of receptor signaling, hence non-core.

## The discriminator, generalized

`flag_candidates.py` now tags a Tier-2 candidate `indirect_ligand` when the gene
has an `ACCEPT`ed signaling-ligand MF (`cytokine / growth factor / hormone /
chemokine / chemoattractant activity`). These float to the top of the queue as
the strongest non-core candidates. Current run surfaces **6**:

| gene | term | readout |
|---|---|---|
| IL21 | positive regulation of T cell proliferation | VIABILITY |
| PDGFB | positive regulation of glomerular mesangial cell proliferation | VIABILITY |
| VEGFA | positive regulation of endothelial cell proliferation | VIABILITY |
| VEGFA | negative regulation of apoptotic process | APOPTOSIS |
| HMGB1 | positive regulation of cytosolic calcium ion concentration | CALCIUM |
| HMGB1 | positive regulation of transcription by RNA pol II | TRANSCRIPTIONAL |

These match the pattern exactly: VEGFA's anti-apoptotic and pro-proliferative
annotations, IL21's pro-proliferative annotation, and extracellular HMGB1's
calcium/transcription effects are all *downstream of secreted-ligand signaling*,
not core molecular functions.

## Recommendation & scope

- The 6 `indirect_ligand` candidates are reasonable `KEEP_AS_NON_CORE`
  proposals. They are **not edited here**: each is defensible (e.g. a curator
  could argue endothelial proliferation is central to VEGFA), and unilaterally
  rewriting curated `ACCEPT`s exceeds what this analysis should decide alone.
  They are handed to curators as a ranked worklist (`flagged_candidates.tsv`).
- The machinery rows (CDK1, MYC, RB1, …) are confirmed correctly core and
  should be left as-is — important evidence that the Tier-2 flag is *low
  precision without the discriminator*.

## Net effect on tooling

- `flag_candidates.py`: `--target {accepted,unreviewed,all}`; Tier-2 ranked by
  class downgrade rate; `indirect_ligand` discriminator column; clean `\n`-
  terminated TSVs (the miners too).
- Honest limitation: the discriminator only catches the *signaling-ligand* class
  of indirect genes. Other indirect cases (e.g. a transporter whose perturbation
  shifts a hub readout) still need human judgement; the ranked queue is the tool
  for that, not an automated verdict.
