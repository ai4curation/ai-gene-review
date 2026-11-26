---
provider: manual
date: 2026-11-25
---

# Manual deep research for S. pombe qcr1

The Falcon deep-research provider and the Perplexity fallback were unavailable in this checkout, so this file records a manual synthesis of the cached literature and database records used for the review.

S. pombe qcr1 should be curated as a bifunctional beta-MPP/Cor1 protein that contributes to mitochondrial presequence cleavage and respiratory complex III.

## Core conserved MPP activity

The S. pombe protein Q9P7X1 is the `PTHR11851:SF149` ortholog of beta-MPP and of respiratory complex III Cor1/Core1 proteins. Its UniProt record assigns EC 3.4.24.64, the M16 zinc-binding-site InterPro entry, a zinc cofactor, mitochondrial matrix localization, and a heterodimeric MPP complex with Mas2 by similarity to S. cerevisiae Mas1.

The older S. cerevisiae MAS1 literature provides the classic fungal transfer source. MAS1 and MAS2 encode the two nonidentical MPP subunits of the matrix protease that removes mitochondrial matrix-targeting signals from imported proteins (`PMID:2007593`), and MAS1 encodes an essential subunit of the mitochondrial processing protease (`PMID:3044780`). The S. cerevisiae beta subunit has the zinc-binding `HXXEH` active-site region, binds alpha-MPP, and helps bind or cleave presequence substrates (`PMID:9299349`, `PMID:9654444`, `PMID:11470436`). Rat PMPCB provides an additional beta-MPP sequence-similarity anchor for the MPP substrate-recognition mechanism (`PMID:12433926`).

S. pombe also has direct evidence for mitochondrial processing peptidase chemistry. The Rsm22-Cox11 tandem precursor is matured in two successive S. pombe import reactions, including a later separation of the Rsm22 and Cox11 domains by MPP cleavage at an internal processing site (`PMID:16835444`).

## Direct S. pombe Cor1 evidence

The strongest target-specific evidence is the 2023 cryo-EM and functional study of the S. pombe CIII2-CIV supercomplex (`PMID:37939086`). The authors showed that the qcr1 product is also Cor1, a matrix-facing subunit of respiratory complex III in the S. pombe III-IV supercomplex. The S. pombe Cor1 protein retains a conserved MPP zinc-binding motif, the structure showed metal density at that site, and purified S. pombe CIII2-CIV1/2 cleaved the radiolabeled pSu9-DHFR MPP substrate in vitro. That direct fission-yeast evidence argues against the terminal 2026 PAINT IRD at qcr1 for GO:0004222.

The same study supports adding a respiratory chain complex III component annotation for qcr1. Cor1 was one of the S. cerevisiae CIII subunit homologs modeled in the S. pombe supercomplex structure, and the preparation retained complex III and supercomplex respiratory activity.

## GO-CAM context

GO-CAM 69729a3800007453 names the same PomBase gene product `SPBP23A10.15c` with the older `mas1` alias, but the current S. pombe symbol is qcr1. The model's signal peptidase activity, mitochondrial protein processing process, and matrix location agree with the gene review. In the final shared GO-CAM consistency-notes PR, record the non-conflicting naming issue and consider noting that S. pombe qcr1/Cor1 integrates beta-MPP activity with complex III.
