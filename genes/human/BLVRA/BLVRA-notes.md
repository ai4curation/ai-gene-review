# BLVRA (Biliverdin reductase A) — review notes

UniProt: P53004 (BIEA_HUMAN). Gene: BLVRA (HGNC:1062). Taxon: Homo sapiens (NCBITaxon:9606).
EC 1.3.1.24. 296 aa; a Precursor (propeptide 1..2 removed, mature chain 3..296).

## Canonical function (primary): biliverdin reductase A

BLVRA catalyzes the **second step of heme catabolism**: reduction of the gamma-methene
bridge of biliverdin IXalpha to bilirubin IXalpha, with concomitant oxidation of NADH or
NADPH. It follows heme oxygenase (HMOX1/HMOX2), which opens the heme ring to biliverdin.

- "Reduces the gamma-methene bridge of the open tetrapyrrole, biliverdin IXalpha, to
  bilirubin with the concomitant oxidation of a NADH or NADPH cofactor"
  [file:human/BLVRA/BLVRA-uniprot.txt FUNCTION, ECO:0000269 PubMed:10858451/7929092/8424666/8631357].
- EC=1.3.1.24; Rhea RHEA:15797 (NAD+) and RHEA:15793 (NADP+); PhysiologicalDirection
  right-to-left (i.e. biliverdin -> bilirubin) [file:human/BLVRA/BLVRA-uniprot.txt CATALYTIC ACTIVITY].
- PATHWAY: "Porphyrin-containing compound metabolism; protoheme degradation"
  [file:human/BLVRA/BLVRA-uniprot.txt PATHWAY].
- Reactome R-HSA-189384 "BLVRA:Zn2+, BLVRB reduce BV to BIL": "BIL is formed from the
  reduction of biliverdin (BV) by bilverdin reductases BLVRA and BLVRB"
  [reactome:R-HSA-189384].

### Dual cofactor / dual pH — unusual property
- "BVR is unique among enzymes characterized to date in that it has dual pH/cofactor
  (NADH, NADPH) specificity" [PMID:8631357 abstract].
- "At pH 6.0-7.0 the NADH was the more effective cofactor, whereas at pH 8.5-8.75 NADPH
  was the preferred cofactor" [PMID:8424666 abstract].
- "It was assumed that NADPH rather than NADH was the physiological electron donor in the
  intracellular reduction of biliverdin" [PMID:7929092 abstract]; UniProt: "NADPH,
  however, is the probable reactant in biological systems (PubMed:7929092)".
- KM: 3.2 uM for NADPH, 50 uM for NADH [file:human/BLVRA/BLVRA-uniprot.txt BIOPHYSICOCHEMICAL PROPERTIES].
- Alpha-isomer specific: "as previously discussed for the rat and ox enzymes, it appears
  that at least one 'bridging propionate' is necessary for optimal binding and catalytic
  activity, whereas two are preferred" (BVR-A prefers IXalpha; BLVRB handles IXbeta)
  [PMID:10858451 abstract]. "Does not reduce bilirubin IXbeta (PubMed:10858451)"
  [file:human/BLVRA/BLVRA-uniprot.txt FUNCTION].

### Zinc metalloprotein
- "Atomic absorption spectroscopy indicates that the protein purified from human liver
  contains Zn at an approximately 1:1 molar ratio" [PMID:8631357 abstract]; UniProt
  COFACTOR "Binds 1 zinc ion per subunit" (Note is ECO:0000305, an inference)
  [file:human/BLVRA/BLVRA-uniprot.txt COFACTOR]. FT BINDING residues 280/281/292/293 for Zn2+
  are annotated with ECO:0000303 (from-statement in the paper), i.e. not a hard structural
  determination. The physiological necessity of Zn is debated (the 2H63 crystal structure
  is with NADP, monomer; no Zn in the FUNCTION statement). Treat zinc binding as
  KEEP_AS_NON_CORE / accept-as-cofactor rather than a core catalytic MF.

### Localization
- Cytosol: "Conversion of biliverdin to bilirubin is catalyzed by the cytosolic enzyme
  biliverdin reductase" [PMID:8424666 abstract]; enzyme isolated from "human liver
  cytosolic fractions" [PMID:7929092 abstract]. UniProt SUBCELLULAR LOCATION "Cytoplasm,
  cytosol" [file:human/BLVRA/BLVRA-uniprot.txt].
- Tissue: Liver [file:human/BLVRA/BLVRA-uniprot.txt TISSUE SPECIFICITY]; HPA "Low tissue
  specificity" (broadly expressed).
