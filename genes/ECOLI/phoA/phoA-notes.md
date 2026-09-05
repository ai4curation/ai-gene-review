# phoA (E. coli K-12) — review notes

UniProt: P00634 (PPB_ECOLI) · bacterial alkaline phosphatase (BAP) · PANTHER
PTHR11596:SF5 · catalytic Ser124 (precursor numbering; the classic Ser102 of the mature
protein).

Reviewed as the family's deep anchor: the seed for both the unrestricted molecular-function
PAINT node and the Enterobacteriaceae periplasm node in PTHR11596.

## What makes this record unusual

phoA is used as a *tool* more than it is studied as an enzyme — as a Sec-export model
substrate, as a periplasmic marker, as a reporter, and as a bench dephosphorylation
reagent. That shows up directly in its GO record, and three of the four citation problems
below are of that kind. It is a useful worked example of how reagent use contaminates
annotation.

## Citation problems

1. **PMID:8634266 — the worst one.** Cited as the IDA source for *two* molecular function
   terms (`GO:0004035` alkaline phosphatase activity, `GO:0004721` phosphoprotein
   phosphatase activity). The paper is "Specific recognition of coiled coils by infrared
   spectroscopy: analysis of the three structural domains of type III intermediate
   filament proteins" — an FTIR study of desmin and neurofilaments. The string "alkaline
   phosphatase" does not occur anywhere in the cached record. Its only contact with
   phosphatases is that neurofilament tails were examined in phosphorylated and
   dephosphorylated forms, which in 1996 would routinely have used AP as a reagent.
   - `GO:0004035` → ACCEPT (term unimpeachable, independently supported by PMID:13826559),
     citation flagged.
   - `GO:0004721` → **UNDECIDED**. This is the only support for a real functional claim —
     that BAP is a protein phosphatase. Not removed (full text unavailable, and the
     project's rule forbids overruling an experimental annotation on abstract-only
     grounds), but it should not stand unexamined. Highest-value follow-up on this gene is
     a records check, which is why it is listed as a suggested experiment.
2. **PMID:23937259** — an IPI source for protein binding, but the paper is a human
   LRRK2 / protein phosphatase 1 study with no mention of alkaline phosphatase. Likely an
   automated interaction import off a reagent use. → UNDECIDED, reference marked
   `relevance: NONE, correctness: UNVERIFIED`.
3. Three further `GO:0005515` rows (PMID:18022369, 19766568, 19924216) are **genuine**
   SecA/translocase interactions — proPhoA is the canonical SecB-independent Sec substrate
   [PMID:19924216, "Like proOmpA5, proPhoA requires SecA as an essential receptor."] — but
   they concern export of the *precursor*, and the signal peptide is cleaved from the
   mature enzyme. KEEP_AS_NON_CORE, not over-annotation.

Note I initially wrote PMID:8634266's title from memory and the reference validator caught
it (I had invented "the amide I mode of type III and IV..."). Titles came from the cached
front matter afterwards. Worth remembering: the title check is real and it works.

## The hydrogenase annotation — real, but pointed backwards

`GO:0033748 hydrogenase (acceptor) activity` and `GO:0030613 oxidoreductase activity,
acting on phosphorus or arsenic in donors`, both IDA from PMID:15148399.

The biology is genuine and remarkable: BAP is the phn-independent phosphite oxidase, and
the reaction evolves H2 [PMID:15148399, "Surprisingly, BAP catalyzes the oxidation of Pt to
phosphate and molecular H2."]. Purified enzyme, N-terminally sequenced.

But GO:0033748 is defined as `H2 + A = AH2` — H2 *consumed*. BAP *evolves* H2. So the term
is directionally inverted. → MODIFY to GO:0030613, which describes the reaction in the
direction it runs (phosphite as the electron donor) and is already annotated from the same
experiment. EC treats hydrogenases as reversible, which is probably how the term was
picked; GO's definition is not written reversibly.

Both rows are KEEP_AS_NON_CORE / MODIFY rather than core because the paper's own numbers
put the side activity 2–3 orders of magnitude below the phosphatase reaction:
[PMID:15148399, "Highly purified BAP catalyzed Pt oxidation with specific activities of
62-242 milliunits/mg and phosphate ester hydrolysis with specific activities of 41-61
units/mg."] I considered adding GO:1902422 hydrogen biosynthetic process and decided
against it — a BP term would overstate the physiological weight of a reaction that slow.

## One NEW

`GO:0042803 protein homodimerization activity` (ISS), for consistency with the family
review, which records the dimer as functionally load-bearing family-wide. UniProt: isozymes
1 and 3 are dimers of identical chains. ISS rather than IDA because I asserted it from the
UniProt subunit record plus the family argument rather than from a cached paper
demonstrating it specifically for phoA.

## Not proposed

`GO:0016036 cellular response to phosphate starvation` would be the physiologically
informative BP for this gene — phoA is the canonical pho-regulon member and the term is
used in E. coli for appA, phoR and psiE. I did not propose it because no cached publication
in this gene's reference set demonstrates the induction, and deep research had not returned
by the time the review was written. It is the obvious next addition if a source is cached.
