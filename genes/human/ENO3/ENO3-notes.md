# ENO3 (Beta-enolase / muscle-specific enolase) review notes

UniProtKB: P13929 (ENOB_HUMAN), 434 aa, HGNC:3354, gene on chr17.

## Core biology
ENO3 is the beta (muscle-specific) isozyme of enolase, a cytosolic metalloenzyme
of the enolase superfamily. It catalyses the penultimate step of glycolysis:
the Mg2+-dependent, reversible dehydration of 2-phospho-D-glycerate (2-PG) to
phosphoenolpyruvate (PEP) + H2O; the reverse hydration reaction operates in
gluconeogenesis.

- EC 4.2.1.11; Rhea:RHEA:10164 (2R)-2-phosphoglycerate = phosphoenolpyruvate + H2O
  [file:human/ENO3/ENO3-uniprot.txt "Reaction=(2R)-2-phosphoglycerate = phosphoenolpyruvate + H2O"]
- FUNCTION: "Enolase that catalyzes the conversion of 2-phosphoglycerate to
  phosphoenolpyruvate in glycolysis and the reverse reaction in gluconeogenesis.
  Appears to have a function in striated muscle development and regeneration."
  [file:human/ENO3/ENO3-uniprot.txt]
- COFACTOR: "Mg(2+) is required for catalysis and for stabilizing the dimer."
  [file:human/ENO3/ENO3-uniprot.txt]
- PATHWAY: "Carbohydrate degradation; glycolysis; pyruvate from D-glyceraldehyde
  3-phosphate: step 4/5." [file:human/ENO3/ENO3-uniprot.txt]

## Isozymes / quaternary structure
Mammalian enolase is a dimer built from three tissue subunits: alpha (ENO1, ubiquitous),
beta (ENO3, muscle) and gamma (ENO2, neuronal). ENO3 forms alpha/beta heterodimers and
beta/beta homodimers in striated muscle.
[file:human/ENO3/ENO3-uniprot.txt "Mammalian enolase is composed of 3 isozyme subunits, alpha, beta and gamma"]
IntAct records the ENO1(P06733)-ENO3 interaction (the alpha/beta heterodimer).

## Localization
- SUBCELLULAR LOCATION: Cytoplasm; "Localized to the Z line. Some colocalization with
  CKM at M-band (By similarity)." [file:human/ENO3/ENO3-uniprot.txt] So a sarcomeric
  (Z-line / M-band) pool exists in addition to the bulk cytosol.
- HPA IDA: cytosol (GO:0005829) and plasma membrane (GO:0005886).
- Various HDA/IDA extracellular/membrane detections (exosome, tear fluid, membrane)
  are proteomic surveys, not indicators of the enzyme's core catalytic role — glycolytic
  enzymes are commonly detected in secretomes/exosomes. Treated as over-annotations.

## Disease
Glycogen storage disease type XIII (GSD13, MIM:612932), beta-enolase deficiency: a
metabolic myopathy of distal glycolysis; exercise-induced myalgias, generalized muscle
weakness/fatigability, increased serum creatine kinase, decreased ENO3 activity, focal
sarcoplasmic glycogen-beta accumulation. Caused by ENO3 variants (Asp-156, Glu-374 in
the seminal report). [file:human/ENO3/ENO3-uniprot.txt; PMID:11506403 (abstract not cached)]

## Annotation review summary (actions)
- MF GO:0004634 phosphopyruvate hydratase activity — CORE. Multiple lines (IBA, IEA,
  ISS, TAS x3). ACCEPT the IBA (phylogenetic, right level) as core; ACCEPT the others.
- MF GO:0000287 magnesium ion binding (IEA, InterPro) — ACCEPT; Mg2+ cofactor is
  experimentally documented as required for catalysis/dimer stability.
- BP GO:0006096 glycolytic process / GO:0061621 canonical glycolysis — CORE. ACCEPT.
- BP GO:0006094 gluconeogenesis — ACCEPT (reverse reaction; UniProt FUNCTION supports).
- CC GO:0000015 phosphopyruvate hydratase complex (IBA, IEA) — ACCEPT; the enolase dimer.
- CC GO:0005829 cytosol / GO:0005737 cytoplasm — ACCEPT (bulk localization).
- CC GO:0005886 plasma membrane (HPA IDA) — KEEP_AS_NON_CORE; enolase surface pool is
  reported but is not the core catalytic role.
- CC GO:0016020 membrane (CAFA IDA, PMID:19433310) — MARK_AS_OVER_ANNOTATED; the paper
  concerns alpha/gamma-enolase neuronal biology, membrane localization is not ENO3-core.
- CC GO:0070062 extracellular exosome (HDA) / GO:0005576 extracellular region (HDA) —
  MARK_AS_OVER_ANNOTATED; proteomic secretome/exosome detections, not core function.
- MF GO:0005515 protein binding (IPI x2, both with ENO1/P06733) — MARK_AS_OVER_ANNOTATED;
  bare "protein binding" is uninformative. The real content (alpha/beta heterodimer) is
  captured by GO:0000015 phosphopyruvate hydratase complex.

## References cited
See ENO3-uniprot.txt DR/CC blocks and publications/PMID_*.md. PMID:11506403 (GSD13) and
PMID:15188056 (PNKD interaction) are cited in UniProt but not cached here; not used for
supporting_text quotes.
