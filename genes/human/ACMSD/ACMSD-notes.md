# ACMSD (human) — gene review notes

UniProt: Q8TDX5 (ACMSD_HUMAN), 336 aa, chromosome 2. HGNC:19288. EC 4.1.1.45.

## Identity / naming
- RecName: **2-amino-3-carboxymuconate-6-semialdehyde decarboxylase**; EC 4.1.1.45; AltName **Picolinate carboxylase**
  [file:human/ACMSD/ACMSD-uniprot.txt "RecName: Full=2-amino-3-carboxymuconate-6-semialdehyde decarboxylase"; "AltName: Full=Picolinate carboxylase"].
- Classic biochemical name: alpha-amino-beta-carboxymuconate-epsilon-semialdehyde decarboxylase (ACMSD).

## Core catalytic function
- Converts alpha-amino-beta-carboxymuconate-epsilon-semialdehyde (ACMS) to alpha-aminomuconate
  semialdehyde (AMS), a benign catabolite
  [file:human/ACMSD/ACMSD-uniprot.txt "Converts alpha-amino-beta-carboxymuconate-epsilon- semialdehyde (ACMS) to alpha-aminomuconate semialdehyde (AMS)"].
- Reaction (Rhea:16557 / EC 4.1.1.45): (2Z,4Z)-2-amino-3-carboxymuconate 6-semialdehyde + H+ =
  2-aminomuconate 6-semialdehyde + CO2
  [file:human/ACMSD/ACMSD-uniprot.txt "Reaction=(2Z,4Z)-2-amino-3-carboxymuconate 6-semialdehyde + H(+) = 2-"].
- Original cDNA cloning + catalytic activity + function: Fukuoka et al. 2002 [PMID:12140278].
- Recombinant human enzyme kinetics (Zn form): Km 5.8 uM, kcat ~7.5 s^-1
  [PMID:25392945 "The Km (5.8 μM) and the kcat (7.5 s−1) values of hACMSD"].

## Branch-point / pathway role
- ACMS is unstable and non-enzymatically dehydrates to quinolinic acid (QUIN), the universal precursor
  for de novo NAD biosynthesis
  [PMID:25392945 "ACMS is unstable and non-enzymatically dehydrates to quinolinic acid (QUIN)"; "QUIN is the universal precursor for the de novo biosynthesis of NAD, providing the pyridine ring"].
- ACMSD is the only known enzyme that processes ACMS to a benign catabolite, preventing quinolinate
  accumulation [PMID:12140278 "the only known enzyme that can process ACMS to a benign catabolite and thus prevent the accumulation of quinolinate from ACMS"].
- Sits at the branch point of the tryptophan-to-NAD pathway, determining the fate of the amino acid:
  transformation into PA (picolinic acid), complete oxidation through the citric acid cycle, or
  conversion into NAD through QA synthesis
  [PMID:19843166 "the enzyme stands at a branch point of the tryptophan to NAD pathway, and determines the final fate of the amino acid, i.e. transformation into PA, complete oxidation through the citric acid cycle, or conversion into NAD through QA synthesis"].
- ACMSD ultimately controls the metabolic fate of tryptophan catabolism along the kynurenine pathway
  [file:human/ACMSD/ACMSD-uniprot.txt "ACMSD ultimately controls the metabolic fate of tryptophan catabolism along the kynurenine pathway"].
- QUIN is a potent endogenous NMDA-receptor excitotoxin; its accumulation is implicated in
  neurodegenerative disease ("quinolinate hypothesis")
  [PMID:12140278 "Quinolinate (quinolinic acid) is a potent endogenous excitotoxin of neuronal cells"].

## Metal / structure
- Zinc-dependent amidohydrolase-superfamily enzyme
  [PMID:19843166 "a zinc-dependent amidohydrolase that participates in picolinic acid (PA), quinolinic acid (QA) and NAD homeostasis"].
- Activity is proportional to zinc content; hACMSD is a zinc-dependent metalloenzyme
  [PMID:25392945 "the activity of hACMSD is proportional to the zinc content of the enzyme. These results suggest that hACMSD is a zinc-dependent metalloenzyme"].
- Zn-binding residues His6, His8, His174, Asp291 (UniProt BINDING features, ECO:0000269|PubMed:19843166).
- Belongs to the metallo-dependent hydrolases superfamily, ACMSD family
  [file:human/ACMSD/ACMSD-uniprot.txt "Belongs to the metallo-dependent hydrolases superfamily. ACMSD family."].
- Note: the amidohydrolase-superfamily fold explains the InterPro "hydrolase activity" IEA, but ACMSD
  is mechanistically a decarboxylase (lyase), not a hydrolase; the metal ion serves the decarboxylation
  chemistry. Substrate does NOT directly coordinate the metal; it is held by active-site arginines
  (Arg47, Arg235*) [PMID:25392945 "the substrate analogue does not directly coordinate to the metal ion but is bound to the active site by two arginine residues"].

