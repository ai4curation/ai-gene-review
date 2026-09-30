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

## Literature-search scope and family boundary

The negative-function conclusion follows a search of PubMed/PMC, the reviewed human
and mouse UniProt records, current GO/QuickGO annotations, and LRIT-specific PANTHER
subfamilies through August 2026. Searches used `LRIT2`, `LRRC22`, A6NDA9, mouse
`Lrit2`, and combinations with retina, synapse, interaction, isoform, knockout, and
disease. The only functional LRIT2-specific primary result found beyond clone and
topology resources was the zebrafish morpholino eye-size phenotype in PMID:31934309;
the mouse LRIT1 association remains accessible only through the curated orthology
statement and an abstract that foregrounds LRIT1.

The same search recovered extensive retinal mechanisms for close family members
LRIT1 and LRIT3. Those papers are not interchangeable evidence. For example,
endogenous tagging indicates that mouse LRIT3 is presynaptic and photoreceptor-derived
[PMID:40263339 "These observations suggest that LRIT3 is confined to pre-synaptic compartment and is expressed solely by photoreceptors."].
LRIT1 has a distinct mGluR6/FRMPD2 cone-synapse role, while LRIT3 organizes the
depolarizing-bipolar-cell signalplex. No source demonstrates either mechanism for
LRIT2, and PANTHER places LRIT1, LRIT2, and LRIT3 in separate gene-specific
subfamilies. These positive paralog data therefore strengthen, rather than weaken, the
decision to leave LRIT2 wholly dark.
