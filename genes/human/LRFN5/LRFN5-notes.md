# LRFN5 / SALM5 literature notes

## Identity and scope

LRFN5 is SALM5, the fifth synaptic adhesion-like molecule. It is not SALM3/LRFN4,
SALM4/LRFN3, SALM2/LRFN1, or SALM1/LRFN2. The downloaded human UniProt record is
Q96NI6 and contains no `ALTERNATIVE PRODUCTS` stanza, so I found no curated human
LRFN5 protein isoform that should be tracked separately. The important splice variants
in the synaptic literature belong instead to the *binding partners* PTPRF/LAR, PTPRD,
and PTPRS.

SALM5 lacks the C-terminal PDZ-binding domain found in SALM1-3
[PMID:18227064 "SALMs 1-3 contain PDZ-binding domains, whereas SALMs 4 and 5 do not."].
Accordingly, the weak biochemical association with PSD-95 must not be described as a
canonical PDZ-tail interaction. SALM5 was weakly recovered with PSD-95, but aggregated
SALM5 did not cluster PSD-95 on dendrites
[PMID:20410109 "SALM3 and SALM5 proteins are enriched in synaptic fractions, and form strong (SALM3) or weak (SALM5) complexes with postsynaptic density-95 (PSD-95), an abundant postsynaptic scaffolding protein at excitatory synapses. Aggregation of SALM3, but not SALM5, on dendritic surfaces induces clustering of PSD-95."].

## Synaptic adhesion and presynapse induction

The earliest direct adhesion study used rat brain and heterologous cells. SALM5 formed
homophilic rather than heterophilic trans-cellular associations
[PMID:18227064 "Both SALMs 4 and 5 formed homophilic, but not heterophilic associations, whereas no trans associations were formed by the other SALMs."].
This is genuine SALM5 biology but should not be conflated with the later heterophilic
SALM5-LAR-RPTP synaptic bridge.

Rat-neuron mixed-culture and knockdown experiments established that SALM5 induces both
excitatory and inhibitory presynaptic differentiation
[PMID:20410109 "We found that expression of the SALM family proteins SALM3 and SALM5 in nonneural and neural cells induces both excitatory and inhibitory presynaptic differentiation in contacting axons."].
Loss of SALM5 decreased synapse abundance and function in both classes
[PMID:20410109 "Knockdown of SALM5 reduces the number and function of excitatory and inhibitory synapses."].

The later ligand study used mouse full-length SALM5, human and mouse LAR-RPTP constructs,
rat dissociated hippocampal neurons, and rat organotypic slices. Mouse SALM5 bound all
three LAR-family receptor phosphatases
[PMID:27225731 "We found that SALM5-expressing cells coaggregated with cells expressing all three LAR-RPTPs (LAR, PTPδ, and PTPσ)."].
The LAR-binding-defective SALM5 S329/S360A mutant did not rescue AMPA-receptor-mediated
synaptic transmission after SALM5 knockdown
[PMID:27225731 "When a mutant SALM5 (S329/S360A) that lacks LAR binding was used in the rescue experiment, it failed to rescue EPSCAMPA (Fig. 6c)."].
Thus the best-supported model is a postsynaptic SALM5 dimer engaging presynaptic
LAR-RPTPs to organize presynaptic differentiation and maintain synaptic transmission.

An independent human extracellular-domain interactome corroborated binding of SALM5 to
PTPRF/LAR, PTPRD, and PTPRS
[PMID:32822567 "With the exception of PTPRF-SALM4, we observed binding of all LAR-PTPRs to all SALMs"].
This study supports the human interaction but does not by itself establish directionality,
cis/trans geometry, or synaptogenic function.

## Structural mechanism and construct boundaries

Two 2018 structural papers independently resolved a 2:2 SALM5-PTPδ assembly. One used
human SALM5 with mouse PTPδ and found that SALM5 dimerization is necessary for
synaptogenic activity, as summarized directly in the paper's abstract
[PMID:29348429 "Our synaptogenic co-culture assay using site-directed SALM5 mutants demonstrates that presynaptic differentiation induced by PTPδ-SALM5 requires the dimeric property of SALM5."].

