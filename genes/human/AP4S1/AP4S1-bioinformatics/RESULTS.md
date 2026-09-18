# AP4S1 (sigma4): if the sigma-side pocket is intact, where does the AP-4 dileucine negative come from?

Reproduce with `uv run python basic_patch.py` in this directory; console output is kept
verbatim in `RESULTS_raw.txt` and the machine-readable form in `results.json`. All eight
sequences are fetched live from the UniProt REST API at run time. Nothing is hardcoded,
every expected sequence length is asserted before scoring, and the script exits 2 rather
than reporting a conclusion if its own method control fails.

## Question

Human AP4S1 encodes sigma4, the small subunit of the AP-4 adaptor. The molecular question
under review is whether sigma4 contributes to cargo-signal recognition the way the sigma
subunits of AP-1, AP-2 and AP-3 do.

The measured answer is that it does not. In a yeast three-hybrid assay, three canonical
`(D/E)XXXL(L/I)` signals — ENTSLL from HIV-1 Nef, ERQPLL from mouse tyrosinase and ERAPLI
from human LIMP-II — each bound the gamma1-sigma1A, alphaC-sigma2 and delta-sigma3A
hemicomplexes but not the homologous epsilon-sigma4 hemicomplex of AP-4
[PMID:21097499].

The companion analysis in `genes/human/AP1S1/AP1S1-bioinformatics/` used sigma4 as a
verified negative control and found it scores 4/5 at the sigma-side hydrophobic pocket —
the same score as the three verified binders. That analysis therefore closed one door
(residue conservation at the sigma pocket does not discriminate) and left the obvious next
question open: it concluded the specificity difference "must lie elsewhere — in the partner
large subunit, in the surrounding surface, or in conformational accessibility of the
pocket." This analysis tests the first of those three.

The site is not built by sigma alone. PMID:21097499 describes it as "hydrophobic pockets on
sigma2 that fit the Leu and (L/I) residues, and a basic patch straddling the boundary of
alpha and sigma2" that reads the acidic residue — so the acidic-residue reader is a
**two-part** patch with one basic residue on the sigma and one on the large subunit. The
paper names the large-subunit residue in each of the three binding complexes (gamma1 Arg15,
alphaC Arg21, delta Arg26) and shows all three matter, with gamma1 Arg15 mattering most:
"mutation of gamma1 R15E caused a much greater reduction in binding to the (D/E)XXXL(L/I)
signals than mutation of sigma1A Arg 15".

So: **is the large-subunit half of the patch present in epsilon (AP4E1)?**

## Design

Anchors are the three large-subunit basic residues named above, each first re-checked
against the live sequence. Positions are transferred onto epsilon by global pairwise
alignment (Biopython `PairwiseAligner`, BLOSUM62, gap open -11 / extend -1).

The large adaptins are ~800-1150 aa and only ~22-30% identical to one another, which is
exactly the regime where a full-length pairwise alignment can silently misplace a single
residue. The script therefore refuses to report the answer unless it first passes a
**method control**: because the paper states the three anchors are equivalent positions,
a trustworthy alignment must recover gamma1 R15 <-> alphaC R21 <-> delta R26 in all six
ordered directions. If it does not, the run exits 2 and Test 2 is not printed.

The sigma side is re-derived in the same run by the same method, so both halves are scored
by one procedure rather than compared across two analyses.

## Result 1 — the anchors are real and the method control passes 6/6

All four published anchor positions hold in the current sequences: gamma1 (O43747) R15,
alphaC (O94973) R21, delta (O14617) R26, sigma2 (P53680) R15.

| from | to | expected | got |
|---|---|---|---|
| gamma1 R15 | alphaC | 21 | 21 (R) |
| gamma1 R15 | delta | 26 | 26 (R) |
| alphaC R21 | gamma1 | 15 | 15 (R) |
| alphaC R21 | delta | 26 | 26 (R) |
| delta R26 | gamma1 | 15 | 15 (R) |
| delta R26 | alphaC | 21 | 21 (R) |

6/6. The mapping method is trustworthy for this position despite the divergence
(gamma1/alphaC 30.5%, gamma1/delta 25.3%, alphaC/delta 23.5%).

