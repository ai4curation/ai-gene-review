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

Those were the opening conditions. Both the heme floor and the signal-peptide clause
were later **measured to be wrong** and have been changed — the sections below are in
the order the measurements happened, so the recommended setting is the one at the end
(`--min-hemes 3 --max-hemes 8 --refine --no-require-signal`), not the one named here.

## Result (run 2026-11-15, *G. sulfurreducens* PCA, UP000000577, 3,402 proteins)

| Filter stage | ≥4 motifs | 4–8 motifs |
|---|---:|---:|
| heme motifs in range | 63 | 36 |
| … and a signal peptide | 55 | 29 |
| … and no TM segment | **52** | **27** |

**Recall is perfect in both.** OmcS, OmcE, OmcZ and OmcT all pass. The inner-membrane
multiheme cytochromes that must not be caught — ImcH (`Q747K6`) and CbcL (`Q74GH2`) —
are both excluded by the transmembrane clause, and the periplasmic nitrite reductase
NrfA (`Q747W1`) is not: it has four motifs, a signal peptide and no TM segment, so it
survives this stage and is removed later, by the named-family rule alone.

**Precision is not.** 52 candidates against three characterised filament subunits is
17-fold over-selection. The upper bound helps, and it is not arbitrary: the known
subunits carry 4, 6, 6 and 8 motifs, while the false positives run to 34, 27 and 26
— they are the large outer-membrane polyheme cytochromes (OmcB, OmcC, OmcA-family) and
lipoprotein cytochromes. Capping at 8 motifs nearly halves the set, to 27, while keeping
4/4 recall.

Of those 27, four are members of CDD `cd21555`, the hand-curated OmcS-like model —
but two of those four are OmcS and OmcT, which are known positives rather than uncertain
hits, so the honest figure is **two** plausible extras (OmcJ and GSU2501). The
remainder are not plausible: the set still contains three nitrite reductases, including NrfA,
which is a well-characterised pentaheme enzyme and emphatically not a filament subunit.

### A second proteome

*S. oneidensis* MR-1 (UP000008186, 4,068 proteins), which has no known cytochrome
filaments, yields 10 candidates under the same 4–8 filter. That the filter returns a
non-empty set from an organism with no known members is the expected behaviour of a
recall-oriented screen, and is a reminder that a hit is a question, not an answer.

## What this settles

The filter is a **good candidate generator and not a classifier**. It cuts 3,402
proteins to 27, a 126-fold reduction, with no loss of the known subunits — which is
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
| *G. sulfurreducens* (tuned on) | 3,402 | 27 | 21 | **17** | 4 / 4 |
| *C. bemidjiense* (held out) | 4,042 | 24 | 17 | **12** | 4 / 5 |
| *G. daltonii* (held out) | 3,798 | 19 | 18 | **14** | 2 / 2 |

**The refinements cost no recall.** Precision improves by about a third, and every
known member that entered the refinement came out of it. The single miss, *C.
bemidjiense* `B5EHF0` (omcS-3), is lost by the **base** filter, not by either new
rule: its UniProt entry has no signal-peptide annotation at all, and running without
`--refine` loses it too. Its InterPro profile (`IPR051174`, `IPR036280`) is exactly
the positive profile.

### The signal-peptide clause should be dropped (measured, 2026-11-15)

The obvious reading of that miss was that the screen needs a real signal-peptide
prediction instead of UniProt's annotation, which would mean installing and running
SignalP over every proteome. Measuring first made that unnecessary. Running with
`--no-require-signal`:

| Proteome | signal required | signal dropped | known members kept |
|---|---:|---:|---|
| *G. sulfurreducens* | 17 | 21 | 4/4 → 4/4 |
| *C. bemidjiense* | 12 | 16 | 4/5 → **5/5** |
| *G. daltonii* | 14 | 17 | 2/2 → 2/2 |

Dropping the clause costs about 25% more candidates and buys complete recall: 11/11
known members across the three organisms instead of 10/11, with `B5EHF0` recovered.

