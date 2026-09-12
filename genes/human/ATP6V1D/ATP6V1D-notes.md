# ATP6V1D Research Notes

## Gene Identity
- UniProt: Q9Y5K8 (VATD_HUMAN)
- Gene symbol: ATP6V1D (also known as ATP6M, VATD)
- Protein: V-type proton ATPase subunit D; 247 amino acids, ~28 kDa

## Core V-ATPase Biology

ATP6V1D encodes the D subunit of the V1 peripheral sector of the vacuolar-type H+-ATPase (V-ATPase). This is a ubiquitously expressed, evolutionarily conserved subunit that forms part of the central rotor of the V1 domain.

[PMID:18752060 "Energy from this reaction drives the rotation of a central stalk consisting of V1 subunits D and F and this is coupled to rotation of the V0 proteolipid ring made up of c, c′ and c″."]

The cryo-EM structure of the complete human V-ATPase (Wang et al. 2020) places subunit D as one of two central rotor subunits (D and F) that transmit ATP hydrolysis energy from the catalytic head to the V0 ring.

[PMID:33065002 "The V1 complex consists of three catalytic AB heterodimers that form a heterohexamer, three peripheral stalks each consisting of EG heterodimers, one central rotor including subunits D and F, and the regulatory subunits C and H"]

Smith et al. (2008) directly demonstrated that the human D subunit physically interacts with the V0 d subunit (d1 and d2) and with subunit F, establishing that subunit D forms part of the central stalk in man:

[PMID:18752060 "each can pull down the central stalk's D and F subunits from human kidney membrane, and in vitro studies using D and F further showed that the interactions between these proteins and the d subunit is direct. These data indicate that the d subunit in man is centrally located within the pump and is thus important in its rotary mechanism."]

## Role in mTORC1 Amino Acid Sensing

Zoncu et al. (2011) demonstrated that the V-ATPase is required for mTORC1 activation by amino acids through an inside-out mechanism. The V1 subunit D directly contacts the Ragulator complex:

[PMID:22053050 "the V1 component D with p18 and, to a lesser degree, with p14 (Fig. 3D). No direct interactions were detected between the Rag GTPases and purified v-ATPase subunits"]

[PMID:22053050 "the v-ATPase engages in extensive amino acid-sensitive interactions with the Ragulator, a scaffolding complex that anchors the Rag GTPases to the lysosome"]

[PMID:22053050 "amino acid starvation and stimulation strengthened and weakened, respectively, the interaction"]

The V-ATPase acts upstream of the Rag GTPases and its ATP hydrolysis (not just the proton gradient) is required for amino acid signaling:

[PMID:22053050 "ATP hydrolysis and the associated rotation of the v-ATPase appear to be essential to relay an amino acid signal from the lysosomal lumen to the Rag GTPases, whereas the capacity of the v-ATPase to set up the lysosomal proton gradient is dispensable."]

## Subcellular Localization

- Primary: lysosomal membrane (as part of V-ATPase complex on lysosomes)
- Also documented on: Golgi, endosomes, plasma membrane (in some cell types), clathrin-coated vesicles
- Notably, ATP6V1D also localizes to centrosome and cilia base (via SNX10 interaction)

[PMID:21844891 "SNX10 interacts with V-ATPase complex and targets it to the centrosome where ciliogenesis is initiated."]
[PMID:21844891 "SNX10/V-ATPase regulate the ciliary trafficking of Rab8a, which is a critical regulator of ciliary membrane extension."]

## Ciliogenesis Role

ATP6V1D (with the whole V-ATPase complex) was found required for ciliogenesis in vitro. Its interaction with sorting nexin SNX10 targets V-ATPase to the centrosome.

[PMID:21844891 "V-ATPase regulates ciliogenesis in vitro and in vivo and does so synergistically with SNX10"]

This is a secondary function relative to the primary proton-pump/acidification role. The ciliogenesis role appears to operate through V-ATPase's vesicular trafficking/acidification function rather than being independent.

## V-ATPase Structure (Human)

[PMID:33065002 "Vesicular- or vacuolar-type adenosine triphosphatases (V-ATPases) are ATP-driven proton pumps comprised of a cytoplasmic V1 complex for ATP hydrolysis and a membrane-embedded Vo complex for proton transfer."]

[PMID:33065002 "They play important roles in acidification of intracellular vesicles, organelles, and the extracellular milieu in eukaryotes."]

## Regulation of Macroautophagy

V-ATPase is broadly required for lysosomal function and autophagy. The annotation to "regulation of macroautophagy" (PMID:22982048) is an indirect inference; direct evidence for a specific regulatory function of subunit D in macroautophagy control, beyond its role in lysosomal acidification, is lacking.

[PMID:22982048 - abstract only; NAS annotation from ParkinsonsUK-UCL - indirect/downstream effect of lysosomal acidification function]

## Curation Notes

- The annotations to guanyl nucleotide exchange factor activator activity (GO:0160124) and positive regulation of TORC1 signaling (GO:1904263) from PMID:22053050 reflect a genuine secondary function: the V-ATPase complex (specifically V1-Ragulator interaction involving subunit D) acts upstream of Rag GTPase activation in the mTORC1 amino acid sensing pathway.
- The cytosol annotations (multiple Reactome TAS) are consistent with the fact that the V1 domain is a peripheral complex on the cytoplasmic face of membranes.
- Extracellular exosome (HDA) annotations from proteomics studies are technically valid observations but represent non-functional localization data for a structural component that may co-purify with exosome membrane fragments.
- Cilium and centrosome annotations (IDA from PMID:21844891) are supported but represent a secondary function.

## Falcon deep research synthesis (2026-06-21)

Falcon deep research has now completed (`file:human/ATP6V1D/ATP6V1D-deep-research-falcon.md`,
21 citations). It corroborates the central-rotor core above and adds general
V-ATPase regulatory detail; no change to annotation calls.

- **Core confirmed.** D is one of the two **central-rotor (central-stalk)**
  subunits (with F); it transmits torque from A3B3 ATP hydrolysis to the V0
  proteolipid ring, coupling chemistry to proton translocation. Ubiquitous,
  essential, not catalytic. No change to the rotor/proton-transport-coupling calls.
- **Reversible-assembly regulation (Sava 2024; Ratto 2022).** In continuously fed
  mammalian cells, V1–V0 assembly/disassembly occurs during the lysosome
  regeneration cycle with rapid cytosolic↔membrane exchange of V1 subunits,
  distinct from amino-acid-depletion control and **not requiring mTORC1 changes**
  in the fed state. Relevant regulatory context for the PN regulation branch.
- **Mode-switching (Kosmidis 2022).** Single mammalian-brain V-ATPase stochastically
  switches between proton-pumping, inactive, and proton-leaky modes, tuned by ATP
  and the electrochemical proton gradient — affecting vesicle-acidification and
  neurotransmitter-loading dynamics. Mechanistic context, not a D-specific MF.
- **Disease.** No ATP6V1D-specific Mendelian disease reported; the section is
  generic V-ATPase (neurodegeneration, dRTA, osteopetrosis via a3, cancer).
  Non-core context.

Net: no change to calls — D is the ubiquitous central-rotor V1 subunit coupling
ATP hydrolysis to proton translocation.
