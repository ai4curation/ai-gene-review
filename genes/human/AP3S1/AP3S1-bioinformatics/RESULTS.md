# AP3S1 (sigma3A): the AP-3 dileucine pocket, and whether sigma3A differs from sigma3B

Reproduce with `uv run python sigma3_pocket.py` in this directory. Every sequence is
fetched live from the UniProt REST API; nothing is hardcoded, and each expected sequence
length is asserted so that a re-released canonical sequence aborts the run instead of
silently shifting every position. The unedited console output is kept in
`RESULTS_raw.txt` and the machine-readable form in `results.json`.

## Questions

Human AP3S1 encodes sigma3A, the small subunit of the AP-3 adaptor. Two separable things
are tested here.

**Q1. Does sigma3A carry the residues the primary literature names for it?**
Acidic dileucine sorting signals — the (D/E)XXXL(L/I) motif — bind no single AP subunit.
They bind the gamma1-sigma1A, alphaC-sigma2 and delta-sigma3 hemicomplexes and not the
homologous epsilon-sigma4 hemicomplex of AP-4. The site was defined structurally on AP-2,
and Mattera et al. (PMID:21097499) transferred it onto AP-3 by mutating sigma3A itself:
V94D and L109S abolish signal binding, and Arg 15 and Leu 107 contribute. This asks
whether those positions really carry those residues in the current Q92572 sequence, and
whether an alignment computed here independently reproduces the sigma2-to-sigma3A
correspondences the paper asserts.

**Q2. Can sigma3A be told apart from sigma3B (AP3S2) at this site?**
GOA gives the two paralogs near-identical annotation sets, and PMID:14691137 found that
both delta-sigma3A and delta-sigma3B bind the LIMP-II dileucine tail. If the site is
identical between them, that interchangeability is a property of the proteins, not a
shortcut in curation.

**Q3** additionally reports the identity between human AP3S1 and the mouse ortholog that
serves as the Ensembl-Compara and ISS donor for four of this gene's annotations.

## Design

The anchor is human sigma2 (AP2S1, P53680), whose pocket is structurally defined and whose
residues were mutated in PMID:21097499. Anchor positions are mapped onto each paralog by
global pairwise alignment (Biopython `PairwiseAligner`, BLOSUM62, gap open -11 /
extend -1), and the mapping is cross-checked against the homologous positions the paper
states independently.

The design includes a **verified negative control**: sigma4 (AP4S1, Q9Y587) is in the same
PANTHER family, PTHR11753, but the epsilon-sigma4 hemicomplex of AP-4 was tested and does
**not** bind these signals. A conservation argument that cannot separate the verified
binders from the verified non-binder is not evidence, and including sigma4 is what makes
that testable rather than assumed.

Ten sequences: sigma3A (Q92572, target), sigma3B (P59780), sigma2 (P53680, anchor),
sigma1A/1B/1C (P61966, P56377, Q96PC3), sigma4 (Q9Y587, negative control), mouse Ap3s1
(Q9DCR2) and two PAINT IBD donors from the AP-3 clade — *S. cerevisiae* Aps3 (P47064) and
*C. albicans* Aps3 (Q59QC5).

## Result 1 — every residue the literature names for sigma3A is present

| Position in Q92572 | Expected | Found | Source of the claim |
|---|---|---|---|
| 15 | R | R | sigma3A Arg 15, contributes to binding the acidic residue |
| 94 | V | V | sigma3A V94D abolishes signal binding |
| 98 | D | D | sigma3A D98A, signal-dependent effect on the tyrosinase signal |
| 107 | L | L | sigma3A L107, substitution decreases binding |
| 109 | L | L | sigma3A L109S abolishes signal binding |

All five verify. Q92572 is at sequence version 1 and is 193 aa, matching the length
asserted by the script.

The alignment computed here also reproduces both correspondences the paper states, without
being told them: sigma2 88 maps to sigma3A 94, and sigma2 103 maps to sigma3A 109. It
reproduces the sigma1A pair (88 -> 88, 103 -> 103) as well. The mapping method is
therefore sound.

## Result 2 — the site is retained, and the negative control defeats the conservation argument

