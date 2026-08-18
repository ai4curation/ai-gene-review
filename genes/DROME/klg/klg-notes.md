# klingon (klg / CG6669 / FBgn0017590), Drosophila melanogaster — review notes

UniProt: Q9VCT4 (Q9VCT4_DROME, TrEMBL, PE=1 evidence at protein level). 545 aa.
Synonyms: CT20712, Dmel\CG6669, h214, Klg, l(3)rN712. Also recovered as the
memory/ethanol mutant allele **ruslan (rus)** [PMID:19104051].

## Protein architecture / molecular features
- IgSF cell-surface protein. UniProt features: three Ig-like domains (101–194,
  197–279, 288–376) plus an FN3 module (InterPro FN3_dom; CDD cd00063 FN3, cd00096 Ig x2;
  SMART IG x3). Consistent with the original description of "three C2-type
  Immunoglobulin-like domains followed by one fibronectin type III repeat"
  [PMID:9043060 "contains three C2-type Immunoglobulin-like domains followed by one fibronectin type III repeat"].
- Membrane attachment is via a GPI anchor (not a transmembrane domain), i.e. an
  **extrinsic/lipid-anchored** component of the plasma membrane:
  [PMID:9043060 "When Klingon is expressed in S2 tissue culture cells, it is associated with the cell membrane by a glycosyl-phosphatidylinositol linkage and can mediate homophilic adhesion"].
- KEGG/Reactome cross-references map it to the L1CAM/basigin-type IgSF adhesion module
  (Reactome R-DME-373760 "L1CAM interactions", etc.) — supportive of an adhesion-molecule role,
  not independent experimental evidence for klg.

## Molecular function
- **Homophilic cell-cell adhesion (IDA).** Direct S2 cell-aggregation assay shows Klingon
  mediates homophilic adhesion [PMID:9043060 "can mediate homophilic adhesion"]; reaffirmed
  as "a homophilic cell adhesion molecule" [PMID:19104051 "rus is a new allele of klingon (klg), which encodes a homophilic cell adhesion molecule"].
  → Best MF representation: cell-cell adhesion mediator activity (GO:0098632) /
  cell adhesion molecule binding (GO:0050839). This is the gene's core molecular function.
- **Protein interaction (IPI, PMID:23827685, Özkan et al. 2013 Cell IgSF/LRR extracellular interactome).**
  UniProt IntAct records Q9VCT4 (klg) binding **Q9VDD5 = cDIP** (a "common Dpr-interacting protein",
  an IgSF ectodomain), NbExp=2 (IntAct EBI-91271/EBI-6881617). The cached full text of PMID:23827685
  does not name klg/cDIP (the pairwise hits are in supplementary tables), so I cannot quote a verbatim
  klg-specific sentence from that paper; the interaction is captured in UniProt. The bare "protein binding"
  (GO:0005515) is uninformative and should be sharpened to an adhesion-molecule binding MF.
- **"Axon guidance receptor activity" (GO:0008046, IBA).** Phylogenetic (GO_Central) inference from the
  IgSF adhesion/guidance family. No direct experimental demonstration that klg transduces a guidance
  signal, and as a GPI-anchored protein it lacks a cytoplasmic signaling domain (would require a
  co-receptor). The family-level term therefore overstates what klg does: MODIFY to
  cell-cell adhesion mediator activity (GO:0098632), which matches the demonstrated homophilic
  adhesion. Knock-on: the GO:0007411 axon guidance annotation is a GO_REF:0000108 inter-ontology
  link whose WITH/FROM is this GO:0008046 IBA, so it inherits this term's weakness.

## Biological process
- **R7 photoreceptor development (core).** klg is expressed in the R7 precursor throughout its
  development and is an essential gene required for R7 neuron development
  [PMID:9043060 "klingon is a member of the Immunoglobulin superfamily and is expressed in a restricted pattern of neurons during embryonic neurogenesis and in the R7 photoreceptor precursor throughout its development"];
  [PMID:9043060 "Genetic analysis has revealed that klingon is an essential gene that participates in the development of the R7 neuron"].
  Genetic interaction with the sevenless pathway: [PMID:9043060 "Ectopic expression of klingon in all neurons in a sevenless background can alter the position of the R8 rhabdomere"].
  Curated as R7 cell fate commitment (IGI), R7 cell differentiation (IMP) [PMID:9043060].
