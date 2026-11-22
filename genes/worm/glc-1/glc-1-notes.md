# glc-1 review notes

## 2026-11-22

Fetched `worm glc-1` as the first GluCl/ivermectin target after the
levamisole-sensitive nAChR lane. The reviewed UniProt accession is `G5EBR3`,
matching WormBase `WBGene00001591` and ORF `F11A5.10`.

`just fetch-gene worm glc-1` seeded 25 GOA rows. The key direct support is the
Cully 1994 abstract, which reports Xenopus oocyte expression cloning of two
functional C. elegans cDNAs encoding an avermectin-sensitive glutamate-gated
chloride channel [PMID:7935817, "we used Xenopus oocytes for expression cloning
of two functional complementary DNAs encoding an avermectin-sensitive
glutamate-gated chloride channel"]. It is abstract-only in the local cache, but
that is enough for the chloride-channel molecular-function and process rows.

The Hibbs and Gouaux structures make GLC-1 an excellent structural anchor for
the ivermectin lane: they resolved a homopentameric GluClcryst channel with
an intersubunit transmembrane ivermectin site and a chloride pore, and then
showed that glutamate binds the purified homomer in an ivermectin-dependent
state [PMID:21572436, "In agreement with the electrophysiology experiments,
[3H]-L-glutamate binding requires ivermectin"]. Althoff et al. then supplied apo
and POPC-bound structures
[PMID:25143115, "We obtained three-dimensional crystals of GluCl in the absence
of ivermectin"].

Dent et al. is full text in the local cache and is the primary source behind
WormBase's avr-14/avr-15/glc-1 genetic-interaction summary: simultaneous loss of
the three GluCl alpha-subunit genes gives C. elegans high-level ivermectin
resistance [PMID:10716995, "simultaneous mutation of three genes, avr-14,
avr-15, and glc-1"]. Cook et al. is abstract-only but directly connects the C.
elegans GluCl set to ivermectin-sensitive locomotion and to the parasitic
nematode target system [PMID:16527366, "ivermectin exerts its paralytic action
on parasitic nematodes through activation of GluCl channels in the motor nervous
system"]. Ghosh et al. identify glc-1 as the major C. elegans natural
avermectin-resistance locus and show that a four-residue deletion in the CB4856
GLC-1 ligand-binding domain confers resistance [PMID:22301316, "a naturally
occurring four-amino-acid deletion in the ligand-binding domain of GLC-1"].
The two WormBase IGI partners in the glc-1 GOA are `WBGene00000232` = `avr-14`
and `WBGene00000233` = `avr-15`, resolved through the Alliance API rather than
by symbol memory.

The PTHR18945 family review was important for the PAINT rows. `PTN001055382` is
the anion-selective glycine/GluCl lineage and supports the chloride transport
IBA, while the same node should not send the excitatory channel term
`GO:0005231` to GLC-1.

Tried to generate a fast provider deep-research file with
`just deep-research-perplexity-lite worm glc-1` while addressing PR review
feedback, but the installed deep-research-client only exposed the `claude_code`
provider and `agentapi` was not available for that path. The Dent and Ghosh
primary papers were resolved through PubMed and added manually above.

Cross-checked the completed GluCl module after
`modules/nematode_glutamate_gated_chloride_channels.yaml` merged. The review's
core function and `GO:0008068` source-defect block already model GLC-1 as the
alpha subunit of a heteromeric GLC-1/GLC-2 extracellularly glutamate-gated
chloride channel, matching the module's `glc1_glc2_receptor` activity.
