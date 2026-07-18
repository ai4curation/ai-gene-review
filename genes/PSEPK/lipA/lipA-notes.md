# lipA curation notes

LipA/Q88DM5 is the 338-amino-acid radical-SAM lipoate synthase. UniProt records
the direct reaction as insertion of sulfur atoms into an octanoyl group already
attached to a lipoyl domain
[file:PSEPK/lipA/lipA-uniprot.txt, "CC   -!- FUNCTION: Catalyzes the radical-mediated insertion of two sulfur atoms"].
The record contains the LipA-specific and radical-SAM domains
[file:PSEPK/lipA/lipA-uniprot.txt, "DR   InterPro; IPR003698; Lipoyl_synth."]
[file:PSEPK/lipA/lipA-uniprot.txt, "DR   InterPro; IPR007197; rSAM."].

For module boundaries, LipA is the second endogenous protein-lipoylation step:
LipB first transfers octanoyl from octanoyl-ACP to the target lipoyl-domain
lysine, and LipA then converts the protein-bound octanoyl group to the mature
lipoyl group.

## Initial annotation decisions

The specific lipoate synthase activity and both immediate process annotations
are accepted. Cytoplasmic localization and 4Fe-4S cluster binding are retained
as non-core context. Generic catalytic activity, sulfurtransferase activity,
and generic iron-sulfur cluster binding are marked over-annotated because the
record already contains their more informative descendants.
