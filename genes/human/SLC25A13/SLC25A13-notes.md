# SLC25A13 (citrin / AGC2) review notes

UniProtKB Q9UJS0. Human liver-type calcium-binding mitochondrial aspartate/glutamate
carrier (AGC2). Paralog of SLC25A12 (aralar / AGC1), the brain/muscle isoform (77% identical).

## Core molecular function

- Electrogenic aspartate/glutamate antiporter: exports mitochondrial L-aspartate to the
  cytosol in exchange for cytosolic L-glutamate + H+. Electrogenic because aspartate is
  transported as the anion while glutamate is co-transported with a proton.
  [PMID:11566871 "shown to catalyze the electrogenic exchange of aspartate for glutamate and a H + "]
- Reaction (RHEA:70783): L-aspartate(in) + L-glutamate(out) + H+(out) = L-aspartate(out) +
  L-glutamate(in) + H+(in) (UniProt CATALYTIC ACTIVITY).
- Confirmed independently and shown NOT to transport GABA (EXP; PMID:38945283).
  [PMID:38945283 "the human AGC isoforms (AGC1/aralar1 and AGC2/citrin) are unable to transport GABA both in homo- and in hetero-exchange with either glutamate or aspartate"]
- Also exchanges L-cysteinesulfinate (3-sulfino-L-alanine) for glutamate+H+ or for aspartate
  (secondary substrate). [PMID:11566871 "AGC also transports cysteinesulfinate in exchange for either aspartate or glutamate"]
- Functions as a monomer with ping-pong kinetics for transport (PMID:38937634), though the
  full-length protein is a structural homodimer via the N-terminal domain (PMID:25410934).

## Biological process

- Component of the malate-aspartate NADH shuttle: overexpression increases MAS activity.
  [PMID:11566871 "Overexpression of the carriers in transfected human cells increased the activity of the malate/aspartate NADH shuttle"]
  MAS transfers cytosolic reducing equivalents into mitochondria and regenerates cytosolic NAD+.
- Urea cycle: supplies cytosolic aspartate consumed by ASS1 (argininosuccinate synthetase).
  [PMID:11566871 "The mitochondrial aspartate/glutamate carrier catalyzes an important step in both the urea cycle and the aspartate/malate NADH shuttle"]
  [PMID:25410934 "In liver, cytosolic aspartate is required for the urea cycle11, which is crucial for the production of urea from the deamination of amino acids"]
  Note: urea cycle (GO:0000050) is NOT currently in GOA for SLC25A13 -> add as NEW.
- Gluconeogenesis: cytosolic aspartate needed for oxaloacetate production.
  [PMID:25410934 "Cytosolic aspartate is also required for the conversion of oxoglutarate to oxaloacetate, a crucial step in gluconeogenesis from lactate and alanine"]
- MAS important for de novo serine biosynthesis (IGI panel of MAS-deficient cells; PMID:37647199,
  full text unavailable in cache but title/abstract support MAS role; SLC25A13 was one MAS component knocked out).

## Regulation / calcium binding

- N-terminal regulatory domain with EF-hands binds calcium in the intermembrane space; only
  EF-hand 2 binds Ca2+ (X-ray structure PDB 4P5W). [PMID:25410934 "Only EF-hand 2 binds calcium"]
  Ca2+ binding stimulates transport / MAS. [PMID:11566871 "stimulated by Ca 2+ on the external side of the inner mitochondrial membrane"]
- NB caveat: PMID:39419476 argues the N-terminal domain does NOT regulate transport via calcium
  as previously thought; instead N-terminal mutations cause a mitochondrial import defect.
  But calcium ion binding by EF-hand 2 is directly demonstrated (IDA, PMID:25410934) regardless
  of its regulatory role -> calcium ion binding annotation is valid.
- Ca2+-stimulated activity raises mitochondrial ATP on agonist stimulation (IDA; PMID:12851387).

## Localization

- Mitochondrial inner membrane, multi-pass (6 TM in carrier domain; N- and C-terminal domains
  protrude into the intermembrane space). [PMID:39419476 "located in the mitochondrial inner membrane"]
  Well supported by EXP/IDA (PMID:10642534, PMID:11566871, PMID:39419476).
- The PMID:10642534 NAS "plasma membrane" annotation is inconsistent with all experimental
  data (mitochondrial inner membrane). The paper itself concludes mitochondrial localization
  [PMID:10642534 "The localization of Aralar2/citrin expressed in human cell lines is mitochondrial"].
  -> REMOVE the plasma membrane annotation.

## Disease

- Citrin deficiency (autosomal recessive): NICCD (neonatal intrahepatic cholestasis), FTTDCD,
  and adult-onset CTLN2 (citrullinemia type II) with hyperammonemic encephalopathy. Broader than
  a pure urea-cycle-enzyme phenotype because of the MAS/redox role. (dismech Citrin_Deficiency.yaml;
  UniProt DISEASE CDAA/CDNI.)

## Interactions

- IntAct IPI annotations (PMID:28514442, PMID:33961781, PMID:40355756) all cite WITH/FROM
  UniProtKB:O75746 (SLC25A12 / aralar). UniProt records the Q9UJS0-O75746 interaction. These are
  bare "protein binding" -> uninformative, MARK_AS_OVER_ANNOTATED. GO:0042802 identical protein
  binding (PMID:25410934) reflects the demonstrated N-terminal homodimer -> KEEP_AS_NON_CORE.

## Falcon deep research

Falcon deep-research file did not land within the polling window; review grounded in the UniProt
record, the dismech Citrin_Deficiency.yaml disorder model, and cached publications.
</content>
