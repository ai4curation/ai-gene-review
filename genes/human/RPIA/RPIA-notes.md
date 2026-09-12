# RPIA (Ribose-5-phosphate isomerase A) — review notes

UniProtKB: P49247 (RPIA_HUMAN). HGNC:10297. EC 5.3.1.6. 311 aa, cytosolic.

## Core biology

RPIA is ribose-5-phosphate isomerase, the enzyme of the non-oxidative branch of the
pentose phosphate pathway (PPP) that catalyses the reversible aldose–ketose
interconversion of D-ribose-5-phosphate and D-ribulose-5-phosphate.

- UniProt FUNCTION: "Catalyzes the reversible conversion of ribose-5-phosphate to
  ribulose 5-phosphate and participates in the first step of the non-oxidative branch of
  the pentose phosphate pathway." [file:human/RPIA/RPIA-uniprot.txt]
- Rhea RHEA:14657: aldehydo-D-ribose 5-phosphate = D-ribulose 5-phosphate; EC=5.3.1.6.
- PATHWAY: pentose phosphate pathway; D-ribose 5-phosphate from D-ribulose 5-phosphate
  (non-oxidative stage): step 1/1. [file:human/RPIA/RPIA-uniprot.txt]
- Family: ribose 5-phosphate isomerase (type A / RpiA). InterPro IPR004788, IPR020672;
  Pfam PF06026; CDD cd01398 RPI_A; PANTHER PTHR11934.

Directionally, RPIA supplies ribose-5-phosphate for nucleotide, nucleotide-cofactor
(NAD, FAD, CoA) and histidine/aromatic precursor biosynthesis; in the regenerative
direction it feeds ribulose-5-phosphate (and downstream via the epimerase into the
transketolase/transaldolase reactions) back toward glycolytic intermediates.

## Disease

Ribose-5-phosphate isomerase deficiency (RPIAD; MIM:608611). Autosomal recessive; one of
the rarest known inborn errors of metabolism (single/very few patients described). Slowly
progressive leukoencephalopathy with peripheral neuropathy; highly elevated polyols
(ribitol, D-arabitol) in brain (MRS) and body fluids.
[PMID:14988808 "the first patient with a deficiency of ribose-5-phosphate isomerase (RPI)
(Enzyme Commission number 5.3.1.6) who presented with leukoencephalopathy and peripheral
neuropathy"; "highly elevated levels of the polyols ribitol and D-arabitol"]
- p.Ala135Val (VAR_019122) plus a frameshift; deficient RPI activity in fibroblasts.
  [file:human/RPIA/RPIA-uniprot.txt VARIANT 135; PMID:14988808]

## Annotation assessment summary

- MF GO:0004751 ribose-5-phosphate isomerase activity: core. EXP (PMID:14988808), IBA, IEA
  (RHEA:14657, EC:5.3.1.6), NAS (PMID:7758956). All ACCEPT.
- BP GO:0009052 pentose-phosphate shunt, non-oxidative branch: core (IBA, IEA). ACCEPT.
- BP GO:0006098 pentose-phosphate shunt (parent), GO:0006014 D-ribose metabolic process:
  correct but less specific / non-core supporting; ACCEPT / KEEP_AS_NON_CORE.
- CC cytosol GO:0005829 / cytoplasm GO:0005737: core location (IBA, IEA, TAS). ACCEPT.
- CC mitochondrion GO:0005739 (HTP, PMID:34800366): RPIA is a soluble cytosolic enzyme
  with no transit/signal peptide; appears only in a large-scale MitoCoP mass-spec dataset.
  Treat as over-annotation (MARK_AS_OVER_ANNOTATED) — do NOT REMOVE an HTP experimental
  annotation whose full text/supp is unverified.
- MF GO:0005515 protein binding (IPI): all from high-throughput interactome maps (Y2H /
  AP-MS: Rual 2005, Rolland 2014, Luck 2020, Yu 2011, etc.). Uninformative bare protein
  binding → MARK_AS_OVER_ANNOTATED (not REMOVE, per policy).
- MF GO:0042802 identical protein binding (IPI, self EBI-744831–EBI-744831): RpiA is a
  homodimer in the family; self-interaction plausible but still an interactome-map bare
  binding term → KEEP_AS_NON_CORE (real homodimerization) but not a core catalytic MF.
- MF GO:0030246 carbohydrate binding / GO:0048029 monosaccharide binding (IEA, Ensembl
  Compara from rat ortholog): over-general electronic mappings; the substrate is a
  phosphorylated pentose bound as the isomerase substrate, not lectin-type sugar binding.
  MARK_AS_OVER_ANNOTATED.

## References
- PMID:14988808 — abstract-only cache (full_text_available: false) but abstract itself
  establishes RPI deficiency, EC 5.3.1.6, catalytic deficiency, disease. HIGH.
- PMID:7758956 — mouse/human RPI gene cloning; GST-mRPI fusion has enzymatic activity.
  Basis for NAS MF annotation. MEDIUM/HIGH.
- Interactome papers (16189514, 21516116, 24722188, 25416956, 25910212, 28514442,
  29892012, 31515488, 32296183, 33961781): high-throughput binary/AP-MS maps; LOW
  relevance to RPIA molecular function.
- PMID:34800366 — MitoCoP mitochondrial proteome; RPIA an HTP hit only; LOW relevance
  (localization likely a co-purification artifact for a cytosolic enzyme).
