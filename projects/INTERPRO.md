---
title: "InterPro Mapping Review Project"
collections: [HOMOLOGY_PROPAGATION, FUNCTION_PREDICTION, MAPPINGS]
maturity: IN_PROGRESS
tags: [PIPELINE]
sidecars:
  slide_charts:
    - INTERPRO/slides/interpro-pipeline.svg
    - INTERPRO/slides/interpro-review-actions.svg
manifest:
  slides:
    - href: INTERPRO/slides/INTERPRO-slides.html
      description: AI generated; figures predate the 2026-11 refresh
  artifacts:
    - href: https://claude.ai/artifact/NaAEVgdB1TnJUKnBWWt69N
      title: Project brief
index_group: CROSS_CUTTING
---

# InterPro Mapping Review Project

**Bottom line:** InterPro2GO (GO_REF:0000002) attaches GO terms to every protein
that matches an InterPro entry, so a term that holds for only some members of a
family is copied onto all of them. We harvested every InterPro2GO annotation our
gene reviews had already judged (3,652 records on 1,706 genes, joined to 1,826
source entries), ranked the entries by how often reviewers flagged them, and ran
family-level deep research on the top of that list. The result so far is a set of
66 rows across 38 entries: 25 removals (for example ATP binding and protein
phosphorylation on the protein kinase domain, IPR000719), 25 proposals to narrow or
qualify a mapping, and 16 endorsements. Those three sum to the 66, and each is a count
over `projects/INTERPRO/interpro2go.sssom.yaml` rather than a figure maintained by
hand: a removal is `skos:exactMatch` with `predicate_modifier: Not`, a narrowing is
`skos:broadMatch`, and an endorsement is an unmodified `skos:exactMatch`. Re-derive
them from the file rather than editing this sentence, because the previous version of
it said 36 across fifteen and stayed self-consistent while the set nearly doubled. These are
proposals for InterPro curators, not changes InterPro has adopted, and the
lower-ranked part of the worklist is not yet assessed.

We did this because a wrong InterPro2GO mapping is a single error that repeats
across every matched gene, so one fix at the mapping level is worth many
gene-level corrections. Gene reviews also catch mappings the ranked worklist
never reaches: three entries came from reading human genes one at
a time, and three more from auditing the bacterial export ATPases FliI and SctN
(see [conserved-function recovery](CONSERVED_FUNCTION_RECOVERY.md)).

**Start here:** [Proposed mapping edits](INTERPRO/interpro2go.sssom.yaml) ·
[Prioritized entry worklist](INTERPRO/interpro_family_priorities.tsv) ·
[Gene-level evidence and reasons](INTERPRO/suspect_interpro_mappings.tsv)

## Findings and proposed curation actions

The [mapping set](INTERPRO/interpro2go.sssom.yaml) records the individual GO terms,
verdicts, and rationales. The following summarizes its recommendations; family-level
research proposals still require checking against the entry's membership and
experimental evidence.

