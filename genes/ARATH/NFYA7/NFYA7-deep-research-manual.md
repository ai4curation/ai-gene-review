# NFYA7 (At1g30500; UniProt Q84JP1) - manual literature synthesis

No deep-research API was available; this summary was compiled by hand from the
UniProt record, the cached publications, and a PubMed search ("NF-YA7 Arabidopsis",
2026-10-28, one hit: PMID:31536532, a sorghum NF-Y genome survey with no NFYA7
experiments).

## Identity and family

- 190-aa nuclear transcription factor Y subunit A-7, one of 10 Arabidopsis NF-YA
  (HAP2/CBF-B) genes. "Belongs to the NFYA/HAP2 subunit family." (UniProt
  CC:SIMILARITY, PROSITE-ProRule PRU00966).
- Domains: Pfam PF02045 CBFB_NFYA; SMART SM00521 CBF; a subunit-association
  domain (residues 103-126) and the NFYA/HAP2-type DNA-binding segment (133-158).
- Two isoforms; isoform 2 lacks residues 78-81 (competing acceptor splice site).

## Molecular function (family-level)

- NF-Y is a heterotrimer of NF-YA, NF-YB and NF-YC; "NF-YB and NF-YC must interact
  and dimerize for NF-YA association and DNA binding" (UniProt CC:SUBUNIT, by
  similarity). NF-YA provides CCAAT sequence specificity:
  [PMID:23118940 "NF-Y activates transcription by recognizing the CCAAT- box cis-acting
  element present in about 30% of eukaryotic promoters in a highly specific manner via
  the DNA binding domain present in the NF-YA subunit"].
- NF-YA cannot bind DNA alone; the whole trimer is required
  [PMID:23118940 "Several studies have shown the requirement of the whole NF-YA/YB/YC
  complex to bind the CCAAT-box and activate the transcription of promoters containing
  this cis-acting element"]. Hence NFYA7 contributes to, rather than alone enables,
  CCAAT-dependent DNA-binding transcription factor activity.
- No NFYA7-specific biochemical (EMSA, ChIP) data were found.
- No NFYA7-specific localization experiment was found; the UniProt nuclear location
  is a curator inference (ECO:0000305).

## Expression

- Induced by low phosphate, low nitrogen and high sucrose
  [PMID:23118940 "An increase in NF-YA2, NF-YA7 and NF-YA10 transcript levels was
  detected 4 days after germination (dag) in low P, low N and high Suc treatments"].
- Unlike most NF-YAs, NFYA7 lacks a miR169 target site
  [PMID:23118940 "transcript levels for NF-YA7, which lacks the target site for miR169,
  were unaffected by the overexpression of miR169"].
- Reported as a direct target of PHR1 [PMID:23118940 "NF-YA7 has recently been
  identified as a direct target of the central regulator of the Pi stress response PHR1"].

## Overexpression phenotypes (PMID:23118940)

- 35S:NF-YA7 plants are dwarf, late-senescent, starch-excess and tolerant to several
  abiotic stresses [PMID:23118940 "Overexpression of NF-YA2, 7 and 10 resulted in dwarf
  late-senescent plants with enhanced tolerance to several types of abiotic stress"].
- The authors attribute the tolerance to growth arrest rather than direct
  stress-response gene activation [PMID:23118940 "stress tolerance is not observed upon
  NF-YA induction but rather at later stages when growth arrest is observed"].
- Inducible NF-YA7 lines were used for transcriptomics; the strongest direct-target
  evidence (CRES-T repressor) was for NF-YA2, not NF-YA7.
- These are gain-of-function and pleiotropic results; no loss-of-function phenotype for
  nf-ya7 is reported.

## Interactions

- High-throughput Y2H: FRS3 (CrY2H-seq, PMID:28650476); IAA9, IAA20, KNAT1, NIMIN-3
  (phytohormone interactome, PMID:32612234). Not validated individually; functional
  meaning unknown.

## Transcriptional repression (PMID:19207209, abstract only)

- In transient assays, LEC1/L1L-NF-YC2 activation of the CRUCIFERIN C promoter was
  reduced by co-expressed NF-YA [PMID:19207209 "However, additional expression of an
  NF-YA subunit interfered with the activation"]. TAIR attributes this IDA to NFYA7;
  the abstract does not name the NF-YA used.
