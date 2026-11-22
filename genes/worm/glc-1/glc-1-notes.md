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
extracellular glutamate sites, an intersubunit transmembrane ivermectin site and
a chloride pore [PMID:21572436, "Ivermectin is bound at each of the GluClcryst
subunit interfaces in the TM domain whereas glutamate electron density is
present in all five of the classical neurotransmitter binding sites in the
ECD"]. Althoff et al. then supplied apo and POPC-bound structures
[PMID:25143115, "We obtained three-dimensional crystals of GluCl in the absence
of ivermectin"].

Cook et al. is also abstract-only but directly connects the C. elegans GluCl
set to ivermectin-sensitive locomotion and to the parasitic nematode target
system [PMID:16527366, "ivermectin exerts its paralytic action on parasitic
nematodes through activation of GluCl channels in the motor nervous system"].
The two WormBase IGI partners in the glc-1 GOA are `WBGene00000232` = `avr-14`
and `WBGene00000233` = `avr-15`, resolved through the Alliance API rather than
by symbol memory.

The PTHR18945 family review was important for the PAINT rows. `PTN001055382` is
the anion-selective glycine/GluCl lineage and supports the chloride transport
IBA, while the same node should not send the excitatory channel term
`GO:0005231` to GLC-1.
