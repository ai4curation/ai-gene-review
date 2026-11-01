# Trpv4 (rat, UniProt Q9ERZ8) - manual literature synthesis

No deep-research provider was available for this session; this file was written by hand
from the cached publications in `publications/` and the UniProt record. Every claim carries
its source.

## Identity

- Rat Trpv4 (RGD:69337, GeneID 66026), 871 aa, Swiss-Prot reviewed entry TRPV4_RAT.
- Member of the TRP superfamily, TRPV subfamily: six transmembrane helices with a pore
  loop between S5 and S6, an N-terminal ankyrin-repeat domain, cytoplasmic N- and C-termini
  [PMID:11081638 "Hydrophobicity analysis of VR-OAC indicates a structure similar to those of OSM-9, VR1, and VRL-1, with six predicted membrane-spanning domains and a putative pore loop"].
- Assembles as a homotetramer [UniProt Q9ERZ8 SUBUNIT "Homotetramer." (By similarity)].

## Discovery and channel activity

- Cloned from rat kidney as VR-OAC (vanilloid receptor-related osmotically activated
  channel) [PMID:11081638 "we cloned cDNAs encoding the vanilloid receptor-related osmotically activated channel (VR-OAC) from the rat, mouse, human, and chicken"].
  The parallel mouse clone was named OTRPC4 [PMID:11025659 "OTRPC4 forms Ca2+-permeable, nonselective cation channels that exhibit spontaneous activity in isotonic media and are rapidly activated by decreases in, and are inhibited by increases in, extracellular osmolarity"].
- Rat VR-OAC in CHO cells: a cation-selective channel gated by hypotonicity
  [PMID:11081638 "This novel cation-selective channel is gated by exposure to hypotonicity within the physiological range."];
  K+ permeability slightly above Na+, Cl- much lower; 310 pS single-channel conductance
  [PMID:11081638 "the single-channel conductance of VR-OAC is 310 pS"].
- Ca2+ enters through the channel and triggers store release
  [PMID:11081638 "Ca 2+ entry through VR-OACs is both necessary and sufficient to evoke internal Ca 2+ release"].
- Not store-operated [PMID:11081638 "VR-OAC is therefore not a store-operated channel"].
- Responds to hypotonicity, not to low Na+ at constant osmolality
  [PMID:11081638 "the channel is unlikely to sense hyponatremia"].
- Gating presumed via membrane stretch [PMID:11081638 "osmotic stimuli, presumably acting through membrane stretch, efficiently gate VR-OAC"].
- Temperature: rat VR-OAC did not respond to heat alone in isotonic medium in the original
  CHO assay, though osmosensitivity peaked at 37 C [PMID:11081638]. Mouse TRPV4 was later
  shown to be warm-activated in oocytes and HEK293 cells
  [PMID:12151520 "TRPV4, previously described as a hypo-osmolarity-activated ion channel, also can be activated by heat"].
  Rat diaphragmatic lymphatics use TRPV4 to sense temperature [PMID:32706268, abstract only].
- Pharmacology used in rat studies: agonists 4alpha-PDD and GSK1016790A; blockers
  HC-067047, GSK2193874, ruthenium red [PMID:22962011; PMID:23136043; PMID:32706268].

## Localization

- Plasma membrane: eGFP-rat VR-OAC at the plasma membrane in CHO cells [PMID:11081638];
  endogenous TRPV4 at the surface of rat aortic smooth muscle cells by immunostaining and
  surface biotinylation [PMID:20650893 "TRPV4 was localized at the cell surface in non-stimulated cells"];
  a biotinylatable plasma-membrane pool in rat astrocytes [PMID:21262839].
- Overexpressed TRPV4-GFP in F11 cells is enriched in filopodia, lamellipodia, growth cones,
  membrane ruffles and cortical actin [PMID:20657843].
- Apical membrane of epithelia, cilia, adherens junctions and ER (assembly) are recorded by
  UniProt by similarity to mouse and human.

## Regulation and partners (rat data)

- AT1aR forms a constitutive complex with TRPV4; angiotensin recruits beta-arrestin 1, which
  acts as adaptor for the E3 ligase AIP4 (ITCH); TRPV4 is ubiquitinated and internalized,
  reducing 4alpha-PDD-evoked Ca2+ influx in rat vascular smooth muscle cells
  [PMID:20650893 "angiotensin-induced ubiquitination of TRPV4 serves as a signal for its internalization but not its degradation"].
- AQP4/TRPV4 complex in rat astrocytes; TRPV4 siRNA abolishes hypotonicity-induced Ca2+ rise
  and regulatory volume decrease (RVD)
  [PMID:21262839 "Calcium imaging and calcein volume measurements of cells treated with control siRNA or siRNA 9 showed that TRPV4 is necessary for hypotonicity-elicited [Ca 2+ ] o influx ( Fig. 2 B – D ) and RVD ( Fig. 2 E )."].
- The TRPV4 C-terminus binds actin and tubulin directly and stabilizes microtubules in vitro;
  activation of TRPV4 disassembles microtubules, retracts growth cones and shortens neurites
  of IB4+ rat DRG neurons; a pull-down complex also contains PKCepsilon and CaMKII
  [PMID:20657843 "The C-terminus of TRPV4 is sufficient for interaction with actin and tubulin"].

## Physiology (rat and orthologs)

- Pulmonary artery smooth muscle: 4alpha-PDD raises [Ca2+]i via TRPV4 coupled to RyR2;
  TRPV4 protein increases in chronic hypoxia [PMID:22962011, abstract only].
- Lung endothelium: TRPV4 blockade prevents the permeability increase and edema caused by
  high pulmonary venous pressure [PMID:23136043 "TRPV4 blockade prevented the increased vascular permeability and resultant pulmonary edema associated with elevated PVP"].
- Lymphatic muscle: TRPV4 mediates temperature-dependent contraction frequency [PMID:32706268].
- Systemic osmoregulation (mouse knockout): impaired drinking and ADH release after
  hyperosmotic challenge [PMID:14581612 "TRPV4 is necessary for the normal response to changes in osmotic pressure and functions as an osmotic sensor in the CNS"].
- Adipocytes (mouse): TRPV4 represses Pgc1a/Ucp1 and promotes chemokine expression via
  ERK1/2; knockout mice resist diet-induced obesity and insulin resistance [PMID:23021218].

## Open questions

- Whether TRPV4 is directly stretch-gated or responds to swelling through accessory proteins
  (AQP4, actin cytoskeleton) and lipid messengers is not settled; PMID:21262839 argues that
  AQP4 is needed for TRPV4 to act as an astrocyte osmosensor.
- The rat channel's direct heat sensitivity is not resolved: there is a negative result in
  PMID:11081638, and the positive data come from mouse/human channels.
