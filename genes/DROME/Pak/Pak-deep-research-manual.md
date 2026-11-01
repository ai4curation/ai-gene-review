# Pak (Drosophila melanogaster, UniProt Q9VI13, FBgn0267698) -- manual literature synthesis

No deep-research API was available for this review; this summary was compiled manually from the
cached publications (`publications/PMID_*.md`), the UniProt record (`Pak-uniprot.txt`) and PubMed
searches. Most cached papers are abstract-only; PMID:24374353 is full text. PMC full text was
retrieved for PMID:21690310 through the PubMed full-text service (not cached).

## Identity and domain architecture

- Pak (DPAK, dPak, Dpak1; CG10295) is a 704-aa group I p21-activated kinase, the fly ortholog of
  mammalian PAK1/2/3. UniProt: "Belongs to the protein kinase superfamily. STE Ser/Thr protein
  kinase family. STE20 subfamily." A second group I PAK, Pak3, and a group II PAK, Mbt, are
  paralogs [PMID:15581872 "In Drosophila, two Group I kinases have been identified, dPak and Pak3"].
- Architecture (UniProt FT): N-terminal PXXP motif (residues 9-12; SH3 binding, ECO:0000269
  PMID:10399914), CRIB/GTPase-binding domain (83-96 / 83-113), autoregulatory region (80-171),
  linker, and C-terminal kinase domain (430-681; ATP-binding K459, proton acceptor D549).
- Group I Paks "possess an autoinhibitory domain that can suppress their kinase activity in trans"
  [PMID:15581872].

## Molecular function

- Binds GTP-bound Rac and Cdc42: "DPAK bound to activated (GTP-bound) Drosophila Rac (DRacA) and
  Drosophila Cdc42" [PMID:8628256]. Rac activation of Pak downstream of the Trio GEF:
  "This GEF domain activates Rac, which in turn activates Pak" [PMID:10847683].
- Binds the SH2/SH3 adaptor Dock (Dreadlocks) through its N-terminal PXXP motif; P9L and R14M
  abolish the interaction (UniProt MUTAGEN, PMID:10399914). "Dock and Pak colocalize to R cell axons
  and growth cones, physically interact" [PMID:10399914].
- Kinase activity is needed in vivo: "Normal patterns of R cell connectivity require Pak's kinase
  activity and binding sites for both Dock and Cdc42/Rac" [PMID:10399914]; K459A fails to rescue
  (UniProt). Catalytic activity in UniProt is by similarity to human PAK1 (Q13153).
- Complex with Pix and Git: "dPak and dGIT form a complex in the presence of dPIX" [PMID:18996366].
- Recruited to Robo: "Slit stimulation can recruit a complex of Dock and Pak to the Robo receptor
  and trigger an increase in Rac1 activity" [PMID:14527437].

## Biological roles

1. Axon guidance (best supported; core). Photoreceptor (R cell) axon guidance and targeting
   downstream of Dock [PMID:10399914 "These data establish Pak as a critical regulator of axon
   guidance and a downstream effector of Dock in vivo"]; Trio-Rac-Pak pathway [PMID:10847683];
   Bolwig's nerve pathfinding with Dscam and Dock [PMID:10892653]; olfactory axon pathfinding
   [PMID:12588847 "Dock and Pak form a signaling pathway that mediates the response of olfactory
   axons to guidance cues"]; Slit/Robo midline repulsion [PMID:14527437]. Pak is not needed for
   axon outgrowth in R cells (UniProt FUNCTION, PMID:10399914), though Rac/Cdc42 via Pak activate
   LIM kinase to restrain axon growth in mushroom-body neurons [PMID:15572110].
2. Postsynaptic development at the larval NMJ. Synaptic Pak depends on the RhoGEF dPix
   [PMID:11709153 "complete reduction of the serine/threonine kinase Pak and the subsynaptic
   reticulum"]; postsynaptic Pak signalling diverges into a Dock-dependent branch controlling
   glutamate receptor (GluRIIA) abundance and a Dock-independent branch controlling muscle
   membrane specialization (SSR) via Dlg [PMID:15295021]. dPAK is "a positive regulator for GluRIIA
   synaptic localization" and is modulated by Henji/Dbo [PMID:27736876]. dPAK is one of "two known
   regulators of SSR development" [PMID:19244343].
3. Epithelial morphogenesis / actin cytoskeleton. Elevated at the leading edge in dorsal closure
   [PMID:8628256]; required for integrity of the leading-edge cytoskeleton, but "did not affect the
   JNK cascade" [PMID:15581872]. Integrin-localized Pak recruits the Scribble complex in septate
   junction formation [PMID:20501591]. In follicle cells Pak is basally localized and required for
   polarized basal F-actin and apical-basal polarity [PMID:17383630]; antagonises Rho1 signalling
   [PMID:21098722].
4. Muscle morphogenesis and myotube guidance; Git localizes Pak to myotube termini
   [PMID:18996366 "dgit mutant muscles fail to localize the p21-activated kinase, dPak, to their
   termini"].
5. Ecdysone-triggered responses. pak is an ecdysone secondary response gene required for robust
   induction of death genes during salivary-gland destruction and contributes to leg-disc extension
   [PMID:24374353]. This is a genetic, upstream role; the mechanism (and whether kinase activity is
   needed) is unknown.
6. Heart: PMID:21690310 (Qian et al. 2011) tests Cdc42 with Tinman in the fly heart; in the text
   available to us Pak is only mentioned as a hypothesised Cdc42 effector ("we reasoned that Cdc42
   may act through the Pak pathway to regulate actin filament assembly and thus myofibrillar
   structure in the fly heart"). No Pak GO annotation derives from it.

## Localization

Cytoplasm [PMID:8628256]; colocalizes with focal adhesions/focal complexes and dynamic actin
[PMID:8628256]; axons and growth cones [PMID:10399914]; leading edge of dorsal epidermis
[PMID:8628256]; lateral membrane/septate junction region of epithelia [PMID:20501591]; postsynaptic
NMJ [PMID:11709153, PMID:15295021]; basal end of follicle cells [PMID:17383630].

## Caveats

- PMID:15169762 (human DSCAM activates PAK1) is a retracted publication; not used.
- No direct in vitro kinase assay on Drosophila Pak was visible in the abstracts available;
  kinase function rests on kinase-dead alleles/transgenes and homology.
