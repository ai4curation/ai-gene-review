# PTK2B / Pyk2 (Q14289) review notes

## Literature search (2026-11-04)

No deep-research provider was available, so the search was by hand:
- Cached all 30 GOA-cited PMIDs (`just fetch-gene-pmids human PTK2B`).
- Read the UniProt FUNCTION, ACTIVITY REGULATION, SUBUNIT and SUBCELLULAR LOCATION sections.
- Most GOA papers are abstract-only; full text available for PMID:25707991 and PMID:38844957.

## Key points

- Core activity is non-receptor tyrosine kinase, EC 2.7.10.2, autophosphorylating at Tyr402
  [file:human/PTK2B/PTK2B-uniprot.txt "Activated by autophosphorylation at Tyr-402"].
- Ca2+ activation is indirect [file UniProt "this activation is indirect and may be mediated by
  calcium-mediated production of reactive oxygen species (ROS)"].
- Mechanism: pTyr402 recruits SRC SH2 [PMID:8849729 "binding of the SH2 domain of Src to tyrosine
  402 of Pyk2 and activation of Src"].

## Notable decisions

- GO:0004683 calcium/calmodulin-dependent protein kinase activity (ISS from rat P70600): REMOVE.
  Pyk2 is a tyrosine kinase; GO:0004683 is a Ser/Thr CaM-kinase term. The rat names
  "calcium-dependent tyrosine kinase / cell adhesion kinase beta" were likely mis-mapped to a
  CaM-kinase term. The correct activity is GO:0004715.
- GO:0004715 TAS (PMID:8497321): the cited paper (Manser 1993) describes a hippocampal kinase that
  binds GTP-Cdc42 via an SH3-adjacent sequence -- that is ACK/TNK2, not Pyk2 (no SH3 domain,
  [PMID:7499242 "lacks ... SH2 and SH3 domains"]). Term ACCEPTed on other evidence; reference
  flagged as probable mis-citation in reference_review.
- GO:0042976 activation of Janus kinase activity (IMP, PMID:8670418): UNDECIDED. The paper is about
  c-Jun N-terminal kinase (JNK), not Janus kinase (JAK) -- possible term confusion. Covered by the
  JNK cascade row instead.
- GO:0030546 signaling receptor activator activity (ISS): MARK_AS_OVER_ANNOTATED -- Pyk2 regulates
  NMDA receptors indirectly via Src, it is not a receptor ligand/activator.
- ~18 bare protein-binding IPI rows: REMOVE per policy, except SRC/SRC-family and FYN rows, which
  MODIFY to GO:0019901 protein kinase binding (the pTyr402-Src SH2 mechanism is informative).

## Module / GO-CAM context

The module `calmodulin_camkii_stat1_potentiation` keeps Pyk2 as an optional, inhibitor-only relay:
the only evidence placing Pyk2 in the interferon-STAT1 branch is that the Pyk2 inhibitor Tyrphostin
A9 blocks STAT1 phosphorylation (PMID:35568036), with no genetic test. This review likewise does not
assert any interferon-pathway annotation for PTK2B; recorded as a knowledge gap and a suggested
experiment. The STAT3 binding seen in lung cancer (PMID:38844957) is unrelated to the STAT1 branch.
