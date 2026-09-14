# LRFN2 / SALM1 literature notes

## Identity, topology, and species scope

Human LRFN2 encodes SALM1, a type-I single-pass membrane protein. The comparative
mouse/human family study reports that Lrfn proteins are glycoproteins spanning the
plasma membrane with extracellular N termini and that Lrfn2's C-terminal tail binds
PSD95 PDZ domains [PMID:16828986 "Lrfn1-5 commonly encode glycoproteins spanning the
plasma membrane, with their N-terminus located on the extracellular side.";
"C-termini of Lrfn1, Lrfn2 and Lrfn4 were bound by PDZ domains of postsynaptic
protein PSD95"]. The original SALM1 work used rat brain and cultured rat hippocampal
neurons; it places SALM1 in synaptic-membrane and postsynaptic-density fractions and
also in axons and dendrites [PMID:16495444 "Distribution studies show that SALM1 is
present in synaptic membrane and postsynaptic density fractions but is also
distributed in axons and dendrites."]. These rodent studies support conservation of
the human protein's architecture and synaptic role, but they are not direct human
neuronal assays.

## Postsynaptic scaffold and glutamate-receptor functions

Rat-brain co-immunoprecipitation showed SALM1 association with PSD-95, SAP102, and
SAP97, while neuronal overexpression recruited NMDA receptors and PSD-95 to dendritic
puncta [PMID:16495444 "SALM1 interacts with PSD-95, synapse-associated protein 102
(SAP102), and SAP97 based on coimmunoprecipitation of detergent-solubilized brain.";
"Overexpression of SALM1 in 14 DIV neurons recruits NMDA receptors (NR) and PSD-95 to
dendritic puncta."]. The Reactome human model captures two possible routes to the
NMDA-receptor complex: direct extracellular SALM1-GRIN1 association and indirect
recruitment through PSD-95 [Reactome:R-HSA-8849906 "SALM1 can directly interact with
the extracellular domain of the NR1 subunit of NMDA receptor or indirectly by
binding to PSD-95"]. This event is an orthology/conservation-based human model; its
decisive primary assays were not performed in human neurons.

Mouse Lrfn2 knockout analysis supports a central role in excitatory synapse
maturation: mutant synapses had smaller PSDs, lower AMPA/NMDA ratios, and enhanced
LTP in one line [PMID:28604739 "The synapses are structurally and functionally
immature with spindle shaped spines, smaller postsynaptic densities, reduced
AMPA/NMDA ratio, and enhanced LTP."]. The same study found that AMPAR surface
expression depends on Lrfn2-PSD-95 association [PMID:28604739 "In vitro experiments
reveal that synaptic surface expression of AMPAR depends on the direct interaction
between Lrfn2 and PSD-95."]. A second mouse knockout study instead reported enhanced
NMDAR transmission but suppressed NMDAR plasticity, plus fewer inhibitory synapses
and reduced inhibitory transmission [PMID:29798891 "mice lacking SALM1/LRFN2
(Lrfn2-/- mice) show a normal density of excitatory synapses but altered excitatory
synaptic function, including enhanced NMDAR-dependent synaptic transmission but
suppressed NMDAR-dependent synaptic plasticity"]. The apparently divergent plasticity
directions should remain visible rather than be synthesized into a single precise
effect.

LRFN2 also participates in AMPA-receptor recycling through sorting nexin 27. A
purified LRFN2 tail peptide directly bound the SNX27 PDZ domain with micromolar
affinity [PMID:34251337 "the isolated recombinant PDZ domain of SNX27 directly bound
to a synthetic peptide corresponding to the LRFN2 PDZ binding motif"]. In rat
neurons, LRFN2 associated with AMPARs, and LRFN2 knockdown decreased surface AMPAR,
synaptic activity, and hippocampal LTP [PMID:34251337 "LRFN2 associates with AMPA
receptors and knockdown of LRFN2 results in decreased surface AMPA receptor
expression, reduced synaptic activity, and attenuated hippocampal long-term
potentiation."].

## Presynaptic SALM1 pool

SALM1 is not exclusively postsynaptic. In mouse hippocampal neurons it was found at
both pre- and postsynaptic membranes, and depletion on either side impaired
neurexin/neuroligin-mediated excitatory synapse formation [PMID:31368584 "SALM1 is
present at pre‐ and postsynaptic membranes of mouse hippocampal neurons and ...
depletion of pre‐ or postsynaptic SALM1 impaired Neuroligin1‐ and
Neurexin1β‐mediated excitatory synapse formation"]. Presynaptic SALM1 promotes
F-actin/PIP2-dependent *cis* clustering of neurexin [PMID:31368584 "SALM1 organizes
synapse development by promoting F‐actin/PIP2‐dependent cis‐oligomerization of
Neurexin at the presynapse."]. This is not a direct SALM1-neurexin biochemical
interaction and should not be described as a trans-synaptic SALM1 ligand pair.
SALM1 also directly associates through its PDZ-binding tail with CASK in the
CASK/Mint1/Lin7b presynaptic organizer [PMID:31368584 "interacting directly with
CASK, via its PDZ binding domain."].

## SALM cis complexes, paralog boundaries, and RTN3

SALM1-3 form complexes in rat brain, but the family-association study found no
trans-cellular association for SALM1-3; only SALM4 and SALM5 formed homophilic trans
associations in its assay [PMID:18227064 "SALMs 1-3 strongly co-immunoprecipitated
with each other"; "Both SALMs 4 and 5 formed homophilic, but not heterophilic
associations, whereas no trans associations were formed by the other SALMs."]. The
Reactome LRFN2 event should therefore be understood as a *cis* SALM complex
[Reactome:R-HSA-8849900 "SALM1, SALM2, and SALM3 form homo- and heteromeric complexes
in a cis manner."].

The classic mixed-culture presynaptic-induction phenotype belongs to SALM3/LRFN4 and
SALM5/LRFN5, not SALM1/LRFN2 [PMID:20410109 "expression of the SALM family proteins
SALM3 and SALM5 in nonneural and neural cells induces both excitatory and inhibitory
presynaptic differentiation in contacting axons."]. This does not contradict the
distinct presynaptic SALM1 mechanism in PMID:31368584, which acts by cis-regulating
neurexin clustering in the SALM1-expressing neuron.

A yeast two-hybrid screen using the SALM1 extracellular domain recovered RTN3A1 and
mapped association to the conserved LRR domain [PMID:19681166 "A clone encoding
full-length reticulon 3A1 was isolated. This interaction was shown to occur through
the LRR domain, which is found on all SALMs."]. Brain immunoprecipitation detected an
RTN3C-sized band with SALM1-4, while a separate 90-kDa signal was selective for
SALM2/3 [PMID:19681166 "A 19-kDa band, identified as reticulon 3C, bound to all four
SALMs, whereas a 90-kDa band ... bound to SALMs 2 and 3."]. Reactome consequently
describes SALM1's interaction as relatively weak compared with SALM2/3
[Reactome:R-HSA-8849882 "RTN3 ... tightly associates with SALM2 and SALM3 ... and
interacts relatively weakly with SALM1 and SALM4."]. Evidence for a trafficking role
is suggestive, not a demonstrated LRFN2 molecular function.

## Additional neuronal phenotypes and open boundaries

SALM family overexpression and perturbation in cultured rat hippocampal neurons
support a neurite-outgrowth phenotype, with SALM1-3 PDZ-binding domains required for
most measured effects [PMID:18585462 "the C-terminal PDZ binding domains of SALMs 1-3
are required for most aspects of neurite outgrowth."]. This is a family-level
in-vitro phenotype and is weaker evidence for a human LRFN2 core function than the
orthologous knockout synapse data.

In mouse retina, LRFN2 is selectively localized at cone terminals with DBC signalplex
members [PMID:38408870 "LRFN2 is selectively expressed at cone terminals and
colocalizes with PNA, and other DBC signalplex members."]. Lrfn2 loss reduced the
photopic ERG b-wave only at the brightest intensities, indicating impaired cone-to-
cone-DBC transmission [PMID:38408870 "LRFN2 absence compromises normal synaptic
transmission between cones and cone DBCs."]. The responsible molecular partner and
whether LRFN2 is pre-, post-, or bidirectionally positioned at this retinal synapse
remain unresolved.
