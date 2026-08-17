# ULK1 curation notes

## Convention: `MARK_AS_OVER_ANNOTATED` vs `KEEP_AS_NON_CORE`

`ULK1-ai-review.yaml` carries a large number of rows in both non-core buckets, and review of
this file asked for the boundary between them to be derivable from the file rather than
inferred case by case. This is the convention the file applies. It is a within-gene
convention; it does not attempt to set repo-wide policy for the ~165 comparable annotations
elsewhere, which remains a curator's call.

**`ACCEPT` rows are outside the test.** They are the statements of the core function, and a
parent term can be the right core statement even when descendants are also annotated —
GO:0000407 phagophore assembly site is accepted with GO:0034045 beneath it, and GO:0016236
macroautophagy is accepted with GO:0000045, GO:0000423 and GO:0061709 beneath it. The test
below only chooses between the two non-core actions.

**The test.** For a row that is not a core statement: *would dropping it lose anything this
gene's other retained rows do not already carry?*

- **No → `MARK_AS_OVER_ANNOTATED`.** The row is losslessly redundant, because a retained
  annotation on this same gene already states the same claim more precisely. Also used for
  the separate case of a row that **overreaches its evidence** rather than merely repeating
  a better one (below).
- **Yes → `KEEP_AS_NON_CORE`.** The row is accurate and non-redundant but peripheral: it
  carries a distinct partner, cargo, context, location-state or downstream consequence that
  no other retained row states.

### Five qualifications, each of which decides at least one row in this file

1. **"More precisely" is judged on the claim, not on term ancestry alone.** For a binding
   term the interaction partner is part of the claim. GO:0051020 GTPase binding is a parent
   of GO:0031267 small GTPase binding and both are annotated here, but the GOA record names
   different partners — `UniProtKB:A1A4Y4` (IRGM) versus `UniProtKB:Q9P2M4` (TBC1D14) — so
   the descendant does not discharge the parent, and GO:0051020 stays `KEEP_AS_NON_CORE`.

2. **The discharging row must itself be retained as established, not under replacement.**
   GO:0010506 regulation of autophagy has GO:0010508 and GO:0016241 beneath it, but both are
   `MODIFY` collapsing onto the proposed GO:0016239, so neither is established and GO:0010506
   stays `KEEP_AS_NON_CORE`. This is the constraint already recorded at
   `projects/SL/SL-0162-MEMBRANE.md:52-59` after the MCH2 and DNAJC25 reverts: that a more
   specific term *exists* is not sufficient; it also has to be accepted.

3. **A row is not redundant if it is the sole experimental support for the claim.** Where the
   more precise rows are propagations (IBA/IEA/ISS) and the broad row is not, dropping the
   broad row costs the claim its evidence. GO:0031175 neuron projection development (IMP) is
   kept for this reason even though GO:0048675 axon extension sits beneath it, because
   GO:0048675 is IBA. The same asymmetry is why GO:0007409 axonogenesis *is* over-annotated:
   it is IEA, so nothing is lost with it. The carve-out does not fire elsewhere — GO:0006914
   autophagy is discharged by GO:0000045 (IDA), GO:0005737 cytoplasm by GO:1903349 and
   GO:0000407 (IDA), GO:0004672 by GO:0004674 (EXP/IDA).

4. **Evidence code does not otherwise protect a row.** Redundancy is a property of the claim,
   so experimental rows are marked over-annotated on the same footing as electronic ones —
   the six GO:0006914 rows include IDA, IGI and IMP, and GO:0005737 cytoplasm includes an
   IDA. `MARK_AS_OVER_ANNOTATED` does not delete anything; it records that the assertion adds
   no information the gene's better rows do not already carry.

5. **Redundancy can run across aspects.** One row is discharged by entailment rather than by
   descent: GO:0007165 signal transduction (IEA) has no annotated descendant on this gene, but
   it is implied by GO:0004674 protein serine/threonine kinase activity, which is accepted here
   on EXP and IDA, and it applies to essentially every protein kinase. It states nothing about
   ULK1 that the accepted molecular function does not already carry, so it is over-annotated.
   This is the only row in the file decided this way, and it is deliberately narrow: it needs a
   term broad enough that the accepted annotation entails it outright, not merely one that
   sits in a related area.

### The second use of `MARK_AS_OVER_ANNOTATED`: overreach

Two rows are marked over-annotated for a different reason — not redundancy but asserting more
than the evidence supports. GO:0034727 piecemeal microautophagy of the nucleus is an IBA whose
only non-node donor is the yeast gene, and the process depends on the budding-yeast
nucleus-vacuole junction, which humans lack. GO:0035032 phosphatidylinositol 3-kinase complex
class III is an IPI, but the ULK1C:PI3KC3-C1 structure puts FIP200 at the interface and not
ULK1, so ULK1 is not a constituent of that complex. Both fit the enum gloss ("not entirely
wrong, but likely represents an over-annotation") without being redundancy cases.

## Changes made under this convention

Applying the test to every non-`ACCEPT` row moved two claims and corrected three reasons that
had stated the right action for a wrong or unverifiable relationship:

- **GO:0006468 protein phosphorylation (NAS)** → `MARK_AS_OVER_ANNOTATED`. GO:0018105
  peptidyl-serine phosphorylation is a strict `is_a` descendant (verified via QuickGO), is
  annotated here on IDA and is accepted. This was the pair raised in review against GO:0004672
  protein kinase activity, which was already over-annotated on identical logic for the
  molecular-function side of the same kinase claim.
- **GO:0005776 autophagosome (IBA, IDA ×2)** → `MARK_AS_OVER_ANNOTATED`. GO:0000421
  autophagosome membrane is a `part_of` descendant, is annotated on IDA and is retained. Same
  call as GO:0005737 cytoplasm, the parent of this gene's other retained locations.
- **GO:0033554 cellular response to stress (IDA)** — action unchanged, reason corrected. It had
  claimed GO:0042594 and GO:0031669 were more specific children that made the parent
  redundant. QuickGO ancestor queries show neither is a descendant of GO:0033554: GO:0042594
  sits under GO:0006950 response to stress rather than the cellular branch, and GO:0031669
  under the response-to-extracellular-stimulus branch. (GO:0009267 cellular response to
  starvation *is* a descendant, but is not annotated to this gene.) The row is therefore not
  redundant and correctly stays non-core, but not for the reason given.
- **GO:0051020 GTPase binding (IPI)** — action unchanged, reason corrected to rest on partner
  distinctness (qualification 1) rather than on being "less informative than GO:0031267",
  which invoked the redundancy logic that would have flipped it.
- **GO:0031175 neuron projection development (IMP)** — action unchanged, reason extended to
  state the sole-experimental-support carve-out (qualification 3) explicitly.

The GO:0005776 IBA row also gained a `propagation_review`, which the validator requires once
an IBA row is marked over-annotated. It is recorded as `EVIDENCE_CIRCULAR_OR_REDUNDANT` with
`GRANULARITY_MISMATCH`, matching the enum gloss "the target already has stronger direct
evidence" — the target carries GO:0000421 on IDA. No `source_entities` are listed, because the
PANTHER donor nodes were not inspected; the redundancy is established from the target's own
annotations, not from the donors, and inventing source identifiers would be worse than
omitting an optional slot.

Partner identifiers above are read from `ULK1-goa.tsv` (WITH/FROM column); ancestor
relationships are from the QuickGO ontology API with `relations=is_a,part_of`.
