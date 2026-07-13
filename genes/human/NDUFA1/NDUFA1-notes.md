# NDUFA1 (MWFE) — gene review notes

## Identity and overview

- UniProt: O15239 (NDUA1_HUMAN); gene symbol **NDUFA1**; HGNC:7683.
- Aliases: **MWFE** protein / Complex I-MWFE / CI-MWFE / NADH-ubiquinone oxidoreductase MWFE subunit.
- Small protein, **70 amino acids**, single-pass membrane protein.
  [file:human/NDUFA1/NDUFA1-uniprot.txt "SEQUENCE   70 AA"], [file:human/NDUFA1/NDUFA1-uniprot.txt "Single-pass membrane protein"]
- Encoded on the **X chromosome** (nuclear-encoded, imported into mitochondria).
  [PMID:10200266 "The NDUFA1 gene encoding the MWFE polypeptide is located on the X chromosome."]
- Belongs to the "complex I NDUFA1 subunit family".
  [file:human/NDUFA1/NDUFA1-uniprot.txt "Belongs to the complex I NDUFA1 subunit family"]

## Molecular function — accessory/structural, NOT catalytic

NDUFA1 is one of the **accessory ("supernumerary") subunits** of mitochondrial Complex I
(NADH:ubiquinone oxidoreductase). It is a genuine, stable subunit of the mature holoenzyme,
not an assembly factor. It is **not one of the 14 conserved core subunits** and is
**believed not to be involved in catalysis** (carries no redox cofactor).

- [file:human/NDUFA1/NDUFA1-uniprot.txt "Accessory subunit of the mitochondrial membrane respiratory"] ... [file:human/NDUFA1/NDUFA1-uniprot.txt "chain NADH dehydrogenase (Complex I), that is believed not to be"] ... [file:human/NDUFA1/NDUFA1-uniprot.txt "involved in catalysis."]
- [PMID:10200266 "This polypeptide is 1 of approximately 28 \"accessory proteins\" identified in complex I"]
- [PMID:10200266 "it is not one of the 14 polypeptides making up the core complex I; a homologous set of 14 polypeptides can make a fully functional proton-translocating NADH-quinone oxidoreductase in prokaryotes."]

Its honest molecular function is therefore **structural molecule activity (GO:0005198)**; it
**contributes_to** the complex-level **NADH dehydrogenase (ubiquinone) activity (GO:0008137)**
but does not enable that activity independently. It should NOT be given GO:0008137 as a direct
`enables`/molecular_function.

## Essential for Complex I assembly and activity

Although non-catalytic, MWFE/NDUFA1 is **absolutely essential** for a functional Complex I:

- A Chinese hamster MWFE mutant (CCL16-B2, deletion producing a truncated protein) has
  Complex I activity reduced to <10%; complementation with hamster NDUFA1 cDNA restored
  rotenone-sensitive Complex I activity to ~100% of parent.
  [PMID:10200266 "In these mutant cells, complex I activity is reduced severely (<10%)."],
  [PMID:10200266 "Complementation with hamster NDUFA1 cDNA restored the rotenone-sensitive complex I activity of these mutant cells to approximately 100% of the parent cell activity."],
  [PMID:10200266 "the MWFE polypeptide is absolutely essential for an active complex I in mammals."]
- Systematic human knockout study of accessory subunits: 25 of 31 accessory subunits are
  strictly required for assembly of a functional Complex I; loss of a subunit destabilizes
  others in the same structural module.
  [PMID:27626371 "We show that 25 subunits are strictly required for assembly of a functional complex"],
  [PMID:27626371 "loss of each subunit affects the stability of other subunits residing in the same structural module."]

## Localization

- Mitochondrion **inner membrane**, matrix side (UniProt subcellular location).
  [file:human/NDUFA1/NDUFA1-uniprot.txt "Mitochondrion inner membrane"]
- Confirmed as a subunit of the inner-membrane Complex I holoenzyme by immunopurification /
  MS (Murray 2003) and by cryo-EM structures.
  [PMID:12611891 "we can resolve and identify the human homologues of 42 polypeptides detected so far in the more extensively studied beef heart complex I."]
- High-confidence mitochondrial proteomics (HTP) also places it in mitochondrion
  (Morgenstern 2021, PMID:34800366).