**It also excludes none of the known negatives**, which is the part worth recording,
because an earlier draft of this page asserted the opposite. Running the screen with and
without the clause leaves the verdict on every negative identical: ImcH and CbcL are
excluded because each *has a transmembrane segment* (CbcL also carries nine motifs, over
the upper bound), and NrfA is excluded by the named-family rule. None is excluded by the
signal-peptide test. The clause was costing a real positive and contributing nothing
against the negatives it was credited with catching.

Each attribution is checked by removing one clause at a time rather than asserted: NrfA
becomes a false positive as soon as `--refine` is dropped, and CbcL stays excluded even
with no upper bound, which is what pins its exclusion on the TM call.

The default still requires a signal peptide so the funnel above reproduces; use
`--no-require-signal` for the recommended setting.

## The archaeal test (2026-11-16)

Every measurement above is from one bacterial family. Baquero et al. 2023
(PMID:37290436) solved two archaeal ECNs by cryo-EM — PcECN (`A3MW92`) in
*Pyrobaculum calidifontis* and AvECN (`F2KMU8`) in *Archaeoglobus veneficus* — and,
unusually, **named every protein they considered in each proteome and why they rejected
it**. That makes these two the only proteomes with published negative reasoning, and the
sharpest available test of the filter: a different domain of life, no sequence homology to
*Geobacter*, and an independent ground truth.

It falsified one rule, confirmed another, and exposed two bugs in this script.

### First, it validated the motif counter

The paper states the CXXCH count for all four *P. calidifontis* proteins that have more
than two: `A3MW89` 4, `A3MW92` 3, `A3MW94` 8, `A3MW99` 8. Running `heme_motifs()` on
those four sequences reproduces **4, 3, 8, 8 exactly**, and the proteome-wide screen
reproduces the paper's own "only four proteins with more than two motifs" exactly (4 = 4).
That is an independent check on the counter against numbers nobody here chose.

It does not reproduce the second screen: the paper reports 17 *A. veneficus* proteins with
three or more CXXCH motifs, where this script finds 13. The gap is **not** a counting
convention (overlapping and non-overlapping CXXCH both give 13) and **not** UniProt
coverage (only five *A. veneficus* entries sit outside the reference proteome, and none
has a single CXXCH). The authors presumably screened their own gene calls rather than
UniProt's. Unexplained, and recorded as such; it does not affect the outcome, since
`F2KMU8` is found either way.

### A double-counting bug, caught by that validation

The counter initially gave `A3MW92` **4** motifs where the paper gives 3. The extra one is
not a heme: a long-linker match `C...16X...CH` starting at 69 ends on the **same histidine**
as the CXXCH at 85. The overlap check tested only whether a candidate match *started*
inside an already-claimed span, so a long match that ends inside one was accepted, and the
docstring's "non-overlapping" was false.

Fixed to reject any span overlap. The effect on earlier results is bounded and was measured
rather than assumed: **20 of 3,402** *G. sulfurreducens* proteins were mis-counted, **none**
of them crossed the ≥4 threshold, and every known positive and negative kept its count. The
`≥4` funnel (63 / 55 / 52) and every final candidate count in the tables above are
unchanged. One protein inflated 8 → 9 had been wrongly pushed out of the 4–8 window, so
four numbers in those tables moved by one and have been corrected in place: the 4–8 column
now reads 36 / 29 / 27, and the refinement table's *G. sulfurreducens* base column 27.

### A reproducibility bug, caught by a number that would not repeat

The named-family rule calls the InterPro API, and `interpro_type()` caught every exception
and returned `("?", "?")`. That is not a family, so a **transient network failure silently
made the filter more permissive and the candidate count larger** — one run put *G. daltonii*
at 31 where repeated runs give 24. Every number on this page was exposed to that.

Now: lookups are cached to `.cache/interpro_types.json`, retried three times with backoff,
and a lookup that still cannot be resolved **raises** instead of returning a value that
would quietly pass. A measurement that cannot resolve its inputs should stop, not report a
bigger number. The failure path was checked with a control arm — an unmutated run resolves
`IPR003321` (Cytochrome c552) and an unreachable endpoint raises — so the gate is known to
be able to fire. Every number in the table below was produced twice and is identical.

