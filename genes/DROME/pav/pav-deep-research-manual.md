# pav (Pavarotti, Pav-KLP; Drosophila melanogaster; UniProt Q9VZF5) - manual literature synthesis

No deep-research API provider was available for this session. This file is a manual
synthesis written by the reviewer from cached publications (`publications/PMID_*.md`)
and PubMed searches. Every claim carries inline provenance.

## Identity and family

- Gene: pavarotti (pav), CG1258, FlyBase FBgn0011692, NCBI GeneID 38515. UniProt Q9VZF5 is an
  unreviewed (TrEMBL) entry of 887 aa.
- Kinesin-6 / MKLP1 (KIF23) family. UniProt: "Belongs to the TRAFAC class myosin-kinesin ATPase
  superfamily. Kinesin family." The entry carries Pfam PF00225 (Kinesin motor) and PF16540
  (MKLP1_Arf_bdg, the KIF23 Arf6-binding domain), and PANTHER PTHR24115:SF600 "KINESIN-LIKE
  PROTEIN KIF23".
- "pav encodes a kinesin-like protein, PAV-KLP, related to the mammalian MKLP-1"
  [PMID:9585508 "pav encodes a kinesin-like protein, PAV-KLP, related
  to the mammalian MKLP-1"].

## Centralspindlin and cytokinesis (core function)

- Pav-KLP with RacGAP50C/Tumbleweed forms the centralspindlin complex
  [PMID:21187330 "the evolutionarily conserved centralspindlin complex, which is composed of a plus end–directed kinesin 6 protein, dubbed MKLP1 in mammals and Pavarotti kinesin-like protein (Pav-KLP) in Drosophila melanogaster"].
  Affinity purification from S2 cells: "Pav-KLP pulled down RacGAP50C and vice versa" [PMID:21187330].
- pav mutants: "cells of pav mutant embryos undergo normal anaphase but then develop an abnormal
  telophase spindle and fail to undertake cytokinesis"; Peanut, actin and Anillin mislocalize
  [PMID:9585508].
- RNAi in S2 cells disrupts cytokinesis [PMID:12134082]; Pav is "essential for central spindle
  bundling during cytokinesis" [PMID:15958489].
- RacGAP50C-Pav complexes are proposed to travel on cortical microtubules to the equator and
  link to the RhoGEF Pebble [PMID:12530961 "RacGAP50C and its binding partner, the Pavarotti
  kinesin-like protein, regulate microtubule bundling"].
- Centralspindlin is required to maintain (not to initially recruit) myosin II at the furrow
  [PMID:16174742].
- Live imaging of GFP-Pav-KLP: spindle, midzone, cortex and cleavage furrow; an ATP-binding
  (motor-dead) mutant fails to reach cortex/midzone and causes furrow formation failure; nuclear in
  interphase via C-terminal NLS elements dispensable for division [PMID:14517316].
- Cdk1 (Cdc2) phosphorylation sites near the motor domain prevent precocious midzone association
  [PMID:15958489].
- Dynactin promotes targeting of Pav-KLP to microtubule plus ends at anaphase onset [PMID:17046997].
- Polo kinase associates with Pav-KLP; in polo mutant spermatocytes Pav-KLP fails to relocalize to
  the midzone [PMID:9585508; PMID:9813088].

## Ring canals (arrested cytokinesis)

- In male meiosis Pav-KLP "persists to become incorporated into the 15 ring canals of the primary
  spermatocyte cyst" and is also seen on some immature axonemes [PMID:9813088].
- Pav-KLP is a stable component of somatic (follicle cell, imaginal disc) ring canals and also
  localizes to germline ring canals in the germarium [PMID:22135360].
- Nesd is a centralspindlin partner at the midbody ring / ring canals [PMID:21187330].

## Post-mitotic and nuclear roles

- Neurons: Pav-KLP inhibits kinesin-1-driven microtubule-microtubule sliding; depletion increases
  neurite outgrowth and causes axon overextension [PMID:25557664]. Trc (NDR kinase) phosphorylates
  Pav at S745, promoting 14-3-3 binding, which is needed for Pav to brake sliding; Pav RNAi
  increases dendritic length but not branch number [PMID:32022690].
- Muscle: pav mutants mislocalize RacGAP50C and gamma-tubulin during myotube extension
  [PMID:19297411]; Polo/Tum/Pav act in a common pathway for myotube guidance [PMID:35140224].
- Wnt: Tum and Pav accumulate in interphase nuclei and restrict Wnt target-gene activity downstream
  of beta-catenin stabilization [PMID:20516152] (abstract only cached).
- pav was first recovered in a PNS-pattern screen (enlarged cells due to cytokinesis failure)
  [PMID:8060613; PMID:9585508].

## Open questions

- Direct in vitro motility (direction, velocity) of Pav-KLP has not been reported in the cached
  literature; plus-end directionality is inferred from MKLP1/ZEN-4.
- Mechanism of the nuclear Wnt role (chromatin or transcription-factor partners) is unknown.
