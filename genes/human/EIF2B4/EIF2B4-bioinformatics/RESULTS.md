# EIF2B4 source-identity analysis

The saved raw inputs reproduce the identity and provenance chains supporting the review. They do not independently establish physiological importance, direct binary contact or natural-product equivalence.

## Interaction and partner scope

The complete IntAct query has 159 records. Eighteen imported generic-binding contexts are joined by exact publication and participant accession. Four have no matching current IntAct record in this export: the historical PMID:29599245 aggregate and the PMID:15060152/PMID:29599213 assembly contexts. Their positive primary-source evidence is assessed separately; a missing current interaction record is not treated as negative experimental evidence.

| Imported context | Matched records | Scope |
|---|---:|---|
| Q53XC2 beta, row 10 | 4 | The official reference sequence is identical to reviewed P49770, 351 residues. |
| P49770 beta, rows 11/14/15/17 | 3/1/3/2 | Separate study/assay contexts remain separate. The BioPlex pair is an association, not a purified binary contact. |
| Viral M2, row 12 | 3 | Viral P06821 is distinct from the human assay host and target. |
| AGT, row 16 | 3 | The full precursor reference does not justify a hormone-activity claim for delta. |
| FOS/KLKB1/LPL/UQCRC1/VHL-2/GATM/GRB2, rows 46–52 | 3 each | Literal assay methods, taxon fields, reference ROGIDs and assayed-feature fields are retained in `records.json`. |

Every selected curated reference checksum matches its saved official sequence. This authenticates the reference entity, not the complete assayed insert. VHL isoform 2 is independently reconstructed as a 172-residue sequence lacking canonical residues 114–154; it is not interchangeable with the shorter N-terminally truncated isoform commonly discussed under a different name. Partner enzymatic activity is not transferred to delta.

The FOS/KLKB1/LPL/GATM binary two-hybrid records support assay-context binding. Independently documented partner classes remain contextual findings, but the specific binding replacements are withdrawn: the exact experimental inserts, processing states and natural-product equivalence remain unresolved, and no independent EIF2B4 role with these partners was established. Generic non-core binding is retained; the primary study’s orthogonal subset is not assigned to an unverified target pair. The viral M2 records instead establish co-complex association, not a resolved direct contact, so generic non-core binding is retained without a transporter-binding replacement. UQCRC1 processing activity remains qualified in its official record, while GRB2 is an adaptor; neither automatically supplies a more specific binding subclass here.

## PAINT and rat donor provenance

The family tree and alignment each contain 288 entries. The human Q9UI10 target is leaf PTN002469356; its ungapped 523-residue sequence exactly matches the official canonical sequence. The 20-node ancestral path includes PTN000027922. Three positive IBD records on that path specify initiation-factor activity, the eIF2B complex and cytoplasmic translational initiation. The two imported IBA rows join their literal ancestral records and extant source sets. No NOT record occurs on this target path in the saved complete IBD snapshot.

The complete rat Q63186 query contains 44 records. Exact IDA provenance maps:

| Term | Donor reference |
|---|---|
| GO:0031369 translation initiation factor binding | PMID:9446619 |
| GO:0009408 response to heat | PMID:9341116 |
| GO:0009749 response to glucose | PMID:8567668 |
| GO:0043434 response to peptide hormone | PMID:8430778 |

These are source joins, not substitutes for reading the donor experiments. The binding paper has selected original rat-liver Methods/Results/captions; the remaining donor assessments use authentic abstracts. A short donor list and target self-grounding are not treated as weaknesses in the ancestral placement.

## Rules, localization and product boundaries

Four ARBA rules have target-matching FunFam conditions. The GEF rule concludes GO:0005085 but its saved conclusion does not expose an annotation relation; it cannot independently establish how an `enables` relation was inherited from another source. The remaining rule conclusions are assessed individually in the review. In particular, the CNS-development and organ-development conclusions are marked over-annotated because the positive clinical observations do not identify those developmental steps beyond the established translation mechanism. The saved ARBA00026561 condition set 55 and ARBA00029247 condition set 240 (zero-based) both match Q9UI10 FunFam 3.40.50.10470:FF:000002; these literal matches do not themselves resolve the biological participation question.

Reactome events 72670/72722 connect through complex 72526 and catalyst activity 72528. Human component 72521 identifies Q9UI10, residues 1–523, and its own cytosol compartment. The exchange catalyst is the complex. Component membership does not mean that delta alone performs the whole exchange reaction.

The three official FASTAs preserve the 523-, 543- and 522-residue natural products. The canonical PAINT/structure match establishes canonical identity only. The 543-aa construct called V1 in PMID:37014850 is not assigned to a natural product by length alone; its overexpression experiments do not establish equivalence of all three products.

The earlier GOA has 57 raw contexts and the current snapshot has 49. The adopted review contains 53 source objects, including four historical assertions absent from the current feed. The raw snapshots and imported dictionaries remain available for exact replay; no lifecycle conclusion is generated by the script.

The full inputs, selection fields and source records are in `source-inputs.zip`, `source-manifest.json` and `records.json`. [Reproduction instructions](README.md) cover offline execution and changed-input rejection. [Original-source locators](original-locators.json) and the [source guide](../EIF2B4-source-guide.md) distinguish cached text from separately inspected originals.
