# ARHGEF15 bioinformatics: the measured substrate, the exchange machinery, and what GO can say

Committed, re-runnable checks. Each was written to be able to fail, and each is self-tested
by breaking its own input on purpose.

```
uv run --no-project python fetch_sequences.py          # panel -> sequences/, panel_identities.json
uv run --no-project python dh_specificity.py           # -> results.json
uv run --no-project python dh_specificity.py --self-test
uv run --no-project python gef_term_availability.py    # -> gef_term_availability.json
uv run --no-project --with openpyxl python muller2020_specificity.py            # -> muller2020_specificity.json
uv run --no-project --with openpyxl python muller2020_specificity.py --self-test
uv run --no-project python comparator_annotations.py   # -> comparator_annotations.json
uv run --no-project --with pyyaml python check_quotes.py --self-test
uv run --no-project --with pyyaml python audit_review.py --self-test
```

`dh_specificity.py` needs MAFFT on the path (L-INS-i); it raises rather than degrading
silently if MAFFT is absent, because a missing aligner is a tooling failure, not a result.

---

## 0. The measured substrate, from a paywalled paper's free supplement

**PMID:32203420** (Müller et al. 2020, Nat Cell Biol) is a family-wide substrate-specificity
screen of all 145 human RhoGEFs and RhoGAPs. It is the source Reactome cites for placing
ARHGEF15 in **both** `RHOA GEFs activate RHOA` (R-HSA-8980691) and `CDC42 GEFs activate
CDC42` (R-HSA-9013159) — and it is **absent from ARHGEF15's GOA entirely**.

The paper is paywalled, Europe PMC reports no PMC record and `isOpenAccess: N`, so the
cached publication is abstract-only. The **supplementary tables are freely downloadable**
from Springer, and Supplementary Table 2 carries the per-gene screen result.
`muller2020_specificity.py` downloads that workbook, locates the gene **by name** (never by
row number), and maps the columns from the two header rows.

**ARHGEF15 (row 85, "GEF"): RhoA `+`, Rac1 `−`, Cdc42 `+`.**
Cited PMIDs on the row: 12775584, 23029280, 21029865, 27145964.

The screen assayed the **human** protein, not a rodent orthologue: Supplementary Table 1
row 56 records `Species in library = Human`, `size of construct = 841 aa` and cDNA
`BAA74938.3,AAH36749.1` — the same GenBank entries UniProt lists for O94989, at its full
length. That makes this a third direct measurement on the human protein, alongside
PMID:12775584 and PMID:23647072, and it is checked by a guard in
`muller2020_specificity.py` rather than assumed.

### Read-controls on the column mapping

The column mapping is not asserted, it is corroborated — by reading GEFs whose specificity
is textbook and checking they come out right:

| control | expected | screen says | recovered |
|---|---|---|---|
| TIAM1 | Rac1 | Rac1 | yes |
| ARHGEF1 / p115RhoGEF | RhoA | RhoA | yes |
| ARHGEF11 / PDZ-RhoGEF | RhoA | RhoA | yes |
| ARHGEF12 / LARG | RhoA | RhoA | yes |
| FGD1 | Cdc42 | Cdc42 | yes |
| **ITSN1** | Cdc42 | **nothing** | **no** |

ITSN1 is kept in the panel precisely because it fails. A textbook Cdc42 GEF scoring negative
for all three is the screen's own false-negative rate made visible, and it is the reason
**a `−` in this table is weak evidence while a `+` is a positive detection**. Dropping the
failing control would have hidden the caveat that governs how the ARHGEF15 row may be read —
so the Rac1 `−` should be read as "not detected here", not as "does not act on Rac1", even
though two other papers independently report no Rac1 activity.

The pass criterion was narrowed accordingly, from "every control recovers" to "each GTPase
column is corroborated by at least one control", because the former conflates a mapping
error with screen sensitivity. The self-test then proves the narrowed predicate still fails
when the three screen columns are rotated by one, so the narrowing did not open a hole.

### How this sits with the rest of the literature

| source | system | RhoA | Rac1 | Cdc42 |
|---|---|---|---|---|
| PMID:12775584 | human/rat VSMC | + | not reported | not reported |
| PMID:21029865 | mouse hippocampal neuron | + | − | − |
| PMID:23029280 | mouse retina EC / HUVEC | not reported | not reported | + |
| PMID:36929019 (via UniProt) | vascular, disease variants | + | − | − |
| **PMID:32203420** | **HEK293-based family-wide screen** | **+** | **−** | **+** |
| PMID:40138406 | mouse brain | + | not reported | + |

