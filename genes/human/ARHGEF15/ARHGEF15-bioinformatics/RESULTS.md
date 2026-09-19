# ARHGEF15 bioinformatics: exchange machinery, and what GO can say about the substrate

Two committed, re-runnable checks. Both were written to be able to fail, and both are
self-tested by breaking their own input on purpose.

```
uv run --no-project python fetch_sequences.py          # panel -> sequences/, panel_identities.json
uv run --no-project python dh_specificity.py           # -> results.json
uv run --no-project python dh_specificity.py --self-test
uv run --no-project python gef_term_availability.py    # -> gef_term_availability.json
```

`dh_specificity.py` needs MAFFT on the path (L-INS-i); it raises rather than degrading
silently if MAFFT is absent, because a missing aligner is a tooling failure, not a result.

---

## 1. The exchange machinery is intact in the human protein — and says nothing about substrate

### What was tested

Margolis et al. 2010 (PMID:21029865) identified three residues "within the α5 helix of E5's
DH domain" — L562, Q566, R567, numbered in **mouse** Ephexin5 — and built the triple-alanine
mutant **E5-LQR** as a predicted GEF-dead control. They introduced those residues as a
*specificity* signature: the three "are conserved in other GEFs that, like E5, activate RhoA
but not Rac1 and Cdc42".

Two separate questions follow, and they are answered separately below:

1. **Mapping.** Does the human protein carry those residues? Human ARHGEF15 is 841 aa and
   mouse Ephexin5 is 849 aa, so the human positions must come from an alignment. Subtracting
   8 would be a guess that happens to be right.
2. **Discrimination.** Is the triad actually a RhoA-vs-Rac/Cdc42 signature? That is a claim
   about a comparator panel and is falsifiable.

### Result 1 — every published site is retained in human ARHGEF15

Pairwise MAFFT L-INS-i, mouse Q5FWH6 → human O94989:

| mouse site | role | human site | status |
|---|---|---|---|
| L562 | α5 triad | **L554** | RETAINED |
| Q566 | α5 triad | **Q558** | RETAINED |
| R567 | α5 triad | **R559** | RETAINED |
| Y361 | EphB2 phosphosite; Cdc42-vs-RhoA selectivity switch | **Y353** | RETAINED |

Y353 is the residue UniProt already annotates as `MOD_RES 353 Phosphotyrosine; by EPHB2`
by similarity to Q5FWH6, so the mapping agrees with the UniProt curator's.

The same alignment was run in the other direction for the disease variants. All three lie
**outside** the UniProt DH domain (417–601):

| human variant | mouse position | same residue in mouse |
|---|---|---|
| R21 (BSVD5 R21C) | R21 | yes |
| V360 (BSVD5 V360M) | **V368** | yes |
| R604 (epilepsy, uncertain significance) | **R612** | yes |

Two of these settle apparent numbering discrepancies rather than creating them.
PMID:36929019 names its knock-in mouse `Arhgef15-e(V368M)` while UniProt lists the human
variant as V360M — the alignment shows these are the same residue in the two species'
numbering, not two different variants. Independently, PMID:23647072 states of its human
R604C variant that "a homologous amino acid in mouse Ephexin5 at Arg612Cys (R612C) shows a
~47% reduction as compared with mouse WT protein", which is the identical human→mouse
correspondence this alignment computes without reference to that paper.

### Result 2 — the triad does not discriminate, in this panel

Twelve DH domains (UniProt-delimited, one per protein), MAFFT L-INS-i, residues read at the
three alignment columns carrying the mouse triad:

| protein | role | triad | full match |
|---|---|---|---|
| O94989 human ARHGEF15 / Ephexin5 | target | **LQR** | yes |
| Q5FWH6 mouse Arhgef15 / Ephexin5 | anchor | LQR | yes |
| Q8N5V2 NGEF / Ephexin1 | family | IQR | no |
| Q8IW93 ARHGEF19 / Ephexin2 | family | IQR | no |
| Q12774 ARHGEF5 / Ephexin3 | family | IQR | no |
| Q5VV41 ARHGEF16 / Ephexin4 | family | IQR | no |
| Q92888 ARHGEF1 / p115RhoGEF | RhoA-specific | PQR | no |
| O15085 ARHGEF11 / PDZ-RhoGEF | RhoA-specific | IQR | no |
| Q9NZN5 ARHGEF12 / LARG | RhoA-specific | PQR | no |
| Q13009 TIAM1 | Rac1-specific | IQR | no |
| P98174 FGD1 | Cdc42-specific | **LQR** | yes |
| Q15811 ITSN1 | Cdc42-specific | **LQR** | yes |

**RhoA-specific comparators carrying the full triad: 0/3.
Rac1/Cdc42-specific comparators carrying the full triad: 2/3.**

