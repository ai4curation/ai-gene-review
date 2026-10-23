# GNAI1 (human, P63096) curation notes

## Session 2026-10-23

### Process notes

- `just fetch-gene human GNAI1` had already been run (uniprot, goa, stub with 146 PENDING rows).
- `just fetch-gene-pmids human GNAI1`: all 44 GOA-cited PMIDs cached.
- Deep research: `just deep-research-falcon human GNAI1 --fallback perplexity-lite` FAILED.
  Falcon failed with `Exception: Failed to authenticate`; the perplexity-lite fallback
  failed with `Provider 'perplexity' not available. Available: openai, falcon, openscientist`
  (the fallback command line in the log also named GNAI2 rather than GNAI1, which looks
  like a wrapper bug). No deep-research file exists for this gene; the review below is
  built from UniProt, the GOA-cited publications and the newly cached Deutsch et al. 2026
  paper (PMID:42870023). No `-deep-research-*.md` was written by hand.

### Identity and family

- Guanine nucleotide-binding protein G(i) subunit alpha-1, 354 aa; G-alpha family,
  G(i/o/t/z) subfamily [file:human/GNAI1/GNAI1-uniprot.txt "Belongs to the G-alpha family. G(i/o/t/z) subfamily."].
- N-myristoylated at Gly-2 and palmitoylated at Cys-3, giving peripheral attachment to the
  cytoplasmic face of the plasma membrane [file:human/GNAI1/GNAI1-uniprot.txt "Myristoylation at Gly-2 is required for membrane anchoring before palmitoylation."].
- Human Gi1 alpha gene cloned alongside Gi2/Gi3 [PMID:2834384 "clones encoding human Gi1 alpha, Gi2 alpha, and Gi3 alpha were isolated"].
- Disease: de novo dominant variants cause NEDHISB (MIM:619854); Gln52Pro/Arg mutants lose
  GTP binding/hydrolysis [PMID:34685729 "At the biochemical level, the three mutant proteins are deficient in binding and hydrolyzing GTP, which is the fundamental function of the healthy G proteins."].

### Core biochemistry: GTPase switch, heterotrimer, receptor coupling

- Gαi1 is the nucleotide-binding subunit of Gi heterotrimers (Gαi1-Gβγ). Coimmunoprecipitation
  of 120 combinations showed Gαi1 assembles with essentially all Gβγ dimers except those
  containing β5 [PMID:25733868 "capability of 120 different G-protein combinations consisting of αi1 or αsL and all possible βγ-dimers to form a heterotrimeric complex"].
- Many cryo-EM structures of Gi1 heterotrimers bound to Gi-coupled receptors (5-HT1A/1D/1E,
  5-HT1F, D2R, D3R, all five dopamine receptors, apelin receptor, GPR88, MRGPRX2, CCR2/CCR3,
  CaSR, GPR146 pathway) [PMID:34239069 "which allows the α5 helix of Gα i1 to insert into the intracellular cavity formed by the receptor TMD bundle"]
  [PMID:35501348 "Here we present cryo-EM structures of the human GPR88-Gi1 signaling complex"].
- RGS proteins act as GAPs on Gαi [PMID:18434541 "RGS domain binding consequently accelerates Galpha-mediated GTP hydrolysis"]
  [PMID:8774883 "RGS10 increases potently and selectively the GTP hydrolytic activity of several members of the G alphai family"].
- GoLoco proteins (RGS14, GPSM2/LGN, GPSM3, PCP2) bind Gαi1-GDP and act as GDIs
  [PMID:11976690 "crystal structure of Galpha(i1) GDP bound to the GoLoco region of the 'regulator of G-protein signalling' protein RGS14"]
  [PMID:22952234 "the C-terminal GL domain of LGN binds four molecules of Gα(i)·GDP"].

### Mechanism of receptor-catalysed nucleotide exchange (Deutsch et al. 2026)

- PMID:42870023 (Nat Struct Mol Biol 2026, full text). Isoform confirmed from Methods: the
  smFRET construct is built on **human Gαi1** [PMID:42870023 "previously published minimal cysteine background (C3S;C66A;C214S;C350S;C325A;C351I) of human Gαi1"].
  The construct (Gαi1Δ6-90C/238C; donor on AHD R90C, acceptor on Ras-like domain E238C) had
  WT-like ligand-dependent GTP turnover.
- AHD opening is needed for exchange [PMID:42870023 "Activation of heterotrimeric G proteins by G-protein-coupled receptors (GPCRs) requires large-scale opening of the Gα α-helical domain (AHD) to expose the nucleotide-binding site and facilitate GDP-GTP exchange"].
- Efficacy is encoded in the rate of AHD opening (destabilised closed state), not in the
  stability of the open state [PMID:42870023 "Mean dwell times in this high-FRET state (τhigh) depended strongly on ligand efficacy"]
  [PMID:42870023 "Thus, ligand-dependent shifts in the AHD’s conformational equilibrium (Fig. 2a) stem from the destabilization of its closed state, rather than stabilization of the open, domain-separated conformation."].
