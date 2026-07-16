# GNPAT (O15228) — review notes

## Identity and function

GNPAT = glyceronephosphate O-acyltransferase, aka dihydroxyacetone phosphate
acyltransferase (DHAPAT / DAP-AT / DAPAT / DHAP-AT), EC 2.3.1.42. A 680-aa
peroxisomal enzyme.

- Catalyzes: **dihydroxyacetone phosphate (glycerone phosphate, DHAP) + acyl-CoA
  → 1-acylglycerone 3-phosphate (acyl-DHAP) + CoA** (EC 2.3.1.42). This is the
  **first committed step of ether-glycerolipid (plasmalogen) biosynthesis**.
  [file:human/GNPAT/GNPAT-uniprot.txt "Reaction=dihydroxyacetone phosphate + an acyl-CoA = a 1-acylglycerone"]
  [file:human/GNPAT/GNPAT-uniprot.txt "Dihydroxyacetonephosphate acyltransferase catalyzing the"]
- The acyl-DHAP product is then handed to AGPS (alkyl-DHAP synthase / alkylglycerone
  phosphate synthase), which replaces the acyl group with a fatty alcohol to create
  the characteristic ether (later vinyl-ether) bond of plasmalogens.
- GO term for the MF is **GO:0016287 glycerone-phosphate O-acyltransferase activity**
  (OLS: "Catalysis of the reaction: acyl-CoA + glycerone phosphate = 1-acylglycerone
  3-phosphate + CoA").

## Subcellular localization

- Peroxisome membrane, peripheral membrane protein, **matrix (lumenal) side**.
  [file:human/GNPAT/GNPAT-uniprot.txt "SUBCELLULAR LOCATION: Peroxisome membrane"]
  [file:human/GNPAT/GNPAT-uniprot.txt "Exclusively localized to the"] (…lumenal side of the peroxisomal membrane).
- Has a C-terminal type-1 peroxisomal targeting signal (PTS1). Human C-terminus is
  ...PATAKL; mouse ortholog ends AKL.
  [PMID:9459311 "containing \na C-terminal type 1 peroxisomal targeting signal"]
  [PMID:10395968 "peroxisomal targeting signal type 1 (PTS1) at its extreme carboxy-terminus \n(alanine-lysine-leucine, AKL)"]
- Experimental localization to peroxisome / peroxisomal membrane in human cells:
  PMID:15687349 (EXP/IDA). Consistent Reactome placement in peroxisomal matrix /
  membrane. HDA proteomics also placed it in "membrane" (generic) and peroxisomal
  membrane (PMID:19946888, PMID:21525035 — both large-scale, generic-membrane or
  co-purification contexts).

## Quaternary structure

- Native enzyme isolated as a **trimeric complex** from peroxisomes.
  [PMID:9459311 "isolated as a trimeric complex by \nsucrose density gradient centrifugation"]
- UniProt: "Part of a heterotrimeric complex composed of GNPAT, AGPS and a modified
  form of GNPAT."
  [file:human/GNPAT/GNPAT-uniprot.txt "Part of a heterotrimeric complex composed of GNPAT, AGPS and a"]
- Reactome R-HSA-75879: "The active form of the enzyme is one subunit of a heterotrimer
  with two molecules of the alkylglycerone phosphate synthase (AGPS) enzyme."
- (An earlier placental-purification paper reported an apparent monomer of ~65 kDa,
  PMID:8186247 "these results suggest that DHAPAT is a monomeric protein" — likely a
  solubilized single subunit; superseded by the trimeric-complex view.)

## Catalytic / functional evidence

- Catalytic activity (EC 2.3.1.42) established via cDNA expression in yeast and enzyme
  assays: mouse cDNA PMID:10395968, human RCDP2 characterization PMID:11152660, and
  functional rescue PMID:15687349.
- **Rescue of DHAPAT-deficient CHO variant (NRel-4) by human DHAPAT cDNA restores
  DHAPAT activity and plasmalogen biosynthesis**; peroxisomal DHAPAT is essential for
  plasmalogen synthesis.
  [PMID:15687349 "recovered DHAPAT activity and plasmalogen biosynthesis"]
  [PMID:15687349 "the peroxisomal DHAPAT is essential for the \nbiosynthesis of plasmalogens in animal cells"]
- Importantly, GNPAT/DHAPAT does **not** normally contribute to non-ether (diacyl)
  glycerolipid biosynthesis:
  [PMID:15687349 "peroxisomal DHAPAT does not normally \ncontribute to nonether glycerolipid biosynthesis"]
  → This argues the "phosphatidic acid biosynthetic process" (GO:0006654) annotation is
  peripheral/non-core for GNPAT, even though acyl-DHAP feeds a minor glycerolipid branch.

## Disease

- Biallelic GNPAT mutations cause **rhizomelic chondrodysplasia punctata type 2 (RCDP2;
  MIM 222765)** — defective plasmalogen biosynthesis.
  [file:human/GNPAT/GNPAT-uniprot.txt "Rhizomelic chondrodysplasia punctata 2 (RCDP2)"]
  [PMID:9536089 "All RCDP type 2 patients \nanalyzed were found to contain mutations in their DHAPAT cDNA"]
- Disease variants (e.g. R211H) cause loss of glycerone-phosphate O-acyltransferase
  activity (UniProt VARIANT annotations, PMID:9536089, PMID:11152660).

## Annotation review reasoning

- **Core MF**: GO:0016287 glycerone-phosphate O-acyltransferase activity — strong
  experimental support (multiple IDA). ACCEPT all; IEA/IBA/TAS copies also ACCEPT (own
  correct core function).
- **Core BP**: GO:0008611 ether lipid biosynthetic process — IDA + IBA + IEA + TAS;
  ACCEPT.
- **Core CC**: GO:0005778 peroxisomal membrane (EXP/IDA/IBA/IEA/HDA) and GO:0005777
  peroxisome — ACCEPT. GO:0005782 peroxisomal matrix (Reactome TAS) is compatible with
  the lumenal/matrix-side localization — KEEP_AS_NON_CORE (matrix vs membrane nuance).
- **Generic/parent MF**: GO:0016746, GO:0016747 acyltransferase activity (IEA parents of
  the specific MF) — MARK_AS_OVER_ANNOTATED (uninformative parents).
- **Broad BP**: GO:0006629 lipid metabolic process, GO:0006650 glycerophospholipid
  metabolic process — correct but general; KEEP_AS_NON_CORE.
- **GO:0006654 phosphatidic acid biosynthetic process** (Reactome TAS) — peripheral;
  PMID:15687349 shows GNPAT does not normally contribute to nonether glycerolipids →
  KEEP_AS_NON_CORE.
- **GO:0016020 membrane** (HDA) — generic; KEEP_AS_NON_CORE (true but uninformative).
- **GO:0005829 cytosol** (Reactome TAS, from Peroxisomal-protein-import pathway) —
  reflects the transient cytosolic state of newly synthesized PTS1 cargo before import,
  not steady-state localization → MARK_AS_OVER_ANNOTATED (as a location claim for the
  mature enzyme).
</content>
