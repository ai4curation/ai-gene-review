# UROC1 (Urocanate hydratase / Urocanase) — Review Notes

UniProt: Q96N76 (HUTU_HUMAN). Gene: UROC1. HGNC:26444. EC 4.2.1.49.

## Identity and catalytic function

UROC1 encodes **urocanate hydratase (urocanase)**, the enzyme catalyzing the
**second step of L-histidine catabolism**. It hydrates trans-urocanate to
4-imidazolone-5-propanoate.

- RecName / EC from UniProt: [file:human/UROC1/UROC1-uniprot.txt "RecName: Full=Urocanate hydratase"], [file:human/UROC1/UROC1-uniprot.txt "Short=Urocanase"], [file:human/UROC1/UROC1-uniprot.txt "EC=4.2.1.49"].
- Catalytic reaction (UniProt CATALYTIC ACTIVITY): [file:human/UROC1/UROC1-uniprot.txt "Reaction=4-imidazolone-5-propanoate = trans-urocanate + H2O"]; Rhea:RHEA:13101, EC 4.2.1.49. Evidence ECO:0000269|PubMed:19304569.
- Note the direction: GO:0016153 "urocanate hydratase activity" is defined as
  "4-imidazolone-5-propanoate + H+ = trans-urocanate + H2O" (OLS/go), i.e. the
  same reaction written in the reverse direction; both refer to the interconversion
  of urocanate and 4-imidazolone-5-propanoate. In vivo the flux runs
  urocanate -> 4-imidazolone-5-propanoate (histidine degradation).

## Cofactor: tightly bound NAD+

Urocanase uses a **tightly (essentially covalently) bound NAD+** as an
**electrophilic cofactor**, not as a redox coenzyme — NAD+ adds to the urocanate
substrate to activate it for hydration, and is regenerated per catalytic cycle.
- UniProt COFACTOR: [file:human/UROC1/UROC1-uniprot.txt "Name=NAD(+); Xref=ChEBI:CHEBI:57540; Evidence={ECO:0000250}"].
- Multiple NAD(+) BINDING sites are annotated by similarity to bacterial urocanase
  P25503 (Pseudomonas): e.g. [file:human/UROC1/UROC1-uniprot.txt "BINDING         343..347"] and
  [file:human/UROC1/UROC1-uniprot.txt "BINDING         594"], all with ligand NAD(+) (ChEBI:CHEBI:57540).
- KW: [file:human/UROC1/UROC1-uniprot.txt "KW   Alternative splicing; Disease variant; Histidine metabolism; Lyase; NAD;"].
- Justifies proposing **GO:0051287 NAD binding** as a core molecular function
  (currently absent from GOA).

## Pathway / biological process

- UniProt PATHWAY: [file:human/UROC1/UROC1-uniprot.txt "Amino-acid degradation; L-histidine degradation into L-"] /
  "glutamate; N-formimidoyl-L-glutamate from L-histidine: step 2/3."
  (UniPathway UPA00379; UER00550).
- Histidine catabolism pathway (4 steps to glutamate): HAL (histidase) makes
  urocanate from histidine (step 1); UROC1 (step 2) hydrates urocanate to
  4-imidazolone-5-propanoate; then imidazolonepropionase (AMDHD1) and
  formiminotransferase (FTCD) complete degradation to glutamate.
- Reactome: [file:human/UROC1/UROC1-uniprot.txt "Reactome; R-HSA-70921; Histidine catabolism."]; the specific
  UROC1 reaction is R-HSA-70903 "urocanate + H2O => 4-imidazolone-5-propanoate".
- Reactome R-HSA-70903 summary: "Cytosolic urocanate hydratase (UROC1) catalyzes
  the hydrolysis of urocanate to form 4-imidazolone-5-propanoate."
  [reactome:R-HSA-70903].

## Localization