| InterPro entry | Finding in the family assessment | Proposed action |
|----------------|----------------------------------|-----------------|
| IPR000719 — Protein kinase domain | Pseudokinase members challenge the assumption that every domain match binds ATP and phosphorylates proteins. | Remove the blanket ATP-binding and protein-phosphorylation mappings; assess narrower catalytic entries. |
| IPR001128 — Cytochrome P450 | The assessment supports cofactor-binding mappings but questions uniform catalytic assignments across functionally diverse members. | Retain the binding mappings; review the scope of monooxygenase and oxidoreductase mappings. |
| IPR001424 — Cu/Zn superoxide dismutase domain | Copper-chaperone members make the domain-wide superoxide-metabolism assignment too broad, while fungal Cu-only SODs show the term still needs cover outside the canonical Cu/Zn SOD rule. | Remove the blanket process mapping and request process-term cover on both the Cu/Zn SOD UniRule and a fungal Cu-only SOD rule or narrower entry; assess metal binding separately. |
| IPR000276 — Rhodopsin-like GPCRs | The assessment flags atypical receptors as exceptions to canonical G-protein coupling. | Review receptor-activity and signaling mappings at subfamily level, verifying evidence for the proposed exceptions. |
| IPR001046 — NRAMP / SLC11 | The assessment supports broad metal-transport terms rather than substrate-specific assignments across the entry. | Retain broad transport mappings; evaluate more specific functions on individual members. |
| IPR012724 — Chaperone DnaJ | The assessment attributes ATP binding to the Hsp70 partner rather than DnaJ. | Remove the ATP-binding mapping; retain protein folding and review the scope of the heat-response mapping. |
| IPR007197 — Radical SAM | Diverse reactions can justify a broad family-level molecular-function term. | Retain catalytic activity and iron-sulfur-cluster binding; avoid unsupported specialization across the domain. |
| IPR020849 — Ras-type small GTPases | The assessment proposes GTPase activity in addition to GTP binding. | Check the proposed addition against family-wide catalytic competence; narrow process and localization assignments where needed. |
| IPR002100 — MADS-box domain | The assessment distinguishes domain-level DNA binding and dimerization from whole-protein transcription-factor function. | Retain the two domain-level mappings; do not infer transcription-factor activity from the domain alone. |
| IPR045122 — Calcium permeable stress-gated cation channel 1-like | The entry name says calcium *permeable*, but `GO:0005227` is defined as a channel that opens when calcium binds it — opposite directions of causation. The TMEM63/OSCA members are stretch- and osmolarity-gated. | Remove the calcium-activated mapping; assess mechanosensitive cation-channel and calcium-channel terms in its place. |
| IPR042371 — Z-binding domain | A catalytic activity is mapped onto a binding domain: the deaminase belongs to ADAR1's separate domain, so ZBP1 inherits an activity it has no domain for. | Remove the deaminase mapping and restrict it to entries carrying the catalytic domain; retain RNA binding. |
| IPR013380 — Type 3 secretion system ATPase SctN | An SctN-specific entry mapped to rotational proton-transporting ATPase activity and ATP biosynthesis. SctN is a soluble protein-exporting ATPase with no Fo partner; the terms are wrong for every member (915 annotations). | Remove `GO:0046961` and `GO:0006754`; retain the type III secretion process and complex mappings; consider adding `GO:0008564` protein-exporting ATPase activity. |
| IPR004100 — ATPase, F1/V1/A1 α/β, N-terminal domain | Sound for rotary ATPase subunits, but the domain is shared by the FliI/SctN export ATPases, which do not transport protons. | Narrow `GO:1902600` and `GO:0046034`: ideally suppress when IPR005714 (FliI/YscN) also matches; if per-entry mappings cannot express that, remove them or move them to narrower entries that exclude FliI/SctN. |
| IPR005714 — ATPase, type III secretion system, FliI/YscN | `GO:0009058` biosynthetic process remains in the 2025-09 mapping file, a remnant of the ATP synthase ancestry. | Remove it; the entry's other four mappings are sound. |
| IPR006935 — Helicase/UvrB, N-terminal | The entry is dominated by DNA-acting enzymes, but the same fold occurs in the RNA-sensing RIG-I-like receptors, so IFIH1 (MDA5) inherits DNA binding. | Replace the DNA-binding mapping with `GO:0003676` nucleic acid binding, as on the sibling helicase entries IPR011545 and IPR006555; the nucleic-acid substrate is a property of the enzyme, not of the shared fold. ATP binding and hydrolase activity are unaffected. |
| IPR023720 — Trehalase, periplasmic (TreA) | `GO:0071474` cellular hyperosmotic response was filed as a removal and the research reversed it. An *E. coli* `treA` null accumulates trehalose extracellularly only under osmotic stress, which is participation evidence rather than mere induction, so the term is earned by the characterised enzyme. It is nevertheless over-broad: the osmotic content is in the circuit around the enzyme — an osmotically regulated promoter, OtsAB synthesis, trehalose excretion — and a trehalase signature detects none of those, so an *E. coli* K-12 regulatory finding reaches all 472 members. | Record as `skos:broadMatch` rather than removing: no other entry and no UniRule supplies the term to periplasmic trehalases, so a removal would strip it from *E. coli* TreA where it is supported. A `rules/curated/` rule cannot separate the members either, because the condition is "the organism runs an osmotically regulated trehalose cycle" — neither a sequence feature nor a taxon. The ask is therefore to keep the mapping and record it as over-broad rather than to move it: no destination exists, so InterPro's only alternatives are to keep it or drop it, and dropping it loses a supported term. If InterPro's policy is not to carry a knowingly over-broad mapping, the fallback is to drop it and let the term be curated per gene where induction or a stress-specific phenotype is shown. |

### Rule cover for the removals

Most removal rows in the mapping set carry a note on what still supplies the term to the
members that should keep it: 17 of the 25 do, as of 2026-11-27. The remaining eight carry no
such note, across six entries -- IPR002844, IPR005778, IPR017679, IPR036080 and, with two rows
each, IPR017681 and IPR017682 -- so a reader should not take the note's presence for granted
when checking a removal.

Test for the note by containment, not by position. Position would nearly succeed: in all 17 the
cover note is the last *topic* in its `comment`. But in two of them the comment's final sentence
is something else -- `IPR000719` `GO:0005524` ends with the sole-source check result, and
`IPR018194` with an `IPR002844`/`IPR036080` cross-reference -- so where a note ends is a
judgement rather than a marked boundary. A single trailing clause is the wrong thing to look for
in any case: 14 of the 17 notes run to more than one sentence.

