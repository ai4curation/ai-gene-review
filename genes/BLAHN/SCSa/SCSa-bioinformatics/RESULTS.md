# Is the curated presequence of Blastocystis SCS alpha distinguishable from chance?

Run `python3 presequence_features.py`. Stdlib only, no network; it reads
`../SCSa-uniprot.txt`, takes the transit-peptide boundary from the record's own
feature table rather than a typed-in number, and hardcodes no results.

Written locally because the OpenScientist service returned nothing for any submission
after 2026-11-26 19:52 (see `genes/BACSU/plsY/plsY-notes.md`). It runs no
targeting-sequence predictor; it computes the features such predictors rest on, and
the expectation for each under this protein's own composition.

## Why this was worth testing

The knowledge gap cites as established "a predicted N-terminal presequence with
arginine two residues before the predicted cleavage site". A companion analysis on
the Mortierellomycota SUCLG2-type beta subunit
(`genes/9FUNG/SUCLG2__A0A9P6TY68/SUCLG2__A0A9P6TY68-bioinformatics/`, addendum) found
that observations of exactly this shape can be chance-level, so the claim should be
tested rather than inherited.

This case differs in a way that matters: the cleavage point here is **curated** in the
record (`TRANSIT 1..18`, `CHAIN 19..318`), not inferred from an alignment. The
arginine-at-−2 observation is therefore not conditional on a guessed cut, which was
the caveat that weakened the equivalent claim for the beta subunit.

## Results, with the beta subunit alongside for calibration

| Feature | SCS alpha (this protein, curated cut) | SUCLG2-type beta (assumed cut) |
|---|---|---|
| Presequence | 18 aa, `MLSRVSQVSRVGFSLARA` | 14 aa, `MPIQRGIVASQVRF` |
| P(zero acidic) | **0.215** | 0.138 |
| P(≥ observed basic) | **0.318** (3 basic) | 0.404 (2 basic) |
| Hydrophobic moment | **+0.460, 98th percentile** | +0.283, 64th percentile |
| Arg at −2 of the cut | **R17, cut curated** | R13, cut assumed |

## What follows

**The composition observations add nothing, again.** Zero acidic residues in 18 occurs
21.5% of the time by chance under this protein's own background, and three or more
basic residues 31.8% of the time. Neither discriminates, exactly as for the beta
subunit. The charge observations that both knowledge gaps lean on are not where the
evidence is.

**But the feature that actually matters is strongly positive here.** Cleavable
mitochondrial presequences form amphipathic helices, and this one sits at the **98th
percentile** of the protein's own 18-residue windows (moment +0.460, 6th of 301). That
is a real signal, and it is the sharpest contrast with the beta subunit, whose
equivalent window was unremarkable at the 64th percentile. The two cases look alike on
the features the gaps quote and come apart on the feature that discriminates.

**The arginine at −2 is worth more here than there.** R17 sits at −2 relative to a
*curated* cleavage point, matching the processing peptidase preference. For the beta
subunit the same observation was conditional on an assumed cut and so was recorded as
merely consistent; here it is not circular.

**Taken together, the presequence prediction for this protein is well supported at
sequence level** — on amphipathicity and the curated −2 arginine, not on the charge
composition the gap cites.

## What this does not establish

Nothing here shows the presequence is **removed**, which is half of what the gap asks,
nor does it locate the protein in the strain of this entry or within the organelle,
which is the other half. A strong presequence prediction is not import, and not
processing. The gap stays OPEN and its resolution still requires the protease
protection, carbonate extraction and N-terminal sequencing it already names. No
localisation dataset was consulted and no annotation was changed.
