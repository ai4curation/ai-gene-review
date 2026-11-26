# Rhea projections onto complex subunits: metric split and flag proposal

Follow-up to [SUBUNIT-PROJECTION.md](SUBUNIT-PROJECTION.md) and ai4curation/ai-gene-review#7071.
That page showed that UniProt's Rhea2GO projection (`GO_REF:0000116`) emits only `enables`, while
curators give some complex subunits `contributes_to`. This page answers the two questions left open:

1. How much of the curated-only disagreement in `consistency.py` is this subunit practice, and not
   disagreement about the activity?
2. Can a complex-membership condition reliably mark projected subunit rows as `contributes_to`
   candidates, and tell catalytic subunits from accessory ones?

**Bottom line.**

1. Subunit practice explains very little of the disagreement: at most 167 of 14,255 curated
   non-consistent pairs (1.2%) on a strict test. Even counting every weaker complex case, it is at
   most 10.4%. The disagreement is mostly partial reactions and sibling chemistries, as already
   described in [RHEA-SWISSPROT-COMPLETENESS](../RHEA-SWISSPROT-COMPLETENESS.md). The subunit effect
   sits on the *consistent* side instead. The metric cannot see the qualifier, so 678 pairs count as
   consistent only through a `contributes_to` row.
2. No complex-membership condition is reliable enough to change qualifiers.
   - The complex signals find almost every curated `contributes_to` pair, but only 7–17% of the
     flagged pairs that carry a curated row are `contributes_to`.
   - The best signal is PAINT having placed `contributes_to` for the term in the entry's PANTHER
     subfamily. It reaches about 60% precision (38% without IBA gold), which is good enough for a
     review queue but not for a rule.
   - The gold standard is itself inconsistent at catalytic subunits, which decides the question
     before any signal does. One PANTHER subfamily of COX1 orthologs carries 106 UniProt ISS
     `enables` rows and 66 UniProt ISS `contributes_to` rows for the same term.

## Data

The inputs were re-fetched on 2026-11-26 with `fetch_data.sh`, and GO mappings come from
go-ontology `go-edit.obo` at `2f2d73a`. The rerun reproduces the `SUBUNIT-PROJECTION.md` counts
exactly: 210,022 entries with a projected term, 1,228 collision pairs. `consistency.py` on the same
inputs gives 18.0% curated-only disagreement (65,100 consistent; 6,144 ancestor_only; 8,111
disjoint). The 2026-11-04 base gave about 17%; the difference comes from newer annotations, not from
a change in method.

**Positive controls.** Every class below is non-empty, so each test is able to return a hit. The
QuickGO join is checked directly: 75% of `contributes_to` rows on Swiss-Prot Rhea entries also
appear, without qualifier, in UniProt's GO cross-references.

## 1. Splitting the consistency metric

`subunit_consistency.py` repeats the curated-only classification. It then puts each
`ancestor_only` or `disjoint` pair into one sub-class, taking the first rule that matches:

| Sub-class | Rule |
|---|---|
| `subunit_ct` | the entry has a `contributes_to` row (QuickGO) on the mapped term or a descendant |
| `subunit_partner` | a same-organism Swiss-Prot entry carrying the same RHEA id is curated-consistent, sits in a **different PANTHER family**, and **shares a complex** with this entry (same ComplexPortal id, or same specific GO "complex" CC term) |
| `complex_only` | as `subunit_partner`, but with no shared complex recorded; the entry has only its own complex signal |
| `disagreement` | none of the above |

The PANTHER-family condition matters. Without it, the partner test caught catalytic paralogs that
share a complex, such as CDK8 (P49336) and IKBKE (Q14164), and inflated `subunit_partner` from 114
to 420. Generic CC terms (more than 10 `is_a` children, e.g. GO:0032991 protein-containing complex)
are ignored for the same reason.

Results (`subunit_consistency_summary.txt`; per-mapping counts in `subunit_consistency.tsv`):

