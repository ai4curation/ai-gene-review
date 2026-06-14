# FKF1 (ADO3, At1g68050; UniProt Q9C9W9) — Gene Review Notes

## Overview / identity

FKF1 = FLAVIN-BINDING, KELCH REPEAT, F-BOX 1 (also ADAGIO 3 / ADO3, FBX2a). Member
of the Arabidopsis ZTL/ADO/LKP family (ZTL/ADO1, FKF1/ADO3, LKP2/ADO2), each with an
N-terminal LOV (PAS-type, flavin-binding) domain, a central F-box, and C-terminal Kelch
repeats forming a beta-propeller.

Domain architecture (UniProt Q9C9W9):
- PAS/LOV domain ~44-123, PAC 127-168
- F-box 211-257
- Kelch repeats 1-5 spanning ~304-571 (beta-propeller, substrate recognition)
- FMN chromophore covalently binds Cys-91 after blue light (S-4a-FMN cysteine); reversed in dark
  [UniProt PTM: "FMN binds covalently to cysteine after exposure to blue light and is reversed in the dark"]

## Core biology (synthesized)

FKF1 is a blue-light photoreceptor that acts as the substrate-recognition subunit (F-box)
of an SCF (SKP1-CUL1-F-box) E3 ubiquitin ligase. Its LOV domain senses blue light via an
FMN chromophore; light promotes formation of an FKF1-GIGANTEA (GI) complex, which is the
functional unit for substrate targeting. The SCF(FKF1)-GI complex degrades CYCLING DOF
FACTOR (CDF) transcriptional repressors (CDF1, CDF2, CDF3), relieving repression of
CONSTANS (CO) and FLOWERING LOCUS T (FT), thereby promoting photoperiodic (long-day)
flowering. FKF1 additionally stabilizes CO protein directly (via LOV/F-box) in the
long-day afternoon. FKF1 mRNA oscillates with a circadian rhythm, peaking in the late
afternoon; its coincidence with light in long days is the basis of day-length measurement.

## Key evidence by paper

- **PMID:10847687** (Nelson 2000, Cell; abstract-only cache). Cloned FKF1 from a
  late-flowering mutant; "encodes a novel protein with a PAS domain similar to the
  flavin-binding region of certain photoreceptors, an F box ... and six kelch repeats."
  "FKF1 mRNA levels oscillate with a circadian rhythm, and deletion of FKF1 alters the
  waveform of rhythmic expression of two clock-controlled genes, implicating FKF1 in
  modulating the Arabidopsis circadian clock." fkf1 is late-flowering. → supports
  positive regulation of flower development (IMP) and circadian rhythm (IMP).

- **PMID:14628054** (Imaizumi 2003, Nature; not cached, UniProt ref). FMN-binding at
  Cys-91; FKF1 essential for photoperiodic-specific light signalling; C91 mutagenesis.
  (UniProt FT: MUTAGEN 91 "C->A: No FMN binding and decreased interaction with GI.")

- **PMID:16002617** (Imaizumi 2005, Science; abstract-only). "FKF1 controls the stability
  of a Dof transcription factor, CYCLING DOF FACTOR 1 (CDF1). FKF1 physically interacts
  with CDF1, and CDF1 protein is more stable in fkf1 mutants." "FKF1 controls daily CO
  expression in part by degrading CDF1, a repressor of CO transcription." → substrate
  adaptor function; CDF1/2/3 binding (IPI). Disruption phenotype: late flowering.

- **PMID:17872410** (Sawa 2007, Science; abstract-only). "FKF1 and GI proteins form a
  complex in a blue-light-dependent manner. The timing of this interaction regulates the
  timing of daytime CO expression." "GI, FKF1, and CDF1 proteins associate with CO
  chromatin." LOV mutagenesis C91/R92/Q163 reduce GI interaction. → blue-light response
  (IDA), circadian rhythm (IDA), regulation of CO transcription (IDA, via degrading CDF1).
  Note GOA labels the IDA as GO:0006355 "regulation of DNA-templated transcription" — FKF1
  is not itself a transcription factor; it regulates transcription indirectly (acts_upstream).

- **PMID:22628657** (Song 2012, Science; FULL TEXT). FKF1 also stabilizes CO protein:
  "FKF1 interacts with CO through its LOV domain, and blue light enhances this interaction."
  "FKF1 also controls FT transcription by stabilizing CO protein and simultaneously
  degrading FT repressors in the long-day afternoon." CDF1 represses both CO and FT.
  F-box mutations (L214A/I223A that block ASK1 binding) attenuate blue-light effect on
  FKF1-CO interaction, "suggesting that the formation of the SCF(FKF1) complex facilitates
  the FKF1-CO protein interaction." GOA labels this IMP as GO:0010468 regulation of gene
  expression (acts_upstream_of_or_within) — consistent.

- **PMID:17704763** (Kim 2007, Nature; abstract-only). About ZTL, not FKF1, but
  establishes the family paradigm: ZTL is "a blue-light photoreceptor" whose "ZTL-GI
  interaction is strongly and specifically enhanced by blue light, through the
  amino-terminal flavin-binding LIGHT, OXYGEN OR VOLTAGE (LOV) domain." GOA's IPI
  GO:0005515 from this PMID is the FKF1-GI (Q9SQI2) interaction (per goa.tsv WITH/FROM
  UniProtKB:Q9SQI2). Supports FKF1-GI binding.

