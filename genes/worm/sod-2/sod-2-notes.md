# sod-2 (C. elegans) — research notes

UniProt: P31161 (SODM1_CAEEL). Gene: sod-2; synonym sdm-1; ORF F10D11.1;
WormBase WBGene00004931. Chromosome I. 221 aa precursor (24-aa mitochondrial
transit peptide, mature chain 25-221). EC 1.15.1.1. PDB: 3DC6 (1.80 Å).

This is the primary/constitutive mitochondrial manganese superoxide dismutase
(MnSOD) of C. elegans. It is one of two mitochondrial MnSODs — the paralog
**sod-3** is on chromosome X and is the DAF-16/insulin-signalling-INDUCIBLE
mtSOD normally expressed at very low basal levels. The two proteins are ~86%
identical, so evidence must be attributed carefully (see paralog section below).
C. elegans has five SOD genes total: sod-1 (major cytosolic Cu/Zn), sod-2 and
sod-3 (mitochondrial MnSOD), sod-4 (extracellular Cu/Zn), sod-5 (cytosolic
Cu/Zn).

## KNOWN — sod-2 specific

### Molecular function: Mn-dependent superoxide dismutase
- Catalyzes 2 superoxide + 2 H+ = H2O2 + O2 (EC 1.15.1.1; RHEA:20696). Binds
  1 Mn(2+) per subunit (UniProt COFACTOR; metal-ligand residues His50, His98,
  Asp182, His186 by similarity). Belongs to the Fe/Mn SOD family.
