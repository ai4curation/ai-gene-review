# ATP6V0D1 manual deep research fallback

Falcon deep research was attempted for human ATP6V0D1 on 2026-06-03 with `perplexity-lite` fallback. Falcon timed out after 600 seconds, and the fallback failed because the Perplexity API returned a 401 quota error. This manually written fallback summarizes the local evidence used for curation.

## Identity and core role

ATP6V0D1 encodes V-type proton ATPase subunit d 1, also called V-ATPase AC39/p39. UniProt places it in the V-ATPase V0D/AC39 family and describes it as a V0-complex subunit of the vacuolar H(+)-ATPase. The protein is a peripheral membrane component on the cytoplasmic side of endolysosomal membranes and is present in V-ATPase complexes that acidify intracellular compartments [file:human/ATP6V0D1/ATP6V0D1-uniprot.txt, "Subunit of the V0 complex of vacuolar(H+)-ATPase (V-ATPase)"; file:human/ATP6V0D1/ATP6V0D1-uniprot.txt, "V-ATPase is responsible for acidifying and maintaining the pH of intracellular compartments"].

The shared d-subunit experimental paper cloned human ATP6V0D1/d1 and ATP6V0D2/d2 and showed that each interacts with V1 central-stalk D and F subunits. The abstract states that d1 and d2 can pull down D and F, that the interactions are direct, and that the d subunit is centrally located in the pump rotary mechanism [PMID:18752060, "human d1 and d2 are able to directly interact with the D and F subunits"; PMID:18752060, "the d subunit in man is centrally located within the pump"].

Cryo-EM structures of complete human V-ATPase support the same interpretation at complex level: V-ATPases are ATP-driven proton pumps with cytoplasmic V1 ATP hydrolysis and membrane-embedded Vo proton transfer sectors, and human structures were solved in multiple rotational states [PMID:33065002, "V-ATPases are ATP-driven proton pumps comprised of a cytoplasmic V1 complex for ATP hydrolysis and a membrane-embedded Vo complex for proton transfer"; PMID:33065002, "human V-ATPase in three rotational states"].

## Signaling and stress-response outputs

V-ATPase has a direct lysosomal amino-acid sensing role upstream of mTORC1. The mTORC1 paper reports that V-ATPase is necessary for amino acids to activate mTORC1, that Ragulator co-immunoprecipitates with endogenous V0 d1 and other V-ATPase subunits, and that purified V0 d1 directly interacts with Ragulator p18 [PMID:22053050, "v-ATPase is necessary for amino acids to activate mTORC1"; PMID:22053050, "direct interaction between the V0 component d1 and p18"]. This supports ATP6V0D1 involvement in amino-acid-stimulated TORC1 signaling as a non-core signaling output of the lysosomal V-ATPase.

ATP6V0D1 is also implicated in HIF1A regulation through V-ATPase-dependent iron handling. A haploid genetic screen identified ATP6V0D1 among five V-ATPase subunits whose disruption increased HIF1A reporter levels, and the paper concludes that V-ATPase disruption causes intracellular iron depletion, impairing PHD activity [PMID:28296633, "five V-ATPase subunits: ATP6AP1, ATP6V1A, ATP6V1G1, ATP6V0A2 and ATP6V0D1"; PMID:28296633, "disrupting the V-ATPase results in intracellular iron depletion"]. This supports intracellular iron homeostasis/HIF context as non-core relative to the primary proton-pump role.

## PN projection decision

For the Proteostasis PN batch, ATP6V0D1 should be projected conservatively as an endolysosomal V-ATPase subunit that maintains acidic lysosomal/endosomal compartments required for lysosome-dependent degradation and signaling. It should not be treated as a direct protein-folding, chaperone, ubiquitin-proteasome, or general macroautophagy regulator. The existing macroautophagy annotation is weak for ATP6V0D1 specifically and should be marked over-annotated rather than used as the principal PN evidence.
