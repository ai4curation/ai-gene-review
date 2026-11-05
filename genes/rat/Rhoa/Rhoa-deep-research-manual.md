# Rhoa (rat, UniProt P61589) - manual literature synthesis

No deep-research API provider was available for this session. This file was
written by the reviewer from the cached publications in `publications/` and the
UniProt record `Rhoa-uniprot.txt`. Every claim carries its provenance.

## Identity and family

- Rat RhoA (Transforming protein RhoA, 193 aa) is a Rho-family small GTPase of the
  Ras superfamily. UniProt: "Belongs to the small GTPase superfamily. Rho family."
  Domain/family signatures: InterPro IPR001806 (Small_GTPase), IPR003578
  (Small_GTPase_Rho), Pfam PF00071 (Ras), PROSITE PS51420 (RHO), PANTHER PTHR24072
  (RHO FAMILY GTPASE) [file:rat/Rhoa/Rhoa-uniprot.txt].
- The mature protein is C-terminally processed (residues 191-193 removed) and
  geranylgeranylated (CAAX box), which anchors it to the cytoplasmic face of
  membranes [file:rat/Rhoa/Rhoa-uniprot.txt "Removed in mature form"].
- The RhoA protein sequence is identical in rat, mouse and human, so
  biochemistry performed with human or mouse RhoA applies directly to the rat
  protein.

## Molecular function: a GTP/GDP switch

- UniProt FUNCTION: "Small GTPase which cycles between an active GTP-bound and an
  inactive GDP-bound state." In the active state it "binds to a variety of effector
  proteins to regulate cellular responses such as cytoskeletal dynamics, cell
  migration and cell cycle" [file:rat/Rhoa/Rhoa-uniprot.txt].
- Direct nucleotide exchange assay: "free RhoA rapidly exchanged its bound
  nucleotide (GDP) with GTP, and the reaction was saturated after 15 min" while
  "RhoA complexed to RhoGDIα did not undergo nucleotide exchange"
  [PMID:20472934]. Phosphorylation of RhoGDIalpha at Ser34 by PKCalpha releases
  RhoA: "Upon phosphorylation, the GDI cannot retain RhoA efficiently,
  facilitating its activation by nucleotide exchange" [PMID:20472934]. This work
  used rat embryo fibroblasts for the cellular GTP-RhoA measurements.
- RhoGDI interaction in rat smooth muscle: "C3 exoenzyme increased RhoA-RhoGDI
  binding and reduced the levels of RhoA-GTP and p(Thr696)-MYPT1" [PMID:17379756].
- GEF input: rat AKAP-Lbc (Akap13; Rt31) co-immunoprecipitates RhoA from rat
  renal collecting duct cells [PMID:11696353], and AKAP-Lbc is "critical for
  activating RhoA and transducing hypertrophic signals downstream of alpha1-adrenergic
  receptors" in rat cardiomyocytes [PMID:17537920]. GEF-H1 "activates RhoA by
  enhancing the rate of exchange of bound GDP for GTP" [PMID:20858895].
- Effectors: UniProt lists ROCK1, ROCK2, PRKCL1 (PKN1), PKN2, DIAPH1, rhotekin
  (RTKN), PLCE1, KCNA2 [file:rat/Rhoa/Rhoa-uniprot.txt]. For rat Kv1.2 (KCNA2):
  "RhoA regulates Kv1.2 activity and is a central component in the mechanism of
  receptor-mediated tyrosine kinase-dependent suppression of Kv1.2" [PMID:9635436].

## Biological roles

- Actin stress fibres and focal adhesions: "Regulates a signal transduction
  pathway linking plasma membrane receptors to the assembly of focal adhesions and
  actin stress fibers" [file:rat/Rhoa/Rhoa-uniprot.txt]. Rat cerebral arteries:
  "UTP-induced actin polymerization was attenuated in RhoA-depleted arteries"
  after siRNA knockdown [PMID:17369454].
- Rat brain endothelium: ICAM-1 cross-linking "induces a strong activation of
  RhoA in RBE4 cells", and PECAM-1 engagement "completely inhibited ICAM-1-induced
  RhoA activation" [PMID:17662049], linking RhoA to receptor-driven cortical actin
  rearrangement.
- Cytokinesis: "Plays an essential role in cleavage furrow formation" and is
  "Involved in a microtubule-dependent signal that is required for the myosin
  contractile ring formation during cell cycle cytokinesis" (by similarity to
  human/mouse) [file:rat/Rhoa/Rhoa-uniprot.txt].
- Neurons: RhoA/ROCK restrains neurite initiation: "RhoA and its specific
  downstream effector ROCK are essential during neuritogenesis in mammalian
  hippocampal neurons by modulating actin stability" and "RhoA inactivation induces
  neurons to sprout more processes" [PMID:14517206]. In rat hippocampal slices,
  "RhoA and Cdc42 were rapidly activated in the stimulated spine" and
  "Inhibition of the Rho-Rock pathway preferentially inhibited the initial spine
  growth" [PMID:21423166]. Active RhoA decreases dendrite number by lowering cypin
  [PMID:17670984]. In PC12 cells RhoA siRNA increased branching of Rin-induced
  neurites [PMID:14662747].
- Smooth muscle contraction: RhoA/ROCK maintains internal anal sphincter basal
  tone [PMID:17379756]; agonist-induced constriction of rat cerebral arteries
  requires RhoA [PMID:17369454].
- Cell survival/death signalling (context dependent): "Rho is required for the
  rapid glutamate-induced activation of p38alpha and ensuing neuronal death"
  [PMID:17369826]; RhoA-ROCK signalling mediates survival of mutant-huntingtin
  striatal cells after microtubule depolymerisation [PMID:20858895].
- Migration: Nogo "enhances the adhesion and inhibits the migration of OECs via NgR
  regulation of RhoA" [PMID:17488779]; progesterone inhibits rat aortic smooth
  muscle migration "through RhoA inactivation induced by cSrc-enhanced RhoA
  degradation" [PMID:21440892].

## Pathophysiology-only literature (expression/activity changes)

Many rat papers in GOA report changes in RhoA expression or activity under
stimuli (diabetes, ethanol, hypoxia, glucocorticoids, phenylalanine, anaesthetics,
statins) [PMID:12095538, PMID:17109064, PMID:17442046, PMID:16205723,
PMID:18391481, PMID:17515837, PMID:17492663, PMID:17596891, PMID:18356410]. These
show that RhoA activity is modulated in disease models; they do not identify new
RhoA activities.