## Membership in Complex I / respiratory chain

- Complex I = **NADH:ubiquinone oxidoreductase**, first enzyme of the respiratory chain,
  ~45 subunits in humans.
  [PMID:27626371 "Complex I (NADH:ubiquinone oxidoreductase) is the first enzyme of the mitochondrial respiratory chain and is composed of 45 subunits in humans"]
- Function of the complex: transfer of electrons from NADH to ubiquinone, coupled to proton
  translocation across the inner membrane.
  [PMID:9878551 "Its main function is the transport of electrons from NADH to ubiquinone, which is accompanied by translocation of protons from the mitochondrial matrix to the intermembrane space."]
- NDUFA1 is assigned within human CI in the cryo-EM megacomplex structure (Guo 2017,
  PMID:28844695), which "reveals the precise assignment of individual subunits of human CI".
  [PMID:28844695 "reveals the precise assignment of individual subunits of human CI and CIII"]
- Complex I participates in respiratory supercomplexes (respirasomes) with CIII and CIV
  (PMID:28844695, PMID:30030361), which underlie the aerobic respiration / proton-motive-force
  and ATP-synthesis roles attributed at the complex level (ComplexPortal NAS annotations,
  PMID:30030361).

## Core biological process

- **GO:0006120** mitochondrial electron transport, NADH to ubiquinone (core).
- **GO:0032981** mitochondrial respiratory chain complex I assembly (NDUFA1 is required for
  assembly; PMID:27626371, PMID:10200266) — reasonable additional core BP.
- Aerobic respiration (GO:0009060) and proton-motive-force ATP synthesis (GO:0042776) are
  complex/pathway-level processes annotated by ComplexPortal (NAS); reasonable to keep as
  non-core context.

## Disease

- X-linked; mutations cause **Mitochondrial complex I deficiency, nuclear type 12 (MC1DN12,
  MIM:301020)**, a mitochondrial encephalomyopathy. Pathogenic missense variants G8R and R37S.
  [file:human/NDUFA1/NDUFA1-uniprot.txt "Mitochondrial complex I deficiency, nuclear type 12 (MC1DN12)"],
  [file:human/NDUFA1/NDUFA1-uniprot.txt "VARIANTS MC1DN12 ARG-8 AND SER-37."]

## Annotation review reasoning summary

- **respiratory chain complex I (GO:0045271, part_of)** — multiple independent IDA/IPI plus IBA
  → ACCEPT as core CC. It is a bona fide holoenzyme subunit.
- **structural molecule activity (GO:0005198)** — best MF; not present in GOA but is the honest
  MF; put in core_functions.
- **NADH dehydrogenase (ubiquinone) activity (GO:0008137), enables (NAS PMID:9878551; TAS
  PMID:10200266)** — this is the *complex-level* catalytic activity. NDUFA1 does NOT enable it
  independently (non-catalytic accessory subunit). Direct `enables` is an over-annotation →
  MARK_AS_OVER_ANNOTATED; captured instead as `contributes_to_molecular_function` in core_functions.
- **mitochondrial inner membrane (GO:0005743) / mitochondrion (GO:0005739) / mitochondrial
  membrane (GO:0031966)** — correct localization, accept (inner membrane most specific/core).
- **mitochondrion IDA PMID:16729965** — that paper is about OCTN1 localization; the NDUFA1 IDA
  is a plausible curator/MGI co-annotation of an endogenous mitochondrial marker. Location is
  correct but generic and the cited paper is not about NDUFA1 function → KEEP_AS_NON_CORE.
- **aerobic respiration (GO:0009060) / proton-motive-force ATP synthesis (GO:0042776)** —
  complex/pathway-level BPs (ComplexPortal NAS) → KEEP_AS_NON_CORE.
- **proton transmembrane transport (GO:1902600, IEA GO_REF:0000108)** — inter-ontology inference
  from GO:0008137. Since NDUFA1 does not itself have GO:0008137 activity and is non-catalytic
  (does not itself translocate protons), this inferred transport annotation is an
  over-propagation → MARK_AS_OVER_ANNOTATED (electronic, but keep per policy for a term whose
  essence — the complex pumps protons — is not entirely wrong).
- Reactome TAS inner-membrane localization annotations → ACCEPT (correct CC, TAS).
