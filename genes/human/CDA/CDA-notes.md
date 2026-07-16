# CDA (Cytidine deaminase) — Gene Review Notes

UniProt: P32320 (CDD_HUMAN). Gene symbol CDA (synonym CDD), HGNC:1712. Human, NCBITaxon:9606.
146 aa, ~16.2 kDa monomer.

## Core identity and function

CDA is **cytidine deaminase** (EC 3.5.4.5), a cytosolic Zn2+-dependent hydrolase that catalyzes
the hydrolytic deamination of cytidine and 2'-deoxycytidine to uridine and 2'-deoxyuridine,
releasing ammonia. It is the pyrimidine-salvage/catabolism enzyme that recycles exogenous and
endogenous (deoxy)cytidine.

- Catalytic activities (UniProt CATALYTIC ACTIVITY):
  - "cytidine + H2O + H(+) = uridine + NH4(+)" (RHEA:16069), EC=3.5.4.5, ECO:0000269|PubMed:7923172
    [file:human/CDA/CDA-uniprot.txt "Reaction=cytidine + H2O + H(+) = uridine + NH4(+);"]
  - "2'-deoxycytidine + H2O + H(+) = 2'-deoxyuridine + NH4(+)" (RHEA:13433), EC=3.5.4.5,
    ECO:0000269|PubMed:9596658
    [file:human/CDA/CDA-uniprot.txt "Reaction=2'-deoxycytidine + H2O + H(+) = 2'-deoxyuridine + NH4(+);"]
- FUNCTION (UniProt): "This enzyme scavenges exogenous and endogenous cytidine and
  2'-deoxycytidine for UMP synthesis."
  [file:human/CDA/CDA-uniprot.txt "This enzyme scavenges exogenous and endogenous cytidine and"]
- Cofactor: Zn(2+) (ChEBI:CHEBI:29105); catalytic zinc coordinated by residues 65, 99, 102
  (UniProt BINDING features). ICP-OES showed 1 Zn atom per subunit
  [PMID:8812871 "analysis revealed the presence of 1 atom of Zn"].
- Active site: proton donor at residue 67 (UniProt ACT_SITE).

## Enzyme characterization / discovery

- Purified 47,000-fold to homogeneity from human placenta; monomer ~16.1 kDa (SDS-PAGE),
  ~48.7 kDa native (gel filtration) → 3–4 identical subunits; cDNA cloned encoding 146 aa;
  gene localized to chromosome 1. High CR deaminase activity of E. coli-expressed protein
  [PMID:7923172 "The expressed protein had a high CR deaminase activity", "suggesting that it contains three or four identical subunits"].
- Recombinant human CDA characterized: tetramer (cross-linking), 1 Zn per subunit; used to
  deaminate several antitumoral cytidine-analog drugs
  [PMID:8812871 "Cross-linking experiment indicated that the enzyme is a tetramer",
  "CDA causes the deamination of several antitumoral cytidine-analog drugs"].

## Quaternary structure

- Homotetramer. UniProt SUBUNIT "Homotetramer." (ECO:0000269|PubMed:15689149).
  [file:human/CDA/CDA-uniprot.txt "Homotetramer."]
- Crystal structure (PDB 1MQ0) of human CDA bound to diazepinone riboside inhibitor 1; a
  substrate-analog/inhibitor sits in the active site making pi/pi with Phe137
  [PMID:15689149 "the first crystal structure of human CDA as a complex with",
  "a canonical pi/pi-interaction with a key active site residue, Phe 137"].
- Homology-model / homotetramer confirmation of the cytosolic metalloprotein
  [PMID:16303324 "Cytidine deaminase (CDA) is a cytosolic metalloprotein whose functional unit can",
  "be either a homotetramer (T-CDA) or a homodimer (D-CDA)"].

## Biological roles

