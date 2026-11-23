# didum (Myosin V, CG2146) — manual literature synthesis

No deep-research API keys were available for this review, so this file is a manual
literature synthesis built from cached publications (publications/PMID_*.md) and
PubMed searches ("(didum OR "myosin V" OR MyoV) AND Drosophila", 46 hits screened by title).
It is NOT the output of an automated deep-research provider.

UniProt: A1Z6Z8 (TrEMBL, unreviewed; 1800 aa); FlyBase FBgn0261397; GeneID 35680.

## Identity and domain architecture

- didum encodes the single Drosophila class V myosin heavy chain
  [PMID:9536440 "The gene encodes a 1792-residue, 207 kDa heavy chain polypeptide which possesses a typical head or motor domain of 771 residues, a region of six IQ motifs (139 residues) which serve as potential calmodulin/light chain binding sites at the head/tail junction"].
- Single myosin V gene, equally related to vertebrate Va and Vb
  [PMID:9536440 "Drosophila myosin V is more closely related to mammalian myosin Va and Vb than to other invertebrate class-V myosins"].
- UniProt A1Z6Z8 features: myosin motor domain 70..779 (PROSITE PS51456), Dilute
  cargo-binding domain 1474..1750 (PROSITE PS51126); Pfam Myosin_head, 4x IQ, DIL;
  PANTHER PTHR13140:SF706 (dilute class unconventional myosin).

## Motor biochemistry

- Non-processive, low-duty-ratio "ensemble" motor, unlike vertebrate myosin Va
  [PMID:15980429 "myosin V from Drosophila has a strikingly different motor mechanism from that of vertebrate myosin Va, and it is a nonprocessive, ensemble motor"].
- Translocates actin filaments in vitro at high surface density
  [PMID:15980429 "in in vitro motility assays, double-headed Drosophila myosin V requires high surface concentrations to exhibit a continuous translocation of actin filaments"].
- Actin-activated ATPase is autoinhibited by the globular tail domain and activated by
  Ca2+ and by GTP-Rab11 [PMID:25940004 "The actin-activated ATPase activity of DmM5 is significantly activated by micromolar levels of calcium."; "We found that GTP-bound dRab11, but not Ltd, significantly activates DmM5 actin-activated ATPase activity."].
- Light chains: calmodulin (Cam) and the essential light chain Mlc-c bind the IQ region
  [PMID:16917818 "We identify four myosins (myosin II, myosin V, myosin VI and myosin VIIA) and a microtubule-associated protein (asp/Abnormal spindle) as binding partners for the essential light chain"].
  The calmodulin-bridging paper (PMID:15178316) is explicitly about murine myosin-V IQ
  peptides in its abstract; the FlyBase IPI may rest on its full text (not cached).

## Cargo transport in photoreceptors

- Rab11-dRip11-MyoV complex delivers rhodopsin-bearing post-Golgi vesicles to the
  rhabdomere base [PMID:17517962 "Binary yeast two hybrids and in vitro protein-protein interaction predict a ternary complex assembled by independent dRip11 and MyoV binding to Rab11."].
- Loss of MyoV causes cytoplasmic rhodopsin accumulation, stunted rhabdomeres and
  ectopic basolateral rhabdomeres [PMID:17517962 "MyoV-reduced photoreceptors also developed ectopic rhabdomeres inappropriately located in basolateral membrane, indicating a role for MyoV in photoreceptor polarity."].
- Crumbs binds and stabilizes MyoV; loss of crb reduces MyoV and Rh1 delivery
  [PMID:22105348 "we show that myosin V (MyoV) coimmunoprecipitated with the Crb complex and that loss of crb led to severe reduction in MyoV levels"].
- Ca2+-activated MyoV pulls pigment granules (via adaptor Lightoid) to the rhabdomere —
  the "longitudinal pupil" [PMID:18585038 "Here we show that Ca(2+)-activated Myosin V (MyoV) pulls pigment granules to the rhabdomere."].

## Oocyte polarity and oskar mRNA

- Posterior-group gene; promotes posterior Oskar accumulation via cortical anchoring
  [PMID:19481457 "didum, encoding the Drosophila actin-based motor Myosin-V, is a new posterior group gene that promotes posterior accumulation of Oskar"].
- Kinesin-1 vs myosin-V competition defines posterior determination
  [PMID:32057294 "While kinesin-1 removes osk/Staufen from the cortex along microtubules, myosin-V anchors osk/Staufen at the cortex."].
- Spire–MyoV direct interaction is dispensable in mid-oogenesis [PMID:41358557].

## Other roles

- Larval viability and spermatid individualization (investment cones)
  [PMID:16126191 "Mutant animals exhibit no detectable defects during embryogenesis but are delayed in larval development; most die prior to 3rd instar."].
- Myosin V depletion increases MT-based mitochondrial transport in cultured neurons
  [PMID:20592219 "we observed a significant increase in mitochondrial transport during myosin V depletion"].
- Apical transport of Crumbs in follicle cells [PMID:31881198 "polarized trafficking of Crb is mediated by transport along microtubules by the motor protein Dynein and along actin filaments by the motor protein Myosin-V (MyoV)"].
