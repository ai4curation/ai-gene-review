# GART (P22102) review notes

Human trifunctional purine biosynthetic protein adenosine-3 (gene GART; synonyms PGFT, PRGS).
Gene on chromosome 21q22.1 (of interest in Down syndrome trisomy region). 1010 aa, isoform Long
(P22102-1) displayed; isoform Short (P22102-2) truncates after the GARS ATP-grasp domain (VSP_005517,
residues 434-1010 missing).

## Verified biology (UniProt P22102, cached publications)

Single polypeptide carrying three consecutive de novo IMP biosynthesis activities:

- **Phosphoribosylamine--glycine ligase / GAR synthetase (GARS)** — EC 6.3.4.13, GO:0004637.
  N-terminal ATP-grasp domain. PRA + glycine + ATP -> GAR + ADP + Pi (RHEA:17453). Step 2 of de novo pathway.
  [UniProt: "The N-terminal ATP-grasp domain carries the phosphoribosylamine--glycine ligase activity."]
- **Phosphoribosylglycinamide formyltransferase / GAR transformylase (GART, GAR Tfase)** — EC 2.1.2.2,
  GO:0004644. C-terminal GART domain. GAR + 10-formyl-THF -> FGAR + THF (RHEA:15053). Step 3; folate-dependent.
  Only activity with EXP (ECO:0000269) support from crystal-structure/kinetics papers.
  [UniProt: "The C-terminal GART domain carries the phosphoribosylglycinamide formyltransferase activity."]
- **Phosphoribosylformylglycinamidine cyclo-ligase / AIR synthetase (AIRS)** — EC 6.3.3.1, GO:0004641.
  Central AIRS domain. FGAM + ATP -> AIR + ADP + Pi (RHEA:23032). Step 5.
  [UniProt: "The central AIRS domain carries the phosphoribosylformylglycinamidine cyclo-ligase activity."]

Cofactor: binds 1 Mg2+ or Mn2+ per subunit (PROSITE PRU00409). ATP-binding (ATP-grasp). Homodimer
(PMID:20631005). Cytosolic; the de novo purine pathway enzymes form a transient "purinosome" that can
co-localize under low-purine conditions (noted in Reactome R-HSA-73810/73813/73814 summaries).

## Key references and what they support

- PMID:2183217 (Schild 1990, PNAS) — cloning by functional complementation of yeast ade5/ade7/ade8
  mutations; establishes the single human cDNA is trifunctional GARS-AIRS-GART, maps to chr 21.
  Basis of MGI IDA annotations for the three MF activities + cytosol + de novo IMP/AMP/GMP/XMP BP.
  ABSTRACT-ONLY in cache (full_text_available: false).
- PMID:12450384 (Zhang 2002, Biochemistry) — crystal structures of human GAR Tfase (purN domain) with
  substrate beta-GAR; pH-dependent activity; EXP support for GO:0004644. Folate-dependent, antitumor target.
- PMID:12755606 (Zhang 2003, Biochemistry) — structure-based folate-analogue inhibitor of human GAR Tfase
  (Ki=15 nM), improvement over Lometrexol; EXP support for GO:0004644 as an anti-neoplastic target.
- PMID:2050105 (Gnirke 1991, EMBO J) — YAC cloning of full-length GART gene; TAS basis. Confirms
  trifunctional GARS-GART-AIRS, maps 21q22.1, functional complementation of GARS-/AIRS-deficient CHO cells.
- PMID:20458337 (Buschow 2010) — B-cell exosome proteome MS survey (539 proteins); source of the
  extracellular-exosome HDA localization. High-throughput; not a specific GART localization claim.

## Curation judgments

- Three MF activities (GO:0004637, GO:0004644, GO:0004641): CORE. Accept the IBA/IDA/EXP/TAS lines.
  GAR Tfase (GO:0004644) has the strongest (EXP) support and is the antifolate drug target.
- Cytosol (GO:0005829): CORE location. Accept IDA/IBA; IEA (Ensembl ortholog) redundant but fine.
- 'de novo' IMP biosynthetic process (GO:0006189): CORE process. Accept.
- purine nucleotide biosynthetic process (GO:0006164) / purine nucleobase (GO:0009113) / purine
  ribonucleoside monophosphate (GO:0009168): correct but broader parents; keep, non-core / accept.
- AMP/GMP/XMP 'de novo' biosynthesis (GO:0044208, GO:0006177, GO:0097294): these branch DOWNSTREAM
  of IMP; GART only makes IMP precursors. The acts_upstream_of_or_within lines are defensible (GART is
  upstream of AMP/GMP/XMP), but the involved_in lines overreach (GART is not part of AMP/GMP/XMP-specific
  synthesis). Mark involved_in AMP/GMP/XMP as over-annotated; keep acts_upstream_of_or_within as non-core.
- adenine biosynthetic process (GO:0046084, IBA): human GART makes purine nucleotides, not free adenine
  base; this is a plant/microbe-flavored term. Over-annotation.
- Developmental terms brainstem/cerebellum/cerebral cortex development (GO:0003360, GO:0021549,
  GO:0021987; IEA GO_REF:0000107 Ensembl Compara from rodent orthologs): housekeeping de novo purine
  enzyme; expression is broad (HPA "Low tissue specificity"). These reflect rodent phenotype/expression
  transfer, not a specific developmental function. Over-annotation.
- extracellular exosome (GO:0070062, HDA): high-throughput proteomics of B-cell exosomes; GART is a
  cytosolic enzyme. Over-annotation.
- catalytic activity (GO:0003824, IEA ARBA): uninformative root MF; accept but non-core / mark general.
- ATP binding (GO:0005524), metal ion binding (GO:0046872): supported by ATP-grasp + Mg/Mn cofactor
  features; accept as molecular-function support (non-core relative to the three named activities).
</content>
