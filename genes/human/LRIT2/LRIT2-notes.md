# LRIT2 review notes

## Identity, topology, and isoforms

Human LRIT2 (A6NDA9) is a reviewed 550-residue precursor. The reviewed UniProt
record places a signal peptide at residues 1-19, an extracellular LRRNT/LRR/LRRCT-
Ig-like-FN3 region before a single predicted transmembrane helix at 466-486, and a
short cytoplasmic tail. This supports type-I membrane topology but not a particular
cellular membrane or biological activity
[`file:human/LRIT2/LRIT2-uniprot.txt`].

UniProt curates two human products. Isoform 2 changes canonical Asp297 to
`DGLLGGKHLTP`, replacing one residue with eleven and therefore adding ten net
residues within the annotated Ig-like domain.
The sequence comes from the MGC cDNA resource, whose paper describes a broad clone
collection rather than an LRIT2 functional comparison
[PMID:15489334 "The status, quality, and expansion of the NIH full-length cDNA project"].
No isoform-specific localization, partner, or physiological phenotype is established.

The isoform-1 cDNA was sourced from human retina in the UniProt record, but the linked
German cDNA Consortium paper is an ORF-resource study, not direct evidence for
endogenous retinal protein localization or function
[PMID:17974005 "Here we describe the generation of a full-ORF clone resource of"].

## Ocular evidence and species boundaries

A mouse coexpression/phenome analysis selected Lrit2 for cross-species validation.
Morpholino knockdown of corresponding zebrafish orthologs was associated with reduced
eye size
[PMID:31934309 "corresponding to mouse candidate genes Adal, Ankrd33, Car14, Ccdc126, Dkk3, Fam169a, Grifin, Kcnj14, Lrit2, Ppef2, and Ppm1n, were found to exhibit reduced eye size phenotype"].
This is useful hypothesis-generating evidence, but it is a zebrafish morpholino result,
not a targeted human or mouse LRIT2 mechanism and not sufficient for a human core GO
process.

UniProt states that LRIT2 interacts with LRIT1 and may form a heterodimer, but the
statement is explicitly transferred from mouse Q6PFC5. The linked local publication
cache is abstract-only and foregrounds mouse Lrit1 synaptic biology; it does not expose
the Lrit2 interaction experiment
[PMID:29590622 "Lrit1-deficient retinas exhibit an aberrant morphology of"].
Accordingly, the association is retained as a research lead, not converted into a
human molecular-function or stable-complex annotation. Mouse Lrit1's mGluR6/FRMPD2
mechanism is not transferred to LRIT2.

## Curation boundary

The only current human GOA row is broad membrane localization inferred from the
UniProt subcellular-location vocabulary. It is topologically plausible and retained as
non-core. No current evidence justifies a human retinal-process, synapse, adhesion,
LRIT1-binding, or receptor-binding annotation. The appropriate synthesis is therefore
DRAFT with an empty core until endogenous human localization, partners, and function
are demonstrated.
