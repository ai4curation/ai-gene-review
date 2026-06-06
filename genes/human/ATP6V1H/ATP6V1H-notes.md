# ATP6V1H Research Notes

## Gene overview

ATP6V1H (UniProt Q9UI12) encodes V-type proton ATPase subunit H (483 amino acids, ~57 kDa), the regulatory subunit H of the V1 peripheral complex of the vacuolar H+-ATPase (V-ATPase). The protein is also known as NBP1 (Nef-binding protein 1) and VMA13 homolog.

There are two isoforms: isoform 1 (canonical, 483 AA) and isoform 2 (Q9UI12-2, differs at residues 176-193 due to VSP_012274).

## V-ATPase complex structure

The V-ATPase is a multi-subunit complex split into the cytoplasmic V1 domain (ATP hydrolysis) and the membrane-embedded V0 domain (proton translocation).

[PMID:9442887 "The peripheral V1 domain, a 500-kDa complex responsible for ATP hydrolysis, contains at least eight different subunits of molecular weight 70-13 (subunits A-H)."]

[PMID:33065002 "The V1 complex consists of three catalytic AB heterodimers that form a heterohexamer, three peripheral stalks each consisting of EG heterodimers, one central rotor including subunits D and F, and the regulatory subunits C and H"]

## Role of subunit H specifically

Subunit H is a regulatory subunit of V1, present as one copy. It is essential for V-ATPase activity but not assembly in yeast (VMA13). It is important for regulating the coupling of ATP hydrolysis to proton transport.

UniProt states: "Regulatory subunit of the V1 complex of vacuolar(H+)-ATPase (V-ATPase). The H subunit activates ATPase activity of the V1 subcomplex when dissociated from V0. It has been proposed to inhibit the non-productive hydrolysis of ATP when V1 is in a free state in the cytoplasm."

The H subunit (VMA13/Subunit H) has a unique regulatory role: in the free V1 complex (dissociated from V0), H inhibits futile ATP hydrolysis. When reassociated with V0, it activates the pump. This regulatory switch is important for the regulated disassembly mechanism.

## Interaction with AP-2 and endocytic machinery

A key non-V-ATPase function: subunit H (identified as NBP1) binds directly to AP-2 (specifically the medium chain mu2, AP2M1), connecting the V-ATPase to the clathrin-mediated endocytic machinery.

[PMID:12032142 "we demonstrate that V1H binds to the C-terminal flexible loop in Nef from HIV-1 and to the medium chain (mu2) of the adaptor protein complex 2 (AP-2) in vitro and in vivo. The interaction sites of V1H and mu2 were mapped to a central region in V1H from positions 133 to 363, which contains 4 armadillo repeats"]

[PMID:12032142 "V1H can function as an adaptor for interactions between Nef and AP-2."]

The biological significance of the V1H-AP2M1 interaction is established: it is not merely a pathogen-hijacking mechanism. The interaction occurs under normal cellular conditions and is part of the endocytic function of the V-ATPase complex on clathrin-coated vesicles.

## HIV Nef interaction

Subunit H (NBP1) was originally identified as the binding partner for HIV-1 Nef.

[PMID:9620685 "we identified the Nef binding protein 1 (NBP1), which interacts specifically with Nef in vitro and in vivo. Since it shares sequence similarity with the catalytic subunit of the vacuolar ATPase (V-ATPase) and complements the loss of this VMA13 gene in yeast, NBP1 is the human homolog of Vma13p."]

[PMID:11179428 "our data demonstrate how Nef contacts the endocytic machinery in the absence of its direct binding to AP-2 and suggest an important role for subunit H of the V-ATPase in viral infectivity."]

The Nef-H interaction hijacks the normal V1H-AP2 endocytic function to force CD4 internalization. This is a consequence of H's role as an adaptor connecting V-ATPase to AP-2.

## Subcellular localization

Subunit H is detected:
- At lysosomal membrane (HDA, PMID:17897319) — part of assembled V-ATPase
- In cytosol (IDA, GO_REF:0000052 immunofluorescence) — free V1 complex
- At Golgi, endosome, plasma membrane (NAS, PMID:32001091) — assembled V-ATPase at various membranes
- At clathrin-coated vesicle membrane (IEA, UniProt mapping) — consistent with AP-2 interaction

## Endocytosis annotation

GO:0006897 endocytosis (IDA, PMID:12032142) — the evidence is that V1H binds AP2M1 and Nef-V1H chimeras can internalize CD4. This demonstrates that V1H contributes to endocytosis via AP-2 interaction. This is a legitimate specific annotation beyond generic "protein binding."

## Regulation of macroautophagy (NAS, PMID:22982048)

As for ATP6V1G1, this annotation is an over-annotation. The cited paper uses V-ATPase disruption to impair lysosomal activity; it does not show that H subunit specifically regulates macroautophagy.

## Reactome annotations: Nef pathway

Multiple Reactome entries refer to the HIV Nef / CD4 internalization pathway via V-ATPase subunit H. These are placed at the cytosol because V1H bridges cytosolic Nef to AP-2. The localization to cytosol in these entries reflects the V1H function in this endocytic context, not primary V-ATPase localization.

## Vacuolar acidification / proton transport annotations

Multiple NAS annotations to vacuolar acidification, endosomal lumen acidification, Golgi lumen acidification, intracellular pH reduction, and proton transmembrane transport from PMID:32001091 and PMID:9442887. These are general review-based annotations for V-ATPase function and are appropriate as NAS.

## Summary

ATP6V1H is both a regulatory subunit of the V1 complex (directly modulating ATPase activity in free V1 versus assembled holoenzyme contexts) and a structural adaptor connecting the V-ATPase complex to the AP-2 endocytic machinery via armadillo repeat-mediated AP2M1 binding. The endocytic adaptor function is a legitimate core function of subunit H, distinct from generic V-ATPase proton pumping, and is exploited by HIV/SIV Nef.
