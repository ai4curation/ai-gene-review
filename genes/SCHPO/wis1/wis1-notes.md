# wis1 (SPBC409.07c, P33886) curation notes

Wis1 is the sole MAP kinase kinase (MAPKK/MAP2K, EC 2.7.12.2) of the fission-yeast
stress-activated (SAPK) Sty1/Spc1 pathway. It is a dual-specificity kinase that
phosphorylates and activates the MAPK Sty1/Spc1 on Thr-171 and Tyr-173 in response to
osmotic, oxidative, heat and nutrient stress. Wis1 is itself activated by phosphorylation
of its activation-loop residues Ser-469 and Thr-473 by the redundant MAPKKKs Wis4
(=Wik1/Wak1) and Win1; the pathway is scaffolded by the Mcs4 response regulator and the
Mak2/Mak3–Mpr1–Mcs4 phosphorelay (two-component system).

## Key evidence

### Identity / kinase domain / MAP kinase kinase activity
- Originally identified as a dosage-dependent mitotic regulator with ser/thr kinase homology
  [PMID:1756736 "The wis1+ gene potentially encodes a 66 kDa protein with homology to the serine/threonine family of protein kinases."]
- It is a MAPKK (MEK) homolog most related to S. cerevisiae Pbs2
  [PMID:7859738 "One locus is identical to wis1+, encoding a MAP kinase kinase (MEK) homolog. The Wis1 sequence is most closely related to the Saccharomyces cerevisiae MEK encoded by PBS2, which is required for osmoregulation."]
- Wis1 is the ONLY MAPKK that activates Spc1/Sty1 under stress
  [PMID:9718372 "Sty1 is activated by a single MAPKK, Wis1."]
  [PMID:12181336 "Wis1 is the only MAPKK responsible for the phosphorylation and activation of Spc1 MAPK under various stress conditions"]
- Activates Spc1 via Thr-171/Tyr-173 (dual-specificity)
  [PMID:12181336 "Wis1 activates Spc1 by phosphorylating threonine-171 and tyrosine-173" — phrased in 9585506 as: "Wis1 activates Spc1 by phosphorylating threonine-171 and tyrosine-173"]
- Activation requires phosphorylation of Wis1 Ser-469 and Thr-473 in its activation loop
  [PMID:12181336 "Phosphorylation of Ser-469 and Thr-473 in the activation loop of the Wis1 kinase domain by two MAPKKKs, Wis4 ... and Win1 ..., is essential for stress-induced activation of Wis1"]
  [PMID:9718372 "the conserved MAPKKK phosphorylation sites Ser 469 and Thr 473 in the catalytic domain of Wis1 are normally essential for Sty1 activation."]

### Upstream MAPKKKs (Wis4, Win1)
- Wis4 phosphorylates Wis1 in vitro and activates it in vivo
  [PMID:9321395 "Wis4, a protein kinase of a new MAPKKK class, phosphorylates Wis1 in vitro and activates it in vivo."]
- Win1 is a MAPKKK that phosphorylates and activates Wis1, major osmostress transducer
  [PMID:9693384 "Win1 is a MAP kinase kinase kinase that phosphorylates and activates Wis1."]
- Wis4 and Win1 form a heteromer; Mcs4 stabilizes it and promotes MAPKKK–Wis1 interaction
  [PMID:23389634 "Mcs4 has an unexpected, phosphorelay-independent function in promoting heteromer association between the Wis4 and Win1 MAPKKKs."]
  [PMID:24255738 "Mcs4 also plays a critical role in osmostress signaling, as a part of the stable ternary complex with the Wis4 and Win1 MAPK kinase kinases (MAPKKKs)."]
  [PMID:24255738 "the MAPKKK-MAPKK interaction is not detectable in strains lacking Mcs4 or one of the MAPKKKs."]
- Wis1 is found on the Mcs4-MAPKKK complex and dissociates upon stress
  [PMID:24255738 "The Wis1 MAPKK and the Tdh1 GAPDH are also found on the complex"]
  [PMID:24255738 "The Wis1 MAPKK is released from the Mcs4-MAPKKK complex in response to phosphorelay-dependent (H2O2) and -independent (osmostress) signals"]

### Stress responses & downstream (Atf1)
- Spc1/Sty1 (downstream) activated by osmotic, oxidative, heat stress; Wis1 required
  [PMID:8649397 "Spc1, also known as Sty1, is activated by Wis1 MAPK kinase ... Spc1 is activated by multiple forms of stress, including high temperature and oxidative stress."]
