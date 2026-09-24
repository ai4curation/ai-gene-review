# TreeGrafter rejection re-review, 2026-09-24

This audit re-examines every TreeGrafter annotation (`IEA` / `GO_REF:0000118`)
whose gene review currently records `action: REMOVE` or
`action: MARK_AS_OVER_ANNOTATED`. The question for each row is whether that
rejection stands on stated biological grounds, or whether it should be relaxed
to `ACCEPT`, `KEEP_AS_NON_CORE`, `MODIFY`, or `UNDECIDED`.

Genes whose rejected rows were already re-assessed in the
[2026-09-20 audit](../rereview-2026-09-20/) (`status: reviewed`) are excluded
here; those decisions stand as recorded there.

Scope is the flagged rows only (`scope: treegrafter_rejections`), not a
full-gene re-review. Other annotations in the same gene are not re-adjudicated
unless a decision on a flagged row logically requires it (for example, a
`MODIFY` whose replacement term is already carried by another row).

## Decision rules

Taken from `CLAUDE.md` and the 2026-09-20 audit README:

1. **`REMOVE` needs positive contrary evidence.** It is appropriate for an
   electronic propagation that is demonstrably wrong: reaction chemistry or
   substrate that the target cannot perform, a domain architecture the target
   lacks, lost catalytic residues, a pathway absent from the organism, or a
   direct experimental contradiction. "Family-level propagation" or "no
   target-specific assay" is not, on its own, grounds for `REMOVE`; the absence
   of a target experiment does not refute a supported phylogenetic inference.
2. **Broad but true terms are not over-annotations.** `cytoplasm` or `cytosol`
   on a soluble bacterial enzyme is correct; redundancy with a more specific
   sibling does not make it wrong. Such rows go to `ACCEPT` (or
   `KEEP_AS_NON_CORE` when the location is real but peripheral). A generic
   location that is *incompatible* with the protein (e.g. `cytosol` on an
   integral membrane transporter with no soluble pool) can stay rejected.
3. **Too-coarse terms are `MODIFY`, not `REMOVE`.** When the propagated term
   is a true ancestor of the gene's real activity, or a sibling that names the
   right chemistry with the wrong specificity, use `MODIFY` with a
   `proposed_replacement_terms` entry, or `ACCEPT` when the specific term is
   already carried by another row and the ancestor is simply true.
4. **`MARK_AS_OVER_ANNOTATED`** is for terms that are not false but attribute
   more than the evidence supports (e.g. a whole-pathway process term on a
   single enzyme whose product could feed that pathway). When even that is
   uncertain, prefer `UNDECIDED` over asserting a rejection.
5. **Verify the term definition** (QuickGO
   `https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:NNNNNNN`) and
   the target's own evidence: `*-uniprot.txt` (catalytic activity, domains,
   InterPro/PANTHER cross-references), `*-goa.tsv` (other evidence for the same
   or related term), the notes and cached deep-research files, and cached
   publications. Do not invent evidence, PMIDs, or term ids.

## Record format

One batch YAML per reviewer batch (`batch-NN.yaml`), top-level `date`, `scope`,
and `genes`. Each gene entry records `gene`, `gene_file`, `status`
(`reviewed`), `scope: treegrafter_rejections`, `outcome` (`changed` /
`confirmed`), and an `annotations` list with `term_id`, `term_label`,
`evidence_type`, `original_reference_id`, `previous_action`, `action`,
`outcome` (`retained` when action unchanged, `changed` otherwise), and a
`rationale` written from the evidence considered. When the review file was
edited, the gene also gets an append-only history record scaffolded with
`just new-history`.

`summary.tsv` is generated from the batch files by `summarize.py`.