To re-derive the 17:

1. Parse the YAML and test each removal row's `comment` value for a `Rule cover (` clause.
2. Do not grep the file. The comments are block scalars and the phrase wraps mid-clause on
   `IPR018194` and `IPR021006`, so a line-based search returns 16 -- which reads as a stale page
   rather than as a broken check.
3. Expect 17 as of 2026-11-27, not 18. A semantic reading can reach 18, because the IPR017682 removal of
   `GO:0050660` says where FAD binding does belong (FrhB, via IPR017679) without carrying a cover
   clause. That row is excluded deliberately: it names cover for a *sibling* entry's members, not
   for this entry's, which is the distinction the count is about.

Where a term is right for only part of an entry, a conditional UniProt rule is often the better
carrier than a mapping, because a rule can require a site, exclude a domain, or limit the taxon.
Every cover note carries its own sources and date, and they are not uniform. Of the 17 on
removal rows, the ten reproduced in the table below were checked against the UniProt UniRule API
and the current interpro2go file on 2026-10-10; the other seven are later -- three on
2026-10-15, one on 2026-11-02, one on 2026-11-05 and two on 2026-11-07 -- and six of those seven
cite only the current interpro2go file rather than any UniProt rule source, the exception being
`IPR018229`. The six cover notes on `broadMatch` rows are later again, all citing interpro2go
alone: two on 2026-11-05, three on 2026-11-15 and one on 2026-11-26. Read the provenance off the
note rather than from this sentence, and re-derive the 17-of-25 split by the clause match given
above.

| Removal | What still supplies the term | Request |
|---------|------------------------------|---------|
| IPR000719 ATP binding | IPR017441 (ATP binding site) for members with the motif; family rules such as the JNK rule UR001528758 for members without it | Remove; all 7 reviewed sole-source losses were accepted or kept. Not derivable from the predicate fields, but recorded verbatim in the row's own `comment`, which names the seven (SCHPO bub1 and ppk34, ARATH CLV1 and FLS2, MEDTR NFP, human ILK and PIK3R4) -- so family rules are needed |
| IPR000719 protein phosphorylation | Active-site entries IPR008271 and IPR008266 | Remove |
| IPR001424 superoxide metabolic process | UniRule UR000000113 selects canonical Cu/Zn SODs and excludes CCS, but assigns only the EC number; Candida albicans SOD5 lacks its PS00332 condition and needs separate Cu-only SOD cover | Remove; add `GO:0019430` to the Cu/Zn rule and to a fungal Cu-only SOD rule or narrower entry |
| IPR012724 ATP binding | Nothing needed; the HAMAP DnaJ rule MF_01152 also assigns no ATP-binding or zinc-ion-binding GO term | Remove |
| IPR042371 dsRNA adenosine deaminase activity | IPR002466 gives ADARs a deaminase term; no rule assigns the specific one | Remove; a rule conditioned on IPR002466 could restore it |
| IPR006935 DNA binding | HAMAP UvrB rule MF_00204; nothing for RIG-I-like receptors or Dicer | Replace with `GO:0003676` |
| IPR045122, IPR013380 (two), IPR005714 | Not needed; the terms are wrong for every member | Remove; for IPR045122 and IPR013380, add the correct family-wide terms as mappings |

This table is a selection, not the whole set: it carries ten of the seventeen cover notes, across
eight of the fifteen entries that have one. The rule rather than the list, because the list grows:
a removal's cover note lives in its own row `comment` in the mapping set, and this table reproduces
only some of them, so read the row before concluding that a removal has no cover. As of this
writing the entries with a cover note absent here are IPR019982, IPR018229, IPR017402, IPR001135,
IPR037893, IPR002956 and IPR018194.