### Two of the three negatives were the wrong proteins

Found by review challenge, not by this screen, and the worst of the three errors because
it was invisible: the accessions registered as CbcL and GSU2359 were neither.

| registered as | accession | what it actually is | CXXCH |
|---|---|---|---:|
| ImcH | `Q747K6` | ImcH (GSU3259), multiheme c-type cytochrome | 6 |
| CbcL | `Q74FN7` | **nicotinamidase-related cysteine hydrolase** (GSU0569) | 0 |
| GSU2359 | `Q74EV9` | **DsbC/DsbG-like disulphide isomerase** (GSU0850) | 0 |

Neither wrong entry is a cytochrome, and neither has a single heme motif, so both were
excluded from the funnel before any clause of the filter applied — which is exactly why
nothing caught it: a negative that is correctly excluded for a nonsense reason looks
identical in the output to one correctly excluded for a real reason. The InterPro family
names quoted for them in an earlier revision of this page (Isochorismatase-like
hydrolase, DsbC/G disulphide bond isomerase) were read correctly off the records; the
records were the wrong proteins. **No claim about CbcL or GSU2359 on this page before
this revision was tested.**

Looking up the real ones changed the negative set substantively:

- **CbcL is `Q74GH2`** (GSU0274), "Cytochrome c, and cytochrome b", 619 aa, **nine**
  CXXCH motifs, with a TM segment — a genuine inner-membrane multiheme cytochrome, and
  still correctly excluded.
- **GSU2359 is `Q74AJ5`**, a family-57 glycoside hydrolase with no hemes. It was never a
  sensible negative for a cytochrome screen and is dropped rather than fixed.
- In its place, **NrfA `Q747W1`** (GSU3154), the periplasmic nitrite reductase this page
  has named as a false positive throughout. It is a far better negative: four motifs, a
  signal peptide and no TM segment, so every clause of the base filter passes it and it
  is removed **only** by the named-family rule.

The set is now built so each negative tests a different clause — ImcH the TM call, CbcL
the TM call with the upper bound as backup, NrfA the named-family rule alone — and each
attribution is verified by removing one clause at a time. That also answers a fair
objection to the named-family rule, that it drops the informative negatives before they
can be scored: with NrfA registered, the rule's one hard case is now scored explicitly
instead of being argued about in prose.

The conclusions this page draws survive the correction, and were re-run rather than
assumed: no candidate count depends on the negative list, and the signal-peptide verdict
is identical with the corrected set, since NrfA has a signal peptide and the other two
are excluded on topology.

### The falsification: a floor of four hemes loses the PcECN

`A3MW92` carries **four hemes per subunit but only three CXXCH motifs** — the fourth is
coordinated across the subunit interface, which the authors could only see in the filament
model. So **motif count underestimates heme count** for a filament protein, which is
exactly the class this screen is for, and a floor of 4 is wrong:

| floor | *P. calidifontis* candidates | PcECN found |
|---|---:|---|
| `--min-hemes 4` | **0** | **MISS** |
| `--min-hemes 3` | **1** | PASS |

At a floor of 4 the screen does not merely rank the answer badly, it returns nothing at all
from a proteome that demonstrably contains an ECN. At a floor of 3 it returns **one
candidate, and that candidate is the PcECN** — 2,151 proteins to 1.

Lowering the floor costs about 20% more candidates elsewhere and loses no recall anywhere,
so **3 is now the default**.

### The five-proteome result

Recommended setting, `--min-hemes 3 --max-hemes 8 --refine --no-require-signal`:

| Proteome | proteins | 3–8 motifs | no TM | final | reduction | known kept |
|---|---:|---:|---:|---:|---:|---|
| *G. sulfurreducens* PCA | 3,402 | 45 | 42 | **24** | 142× | 4 / 4 |
| *C. bemidjiense* Bem | 4,042 | 36 | 33 | **18** | 225× | 5 / 5 |
| *G. daltonii* FRC-32 | 3,798 | 36 | 33 | **24** | 158× | 2 / 2 |
| *P. calidifontis* VA1 | 2,151 | 4 | 1 | **1** | 2151× | 1 / 1 |
| *A. veneficus* SNP6 | 2,065 | 10 | 9 | **7** | 295× | 1 / 1 |

