# GND1 (A0A1D8PFS4) coenzyme-specificity motif check

Script: `check_coenzyme_motifs.py` (plain Python 3, no third-party dependencies).
Run from this folder: `python3 check_coenzyme_motifs.py` (reads `../GND1-uniprot.txt`,
writes `results.json`).

## Question

GO:0004616 (phosphogluconate dehydrogenase (decarboxylating) activity) is defined
as the NADP+-dependent reaction (EC 1.1.1.44, RHEA:10116). 6PGDH enzymes also exist
as NAD+-specific and dual-specificity forms (EC 1.1.1.343), so a cofactor-specificity
error is possible in principle. The only C. albicans enzyme assay in the literature
(Strijbis et al. 2012, PMID:22094058) used NADP+, but the paper is abstract-only in
our cache. This check asks whether the sequence carries the structural determinants
of NADP+ specificity described by Hanau & Helliwell (2022, PMID:35234135).

## Determinants tested (sheep 6PGDH numbering, PMID:35234135)

| Determinant | NADP+-specific 6PGDH | NAD+-preferring 6PGDH |
|---|---|---|
| dinucleotide-binding fingerprint, beta-a/alpha-a turn (sheep 9-14) | Gly-X-Ala-X-Met-Gly | classical Gly-X-Gly-X-X-Gly |
| 2'-phosphate-binding turn, beta-b/alpha-b (sheep 32-34) | Asn-Arg-Thr | Asp-Arg-Asp (Asp hinders the 2'-phosphate) |

## Result

| Motif | C. albicans Gnd1 | Position (1-based) | Overlaps UniProt NADP(+) BINDING feature |
|---|---|---|---|
| Gly-X-Ala-X-Met-Gly fingerprint | `GLAVMG` | 13-18 | yes (13..18) |
| classical NAD+ fingerprint Gly-X-Gly-X-X-Gly | not found in residues 1-60 | - | - |
| Asn-Arg-Thr NADP+ 2'-phosphate motif | `NRT` | 36-38 | yes (36..38) |
| Asp-Arg-Asp NAD+-type motif | not found in residues 1-60 | - | - |

Verdict (from `results.json`): NADP+-specific determinants present (Asn-Arg-Thr); NAD+-type Asp-Arg-Asp absent.

Both NADP+-specificity determinants of the sheep enzyme are conserved in C. albicans
Gnd1 at a constant offset of +4 residues, and both coincide exactly with the
PIRSR-derived NADP(+) binding features in the UniProt record (13..18 and 36..38).
The Asp substitution that switches 6PGDH toward NAD+ is absent.

## Interpretation

The sequence supports the NADP+-specific term GO:0004616 (EC 1.1.1.44) as the
correct cofactor-specific molecular function for GND1, and the accompanying
NADP binding (GO:0050661) annotations. This is a sequence-level inference and
does not replace a kinetic comparison of NAD+ versus NADP+ with the purified
enzyme, which has not been reported for the C. albicans protein.