- Wis1-Spc1 pathway required for survival in heat, osmolarity, oxidation, nutrient limitation
  [PMID:9321395 "integrity of the Wis1-Spc1 pathway is required for survival in extreme conditions of heat, osmolarity, oxidation or limited nutrition."]
- Osmostress and oxidative stress strongly activate Wis1; heat shock only weakly/transiently
  [PMID:10398679 "osmostress and oxidative stress induce strong activation of the Wis1 MAPK kinase (MEK), which activates Spc1 through Thr-171/Tyr-173 phosphorylation, activation of Wis1 upon heat shock is relatively weak and transient."]
- Atf1 transcription factor is the key nuclear substrate of the Sty1/Wis1 pathway
  [PMID:8824588 "the fission yeast Atf1 factor is also regulated by a stress-activated kinase, Sty1. The Sty1 kinase is stimulated by a variety of different stress conditions including osmotic and oxidative stress and heat shock."]
- Oxidative-stress signaling to the pathway via Mpr1-Mcs4 phosphorelay
  [PMID:10749922 "oxidative stress stimuli are transmitted by a multistep phosphorelay system to the Spc1/Sty1 stress-activated protein kinase"]

### Osmoregulation
- wis1 (=sty2) required for growth in high-osmolarity; deletion osmosensitive
  [PMID:7657164 "we find that sty2 is allelic to the wis1 MAP kinase kinase and that delta sty1 and delta wis1 cells are unable to grow in high osmolarity medium."]
- Conserved with HOG osmoregulatory pathway
  [PMID:7859738 "divergent yeasts have functionally conserved MAP kinase pathways, which are required to increase intracellular osmotic concentrations in response to osmotic stress."]
- PP2C and Pyp phosphatases counteract the pathway (downstream / negative regulators)

### Cell cycle / G2-M
- Dosage-dependent mitotic inducer; overexpression advances mitosis (small cell size)
  [PMID:1756736 "Increased levels of wis1+ expression cause mitotic initiation to occur at a reduced cell size."]
- Links cell cycle G2/M to extracellular environment
  [PMID:7501024 "a fission yeast MAP kinase pathway links the cell-cycle G2/M control with changes in the extracellular environment ... Spc1 promotes the onset of mitosis. Spc1 is a MAP kinase homologue that is activated by Wis1 kinase in response to osmotic stress and nutrient limitation."]

### Localization
- Wis1 is cytoplasmic (NES-dependent, Crm1 export); a fraction goes to nucleus on stress
  [PMID:9585506 "Wis1 is detected completely in the cytoplasm ... These patterns of localization are unaffected by stress."]
  [PMID:12181336 "the N-terminal, noncatalytic domain of Wis1 also has a MAPK-docking site and an NES sequence ... cytoplasmic localization of Wis1 by its NES is important for stress signaling to the nucleus."]
  [PMID:12181336 "a fraction of Wis1 translocates into the nucleus in response to stress."]
- Cytoplasmic localization is required for Wis1 to enable nuclear targeting of Spc1.

### Heterochromatin (non-core, indirect)
- MAPK pathway (via Atf1/Pcr1) contributes to Swi6/HP1 heterochromatin assembly at mat locus
  [PMID:15292231 "a phosphorylation event catalyzed by the conserved mitogen-activated protein kinase pathway is important for regulation of heterochromatin silencing by Atf1 and Pcr1."]
  This is an indirect, downstream consequence via Atf1; not a core molecular function of Wis1.

## Curation conclusions
- Core MF: MAP kinase kinase activity (GO:0004708). Broad parents protein kinase activity /
  protein serine/threonine kinase / protein serine kinase / protein tyrosine kinase /
  ATP binding are correct but less informative.
- Core BP: stress-activated MAPK cascade / response to osmotic & oxidative stress.
  GO:0038066 "p38MAPK cascade" is the term PomBase uses; acceptable but the Sty1 pathway is a
  fungal SAPK analogous to p38 — keep but note it is the conventional term used.
- Core CC: cytosol/cytoplasm (IDA) and Mcs4 RR-MAPKKK complex (IDA/IPI).
- protein binding (GO:0005515 IPI) is uninformative -> mark over-annotated; the meaningful
  interaction (Mcs4 complex) is already captured by GO:1990315.
- G2/M (GO:0010971) is real but dosage/genetic and is a non-core, indirect output of the SAPK
  pathway. Keep as non-core.
- Heterochromatin (GO:0090055) is an indirect downstream pathway-level effect via Atf1/Pcr1 ->
  keep as non-core.
