# ATP6V1C1 Research Notes

## Gene overview

ATP6V1C1 encodes the C1 subunit of the V1 peripheral domain of the vacuolar-type H+-ATPase (V-ATPase). The C subunit (also called subunit C or subunit C1) is a regulatory subunit of the V1 complex, present in a single copy per V1 complex. ATP6V1C1 is one of two isoforms of the C subunit; the other is ATP6V1C2, which is expressed specifically in testes.

## Core function — V-ATPase regulatory C subunit

Subunit C is necessary for assembly of the catalytic sector (V1) of V-ATPase and is likely to have a specific function in its catalytic activity. Structural data from the complete human V-ATPase places C in the V1 complex along with subunits A, B, D, E, F, G, and H.

[PMID:33065002 "The V 1 ATPase is composed of three copies of subunits A, B, E, and G, and one copy of subunit C, D, F, and H"]

[file:human/ATP6V1C1/ATP6V1C1-uniprot.txt "Subunit C is necessary for the assembly of the catalytic sector of the enzyme and is likely to have a specific function in its catalytic activity"]

## Tissue specificity

ATP6V1C1 is ubiquitously expressed. The C2 paralog (ATP6V1C2) has a more restricted expression pattern in testes.

[PMID:12384298 - "Molecular cloning and characterization of novel tissue-specific isoforms of the human vacuolar H(+)-ATPase C, G and d subunits"]
[file:human/ATP6V1C1/ATP6V1C1-uniprot.txt "Ubiquitous."]

## Discovery and cloning

ATP6V1C1 was originally cloned from human osteoclastoma tissue (PMID:8250920). The abstract notes: "The catalytic site of the V-ATPase consists of a hexamer of three A subunits and three B subunits which bind and hydrolyse ATP and are regulated by accessory subunits C, D and E."

[PMID:8250920 "are regulated by accessory subunits C, D and E. cDNAs encoding subunits C, D, and E were cloned from human osteoclastoma"]

## Interaction with ARF6/ARNO

ATP6V1C1 interacts with ARF6 (ADP-ribosylation factor 6) as shown in UniProt INTERACTION records (IntAct EBI-988663, EBI-638181; NbExp=4). This interaction was identified in the context of the V-ATPase/ARNO/Arf6 system in early endosomes (PMID:16415858). 

Note: The PMID:16415858 paper reports that Arf6 interacts with the c-subunit (V0 c-subunit, not V1 C subunit) and ARNO interacts with the a2-isoform of V-ATPase. The protein binding annotation for ATP6V1C1 from PMID:16415858 may reflect the broader V-ATPase complex interaction rather than a specific direct interaction of V1 C subunit with ARNO/Arf6.

[PMID:16415858 "The recruitment of the small GTPase Arf6 and ARNO from cytosol to endosomal membranes is driven by V-ATPase-dependent intra-endosomal acidification."]

## Subcellular localizations

ATP6V1C1 is found at:
- Synaptic vesicle membrane (by similarity with rat C subunit)
- Clathrin-coated vesicle membrane (by similarity with rat C subunit)
- Lysosomal membrane (detected by proteomics, PMID:17897319)
- Cytosol (during V1-V0 disassembly)

## Annotation quality notes

- Protein binding (GO:0005515) IPI from PMID:16415858 should be MARK_AS_OVER_ANNOTATED. The specific functional interaction with ARF6/ARNO involves the V0 c-subunit and a2 isoform; the C subunit involvement is via the intact V-ATPase complex.
- Membrane (GO:0016020) from ARBA IEA is over-annotated (too broad); better captured by specific compartment terms.
- Regulation of macroautophagy (NAS, PMID:22982048) is an indirect effect of lysosomal acidification.
- Extracellular exosome (HDA, PMID:19056867) likely reflects contamination.
- Multiple Reactome TAS annotations for cytosol reflect V1-V0 disassembly; valid but non-core.
- The TAS annotations from PMID:8250920 provide the original characterization of the C subunit as part of V-ATPase.
