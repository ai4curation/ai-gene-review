# Heme-chain geometry across cytochrome filament structures

Run `uv run python heme_geometry.py` in this folder to reproduce. Structures are
fetched from RCSB and cached under a git-ignored `.cache/`.

## Why

Two papers state, in prose, that this class of filaments is held together by a
conserved heme arrangement rather than by sequence or fold similarity:

- Wang et al. on OmcE and OmcS: "Although OmcE and OmcS subunits have no overall
  sequence or structural similarities, upon polymerization both form filaments that
  share a conserved haem packing arrangement in which haems are coordinated by
  histidines in adjacent subunits" (PMID:35798889).
- Baquero et al. across domains: "The ECN protein subunits lack similarities in
  their folds; however, they share a common heme arrangement" (PMID:37290436).

That is a geometric claim about deposited coordinates, so it can be measured rather
than quoted. It matters for this project because it decides what an automated
classifier would have to key on.

## Result (run 2026-11-14)

| PDB | Protein | Hemes / protomer | Chains | Median NN Fe–Fe | Min | Max |
|---|---|---:|---:|---:|---:|---:|
| 7TFS | OmcE (`Q74FJ0`) | 4 | 1 | **10.4 Å** | 9.7 | 11.6 |
| 6NEF | OmcS (`Q74A86`) | 6 | 1 | **9.3 Å** | 9.3 | 13.0 |
| 7LQ5 | OmcZ (`Q74BG5`) | 8 | 3 | **9.2 Å** | 8.6 | 11.3 |
| 8D9M | OmcZ (`Q74BG5`), independent deposition | 8 | 1 | **9.4 Å** | 8.8 | 11.4 |

Across three proteins carrying four, six and eight hemes, with no sequence or fold
similarity between them, the median nearest-neighbour Fe–Fe distance falls in a band
about 1.2 Å wide. The two independent OmcZ depositions, from different groups, agree
to 0.2 Å, which is the internal control: the measurement is reproducible across
depositions, so the spread between proteins is not deposition noise.

## What this does and does not show

- **Fe–Fe is a proxy.** The papers quote edge-to-edge porphyrin distances, which are
  smaller (OmcS hemes pack within ~3.5–6 Å edge to edge). Fe–Fe is used here because
  it needs no ring geometry and is unambiguous. The two are not interchangeable; only
  compare Fe–Fe values with other Fe–Fe values.
- **The maxima are chain ends and branches**, not packing failures. OmcS's 13.0 Å is
  its branched, solvent-exposed heme; a terminal heme in a single-protomer extraction
  has a neighbour on one side only.
- **7LQ5 includes inter-subunit neighbours** because the deposition has three chains,
  which is why its spread is the tightest. That is the physiologically relevant case
  for a polymer, and the single-chain rows understate how regular the real filament is.
- **Four structures is not a survey.** This is consistent with the published claim,
  not an independent test of it across the class. The archaeal ECN structures
  (PMID:37290436) would be the obvious extension.

## Why it matters for classification

The invariant is a cofactor geometry. A sequence HMM reads the backbone and a
structural search such as Foldseek matches the fold, and both of those are the things
the papers say are *not* conserved here. So neither tool can see the feature that
defines the class, which is consistent with what the resources actually do: PANTHER
misplaces OmcS, misplaces OmcE and has no family for OmcZ (see the parent project
page). Any automated route to this class has to key on where the hemes sit.
