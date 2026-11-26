# EXOSC8 notes

EXOSC8/RRP43/OIP2 is one of the six RNase PH-like subunits in the human Exo-9 RNA exosome core. EXOSC8 pairs with EXOSC5/RRP46 in the heterohexameric PH-like ring and acts as a non-catalytic scaffold for the associated DIS3, DIS3L and EXOSC10/RRP6 ribonucleases [PMID:20531389, "The nine-subunit core of the eukaryotic exosome is catalytically inactive and may have an architectural function and mediate substrate binding."].

EXOSC8 is directly supported as an AU-rich RNA-binding protein. Anderson et al. tested human exosome RNase PH domains and found that OIP2/EXOSC8, PM-Scl-75/EXOSC9, and RRP41/EXOSC4 could bind AU-rich elements [PMID:16912217, "RNase PH domains from two other exosomal components, OIP2 and RRP41, as well as from Escherichia coli polynucleotide phosphorylase, are all capable of specifically interacting with RNAs containing an AU-rich element"]. The GO:0035925 IBA therefore lands on EXOSC8 correctly even though the PAINT IBD sits too high and also reaches EXOSC7.

The UniProt Neisseria OpaP note was weighed but is not represented in GOA. It is a pathogen-host Y2H interaction with a bacterial outer-membrane protein and is not part of the conserved RNA exosome role.

The many EXOSC8 bare GO:0005515 IPI rows are high-throughput interactions, mostly from IntAct. They stay as separate rows with their individual WITH/FROM partners under the one-row-per-GOA-row rule and are removed only because bare protein binding is uninformative.

No production GO-CAM in `gocams/index.tsv` names EXOSC8, and no family-specific two-part module fits the three RNase PH-like scaffold paralogs better than the existing ComplexPortal and Reactome descriptions of the larger RNA exosome.
