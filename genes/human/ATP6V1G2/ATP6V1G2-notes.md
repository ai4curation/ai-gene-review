# ATP6V1G2 (V-type proton ATPase subunit G 2) review notes

## Identity and overview
- UniProt: O95670 (VATG2_HUMAN), 118 aa, 13.6 kDa. Gene ATP6V1G2 (synonyms ATP6G, ATP6G2, NG38). HGNC:862. Located at 6p21.3 in the MHC class III region near the TNF locus [PMID:10202016 "A new member of the Ig superfamily and a V-ATPase G subunit are among the predicted products of novel genes close to the TNF locus in the human MHC"].
- One of three human paralogs of the V-ATPase V1 "G" subunit (ATP6V1G1 ubiquitous, ATP6V1G2 brain-enriched, ATP6V1G3 kidney). Tissue specificity: brain [PMID:12384298 "Molecular cloning and characterization of novel tissue-specific isoforms of the human vacuolar H(+)-ATPase C, G and d subunits"]. HPA: tissue enriched (brain); Bgee expressed in cerebellar cortex.

## Function (from UniProt and V-ATPase structural biology)
- Subunit of the V1 (peripheral, ATP-hydrolytic) complex of the vacuolar H+-ATPase (V-ATPase) [file:human/ATP6V1G2/ATP6V1G2-uniprot.txt FUNCTION "Subunit of the V1 complex of vacuolar(H+)-ATPase (V-ATPase), a multisubunit enzyme composed of a peripheral complex (V1) that hydrolyzes ATP and a membrane integral complex (V0) that translocates protons"].
- The V1 complex contains three catalytic AB heterodimers, three peripheral stalks each consisting of EG heterodimers, a central rotor (D, F), and regulatory subunits C and H [file:human/ATP6V1G2/ATP6V1G2-uniprot.txt SUBUNIT "three peripheral stalks each consisting of EG heterodimers"]. Subunit G therefore partners subunit E to form the peripheral (stator) stalks that anchor the catalytic A3B3 head to the V0 membrane sector, resisting torque during rotary catalysis.
- V-ATPase acidifies and maintains the pH of intracellular compartments (endosomes, lysosomes, synaptic vesicles, clathrin-coated vesicles, melanosomes) and, in some cell types, acidifies the extracellular environment when targeted to the plasma membrane [file:human/ATP6V1G2/ATP6V1G2-uniprot.txt FUNCTION].
- Belongs to the V-ATPase G subunit family [file:human/ATP6V1G2/ATP6V1G2-uniprot.txt SIMILARITY]. InterPro IPR005124 (V-ATPase_G); Pfam PF03179.
- The G subunit is largely an extended/coiled-coil helical protein; the central region (~25-90) is predicted disordered (MobiDB-lite) but in the assembled stalk pairs with subunit E.

## Subcellular localization
- Melanosome: experimentally detected by proteomics in melanoma melanosomes; highly enriched in late-stage melanosomes [PMID:17081065 "Proteomic and bioinformatic characterization of the biogenesis and function of melanosomes"; file:human/ATP6V1G2/ATP6V1G2-uniprot.txt "Highly enriched in late-stage melanosomes"]. This is consistent with V-ATPase being present on the melanosome membrane; it reflects organelle membrane localization, not a melanosome-specific function.
- Clathrin-coated vesicle membrane; peripheral membrane protein [file:human/ATP6V1G2/ATP6V1G2-uniprot.txt SUBCELLULAR LOCATION, by similarity to Q0VCV6].
- Synaptic vesicle membrane / synaptic vesicle lumen acidification: inferred from rodent orthologs (the G subunit on neuronal synaptic vesicles) and phylogeny; ATP6V1G2 is the neuronal/brain-enriched isoform.

## Interactions
- IntAct: O95670 interacts with ATP6V1E2 (Q96A05; NbExp=7) — this is the expected E-subunit partner forming the EG peripheral stalk heterodimer [file:human/ATP6V1G2/ATP6V1G2-uniprot.txt INTERACTION].
- IntAct: O95670 interacts with USP20 (Q9Y2K6; NbExp=3) [file:human/ATP6V1G2/ATP6V1G2-uniprot.txt INTERACTION].
- Reference interactome (HuRI, Y2H) reports binary interactions [PMID:32296183 "A reference map of the human binary protein interactome"]. These yield generic GO:0005515 protein binding annotations.
- Multimodal cell map (AP-MS/IF based) [PMID:40205054 "Multimodal cell maps as a foundation for structural and functional genomics"]; also generic protein binding.
- The ATP6V1E2 interaction is functionally informative (peripheral stalk EG heterodimer assembly), but the GOA annotations are recorded as bare GO:0005515 protein binding, which is uninformative per curation guidelines.

## GO annotation assessment summary
- Core MF/CC/BP: proton-transporting ATPase activity, rotational mechanism (GO:0046961); proton transmembrane transport (GO:1902600); V-ATPase complex (GO:0016471) / V1 domain (GO:0000221); synaptic vesicle lumen acidification (GO:0097401); synaptic vesicle membrane (GO:0030672). These are well-supported for a V1 G subunit and consistent with the brain-enriched isoform.
- The peripheral stalk role is the molecular essence: the G subunit itself does not hydrolyze ATP (that is the A/B subunits) but is part of the complex that does; "enables proton-transporting ATPase activity, rotational mechanism" is a part-of-complex MF annotation appropriate at the complex level. ATP hydrolysis activity (GO:0016887, in UniProt DR but not in GOA TSV) is a complex-level activity, not a function of the isolated G subunit.
- Cytosol (GO:0005829, Reactome TAS, many entries): reflects the assembled/cytosolic V1 sector and pathway participation (phagosome acidification, endosome acidification, transferrin recycling, mTORC1 amino-acid signaling). The V1 sector is peripheral/cytosolic-facing, so cytosol is defensible but is a generic Reactome reaction-participant location; keep as non-core.
- regulation of macroautophagy (GO:0016241, NAS, PMID:22982048): the cited paper is a general lipofuscin/autophagy study in senescent fibroblasts and does not provide gene-specific evidence that ATP6V1G2 regulates macroautophagy. Over-annotation (any V-ATPase generically affects lysosomal/autophagic flux, but this is an indirect downstream consequence, not a core function of this subunit). Mark as over-annotated.
- melanosome EXP (PMID:17081065) and IEA: organelle membrane localization; keep as non-core (not the defining brain/synaptic role).
- extrinsic component of synaptic vesicle membrane (GO:0098850): accurate description of how the peripheral V1 sector (including subunit G) attaches to the vesicle membrane; keep.
- bare protein binding (GO:0005515): uninformative per project guidelines; mark as over-annotated.

## Core function statement
ATP6V1G2 is the brain/neuron-enriched G-subunit isoform of the vacuolar H+-ATPase V1 peripheral sector. Together with subunit E it forms the EG peripheral (stator) stalks that physically couple the catalytic A3B3 head of V1 to the V0 membrane rotor, enabling ATP-hydrolysis-driven rotary proton translocation and thereby acidification of synaptic vesicles and other organelles in neurons.
