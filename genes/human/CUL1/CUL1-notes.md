# CUL1 (Cullin-1, UniProt Q13616) — curation notes

## Working picture of the gene

CUL1 is the cullin scaffold of the SCF (SKP1–CUL1–F-box protein) family of cullin-RING
ubiquitin ligases (CRL1). It is not an enzyme: it is an elongated, rigid platform whose
N-terminal stalk (three cullin repeats) binds the SKP1 adaptor, which in turn carries one of
~70 interchangeable F-box substrate receptors, while its C-terminal globular domain binds the
RING protein RBX1, which recruits ubiquitin-charged E2s (CDC34/UBE2R, UBE2D) or the RBR E3
ARIH1. [PMID:11961546 "Cul1 serves as a rigid scaffold that organizes the Skp1-F boxSkp2 and Rbx1
subunits, holding them over 100 A apart"] [PMID:15520277 "The CUL1/RBX1 complex functions as a
scaffold to assemble the E2 ubiquitin conjugating enzyme with the substrate specificity mod"].

Key mechanistic facts used in the review:

- Scaffold/positioning contribution to catalysis, no covalent ubiquitin intermediate on CUL1.
  [PMID:11961546 "The structure suggests that Cul1 may contribute to catalysis through the positioning
  of the substrate and the ubiquitin-conjugating enzyme"]
- Processivity: the CUL1 "basic canyon" binds the acidic tail of the E2 CDC34 with nanomolar
  affinity but rapid on/off kinetics. [PMID:19945379 "rapid association driven by electrostatic
  interactions between the acidic tail of Cdc34 and a basic 'canyon' in the Cul1 subunit of SCF"]
- Activation by NEDD8 conjugation (Lys720), which reorients the WHB/RBX1 RING module and
  removes the CAND1-binding site. [PMID:18805092 "In NEDD8ylated CRL structures, the cullin WHB and
  Rbx1 RING subdomains are dramatically reoriented, eliminating a CAND1-binding site and imparting
  multiple potential catalytic geometries to an associated E2"]; autoinhibition by the CUL1 extreme
  C-terminal domain [PMID:18723677 "deletion of ECTD, or missense mutations designed to disrupt the
  predicted ECTD x ROC1 interaction, markedly increased the ability of SCF(betaTrCP2) to promote
  IkappaB alpha polyubiquitination"].
- CAND1 binds unneddylated CUL1, blocks SKP1 binding and drives F-box exchange.
  [PMID:12504026 "CAND1 prevents the binding of SKP1 and SKP2 to CUL1 while dissociation of CAND1 from
  CUL1 promotes the reverse reaction"] [PMID:15537541 "Cand1, a 120 kDa HEAT repeat protein, forms a
  tight complex with the Cul1-Roc1 SCF catalytic core, inhibiting the assembly of the multisubunit E3
  complex"]. Deneddylation by the COP9 signalosome.
- Neddylated CUL1–RBX1 also recruits and activates the RBR E3 ARIH1 (tandem SCF/ARIH1
  ubiquitination). [PMID:24076655 "binding of the cognate neddylated CRL to TRIAD1 or HHARI greatly
  stimulates RBR ligase activity in vitro"]
- Neddylated CUL1–RBX1 serves as the catalytic module of the CUL7–FBXW8 assembly.
  [PMID:35982156 "our data indicate that CRL7 serves as a substrate receptor linked via SKP1-FBXW8 to a
  neddylated CUL1-RBX1 catalytic module mediating ubiquitination"]
- Alternative RING partner TRIM21/Ro52 in an SCF(SKP2)-like p27 ligase. [PMID:16880511 "we
  identify Skp2 as a component of an Skp1-cullin-F-box complex that is based on a Cul1-Ro52 RING finger
  B-box coiled-coil motif family protein catalytic core"]

Canonical outputs (F-box receptor → substrate): SKP2 → p27/CDKN1B, p21, p130 (G1/S);
beta-TrCP (BTRC/FBXW11) → IkappaB-alpha, beta-catenin, EMI1, CDC25A, DEPTOR, MDM2, TFE3/MITF;
FBXW7 → cyclin E, MYC, NOTCH, WDR5; cyclin F → CP110, RRM2, E2F1; FBXL3/FBXL21 → CRY1/2;
FBXL5 → IRP2; FBXO9 → TEL2/TTI1, PRMT4; FBXW5 → SAS-6, MCAK; FBXO31 → C-terminally amidated
proteins; FBXL4 → NIX/BNIP3; FBXO2 → glycosylated bacterial surface (xenophagy).

## Curation decisions

- **Core**: GO:0160072 ubiquitin ligase complex scaffold activity (IBA + 7 IDA + IEA) with
  `contributes_to` GO:0061630 ubiquitin protein ligase activity; GO:0019005 SCF complex;
  GO:0031146 SCF-dependent proteasomal catabolism; GO:0016567 / GO:0070936 ubiquitination;
  GO:0000082 G1/S transition (the SCF(SKP2)–p27 switch; CUL1 is the cullin exemplar in
  `modules/g1_s_transition.yaml`); nucleus / nucleoplasm / cytosol / cytoplasm.
- **GO:0005515 protein binding (140 IPI rows)**: repository policy — resolve to an informative
  MF when the paper supports one, otherwise REMOVE as uninformative (not a claim the interaction
  is false). Decided per paper so that actions on one reference are consistent:
  - Papers demonstrating CUL1 organizing SKP1/F-box/RBX1 (or an SCF substrate bound through
    them) → MODIFY to GO:0160072.
  - CDC34 (PMID:19945379) → MODIFY to GO:0031624 ubiquitin conjugating enzyme binding.
  - ARIH1 (PMID:24076655) → MODIFY to GO:0031625 ubiquitin protein ligase binding.
  - Papers in which CUL1 is only the *target* of a regulator (CAND1-only, NEDD8 E2/DCUN1D
    neddylation-mechanism, COMMD/CCDC22, UBXN7, COPS9, HSP90, viral hijack) or high-throughput
    interactome screens (BioPlex, DUB/ISG/PcG/TF/CFTR maps, PLA screen) → REMOVE as uninformative.
- **Pathway-output process terms** (NAS/IDA rows for circadian rhythm, iron homeostasis, BMP,
  TOR, NF-kB, inflammation, centrosome, mitophagy, xenophagy, DNA-damage checkpoint, oxidative
  stress, mitotic-cell-cycle regulation): each is the output of one F-box receptor; CUL1 is the
  shared scaffold, so KEEP_AS_NON_CORE.
- **MARK_AS_OVER_ANNOTATED**: GO:0060173 limb development (mouse Dac/Fbxw4 phenotype, no CUL1
  data), GO:0014033 neural crest differentiation (SCF(FBXL17) developmental phenotype),
  GO:0042981 regulation of apoptotic process (two steps removed), GO:0006355 regulation of
  transcription (SCF(FBXL14) degrades a Pol I subunit), GO:0097193 intrinsic apoptotic signaling
  (C. elegans cul-1 hyperplasia phenotype / ARBA propagation).
- **MODIFY**: GO:0051298 centrosome duplication (NAS, PMID:34388369) — the cited paper is the
  signal peptidase complex structure and does not mention CUL1 (WRONG_IDENTIFIER); the biology
  (SCF(FBXW5)–SAS-6, SCF(cyclin F)–CP110) supports GO:0010824 regulation of centrosome
  duplication instead. GO:0060271 cilium assembly → GO:1902017 regulation of cilium assembly
  (SCF(FBXW5) degrades MCAK to permit ciliogenesis; the scaffold does not build the cilium).
- **GO:0005886 plasma membrane (IDA, PMID:19617556)**: DCNL3 recruits cullins to membranes;
  cached abstract discusses CUL3, but the curator read the full text — KEEP_AS_NON_CORE.
- **GO:1990452 Parkin-FBXW7-Cul1 complex (IPI, PMID:12628165)**: single-study complex; kept as
  non-core with a question for experts.
- IBA rows (nucleus, protein ubiquitination, SCF complex, SCF-dependent catabolism, ubiquitin
  protein ligase binding, scaffold activity) all ACCEPTED; they match the human experimental data.

## Reference problems found

- PMID:34388369 is "Structure of the human signal peptidase complex" — mis-cited for centrosome
  duplication (flagged WRONG_IDENTIFIER in `reference_review`).
- PMID:35414786 and PMID:36135912 are general reviews (tumour metastasis; mitochondrial
  dynamics) cited as NAS support; relevance LOW.
- PMID:22479149 (yeast Mediator/Gal4) supports an IPI with MED6; the cached abstract is about
  S. cerevisiae — row removed as uninformative, not as false.
