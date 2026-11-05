# NFYA10 review notes

## Session 1 (2026-10-28)

- fetch-gene resolved Q8LFU0 (TAIR AT5G06510, GeneID 830539), Swiss-Prot reviewed, 9 GOA rows
  (all IBA/IEA/ISS/ISM; no experimental GOA rows).
- Literature: PMID:23118940 (full text, OE phenotypes, miR169 regulation), PMID:28469131 (full text,
  ChIP at YUC2), PMID:40051141 (full text, ChIP at LAZY1/2, GFP nuclear), PMID:24533947 (abstract).
  Wheat TaNF-YA10 papers (PMID:26083807, PMID:25461698) are about a different gene; not used.
- Key experimental points not in GOA:
  - nuclear localization of GFP-NF-YA10 [PMID:40051141 "We observed GFP:NF‐YA10 accumulation in the nuclei of root vasculature, endodermis, and cortex cells"]
  - in vivo promoter binding at CCAAT boxes [PMID:40051141 "ChIP‐qPCR showed that LAZY1 and LAZY2 promoters are bound by NF‐YA10"; PMID:28469131 "YUC2, a key speed-limiting gene in auxin homeostasis, acts as a direct target of NF-YA2 and NF-YA10."]
- Decisions:
  - MF: GO:0000981 kept as core but in contributes_to (NF-YA needs NF-YB/NF-YC dimer to bind DNA,
    UniProt by-similarity SUBUNIT note). GO:0003700 rows MODIFY to GO:0000981 (is_a checked with OAK).
  - GO:0003677 DNA binding MODIFY to GO:0000978 RNA polymerase II cis-regulatory region
    sequence-specific DNA binding (is_a descendant of GO:0003677, checked with OAK), supported by ChIP.
  - GO:0006355 MODIFY to GO:0006357 (already carried, IBA).
  - Nucleus rows ACCEPT (GFP evidence); CCAAT-binding factor complex ACCEPT.
  - No NEW process terms: root gravitropism / leaf growth / stress tolerance phenotypes come from
    overexpression or miR-resistant lines; NF-YA10 participates by regulating target transcription,
    which is captured by GO:0006357. A more specific negative regulation term would be a descendant
    of GO:0006357 (already carried) so not added as NEW; raised as a question.
- Curation gap: GOA lacks the IDA nucleus (PMID:40051141) and ChIP-based DNA binding rows.
