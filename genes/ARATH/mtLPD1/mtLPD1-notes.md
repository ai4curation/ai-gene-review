# mtLPD1 (At1g48030, UniProt Q9M5K3) - curation notes

**Deep research could not be run** in this environment (no provider API keys).
These notes are a manual literature summary built only from the cached
publications in `publications/`, the UniProt record (`mtLPD1-uniprot.txt`) and
PubMed searches. No `-deep-research-*.md` file exists for this gene.

## Identity and naming caution

- UniProt Q9M5K3 (DLDH1_ARATH), "Dihydrolipoyl dehydrogenase 1, mitochondrial"
  (AtmLPD1, mtLPD1), EC 1.8.1.4; gene LPD1, locus At1g48030. AltName "Glycine
  cleavage system L protein 1".
- The folder is named `mtLPD1` because the symbol LPD1 is also used for the
  plastid E3 proteins (ptLPD1/ptLPD2). Everything here is about the
  mitochondrial At1g48030 protein.
- Mitochondrial paralog: mtLPD2, At3g17240 (UniProt Q9M5K2); reviewed in
  `genes/ARATH/mtLPD2/`. The two share 94% identity
  [PMID:11743115 "These predicted proteins are identical in length (507 amino acids) and share 94% identity at the amino acid level."].
- In the Rostock (Bauwe/Timm) nomenclature, mtLPD1 is GDC-L1
  [PMID:31413204 "GDC-L1 (mtLPD1; At1g48030), GDC-L2 (AT3G17240)"]. The
  "GCS-L1" of the Wittmiss et al. 2020 stoichiometry paper (same group) is taken
  to be the same protein; the cached abstract does not give the locus.
- Mitochondrial transit peptide 1..36 (cleavage after Phe-36 determined
  experimentally, UniProt ECO:0000269 PubMed:25732537, 25862457); class-I
  pyridine nucleotide-disulfide oxidoreductase family; FAD/NAD binding sites and
  redox-active disulfide 82-87 (by similarity).

## Biochemical function

- Dihydrolipoyl dehydrogenase (E3, L protein): reoxidizes protein-bound
  dihydrolipoamide using NAD+ via FAD (UniProt CATALYTIC ACTIVITY, RHEA:15045)
  [PMID:22303256 "This reaction is catalyzed by L-protein, a homodimeric dihydrolipoamide dehydrogenase (EC 1.8.1.4). Electrons are first transferred to the co-factor FAD that is re-oxidized by NAD + resulting in the formation of NADH"].
- Direct biochemistry on the Arabidopsis protein: recombinant mtLPD1 was
  characterized and is inhibited by NADH and redox-regulated by thioredoxins
  (abstract only)
  [PMID:38518065 "biochemical analysis of recombinant mtLPD1 supported this. It also revealed mtLPD1 inhibition by NADH"].
  A methods chapter describes expression, purification, activity and redox
  regulation of plant mtLPD1 (abstract only) [PMID:38861078].
- Note: the recombinant L protein in the TRXo1 paper (PMID:31413204) was the pea
  enzyme (PsmtLPD), not At1g48030.

## Multienzyme complexes served

- Mitochondrial E3 is shared by four complexes: GDC, pyruvate dehydrogenase,
  2-oxoglutarate dehydrogenase and branched-chain 2-oxoacid dehydrogenase
  [PMID:38861078 "its function is required to drive four multienzymes involved in photorespiration, the tricarboxylic acid (TCA) cycle, and the degradation of branched-chain amino acids"].
- Leaf GDC stoichiometry by MS (abstract only): the Arabidopsis leaf complex
  contains four times more L1 than L2
  [PMID:32311173 "The Arabidopsis GDC contains four times more of the isoforms GCS-P1 and GCS-L1 in comparison with GCS-P2 and GCS-L2"].
  This is the most direct protein-level evidence that mtLPD1 is the main leaf GDC
  L protein.
- In non-photosynthetic cell-culture mitochondria, both proteins were identified
  but mtLPD2 was more abundant (AAF34795 is the mtLPD1 cDNA, EMBL AF228639)
  [PMID:11743115 "Further, it appears there is significantly more Q9 M 5K2 than AAF34795 protein in our mitochondrial samples"].

## Expression

- mtLPD1 mRNA is high in green leaves and low in roots, and strongly
  light-induced; mtLPD2 shows the inverse organ pattern (abstract only)
  [PMID:11598235 "mtLPD1 had higher RNA levels in green leaves compared with the much lower level in roots"]
  [PMID:11598235 "Analysis of etiolated seedlings transferred to light showed a strong induction of RNA expression for mtLPD1 but only a moderate induction of mtLPD2"].
- From this the authors hypothesized the division of labour, while assuming
  interchangeability in the matrix
  [PMID:11598235 "we hypothesize that mtLPD1 encodes the protein most often associated with the Gly decarboxylase complex, and mtLPD2 encodes the protein incorporated into alpha-ketoacid dehydrogenase complexes"]
  [PMID:11598235 "we assume that the proteins, once in the mitochondrial matrix, are interchangeable among the different multienzyme complexes"].
  The 2001 paper characterized only an mtlpd2 knockout, not an mtlpd1 mutant.

