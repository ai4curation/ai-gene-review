# LOXHD1 bioinformatics results

## Outcome

The curated Q8IVV2 sequence is a near-continuous array of 15 annotated PLAT
domains (residues 43-2064), with no separately annotated catalytic domain.
Across the 105 repeat pairs, global identity ranges from 20.16% to 49.58%, with
a median of 34.71%. This quantifies primary-sequence similarity among repeats
*within human LOXHD1*; it is not a statistical significance test or an
ortholog-conservation analysis. [UniProt Q8IVV2 input:
`../LOXHD1-uniprot.txt`; direct outputs: `results/domains.tsv`,
`results/repeat_pairwise_identity.tsv`, and `results/summary.json`; input SHA-256
`675481b5c18ee06ce18fe7a6df1b95fd5eb153608f0cea5fd56bde6badee336e`]

The isoform-coordinate mapping is:

- Q8IVV2-1 retains all 15 annotated repeats.
- Q8IVV2-3 loses repeats 1-6, deletes 92 of 121 annotated residues in repeat 7,
  retains repeats 8-14, and alters repeat 15 through a 12-residue replacement
  followed by deletion from residue 2020 onward.
- Q8IVV2-4 loses repeats 1-11, deletes the first four annotated residues of
  repeat 12, retains repeats 13-14, and deletes the C-terminal 52 annotated
  residues of repeat 15.
- Q8IVV2-5 loses repeats 1-11, deletes the first four annotated residues of
  repeat 12, and retains repeats 13-15.

These are coordinate-derived domain effects, not demonstrations that a partial
repeat folds or functions. [UniProt `VAR_SEQ` and `DOMAIN` features mapped in
`results/isoform_repeat_effects.tsv`; aggregate counts and feature provenance in
`results/summary.json`]

The architecture is consistent with a nonenzymatic repeat/scaffold protein and
does not support treating the name "lipoxygenase homology" as evidence for a
lipoxygenase reaction. However, sequence architecture alone cannot prove the
absence of catalytic activity; that conclusion still depends on the lack of a
demonstrated reaction in experimental literature. No catalytic residues,
substrate, product, or enzymatic mechanism were inferred by this pipeline.

## Controls

The generic parser was run without code changes on two independent curated
human proteins. For GLRX3/O76003 it extracted three annotated domains, selected
both domains containing the label `Glutaredoxin`, and generated their single
pairwise comparison (54.90% identity). For LOX/P28300 it selected zero PLAT
domains, as expected for the requested label, and generated an empty comparison
set without failure. [Direct outputs:
`control-results/glrx3-positive/summary.json` and
`control-results/lox-negative/summary.json`]

## Reproducibility checklist

- [x] No script uses hardcoded input or output paths; all are command-line
  parameters, with convenience defaults confined to the `justfile`.
- [x] The script was tested on two other protein inputs (GLRX3 and LOX).
- [x] Target and both control analyses completed as expected.
- [x] Direct result files are present under `results/` and `control-results/`.
- [x] Summary statements have detailed provenance and bounded interpretation.
