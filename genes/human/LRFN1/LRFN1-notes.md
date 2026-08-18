# LRFN1 / SALM2 literature notes

## Scope and nomenclature

Human LRFN1 (UniProt Q9P244) is SALM2. SALM family numbering does not match LRFN numbering: SALM1/LRFN2, SALM2/LRFN1, SALM3/LRFN4, SALM4/LRFN3, and SALM5/LRFN5. The primary literature often uses rat or mouse SALM2 constructs and cultured rodent neurons; species and paralog boundaries below are therefore explicit.

## Direct functional evidence

- Ko et al. identify SALM2 at excitatory rather than inhibitory sites and connect it to postsynaptic assembly: [PMID:16630835, "SALM2, a SALM isoform, distributes to excitatory, but not inhibitory, synaptic sites."] Aggregating SALM2 coclustered PSD-95, GKAP, and AMPA receptors [PMID:16630835, "Bead-induced direct aggregation of SALM2 results in coclustering of PSD-95 and other postsynaptic proteins, including GKAP and AMPA receptors."]
- Both gain- and loss-of-function support a role in excitatory-synapse differentiation: [PMID:16630835, "Overexpression of SALM2 increases the number of excitatory synapses and dendritic spines."] and [PMID:16630835, "Knockdown of SALM2 by RNA interference reduces the number of excitatory synapses and dendritic spines and the frequency, but not amplitude, of miniature excitatory postsynaptic currents."]
- SALM2 also promotes neurite growth in cultured hippocampal neurons as one member of a family-wide phenotype: [PMID:18585462, "Over-expression of each SALM resulted in enhanced neurite outgrowth, but with different phenotypes."] The domain-dissection boundary is important: [PMID:18585462, "the C-terminal PDZ binding domains of SALMs 1-3 are required for most aspects of neurite outgrowth."] and [PMID:18585462, "by using a chimera of SALMs 2 and 4, we found that the N-terminus is also involved in neurite outgrowth."]

## Localization, topology, and postsynaptic scaffolds

- Comparative Lrfn work defines the family architecture as [PMID:16828986, "leucine-rich repeat (LRR)-immunoglobulin-like (Ig)-fibronectin type III (Fn)-transmembrane domain structure"] and reports that [PMID:16828986, "Lrfn1-5 commonly encode glycoproteins spanning the plasma membrane, with their N-terminus located on the extracellular side."]
- Lrfn1 has a PSD95-binding cytoplasmic tail: [PMID:16828986, "C-termini of Lrfn1, Lrfn2 and Lrfn4 were bound by PDZ domains of postsynaptic protein PSD95, re-distributing PSD95 to cell periphery where the Lrfn proteins were detected."]
- Reactome's receptor-association reaction is consistent with the primary Ko paper but is secondary evidence: it reports [Reactome:R-HSA-8849881, "SALM2 coimmunoprecipitates with NMDAR and AMPAR subunits isolated from detergent-solubilized brain (Ko et al. 2006)."] The available evidence supports membership in receptor/scaffold-containing complexes; it does not by itself prove every association is a direct binary contact or a stable obligate complex.

## SALM-SALM cis complexes and trans-adhesion boundary

- Rat-brain co-immunoprecipitation supports a SALM1-3 complex: [PMID:18227064, "In brain, we found that SALMs 1-3 strongly co-immunoprecipitated with each other"]. Heterologous cells broadened this to family homo- and heteromeric associations: [PMID:18227064, "co-immunoprecipitation studies showed that all five SALMs form heteromeric and homomeric complexes."]
- These results must not be converted into SALM2 trans homophilic adhesion. The same paper reports [PMID:18227064, "Both SALMs 4 and 5 formed homophilic, but not heterophilic associations, whereas no trans associations were formed by the other SALMs."] Thus SALM2-containing SALM complexes are best described as cis/same-cell co-complexes under the tested conditions.
- Reactome retains the unresolved functional boundary: [Reactome:R-HSA-8849900, "Whether the homo  and heteromeric complexes formed between SALMs 1-3 contribute to synapse formation or neurite outgrowth remains to be determined (Seabold et al. 2008)."]

