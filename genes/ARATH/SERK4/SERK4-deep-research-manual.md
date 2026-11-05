# SERK4 / BKK1 (At2g13790, UniProt Q9SKG5) - manual literature synthesis

No deep-research API was available; this summary was compiled by hand from the
cached publications in `publications/` and the UniProt record. Each claim
carries inline provenance.

## Identity and domain architecture

- SERK4 (synonyms BKK1, BAK1-LIKE 1; BAK7 in Jeong et al. 2010) is one of five
  Arabidopsis SOMATIC EMBRYOGENESIS RECEPTOR KINASEs in LRR-RLK subfamily II
  [PMID:22253607 "The Arabidopsis thaliana somatic embryogenesis receptor kinases (SERKs) consist of five members, SERK1 to SERK5, of the leucine-rich repeat receptor-like kinase subfamily II (LRR-RLK II)"].
- 620 aa: predicted signal peptide (1-33), extracellular domain with plant LRR-N
  cap and five LRRs (34-234), single TM helix (235-255), cytoplasmic protein
  kinase domain (294-591) with active-site Asp421 (UniProt FT lines,
  file:ARATH/SERK4/SERK4-uniprot.txt). PANTHER family PTHR47988.

## Catalytic activity

- Dual-specificity kinase: autophosphorylates on Ser/Thr and Tyr
  [PMID:19124768 "many recognized receptor kinases, including BKK1 ( 19 ), HAESA ( 20 ), and the light-repressible receptor kinase (At3g21340) ( 21 ), all appear to be dual-specificity kinases"];
  UniProt PTM "Autophosphorylated on Thr and Tyr residues" (ECO:0000269 PubMed:19105183, 19124768).
- In vitro autophosphorylation sites mapped for the SERK family kinase domains
  (Karlova et al. 2009, PMID:19105183; abstract only in cache; UniProt records
  Ser295 of SERK4 from this paper).
- Kinase activity is required for its signalling role: kinase-dead mBKK1 (K322E)
  is dominant negative in bri1-5 [PMID:22253607 "Overexpression of kinase-inactive mutants, mSERK1 (K330E), mSERK2 (K333E), mBAK1 (K317E), and mBKK1 (K322E) dramatically enhances bri1-5 defective phenotypes."].

## Biological roles (all as a co-receptor of ligand-binding LRR-RKs)

1. Brassinosteroid signalling (with BRI1). BKK1 is redundant with BAK1
   [PMID:17600708 "BAK1-LIKE 1 (BKK1) functions redundantly with BAK1 in regulating BR signaling"].
   serk1 bak1 bkk1 triple null is BR-blind
   [PMID:22253607 "In a serk1 bak1 bkk1 triple null mutant plant, on the other hand, BR signaling apparently is entirely blocked from BRI1 to BES1"].
   Overexpression of BKK1/BAK7 suppresses bri1 mutants [PMID:20108170; PMID:22253607].
2. Pattern-recognition receptor signalling. Ligand-induced complex with FLS2 and
   EFR; BAK1 and BKK1 cooperate for full PTI and disease resistance
   [PMID:21693696 "BAK1 and BKK1 cooperate genetically to achieve full signaling capability in response to elf18 and flg22 and to the damage-associated molecular pattern AtPep1"].
   Co-receptor of MIK2 for SCOOP phytocytokines
   [PMID:34535661 "BAK1/SERK4 are required for SCOOP-triggered responses, indicating that BAK1/SERK4 are coreceptors of MIK2 in perceiving SCOOPs"].
3. Cell-death control (BR-independent). bak1 bkk1 double null is seedling lethal
   due to spontaneous, light-dependent cell death with constitutive defence
   [PMID:17600708 "bak1 bkk1 double mutants exhibit a seedling-lethality phenotype due to constitutive defense-gene expression, callose deposition, reactive oxygen species (ROS) accumulation, and spontaneous cell death even under sterile growing conditions"];
   [PMID:18667726 "together with SERK4, can mediate cell death control"].
   The cell death is generally interpreted as autoimmunity, possibly through
   guarding of BAK1/BKK1 complexes [PMID:21693696 "the integrity and/or activity of the BAK1/BIR1/BKK1-containing complex(es) is guarded by hypothetical R protein(s)"].
4. Stomatal patterning (minor contributor). EPF2-induced association with ER;
   association with ERL1 and TMM
   [PMID:26320950 "Importantly, EPF2 induced the association of ER with SERK1, SERK2, BAK1 and SERK4 (Figure 5B)"];
   [PMID:26320950 "SERK4 also plays an important but relatively minor role in stomatal development compared to BAK1 and SERK2"].
5. Senescence. BAK7 (SERK4) RNAi lines show early senescence
   [PMID:20108170 "severe growth retardation and early senescence in these lines"].

## Interactions

Large ectodomain interaction screens (PMID:29320478, PMID:30806640) recorded
binding of the SERK4 ectodomain with many LRR-RKs (BIR1, BAK1, SERK1, SERK5,
ERECTA, ERL1/2, NIK1, SUB, IOS1, SRF7...). These are in vitro ECD-ECD assays.

## Localisation

Plasma membrane receptor (signal peptide + TM; UniProt "Cell membrane"; PM IDA by
UniProt from PMID:19616764). The HDA mitochondrion row (PMID:28887381) comes from
a membrane-fraction SEC profiling dataset not designed to assign organelles;
the AtSubP chloroplast prediction conflicts with the secretory signal peptide.
