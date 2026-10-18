# CLYBL (Q8N0X4) — curation journal

Human CLYBL, "citrate lyase beta-like protein". Nuclear-encoded, mitochondrial matrix,
homotrimeric Mg2+-dependent enzyme of the HpcH/HpaI aldolase family (citrate lyase beta
subunit-like subfamily). Humans lack the other citrate-lyase subunits, so CLYBL is not part
of an ATP-independent citrate lyase (UniProt CAUTION on Q8N0X4).

Ubiquitously expressed:
[PMID:24334609 "The protein is expressed in the mitochondria of all mammalian organs, with highest expression in brown fat and kidney."]

A common premature-stop polymorphism (rs41281112, p.Arg259*) ablates the protein in a few
percent of people and is the gene's only consistent human phenotype — reduced circulating
vitamin B12:
[PMID:24334609 "Approximately 5% of all humans harbor a premature stop polymorphism in CLYBL that has been associated with reduced levels of circulating vitamin B12."]
(UniProt gives the carrier frequency of the null protein as 2.7%.)

---

## Successive function assignments

### 1. Malate / beta-methylmalate synthase (Strittmatter 2014)
[PMID:24334609 "We report that CLYBL encodes a malate/β-methylmalate synthase, converting glyoxylate and acetyl-CoA to malate, or glyoxylate and propionyl-CoA to β-methylmalate."]
This is the Claisen-condensation direction. Kinetics are poor: kcat 0.12 s-1, KM(glyoxylate)
3.6 mM (UniProt Q8N0X4 BIOPHYSICOCHEMICAL PROPERTIES, from this paper). A millimolar KM for
glyoxylate in a mitochondrion is not a physiological operating point.

### 2. (S)-Citramalyl-CoA lyase; the itaconate model (Shen 2017)
[PMID:29056341 "we report that CLYBL operates as a citramalyl-CoA lyase in mammalian cells"]
[PMID:29056341 "Cells lacking CLYBL accumulate citramalyl-CoA, an intermediate in the C5-dicarboxylate metabolic pathway that includes itaconate"]
[PMID:29056341 "We report that CLYBL loss leads to a cell-autonomous defect in the mitochondrial B12 metabolism and that itaconyl-CoA is a cofactor-inactivating, substrate-analog inhibitor of the mitochondrial B12-dependent methylmalonyl-CoA mutase (MUT)."]
[PMID:29056341 "Our work reveals an unanticipated consequence of exposure to itaconate: B12 inactivation"]

This paper already settles the malate-synthase question against the 2014 assignment:
[PMID:29056341 "The specificity constant (kcat/KM) for the citramalyl-CoA lyase activity is >1000 fold higher than the forward malate/methylmalate/citramalate synthase activity"]

and it already saw the thioesterase that would later be named the physiological reaction:
[PMID:29056341 "We also found that CLYBL has a thioesterase activity and hydrolyzes malyl-CoA to malate and free CoASH, but we did not quantify this activity in detail."]

### 3. Malyl-CoA metabolite repair (Griffith 2025)
[PMID:40108300 "The discrepancy between the highly inducible and locally confined production of itaconate and the broad expression profile of CLYBL across tissues suggested a role for this enzyme beyond itaconate catabolism."]
[PMID:40108300 "Here we discover that CLYBL additionally functions as a metabolite repair enzyme for malyl-CoA, a side product of promiscuous citric acid cycle enzymes."]
[PMID:40108300 "We found that CLYBL knockout cells, accumulating malyl-CoA but not itaconyl-CoA, show decreased levels of adenosylcobalamin and that malyl-CoA is a more potent inhibitor of methylmalonyl-CoA mutase than itaconyl-CoA."]
[PMID:40108300 "Our work thus suggests that malyl-CoA plays a role in the B12 deficiency observed in individuals with CLYBL loss of function."]

Reaction (UniProt CATALYTIC ACTIVITY, RHEA:38291, EC 3.1.2.30):
`(S)-malyl-CoA + H2O = (S)-malate + CoA + H+`, PhysiologicalDirection left-to-right.
Kinetics from Griffith 2025 via UniProt: KM 11 uM, kcat 9.4 s-1, Vmax 15.1 umol/min/mg —
comparable to the citramalyl-CoA lyase reaction (KM 22 uM, kcat 1.6 s-1 in the same paper)
and ~100x better than malate synthase.

---

## The argument, and where the B12 variant fits

The itaconate/citramalyl-CoA model and the malyl-CoA model are not mutually exclusive
chemistry — both are Mg2+-dependent reactions on a C4/C5 acyl-CoA at the same active site,
and both converge on protecting MMUT's adenosylcobalamin. They differ on which one explains
the human phenotype.

The decisive observation is **where the two substrates come from**. Itaconate is made by
ACOD1/IRG1 in activated macrophages — inducible and spatially restricted. Malyl-CoA arises
continuously as a side product of promiscuous TCA-cycle enzymes in every cell. CLYBL is
expressed in every tissue, and the rs41281112 null allele lowers circulating B12 in
unselected, non-inflamed populations. A B12 phenotype that tracks the genotype rather than
inflammatory state fits the constitutive malyl-CoA source, not the inducible itaconate one.
Griffith's KO cells make the point directly: they accumulate malyl-CoA *but not* itaconyl-CoA,
and still lose adenosylcobalamin.