| Curated sources only | Pairs | Share of non-consistent |
|---|---:|---:|
| consistent | 65,100 | |
| ... of which consistent **only** through a `contributes_to` row | 678 | |
| non-consistent (ancestor_only + disjoint) | 14,255 | 100% |
| `subunit_ct` | 53 | 0.4% |
| `subunit_partner` | 114 | 0.8% |
| `complex_only` | 1,312 | 9.2% |
| `disagreement` | 12,776 | 89.6% |

Setting aside `subunit_ct` and `subunit_partner` lowers the curated-only disagreement rate only from
18.0% to 17.8%.

**Where the 1,228 collision pairs land.** The collision pairs are those from `SUBUNIT-PROJECTION.md`,
where the projection says `enables` and a curator says `contributes_to`. Because the metric cannot
see the qualifier, a collision pair can add to disagreement only through `disjoint` or
`ancestor_only`, where the entry's curated rows hold a different, often subunit-level, activity.
Joining per-entry classes (`consistency_entries.tsv`, in the data directory) to
`subunit_projection.tsv`:

| Curated class | Collision pairs | Effect on the metric |
|---|---:|---|
| consistent | 665 | the `contributes_to` row is read as agreement |
| none | 528 | outside the denominator |
| disjoint | 19 | counted as disagreement |
| ancestor_only | 16 | counted as disagreement |

So the collisions add only 35 pairs to disagreement (0.25% of the 14,255), led by anthranilate
synthase (7). The 528 `none` pairs reveal a second input defect. UniProt's GO cross-references show
one evidence code per term, and on 511 of these pairs the curated `contributes_to` row, mostly PAINT
IBA, appears only under an IEA code (UniRule 359, EC 144). The curated-only metric therefore drops
it. A qualifier-aware metric fed from GOA/QuickGO rows would fix both defects.

**Spot-check of `subunit_partner`.** The class is mixed, so 167 is an upper bound.

- Real subunit cases: anthranilate synthase component 2 (TrpG), and the subunits of heteromeric
  ENaC, NMDA, nicotinic and GABA-A channels. In each, the channel activity is annotated on a
  partner.
- Not subunit cases: RNA helicases under ATP hydrolysis, and histone acetyltransferases (KAT2A,
  CREBBP) under protein propionyltransferase. These are partial-reaction or sibling-specificity
  cases in which a partner happens to share a complex.

**Proposal for question 1.**

- Keep the headline metric as it is, and add the sub-class counts as diagnostic columns
  (`subunit_consistency.tsv`).
- Report the 678 qualifier-blind consistent pairs next to it. They are the real subunit effect on
  this metric: the input drops the qualifier, so "consistent" includes subunits that curators record
  only as contributing.
- To make the metric qualifier-aware, read the qualifier from GOA (GPAD or QuickGO) instead of
  UniProt's cross-references. That changes the input source, so it is left for a separate decision.

## 2. Flagging projected subunit rows

`subunit_flag_eval.py` scores candidate signals on every projected (entry, term) pair (240,641). The
gold standard is curated rows on the projected term or a descendant:

- CT means the entry has a `contributes_to` row;
- EN means it has a curated row with no `contributes_to`.

Pairs with no curated row (187,309) are unlabelled.

| Signal | Flagged | CT | EN | Precision | Recall | Precision, no IBA |
|---|---:|---:|---:|---:|---:|---:|
| ComplexPortal xref | 2,150 | 246 | 1,334 | 15.6% | 17.6% | 14.2% |
| specific GO "complex" CC term | 18,262 | 1,156 | 5,662 | 17.0% | 82.5% | 12.9% |
| heteromeric SUBUNIT note | 33,759 | 1,117 | 9,685 | 10.3% | 79.7% | 7.2% |
| any of the three | 39,635 | 1,321 | 11,372 | 10.4% | 94.3% | 7.0% |
| PAINT `contributes_to` in the PANTHER subfamily | 4,924 | 907 | 589 | 60.6% | 64.7% | 38.2% |
| no ACT_SITE feature | 146,452 | 1,194 | 29,737 | 3.9% | 85.2% | 2.7% |
| name says subunit/component/chain | 29,927 | 1,140 | 4,177 | 21.4% | 81.4% | 13.8% |
| complex & no ACT_SITE & subunit name | 12,868 | 930 | 2,362 | 28.3% | 66.4% | 18.5% |
| every projected pair (baseline) | 240,641 | 1,401 | 51,931 | 2.6% | 100% | 1.8% |

