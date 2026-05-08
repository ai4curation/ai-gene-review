# OCBIM_22008529mg (SLC6A4 / SERT) - Deep Research Summary

## Gene Identity

- **UniProt:** A0A0L8FU48 (TrEMBL, unreviewed)
- **Gene model:** OCBIM_22008529mg
- **Organism:** *Octopus bimaculoides* (California two-spotted octopus), NCBI Taxon:37653
- **Protein name:** Sodium-dependent serotonin transporter (SERT)
- **Ortholog:** SLC6A4 (vertebrate nomenclature)
- **Length:** 507 amino acids, 57.0 kDa
- **Accession:** EMBL KQ426666 / KOF67960.1 (from O. bimaculoides genome project)
- **Classification:** SLC6 (Solute Carrier 6) / SNF (Sodium:Neurotransmitter symporter Family)
- **PANTHER:** PTHR11616:SF279 (Sodium-dependent serotonin transporter)

## Structural Features

### Transmembrane Topology

OCBIM_22008529mg encodes a multi-pass membrane protein with the canonical structure of SLC6 family transporters:
- **Signal peptide:** residues 1-17
- **10 predicted transmembrane helices** (Phobius predictions): positions 38-65, 131-148, 160-184, 204-228, 240-265, 298-328, 340-365, 371-394, 415-434, 446-470
- **Conserved disulfide bond:** Cys77-Cys86, in the second extracellular loop (characteristic of monoamine transporters)

### Ion Binding Sites

Sodium-dependent transport is mediated by conserved Na+ binding residues at positions 214, 246, 311, and 314 [UniProt, PIRSR:PIRSR600175-1]. These correspond to the Na1 and Na2 binding sites characterized in crystal structures of the bacterial leucine transporter LeuT and human SERT.

### MDMA Binding Site Conservation

Edsinger and Dolen (2018) performed phylogenetic and sequence analysis to demonstrate that the SERT transmembrane domain binding pocket for MDMA shows conservation of key residues across vertebrate and invertebrate species, including *O. bimaculoides* [PMID:30245101, "the evolutionary conservation of the serotonin transporter (SERT, encoded by the Slc6A4 gene) binding site of MDMA in the O. bimaculoides genome"]. The octopus SERT is confirmed as orthologous to human SLC6A4 based on phylogenetic analysis [PMID:30245101].

### Structural Context from Human SERT

While no crystal structure exists for the octopus SERT, the human SERT structure has been solved in complex with various ligands. MDMA binds in the central substrate-binding site (S1 site) within the transmembrane domain, overlapping with the serotonin binding pocket. The conservation of key residues at this site in octopus SERT provides the structural basis for MDMA's pharmacological activity across species.

## Primary Function

### Serotonin Reuptake

SERT is a sodium- and chloride-dependent transporter that mediates the reuptake of serotonin (5-hydroxytryptamine, 5-HT) from the synaptic cleft into presynaptic neurons. It terminates serotonergic signaling and recycles serotonin for subsequent release. The GO annotations from TreeGrafter include:
- **GO:0005335:** serotonin:sodium:chloride symporter activity
- **GO:0051378:** serotonin binding

The transport mechanism involves co-transport of one Na+ and one Cl- ion with each serotonin molecule, with counter-transport of K+. This is the primary mechanism for terminating serotonergic neurotransmission in both vertebrate and invertebrate nervous systems.

### MDMA Target

MDMA (3,4-methylenedioxymethamphetamine) binds to SERT and reverses its transport direction, causing release of serotonin into the extracellular space rather than uptake [PMID:30245101]. This mechanism underlies MDMA's well-characterized prosocial and empathogenic effects in humans and, as demonstrated by Edsinger and Dolen, in octopus as well.

## Biological Role

### MDMA-Induced Prosocial Behavior in Octopus

The landmark study by Edsinger and Dolen (2018) demonstrated that MDMA induces prosocial behavior in *O. bimaculoides*, an otherwise asocial and solitary species [PMID:30245101]:

- **Experimental paradigm:** A three-chambered social approach task was used, with one chamber containing a novel conspecific in a perforated container
- **Key finding:** MDMA-treated octopuses spent significantly more time in the social proximity zone near the novel conspecific compared to saline controls [PMID:30245101, "MDMA enhances acute prosocial behaviors in Octopus bimaculoides"]
- **Behavioral changes:** MDMA-treated octopuses exhibited extensive ventral surface tactile exploration of the social stimulus, a behavior not seen in controls
- **Dose-dependent:** The effects were observed after bath application of MDMA at doses comparable to those used in rodent studies

This study provided the first evidence that pharmacological manipulation of serotonergic neurotransmission can modulate social behavior in a cephalopod.

### Serotonergic Signaling in Cephalopod Nervous Systems

Serotonin is an evolutionarily ancient neurotransmitter present in cephalopod nervous systems with multiple established roles:

1. **Learning and memory:** Serotonin modulates synaptic plasticity in the octopus vertical lobe (VL), the primary learning and memory center. Stern-Mentch et al. (2022) confirmed the presence of 5-HT in the VL and identified its role as a neuromodulator of both short- and long-term synaptic plasticity at the MSFL-to-AM synapse [PMID:35107842, "5-HT, octopamine, dopamine and nitric oxide modulate short- and long-term VL synaptic plasticity"].

