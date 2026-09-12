# SLC25A12 (Aralar / AGC1) — gene review notes

## Identity
- UniProt: O75746 (S2512_HUMAN); HGNC:10982; gene SLC25A12; 678 aa.
- RecName: "Electrogenic aspartate/glutamate antiporter SLC25A12, mitochondrial";
  AltName: Aralar / Aralar1; Mitochondrial aspartate glutamate carrier 1 (AGC1);
  synonyms AGC1, ARALAR1 [file:human/SLC25A12/SLC25A12-uniprot.txt lines 6-14].
- Member of the mitochondrial carrier (SLC25 / TC 2.A.29) family
  [file:human/SLC25A12/SLC25A12-uniprot.txt "Belongs to the mitochondrial carrier (TC 2.A.29) family."].
- Paralog: SLC25A13 / citrin / AGC2 (Q9UJS0), the non-excitable-tissue isoform; 77% identical
  [PMID:25410934 "The two human isoforms citrin (74 kDa) and aralar (75 kDa) are 77% identical"].

## Core molecular function — aspartate/glutamate antiporter
- Mitochondrial electrogenic aspartate/glutamate antiporter: exports L-aspartate from the matrix
  in exchange for cytosolic L-glutamate + H+
  [file:human/SLC25A12/SLC25A12-uniprot.txt "that favors efflux of aspartate and entry of glutamate and proton"].
- Rhea reaction (UniProt CATALYTIC ACTIVITY): L-aspartate(in) + L-glutamate(out) + H(+)(out) =
  L-aspartate(out) + L-glutamate(in) + H(+)(in); RHEA:70783
  [file:human/SLC25A12/SLC25A12-uniprot.txt lines 221-226].
- Reconstituted-liposome proof of transport function (recombinant human aralar1 + citrin):
  [PMID:11566871 "reconstituted \ninto liposomes and shown to catalyze the electrogenic exchange of aspartate for \nglutamate and a H"].
  Overexpression in HEK-293T cells raised shuttle activity
  [PMID:11566871 "increased the activity of the malate/aspartate NADH shuttle"].
- Ca2+ stimulation from the external (IMS) face of the inner membrane
  [PMID:11566871 "was stimulated by Ca 2+ on the external side of"; and file:...-uniprot.txt
  "ACTIVITY REGULATION: Activated by calcium-binding in the mitochondrial"].
- Also transports L-cysteinesulfinate in exchange for glutamate or aspartate
  [PMID:11566871 "AGC also transports cysteinesulfinate in exchange for either aspartate or glutamate"].
  This underlies the GO:0000514 (3-sulfino-L-alanine:proton,glutamate antiporter) annotation (IDA PMID:11566871).
- Does NOT transport GABA (negative finding, corrects a Drosophila claim) and does not transport
  L-glutamine [PMID:38945283 "AGC does not transport GABA"; "GABA has no inhibitory effect on the";
  file:...-uniprot.txt "Lacks transport activity towards L-glutamine or ... GABA"].

### GO term choice for core MF
- GO:0000515 "aspartate:glutamate, proton antiporter activity" (MF) is the most specific term and
  matches the Rhea reaction exactly. Confirmed in go.db to be a descendant of GO:0015183
  (L-aspartate transmembrane transporter activity), GO:0005313 (L-glutamate transmembrane transporter
  activity), GO:0015297 (antiporter activity), and GO:0015078 (proton transmembrane transporter
  activity). Strong experimental support: IDA PMID:11566871, EXP PMID:19641205, EXP/IDA PMID:24515575,
  EXP PMID:38945283. This is the primary core function.
- GO:0000514 "3-sulfino-L-alanine: proton, glutamate antiporter activity" (MF, IDA PMID:11566871) is
  a genuine secondary catalytic-transport activity (cysteinesulfinate carrier).
- The IBA terms GO:0015183 and GO:0005313 are correct but less specific parents of GO:0000515.

