# ADSS1 (Q8N142 / PURA1_HUMAN) review notes

Deep research: falcon provider is out of credits (HTTP 402); no `-deep-research-falcon.md`
was generated. Review grounded in the cached UniProt record, the seeded GOA, and cached
`publications/PMID_*.md`. No content was fabricated as deep research.

## Identity
- ADSS1 = adenylosuccinate synthetase isozyme 1, the **muscle (basic / M-type) isozyme**
  (synonym ADSSL1). Paralog **ADSS2** (P30520) is the liver/ubiquitous ("acidic") isozyme.
- EC 6.3.4.4; RHEA:15753. HGNC:20093; chromosome 14. UniProt PE 1 (protein-level evidence).
- 457 aa homodimer; belongs to the adenylosuccinate synthetase family (HAMAP MF_03126);
  P-loop NTPase fold with three Gene3D domains (CDD cd03108 AdSS).

## Reaction / function
- Catalyses the **first committed step of AMP synthesis from IMP**:
  IMP + L-aspartate + GTP = N6-(1,2-dicarboxyethyl)-AMP (adenylosuccinate / S-AMP)
  + GDP + phosphate + 2 H+ [UniProt CATALYTIC ACTIVITY; RHEA:15753].
  Mg2+-dependent (binds 1 Mg2+ per subunit) [UniProt COFACTOR].
- Adenylosuccinate lyase (ADSL) then cleaves S-AMP -> AMP + fumarate (second step).
- PATHWAY: "Purine metabolism; AMP biosynthesis via de novo pathway; AMP from IMP:
  step 1/2" [UniProt PATHWAY; UniPathway UPA00075/UER00335].
- Component of the **purine nucleotide cycle (PNC)** which interconverts IMP and AMP to
  regulate nucleotide levels; contributes to glycolysis and ammoniagenesis in muscle
  [UniProt FUNCTION, ECO:0000269|PubMed:26506222].

## Key experimental evidence
- PMID:15786719 (Sun et al. 2005) — cloned human AdSSL1 from bone marrow stromal cells;
  "catalyzes the first committed step in AMP synthesis"; recombinant protein "possesses
  typical enzymatic activity to catalyze adenylosuccinate formation" (IDA GO:0004019);
  "Overexpressed AdSSL1 protein in COS-7 cells locates in cytoplasm" (IDA cytoplasm);
  "predominantly expressed in skeletal muscle and cardiac tissue". Abstract-only in cache.
  This paper is also the NAS source for GTP binding, phosphate ion binding, and
  "immune system process" (leukemia-cell expression framing).
- PMID:26506222 (Park et al. 2016, Ann Neurol) — compound-het ADSSL1 mutations
  (p.D304N and p.I350fs) cause autosomal-recessive adolescent-onset distal myopathy (MPD5,
  MIM 617030). "Both the D304N and I350fs mutations in ADSSL1 led to decreased enzymatic
  activity." D261N (=D304N in another numbering) VARIANT: decreased activity/stability.
  IMP GO:0004019 by IMP (mutation -> loss of catalytic activity). Abstract-only in cache.

## Cellular location
- Cytoplasm / cytosol [UniProt SUBCELLULAR LOCATION Cytoplasm; Reactome R-HSA-111524 cytosol TAS].

## Interactions (IPI, GO:0005515 protein binding)
- Three IntAct proteome-scale IPIs (PMID:28514442, 33961781, 40205054) all with
  WITH/FROM = UniProtKB:P30520 (ADSS2). UniProt INTERACTION records the ADSS1–ADSS2
  interaction (NbExp=4). Cached texts are the large interactome papers and do not name
  ADSS1 in the body. Per curation policy, bare `protein binding` IPIs -> MARK_AS_OVER_ANNOTATED
  (uninformative MF term), not REMOVE.

## Curation decisions summary
- Core MF: GO:0004019 adenylosuccinate synthase activity (IBA/IEA/IMP/IDA) — ACCEPT.
- GTP binding GO:0005525, Mg2+ binding GO:0000287, nucleotide binding GO:0000166 — molecular
  detail of the catalytic mechanism; ACCEPT (nucleotide binding is a general parent of GTP
  binding — keep, non-core-ish but accurate).
- BP: 'de novo' AMP biosynthetic process GO:0044208, AMP biosynthetic process GO:0006167,
  purine nucleotide biosynthetic process GO:0006164 — ACCEPT (directly involved).
- IMP metabolic process GO:0046040 — ACCEPT (IMP is the substrate).
- AMP salvage GO:0044209 (IEA, Ensembl orthology) — ADSS1 is a *de novo* AMP biosynthesis
  enzyme; in muscle it runs the PNC AMP-regenerating limb, which is functionally part of
  purine salvage/recycling. Keep but MARK_AS_OVER_ANNOTATED — "salvage" (reuse of preformed
  bases/nucleosides) is not the precise process; the committed IMP->AMP step is de novo.
- cytoplasm GO:0005737 / cytosol GO:0005829 — ACCEPT.
- immune system process GO:0002376 (NAS, PMID:15786719) — based on leukemia-cell expression;
  no functional immune role established. KEEP_AS_NON_CORE (weak, expression-based).
- phosphate ion binding GO:0042301 (NAS) — phosphate is a *product*, and the enzyme binds
  GTP/GDP phosphates; MARK_AS_OVER_ANNOTATED (not an informative standalone MF).
- protein binding GO:0005515 x3 — MARK_AS_OVER_ANNOTATED.
