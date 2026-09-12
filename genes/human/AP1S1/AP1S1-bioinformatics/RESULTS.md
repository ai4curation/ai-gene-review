# AP1S1 (sigma1A): does the dileucine-signal binding site survive in this paralog?

Reproduce with `uv run python dileucine_site.py` in this directory. All sequences are
fetched live from the UniProt REST API; nothing is hardcoded, and every expected
sequence length is asserted so that a re-released canonical sequence aborts the run
instead of silently shifting every position.

## Question

Human AP1S1 encodes sigma1A, the small subunit of the AP-1 clathrin adaptor. The
molecular claim under review is that sigma1A is not merely a structural filler but
supplies half of the binding site for `[DE]XXXL[LI]` ("dileucine") cargo sorting
signals, which are recognised by the gamma1-sigma1A hemicomplex rather than by any
single subunit. The structural site was originally defined on AP-2, where hydrophobic
pockets on sigma2 accept the Leu and (L/I) residues and a basic patch straddling the
alpha/sigma2 boundary binds the acidic residue.

This analysis asks two separable things:

1. Are the residues that the primary literature names for sigma1A actually present at
   those positions in the current UniProt sequence?
2. Is residue conservation at the sigma2 pocket, on its own, sufficient evidence that a
   given sigma paralog binds dileucine signals?

## Design

The anchor is human sigma2 (AP2S1, P53680), whose pocket is structurally defined and
whose residues were mutated in PMID:21097499. Anchor positions are mapped onto each
paralog by global pairwise alignment (Biopython `PairwiseAligner`, BLOSUM62,
gap open -11 / extend -1), and the mapping is cross-checked against the homologous
positions the paper states independently.

The design includes a **verified negative control**: sigma4 (AP4S1, Q9Y587) is in the
same PANTHER family, PTHR11753, but the epsilon-sigma4 hemicomplex of AP-4 was tested
and does **not** bind these signals. A conservation argument that cannot separate the
verified binders from the verified non-binder is not evidence, and including sigma4 is
what makes that testable rather than assumed.

Sequences: sigma1A (P61966, the target), sigma1B (P56377), sigma1C (Q96PC3),
sigma2 (P53680, anchor), sigma3A (Q92572), sigma4 (Q9Y587, negative control), plus
three PAINT IBD donors for the family node — mouse Ap1s1 (P61967), *S. pombe* vas2
(Q9P7N2) and *S. cerevisiae* Aps1 (P35181).

## Result 1 — every residue the literature names for sigma1A is present

| Position in P61966 | Expected | Found | Source of the claim |
|---|---|---|---|
| 15 | R | R | basic patch, "equivalent to sigma2 Arg 15" — but see the caveat below |
| 63 | A | A | A63D abolishes binding in sigma2 |
| 88 | V | V | sigma1A V88D abolishes signal binding |
| 103 | I | I | sigma1A I103S abolishes signal binding |
| 90 | L | L | the MEDNIK causal variant position, L90P |

All five verify. P61966 is at sequence version 1 and is 158 aa, matching the length
asserted by the script.

**Position 15 is the weakest of the five and is scored anyway.** Mattera et al. report that
sigma1A R15E is *among the substitutions that did not abolish* binding of the Nef and
tyrosine signals, and that mutating the large subunit's arginine (gamma1 R15E) "caused a
much greater reduction in binding ... than mutation of sigma1A Arg 15". So the acidic
residue of the sorting signal is read mainly by the large subunit, and sigma1A's Arg15 is a
subordinate contributor. It is kept as one of the five anchor sites because it is part of
the structurally defined basic patch and because dropping an inconvenient site would bias
the scoring, but no conclusion here should lean on it. The same subordination is recorded
in the `residue_claims` comment in the gene review.

## Result 2 — the alignment independently reproduces the stated homologies

The paper states specific homologous positions; the alignment was not told them and
recovers every one:

| sigma2 anchor | stated homologue | alignment gives |
|---|---|---|
| 88 | sigma1A 88 | sigma1A 88 |
| 103 | sigma1A 103 | sigma1A 103 |
| 88 | sigma3A 94 | sigma3A 94 |
| 103 | sigma3A 109 | sigma3A 109 |

This is a control on the method rather than a new finding, but it means the mapping
used for the remaining paralogs is trustworthy.

## Result 3 — the negative control retains the site, so conservation alone proves nothing

| Accession | Paralog | Binds dileucine? | % id to sigma2 | Identical at the 5 anchor sites |
|---|---|---|---|---|
| P61966 | sigma1A (target) | yes | 46.5 | 4/5 |
| P56377 | sigma1B | yes | 48.9 | 4/5 |
| Q96PC3 | sigma1C | yes | 44.4 | 4/5 |
| Q92572 | sigma3A | yes | 42.3 | 5/5 |
| **Q9Y587** | **sigma4** | **NO** | 43.0 | **4/5** |
| P61967 | mouse Ap1s1 | not tested | 46.5 | 4/5 |
| Q9P7N2 | pombe vas2 | not tested | 50.7 | 5/5 |
| P35181 | yeast Aps1 | not tested | 42.6 | 4/5 |

The single non-identity in sigma1A, sigma1B, sigma1C and sigma4 alike is the
conservative L103I substitution relative to sigma2; sigma1A carries Ile at 103, which
is exactly the residue Mattera et al. mutated as I103S.

**The negative control scores 4/5, the same as the target and the other two verified
sigma1 binders.** Residue identity at this pocket therefore does not discriminate
binders from the non-binder, and the conservation argument for sigma1A is weaker than
it appears. The specificity difference between the AP-1/AP-2/AP-3 sigmas and sigma4
must lie elsewhere — in the partner large subunit, in the surrounding surface, or in
conformational accessibility of the pocket — not in these five positions.

## Conclusion

The site is fully **retained** in sigma1A: all five positions named in the literature
are present, and the one difference from sigma2 (L103I) is conservative and is itself a
validated functional position in sigma1A. But retention is not what establishes the
function here. What establishes it is direct evidence on sigma1A itself: the
gamma1-sigma1A hemicomplex binds the Nef, tyrosinase and LIMP-II dileucine tails while
mismatched subunit combinations do not; point substitutions in sigma1A (V88D, I103S,
A63D) abolish that binding; and the AP-1 crystal structure with HIV-1 Vpu shows the Vpu
dileucine mimic bound in a pocket on the sigma1 subunit itself.

The practical consequence for annotation is that sigma1A's contribution to cargo
recognition is a genuine, subunit-attributable molecular function — but one it exerts
only as part of the gamma1-sigma1A hemicomplex, never alone, which is the reading that
`contributes_to` expresses. It also means a residue-conservation argument should not be
used to extend this function to an untested sigma paralog.
