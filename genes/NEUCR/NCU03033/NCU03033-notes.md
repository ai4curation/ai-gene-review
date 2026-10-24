# NCU03033 evidence notes

NCU03033 is the Hap2/NF-YA subunit of the heterotrimeric CCAAT-binding transcription factor. Its conserved DNA-recognition domain works with the two partner subunits to bind CCAAT promoter elements and regulate nuclear RNA polymerase II transcription.

## Identity and provenance

The exact current accession is Q7SGY4; NCU03033 is retained as the current locus identifier. No independently established formal gene-symbol replacement was found. Original claims are preserved in NCU03033-protnlm-source.json from the live API snapshot retrieved 2026-09-09T03:00:51.831347+00:00. The current sequence is not proven to be the prediction-time input, and placeholder API dates do not establish release or training membership.

## Primary evidence and justified transfer

- [PMID:25589790] "The CBC consists of
three subunits, which are named in the filamentous fungus Aspergillus nidulans
HapB, HapC, and HapE."
- [PMID:25589790] "Initial
binding of the CBC to CCAAT boxes is mandatory for DNA recognition of HapX."

The specific domain/family observation used is `DR   InterPro; IPR001289; NFYA.`. Family membership and characterized relatives establish the inference; ARBA or AI-generated names are not independent functional evidence. PAINT is a curator-reviewed ancestral assertion, not donor-count evidence.

## Unresolved assertions

No unresolved GOA assertion remains at the reviewed level of specificity. Experimental observations on relatives are distinguished from target observations.

Additional primary evidence: [PMID:19965775] "The corresponding Aspergillus nidulans CCAAT-binding factor (AnCF)
consists of the subunits HapB, HapC and HapE. All of the three subunits are
necessary for DNA binding.". Full text also documents prior cross-species complementation evidence for Hap2/HapB/NF-YA, supporting conserved family transfer. Oxidative regulation of the partner HapC is not assigned as a Hap2-specific phenotype.

## Falcon report appraisal

The actual Falcon report arrived after the wrapper timeout and was inspected. It supports the conserved Hap2/NF-YA CCAAT-recognition role and cautions against transferring individual fungal regulons, essentiality or autonomous activation-domain function. The present review already grounds the family mechanism in Aspergillus primary biochemical papers (PMID:25589790; PMID:19965775). Its additional cellulase, respiration and iron-control suggestions are not used as target-specific annotations. The wrapper reported a 600-second Falcon timeout and the fallback returned HTTP 401 insufficient quota; the original Falcon child nevertheless completed, so no replacement report was fabricated or duplicate job submitted.

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 files were not opened or used.

### Identity
- Q7SGY4 (314 aa, TrEMBL, PE 3) is the full-length NCU03033 product (RefSeq XP_965419.1), not a fragment,
  isoform or alternative model. It carries the complete NF-YA/Hap2 essential core: subunit-association
  motif 194-217 and NFYA/HAP2-type DNA-binding region 225-250 (PROSITE PRU00966). It is the only
  PTHR12632/IPR001289 protein in N. crassa OR74A (UniProt query organism_id:367110), so there is no paralog.

### Evolutionary grounding
- UniProt places Q7SGY4 in PTHR12632 with no subfamily; InterPro also reports no subfamily. The PAINT IBA
  rows come from PTN000290575 (MF/BP; donors yeast HAP2 SGD:S000003206, human NFYA P23511, mouse Nfya,
  worm nfya-1) and PTN000290576 (CC), so Q7SGY4 sits under the NF-YA/Hap2 ancestral nodes together with
  yeast HAP2, Candida HAP2 and animal NFYA (all PTHR12632:SF6 in PANTHER 19.0 reference files).
- New analysis (compare_core_rereview.py, RESULTS-rereview.md): core identity 77.8% to S. pombe php2,
  76.2% to S. cerevisiae HAP2, 66.1% to human NFYA; no indels, DNA-recognition "YLHESRH.HAMRRPRG.GGRF"
  segment intact.
- Functional interchangeability of yeast Hap2, A. nidulans HapB and human NF-YA [PMID:19965775 "Moreover,
  S. cerevisiae Hap2p, A. nidulans HapB and human NF-YA are functionally interchangeable"] supports the
  family-level transfer.

### Decisions
- ACCEPT: GO:0000981 (IBA), GO:0006357 (IBA), GO:0016602 (IBA and IEA), GO:0005634 (IEA).
- MODIFY: GO:0003677 DNA binding -> GO:0000978 RNA pol II cis-regulatory region sequence-specific DNA
  binding (was previously -> GO:0000981, which is not a DNA-binding descendant); GO:0003700 -> GO:0000981;
  GO:0006355 -> GO:0006357; GO:0006351 -> GO:0006357 (lateral correction).
- Kept "regulation" not "positive regulation": the fungal CBC both activates and represses
  [PMID:19965775 "AnCF-mediated repression of gene expression was also found"]; in yeast activation is
  supplied by Hap4.
- Not transferred: iron/HapX regulon, oxidative-stress role (a HapC property), cellulase, respiration
  targets; N. crassa regulon unmapped.

### Relative
- Closest characterised relative by PAINT placement: S. cerevisiae HAP2 (P06774, SGD:S000003206), a donor
  to PTN000290575 and PTHR12632:SF6. No yeast HAP2 review exists in the repo (genes/yeast has HAP4 only).
  A. nidulans HapB is phylogenetically closer and biochemically characterised but has no PANTHER
  subfamily or PAINT donor status to anchor placement.
- Family review interpro/panther/PTHR12632/PTHR12632-review.yaml: single subfamily-agnostic grouping,
  representative member Q7SGY4; no disagreement (it asserts no SF-level placement).
- Module: modules/dmel_nf_y_complex.yaml (Drosophila NF-Y complex; same GO:0016602 complex, different
  species).
