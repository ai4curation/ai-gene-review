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

## Result: in class (run 2026-11-14, archaeal rows added 2026-11-16)

| PDB | Protein | Hemes / protomer | Chains | Median NN Fe–Fe | Min | Max |
|---|---|---:|---:|---:|---:|---:|
| 7TFS | OmcE (`Q74FJ0`) | 4 | 1 | **10.4 Å** | 9.7 | 11.6 |
| 6NEF | OmcS (`Q74A86`) | 6 | 1 | **9.3 Å** | 9.3 | 13.0 |
| 6EF8 | OmcS (`Q74A86`), 7-subunit segment | 6 | 7 | **9.1 Å** | 8.8 | 12.5 |
| 7LQ5 | OmcZ (`Q74BG5`) | 8 | 3 | **9.2 Å** | 8.6 | 11.3 |
| 8D9M | OmcZ (`Q74BG5`), independent deposition | 8 | 1 | **9.4 Å** | 8.8 | 11.4 |
| 8E5F | PcECN (`A3MW92`), *P. calidifontis* | 4 | 1 | **10.4 Å** | 9.4 | 12.3 |
| 8E5G | AvECN (`F2KMU8`), *A. veneficus* | 4 | 1 | **9.4 Å** | 9.4 | 9.4 |
| 9YUQ | DsECN (`A0A0M4DKA8`), *D. soudanensis*, 16-chain bundle | 4 | 16 | **8.7 Å** | 7.8 | 11.9 |

Across six proteins carrying four, six and eight hemes, from two domains of life,
with no sequence or fold similarity between them, the median nearest-neighbour Fe–Fe
distance falls in a band about 1.7 Å wide, **8.7–10.4 Å**. The band widened when the
*Desulfuromonas* filament was added: it is the tightest-packed member measured, 0.4 Å
below the previous lower edge, which moves NrfA's 9.7 Å from just inside the band to
near its middle. The two independent OmcZ
depositions, from different groups, agree to 0.2 Å, which is the internal control: the
measurement is reproducible across depositions, so the spread between proteins is not
deposition noise. The two archaeal filaments were added after the bacterial band was
fixed and land inside it (10.4 Å, matching OmcE exactly; 9.4 Å, matching OmcZ), so
they are a genuine out-of-sample confirmation of the published claim.

## Result: out of class — the band is NOT specific (2026-11-16)

The measurement above shows the invariant holds *within* the class. It says nothing
about whether it is *specific* to the class, and the project page previously proposed
the spacing as a precision stage without having checked. Checked now, against two sets
of non-filament multiheme cytochromes. All chains pooled:

| PDB | Protein | Hemes / protomer | Median NN Fe–Fe | Inside the 8.7–10.4 Å band? |
|---|---|---:|---:|---|
| 1GYO | di-tetraheme cytochrome c3, *D. gigas* | 4 | 11.7 Å | no |
| 2BQ4 | type I cytochrome c3, *D. africanus* | 4 | 11.6 Å | no |
| 2E84 | Hmc, 16-heme HMW cytochrome c, *D. vulgaris* | 16 | 11.4 Å | no |
| 1OAH | NrfA nitrite reductase, *D. desulfuricans* | 5 | 9.7 Å | **YES** |
| 2J7A | NrfHA nitrite reductase complex, *D. vulgaris* | 5 | 9.7 Å | **YES** |
| 3L1T | NrfA nitrite reductase, *E. coli* | 5 | 9.7 Å | **YES** |

Two findings, and they point opposite ways.

**The counterexample the literature offers is not one.** PMID:36732469 states that "c3
cytochromes from *Desulfovibrio* species also have similar haem structures (PDB IDs:
1gyo, 2bq4 and 2e84) … All four structures have consecutive histidines causing tight
haem T-junction with similar haem–haem distances. However, none of the c3 cytochromes
is known to form nanowires." At the Fe–Fe level that is not what the coordinates say:
all three sit 1.0–3.0 Å *above* the filament band and separate cleanly from it. The
paper is describing edge-to-edge porphyrin contact and T-stacking geometry, which is a
different measurement, so this is not a contradiction of the paper — but it does mean
the c3 entries cannot be used to argue that spacing is non-specific.

