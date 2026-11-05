# LOC541641 (ZmHK2) manual literature research

No deep-research API was available; this summary was compiled manually from cached
publications and PubMed searches (queries: "ZmHK2", "maize cytokinin receptor",
"Lomin SN[Author]", "Yonekura-Sakakibara K[Author]").

## Identity

- UniProt A0A1D6N2S4 (TrEMBL, unreviewed), 1007 aa; NCBI GeneID 541641 is named
  "histidine kinase 2" (alias hk2, GRMZM2G471529, Zm00001d042312; B73 v5 Zm00001eb143050).
- The ZmHK2 cDNA (GenBank AB102956) encodes a 1,007-residue protein
  [PMID:15064375 "The longest cDNA clones of ZmHK1 and ZmHK2 contained reading frames of 974 and 1,007 amino acids, respectively."].
  The ZmHK2 cloning primer used by Lomin et al. (5'-CGGATCCAATGACCGTTACGGCG-3')
  encodes M-T-V-T-A, matching the A0A1D6N2S4 N terminus (MTVTAR...), and the
  Ala695-Gln1007 fragment boundary matches the 1007-residue length [PMID:21778179].
- ZmHK2 is the maize orthologue of Arabidopsis AHK3 [PMID:15064375 "Homology analyses revealed that ZmHK1, ZmHK2, and ZmHK3a/b were closely related to AHK4, AHK3, and AHK2, respectively"]; PANTHER PTHR43719:SF73 (HISTIDINE KINASE 3).

## Domain architecture (UniProt A0A1D6N2S4)

Two predicted TM helices (68-86, 370-392) flanking a CHASE domain (137-361), a
histidine kinase domain (429-699; phospho-His432), a receiver-like domain (CRE1
first receiver, Pfam PF24896) and a C-terminal receiver domain (864-1000; Asp914).
All residues needed for HK and receiver function are conserved
[PMID:15064375 "All of the amino acid residues required for the HK and receiver function ( Mizuno, 1998 ) were conserved (data not shown)."].

## Receptor function

- Expressed in the E. coli rcsC mutant (cps::lacZ reporter), ZmHK2 confers
  cytokinin-inducible reporter expression; tZ and tZ riboside are the strongest
  activators [PMID:15064375 "On the other hand, in ZmHK2 -expressing E. coli , tZ and tZ riboside (tZR) activated lacZ expression most strongly"];
  ZmHK2 also responds to cis-zeatin [PMID:15064375 "all ZmHKs responded to cis-zeatin (cZ)"].
- Direct radioligand ([3H]tZ) competition binding in bacterial spheroplasts:
  ZmHK2 has the highest affinity of the three maize receptors for most cytokinins
  [PMID:21778179 "ZmHK2 demonstrated the highest affinities to almost all the cytokinins tested, including DZ"],
  and a uniquely high affinity for dihydrozeatin
  [PMID:21778179 "the DZ affinity of ZmHK2 was more than two orders of magnitude higher than those of other receptors"].

## Localization

- ZmHK2 itself has not been localized with a specific antibody or a fluorescent
  fusion; the monoclonal antibody used by Lomin et al. recognises ZmHK1 only
  [PMID:21778179 "The mAB reacted with ZmHK1, but not with ZmHK2 and ZmHK3a"].
- In leaves, where ZmHK2 predominates
  [PMID:21778179 "leaf microsomes seemed greatly enriched with ZmHK2"],
  specific tZ binding per mg protein was higher in the plasma membrane-enriched
  fraction, but after correcting for membrane abundance at least 80% of leaf binding
  was assigned to endomembranes
  [PMID:21778179 "it was estimated that no less than 90% and 80% of the total amount of [3H]tZ specific binding was attributed to endomembrane fractions from roots and leaves, respectively."].
- The Arabidopsis orthologue AHK3 is mainly in the ER [PMID:21709172], with its
  CHASE domain facing the ER lumen and active phosphotransfer from ER membranes
  [PMID:32291033]; reviews conclude the ER is the predominant but not exclusive
  site of perception [PMID:29355964].

## Expression and genetics

- ZmHK2 is the predominant receptor transcript in leaf blades
  [PMID:15064375 "The accumulation of the ZmHK2 transcript in leaf blades was 4- and 13-fold larger than that of ZmHK1 and ZmHK3a"].
- Overexpression of ZmHK2 in Arabidopsis reduced seed size and root growth and
  up-regulated ARR5 [PMID:24585212, abstract only]. No maize loss-of-function
  mutant has been described. These heterologous phenotypes do not establish
  participation in specific developmental processes.

## Inference for GO

- MF: transmembrane histidine kinase cytokinin receptor activity (GO:0009885),
  cytokinin binding (GO:0044373), phosphorelay sensor kinase activity (GO:0000155).
- BP: cytokinin-activated signaling pathway (GO:0009736); phosphorelay signal
  transduction system (GO:0000160).
- CC: endomembrane system / membrane; ER membrane likely by orthology but not
  directly shown for ZmHK2.

## Literature-search negatives

PubMed searches for ZmHK2 (and maize cytokinin receptors generally) found no study of
ZmHK2 in cold responses or in seed germination in maize.
