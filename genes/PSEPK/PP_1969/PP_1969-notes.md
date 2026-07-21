# PP_1969 curation notes

## 2026-07-20 OpenScientist report assessment

The generated OpenScientist report is retained unchanged as provider output but is
assessed as `MISCITED` for target-level curation. It declares Q88LG4 canonical MoaA
and an exact GTP 3',8'-cyclase despite the absence of a PP_1969 assay
[file:PSEPK/PP_1969/PP_1969-deep-research-openscientist.md, "PP_1969 encodes **MoaA**"];
that catalytic conclusion is not propagated.

The report also states `moaB = PP_1294` and `mogA = PP_3457`. Local target records
show that PP_1294 is `moaE`, the molybdopterin synthase catalytic subunit
[file:PSEPK/moaE/moaE-uniprot.txt, "GN   Name=moaE"] and that PP_3457 is reviewed
`mobA`, the molybdenum cofactor guanylyltransferase
[file:PSEPK/mobA/mobA-uniprot.txt, "GN   Name=mobA"]. The report's residue-numbered
motif analysis was not saved as a reproducible local analysis and is not used as
evidence.

The curation decision remains conservative: Q88LG4 is a divergent MoaA-like
radical-SAM candidate. Its exact substrate, GTP 3',8'-cyclase activity, and pathway
necessity remain `UNDECIDED`, grounded in the target UniProt record and the saved
local sequence comparison rather than the provider's catalytic claims.
