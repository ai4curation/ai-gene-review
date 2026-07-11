# PGAP1 (Q75T13) review notes

Human PGAP1 = **GPI inositol-deacylase** (Post-GPI Attachment to Proteins factor 1; hPGAP1).
922 aa, multi-pass ER membrane protein (10 TM in the fungal ortholog structure), alpha/beta-hydrolase
(serine-hydrolase) fold; catalytic Ser predicted at ~residue 174 (ACT_SITE by similarity to Q765A7).

## Core biology (verified)

- PGAP1 removes the **acyl chain attached to the 2-OH of the inositol ring** of the GPI anchor
  **after** the GPI has been transferred en bloc to the protein by the transamidase — i.e. it acts in the
  **post-attachment remodeling** phase of GPI-anchored-protein (GPI-AP) biogenesis, in the ER.
  [PMID:24784135 "PGAP1 is a deacylase that removes an acyl-chain from the inositol of GPI anchors in the endoplasmic reticulum immediately after attachment of GPI to proteins"]
  [PMID:38167496 "Residing in the ER membrane, PGAP1 removes the inositol-linked acyl chain from nascent triacylated GPI-APs (dubbed GPI-AP3) to form the diacylated forms"]
- This is the acyl group that was added earlier (during GPI synthesis) by PIGW; PGAP1 initiates remodeling,
  MPPE1/PGAP5 then removes an EtN-P side chain, then Golgi remodeling by PGAP3/PGAP2.
  [PMID:24784135 "This remodeling starts in the ER by eliminating the acyl-chain linked to the inositol in the GPI-anchor by PGAP1"]
- Deacylation is **required for efficient ER-to-Golgi transport** of GPI-APs (binding of the remodeled anchor
  to p24-family cargo receptors that load GPI-APs into COPII vesicles).
  [PMID:38167496 "in mammalian cells, the deacylation by hPGAP1 is necessary for efficient ER export"]
  [PMID:38167496 "the deacylation is required for binding with p24-family cargo receptors"]
- Reactome models the exact reaction (uPAR-acyl-GPI + H2O -> uPAR + long-chain fatty acid) in the ER and
  links it to efficient ER->Golgi transport [Reactome:R-HSA-162729; R-HSA-162791].
- Catalysis: serine-hydrolase-type mechanism (structural/biochemical study of fungal ortholog).
  [PMID:38167496 "serine hydrolase-type catalysis"]

## Enzyme classification / MF term

- GOA/UniProt MF term is **GO:0160215 "deacylase activity"** (current label is the generic "deacylase activity";
  definition: "hydrolysis of an acyl group or groups from a substrate molecule"). There is no dedicated
  "GPI inositol-deacylase activity" GO term (checked go.db; the closest specific term
  GO:0050185 phosphatidylinositol deacylase activity is a different substrate). So GO:0160215 is the correct,
  currently-available MF term and is used both in existing_annotations and core_functions.
- InterPro/Reactome also give the parent GO:0016788 "hydrolase activity, acting on ester bonds" — correct but
  less specific than GO:0160215; kept (ACCEPT) as a valid broader IEA/TAS.
- EC=3.1.-.- (carboxylic-ester hydrolase) per UniProt; RHEA:83663/83787 catalytic reactions.

## Localization

- ER / ER membrane; multi-pass membrane protein. GO:0005789 (ER membrane) supported by SubCell (IEA),
  ISS (from mouse Q765A7), and Reactome (TAS). GO:0005783 (ER) IBA also fine.
  [UniProt "SUBCELLULAR LOCATION: Endoplasmic reticulum membrane ... Multi-pass membrane protein"]

## Disease

- Biallelic loss-of-function causes an inherited GPI-deficiency / GPI-anchor biosynthesis defect (GPIBD):
  neurodevelopmental disorder with dysmorphic features, spasticity, and brain abnormalities (NEDDSBA,
  MIM:615802) — global developmental delay, impaired intellectual development, hypotonia/spasticity,
  epilepsy, brain atrophy. Distinctively, in PGAP1 deficiency the *surface levels* of GPI-APs are normal but
  the anchor *fine structure* is abnormal (PI-PLC-resistant), because remodeling — not attachment — is lost.
  [PMID:24784135 "null mutations in PGAP1 lead to severe intellectual disability and encephalopathy"]
  [PMID:24482476 links PGAP1 to corticospinal motor neuron disease / NEDDSBA]

## Curation decisions (GOA rows)

- GO:0160215 deacylase activity (IBA, 2x IDA) -> ACCEPT (core MF; the two IDAs = 24784135, 38167496).
- GO:0016788 hydrolase acting on ester bonds (IEA InterPro, TAS Reactome) -> ACCEPT (correct broader parent).
- GO:0005783 ER (IBA), GO:0005789 ER membrane (IEA SubCell, ISS, TAS) -> ACCEPT (localization).
- GO:1902953 positive regulation of ER to Golgi vesicle-mediated transport (ISS) -> KEEP_AS_NON_CORE
  (real, well-supported downstream consequence of deacylation, but a regulatory/phenotypic BP rather than
  the direct molecular role).
- GO:0016255 attachment of GPI anchor to protein (TAS Reactome) -> MARK_AS_OVER_ANNOTATED. PGAP1 does NOT
  catalyze transamidase attachment; it acts *after* attachment on the anchor. The Reactome pathway groups the
  deacylation reaction within the "Attachment of GPI anchor to uPAR" pathway, so the term is not wrong at the
  pathway level, but it over-states PGAP1's role. Better BP = GPI anchor biosynthetic/metabolic process
  (GO:0006506), which UniProt also carries as IBA. Added as core BP via core_functions.

## core_functions
- MF: GO:0160215 deacylase activity (GPI inositol-deacylase)
- BP: GO:0006506 GPI anchor biosynthetic process (post-attachment remodeling step)
- CC: GO:0005789 endoplasmic reticulum membrane