**13 / 13 recall**, across two domains of life, at 142–2151× reduction. The two
*G. sulfurreducens* rules derived from four bacterial positives were never tuned on an
archaeon, and both survive it: all seven proteins the paper considered carry **only**
`IPR036280` (multiheme cytochrome, a homologous superfamily) and no named family, so the
family rule keeps every one of them; the TM clause does the real work in
*P. calidifontis*, excluding `A3MW89`, `A3MW94` and `A3MW99`; and the lipoprotein rule
drops two in *A. veneficus*.

The caveat on the held-out Geobacteraceae still applies and is now explicit in the script:
their "known members" are CDD `cd21555` homologs — membership in a hand-curated model, not
a solved filament. Counting strictly, **five** of the thirteen are solved filaments — OmcE
(7TFS), OmcS (6NEF), OmcZ (7LQ5, 8D9M), PcECN and AvECN — and all five are recovered, so
the honest recall figure on solved structures is 5 / 5. OmcT is a characterised tandem
paralog of OmcS with no structure of its own, and the remaining seven are cd21555 model
members.

### What the filter provably cannot do

The best evidence for the structural second stage comes from the paper's own negatives.
In *A. veneficus*, `F2KMU7` and `F2KPF5` both **pass this filter** and are retained among
the seven candidates. The authors excluded them only after building them into the cryo-EM
map: `F2KMU7` has a helix-rich region at 120–150 that the map cannot explain, and `F2KPF5`
has a loop (131–151) too short to fit where `F2KMU8` needs 136–164. In *P. calidifontis*,
`A3MW89` — the *only* protein in that proteome with four CXXCH motifs, and so the obvious
sequence-level candidate — was excluded because its AlphaFold fold does not match the map.

Nothing in the sequence separates these from the real subunit. They are tracked as
`near_misses` rather than negatives for that reason: counting them as false positives would
blame the filter for the one thing a sequence filter cannot be expected to do, and would
understate what the structural stage is for. An independent group needed cryo-EM to make
exactly the discrimination this project proposes to make with heme geometry.

## Honest limits

- **Five solved filaments is still a small positive set.** Precision measured against
  five positives across five proteomes is a weak estimate, and the true positive set in
  any of these organisms is unknown and plausibly larger — which is the point of the
  cd21555 overlap above. The seven cd21555 homologs in the held-out Geobacteraceae are
  model members, not solved structures, so they test propagation rather than truth.
- **Motif counting is a proxy for heme count, and the archaea showed it can undercount.**
  `A3MW92` binds four hemes through three motifs. The fix for that was to lower the
  floor, not to claim the counter is right: a heme coordinated across a subunit
  interface is invisible to any single-sequence rule, so the floor is now set to
  tolerate one such heme and would still miss a subunit with two.
- **A motif is not necessarily a heme.** `CXXCH`, `CXXXCH` and long-linker variants are
  counted canonical-first and non-overlapping; a motif present but not used for heme
  attachment still counts, and an unusual attachment chemistry would be missed.
- **Signal-peptide and TM calls are UniProt's**, largely from SignalP and Phobius for
  unreviewed entries, so the filter inherits their error rates. The signal clause is now
  off by default, so only the TM call is load-bearing — and in *P. calidifontis* it is
  load-bearing on its own, excluding all three of that proteome's other multiheme
  candidates.
- **The named-family rule is still the weakest.** It survived an archaeal test it was
  never tuned on, which is real evidence, but it remains close to "the positives are
  unclassified" — partly a fact about what InterPro has curated rather than about the
  biology. If InterPro ever builds a family for this class, the rule inverts.
- **Two domains, five proteomes.** The *S. oneidensis* run is a sanity check, not a
  measurement. Untested: the ANME and Methanoperedenaceae OmcZ-type cytochromes, where
  there is no solved filament to score against.