The checks themselves are described in [Before proposing a removal](INTERPRO/README.md#before-proposing-a-removal).

A recurring curation question is **whether a function holds across the matched
entry**, not simply whether it is well established for one member. Conversely, a
broad term can be appropriate for a diverse family even when a more specific term
is preferable for an individual gene.

**Archaeal additions (2026-10-15).** Gene reviews in the [ARCHAEA](ARCHAEA.md)
project added six rows to the mapping set. They are inside the totals above, which are
derived over the whole file, and the three removals among them carry rule-cover clauses, so
they are inside the 17 of 25 as well:
removals for IPR019982 to threonine-type endopeptidase activity (non-catalytic
archaeal proteasome alpha subunits), IPR018229 to ion channel activity and
IPR017402 to light-activated ion channel activity (rhodopsin pumps); a proposed
Eukaryota restriction for IPR000426 to ubiquitin-dependent protein catabolic
process and IPR005024 to vacuolar transport; and narrowing IPR000534 to NAD
binding. interpro2go has no conditions, so the two restriction rows each name a
curated replacement rule in [rules/curated](../rules/curated/README.md) (CR-0001,
CR-0003) that couples the InterPro condition with a taxon condition.

## What curators can act on

1. **Assess the four removal proposals first:** ATP binding (GO:0005524) and protein
   phosphorylation (GO:0006468) for IPR000719, superoxide metabolic process
   (GO:0006801) for IPR001424, and ATP binding (GO:0005524) for IPR012724. Verify the cited exceptions and the current entry scope.
   Most removal rows carry a rule-cover note, but eight of the 25 do not, so check for one
   rather than assuming it before forwarding the removal.
   The IPR013380 removals (GO:0046961, GO:0006754) are simpler: the entry is SctN-specific, so
   they are wrong for every member rather than for an exception subset.
2. **Resolve the proposed GTPase-activity (GO:0003924) addition for IPR020849.** Confirm that the
   assignment is supported across the entry, including divergent members.
3. **Separate gene-level refinement from mapping-level error.** A `MODIFY` or
   `KEEP_AS_NON_CORE` decision on one gene does not by itself justify changing a
   family-wide mapping. Record whether a proposal requires removal, a narrower entry,
   or only a more specific annotation on that gene.
4. **Check apparently accepted annotations on exception members.** Prioritize
   pseudokinases, copper chaperones, and other members whose functions diverge from
   the mapped activity; update gene reviews when the evidence supports a correction.
5. **Extend the family assessments using the ranked worklist.** Each recommendation
   should identify the affected entry and GO term, supporting evidence, and a specific
   requested change for InterPro curators.

## Evidence snapshot

The committed [annotation table](INTERPRO/suspect_interpro_mappings.tsv) contains
**3,652 InterPro2GO annotation records**. Its priority table covers **1,826 resolved
InterPro entries**, plus an unresolved-source group. These are stored extraction
results, not live counts of the growing review collection.

| Gene-review action | Count |
|--------------------|------:|
| ACCEPT | 1,870 |
| MODIFY | 609 |
| KEEP_AS_NON_CORE | 523 |
| MARK_AS_OVER_ANNOTATED | 391 |
| REMOVE | 194 |
| NEW | 30 |
| UNDECIDED | 15 |
| PENDING | 20 |

The worklist flags **1,732 records (47%)**: `MODIFY`, `KEEP_AS_NON_CORE`,
`MARK_AS_OVER_ANNOTATED`, `REMOVE`, or `UNDECIDED`. **This is a review-priority
measure, not an estimated mapping error rate.** It includes valid but non-core
annotations, specificity refinements, and unresolved judgments. `NEW` and `PENDING`
records are excluded from this flag.

### Entries with repeated gene-level flags

These counts prioritize investigation; they are not family-level verdicts. A record
can cite several entries, so counts across entries should not be summed.

| InterPro entry | Annotation records | Flagged records |
|----------------|-------------------:|----------------:|
| IPR000719 | 112 | 50 |
| IPR008271 | 55 | 34 |
| IPR001128 | 44 | 26 |
| IPR036396 | 44 | 26 |
| IPR001424 | 20 | 16 |
| IPR036423 | 20 | 16 |
| IPR001046 | 27 | 15 |
| IPR012724 | 24 | 13 |
| IPR000276 | 21 | 12 |

See the [complete worklist](INTERPRO/interpro_family_priorities.tsv) for action
breakdowns, example genes, and affected GO terms.

## Supporting material

- [Proposed InterPro2GO edits](INTERPRO/interpro2go.sssom.yaml) — 66 mapping assessments across
  38 entries, with term identifiers and rationales. The per-date breakdown this bullet used to give
  has been dropped rather than corrected: `mapping_date` appears once at set level and no row carries
  its own, so a split by date cannot be re-derived from the file and would go stale the same way the
  counts did. Adding per-row `mapping_date` to the SSSOM would make it derivable. In this project's encoding,
  `exactMatch` endorses or proposes a mapping, `broadMatch` flags a scope or specificity
  issue, and `exactMatch` with `predicate_modifier: Not` proposes removal.
- [Methods, data, and reproducibility](INTERPRO/README.md) — extraction, family research,
  mapping format, and validation commands.
- [Status and historical notes](INTERPRO/notes.md) — open follow-up tasks, archived
  workstream checklists, and session chronology.
- [Protein families](FAMILIES.md) · [IBA annotation review](IBA_REVIEW.md) ·
  [Over-annotation patterns](OVER_ANNOTATION_PATTERNS.html) — related collections.
