---
title: "IBA Annotation Quality Project"
maturity: MATURE
tags: [PIPELINE, FLAGSHIP]
species: [human, CANAL, MYCTU, VIBCH, SCHPO, ECOLI, mouse, rat, worm, yeast, ANOGA, POPTR, DANRE, DICDI, NEUCR]
genes:
  - cao-1
  - NQO2
  - Epe1
  - cds1
  - LPL1
  - UBA7
  - RIMBP2
  - arnF
  - DPYSL2
  - CRMP1
  - DPYSL3
  - AGO4
  - UBAC2
  - CAPG
  - CRYAA
  - BCL2
  - Bcl2
  - BCL2L1
  - EIF4E2
  - Aldh1l1
  - Hmgcs2
  - PEX2
  - AGK
  - AKTIP
  - DPYSL4
  - SAMD8
  - CPT1C
  - NTN1
  - NTN3
  - NOTCH1
  - IL23R
  - ABRAXAS1
  - PIWIL1
  - prg-1
  - wago-1
  - EIF2AK3
  - BIRC6
  - SSB2
  - SSZ1
  - BAIAP2L2
  - PIK3C3
  - SCGB1A1
  - rqh1
  - HDA1
  - TOLL9
  - ndhA
  - ndhD
  - ndhK
  - che-3
  - D7r2
  - D7r4
  - D7r5
  - D7L1
  - sta-2
  - fshr-1
  - opa1
  - eat-3
  - hsp-12.3
  - hsp-12.6
  - YAR1
  - ACL4
  - SIR3
  - lys-7
  - UBP3
  - CASP12
  - carD
  - rasC
  - pten
  - regA
  - pdsA
  - acgA
  - yakA
  - statA
  - statC
---

# IBA Annotation Quality Project

## Overview

> Project log, per-pass verification narrative, and lessons learned: [IBA_REVIEW/HISTORY.md](IBA_REVIEW/HISTORY.md).
>
> Consistency audit of the structured `propagation_review` blocks across all 1843 rows:
> [IBA_REVIEW/propagation-review-audit.md](IBA_REVIEW/propagation-review-audit.md).

This project examines the quality of IBA (Inferred from Biological Aspect of Ancestor) annotations discovered through AI-assisted gene review. IBA annotations use phylogenetic trees to transfer function from characterized proteins to uncharacterized orthologs.

While IBA is a powerful curation tool, it can produce problematic annotations when:
1. **Functional divergence** - Orthologs have evolved different functions
2. **Pseudo-enzymes** - Catalytic function lost despite domain retention
3. **Context-specific function** - Function differs between organisms/tissues
4. **Over-generalization** - Broad terms transferred when specific functions differ

