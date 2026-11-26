# bioB (P12996) notes

Part of the RADICAL_SAM project (projects/RADICAL_SAM.md), Phase 2 E. coli K-12.

## Literature sources

No deep-research file is available for this gene (falcon fails authentication and asta
returned nothing useful in Phase 1). These notes are built from the cached publications
(`publications/PMID_*.md`, most abstract-only; PMID:19821612 and PMID:24561554 are full text),
the UniProt record and PubMed searches.

## Identity and family

- Biotin synthase, EC 2.8.1.6, 346 aa. Radical SAM superfamily, biotin synthase family
  (HAMAP MF_01694, TIGR00433 bioB, PTHR22976, Pfam PF04055 Radical_SAM + PF06968 BATS).
  [file:ECOLI/bioB/bioB-uniprot.txt "Belongs to the radical SAM superfamily. Biotin synthase family."]
- Crystal structure (PDB 1R30, 3.4 A) with SAM and dethiobiotin bound.
  [PMID:14704425 "The crystal structure of biotin synthase from Escherichia coli in complex with S-adenosyl-L-methionine and dethiobiotin has been determined to 3.4 angstrom resolution."]

## Catalytic activity

- Converts dethiobiotin (DTB) to biotin by inserting one sulfur between C6 and C9, the last step
  of biotin synthesis. [file:ECOLI/bioB/bioB-uniprot.txt "Catalyzes the conversion of dethiobiotin (DTB) to biotin by the insertion of a sulfur atom into dethiobiotin via a radical-based mechanism."]
- First purification and in vitro activity; Km(DTB) 2 uM; dimer.
  [PMID:8142361 "The bioB gene product we have isolated is active in the conversion of dethiobiotin to biotin in vitro in the presence of NADPH, AdoMet, Fe3+ or Fe2+, and additional unidentified factors from the crude extracts of E. coli."]
- Catalysis needs SAM and flavodoxin (the physiological reductant: NADPH, flavodoxin
  reductase, flavodoxin) and gives 5'-deoxyadenosine and methionine.
  [PMID:11444982 "Catalysis requires AdoMet and flavodoxin and generates 5'-deoxyadenosine and methionine, suggesting that biotin synthase is an AdoMet-dependent radical enzyme."]
- Mechanism: sulfur added first at C9 (9-mercaptodethiobiotin), then at C6.
  [PMID:22326745 "a [2Fe-2S](2+) cluster bound deep within biotin synthase provides a sulfur atom that is added to dethiobiotin in a stepwise reaction, first at the C9 position to generate 9-mercaptodethiobiotin"]
- YNHNLD motif mutants: inactive variants still carry clusters but cannot cleave SAM; all six
  cluster cysteines are required. [PMID:17014080 "Single-point mutation of each of these six conserved cysteines produced inactive variants."]

## Clusters

- Two clusters: a radical SAM [4Fe-4S] (Cys53, Cys57, Cys60 + SAM) and an auxiliary [2Fe-2S]
  (Cys97, Cys128, Cys188, Arg260). [PMID:17014080 "a [4Fe-4S](2+) cluster liganded by Cys-53, Cys-57, and Cys-60 and the S-adenosylmethionine (AdoMet or SAM) cosubstrate and a [2Fe-2S](2+) cluster liganded by Cys-97, Cys-128, Cys-188, and Arg-260"]
- Spectroscopic confirmation of two distinct sites; SAM binds the unique Fe of the [4Fe-4S].
  [PMID:14967041 "The results confirm that BioB contains two distinct Fe-S cluster binding sites."]
- The [2Fe-2S] is destroyed during a single turnover while the [4Fe-4S] survives: the
  auxiliary cluster is the sulfur source. [PMID:11444982 "during catalysis the [4Fe-4S](2+) cluster is preserved while the [2Fe-2S](2+) cluster is destroyed"]
  [PMID:12873140 "This is consistent with the hypothesis that the reduced (4Fe-4S) cluster is involved in mediating the cleavage of AdoMet and that the (2Fe-2S)(2+) is the sulfur source for biotin."]
- Structure places the substrate between the two clusters.
  [PMID:14704425 "The structure places the substrates between the Fe4S4 cluster, essential for radical generation, and the Fe2S2 cluster, postulated to be the source of sulfur"]
- Older proposals (PLP-dependent cysteine desulfurase activity of BioB) were not reproduced.
  [PMID:14967041 "no evidence for PLP binding or for PLP-induced cysteine desulfurase or biotin synthase activity was observed"]

## In vivo turnover and cluster regeneration

- In vitro BioB makes <1 biotin per polypeptide; in vivo it is catalytic but catalysis puts the
  protein at risk of proteolysis. [PMID:15850983 "We report in vivo experiments demonstrating that biotin synthase is catalytic but that catalysis puts the protein at risk of proteolytic destruction."]
- HscA (Hsp70-type ISC chaperone) binds apo/partially cluster-loaded BioB and improves [2Fe-2S]
  assembly in vivo; ternary complex with IscU. [PMID:19821612 "we show that in Escherichia coli, HscA significantly improves the efficiency of the in vivo assembly of the [2Fe-2S](2+) cluster on BioB under conditions of low to moderate iron"]
  BioB is the client here; the interaction does not define a BioB molecular function.
- 5'-deoxyadenosine product inhibition; requires Pfs (MtnN) nucleosidase in vivo.
  [PMID:15911379 "Escherichia coli strains lacking the 5'-methylthioadenosine/S-adenosylhomocysteine nucleosidase encoded by the pfs gene are deficient in biotin synthase activity due to accumulation of 5'-deoxyadenosine"]

## Quaternary structure

- Homodimer by native gel (PMID:8142361), aerobic purification (PMID:11444982), and crystal
  structure (PMID:14704425, 1R30 chains A/B). Structural, not core to catalysis.

## Interactions

- Y2H with YafJ (Q47147, putative glutamine amidotransferase) from the binary interactome
  screen (PMID:24561554). No functional follow-up; uninformative.

## GO decisions (summary)

- Generic rows follow the RADICAL_SAM treatment rule: GO:0003824 -> GO:0004076; GO:0051536 ->
  GO:0051539 + GO:0051537 (BioB has both cluster types, so both descendants are listed);
  GO:0005506 iron ion binding treated like GO:0046872 (lateral correction to the two cluster
  terms).
- GO:0051537 is ACCEPTed as core: the [2Fe-2S] is the sulfur donor, not a peripheral feature.
  This differs from genes/PSEPK/bioB (KEEP_AS_NON_CORE) and matches yeast/BIO2 and SCHPO/bio2 (ACCEPT).
- NEW GO:1904047 SAM binding (IDA, crystal structure with SAM bound, PMID:14704425).
- Protein binding rows (HscA, YafJ) REMOVE as uninformative.