**The nitrite reductases are the real counterexample, and they are decisive.** Three
independent NrfA structures from three organisms give a median of 9.7 Å each — inside
the filament band, between OmcS's 9.3 and OmcE's 10.4, and reproducible to 0.0 Å
across depositions. These are precisely the proteins the sequence screen in
[BASELINE.md](BASELINE.md) produces as false positives. **So nearest-neighbour Fe–Fe
spacing cannot be the precision stage: the hardest false positives already satisfy
it.**

## What does separate them: continuity through the subunit interface

The papers name the actual signature and it is not a distance. Wang et al. describe
haems "coordinated by histidines in adjacent subunits" (PMID:35798889), and
PMID:36732469 distinguishes c3's `CXXCHH` (one proximal, one distal histidine) from
OmcZ's two distal histidines. The geometric consequence is testable: in a wire the
heme chain runs *through* the subunit interface, so the spacing does not change there.
In a globular enzyme the hemes stay inside one protomer.

Measured as the closest inter-chain Fe–Fe divided by the intra-chain spacing, on every
deposition here that contains more than one chain:

| PDB | Protein | closest inter-chain | intra-chain spacing | ratio | chains continuous |
|---|---|---:|---:|---:|---:|
| 6EF8 | **OmcS filament** | 9.1 Å | 9.1 Å | **1.00×** | **7 / 7** |
| 7LQ5 | **OmcZ filament** | 9.3 Å | 9.3 Å | **1.00×** | **3 / 3** |
| 9YUQ | **DsECN filament**, bundled | 8.7 Å | 8.8 Å | **1.00×** | 4 / 16 |
| 2J7A | NrfHA complex | 10.7 Å | 9.7 Å | 1.10× | 0 / 18 |
| 1OAH | NrfA | 11.1 Å | 9.7 Å | 1.15× | 0 / 2 |
| 3L1T | NrfA | 11.7 Å | 9.7 Å | 1.21× | 0 / 4 |
| 1GYO | cytochrome c3 (biological dimer) | 15.2 Å | 11.7 Å | 1.29× | 0 / 2 |
| 2BQ4 | cytochrome c3 (crystal copies) | 24.8 Å | 11.6 Å | 2.14× | 0 / 2 |

All three filaments sit at exactly **1.00×** — the chain simply does not notice the
interface — and every non-filament is at 1.10× or above, with not one chain of any of
them continuous at the 1.05× factor. The strongest control is
`2J7A`, the NrfHA complex, where electrons genuinely do cross a subunit interface
during catalysis: even there the closest inter-subunit Fe–Fe is 10% longer than the
intra-subunit spacing, and no heme's nearest neighbour is in the other subunit. That
is the difference between a relay with a junction and a wire.

**Two statistics, and only one of them is robust.** The ratio is an *existence* claim:
one close pair anywhere in the deposition sets it. The per-chain count says how
pervasive the continuity is, and the two can disagree. `6EF8` is uniform — every one of
seven OmcS subunits has a neighbour at exactly 1.00×, a wire throughout — and `7LQ5` is
3/3. `9YUQ` is not: two chains at 1.00×, two at 1.05×, two more at 1.054× just over the
cutoff, and the remaining ten at 1.29–1.40×. Its per-chain count is therefore
threshold-sensitive, reading 2/16 at a factor of 1.03, 4/16 at 1.05 and 6/16 at 1.07,
and it is reported as indicative only. The architecture explains that rather than
undermining it: this is a *bundled antiparallel* filament, so most of the sixteen
modelled chains are laterally packed at 11.3–12.3 Å rather than in axial contact, and
what the count measures is how much of the bundle the model places in axial register.
The minimum ratio is the statistic that separates, and on it all three filaments reach
1.00× while nothing out of class gets below 1.10×.

**The chain-level contact topology is the clearest view**, and it is what a wire should
look like. Counting pairs of chains whose hemes come within the 1.05× cutoff: `6EF8`
gives six pairs over seven chains, with contacts per chain of 2, 2, 2, 2, 2, 1, 1 — a
single unbranched run with two ends, which is a filament and nothing else. `7LQ5` gives
2, 1, 1 over three chains, the same topology as far as three subunits can show. `2J7A`,
with eighteen chains and a real catalytic interface, gives **zero** pairs.