- Hunter et al. 1997 cloned sod-2 and sod-3, expressed the mature proteins in
  E. coli deficient in cytosolic SODs, and directly measured SOD activity: the
  enzymes are Mn-type (not inhibited by H2O2 or cyanide, which distinguishes
  Mn-SOD from Fe-SOD and Cu/Zn-SOD), dimeric, and have comparable specific
  activities [PMID:9353332 "The expressed enzymes, which were not inhibited by
  hydrogen peroxide or cyanide, are dimeric, show quite different electrophoretic
  mobilities and isoelectric points, but exhibit comparable specific activities."].
  This is the basis of the WormBase IDA annotation to GO:0004784 (superoxide
  dismutase activity).
- Functional (heterologous) evidence for superoxide removal: the worm enzymes
  protected SOD-deficient E. coli against methyl-viologen (paraquat) oxidative
  stress [PMID:9353332 "Both proteins were shown to be active in E. coli,
  providing similar protection against methyl viologen-induced oxidative stress."].
  Basis of the WormBase IMP annotation to GO:0019430 (removal of superoxide
  radicals). NOTE: this is a heterologous E. coli complementation assay, not a
  worm mutant phenotype; the annotation is nonetheless functionally sound.

### Localization: mitochondrion / mitochondrial matrix, and ETC supercomplex
- N-terminal mitochondrial transit peptide (residues 1-24); UniProt subcellular
  location = mitochondrion matrix [PMID:9353332 "Both deduced protein sequences
  contain the expected N-terminal mitochondrial transit peptides."].
- SOD-2 is the primary mitochondrial SOD: "sod-2 encodes the primary SOD found
  in the mitochondrion" [PMID:23895727].
- SOD-2 physically co-localizes with the mitochondrial respiratory
  supercomplex I:III:IV by blue-native gel Western blotting (Fig 4D)
  [PMID:23895727 "Western blots of BNGs indicated that SOD-2 co-localized with
  the I:III:IV supercomplex (Figure 4D)."]. Basis of the WormBase IDA
  annotation to GO:0098803 (respiratory chain complex, located_in). SOD-3 also
  localizes there. This is an association/embedding, not classical structural
  subunit membership; the authors conclude "mtSODs are embedded within the
  supercomplex I:III:IV and stabilize or locally protect it from reactive
  oxygen species (ROS) damage" [PMID:23895727].
- HDA mitochondrial-proteome localization (GO:0005739) is attributed to
  PMID:20188671 (Haynes et al. 2010). That paper's abstract is about HAF-1/ClpP
  and the mitochondrial UPR (mtUPR) and does not mention sod-2; the annotation
  is a high-throughput direct-assay (mass-spec) mitochondrial localization.
  Localization of a MnSOD to the mitochondrion is biologically unambiguous, so
  this is accepted (as a general, less-specific companion to matrix).

### Effect of loss of SOD-2 on the ETC (sod-2-specific, from PMID:23895727)
- Loss of SOD-2 specifically decreases complex I and complex II activities;
  complexes III and IV remain normal [PMID:23895727 "Loss of SOD-2 specifically
  (i) decreases the activities of complexes I and II, complexes III and IV
  remain normal"].
- sod-2(0) reduces formation of I:III and I:III:IV supercomplexes (~28%),
  implying SOD-2 stabilizes or protects the supercomplex.
- Complex I function decreases out of proportion to ROS damage, suggesting a
  possible direct structural/stabilizing role in addition to local scavenging.

## KNOWN — paralog (sod-3) attribution notes
- sod-2 and sod-3 are 86.3% identical MnSODs, both mitochondrial, both with
  transit peptides, both trans-spliced to SL-1, both catalytically active
  [PMID:9353332]. sod-3 is on chromosome X; sod-2 on chromosome I.
- sod-3 is the DAF-16 (FOXO)/insulin-IGF-inducible mtSOD, "normally expressed in
  very low levels in wild type worms" [PMID:23895727]; sod-2 is constitutive and
  quantitatively dominant. daf-2 longevity increases sod-3, but eliminating both
  sod-2 and sod-3 does not suppress daf-2 long life.
- Antibody cross-reactivity: the anti-SOD-2 antibody used in PMID:23895727 also
  detected SOD-3 (residual signal in sod-2 single mutant was lost in the
  sod-2;sod-3 double), so the supercomplex-localization result reports both
  mtSODs; the sod-2-specific signal is real (dominant band lost in sod-2 mutant).
- Phenotypic divergence: loss of sod-2 vs sod-3 have DIFFERENT genetic
  interactions with ETC mutants (gas-1/complex I, mev-1/complex II,
  isp-1/complex III). E.g. sod-2;gas-1 lives longer than gas-1; sod-3 does not
  change gas-1 lifespan [PMID:23895727]. So they are NOT functionally redundant.

## NOT known / knowledge gaps
1. **Counterintuitive longevity of sod-2 loss.** Deleting the *primary*
   mitochondrial antioxidant does not shorten, and can EXTEND, lifespan —
   contrary to the oxidative-damage theory of aging. Suthammarak et al. quote
   the prior finding directly: "Hekimi reported that a deletion of sod-2
   lengthened lifespan, and that clk-1;sod-2 lived longer than the long-lived
   clk-1, despite increased oxidative damage in mitochondrial protein"
   [PMID:23895727]; and note that all five SODs could be eliminated without
   shortening lifespan [PMID:23895727 "Van Raamsdonk eliminated all of the
   superoxide dismutases in C. elegans without shortening lifespan"]. Yet
   sod-2(gk257) on its own has a normal lifespan [PMID:23895727 "sod-2(gk257)
   had a normal lifespan in agreement with Gems and colleagues"]. The mechanism
   (mitohormesis / superoxide as a pro-longevity signal vs. metabolic slowing)
   is unresolved: "no single component of mitochondrial physiology that we
   studied correlates simply with lifespan" [PMID:23895727].
2. **Functional division of labour between sod-2 and sod-3.** Why two nearly
   identical mitochondrial MnSODs? Their non-redundant, opposite genetic
   interactions with ETC mutants are unexplained, and the interaction of sod-3
   with the supercomplex was, at time of writing, still being investigated:
   "Studies are now being undertaken to characterize the interaction of sod3
   with supercomplex I:III:IV formation" [PMID:23895727].
3. **Scavenger vs. structural role in the supercomplex.** Whether SOD-2 acts
   only as a local superoxide scavenger at the site of ROS production or also
   as a direct structural stabilizer of supercomplex I:III:IV is undetermined:
   complex I function falls "out of proportion to the amount of ROS damage",
   so "it is also possible that the mtSODs may directly serve as stabilizing
   factors in the I:III:IV supercomplex" [PMID:23895727].

## Annotation review plan (GOA has 12 rows)
- GO:0004784 superoxide dismutase activity — IDA (PMID:9353332) → ACCEPT, CORE.
  Same term IBA (GO_REF:0000033) and IEA (GO_REF:0000120) → ACCEPT (redundant
  support, non-core duplicates).
- GO:0030145 manganese ion binding — IBA (GO_REF:0000033) → ACCEPT, CORE
  (matches UniProt Mn cofactor; the correct specific metal term).
- GO:0046872 metal ion binding — IEA (InterPro) → generalization of manganese
  ion binding; KEEP_AS_NON_CORE (less informative parent).
- GO:0005759 mitochondrial matrix — IEA (SubCell) → ACCEPT, CORE location.
- GO:0005739 mitochondrion — IBA (is_active_in) and HDA (PMID:20188671) →
  ACCEPT as non-core (less specific than matrix).
- GO:0098803 respiratory chain complex — IDA (PMID:23895727) and IEA (ARBA) →
  the IDA reflects real BNG co-localization; KEEP_AS_NON_CORE (association, not
  a core catalytic/structural identity). The IEA(ARBA) part_of duplicate: keep
  non-core.
- GO:0019430 removal of superoxide radicals — IMP (PMID:9353332) → ACCEPT, CORE
  process (heterologous complementation; functionally correct).
- GO:0006801 superoxide metabolic process — IEA (InterPro) → parent BP; ACCEPT
  as non-core (removal of superoxide radicals is more specific).
- GO:0042803 protein homodimerization activity (in UniProt DR as ARBA IEA) — not
  present in GOA TSV rows; the mature enzyme is dimeric [PMID:9353332], but this
  is a structural property, not a core informative function; not added.

## Update from falcon deep research (sod-2-deep-research-falcon.md, Edison, 33 cites)
Additional sod-2-specific literature retrieved (PMIDs then cached and cited in the
review):
- **Lifespan extension (seminal).** Van Raamsdonk & Hekimi 2009 deleted each of the
  five worm sod genes; none shortens lifespan and sod-2 loss extends it
  [PMID:19197346 "we find that sod-2 mutants are long-lived despite a significant
  increase in oxidatively damaged proteins"; "deletion of sod-2 extends worm lifespan
  by altering mitochondrial function"]. Threshold model: sod-2 deletion increases
  lifespan in clk-1 (mild mito dysfunction) but decreases it in isp-1 (severe)
  [PMID:19197346 "sod-2 deletion markedly increases lifespan in clk-1 worms while
  clearly decreasing the lifespan of isp-1 worms"].
- **Mechanism (RDRS).** Branicky et al. 2022 Sci Adv: loss of SOD-2 raises
  mitochondrial superoxide; cytosolic SOD-1 converts it to H2O2 that oxidizes
  LET-60/RAS Cys118, driving a genome-wide developmental program; requires SOD-1
  [PMID:36449615 "RDRS is regulated by negative feedback from the superoxide
  dismutase 1 (SOD-1)-dependent conversion of superoxide into cytoplasmic hydrogen
  peroxide, which, in turn, acts on a redox-sensitive cysteine (C118) of RAS"]. This
  substantially NARROWS knowledge gap 1 (mechanism of longevity).
- **Sperm activation (sod-2-specific).** Sakamoto & Imai 2017: SOD-2-produced H2O2 is
  a positive signal for sperm pseudopod extension; sod-2, not sod-1, is the required
  SOD [PMID:28724632 "sod-2 is required for pseudopod extension"; "SOD-2 plays an
  important role in the sperm activation of C. elegans by producing H2O2 as an
  activator of pseudopod extension"]. Reinforces sod-2/sod-3 non-redundancy and the
  signalling (not merely detoxifying) role of the H2O2 product.
- **Transcriptional regulation split (from falcon; sources not cached).** falcon
  reports sod-2 is regulated mainly by SKN-1/Nrf2 via p38 MAPK, whereas sod-3 is a
  DAF-16/FOXO (insulin/IGF-1) target (Yanase 2020; Honda 1999). Not independently
  quote-verified here (papers not in cache); recorded as context only.

## Sources
- PMID:9353332 Hunter et al. 1997 J Biol Chem (abstract only in cache) — cloning
  + heterologous expression + biochemical characterization of sod-2 and sod-3.
- PMID:23895727 Suthammarak et al. 2013 Aging Cell (full text cached) — mtSOD /
  ETC supercomplex interactions and lifespan; richest sod-2-specific source.
- PMID:19197346 Van Raamsdonk & Hekimi 2009 PLoS Genet (full text cached) —
  sod-2 deletion extends lifespan; oxidative-stress-theory challenge.
- PMID:36449615 Branicky et al. 2022 Sci Adv (full text cached) — RAS-dependent
  ROS signalling (RDRS) mechanism of sod-2 longevity.
- PMID:28724632 Sakamoto & Imai 2017 J Biol Chem (abstract only) — SOD-2 H2O2 in
  sperm activation; sod-2-specific.
- PMID:20188671 Haynes et al. 2010 Mol Cell (abstract only) — source of HDA
  mitochondrial-proteome localization annotation.
- genes/worm/sod-2/sod-2-deep-research-falcon.md — Edison deep research (33 cites).
