# SERK2 (At1g34210, UniProt Q9XIC7) - manual literature synthesis

No deep-research API was available; this synthesis was written by hand from the cached
publications in `publications/` and PubMed searches. Quotes are verbatim from the cached text.

## Identity and architecture

- SOMATIC EMBRYOGENESIS RECEPTOR KINASE 2, one of five SERK LRR receptor-like kinases (LRR-RLK II)
  in Arabidopsis; 90% identical to SERK1 [PMID:27920157 "The primary amino acid sequences of SERK1 and SERK2 share 90% identity"].
- Signal peptide 1-29, short LRR ectodomain (4 LRRs plus an N-terminal LRR cap), single TM helix 242-262,
  cytoplasmic Ser/Thr kinase domain 305-592 with ATP-binding lysine (K333) and catalytic Asp432
  (UniProt Q9XIC7 FT lines).
- Plasma membrane, single-pass type I [UniProt CC SUBCELLULAR LOCATION, ECO:0000269 PMID:16284305].

## Kinase activity

- Kinase domain autophosphorylates in vitro, with intermediate activity among the SERKs
  [PMID:19105183 "Differences in autophosphorylation that ranged from high activity of SERK1,
  intermediate activities for SERK2 and SERK3 to low activity for SERK5 were noted"] (abstract-only).
- SERK2 cytoplasmic domain autophosphorylates and transphosphorylates with the EMS1 kinase domain
  [PMID:27920157 "Phosphorylation levels of EMS1-CD, SERK1-CD, and SERK2-CD were enhanced significantly
  when EMS1-CD was incubated with SERK1-CD or SERK2-CD"].
- Kinase-dead mSERK2 (K333E) is dominant negative in bri1-5 [PMID:22253607 "Overexpression of
  kinase-inactive mutants, mSERK1 (K330E), mSERK2 (K333E), mBAK1 (K317E), and mBKK1 (K322E) dramatically
  enhances bri1-5 defective phenotypes."].

## Co-receptor roles (ligand-induced heteromerisation with LRR receptor kinases)

- EMS1/TPD1 (anther tapetum specification): SERK1/2 act redundantly as co-receptors of EMS1
  [PMID:27920157 "Here, we show that SERK1 (SOMATIC EMBRYOGENESIS RECEPTOR-LIKE KINASE1) and SERK2 LRR-RLKs
  act redundantly as coregulatory and physical partners of EMS1."].
- ERECTA family (stomatal patterning): EPF2 induces ER-SERK2 association; SERK2 is the second most
  important SERK in stomatal patterning after BAK1 [PMID:26320950 "Importantly, EPF2 induced the association
  of ER with SERK1, SERK2, BAK1 and SERK4 (Figure 5B)"; "with descending order of importance from BAK1,
  SERK2, SERK1 to SERK4"]. TMM also co-immunoprecipitates SERK2.
- PSKR1 (phytosulfokine): crystal structure of PSKR-PSK-SERK complex; PSK enhances PSKR-SERK heterodimerisation
  [PMID:26308901] (abstract-only).
- RGF receptors RGFR1-5 (root meristem growth) [PMID:27229311 "We also offer evidence showing that SERKs
  function as co-receptors for RGFs."] (abstract-only).
- PXY/TDR (TDIF/CLE41, vascular development): PXY-TDIF-SERK2 crystal structure [PMID:27449136
  "Crystal structure of the PXY-TDIF-SERK2 complex reveals that the last amino acid of TDIF conserved
  among CLEs and other evolutionary-related peptides is important for the interaction between SERK2 and PXY."]
  (abstract-only).
- BRI1 (brassinosteroid): SERK2 interacts only weakly with BRI1 and contributes little under normal conditions
  [PMID:22253607 "These results suggest that SERK2 may have fewer roles in BR signaling compared to the other
  three SERKs, but unnatural manipulation such as overexpression of SERK2 and exogenous application of BR can
  reveal its functions in BR signaling."]. serk2 bak1-5 and serk1 serk2 bak1-5 seedlings are BR-sensitive
  [PMID:26320950].

## Genetics

- serk2 single mutants have no visible phenotype; serk1 serk2 double mutants are male sterile because the
  tapetum is not specified [PMID:16284305; PMID:16284306 "Further confocal microscopic and molecular analyses
  showed that serk1 serk2 double mutant anthers lack development of the tapetal cell layer, which accounts for
  the microspore abortion and male sterility."].
- SERK members are redundant in pairs, which differ by pathway [PMID:18667726].
- The serk1 serk2 bak1 bkk1 quadruple mutant is embryo lethal [PMID:22253607].

## Ectodomain interaction screens

- SERK2 ectodomain binds many LRR-RK ectodomains in high-throughput screens (PMID:29320478, PMID:30806640);
  these produce the bare protein-binding GOA rows.