The signature points the wrong way in this panel. Q and R are effectively invariant across
all twelve DH domains, so the only discriminating column is the first, and there human
Ephexin5 groups with the two Cdc42-specific GEFs (FGD1, ITSN1) rather than with the three
canonical RhoA-specific GEFs.

### What this does and does not license

It does **not** refute Margolis et al. Their assignment was made against a structure-based
set of RhoA-specific GEFs (Snyder et al. 2002); the alignment here is sequence-based over a
panel they did not choose, so a disagreement is a failure to reproduce the discrimination,
not a demonstration that no such determinant exists.

What it does establish is that the triad **cannot be used to infer human substrate
specificity**, and the functional literature agrees with that reading rather than with the
specificity reading. Petshow et al. 2025 (PMID:40138406) use the very same triple mutant as
their **GEF-dead control for Cdc42** — "either E5WT, E5Y361F, or GEF-dead E5 (E5LQR)" — so
the triad is required for exchange onto Cdc42 as well as onto RhoA. A residue set required
for both activities is exchange machinery, not a substrate selector.

Hence the conclusion runs in both directions, and neither direction is decisive on its own:

- **Presence is not activity.** Human ARHGEF15 retains the full triad and the phosphosite,
  which is consistent with an intact exchange site; it is not evidence that the human
  protein is active, and no measurement of human ARHGEF15 exchange activity exists outside
  the two transfected-cell assays cited in the review.
- **Absence would not have been inactivity, and presence is not specificity.** The residues
  do not separate RhoA-GEFs from Cdc42-GEFs here, and the one substrate-selectivity switch
  that *is* experimentally established for this protein is not a DH residue at all but the
  phosphorylation state of Y361/Y353, which sits 60 residues N-terminal of the DH domain.

## 2. GO can no longer name the GTPase a GEF acts on

Checked on two independent services, because this is load-bearing for the review's
knowledge gap and because neither service alone is trustworthy on merges. QuickGO
**silently resolves** merged identifiers — asking for a merged id returns the *successor's*
record with `isObsolete: false` — so "not obsolete" from QuickGO is ambiguous between
"current" and "merged away". OLS4 is a different codebase and reports `is_obsolete` plus
`term_replaced_by` against the id actually requested.

**Molecular function — flattened. All five substrate-specific GEF terms are merged into
`GO:0005085 guanyl-nucleotide exchange factor activity`, agreed by both services (5/5, zero
disagreements):**

| merged id | historical label | QuickGO returns | OLS4 `term_replaced_by` |
|---|---|---|---|
| GO:0005086 | ARF guanyl-nucleotide exchange factor activity | GO:0005085 | GO_0005085 |
| GO:0005087 | Ran guanyl-nucleotide exchange factor activity | GO:0005085 | GO_0005085 |
| GO:0005088 | Ras guanyl-nucleotide exchange factor activity | GO:0005085 | GO_0005085 |
| **GO:0005089** | **Rho guanyl-nucleotide exchange factor activity** | GO:0005085 | GO_0005085 |
| GO:0008321 | Ral guanyl-nucleotide exchange factor activity | GO:0005085 | GO_0005085 |

`GO:0005085` has **zero `is_a` children** (OLS4); QuickGO returns only `GO:0032045`
(`capable_of`) and `GO:1905098` (`negatively_regulates`), neither of which is a subtype. The
substrate names survive only as **synonyms** of the general term — Rho, Rac, Ras, Ran, Rab,
Rap, Ral, ARF and Sar are all listed as `guanyl-nucleotide exchange factor activity`
synonyms. This is the exact mirror of the GAP side, where GO:0005097/0005099/0005100/0008060
were merged into `GO:0005096 GTPase activator activity`.

**Biological process — not flattened.** All seven substrate-specific BP terms checked are
current on both services: `GO:0007266 Rho protein signal transduction`,
`GO:0032488 Cdc42 protein signal transduction`, `GO:0035023`/`GO:0035025` (regulation and
positive regulation of Rho protein signal transduction), `GO:0032489 regulation of Cdc42
protein signal transduction`, `GO:0035020`/`GO:0035022` (Rac).

So the two aspects disagree about whether a GEF's substrate is expressible: the BP branch
still names it, the MF branch no longer can.

One gap inside the BP branch is worth recording, since it bears directly on this gene.
`GO:0032489 regulation of Cdc42 protein signal transduction` has **zero children on both
services**, whereas the Rho and Rac equivalents each carry signed children
(`GO:0035025`/`GO:0035024`, `GO:0035022`). There is therefore no *positive* regulation of
Cdc42 protein signal transduction term, so a GEF shown to activate Cdc42 can only be placed
on the unsigned parent. Note also that `GO:0032488` is an `is_a` descendant of `GO:0007266`,
so the Rho terms do not exclude Cdc42 — `GO:0035025`, which human ARHGEF15 already carries,
is satisfied by activating either.
