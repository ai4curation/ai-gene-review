# ADPRHL1 bioinformatics

Two committed, self-testing scripts. Both exit non-zero on failure so they can gate a commit.

## `catalytic_site_census.py`

Answers the review's central question by measurement rather than by family name: **does
human ADPRHL1 (ARH2, Q8NDY3) retain the catalytic apparatus of its active paralogues?**

It takes UniProt's own annotated `Binding site` positions on ADPRH (P54922, 20 sites) and on
ADPRS/ARH3 (Q9NX46, 17 sites) as the reference sets — nothing is hand-assigned — maps them
through global pairwise alignments onto 17 family members, and scores each mapped residue
three ways: identity, BLOSUM62 class, and a mechanism-anchored `donor_group` test asking
whether the coordinating carboxylate or hydroxyl oxygen survives.

Controls, because a zero and a broken query look identical:

- **positive**, must score high: four ADPRH orthologues including *Dictyostelium* at 48.4%
  identity — an **identity-matched** control for ADPRHL1's 42.6–47.7%;
- **positive at low identity**: *R. rubrum* DraG (P14300), a characterised
  ADP-ribosylarginine hydrolase at 27.5%;
- **discriminating**: four ADPRS/ARH3 orthologues — active enzymes that sit further from
  ADPRH than ADPRHL1 does.

Two external checks reproduce published figures before anything else is reported: measured
identity 46.6% vs a published 46%, and 74.6% vs 75% (both `PMID:32726316`).

**Reproduction gate.** Before printing its own numbers it reproduces the sibling ADPRH
review's five-position panel (`origin/paint/ADPRH`) for the five accessions the two analyses
share, splitting the comparison into two channels: residue-and-position (objective; must
agree) and class label (a difference of *metric*, reported and explained, not absorbed).

```
python catalytic_site_census.py            # writes results.json + RESULTS.md, runs self-tests
git diff --exit-code RESULTS.md            # must be clean: the report is reproducible
```

`cache/` holds the raw UniProt JSON so a re-run is byte-reproducible and offline-safe.

## `audit_adprhl1_review.py`

Seven invariants on `../ADPRHL1-ai-review.yaml` that **no repo gate covers**, each written
for a defect this campaign has actually shipped:

| check | catches |
|---|---|
| A | duplicate YAML keys, which silently delete data *before* any parsed-tree gate runs |
| B | YAML anchors, which silently multiply one quote across N rows |
| C | every quote verbatim, including `provenance` and `knowledge_gaps[].provenance`, which `checkquotes.py` does not walk; plus a raw-vs-parsed count reconciliation |
| D | GOA rows vs reviewed rows, since the `fetch-gene` stub is known to collapse rows |
| E | `supporting_entities` and `propagation_review.source_entities` derived from the GOA WITH/FROM column, never hand-maintained |
| F | `core_functions` ↔ ACCEPT/NEW in **both** directions |
| G | prose contradicting its own `action`, keyed on `review.action` so wording drift cannot skip it |

```
python audit_adprhl1_review.py             # gate
python audit_adprhl1_review.py --self-test # break-test every check
```

The self-test mutates one residue, one token or one label at a time — a mutation coarse
enough to be caught by a much weaker implementation proves nothing about what the check
distinguishes. It also asserts the *happy* directions: an attributed cross-reference
("unlike the sarcomere rows, which are accepted…") must **not** fire check G, and the
committed file itself must be clean. Two real defects were found by running it: an
unanchored substring test in the census break-test that also matched sibling rows, and a
`KeyError` in check F that aborted check G on exactly the input check G exists to report.
