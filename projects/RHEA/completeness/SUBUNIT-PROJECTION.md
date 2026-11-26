# Rhea projections onto complex subunits

**Bottom line:** a Rhea reaction and its GO term can describe the same activity while the two
resources attach that activity to proteins differently. Swiss-Prot often records a complex's
reaction on every subunit. GO curators give the subunits that only help `contributes_to`. UniProt's
Rhea2GO projection (`GO_REF:0000116`) turns each catalytic-activity line into an `enables` row; of
its 528,129 rows in GOA, none is `contributes_to` (QuickGO, 2026-11-26; the query is in
`fetch_data.sh` and writes `rhea2go_projection_qualifiers.txt`). So wherever a reaction
sits on a subunit, the projection asserts that the subunit alone carries out the activity. We
measured 1,215 Swiss-Prot entries (1,228 entry-term pairs) where the projection says `enables`
for a term on which a curator has recorded `contributes_to`, the same term or a more specific
one. That is a lower bound: 33,495 entries with a projected term show some sign of complex
membership, and most have no `contributes_to` row to compare against.

## What this means for the mapping work

- **Mappings are about activity types.** Whether RHEA:29779 and an ABC-type L-methionine
  transporter term describe the same activity does not depend on which MetNIQ subunit is
  reviewed. A subunit review can back a staged mapping
  (see ai4curation/ai-gene-review#7071).
- **Projections need the critical look.** A projected `enables` row on a subunit may need to
  be `contributes_to`. The issue is in the projection, not in the mapping.
- **The consistency metric cannot see the qualifier.** `consistency.py` reads native MF terms
  from UniProt's GO cross-references (`fetch_by_acc.py`), which drop the qualifier. A subunit
  whose only row is `contributes_to` on the mapped term therefore counts as *consistent*,
  which inflates agreement rather than disagreement. A subunit with no catalytic MF counts as
  `none`, which the 83% agreement figure leaves out of its denominator. The one route by which
  subunit practice can add to the disagreement is `disjoint`: a subunit that carries its own
  subunit-level activity, such as glutaminase on the small subunit of carbamoyl-phosphate
  synthase, against a complex-level mapped term. Measuring that needs per-entry consistency
  output, which `consistency.py` does not yet write.

## Measurement

`subunit_projection.py` (run by `run_all.sh`; inputs from `fetch_data.sh`) joins:

- Swiss-Prot entries and their Rhea reactions (`rhea2uniprot_sprot.tsv`);
- GO's RHEA xrefs with `skos:exactMatch` or `skos:narrowMatch` from `go-edit.obo` (go-ontology
  `2f2d73a`, 2026-11-21), which are the xrefs the projection uses;
- every `contributes_to` molecular-function row in GOA (QuickGO, 115,162 rows; the script
  fails if the count reaches the download limit);
- complex signals from UniProt: a ComplexPortal xref, a GO cellular-component term whose label
  contains "complex" anywhere (so "mitochondrial respiratory chain complex IV" counts), or a
  SUBUNIT note naming a heteromer, a complex or subunits.

Results (`subunit_projection_summary.txt`, rows in `subunit_projection.tsv`):

| Measure | Entries |
|---|---|
| Swiss-Prot entries with a Rhea reaction (UniProt stream) | 236,488 |
| Entries with at least one projected GO term (Rhea FTP join; all also in the stream) | 210,022 |
| ... of those, with a complex signal | 33,495 |
| ... of those, with any `contributes_to` MF row | 1,910 |
| Projection `enables` vs native `contributes_to` on the same term or a descendant | 1,215 |

All 1,215 entries carry at least one complex signal.

The `ct_sources` column records each supporting `contributes_to` row as
assigned_by:reference:ECO. Counted as source mentions (a pair can have several, so these sum
to more than 1,228), they come mainly from GO_Central (751, of which 688 are IBA,
ECO:0000318) and UniProt (469, of which 373 are ISS, ECO:0000250). Those UniProt ISS rows sit
on the same entries whose Rhea lines produce the `enables` rows, so UniProt sometimes asserts
both relations for one protein.

Top projected terms among the 1,228 pairs:

| Term | Pairs |
|---|---|
| GO:0004129 cytochrome-c oxidase activity | 303 |
| GO:0034062 5'-3' RNA polymerase activity | 189 |
| GO:0004088 carbamoyl-phosphate synthase (glutamine-hydrolyzing) activity | 64 |
| GO:0050567 glutaminyl-tRNA synthase (glutamine-hydrolyzing) activity | 55 |
| GO:0004826 phenylalanine-tRNA ligase activity | 44 |
| GO:0008137 NADH dehydrogenase (ubiquinone) activity | 44 |

These are respiratory complexes, RNA polymerase and heteromeric enzymes with separate
glutaminase and synthase subunits, as expected.

## Limits

- The 1,215 count needs a curator's `contributes_to` row. Complexes nobody has annotated that
  way are missed, so the true number is larger.
- The complex signal is coarse. Its 33,495 entries include catalytic subunits, for which a
  projected `enables` is right, and homomers whose SUBUNIT note uses the word "complex".
- Whether a catalytic subunit should itself be `contributes_to` for a complex-level activity is
  a convention question. The OXPHOS project treats even catalytic subunits as contributing to
  the complex activity; the counts here do not decide it.
- A `contributes_to` row can be wrong too. The table lists candidates, not errors.

## Related projects

- [Protein Complex Functions](../../PROTEIN_COMPLEX_FUNCTIONS.md): the decision framework for
  which subunits enable and which contribute. The Rhea projection is another channel by which
  a complex activity reaches every subunit, alongside domain signatures, IBA and GO-CAM export.
- [OXPHOS](../../OXPHOS.md): cytochrome-c oxidase and complex I lead the table above.
- [Complex Portal](../../COMPLEXPORTAL.md): Complex Portal copies BP and CC terms to subunits but
  not MF. The Rhea projection is in effect the MF counterpart.
- [Over-annotation patterns](../../OVER_ANNOTATION_PATTERNS.md), pattern 8 (catalytic function
  assigned to non-catalytic complex subunits), and the `ROLE_CONFLATION` pattern in
  [IBA review](../../IBA_REVIEW.md).
- The prediction-review error type `COMPLEX_ACTIVITY_TRANSFER` names the same failure for
  predictions.
