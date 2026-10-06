# RBMP1 / BST4 (Cre06.g261750; UniProt A0A2K3DMS8) notes

## Identity

- RBMP1 (Rubisco-binding membrane protein 1) and BST4 (bestrophin-like protein 4)
  are the same gene, Cre06.g261750. [PMID:39240724 "The protein BST4 (bestrophin-like protein 4, also known as Rubisco binding membrane protein 1, RBMP1; Cre06.g261750) localizes exclusively to the pyrenoid tubules"]
- The name RBMP1 was coined by Meyer et al. 2020. [PMID:33177094 "The proteins we named Rubisco-binding membrane proteins RBMP1 (Cre06.g261750) and RBMP2 (Cre09.g416850) have predicted transmembrane domains"]
- UniProt A0A2K3DMS8 is an unreviewed TrEMBL entry ("Uncharacterized protein", 668 aa)
  with InterPro IPR044669 (YneE/VCCN1/2-like), Pfam PF25539 (Bestrophin_2) and PANTHER
  PTHR33281 (UPF0187 protein YneE). The UniProt "Cell membrane" location is an ARBA rule,
  not an observation. Disordered C-terminal regions 437-503 and 546-668 (MobiDB-lite).
- Naming hazard for the CCM project: `projects/CO2_CONCENTRATING_MECHANISMS.md` lists
  RBMP1 and BST4 as two separate genes, and `modules/pyrenoid_ccm.yaml` cites the BST4
  preprint (PMID:38014171) as describing a separate candidate tether. They are one gene.

## Domain architecture

- N-terminal bestrophin channel domain (transmembrane) plus a long disordered C-terminus with
  two Rubisco-binding motifs (RBMs). [PMID:39240724 "BST4 also has a well-conserved bestrophin domain similar to those in the thylakoid-localized BST1-3 proteins (Mukherjee et al. 2019)"]
- Diverged from BST1-3: phenylalanine at the first position of the putative selectivity pore,
  and a separate clade. [PMID:39240724 "Second, BST4 has a phenylalanine residue in the first position of the putative selection pore, as opposed to valine which is conserved throughout BST1-3"]
- Meyer 2020 also called it a predicted bestrophin-family anion channel. [PMID:33177094 "RBMP1 is predicted to be a Ca2+-activated anion channel of the bestrophin family (fig. S2, D and F)"]

## Localization

- Pyrenoid tubules in Chlamydomonas (fluorescent tagging, two independent groups).
  [PMID:33177094 "Fluorescently tagged RBMP1 and RBMP2 localized to the tubules"]
  [PMID:39240724 "indicating that BST4 is located in the tubules and not the Rubisco-enriched pyrenoid matrix"]
- Expansion microscopy places BST4 in a tubule subdomain at an intermediate radius, distinct
  from MITH1 and CAH3. [PMID:42465278 "The distribution of the transmembrane BST438,39 occupied an intermediate radial distribution"] (bioRxiv preprint)
- In Arabidopsis expression, BST4 sits in stroma lamellae thylakoids with the C-terminus facing
  the stroma (protease protection). [PMID:39240724 "We found that the BST4 C-terminus was fully degraded after a 60 min treatment of trypsin, indicating that it faced the stroma"]
- Tubule targeting depends on the RBM-bearing C-terminus. [PMID:39240724 "BST4ΔC-term-mScarlet expressed in the bst4 mutant line did not localize to the pyrenoid tubules but was found throughout the thylakoid membrane (Fig. 5)"]

## Rubisco binding

- Original evidence: AP-MS (cited by Meyer as ref 18, the spatial interactome; the cached text of
  PMID:28938113 does not name Cre06.g261750, so the gene-level hit is in supplementary tables),
  plus the RBM itself. [PMID:33177094 "SAGA2, RBMP1, RBMP2, and CSP41A by affinity purification–mass spectrometry (18)"]
- Y2H: the BST4 C-terminus interacts with RBCS1. WR-to-EE mutation of the RBMs abolishes the
  interaction. FRET shows BST4 and RBCS1 are close in vivo. [PMID:39240724 "We confirmed using a yeast-2-hybrid approach that the C-terminus of BST4 interacts with CrRBCS1"]

## Tether hypothesis: tested and not supported

- Meyer 2020 model: RBMs on RBMP1/RBMP2 recruit Rubisco to the tubules. [PMID:33177094 "the presence of the same motif on the pyrenoid tubule-localized transmembrane proteins, RBMP1 and RBMP2, recruits Rubisco to the tubules and favors assembly of the matrix around them"]
- Adler et al. 2024 (peer-reviewed version of the 2023 preprint PMID:38014171):
  - bst4 pyrenoids are normal, with tubules. [PMID:39240724 "As a result, we conclude that BST4 is not necessary for the pyrenoid tubule–Rubisco matrix interface in Chlamydomonas."]
  - BST4 cannot pull thylakoids into an EPYC1-Rubisco condensate in Arabidopsis.
  - Conclusion: "BST4 is a pentameric transmembrane channel found within the pyrenoid tubules but is not crucial for Rubisco matrix tethering."
- Possible redundancy with other RBM tubule proteins (RBMP2) is not excluded, but there is no
  positive evidence that RBMP1 tethers anything. So molecular adaptor activity (GO:0060090) is
  NOT justified. The Rubisco interaction looks like a targeting mechanism that holds the channel
  in the tubules.

## Channel and physiology

- Pentameric assembly by Slimfield single-molecule counting, an AlphaFold pentamer, and a
  ~1 MDa BN-PAGE complex. [PMID:39240724 "The resulting probability distribution revealed that the most common BST4 complex is made up of 5 molecules (Fig. 2F)"]
- Xenopus oocytes gave no currents with KCl, NaHCO3, K-PEP or K-gluconate, including for
  C-terminal truncations. Permeant unknown. [PMID:39240724 "Therefore, we were unable to conclude what BST4 is permeable to."]
- bst4: no growth defect at air CO2 under continuous light, but a growth defect under
  fluctuating high light. NPQ (qE) is transiently higher during dark-to-light transitions,
  which suggests a lower lumenal pH. [PMID:39240724 "We found that under fluctuating high light, bst4 had a growth defect compared to the WT and the line complemented with full-length BST4"]
- Authors' model: BST4 is a tubule ion channel that contributes to lumen ion homeostasis/pH,
  possibly as an HCO3- channel. [PMID:39240724 "Specifically, wetsiri propose that BST4 influences the ion homeostasis and subsequently the pH of the pyrenoid tubules through its function as an ion channel, particularly during fluctuating light."]

## GOA assessment summary

- IBA voltage-gated chloride channel activity (from AtVCCN1): the family is right, but chloride
  and voltage gating are not shown, and no Cl- current was detected. Generalize to GO:0005216.
- IEA chloride transmembrane transport: comes from the IBA MF. Chloride is not shown, so mark
  it as over-annotated.
- IBA photosynthesis, light reaction: consistent with the bst4 NPQ and fluctuating-light
  phenotypes. Accept.
- IBA thylakoid membrane: consistent (the tubules are thylakoid-derived). Accept, and add pyrenoid
  tubule (GO:0160223) as NEW.
- IEA plasma membrane (ARBA): contradicted by every localization study. Remove.

## Deep research

- `deep_research_wrapper.py CHLRE RBMP1 falcon --fallback perplexity-lite` was run once
  (2026-10-03). Falcon returned HTTP 402 Payment Required. The perplexity-lite fallback failed
  with "Provider 'perplexity' not available". It was not retried, and the review is based on
  the cached primary literature above.
