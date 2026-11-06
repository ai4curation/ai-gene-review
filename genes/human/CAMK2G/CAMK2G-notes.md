# CAMK2G (Q13555) review notes

## Literature search (2026-11-04)

No deep-research provider was available in this environment, so the search was done by hand:

- Cached all GOA-cited PMIDs (`just fetch-gene-pmids human CAMK2G`): 9060999, 9240463,
  15294044, 19946888, 20668654, 22939624, 30184290, 32707033, 33961781, 35271311, 40205054.
- Fetched the papers behind the UniProt record and the STAT1 context: PMID:16690701
  (muscle CaMKII), PMID:14722083 (four-isoform comparison), PMID:11972023 (STAT1 Ser727).
- Web search "gammaCaMKII shuttles Ca2+/CaM to the nucleus CREB" found PMID:25303525
  (Ma et al. 2014 Cell) and the follow-up PMID:29934532 (Cohen et al. 2018 Nat Commun);
  both fetched with full text.

## Findings

- Kinase and CaM binding: all four isoforms are dodecamers; gamma has the highest CaM
  affinity [PMID:14722083 "the rank order of CaM binding affinity (gamma > beta > delta > alpha)"].
- Neurodevelopment: [PMID:30184290 "We found that knockdown of CAMK2G results in inappropriate
  precocious neuronal maturation."] The ID variant p.Arg292Pro is a gain of function.
- CaM shuttle: [PMID:25303525 "whereas γCaMKII operates as a carrier, not as a kinase"];
  [PMID:29934532 "elimination of γCaMKII prevents activity-dependent expression of key genes
  (BDNF, c-Fos, Arc), inhibits persistent synaptic strengthening, and impairs spatial memory in vivo"].
- STAT1: [PMID:11972023 "These results indicate that there is a specific interaction between
  Stat1 and the ubiquitous members of the CaMKII family, i.e., CaMKIIγ/δ."] The GO-CAM built
  from this paper, `gocams/62b4ffe300004489/62b4ffe300004489-src.yaml`, has its kinase node
  (activity 62b4ffe300004580) enabled by CAMK2A (UniProtKB:Q9UQM7). That is recorded in this
  review as a WRONG_GENE_PRODUCT source defect (resource GO_CAM) on the GO:0042501 NEW row. (A
  STAT1 module and GO-CAM review are proposed in ai4curation/ai-gene-review#5904; context only.)

## Decisions

- GO:0004723 calcium-dependent phosphatase (NAS, PMID:9060999): REMOVE; the paper describes
  a kinase and has no phosphatase data. Recorded as a WRONG_TERM source defect (UniProt).
- ER membrane and endocytic vesicle membrane: over-annotated (Reactome compartments of
  the substrate, or an assumed location).
- Calmodulin binding is ACCEPT (core) here, unlike CAMK2A, because of the gamma-specific
  CaM shuttle role.
- NEW: GO:0042501 serine phosphorylation of STAT protein (IDA PMID:11972023), and
  GO:0019722 calcium-mediated signaling (ISS from rodent PMID:25303525).