## Result 2 — epsilon does not carry a basic residue at that position

All three anchors independently map to the **same** epsilon residue, position 44, and it
is threonine:

| anchor | maps to epsilon | residue | basic? |
|---|---|---|---|
| gamma1 R15 | 44 | T | no |
| alphaC R21 | 44 | T | no |
| delta R26 | 44 | T | no |

Local sequence makes the mapping visible without trusting the aligner:

```
delta   (AP3D1)  D L V R G I [R] N H K E D E     <- R26
epsilon (AP4E1)  S L V R G I [T] A L T S K H     <- T44
gamma1  (AP1G1)  E L I R T I [R] T A R T Q A     <- R15
alphaC  (AP2A2)  V F I S D I [R] N C K S K E     <- R21
```

Epsilon and delta share an identical `LVRGI` immediately N-terminal to the anchor, so the
register is not in doubt: the residue in question is substituted, not displaced.

Note what is *not* being claimed. Epsilon is not devoid of basic residues here — it retains
the arginine three positions upstream (R41), the one delta carries as R23. What is missing
is the arginine at the patch position itself, the residue whose mutation
(gamma1 R15E / alphaC R21E / delta R26E) reduces signal binding in all three binding
complexes.

## Result 3 — the sigma side is retained, including in sigma4

Mapping sigma2 Arg15 by the same method:

| sigma | position | residue | basic? |
|---|---|---|---|
| sigma1A (AP1S1, P61966) | 15 | R | yes |
| sigma3A (AP3S1, Q92572) | 15 | R | yes |
| sigma4 (AP4S1, Q9Y587) | 15 | R | yes |

This reproduces, by an independent route, the AP1S1 analysis's finding that sigma4 looks
like a binder at the sigma-side positions.

## Conclusion, and what it is not

The acidic-residue-reading basic patch of the dileucine site is **half-complete in AP-4**:
present on sigma4 (Arg15, retained), absent on epsilon (Thr44, substituted). Every complex
that binds `(D/E)XXXL(L/I)` signals has both halves; the one complex that does not bind
them is the one missing the large-subunit half.

**This is a hypothesis consistent with the measured negative, not a test of it.** The
experiment that would test it is an epsilon T44R substitution assayed as an
epsilon(T44R)-sigma4 hemicomplex against the same three signals. Three caveats bound the
claim:

1. Half a patch is sufficient to weaken binding, not obviously to abolish it. In AP-1 the
   sigma-side arginine is close to dispensable (sigma1A R15E is "among the substitutions
   that did not abolish binding"), so AP-4 could be argued to have lost the half that
   matters — but AP-2 and AP-3 need both, and no quantitative prediction follows.
2. The negative itself is bounded: three signals, one assay format. The authors of
   PMID:21097499's predecessor wrote that "it will be of interest to determine whether
   other [DE]XXXL[LI] signals are recognized by alpha-sigma2 or epsilon-sigma4, which
   tested negative in our assays" [PMID:14691137] — and the alpha-sigma2 half of that
   earlier negative did not hold: by 2011 the same laboratory reported that all three
   signals do interact with alphaC-sigma2 [PMID:21097499]. Only the epsilon-sigma4
   negative survived the broader panel.
3. AP-4's own cargo signals are read elsewhere entirely: the YXXO-type signal of APP binds
   a distinct site on mu4 [PMID:20230749, PMID:24498434], and the ATG9A peptide binds
   mu4-CTD with Kd 1.1 uM by ITC [PMID:41565640]. Nothing here suggests AP-4 is a poor
   adaptor; it suggests AP-4 does not use the sigma-plus-large-subunit dileucine site.

In short: sigma4 retains Arg15 of the basic patch, epsilon carries Thr44 where all three binding complexes carry Arg, and this analysis supports no cargo-signal-binding molecular function for AP4S1.

**Consequence for annotation.** No cargo-signal-binding molecular function should be
asserted for AP4S1, by conservation argument or otherwise. The AP1S1 analysis's rule —
"a residue-conservation argument should not be used to extend this function to an untested
sigma paralog" — holds, and this analysis shows the converse is also true: sigma4's intact
pocket is not evidence of binding, because the half of the site it cannot supply on its own
is the half AP-4 has lost.
