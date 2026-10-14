# NRXN1 (human, Q9ULB1) curation notes

## 2026-09-30 — initial review

### Identity and scope
- Q9ULB1 is the canonical neurexin-1-alpha entry (1477 aa; signal peptide, six LNS/laminin G-like domains with three interspersed EGF repeats, stalk, one TM helix at 1402-1422, 55-aa cytoplasmic tail ending ...KEYYV, a class II PDZ-binding motif). The beta isoforms from the internal promoter are a separate UniProt entry, P58400.
- UniProt annotates Ca2+-binding residues in LNS2, LNS4 and LNS6 (e.g. 329, 346, 407; 765, 782, 841; 1176, 1193, 1245, 1247) and a CASK-interaction region 1444-1470.
- The Falcon deep-research file was generated with a P58400 (beta) template header by mistake; its text is largely beta-framed but gene-level. Used as retrieval support only.

### Core biology (with provenance)
- Discovery as alpha-latrotoxin receptor; synaptic surface protein [PMID:1621094 "The neurexins were discovered by the identification of one member of the family as the receptor for alpha-latrotoxin."] [PMID:1621094 "An antibody to neurexin I showed highly concentrated immunoreactivity at the synapse."]
- Trans-synaptic adhesion with neuroligins, splice-regulated [PMID:16242404 "neuroligin binding to alpha- and beta-neurexins mediates trans-synaptic cell adhesion but has distinct effects on synapse formation"]
- LRRTM2 binds only SS4-lacking neurexins and forms adhesion junctions [PMID:20064387 "Binding of neurexins to LRRTM2 can produce cell-adhesion junctions, consistent with a trans-interaction regulated by neurexin alternative splicing"]; NRXN1 is the LRRTM2 receptor [PMID:20064388 "LRRTM2 binds to both Neurexin 1alpha and Neurexin 1beta, and shRNA-mediated knockdown of Neurexin1 abrogates LRRTM2-induced presynaptic differentiation."]
- Latrophilin-1/CIRL1 [PMID:22262843 "Cell adhesion assays using cells expressing neurexins and CL1 revealed that their interaction produces a stable intercellular adhesion complex, indicating that their interaction can be trans-cellular."]
- Dystroglycan, Ca2+-dependent via LNS Ca2+ site [PMID:11470830 "As with the Ig fusion proteins, the GST fusion protein bound dystroglycan in a Ca2+-dependent manner; binding was completely abolished by the Ca2+-binding site mutant."]
- Cerebellin-GluD tripartite bridge, SS4+ selective [PMID:20537373 "Here, we show that the N-terminal domain (NTD) of GluRdelta2 interacts with presynaptic neurexins (NRXNs) through cerebellin 1 precursor protein (Cbln1)."] [PMID:21356198 "The interactions of Cbln1, Cbln2 and Cbln4 were selective for NRXN variants containing splice segment (S) 4."]
- GABA-A receptors [PMID:20471353 "neurexins directly and stoichiometrically bind to GABA(A) receptors"]; the same paper: overexpressed neurexins do not increase synapse density.
- Neurexin induces postsynaptic differentiation [PMID:15620359 "We show here that neurexin alone is sufficient to induce glutamate postsynaptic differentiation in contacting dendrites."]
- Human NRXN1-alpha surface trafficking and rodent NRXN1-alpha clustering of PSD-95/LRRTM2 and NLGN2/gephyrin [PMID:21424692 "Whereas wild-type HA-neurexin1α induced robust clustering of glutamatergic postsynaptic components YFP-LRRTM2 and endogenous PSD-95 at dendrite contact sites"]
- Cytoplasmic tail binds CASK via C-terminal residues [PMID:8786425 "In neurexin I, this interaction is dependent on the C-terminal three residues."]
- Alpha-neurexins: release, not synapse formation [PMID:12827191 "Using triple-knockout mice, we show that alpha-neurexins are not required for synapse formation, but are essential for Ca2+-triggered neurotransmitter release."]; channels not directly gated [PMID:17035546 "alpha-neurexins do not affect the activation or inactivation properties of Ca2+ channels directly but may be responsible for coupling them to release-ready vesicles and metabotropic receptors"]
- Nrxn1-alpha single KO mouse: presynaptic excitatory defect; normal social behaviour and spatial learning; enhanced rotarod learning [PMID:19822762 "neurexin-1alpha deficient mice did not exhibit any obvious changes in social behaviors or in spatial learning"]
- Human disease: biallelic loss -> Pitt-Hopkins-like syndrome 2 [PMID:19896112 "All four patients with recessive defects in CNTNAP2 or NRXN1 showed severe MR with lack of speech or with speech limited to single words (P1b), whereas motor milestones were normal or only mildly delayed, with a walking age of 2 years in P3."]

