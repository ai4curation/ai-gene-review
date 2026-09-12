# ACACB (Acetyl-CoA carboxylase 2 / ACC2 / ACC-beta) — review notes

UniProt: O00763 (ACACB_HUMAN), 2458 aa precursor. HGNC:85. Gene synonyms ACC2, ACCB.
Source of record: `genes/human/ACACB/ACACB-uniprot.txt` (authoritative). 55 GOA annotations reviewed.

## Core identity and catalytic function

ACACB is one of the two mammalian acetyl-CoA carboxylases (the other being ACACA/ACC1).
It is a biotin-dependent, multidomain ligase that catalyzes the first committed step of
fatty-acid metabolism: the ATP-dependent carboxylation of acetyl-CoA to malonyl-CoA.

- Reaction (EC 6.4.1.2): "Reaction=hydrogencarbonate + acetyl-CoA + ATP = malonyl-CoA +
  ADP + phosphate + H(+); ... EC=6.4.1.2" [file:human/ACACB/ACACB-uniprot.txt].
  Multiple EXP/IDA papers establish the activity for the human ACC2 protein directly:
  - PMID:16854592 "The resultant human ACC2, human ACC1, and rat ACC2 possess high
    specific activities, are properly biotinylated" — recombinant human ACC2 activity + biotinylation.
  - PMID:19236960 "the steady-state kinetic analysis of a purified recombinant human form
    of the enzyme, namely ACC2, using a novel LC/MS/MS assay to directly measure
    malonyl-CoA formation" — direct malonyl-CoA formation assay.
  - PMID:19900410 crystal structure of the BC domain of human ACC2 + AMPK phospho-regulation.
  - PMID:20457939 / PMID:20952656 — ACC polymerization/activity assays (MIG12/S14).
  - PMID:26976583 "prevent dimerization and inhibit the enzymatic activity of both ACC
    isozymes" — ND-630 inhibits ACC1 and ACC2 activity.
- Reaction proceeds in two half-reactions: biotin carboxylase (BC) domain ATP-dependently
  carboxylates the biotin on the biotin-carboxyl-carrier (BCC) domain; the carboxyl
  transferase (CT) domain transfers the carboxyl to acetyl-CoA [file:human/ACACB/ACACB-uniprot.txt,
  FUNCTION + DOMAIN].
- Cofactor biotin, covalently attached at Lys929 (N6-biotinyllysine)
  [file:human/ACACB/ACACB-uniprot.txt]; requires 2 Mg2+/Mn2+ per subunit.
- Domain architecture (UniProt FT): Biotin carboxylation 259..761; ATP-grasp 414..609;
  Biotinyl-binding 888..962; CoA carboxyltransferase 1695..2345.

Core MF terms: acetyl-CoA carboxylase activity (GO:0003989); biotin carboxylase activity
(GO:0004075, the BC half-reaction); biotin binding (GO:0009374, cofactor); ATP binding
(GO:0005524, ATP-grasp).

## Distinguishing feature: mitochondrial outer membrane localization → regulation of beta-oxidation

Unlike cytosolic ACC1/ACACA, ACC2 carries a unique hydrophobic N-terminal targeting sequence
that anchors it to the mitochondrial outer membrane, where the malonyl-CoA it produces
inhibits carnitine palmitoyltransferase 1 (CPT1) and thereby restrains mitochondrial
fatty-acid uptake and beta-oxidation.

- PMID:10677481 (IDA subcellular localization): "ACC1 is a cytosolic protein and that ACC2
  was associated with the mitochondria" ... "The association of ACC2 with the mitochondria
  is consistent with the hypothesis that ACC2 is involved in the regulation of mitochondrial
  fatty acid oxidation through the inhibition of carnitine palmitoyltransferase 1 by its
  product malonyl-CoA." Note: this paper reports mitochondrial association; the GOA IDA
  annotations from this paper include GO:0005739 (mitochondrion) and — surprisingly —
  GO:0005634 (nucleus). The abstract does not support a nuclear localization; the
  mitochondrial finding is the robust claim.
- UniProt SUBCELLULAR LOCATION: "Mitochondrion {ECO:0000269|PubMed:10677481}"
  [file:human/ACACB/ACACB-uniprot.txt]. Reactome and UniProt SubCell (SL-0173) place ACC2
  specifically at the mitochondrial outer membrane (GO:0005741).
- UniProt FUNCTION: "Through the production of malonyl-CoA that allosterically inhibits
  carnitine palmitoyltransferase 1 at the mitochondria, negatively regulates fatty acid
  oxidation (By similarity)." [file:human/ACACB/ACACB-uniprot.txt].

Core CC: mitochondrial outer membrane (GO:0005741). Core BP: malonyl-CoA biosynthetic
process (GO:2001295) / fatty acid biosynthetic process (GO:0006633, as the class-level
malonyl-CoA production shared with ACC1); and negative regulation of fatty acid
beta-oxidation (GO:0031999) as the physiological role distinguishing ACC2 from ACC1.