- **Axon guidance / synapse organization (IBA/IEA).** Neuronal-expression + family-based inferences.
  Klg protein accumulates at neuropil boundaries and mushroom-body lobe/calyx–glia junctures
  [PMID:19104051 "immunohistochemical experiments demonstrate extensive localization of Klg protein at the junctures between the neuropil and neuropil glia, including the junctures between the lobes and calyces of the mushroom bodies and the surrounding glial cells"],
  consistent with an adhesive role at neurite/synaptic interfaces, but no direct klg loss-of-function
  axon-guidance or synapse-organization assay is in the cached literature. Non-core.
- **Long-term memory (IMP) — a genuine, acute requirement, but a distal/behavioral role.**
  klg (=rus) is required for protein-synthesis-dependent LTM and its protein rises on LTM induction
  [PMID:19104051 "Klg is acutely required for LTM but not anesthesia-resistant memory formation, and Klg expression increases upon LTM induction"];
  it is a downstream effector of Notch [PMID:19104051 "We propose that Klg is a downstream effector of Notch signaling that links Notch activity to memory"].
  Independently confirmed as an LTM mutant abolishing the α/β mushroom-body LTM calcium trace
  [PMID:21490205 "A third mutant, D0417, is within the Klingon (Klg) gene, which encodes a member of the Ig superfamily of cell adhesion molecules and has also been implicated in photoreceptor development"];
  [PMID:21490205 "Klg has been shown to be acutely required for LTM and regulated by Notch"].
- **NOT anesthesia-resistant memory (negated IMP, valid negative finding).** The same study shows Klg is
  specifically required for LTM but **not** ARM
  [PMID:19104051 "Klg is acutely required for LTM but not anesthesia-resistant memory formation"].
  The negated GO:0007615 annotation correctly records this specificity — keep negated:true, ACCEPT.
- **Behavioral response to ethanol (IMP, PMID:18435628).** The klg allele (ruslan) is among LTM mutants
  scored for ethanol behavior; ruslan shows increased ethanol sensitivity and reduced tolerance
  [PMID:18435628 "a number of mutants exhibited both increased sensitivity and reduced tolerance: either rapid (ikar, milord-1, and zolotistuy), chronic (iks and rafael), or both (ruslan)"].
  (The paper refers to mutants by original names; ruslan = klg per PMID:19104051.) Experimental but a
  distal/pleiotropic behavioral phenotype → non-core.

## Localization
- Plasma membrane (GPI-anchored, extrinsic component) [PMID:9043060 GPI linkage quote above].
- Neuronal cell body / axon / neuropil (IBA + immunostaining at neuropil-glia junctures) [PMID:19104051].

## Curation decisions (summary)
- Core MF: cell-cell adhesion mediator activity (GO:0098632) — homophilic Ig adhesion (IDA-backed).
- Core BP: homophilic cell-cell adhesion (GO:0007156); R7 cell differentiation / fate commitment
  (GO:0045466 / GO:0007465).
- Core CC: plasma membrane / extrinsic component of plasma membrane (GO:0005886 / GO:0019897).
- MODIFY bare protein binding (GO:0005515) → cell adhesion molecule binding (GO:0050839).
- MODIFY axon guidance receptor activity (GO:0008046) → cell-cell adhesion mediator activity (GO:0098632).
- KEEP_AS_NON_CORE: axon guidance (GO:0007411), synapse organization (GO:0050808),
  long-term memory (GO:0007616), behavioral response to ethanol (GO:0048149).
- ACCEPT (negated) the NOT anesthesia-resistant memory annotation (GO:0007615).
- Broad ARBA/IEA parents (GO:0009653, GO:0030154, GO:0160108) accepted as correct-but-general.