2. **Behavioral modulation in cephalopods:** Antidepressants acting on the serotonergic system (SSRIs like fluoxetine and SNRIs like venlafaxine) affect burying/camouflage behavior in juvenile cuttlefish (*Sepia officinalis*) at environmentally relevant concentrations, suggesting the serotonergic system broadly regulates innate behaviors in cephalopods [PMID:31610357].

### Presynaptic Localization

Based on GO annotations (IEA:TreeGrafter and IEA:GOC), the octopus SERT is predicted to localize to:
- **Neuron projections** (GO:0043005)
- **Plasma membrane** (GO:0005886)
- **Presynapse** (GO:0098793)

This is consistent with the well-characterized presynaptic localization of SERT in vertebrate serotonergic neurons, where it functions in the presynaptic membrane to terminate synaptic transmission.

## Expression and Localization

The gene model OCBIM_22008529mg was identified from the *O. bimaculoides* genome assembly [PMID:26268193]. The genome submission notes gonad as the tissue source for RNA, but SERT is expected to be broadly expressed in the nervous system based on vertebrate homology and the functional data from Edsinger and Dolen (2018) showing SERT-dependent behavioral effects.

In vertebrates, SLC6A4 is expressed in serotonergic neurons of the raphe nuclei and in peripheral tissues including gut enterochromaffin cells, platelets, and placenta. The extent of peripheral SERT expression in octopus has not been characterized in detail.

## Evolutionary Context

### Deep Conservation of Serotonergic Social Circuits

The central finding of Edsinger and Dolen (2018) is that the role of serotonergic neurotransmission in regulating social behaviors is conserved across more than 500 million years of evolution, despite massive divergence in brain organization between cephalopods and vertebrates [PMID:30245101, "the neural mechanisms subserving social behaviors exist in O. bimaculoides and indicate that the role of serotonergic neurotransmission in regulating social behaviors is evolutionarily conserved"].

This is particularly remarkable because:
- Octopus and human lineages diverged over 500 million years ago
- Cephalopods have a fundamentally different brain organization (distributed nervous system with 2/3 of neurons in the arms)
- Members of Octopoda are predominantly asocial, suggesting the serotonergic social circuitry is maintained even in species that rarely deploy it

### SLC6 Family Evolution

The SLC6 family is ancient and diversified early in animal evolution. Studies in the chordate invertebrate *Ciona savignyi* identified 40 SLC6 family genes, demonstrating extensive gene expansion in this family across invertebrate lineages [PMID:31026570]. The SLC6A4 subfamily (monoamine/serotonin transporters) is phylogenetically distinct from the amino acid transporter subfamilies (AA1/AA2) and GABA transporter subfamily within SLC6. Cross-species chimera studies between human and *Drosophila* SERT have mapped structural determinants of transport specificity and pharmacological sensitivity [PMID:9779469].

### Octopus Genome Context

The *O. bimaculoides* genome (2.7 Gb, ~33,000 protein-coding genes) was sequenced by Albertin et al. (2015), revealing that cephalopods achieved neural and morphological complexity through massive expansion of specific gene families (protocadherins, zinc-finger transcription factors), extensive mRNA editing, and genomic rearrangements, rather than through whole-genome duplication [PMID:26268193]. The SERT gene appears to be present as a single copy, consistent with the ancestral state for monoamine transporters.

## Key References

1. **Edsinger E, Dolen G (2018).** A Conserved Role for Serotonergic Neurotransmission in Mediating Social Behavior in Octopus. *Current Biology* 28:3136-3142.e4. [PMID:30245101] -- Landmark study demonstrating MDMA-induced prosocial behavior in O. bimaculoides, conservation of SERT/MDMA binding site, and evolutionary conservation of serotonergic social behavior circuits.

2. **Albertin CB et al. (2015).** The octopus genome and the evolution of cephalopod neural and morphological novelties. *Nature* 524:220-4. [PMID:26268193] -- Source of the O. bimaculoides genome assembly containing the OCBIM_22008529mg gene model.

3. **Stern-Mentch N et al. (2022).** Neurotransmission and neuromodulation systems in the learning and memory network of Octopus vulgaris. *J Morphol* 283:557-584. [PMID:35107842] -- Comprehensive characterization of neurotransmitter systems in octopus vertical lobe, including serotonin's role in synaptic plasticity.

4. **Chabenat A et al. (2019).** Hidden in the sand: Alteration of burying behaviour in shore crabs and cuttlefish by antidepressant exposure. *Ecotoxicol Environ Saf* 186:109738. [PMID:31610357] -- Serotonergic disruption by SSRIs/SNRIs alters innate behavior in cuttlefish, demonstrating the importance of serotonin signaling in cephalopod behavior.

5. **Ren P et al. (2019).** Identification and functional characterization of solute carrier family 6 genes in Ciona savignyi. *Gene* 705:142-148. [PMID:31026570] -- SLC6 family expansion and functional characterization in a chordate invertebrate.

6. **Barker EL, Blakely RD (1998).** Structural determinants of neurotransmitter transport using cross-species chimeras: studies on serotonin transporter. *Methods Enzymol* 296:475-98. [PMID:9779469] -- Cross-species chimera studies mapping SERT functional domains.
