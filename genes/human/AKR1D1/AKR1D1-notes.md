# AKR1D1 (P51857) review notes

## Identity
- Human AKR1D1 = aldo-keto reductase family 1 member D1; a.k.a. 3-oxo-5-beta-steroid
  4-dehydrogenase; Delta(4)-3-ketosteroid 5-beta-reductase; Delta(4)-3-oxosteroid
  5-beta-reductase; gene synonym SRD5B1. EC 1.3.1.3.
- 326 aa, cytosolic (SUBCELLULAR LOCATION: Cytoplasm ECO:0000269|PubMed:7508385).
- Highly expressed in liver; also testis, weakly colon [file:human/AKR1D1/AKR1D1-uniprot.txt
  "Highly expressed in liver. Expressed in testis and"].

## Core molecular function
- NADPH-dependent stereospecific reduction of the C4-C5 (Delta4) double bond of
  3-oxo-Delta4 steroids to the 5-beta configuration, producing the A/B cis-ring
  junction characteristic of bile acids.
  [file:human/AKR1D1/AKR1D1-uniprot.txt "Catalyzes the stereospecific NADPH-dependent reduction of the"
   ... "C4-C5 double bond of bile acid intermediates and steroid hormones"]
- The specific, informative MF term is **GO:0047787 Delta4-3-oxosteroid 5beta-reductase
  activity** (present in GOA as IEA GO_REF:0000120 via EC:1.3.1.3 + RHEA). This is the
  CORE MF. The GOA also carries family-level GO:0004032 aldose reductase (NADPH) activity
  (IBA) — this is an over-annotation / less-informative parent-family activity; human
  AKR1D1 has only 50% identity to aldose reductase and is a 5-beta-reductase, not an
  aldose reductase [PMID:7508385 abstract: "50% overall identity with ... human aldose reductase"].
- Broad steroid substrate range C18–C27: bile acid intermediates (7alpha-hydroxy- and
  7alpha,12alpha-dihydroxy-cholest-4-en-3-one), and steroid hormones (testosterone,
  cortisol, cortisone, progesterone, androstenedione, aldosterone, corticosterone).
  UniProt lists many Rhea catalytic-activity reactions all EC 1.3.1.3.

## Biological process
- Bile acid biosynthesis (GO:0006699): reduces the CYP7A1/CYP8B1 products
  7alpha-hydroxy-4-cholesten-3-one and 7alpha,12alpha-dihydroxy-4-cholesten-3-one to the
  5beta-cholestan-3-one intermediates, giving bile acids their 5beta (cis) A/B ring.
  [PMID:7508385 "high activity toward the bile acid intermediates 7 alpha,12 alpha-dihydroxy-4-cholesten-3-one and 7 alpha-hydroxy-4-cholesten-3-one"; "more important for bile acid biosynthesis than for metabolism of steroid hormones"]
  Reactome models 6 5beta-reduction steps in bile acid synthesis (R-HSA-192033, -192067,
  -193746, -193755, -193821, -193824) plus 3 pathway-level nodes (R-HSA-193368, -193775,
  -193807).
- Steroid hormone metabolism (androgen/C21 steroid) — secondary; the human enzyme has a
  narrower steroid-hormone activity than rat [PMID:7508385 "substrate specificity of the
  human enzyme is considerably narrower than that of the rat enzyme"].

## Disease
- Congenital bile acid synthesis defect type 2 (CBAS2, MIM:235555; AKR1D1 deficiency):
  neonatal jaundice, intrahepatic cholestasis, hepatic failure; low chenodeoxycholic and
  cholic acid. [file:human/AKR1D1/AKR1D1-uniprot.txt "A condition characterized by jaundice, intrahepatic cholestasis and"]

## Annotation decisions summary
- KEEP AS CORE: GO:0047787 (Delta4-3-oxosteroid 5beta-reductase activity, the specific MF);
  GO:0006699 bile acid biosynthetic process (IDA PMID:7508385, Reactome TAS, InterPro IEA);
  GO:0005829 cytosol (IDA HPA, IDA PMID:7508385, Reactome TAS); GO:0016229 steroid
  dehydrogenase activity (IBA — reasonable parent, but keep specific MF as core).
- MODIFY: GO:0004032 aldose reductase (NADPH) activity (family-level IBA) → replace with
  GO:0047787. GO:0016491 oxidoreductase (too general) → GO:0047787.
- MARK_AS_OVER_ANNOTATED: GO:0047086 ketosteroid monooxygenase (IBA family term; AKR1D1 is
  a reductase not a monooxygenase); GO:0008106 alcohol dehydrogenase (NADP+) (Reactome/ARBA
  mechanistic label for the reduction reactions — the reaction reduces a C=C double bond,
  not an alcohol/aldehyde; less informative than 5beta-reductase); GO:0072582
  17beta-HSD(NADP+); GO:0005515 protein binding (2 IPI, BioPlex AP-MS, AKR1C1) — bare,
  uninformative; GO:0008202 steroid metabolic / GO:0042445 hormone metabolic /
  GO:0032787 monocarboxylic acid metabolic (ARBA broad BP); GO:0008207 C21-steroid,
  GO:0008209 androgen metabolic (human enzyme steroid-hormone activity minor vs bile acids);
  GO:0006707 cholesterol catabolic (bile acid synthesis is downstream of cholesterol but
  AKR1D1 does not act on cholesterol itself); GO:0007586 digestion (too indirect/downstream).
- KEEP_AS_NON_CORE: GO:0005737 cytoplasm (broader CC, redundant with cytosol; keep).

## Provenance
- No falcon deep-research file (provider out of credits). Grounded in
  AKR1D1-uniprot.txt, AKR1D1-goa.tsv, cached PMID_7508385 (abstract only),
  PMID_28514442/PMID_33961781 (BioPlex AP-MS), and cached Reactome R-HSA-* nodes.
</content>
</invoke>