- Pyrimidine salvage / catabolism: recycles (deoxy)cytidine to (deoxy)uridine feeding UMP
  synthesis (UniProt FUNCTION). Reactome "Pyrimidine salvage" (R-HSA-73614) and the reaction
  "deamination of 2'-Deoxycytidine to 2'-Deoxyuridine" (R-HSA-73608)
  [reactome/R-HSA-73608.md "Cytosolic cytidine deaminase catalyzes the hydrolysis of cytidine or dexoycytidine"].
- Hematopoietic growth regulation: recombinant CDA potently inhibits growth of
  granulocyte-macrophage colony-forming cells (GM-CFC); requires catalytic activity; acts by
  depleting the cytidine/deoxycytidine pool needed for DNA synthesis
  [PMID:9596658 "the catalytic nucleoside deaminating function of the protein is essential for the growth suppressive effect",
  "CDD exerts growth inhibition by depleting the cytidine and deoxycytidine pool"].
  dCMP is NOT a substrate: [PMID:9596658 "deoxycytidine monophosphate, which is",
  "not a substrate for CDD"] — i.e. CDA acts on nucleosides, not the monophosphates.
- Drug metabolism (pharmacology): CDA inactivates cytidine-analog chemotherapeutics
  (cytarabine/ara-C, gemcitabine, decitabine, azacitidine, capecitabine); UniProt DrugBank
  cross-references list these. It is a Tclin pharmacology target (Pharos). CDA polymorphisms
  (e.g. K27Q, rs2072671) modulate drug toxicity. Not directly annotated with a GO drug-response
  term in GOA, but underlies the pharmacogenomic importance.

## Localization

- Cytosol/cytoplasm: strongly supported (IDA UniProtKB DR "C:cytosol; IDA:UniProtKB";
  multiple GOA IDA entries; Reactome R-HSA-73608 "Cytosolic cytidine deaminase").
  [file:human/CDA/CDA-uniprot.txt "GO:0005829; C:cytosol; IDA:UniProtKB."]
- Neutrophil-granule / extracellular-region annotations come from Reactome neutrophil
  degranulation proteomics (R-HSA-6798745/6798748/6800434, "Exocytosis of ... granule lumen
  proteins"). CDA has no signal peptide (UniProt shows no SIGNAL feature; CHAIN 1..146,
  cytosolic). These extracellular/granule-lumen locations reflect release during neutrophil
  degranulation, not the primary catalytic compartment — treat as non-core / secondary.

## Protein interactions (GO:0005515 IPI / GO:0042802)

- Many high-throughput binary-interactome IPI entries (Rolland 2014 PMID:25416956; Luck 2020
  PMID:32296183; Sahni 2015 PMID:25910212; Huttlin/others PMID:31515488) list partners
  (SDCBP, ZBTB24, PSMA1, PTGER3, LNX1, PLEKHB2, NTAQ1, FNDC11, ARRDC3, FOXN1, DDIT4L, INCA1,
  KRTAP6-1, KRTAP8-1, GORASP2, ADAT3). No specific biological function established for these;
  "protein binding" (GO:0005515) is uninformative. Self-interaction IPI (GO:0042802 identical
  protein binding) is consistent with the well-established homotetramer.

## Term-quality notes

- GO:0009972 "cytidine deamination" is OBSOLETE (single-step process; no replacement) — do NOT
  use in core_functions. Use GO:0006216 "cytidine catabolic process" / GO:0006217 "deoxycytidine
  catabolic process" or GO:0008655 "pyrimidine-containing compound salvage" for BP.
- CMP/dCMP catabolic process (GO:0006248 / GO:0006249) IDA from MGI: CDA's direct substrates are
  the *nucleosides* (deoxy)cytidine, NOT the monophosphates CMP/dCMP (deamination of dCMP is
  performed by DCTD). These are experimental annotations (do not REMOVE) but are at best
  pathway-context / arguably imprecise for the direct catalytic step; mark non-core.
- Reactome cytosol TAS (R-HSA-73608) and neutrophil-granule TAS entries are auto-imported.