| accession | binds dileucine | %id to sigma2 | R15 | A63 | V88 | E100 | L103 | identical |
|---|---|---|---|---|---|---|---|---|
| Q92572 sigma3A | yes | 42.3 | R15 | A69 | V94 | E106 | L109 | 5/5 |
| P59780 sigma3B | yes | 39.4 | R15 | A69 | V94 | E106 | L109 | 5/5 |
| P61966 sigma1A | yes | 46.5 | R15 | A63 | V88 | E100 | I103 | 4/5 |
| P56377 sigma1B | yes | 48.9 | R14 | A62 | V87 | E99 | I102 | 4/5 |
| Q96PC3 sigma1C | yes | 44.4 | R15 | A63 | V88 | E100 | I103 | 4/5 |
| **Q9Y587 sigma4** | **NO** | 43.0 | R15 | A63 | V88 | E100 | I103 | **4/5** |
| Q9DCR2 Ap3s1 (mouse) | n/d | 42.3 | R15 | A69 | V94 | E106 | L109 | 5/5 |
| P47064 Aps3 (yeast) | n/d | 33.8 | R15 | A81 | V106 | E118 | L121 | 5/5 |
| Q59QC5 Aps3 (*C. albicans*) | n/d | 37.3 | R15 | A70 | V95 | E107 | L110 | 5/5 |

sigma3A scores 5/5 — the site is fully retained, and it is in fact a closer match to the
sigma2 anchor than any of the AP-1 sigmas, which carry Ile rather than Leu at the
sigma2 L103 position.

**But sigma4, the verified non-binder, scores 4/5, the same as sigma1A, sigma1B and
sigma1C, all verified binders.** Identity at this pocket therefore does not separate
binders from the non-binder, and the conservation argument for sigma3A carries no weight
on its own. What carries the claim is the direct mutagenesis of sigma3A itself
(PMID:21097499) and the yeast three-hybrid result that the delta-sigma3A hemicomplex binds
the Nef, LIMP-II and tyrosinase signals while alphaC-sigma2 and epsilon-sigma4 handle them
differently or not at all (PMID:14691137, PMID:16162817).

This is worth stating plainly because the mirror error — inferring function from a
retained fold — is as common as inferring loss from a missing residue, and this family is
a case where the fold genuinely does not predict the function.

The two fungal Aps3 sequences, which are PAINT IBD seeds for the family node that gives
AP3S1 its only IBA, also score 5/5, so the site is old.

## Result 3 — sigma3A and sigma3B are indistinguishable at this site

Global identity between AP3S1 and AP3S2 is 83.9% over 193 aa (31 differing positions), and
**all five literature-named pocket positions are identical between them** (R15, V94, D98,
L107, L109 in both). No sequence feature of the cargo-signal site separates sigma3A from
sigma3B.

This is the sequence-level counterpart of the experimental result that both delta-sigma3A
and delta-sigma3B bind the LIMP-II dileucine tail (PMID:14691137), and it means that the
near-identical GOA annotation sets carried by AP3S1 and AP3S2 are a fair representation of
what is known rather than a failure to distinguish them. Whatever separates the two
paralogs functionally, it is not this site.

## Result 4 — the mouse ortholog is sequence-identical

Human AP3S1 (Q92572) and mouse Ap3s1 (Q9DCR2) are both 193 aa and **100% identical**, so
the four annotations this gene receives by Ensembl-Compara transfer or by curator ISS from
Q9DCR2 rest on an unusually safe orthology relation: there is no divergence anywhere in
the protein for the transfer to have to bridge.

## Limits

- Identity at a mapped position is not a structural argument. The pocket geometry was
  solved on AP-2, not on AP-3, and the AP-3 cryo-EM structures (PMID:39705307) show the
  sigma3 dileucine pocket occupied by the N-terminal extension of beta3 rather than by
  cargo, so the site's accessible state in the assembled complex is not settled here.
- The global pairwise alignment is computed ad hoc rather than taken from a versioned
  resource. That is deliberate: the claims state both positions and both residues, so the
  alignment is only how the correspondence was discovered, and each residue is read
  directly from its own sequence.
- Nothing here tests binding. The script cannot and does not assert that sigma3A binds a
  dileucine signal; it tests whether the residues the literature names are where the
  literature says they are, and whether conservation at that site is informative. The
  answer to the second is no.
