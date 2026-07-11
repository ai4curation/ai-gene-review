# DLST (P36957) review notes

## Provenance / process
- Deep research (falcon) could NOT be generated in this environment: `just deep-research-falcon human DLST`
  fails with a Python type-union error (`unsupported operand type(s) for |: 'type' and 'NoneType'`,
  project.justfile line 218). The OLS MCP also errors (`No module named 'rich.traceback'`).
  No `-deep-research-*.md` fabricated. Review grounded in the cached UniProt record
  (`DLST-uniprot.txt`), the seeded GOA TSV, and the cached `publications/PMID_*.md`.

## Core biology (verified)
- DLST = ODO2_HUMAN, the **E2 (dihydrolipoyllysine-residue succinyltransferase, EC 2.3.1.61)**
  core component of the mitochondrial **2-oxoglutarate (alpha-ketoglutarate) dehydrogenase complex
  (OGDHC)** of the TCA cycle. Reaction: N6-[(R)-dihydrolipoyl]-L-lysyl-[protein] + succinyl-CoA <=>
  N6-[(R)-S8-succinyldihydrolipoyl]-L-lysyl-[protein] + CoA (RHEA:15213). In the complex it transfers
  the succinyl group from its lipoyl arm to CoA, forming succinyl-CoA. Complex = OGDH (E1) + DLST (E2)
  + DLD (E3) (+ assembly factor MRPS36/KGD4). [UniProt P36957; PMID:36854377; PMID:30929736]
- The SAME DLST E2 is SHARED by the **2-oxoadipate dehydrogenase complex (OADHC)** with the DHTKD1 E1
  and the shared DLD E3, acting in L-lysine / L-tryptophan catabolism (2-oxoadipate -> glutaryl-CoA).
  DLST there acts as a dihydrolipoyllysine-residue **glutaryltransferase** (GO:0120571). Both complexes
  share E2 (DLST) and E3 (DLD). [PMID:29191460]
- Structural mechanism (MRPS36 paper): "2-oxoglutarate is decarboxylated by ... E1o (OGDH) and the
  respective 2-succinyl intermediate is transferred to the flexible lipoyl domain (LD) of E2o (DLST).
  Second, E2o transfers the succinyl functional group from its LD domain onto CoA-SH generating
  succinyl-CoA." Eukaryotic E2o lacks the PSBD; MRPS36 substitutes as E3 adaptor. [PMID:36854377]
- Active site His424 (mutagenesis H424A = loss of succinyltransferase activity); EC/catalytic activity
  and TCA-cycle + lysine-degradation pathways established by PMID:30929736. Lipoyl-binding domain
  70-144; N6-lipoyllysine at K110. [UniProt FT; PMID:30929736]

## Moonlighting / localization
- A small (~1-1.6%) nuclear fraction of the OGDH complex (OGDH+DLST+DLD) associates with KAT2A/GCN5
  on gene promoters and locally generates succinyl-CoA for KAT2A-mediated histone H3K79 succinylation.
  DLST NLS residues Arg224/Lys226 drive nuclear translocation. Mainly mitochondrial matrix; nucleus is
  a minor moonlighting pool. [PMID:29211711]
- Bulk proteomics puts DLST in mitochondria (PMID:34800366 HTP, PMID:36854377 NAS). "nucleoplasm"
  (HPA IDA GO_REF:0000052), "nucleus" (HDA sperm-nucleus proteome PMID:21630459; SubCell IEA), and
  "membrane" (HDA NK-cell membrane proteome PMID:19946888) are proteomic-survey localizations; the
  nucleus pool is supported by focused work (PMID:29211711) but "membrane" is a soluble-matrix protein
  co-purifying artifact.

## Disease
- Pheochromocytoma/paraganglioma syndrome 7 (PPGL7, MIM:618475), autosomal dominant; recurrent germline
  DLST p.Gly374Glu functionally compromises DLST, causes 2-hydroxyglutarate accumulation and a
  pseudohypoxic/EPAS1-like signature. [PMID:30929736]

## Interaction annotations
- Rows 11-84 are IPI `protein binding` (GO:0005515) from three interactome screens:
  Y2H (PMID:16169070, NAP1L1), mitochondrial AP/MS ND network (PMID:29128334: CDK1, PSMC4, NAP1L1,
  YWHAE), and Y2H neurodegeneration interactome (PMID:32814053, ~70 preys). All are bare, uninformative
  `protein binding`; per curation policy avoid `protein binding` and mark as over-annotated rather than
  REMOVE (experimental IPIs). Functionally meaningful partners (OGDH, DLD, KAT2A, ABHD11) are captured
  by complex/process terms instead.

## Action plan
- Core: GO:0004149 (MF succinyltransferase), GO:0006099 (TCA cycle), GO:0006103 (2-oxoglutarate
  metabolic process), GO:0045252 (OGDH complex), GO:0160167 (oxoadipate dehydrogenase complex),
  GO:0120571 (glutaryltransferase, OADHC MF), GO:0005759 (mitochondrial matrix), and lysine catabolism.
- Accept mitochondrial/matrix/complex/TCA/succinyltransferase annotations. Mark bare protein-binding
  IPIs as over-annotated. REMOVE only clearly wrong IEA-style inferences (GO:0005634 nucleus SubCell
  IEA is over-broad but nucleus is real per PMID:29211711 -> keep as non-core; GO:0016020 membrane HDA
  is a soluble matrix protein mislocalized -> over-annotated).