The "no IBA" column drops IBA rows from both labels. Most CT rows are PAINT IBA, and the PAINT signal
is derived from PAINT, so that column is the fairer test of it. The CT count here (1,401) is a little
higher than the 1,228 in `SUBUNIT-PROJECTION.md` because descendants are resolved with the go-basic
closure.

### Spot-checks (`subunit_flag_spotcheck.tsv`, seven model organisms)

- **Cytochrome-c oxidase.** Swiss-Prot puts the reaction only on the catalytic core, COX1, COX2 and
  COX3. The nuclear subunits do not carry it, so they are not projected. All the human and yeast core
  subunits are CT. This is the [OXPHOS](../../OXPHOS.md) convention: even catalytic subunits only
  contribute to the complex activity. The orthologs are split, however. Human COX3 (P00414) has a
  PAINT `contributes_to` and a UniProt ISS `enables` for GO:0004129. Across the COX1 subfamily
  PTHR10422:SF18, UniProt's own ISS rows give 106 `enables` and 66 `contributes_to`. No membership
  signal can reproduce a split that the curation itself makes inconsistently.
- **RNA polymerase.**
  - The catalytic subunits are labelled inconsistently: yeast RPB1, RPB2, RPA190 and RPC1 are CT,
    while human RPB1, RPA1 and RPC1 are EN.
  - The truly accessory subunits are E. coli α (rpoA, P0A7Z4) and ω (rpoZ, P0A800). Swiss-Prot puts
    the RNA polymerase reaction on both, and QuickGO shows a RHEA `enables GO:0034062` row on each.
  - These two are the clearest projection errors in the set. Yet they have no curated row on the
    term, so the gold standard cannot score them. PAINT has no `contributes_to` for their families,
    so the best signal misses them too.
- **Glutamine amidotransferases.** Practice varies by enzyme:
  - E. coli and yeast CarA/CarB are CT for the overall glutamine-dependent carbamoyl-phosphate
    synthase activity, and E. coli CarA is EN for glutaminase.
  - E. coli HisH/HisF are both EN for imidazoleglycerol-phosphate synthase.
  - TrpE (component 1) is EN for anthranilate synthase; the TrpG-containing proteins are CT.
  - GatB is CT in human and EN in yeast.
  - Each partner carries out one half-reaction of the overall activity, so the right relation for
    the overall term is a convention. Membership cannot decide it.

### Convention check

Among 5,960 (PANTHER subfamily, projected term) groups with at least two labelled members, with IBA
excluded:

- 5,829 are all EN;
- 25 are all CT;
- 106 are mixed.

The mixed groups are led by the COX1, COX2 and COX3 subfamilies, then ATP synthase subunit a,
complex I chain 5, the succinate dehydrogenase flavoprotein and the ribonucleotide reductase large
chain. Where curators use
`contributes_to` at all, they often do so inconsistently across orthologs.

### Proposal for question 2

1. **Do not convert projected rows automatically.** No condition separates catalytic from accessory
   subunits well. Complex signals have high recall but precision of about 10%. Missing active-site
   features say nothing, because metal and heme centres are recorded as binding sites. The gold
   standard is inconsistent wherever it matters most.
2. **Flag a review queue in two tiers,** without asserting anything:
   - *Tier A, PAINT disagrees:* projected `enables` rows where PAINT has placed `contributes_to`
     for the term in the entry's PANTHER subfamily. That is 4,924 pairs at about 60% precision; the
     rest are mainly the convention split above.
   - *Tier B, complex member with no curated decision:* projected rows on entries with a complex
     signal and no curated row on the term (about 27,000 pairs). The accessory-subunit errors such
     as rpoA and rpoZ live here, and nothing measured here can rank them yet.
