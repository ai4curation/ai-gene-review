# Psmc6 (rat, G3V6W6): manual literature research

No deep-research provider API was available for this session, so this summary was
compiled by hand from the cached publications, the UniProt record and PubMed. Every
claim carries its source.

## Identity

- Rat Psmc6 (UniProt G3V6W6, unreviewed TrEMBL entry, 403 aa; RGD:1308825,
  GeneID 289990) is the 26S proteasome regulatory subunit 10B, also called p42, S10b
  and, in yeast nomenclature, Rpt4 (Sug2 in budding yeast). Names on the TrEMBL entry
  are ARBA-generated, but the gene is unambiguous through RGD, Ensembl and CTD (human
  gene 5706, PSMC6). [file:rat/Psmc6/Psmc6-uniprot.txt]
- Family and domains: AAA ATPase family (RuleBase RU003651), InterPro
  26S_Proteasome_ATPase (IPR050221), ATPase_AAA_core (IPR003959), AAA conserved site
  (IPR003960, PROSITE PS00674), AAA lid (IPR041569) and the proteasomal ATPase OB-fold
  (IPR032501); PANTHER PTHR23073. [file:rat/Psmc6/Psmc6-uniprot.txt]
- Sequence features read from the record: Walker A P-loop GPPGTGKT (in
  ...LLYGPPGTGKTLLARA...), Walker B ...IIFMDEIDAI... (DEID), and an N-terminal region
  predicted to form the coiled coil that pairs with Rpt5. The C-terminus ends ...LDYKPV,
  which is NOT a hydrophobic-tyrosine-X (HbYX) motif; Rpt2, Rpt3 and Rpt5 carry HbYX
  tails, Rpt4 does not.
- Structure: rat Psmc6 chains are present in the in-situ cryo-ET 26S proteasome models
  from rat primary neurons (PDB 6EPC/6EPD/6EPE/6EPF), fitted from yeast 26S atomic
  models. [PMID:29398115 "we transduced primary rat neuronal cultures with a GFP-tagged codon-modified synthetic construct expressing (GA)175-GFP"]

## Function in the 26S proteasome (family and orthology level)

- The six 19S base ATPases form a heterohexameric ring in a fixed order, with Rpt4
  between Rpt3 and Rpt5.
  [PMID:23495936 "The six ATPases adopt a single arrangement in normal cells: Rpt1-Rpt2-Rpt6-Rpt3-Rpt4-Rpt5"]
- Mammalian base assembly proceeds through three ATPase-pair modules; Rpt4 enters
  with Rpt5 and the chaperone p27 (PSMD9).
  [PMID:19490896 "followed by incorporation of the p27-Rpt5-Rpt4 complex and Rpn2"]
- The base ATPases use ATP to unfold substrates and open the 20S gate; HbYX tails
  dock into alpha-ring pockets.
  [PMID:17803938 "Upon ATP binding, these C-terminal residues bind to pockets between the 20S's alpha subunits."]
- Rpt4's own tail is the exception: in the human substrate-engaged structures it was
  not seen in an alpha pocket, consistent with its non-HbYX C-terminus. Rpt4
  therefore contributes to substrate unfolding/translocation as part of the ring, but
  not to gate opening by HbYX docking.
  [PMID:29636472 "the carboxyl (C)-terminal tails of Rpt subunits, with the exception of Rpt4, were inserted into the corresponding α-pockets"]
- Localisation: yeast Rpt4 is almost exclusively nuclear, in contrast to proteasome
  localisation in multicellular organisms, where proteasomes are cytosolic and nuclear.
  [PMID:10419517 "In contrast to findings in multicellular organisms, these proteins are localized almost exclusively to the nucleus throughout the cell cycle."]

## Rat experimental data

### Rousseau et al. 2009 (PMID:18986984, full text read)

- In rat hippocampal primary neurons (E18), endogenous Rpt4 and Rpt3 co-localise with
  mutant huntingtin (Htt73) inclusions; 20S alpha7 does not.
  [PMID:18986984 "Rpt4 and Rpt3 co-localize with poly(Q) inclusions."]
  [PMID:18986984 "Primary cultures of rat hippocampal neurons were prepared from E18 rats."]
- In (human) 293T cell glycerol gradients, endogenous and overexpressed Rpt4 is in both
  the 26S proteasome and the 20S-free "APIS"/free 19S-like complex; most overexpressed
  Rpt4 sits in APIS.
  [PMID:18986984 "Similarly, a fraction of overexpressed Rpt4 entered the 26S proteasome, whereas most of the protein was found in the smaller APIS complex"]
- Overexpression of Rpt4 or Rpt6 increases aggregation of mutant Htt and ataxin-3
  without impairing proteasomal degradation (293T cells).
- siRNA knockdown of endogenous Rpt4 (rat siRNAs, ~50% reduction) in rat primary
  neurons reduces the fraction of Htt73-expressing neurons with inclusions; this is the
  basis of the IMP positive regulation of inclusion body assembly row.
  [PMID:18986984 "Similarly, two siRNAs designed against Rpt4 reduced the levels of the protein"]
  [PMID:18986984 "demonstrates that reducing the levels of Rpt4 or Rpt6 in primary neurons"]
- Authors' model: aggregation is promoted by the 19S chaperone (unfoldase) subunits,
  independently of proteolysis. This is a disease-model gain-of-aggregation effect,
  not a normal physiological process.

### Guo et al. 2018 (PMID:29398115, full text cached)

- Poly-GA aggregates in rat primary neurons recruit numerous 26S proteasomes, stalled
  in a substrate-processing conformation; this is the source of the rat Psmc6 PDB
  models.
  [PMID:29398115 "poly-GA aggregates consist of densely packed twisted ribbons that recruit numerous 26S proteasome complexes"]

### Sun et al. 2023 (PMID:37228199, abstract only; no PMC copy)

- Free 19S particles are abundant near synapses in rat cortical neurons; they bind and
  deubiquitylate K63-ubiquitin; inhibition of 19S deubiquitylase activity reduced
  synaptic AMPA receptor availability in a proteasome-independent manner.
  [PMID:37228199 "We discovered an unexpected abundance of free 19S particles near synapses."]
- The abstract does not mention synaptic vesicles or Psmc6 individually. The
  ComplexPortal annotations to every 19S subunit (synaptic vesicle IDA/NAS, AMPA
  receptor activity IDA, proteasome accessory complex IPI) cannot be checked against
  Psmc6-specific data.

## Open points

- Identical protein binding (ISO/IEA from human PSMC6) could not be traced to a
  cached paper; Rpt4 is not known to self-associate within the proteasome, where it
  pairs with Rpt5. Likely a high-throughput interactome hit.