## Secondary molecular function — calcium binding (EF-hands)
- N-terminal regulatory domain (residues 2-294) has EF-hand motifs; binds Ca2+ in the IMS to gate the
  carrier [file:...-uniprot.txt "Regulatory N-terminal domain"; "binds one calcium in the mitochondrial
  intermembrane space. Calcium"].
- Crystal structures (4P5X/4P60): homodimer; of 8 EF-hands only EF-hand 2 binds Ca2+; EF-hands 4-8 form
  a static dimerization interface [PMID:25410934 "Only EF-hand 2 binds calcium"; "form a twofold
  symmetrical homodimer"; "import glutamate together with a proton into the mitochondrial matrix and
  export aspartate"].
- GO:0005509 calcium ion binding is well supported experimentally (IDA PMID:9722566, IDA PMID:25410934).
  GO:0042802 identical protein binding (IDA PMID:25410934) captures the homodimer (SUBUNIT: "Homodimer
  (via N-terminus)").

## Biological process
- Makes the malate-aspartate shuttle directional/irreversible; transfers reducing equivalents (NADH)
  into mitochondria [PMID:19641205 "supplies aspartate to the cytosol and, as a component of the";
  "malate-aspartate shuttle, enables mitochondrial oxidation of cytosolic NADH"; PMID:24515575 "an
  essential component of the" neuronal malate/aspartate shuttle that "transfers NADH and H(+) reducing"
  equivalents]. GO:0043490 malate-aspartate shuttle (IDA PMID:11566871; IGI PMID:37647199).
- Downstream transport processes: GO:0015810 aspartate transmembrane transport, GO:0015813 L-glutamate
  transmembrane transport (both IDA PMID:11566871/19641205/24515575) — components of the antiport.
- Ca2+ regulation captured by GO:0051592 response to calcium ion (IDA PMID:11566871).

## Localization
- Mitochondrion inner membrane, multi-pass; N- and C-terminal domains face the intermembrane space
  [file:...-uniprot.txt "SUBCELLULAR LOCATION: Mitochondrion inner membrane"]. GO:0005743 mitochondrial
  inner membrane (IDA PMID:11566871; EXP PMID:9722566/19641205/24515575; TAS Reactome). GO:0005739
  mitochondrion (IDA/HDA/HTP) is the correct but less specific parent.

## Physiology / disease
- Predominantly heart and skeletal muscle, weaker in brain/kidney; neuron- and muscle-specific isoform
  [file:...-uniprot.txt "Expressed predominantly in the heart and skeletal muscle, weakly in brain and kidney"].
- Biallelic loss-of-function causes Developmental and epileptic encephalopathy 39 with leukodystrophy
  (DEE39; MIM:612949) — global cerebral hypomyelination, epilepsy, reduced N-acetylaspartate. Variants
  Q590R and R353Q abolish/reduce antiporter activity [PMID:19641205 "showed abolished activity";
  PMID:24515575 "AGC1 activity was reduced to 15% of" wild type]. Neuronal aspartate efflux is required
  for NAA production and myelination.

## Protein-binding (IPI) annotations
- GO:0005515 protein binding IPIs: with SLC25A13/citrin (Q9UJS0; PMID:28514442 BioPlex, PMID:33961781,
  PMID:40355756 SLC superfamily interactome) and with MAVS (Q7Z434; PMID:31767682). These are generic
  "protein binding" (uninformative MF); the citrin ones are consistent with the shared SLC25 biology and
  the UniProt IntAct records (O75746–Q9UJS0, O75746–Q7Z434). Per policy, bare protein binding IPIs are
  marked MARK_AS_OVER_ANNOTATED (not removed); the homodimer is better captured by GO:0042802.
- PMID:31767682: SLC25A12, as part of a prohibitin complex, associates with MAVS and links mitochondrial
  metabolism to antiviral innate immunity [PMID:31767682 "associates with the mitochondrial
  antiviral-signaling"]. This is a regulatory/context finding, not a core MF.

## Annotation-action summary (rationale)
- ACCEPT (core): GO:0000515 antiporter MF (all IDA/EXP), GO:0043490 malate-aspartate shuttle (IDA/IGI),
  GO:0005743 mito inner membrane (IDA/EXP), GO:0005509 calcium ion binding (IDA).
- ACCEPT (non-core but correct/experimental): GO:0000514 cysteinesulfinate antiporter (IDA), GO:0015810,
  GO:0015813 (IDA transport processes), GO:0051592 response to calcium (IDA), GO:0042802 identical
  protein binding (IDA, homodimer), GO:0005739 mitochondrion (IDA/HDA/HTP), GO:0016020 membrane (NAS,
  less specific parent).
- IBA (phylogenetic) annotations to transporter MF/BP and inner membrane: ACCEPT (consistent with
  experimental data), though GO:0015183/GO:0005313 are less specific than GO:0000515.
- IEA: mostly ACCEPT as correct-but-redundant (ARBA duplicates of experimental terms; SubCell inner
  membrane; InterPro transmembrane transport). GO:0015804 "neutral amino acid transport" (GOC inference
  from the cysteinesulfinate term) and GO:1902600 "proton transmembrane transport" (GOC) are marked
  over-annotated / kept as non-core — aspartate and glutamate are acidic amino acids, and the proton is
  co-transported as part of the antiport rather than representing a standalone proton-transport function.
- Protein binding IPIs (GO:0005515 x4): MARK_AS_OVER_ANNOTATED (uninformative bare MF), never removed.
</content>
</invoke>
