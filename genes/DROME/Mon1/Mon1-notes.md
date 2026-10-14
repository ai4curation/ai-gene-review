# Mon1 (Drosophila melanogaster, Q9VR38) notes

The falcon deep research report (Mon1-deep-research-falcon.md) arrived after the wrapper timeout; it additionally summarises fly fat-body autophagy data (Mon1 null cells fail to recruit Rab7 to autophagosomes).

## Identity
- Dmon1/Sand1 family; catalytic-core subunit (with Ccz1) of the Mon1-Ccz1-Bulli (RMC1) Rab7 GEF that drives Rab5-to-Rab7 conversion on maturing endosomes.

## Literature
- [PMID:23418349 "We found that loss of function of Dmon1 results in an enlargement of maturing endosomes and loss of their association with Rab7."]; [PMID:23418349 "Our results suggest that the phenotype can be explained by the loss of function of Rab7."]
- Trimeric GEF [PMID:32499409 "Recruitment of Rab7 to endosomes requires the Mon1-Ccz1 guanine-nucleotide-exchange factor (GEF)."]; [PMID:32499409 "Both the Mon1-Ccz1 dimer and a Bulli-containing trimer display Rab7 GEF activity."]
- Cryo-EM of Drosophila Mon1-Ccz1-RMC1 [PMID:37216550 "Here, we report a near-atomic resolution cryogenic-electron microscopy structure of the Drosophila Mon1-Ccz1-RMC1 complex."]
- Regulation: [PMID:37463208 "We show that the intrinsically disordered N-terminal domain of Mon1 autoinhibits Rab5-dependent GEF activity on membranes."]; [PMID:37463208 "Using modeling, we further identify a conserved Rab5-binding site in Mon1."]
- Synapse: [PMID:26290519 "We have identified a role for Drosophila Mon1 in regulating glutamate receptor levels at the larval neuromuscular junction."]

## Curation thoughts
- Protein binding (Rab5) -> MODIFY to small GTPase binding (Rab5 recruits/activates the GEF on membranes).
- GEF inhibitor activity reflects intramolecular autoinhibition by the Mon1 N-terminus of its own complex -> over-annotation as an MF.
- Synaptic cleft (IDA) cannot be verified from the abstract; a cytosolic GEF subunit in the cleft is unexpected -> UNDECIDED.
