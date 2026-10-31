# Htr1a (rat, UniProt P19327) - manual literature synthesis

No deep-research provider was run for this gene (no API keys in the session). This file
is a manual synthesis written by the reviewer from the cached publications in
`publications/` and the UniProt record `Htr1a-uniprot.txt`. All statements carry inline
provenance; quotes are verbatim from the cited cached source.

## Identity and family

- 5-hydroxytryptamine receptor 1A, 422 aa, seven-transmembrane class A (rhodopsin-like)
  GPCR; UniProt: "Belongs to the G protein-coupled receptor 1 family. 5-hydroxytryptamine
  receptor subfamily. HTR1A sub-subfamily." (PROSITE-ProRule PRU00521). InterPro
  IPR000610 (5HT1A_rcpt), IPR002231 (5HT_rcpt), IPR000276/IPR017452 (GPCR rhodopsin 7TM);
  PANTHER PTHR24248:SF191.
- Rat gene cloned as "clone D" by low-stringency screening with the beta2-adrenergic
  receptor [PMID:2156831 "it possesses an intronless open reading frame encoding a protein
  with seven putative transmembrane domains and 89% amino acid identity with the human
  5-HT1A receptor"].

## Molecular function: Gi/o-coupled serotonin receptor

- Ligand binding with 5-HT1A pharmacology in transfected cells, G-protein interaction and
  inhibition of cAMP accumulation [PMID:2156831 "it expresses a ligand-binding site with
  the pharmacology of the 5-HT1A receptor subtype"; "its binding site interacts with G
  proteins and because it mediates agonist-induced inhibition of basal and stimulated cAMP
  accumulation in transfected GH4C1 pituitary cells"].
- Native rat brain receptors physically associate with Galpha(o) and Galpha(i3) (and Gi1,
  Gz in hypothalamus), with region-specific coupling [PMID:16772521 "5-HT1A receptors were
  found to interact equally with Galpha(o) and Galpha(i3) in the cerebral cortex"; "In the
  anterior raphe, 5-HT1A receptors seem to interact specifically with Galpha(i3), whereas
  in the hippocampus, they are mainly coupled to Galpha(o) proteins"].
- Agonist-stimulated [35S]GTPgammaS binding as a readout of receptor-G protein activation,
  which is desensitized in raphe after chronic fluoxetine [PMID:11927181 "the
  desensitization of somatodendritic 5-HT(1A) autoreceptors in the dorsal and median raphe
  following chronic SSRI treatment appears to be due to a reduced capacity of the 5-HT(1A)
  receptor to activate G protein"].

## Effectors and signalling outputs

- GIRK-type inwardly rectifying K+ current in dorsal raphe neurons, pertussis-toxin
  sensitive and cAMP-independent [PMID:8271204 "in acutely isolated adult DR neurones 5-HT
  activates an inwardly rectifying K+ current and this involves a PTX-sensitive G-protein
  in the transduction pathway which may interact with the K+ channel directly"; "cAMP and
  lipoxygenase metabolites ... were found not to alter the effectiveness of 5-HT"].
  Note: this paper therefore supports Gi/o coupling to a K+ channel, not the adenylate
  cyclase arm.
- Inhibition of Ca2+ current in raphe neurons [PMID:2140514 "low concentrations of 5-HT
  and the 5-HT1A-selective agonist 8-OH-DPAT reversibly decrease whole-cell calcium
  current"].
- PKA/PP1/CaMKII cascade in PFC pyramidal neurons reducing AMPA currents [PMID:12149253
  "serotonin, by activating 5-HT(1A) receptors, suppress glutamatergic signaling through the
  inhibition of CaMKII, which is achieved by the inhibition of PKA and ensuing activation
  of PP1"] - this is the evidence for the adenylate cyclase/PKA arm in native neurons.
- NMDA receptor down-regulation in PFC via microtubule depolymerization and impaired NMDAR
  transport [PMID:18442977 "activation of 5-HT(1A) receptors inhibits N-methyl-D-aspartate
  (NMDA) receptor (NMDAR) currents in PFC pyramidal neurons by disrupting microtubule-based
  transport of NMDARs"; full text: "application of 8-OH-DPAT (40 μm, 20 min) caused a potent
  increase in free tubulin" and "application of 8-OH-DPAT (40 μm, 5 min), caused a marked
  reduction in the number and size of surface NR2B clusters"]. The receptor reduces, rather
  than performs, NMDAR clustering.
- Presynaptic inhibition of GABA release in basolateral amygdala via AC-cAMP inhibition
  [PMID:10381597 "5-HT inhibits GABAergic mIPSCs by inactivating the AC-cAMP signal
  transduction pathway via a G-protein-coupled 5-HT1A receptor"]. The receptor assignment
  rests on 8-OH-DPAT and spiperone pharmacology (abstract-only in cache).

## Localization

- Plasma membrane (transfected cells; PMID:2156831) and somatodendritic domain; dendritic
  targeting depends on the C-terminal 17-aa region and Yif1B [PMID:18685031 "The 5-HT(1A)R
  is confined to the somatodendritic domain of central neurons, where it mediates
  serotonin-evoked hyperpolarization"; "inhibition of endogenous expression of Yif1B ...
  specifically prevented the addressing of 5-HT(1A)R to distal portions of the
  dendrites"].
- Axon hillock and pyramidal cell body in medial prefrontal cortex [PMID:18622042
  "5-HT1A-immunopositive material is present in the axonal hillocks and, to lower extend, in
  cytoplasm of presumably pyramidal cell bodies"].

## Heteroreceptor complexes

- FGFR1-5-HT1A heteroreceptor complexes in hippocampus and raphe, by BRET, co-IP, PLA and
  FRET, with synergistic ERK signalling [PMID:22035699 "fibroblast growth factor receptor 1
  (FGFR1)-5-hydroxytryptamine 1A (5-HT1A) receptor complexes have been demonstrated";
  PMID:25485703 "The heteroreceptor complex formation was dependent on TMV of the 5-HT1A
  receptor"].

## Physiology and behaviour (indirect; context only)

- Raphe somatodendritic autoreceptor feedback on 5-HT release [PMID:2140514 "The release
  of serotonin (5-HT) from the terminals of serotonergic (raphe) neurons is under
  inhibitory feed-back control"].
- Pharmacological (8-OH-DPAT, buspirone, WAY-100635) effects on feeding [PMID:11900812],
  ultrasonic vocalization [PMID:24275076], PVN GABA release [PMID:30217553].
- mRNA/protein expression changes after morphine [PMID:24055683 "The 5-HT1A receptor mRNA
  was significantly decreased after 3 hours of morphine exposure compared to placebo"],
  nicotine withdrawal with Rhodiola [PMID:22921986], gastrodin / 4-hydroxybenzyl alcohol
  [PMID:25817367, PMID:26899441]. These are expression responses of the transcript, not
  receptor functions.
