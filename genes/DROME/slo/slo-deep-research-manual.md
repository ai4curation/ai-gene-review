# slo (slowpoke), Drosophila melanogaster -- manual literature synthesis

No deep-research API was available for this session, so this file is a manual synthesis from the
cached publications in `publications/` and the UniProt record (Q03720, SLO_DROME).

## Identity and molecular function

- slo encodes the pore-forming alpha subunit of the large-conductance ("Big K", BK, maxi-K)
  Ca2+- and voltage-activated K+ channel. It was the first BK channel cloned
  [PMID:1857984 "The Drosophila slowpoke (slo) locus, mutations of which specifically abolish a Ca(2+)-activated K+ current in
  muscles and neurons, provides an opportunity for molecular characterization of
  these channels."].
- Heterologous expression from slo cDNAs gives Ca2+-activated K+ channels with ~126 pS unitary
  conductance [PMID:1497890 "Excised
  inside-out membrane patches showed potassium channel openings only with
  micromolar calcium present at the cytoplasmic side; activity increased steeply
  both with depolarization and with increasing calcium concentration. The
  single-channel conductance was 126 pS with symmetrical potassium concentrations."].
  Alternative splicing in the cytoplasmic region generates many functionally distinct channel
  variants (UniProt lists 20 isoforms).
- Domain architecture (UniProt): S0-S6 transmembrane segments with an S4 voltage sensor, a P-loop
  with the K+ selectivity motif, two cytoplasmic RCK domains and a "calcium bowl" motif.
- Dslo, like bovine Slo, is blocked from the cytoplasmic side by serine-proteinase inhibitors
  (BPTI, ovoinhibitor), suggesting a conserved inhibitor-binding site in the C-terminal domain
  [PMID:8973172 "Both Bslo and Dslo KCa channels were sensitive to inhibition
  by the internally applied serine proteinase inhibitors"].

## Interacting proteins / regulation

- Slob binds the C-terminal domain; applying Slob to the cytoplasmic face of patches increases
  channel activity [PMID:9539129 "Direct application of Slob to the cytoplasmic face of detached membrane patches
  containing dSlo channels leads to an increase in channel activity."].
- dSLIP1 (Slip1) binds dSlo and reduces surface channel number
  [PMID:9502797 "dSLIP1
  selectively reduces Slo BK currents by reducing the number of BK channels in the
  plasma membrane."].
- Src and PKA catalytic subunit bind simultaneously; PKAc binds directly to a 172-aa C-terminal
  region [PMID:10234050 "The PKAc binds directly to a 172-amino acid
  region in the C-terminal domain of dSlo"]; the authors propose the channel scaffolds its own
  modulatory enzymes.
- The PDZ scaffold Dyschronic (DYSC, whirlin homolog) binds SLO and promotes its expression
  (PMID:25359729, citing Jepson et al. 2012).

## Physiology and organismal roles (mostly mutant phenotypes)

- Synaptic: slo null larvae show enlarged boutons, enlarged/merged active zones, increased evoked
  EJC amplitude and increased spontaneous release; dysc and slo act in a common pathway
  [PMID:25359729 "suggesting that dysc and slo act in a common genetic
  pathway to modulate synaptic development and output."].
- Circadian: slo4 null flies are behaviourally arrhythmic without loss of total activity
  (PMID:12417656); the core molecular clock in small LNvs is preserved, the defect lies in
  output, with impaired PDF dorsal arborisation (PMID:17369364). Neuronal (not muscle) slo
  rescues the rhythm defect.
- Courtship song: slo mutations cause severe song abnormalities [PMID:9504928 "slowpoke mutations, which affect a
  calcium-activated potassium channel, cause severe song abnormalities."].
- Drug tolerance: a single benzyl-alcohol sedation induces slo expression and rapid tolerance; a
  slo null prevents tolerance, and inducible slo expression mimics it (PMID:15569939).
- Heart: in PMID:21690310 (Qian et al. 2011, J Cell Biol; read via PMC full text PMC3216339), slo
  and dSUR transcripts are down-regulated in Cdc42/tinman compound heterozygous hearts and in
  hearts over-expressing miR-1; tin/slo transheterozygotes show increased arrhythmia. These data
  place slo expression downstream of a Tinman-Cdc42 regulatory interaction; they are genetic and
  expression data and do not by themselves add a GO process for the channel (the existing GOA set
  has no cardiac row).

## Localisation

- Immunostaining: SLO puncta along neuronal processes and in cell bodies of dorsal-brain clusters
  (pars intercerebralis), adjacent to PDF neuron projections (PMID:17369364).
- Tissue: muscle, CNS/PNS neurons, mushroom bodies, midgut cells, tracheal cells (UniProt, PMID:7666207,
  PMID:8774450).
