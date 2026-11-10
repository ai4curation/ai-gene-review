# Prkar2a (rat, UniProt P12368) - manual literature synthesis

No deep-research provider was run for this gene (no API keys available in this
environment). This file records a manual synthesis from the UniProt record and
the cached publications in `publications/`. Each statement carries its source.

## Identity and domain architecture

- Rat Prkar2a encodes the type II-alpha regulatory subunit (RIIalpha) of
  cAMP-dependent protein kinase (PKA), 401 aa [UniProt P12368].
- Domain organisation: an N-terminal dimerization/docking (D/D, RIIa) domain
  (Pfam PF02197; SMART SM00394), a linker containing the autoinhibitory
  (pseudosubstrate/substrate) site, and two tandem cyclic nucleotide-binding
  domains (Pfam PF00027 x2; CDD cd00038 x2) [UniProt P12368 DR lines].
  UniProt: "Belongs to the cAMP-dependent kinase regulatory chain family."
- UniProt FUNCTION: "Regulatory subunit of the cAMP-dependent protein kinases
  involved in cAMP signaling in cells. Type II regulatory chains mediate
  membrane association by binding to anchoring proteins, including the MAP2
  kinase."
- UniProt SUBUNIT: "The inactive form of the enzyme is composed of two
  regulatory chains and two catalytic chains. Activation by cAMP produces two
  active catalytic monomers and a regulatory dimer that binds four cAMP
  molecules."

## Core biochemistry

- Inhibition of the catalytic subunit and cAMP-triggered release
  [PMID:21177871 "RII subunits bind to the catalytic subunits and potently
  inhibit their activity. cAMP causes the dissociation of C subunits from RII
  subunits and thereby activation of the catalytic subunits."]. In that paper
  recombinant RIIalpha titrated onto C subunits limited C activity to ~40%, and
  cAMP restored activity.
- cAMP binding of RIIalpha measured directly on 8-AHA-cAMP SPR chips
  [PMID:21177871 "binding of RIIα to cAMP was reduced by 50%" (by the compound
  FMP-API-1/27)]. Note: SPR used "human PKA regulatory subunit RIIα" and RIIalpha
  numbering 1-404 (human length); rat RIIalpha is 401 aa.
- [3H]cAMP binding to R subunits and RIIalpha protein levels in rat brain
  particulate and cytosolic fractions [PMID:11907174, abstract only].

## AKAP anchoring (the defining RII property)

- D/D domain forms a hydrophobic groove that docks the AKAP amphipathic helix
  [PMID:17081990 "A stable, hydrophobic docking groove is formed by the helical
  interface of two RIIalpha protomers."]; crystal structure of the RIIalpha D/D
  bound to the D-AKAP2 helix [PMID:17081990].
- AKAP partners reported with rat RIIalpha: mAKAP (cardiac myocyte hypertrophy;
  PMID:16306226, abstract only), AKAP15/18 in cardiac T-tubules with CaV1.2
  [PMID:14569017, full text: "Whereas a clear overlap of Ca V 1.2 channel and
  RIIα staining was detected along the z -line in the transverse tubules"],
  AKAP15/18 regulated by RII Ser96 phosphorylation [PMID:18550536, abstract only],
  GSKIP [PMID:20007971 "GSKIP directly interacts with PKA and GSK3beta"],
  myomegalin [PMID:21569246], dystrobrevin [PMID:17610895], MyRIP [UniProt,
  PMID:17827149], neurobeachin [Reactome R-RNO-9668570].
- Small-molecule AKAP-PKA disruptor FMP-API-1 binds an allosteric site
  C-terminal to the D/D domain and both displaces RII from AKAPs and activates
  PKA [PMID:21177871 "The molecules bind to an allosteric site of regulatory
  subunits of PKA"].

## Localisation

- Cytoplasm, cell membrane (by similarity) [UniProt]; T-tubules of ventricular
  myocytes [PMID:14569017]; perinuclear region of cardiomyocytes
  [PMID:18550536, GOA IDA; abstract does not state it]. Human orthologue:
  centrosome, axoneme, membrane rafts (ISO rows; not inspected here).

## Physiology

- Oocyte meiotic arrest: active PKA maintains meiotic arrest in growing rat
  oocytes; R:C ratio 1:1 [PMID:16816331, abstract only]. This is PKA-level
  physiology rather than an RIIalpha-specific step.
- Cardiac: compartmentalized PKA signalling controlling phospholamban/RyR
  phosphorylation and contractility [PMID:18550536; PMID:21177871].

## Uncertainties

- Which rat experiments in PMID:21177871 used rat versus human RIIalpha.
- The source of the RGD ISO oocyte/germinal vesicle annotations (RGD:14184392)
  could not be inspected.
