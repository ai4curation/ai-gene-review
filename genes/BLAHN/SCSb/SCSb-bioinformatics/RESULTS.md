# Is the curated presequence of Blastocystis SCS beta distinguishable from chance?

Run `python3 presequence_features.py`. Stdlib only, no network; it reads
`../SCSb-uniprot.txt`, takes the transit-peptide boundary from the record's own feature
table, and hardcodes no results.

Written locally because the OpenScientist service returned nothing for any submission
after 2026-11-26 19:52 (see `genes/BACSU/plsY/plsY-notes.md`). It runs no
targeting-sequence predictor.

## Why the pair was tested together

The source behind both subunits' gaps makes a **plural** claim — "the Blastocystis SCS
leader sequences also have arginine at position −2 from the putative cleavage site" —
so testing one subunit leaves the claim half-checked. This completes the pair, with
the Mortierellomycota SUCLG2-type beta subunit as an outgroup for calibration.

## Three presequences, same method

| | SCS beta (here) | SCS alpha | SUCLG2-type beta |
|---|---|---|---|
| Record status | reviewed, curated cut | reviewed, curated cut | unreviewed, cut assumed from alignment |
| Presequence | 14 aa, `MLRMAPKTVGAVRN` | 18 aa, `MLSRVSQVSRVGFSLARA` | 14 aa, `MPIQRGIVASQVRF` |
| P(zero acidic) | 0.167 | 0.215 | 0.138 |
| P(≥ observed basic) | 0.280 (3 basic) | 0.318 (3 basic) | 0.404 (2 basic) |
| **Hydrophobic moment** | **+0.521, 97.8th pct** | **+0.460, 98.0th pct** | +0.283, 64.1st pct |
| Arg at −2 | R13, curated cut | R17, curated cut | R13, assumed cut |

## What follows

**The published plural claim holds.** Both *Blastocystis* subunits carry an arginine at
exactly −2 relative to their curated cleavage points — R13 here, R17 in the alpha
subunit. Neither observation depends on a guessed cut.

**Charge composition is uninformative in all three cases.** Zero acidic residues and
three basic residues in a window this short are what the proteins' own compositions
give by chance (P = 0.167 and 0.280 here). This is the third protein in a row where
the charge observations a knowledge gap quotes add nothing, which is worth stating as
a pattern rather than three separate coincidences.

**Amphipathicity separates the real cases cleanly.** Both *Blastocystis* presequences
sit at the 98th percentile of their own proteins' windows (+0.521 and +0.460), while
the SUCLG2-type gene model's N-terminus sits at the 64th. That contrast is the useful
output of running all three: the method is not simply calling everything chance-level,
so the earlier negative on the SUCLG2 model is a property of that sequence rather than
of the test.

**An incidental confirmation.** The curated transit peptide here is residues 1–14,
which is exactly the mature-chain numbering offset of −14 that the structural
literature on this subunit uses and that was verified independently from two
OpenScientist analyses earlier in this campaign. The curated feature and the
crystallographic numbering convention agree.

## What this does not establish

Nothing here detects the beta subunit in the organelle of this strain, shows that the
presequence is **removed**, or assigns a compartment within the organelle — which is
exactly what the knowledge gap asks for. A strong presequence prediction is neither
import nor processing nor sub-organellar location. The gap stays OPEN and still
requires the immunogold or epitope-tag localisation and N-terminal sequencing it
already names. No localisation dataset was consulted and no annotation was changed.
