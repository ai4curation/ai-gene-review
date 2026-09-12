# sod-3 (C. elegans) — curation notes

UniProt: **P41977** (SODM2_CAEEL). WormBase: WBGene00004932 / C08A9.1. Chromosome X.
EC 1.15.1.1. 218 aa precursor with N-terminal mitochondrial transit peptide (1–24),
mature chain 25–218. Mn(2+) ligand residues 50, 98, 179, 183 (UniProt, by similarity).
7 PDB structures (e.g. 6S0D at 1.52 Å). PANTHER PTHR11404:SF6.

## One-line identity
sod-3 encodes the **DAF-16/FOXO-inducible, low-basal mitochondrial matrix manganese
superoxide dismutase (MnSOD)** of C. elegans; paralog of the constitutive, dominant
sod-2 (~86% identical protein). Classic DAF-16/insulin-signalling target gene and
widely used longevity reporter.

## KNOWN (well supported)
- **Mn-type superoxide dismutase activity** (EC 1.15.1.1). Mature SOD-3 protein
  expressed in SOD-deficient E. coli is an active dismutase; Mn-type identity shown
  by insensitivity to H2O2 and cyanide; dimeric. [PMID:9353332 "The expressed enzymes,
  which were not inhibited by hydrogen peroxide or cyanide, are dimeric, show quite
  different electrophoretic mobilities and isoelectric points, but exhibit comparable
  specific activities."] — NOTE: this paper cloned and assayed BOTH sod-2 and sod-3;
  the quote refers to both expressed enzymes, so it is genuinely sod-3-specific.
- **Removal of superoxide radicals** (protective against superoxide stress). Both
  MnSODs rescued paraquat/methyl-viologen sensitivity of SOD-null E. coli.
  [PMID:9353332 "Both proteins were shown to be active in E. coli, providing similar
  protection against methyl viologen-induced oxidative stress."] — evidence is
  heterologous complementation, not a worm sod-3 loss-of-function phenotype.
- **Mitochondrial localization.** UniProt subcellular location = Mitochondrion,
  ECO:0000269|PubMed:17894411 (Wolf et al. 2008); N-terminal mitochondrial transit
  peptide present in the deduced sequence. [PMID:9353332 "Both deduced protein
  sequences contain the expected N-terminal mitochondrial transit peptides."] The
  17894411 abstract itself does not state the mitochondrial localization (it is in the
  full text; abstract-only in cache), but UniProt cites it for SUBCELLULAR LOCATION.
- **Localizes to respiratory supercomplex I:III:IV.** By blue-native gel Western,
  SOD-3 co-migrates with the I:III:IV supercomplex. [PMID:23895727 "In addition, the
  results show that SOD-3 is also localized to the I:III:IV supercomplex."] This is the
  source of the WormBase IDA GO:0098803 (respiratory chain complex) annotation.
  Caveat: the anti-SOD-2 antibody cross-reacts with SOD-3 (Figure S2); the authors
  nonetheless conclude SOD-3 localizes to the supercomplex.
- **DAF-16/FOXO-inducible, low basal expression.** sod-3 is normally expressed at very
  low levels and is induced by DAF-16 (insulin/IGF-1 signalling). [PMID:23895727 "The
  activation of daf-16 increased expression of sod-3, an mtSOD normally expressed in
  very low levels in wild type worms"]. JNK-1 promotes DAF-16 nuclear translocation and
  sod-3 target-gene expression in peripheral tissue. [PMID:17894411 "a promoting
  influence of JNK-1 on both nuclear DAF-16 translocations and DAF-16 target gene
  (superoxide dismutase 3, sod-3) expressions within peripheral, non-neuronal tissue"].
- **Tissue expression (UniProt, from PMID:17894411 full text):** pharynx and rectum
  basally; on thermal stress also vulva, body-wall muscle, hypodermis. Induced by heat.
- **sod-3 single mutant lifespan = wild type.** [PMID:23895727 "the lifespan of sod-3
  was not different from N2 (Figure S1)"].
- **Non-redundant with sod-2 in ETC-mutant interactions.** [PMID:23895727 "the mutation
  sod-3 differed from sod-2 in its interactions with gas-1, mev-1 and isp-1."]
  Specifically: gas-1;sod-3 ≈ gas-1; mev-1;sod-3 shorter than mev-1; isp-1;sod-3 longer
  than isp-1. Complex I-dependent respiration decreased in sod-2 but NOT sod-3; sod-3
  BNGs normal. [PMID:23895727 "sod-3 BNGs were normal (Figure 5E)."]

## sod-3 vs sod-2 attribution (important)
- sod-2 (P31161): constitutive, quantitatively dominant mitochondrial MnSOD; loss lowers
  complex I/II activity, destabilizes supercomplex, and (counterintuitively) does not
  shorten / can extend lifespan.
- sod-3 (P41977): low-basal, DAF-16-inducible paralog; single-mutant lifespan normal;
  does not by itself decrease complex I respiration; also localizes to supercomplex and
  may be able to substitute for SOD-2's supercomplex-protective function when SOD-2 is
  absent. [PMID:23895727 "the lack of a large increase in ROS damage to supercomplexes
  in a sod-2 animal may indicate that SOD-3 is also capable of performing this function,
  especially when the amount of supercomplex I:III:IV is reduced."]
- PMID:9353332 assayed BOTH proteins → its enzymatic/complementation quotes apply to
  sod-3 as well as sod-2. PMID:23895727 has explicit sod-3-specific statements.

## NOT known / open
- Whether basal sod-3 (very low) contributes materially to matrix superoxide scavenging
  in the wild type, or whether it is essentially a stress-inducible reserve isoform.
- The mechanistic basis of the sod-2/sod-3 division of labour (substrate, sub-mito
  context, partner). Authors explicitly state this is under investigation.
  [PMID:23895727 "Studies are now being undertaken to characterize the interaction of
  sod3 with supercomplex I:III:IV formation."]
- Whether DAF-16-driven sod-3 induction is causally protective (extends life / raises
  stress resistance) or is chiefly a transcriptional MARKER of DAF-16 activity. In daf-2
  longevity, eliminating both mtSODs did not suppress the long lifespan, arguing sod-3
  induction is not required for daf-2 longevity [PMID:23895727 "elimination of both
  mitochondrial sod-2 and sod-3 failed to suppress the long life span of daf-2"].
- Whether SOD-3 is a catalytic scavenger or also a structural stabilizer of the
  supercomplex (catalysis-independent role), as proposed for the mtSODs generally
  [PMID:23895727 "it is also possible that the mtSODs may directly serve as stabilizing
  factors in the I:III:IV supercomplex"].

## GOA annotation inventory (12)
1. GO:0005739 mitochondrion — IBA — GO_REF:0000033 — is_active_in
2. GO:0004784 superoxide dismutase activity — IBA — GO_REF:0000033 — enables
3. GO:0030145 manganese ion binding — IBA — GO_REF:0000033 — enables
4. GO:0004784 superoxide dismutase activity — IEA — GO_REF:0000120 — enables
5. GO:0005739 mitochondrion — IEA — GO_REF:0000044 (SubCell) — located_in
6. GO:0006801 superoxide metabolic process — IEA — GO_REF:0000002 (InterPro2GO) — involved_in
7. GO:0046872 metal ion binding — IEA — GO_REF:0000002 (InterPro2GO) — enables
8. GO:0098803 respiratory chain complex — IEA — GO_REF:0000117 (ARBA) — part_of
9. GO:0098803 respiratory chain complex — IDA — PMID:23895727 — part_of
10. GO:0004784 superoxide dismutase activity — IDA — PMID:9353332 — enables
11. GO:0019430 removal of superoxide radicals — IMP — PMID:9353332 — involved_in
12. GO:0005739 mitochondrion — IDA — PMID:17894411 — located_in

## Planned actions (mirrors sod-2 modeling; PR #1711)
- SOD activity (IBA/IEA/IDA), manganese ion binding (IBA), mitochondrial matrix,
  removal of superoxide radicals = CORE. ACCEPT the experimental/phylogenetic calls.
- mitochondrion (generic) IBA/IEA/IDA → KEEP_AS_NON_CORE (matrix is the specific core CC).
- superoxide metabolic process (IEA) → KEEP_AS_NON_CORE (parent of removal of superoxide).
- metal ion binding (IEA) → KEEP_AS_NON_CORE (parent of manganese ion binding).
- respiratory chain complex part_of IEA (ARBA) → KEEP_AS_NON_CORE (over-generalized;
  SOD-3 associates with, not structural subunit of, the supercomplex).
- respiratory chain complex located_in IDA (PMID:23895727) → KEEP_AS_NON_CORE
  (real sod-3-specific supercomplex co-localization; peripheral association not core identity).

## Project note (not for the review file)
projects/CAEEL_MITOPHAGY.md line 76 mislabels sod-3 as "Fe-SOD"; it is a Mn-SOD
(UniProt "Superoxide dismutase [Mn] 2"; PMID:9353332). Out of scope for this PR.
