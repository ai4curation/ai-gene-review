# exoc3l2a notes

## Setup and provenance

- Fetched with `just fetch-gene` on A0A8N7TEH3 (TrEMBL, RefSeq XP_683981.7, "Exocyst complex
  component 3-like protein 2", 932 aa); 5 GOA rows (3 IBA, 2 IEA), none with a PMID. The GOA
  gene-name column reads "Tumor necrosis factor alpha-induced protein 2-like", which reflects
  PANTHER's subfamily naming (PTHR21292:SF18, "TUMOR NECROSIS FACTOR ALPHA-INDUCED PROTEIN 2"), not
  the orthology (see below). ZFIN ZDB-GENE-060526-343, Ensembl ENSDARG00000008414, chromosome 5.
- **Deep research unavailable**: Edison returned 402 Payment Required and the OpenAI key is
  invalid, so no `-deep-research-*.md` file exists. Literature searched by hand via Europe PMC
  (queries: `exoc3l2a OR exoc3l2b`, `EXOC3L2`, `TITLE:"exocyst complex component 3-like 2"`,
  `EXOC3L2 AND endothelial AND migration`, `exoc3l2 AND zebrafish`, `EXOC3L4`).
- DANRE_DUPLICATION random sample, draw 4 (seed 20260928); paralog exoc3l2b.

## Which human gene is this an ortholog of?

- ZFIN/Ensembl name the gene after EXOC3L2, and Ensembl Compara calls human EXOC3L2 an
  ortholog (one-to-many, Euteleostomi) and places the exoc3l2a/exoc3l2b duplication at
  Osteoglossocephalai, with one gar ortholog (ENSLOCG00000014731) for both copies
  (file:DANRE/exoc3l2a/exoc3l2a-bioinformatics/RESULTS.md).
- PANTHER's TGD table lists EXOC3L4 as the human ortholog, and PANTHER's HMM assigns the
  zebrafish proteins to TNFAIP2-named subfamilies (SF18/SF17) while human EXOC3L2 is in SF7.
- My alignment: exoc3l2a is 35.3% identical to human EXOC3L2 but only 19.7-21.8% to EXOC3,
  EXOC3L1, EXOC3L4 and TNFAIP2; zebrafish also has its own exoc3l4, tnfaip2a/b and exoc3l1
  genes, which are all ~17-22% identical to exoc3l2a. The gar and medaka orthologs show the same
  pattern (35-39% to EXOC3L2). **Conclusion: exoc3l2a is an EXOC3L2 co-ortholog; the PANTHER
  EXOC3L4 label is not supported by sequence.** (RESULTS.md)

## Zebrafish literature

- Endothelial expression at 24 hpf (AngioTag TRAP-seq + WISH):
  [PMID:40613926 "In situ hybridization for three of these genes– exoc3l2a, slc22a7b.1, and bpifc–, confirmed their endothelial-specific expression pattern"].
  Figure legend gives the stage: [PMID:40613926 "Whole mount in situ hybridization of 24 hpf wild type zebrafish probed for exoc312a"] (sic).
- Part of the caudal hematopoietic tissue (CHT) vascular-niche endothelial signature:
  [PMID:37119815 "There are numerous genes identified by this study that were not previously associated with the HSPC niche, including several with activities related to endocytosis and membrane trafficking: ap1b1, dab2, pxk, exoc3l2a and snx8."]
- No mutant, morphant or protein-level study. ZFIN has no curated wild-type expression rows.

## Mammalian EXOC3L2 (the single-copy ortholog)

- Human endothelial cells: associates with exocyst, needed for VEGFR2 phosphorylation and
  directional migration [PMID:21566143 "Myc-tagged EXOC3L2 co-precipitates with the exocyst protein EXOC4, and immunofluorescence detection of EXOC3L2 shows partial subcellular colocalization with EXOC4 and EXOC7."]
  [PMID:21566143 "Finally, we show that exoc3l2 silencing inhibits VEGF receptor 2 phosphorylation and VEGFA-directed migration of cultured endothelial cells."]
  Vascular expression in mouse brain: [PMID:21566143 "The brain sections were stained for EXOC3l2 together with PECAM and expression of EXOC3l2 was detected in endothelial cells, particularly in the larger vessels"]
- Mouse knockout: embryonic lethal with hemorrhage; endothelial/hematopoietic (Tie2-Cre)
  deletion reproduces it [PMID:36362885 "Most of the Exoc3l2 KO embryos died in utero and showed hemorrhage, abnormal heart and brain development."]
  [PMID:36362885 "Conditional KO animals lacking Exoc3l2 in hematopoietic and endothelial lineages showed similar phenotypes, such as hemorrhage and heart defects, indicating that Exoc3l2 in hematopoietic and endothelial lineages is responsible for normal cardiovascular development."]
  Dispensable for postnatal retinal angiogenesis [PMID:36362885 "Inducible KO in endothelial cells during postnatal retinal development resulted in normal angiogenesis in the retina, indicating that Exoc3l2 is dispensable for postnatal angiogenesis in the retina."]
  Mouse expression also in probable cranial neural crest [PMID:36362885 "GFP expression was also observed in non-endothelial cells, which are most likely cranial neural crest cells (Figure 1c)."]
- Human disease: [PMID:30327448 "We propose that biallelic EXOC3L2 mutations lead to a novel syndrome that affects hindbrain development, kidney and possibly the bone marrow."]
- Structure: EXOC3L2 is a paralog of M-Sec/TNFAIP2 and may bind RalA; whether it is an
  exocyst subunit or acts independently is open [PMID:30086153 "Therefore, it will be relevant to determine whether EXOC3 paralogs, particularly M-Sec and EXOC3L2, are interchangeable subunits that are selectively assembled into different functional variants of the exocyst complex, or independent operators."]
  Note: PMID:30086153 uses "Exoc3l2a" for a *mouse splice variant*; unrelated to the zebrafish gene name.
- Human EXOC3L2 in GOA (QuickGO, 2026-09-28) has only IEA exocyst/exocytosis rows and IPI
  protein-binding rows; it carries no IBA from PTN000480155, whereas human EXOC3, EXOC3L1,
  EXOC3L4 and TNFAIP2 do. So in PANTHER the zebrafish copies sit with the paralogs that inherit
  the node, not with human EXOC3L2 (consistent with the PANTHER EXOC3L4 call).

## Own analyses (file:DANRE/exoc3l2a/exoc3l2a-bioinformatics/RESULTS.md)

See RESULTS.md. Key points: 50.9% identity between the copies; exoc3l2a carries about twice as
many lineage-specific changes as exoc3l2b relative to gar (138 vs 71; chi2 21.5); both keep a
full-length Sec6 domain; similar whole-embryo time courses; broadly overlapping adult Bgee calls.

## Annotation decisions

- exocyst (IBA, IEA): accepted; mammalian EXOC3L2 co-precipitates with EXOC4 and colocalises
  with EXOC4/EXOC7, and the Sec6 domain is intact. Membership of the canonical octamer is not
  shown, so association rather than stoichiometric subunit.
- exocytosis (IBA, IEA): kept as non-core; no secretion assay for EXOC3L2 in any species.
- SNARE binding (IBA): marked over-annotated; the only experimental donor is yeast Sec6.
