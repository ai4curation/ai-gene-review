# rsks-1 (Q9NAH6) manual literature research

No deep-research provider API was available for this session, so this is a manual
literature synthesis from cached publications (publications/PMID_*.md), the UniProt
record (rsks-1-uniprot.txt) and PubMed/PMC full text. All quotes are verbatim.

## Identity and family

- RSKS-1 (Y47D3A.16, WBGene00012929) is the single C. elegans p70 ribosomal protein S6
  kinase (S6K) ortholog, 550 aa, AGC kinase family, S6 kinase subfamily
  [UniProt Q9NAH6 "Belongs to the protein kinase superfamily. AGC Ser/Thr protein kinase family. S6 kinase subfamily."].
- Domains: protein kinase domain 83-344 (ATP-binding K115; proton acceptor D210), AGC-kinase
  C-terminal domain 345-415, disordered C-terminal tail (UniProt FT lines; PIRSF000605,
  CDD cd05584 STKc_p70S6K).
- T404 corresponds to the TOR-site hydrophobic-motif threonine (T389 in human S6K1)
  [PMID:22278922 "TOR phosphorylates a highly conserved threonine residue in Drosophila and human S6K"];
  T404A fails to rescue the germline phenotype [PMID:22278922 "the T404A transgene did not rescue the germline phenotype of rsks-1(sv31)"].
- Kinase activity has not been measured biochemically for the worm protein; K115Q
  (predicted kinase-dead) behaves as loss of function in axon regrowth (UniProt MUTAGEN 115,
  PMID:24431434).

## TORC1 pathway position

- Acts downstream of TOR/RAPTOR in germline progenitor expansion
  [PMID:22278922 "rsks-1 (S6K) acts downstream of let-363 (TOR) and daf -15 (RAPTOR) for proper larval expansion of the germline progenitor pool"].
- Used as the canonical TORC1 output in a sphingolipid-TORC1 postembryonic development pathway
  [PMID:23705068 "we used RNAi to knock down C. elegans orthologs of elf4E (ife-2) and p70S6K(rsks-1), two well-known downstream targets of TORC1"].
- Translation: rsks-1 and ife-2 promote protein biosynthesis but are not required for
  completion of larval development [PMID:18804378 "rsks-1/S6 kinase and ife-2/eIF4E each promoted protein biosynthesis, but neither was necessary to complete larval development or to localize FIB-1"].

## Lifespan and stress

- Loss of S6K extends lifespan [PMID:17266679 "reducing the levels of ribosomal proteins, ribosomal-protein S6 kinase or translation-initiation factors increases the lifespan of Caenorhabditis elegans"];
  [PMID:17266680 "rsks-1, the worm homologue of S6 kinase, results in lifespan extension in Caenorhabditis elegans"].
- Lifespan extension of rsks-1 requires pha-4/FoxA [PMID:18804378 "We observed a ~10% extension in lifespan for rsks-1(ok1255) in 4/4 experiments"].
- rsks-1 mutation extends lifespan; raga-1 further extends it [PMID:20523893 "rsks-1mutation produced a moderate increase in lifespan compared to wild-type (Figure S7)"].
- HSF-1 mediates rsks-1 longevity [PMID:23879233 "mediates the prolonged lifespan conferred by mutations in C. elegans S6K (rsks-1)"].
- daf-2; rsks-1 synergistic longevity via germline signalling and AAK-2 (PMID:24332851).
- A NOT lifespan annotation from the ife-2 paper (PMID:17277769) could not be checked; the
  abstract does not discuss rsks-1.

## Autophagy

- Adult RNAi of rsks-1 reduced LGG-1 autophagic puncta
  [PMID:22560223 "autophagy was reduced by knockdown of the S6 kinase RSKS-1, which increases translation downstream of TORC1 but also promotes autophagy"].
  UniProt's text ("RNAi-mediated knockdown in adults causes increase in lgg-1 positive
  autophagic vesicles"; "Negatively regulates autophagy") states the opposite direction from
  the paper; this appears to be a UniProt curation error.
- Sheaffer et al. note rsks-1 mutants do not show increased autophagy
  [PMID:18804378 "Neither ife-2/eIF4E nor rsks-1/S6K mutants have increased autophagy, yet they extend longevity"].

## Development, germline, neurons

- Germline: required germline-autonomously for larval accumulation of germline progenitors
  [PMID:22278922 "rsks-1 (S6K) is required germline-autonomously for larval accumulation of germline progenitors, promoting both cell cycle progression and the proliferative fate"].
- Larval development: rsks-1 mutations suppress pha-4 larval lethality
  [PMID:18804378 "rsks-1/S6 kinase mutations, but not ife-2/eIF4E, can suppress pha-4-associated larval lethality"].
- Axon regeneration: cell-autonomous inhibitor of axon regrowth acting via AAK-2/AMPK
  [PMID:24431434 "we have identified the ribosomal S6 kinase RSKS-1 as a new cell-autonomous inhibitor of axon regeneration"].
  Localized to axon and perikaryon of touch neurons, enriched in the PLM synaptic branch (UniProt SUBCELLULAR LOCATION, PMID:24431434).
