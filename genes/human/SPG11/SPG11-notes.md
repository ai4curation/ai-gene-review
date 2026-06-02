# SPG11 review notes

Review focus: proteostasis network context places SPG11/spatacsin under autophagic lysosome reformation (ALR), with the specific PN row marked `no_mapping`. For curation, this row is search context unless backed by primary literature. SPG11 has direct primary support for ALR and lysosome membrane remodeling, so the review should center on lysosome organization/lysosomal membrane organization rather than generic protein binding or broad neuronal phenotypes.

## Core lysosome reformation and membrane remodeling

- The JCI ALR paper directly supports SPG11/spatacsin as an ALR factor: "the SPG15 protein spastizin and the SPG11 protein spatacsin, are pivotal for autophagic lysosome reformation (ALR)" and "spastizin and spatacsin were essential components for the initiation of lysosomal tubulation" [PMID:25365221].
- This supports retaining `GO:0007040 lysosome organization` as core. `GO:1905037 autophagosome organization` is less precise, because the described defect is generation/reformation of lysosomes after autophagy, not organization of autophagosomes themselves [PMID:25365221 "Loss of spastizin or spatacsin resulted in depletion of free lysosomes" / "an accumulation of autolysosomes, reflecting a failure in ALR"].
- The 2025 structure paper supports a membrane-remodeling mechanism for the AP5-SPG11-SPG15 complex: "SPG11-SPG15 can cooperate with the fifth adaptor protein complex (AP5) involved in membrane sorting of late endosomes" and "AP5-SPG11-SPG15 complex can bind PI3P molecules, sense membrane curvature and drive membrane remodeling in vitro" [PMID:40175557]. This supports `GO:0097212 lysosomal membrane organization`, `GO:0097753 membrane bending`, late endosome/lysosome context, and modifying generic protein-binding rows from that reference.
- Lysosome membrane recycling is independently supported in neuronal disease models: "spatacsin, which is required for lysosome recycling" and "spatacsin acts downstream of clathrin and recruits dynamin to allow lysosome membrane recycling and clearance of gangliosides from lysosomes" [PMID:29949766]. This is core proteostasis/endolysosomal evidence, but the seeded `protein binding` annotation from this paper should be replaced with lysosome organization/lysosomal membrane organization, not retained as generic binding.
- Recent work also supports ER-linked lysosome trafficking/tubulation: "spatacsin is an ER-resident protein regulating the formation of tubular lysosomes" and "spatacsin-regulated degradation of AP5Z1 controls the directionality of lysosomes trafficking" [PMID:37871017]. This supports ER/late-endolysosomal context and lysosome organization, but generic `protein binding` remains uninformative.

## AP-5/SPG15 complex context

- AP-5/SPG11/SPG15 interaction is real and mechanistically important: "the four AP-5 subunits can be coimmunoprecipitated with SPG11 and SPG15" and "AP-5, SPG11, and SPG15 colocalize on a late endosomal/lysosomal compartment" [PMID:23825025]. The same abstract proposes a coat-like complex in which SPG11 forms a scaffold. Generic `protein binding` should therefore be modified to endolysosomal membrane organization or kept only as non-core interaction context.
- UniProt summarizes a narrower interaction set: "Interacts with AP5Z1, AP5B1, AP5S1 and ZFYVE26" [file:human/SPG11/SPG11-uniprot.txt]. This supports interaction provenance but not a useful GO molecular function term.
- The original SPG48/DNA-repair screen paper contains SPG11-LAP immunoprecipitation methods and described a putative helicase interacting with SPG11/SPG15, but this is not SPG11's proteostasis core function [PMID:20613862 "putative helicase that interacts with SPG11 and SPG15"].

## Neuronal transport and disease biology

- Neuronal transport evidence is strong but should be non-core in this proteostasis review. Spatacsin was found in axons/dendrites and synaptosomes, and knockdown/patient-derived neurons showed vesicle trafficking defects [PMID:24794856 "spatacsin was located in axons and dendrites" / "reduction in the anterograde vesicle trafficking indicative of impaired axonal transport" / "SPG11 is implicated in axonal maintenance and cargo trafficking"].
- IBA annotations for axonogenesis, chemical synaptic transmission, axo-dendritic transport, synapse, and synaptic vesicle transport are plausible by orthology and human evidence, but they are secondary phenotypes/contexts relative to ALR and lysosome organization.

## Locations

- UniProt supports cytosol/cytoplasm and neuronal processes: "Cytoplasm, cytosol", "Nucleus", "Cell projection, axon", and "Cell projection, dendrite", with note "Mainly cytoplasmic" [file:human/SPG11/SPG11-uniprot.txt].
- Murmu 2011 supports cytoplasmic vesicle/ER/microtubule colocalization: "diffuse punctate, cytoplasmic" and "partially co-localized with multiple organelles, particularly with protein-trafficking vesicles, endoplasmic reticulum and microtubules" [PMID:21545838]. These locations are useful but broad; ER is now better supported as a functional location by PMID:37871017.
- Nucleolus and plasma membrane HPA rows are weak relative to the lysosome/ER/neural-process evidence and should be kept non-core or marked over-annotated unless stronger gene-specific evidence is found.

## Generic binding annotations

- Generic `GO:0005515 protein binding` is overused in this record. The curation guideline says to avoid protein binding when a more informative term captures function. For SPG11, AP5/SPG15/dynamin/14-3-3 interactions are better captured as lysosome organization, lysosomal membrane organization, membrane bending, lysosome trafficking/regulation, or kept as non-core regulatory context.
- The PKA/14-3-3 paper supports regulatory interaction but not SPG11 core function: "identified a subset of 14-3-3 proteins as physiological interactors of spatacsin" and "The interaction is modulated by Protein Kinase A (PKA)-dependent phosphorylation of spatacsin at Ser1955" [PMID:36096339].
- Proteome-scale interactome rows from PMID:25416956 and PMID:33961781 are insufficiently informative for core GO curation without a mechanism specific to SPG11; they should be marked over-annotated.

## Deep research

- Falcon deep research was started with `just deep-research-falcon human SPG11` during this review and timed out after 600s with `All providers failed`; no `SPG11-deep-research-falcon.md` evidence was available for this review.