- Cytosolic. UniProt does not carry an explicit SUBCELLULAR LOCATION comment, but
  Reactome designates it "Cytosolic urocanate hydratase" [reactome:R-HSA-70903],
  and GOA has cytosol from both Reactome (TAS) and BHF-UCL (IDA, PMID:19304569).
- Expression is liver-enriched: [file:human/UROC1/UROC1-uniprot.txt "HPA; ENSG00000159650; Tissue enriched (liver)."],
  consistent with hepatic histidine catabolism.

## Disease: Urocanase deficiency (urocanic aciduria)

- UniProt DISEASE: [file:human/UROC1/UROC1-uniprot.txt "Urocanase deficiency (UROCD) [MIM:276880]: An inborn error of"]
  histidine metabolism resulting in urocanic aciduria and neurological
  manifestations (intellectual disability, ataxia, aggressive behavior).
  Evidence ECO:0000269|PubMed:19304569.
- First human mutations reported by Espinós et al. 2009 (PMID:19304569):
  "This report describes the first putative mutations, p.L70P and p.R450C, in the
  coding region of the UROC1 gene in a girl with urocanic aciduria presenting with
  mental retardation and intermittent ataxia." [PMID:19304569].
- Functional characterization in that paper: enzyme activity assays and protein
  expression studies showed neither variant produces a fully functional enzyme:
  "enzyme activity assays suggest that none of the mutations can produce a fully
  functional enzyme" [PMID:19304569]. The R450C variant is annotated in UniProt as
  "loss of activity" [file:human/UROC1/UROC1-uniprot.txt "R -> C (in UROCD; loss of activity;"].
- This IMP/IDA evidence directly supports UROC1's role in L-histidine catabolism
  (loss-of-function -> urocanic aciduria) and its urocanate hydratase activity.

## Protein family / structure

- SIMILARITY: [file:human/UROC1/UROC1-uniprot.txt "Belongs to the urocanase family."] (ECO:0000305).
- Domains: Pfam PF01175 Urocanase, PF17391 Urocanase_N, PF17392 Urocanase_C;
  PANTHER PTHR12216 UROCANATE HYDRATASE; HAMAP MF_00577 HutU; PROSITE PS01233
  UROCANASE. Single-copy, well-conserved enzyme family with a Rossmann-like fold
  binding NAD.

## Interactions / "protein binding" annotation

- GOA has a single GO:0005515 "protein binding" IPI (PMID:32296183) with_from
  UniProtKB:Q15699 (ALX1). This is the same interaction recorded in the UniProt
  INTERACTION block: [file:human/UROC1/UROC1-uniprot.txt "Q96N76; Q15699: ALX1; NbExp=3; IntAct=EBI-13073486, EBI-750671;"].
- PMID:32296183 (Luck et al. 2020, Nature) is the HuRI human binary interactome
  map — a high-throughput Y2H screen. It reports ~53,000 interactions systematically
  ("With approximately 53,000 protein-protein interactions" [PMID:32296183]). The
  UROC1-ALX1 pairing is a systematic-screen hit with no known biological meaning for
  a cytosolic metabolic enzyme paired with a homeodomain transcription factor; the
  bare "protein binding" term is uninformative. Keep but mark as over-annotated
  (do not remove an experimental IPI per policy).

## Summary of core functions

- MF: **GO:0016153 urocanate hydratase activity** (urocanase; EC 4.2.1.49), with
  **GO:0051287 NAD binding** (tightly bound NAD+ electrophilic cofactor).
- BP: **GO:0006548 L-histidine catabolic process** (step 2 of histidine degradation
  to glutamate).
- CC: **GO:0005829 cytosol**.

## Term-obsolescence note

The two UniProt DR IEA BP terms GO:0019556 ("L-histidine catabolic process to
glutamate and formamide") and GO:0019557 ("...to glutamate and formate") are now
**OBSOLETE** in GO (verified via OLS). They are not present in the seeded review /
goa.tsv and are superseded by GO:0006548; no action needed here.
