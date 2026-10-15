# STE7 (YDL159W, UniProt P06784) curation notes

## Identity
- Ste7, 515 aa, protein kinase domain 191-466; STE Ser/Thr kinase family, MAP kinase kinase subfamily
  (UniProt). PANTHER PTHR48013:SF9 (MAP2K family). Activation-loop Ser359/Thr363 phosphorylated; S359A
  and T363A are inactive [file:yeast/STE7/STE7-uniprot.txt, MUTAGEN features citing PMID:8131746].

## Molecular function: MAP kinase kinase (MAP2K/MEK)
- Dual-specificity kinase that phosphorylates Fus3 on its activation-loop Thr/Tyr and activates it
  [PMID:8384702 "Here we report that STE7 is a dual-specificity kinase that modifies FUS3 at the
  appropriate sites and stimulates its catalytic activity in vitro."].
- In vitro reconstituted cascade: Ste11 -> Ste7 -> Fus3 [PMID:8159759 "reconstituted a kinase cascade in
  which STE11 phosphorylates and activates STE7, which in turn phosphorylates the mitogen-activated
  protein kinase FUS3"]; Ste11-dependent phosphosite required for Ste7 activity [PMID:8159759].
- Pheromone activates Ste7 independently of Fus3/Kss1; Ste7 activation precedes MAPK modification
  [PMID:8455599 "Using in vitro assays for FUS3 phosphorylation, we show that pheromone activates STE7
  even in the absence of FUS3 and KSS1."].
- High-affinity docking of Kss1 and Fus3 to Ste7 (Kd ~5 nM), independent of catalytic core; Hog1, Mpk1
  and Erk2 do not bind; docking-region deletions reduce signaling [PMID:8668180].
- Substrate selectivity: Kss1 is intrinsically a good Ste7 substrate, Fus3 a poor one; the Ste5
  minimal-scaffold (VWA) domain binds Ste7 tightly and "unlocks" Fus3 (~5000-fold kcat increase)
  [PMID:19303851 "We find that Fus3 is intrinsically a poor substrate for activated Ste7, while Kss1 is
  intrinsically a very good substrate."]. Conserved across Fus3 orthologs [PMID:23953117].
- Reciprocal feedback: Fus3/Kss1 phosphorylate Ste7 (hyperphosphorylation) [PMID:8455599,
  PMID:15456892]; feedback phosphorylation does not attenuate Ste7 kinase activity [PMID:15456892].
- GO: GO:0004708 MAP kinase kinase activity (is_a GO:0004712 protein Ser/Thr/Tyr kinase activity).
  Rhea-based IEAs for Tyr kinase (true: Tyr of TEY/TXY motif) and Ser kinase (no evidence of physiological
  Ser phosphorylation; treated as over-annotation from the EC 2.7.12.2 reaction set).

## Pathways
- Pheromone response MAPK cascade (Ste20-Ste11-Ste7-Fus3/Kss1 on the Ste5 scaffold) [PMID:8455599,
  PMID:8668180, PMID:8062390, PMID:7851759].
- Filamentous/invasive growth pathway: Ste7 -> Kss1, Ste5-independent [PMID:9363895 "We show instead that
  Kss1 is the principal target of Ste7 in the invasive-growth response in both haploids and diploids."];
  haploid invasive growth and diploid pseudohyphal growth require STE7 [PMID:8001818, PMID:8643578].
- Constitutive Ste7 activates Kss1 but not Fus3 in vivo, driving invasion but not mating [PMID:15456892].
- Glycosylation-defect response: a Sho1 -> Ste20/Ste50 -> Ste11 -> Ste7 -> Kss1 -> Ste12 pathway activates
  FUS1 and contributes to cell wall integrity [PMID:10880465]. GO:0000196 "cell integrity MAPK cascade"
  is defined as the Slt2-containing cascade; Ste7 is not a tier of that cascade, so the annotation is a
  term mismatch (MODIFY to generic MAPK cascade).

## Localization
- Predominantly cytoplasmic; localizes to mating projection tips in pheromone-treated cells
  [PMID:11781566 "Ste5p, Ste7p and Fus3p also localized to tips of mating projections in pheromone-treated
  cells."]; Fus3-activating kinases partitioned to shmoo tip [PMID:17952059].

## Interactions (GO:0005515 rows)
- Kss1/Fus3: direct high-affinity docking (PMID:8668180) plus Y2H/AP-MS -> MODIFY to GO:0051019
  mitogen-activated protein kinase binding.
- Ste5: scaffold binding (PMID:8062390, PMID:7851759, PMID:9311911, PMID:19303851) -> MODIFY to
  GO:0097110 scaffold protein binding.
- Hog1 (AP-MS, PMID:20489023): Bardwell 1996 found no detectable Hog1-Ste7 association in vitro; Hog1 is
  activated by Pbs2 not Ste7 -> REMOVE (uninformative; not asserting the co-purification is false).
- Cdc14 (AP-MS, PMID:20489023): no functional consequence for Ste7 established in cached text -> REMOVE.

## Other regulation (deep research, not in GOA)
- Pheromone-dependent Ste7 polyubiquitination regulated by Ubp3 (Wang & Dohlman 2002, JBC) [cited via
  file:yeast/STE7/STE7-deep-research-falcon.md; not fetched].
