# ATP6V0D1 notes

## Local evidence reviewed

- `just fetch-gene human ATP6V0D1` created the UniProt record, GOA table, review stub, and cached publication set. GOA seeded 60 review entries from 65 fetched annotations.
- `just deep-research-falcon human ATP6V0D1 --fallback perplexity-lite` was run on 2026-06-03. Falcon timed out after 600 seconds. The configured fallback then failed with a Perplexity API 401 quota error, so no provider-generated deep research file was produced.
- This manual fallback review uses local UniProt, GOA, cached publications, Reactome entries, and PN-context curation. A separate `ATP6V0D1-deep-research-manual.md` file summarizes the evidence used for the review.
- UniProt describes ATP6V0D1 as V-type proton ATPase subunit d 1, a V0-sector subunit of the V-ATPase that acidifies intracellular compartments [file:human/ATP6V0D1/ATP6V0D1-uniprot.txt, "V-ATPase is responsible for acidifying and maintaining the pH of intracellular compartments"].
- The human d-subunit paper supports the core complex/mechanism call: human d1 and d2 pull down V1 D and F subunits and the d subunit is centrally located in the pump rotary mechanism [PMID:18752060, "human d1 and d2 are able to directly interact with the D and F subunits"; PMID:18752060, "the d subunit in man is centrally located within the pump"].
- Human V-ATPase cryo-EM supports treating ATP6V0D1 as part of the assembled proton pump rather than as an independent enzyme [PMID:33065002, "V-ATPases are ATP-driven proton pumps comprised of a cytoplasmic V1 complex for ATP hydrolysis and a membrane-embedded Vo complex for proton transfer"].
- The mTORC1 amino-acid sensing paper supports a lysosomal signaling output of V-ATPase: the V-ATPase is necessary for amino acids to activate mTORC1 and provides a physical/functional link to Ragulator/Rag GTPases [PMID:22053050, "the vacuolar H(+)-adenosine triphosphatase ATPase (v-ATPase) is necessary for amino acids to activate mTORC1"; PMID:22053050, "Ragulator provides a physical and functional link between the v-ATPase and the Rag GTPases"].
- The HIF/iron paper directly includes ATP6V0D1 among V-ATPase genes whose disruption stabilizes HIF1A in aerobic conditions via intracellular iron depletion [PMID:28296633, "five V-ATPase subunits: ATP6AP1, ATP6V1A, ATP6V1G1, ATP6V0A2 and ATP6V0D1"; PMID:28296633, "disrupting the V-ATPase results in intracellular iron depletion"].
- The SNX10/ciliogenesis row is supported only as a V-ATPase-dependent trafficking context, not as the core ATP6V0D1 function [PMID:21844891, "SNX10 interacts with V-ATPase complex and targets it to the centrosome"].
- High-throughput exosome and binary-interactome rows provide context but should not define ATP6V0D1 function. Generic `protein binding` rows are over-annotated; the informative biology is V-ATPase V0-sector complex membership and contribution to proton-pump rotational activity.

## PN proteostasis synthesis

ATP6V0D1 is appropriate for a conservative proteostasis projection only through lysosomal/endosomal acidification and downstream lysosome-dependent degradation capacity. It is not a chaperone, proteasome component, ubiquitin-system factor, or direct protein-folding machinery component.

The core review should therefore prioritize V-ATPase complex membership, contribution to rotational proton pump activity, and acidification of lysosomal/endosomal/vacuolar compartments. mTORC1 amino-acid sensing, iron/HIF regulation, cilium assembly, phagosome/synaptic vesicle contexts, plasma membrane V-ATPase, and extracellular exosome detection should be retained as non-core or context-specific where supported.

The `regulation of macroautophagy` row from the lipofuscin paper is not strong direct evidence for ATP6V0D1 as a macroautophagy regulator; it is best treated as an over-annotation in this PN review.
