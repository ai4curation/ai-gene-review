# ATP6V1G1 Research Notes

## Gene overview

ATP6V1G1 (UniProt O75348) encodes V-type proton ATPase subunit G 1, a 118 amino acid peripheral subunit (13.8 kDa) that is a component of the V1 peripheral complex of the vacuolar H+-ATPase (V-ATPase). The protein is also known as V-ATPase 13 kDa subunit 1 and Vacuolar proton pump subunit G 1.

## V-ATPase complex function

V-ATPases are ATP-hydrolysis-driven proton pumps that acidify intracellular compartments across all eukaryotes.

[PMID:33065002 "Vesicular- or vacuolar-type adenosine triphosphatases (V-ATPases) are ATP-driven proton pumps comprised of a cytoplasmic V1 complex for ATP hydrolysis and a membrane-embedded Vo complex for proton transfer. They play important roles in acidification of intracellular vesicles, organelles, and the extracellular milieu in eukaryotes."]

[PMID:9442887 "The vacuolar (H+)-ATPases (or V-ATPases) function in the acidification of intracellular compartments in eukaryotic cells. The V-ATPases are multisubunit complexes composed of two functional domains. The peripheral V1 domain, a 500-kDa complex responsible for ATP hydrolysis, contains at least eight different subunits of molecular weight 70-13 (subunits A-H). The integral V0 domain, a 250-kDa complex, functions in proton translocation and contains at least five different subunits of molecular weight 100-17 (subunits a-d)."]

## Role of subunit G 1 specifically

Subunit G 1 is one of three G-subunit paralogs in humans (G1, G2, G3). G1 is ubiquitously expressed.

The V1 complex contains three peripheral stalks, each consisting of EG heterodimers.
[PMID:33065002 "The V1 complex consists of three catalytic AB heterodimers that form a heterohexamer, three peripheral stalks each consisting of EG heterodimers, one central rotor including subunits D and F, and the regulatory subunits C and H"]

The G subunit forms heterodimers with the E subunit, and these peripheral stalks link V1 to V0.
[PMID:17360703 "This confirms that a4 and G3 are component subunits of the same proton pump and explains the observed epitope masking. This interaction was also found to be a more general feature of human H(+)-ATPases, as similar G1/a1, G3/a1, and G1/a4 interactions were also demonstrated. These interactions represent a novel link between the V(1) and V(0) domains in man, which is known to be required for H(+)-ATPase assembly and regulation."]

UniProt notes the G1 subunit has been directly identified by mass spectrometry in the V1 complex of the human V-ATPase structure.
[file:human/ATP6V1G1/ATP6V1G1-uniprot.txt "Subunit of the V1 complex of vacuolar(H+)-ATPase (V-ATPase), a multisubunit enzyme composed of a peripheral complex (V1) that hydrolyzes ATP and a membrane integral complex (V0) that translocates protons"]

## Role in iron homeostasis / HIF pathway

A key functional study showed that loss of ATP6V1G1 (identified in a genome-wide screen) impairs V-ATPase activity, leading to iron depletion and HIF1alpha stabilization.
[PMID:28296633 "we identify that genetic disruption of the Vacuolar H+ ATPase (V-ATPase), the key proton pump for endo-lysosomal acidification, and two previously uncharacterised V-ATPase assembly factors, TMEM199 and CCDC115, stabilise HIF1α in aerobic conditions. Rather than preventing the lysosomal degradation of HIF1α, disrupting the V-ATPase results in intracellular iron depletion, thereby impairing PHD activity and leading to HIF activation."]

[PMID:28296633 "the top ranked biological process was transferrin transport and V-ATPase function, principally relating to mutagenesis of genes encoding five V-ATPase subunits: ATP6AP1, ATP6V1A, ATP6V1G1, ATP6V0A2 and ATP6V0D1"]

This places intracellular iron homeostasis as a downstream consequence of V-ATPase activity (proton pump function needed for endosomal acidification and iron release from transferrin).

## Subcellular localization

UniProt lists apical cell membrane in kidney, based on co-localization with other H+-ATPase subunits in TAL and DCT segments.
[PMID:29993276 "Furthermore, the H+-ATPase B1 subunit colocalized with other H+-ATPase subunits in the TAL and DCT."]

Also detected in lysosomal membrane (HDA, mass spec from lysosome-enriched fractions) and in cytosol (as component of unassembled V1 complex). Identification in extracellular exosomes is likely a contaminant in those datasets and is non-core.

## Regulation of macroautophagy

A NAS annotation links V-ATPase (including ATP6V1G1) to regulation of macroautophagy. This is an indirect/downstream effect of lysosomal acidification — V-ATPase activity is required for lysosomal function and thus autophagy completion, but the G1 subunit does not directly regulate autophagy.
[PMID:22982048 "macroautophagy is responsible for the uptake of lipofuscin into the lysosomes" — here V-ATPase disruption is used to impair lysosomal activity]

## Protein binding annotations

Multiple high-throughput interactome datasets contribute generic protein binding annotations (GO:0005515) for ATP6V1G1. These should all be treated as over-annotations. The specific functional interaction is with ATP6V1E1/E2 (forming G-E peripheral stalks).
[file:human/ATP6V1G1/ATP6V1G1-uniprot.txt "O75348; P36543: ATP6V1E1; NbExp=3; IntAct=EBI-711802, EBI-348639; O75348; Q96A05: ATP6V1E2; NbExp=12; IntAct=EBI-711802, EBI-8650380"]

The ATPase binding annotation (PMID:17360703) reflects the G1/a (V0 subunit a) interaction documented in that paper — this is more informative than generic protein binding.

## Summary of core function

ATP6V1G1 is a structural peripheral stalk subunit of the V1 complex of the V-ATPase. Its core function is as part of the proton-transporting ATPase complex. Annotations to V1 domain membership, proton transmembrane transport, and lysosomal/endosomal membrane localization are all well-supported. The iron homeostasis and HIF pathway effects are downstream consequences of V-ATPase proton pump activity rather than direct molecular functions of the G1 subunit per se.
