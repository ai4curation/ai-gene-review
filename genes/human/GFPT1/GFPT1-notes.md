# GFPT1 (Q06210) review notes

Human glutamine--fructose-6-phosphate aminotransferase [isomerizing] 1 (GFAT1 / GFPT1).
HGNC:4241. 699 aa. EC 2.6.1.16. Reviewed from local files only (no deep-research run).

## Identity and core biochemistry

- UniProt RecName "Glutamine--fructose-6-phosphate aminotransferase [isomerizing] 1";
  EC=2.6.1.16 with experimental evidence from PubMed:32019926 and PubMed:35229715
  [file:human/GFPT1/GFPT1-uniprot.txt "EC=2.6.1.16 {ECO:0000269|PubMed:32019926, ECO:0000269|PubMed:35229715}"].
- CATALYTIC ACTIVITY (UniProt, Rhea RHEA:13237):
  D-fructose 6-phosphate + L-glutamine = D-glucosamine 6-phosphate + L-glutamate
  [file:human/GFPT1/GFPT1-uniprot.txt "Reaction=D-fructose 6-phosphate + L-glutamine = D-glucosamine 6-"].
- Rate-limiting enzyme of the hexosamine biosynthetic pathway (HBP); controls flux of
  glucose into the HBP; feedback-inhibited by UDP-GlcNAc
  [file:human/GFPT1/GFPT1-uniprot.txt "Rate-limiting enzyme of the hexosamine biosynthetic pathway"].
- Two-domain architecture: N-terminal glutamine amidotransferase type-2 domain (aa 2-305,
  hydrolyses L-Gln -> L-Glu + NH3) + C-terminal isomerase region (aa 313-680, two SIS
  subdomains) that isomerises Frc6P to Glc6P and aminates it to GlcN6P
  [file:human/GFPT1/GFPT1-uniprot.txt "Glutamine amidotransferase type-2"; "SIS 1"; "Isomerase"].
- PMID:32019926 (Ruegenberg 2020, full text): "In the first step of the HP, GFAT synthesizes
  d-glucosamine-6-phosphate (GlcN6P) from l-glutamine (l-Gln) and Frc6P, releasing l-glutamate
  (l-Glu)"; "the rate-limiting enzyme of the HP"; "UDP-GlcNAc directly interacts with GFAT-1,
  inhibiting catalytic activity". Full-length crystal structure of human GFAT-1; defines
  UDP-GlcNAc feedback site (G469E / G451E-numbering gain-of-function loses feedback).
- PMID:35229715 (Kroef 2022, full text): "In the first and rate limiting step of the HBP,
  glutamine fructose-6-phosphate amidotransferase (GFPT) converts fructose-6-phosphate (Frc6P)
  and L-glutamine (L-Gln) to D-glucosamine-6-phosphate (GlcN6P)". Paper is mainly about GFPT2 /
  AMDHD2 but directly assays GFPT1 enzyme activity and UDP-GlcNAc sensitivity
  ("Compared with GFPT1, GFPT2 had a much lower sensitivity to UDP-GlcNAc"). GFPT1 is the
  ubiquitously expressed paralog. FlyBase (dataset source) attributed the IDA GFPT1
  annotations to this paper; kept (experimental, do not remove).

## Downstream / pathway context

- GlcN6P is the committed precursor for UDP-GlcNAc, feeding N-/O-linked glycosylation,
  O-GlcNAcylation, GPI anchors, glycosaminoglycans/hyaluronan (HBP as nutrient/flux sensor).
- PMID:26887390 (Oikari 2016, abstract only): GFAT1 siRNA silencing "reduced the cellular pool
  of UDP-GlcNAc and hyaluronan synthesis" in human keratinocytes -> supports IMP for
  UDP-N-acetylglucosamine biosynthetic process (GO:0006048).
- PMID:1460020 (McKnight 1992, abstract only): cloning of human GFAT; recombinant enzyme
  raised "GFAT activity 4.5-fold" and was "inhibited 51% by UDP-GlcNAc". This is the source
  of the legacy ProtInc TAS annotations. It supports catalytic activity, NOT "energy reserve
  metabolic process".
- PMID:8144040 (Sayeski 1994, abstract only): murine GFAT cDNA; "GFAT is the rate-limiting
  enzyme in hexosamine synthesis". Source of the older PINC TAS GO:0004360 / GO:0006002.

## Localization

- Cytosolic enzyme (Reactome TAS: R-HSA-4085027, R-HSA-449715, R-HSA-1791088 -> GO:0005829).
- GO:0070062 extracellular exosome (HDA, PMID:20458337, B-cell exosome proteomics): common
  mass-spec exosome-fraction hit; kept as non-core (not the site of catalytic function).

## Disease

- GFPT1 loss-of-function variants cause congenital myasthenic syndrome type 12 (CMS12;
  limb-girdle CMS with tubular aggregates), MIM:610542 (PubMed:21310273, Senderek 2011)
  [file:human/GFPT1/GFPT1-uniprot.txt "Myasthenic syndrome, congenital, 12 (CMS12)"].
- Reactome R-HSA-4085023 "Defective GFPT1 causes CMSTA1".

## Annotation review decisions (summary)

- Core MF: GO:0004360 L-glutamine:D-fructose-6-phosphate transaminase (isomerizing) activity.
  All 6 GO:0004360 annotations (IBA, IEA, 2x Reactome TAS, EXP PMID:32019926, IDA PMID:35229715,
  TAS PMID:8144040) ACCEPTed.
- Core BP: GO:0006048 UDP-N-acetylglucosamine biosynthetic process (IBA, 2x IEA/Reactome/ARBA,
  IDA PMID:35229715, IMP PMID:26887390) ACCEPTed.
- GO:0006002 fructose 6-phosphate metabolic process: real (substrate metabolism) but a
  by-product framing of the same reaction; KEEP_AS_NON_CORE.
- Cytosol GO:0005829: ACCEPT.
- GO:0006112 energy reserve metabolic process: biologically wrong (HBP diverts F6P AWAY from
  energy/glycogen metabolism). ARBA IEA -> REMOVE; legacy ProtInc TAS (PMID:1460020) ->
  MARK_AS_OVER_ANNOTATED (experimental/author annotation, not removed per policy).
- GO:0005515 protein binding (2x IPI, both WITH GFPT2 O94808): this is the GFPT1-GFPT2
  homolog/heteromer interaction from high-throughput interactome maps
  (UniProt INTERACTION "Q06210; O94808: GFPT2; NbExp=3"). Bare "protein binding" ->
  MARK_AS_OVER_ANNOTATED (uninformative; not removed per policy). Neither cited interactome
  paper's cached text names GFPT1/GFPT2 in prose, so no verbatim quote given.
- GO:0097367 carbohydrate derivative binding / GO:1901135 / GO:1901137 (InterPro IEA):
  over-general parent terms subsumed by the specific MF/BP; KEEP_AS_NON_CORE.
- GO:0032922 circadian regulation of gene expression (IEA Ensembl + ISS, both from mouse
  P47856 "By similarity"): HBP/UDP-GlcNAc modulates peripheral clock oscillation
  [file:human/GFPT1/GFPT1-uniprot.txt "modulates peripheral clock oscillation (By similarity)"],
  but this is an indirect downstream/By-similarity role, not a core function of the enzyme;
  KEEP_AS_NON_CORE.
- GO:0070062 extracellular exosome (HDA): KEEP_AS_NON_CORE.
