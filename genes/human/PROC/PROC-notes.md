# PROC (human, UniProt P04070) review notes

## 2026-11-26 session: de novo review (RGD_PATHWAY_ONTOLOGY blood set, coagulation_cascade module)

### Deep research status

- `just deep-research human PROC --provider asta` ran (5.6 s) but returned 20 papers that are
  all unrelated to protein C (generic bioinformatics resources, network pharmacology, a seal
  influenza study, a cucurbit database). The template query was swamped by the identity-check
  boilerplate. Nothing in the output was usable, so the file was not kept. These notes are the
  literature record for this review instead.

### PubMed queries run (via the PubMed MCP, 2026-11-26)

1. `Stearns-Kurosawa endothelial cell protein C receptor augments protein C activation` -> PMID:8816778
2. `Kalafatis activated protein C factor Va inactivation Arg506 Arg306 cleavage` -> PMID:7989361, PMID:8043858, PMID:9300501
3. `activated protein C cytoprotective signaling EPCR PAR1 review Mosnier Griffin` -> PMID:25230930 (review, not cached)
4. `Fay activated protein C-catalyzed inactivation of human factor VIII and factor VIIIa` -> PMID:1939075
5. `Mosnier activated protein C biased signaling PAR1 Arg46 noncanonical cleavage` -> PMID:23149848

Newly cached (abstract only): PMID:8816778, PMID:7989361, PMID:1939075, PMID:23149848, PMID:8043858.
All GOA-cited papers except PMID:32296183 are abstract-only in the cache.

### Identity and structure

- Vitamin K-dependent plasma glycoprotein made in liver; signal peptide 1-18, propeptide 19-42,
  light chain 43-197 (Gla domain 43-88, two EGF-like domains), heavy chain 200-461 with the
  activation peptide 200-211 and the trypsin-like protease domain 212-450 (catalytic triad
  H253, D299, S402) [file:human/PROC/PROC-uniprot.txt]. Belongs to peptidase S1.
- Secreted as a disulfide-linked two-chain zymogen; ComplexPortal models the active enzyme as
  CPX-6224 "Active Protein C complex" (light + heavy chain).

### Activation

- Thrombin bound to thrombomodulin cleaves the activation peptide on the endothelial surface;
  EPCR binding of the protein C Gla domain lowers the apparent Km.
  [PMID:8816778 "These data indicate that the protein C activation complex involves protein C, thrombin, thrombomodulin, and EPCR."]
  [PMID:15005336 "Activation of protein C is achieved on the surface of endothelial cells by thrombin bound to the membrane protein thrombomodulin."]
- Glycosylation at Asn313 slows activation; T315A removes the sequon and raises the Vmax of
  activation by thrombin-TM four- to fivefold [PMID:25651845 "its elimination significantly (∼four- to fivefold) improves the maximum velocity of PC activation by the thrombin-TM complex"].
- Na+ and Ca2+ sites in the protease domain raise catalytic efficiency ~110-fold
  [PMID:12029084 "Sodium-occupied APC has approximately 100-fold increased catalytic efficiency"].

### Anticoagulant activity (core)

- APC inactivates membrane-bound FVa by cleaving the heavy chain at Arg506 then Arg306 (Arg679 minor)
  [PMID:7989361 "Our data demonstrate that inactivation of human factor V and human factor Va only occurs in the presence of a membrane surface after cleavage at Arg306."].
- Membrane binding through the Gla domain is required for the Arg306 cleavage
  [PMID:8043858 "impairs membrane binding of human APC, which in turn is required for cleavage of factor Va at Arg306 and inactivation of the cofactor"].
- APC inactivates FVIIIa by cleaving Arg336 and Arg562
  [PMID:1939075 "Human factor VIII and factor VIIIa were proteolytically inactivated by activated protein C."].
- Protein S (and FV) are cofactors [PMID:15005336 "Vitamin K-dependent protein S stimulates the APC-mediated regulation of coagulation."].
- Deficiency causes venous thrombosis (THPH3/THPH4) and neonatal purpura fulminans [PMID:25618265].