## LAR-family receptor phosphatase interactions and structure

- A human cell-surface ectodomain screen followed by SPR expands SALM2 binding from PTPRD to all three LAR-family RPTPs: [PMID:32822567, "PHA led us to test binding of all LAR-PTPRs to all SALMs by SPR. With the exception of PTPRF-SALM4, we observed binding of all LAR-PTPRs to all SALMs"]. This is direct biochemical binding evidence for human SALM2/LRFN1 with PTPRD, PTPRF, and PTPRS, but it does not establish the physiological consequence of each pair.
- Structural work used mouse SALM2 and mouse PTPδ, not human LRFN1: [PMID:29348429, "For crystallization, a mouse PTPδ isoform containing both meA9 and meB inserts, and human SALM5 and mouse SALM2 were used"]. It resolved [PMID:29348429, "PTPδ (Ig1–Ig3)–SALM2 (LRR–Ig)"] and found [PMID:29348429, "The LRR domains of SALM2 and SALM5 are composed of eight parallel β-strands flanked by the N- and C-terminal caps."]
- The binding interface is distributed over both SALM2 domains: [PMID:29348429, "the Ig2 and Ig3 domains of PTPδ sandwiches the Ig domain of SALM2 or SALM5. The Ig2 domain of PTPδ also interacts with the LRR domain of SALM2 or SALM5"]. The crystallographic assembly is [PMID:29348429, "Our structures revealed the 2:2 binding mode of PTPδ and SALMs. SALMs form a dimer, which bridges two PTPδ monomers."]
- Alternative splicing is a property of the PTPδ partner, not an LRFN1 isoform claim: [PMID:29348429, "meA is not involved in the binding between the type-IIa RPTPs and SALMs, whereas the insertion of meB is preferred but dispensable for the binding."] The authors also explicitly caution [PMID:29348429, "we cannot exclude the possibility that the present PTPδ–SALM2 and PTPδ–SALM5 structures may also reflect the cis complex formed on the postsynaptic membrane."]

## Paralog-specific boundary

SALM2 controls excitatory postsynaptic differentiation, but it was not a presynaptic organizer in the standard mixed-culture assay. Mah et al. report [PMID:20410109, "SALM3 and SALM5, but not other members of the SALM family, are capable of inducing excitatory and inhibitory presynaptic differentiation in contacting axons."] Goto-Ito et al. likewise state [PMID:29348429, "Only SALM3 and SALM5 have synaptogenic activity in a trans manner among the SALM isoforms"] The 2:2 SALM5/PTPδ mechanism and SALM5 disease associations therefore must not be transferred wholesale to LRFN1.

## Disease and isoform context

- The PubMed search did not identify a peer-reviewed primary study establishing an LRFN1-specific human disease mechanism. A 2021 conference abstract described LRFN1 as an autism candidate, which is insufficient for a verified functional or causal conclusion. Published SALM-family neurodevelopmental-disease claims frequently concern SALM5/LRFN5, a distinct paralog.
- The reviewed human UniProt record supplies a single canonical 771-aa LRFN1 sequence and does not curate an experimentally resolved alternative-protein isoform. The splice dependence demonstrated structurally concerns mini-exons of the PTPδ binding partner.

## Reference-access audit

- Full cached text: PMID:20410109, PMID:29348429, PMID:32822567.
- Abstract-only cache: PMID:16630835, PMID:16828986, PMID:18227064, PMID:18585462. PMID:18227064 and PMID:18585462 have PMC identifiers, but the project fetcher could not retrieve usable full text from the publisher/PMC routes; findings are therefore limited to exact abstract text.
- All four seeded GO_REF records were checked as annotation-method provenance and contain no gene-specific experimental findings. All three seeded Reactome records were checked against their cached text and linked primary literature.
