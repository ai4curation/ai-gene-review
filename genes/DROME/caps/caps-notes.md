# capricious (caps) — curation notes

UniProt: A0A0S0WP14 (isoform E, TrEMBL) · FlyBase: FBgn0023095 · CG11282 · Drosophila melanogaster (NCBITaxon:7227)

## Protein architecture / molecular identity

- Single-pass type I transmembrane protein with an extracellular leucine-rich-repeat (LRR)
  ectodomain. UniProt record: signal peptide 1–39, extracellular LRR array (SMART finds 12
  LRR_TYP repeats + LRRCT cap, domain 395–446), single TM helix 454–477, and a cytoplasmic
  tail (~478–811). InterPro/Pfam: LRR_8 (PF13855 ×3), LRRCT, LRR_dom_sf; Gene3D 3.80.10.10
  "Ribonuclease Inhibitor" horseshoe fold. This is the canonical LRR cell-surface-receptor
  architecture. [caps-uniprot.txt]
- caps is the paralog of *tartan (trn)*; their extracellular domains are ~65% identical:
  "The XC domains of Trn and Caps are 65% identical" [PMID:18817735]. The two proteins act
  partially redundantly and may share a common receptor: "Studies of Trn and Caps function in
  imaginal discs suggest that the two proteins can interact with a common receptor" [PMID:18817735].
- Molecular function is best described as LRR-mediated cell-surface adhesion / target
  recognition. Direct biochemical evidence for homophilic adhesion: "CAPS promotes homophilic
  cell adhesion in transfected S2 cells" [PMID:16423695]. The field also entertains heterophilic
  binding: "It has been suggested that Caps and Trn act as homophilic or heterophilic adhesion
  receptors or serve another unidentified function during adhesion" [PMID:19064711]. A domain
  dissection in the visual system shows the ectodomain is essential while the intracellular
  domain contributes to (but is not strictly required for) activity, arguing Caps is more than a
  passive adhesion molecule and may signal: overexpression of a construct "which lacks the
  intracellular domain, showed a much milder R7 stopping phenotype than Caps full length
  overexpression" whereas the ectodomain-deleted form "did not induce any mistargeting of R7
  axons... indicating that the ectodomain is essential for Caps function" [PMID:24386266].
  In trachea, "Capricious requires both extracellular and intracellular domains during tracheal
  branch outgrowth" [PMID:16764850].

## Biological process — synaptic target recognition / motor axon guidance (best-characterized, core)

- caps was originally defined as a motor-axon target-recognition molecule at the larval
  neuromuscular junction (NMJ). "The gene capricious (caps), which encodes a cell-surface
  protein, functions as a recognition molecule in motor axon guidance, regulating the formation
  of the selective connections between the SNb-derived motoneuron RP5 and muscle 12" [PMID:11677048].
- caps is expressed on a subset of muscles including muscle 12: "Capricious (Caps) is a
  leucine-rich repeat (LRR) protein that is expressed on muscle 12, as well as on ventral muscles
  and a subset of dorsal muscles." Ectopic pan-muscle expression drives mistargeting
  ("12→13 loopback"), while caps null alleles give only weak phenotypes [PMID:18817735].
- caps and trn act redundantly in embryonic ISNb/SNa motor axon guidance: in trn caps double
  mutants "The penetrances of the ISNb and SNa phenotypes (55% and 60%, respectively) in double
  mutant embryos were roughly doubled relative to trns064117 single mutants" [PMID:18817735]. caps
  single mutants: "caps65.2 embryos had weak ISNb phenotypes and no SNa phenotypes." So caps is
  a genuine but partially redundant contributor. This grounds GO:0008045 (motor neuron axon
  guidance) and the parent GO:0007411 (axon guidance).
- Postsynaptic recognition mechanism: Caps localizes to the tips of myopodia (muscle postsynaptic
  filopodia) and acts there in synaptic matchmaking. "CAPS, expressed as a GFP-fusion protein in
  M12, accumulated at the tips of myopodia"; in caps (and caps trn) mutants "we observed fewer
  contacts between myopodia of M12 and the presynaptic growth cones... The nascent synaptic sites
  of M12 were also reduced" [PMID:19270171]. This links Caps localization (muscle cell
  projection / myopodium) to its target-recognition function.

## Synapse assembly — nuanced / non-core

- At the NMJ, caps loss reduces nascent synaptic sites (above) — a real but downstream/secondary
  contribution to synapse formation via its target-recognition role [PMID:19270171].