### Cytoprotective signalling

- EPCR-bound APC cleaves PAR1 on endothelial cells
  [PMID:12052963 "Activated PC (APC) was shown to use the endothelial cell PC receptor (EPCR) as a coreceptor for cleavage of protease activated receptor 1 (PAR1) on endothelial cells."].
- APC cleaves PAR1 at Arg46 (non-canonical) as well as Arg41; the Arg46-generated tethered ligand
  (TR47) drives beta-arrestin-2 biased cytoprotective signalling (Akt, Rac1, barrier stabilisation)
  [PMID:23149848 "Biochemical studies of APC's protease specificity showed that APC cleaved PAR1 sequences at both Arg41 and Arg46."].
- Downstream effects: anti-apoptotic (p53 inhibition in brain endothelium, EPCR and PAR1 dependent)
  [PMID:12563316], anti-inflammatory and endothelial barrier protection [PMID:25651845; UniProt FUNCTION].
  These are consequences of the PAR1 signalling, kept non-core in the review.

### Localization

- Plasma (secreted). ER and Golgi rows come from overexpression of wild-type and mutant PC in
  HEK293T/COS-7 cells (PDI and GM130 co-staining; PMID:25748729, PMID:22531345). This is a
  biosynthetic transit pool with direct evidence on the gene product: root ER and Golgi rows
  KEEP_AS_NON_CORE (ORGANELLES.md rule 7). ER-lumen and Golgi-lumen rows (ARBA, Reactome
  biosynthesis events) show transit only -> MARK_AS_OVER_ANNOTATED, matching PROS1.

### Interactions

- IntAct row PMID:15248212 is WITH UniProtKB:P51511 (MMP15), but the abstract describes MMP-2
  (gelatinase A, P08253) co-immunoprecipitating with APC. Possible partner mis-mapping; recorded
  as a SUSPECTED CHECK source defect (abstract-only; full text not read).

### Comparator check for the NEW cell surface receptor signaling row

- Positive control: QuickGO query of F2 (P00734) returns 57 MF/BP annotations, including
  GO:0007166 cell surface receptor signaling pathway (IDA) and GO:0070493 thrombin-activated
  receptor signaling pathway, so the query shape returns positives. Thrombin is the comparator in
  the same role (protease that cleaves PAR1 to generate the tethered ligand). PROC carries no
  signalling term at present (19 MF/BP rows). GO:0070493 is defined as initiated by thrombin, so
  the general GO:0007166 is used for APC.
- Participation test: APC itself performs the initiating step (cleavage of PAR1 at Arg46 that
  creates the tethered agonist), so it does work in the pathway rather than merely being required.

## 2026-11-26 coordinator follow-up
- Wrote the review YAML from these notes after the drafting session was interrupted.
- Changed one planned call: the root ER and Golgi rows (EXP, IDA and the UniProt-keyword IEA) rest
  on wild-type and mutant protein C overexpressed in HEK293T or COS-7 cells, with mutants retained;
  ORGANELLES rule 7 treats that as transit or retention of overexpressed protein, so they are
  MARK_AS_OVER_ANNOTATED rather than KEEP_AS_NON_CORE.
- Proteolysis rows are KEEP_AS_NON_CORE: APC is itself the protease, so the term is correct but general.
- `just validate human PROC`: valid; quote_check 71 verified.

## 2026-11-26 PR review follow-up
- Reverted the four direct ER and Golgi rows (EXP and IDA) to KEEP_AS_NON_CORE: rule 7 keeps a secretory protein's ER row non-core when there is direct evidence on the gene, and wild-type protein C was seen with PDI and GM130. The UniProt-keyword IEA rows and the lumen rows stay MARK_AS_OVER_ANNOTATED.
- Reworded the proteolysis reason: no narrower process term exists and the mechanism is peripheral, rather than "correct but general".
