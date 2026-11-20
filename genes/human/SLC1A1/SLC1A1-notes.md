# SLC1A1 (EAAT3 / EAAC1) — curation notes

UniProt: P43005 (EAA3_HUMAN), 524 aa. HGNC:10939. Chromosome 9p24.2.
Family: dicarboxylate/amino acid:cation symporter (DAACS, TC 2.A.23), SLC1A1 subfamily;
PANTHER PTHR11958:SF109. Mouse ortholog P51906, rat P51907, bovine Q95135 (all EAAT3/Slc1a1).

## Core biology (synthesized)

SLC1A1/EAAT3 is a sodium-dependent, high-affinity transporter of acidic amino acids
(L-glutamate, L-aspartate, D-aspartate) that also transports L-cysteine. It is a
secondary active transporter that couples uptake of one amino acid to symport of 3 Na+
and 1 H+ and counter-transport (antiport) of 1 K+, and additionally carries a
thermodynamically uncoupled anion (Cl-) conductance.

- Coupling stoichiometry established by flux measurements: [PMID:8857541 "three sodium ions and one proton are cotransported with each glutamate ion into the cell, while one potassium ion is transported out of the cell"]. Supports a transmembrane glutamate gradient >10^6.
- High affinity, electrogenic, plasma-membrane transport: [PMID:7914198 "High affinity transport of glutamate across plasma membranes of brain neurons and epithelial is mediated by a Na(+)- and K(+)-coupled electrogenic transporter"]; Km L-glutamate ~30 µM (Kanai), 18–97 µM across assays (Arriza [PMID:7521911]).
- Substrate range (UniProt FUNCTION): [file:human/SLC1A1/SLC1A1-uniprot.txt "Sodium-dependent, high-affinity amino acid transporter that mediates the uptake of L-glutamate and also L-aspartate and D-aspartate"]; [file:human/SLC1A1/SLC1A1-uniprot.txt "Can also transport L-cysteine"].
- Uncoupled chloride flux: [file:human/SLC1A1/SLC1A1-uniprot.txt "Mediates Cl(-) flux that is not coupled to amino acid transport; this avoids the accumulation of negative charges due to aspartate and Na(+) symport"]. This is a substrate-gated anion channel property of EAATs, not a coupled transport step; genuine but non-core.
- Structure: homotrimer, elevator mechanism; cryo-EM of hEAAT3 with Na+/aspartate [PMID:33658209]. UniProt SUBUNIT: [file:human/SLC1A1/SLC1A1-uniprot.txt "Homotrimer"].

## Physiological roles

1. Epithelial (kidney/intestine) reabsorption of glutamate/aspartate — the dominant role in humans:
   - [PMID:21123949 "SLC1A1 is the major renal transporter of glutamate and aspartate in humans"]; apical proximal tubule: [PMID:21123949 "In normal human kidney, SLC1A1 was distributed at the apical surface throughout the proximal tubule"].
   - [PMID:33658209 "It is the major glutamate and aspartate transporter outside of the central nervous system, including kidneys and intestines"].
   - Loss of function → dicarboxylic aminoaciduria (DCBXA, MIM:222730), autosomal recessive; variants R445W and I395del [PMID:21123949 "These mutations of conserved residues impeded or abrogated glutamate and cysteine transport by SLC1A1 and led to near-absent surface expression in a canine kidney cell line"].
2. Neuronal: somatodendritic glutamate transporter; buffers synaptic/perisynaptic glutamate (minor vs EAAT2). Immunolocalization: [PMID:9409715 "intense labeling of neuronal somata, dendrites, fine-caliber fibers and puncta"]; glia-negative: [PMID:9409715 "astrocytes were not co-labeled for EAAC1"]. Excluded from presynaptic membranes: [PMID:33658209 "excluded from presynaptic membranes"].
3. Neuronal cysteine uptake → glutathione / antioxidant defense: EAAT3 is the major neuronal Na+-dependent cysteine route: [PMID:21123949 "Neurons use sodium-dependent cysteine uptake as the major route for cysteine uptake (80%-90% of total uptake), most of which is handled by SLC1A1"]; [PMID:33658209 "transport cysteine, which is a rate-limiting intermediate in the biosynthesis of the antioxidant glutathione"]. NOTE: EAAT3 supplies the cysteine substrate; it does not itself catalyse any glutathione-biosynthesis step (GCL/GSS do). So GO:0006750 glutathione biosynthetic process is a substrate-supply/upstream role, not participation → over-annotation. Likewise superoxide metabolic process, neuron apoptosis protection are downstream of transport.