- Extracellular exosome (HDA) from two large-scale exosome proteomics datasets
  (PMID:19056867 urinary exosomes; PMID:20458337 B-cell exosomes). These are
  high-throughput MS detections; the protein is a soluble cytosolic enzyme that is a
  common exosome cargo — KEEP_AS_NON_CORE (not a functional location).

## Moonlighting function (genuine second role): kinase / MAPK scaffold

Human BVR-A is a well-documented dual-specificity Ser/Thr/Tyr kinase and signaling
scaffold in insulin/IGF1/MAPK/PI3K and PKC pathways, and a transcriptional regulator
(leucine-zipper) for HMOX1.

- "Human biliverdin reductase (hBVR) is a recently described Ser/Thr/Tyr kinase in the
  MAPK insulin/insulin-like growth factor 1 (IGF1)-signaling cascade" [PMID:18463290
  abstract]. It forms a ternary MEK/ERK/hBVR complex, activates MEK1 and ERK1/2, is an
  ERK nuclear transporter required for Elk1 transcriptional activity, and "in the complex,
  hBVR functions as a scaffold" [PMID:18463290 full text, PMC2383961].
- Also documented (in this paper's discussion) as an activator of PKCbetaII and PKCzeta
  through protein-protein interaction [PMID:18463290].

This role is not present in the curated GOA TSV (BLVRA-goa.tsv). It appears only as
electronic IEA:Ensembl projections in the UniProt DR GO section
(GO:0004674 protein serine/threonine kinase activity; GO:0000978 RNA Pol II CRM
sequence-specific DNA binding; GO:0005634 nucleus; GO:0009986 cell surface). Because it
is a genuine, experimentally described function of the human protein, it is captured as a
**second core function** (protein serine/threonine kinase activity, GO:0004674), grounded
in PMID:18463290, rather than being ignored. NB the kinase/scaffold role has been assayed
almost entirely by one group (Maines lab); flag as an expert question.

## Protein interactions (IPI, GO:0005515) — bare "protein binding"
GOA has four IPI "protein binding" annotations. Per policy these are not removed (they are
experimental IPI); marked MARK_AS_OVER_ANNOTATED because bare protein binding is
uninformative. The with/from partners:
- PMID:18463290 -> UniProtKB:P28482 (MAPK1/ERK2) — meaningful (the ERK-scaffold role);
  UniProt INTERACTION lists P53004–P28482 MAPK1.
- PMID:25416956 / PMID:29892012 / PMID:31515488 -> UniProtKB:Q8TBB1 (LNX1) — large-scale
  Y2H/interactome maps; UniProt INTERACTION lists P53004–Q8TBB1 LNX1 (NbExp=5).
  These interactome papers do not discuss BLVRA specifically in the cached text; they are
  high-throughput screens. Kept as over-annotated bare protein binding.

## Disease
- Hyperbiliverdinemia (HBLVD, MIM:614156) / "green jaundice": "It is due to increased
  biliverdin resulting from inefficient conversion to bilirubin. Affected individuals
  appear to have symptoms only in the context of obstructive cholestasis and/or liver
  failure" [file:human/BLVRA/BLVRA-uniprot.txt DISEASE, ECO:0000269 PubMed:19580635].

## Family
- Gfo/Idh/MocA family, Biliverdin reductase subfamily; NAD(P)-binding Rossmann-fold + C-terminal
  cat domain [file:human/BLVRA/BLVRA-uniprot.txt SIMILARITY]. PANTHER PTHR43377 BILIVERDIN REDUCTASE A.

## Annotation-review summary
- Core MF: GO:0004074 biliverdin reductase [NAD(P)H] activity (ACCEPT experimental IDA;
  the NADH- and NADPH-specific children GO:0106276/GO:0106277 are also experimentally
  supported and ACCEPTed as they capture the dual-cofactor specificity).
- Core BP: GO:0042167 heme catabolic process (ACCEPT IDA).
- Second core MF (moonlighting): GO:0004674 protein serine/threonine kinase activity
  (from PMID:18463290; not in GOA, added as core_function).
- Cytosol IDA (GO:0005829) ACCEPT; cytoplasm IEA / cytosol IEA/TAS ACCEPT or non-core.
- nucleotide binding (GO:0000166), zinc ion binding (GO:0008270): IEA cofactor/ligand-binding,
  KEEP_AS_NON_CORE (real but sub-functional / part of the catalytic mechanism).
- extracellular exosome (GO:0070062, HDA x2): KEEP_AS_NON_CORE (HTP cargo, not functional site).
- protein binding IPI x4 (GO:0005515): MARK_AS_OVER_ANNOTATED (bare protein binding).
- IEA biliverdin reductase duplicates (IBA/IEA of GO:0004074, GO:0106276, GO:0106277):
  ACCEPT / KEEP as they agree with the experimental evidence.