The other study used human SALM5 and human PTPδ fragments and observed a central SALM5
dimer bridging two PTPδ monomers
[PMID:29348579 "For the SALM5/PTPδ complex crystal, the asymmetric unit contained one dimeric complex, in a 2:2 stoichiometry, where a central SALM5 dimer bridges two monomeric PTPδ molecules together."].
A dimer-disrupting human SALM5 mutation retained PTPδ binding but abolished presynaptic
induction in a rat-neuron heterologous assay
[PMID:29348579 "This meant that R110N/E160S mutation abrogated the capacity of SALM5 to induce presynaptic differentiation. Taken together, disrupting SALM5 dimerization may significantly impair its functionality in mediating presynaptic differentiation."].

These structures use extracellular fragments (LRR-Ig for crystallography and, in some
functional experiments, an ectodomain displayed on HEK293 cells or beads), not intact
human neurons expressing endogenous full-length human LRFN5. They directly establish the
extracellular recognition mechanism but not an LRFN5 cytoplasmic signaling pathway.

## LAR-RPTP splice-code discrepancy

The 2016 cell-aggregation study concluded that partner mini-exon B suppresses SALM5
binding
[PMID:27225731 "Taken together, these results suggest that the meA and meB splice inserts in LAR-RPTPs differentially regulate SALM5 binding, and that the meB splice insert strongly inhibits the SALM5–LAR-RPTP interactions."].
In contrast, purified-protein SPR and structural studies found that PTPδ mini-exon B is
favored. In the human-human study, adding MeB increased SALM5 binding by about 20- to
27-fold
[PMID:29348579 "which clearly showed that the addition of MeB to PTPδ significantly enhanced PTPδ/SALM5 interaction (by 27 or 20 folds, respectively, for the presence or absence of MeA)."].
The authors explicitly attributed the discrepancy as potentially assay-dependent. The
review should preserve this unresolved conflict rather than state one splice preference
as settled in vivo.

## CNS immune function

SALM5 also has a distinct, experimentally supported immune-regulatory role. Human and
mouse SALM5 bind HVEM/TNFRSF14, and the reciprocal human screen was selective for SALM5
among SALM family members
[PMID:27152329 "The HVEM-Ig screening did not generate any positive signal in the wells containing the other four SALM family members, though members of the SALM family share about 50% homology in their protein sequences."].
The SALM5 LRR domain was sufficient for this interaction
[PMID:27152329 "The LRR domain, but not the Ig or FN domain from SALM5, is sufficient to endow the binding capacity to HVEM"].

The functional inflammation experiments were primarily mouse, despite direct human
binding validation. SALM5-expressing cells suppressed macrophage IL-6 and TNF production
[PMID:27152329 "As shown in Fig. 2C, the production of both IL-6 and TNFα from the cultured macrophages was significantly inhibited by SALM5+ HEK293T cells. Therefore, SALM5 directly suppressed macrophage activation, likely by engaging a putative receptor on macrophages."].
This role is biologically credible and annotation-relevant, but it is a CNS immune-context
function rather than the central synaptic organizer mechanism.

## Broader neurite and disease context

Family-wide experiments found that each SALM enhanced neurite outgrowth in cultured
hippocampal neurons
[PMID:18585462 "Over-expression of each SALM resulted in enhanced neurite outgrowth, but with different phenotypes. Neurite outgrowth could be reduced by applying antibodies targeting the extracellular leucine rich regions of SALMs and with RNAi."].
This supports a broader neuronal-development role but does not isolate an LRFN5-specific
mechanism as cleanly as the presynapse-induction and LAR-RPTP studies.

PubMed searches also recovered LRFN5 locus/copy-number associations with autism,
developmental delay, and schizophrenia. Those association studies were not added as core
functional references because they do not directly establish the molecular or cellular
function of LRFN5. Disease association should remain contextual and should not be used to
infer a specific GO activity.
