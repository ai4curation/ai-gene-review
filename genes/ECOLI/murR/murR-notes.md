# murR (yfeT, b2427, P77245) notes

## 2026-10-31 — initial review

No deep-research file; literature gathered from the publication cache, PubMed/PMC and
the UniProt record. Papers read: PMID:18723630 (full text), PMID:35640608 (full text),
PMID:19897902 (abstract only).

### Identity and locus
- RpiR/AlsR-family (COG1737, PTHR30514:SF17) regulator: N-terminal HTH_RpiR domain
  (1-77) and C-terminal SIS domain (128-268) (UniProt P77245).
- murR is divergent from murQP; the murQ and murR promoters face each other inside the
  intergenic region ("nonoverlapping face-to-face (convergent) promoters")
  [PMID:18723630 "murR and murQ are divergently orientated and expressed from nonoverlapping face-to-face (convergent) promoters"].

### Repression (in vivo)
- Deleting murR shortens the lag on MurNAc about sixfold and the doubling time about
  twofold [PMID:18723630 "Hence, inactivation of murR markedly increases growth on MurNAc, indicating that MurR functions as a repressor of the MurNAc pathway."].
- Chromosomal murQ-lacZ is 20-fold higher in ΔmurR [PMID:18723630 "a 20-fold increase in β-galactosidase activity was determined for murQ-lacZ in TJ105 (Δ murR ) compared to the wild-type background (TJ107)"].
- Independently confirmed by RT-qPCR in MG1655: ΔmurR raises murQ, murP and pbp4B
  transcripts [PMID:35640608 "the deletion of murR evidently increased the transcription levels of all three genes"].
  So pbp4B (downstream of murP) is also MurR-controlled.
- Autoregulation: MurR represses murR (murR-lacZ only detectable in ΔmurR)
  [PMID:18723630]; PMID:19897902 additionally reports MurR-dependent stimulation of murR
  in rich medium involving several PTS EIIBC components (abstract only; mechanism unclear).

### Direct, sequence-specific DNA binding
- EMSA with purified MurR: half-shift of the 363 bp intergenic fragment at 2 nM; only
  reg III (the fragment carrying IR1/IR2) is shifted, not flanking fragments
  [PMID:18723630 "reg III, but not reg II or reg IV, was retarded by binding to MurR"].
- DNase I footprint: single protected region centred at −29 relative to PQ1 covering
  IR1 and IR2, overlapping the murQ −10/−35 elements [PMID:18723630].
- Cell-free (CFPS) eGFP reporter: MurR represses only when the murR-murQ intergenic
  region is inserted [PMID:35640608 "This result demonstrated that MurR could efficiently and specifically regulate the expression of eGFP."].
- Oligomer: tetramer by gel filtration/DLS [PMID:18723630] and by SEC and sedimentation
  velocity [PMID:35640608 "MurR forms a tetramer (125 KDa) rather than a dimer (62 KDa) in solution"].
- cAMP-CAP binds a weak class I site upstream of the murQ promoter and activates murQ;
  MurR and CAP can bind simultaneously [PMID:18723630].

### Effector
- MurNAc-6P releases MurR from operator DNA (EMSA, half-release at 14 µM in
  PMID:18723630; ~400 µM under the different conditions of PMID:35640608).
- ITC: MurNAc-6P Kd 4.3 µM, 1:1 [PMID:35640608].
- Crystal structures: apo (7EN6), MurNAc-6P (7EN7) and GlcNAc-6P (7EN5) complexes of
  the SIS domain; ligand pocket formed by three subunits; S146, K159, H171, S190, S192,
  K195 mutants lose MurNAc-6P response in vitro and grow poorly on MurNAc in vivo
  [PMID:35640608].
- **GlcNAc-6P: the two papers disagree on binding but agree on function.**
  PMID:18723630 saw no effect of GlcNAc-6P (up to 5 mM) on MurR-DNA binding.
  PMID:35640608 shows GlcNAc-6P does bind (ITC Kd 17.6 µM) and at very high
  concentration (40 mM) partially disrupts the MurR-DNA complex, but it does not relieve
  repression in the CFPS reporter or in cells
  [PMID:35640608 "Taken together, in the tested conditions, MurNAc-6-P, but not GlcNAc-6-P, could alleviate the binding of MurR with the operator DNA."].
  Conclusion: MurNAc-6P is the physiological inducer; GlcNAc-6P is a weak binder, not an
  inducer.

### GO term notes
- GO:0097173 N-acetylmuramic acid catabolic process is classified under carboxylic acid
  catabolic process, not under carbohydrate catabolic process or amino sugar catabolic
  process. So GO:0043470 "regulation of carbohydrate catabolic process" is not an
  ontological ancestor of a regulation of MurNAc catabolism term.
- GO has GO:0160159 positive regulation of N-acetylmuramic acid catabolic process only;
  no negative or unsigned term. Same NTR as the ybbH review.
- UniProt PATHWAY reads "N-acetylmuramate degradation [regulation]"; the UniPathway2GO
  IEA (GO_REF:0000041) for GO:0097173 dropped the [regulation] qualifier.

### Bearing on genes/BACSU/ybbH
- E. coli evidence fully supports repression, direct sequence-specific operator binding
  and MurNAc-6P as the effector (with structures and mutants since 2022).
- PMID:35640608 shows GlcNAc-6P binds E. coli MurR in vitro; the ybbH suggested
  experiment that includes GlcNAc-6P is well motivated, but the ybbH text does not claim
  otherwise.
- PMID:35640608 lists B. subtilis among species with MurR-like regulators (gene
  neighbourhood) but does no B. subtilis experiment.
