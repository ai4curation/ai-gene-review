---
title: "ARBA00027234: search for additional phosphorylation demo candidates"
autolink_gene_symbols: false
---

# ARBA generic phosphorylation audit

**No defensible additions to the 48-gene demo shortlist from this screen.**
This is a focused candidate search, not a completed formal rule review.
Screened 2026-09-28 PDT / 2026-09-29 UTC.

## What was checked

[ARBA00027234](https://rest.uniprot.org/arba/ARBA00027234.json) predicts
`GO:0006468 protein phosphorylation` through 90 alternative condition sets.
Its current record is dated 2026-05-04. The
[saved rule](ARBA00027234.json) preserves the exact conditions.

Each condition set was translated into a UniProt search with AND between
conditions, OR within each condition's values, and its taxonomic constraints
retained. All 90 sets were queried against Swiss-Prot, both with and without
excluding `GO:0004672 protein kinase activity` and descendants. The searches
returned **370 distinct Swiss-Prot proteins, and zero lacking a positive
protein-kinase annotation**. All result sets were completely retrieved.
The [match table](reviewed-matches.tsv) records proteins and their matching
condition-set numbers. [audit.json](audit.json) contains the 180 query URLs,
counts, provenance checks, and the caution cases below.

The PANTHER subfamily condition (set 9) needs an exact quoted text search
for `PTHR11042:SF160`. An `xref:panther-"PTHR11042:SF160"` search returned
zero even though the exact-text query found 10 proteins. The corrected
query is used in the saved results. InterPro conditions use structured
cross-reference queries; FunFam conditions use exact quoted identifiers.

Absence of a kinase annotation is a screening criterion, not the only test
for error. The returned records were also searched for explicit inactivity
and pseudokinase cautions. Additional exploratory samples included unreviewed
matches of unusual-looking conditions: the PH-domain condition matched
ROCK/MRCK kinases; the paired PKN regulatory-domain condition matched PKN
kinases; the amphibian condition matched insulin/IGF receptors; bacterial
conditions matched histidine kinases or Wzc/Etk tyrosine kinases. These were
not convincing regulator/substrate mistakes. The unreviewed proteome was
not exhaustively screened, and this audit does not establish that the rule
is universally correct.

## Rule records versus emitted annotations

QuickGO queries with `withFrom=ARBA:ARBA00027234` returned **zero current
annotation rows**. The same was true for ARBA00026648, ARBA00026662,
ARBA00085084, and ARBA00088043. A positive control, ARBA00089890, returned
92 rows, including a current `GO_REF:0000117` IEA annotation explicitly
naming that rule. Requests and complete first-page responses are preserved
in `audit.json`.

Consequently, a rule record with a GO output is not sufficient evidence
that a particular protein currently carries an ARBA-derived assertion.
Domain-condition matches were not inserted into the demo's list of current
GOA annotations. These observations do not establish why the five rules
have no current rows in QuickGO, nor prove that they were never applied.

## Caution case: IRAK3, condition set 68

Set 68 requires these three FunFams together:

- `1.10.510.10:FF:000461`
- `1.10.533.10:FF:000055`
- `3.30.200.20:FF:000364`

It matches human [IRAK3/Q9Y616](https://www.uniprot.org/uniprotkb/Q9Y616/entry)
and mouse [Irak3/Q8K4B2](https://www.uniprot.org/uniprotkb/Q8K4B2/entry).
Both UniProt records explicitly flag replacement of the expected catalytic
Asp and disagreement about kinase activity. However, both also report low
autophosphorylation activity and carry experimentally supported kinase and
phosphorylation annotations: human PMID:10383454 and mouse PMID:12054681.
These are **disputed/nuanced candidates, not obvious errors**. No experimental
annotation has been rejected on the basis of the caution text. Human IRAK3
also already has repository reviews and is ineligible for the original demo.

Mouse Irak3 could be a separate future pseudokinase discussion case after
reading the conflicting studies. It is not counted as an ARBA-derived
misannotation or appended to the current shortlist.

## Reproduction

From the repository root:

```bash
python3 projects/PHOSPHORYLATION_REFACTOR/demo/arba-audit/scan_rule.py \
  --rule ARBA00027234 --output /tmp/phosphorylation-arba-recheck
```

This refetches the rule, reruns both Swiss-Prot searches for every condition
set, checks rule attribution in QuickGO with a positive control, and writes
fresh evidence to the chosen output directory. It fails on unknown condition
types or API errors rather than treating those failures as zero matches.
It never creates gene reviews or changes the demo candidate list.

[Back to the demo shortlist](../README.md)