- In the central visual system, a careful reassessment found Caps is largely dispensable for
  synaptogenesis proper: "Caps does not have a major role in synapse formation at specific sites in
  R8 photoreceptor axons" and it "did not affect presynapse specification in R8 photoreceptors"
  [PMID:24386266]. Thus GO:0007416 (synapse assembly) is best kept as a non-core annotation:
  Caps sets up specific contacts (recognition) rather than assembling the synapse machinery.

## Photoreceptor / visual-system layer targeting (non-core, redundant)

- Reciprocal R8/R7 expression model: "caps is specifically expressed in R8 and its target layer
  but not in R7 or its recipient layer. caps loss-of-function mutations cause local targeting
  errors by R8 axons, including layer change. Conversely, ectopic expression of caps in R7
  redirects R7 axons to terminate in the CAPS-positive R8 recipient layer" [PMID:16423695].
- A later study found the endogenous requirement modest and questioned the strict homophilic
  model: "Caps has a marginal role in the guidance of R8 pho[toreceptor axons]" and "the
  recognition of the M3 layer by photoreceptors is not mediated by Caps homophilic axon-target
  interactions" [PMID:24386266]. Supports GO:0072499 (photoreceptor cell axon guidance) but as a
  redundant, non-core context.

## Tracheal morphogenesis (non-core)

- Caps is displayed on mesodermal "bridge-cells" and instructs dorsal-trunk branch fusion:
  "Capricious is specifically localized on the surface of bridge-cells and facilitates the
  outgrowing dorsal trunk cells of adjacent metameres toward each other" [PMID:16764850]. This
  grounds GO:0035147 (branch fusion, open tracheal system). Notably caps and trn have *distinct*
  (not merely redundant) roles here — Caps is instructive on bridge cells, Trn is a permissive
  broadly-expressed substrate [PMID:16764850].

## Salivary gland / tubulogenesis (non-core)

- Identified in a fork head–GAL4 gain-of-function tubulogenesis screen; gain- and loss-of-function
  comparisons implicate caps: "The analysis of caps and tartan mutant phenotypes suggests a role
  for these genes in salivary gland morphogenesis" [PMID:19064711]. Grounds GO:0007436 (larval
  salivary gland morphogenesis).

## Cytoneme / ASP (non-core localization)

- In the tracheal air-sac primordium (ASP), a Caps:GFP fusion localizes along cytonemes, enriched
  at tips, and caps is required for cytoneme-mediated Dpp reception: "Caps:GFP that was expressed
  in trachea was detected in ASP cytonemes, and concentrated at the tips" [PMID:24385607]. caps
  and nrg here are described as "putative cell adhesion transmembrane proteins" [PMID:24385607].
  Grounds GO:0035230 (cytoneme, colocalizes_with).

## Imaginal-disc affinity boundaries / other

- caps/trn also generate compartment-affinity boundaries in the wing disc and elsewhere; the ASP
  paper summarizes that the paralogs "contribute partially redundant functions to the formation of
  compartment boundaries of the wing disc" [PMID:24385607], and the salivary-gland paper lists
  "separation of ventral and dorsal compartment cells in the wing disc (Milan et al. 2001)"
  among Caps/Trn roles [PMID:19064711]. This affinity/cell-sorting behavior is an adhesion-based
  function, not clearly "cell migration."

## Reference-quality flags

- PMID:12717815 ("Pattern formation in the Drosophila wing: the development of the veins",
  De Celis 2003) and PMID:12508275 ("Size isn't everything", Tyler & Baker 2003) are review
  articles; both cached entries are abstract-only and neither abstract mentions caps. They are the
  cited support for GO:0007155 (cell adhesion, NAS) and GO:0016477 (cell migration, TAS)
  respectively. The underlying functions are only weakly/indirectly tied to these specific reviews.
- The synapse-assembly annotation (GO:0007416) cites PMID:24386266, which actually concludes Caps
  is largely dispensable for R8 synaptogenesis — the annotation is better supported at the NMJ
  (PMID:19270171); treated as non-core.

## Curation synthesis

- Core molecular function: LRR-mediated cell-cell adhesion / synaptic target-recognition
  (cell–cell adhesion mediator activity; homophilic and possibly heterophilic).
- Core biological process: synaptic partner matching / motor-axon target selection at the NMJ.
- Core location: plasma membrane (single-pass TM protein), concentrating at the tips of cellular
  projections (myopodia, cytonemes).
- Pleiotropic non-core contexts (all adhesion/recognition manifestations): photoreceptor layer
  targeting, tracheal branch fusion, salivary-gland morphogenesis, wing-disc affinity boundaries,
  dendrite/olfactory targeting.
</content>
