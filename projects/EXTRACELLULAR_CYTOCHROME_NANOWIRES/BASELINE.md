# How badly does the cheap sequence filter over-select?

Run `uv run python filament_baseline.py` in this folder to reproduce. The proteome
TSV is fetched from UniProt and cached under a git-ignored `.cache/`.

## Why run it

The project page argues that extracellular cytochrome nanowires cannot be found by
sequence, because the class is defined by heme geometry, and proposes a structural
route. Before building anything structural, the cheap alternative has to be
eliminated: a pure-sequence filter for **at least four covalent heme motifs, a signal
peptide, and no transmembrane segment** catches all three characterised filament
subunits. If that filter is specific enough on its own, the structural work is
unnecessary. If it is hopeless, the structural work has to carry everything. Either
way the number settles it, and it needs no structures.

## Result (run 2026-11-15, *G. sulfurreducens* PCA, UP000000577, 3,402 proteins)

| Filter stage | ≥4 motifs | 4–8 motifs |
|---|---:|---:|
| heme motifs in range | 63 | 35 |
| … and a signal peptide | 55 | 28 |
| … and no TM segment | **52** | **26** |

**Recall is perfect in both.** OmcS, OmcE, OmcZ and OmcT all pass. The inner-membrane
multiheme cytochromes that must not be caught — ImcH, CbcL, GSU2359 — are all excluded,
by the transmembrane clause.

**Precision is not.** 52 candidates against three characterised filament subunits is
17-fold over-selection. The upper bound helps, and it is not arbitrary: the known
subunits carry 4, 6, 6 and 8 motifs, while the false positives run to 34, 27 and 26
— they are the large outer-membrane polyheme cytochromes (OmcB, OmcC, OmcA-family) and
lipoprotein cytochromes. Capping at 8 motifs halves the set to 26 while keeping 4/4
recall.

Of those 26, four are members of CDD `cd21555`, the hand-curated OmcS-like model
(OmcS, OmcT, OmcJ and GSU2501), so they are plausible rather than clear errors. The
remainder are not: the set still contains three nitrite reductases, including NrfA,
which is a well-characterised pentaheme enzyme and emphatically not a filament subunit.

### A second proteome

*S. oneidensis* MR-1 (UP000008186, 4,068 proteins), which has no known cytochrome
filaments, yields 10 candidates under the same 4–8 filter. That the filter returns a
non-empty set from an organism with no known members is the expected behaviour of a
recall-oriented screen, and is a reminder that a hit is a question, not an answer.

## What this settles

The filter is a **good candidate generator and not a classifier**. It cuts 3,402
proteins to 26, a 130-fold reduction, with no loss of the known subunits — which is
exactly what a first-stage screen should do. It cannot do the second stage: it keeps
nitrite reductases, and nothing in the sequence distinguishes them from a filament
subunit, because what distinguishes them is where the hemes end up.

So the structural half is worth building, and the experiment that could have made it
unnecessary did not. The sensible shape is this filter for recall, then heme geometry
for precision, as the project page proposes.

## Refining it: two more rules, validated on held-out organisms (2026-11-15)

Run with `--refine`. The 26 survivors above were inspected for features the four
characterised subunits share and the rest do not, which gave two rules:

1. **Not a lipoprotein** (`--refine`). A lipid-anchored protein is tethered to a
   membrane; a filament subunit is a free polymer. None of OmcS, OmcE, OmcZ or OmcT
   carries a lipid anchor. This is mechanistically motivated rather than fitted.
2. **No named InterPro family.** The characterised subunits carry only homologous
   superfamilies (`IPR036280` multiheme cytochrome) and structural domains (Ig-like,
   IPT, doubled CXXCH), plus `IPR051174`, which is only the mirror of PANTHER
   `PTHR30333` — the family this project's own review records as heterogeneous, so it
   is excluded from the rule. A protein that *does* carry a family-level entry has
   already been classified as something else: Cytochrome c552, Octaheme c-type
   cytochrome, Cytochrome c550/c551-like.

The obvious risk is fitting two rules to four positives, so they were tested on two
Geobacteraceae not used to derive them, each with known OmcS-family members from CDD
`cd21555`:

| Proteome | proteins | base 4–8 | not lipo | no named family | known members kept |
|---|---:|---:|---:|---:|---|
| *G. sulfurreducens* (tuned on) | 3,402 | 26 | 20 | **17** | 4 / 4 |
| *C. bemidjiense* (held out) | 4,042 | 24 | 17 | **12** | 4 / 5 |
| *G. daltonii* (held out) | 3,798 | 19 | 18 | **14** | 2 / 2 |

**The refinements cost no recall.** Precision improves by about a third, and every
known member that entered the refinement came out of it. The single miss, *C.
bemidjiense* `B5EHF0` (omcS-3), is lost by the **base** filter, not by either new
rule: its UniProt entry has no signal-peptide annotation at all, and running without
`--refine` loses it too. Its InterPro profile (`IPR051174`, `IPR036280`) is exactly
the positive profile.

So the signal-peptide clause is now the known weak point. It is doing real work —
it is part of what excludes the inner-membrane cytochromes — but it depends on an
annotation that is missing for at least one genuine member, and a secreted protein
whose signal peptide was never annotated is invisible to this screen.

## Honest limits

- **"Known filament subunit" is a set of three.** Precision measured against three
  positives is a weak estimate; the true positive set in this organism is unknown and
  is plausibly larger than three, which is the point of the cd21555 overlap above.
- **Motif counting is approximate.** `CXXCH`, `CXXXCH` and long-linker variants are
  counted greedily and non-overlapping; a motif that is present but not used for heme
  attachment still counts, and an unusual attachment chemistry would be missed.
- **Signal-peptide and TM calls are UniProt's**, largely from SignalP and Phobius for
  unreviewed entries, so the filter inherits their error rates.
- **One organism, one genus.** The *S. oneidensis* run is a sanity check, not a second
  measurement; the filter has not been tested on the archaeal members at all.
