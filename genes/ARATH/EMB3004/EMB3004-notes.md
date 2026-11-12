# DHQSD / EMB3004 (Q9SQT8, At3g06350) – Arabidopsis bifunctional 3-dehydroquinate dehydratase / shikimate dehydrogenase, chloroplastic

## Provenance of these notes

Provider deep research (`just deep-research`) was unavailable for this review (no provider
key in the session), so no `-deep-research-*.md` file exists. These notes are compiled by
hand from cached publications in `publications/`, the UniProt record (`EMB3004-uniprot.txt`)
and the PANTHER family review (`interpro/panther/PTHR21089/PTHR21089-review.yaml`).
Literature checked: PMID:16784230 (abstract only), PMID:15634699, PMID:18431481,
PMID:18633119, PMID:20061580, PMID:21166475, PMID:25293756, PMID:12837789 and PMID:25524738
(family context). The 2007 Cryst. Growth Des. structure (DOI:10.1021/cg7007107) and
PMID:29890023 are known only through the UniProt record.

## Domain architecture

- 603 residues; predicted chloroplast transit peptide 1-66 (UniProt FT TRANSIT, ECO:0000255),
  mature chain 67-603.
- N-terminal region 96-313: type I 3-dehydroquinase (Pfam PF01487 DHquinase_I, InterPro
  IPR001381, NCBIfam TIGR01093 aroD, HAMAP MF_00214). The Schiff-base lysine (K241) and
  proton acceptor (H214) are placed by PMID:16784230. This domain is homologous to the type I
  DHQase family (PANTHER PTHR43699), but PANTHER classifies the whole protein only in
  PTHR21089:SF1.
- C-terminal region 328-558: shikimate dehydrogenase (Pfam PF08501/PF01488/PF18317, IPR011342,
  TIGR00507 aroE, HAMAP MF_00222), PTHR21089:SF1.
- UniProt: "In the N-terminal section; belongs to the type-I 3-dehydroquinase family" and
  "In the C-terminal section; belongs to the shikimate dehydrogenase family".

## Activities (both core)

- Bifunctional: catalyses steps 3 and 4 of the shikimate pathway
  [PMID:16784230 "The bifunctional enzyme dehydroquinate dehydratase-shikimate dehydrogenase (DHQ-SDH) catalyzes the dehydration of dehydroquinate to dehydroshikimate and the reduction of dehydroshikimate to shikimate in the shikimate pathway."].
- Crystal structure with shikimate in the SDH site and tartrate in the DHQ site; mutagenesis
  identifies the SDH catalytic residues
  [PMID:16784230 "Site-directed mutagenesis and mechanistic analysis revealed that Asp 423 and Lys 385 are key catalytic groups and Ser 336 is a key binding group."].
- The two active sites face each other, which raises the effective concentration of the
  intermediate 3-dehydroshikimate
  [PMID:16784230 "The arrangement of the two functional domains reveals that the control of metabolic flux through the shikimate pathway is achieved by increasing the effective concentration of dehydroshikimate through the proximity of the two sites."].
- UniProt kinetics (ECO:0000269, PMID:16784230): Km 685 uM shikimate, 131 uM NADP; monomer.
  The physiological direction is DHQ -> DHS (dehydratase) and DHS -> shikimate (NADPH reductase).
- NADP(H) complex structures (PDB 2O7S, Ref.8) define the NADP-binding residues.

## Location

- Plastid enzyme: predicted transit peptide; found in several chloroplast proteomes.
  - Zybailov et al. 2008: 1325 proteins in ten chloroplast preparations
    [PMID:18431481 "Here we present a large scale analysis by nanoLC-Q-TOF and nanoLC-LTQ-Orbitrap mass spectrometry (MS) of ten independent chloroplast preparations from Arabidopsis thaliana which unambiguously identified 1325 proteins."].
  - AT_CHLORO (Ferro et al. 2010) assigned subplastidial location (stroma, thylakoid, envelope)
    by spectral counting [PMID:20061580 "We assessed the partitioning of each protein in the three chloroplast compartments by using a semiquantitative proteomics approach (spectral count)."].
  - Rutschow et al. 2008 (van Wijk lab) quantitative stromal proteomics of the cpSRP54 (ffc) mutant (PMID:18633119) gives the second
    stroma HDA row (abstract-only cache).
  - Aryal et al. 2014 (PMID:25293756) is a size-exclusion study of the crude cytosolic fraction of
    leaves; how it supports a chloroplast HDA row cannot be seen in the cached text.
- The Ito et al. 2011 cytosolic proteome of cell suspensions (PMID:21166475) is the basis of a NOT
  cytosol (RCA) row. This is consistent with the transit peptide and plastid proteomics.
- Stroma is the sub-compartment where the shikimate pathway enzymes act. Two independent lines
  support it: the soluble enzyme has no transmembrane segment after the transit peptide, and
  AT_CHLORO places it in the stroma.

## In vivo role

- Listed as EMBRYO DEFECTIVE 3004; a Ds insertion from the Pagnussat et al. 2005 female
  gametophyte/early embryo screen (PMID:15634699, abstract-only) gives the IMP embryo development
  row. The phenotype is best read as the consequence of losing the plastid shikimate pathway (the
  only source of aromatic amino acids), not as a developmental function of the enzyme.
- Arabidopsis has DHQ-SDH-like paralogs that act as quinate dehydrogenases in secondary metabolism
  (PMID:29890023, via UniProt), so EMB3004 is the biosynthetic shikimate-pathway isoform.

## Curation conclusions (summary)

- Core: 3-dehydroquinate dehydratase activity (GO:0003855) and shikimate 3-dehydrogenase (NADP+)
  activity (GO:0004764), both in chorismate biosynthetic process (GO:0009423), in the chloroplast
  stroma (GO:0009570).
- Chloroplast root rows are kept; the stroma rows already exist (HDA), so no NEW row is needed.
- NOT cytosol is accepted.
- Embryo development is kept as non-core (indirect).