RhoA is unanimous. Rac1 is negative wherever tested. Cdc42 splits: positive in the
endothelial, family-screen and 2025 neuronal work, negative in the 2010 neuronal work and in
the disease paper. Two of the three Cdc42-positive results are in human cells or on the
human protein.

### Secondary readouts from the same workbook

Supplementary Table 3 (AP-MS interactome) gives ARHGEF15 eight GOLD-confidence preys, of
which **three are the ERM family** — EZR, MSN and RDX — each flagged `ActinbindingPrey =
ACTIN`. Supplementary Table 4 records the localization determined in that study as `actin`,
with the note "Enrichment on membrane ruffles, likely peripheral actin. Actin association
confirmed by Cytochalasin D assay. Plasma membrane localization in addition to peripheral
actin cannot be ruled out." Their Cell Atlas column for this gene reads `Plasma membrane`
at `Supported` confidence, which is the same evidence stream as GOA's `GO:0005886` HPA IDA
row. The construct is an overexpressed Citrine fusion and the authors hedge in their own
note, so this corroborates the existing plasma-membrane row rather than justifying a new
cortical-actin or ruffle annotation.

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
  the three assays on the human protein cited in the review.
- **Absence would not have been inactivity, and presence is not specificity.** The residues
  do not separate RhoA-GEFs from Cdc42-GEFs here, and the one substrate-selectivity switch
  that *is* experimentally established for this protein is not a DH residue at all but the
  phosphorylation state of Y361/Y353, which sits 60 residues N-terminal of the DH domain.

One tempting over-read has to be named and refused. Human Ephexin5 shares the discriminating
first residue (L) with FGD1 and ITSN1, and section 0 shows Müller et al. measured Cdc42
activity for ARHGEF15 and for FGD1. That is a single coincidence on a single column across
twelve proteins, in the *opposite* direction to the published interpretation of the same
residues, and the panel contains no design that would have detected it as signal. It is
recorded here only so that nobody later mistakes it for a prediction; nothing in the review
rests on it.

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

## 3. Claims about *other* genes, recorded as query results rather than asserted

The review says things about proteins that have no GOA file in this repository, so they
cannot be checked from the committed corpus: the comparator behind the `GO:0046875` MODIFY,
the evidence code and reference behind each PAINT seed's own annotation, and the donor rows
behind each ISS and Ensembl projection. `comparator_annotations.py` fetches each from QuickGO
and fails if the observed evidence code or reference does not match what the review claims,
so a wrong sentence breaks the script rather than sitting there looking specific.

**15/15 verified.**

| claim made in the review | QuickGO |
|---|---|
| NGEF/Ephexin1 carries `GO:0046875` — the comparator for the EPHA4 `MODIFY` | **IEA**, `GO_REF:0000107` (Ensembl projection from mouse Ngef, *not* experimental) |
| NGEF `GO:0005085` | EXP, PMID:15848799 |
| ARHGEF5 `GO:0005085` | IDA, PMID:15601624 |
| ARHGEF16 `GO:0005085` | IDA, PMID:20679435 |
| ARHGEF5 `GO:0032956` | IMP, PMID:14662653 |
| ARHGEF19 `GO:0032956` | IGI, PMID:20643356 |
| mouse Arhgef15 `GO:0005085` | IDA, PMID:21029865 |
| mouse Arhgef15 `GO:2000297` | IMP, PMID:21029865 |
| mouse Arhgef15 `GO:0030425` | IDA, PMID:21029865 |
| mouse Arhgef15 `GO:0098794` / `GO:0098978` / `GO:0150052` | IDA **and** IMP, PMID:28185854 |
| rat Arhgef15 `GO:0005737` / `GO:0051496` | IDA, PMID:12775584 |
| ARHGEF16 `GO:0032489` — the sibling that already sits on the Cdc42 BP term | IDA, PMID:21139582 |

The first row is the one worth reading twice. The comparator that justifies modifying the
EPHA4 row to `GO:0046875` is itself an **IEA projection from mouse Ngef**, not an
experimental annotation. That does not undermine the MODIFY — the ARHGEF15 evidence for
receptor coupling is the human IPI plus the phosphorylation mechanism in PMID:12775584, and
the comparator only shows the term is used this way for this protein family — but the review
now says "albeit by Ensembl projection from mouse Ngef rather than experimentally" rather
than leaving the reader to assume otherwise.