This project covers **both directions** of IBA quality: most of the page catalogs
where IBA is *wrong* (over-annotation, patterns 1–15), while
[IBA Incompleteness](#iba-incompleteness-core-function-that-iba-fails-to-propagate)
quantifies where IBA *under-calls* established biology — 511 curated human core
molecular functions that IBA alone would miss.

## Propagation Taxonomy and Checklist

The patterns below are biological failure modes, but IBA review also needs a
root-cause call: is the source annotation bad, or is the propagation bad? Use the
same `review.propagation_review` structure as the
[ISO review project](ISO.md#failure-taxonomy): `root_cause`, optional
`failure_modes`, and per-source `source_entities` with short source-specific
comments.

### Root-cause classes

These are the schema values for `propagation_review.root_cause`.

| Code | IBA interpretation |
|---|---|
| `NO_FAILURE_CORE` | The ancestral/family inference is correct and core for the target. |
| `NO_FAILURE_NON_CORE` | The inference is defensible but contextual, secondary, or generic. |
| `SOURCE_BAD` | A seed/source annotation or family-node assertion is itself wrong, miscited, homonym-confused, or contradicted. |
| `SOURCE_STALE_OR_MISSING` | The transferred term no longer appears on the current source record, or the donor trace cannot recover it. |
| `SOURCE_WEAK_OR_INFERRED` | The source exists but is only inferred, statement-level, or otherwise weak for confident propagation. |
| `EVIDENCE_CIRCULAR_OR_REDUNDANT` | The chain transfers from another transfer, or the target already has stronger direct evidence. |
| `PROPAGATION_BAD` | The source biology is real, but the PANTHER node propagated it to the wrong target, subfamily, lineage, compartment, or role. |
| `TERM_SCOPING_PROBLEM` | The propagated biology is related, but the GO term is too broad, too specific, or has the wrong role/qualifier. |
| `UNRESOLVED` | The propagation issue was investigated but cannot yet be classified confidently. |

### Biological subtypes

These are the schema values for `propagation_review.failure_modes`.

| Code | IBA signal |
|---|---|
| `WRONG_ORTHOLOG_OR_PARALOG` | Donor/source is a paralog, expanded family member, or wrong subfamily. |
| `FUNCTIONAL_DIVERGENCE` | Target retained fold or orthology but changed substrate, product, activity, or pathway role. |
| `PSEUDO_OR_SUBACTIVITY_LOSS` | Catalytic residues or a specific sub-activity are lost even though the domain remains. |
| `CONTEXT_OR_TISSUE_MISMATCH` | Donor evidence is tissue, developmental, organismal, or disease-context specific. |
| `LINEAGE_OR_TAXON_MISMATCH` | Process does not occur in the target lineage or organelle system. |
| `COMPARTMENT_OR_COMPLEX_MISMATCH` | Localization, complex membership, or pathway compartment does not transfer. |
| `REGULATORY_SIGN_INVERSION` | Family contains activators and inhibitors, and a positive/negative regulatory term leaks across members. |
| `ROLE_CONFLATION` | Substrate, regulator, effector, or specificity subunit is annotated as the agent or core machinery. |
| `GRANULARITY_MISMATCH` | Parent term is true but uninformative, or child term overstates specificity. |
| `SOURCE_MISCITATION` | Source evidence points to the wrong gene, organism, publication, or homonym. |
| `SOURCE_EVIDENCE_WEAK` | Source evidence is inferred, statement-level, stale, or otherwise too weak for confident propagation. |
| `CIRCULAR_PROPAGATION` | Propagation chain depends on another propagated annotation rather than independent source evidence. |

### Source status values

These are the schema values for `propagation_review.source_entities[].source_status`.

| Code | Source-level interpretation |
|---|---|
| `SUPPORTS_TRANSFER` | Source evidence supports the term and the transfer to the target. |
| `SUPPORTS_SOURCE_BUT_NOT_TARGET` | Source evidence supports the source annotation, but propagation to the target is unsafe. |
| `SOURCE_BAD` | Source annotation or source citation is itself wrong. |
| `SOURCE_STALE_OR_MISSING` | Current source record no longer carries the transferred term, or tracing cannot recover it. |
| `SOURCE_WEAK_OR_INFERRED` | Source exists but is only inferred, statement-level, or otherwise weak. |
| `CIRCULAR_OR_REDUNDANT` | Source participates in a circular transfer chain or adds no independent support. |
| `NOT_RELEVANT` | Source was inspected but is not relevant to the target annotation. |
| `UNRESOLVED` | Source could not be classified confidently. |

### How many sources to enumerate

`source_entities` is a **curated subset, not an exhaustive mirror** of the row's
`WITH/FROM`. Enumerate the sources the review's argument actually rests on; where a
column carries dozens of donors, characterise the span in prose and name the ones that
matter. In mouse alone, `Mapk1 GO:0035556` has 53 donors, `Ccnb1 GO:0005634` has 45 and
`Egfr GO:0005886` has 67 — listing all of them is noise, not rigour, and it buries the
two or three that carry the reasoning.

The rule that does bind: **no sentence may claim more than the enumeration shows.**
A block that names one seed and calls it *"the* IBD seed" asserts a sole-donor fact the
`WITH/FROM` may contradict, and that is a defect regardless of how many sources are
listed. Definite singulars — "the IBD seed", "the sole donor", "the only seed" — must be
checked against the donor count before use; prefer "one of the IBD seeds" whenever more
than one gene-level donor exists.

Two traps when counting donors:

- The `PANTHER:PTN…` entry is the **node**, not a donor. A row whose `WITH/FROM` is
  `MGI:MGI:95407|PANTHER:PTN002571322` has exactly one donor, so "the IBD seed" is
  correct there.
- The same entity can appear twice under different identifiers — `RGD:2275` and
  `UniProtKB:P55213` are both rat caspase-3. Two entries, one donor.

Two mouse blocks were corrected under this rule, both by rewording the claim and adding
the co-donors: `Grpel2 GO:0051082` said "the IBD seed" while the row carries a human
GRPEL1 co-donor, and `Gulo GO:0016491` said the same while carrying seven gene donors
spanning fungi, plants and bacteria. Both now enumerate their full `WITH/FROM`.

### Resolving a donor before calling it unresolvable

`interpro/panther/<FAMILY>/<FAMILY>-entries.csv` is keyed on **UniProt accession** and
covers the whole family, not just `representative_members`. It gives the protein name,
gene symbol and source organism, so it resolves donors that a `grep` over `genes/` will
not:

```
$ grep '^P9WIT3,' interpro/panther/PTHR43762/PTHR43762-entries.csv
P9WIT3,"L-gulono-1,4-lactone dehydrogenase",protein,83332,
       Mycobacterium tuberculosis (strain ATCC 25618 / H37Rv),…,Rv1771,…
```

Check it before writing "the local index does not resolve this". The `CLAUDE.md`
restraint is *assert nothing you cannot establish* — not *assert nothing about UniProt
ids*, and a resolved donor usually strengthens the block's argument rather than being
mere bookkeeping. Note the limits: it is accession-keyed, so `FB:`/`SGD:`/`RGD:`/`MGI:`
identifiers are **not** lookups in it, and a family whose directory is absent from
`interpro/panther/` resolves nothing.

**A MOD-id seed can therefore only be name-matched, and a name match returns every
species' ortholog — so check the taxon column.** `PTHR10836` carries `Gapdh2` for
*D. melanogaster* (`P07487`), *D. pseudoobscura* (`O44104`) and *D. subobscura*
(`O44105`); matching on the gene name alone picks whichever comes first. A name match
corroborates that the family contains such a gene; it does not establish that the
`FB:`/`SGD:` id in the `WITH/FROM` **is** that entry. Say "corroborated", not
"resolved", when that is what happened.

In this corpus **"corroborated through the UniProt cross-reference for this MOD id
(ACC)"** is the standard phrasing for that situation: the family index confirms `ACC`
is the named protein, while the MOD-id-to-accession step is an inference rather than a
lookup. Reserve "resolved" for a step some file in the repository actually performs. And there
is a third state the substitution above can fall through: the family has no local directory
and the accession appears nowhere, so **nothing corroborates it either**. Say that
explicitly — "asserted from external knowledge, not corroborable here" — rather than
reaching for the weaker verb, which still implies a check that did not happen.

The mechanical test for which of the three verbs applies is **whether the family has a
directory under `interpro/panther/`** — check that before choosing the wording, not after.
That is what separates `Gulo` (index present, `P9WIT3` resolves to *M. tuberculosis*
Rv1771) from `Bcl2` (`PTHR11256`) and `Ednra` (`PTHR46099`), where no index exists at all
and so no amount of grepping can corroborate the MOD-id-to-accession step. A bare `grep`
for the accession is not a substitute: a hit may be an unnamed `ECO:0000250` or `WITH/FROM`
reference, or a substring collision with an EMBL id (`AAP97287.1` matches `P97287`), and a
miss tells you only that the repository is silent. Check the route, not the grep.

The middle verb has a worked example too, and it is the one place all three states
appear in a single claim. `genes/mouse/Bcl2` cites `Q64373` as mouse Bcl2l1: the
accession is **named in no cached record** (so "resolved" is unavailable), *and* the
identification is nonetheless **corroborated**, because `BCL2L1-goa.tsv` carries it as
the mouse-ortholog donor (`UniProtKB:Q64373|ensembl:ENSMUSP00000105445`) in the
`GO_REF:0000107` Ensembl-compara rows on human BCL2L1 — an orthology assertion is not a
name, but it establishes which gene the accession is. Note the route: an accession absent
from every `entries.csv` can still be corroborated by a **GOA `WITH/FROM` column in
another gene's file**, which is why "the family has no index" settles the first verb but
not the second.

Finally, do not assert the lookup in the same breath as disclaiming it. "The UniProt
cross-reference for this MOD id **points to** `ACC`" states the mapping as fact — which is
the step the sentence exists to say is uncheckable. Write "the accession `ACC` **is asserted
from** external knowledge" instead.

Universal quantifiers over a seed set need the same care as a definite singular:
"seeded entirely by X" or "every seed is an X" claims something about donors the block
may not have identified. Scope it — "every seed this review identified" — or name the
unidentified ones and say no claim is made about them.

### When a REMOVE overrules a curator, and when it does not

`CLAUDE.md` forbids using `REMOVE` on an experimental annotation (IDA/IMP/IPI/IGI/IEP/EXP)
just because the cached title or abstract is about a different gene — the full text the
curator read is usually not in `publications/`. Applying that across `genes/mouse` needed a
test sharper than "is the reason biological?", and the two ways of getting it wrong are both
on the record here.

**The condition, not the phrasing — but that is necessary, not sufficient.** A first pass
selected rows by matching phrases in the reason and missed a row whose immediate neighbour it
caught — same gene, same PMID, same evidence code, same argument, differing only in that one
said "The paper concerns" and the other "This physiology belongs to". Key on the condition
instead: an experimental evidence code, a cited PMID whose cache is
`full_text_available: false`, and a reason that turns on **what the paper contains or which
gene it studies**. That took the class from the 25 the phrase list found to 42.

The class is actually **48 rows across 17 genes**. The last six were routed into the *keep*
bucket because their shared reason cited biology — and it took reading each row's qualifier
to get them out. So the residual error does not live in the sweep; it lives in the triage of
what the sweep keeps, which is what the table below is for.

**Then ask whether the cited biology contradicts *this* annotation, given its qualifier and
aspect.** This is the step that separates a sound `REMOVE` from one that only sounds sound:

| Keep the `REMOVE` | Convert to `UNDECIDED` |
|---|---|
| `GO:0005515` protein binding — policy against the term, independent of any text | the reason asserts what the paper is about |
| the biology is stated **in the cached abstract itself** — Uox's abstract gives the enzyme's real reaction, which is what makes the deoxynucleoside-catabolism terms wrong | the reason turns on unread full text |
| the argument is about the gene's molecular identity — a protease that cleaves a CDK inhibitor is not one, so `GO:0004861` goes | the argument answers a claim the annotation does not make |

The last row is the trap. Six Bcl2 rows carried "…or describes an enzymatic/molecular
activity not enabled by Bcl2" — true of Bcl2, and irrelevant to every row it was applied to.
Four were qualified `acts_upstream_of_or_within`, which asserts **regulation**, not
catalysis; two were `located_in` cellular-component calls, which assert neither. **Read the
qualifier and the aspect before accepting that a biological argument bites.**

**A shared reason is suspicious only under a corrective action.** Reuse alone is not a
signal: a reason string whose rows span ≥3 distinct terms occurs in **201 groups** across
`genes/mouse`, up to 243 rows on one string. Where those groups sit is the whole point:

| action | groups | rows | largest |
|---|---:|---:|---:|
| `KEEP_AS_NON_CORE` | 83 | 2952 | 228 |
| `ACCEPT` | 60 | 1648 | 139 |
| `MARK_AS_OVER_ANNOTATED` | 30 | **587** | 202 |
| `MODIFY` | 14 | 108 | 18 |
| `REMOVE` | 10 | **93** | 23 |
| `UNDECIDED` | 3 | 21 | 9 |

(The scoped rows do not sum to 5432: qualification is per-scope, so a group can clear ≥3
terms overall and not within one action, or the reverse.)

Reproduce every figure here, as of the commit that ships the script
(`git log --oneline -1 -- projects/IBA_REVIEW/shared_reason_groups.py`):

```
python3 projects/IBA_REVIEW/shared_reason_groups.py
python3 projects/IBA_REVIEW/shared_reason_groups.py --action REMOVE --list
python3 projects/IBA_REVIEW/shared_reason_groups.py --action MARK_AS_OVER_ANNOTATED --list
```

**`REMOVE` is not the whole of "corrective", and scoping to it hid the larger half.** An
earlier revision of this paragraph reported only the `REMOVE` row — 10 groups over 93 —
and called the rest "nearly all `KEEP_AS_NON_CORE` or `ACCEPT`". `MARK_AS_OVER_ANNOTATED` is
corrective too, and carries **587 rows, six times as many**, with a single string on 202 of
them. "Nearly all" was also wrong on its own terms: `KEEP_AS_NON_CORE` and `ACCEPT` together
are 85% of scoped rows and 72% of groups, not nearly all.

The lesson is about operationalization, not arithmetic. The rule names a *property*
("corrective"); the measurement named *one action*; and because the narrower figure was the
one that made the point cleanly, nothing prompted a check that the two matched. When a rule
and its measurement are worded differently, the gap is where the finding hides.

The `REMOVE` breakdown, for reference, is Casp3 23; Ang2 18, 8, 4 and 3; Uox 12; Hsp90aa1 8;
Cyp1a1 7; Agtr1a 5; Ednra 5.

**A caveat that the `MARK_AS_OVER_ANNOTATED` figure does not settle.** The two actions are
not equally exposed to the objection. `REMOVE` withdraws an annotation, so its reason has to
carry a per-annotation verdict; `MARK_AS_OVER_ANNOTATED` withdraws nothing and records a
scoping judgement, where one class rationale across many terms is more often the honest
description. So the 587 is not 587 defects. But it is 587 rows the rule as stated reaches and
the measurement did not — and the second-largest group, `Bcl2`'s 35 rows over 19 terms on
*"this term is too indirect, broad, or mechanistically ambiguous"*, is a three-way disjunction
that never says which disjunct applies, which is exactly the shape dismantled under `REMOVE`
in that same file. (The largest, 202 rows, spans four genes on *"This overstates the direct
role of the gene product; the curated model…"* — a cross-file class rationale, and a different
question.) Measured and recorded here; not repaired, because doing it
properly is per-term work across 19 terms and this paragraph's own history is a warning
against opportunistic rewrites (see the Ang2 note below).

**That script exists because these figures had been wrong twice before it did**, the second
time in a way no reader could have caught. The published pair — 160 groups, and 7 over 63
under `REMOVE` — turned out to come from three mutually inconsistent predicates in a single
sentence: the `REMOVE` breakdown reproduces only with a ≥40-character minimum on the reason
string, the "177 rows" figure only with rows deduplicated by (file, term), and 160 reproduces
under neither. `grep`-able counts of a folded scalar need a parser, and a figure a reader
cannot reproduce does not go wrong quietly — it goes wrong invisibly. State the predicate,
ship the command, and quote no number you cannot re-run.

The length cutoff was not a harmless tuning choice either. It hid Ang2's three largest
`REMOVE` groups — 20, 8 and 4 rows on "No direct mouse evidence.", "Stale ISO transfer." and
"Do not stack inference on inference." — the most boilerplate-looking rows in the corpus and
exactly the ones the paragraph wants counted. So no minimum length is applied here, and
counting those 32 rows is what turned up the finding below.

### What the count is for: a pointer, not a verdict

All 32 are `ISO` or `IEA` — no experimental row among them — and inspection split them in two.
The question that separates them is **what the reason is about**:

- **12 rows** (8 + 4) shared one string in `reason` *and* one in `summary`, and are
  **legitimately** shared: "the current human source no longer carries this term", "the
  current human source is itself inferred-only (IBA)". Those are claims about the
  **transfer**, and one `GO_REF:0000119` transfer from one human source fails the same way
  for every term it carried. Restating it eight times would be duplication, not diligence.
- **20 rows** were the real defect, and not the one a shared string suggests. Their `reason`
  said only "No direct mouse evidence." — which is not an argument against an `ISO` at all,
  since transferred-without-mouse-data is precisely what `ISO` asserts. The row-specific
  material sat in `summary` ("Transferred heparin binding from human ANG, not shown for mouse
  Ang2"), which restates the same absence. So 20 corrective verdicts rested on a
  **tautology**, while the file's neighbouring rows carried the real argument — the functional
  divergence `PMID:8633065` documents. Those 20 now carry it (18 `ISO` rows share the
  transfer-level wording; the 2 `IEA` rows name the automated import instead). **No action
  changed**; what changed is that the reason now says something that could be wrong.

  And the first repair got the paper wrong, which is the part worth keeping. It said
  `PMID:8633065` showed Angrp "lacks Ang's angiogenic activity, **the one function directly
  compared**". The abstract compares three things: Angrp is not angiogenic; that is *not* a
  catalytic deficiency, because Angrp's ribonucleolytic activity toward tRNA is somewhat
  *greater* than Ang's; and an inability to bind cellular receptors is implicated, with poor
  conservation of the receptor recognition sequence 58-69. The middle finding is quoted as
  `supporting_text` **six times in the same file** — on four `ACCEPT`ed rows (`GO:0004540` as
  IBA, IEA and ISO, and the narrower `GO:0004549 tRNA-specific ribonuclease` as ISO), in
  `core_functions`, and in the `reference_review.findings` — so one document was
  simultaneously accepting that Angrp is the *better* RNase, on a *more specific* RNase term,
  and removing RNase-driven terms on the ground that it had lost activity. The reasons now
  state all three findings and rest on the receptor-binding defect, which is what actually
  blocks the receptor-mediated uptake that ANG's nuclear and stress-response biology depends
  on.

  Note where the right reading already lived: the file's own `references[].findings` for
  this PMID recorded all three results, including that the angiogenic loss is "attributed to
  defective cellular receptor binding rather than loss of RNase catalytic capacity" — while 20
  `reason` fields citing the same paper said otherwise. A `reference_review` is the curator's
  reading of the paper; when a `reason` citing that paper disagrees with it, the `reason` is
  the thing to check first.

  The `summary` fields were left as they are, deliberately. "Transferred heparin binding from
  human ANG, not shown for mouse Ang2" is an accurate *description* of the annotation and its
  status; it was only a defect while it was also the whole argument. Summary describes, reason
  argues — and conflating the two is what produced the tautology in the first place.

Note what the two groups have in common after the fix: the repaired reason is *also* one
shared string across 18 rows, and belongs there. Sharing was never the defect. A claim about
the term must be per-term; a claim about the source or the transfer covers every term that
transfer moved; and a claim that merely restates the evidence code is not a claim.

**`source_label` is perspectival, and the three-verb standard does not reach it.** The verbs
(*resolved* / *corroborated* / *asserted from external knowledge*) govern provenance claims in
prose, where the `comment` says how an identity was established. `source_label` is a readable
handle for the source *as it stands to this target* — the same role `preferred_term` plays
beside a PANTHER `term.label`, which `CLAUDE.md` already separates from the checked field.

That makes a cross-file consistency check on it actively wrong. Of **64 distinct MOD ids**
carrying a label in `genes/mouse` (89 labelled sources; MOD = `MGI`/`RGD`/`SGD`/`FB`/`WB`/
`ZFIN`/`TAIR`/`PomBase`/`dictyBase`/`CGD`/`Xenbase`), three are labelled differently in
different files, and all three are correct:

| id | in one file | in the other |
|---|---|---|
| `MGI:MGI:1346858` | `mouse Mapk1 (the review target itself)` | `mouse Mapk1 (ERK2, the target's closest paralog)` |
| `MGI:MGI:1346859` | `mouse Mapk3 (ERK1, the target's closest paralog)` | `mouse Mapk3 (the review target itself)` |
| `MGI:MGI:88316` | `mouse Ccne1 (cyclin E1)` | `mouse Ccne1 (this gene)` |

The **identity half agrees in all three**; only the relationship clause differs, because the
relationship differs. So check the symbol, leave the parenthetical alone.

Where to check it needs saying, because the obvious answer does not reach most rows. Only
**26 of those 89** labelled sources have a `comment` carrying a provenance verb; on the other
63 the comment is biological commentary ("A mammalian D-type cyclin seed at the same node")
and the symbol is asserted in the label alone, with nothing to check it against. So the rule
is not *check the label against the comment* — it is that **the symbol is an identity claim
wherever it is written**, and is owed the same standard there: establish it from the local
index (PAINT seeds, `*-entries.csv`, the GOA `WITH/FROM`) or write no label. A label whose
symbol you cannot establish is a reason to write no label, not to invent one; the
`SGD:S000004812` seed in `Ccnb1 GO:0005737` is cited by bare identifier for exactly that
reason, three lines below a labelled row whose comment makes no identity claim at all.

Every figure above comes from a parse of `propagation_review.source_entities`, not a `grep`:
159 of the 234 sources in `genes/mouse` carry a label, of which 89 are MOD-prefixed, and 26
of those 89 have a `comment` matching one of the three provenance verbs (*resolved* /
*corroborated* / *asserted from external knowledge*). An
earlier revision of this paragraph said 66 ids over 91 sources, which is the same sweep run
as *not-`UniProtKB`, not-`PANTHER`* — a filter that also admits the two `InterPro:` sources in
`Serpinh1`. Same finding either way; different set.

**A self-seed marks node membership always; it marks independent grounding only when the
target's own same-term annotation is itself retained.** `CLAUDE.md` glosses a self-seed as
"a marker that experimental grounding exists on the target itself", and that is the usual
case — but it presumes this review still stands behind that annotation. Where the target's
only same-term experimental row is one this review removes, the self-seed still shows the
target is inside the clade and `SUPPORTS_TRANSFER` is still right (`CIRCULAR_OR_REDUNDANT`
is forbidden for a self-seed), yet citing it as grounding leans on evidence the same file
rejects. Say node membership and say explicitly that grounding is not claimed. One block in
`genes/mouse` needed this — `Agtr1a GO:0006954`, whose own IGI at the term is `REMOVE`d on
full text that *is* available. Its comment asserted the canonical gloss until `9ce63aa88`, so
the block as it now stands is the corrected form, not the defect. The other twelve self-seed
claims cite annotations their files retain, so the canonical gloss holds for them.

**Finally, keep the row's own evidence pointing the same way as its verdict.** When an action
is withdrawn, the `summary` and the `supported_by` have to move with it; otherwise the block
asserts a conclusion its action has given up. Both have been missed here — 42 summaries that
still argued for removal, and six `supported_by` entries citing the very argument the new
reason withdrew. A `propagation_review` self-seed comment is the same hazard in another
place: do not cite, as the target's experimental grounding, an annotation this review
elsewhere removes. Of 13 such grounding claims in `genes/mouse`, one (`Agtr1a GO:0006954`)
did exactly that, until `9ce63aa88` rewrote it to the node-membership form above.

### What an IBA actually asserts, and two ways to misread the WITH/FROM

An IBA is not a similarity transfer from one gene to another. Behind every IBA is a
**PAINT curator's IBD** (Inferred from Biological aspect of Descendant): the curator
inspected the family tree and the multiple sequence alignment, read the experimental
annotations of *all* extant members, decided at which node the function arose — sometimes
recent, sometimes as deep as LUCA — and placed the assertion there. The IBA rows are then
the mechanical consequence of descent from that node. So an IBA carries a considered
phylogenetic judgment that no pairwise transfer does, and reviewing it means arguing with
that judgment, not with a similarity score.

Two corollaries, both of which are easy to get backwards:

**A small donor list does not mean weak support.** A node seeded by a single well-characterized
MOD or human gene can be perfectly strong, because the curator's claim is about where the
function arose, and they made that call with the whole alignment and the whole tree in view.
Counting donor genes is not a measure of evidential strength. If you want to challenge an IBA,
challenge the node placement — is the target inside or outside the clade that inherited the
function, and is there target-specific evidence of loss or divergence?

**The target appearing in its own `WITH/FROM` is correct and expected.** When a gene has its
own experimental annotation for the term, that annotation is one of the descendant evidences
the curator used to place the IBD, so the gene legitimately appears among the sources of the
IBA it later receives. This is **not** circular and **not** self-citation. It means the target's
own experimental data helped establish that the function is ancestral, and the IBA is then
saying something additional: that the function is inherited rather than lineage-specific.
Do **not** mark such a source `CIRCULAR_OR_REDUNDANT` and do not describe it as inflating
support.

`CIRCULAR_OR_REDUNDANT` is for genuine circularity — a propagation whose source is *itself*
a propagated annotation with no experimental grounding anywhere in the chain, or a source
that adds nothing because the target already has stronger direct evidence for the same claim.
Target-in-own-`WITH/FROM` is the opposite situation: it is a marker that experimental
grounding exists, and on the target itself.

Before a strong `REMOVE` on an IBA row, record that these checks were done:

- The GO term definition, aspect, qualifier, and taxon constraints were checked.
- The GOA `WITH/FROM` field was read and the PANTHER `PTN...` node and seed
  proteins were recorded.
- The target and seed proteins were placed in their PANTHER family/subfamily
  context. Cross-subfamily propagation is triage evidence, not a verdict.
- The source annotation or family-node assertion was checked separately from the
  propagation decision.
- Target-specific evidence was checked where relevant: direct experiments,
  curated `NOT` rows, active-site residues, domain architecture, localization,
  isoforms, organismal context, and lineage constraints.
- `review.reason` states the biological rationale, while
  `review.propagation_review` records the mechanical root cause, failure modes,
  and source entities.

## Slides

- [Slides](IBA_REVIEW/slides/IBA_REVIEW-slides.html) (Marp source: [IBA_REVIEW-slides.md](IBA_REVIEW/slides/IBA_REVIEW-slides.md)) — AI generated

## IBA Quality Issues

### 1. Pseudo-Enzyme Propagation

**The Problem**: Enzymatic activity transferred to proteins that have lost catalytic function.

**Example - Epe1 (S. pombe)**:
- IBA annotation: `GO:0032452` (histone demethylase activity)
- Source: Related JmjC domain proteins with characterized demethylase activity
- Reality: Epe1 has degenerate active site (HVD vs HXD), no detectable activity
- **Impact**: Misleading annotation propagated via phylogenetic inference

### 2. Ubiquitin-Like Modifier Specificity: IBA as a Positive Control

**The contrast**: UBA7 shows the opposite of an IBA failure. The IBA rows correctly
capture the conserved ISGylation pathway, while naive domain propagation and some
non-IBA annotations blur ISG15-specific E1 activity into generic ubiquitin-like or
ubiquitin terms.

**Example - UBA7 (human)**:
- Correct IBA annotations:
  - `GO:0019782` (ISG15 activating enzyme activity)
  - `GO:0032020` (ISG15-protein conjugation)
  - `GO:0045087` (innate immune response)
- Over-generic or wrong non-IBA rows:
  - `GO:0008641` (ubiquitin-like modifier activating enzyme activity) - `IEA`
    from InterPro2GO; technically related but too general.
  - `GO:0004842` (ubiquitin-protein transferase activity) and
    `GO:0016567` (protein ubiquitination) - non-IBA ubiquitin terms that should
    be redirected to ISG15 activation/conjugation.
- Reality: UBA7 specifically activates ISG15, not ubiquitin, in mammals.
- **Impact**: IBA provides a useful specific annotation that corrects the less
  discriminating domain/keyword propagation.

### 3. Substrate Specificity Transfer

**The Problem**: Specific substrate preference may differ between orthologs.

**Example - LPL1 (C. albicans)**:
- IBA annotation: `GO:0004622` (phosphatidylcholine lysophospholipase activity)
- Source: S. cerevisiae ortholog with characterized PC specificity
- Reality: Enzyme has broad specificity for ALL glycerophospholipids
- **Impact**: Over-specific annotation from ortholog doesn't capture full activity

### 4. Neo-Functionalization: Opposite Function in Subfamily

**The Problem**: When a subfamily undergoes neo-functionalization to catalyze the **opposite reaction**, IBA from the family root propagates the wrong function.

**Example - Cds1 (M. tuberculosis, V. cholerae) - PTHR10314 SF135**:
- IBA annotation: `GO:0019344` (cysteine biosynthetic process)
- Source: Root node (PTN000034104) of PTHR10314 family
- Reality: Cds1 catalyzes cysteine **CATABOLISM** (EC 4.4.1.1), the exact opposite!
- **Impact**: IBA propagates biosynthesis when the enzyme actually degrades cysteine to H2S + pyruvate

**Why this is severe**: The annotation isn't just wrong - it's **directionally opposite**. The enzyme produces H2S from cysteine degradation; the annotation says it synthesizes cysteine.

**Root Cause Analysis**:
| Evidence | SF135 (Cds1) | SF194/SF162 (Synthases) |
|----------|--------------|-------------------------|
| EC Number | **4.4.1.1** (lyase) | 2.5.1.47 (transferase) |
| Reaction | L-Cys → H2S + pyruvate | O-Ac-Ser + H2S → L-Cys |
| Branch length | **0.528** (longest) | 0.402-0.458 |
| Seq identity to synthases | **~24%** | 40-43% between each other |
| Active site motif | **ASSGST** | PTSGNTG |

The subfamily SF135 shares only 24% identity with synthases - less than synthases share with each other (43%). The longest branch length indicates maximum divergence and neo-functionalization.

### 5. Paralog/Secondary Activity Transfer

**The Problem**: A real activity in one paralog or source subfamily can be
promoted to a related but distinct target whose closest characterized comparator
supports a different substrate class. This should not be called
`KEEP_AS_NON_CORE` unless there is evidence the target actually has the activity
as a secondary function.

**Example - LPL1 (C. albicans)**:
- IBA annotation: `GO:0047372` (monoacylglycerol lipase activity)
- Source trace: `PANTHER:PTN000773837|SGD:S000003112`, corresponding to the
  S. cerevisiae ROG1 monoacylglycerol lipase source
- Closest characterized LPL1 comparator: S. cerevisiae LPL1, a lipid-droplet
  phospholipase B acting on glycerophospholipids
- **Action**: UNDECIDED for C. albicans LPL1 pending source-tree and substrate
  review; do not mark as non-core without evidence that Candida LPL1 hydrolyzes
  monoacylglycerols

### 6. Organism/Tissue Context Transfer

**The Problem**: Annotations derived from organism-specific experimental systems carry that context to orthologs where it doesn't apply.

**Example - RIMBP2 (human)**:
- IBA annotation: `GO:0007274` (neuromuscular synaptic transmission)
- Source: Drosophila ortholog (FB:FBgn0262483) where NMJ is the primary synapse model
- Reality: Human RIMBP2 functions mainly at CNS synapses (hippocampal, auditory)
- **Impact**: Term implies NMJ function when actual function is at central synapses
- **Root cause**: IBA quality limited by organism-specific biases in source annotations

### 7. Pseudo-Enzyme Propagation Is a Recurring Human Pattern

**The Problem**: The Epe1 pseudo-demethylase case is not isolated. Catalytic-residue loss with fold retention recurs across human families, and IBA repeatedly transfers the ancestral enzymatic activity to the catalytically dead member. These are the **most defensible** REMOVE calls, because the catalytic deficiency is independently documented in UniProt.

**Examples (REMOVE — each verified against the UniProt record, not just the review)**:
- **DPYSL2 / CRMP1 / DPYSL3** — `GO:0016812` (metallo-hydrolase activity, cyclic amides): the CRMP/dihydropyrimidinase-like proteins are explicitly flagged by UniProt CAUTION — *"Lacks most of the conserved residues that are essential for binding the metal cofactor and hence for dihydropyrimidinase activity."* **Confirmed first-hand by MSA** ([msa/RESULTS.md](IBA_REVIEW/msa/RESULTS.md)): aligned against active dihydropyrimidinase (DPYS), all five CRMP/DPYSL paralogs have lost the carbamylated catalytic Lys (K159→L/M/Q) plus multiple Zn-coordinating His/Asp. They are non-catalytic cytoskeletal regulators.
- **AGO4** — `GO:0004521` (RNA endonuclease activity): UniProt FUNCTION states directly that AGO4 *"Lacks endonuclease activity and does not appear to cleave target mRNAs"* — only AGO2 is the catalytic slicer in humans. **MSA confirms** ([msa/RESULTS.md](IBA_REVIEW/msa/RESULTS.md)) AGO4 carries two substitutions in the catalytic tetrad (D669G, H807R) vs intact AGO2; usefully, the same alignment shows AGO3 *retains* the tetrad, so the "non-slicer" story is residue-specific, not a blanket family claim.
- **UBAC2** — `GO:0004252` (serine-type endopeptidase activity): UBAC2 has a rhomboid-**like** fold (a known inactive-rhomboid/pseudoprotease clan) but UniProt attributes no protease function — its curated roles are as an ERAD/ER-phagy adaptor. **Now confirmed by MSA** ([msa/RESULTS.md](IBA_REVIEW/msa/RESULTS.md)): against active GlpG/RHBDL2/PARL, UBAC2 has lost *both* residues of the Ser-His catalytic dyad (S→L131, H→A183). *(This supersedes the earlier caveat that the residue loss was only inferred from the inactive-rhomboid classification.)*
- **AKTIP** — `GO:0061631` (ubiquitin-conjugating enzyme activity): UniProt CAUTION states it *"Lacks the conserved Cys residue necessary for ubiquitin-[conjugating]"* activity. It is in the E2 PANTHER family (PTHR24067) and the IBA is inferred from many genuine UBE2 enzymes, but as a UEV-domain protein it is a catalytically dead pseudo-E2 (a component of the FTS/Hook/FHIP complex). A second annotation even records the NOT form.
- **DPYSL4** — `GO:0016812`: a fourth CRMP-family member (Dihydropyrimidinase-related protein 4) carrying the same metallo-hydrolase IBA on the same basis as DPYSL2/3/CRMP1 — the whole CRMP/dihydropyrimidinase-*related* clade is non-catalytic (see the MSA above); only true dihydropyrimidinase (DPYS) retains the activity.
- **CASP12 (human)** — `GO:0004197` (cysteine-type endopeptidase activity): UniProt RecName is literally *"Inactive caspase-12."* Most humans carry a truncated, catalytically dead variant; the caspase-family protease IBA is over-propagated. **Note the mechanism is truncation, not site degeneracy** — MSA shows the full-length Csp12-L variant retains an intact His-Cys dyad and the canonical QACRG motif ([msa/RESULTS.md](IBA_REVIEW/msa/RESULTS.md)). The inactivity comes from a nonsense variant at codon 125 in the reference allele, upstream of the catalytic domain.
- **Serpinh1/HSP47 (mouse)** — `GO:0004867` (serine-type endopeptidase inhibitor activity): the textbook **non-inhibitory serpin** — UniProt describes a collagen-specific ER molecular chaperone (*"Collagen-binding protein"*), not a protease inhibitor. The serpin-fold IBA propagates inhibitory activity HSP47 does not have.
- **Lesson**: a degenerate/absent active site, **independently documented** (UniProt CAUTION/FUNCTION, an "Inactive"/non-inhibitory RecName, or — best — the missing catalytic residue seen in an MSA), is the strongest single signal that an enzymatic IBA is wrong. Residue-verified by alignment: Epe1 (Fe-ligand His370→Tyr, against its own KDM2A/KDM2B IBA donors), the CRMP family DPYSL2/3/4/CRMP1 (amidohydrolase), AGO4 and worm wago-4 (slicer), UBAC2 (protease), AKTIP (E2 ligase), ADGB (calpain), ADPRHL1 (ARH2), SEPHS1 (selenophosphate synthetase), CPS1 (GATase half-reaction), KDX1 (pseudokinase), SSZ1 (Hsp70 ATPase), cts2 (GH18 chitinase), PGRPLC (PGRP amidase), and *Arabidopsis* CRY1 (photolyase). HSP47 (protease inhibitor) rests on the non-inhibitory RecName.
- **Counter-lesson — check the mechanism, not just the conclusion.** A systematic residue pass over this pattern found **4 of 17 targets with a fully intact catalytic site**: CASP12 (truncation), LPA (blocked zymogen activation junction), AZIN1 (loses *substrate* contacts, keeps the catalytic Cys — while its paralog AZIN2 does the opposite), and HSPA13 (intact nucleotide site; the issue is the substrate-binding domain). Each conclusion survives, but the stated reason did not. "Lacks the catalytic residues" is cheap to assert and was wrong about a quarter of the time here — see [msa/RESULTS.md](IBA_REVIEW/msa/RESULTS.md).

### 8. Partial Sub-Activity Loss Within a Multidomain Family

**The Problem**: Distinct from full pseudo-enzymes — the protein **retains part of the ancestral activity but lost a specific sub-activity**, and IBA transfers the lost sub-activity.

**Examples (REMOVE — verified)**:
- **CAPG (human)** — `GO:0051014` (actin filament **severing**): CAPG caps but does **not** sever. The original characterization (cached PMID:1322908) states verbatim that CAPG *"reversibly blocks the barbed ends of actin filaments but does not sever preformed actin"*. The severing term over-extends from the gelsolin/villin family; CAPG retains capping only.
- **human/CRYAA** — `GO:0042026` (protein **refolding**): αA-crystallin is an ATP-independent **holdase** that prevents aggregation but cannot refold clients. This one is corroborated **inside GOA itself**: there is an explicit curated `NOT|involved_in` (ISS) annotation to GO:0042026, which the IBA directly contradicts. UniProt describes only aggregation-prevention chaperone activity, no refolding.
- **Worm small heat-shock proteins** — `GO:0042026` (protein refolding): a stronger version of the CRYAA case. hsp-16.2 is a holdase, not a foldase; and **hsp-12.3 / hsp-12.6 have *no* chaperone activity at all** — the title of PMID:9744800 is literally *"…Hsp12.2 and Hsp12.3 form tetramers and have no chaperone-like activity."* They are pseudo-sHSPs (tetramers/monomers rather than the large oligomers holdase function needs), so the family-level refolding IBA is fully refuted.
- **Lesson**: capping≠severing and holdase≠foldase are sub-activity distinctions that family-level IBA flattens. The CRYAA and hsp-12.3 cases are especially clean because a curator negated the term (CRYAA) or a paper demonstrated zero activity (hsp-12.3).

### 9. Regulatory-Sign Inversion Within a Family

**The Problem**: When a protein family contains members with **opposite regulatory signs** (activators vs inhibitors of the same process), a family-node IBA can transfer the wrong sign.

**Example - BCL2 (human and mouse)**:
- IBA annotation: `GO:0043065` (**positive** regulation of apoptotic process)
- Reality: BCL2 is the prototypical **anti-apoptotic** guardian; it inhibits MOMP and cytochrome c release (PMID:9027314, PMID:9219694).
- **Root cause (verified from GOA WITH/FROM)**: the IBA for GO:0043065 is inferred from a PANTHER node (PTN000135648) whose WITH/FROM list **mixes pro- and anti-apoptotic BCL2-family members** — pro-apoptotic BAX (Q07812) and BAK1 (Q16611) alongside anti-apoptotic members. The shared BH-domain fold unites activators and inhibitors of apoptosis under one family, so the "positive regulation" sign can leak onto BCL2.
- **Caveat (why this is "non-core" rather than flatly "wrong")**: BCL2 *does* have documented context-dependent pro-apoptotic behavior (e.g. caspase-cleaved BCL2), and GOA additionally carries a separate **NAS** annotation (PMID:14634621, ComplexPortal) to the very same GO:0043065. So the honest framing is that the *IBA family-node inference is unreliable for sign* (verified mechanism), not that positive regulation is impossible for BCL2. The companion review more confidently re-points related terms to their negative-regulation children (e.g. `GO:0001836` release of cytochrome c → `GO:0090201` *negative* regulation of release of cytochrome c).

### 10. Complex / Compartment / Pathway Membership Over-Transfer

**The Problem**: A family-level IBA asserts membership in a **specific complex, compartment, or pathway** that the target protein does not actually occupy, even though the catalytic fold or sequence homology is real. Compartment-split paralogs are the classic trap: they share a fold but route their product to different destinations.

**Examples (verified across multiple lines of evidence)**:
- **EIF4E2 (human)** — `GO:0016281` (eIF4F complex): 4EHP/EIF4E2 binds the cap but UniProt states it *"is unable to bind eIF4G"* and *"Does not interact with eIF4G"*; it is a translational repressor (4EHP-GYF2 complex), never an eIF4F subunit. A clear family-level over-transfer from EIF4E.
- **ALDH1L1 (rat)** — `GO:0005739` (mitochondrion): UniProt names it *Cytosolic 10-formyltetrahydrofolate dehydrogenase* with `SUBCELLULAR LOCATION: Cytoplasm, cytosol` and a cytosol IDA. Mitochondrial one-carbon oxidation is the job of the distinct paralog **ALDH1L2**.
- **HMGCS2 (rat)** — `GO:0010142` (farnesyl-PP biosynthesis, mevalonate pathway): a **paralog-pathway conflation**. The IBA comes from a PANTHER node (PTN000222418) that lumps the HMGCS paralogs. The cytosolic paralog **HMGCS1** feeds mevalonate→FPP→sterol/isoprenoid synthesis; mitochondrial HMGCS2's HMG-CoA is cleaved by HMG-CoA lyase to acetoacetate (ketogenesis). The shared HMG-CoA-synthase *reaction* is correctly classified under mevalonate biosynthesis (UniProt UniPathway tag), but assigning HMGCS2 to **FPP/isoprenoid** biosynthesis follows the wrong paralog's flux — an over-annotation. *(Nuance: the enzymatic step is real, so this is paralog over-annotation, not a fabricated activity.)*
- **PEX2 (human)** — `GO:0016593` (Cdc73/Paf1 complex): PEX2 is a peroxisomal RING E3 ligase for PEX5 retrotranslocation (UniProt) and has no role in RNA Pol II transcription elongation, so membership in the Cdc73/Paf1 complex is clearly wrong. *(Caveat: the cause is unconfirmed — the IBA WITH/FROM is a PANTHER node, not a PAF1 gene. A legacy synonym collision — PEX2's old name "PAF1"/Peroxisome Assembly Factor 1 vs the unrelated transcription factor PAF1 — is a plausible but unverified explanation.)*
- **CIRBP (human)** — `GO:0005681` (spliceosomal complex) + `GO:0000398` (mRNA splicing, via spliceosome): the cold-inducible RNA-binding protein CIRBP shares only the N-terminal RRM with the transformer-2/RBMX splicing factors that anchor these terms. PANTHER PAINT shows the splicing IBD sits at ancestral node **PTN000391532** (seeded by TRA2A, TRA2B, RBMX, *Drosophila* tra2, rat Tra2 — all bona fide splicing factors), while CIRBP's own subfamily node **PTN008729690** carries only `mRNA binding`. CIRBP has no experimental splicing evidence; its function is 3'-UTR binding, mRNA stabilization and translational control. A non-enzyme instance of complex-membership over-transfer across a functional-divergence boundary. *(See Featured Example and `families/PTHR48034/PTHR48034-review.md`.)*
- **Lesson**: complex membership, compartment, and downstream pathway are not conserved across paralogs even when the fold/reaction is; verify the protein actually occupies the annotated complex/compartment and that its product reaches the annotated pathway.

### 11. Substrate Over-Propagation From a Multi-Specificity Enzyme Family

**The Problem**: A PANTHER family lumps enzymes of **different substrate specificities**; a substrate-specific term is then propagated to a member that experimentally lacks that activity. Unlike LPL1 (a real but secondary/broader specificity), here the propagated activity is **absent** in the target.

**Example - AGK (human)** — `GO:0001729` (ceramide kinase), `GO:0046513`/`GO:0046512` (ceramide/sphingosine biosynthesis):
- AGK sits in PANTHER **PTHR12358**, which lumps "ACYLGLYCEROL KINASE" with "SPHINGOSINE KINASE." The ceramide-kinase IBA is propagated from a family node (Drosophila + mouse + node PTN008994514); the IEA/ISS variants both trace to one rodent ortholog (Q9ESW4).
- **Three independent lines refute the activity in human AGK**, outweighing the family inference:
  1. The direct human enzymology paper (the one UniProt itself cites): *"Significant phosphorylated products were only detected with monoacylglycerols and diacylglycerols as substrates, but not with any other lipid tested, including ceramide and sphingosine"* (PMID:15939762).
  2. A second study: *"No evidence for phosphorylation of ceramide by the recently described multiple lipid kinase was found"* (PMID:16269826).
  3. UniProt's own FUNCTION line states *"Does not phosphorylate sphingosine (PubMed:15939762)"*; its sole ceramide claim is a weak **"By similarity"** tag (propagated from Q9ESW4), not direct evidence.
- The dedicated ceramide kinase is the **separate** enzyme CERK. AGK's verified activity is MAG/DAG kinase (plus a kinase-independent TIM22 structural role).

**Example - SAMD8/SMSr (human)** — `GO:0033188` (sphingomyelin synthase activity):
- SAMD8 is in the sphingomyelin-synthase PANTHER family (PTHR21290), but UniProt's experimentally-supported FUNCTION says it makes **ceramide phosphoethanolamine (CPE)**, transferring a phospho**ethanolamine** head group from PE to ceramide — explicitly *not* the phospho**choline**-from-PC reaction that defines sphingomyelin synthases SMS1/SMS2: *"The larger PC prevents an efficient fit in the enzyme's catalytic pocket."* So the family-level sphingomyelin-synthase term is the wrong product/substrate; this is also accompanied by mislocalization IBAs (Golgi, plasma membrane) that belong to SMS1/SMS2, whereas SMSr is ER-retained.

**Example - CPT1C (human)** — `GO:0006631` (fatty acid metabolic process), `GO:0009437` (carnitine metabolic process):
- A **neofunctionalization** case: UniProt's RecName is literally *"Palmitoyl thioesterase CPT1C."* Although it sits in the carnitine O-acyltransferase family (PTHR22589) with CPT1A/B, experimental work shows CPT1C **lacks the canonical carnitine palmitoyltransferase activity** (it binds malonyl-CoA but does not catalyze carnitine-dependent acyl transfer). The IBA propagates the ancestral CPT1A/B fatty-acid/carnitine metabolism that CPT1C no longer performs.
**Example - cao-1 / CAO-1 (*Neurospora crassa*)** — `GO:0010436` (carotenoid dioxygenase activity), `GO:0016121` (carotene catabolic process):
- CAO-1 sits in PANTHER **PTHR10543** subfamily **SF89** (labelled *"carotenoid 9,10(9',10')-cleavage dioxygenase 1"*), a node that is functionally heterogeneous: it lumps genuine carotenoid cleavers (*Arabidopsis* CCD1, *Synechocystis* apocarotenoid oxygenase, *M. tuberculosis* Rv0654), **stilbenoid/resveratrol cleavers** (*U. maydis* RCO1, *Botrytis* rco1, and CAO-1 itself), and **phenylpropanoid cleavers** (*Pseudomonas* isoeugenol monooxygenase). The carotenoid-dioxygenase IBA propagates from node **`PTN001631894`**, whose `WITH/FROM` includes the *M. tuberculosis* carotenoid cleaver `UniProtKB:P9WPR5`.
- Direct experimental evidence **refutes carotenoid activity**: heterologously expressed CAO-1 did not convert β-carotene or any carotenoid/apocarotenoid tested, while it cleaves the interphenyl Cα–Cβ double bond of **resveratrol and piceatannol** (PMID:23893079). GOA already carries the corrective experimental **`NOT` carotenoid metabolic process** (GO:0016116, IDA, PMID:23893079). Crystal structures show the conserved four-His non-heme Fe(II) center but a **stilbenoid-adapted substrate cleft** (PMID:28493664).
- A **blinded OpenScientist** function-assignment run — given only the neutral hypothesis *"cao-1 has carotenoid dioxygenase activity"* — independently returned **"REFUTED (over-annotated)"** and likewise attributed the error to CCO/RPE65 (PTHR10543) family IBA, an independent confirmation of the manual call.
- **Positive-control paralog (the decisive contrast):** the *N. crassa* paralog **CAO-2 (A7UXI1, NCU11424)** carries the **identical** family IBAs — `GO:0010436` and `GO:0016121`, both from `GO_REF:0000033` — but for CAO-2 they are **correct**: CAO-2 is a genuine torulene dioxygenase (EC 1.13.11.59, KEGG KO K17842) and an integral step of the **carotenoid biosynthesis pathway** (KEGG `ncr00906`), whereas cao-1 (KO K28521) is mapped to **no pathway**. Same family term, same GO_REF, one genome — **right for one paralog, wrong for the other**, distinguishable only by target-specific experimental evidence (the direct assay + curated `NOT` on cao-1). The two sit in different PTHR10543 subfamilies (cao-1 SF89, cao-2 SF24) yet inherited the same ancestral carotenoid annotation.
- Action: **REMOVE** the carotenoid MF IBA; **MODIFY** the carotene-catabolic BP IBA to `GO:0046272` (stilbene catabolic process). The accurate MF (`GO:0016702` dioxygenase) is already present by IDA, and a class-level *stilbenoid α,β-dioxygenase activity* grouping term is proposed. `root_cause: PROPAGATION_BAD`, `failure_modes: [FUNCTIONAL_DIVERGENCE]`.

**Example - NQO2 (human)** — `GO:0003955` (NAD(P)H dehydrogenase (quinone) activity):
- NQO2 sits with NQO1 in the NAD(P)H:quinone oxidoreductase family (PANTHER **PTHR10204**). The family IBA transfers `GO:0003955`, which maps to **EC 1.6.5.2** and specifies **NAD(P)H** as the electron donor — but NQO2 characteristically **does not use NAD(P)H**; it uses **dihydronicotinamide riboside (NRH)** (PMID:10945627). The divergence here is in the **cofactor / co-substrate**, not the cleaved-substrate class or the fold.
- A **blinded OpenScientist** run (neutral hypothesis *"NQO2 has NAD(P)H dehydrogenase (quinone) activity"*) independently returned **over-annotated → the NAD(P)H term is substrate-incorrect**, citing Wu et al. 1997 (PMID:9367528) that NQO2 uses NRH "rather than NAD(P)H," and noting the correct term GO:0001512 is already annotated by IDA.
- Action: **MODIFY** to the NRH-specific `GO:0001512` (dihydronicotinamide riboside quinone reductase activity; **EC 1.10.5.1**, **RHEA:12364**), already supported by IDA. `root_cause: PROPAGATION_BAD`, `failure_modes: [FUNCTIONAL_DIVERGENCE]`.

- **Lesson**: a "By similarity"/propagated annotation is weak evidence; when direct experimental papers in the target species report the activity is **absent or different in product** (AGK no ceramide; SAMD8 makes CPE not SM; CPT1C is a thioesterase not a transferase; CAO-1 cleaves stilbenes not carotenoids; NQO2 uses NRH not NAD(P)H), the substrate/activity-specific IBA is an over-propagation. A family node that mixes substrate specificities (acylglycerol+sphingosine kinases; SM+CPE synthases; carotenoid+stilbenoid+phenylpropanoid cleavage oxygenases) leaks substrate terms across specificity boundaries — and the leak can be in the **cleaved substrate** (CAO-1) or the **cofactor/co-substrate** (NQO2). Where a subfamily label itself names one specificity (`PTHR10543:SF89` = "carotenoid … cleavage dioxygenase") while spanning several, that label is the mechanical origin of the leak.

### 12. Mis-Grouping Revealed by the WITH/FROM Column

**The Problem**: The IBA `WITH/FROM` field names the exact source proteins the function was transferred *from*. Reading it frequently reveals the error directly — the source is either the **wrong family entirely** or the **wrong paralog**. This is the single most useful diagnostic in this whole catalog.

**Tier A — wrong family / over-broad superfamily** (egregious; the source proteins are functionally unrelated):
- **NTN1 / NTN3 (human)** — `GO:0000981`/`GO:0006357`/`GO:0000978` (DNA-binding transcription-factor activity, Pol II transcription regulation, cis-regulatory DNA binding): Netrins are **secreted** axon-guidance cues (UniProt: extracellular; PANTHER PTHR10574 Netrin/Laminin) with no DNA-binding domain — yet they carry nuclear **POU-domain transcription-factor** IBAs. The WITH/FROM proves it: the source list is POU-domain TFs (POU2F1 P14859, POU1F1 P28069, POU4F1 Q12837, POU4F3 Q15319, …). A secreted protein cannot be a Pol II transcription factor; this is a phylogenetic grouping error.
- **NOTCH1 (human)** — `GO:0007411` (axon guidance): the WITH/FROM is **SLIT1/2/3** (O75093, O94813, O75094). NOTCH1 signals in neurogenesis but axon guidance is a SLIT function transferred across an over-broad node.
- **IL23R (human)** — `GO:0004925` (prolactin receptor activity), `GO:0017046` (peptide hormone binding): the WITH/FROM is **PRLR** (P16471). IL23R is a type-I cytokine receptor that binds the cytokine IL-23, not the hormone prolactin; the superfamily node is too broad.

**Tier B — wrong paralog** (subtle; the source is a close relative with a different function):
- **ABRAXAS1 (human)** — `GO:0090307`/`GO:0008608`/`GO:0008017` (mitotic spindle assembly, spindle–kinetochore attachment, microtubule binding): every one of these IBAs traces via WITH/FROM to **`UniProtKB:Q15018` = ABRAXAS2** (ABRO1, the BRISC-complex paralog). ABRAXAS1 is a nuclear BRCA1-A DNA-damage scaffold; the spindle/MT biology belongs to ABRAXAS2.
- **HINT2 (human)** — `GO:0005737` (cytoplasm): HINT2 has a mitochondrial targeting sequence and is mitochondrial; the cytoplasm term reflects the **HINT1** paralog.
- **CPT1C** (above) similarly inherits CPT1A/B metabolism it no longer performs.
- **opa1 (zebrafish) / eat-3 (worm)** — `GO:0016559` (peroxisome fission): both are UniProt *"Dynamin-like GTPase OPA1, mitochondrial"* inner-membrane **fusion** proteins. Peroxisome fission is done by the DRP1/DNM1L branch of the dynamin superfamily; the term is a within-superfamily mis-transfer (wrong organelle *and* wrong direction).
- **YAR1 (yeast)** — `GO:0045944` (positive regulation of transcription): YAR1 is an RPS3-binding 40S-ribosome-biogenesis factor (UniProt: interacts with RPS3), not a transcription activator; **ACL4 (yeast)** likewise gets mitochondrial-import terms by TOM70-family over-transfer despite being an Rpl4 chaperone.
- **Lesson**: **always read the WITH/FROM before flagging.** It tells you whether the IBA is a defensible family-level transfer or a traceable mis-grouping — and if a single paralog or out-of-family protein is the source, that is strong, near-mechanical evidence of error.

### 13. Generic / Mutually-Exclusive Compartment Over-Propagation

**The Problem**: Localization is one of the most frequently over-propagated IBA categories — but whether a flag is valid depends entirely on the **GO compartment hierarchy**, which makes this a two-sided pattern. Mutually-exclusive compartments are valid REMOVE grounds; broad *subsuming* terms are not.

**Tier A — valid REMOVE: a mutually-exclusive specific compartment on a protein that lives elsewhere.** `GO:0005634` nucleus is the one compartment the cytoplasm definition explicitly **excludes**, and plasma membrane / peroxisome / a specific organelle are likewise non-overlapping — so these are genuine errors:
- **Cytoplasmic PIWI/Argonaute & germ-granule proteins given `GO:0005634` nucleus** — PIWIL1 (human), and worm prg-1, wago-1, glh-1. All are cytoplasmic nuage/P-granule/chromatoid-body proteins (UniProt: cytoplasmic granule, no nucleus). The WITH/FROM nodes include **nuclear-acting Piwi orthologs** (e.g. *Drosophila* Piwi is nuclear; nuclear PIWIL4/MIWI2), so the nuclear compartment leaks onto the cytoplasmic members.
- **EIF2AK3/PERK → nucleus** (UniProt: ER membrane kinase) and **BIRC6 → nucleus** (UniProt: TGN/endosome/cytoskeleton/midbody — no nuclear pool).
- **Ribosome-associated chaperones SSB2 / SSZ1 (yeast) → `GO:0005886` plasma membrane** (UniProt: cytoplasmic, ribosome-associated) — PM propagated across the HSP70 family node.
- **BAIAP2L2 → `GO:0005654` nucleoplasm** (UniProt: plasma membrane / cell junction; I-BAR family) and **PIK3C3/VPS34 → `GO:0005777` peroxisome** (UniProt: autophagosome/endosome/midbody).
- **Inverse** — strictly **nuclear** proteins given `GO:0005737` cytoplasm: rqh1 (RecQ helicase) and HDA1 (HDAC) are nucleus-only, and nucleus is excluded from cytoplasm, so cytoplasm is wrong. And the genuinely **extracellular** SCGB1A1 given cytoplasm (secreted = outside the cell).

**Tier B — anti-pattern (do NOT flag; these reviewer REMOVEs were over-reaches).** `GO:0005737` cytoplasm **subsumes** mitochondrion, ER, Golgi, and lysosome (all `part_of` cytoplasm), so "cytoplasm" is defensible — if imprecise — for an organellar protein:
- "cytoplasm" REMOVE on **Aga / GLA** (lysosome), **DHCR24** (ER membrane, catalytic domain faces the cytosol), **ISCA1 / ATP5IF1 / gtpbp3** (mitochondrion) — all should be UNDECIDED/KEEP, not REMOVE.
- "membrane" (`GO:0016020`) REMOVE on **flvcr2a** is wrong — it is a multi-pass membrane transporter.
- **Self-correction**: HINT2's "cytoplasm" flag (added in the WITH/FROM pass) belongs here too — HINT2 is mitochondrial, but mitochondrion ⊂ cytoplasm, so cytoplasm is not strictly wrong; downgraded from the findings.

**Lesson**: before a localization REMOVE, place both compartments in the GO hierarchy. Mutually-exclusive (nucleus vs cytoplasm; PM vs internal; one organelle vs another) → valid. A broad subsuming term over a more specific true location (cytoplasm over any organelle; membrane over a membrane protein) → leave it.

### 14. Lineage-Inappropriate (Cross-Kingdom) Process Transfer

**The Problem**: Phylogenetic inference crosses kingdom/clade boundaries and lands a biological-process term on an organism where **the process does not exist** — or where the homolog was repurposed into a different system. The WITH/FROM typically names a vertebrate or *Drosophila* source. This is one of the largest and cleanest BP error classes.

**Examples (REMOVE — verified via UniProt + WITH/FROM):**
- **TOLL9 (mosquito, ANOGA)** — `GO:0006954` (inflammatory response): the IBA traces to **human TLR4 (O00206)** and other mammalian TLRs. Insects have Toll-pathway innate immunity but no vertebrate inflammation (no vasculature, immune-cell infiltration); the term is lineage-inappropriate.
- **ndhA / ndhD / ndhK (poplar, POPTR)** — `GO:0009060` (aerobic respiration): UniProt labels these *"NAD(P)H-quinone oxidoreductase, **chloroplastic**"* (`OG Plastid; Chloroplast`). They are photosynthetic plastid NDH subunits homologous to mitochondrial complex I — an **organelle-system swap**, not mitochondrial respiration.
- **che-3 (worm)** — `GO:0060294` (cilium movement involved in cell motility): che-3 is cytoplasmic **dynein-2** (retrograde IFT motor); *C. elegans* sensory cilia are **non-motile**. The motility term comes from axonemal-dynein orthologs in organisms with motile cilia.
- **D7 salivary proteins (mosquito, ANOGA: D7r2/D7r4/D7r5/D7L1)** — `GO:0007608` (sensory perception of smell): UniProt calls D7r4 a *"salivary protein… modulates blood feeding,"* female-saliva-specific. The OBP/PBP-GOBP fold was repurposed for binding biogenic amines/eicosanoids in saliva — these proteins are not expressed in antennae and have no olfactory role.
- **sta-2 (worm)** — `GO:0007259` (JAK-STAT signaling): transferred from fly/mammalian STATs, but *C. elegans* has **no JAK kinases**; STA-2 is activated via SNF-12/hemidesmosomes.
- **fshr-1 (worm)** — `GO:0009755` (hormone-mediated signaling): *C. elegans* lacks gonadotropins (FSH/LH/TSH); FSHR-1 functions in innate immunity/stress.
- **HEN1 (Arabidopsis)** — `GO:0034587` (piRNA processing): piRNAs are metazoan; plant HEN1 methylates miRNA/siRNA duplexes. Over-transfer from the metazoan HEN1/HENMT1 context.
- **Lesson**: check **taxon appropriateness** — does the process even occur in this lineage? GO taxon constraints catch some of these; the WITH/FROM naming a vertebrate/insect source is the tell. Watch especially for organelle-system swaps (plastid↔mitochondrion; cytoplasmic↔axonemal dynein).

### 15. Regulator / Effector and Direct / Downstream Conflation

**The Problem**: IBA (and curation generally) can blur the line between a **regulator or effector** of a process and the **core machinery**, or between a **downstream consequence** and the **direct function**.

**Examples (verified):**
- **lys-7 (worm)** — `GO:0007165` (signal transduction): LYS-7 is an antimicrobial **effector** whose expression is regulated *by* signaling; it is not itself a signaling component. (Same logical error as arnF's "response to iron" — see §arnF.)
- **SIR3 (yeast)** — `GO:0006270` (DNA replication initiation): SIR3 **represses** origin firing (negative regulation of MCM loading), the opposite of being part of the initiation machinery (ORC/CDC6/CDT1/MCM2-7).
- **UBP3 (yeast)** — `GO:0031647` (regulation of protein stability): a downstream *consequence* of its deubiquitinase activity (`GO:0004843`, the direct function), not a separate function.
- **sigF / sigG / sigK (*B. subtilis*)** — `GO:0003899` (DNA-directed RNA polymerase activity): these are **sigma initiation factors** (UniProt: *"initiation factors that promote…"* promoter recognition) — they confer promoter specificity to RNA polymerase but have **no catalytic polymerase activity**, which belongs to the core enzyme (RpoB/RpoC). A regulatory subunit assigned the **holoenzyme's** catalytic activity.
- **Lesson**: distinguish "does X" from "regulates/enables/results-in X." Effectors are not signal transducers; repressors are not part of the machinery they inhibit; a specificity subunit does not carry the catalytic activity of the complex it joins; downstream consequences are not direct molecular functions.

## Featured Examples

### Epe1 - Pseudo-Demethylase

**Species**: pombe
**Status**: COMPLETE

**IBA Annotations Flagged**:
| Term | Issue | Action |
|------|-------|--------|
| GO:0032452 histone demethylase activity | Pseudo-enzyme - no activity | REMOVE |
| GO:0006338 chromatin remodeling | Too broad | MODIFY |
| GO:0006357 regulation of transcription by RNA pol II | Valid | ACCEPT |
| GO:0003712 transcription coregulator activity | Valid | ACCEPT |

**Lesson**: IBA can propagate enzymatic activity to pseudo-enzymes that retain the domain fold but lack catalytic function.

### UBA7 - ISG15-Specific E1

**Species**: human
**Status**: COMPLETE

**Annotations reviewed**:
| Term | Issue | Action |
|------|-------|--------|
| GO:0005737 cytoplasm | IBA, correct | ACCEPT |
| GO:0019782 ISG15 activating enzyme activity | IBA, correct and specific | ACCEPT |
| GO:0032020 ISG15-protein conjugation | IBA, correct | ACCEPT |
| GO:0045087 innate immune response | IBA, correct | ACCEPT |
| GO:0006974 DNA damage response | IBA, correct | ACCEPT |
| GO:0008641 ubiquitin-like modifier activating enzyme activity | InterPro2GO IEA, too general | MODIFY to GO:0019782 |
| GO:0004842 ubiquitin-protein transferase activity | Non-IBA ubiquitin term, wrong activity class | MODIFY to GO:0019782 |
| GO:0016567 protein ubiquitination | UniPathway IEA, wrong modifier process | MODIFY to GO:0032020 |

**Lesson**: UBA7 should be highlighted as a positive-control case for IBA
specificity. The bad rows are not IBA propagation errors; they are generic or
ubiquitin-biased non-IBA mappings that the IBA annotations help correct.

### LPL1 - Phospholipase Specificity

**Species**: CANAL
**Status**: COMPLETE

**IBA Annotations Flagged**:
| Term | Issue | Action |
|------|-------|--------|
| GO:0006629 lipid metabolic process | Correct | ACCEPT |
| GO:0004622 PC lysophospholipase activity | Too narrow | MODIFY |
| GO:0005811 lipid droplet | Correct | ACCEPT |
| GO:0047372 monoacylglycerol lipase activity | ROG1-paralog/substrate-specificity transfer; target evidence absent | UNDECIDED |

### RIMBP2 - Context-Specific Term Transfer

**Species**: human
**Status**: COMPLETE
**PANTHER Family**: [PTHR14234](../interpro/panther/PTHR14234/) (RIM BINDING PROTEIN-RELATED)

**IBA Annotations Flagged**:
| Term | Issue | Action |
|------|-------|--------|
| GO:0007274 neuromuscular synaptic transmission | Wrong synapse type context | MODIFY |

**Lesson**: IBA transferred a term specific to *Drosophila* NMJ context to a human gene that functions primarily at CNS synapses. The IBA source (FB:FBgn0262483) is the fly ortholog where neuromuscular junctions are a major experimental system. However, human RIMBP2 functions at hippocampal (mossy fiber, CA3-CA1), auditory ribbon, and other central synapses - not primarily at neuromuscular junctions. This illustrates how IBA can propagate organism-specific or tissue-specific contexts that don't apply to the target species.

**Root Cause Analysis**: This is a case where **IBAs are only as good as the manual annotations on orthologs**. The Drosophila RIMBP ortholog is well-characterized at the NMJ because that's the major accessible synapse type in flies. When this annotation gets transferred to human via phylogenetic inference, it carries the fly-specific context with it.

**Family-Level Context**: The [PANTHER family analysis](../interpro/panther/PTHR14234/PTHR14234-deep-research-falcon.md) reveals additional IBA quality concerns:
- The representative structure (PDB 4z8a) is from *Drosophila* RIM-BP bound to Cacophony (fly NMJ Ca2+ channel)
- The family contains **functionally divergent subfamilies**:
  - RIMBP1/2 (SF18, SF20): Neuronal synaptic scaffolds
  - RIMBP3 (SF21): **Non-synaptic** - testis-specific, spermiogenesis/manchette function
- The family research explicitly warns: "Avoid propagating 'regulation of neurotransmitter release' to RIMBP3 paralogs"
- This demonstrates that IBA issues can affect entire subfamilies, not just individual genes

### arnF (PTHR30561) - Functional Divergence Within SMR Superfamily

**Species**: ECOLI (Escherichia coli K12)
**Status**: COMPLETE
**Family**: PTHR30561 (Small Multidrug Resistance / Drug-Metabolite Transporter superfamily)

**IBA Annotations Flagged**:
| Term | Issue | Action |
|------|-------|--------|
| GO:0022857 transmembrane transporter activity | Too generic; conflates drug efflux with lipid flipping | MODIFY → GO:0140303 |
| GO:0005886 plasma membrane | Correct | ACCEPT |
| GO:0055085 transmembrane transport | Acceptable broad term | ACCEPT |

**Lesson**: The PANTHER family PTHR30561 groups **four functionally distinct protein families** that share the SMR/DMT fold:
- **ArnE/ArnF** — undecaprenyl phosphate-L-Ara4N **flippases** (intramembrane lipid translocation)
- **EmrE** (P23895) — multidrug **efflux pump** (exports lipophilic cations)
- **MdtI/MdtJ** (P69210/P69212) — **spermidine export**
- **Gdx/SugE** (P69937) — **guanidinium export**
- **Mmr** (P9WGF1) — *M. tuberculosis* multidrug resistance

The IBA inference of "transmembrane transporter activity" comes from propagating annotations from these bona fide solute exporters (EmrE, MdtI/J, Gdx, Mmr) to ArnF. But ArnF does something mechanistically different: it **flips a lipid-linked sugar between membrane leaflets**, not export a solute across the membrane. The correct MF term is GO:0140303 (intramembrane lipid transporter activity).

**Why this is instructive**: Unlike the cds1 case (opposite reaction) or Epe1 (lost activity), arnF retains *transport* function — the IBA isn't wrong in kind, just wrong in specificity. The SMR superfamily is a case where sequence homology correctly identifies the structural fold (small multidrug resistance-like) but the functional annotation doesn't track the divergence from drug efflux to lipid flipping. This is a **moderate severity** issue because the parent term "transmembrane transporter" is not false, but it's misleading about mechanism.

**EcoCyc vs. IBA comparison**: EcoCyc contributed 5 annotations for arnF, including two "response to iron(III) ion" annotations (IGI from PMID:12139617, IEP from PMID:15322361) that were marked as over-annotated — they conflate transcriptional regulation of the arn operon by BasS-BasR with direct gene function. The IMP annotations from EcoCyc (carbohydrate derivative transport/transporter activity, plasma membrane IDA) are well-supported. The IBA annotations from GO_Central are reasonable at the superfamily level but miss the flippase specialization.

**Root Cause Analysis**:
| Feature | ArnE/ArnF | EmrE | MdtI/J | Gdx |
|---------|-----------|------|--------|-----|
| Function | Lipid flippase | Drug efflux | Spermidine export | Guanidinium export |
| Substrate | Lipid-linked sugar | Lipophilic cations | Spermidine | Guanidinium |
| Mechanism | Intramembrane flip | Transmembrane export | Transmembrane export | Transmembrane export |
| PANTHER SF | SF9 | (family-level) | SF6 | (family-level) |

### Cds1 (PTHR10314) - Neo-Functionalization (Opposite Reaction)

**Species**: MYCTU (Mycobacterium tuberculosis), VIBCH (Vibrio cholerae)
**Status**: COMPLETE
**Family**: PTHR10314 (Cysteine Synthase/Cystathionine Beta-Synthase)

**IBA Annotations Flagged**:
| Term | Issue | Action |
|------|-------|--------|
| GO:0019344 cysteine biosynthetic process | **Opposite function** - enzyme is catabolic | REMOVE |

**Lesson**: This is the most severe type of IBA error - the annotation isn't merely imprecise, it's **directionally wrong**. Cds1 (subfamily SF135) catalyzes cysteine **degradation** (EC 4.4.1.1), producing H2S + pyruvate from L-cysteine. The IBA annotation GO:0019344 says it participates in cysteine **biosynthesis** - the exact opposite reaction!

**Root Cause Analysis**:
1. GO:0019344 is annotated at the PANTHER family root node (PTN000034104)
2. Root annotation propagates to ALL descendants, including subfamily SF135 (Cds1)
3. SF135 underwent **neo-functionalization**: same fold, opposite reaction
4. Evidence of neo-functionalization:
   - Longest branch length (0.528) from root = most divergent
   - Different EC class: 4.4.1.1 (lyase/catabolism) vs 2.5.1.47 (transferase/biosynthesis)
   - Only 24% sequence identity with synthases (synthases share 40-43% with each other)
   - Distinct active site motif: ASSGST (Cds1) vs PTSGNTG (synthases)

**Experimental Evidence**:
- PMID:34439535 (M. tuberculosis): Cds1 produces H2S, pyruvate from cysteine; KM=11.26 mM, kcat=78.71/s
- PMID:34283874 (V. cholerae): VC1061/cds1 is principal enzyme for cysteine-derived H2S production

**Recommendation for PANTHER Curators**:
- Remove GO:0019344 propagation to SF135
- Add SF135-specific annotations: GO:0019450 (L-cysteine catabolic process to pyruvate), GO:0080146 (L-cysteine desulfhydrase activity)

See detailed family analysis: `interpro/panther/PTHR10314/PTHR10314-notes.md`

### CIRBP (PTHR48034) - Splicing Terms Over-Propagated to a Cold-Shock mRNA-Stability Subfamily

**Species**: human (Q14011); applies equally to the RBM3/CIRBP branch (mouse Cirbp P60824, RBM3, *Xenopus* cirbp-a)
**Status**: COMPLETE
**Family**: PTHR48034 (RNA-binding motif / RBM; InterPro IPR050441)

**IBA Annotations Flagged**:
| Term | Issue | Action |
|------|-------|--------|
| GO:0000398 mRNA splicing, via spliceosome | No splicing evidence for CIRBP; seeded by transformer-2/RBMX splicing factors | MARK_AS_OVER_ANNOTATED |
| GO:0005681 spliceosomal complex | CIRBP is not a spliceosome component; co-purification only | MARK_AS_OVER_ANNOTATED |

**Lesson**: PTHR48034 is a heterogeneous RRM family that lumps two functionally divergent groups sharing only the N-terminal RRM: (i) **transformer-2/RBMX/SR-type splicing regulators** (RS-domain C-terminus) and (ii) **cold-inducible mRNA-stability/translation proteins** CIRBP and RBM3 (glycine-rich/RGG C-terminus). The splicing terms are real for group (i) but were propagated across the divergence boundary into group (ii). This is the RNA-biology analogue of the arnF case — homology correctly identifies the fold, but the annotation does not track the functional split (pre-mRNA splicing → mRNA stabilization/translational control). CIRBP's verified activities are 3'-UTR binding (IDA: RPA2, TXN), mRNA stabilization, and translational control, with stress-granule recruitment — none of which is splicing.

**Root Cause Analysis** (PANTHER PAINT, `interpro/panther/PTHR48034/PTHR48034-paint.tsv`):
1. Splicing IBD is anchored at **internal node PTN000391532**, seeded *only* by splicing factors: `GO:0000398` from TRA2A (Q13595), TRA2B (P62995), *Drosophila* tra2 (FBgn0003742), rat Tra2 (RGD:1306751, RGD:1565256); `GO:0005681` from TRA2B (P62995), RBMX (P38159), rat Tra2 (RGD:1306751).
2. The node's annotations descend as IBA to **all** descendants, including the cold-shock branch.
3. CIRBP's own subfamily node **PTN008729690** carries only `GO:0003729` mRNA binding (and lists CIRBP, Q14011, as a seed) — the correct, generic call.
4. CIRBP's GOA WITH/FROM names the source node explicitly: `PANTHER:PTN000391532|...|UniProtKB:P62995|UniProtKB:Q13595` — a textbook case of mis-grouping revealed by the WITH/FROM column (pattern 12).
5. PAINT already prunes other branches of this family (node PTN001924395 carries IRD/NOT records blocking `GO:0003729`, `GO:0000381`, `GO:0016607`), so the gap is the absence of an equivalent pruning on the CIRBP/RBM3 branch.

**Seed (mod) genes verified as bona fide splicing factors** (no change needed):
- TRA2B (P62995): UniProt "participates in the control of pre-mRNA splicing"; direct IDA GO:0000398 (PMID:9546399); controls SMN2 exon 7 / MAPT exon 10. Falcon: "Belongs to the splicing factor SR family."
- TRA2A (Q13595), RBMX (P38159), *Drosophila* tra2 (P19018), rat Tra2b (P62997): all UniProt-confirmed pre-mRNA / alternative splicing regulators.

**Recommendation for PANTHER Curators**:
- Add an IRD/NOT (or restrictive re-annotation) for GO:0000398 and GO:0005681 on the CIRBP/RBM3 subfamily branch (node PTN008729690 and descendants), so the splicing terms stop descending to the cold-inducible mRNA-stability members.

See detailed family analysis: `families/PTHR48034/PTHR48034-review.md`

### DICDI cAMP / STAT developmental families — Stage-Specific Paralog & Lineage Over-Propagation

*Dictyostelium discoideum* development is driven by several **paralog families whose
members do the same molecular job at different developmental stages** (the cAMP
receptors cAR1–4, the adenylate cyclases ACA/ACG/ACR, the Ras GTPases RasC/RasG,
the STATs Dd-STATa/c). Reviewing one representative per family alongside its
sisters exposed IBA transferring a **family-node consensus onto the wrong member,
stage, compartment, or lineage** — the same failure classes catalogued above, now
in a social amoeba:

- **Stage/paralog leakage (`PROPAGATION_BAD` · `WRONG_ORTHOLOG_OR_PARALOG`).**
  The aggregation-stage "adenylate cyclase-activating cAMP receptor signaling"
  role (`GO:0007189`) is propagated by the cAR family node onto the *later*,
  lower-affinity receptor **cAR4/carD**, whose characterised output is the
  PTP/GSK3 axis, not adenylate-cyclase activation. Likewise **rasC** carries
  `GO:0000281` mitotic cytokinesis, but rasC-null cells divide normally — cytokinesis
  is **RasG's** job in this family.
- **Lineage-inappropriate process transfer (`LINEAGE_OR_TAXON_MISMATCH`).** The STAT
  family node **PTN000927860** transfers metazoan STAT roles — `GO:0006952` defense
  response and `GO:0042127` regulation of cell population proliferation — onto both
  **Dd-STATa** and **Dd-STATc** from all-metazoan seeds (human/mouse/rat/fly/worm
  STAT1/2/5…). This mirrors the existing worm `sta-2`/`fshr-1` cross-kingdom row.
- **Term-scoping across a lineage gap (`TERM_SCOPING_PROBLEM`).** Both Dictyostelium
  STATs are annotated `GO:0007259` "signaling via **JAK**-STAT", yet *Dictyostelium*
  has **no JAK** (they are activated by the TKL kinases Pyk2/Pyk3); the term is
  rescoped to `GO:0097696` STAT signaling.
- **Functional divergence with fold retained (`FUNCTIONAL_DIVERGENCE`).** **regA**
  inherits `GO:0047555` cGMP-phosphodiesterase activity from the cyclic-nucleotide
  PDE family node, but RegA is **cAMP-specific** (>200-fold selectivity). **yakA**
  (a dual-specificity DYRK) carries the family's generic `GO:0004713` protein
  **tyrosine** kinase activity.
- **Compartment mismatch (`COMPARTMENT_OR_COMPLEX_MISMATCH`).** **pten** inherits
  `GO:0005634` nucleus (a mammalian-PTEN behaviour) although all Dictyostelium
  evidence places it at the membrane/cortex/cytosol; **spiA** (a demonstrated
  spore-coat protein) inherits the canonical SCAMP `trans-Golgi`/`recycling
  endosome` localisations.

Each of these rows carries a structured `review.propagation_review`
(`root_cause` + `failure_modes` + the real GOA `WITH/FROM` PANTHER `PTN…` node
and a representative seed) in the corresponding
`genes/DICDI/<gene>/<gene>-ai-review.yaml`. Full module and paralog context:
[Dictyostelium Development Project](DICTYOSTELIUM_DEVELOPMENT.md).

> **Connection to pathway satisfiability.** The JAK-STAT case is the clearest
> instance of a broader, *automatable* rule. `GO:0007259` "signaling via
> **JAK**-STAT" names an obligate component — a Janus kinase — that the
> *Dictyostelium* genome does not encode (the Dd-STATs are activated by the TKL
> kinases Pyk2/Pyk3). Read as a boolean formula over required components under a
> **genome-content oracle**, the annotation is *unsatisfiable* and the IBA
> transfer is unsupportable — so it is rescoped to the JAK-independent parent
> `GO:0097696` STAT signaling. This is the signaling-domain analogue of the
> genome-content check in the
> [Pathway satisfiability project](PATHWAY_SATISFIABILITY.md): a process/pathway
> term whose definition entails a component **absent from the target's genome**
> is a candidate `LINEAGE_OR_TAXON_MISMATCH` over-propagation. A runnable
> prototype of exactly this check —
> [taxon-absent-component detector](PATHWAY_SATISFIABILITY/taxon_absent_component/README.md)
> — confirms JAK is genome-absent in *Dictyostelium* (`GO:0007259` unsatisfiable
> → `GO:0097696`). It uses **two oracles**: an InterPro domain signature and,
> primarily, **PANTHER family (`PTHR…`) membership** — the divergence-robust one,
> since IBA propagates along the PANTHER tree. That distinction matters: an
> InterPro-only screen falsely calls STAT and P2X *absent* in *Dictyostelium*
> (both diverged past their metazoan domain signature), whereas PANTHER correctly
> recovers the 4 Dd-STATs and the ~5 divergent P2X receptors — so the organism
> **does** have (ionotropic) P2X, and only the metabotropic **P2Y (GPCR)**
> component that `GO:0035589` specifically requires is genuinely absent. Even at
> HIGH confidence an `ABSENT` verdict is a strong lead for review, not an
> automatic `REMOVE`.

## Genes with IBA Issues

| Gene | Species | IBA Issue Type | Severity | Status |
|------|---------|----------------|----------|--------|
| Epe1 | pombe | Pseudo-enzyme propagation | HIGH | COMPLETE |
| cds1 | MYCTU, VIBCH | **Neo-functionalization (opposite reaction)** | **CRITICAL** | COMPLETE |
| LPL1 | CANAL | Substrate specificity | MEDIUM | COMPLETE |
| UBA7 | human | Positive control: IBA corrects generic/domain propagation | N/A | COMPLETE |
| RIMBP2 | human | Context-specific term transfer | MEDIUM | COMPLETE |
| arnF | ECOLI | Functional divergence within SMR superfamily | MEDIUM | COMPLETE |
| DPYSL2/CRMP1/DPYSL3 | human | Pseudo-enzyme (UniProt CAUTION: metallo-hydrolase residues absent) | HIGH | COMPLETE |
| AGO4 | human | Pseudo-enzyme (UniProt: lacks endonuclease activity) | HIGH | COMPLETE |
| UBAC2 | human | Pseudo-enzyme (rhomboid-like, no curated protease activity) | MEDIUM | COMPLETE |
| CAPG | human | Partial sub-activity loss (caps but does not sever actin; PMID:1322908) | MEDIUM | COMPLETE |
| CRYAA | human | Partial sub-activity loss (holdase not foldase; curated NOT(refolding)) | MEDIUM | COMPLETE |
| BCL2 | human, mouse | Regulatory-sign inversion (anti-apoptotic; family-node mixes pro-/anti-) | MEDIUM | COMPLETE |
| EIF4E2 | human | Complex over-transfer (UniProt: does not bind eIF4G, no eIF4F) | MEDIUM | COMPLETE |
| ALDH1L1 | rat | Compartment conflation (UniProt cytosolic; mito is ALDH1L2) | MEDIUM | COMPLETE |
| HMGCS2 | rat | Paralog-pathway over-annotation (ketogenic; FPP synthesis is HMGCS1) | MEDIUM | COMPLETE |
| PEX2 | human | Complex over-transfer (peroxisomal E3, not Cdc73/Paf1 complex) | MEDIUM | COMPLETE |
| AGK | human | Substrate over-propagation (no ceramide/sphingosine kinase activity; 2 papers) | MEDIUM | COMPLETE |
| cao-1 | NEUCR | Substrate over-propagation (cleaves stilbenes not carotenoids; PTHR10543:SF89 mixes specificities; blinded-confirmed) | MEDIUM | COMPLETE |
| NQO2 | human | Cofactor over-propagation (uses NRH not NAD(P)H; MODIFY to NRH:quinone reductase; blinded-confirmed) | MEDIUM | COMPLETE |
| AKTIP | human | Pseudo-enzyme (UniProt CAUTION: lacks catalytic Cys for E2 activity) | HIGH | COMPLETE |
| DPYSL4 | human | Pseudo-enzyme (CRMP-family metallo-hydrolase, non-catalytic) | HIGH | COMPLETE |
| SAMD8 | human | Substrate neofunctionalization (CPE synthase, not sphingomyelin synthase) | MEDIUM | COMPLETE |
| CPT1C | human | Neofunctionalization (palmitoyl thioesterase; lost carnitine transferase) | MEDIUM | COMPLETE |
| NTN1/NTN3 | human | Wrong-family grouping (secreted Netrin → POU-domain TF activity) | HIGH | COMPLETE |
| NOTCH1 | human | Wrong-source transfer (axon guidance from SLIT1-3) | MEDIUM | COMPLETE |
| IL23R | human | Over-broad superfamily (prolactin-receptor activity from PRLR) | MEDIUM | COMPLETE |
| ABRAXAS1 | human | Wrong-paralog (spindle/MT terms trace to ABRAXAS2) | MEDIUM | COMPLETE |
| PIWIL1 / prg-1 / wago-1 | human, worm | Nucleus on cytoplasmic PIWI/Argonaute (mutually-exclusive compartment) | MEDIUM | COMPLETE |
| EIF2AK3, BIRC6 | human | Nucleus on ER-membrane / TGN-cytoskeletal protein | MEDIUM | COMPLETE |
| SSB2 / SSZ1 | yeast | Plasma membrane on cytoplasmic ribosome-associated chaperone | LOW | COMPLETE |
| BAIAP2L2, PIK3C3 | human | Nucleoplasm / peroxisome on membrane / autophagy protein | LOW | COMPLETE |
| SCGB1A1 | human | Cytoplasm on a secreted (extracellular) protein | LOW | COMPLETE |
| rqh1, HDA1 | SCHPO, yeast | Cytoplasm on strictly nuclear proteins | LOW | COMPLETE |
| TOLL9 | ANOGA | Cross-kingdom: inflammatory response from vertebrate TLR4 | MEDIUM | COMPLETE |
| ndhA/ndhD/ndhK | POPTR | Organelle swap: chloroplast NDH annotated as mito respiration | MEDIUM | COMPLETE |
| che-3 | worm | Cross-lineage: cilium motility on non-motile sensory cilia (IFT dynein) | MEDIUM | COMPLETE |
| D7r2/D7r4/D7r5/D7L1 | ANOGA | Cross-function: smell perception on repurposed salivary OBP-fold | MEDIUM | COMPLETE |
| sta-2, fshr-1 | worm | Cross-kingdom: JAK-STAT / hormone signaling absent in nematodes | MEDIUM | COMPLETE |
| opa1, eat-3 | DANRE, worm | Mis-grouping: peroxisome fission on mito-fusion OPA1 | MEDIUM | COMPLETE |
| hsp-12.3/hsp-12.6 | worm | Pseudo-sHSP: refolding, but "no chaperone-like activity" (PMID:9744800) | HIGH | COMPLETE |
| YAR1, ACL4 | yeast | Family over-transfer (Rps3 biogenesis factor; Rpl4 chaperone) | LOW | COMPLETE |
| SIR3, lys-7, UBP3 | yeast, worm | Regulator/effector & downstream conflation | LOW | COMPLETE |
| CASP12 | human | Pseudo-enzyme (UniProt "Inactive caspase-12") | MEDIUM | COMPLETE |
| Serpinh1/HSP47 | mouse | Pseudo-inhibitor (non-inhibitory serpin; collagen chaperone) | MEDIUM | COMPLETE |
| sigF/sigG/sigK | BACSU | Subunit assigned holoenzyme catalytic activity (sigma ≠ RNA pol) | LOW | COMPLETE |
| CIRBP / RBM3 | human | Functional divergence within RRM family (splicing terms on cold-shock mRNA-stability subfamily; PTHR48034 node PTN000391532) | MEDIUM | COMPLETE |
| statA / statC | DICDI | Cross-kingdom: metazoan STAT defense/proliferation + JAK-STAT (no JAK in amoebae); node PTN000927860 | MEDIUM | COMPLETE |
| carD (cAR4) | DICDI | Stage-specific paralog: aggregation adenylate-cyclase-activating role leaked onto a late low-affinity cAMP receptor | MEDIUM | COMPLETE |
| rasC | DICDI | Wrong-paralog: mitotic cytokinesis (RasG's role; rasC-null divides normally) | MEDIUM | COMPLETE |
| regA | DICDI | Functional divergence: cGMP-PDE activity on a cAMP-specific phosphodiesterase | MEDIUM | COMPLETE |
| pten | DICDI | Compartment mismatch: nucleus on a membrane/cortex PtdIns(3,4,5)P3 phosphatase | LOW | COMPLETE |
| spiA | DICDI | Compartment mismatch: SCAMP TGN/recycling-endosome on a spore-coat protein | LOW | COMPLETE |
| acgA, pdsA, yakA | DICDI | Role/granularity conflation (peptide-receptor, neg-reg cAMP/PKA, generic Tyr-kinase) | LOW | COMPLETE |

## IBA Incompleteness: core function that IBA fails to propagate

All the patterns above concern IBA being *wrong* (over-annotation). The opposite
failure mode is just as real: IBA is frequently **incomplete** — it under-calls
well-established biology. Phylogenetic propagation is conservative by
construction (it only transfers what a curated ancestor already carries, at the
granularity the ancestor was annotated), so a great deal of experimentally
defined molecular function never reaches the leaf.

We quantified this with a generic **evidence-subtraction** tool
(`ai-gene-review subtraction-report`; see
[docs](https://ai4curation.io/ai-gene-review/subtraction_report/)). Running it in
"keep only IBA" mode over the 1015 reviewed human genes — i.e. asking *if IBA
were the sole evidence, what curated biology would we lose?* — and applying
ontology closure so that an IBA call to a **more general parent still counts** as
covering its ancestors:

- **62%** of annotation-grounded `core_functions` terms (4516 / 7278) would be
  lost if IBA were the only evidence.
- Restricting to **molecular function** and excluding low-information `binding`
  terms (GO:0005488, incl. `protein binding`): **511 curated core molecular
  functions across 423 genes** have **no IBA support at all**, **401** of them
  grounded by experimental/traceable evidence (IDA/IMP/IPI/EXP/TAS).

Because a term is only counted when it sits in a gene's `core_functions` — the
curator's distilled, highest-confidence judgement of what the protein *does* —
these are not annotation noise; they are the central activities a leaf-level
review would lose by trusting IBA alone. Two mechanisms recur:

### A. Activity absent from IBA entirely

The experimentally characterised activity is simply not propagated to the leaf —
no IBA annotation touches that branch — even though it is the protein's defining
biochemistry. These are clean, single-line losses (each verified: strong
non-IBA evidence, **zero** IBA at the term or any descendant):

| Gene | Core molecular function IBA misses | Evidence |
|------|-------------------------------------|----------|
| **USP21** | cysteine-type deubiquitinase activity (GO:0004843); deNEDDylase (GO:0019784) | IDA (PMID:10799498, PMID:32011234), IMP (PMID:26100909) |
| **P4HB** (PDI) | protein disulfide isomerase (GO:0003756); protein-disulfide reductase (GO:0015035) | EXP, IDA |
| **INPP5D** (SHIP1) | inositol-polyphosphate / PI(3,4,5)P3 5-phosphatase (GO:0004445, GO:0034485) | EXP, IDA |
| **FTH1** | ferroxidase activity (GO:0004322) | IMP |
| **PLD3** | single-stranded DNA 5′→3′ exonuclease (GO:0045145) | IDA |
| **NPM1** | histone chaperone activity (GO:0140713) | IDA |
| **PARK7** (DJ-1) | superoxide dismutase copper chaperone activity (GO:0016532) | IDA |
| **LRRK2** | GTPase activity (GO:0003924) | IDA |
| **SIRT2** | NAD-dependent demyristoylase (GO:0140773); tubulin deacetylase (GO:0042903) | IDA (PMID:25704306, PMID:32103017) |

### B. IBA stops at a general parent (true "too conservative")

Here IBA *does* annotate the gene with a broad term, but the experimentally
established **specific** activity — the exact substrate, regioselectivity, or
sub-activity — is never propagated. Closure confirms the IBA term is a strict
ancestor of the missed term, so this is genuine loss of resolution, not absence:

| Gene | IBA gives (general) | Experiment establishes (specific, IBA misses) |
|------|---------------------|------------------------------------------------|
| **HDAC6** | protein deacetylase (family) | tubulin deacetylase (GO:0042903); protein-lysine deacetylase (GO:0033558) — EXP/IDA/IMP |
| **SIRT2** | NAD-dependent deacetylase | histone **H4K16** deacetylase (GO:0046970) — IDA |
| **DPEP1** | (peptidase) | metallodipeptidase activity (GO:0070573) — IDA |
| **PARK7** (DJ-1) | (broader) | glyoxalase, glycolic-acid-forming (GO:1990422) — IDA |

**Caveat — IBA is not always the laggard.** Many of these genes are exceptionally
well studied; IBA legitimately covers their *canonical* function and only misses
secondary or recently characterised activities. **PTEN** is the clearest example:
its textbook PIP3 3-phosphatase activity (GO:0016314) *is* carried by IBA; what
IBA misses is the secondary protein-serine/threonine phosphatase (GO:0004722,
IDA PMID:9256433) and PI(3,4)P2 3-phosphatase (GO:0051800) activities. So
"incompleteness" should be read as *resolution and coverage gaps*, not as IBA
being useless — the same tool's forward direction shows IBA is the **sole**
support for 66 human core molecular functions (e.g. AKIRIN2 transcription
coregulator, GET1 protein-membrane adaptor, ATG14 PI3K regulator), so the two
analyses bound IBA's value from both sides.

**Reproduce:** `just subtraction-report-iba-conservative-core-mf` (writes
`reports/iba-too-conservative-core-mf.md`, the full ranked, evidence-enriched
table for all 423 genes); the raw keep-only TSVs come from
`just subtraction-report-iba-only-tsv`.

**Lesson for curators:** a leaf with only IBA annotations is very likely
*under*-annotated, not fully annotated. When IBA supplies only a broad
molecular-function term, treat it as a prompt to look for the specific
experimentally defined activity rather than as a finished call.

## Recommendations for IBA Curation

1. **Flag pseudo-enzyme candidates**: Proteins with enzyme domains but missing catalytic residues
2. **Flag neo-functionalized subfamilies**: Long branch lengths and different EC numbers indicate potential opposite function
3. **Validate substrate specificity**: Don't assume identical specificity across orthologs
4. **Distinguish core vs. secondary**: Mark promiscuous activities as non-core
5. **Prefer specific terms**: Replace generic IBA with specific terms when evidence exists
6. **Check for functional divergence**: Especially in rapidly evolving families
7. **Consider organism-specific biases**: Source annotations may reflect experimental systems (e.g., NMJ in flies) that don't apply to target species
8. **Validate annotations at family root**: Root-level annotations propagate everywhere - ensure they're truly universal to ALL subfamilies
9. **Synthesize multiple lines of evidence before flagging — never a single keyword**: a UniProt keyword (especially "By similarity"), a PANTHER node label, and a review assertion are each *individually* weak. Cross-check the term definition, direct experimental papers in the target species, the IBA WITH/FROM provenance, the MSA/active-site residues, and phylogenetic placement, and reason over the whole picture. The strongest REMOVE cases pair an explicit UniProt CAUTION/NOT with direct enzymology (DPYSL2, AGO4, CRYAA, AGK)
10. **Watch for opposite-sign family members**: When a family contains both activators and inhibitors (e.g., BCL2 family), a family-node IBA can transfer the wrong regulatory sign — inspect the WITH/FROM list for mixed members (but check whether independent non-IBA evidence also supports the term before calling it flatly wrong)
11. **Distinguish sub-activities**: capping vs severing, holdase vs foldase, slicing vs non-slicing — family-level IBA flattens these distinctions
12. **Don't inherit a paralog's compartment/complex**: family members share folds but not localization or complex membership — verify the protein actually occupies the annotated complex/compartment (EIF4E2, ALDH1L1, PEX2)
13. **Check the GO term's definition, not just its label, before calling an IBA directionally wrong**: e.g. "copper ion import" (GO:0015677) covers movement into a cell *or organelle*, so a Golgi-loading copper exporter can still satisfy it — a label that *looks* opposite may not be
14. **Read the WITH/FROM column first**: it names the exact source proteins. If they are the wrong family (NTN1←POU TFs; NOTCH1←SLITs) or a single wrong paralog (ABRAXAS1←ABRAXAS2; HINT2←HINT1), that is near-mechanical evidence of error. If they are a broad, coherent set of true orthologs, the transfer is probably defensible — slow down before flagging

## Quality Indicators

**Signs of problematic IBA**:
- Enzymatic activity for proteins with degenerate active sites
- **Long branch lengths from family root** (indicates divergence/neo-functionalization)
- **Different EC numbers between subfamilies** (may catalyze opposite reactions!)
- Generic terms when specific function is known
- Process annotations that don't match organism biology
- Multiple conflicting IBA annotations
- **Superfamily contains members with different transport mechanisms** (e.g., solute export vs lipid flipping in SMR family)
- **Enzymatic terms on proteins with a UniProt-documented degenerate/absent active site** (the strongest signal; e.g. DPYSL2, AGO4)
- **Family unites opposite-sign regulators** (activators + inhibitors of the same process; check WITH/FROM for mixed members — but confirm against non-IBA evidence)
- **Complex-membership or compartment terms on a protein whose paralog/relative occupies it instead** (cytosolic vs mitochondrial; eIF4F vs 4EHP repressor)

**NOT reliable grounds for flagging — verify with reasoning, not a single keyword**:
- A label that merely *looks* opposite — check the term **definition**. GO:0015677 "copper ion import" covers movement into a cell *or organelle*, so a Golgi-loading copper exporter (ATP7B) still satisfies it. (This is why ATP7B was **not** flagged.)
- A shared reaction that is *classified* under a pathway does not prove pathway membership in vivo — but it does mean the activity is real, so prefer "over-annotation/non-core" over "absent" (HMGCS2: the HMG-CoA-synthase step is genuine; only the FPP-pathway *flux* belongs to the other paralog).
- **Neither** a UniProt keyword **nor** a review assertion is sufficient on its own. Weigh all lines: a UniProt "By similarity" tag is weak and can be overturned by direct experimental papers (AGK: "ceramide By similarity" is refuted by two papers reporting no ceramide/sphingosine phosphorylation — so AGK *was* flagged); an explicit UniProt CAUTION or a curated NOT annotation is strong (DPYSL2, CRYAA).
- A broad **subsuming compartment** is not wrong just because a more specific location is known. `GO:0005737` cytoplasm includes mitochondrion, ER, Golgi, and lysosome (`part_of` cytoplasm), so "cytoplasm" is defensible for an organellar protein; only nucleus, plasma membrane, the extracellular space, or a *different* organelle are mutually exclusive enough to justify a localization REMOVE (see Pattern 13).

**Signs of reliable IBA**:
- Core metabolic enzymes with conserved mechanism
- Well-defined pathways with conserved components
- Structural proteins with conserved function
- Process/location terms that are organism-agnostic
- **Subfamilies with high sequence identity and same EC number**

---

## Project history & methodology

This page records the **synthesized findings**. The dated project log, the per-pass
verification narrative (what was added, what was retracted and why), and the
**lessons learned** are kept separately in [IBA_REVIEW/HISTORY.md](IBA_REVIEW/HISTORY.md).

A reproducible **multiple-sequence-alignment check** of the two central pseudo-enzyme
claims (Argonaute catalytic tetrad; CRMP/DPYSL metal-coordinating residues) lives in
[IBA_REVIEW/msa/](IBA_REVIEW/msa/RESULTS.md) — `uv run python catalytic_residue_msa.py`.