## Oligomeric state
- UniProt: Monomer [file:human/ACMSD/ACMSD-uniprot.txt "SUBUNIT: Monomer."].
- Crystallography (Huo 2015): trimer of dimers in the asymmetric unit; dilution to nM loses activity,
  implying the enzyme is unlikely to be active as a monomer
  [PMID:25392945 "hACMSD is unlikely to be active in the monomeric state"]. So oligomeric state is
  somewhat contested between the two structural studies; not central to the review.

## Localization
- Cytosol (IDA, UniProt, PMID:12140278). HPA: group enriched kidney/liver
  [file:human/ACMSD/ACMSD-uniprot.txt "Group enriched (kidney, liver)"]. Consistent with the liver/kidney
  site of hepatic tryptophan-to-NAD and picolinate metabolism.

## Interaction annotation
- GO:0005515 protein binding IPI from PMID:25416956 (Rolland et al., proteome-scale interactome map,
  IntAct with MAGEA11 / P43364-2). Large-scale Y2H screen; no ACMSD-specific functional interpretation
  in the paper. Bare "protein binding" — uninformative for MF; kept but marked over-annotated (do not
  REMOVE an IPI per policy).

## Drug-target context
- DHAP (glycolytic intermediate) is a potent ACMSD inhibitor, suggesting a regulatory link between NAD
  synthesis and glycolysis [PMID:19843166 "DHAP, which we discovered to be a potent enzyme inhibitor"].
- ACMSD inhibition raises cellular NAD+; ACMSD is an actively pursued small-molecule drug target
  (Pharos Tchem; ChEMBL; DrugCentral). This is downstream pharmacology, not a distinct GO function.

## Curation summary of existing annotations
- Core MF: **GO:0001760 aminocarboxymuconate-semialdehyde decarboxylase activity** — multiple IDA
  (PMID:12140278 original cloning, PMID:25392945 recombinant human enzyme). ACCEPT (core).
- **GO:0008270 zinc ion binding** IDA (PMID:25392945, PMID:19843166) — ACCEPT (core; catalytically
  essential Zn). Note: PMID:19843166 defines the Zn-binding sites structurally; PMID:25392945
  demonstrates Zn-dependence biochemically.
- **GO:1904985 negative regulation of quinolinate biosynthetic process** IDA (PMID:12140278) — ACCEPT;
  this is the defining physiological consequence of the reaction (diverting ACMS away from
  spontaneous cyclisation to quinolinate).
- **GO:0006569 L-tryptophan catabolic process** (TAS/IEA) — ACCEPT (kynurenine-pathway BP).
- **GO:1905012 regulation of 'de novo' NAD biosynthetic process from L-tryptophan** (TAS x2) — ACCEPT;
  by controlling quinolinate supply ACMSD regulates de novo NAD synthesis.
- **GO:1905004 picolinic acid biosynthetic process** (TAS) — ACMS → AMS is the committed step upstream
  of picolinate formation; KEEP_AS_NON_CORE (ACMSD does not itself make picolinate; downstream product).
- **GO:0005829 cytosol** IDA (PMID:12140278) + IBA — ACCEPT (core location).
- **GO:0005737 cytoplasm** IBA — parent of cytosol; KEEP_AS_NON_CORE (redundant/general vs cytosol).
- **GO:0016831 carboxy-lyase activity** IEA (InterPro) — correct parent class of the decarboxylase MF;
  MARK_AS_OVER_ANNOTATED (redundant general parent of GO:0001760).
- **GO:0016787 hydrolase activity** IEA (InterPro, from amidohydrolase fold) — mechanistically wrong:
  ACMSD is a decarboxylase/lyase, not a hydrolase; the term derives from the fold family (IPR006680
  Amidohydro-rel), not the reaction. MODIFY → GO:0016831 carboxy-lyase activity (or REMOVE as a
  clearly-wrong fold-based IEA). Chose MODIFY to point to the correct lyase parent.
- **GO:0019748 secondary metabolic process** IBA — tryptophan/NAD catabolism is primary/central
  metabolism, not secondary metabolism; misleading. MARK_AS_OVER_ANNOTATED (IBA, do not REMOVE by
  preference; the specific tryptophan-catabolism BP terms already cover the biology).
- **GO:0005515 protein binding** IPI (PMID:25416956) — bare, uninformative; MARK_AS_OVER_ANNOTATED.
- **GO:0001760** IEA (GO_REF:0000120, ARBA) — same MF as the IDA; ACCEPT (redundant IEA of the core MF).

## Core functions chosen
1. MF GO:0001760 aminocarboxymuconate-semialdehyde decarboxylase activity (EC 4.1.1.45), Zn-dependent
   (GO:0008270), in cytosol (GO:0005829), directly involved in L-tryptophan catabolic process
   (GO:0006569), negative regulation of quinolinate biosynthesis (GO:1904985), and regulation of de
   novo NAD biosynthesis from L-tryptophan (GO:1905012).
