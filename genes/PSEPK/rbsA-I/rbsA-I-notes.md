# rbsA-I curation notes

Q88K37 is the ATP-binding component in the contiguous PP_2454-PP_2459 `rbs`
locus. ATP hydrolysis is its intrinsic catalytic function; D-ribose transporter
activity belongs to the assembled RbsABC complex and must use a `contributes_to`
qualifier in the synthesized core. The protein is peripheral to the inner
membrane rather than an integral permease
[file:PSEPK/rbsA-I/rbsA-I-uniprot.txt, "CC       {ECO:0000256|ARBA:ARBA00004202}; Peripheral membrane protein"].

The submitted name and locus support ribose import, but the current PANTHER
subfamily is D-allose-import-related. It is therefore omitted from the reusable
module rather than relabeled
[file:PSEPK/rbsA-I/rbsA-I-uniprot.txt, "DR   PANTHER; PTHR43790:SF3; D-ALLOSE
IMPORT ATP-BINDING PROTEIN ALSA-RELATED; 1."].

OpenScientist supports a two-fused-NBD RbsA-family ATPase interpretation from
the sequence architecture, locus, and E. coli ortholog literature, but it
states, "No direct experimental data on PP_2455 itself."
[file:PSEPK/rbsA-I/rbsA-I-deep-research-openscientist.md]. It also emphasizes
that substrate specificity is assigned by RbsB rather than by RbsA-I. The
report therefore reinforces `ATP hydrolysis activity` as intrinsic and
`ABC-type D-ribose transporter activity` as `contributes_to`.