So the B12 variant does bear on the question, and it argues for malyl-CoA repair as the
housekeeping physiological reaction, with citramalyl-CoA lyase as the same active site doing
real and important work in a specific inflammatory context.

## Position taken in this review

- **Core MF 1**: (S)-malyl-CoA thioesterase. No dedicated GO term exists; the closest is
  `GO:0016289 acyl-CoA hydrolase activity`, which GOA already carries as IDA from
  PMID:40108300 and as an IEA from the Rhea mapping. Accepted as core; a specific child term
  `(S)-malyl-CoA hydrolase activity` is proposed.
- **Core MF 2**: `GO:0047777 (S)-citramalyl-CoA lyase activity`. Accepted as core. Both
  activities serve the same biological process, `GO:0110052 toxic metabolite repair`.
- **`GO:0004474 malate synthase activity` → MODIFY.** The reaction is genuinely catalysed in
  vitro and the IDA annotations are correct as measurements; but the specificity constant is
  >1000-fold below the lyase reaction and the KM for glyoxylate is millimolar, so this is a
  promiscuous reverse activity of the lyase/thioesterase active site, not the enzyme's
  function. Replacement proposed: `GO:0016289 acyl-CoA hydrolase activity` /
  `GO:0047777`. Note also that human mitochondria have no glyoxylate shunt, so a malate
  synthase has no pathway to belong to.
- **`GO:0106121 positive regulation of cobalamin catabolic process` → MODIFY, direction
  appears inverted.** CLYBL *removes* the CoA esters that destroy adenosylcobalamin; loss of
  CLYBL is what increases B12 destruction and lowers circulating B12. The gene product
  therefore *reduces* cobalamin catabolism. `GO:0106122 negative regulation of cobalamin
  catabolic process` exists and currently has zero annotations in QuickGO, while GO:0106121
  is annotated essentially only to CLYBL and its orthologues — consistent with the term pair
  having been created for this gene and the wrong sign having been picked. Flagged for a GO
  curator rather than asserted as settled; recorded in `suggested_questions`.
- **`GO:0106064 regulation of cobalamin catabolic process` (IBA, IEA) → ACCEPT.** The parent
  is directionally neutral and therefore not wrong. Not modified, because the IBA was placed
  by a PAINT curator whose tree I have not inspected.
- `GO:0000287 magnesium ion binding` (two IDAs) — accepted, genuine catalytic cofactor.
- `GO:0070207 protein homotrimerization` — accepted as non-core (real, from the crystal
  structure, but an assembly property).

## Open questions
- Is GO:0106121 the intended direction? If yes, what is the reasoning?
- What is the source of mitochondrial malyl-CoA in vivo (which TCA enzyme, at what flux)?
- Does the rs41281112 null allele show any B12 phenotype modulation by inflammatory state,
  which would be the direct test of itaconate vs malyl-CoA as the dominant driver?
- Should EC 2.3.3.9 (malate synthase) be retained on the UniProt entry at all?

## 2026-10-18 ORGANELLES pilot: mitochondrial sub-compartment

Applied the ORGANELLES policy (projects/ORGANELLES.md, "Policy") to the three GO:0005739
mitochondrion rows. Lines of evidence for the matrix, all agreeing:

1. Targeting: UniProt annotates a mitochondrial transit peptide, residues 1-22 (ECO:0000255,
   predicted), with the mature chain at 23-340, and the entry has no TRANSMEM/INTRAMEM feature
   [file:human/CLYBL/CLYBL-uniprot.txt "FT   TRANSIT         1..22"]. Cleavable presequence plus
   no membrane anchor is the matrix signature.
2. Structure: the mature, MTS-less chain is a soluble Mg(2+)-bound homotrimer
   [PMID:29056341 "lacking the predicted mitochondrial targeting sequence (aa 23 – 340),"].
3. Literature statement (secondary, citing MitoCarta2.0/Calvo 2016)
   [PMID:29056341 "CLYBL is a ubiquitously expressed mitochondrial matrix soluble enzyme of"].
4. Function: substrates are matrix CoA esters - malyl-CoA from citric acid cycle side reactions
   [PMID:40108300 "a side product of promiscuous citric acid cycle enzymes"] and itaconate-derived
   citramalyl-CoA - and the protected B12 enzyme MUT is a matrix enzyme
   [PMID:29056341 "mitochondrial matrix enzyme that uses coenzyme B12 or"]; CLYBL loss causes a
   cell-autonomous defect in mitochondrial B12 metabolism [PMID:29056341].

Nothing argues for another sub-compartment (no TM segment, no IMS/outer-membrane report). No
direct sub-mitochondrial fractionation / protease-protection experiment was found (PubMed
search "CLYBL mitochondrial matrix" returned nothing), so the new row is IC, not IDA.

Changes: IEA GO_REF:0000044 mitochondrion ACCEPT -> MODIFY (to GO:0005759); IDA (PMID:24334609)
and HTP (PMID:34800366) mitochondrion rows left ACCEPT (organelle-level assays); NEW IC row
GO:0005759 mitochondrial matrix; core_functions locations mitochondrion -> mitochondrial matrix.