### Caution: retracted paper
- PMID:28472659 (Chen et al. 2017 Neuron, "Conditional Deletion of All Neurexins Defines Diversity of Essential Synaptic Organizer Functions for Neurexins") carries a 2025 retraction notice in PubMed. It was fetched while researching and deliberately NOT cited. The "context-dependent specifier" framing is instead supported by PMID:12827191 and PMID:20471353.

### Decisions (81 GOA rows + 1 NEW)
- ACCEPT: plasma membrane (all 8), cell surface IDA, presynaptic membrane (IEA, ISS), presynaptic active zone membrane IBA, trans-synaptic protein complex IBA, neuroligin family protein binding (IBA, ISS), cell adhesion molecule binding ISS, neurotransmitter secretion ISS, NOT neuromuscular process controlling balance (the negation is accepted).
- MODIFY: 24 x protein binding -> GO:0030165 PDZ domain binding (all partners are PDZ proteins; fragmentomics/Y2H use the cytoplasmic tail/PBM); neuron cell-cell adhesion (IEA, TAS) -> GO:0099560 synaptic membrane adhesion; signal transduction IBA -> GO:0099545 trans-synaptic signaling by trans-synaptic complex.
- REMOVE: axon guidance TAS (1992 paper only notes sequence similarity to guidance proteins); neuromuscular process controlling balance ISS (mouse rotarod shows enhanced motor learning, not a balance role; contradicts the human NOT).
- MARK_AS_OVER_ANNOTATED: calcium channel regulator activity (effect is indirect coupling, PMID:17035546); ER, nuclear membrane, vesicle, neuronal cell body ISS (transit compartments; mouse donor annotations no longer present in mouse GOA); positive regulation of synapse maturation ISS (source is an nAChR-targeting study); vocal learning and vocalization behavior rows (absent speech in severe ID is not a vocalization function).
- KEEP_AS_NON_CORE: transmembrane signaling receptor activity IBA; signaling receptor activity TAS; calcium ion binding; acetylcholine receptor binding; chemical synaptic transmission; nervous system development; synapse assembly; positive regulation of synapse assembly; the postsynaptic clustering/assembly terms (gephyrin, neuroligin, PSD-95, postsynaptic membrane assembly); glutamatergic transmission / EPSP; learning, adult behavior, social behavior.
- NEW: GO:0098632 cell-cell adhesion mediator activity (ISS, PMID:20064387). Comparator check: CLSTN1, contactins, CD200 carry it; used for neurexin in modules/neurexin_transsynaptic_adhesion.yaml.

### Comparison with the neurexin module
- Consistent: GO:0098632 (via NEW) as the neurexin MF and GO:0099560 (via MODIFY of the neuron cell-cell adhesion rows) as the process; presynaptic membrane location; PAINT node PTN002227321.
- Addition beyond the module: the review also treats GO:0099545 trans-synaptic signaling and alpha-neurexin release-site organization (GO:0007269) as core; the module lists GO:0099545 as a module concept but not on the neurexin annoton.

### P58400 (beta entry) GOA comparison (reference only, not reviewed)
- The beta entry has overlapping ISS rows from rat Nrxn1 beta (P0DI97) for synapse assembly, clustering terms, adhesion, NLGN binding, plus IDA rows from PMID:22750515 (FGFR1 binding / neurite outgrowth) and PMID:26078884 (DISC1/Kal-7/Rac1 signalosome gene-expression and kinase-cascade terms). It also carries the behaviour IMP rows from a beta signal-peptide variant paper (PMID:17034946). If the beta entry is reviewed, the same patient-phenotype considerations apply, and the signalling-cascade IDAs from 26078884 would need separate assessment.
