# tub (Tube, P22812) review notes

## Identity
- Drosophila melanogaster Tube, FBgn0003882; N-terminal death domain (Pfam Death_2 / IPR029397 Tube_Death), C-terminal Tube repeats (UniProt P22812). No kinase domain.
- Interacts with Pelle (Q05652), Myd88 (Q7K105) and Dorsal (P15330) per UniProt INTERACTION.

## Core biology (with provenance)
- Adaptor bridging MyD88 and Pelle: [PMID:12351681 "Tube recruits MyD88 and Pelle into the heterotrimer by two distinct binding surfaces on the Tube death domain"]; [PMID:12351681 "we find a heterotrimeric association of the death domains of MyD88, Tube, and the protein kinase Pelle"].
- Tube-Pelle death domain heterodimer structure: [PMID:10589682 "Crystal structure of the Pelle and Tube death domain heterodimer reveals that the two death domains adopt a six-helix bundle fold"]; interface required in vivo.
- Tube-Pelle DD binding in two-hybrid and with purified proteins, Kd about 0.5 uM [PMID:10512628].
- Membrane recruitment model: [PMID:7635064 "We propose a model wherein tube activates pelle by recruiting it to the plasma membrane, thereby propagating the axis-determining signal."]; Tube associates with plasma membrane in interphase embryos [PMID:7635064].
- dMyD88 recruits Tube from cytosol to the plasma membrane in S2 cells [PMID:22464168 "Expressing Tube in S2 cells revealed that Tube is found to be evenly distributed throughout the cytosol"; "Rather, Tube co-localized with full length dMyD88 at the plasma membrane"].
- Tube binds Dorsal via Tube repeats [PMID:12351681 "C-terminal Tube repeats that mediate binding to Dorsal"]; [PMID:9367441 "Dorsal binds specifically to Tube, Pelle and Cactus"].
- Genetics: dorsal-group maternal gene; strong alleles give embryos lacking ventral and lateral pattern elements; acts downstream of Toll [PMID:8244004]. Kra/dMyD88 acts between Toll and Tube [PMID:12559494].
- Immunity: required for drosomycin induction and survival after fungal infection [PMID:8808632; PMID:11743586]. In S2 cells required for Drosomycin but not Attacin reporter (LPS/Imd readout) [PMID:12351681 "Drosophila MyD88, like Tube and Pelle, was required for activation of the Drosomycin, but not the Attacin, reporter"].
- Muscle: spz, tube, pelle required for embryonic muscle patterning via epidermal Toll [PMID:9676200].

## Curation decisions (summary)
- ACCEPT all GO:0008063 Toll signaling pathway rows (correct fly-specific term; no vertebrate GO:0002224 rows present).
- REMOVE GO:0031663 lipopolysaccharide-mediated signaling pathway (IBA): ligand-specific mammalian TLR4-lineage term; Tube is not needed for the LPS/Attacin readout. This bears on the project question on ligand-specific pathway terms reaching orthologues.
- REMOVE nucleus IBA (kinase-family node; no evidence Tube is nuclear).
- REMOVE apoptotic process NAS (inferred from death-domain naming).
- MODIFY GO:1990782 protein tyrosine kinase binding: Pelle is a Ser/Thr IRAK-family kinase -> death domain binding / protein kinase binding.
- protein binding rows -> death domain binding (DD papers), protein kinase binding (Pelle), NF-kappaB binding (Dorsal); DPIM2 AP-MS row REMOVE.
- NEW GO:0035591 signaling adaptor activity (comparator: human MYD88 and TIRAP and fly Myd88 carry it in GOA).
- hemocyte proliferation TAS from a review whose cached abstract does not mention Tube -> UNDECIDED.

## Deep research
Falcon deep research had not started for DROME genes when this review was written. Review done from UniProt and cached publications.
