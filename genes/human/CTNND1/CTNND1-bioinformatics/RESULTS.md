# Historical p120 construct mapping

The translation of ENA Z17804.1 (CAA79078.1, mouse, 911 residues) aligns best
among the 32 supplied human CTNND1 products to O60716-8, currently named isoform
1 (912 residues). There are 887 identical pairs among 911 paired residues
(97.3655%); all query residues align. Current human isoform 1B, O60716-6
(941 residues), ranks fourth with 886 identical pairs. A historical construct
name therefore cannot by itself establish a current human isoform identifier.

In the best alignment, query Tyr96, Tyr112, Tyr217, Tyr228 and residues 622–628
(KKGKGKK) map to identical residues at the same human positions. The first two
optimal alignments agree on all selected positions. The software flags multiple
optimal alignments; it does not enumerate all of them. Human product 1C has an
insertion within the mapped basic region, illustrating why shared gene identity
cannot establish equivalent regulation of all products.

These are sequence results, not measurements of GDP inhibition. Together with
the cited mouse functional experiments they support a qualified inference for
human long products. They do not authenticate an experimental plasmid, measure
any human product, or demonstrate activity of all 32 forms.

The independent CTNNB1 human P35222/mouse Q02248 control aligns all 781 residues,
with 780 identities and no alternative optimal alignment. This checks that the
same generic program works on another gene; it is not a functional control.

## Reproduction and provenance

`just analyze check-other-gene` completed successfully using the locked
environment and Biopython 1.85. Both complete JSON outputs are in `results/`.
Parameters and source identifiers are in README.md; source paths and SHA-256
digests are in `data/provenance.json`. ENA input digest:
`9d1c21be2c0cecd4f0e437792025dddc33d1d3f0a3fb12bf3e1f2d74d7b07487`.

- [x] Scripts accept inputs and calculate outputs without hardcoded sequences or results.
- [x] The alignment script ran on an independent gene input.
- [x] Both analyses completed successfully; ranked mappings and control alignment were inspected.
- [x] Direct results and archived input sequences are in this folder.
- [x] Provenance, parameters, tie handling and interpretation limits are documented.
