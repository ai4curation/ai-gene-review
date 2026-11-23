# NFYA10 (At5g06510, Q8LFU0) - manual literature research

No deep-research API was available; this summary was compiled by hand from the cached
publications (`publications/PMID_*.md`) and a PubMed search for `"NF-YA10" AND Arabidopsis`
(6 hits, two of which concern wheat TaNF-YA10, a different gene).

## Identity and family

- Arabidopsis NF-YA10 (At5g06510) is one of 10 NF-YA (HAP2/CBF-B) subunits of the plant NF-Y
  CCAAT-binding heterotrimer [PMID:23118940 "In Arabidopsis, 10 NF-YA, 13 NF-YB and 13 NF-YC genes encode the different subunits of NF-Y."].
- UniProt Q8LFU0: 269 aa, NFYA/HAP2-type DNA-binding region 164-189, subunit association domain
  137-158; "Belongs to the NFYA/HAP2 subunit family" (PROSITE PRU00966). Function and subunit
  statements are by similarity (ECO:0000250): "NF-YB and NF-YC must interact and dimerize for NF-YA
  association and DNA binding".
- NF-YA10 arose from a recent Brassicaceae duplication with NF-YA2
  [PMID:40051141 "NF‐YA10 diverged from a recent duplication with NF‐YA2 within Brassicaceae"].

## Mechanism

- NF-Y binds CCAAT boxes as a trimer; NF-YA carries the DNA-binding domain
  [PMID:23118940 "Several studies have shown the requirement of the whole NF-YA/YB/YC complex to bind the CCAAT-box and activate the transcription of promoters containing this cis-acting element"].
- In vivo promoter binding by NF-YA10 itself (ChIP):
  - LAZY1 and LAZY2 promoters at TSS-proximal CCAAT boxes, with repression of these genes in
    miR169-resistant NF-YA10 lines [PMID:40051141 "ChIP‐qPCR showed that LAZY1 and LAZY2 promoters are bound by NF‐YA10, in contrast to LAZY3 when compared to the nearby negative control."].
  - YUC2 promoter CCAAT element, YUC2 repressed in overexpressors
    [PMID:28469131 "YUC2, a key speed-limiting gene in auxin homeostasis, acts as a direct target of NF-YA2 and NF-YA10."].
- Location: GFP-NF-YA10 is nuclear [PMID:40051141 "We observed GFP:NF‐YA10 accumulation in the nuclei of root vasculature, endodermis, and cortex cells"].

## Regulation

- NF-YA10 transcript is induced by low phosphate, low nitrogen and high sucrose and is a miR169
  target; strongest induction under low Pi [PMID:23118940 "NF-YA10 under low P (51-fold induction at 14 dag)"].
- miR169defg isoform specifically targets NF-YA2 and NF-YA10 in root growth control (PMID:24533947,
  abstract only).

## Phenotypes (gain-of-function only; no loss-of-function data found)

- 35S:NF-YA10 plants are dwarf, late senescent and abiotic-stress tolerant (PMID:23118940).
- Another study reports overexpression increases leaf size and lowers IAA content (PMID:28469131);
  note the apparent contrast with the dwarfism in PMID:23118940 (different constructs/expression
  levels).
- miR169-resistant NF-YA10 alters lateral-root gravitropic angle and root-explored area
  (PMID:40051141).

These phenotypes reflect overexpression/miRNA-resistance and do not by themselves establish
participation in a specific process beyond transcriptional regulation of target genes.