## Genetic evidence for photorespiration

- Liu et al. 2026 (abstract only; no PMC full text) characterized loss-of-function
  mutants for both mtLPDs: mtLPD1 has the predominant role in photorespiration,
  the two are largely redundant for BCAA degradation in carbon starvation, and
  both act dose-dependently in gametophyte development
  [PMID:41990722 "While the two mtLPDs both contribute to photorespiration, mtLPD1 plays a more predominant role, especially under high-light stress."]
  [PMID:41990722 "the two mtLPDs are largely functionally redundant in BCAA degradation during carbon starvation"]
  [PMID:41990722 "we uncovered a critical and dose-dependent role for both mtLPDs in male and female gametophytic development"].
  Allele identities, the high-light assay and whether gametophyte defects require
  combined loss cannot be checked from the abstract.
- Overexpression of the GDC L protein (Timm et al. 2015; abstract only) increased
  CO2 assimilation, photorespiration and growth
  [PMID:26116608 "Additionally, increased rates of CO2 assimilation, photorespiration, and plant growth were observed."].
  The 2015 abstract does not name the transgene. The 2025 follow-up calls the lines
  mtLPD1 overexpressors, but designates them "PsL-L2 and PsL-L3"
  [PMID:40032651 "two previously characterized glycine decarboxylase (GDC) L‐protein (mtLPD1; EC:1.8.1.4.) overexpression lines (designated as PsL‐L2 and PsL‐L3)"],
  which suggests (not verified here) a pea L-protein transgene. Gain-of-function
  data therefore show that L-protein activity limits photorespiratory flux, but
  are not evidence about the endogenous At1g48030 gene specifically.
- Thioredoxin o1/h2 mutants: metabolite patterns point at mtLPD1-dependent
  pathways (PMID:38518065).

## Localization

- Mitochondrial matrix (UniProt, ECO:0000269 PubMed:14671022). Found in
  mitochondrial proteomes (PMID:11743115, 14671022, 17137349, 18385124, 22923678,
  25293756).
- Complex I (IDA, PMID:20197505): the authors list lipoamide dehydrogenase among
  contaminants of their complex I preparation
  [PMID:20197505 "a few contaminating proteins like prohibitin, the β-subunit of ATP synthase (complex V), Ser hydroxymethyltransferase, and lipoamide dehydrogenase"].
- NOT Golgi (RCA, PMID:22430844): consistent with matrix location.
- Nucleus (HDA, PMID:28887381) and apoplast (HDA, PMID:18538804): single
  high-throughput hits for a matrix protein; treated as over-annotations per
  `projects/ARATH/organelle-audit.md`.

## Ligand-affinity proteomics

- Cu/Zn/Co IMAC (PMID:20018591) and immobilized-ATP capture (PMID:17137349): not
  physiological ligands of LPD (FAD and NAD+ are). Same treatment as mtLPD2.

## Stress responses

- Cadmium (IEP, PMID:20005002): leaf 2D-gel proteome; abstract only, and the
  abstract does not name the LPD spot or say how the 94%-identical paralogs were
  distinguished. Not verifiable here.

## Comparator check for GDC/photorespiration terms (QuickGO, 2026-10-20)

- GO:0009853 photorespiration in Arabidopsis is carried by other C2-cycle
  enzymes (SHM1, GLYK, HPR, GGAT1, PLGG1...) but by no GDC subunit in GOA; the
  sibling reviews GLDP1, GLDP2, GDCST and GDCH each added NEW photorespiration.
- L proteins in other species do carry GCS terms: pea mitochondrial LPD P31023
  has GO:0005960 glycine cleavage complex (IDA) and GO:0019464 (IDA); yeast LPD1
  P09624 has GO:0005960 (IMP), GO:0006546 (IMP) and GO:0019464 (RCA). So no
  convention excludes the shared E3 from GCS annotations.
- Participation: the L protein catalyses the last step of the GCS cycle
  (reoxidation of the H-protein dihydrolipoyl arm), so it does part of the work
  of glycine decarboxylation and hence of photorespiration.

## Module cross-check

- `modules/photorespiration_c2_cycle.yaml` says "The leaf L protein is mainly
  mitochondrial LPD1 (mtLPD1, At1g48030, UniProtKB:Q9M5K3)". Supported by: leaf
  GDC stoichiometry (L1 4x L2, PMID:32311173, isoform mapping by group
  nomenclature), leaf-enriched and light-induced expression (PMID:11598235), and
  the mutant analysis showing mtLPD1 predominant in photorespiration
  (PMID:41990722). Both proteins are in the complex, so "mainly" is the right word.
  The module currently cites only the expression hypothesis (PMID:11598235) and
  the methods-chapter statement (PMID:38861078); PMID:32311173 and PMID:41990722
  are stronger evidence that could be added there.
- `modules/glycine_cleavage_system.yaml` L-protein role uses GO:0004148 with
  non-plant representatives; consistent with the MF here.
