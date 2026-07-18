# lipB curation notes

LipB/Q88DM4 is the endogenous-pathway octanoyltransferase. UniProt records
transfer of octanoate from octanoyl-ACP to lipoyl-domain lysine residues
[file:PSEPK/lipB/lipB-uniprot.txt, "CC   -!- FUNCTION: Catalyzes the transfer of endogenously produced octanoic acid"].
The entry belongs to the LipB octanoyltransferase family
[file:PSEPK/lipB/lipB-uniprot.txt, "DR   InterPro; IPR000544; Octanoyltransferase."].

For module boundaries, LipB supplies the protein-bound octanoyl intermediate
used by LipA. Lipoate-dependent dehydrogenase complexes and the glycine-cleavage
system are downstream clients, not catalytic parts of the lipoylation module.

## Initial annotation decisions

The specific lipoyl(octanoyl) transferase activity and protein-lipoylation
process are accepted. Cytoplasmic localization is retained as non-core context.
The generic acyltransferase parent is marked over-annotated because it adds no
information beside the substrate-specific term.

## OpenScientist assessment

The completed report supports the LipB identity, reaction, active-site family,
and direct LipB-to-LipA pathway order
[`file:PSEPK/lipB/lipB-deep-research-openscientist.md`]. It found no direct
biochemical study of Q88DM4 itself; confidence instead comes from the exact
HAMAP/InterPro assignment, conserved catalytic architecture, and strong
orthology to characterized LipB proteins. Claims about the detailed client
range, regulation, and salvage interplay remain hypotheses for KT2440 and are
not promoted into GO assertions.
