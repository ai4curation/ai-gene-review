# dnaK / Q88DU2 annotation audit notes

## 2026-08-29 — qualifier-aware review

Reviewed the three current `dnaK-goa.tsv` signatures, UniProt Q88DU2, the
Falcon report, the complete cached PMID:33668424 paper, abstract-only
PMID:7937953, the E. coli DnaK precedent, and
`projects/UNFOLDED_PROTEIN_BINDING.md`. Current GOA contains exactly two
`enables` rows and one `involved_in` row. All three are represented exactly once
and ACCEPTed. There are no IBA or PANTHER/PTN rows to audit.

The three current claims are coherent and mutually reinforcing: ATP binding
(GO:0005524) and ATP hydrolysis (GO:0016887) drive the folding process
(GO:0006457). The KT2440-isogenic full text describes the molecular coupling
directly [PMID:33668424, "ATP binding and hydrolysis by DnaK NBD allosterically
controls the binding of SBD to its substrates—short hydrophobic peptide segments
that would normally be buried in the folded structure."]

## GO:0051082 replacement

The initial YAML contained an author-supplied NEW row for GO:0051082, using the
InterPro IEA visible in the UniProt flat file even though that assertion is
absent from the current GOA. GO:0051082 is now obsolete. It was not retained as
an interim or retired annotation merely to silence reconciliation checks.
Instead, the synthetic obsolete row was removed and replaced with a NEW,
qualifier-aware ISS proposal for GO:0140662 **ATP-dependent protein folding
chaperone**, the specific current child of GO:0044183 matching the Hsp70
mechanism.

The evidence code is deliberately ISS rather than IDA. PMID:33668424 is a
full-text P. putida study and describes repeated ATP-dependent binding and
release by DnaK, while its experiments address the C-terminal tail, GraT
phenotypes and competitive fitness rather than purified Q88DU2 client
refolding. Direct biochemical reconstitution is supplied by the canonical E.
coli DnaK ortholog [PMID:7937953, "The binding and release of substrate protein
for folding involves the following ATP hydrolysis-dependent cycle: (i) unfolded
luciferase binds initially to DnaJ; (ii) upon interaction with
luciferase-DnaJ, DnaK hydrolyzes its bound ATP, resulting in the formation of a
stable luciferase-DnaK-DnaJ complex; (iii) GrpE releases ADP from DnaK; and (iv)
ATP binding to DnaK triggers the release of substrate protein, thus completing
the reaction cycle."]

Client binding can transiently prevent aggregation, but the evidence reviewed
here places it inside an ATP-driven foldase cycle. No Q88DU2-specific evidence
establishes a separable ATP-independent holdase regime, so the holdase NTR was
not proposed for this gene and carrier-specific GO:0140309 is inapplicable.

The review is COMPLETE. The remaining experimental gap is direct biochemical
reconstitution of Q88DU2 with its KT2440 DnaJ and GrpE partners, which would
permit an IDA annotation to GO:0140662.
