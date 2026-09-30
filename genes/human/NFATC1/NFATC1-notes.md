# NFATC1 (human, O95644) review notes

Context: ADAPTIVE_IMMUNITY project, T cell receptor trunk (after LCK, ZAP70, LAT, LCP2, PLCG1).
Framing kept pleiotropic: T cell cytokine genes, osteoclast differentiation, heart valves.

## Sources
- Falcon deep research (`NFATC1-deep-research-falcon.md`, auto-generated; cites reviews without PMIDs, used for background only).
- UniProt O95644; cached publications for all GOA PMIDs (`just fetch-gene-pmids human NFATC1`, 19/19 cached),
  plus PMID:12479813 and PMID:10358178, which were already in the cache.

## Key biology (with provenance)
- Rel homology DNA-binding domain; NMR structure of human NFATC1 DBD on IL2 ARRE2
  [PMID:9506523 "solution structure of the binary complex formed between the core DNA-binding domain of human NFATC1 and the ARRE2 DNA site from the interleukin-2 promoter"].
- Cytoplasmic when phosphorylated; calcineurin dephosphorylation drives nuclear import
  [PMID:16511445 "In resting cells, NFAT proteins are heavily phosphorylated and reside in the cytoplasm"].
- Calcineurin docking via two sites (PxIxIT, LxVP) [PMID:10860980 "second Cn-binding element in NFATc"; PMID:24954618 LxVP peptide binds CnA].
- IL2 [PMID:8202141 "indicating that NF-ATc is required for IL-2 gene expression"].
- Osteoclasts (mouse) [PMID:12479813 "NFATc1 may represent a master switch for regulating terminal differentiation of osteoclasts, functioning downstream of RANKL"];
  PU.1 partner at cathepsin K [PMID:15304486].
- Valves (mouse KO) [PMID:12370307 "Disruption of the NFATc1 gene resulted in embryonic lethality due to aberrant heart valve formation"].
- Chromatin-restricted complexes with JUN, CREB1, ATF1/2/3 [PMID:25609649].

## Decisions
- 66 GOA rows + 2 NEW. Protein binding IPI rows: PPP3CA -> MODIFY to GO:0030346 PP2B binding;
  JUN/ATF1/ATF2/ATF3/CREB1 -> MODIFY to GO:0061629; OGT, HOMER2, HOMER3, DVL1, HOXC13 -> REMOVE (uninformative; NFATC1 is client/substrate).
- FK506 binding (TAS, PMID:8702849) REMOVED: FK506 binds FKBP12; the paper only shows CsA sensitivity.
- Negative regulation of inflammatory response (PMID:35930205) MARK_AS_OVER_ANNOTATED: NFAT dependence shown only with CsA; anti-inflammatory outcome inferred.
- TAS PMID:10821850 is about "NFAT1" (usually NFATC2); accepted since the MF is correct, flagged in reference_review.
- Valve morphogenesis, Wnt repression, VSMC differentiation, p38 binding, nuclear body, intracellular signal transduction -> KEEP_AS_NON_CORE.
- NEW: GO:0030316 osteoclast differentiation (PMID:12479813; TF does the program's work, comparator SPI1 carries GO:0030316 in human GOA);
  GO:0032743 positive regulation of interleukin-2 production (PMID:8202141).
- Core MF: GO:0001228 (activator), GO:0061629 (partner TF binding), GO:0030346 (calcineurin docking).
