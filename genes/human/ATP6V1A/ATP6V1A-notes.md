# ATP6V1A Research Notes

## Gene overview

ATP6V1A encodes the catalytic A subunit (V1A, also known as the 70 kDa or alpha subunit) of the V1 peripheral domain of the vacuolar-type H+-ATPase (V-ATPase). The V1 domain is the ATP-hydrolyzing sector of the proton pump; subunit A forms the catalytic AB heterodimer (three copies per V1 hexamer) together with subunit B and contains the nucleotide-binding/hydrolysis site.

## Core function — proton-transporting ATPase

The primary role of ATP6V1A is to hydrolyze ATP and power proton translocation across the membranes of intracellular organelles (lysosomes, endosomes, Golgi, secretory vesicles) and, in specialized cells, the plasma membrane.

[PMID:32001091 "V-ATPases are the primary source of organellar acidification in all eukaryotes, making them essential for many fundamental cellular processes."]

[PMID:33065002 "Vesicular- or vacuolar-type adenosine triphosphatases (V-ATPases) are ATP-driven proton pumps comprised of a cytoplasmic V1 complex for ATP hydrolysis and a membrane-embedded Vo complex for proton transfer."]

[PMID:8463241 "Subunit A is thought to be the main component of the catalytic site of the vacuolar-type H(+)-ATPase."]

## Complex assembly and structure

The complete human V-ATPase structure was determined by cryo-EM (Wang et al. 2020, PMID:33065002). The V1 complex consists of three catalytic AB heterodimers forming a heterohexamer, three EG peripheral stalks, one central rotor (subunits D and F), and regulatory subunits C and H. ATP hydrolysis by subunit A (the catalytic subunit) at the AB interface drives rotation of the central rotor, which in turn drives proton translocation through the V0 ring.

[PMID:33065002 "The V1 ATPase is composed of three copies of subunits A, B, E, and G, and one copy of subunit C, D, F, and H."]

## mTORC1 lysosomal amino acid sensing

The V-ATPase (including the V1A subunit) is required for amino acid sensing by mTORC1 at the lysosome surface. This is mediated through interactions of the V1 domain with the Ragulator complex in an amino acid-sensitive manner, allowing mTORC1 recruitment and activation.

[PMID:22053050 "We found that the vacuolar H(+)-adenosine triphosphatase ATPase (v-ATPase) is necessary for amino acids to activate mTORC1."]

[PMID:22053050 "The v-ATPase engages in extensive amino acid-sensitive interactions with the Ragulator, a scaffolding complex that anchors the Rag GTPases to the lysosome."]

[PMID:22053050 "These results identify the v-ATPase as a component of the mTOR pathway and delineate a lysosome-associated machinery for amino acid sensing."]

## Iron homeostasis and HIF1A regulation

V-ATPase function (including ATP6V1A) is required for intracellular iron homeostasis. Loss of V-ATPase activity leads to intracellular iron depletion, reduced PHD activity, and HIF1A stabilization under aerobic conditions.

[PMID:28296633 "we identify that genetic disruption of the Vacuolar H+ ATPase (V-ATPase), the key proton pump for endo-lysosomal acidification, and two previously uncharacterised V-ATPase assembly factors, TMEM199 and CCDC115, stabilise HIF1α in aerobic conditions."]

[PMID:28296633 "disrupting the V-ATPase results in intracellular iron depletion, thereby impairing PHD activity and leading to HIF activation."]

## Regulation of macroautophagy

V-ATPase acidification of lysosomes is required for autophagic flux. The annotation linking V-ATPase to regulation of macroautophagy comes from a study on lipofuscin formation (PMID:22982048), where lysosomal activity inhibition was a secondary experimental variable.

## Interaction with WFS1

ATP6V1A interacts with WFS1 (Wolfram syndrome 1 protein) in secretory granules in neuroblastoma cells. WFS1 regulates the expression and stability of the V1A subunit.

[PMID:23035048 "We demonstrated a novel interaction between WFS1 and the V1A subunit of the H(+) V-ATPase (proton pump) by co-immunoprecipitation in human embryonic kidney (HEK) 293 cells and with endogenous proteins in human neuroblastoma cells."]

## Disease associations

**ARCL2D (autosomal recessive cutis laxa type 2D, MIM:617403)**: Caused by biallelic loss-of-function variants in ATP6V1A. Manifests as skin wrinkling, large fontanelle, facial appearance, hypotonia, cardiovascular and neurologic involvement.

**IECEE3 (infantile/early childhood epileptic encephalopathy 3, MIM:618012)**: Caused by dominant (de novo) heterozygous missense mutations. De novo mutations p.Pro27Arg, p.Asp100Tyr, p.Asp349Asn, p.Asp371Gly identified in patients with developmental encephalopathy with epilepsy.

[PMID:29668857 "we identified de novo heterozygous mutations (p.Pro27Arg, p.Asp100Tyr, p.Asp349Asn, p.Asp371Gly) in ATP6V1A, encoding the A subunit of v-ATPase, in four patients with developmental encephalopathy with epilepsy."]

[PMID:29668857 "both mutations caused a similar defect in neurite elongation accompanied by loss of excitatory inputs, revealing that altered lysosomal homeostasis markedly affects neurite development and synaptic connectivity."]

## Subcellular localization

ATP6V1A is a peripheral membrane protein of the V1 domain. It is found at lysosomal membrane (is_active_in), secretory granules (co-localizes with WFS1 in neuroblastoma), and the cytosol (V1 domain can reversibly dissociate from V0). Presence in cytoplasm reflects the known regulated V1-V0 disassembly mechanism (e.g., under nutrient deprivation). Some GO annotations cite plasma membrane localization from specific cell types (e.g., osteoclasts). Extracellular exosome annotations are from high-throughput proteomics studies.

## Microbial infection note

ATP6V1A facilitates Rabies virus uncoating in endosomes through interaction with the viral M protein. This is a host-pathogen interaction rather than a core cellular function.

[PMID:33208464 "ATP6V1A facilitated RABV replication. We further found that ATP6V1A was involved in the dissociation of incoming viral M proteins during viral uncoating."]

## Annotation quality notes

- Multiple cytosol annotations from Reactome (TAS) reflect the reversible disassembly of V1 from V0 membrane complex — these are valid but non-core cellular context annotations rather than the primary functional localization.
- Protein binding (GO:0005515) annotations from interaction studies should be MARK_AS_OVER_ANNOTATED.
- The NAS annotations from ComplexPortal (PMID:32001091) for multiple acidification processes are valid and core.
- Regulation of macroautophagy (NAS, PMID:22982048) is an indirect effect of lysosome function; the paper studied lipofuscin, not V-ATPase function per se.
- The guanyl nucleotide exchange factor activator activity (GO:0160124) annotation from the PMID:22053050 mTORC1 paper captures the functional role of V-ATPase in activating Rag GTPase GEF activity (Ragulator) — this is a legitimate but non-core moonlighting function.
