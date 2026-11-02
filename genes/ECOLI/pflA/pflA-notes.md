# pflA (P0A9N4) notes

Part of the RADICAL_SAM project (projects/RADICAL_SAM.md), Phase 2 E. coli K-12.

## Literature sources

No deep-research file is available for this gene: the falcon provider fails authentication
(403) and asta returned nothing useful in Phase 1, so deep research was not run. These notes are
built from cached publications (`publications/PMID_*.md`), the UniProt record, PubMed and
QuickGO. The Knappe-lab papers are abstract-only in the cache; PMID:19711960, PMID:24016774 and
PMID:28768413 (Broderick lab) have full text.

## Identity and family

- Pyruvate formate-lyase 1-activating enzyme (PFL-AE, PFL activase, PflA; 246 aa, Met1
  removed), EC 1.97.1.4. Founding member of the organic radical-activating enzyme family of
  the radical SAM superfamily; paralogs NrdG, PflC, YbiY, YjjW.
  [file:ECOLI/pflA/pflA-uniprot.txt "Activation of pyruvate formate-lyase 1 under anaerobic conditions by generation of an organic free radical, using S-adenosylmethionine and reduced flavodoxin as cosubstrates to produce 5'-deoxy-adenosine."]

## Activity

- Active PFL (Ea) is formed from inactive PFL (Ei) post-translationally by a distinct
  activating enzyme, coupled to SAM cleavage to methionine and 5'-deoxyadenosine.
  [PMID:6364987 "The catalytically active form (Ea) of pyruvate formate-lyase in Escherichia coli cells is generated from an inactive form of the enzyme (Ei) through a post-translational process that requires a distinct activating enzyme and is linked to the cleavage of adenosylmethionine to methionine and 5'-deoxyadenosine."]
- Radical is on PflB Gly734. [PMID:1310545 "The N-terminal block on the small fragment was identified by mass spectrometry as an oxalyl residue that derives from Gly-734, thus assigning the primary structural glycyl radical position."]
- Mechanism: 5'-dAdo radical abstracts the pro-S H of Gly734; dihydroflavodoxin is the
  physiological reductant; heptapeptide RVSGYAV (PflB 731-737) is a substrate.
  [PMID:8175649 "Our results show that the radical in pyruvate formatelyase is produced by stereospecific abstraction of the pro-S hydrogen of glycine 734 by the 5'-dAdo radical generated in the active center of PFL activase."]
- Flavodoxin (FldA) binds PFL-AE only in its FMN-bound holo form.
  [PMID:24016774 "Holo-Fld is capable of associating with NADP(+)-dependent flavodoxin oxidoreductase (FNR) and pyruvate formate-lyase activating enzyme (PFL-AE) whereas there is no detectable interaction between apo-Fld and either protein."]
- Structure (Vey 2008): substrate-free and peptide-bound PFL-AE, first activase structures.
  [PMID:18852451 "Pyruvate formate-lyase activating enzyme generates a stable and catalytically essential glycyl radical on G(734) of pyruvate formate-lyase via the direct, stereospecific abstraction of a hydrogen atom from pyruvate formate-lyase."]

## Cofactors

- [4Fe-4S] cluster; Cys29/33/36 (mature numbering; Cys30/34/37 in UniProt) essential;
  cluster required for SAM binding.
  [PMID:9478932 "Cys --> Ser replacements by site-directed mutagenesis determined Cys-29, Cys-33, and Cys-36 to be essential to yield active holoenzyme."]
  [PMID:9478932 "The iron-sulfur cluster complement proved to be a prerequisite for effective binding of adenosylmethionine"]
- Cluster interconverts in vivo with O2 status; only [4Fe-4S]+ is active.
  [PMID:19711960 "Purified PFL-AE contains an oxygen-sensitive, labile [4Fe-4S] cluster that undergoes cluster interconversions in vitro, with only the [4Fe-4S](+) cluster state being catalytically active."]
- Catalytically essential monovalent cation site, liganded by a SAM carboxylate oxygen;
  activity maximal with K+.
  [PMID:28768413 "We show that PFL-AE binds a catalytically essential monovalent cation at its active site"]

## Location

- Cytosol by fractionation proteomics (PMID:15911532; abstract-only).

## Processes

- GO has no glycyl radical formation term; PAINT places GO:0018201 peptidyl-glycine
  modification and GO:0051604 protein maturation on the PflA node, and PflA has both by IDA.
  PflA performs the modification, so these pass the participation test.
- GOA carries no pyruvate fermentation / mixed-acid fermentation term for PflA, consistent with
  the activase being upstream of PflB's catalysis. No NEW downstream process is proposed.
- DNA damage response (IEP, PMID:11967071): genome-wide mitomycin C microarray; the abstract
  does not mention pflA. Expression change, not participation.

## Decisions

- Core MF: GO:0043365 (ACCEPT), GO:0051539 (ACCEPT), NEW GO:1904047 (IDA PMID:9478932).
- Core BP: GO:0018201 + GO:0051604 (ACCEPT).
- Generic rows per RADICAL_SAM rule (GO:0003824, GO:0016491, GO:0043364 → MODIFY to
  GO:0043365; GO:0051536 → GO:0051539).
