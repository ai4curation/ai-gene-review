# Ctnnb1 (rat, UniProt Q9WU82) - manual literature synthesis

No deep-research API was available for this review. This file is a manual
synthesis from the cached publications in `publications/`, the UniProt record
(`Ctnnb1-uniprot.txt`) and the existing human (`genes/human/CTNNB1`) and mouse
(`genes/mouse/Ctnnb1`) reviews. Quotes are verbatim from the cited source.

## Identity and family

- Rat beta-catenin, 781 aa, Swiss-Prot reviewed, RGD:70487, GeneID 84353.
  "Belongs to the beta-catenin family" (UniProt Q9WU82, SIMILARITY).
- Twelve armadillo (ARM) repeats (FT REPEAT 151..666; InterPro IPR013284
  Beta-catenin; Pfam PF00514 Arm). The ARM superhelix is the binding platform
  for cadherins, TCF/LEF factors, APC and Axin: "As a component of adherens
  junctions and the Wnt signaling pathway, beta-catenin binds cadherins, Tcf
  family transcription factors, and the tumor suppressor APC"
  [PMID:11348595]. The cadherin interaction "spans all 12 arm repeats"
  [PMID:11348595].
- The N-terminal region binds alpha-catenin: "although the amino-terminal half
  independently binds alpha-catenin" [PMID:7890674].

## Molecular functions

1. **Cadherin binding / adherens-junction scaffold.** UniProt: "Involved in the
   regulation of cell adhesion, as component of an E-cadherin:catenin adhesion
   complex" (By similarity). In rat tissue: "An anti-N-cadherin antibody can pull
   out beta-catenin, whereas N-cadherin can also be pulled out using an
   anti-beta-catenin antibody" (Sertoli-germ cell junctions) [PMID:12533412].
   Rat adult cardiomyocytes form "two distinct and separable N-cadherin/catenin
   complexes" in which N-cadherin and alpha-catenin "bind to either beta-catenin
   or plakoglobin in a mutually exclusive manner" [PMID:8834786]. The atypical
   cadherin Fat1 binds beta-catenin in rat VSMCs [PMID:16682528].
2. **alpha-catenin binding.** Rat epididymis immunoprecipitation (RGD IPI,
   PMID:12960056) and the structural work above [PMID:7890674].
3. **Transcription coactivator for TCF/LEF.** UniProt: "In the presence of Wnt
   ligand, CTNNB1 is not ubiquitinated and accumulates in the nucleus, where it
   acts as a coactivator for transcription factors of the TCF/LEF family, leading
   to activate Wnt responsive genes". "hTcf-4 transactivates transcription only
   when associated with beta-catenin" [PMID:9065401]; beta-catenin is "a
   dedicated coactivator of LEF/TCF" [PMID:11751639]; "Stimulation of the Wnt
   pathway leads to the association of beta-catenin with Tcf and BCL9 in the
   nucleus" [PMID:17052462]. In rat uterus, "Beta-catenin binding to TCF/LEF
   increased (P<0.05) in progesterone-pretreated uteri in response to estradiol"
   [PMID:17170212].
4. **Regulated substrate of the destruction complex.** UniProt: "In the absence
   of Wnt, forms a complex with AXIN1, AXIN2, APC, CSNK1A1 and GSK3B that
   promotes phosphorylation on N-terminal Ser and Thr residues and
   ubiquitination of CTNNB1 via BTRC". Rat Axin: "rAxin also interacted directly
   with the armadillo repeats of beta-catenin" and "rAxin promoted
   GSK-3beta-dependent phosphorylation of beta-catenin" [PMID:9482734].
   Beta-catenin is the **substrate** of phosphorylation, ubiquitination and
   proteasomal degradation, not an executor of those processes.

## Rat-specific cell biology (mostly abstracts)

- Smad3/Smad4 stabilise beta-catenin and promote its nuclear translocation in
  rat RCJ3.1C5.18 chondrogenic cells: "the formation of the Smad3-Smad4-beta-catenin
  protein complex also mediated beta-catenin nuclear translocation" [PMID:20097766].
- Mechanical strain in rat UMR-106 osteoblast-like cells activates beta-catenin
  through IGF-IR/PI3K/AKT, independent of Wnt/LRP5: "there is rapid PI3K-mediated
  activation of AKT, AKT-mediated inhibition of GSK-3β, and increased levels of
  active nuclear β-catenin"; "the majority of active β-catenin is in the
  cytoplasm, concentrated in the perinuclear area" [PMID:20042609].
- Neurons: beta-catenin "moves from dendritic shafts into spines upon
  depolarization, increasing its association with cadherins" [PMID:12123611];
  GSK-3beta "phosphorylates beta-catenin and disrupts beta-catenin-NR2B
  interaction" in rat prefrontal cortex [PMID:20007479]; FGF1 causes "beta-catenin
  translocation into the nucleus" in rat neurons [PMID:12095987].
- Schwann cells: "beta-catenin reduction inhibited axon-contact-dependent SC
  proliferation" [PMID:17941050].
- Testis: NOS2/NOS3 "were structurally associated with the N-cadherin
  (CDH2)/beta-catenin (CATNB)/actin complex" [PMID:15858215].
- Epididymis: beta-catenin at "the lateral plasma membranes (LPM)" and ZO-1
  "coprecipitates with beta-catenin at the level of the apical tight junctions"
  [PMID:12960056].
- Many rat IEP annotations (liver, midgut, epididymis, bone, hormone, cadmium,
  zinc, exercise responses) rest on changes in beta-catenin level or
  localisation, not on loss-of-function data.
- Rat colon tumours induced by heterocyclic amines carry activating Ctnnb1
  mutations at the N-terminal phosphorylation sites [PMID:9515794].

## Interpretation

Rat beta-catenin has two core activities, conserved with human and mouse:
(i) an armadillo-repeat scaffold that binds cadherin cytoplasmic tails and
alpha-catenin in the cadherin-catenin complex at adherens junctions, and
(ii) a TCF/LEF-binding transcriptional coactivator, the nuclear effector of
canonical Wnt signalling, whose abundance is set by destruction-complex
phosphorylation and BTRC-mediated ubiquitination. The large set of
developmental process annotations (almost all ISO from mouse) are downstream,
context-dependent consequences of Wnt/beta-catenin transcription.
