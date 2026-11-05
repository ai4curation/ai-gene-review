---
title: "InterPro2GO: GO:0019685 'dark reaction' read as 'light-independent'"
---

# InterPro2GO: GO:0019685 "dark reaction" read as "light-independent"

Back to the [project page](../CACAO.md). Reproduce with
`uv run python projects/CACAO/scripts/upstream_checks.py`; raw query output in
[`data/interpro2go-GO0019685-2026-11-01.tsv`](data/interpro2go-GO0019685-2026-11-01.tsv)
(the 3,731 annotation rows).

Found while reviewing the CACAO annotations on *Rhodobacter capsulatus*
[bchF](../../genes/RHOCB/bchF/bchF-ai-review.yaml), whose own CACAO row was
sound. The defective row on that gene was not CACAO's.

## The claim

`GO:0019685` is the carbon-fixation grouping term. Its `is_a` children are
`GO:0019253` reductive pentose-phosphate cycle (synonyms "Calvin cycle", "C3
photosynthesis"), `GO:0009760` C4 photosynthesis and `GO:0009761` CAM
photosynthesis, and its definition reads:

> A complex cycle of enzyme-mediated reactions which catalyzes the reduction of
> carbon dioxide to sugar. As well as carbon dioxide the cycle requires reducing
> power in the form of reduced nicotinamide adenine dinucleotide phosphate
> (NADP) and chemical energy in the form of adenosine triphosphate (ATP). The
> reduced NADP (NADPH) and ATP are produced by the 'light' reactions.

Four InterPro entries map to it, and all four are light-independent
(bacterio)chlorophyll biosynthesis families:

| Entry | Name | Proteins |
|---|---|---|
| IPR005969 | Light-independent protochlorophyllide reductase, B subunit | 1,039 |
| IPR005970 | Light-independent protochlorophyllide reductase, N subunit | 1,030 |
| IPR005971 | Light-independent protochlorophyllide reductase, iron-sulphur ATP-binding protein | 1,068 |
| IPR009905 | 2-vinyl bacteriochlorophyllide hydratase | 632 |

The first three are the subunits of dark-operative protochlorophyllide
oxidoreductase (BchB/N/L, ChlB/N/L); the fourth is BchF. None of them fixes
carbon. The mapping is explicable only as reading the term's label — "dark
reaction" — as a synonym for "light-independent", which is what the entry names
say.

The error is invisible to any ancestor or descendant check, because the term is
neither too broad nor too narrow for these families. It is a different pathway.

## Scale

`GO:0019685` carries **3,731 GOA annotations, and every one of them is IEA from
`GO_REF:0000002`, assigned by InterPro** — one reference, one assigning group.
The term has no use in GOA independent of this mapping. Every annotation GO
holds on carbon fixation's grouping term was produced by misreading its name.

## Requested change

**Delete the `GO:0019685` line from all four entries.** No replacement needs to
be chosen, because each entry already carries its correct terms beside the wrong
one:

```
IPR005969  GO:0016730 oxidoreductase activity, acting on iron-sulfur proteins as donors
IPR005969  GO:0015995 chlorophyll biosynthetic process
IPR005969  GO:0019685 photosynthesis, dark reaction            <-- remove
IPR005970  GO:0016730, GO:0015995                              (same pattern)
IPR005971  GO:0005524 ATP binding, GO:0016730, GO:0015995      (same pattern)
IPR009905  GO:0016836 hydro-lyase activity
IPR009905  GO:0030494 bacteriochlorophyll biosynthetic process
IPR009905  GO:0019685 photosynthesis, dark reaction            <-- remove
```

Deleting the four lines removes 3,731 wrong annotations and loses nothing.

Two optional refinements, lower priority and for a curator who knows the
families better than this review does:

- The three DPOR subunits could carry `GO:0016630` protochlorophyllide
  reductase activity, which is exact for all three regardless of organism and
  avoids the chlorophyll/bacteriochlorophyll split that makes a single BP
  mapping imprecise (`GO:0036068` light-independent chlorophyll biosynthetic
  process for ChlB/N/L against `GO:0036070` light-independent
  bacteriochlorophyll biosynthetic process for BchB/N/L).
- `IPR009905` is bacteriochlorophyll-specific, so `GO:0036070` would be more
  precise than the `GO:0030494` it already has. There is no MF term for the
  BchF reaction (EC 4.2.1.165); the bchF review files that as a separate
  `proposed_new_terms` request.

## Separate request to GO, on the term itself

Two problems with `GO:0019685` that this mapping exposes but does not cause.

**The label is obsolete and actively misleading.** "Dark reaction" was
abandoned in the field decades ago precisely because it suggests a reaction that
occurs in the dark rather than one that does not itself require light — and that
is exactly the misreading above. Suggest renaming to a carbon-fixation label and
keeping "photosynthesis, dark reaction" as an exact synonym, so that no future
pipeline can make the same inference from the primary name. The term dates to
2001-10-22 and its label has not been revisited since 2002-06-26.

**The definition describes only one of its children.** It is written as the
Calvin cycle specifically — CO2 to sugar via NADPH and ATP — while `GO:0009760`
C4 and `GO:0009761` CAM photosynthesis are also `is_a` children. The definition
should be generalised to the grouping the term actually is, or the term should be
restructured. Note that `GO:0019253`, the proper Calvin cycle term, is the one
carrying the "Calvin cycle" synonym and the MetaCyc `CALVIN-PWY` and
UniProtKB-KW `KW-0113` cross-references, and has 7,851 annotations of its own, so
there is no question of merging the two: `GO:0019685` is the parent, not a
duplicate.

## Status

- [ ] Report the four mapping deletions to InterPro.
- [ ] Report the label and definition problems to GO as a separate,
      lower-priority ontology request.