### A criterion that did not work, recorded so it is not retried

The obvious generalisation — link every pair of hemes within a fixed cutoff and ask
whether they form one connected component spanning the filament — **fails**, and fails
in both directions, so it is not used. At a 14 Å cutoff `6EF8` and `7LQ5` do give a
single component containing every heme, but so does `1OAH`: NrfA's two pentaheme
protomers come within 11.1 Å, so the dimer links into one component of all ten hemes
and reads as wire-like. Meanwhile the genuine `9YUQ` filament splits into three
components, because the bundle's lateral spacings exceed the cutoff. Tightening to 12 Å
fragments everything, filaments included. The result is threshold-dependent and
separates the classes at none of the cutoffs tried (10, 12, 14 Å), which is why the
criterion above is framed as a *ratio to each structure's own intra-chain spacing*
rather than as an absolute distance.

This is what the structural second stage has to measure. It is also harder than the
project page assumed, for a reason that matters: **continuity is a property of the
polymer, not of the subunit.** It cannot be computed from a monomer, and the earlier
finding on this project that AlphaFold DB models are apo monomers without the
inter-subunit signature now has a second edge — the signature is exactly the thing a
monomer prediction cannot carry.

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
- **Seven in-class depositions is still not a survey**, though it is no longer one
  genus: the two archaeal filaments were measured after the bacterial band was fixed
  and fall inside it, which is a real out-of-sample confirmation of the published
  claim.
- **The continuity criterion rests on three filaments.** `6EF8` (OmcS, 7 subunits),
  `7LQ5` (OmcZ, 3 subunits) and `9YUQ` (DsECN, 16 chains) are the multi-subunit
  depositions; `6NEF`, `7TFS`, `8D9M`, `8E5F` and `8E5G` each hold a single chain, so
  continuity cannot be computed for them. `9YUQ` was added after the 1.05× threshold was
  set and did not move it, which is the only out-of-sample test the criterion has had.
  The margin is still modest — 1.00× against 1.10× for the nearest control — and three
  filaments against five non-filaments is a small test set. A filament of a fourth
  family, and a non-filament multiheme polymer if one exists, are what would stress it.
- **Not every inter-chain contact means the same thing.** For the filaments and for
  `2J7A`/`1OAH`/`3L1T`/`1GYO` the chains are biological; for `2BQ4` they are two
  crystallographic copies, so its 2.14× is partly a packing accident and is reported
  rather than relied on. The within-chain column is printed alongside the pooled one
  for exactly this reason, and for every structure here the two medians agree, so no
  conclusion turns on the choice.

## Why it matters for classification

The invariant is a cofactor geometry. A sequence HMM reads the backbone and a
structural search such as Foldseek matches the fold, and both of those are the things
the papers say are *not* conserved here. So neither tool can see the feature that
defines the class, which is consistent with what the resources actually do: PANTHER
misplaces OmcS, misplaces OmcE and has no family for OmcZ (see the parent project
page). Any automated route to this class has to key on where the hemes sit.

**But not on how far apart they are.** That was the project's working proposal and the
out-of-class measurement refutes it: NrfA, the sequence screen's own hardest false
positive, has a 9.7 Å median in three independent structures, inside the filament
band. A spacing filter would keep every nitrite reductase the sequence stage keeps,
which is to say it would add nothing where it is needed.

What survives is narrower and more demanding. The discriminating feature is that the
heme chain is **continuous through the subunit interface** — spacing unchanged across
it, and a measurable fraction of hemes whose nearest neighbour is in the neighbouring
subunit. That is a property of the assembled polymer. The practical consequence for
this project is that the structural stage cannot be a monomer-structure lookup: it
needs the filament, either from a deposition or from a polymer prediction, and
AlphaFold DB supplies neither. Until that is solved the honest position is that the
sequence screen is a candidate generator with no automated second stage, and the
second stage remains the cryo-EM work the papers did by hand.
