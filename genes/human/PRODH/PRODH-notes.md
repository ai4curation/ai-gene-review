# PRODH (human) — review notes

UniProt: O43272 (PROD_HUMAN), "Proline dehydrogenase 1, mitochondrial"; EC 1.5.5.2.
Aliases: proline oxidase (POX), proline oxidase 2, p53-induced gene 6 protein (PIG6).
Gene at 22q11.2; HGNC:9453.

## Core molecular function and reaction

PRODH catalyzes the first, committed step of proline catabolism: oxidation of
L-proline to (S)-1-pyrroline-5-carboxylate (P5C), a FAD-dependent dehydrogenase
that donates electrons to the mitochondrial electron transport chain (ubiquinone).

- Reaction (UniProt CATALYTIC ACTIVITY, EC 1.5.5.2):
  [file:human/PRODH/PRODH-uniprot.txt "Reaction=L-proline + a quinone = (S)-1-pyrroline-5-carboxylate + a"]
- FUNCTION: [file:human/PRODH/PRODH-uniprot.txt "Converts proline to delta-1-pyrroline-5-carboxylate."]
- Cofactor FAD: [file:human/PRODH/PRODH-uniprot.txt "Name=FAD; Xref=ChEBI:CHEBI:57692;"]
- Pathway: [file:human/PRODH/PRODH-uniprot.txt "L-proline degradation into L-"] glutamate; step 1/2.
- GO:0004657 "proline dehydrogenase activity" definition matches exactly: "L-proline + a
  quinone = (S)-1-pyrroline-5-carboxylate + a quinol + H+" (OLS/go.db). This is the correct
  catalytic MF; verified experimentally in [PMID:15662599].

Bender et al. 2005 directly assayed POX activity of WT and mutant PRODH and describe it as a
"mitochondrial inner-membrane enzyme that catalyzes the first step in the proline"
degradation pathway [PMID:15662599 "mitochondrial inner-membrane enzyme that catalyzes the first step in the proline"].
The EC=1.5.5.2 and FAD cofactor are ECO:0000269|PubMed:15662599 in UniProt.

## Localization

- UniProt SUBCELLULAR LOCATION: [file:human/PRODH/PRODH-uniprot.txt "Mitochondrion matrix."]
- Reactome (R-HSA-70670) and Bender 2005: the enzyme is tightly bound to the inner
  mitochondrial membrane [reactome:R-HSA-70670 "coupled to the conversion of FAD to FADH2 is the first step in proline breakdown"].
- Functionally, PRODH is an inner-membrane-associated flavoprotein whose FAD passes electrons to
  ubiquinone in the ETC; the enzyme is bound to the matrix face of the inner membrane. Both
  GO:0005743 (inner membrane, TAS/Reactome) and GO:0005759 (matrix, IEA/SubCell) are consistent.
  Inner membrane (GO:0005743) is the more functionally informative core location.

## Secondary / regulatory functions (genuine, non-core)

- p53 target ("PIG6"). Induced during p53/TP53-induced apoptosis
  [file:human/PRODH/PRODH-uniprot.txt "During p53/TP53-induced apoptosis."]. Polyak et al. 1997
  identified PRODH among p53-induced redox genes as part of a ROS-generating apoptotic program
  [PMID:9305847] — this is the basis of the NAS annotation to GO:0008631 (intrinsic apoptotic
  signaling in response to oxidative stress). PRODH generates ROS/superoxide during proline
  oxidation, which links it to redox signaling and apoptosis. Genuine but secondary to the
  catabolic role → KEEP_AS_NON_CORE.
- GO:1903376 (regulation of oxidative-stress-induced neuron intrinsic apoptotic signaling),
  IDA from [PMID:23743200] (ParkinsonsUK-UCL). NOTE: the cached abstract of PMID:23743200 is
  about DJ-1/PARK7 and PYCR1 (P5C reductase, proline *biosynthesis*), and does not mention PRODH
  in the abstract. This is an experimental (IDA) annotation made by a curator with full-text
  access; per policy do not REMOVE an experimental annotation from an incomplete (abstract-only)
  view. The redox/apoptosis role of PRODH is biologically real, so retain as KEEP_AS_NON_CORE
  (non-core, and secondary — flagged for the mismatch between abstract and annotated gene).

## Hydroxyproline over-annotation (paralog confusion)

- GO:0019470 "trans-4-hydroxy-L-proline catabolic process" is annotated TAS from [PMID:21998747].
  That paper (human HOGA / 4-hydroxy-2-oxoglutarate aldolase structure) describes the 4-Hyp
  degradation pathway as using **hydroxyproline oxidase (HPOX)** as the first enzyme — this is the
  distinct paralog PRODH2 (HYPDH), NOT PRODH. PRODH oxidizes L-proline; 4-hydroxy-L-proline is the
  substrate of PRODH2. The paper does not implicate PRODH in hydroxyproline catabolism
  [PMID:21998747 "hydroxyproline oxidase (HPOX)"]. This looks like a paralog mis-attribution /
  over-annotation. It is TAS (not experimental), so MARK_AS_OVER_ANNOTATED (conservative; not
  removed).

## Disease

- Hyperprolinemia type 1 (HYRPRO1, MIM 239500): loss-of-function/hypomorphic PRODH variants raise
  plasma/urine proline [file:human/PRODH/PRODH-uniprot.txt covers HYRPRO1].
- Schizophrenia susceptibility (SCZD4, MIM 600850); PRODH is in the 22q11 (velocardiofacial/DiGeorge)
  deletion region. Reduced POX function is a schizophrenia risk factor [PMID:15662599 abstract];
  PRODH modulates sensorimotor gating in mice [PMID:10192398].

## Annotation-by-annotation disposition (summary)

Core MF: GO:0004657 proline dehydrogenase activity (the IDA/PMID:15662599, IBA, IEA copies → ACCEPT;
the TAS/PMID:10192398 copy → ACCEPT).
GO:0016649 (oxidoreductase, CH-NH donor, quinone acceptor) EXP → parent of 0004657; ACCEPT
  (correct but more general; the specific 0004657 is the core term).
Core cofactor MF: GO:0071949 FAD binding (IDA + IBA) → ACCEPT.
Core BP: GO:0006562 L-proline catabolic process (IBA, IEA, TAS/Reactome) → ACCEPT.
Location: GO:0005743 inner membrane (TAS/Reactome) → ACCEPT (core); GO:0005739 mitochondrion
  (IBA is_active_in, IEA, HTP) → ACCEPT/KEEP_AS_NON_CORE (correct but general); GO:0005759
  matrix (IEA/SubCell) → ACCEPT (consistent with UniProt).
GO:0019470 hydroxyproline catabolism (TAS) → MARK_AS_OVER_ANNOTATED (paralog PRODH2/HPOX).
GO:0008631 apoptotic signaling in response to oxidative stress (NAS) → KEEP_AS_NON_CORE.
GO:1903376 regulation of oxidative-stress neuron apoptosis (IDA) → KEEP_AS_NON_CORE.

GO:0010133 "L-proline catabolic process to L-glutamate" (in UniProt DR line as IBA:GO_Central) is
now OBSOLETE in GO — not present in the seeded GOA TSV, so not reviewed; would map to GO:0006562.
