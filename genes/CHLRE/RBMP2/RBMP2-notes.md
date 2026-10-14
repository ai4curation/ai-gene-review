# RBMP2 (Cre09.g416850; UniProt A0A2K3DG19) notes

## Deep research

Not run. The falcon provider returned HTTP 402 and perplexity was unavailable in this
session, so this review rests on the cached primary literature, a PubMed search, and a
local sequence analysis (`RBMP2-bioinformatics/`). No `-deep-research-*.md` file exists.

## Identity and record

- UniProt A0A2K3DG19 is an unreviewed TrEMBL entry, "Rhodanese domain-containing
  protein", 1690 aa, ORF CHLRE_09g416850v5. Its only feature annotations are a PROSITE
  PS50206 rhodanese domain (775-920) and MobiDB disordered regions. PANTHER places it in
  PTHR24216 ("paxillin-related"), which looks like a low-complexity artefact rather than a
  meaningful family call.
- GOA has 0 annotations for this protein.
- Named by Meyer et al. 2020. [PMID:33177094 "The proteins we named Rubisco-binding membrane proteins RBMP1 (Cre06.g261750) and RBMP2 (Cre09.g416850) have predicted transmembrane domains and were previously found to bind to Rubisco"]
- PubMed search "RBMP2 AND (pyrenoid OR Chlamydomonas)" (Oct 2026) returned one hit,
  the functional preprint PMID:42427617, which was then cached.

## Domain architecture

- Wu et al. 2026: [PMID:42427617 "RBMP2 contains an N-terminal region with predicted membrane-contact probability (MCP)33, a central non-catalytic rhodanese domain (RHO), predicted transmembrane helices (TM) on both sides of the RHO domain and six C-terminal Rubisco-binding motifs (RBMs)27"]
- Six RBMs, consistent with a review. [PMID:35961043 "RBMP2 is considerably larger (165 kDa) and contains a long stromal C-terminal region with six RBMs."]
- Local check (file:CHLRE/RBMP2/RBMP2-bioinformatics/RESULTS.md): six matches to the
  [D/N]W[R/K]XX[L/I/V/A] consensus at 1126, 1265, 1345, 1592, 1638 and 1685 (the last at the
  exact C-terminus, ending in Val). Hydrophobic segments at 684-714 (strong) and 961-981
  (weaker) flank the rhodanese domain.

### Rhodanese domain: non-catalytic

- The whole protein has a single cysteine (Cys498, in the low-complexity N-terminal half).
  The rhodanese domain (775-920) has none. A crude loop scan puts Asp870 (`DSYGVE`) in the
  position of the catalytic cysteine.
- Wu et al.'s alignment agrees. [PMID:42427617 "The catalytic cysteine residue is marked in green, and the non-catalytic aspartic acid residue in RBMP2 is marked in grey."]
- Consequence: no sulfurtransferase (thiosulfate-cyanide sulfurtransferase) or
  CDC25-like phosphatase activity can be inferred. The InterPro rhodanese hit should not
  be turned into an MF annotation by any pipeline. Its role is structural or interaction
  based. [PMID:42427617 "A notable finding of this work is that a non-catalytic rhodanese domain can influence membrane morphology"]

## Localization

- Pyrenoid tubules, Venus fusion. [PMID:33177094 "Fluorescently tagged RBMP1 and RBMP2 localized to the tubules"]
- Central reticulated region, unlike RBMP1. [PMID:33177094 "Our microscopy data suggest that RBMP2 is confined to the central reticulated region of the tubules"]
- Confirmed with expansion microscopy, and the region expands on overexpression. [PMID:42427617 "In wild-type cells overexpressing RBMP2-Venus, we observed by ExM that RBMP2-Venus localized throughout an enlarged reticulated region (Fig. 2g)."]
- PMID:42465278 (ExM of pyrenoid membranes) does not mention RBMP2. It shows CAH3
  concentrated in the reticulated region. [PMID:42465278 "notably suggesting a role for the central reticulated region in localizing the essential CO2-delivering carbonic anhydrase CAH3"]

## Rubisco binding