## Regulation / interactions

- ARL6IP5 / GTRAP3-18 (JWA): negative modulator of EAAT3 glutamate uptake [PMID:12562531 "GTRAP3-18 (JWA, Arl6ip5) is a novel protein that interacts with EAAT3 and negatively modulates EAAT3-mediated glutamate uptake"]. UniProt: "Negatively regulated by ARL6IP5."
- Caveolin-1: negative regulator, forms complexes with EAAT3 [PMID:26690923 "caveolin-1 is a powerful negative regulator of the excitatory glutamate transporters EAAT1, EAAT2, EAAT3, and EAAT4"].
- Numb: clathrin adaptor directing EAAT3 trafficking via YVNGGF (YxNxxF) motif [PMID:27358480 "Numb ... directly binds the YVNGGF motif and regulates the localization of EAAT3"]; EAAT3 "localizes primarily within the cell and at the apical plasma membrane" — intracellular recycling-endosome pool.
- Many PDZ scaffolds (DLG1-4/PSD-95, GRIP1/2, PDZK1, NHERF2/4, MPDZ, MAGI1/2, PATJ, TJP1, WHRN) and RNF5, RTN2, SORCS2 (UniProt SUBUNIT/INTERACTION). These are captured as regulation/trafficking context; bare GO:0005515 protein-binding rows are uninformative and removed per policy.

## Disease
- DCBXA (MIM:222730) — the established LoF phenotype [PMID:21123949].
- SCZD18 susceptibility (MIM:615232) — 9p24.2 deletion upstream of SLC1A1 [UniProt DISEASE; PMID:21982423, PMID:23341099]. Regulatory/dosage, not a transporter-function claim.

## Localization summary
Core: plasma membrane (GO:0005886), apical plasma membrane in epithelia (GO:0016324).
Non-core (genuine but peripheral): somatodendritic/synaptic neuronal compartments (soma,
dendrite/spine/shaft, perikaryon, axon terminus, synapse, perisynaptic), endosomal
recycling pool (early/late/recycling endosome membrane), membrane raft/caveolae,
cell surface, urinary extracellular exosome (HDA, [PMID:19056867 "Normal human urine contains large numbers of exosomes"]).
"Active in cytoplasm" is misleading (the transport activity is at the PM).
Glial cell projection ISS is at odds with the neuronal/epithelial expression and
Shashidharan's astrocyte-negative data → over-annotation (ortholog transfer).

## Annotation decisions (headline)
- Core MF: high-affinity L-glutamate transmembrane transporter activity (GO:0005314),
  glutamate:sodium symporter activity (GO:0015501), L-aspartate transmembrane transporter
  activity (GO:0015183), L-cysteine transmembrane transporter activity (GO:0033229).
- TOO_GENERAL: symporter activity (GO:0015293), amino acid transport (GO:0006865),
  import into cell (GO:0098657), cell periphery (GO:0071944) — all entailed by accepted specifics.
- MODIFY membrane (GO:0016020) → plasma membrane (GO:0005886).
- REMOVE: all bare protein binding (GO:0005515) rows (IntAct/IPI + MGI) per protein-binding policy.
- MARK_AS_OVER_ANNOTATED: Ensembl ortholog-projected behavioral/pharmacological/physiological
  phenotypes (response to amphetamine/morphine/cocaine, grooming/locomotory/motor/adult/exploration
  behavior, memory, conditioned place preference, heart-rate regulation, dopamine signaling/metabolism,
  gene expression, cytokine signaling, neurogenesis, brain/retina development, synapse organization,
  glutamate receptor signaling, neuron apoptosis +/- reg); downstream metabolic terms (glutathione
  biosynthetic process, superoxide metabolic process, zinc homeostasis/transport); BBB terms
  (transport across/maintenance of BBB, blood vessel morphogenesis); is_active_in cytoplasm;
  glial cell projection; presynapse.
