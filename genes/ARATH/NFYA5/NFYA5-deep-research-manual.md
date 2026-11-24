# NFYA5 (At1g54160; UniProt Q9SYH4) - manual literature synthesis

No deep-research API was available; this summary was compiled by hand from the
UniProt record, the cached publications, and a PubMed search
("(NFYA5 OR NF-YA5) AND Arabidopsis", 2026-10-28; 6 hits: PMID:18682547,
PMID:25514924, PMID:28332758, PMID:39273166, PMID:40573788 (in silico miRNA
target prediction only) and PMID:28261246 (NMD/flowering, passing mention)).

## Identity and family

- 308-aa nuclear transcription factor Y subunit A-5, one of 10 Arabidopsis NF-YA
  (HAP2/CBF-B) genes; "Belongs to the NFYA/HAP2 subunit family." (UniProt
  CC:SIMILARITY, PROSITE-ProRule PRU00966). Pfam PF02045 CBFB_NFYA, SMART SM00521,
  PROSITE PS00686/PS51152; subunit association domain (SAD) residues 181-204 and
  NFYA/HAP2-type DNA-binding segment 211-236 (UniProt FT).
- The transcript carries a miR169 target site and is a cis-natural-antisense pair
  with NERF (At1g54150) [PMID:25514924 "NFYA5 is an important drought-stress
  inducible transcription factor gene that is targeted by miR169 in Arabidopsis"].

## Molecular function (family-level)

- NF-Y is an NF-YA/NF-YB/NF-YC heterotrimer; "NF-YB and NF-YC must interact and
  dimerize for NF-YA association and DNA binding" (UniProt CC:SUBUNIT, by similarity).
- The NF-YA subunit supplies CCAAT specificity [PMID:23118940 "NF-Y activates
  transcription by recognizing the CCAAT- box cis-acting element present in about 30%
  of eukaryotic promoters in a highly specific manner via the DNA binding domain
  present in the NF-YA subunit"], but the whole trimer is needed to bind
  [PMID:23118940 "Several studies have shown the requirement of the whole NF-YA/YB/YC
  complex to bind the CCAAT-box and activate the transcription of promoters containing
  this cis-acting element"].
- NF-YA5 was recovered among upstream regulators of PRC2 genes in an enhanced yeast
  one-hybrid screen (PMID:27650334; TAIR IPI to the MEA/AT1G02580 promoter). The
  cached full text is truncated and does not show the NF-YA5 result.
- No NFYA5-specific EMSA or ChIP data were found.

## Biological roles

- Drought: NFYA5 is induced by drought in an ABA-dependent manner, partly
  transcriptionally and partly through drought repression of miR169a/c; it is
  expressed in vascular tissue and guard cells; nfya5 knockouts lose more leaf water
  and are drought sensitive, overexpressors are drought resistant, and NFYA5 is
  required for expression of a set of drought-responsive genes [PMID:18682547
  "nfya5 knockout plants and plants overexpressing miR169a showed enhanced leaf water
  loss and were more sensitive to drought stress than wild-type plants"; "Microarray
  analysis indicated that NFYA5 is crucial for the expression of a number of drought
  stress-responsive genes"]. Abstract only cached.
- Dehydration shock induces both miR169 and NFYA5; miR169 family members differ in
  how they repress NFYA5 [PMID:28332758, abstract].
- NERF antisense siRNAs raise NFYA5 transcript levels; NERF, "like NFYA5", controls
  stomatal aperture and drought resistance [PMID:25514924].
- Blue light / ABA: a GCR1-GPA1-PRN1-NF-Y (A5, B9, possibly C9) chain was proposed
  for LHCB expression in etiolated seedlings, from T-DNA mutants and Y2H/
  co-precipitation [PMID:17322342 "a nuclear factor Y heterotrimer comprised of A5,
  B9, and possibly C9"]. Abstract only cached; single study.
- Embryo/seed: overexpression of NF-YA1/5/6/9 affects gametogenesis, embryogenesis,
  seed development and induces somatic embryos, but single/double mutants have no
  detectable phenotype [PMID:22933713 "single or double mutants of these NF-YA genes do
  not have detectable phenotype"]. Abstract only. Later work implicated
  miR169-targeted NF-YAs, including NF-YA5, as positive regulators of somatic
  embryogenesis induction (PMID:39273166, abstract; not cached).
- Nutrient/sucrose stress: NF-YA5 transcripts rise strongly under high sucrose and are
  post-transcriptionally controlled by miRNAs (higher in hen1-1) [PMID:23118940
  "NF-YA5 was most responsive in high Suc (43-fold induction at 14dag)"]. The
  overexpression phenotypes in that paper were for NF-YA2, 7 and 10, not NF-YA5.
- Repression: in transient assays an extra NF-YA subunit interfered with
  LEC1/L1L-NF-YC2 activation of the CRC promoter (PMID:19207209, abstract does not
  name the NF-YA; TAIR attributes to NF-YA5). Proposed sequestration model
  [PMID:23118940 "The second mechanism proposes that NF-YA acts as a repressor by
  sequestering the NF-YB/YC heterodimer"].

## Location

- Nucleus: UniProt curator inference (ECO:0000305); no NFYA5-specific localization
  experiment found.
