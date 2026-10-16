# mad3 (S. pombe, UniProt O59767, PomBase SPCC1795.01c) - curation notes

Working notes for the GO annotation review. Inline citations quote the cached
publication text verbatim where it is available.

## Identity

- Fission-yeast Mad3, the BubR1/Mad3-family spindle assembly checkpoint (SAC)
  protein; 310 aa, ~36 kDa; ORF aliases SPCC1795.01c and SPCC895.02. Not the
  S. cerevisiae MAD3 (P47074), which is the comparator review in this repository.
- Domain architecture (UniProt): BUB1 N-terminal / Mad3_BUB1_I TPR-like domain
  (residues 56-218; crystallised as residues 1-223 in PDB 4AEZ), disordered region
  20-63, no kinase domain. Two conserved KEN boxes, KEN20 (KEN1) and KEN271
  (KEN2), and C-terminal ABBA/D-box-like motifs (deep research, Sewart and Hauf
  2017).
- Unlike budding-yeast Mad3 and metazoan BubR1, S. pombe Mad3 has no GLEBS motif
  and does not bind Bub3 stably [PMID:18556659 "S. pombe Mad3 lacks the GLEBS
  motif that is necessary and sufficient for Saccharomyces cerevisiae Mad3 to bind
  Bub3 (37)"; PMID:31257143 "SpMad3 interacts with kinetochores in a
  Bub1-dependent fashion, but SpMad3 lacks a Bub3 binding domain of its own [36,
  42]."]. The fission-yeast MCC is therefore Mad3-Mad2-Slp1 [PMID:18556659 "Mad3
  is part of the MCC, which in fission yeast is comprised exclusively of Mad3,
  Mad2, and Cdc20."]. The task brief describes the MCC as including Bub3; that is
  true of the budding-yeast and human complexes but not of the S. pombe one, and
  the review follows the primary literature on this point.

## Function: MCC subunit that inhibits APC/C-Slp1

- Founding paper (Millband and Hardwick 2002; abstract + discussion cached only):
  mad3 delta is checkpoint-null but viable [PMID:11909965 "We have identified the
  fission yeast mad3 + gene and found it to be nonessential for normal cell
  division, but required for spindle checkpoint function."]; phenotypes:
  benomyl hypersensitivity, minichromosome loss, rereplication, precocious sister
  separation [PMID:11909965 "Cells deleted for mad3 + are hypersensitive to
  microtubule poisons such as benomyl, have elevated levels of minichromosome loss
  rates, and rereplicate their DNA when spindle function is compromised."].
- Mad3 co-IPs Bub3, Mad2 and Slp1 [PMID:11909965 "Mad3p coimmunoprecipitates
  Bub3p, Mad2p, and the spindle checkpoint effector Slp1/Cdc20p."] and is the only
  checkpoint protein required for the Mad2-overexpression arrest [PMID:11909965
  "We demonstrate that Mad3p function is required for the overexpression of Mad2p
  to result in a metaphase arrest. Mad1p, Bub1p, and Bub3p are not required for
  this arrest."]. Deep research: ~70% arrest in wild type vs 8% in mad3 delta.
- Sczaniecka et al. 2008 (full text cached): Lid1(Apc4)-TAP from nda3-arrested
  cells recovers Mad3, Mad2 and Slp1; sucrose-gradient co-fractionation
  [PMID:18556659 "Pools of Mad2, Mad3-GFP, and Cdc20/Slp1-HA were seen to
  co-fractionate with Lid1-TAP (Fig. 2C)."]; APC/C binding requires Slp1, Mad2 and
  KEN20 [PMID:18556659 "Thus, Mad3 is dependent on its own N-terminal KEN box,
  Mad2, and Cdc20 for APC/C association."]; KEN mutants are checkpoint-null
  [PMID:18556659 "Both KEN mutants behaved like the mad3Δ strain in this assay;
  cells failed to arrest with condensed chromosomes, mis-segregated their DNA,
  displayed the cut (cells untimely torn) phenotype (Fig. 5A), and lost viability
  rapidly after 3 h at 18 °C (Fig. 5B)."]. MCC and MCC-APC/C form every mitosis
  in the nucleoplasm, independently of Bub1/Bub3/Mph1/Mad1 and kinetochore
  targeting [PMID:18556659 "We propose that MCC formation and APC/C binding take
  place in the nucleoplasm every mitosis, independently of kinetochore-based SAC
  signaling."], but such complexes made in upstream mutants cannot arrest cells,
  implying kinetochore-dependent modifications are needed.
- Chao et al. 2012 (abstract cached): 2.3 A crystal structure of the S. pombe MCC
  (PDB 4AEZ) [PMID:22437499 "The MCC inhibits the APC/C by obstructing degron
  recognition sites on Cdc20 (the substrate recruitment subunit of the APC/C) and
  displacing Cdc20 to disrupt formation of a bipartite D-box receptor with the
  APC/C subunit Apc10."; "Mad2, in the closed conformation (C-Mad2), stabilizes
  the complex by optimally positioning the Mad3 KEN-box degron to bind Cdc20."].
- Zich et al. 2016 (full text cached): Mad3 is an Mph1 substrate; C-terminal
  phospho-sites flanking KEN2 (mad3-C9A) are dispensable for kinetochore targeting
  and MCC assembly but needed for stable APC/C binding and arrest maintenance
  [PMID:26882497 "We conclude that reduced phosphorylation of either Mad3p or Mad2p
  impairs maintenance of a checkpoint arrest, and that reduced phosphorylation of
  both proteins further reduces their ability to maintain a robust checkpoint
  response."]. Reconstituted APC/C assay: recombinant Mad3 inhibits Cut2
  ubiquitination; phosphomimetics are more potent [PMID:26882497 "These
  experiments demonstrate that the Mad3 phosphomimics are better in vitro APC/C
  inhibitors than the recombinant wild-type Mad3 protein and that they display a
  graded increase in potency (c.f. 0,3,4 and 7 phospho-mimicking D/E residues)."].
  This is the basis of the GO:1990948 ubiquitin ligase inhibitor activity IDA.

## Kinetochore recruitment

- Mad3-GFP goes to unattached kinetochores early in mitosis and accumulates on
  prolonged arrest; recruitment needs Bub1, Bub3 and Mph1 but not Mad1/Mad2
  [PMID:11909965 "We find Mad3-GFP kinetochore localization to be dependent upon
  Bub1p, Bub3p, and the Mph1p kinase, but not upon Mad1p or Mad2p."].
- Upstream: Mph1 phosphorylates Spc7 (KNL1) MELT motifs to recruit Bub1-Bub3,
  which is required for Mad1-Mad2-Mad3 localisation [PMID:22660415 "This
  phosphorylation promotes the in vitro binding to the Bub1-Bub3 complex, which is
  required for kinetochore-based SAC activation (Mad1-Mad2-Mad3 localization) and
  chromosome alignment."; PMID:22521786 full text].
- Direct Bub1-TPR / Mad3-TPR interaction (Leontiou et al. 2019): the Bub1 TPR is
  necessary and sufficient to recruit Mad3 to a tetO array, independent of Bub3,
  and purified TPR domains form a stable complex [PMID:31257143 "Size exclusion
  chromatography profiles demonstrate that simply mixing the two proteins together
  in vitro was sufficient to produce a stable Bub1-Mad3 TPR complex."]. Synthetic
  Mph1-Bub1 tethering arrests require Mad3 [PMID:31257143 "As was the case for
  Mps1-KNL1Spc7 arrest [21], we found that the Mad1, Mad2, and Mad3 proteins were
  all required for Mph1Mps1-Bub1 arrest."].
- Ark1 (Aurora)/survivin is not needed for Mad3 kinetochore association but is
  needed for Mad2 to form a complex with Mad3 [PMID:12676091 "Ark1/survivin
  function was not required for the association of Bub1 or Mad3 with the
  kinetochores."].

## Localisation

- Nucleus (closed mitosis; kinetochores and nucleoplasmic MCC-APC/C): UniProt
  EXP from PMID:22660415, HDA from the ORFeome screen PMID:16823372, IBA, IEA.
- Kinetochore: two NAS rows cite PMID:15930132 (Saitoh et al. 2005), whose
  cached full text never mentions Mad3 (it studies Mad2/Bub1 loading onto the
  Mis6/Nuf2 complexes). The localisation is correct and directly shown in
  PMID:11909965 and PMID:31257143, so the rows are ACCEPTed with those references
  added and PMID:15930132 flagged MISCITED/LOW relevance in reference_review.
- Cytosol HDA (PMID:16823372): kept as non-core; no cytosolic function is
  described and endogenous Mad3-GFP is nuclear.

## Decisions on the review rows (summary)

- ACCEPT (18): kinetochore NAS x2; nucleus EXP/HDA/IBA/IEA; GO:0007094
  IBA/IEA/IMP x3/NAS; GO:0010997 APC binding IPI (Slp1); GO:0033597 IDA x2 + IPI;
  GO:0045841 IPI; GO:1990948 IDA.
- MODIFY (5): three protein-binding IPIs with Mad2 (O14417) -> GO:0033597 mitotic
  checkpoint complex (same resolution as yeast MAD3 / S. pombe mad2 reviews);
  GO:0032991 IEA -> GO:0033597; GO:0140678 molecular function inhibitor activity
  (contributes_to, from the MCC structure) -> GO:1990948 ubiquitin ligase
  inhibitor activity.
- REMOVE (1): protein binding IPI with Bub1 (SPCC1322.12c, PMID:31257143). The
  interaction is real and important, but on the Mad3 side it is a recruitment
  event without a distinct MF term; the adaptor activity is annotated on the bub1
  review (GO:0030674). Removal does not dispute the interaction.
- KEEP_AS_NON_CORE (1): cytosol HDA.
- No NEW terms proposed. GO:0045841 is an ancestor of GO:0007094 (checked via
  QuickGO), so it adds no coverage but is correct and directly supported.

## Comparators and repository context

- genes/yeast/MAD3 (complete): same core MF (GO:1990948), MCC in_complex, nucleus.
- genes/human/BUB1B (complete): GO:1990948 core function plus a second
  PP2A-B56/KARD kinetochore-adaptor function that S. pombe Mad3 lacks (no KARD
  motif), so only the APC/C-inhibition axis is carried over here.
- modules/metaphase_anaphase_transition_and_mitotic_exit.yaml cites PMID:22437499
  and models the MCC with a BubR1/Mad3 active unit (PTHR14030).
- No GO-CAM in gocams/index.tsv includes O59767 / SPCC1795.01c.

## Papers noted from the deep research but not in the publication cache

- Sewart and Hauf 2017 Curr Biol (doi:10.1016/j.cub.2017.03.007): C-terminal
  KEN2/ABBA/D-box-mimic motifs are dispensable for core MCC assembly but needed for
  full checkpoint activity; proposed engagement of a second Slp1 molecule.
- Iglesias-Romero et al. 2024 BMC Biol; Sun et al. 2024 eLife: Pmk1 MAPK-dependent
  Slp1 turnover under stress, with a reported Mad3 requirement in the former.
  These inform suggested_questions only; nothing in the review depends on them.

## Cache status

Abstract-only: PMID:11909965 (abstract + discussion), PMID:12676091,
PMID:22437499, PMID:22660415, PMID:16823372. Full text: PMID:15930132,
PMID:18556659, PMID:22521786, PMID:26882497, PMID:31257143. No experimental
annotation was removed on the strength of an abstract-only cache.
