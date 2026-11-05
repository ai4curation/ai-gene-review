# drpr (Draper, Q9W0A0) curation notes

No deep-research provider output was available for this review; these notes were
assembled manually from Europe PMC searches (query `TITLE:draper AND drosophila`,
sorted by citations, 2026-10-26), the UniProt record and cached publications.

## Identity and architecture

- Single-pass type I transmembrane receptor (signal peptide 1-16, TM 801-821),
  extracellular EMI domain followed by many atypical EGF/laminin-EGF repeats;
  InterPro IPR042635 MEGF10/SREC1/2-like; sole fly homolog of MEGF10/11/12 and
  ortholog of C. elegans CED-1 [PMID:25111228 "drpr is the sole Drosophila homolog of the human genes MEGF10, MEGF11, and MEGF12 (JEDI, PEAR)"].
- Intracellular domain carries an NPxY motif (CED-6 adaptor) and an ITAM
  (Src42A phosphorylation, Shark recruitment)
  [PMID:18432193 "Drosophila Shark, a non-receptor tyrosine kinase similar to mammalian Syk and Zap-70, binds Draper through an immunoreceptor tyrosine-based activation motif (ITAM) in the Draper intracellular domain"];
  [PMID:23337816 "indicating a role of the motif NPxY, but not YxxL, in Draper-mediated phagocytosis"].
- Isoforms: Draper-I (B, displayed, activating, ITAM) vs Draper-II (A,
  ITIM-like, inhibitory via the phosphatase Csw)
  [PMID:22426252 "Draper-I promotes engulfment of axonal debris through an immunoreceptor tyrosine-based activation motif (ITAM). In contrast, Draper-II, an alternative splice variant, potently inhibits glial engulfment function."].

## Ligands (recognition)

- Phosphatidylserine, directly, via the EMI/NIM N-terminal region
  [PMID:23420848 "Draper is a phosphatidylserine-binding receptor for phagocytosis"].
  PS-coated beads alone trigger Draper microclusters and engulfment in S2 cells
  [PMID:30139739 "PS-ligated Draper forms dynamic microclusters that recruit cytosolic effector proteins"].
- PS bridging by the secreted chemokine-like Orion for neuron debris
  [PMID:37276397 "it is supplied cell-non-autonomously to coat PS-exposing dendrites and to mediate interactions between PS and Drpr"].
- Pretaporter (ER protein relocated to apoptotic cell surface)
  [PMID:19927123 "Pretaporter relocates from the endoplasmic reticulum to the cell surface during apoptosis to serve as a ligand for Draper"].
- S. aureus lipoteichoic acid [PMID:19890048 "lipoteichoic acid bound to the extracellular region of Draper"].

## Signalling

- Src42A -> Draper ITAM phosphorylation -> Shark [PMID:18432193].
- CED-6 adaptor via NPxY; junctophilin Undertaker / Ca2+ homeostasis
  [PMID:18984163 "link Draper-mediated phagocytosis to Ca2+ homeostasis"].
- TRAF4 binds the intracellular domain -> MSN -> JNK -> dAP-1/STAT92E transcription
  in reactive glia [PMID:28165006 "TRAF4 physically associates with the Draper intracellular domain in the region of the NPXY motif"].
- Positive feedback: JNK/AP-1 and STAT92E up-regulate draper after injury
  [PMID:23618811 "a primary role for the glial Slipper/Tak1 →MKK4 →dJNK →dAP-1 signaling cascade appears to be activation of draper expression after axon injury"];
  insulin-like signalling also induces draper [PMID:27498858].

## Biological contexts (all phagocytic or damage-sensing)

1. Embryonic hemocytes/macrophages: apoptotic cell engulfment [PMID:15342648].
2. Embryonic glia: apoptotic neuron clearance downstream of SIMU; in drpr mutants
   corpses are engulfed but accumulate undegraded inside glia
   [PMID:18455990 "drpr primarily required for the degradation of cell corpses"].
3. Glia, metamorphosis: mushroom body axon pruning debris
   [PMID:16772168, PMID:16772170].
4. Adult glia (ensheathing/cortex): Wallerian degeneration debris after axotomy
   [PMID:16772169, PMID:19369546, PMID:22426252].
5. NMJ: glia and muscle clear shed presynaptic debris and ghost boutons;
   drpr mutants have reduced synaptic growth [PMID:19707574].
6. Epidermal cells engulf degenerating dendrites [PMID:24412417].
7. Ovarian follicle cells engulf dying germline (nurse) cells; Draper -> JNK
   [PMID:22992958]; Draper on phagocytic cup and nascent phagosomes
   [PMID:27347682 "The phagocytic receptor Draper is present on the phagocytic cup and on nascent, phosphatidylinositol 3-phosphate (PI(3)P)- and Rab7-positive phagosomes"].
8. Salivary gland: cell-autonomous requirement for autophagy during cell death
   [PMID:20577216].
9. Cell competition: winner cells engulf Minute losers [PMID:17574031].
10. Hemocyte bacterial phagocytosis and defense against S. aureus [PMID:19890048].
11. Damage receptor in macrophages: H2O2 -> Src42A -> Draper -> Shark for wound
    recruitment [PMID:26028435]; corpse engulfment primes macrophages via
    Ca2+/JNK -> raised Draper [PMID:27212238]; Pez interacts genetically [PMID:33296680].
12. Muscle: drpr knockdown in muscle causes degeneration and locomotor defects
    (MEGF10 myopathy model) [PMID:25111228].

## Curation decisions of note

- Core MF: scavenger receptor activity (IBA, PAINT node seeded by drpr, CED-1,
  MEGF10) plus phosphatidylserine binding; signalling via transmembrane
  signaling receptor activity (ITAM/NPxY). Protein binding rows (Shark, Ced-6,
  Pretaporter) were MODIFIED to transmembrane signaling receptor activity.
- `phagocytosis` rows modified to the more specific terms already in the gene's
  set: engulfment of apoptotic cell / phagocytosis, engulfment.
- PMID:22992958 is cited by UniProt for "Postsynaptic cell membrane"; the full text
  (follicle cell engulfment) contains no synapse/NMJ data. Recorded as a probable
  WRONG_REFERENCE source defect for UniProt (the claim itself is supported by PMID:19707574).
- Axon location (UniProt, from PMID:16772169) left UNDECIDED: the abstract
  describes Draper as a glial receptor recruited toward severed axons; the full
  text was not accessible to check whether neuronal Draper was shown.
- Wing D/V pattern (IGI, Bx1 suppressor screen): the paper itself states draper
  is not essential for wing development, so over-annotation.
- Organelle-root policy not triggered (no root organelle terms).

## Additional literature noted but not used for annotation

- PMID:29109235 glial Draper rescues Abeta toxicity; PMID:28825401 Draper/MMP-1;
  PMID:27647497 aging reduces PI3K/Draper; PMID:32142708 sleep regulates Draper;
  PMID:29520845 Draper-JNK in glial clearance of apoptotic neurons during metamorphosis;
  PMID:36177600 Draper-induced non-autonomous death needs JNK and Src; PMID:42082485
  Notch as a Draper ligand in spermatogonia (2026, not reviewed).