## SCF / ASK (SKP1) interaction papers (support F-box SCF adaptor role; "protein binding")

- **PMID:14749489** (Takahashi 2004, PCP; abstract-only). Y2H of ASKs vs F-box proteins:
  "ASK1, ASK2, ASK11 and ASK12 interacted well with COI1, FKF1, UFO-like protein..." GOA
  IPI WITH/FROM SKP1B(Q9FHW7) and SRK2G(P43292). Confirms FKF1 binds SKP1/ASK proteins →
  SCF complex assembly.
- **PMID:15310821** (Yasuhara 2004, JXB; abstract-only). LKP2 study; "LKP2 interacted not
  only with itself but also with other members of the family, LKP1 and FKF1." GOA IPI
  WITH/FROM SKP1B(Q9FHW7). Supports family/ASK interactions.
- **PMID:23166809** (Kuroda 2012, PLoS ONE; full text). Comprehensive ASK x F-box Y2H;
  "FBX proteins with a Kelch domain had high specificity to ASK13." GOA IPI WITH/FROM
  AT1G75950 (ASK2/SKP1B) and AT5G42190. Supports SCF assembly.
- **PMID:21798944** (Arabidopsis Interactome Consortium 2011, Science; abstract-only).
  Large-scale binary interactome. GOA IPI WITH/FROM SKP1B(Q9FHW7) and SRK2G(P43292).
  Background interactome; supports protein binding only generically.

All seven GO:0005515 "protein binding" (IPI) annotations are generic. Per curation
guidelines, bare "protein binding" is uninformative and should not be treated as a core
molecular function; the informative function is "molecular adaptor / SCF F-box
substrate-recognition" + "blue-light photoreceptor activity (FMN)". Mark these as
NON_CORE (KEEP_AS_NON_CORE) — they record real, useful interaction evidence but are not
core MF statements.

## Additional / pleiotropic functions

- **PMID:31221729** (Yuan 2019, Plant Physiol; abstract+partial full text). FKF1 is a
  negative regulator of cellulose biosynthesis: "The fkf1 mutants showed significant
  increases in cellulose content and CESA gene expression compared with that in wild-type
  Columbia-0 plants, suggesting a negative role of FKF1 in cellulose biosynthesis." IMP.
  Real but non-core / secondary role of this flowering photoreceptor. GO:2001007 negative
  regulation of cellulose biosynthetic process (acts_upstream_of_or_within).

- **PMID:36771626** (Yuan 2023, Plants Basel; full text). FKF1 interacts with CHUP1
  (C-terminus) via its F-box and regulates chloroplast photorelocation (avoidance
  response): "overexpression of FKF1 compromised the avoidance response, while the absence
  of FKF1 enhanced chloroplast movements under high light." "FKF1 regulates CHUP1 protein
  abundance through an unknown mechanism." IMP GO:0009902 chloroplast relocation. Real but
  non-core. (Mechanism — degradation vs. dimerization prevention — not established.)

## Localization

UniProt: "SUBCELLULAR LOCATION: Nucleus. Cytoplasm. Note=Moves from the nucleus into
cytosolic speckles upon interaction with ADO1 and ADO2." Song 2012 (PMID:22628657)
full text: "We found FKF1 in both cytosolic and nuclear fractions." Both nucleus and
cytoplasm/cytosol are supported. GOA has nucleus (IEA SubCell, ISM AtSubP) and cytoplasm
(IEA SubCell). UniProt DR also lists cytosol IBA:GO_Central.

## GO annotation assessment summary

Core: blue-light photoreceptor (FMN/LOV) → GO:0009881 photoreceptor activity (MF, missing
from GOA but in UniProt DR/keyword); SCF E3 substrate adaptor (F-box/Kelch) → SCF ubiquitin
ligase complex (GO:0019005, in UniProt DR IBA but not GOA) and ubiquitin-dependent protein
catabolism / protein ubiquitination; photoperiodic flowering (positive regulation of flower
development, regulation of CO/FT via CDF degradation), circadian rhythm, response to blue
light.

The GOA IPI "protein binding" terms are all kept as non-core (real evidence, uninformative
term). The two BP IEAs (circadian rhythm, response to blue light from ARBA) duplicate
experimental IDA annotations and are accepted/kept-as-non-core. No annotation warrants
REMOVE (all experimental annotations are biologically consistent; IEAs are not demonstrably
wrong). No UNDECIDED needed (all supporting publications were accessible at least at
abstract level and are consistent with well-established FKF1 biology).

GO:0006355 "regulation of DNA-templated transcription" (IDA, PMID:17872410): FKF1 is NOT a
transcription factor — it regulates CO/FT transcription indirectly by degrading the CDF
repressors and associating with CO chromatin. The acts_upstream_of_or_within qualifier is
appropriate, so the annotation is defensible; kept as non-core (the molecular event is
ubiquitin-mediated proteolysis, not direct transcription regulation).
</content>
</invoke>
