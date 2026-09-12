# CPT2 (Carnitine O-palmitoyltransferase 2, mitochondrial) — review notes

UniProt: P23786 (CPT2_HUMAN), 658 aa, HGNC:2330, chromosome 1p32.
EC 2.3.1.21. Belongs to the carnitine/choline acetyltransferase family.

## Core biology (verified)

CPT2 is the matrix-facing enzyme of the mitochondrial **inner membrane** that
completes the carnitine shuttle. After CPT1 (outer membrane) converts long-chain
acyl-CoA + carnitine to acylcarnitine, and the carnitine/acylcarnitine
translocase (SLC25A20) moves acylcarnitine across the inner membrane, **CPT2
regenerates long-chain acyl-CoA in the matrix**: long-chain acylcarnitine + CoA →
long-chain acyl-CoA + L-carnitine. This is the final step of the shuttle and is
required so that beta-oxidation can proceed in the matrix.

- UniProt FUNCTION: "Involved in the intramitochondrial synthesis of
  acylcarnitines from accumulated acyl-CoA metabolites ... Reconverts
  acylcarnitines back into the respective acyl-CoA esters that can then undergo
  beta-oxidation, an essential step for the mitochondrial uptake of long-chain
  fatty acids and their subsequent beta-oxidation in the mitochondrion. Active
  with medium (C8-C12) and long-chain (C14-C18) acyl-CoA esters."
  [ECO:0000269|PubMed:20538056, PubMed:24780397]
- SUBCELLULAR LOCATION: "Mitochondrion inner membrane; Peripheral membrane
  protein; Matrix side." Topology features: matrix 26-178, intramembrane 179-208
  ("Mitochondrial inner membrane"), matrix 209-658. So the bulk (incl. catalytic
  domain) is matrix-facing but the protein is anchored/peripheral at the inner
  membrane. This makes both `mitochondrial inner membrane` (located_in) and
  `mitochondrial matrix` (is_active_in) reasonable.
- Catalytic activity: RHEA:12661 (hexadecanoyl-CoA + carnitine ⇌ palmitoylcarnitine
  + CoA), EC 2.3.1.21. Physiological direction annotated right-to-left (regenerating
  acyl-CoA). Multiple additional Rhea reactions for C8-C20 acyl-CoAs.

## Substrate specificity (PMID:20538056, Violante et al. 2010)

Human CPT2 expressed in S. cerevisiae; substrate profiling by ESI-MS/MS.
- "CPT2 is active with medium (C8-C12) and long-chain (C14-C18) acyl-CoA esters,
  whereas virtually no activity was found with short- and very long-chain
  acyl-CoAs or with branched-chain amino acid oxidation intermediates."
- Supports MF: carnitine O-palmitoyltransferase activity (GO:0004095, C16),
  carnitine O-octanoyltransferase activity (GO:0008458, C8), and the parent
  carnitine O-acyltransferase activity (GO:0016406).
- "trans-2-C16:1-CoA may act as a competitive inhibitor of CPT2 (K(i) of 18.8
  microM)" → ACTIVITY REGULATION.
- Km 7.1 uM for hexadecanoyl-CoA.
- This is the IDA/EXP basis for GO:0004095, GO:0008458, GO:0016406, GO:0016746
  (acyltransferase), GO:0001676 (long-chain fatty acid metabolic process),
  GO:0006635 (fatty acid beta-oxidation), GO:0009437 (carnitine metabolic process).
  All from the same paper (Reactome/UniProt attributions).

## Disease (context, not a GO BP by itself)

CPT2 deficiency (MONDO:0015515): autosomal recessive inborn error of mitochondrial
long-chain FAO. Three forms: lethal neonatal (CPT2DLN), severe infantile
hepatocardiomuscular (CPT2DI), and the common adult myopathic form (CPT2D,
MIM:255110) — the most common inherited disorder of muscle FA metabolism,
presenting as exercise/fever/fasting-triggered myalgia, rhabdomyolysis,
myoglobinuria. Thermolabile variants (F352C, V368I) predispose to
influenza-associated encephalopathy (IIAE4). Confirms core role in long-chain FAO
/ carnitine shuttle. (UniProt DISEASE; dismech KB
Carnitine_Palmitoyltransferase_II_Deficiency.yaml; PMID:24780397, PMID:7711730.)

## Thermogenesis (GO:0120162)

PMID:25578732 (Lee et al.): adipose-specific Cpt2 knockout MOUSE (Cpt2^A-/-).
"CPT2(A-/-) mice became hypothermic after an acute cold challenge, and CPT2(A-/-)
brown adipose tissue (BAT) failed to upregulate thermogenic genes..." Shows adipose
FAO (via CPT2) is required for cold-induced thermogenesis. The human
GO:0120162 "positive regulation of cold-induced thermogenesis" is an ISS/IEA
transfer from mouse ortholog P52825. This is a genuine but tissue-specific
(BAT), context-dependent physiological role — KEEP_AS_NON_CORE. The core function
is the enzymatic step of the carnitine shuttle; thermogenesis is a downstream
organismal consequence in a specific tissue.

## Protein-binding IPIs (bare protein binding)

- PMID:28514442 (BioPlex/Huttlin interactome), PMID:32296183 (HuRI binary
  interactome; partners CYSRT1/A8MQ03, OTX1/P32242), PMID:33961781 (BioPlex
  cell-specific). MCUR1 (Q96AQ8) interaction also listed. These are high-throughput
  interactome screens; CPT2 appears only in supplementary partner tables, not main
  text. Bare `protein binding` (GO:0005515) is uninformative and none define a
  specific molecular function. Per policy: MARK_AS_OVER_ANNOTATED (not REMOVE for
  experimental IPI). UniProt INTERACTION section lists CYSRT1, MCUR1, OTX1.

## Annotation plan summary

Core functions:
- MF GO:0004095 carnitine O-palmitoyltransferase activity (well supported IDA/EXP).
- BP GO:0006853 carnitine shuttle (directly_involved_in) — the process CPT2 completes.
- BP GO:0006635 fatty acid beta-oxidation (directly_involved_in) — enabled by CPT2's step.
- CC GO:0005743 mitochondrial inner membrane (location; matrix side).

Actions:
- ACCEPT: MF carnitine O-palmitoyltransferase (IBA, IEA, EXP, IDA, NAS);
  carnitine O-octanoyltransferase (IEA, EXP); carnitine O-acyltransferase (EXP x2);
  fatty acid beta-oxidation (IBA, IEA, IDA); carnitine shuttle (IEA, TAS);
  carnitine metabolic process (IDA); long-chain fatty acid metabolic process (IDA);
  mitochondrion (IBA, IDA, HTP); mitochondrial inner membrane (IEA, TAS x2, NAS);
  mitochondrial matrix (IEA).
- MODIFY: GO:0016746 acyltransferase activity (IEA, IDA) — too general; replace with
  GO:0004095. GO:0015909 long-chain fatty acid transport (ARBA IEA) — CPT2 does not
  transport FAs across membrane (that's the translocase SLC25A20); its role is
  enzymatic regeneration of acyl-CoA enabling import. Replace with carnitine shuttle
  / fatty acid beta-oxidation.
- KEEP_AS_NON_CORE: GO:0120162 positive regulation of cold-induced thermogenesis
  (ISS, IEA) — real but tissue-specific downstream role.
- MARK_AS_OVER_ANNOTATED: three GO:0005515 protein binding IPIs (bare protein binding).
</content>
