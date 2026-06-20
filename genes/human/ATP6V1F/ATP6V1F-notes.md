# ATP6V1F Research Notes

## Gene Identity
- UniProt: Q16864 (VATF_HUMAN)
- Gene symbol: ATP6V1F (also known as ATP6S14, VATF)
- Protein: V-type proton ATPase subunit F; 119 amino acids, ~13 kDa (the smallest V1 subunit)
- Two isoforms from alternative splicing (Q16864-1, Q16864-2)

## Core V-ATPase Biology

ATP6V1F encodes the F subunit of the V1 peripheral sector of the vacuolar-type H+-ATPase (V-ATPase). Together with subunit D, subunit F forms the central rotor of V1 that transmits ATP hydrolysis energy to rotate the V0 proteolipid ring, driving proton translocation.

[PMID:18752060 "Energy from this reaction drives the rotation of a central stalk consisting of V1 subunits D and F and this is coupled to rotation of the V0 proteolipid ring made up of c, c′ and c″."]

[PMID:33065002 "The V1 complex consists of three catalytic AB heterodimers that form a heterohexamer, three peripheral stalks each consisting of EG heterodimers, one central rotor including subunits D and F, and the regulatory subunits C and H"]

Smith et al. (2008) directly demonstrated that human subunit F interacts with the V0 d subunit, confirming its central stalk position:

[PMID:18752060 "d2-GST (250µg) or GST (100µg), which had been immobilized on Glutathione Sepharose 4B in 1× PBS by incubation at 4°C for 2h. The samples were incubated on a spiramixer at 4°C overnight. Unbound proteins were removed by washing twice with buffer A"]

## Original Cloning

Subunit F (14 kDa) was cloned from human fetal brain by Fujiwara et al. (1995). Northern blot analysis showed ubiquitous expression across human tissues.

[PMID:8581736 "A single 0.8-kb band was detected in various human tissues by Northern blot analysis. Since the human 14-kDa subunit is expressed ubiquitously, it might be a housekeeping protein."]

[PMID:8581736 "A cDNA encoding the 14-kDa subunit of vacuolar ATPase was cloned from human fetal brain."]

## Subcellular Localization

- Primary: lysosomal membrane, as part of the V-ATPase complex on the cytoplasmic face of acidic organelle membranes
- Also: Golgi membrane, endosome membrane, plasma membrane (in specialized cells), clathrin-coated vesicle membrane, synaptic vesicle membrane

As a V1 peripheral complex subunit, the cytoplasmic face (cytosol) is the functional location.

## Structural Data

Subunit F is present in all four cryo-EM structures of the complete human V-ATPase (PDB: 6WLZ, 6WM2, 6WM3, 6WM4; PMID:33065002), chain N, at near-atomic resolution. The structure confirms its position in the central rotor of V1.

## Interaction with ATP6V1D

The F subunit directly interacts with subunit D (ATP6V1D) as shown by IntAct (NbExp=7, EBI-714690 x EBI-2684998) and by biochemical pulldowns (PMID:18752060). This D-F pair constitutes the central stalk of V1.

## Curation Notes

- "Protein binding" annotations (IPI from PMID:32296183, PMID:33961781, PMID:35271311) are from high-throughput interactome studies and represent generic protein-protein interaction data with no functional specificity.
- The protein binding annotation from PMID:18752060 (IPI) reflects a specific, functionally important interaction between subunit F and the V0 d subunit (ATP6V0D1), which is mechanistically central to the rotary pump mechanism.
- "Monoatomic ion transmembrane transport" (GO:0034220, IEA) is an appropriate but potentially redundant term given the more specific "proton transmembrane transport" (GO:1902600).
- The extracellular exosome (HDA) annotations are from proteomics surveys; subunit F has no known function outside the V-ATPase complex.
- There is no dedicated disease association for ATP6V1F specifically (unlike ATP6V1E1 which causes ARCL2C), though V-ATPase dysfunction in general causes multiple disorders.
- The ATPase-coupled ion transmembrane transporter activity (GO:0042625, NAS from PMID:8581736) and proton transmembrane transporter activity (GO:0015078, NAS from PMID:8581736) annotations are from the original cloning paper and are appropriate for a V-ATPase subunit contributing to overall complex activity.
