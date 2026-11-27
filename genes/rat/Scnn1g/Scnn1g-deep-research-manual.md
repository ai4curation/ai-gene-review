# Scnn1g (rat) - manual literature synthesis

No deep-research API was available for this review. This synthesis was compiled by hand from
the UniProt record (P37091) and the cached publications in `publications/`. Many cached entries
are abstract-only; full text was available for PMID:17562820, PMID:18308722, PMID:22045317,
PMID:24419567, PMID:26297031 and PMID:27413634.

## Identity and structure

- Rat Scnn1g (UniProt P37091, RGD:3641, 650 aa) encodes gamma-ENaC, the gamma subunit of the
  amiloride-sensitive epithelial sodium channel. It belongs to the DEG/ENaC family
  (TC 1.A.6), SCNN1G subfamily [UniProt P37091 "Belongs to the amiloride-sensitive sodium channel (TC 1.A.6) family. SCNN1G subfamily."].
- It was cloned in two labs in 1994: by functional complementation of the alpha subunit
  [PMID:8107805 "Here we identify two other subunits (beta and gamma) by functional complementation of the alpha-subunit of the rat epithelial Na+ channel."]
  and as RCNaCh2 from rat colon
  [PMID:8188647 "The 650-amino acid protein, entitled RCNaCh2, is 58% homologous to RCNaCh1 and displays a similar structure."].

## Molecular function: subunit of a Na+-selective channel

- Gamma alone is inactive, but it strongly increases channel activity with alpha
  [PMID:8188647 "It had no intrinsic activity when expressed alone in Xenopus oocytes, but its co-expression with RCNaCh1 increased the channel activity 18 +/- 5-fold."].
- The alpha-beta-gamma channel reproduces the native channel
  [PMID:8107805 "The ion-selective permeability, the gating properties and the pharmacological profile of the channel formed by coexpressing the three subunits in oocytes are similar to that of the native channel."].
- Stoichiometry: [PMID:17562820 "Our results support a tetrameric arrangement of ENaC subunits where 2alpha, 1beta, and 1gamma come together around central pore."]
  (Later cryo-EM work on human ENaC indicates a 1:1:1 heterotrimer, consistent with UniProt.)
- Gating: a conserved N-terminal glycine, mutated in PHA-1, controls open probability in all
  three subunits [PMID:9118951 "Homologous mutations, introduced into alpha, beta or gamma subunits, all significantly reduce macroscopic sodium channel currents recorded in Xenopus laevis oocytes."].
- ENaC is constitutively active. Proteolysis activates it: furin and prostasin cleave gamma and
  release an inhibitory tract [UniProt P37091 "Furin cleaves the SCNN1G subunit first, followed by cleavage by prostasin (PRSS8), which results in a stepwise increase in the open probability of the channel due to the release of an inhibitory tract."].
  It is not a classic ligand-gated channel.

## Location

- Apical plasma membrane of Na+-absorbing epithelia
  [PMID:11773057 "using electron microscopy, we demonstrated apical, but not basal, membrane localization of ENaC in these cells."];
  in rat kidney, apical targeting of gamma-ENaC rises in nephrotic syndrome [PMID:15075188].
- Large intracellular pools [PMID:12136275 "Immunocytochemical analysis confirmed that ENaC is primarily located intracellularly."].
  Vasopressin enlarges the intracellular gamma pool [PMID:16528252].
- Non-epithelial expression: hypothalamic magnocellular neurons (somata and dendrites) [PMID:22045317],
  nodose ganglion neurons [PMID:26297031], vascular smooth muscle [PMID:18024548, PMID:16844921].

## Regulation

- Aldosterone and low-salt diet induce gamma-ENaC [PMID:8188647 "The increase in messenger level for RCNaCh2 during the time course of the diet is likely to explain the positive regulation of the rat colon Na+ channel by steroids."].
- Nedd4 WW domains bind the gamma PY motif (PPPRY), which is deleted in Liddle syndrome
  [PMID:8665844 "the rNedd4-WW domains mediate this association by binding to the P2 regions, which include the PY motifs (XPPXY) of either betarENaC (PPPNY) or gammarENaC (PPPRY)."].
- Gamma is ubiquitinated on N-terminal lysines, which controls how many channels reach the surface
  [PMID:9351815 "ENaC is a short-lived protein (t1/2 approximately 1 h) that is ubiquitinated in vivo on the alpha and gamma (but not beta) subunits."].
  In vivo, ubiquitination follows proteolytic processing [PMID:32174140].
- Kinase sites in the C-terminus: ERK (gamma T623) [PMID:16476738]; CK2 (gamma T599)
  [PMID:18308722 "Expression of a trimeric channel lacking both CK2 sites (alphabeta(S631A)gamma(T599A)) produced a largely attenuated amiloride-sensitive whole cell conductance and rendered the mutant channel insensitive to CK2."].
  The CK2 effect depends on Nedd4-2 [PMID:18308722 "This implies a role for CK2 in inhibiting the Nedd4-2 pathway."].

## Physiology

- ENaC is the rate-limiting step for distal Na+ reabsorption
  [PMID:8107805 "The amiloride-sensitive epithelial sodium channel constitutes the rate-limiting step for sodium reabsorption in epithelial cells that line the distal part of the renal tubule, the distal colon, the duct of several exocrine glands, and the lung."].
  It is central to Na+ balance and blood pressure [PMID:24419567].
- Many rat studies report changes in gamma-ENaC expression in response to hormones, salt, hypoxia,
  drugs and disease models (PMID:16426574, 17485228, 18305093, 27413634, 27592201, 12372821,
  24093724, 17873005, 16263802, 18355814). These are expression and regulation data, not
  evidence that the gene takes part in those responses.