## Regulation and interactions

- Phosphorylation at Ser222 by AMPK inactivates the enzyme by disrupting polymerization:
  PMID:19900410 "The phosphorylated Ser222 binds to the putative dimer interface of BC,
  disrupting polymerization and providing the molecular mechanism of inactivation by AMPK."
  Also soraphen A binds the same site (competitive with the active filamentous form).
- Activity increased by oligomerization into filaments (PMID:19900410); inhibited by product
  malonyl-CoA; activated by citrate (PMID:16854592, PMID:19236960).
- MID1IP1/MIG12 (Q9CQ20) binds ACC and lowers the citrate threshold for polymerization,
  strongly activating the enzyme: PMID:20457939 "MIG12 ... binds to ACC and lowers the
  threshold for citrate activation into the physiological range". Basis of the IPI
  protein-binding and homotetramerization annotations.
- PMID:20952656 (Spot 14/S14 structure): "MIG12 modulates fatty acid synthesis by inducing
  the polymerization and activity of acetyl-CoA carboxylase"; provides ACC2 IDA activity,
  acetyl-CoA metabolic process, protein homotetramerization (GO:0051289), and IPI (self/MIG12).
- HLCS (holocarboxylase synthetase, P50747) biotinylates ACC2; the IPI (PMID:20085763) and
  Reactome R-HSA-4167511 capture this enzyme-substrate interaction. Abstract is general
  (hHCS biotinylates biotin acceptor proteins); ACACB is a known HCS substrate.
- TRB3/COP1 pathway (PMID:16794074) triggers ubiquitination/degradation of ACC during
  fasting; IPI with mouse Trib3 (Q8K4K2), assigned by BHF-UCL. Bare "protein binding".

## Physiological / disease context

- Highest expression in heart, skeletal muscle, liver, adipose tissue [file:human/ACACB/ACACB-uniprot.txt,
  TISSUE SPECIFICITY]; oxidative tissues where regulating beta-oxidation matters.
- Validated drug target: "Inhibition of ACACB may prevent lipid-induced insulin resistance
  and type 2 diabetes ... a potential pharmaceutical target for treatment of obesity and
  type 2 diabetes." [file:human/ACACB/ACACB-uniprot.txt, BIOTECHNOLOGY]. PMID:26976583
  (ND-630) demonstrates therapeutic benefit of dual ACC1/ACC2 inhibition in rats.

## Notes on over-annotations (Ensembl GO_REF:0000107 orthology transfers)

A large block of IEA annotations was electronically transferred from rat/mouse orthologs
(GO_REF:0000107). Several are non-specific or reflect downstream/systemic physiology of the
ortholog rather than ACC2's molecular activity, and should be treated as non-core or
over-annotations:
- Reasonable and consistent with ACC2 biology (keep as non-core): negative regulation of
  fatty acid beta-oxidation (GO:0031999), negative regulation of fatty acid oxidation
  (GO:0046322), fatty acid oxidation (GO:0019395 — regulatory, not that ACC2 performs
  oxidation), negative regulation of lipid catabolic process (GO:0050995), positive
  regulation of lipid storage (GO:0010884), regulation of glucose metabolic process
  (GO:0010906), energy homeostasis (GO:0097009), response to nutrient/response to nutrient
  levels, biotin binding (GO:0009374 — actually a genuine cofactor MF), positive regulation
  of heart growth (GO:0060421), regulation of cardiac muscle hypertrophy (GO:1903242).
- Weak/likely-spurious ortholog transfers from a rat isoform (A0A0G2K1F2) that pull in TCA /
  amino-acid / glucose-import / glycolysis physiology not attributable to ACC2's carboxylase
  function: pentose-phosphate shunt (GO:0006098), purine nucleotide metabolic process
  (GO:0006163), tricarboxylic acid metabolic process (GO:0072350), intracellular aspartate
  homeostasis (GO:0090459), intracellular glutamate homeostasis (GO:0090461), lactic acid
  secretion (GO:0046722), D-glucose import across plasma membrane (GO:0098708), part_of
  mitochondrial fatty acid beta-oxidation multienzyme complex (GO:0016507 — ACC2 is not a
  subunit of the beta-oxidation trifunctional/multienzyme complex), response to xenobiotic
  stimulus (GO:0009410). These are marked MARK_AS_OVER_ANNOTATED (kept, since IEA, but
  flagged) or REMOVE where clearly a wrong-CC / mis-transfer.

## Anomalies

- GO:0005634 (nucleus) IDA from PMID:10677481: abstract supports only mitochondrial/cytosolic
  localization, not nuclear. Experimental annotation → MARK_AS_OVER_ANNOTATED (do not REMOVE
  an IDA), with note that the cached abstract does not support nuclear localization.
- GO:0005829 (cytosol) TAS from Reactome (expression/transcription reactions): ACC2 is
  mito-outer-membrane, not a bona fide cytosolic pool; these TAS come from
  expression/ChREBP reactions. Keep as non-core.
</content>
</invoke>