3. **Settle the catalytic-subunit convention first.** For complex-level reaction terms on catalytic
   subunits, the choice is between `enables` (e.g. human RPB1 and RPC1, and part of UniProt's ISS
   rows) and `contributes_to` (OXPHOS, PAINT for these families, yeast RNA polymerase). Until that is
   decided, flagging catalytic subunits only moves disagreement around. Accessory subunits that
   carry a complex reaction are a narrower and less contested target. They could be found by
   curating, per complex class, which subunit families are non-catalytic, which is what
   [Protein Complex Functions](../../PROTEIN_COMPLEX_FUNCTIONS.md) aims at.

### Why this is not a `rules/curated/` rule

- A `CuratedRule` assigns GO terms. `RuleGOAnnotation` has no qualifier slot, so a rule cannot say
  "emit `contributes_to` instead of `enables`".
- `CuratedRuleConditionTypeEnum` has no complex-membership condition type, so ComplexPortal, GO CC
  and SUBUNIT text cannot be conditions. PANTHER can, so a tier-A rule would be expressible if the
  schema gained a qualifier.
- That would be a schema change, and given the numbers above it would not yet be justified.

A sketch of what a tier-A rule would look like is below. It is not a valid record and is not
committed as one.

```yaml
# Not valid against the current schema: RuleGOAnnotation has no `qualifier`.
id: CR-nnnn
status: PROPOSED
condition_sets:
- number: 1
  conditions:
  - condition_type: PANTHER
    value: PTHR10422:SF18       # COX1 orthologs; one set per subfamily where PAINT places contributes_to
go_annotations:
- go_id: GO:0004129
  go_label: cytochrome-c oxidase activity
  aspect: molecular_function
  qualifier: contributes_to     # proposed slot
replaces:
- source_type: OTHER
  source_id: GO_REF:0000116     # Rhea2GO projection, for entries in these subfamilies only
  consequent: GO:0004129
```

## Limits

- The EN gold mixes deliberate `enables` on catalytic subunits with possible over-annotation of
  accessory ones. Precision against it is therefore a measure of agreement with current curation,
  not of correctness, and a `contributes_to` row can be wrong too.
- The unlabelled pairs (78% of the projection) include exactly the accessory-subunit errors this
  work is after, and no signal here was scored on them.
- The SUBUNIT-note regex is coarse. It matches some homomers whose note says "complex".
- PANTHER assignments come from UniProt's cross-references, which use the current release.

## Related projects

- [Protein Complex Functions](../../PROTEIN_COMPLEX_FUNCTIONS.md): the decision framework for
  which subunits enable a complex activity and which contribute. The convention split above is its
  "catalytic or functional subcomplex" row seen in GOA.
- [OXPHOS](../../OXPHOS.md): its convention is that catalytic subunits also only contribute to the
  complex activity. Cytochrome-c oxidase is the largest mixed group here.
- [Complex Portal](../../COMPLEXPORTAL.md): ComplexPortal copies BP and CC terms to subunits but not
  MF. As a signal it has the lowest recall (18%).
- [Over-annotation patterns](../../OVER_ANNOTATION_PATTERNS.md), pattern 8: catalytic function
  assigned to non-catalytic complex subunits. rpoA and rpoZ are instances of it produced by the
  Rhea projection.
- The `ROLE_CONFLATION` pattern in [IBA review](../../IBA_REVIEW.md). Here PAINT is on the
  conservative side: its `contributes_to` placements are the most precise signal available.
- The prediction-review error type `COMPLEX_ACTIVITY_TRANSFER`
  (`src/ai_gene_review/schema/gene_review.yaml`) names the same failure for predictions. A
  projected subunit row is a deterministic instance of it.

## Files

| File | Content |
|---|---|
| `subunit_consistency.py` | sub-classes for the curated-only non-consistent pairs; per-entry classes (`consistency_entries.tsv`, data directory only) and the collision-pair breakdown |
| `subunit_consistency_summary.txt`, `subunit_consistency.tsv` | its summary and per-mapping counts |
| `subunit_flag_eval.py` | signal precision and recall against curated qualifiers, and the convention check |
| `subunit_flag_eval_summary.txt`, `subunit_flag_spotcheck.tsv` | its summary and the spot-check families in seven model organisms |