- AP-MS (Meyer's ref 18). [PMID:33177094 "SAGA2, RBMP1, RBMP2, and CSP41A by affinity purification–mass spectrometry (18)"]
  The cached text of PMID:28938113 (the spatial interactome, presumably ref 18) does not
  name RBMP2 or its locus, so I did not use it as support.
- Peptide arrays tiling RBMP2 were probed with Rubisco. [PMID:33177094 "Arrays of 18–amino acid peptides tiling across the sequences of SAGA2 (B) and RBMP2 (C) were synthesized and probed with Rubisco."]
- The SAGA1 antibody did not detect RBMP2 on blots, which the authors put down to its
  C-terminal Val.
- GO has no Rubisco-binding MF term, and "protein binding" is uninformative, so no MF was
  made from this.

## Tether hypothesis vs membrane shaping

- Original model: RBMs on RBMP1/RBMP2 recruit Rubisco to the tubules. [PMID:33177094 "the presence of the same motif on the pyrenoid tubule-localized transmembrane proteins, RBMP1 and RBMP2, recruits Rubisco to the tubules and favors assembly of the matrix around them"]
- RBMP1/BST4 was later shown not to be needed for tubule-matrix contact. The paper raises
  redundancy in general terms but does not name RBMP2. [PMID:39240724 "Collectively, these data indicate that BST4 may require a preexisting pyrenoid tubule network to be localized in the pyrenoid rather than driving the inclusion of thylakoid membranes into the Rubisco matrix or is redundant as a tether protein."]
- Wu et al. 2026 (bioRxiv, not yet peer reviewed) is the first functional study of RBMP2:
  - Null phenotype: [PMID:42427617 "We show that RBMP2 loss eliminates this central reticulated membrane network, mislocalizes CAH3 and impairs growth under very low CO2."]
  - Rescue: [PMID:42427617 "We conclude that RBMP2 is required for normal CAH3 localization and for maintaining pyrenoid function under strongly CO2-limiting conditions."]
  - Tubules still enter the matrix without RBMP2, so it is not needed for the
    tubule-matrix interface as such. [PMID:42427617 "In the rbmp2 mutant, cylindrical tubules still extended from the pyrenoid periphery toward the center, but we never observed them forming a reticulated network"]
  - Overexpression is sufficient to enlarge the region. [PMID:42427617 "Thus, RBMP2 is not only required for reticulated-region formation; overexpressing the RBMP2 protein is sufficient to promote the expansion of the reticulated region in wild-type cells."]
  - Rhodanese domain: [PMID:42427617 "These results suggest that the RHO domain performs an essential and upstream function in reticulated-region biogenesis, likely promoting extension of the tubules."]
  - MCP and TM: [PMID:42427617 "MCP and TM domains are not required for cylindrical tubule elongation. Instead, they are required to convert elongated cylindrical tubules into reticulated-region tubules."]
  - RBMs dispensable: [PMID:42427617 "These results suggest that the RBMs are dispensable for detectable reticulated-region formation, although they may still contribute to RBMP2 function in ways not resolved by these assays."]
  - LCI16 binds (IP, AlphaFold model with the rhodanese domain) but is not needed. [PMID:42427617 "However, the presence of a normal reticulated region in the lci16 mutant38 suggests that LCI16 is not essential for reticulated-region biogenesis."]
- Conclusion: RBMP2 is a membrane-shaping factor for the CAH3-hosting reticulated region,
  not an established tether. A tether contribution by its RBMs, redundant with other RBM
  proteins, is still untested.

## GO decisions

- NEW CC GO:0160223 pyrenoid tubule (IDA, PMID:33177094; also PMID:42427617).
- NEW BP GO:0010027 thylakoid membrane organization (IMP, PMID:42427617). This passes the
  participation test: RBMP2 is in the remodelled membrane, its MCP/TM regions are needed
  for the shape change, and overexpression enlarges the region. It matches the term used
  for SAGA1 and MITH1. GO:0097749 membrane tubulation was considered, but the tubules
  form without RBMP2, so it is not the tubulation factor. What RBMP2 does is extend them
  and convert them into the reticulated region.
- No MF asserted. GO:0180020 membrane bending activity is the candidate if bending is
  shown in vitro. GO:0043495 protein-membrane adaptor activity (used for SAGA1/MITH1) is
  not supported, because the RBMs are dispensable. Sulfurtransferase or phosphatase
  activity is excluded on sequence grounds.

## Module (pyrenoid_ccm, node tubule_matrix_tethering)

- Proposed annoton: participant UniProtKB:A0A2K3DG19; function given as free text
  only (no GO id; "membrane-shaping protein, activity unknown"); process GO:0010027;
  location GO:0160223. The role is to build the reticulated region that positions CAH3.
  The node text "RBMP2 ... untested" should be updated: RBMP2 has now been tested and
  shapes membranes rather than tethering them.