- An intermediate (mid-FRET, partly open) state lies on the exchange path
  [PMID:42870023 "suggesting that a partially open AHD could mediate transitions between the GDP-bound and fully open conformations"].
- Generalises to NTSR1-Gi complexes [PMID:42870023 "Parallel smFRET imaging of NTSR1–Gi ternary complexes (Methods), which couple promiscuously in vitro, yielded a correlation between agonist-induced low-FRET occupancy and GTP turnover similar to that of μOR"].
- Relevance to GO: supports GTPase / G protein activity, heterotrimeric G-protein complex,
  GPCR binding (receptor-catalysed GDP release on the receptor-bound heterotrimer). The
  μOR used is a mouse sequence; Gβ1γ2 human.

### Effector: adenylyl cyclase inhibition

- Purified Gi alpha 1 inhibits AC types V and VI most strongly, and type I
  [PMID:8119955 "Types V and VI adenylyl cyclase are most sensitive to inhibition by Gi alpha 1, Gi alpha 2, and Gi alpha 3"].
- Direct, receptor-stimulated Gαi1-AC5 interaction in cells (FRET)
  [PMID:23841650 "This led us to the conclusion that AC5, by binding active Gαi1, interferes with G-protein deactivation and reassembly"].
- Note: [PMID:8119955 "High concentrations of Gi alpha can interact with site 1 on types I and II adenylyl cyclase and activate the enzymes."] -- non-physiological; does not support an AC-activating pathway annotation. The GOA row GO:0007189 (ISS) was transferred from dog ADCY6 (P30804), an adenylyl cyclase, not a Gα ortholog.

### Non-canonical: mitosis, spindle positioning

- Gαi1 at centrosomes and midbody; GTPase-deficient Gαi1 causes cytokinesis defects
  [PMID:17635935 "We show expression of G(ialpha1), G(ialpha2), and G(ialpha3) in the centrosomes and at the midbody."]
  [PMID:17635935 "Expression of GTPase-deficient G(ialpha1) results in defective cytokinesis"].
- Gαi-LGN-NuMA anchors dynein-dynactin at the metaphase cortex
  [PMID:22327364 "we found that the LGN binding proteins Gαi and NuMA were required for LGN and dynein localization to the cell cortex"]
  [PMID:23870127 "Depletion of LGN or Gαi eliminated the cortical localization of dynein (DHC-GFP), the dynactin subunit p150, and NuMA during metaphase"]
  [PMID:26766442 "Proper spatiotemporal localization of the evolutionarily conserved Gαi-LGN-NuMA protein complex is critical for mitotic spindle orientation"].
- Overexpressed Gαi1 mispositions spindles; non-myristoylated Gαi1 is cytoplasmic
  [PMID:23027904 "overexpression of Gαi1-YFP or YFP-LGN leads to defective spindle positioning on uniform fibronectin-coated coverslips"].
- In this context Gαi1-GDP acts as a membrane anchor for LGN rather than as a signal
  transducer (no receptor or GTP needed in the model). Evidence is mostly pan-Gαi
  (triple knockdown), so GNAI1-specific necessity is not established.

### Physiological pathway contexts (all via Gi coupling; non-core)

- NmU receptors (PTX-sensitive AC inhibition) [PMID:15331768 "a pertussis toxin-sensitive inhibition of adenylyl cyclase with subnanomolar potency for each"].
- EP4 receptor [PMID:16204467 "couples to a PTX-sensitive inhibitory G-protein (Galpha(i)) that can inhibit cAMP-dependent signaling"].
- Lactate/GPR81 anti-lipolysis [PMID:19047060].
- Naive CD4 T-cell chemotaxis [PMID:20829352 "and Gα(i1) in naive (but not memory) CD4(+) T cells inhibited chemokine-dependent migration"].
- Smooth muscle NPR-C -> Gi1/Gi2 -> eNOS -> relaxation (rabbit) [PMID:9843699 "activation of eNOS via Gi1 and Gi2, stimulation of cGMP formation, and muscle relaxation"].

### Decisions summary

- Core: G protein activity / GTPase activity, GTP/GDP binding, Gβγ binding / heterotrimer,
  GPCR binding, adenylate cyclase inhibitor activity, AC-inhibiting GPCR signaling, plasma
  membrane (cytoplasmic side).
- Generic `protein binding` rows: GNB1/GNGT1 partners MODIFIED to G-protein beta/gamma-subunit
  complex binding; other partners (GoLoco proteins, RGS, RIC8A, NuMA) REMOVED as uninformative.
- `adenylate cyclase-modulating GPCR signaling` MODIFIED to the inhibiting child.
- AC-activating pathway (ISS from ADCY6) REMOVED.
- IL-8 signaling IDA from an NmU-receptor paper: UNDECIDED (abstract does not mention IL-8;
  full text unavailable).
