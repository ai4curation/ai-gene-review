# Mapk8 (rat, P49185) - manual literature research

No deep-research API provider was available for this session. This file records the
literature work done by hand from the cached publications in `publications/` and the
UniProt record. Every statement carries inline provenance.

## Identity and family

- Rat Mapk8 encodes JNK1 / SAPK gamma, a 411-aa member of the CMGC Ser/Thr kinase group,
  MAP kinase subfamily [file:rat/Mapk8/Mapk8-uniprot.txt "Belongs to the protein kinase
  superfamily. CMGC Ser/Thr protein kinase family. MAP kinase subfamily."].
- Kinase domain 26-321, catalytic Asp151 proton acceptor, activation-loop TXY motif 183-185
  [file:rat/Mapk8/Mapk8-uniprot.txt "The TXY motif contains the threonine and tyrosine
  residues whose phosphorylation activates the MAP kinases."].
- InterPro IPR008351 (MAPK_JNK) and PANTHER PTHR24055 place it in the JNK clade.

## Activation and regulation

- Activated by dual phosphorylation of Thr183/Tyr185 by MAP2K4 and MAP2K7 (by similarity to
  human P45983) [file:rat/Mapk8/Mapk8-uniprot.txt "Dually phosphorylated on Thr-183 and
  Tyr-185 by MAP2K7 and MAP2K4, which activates the enzyme."].
- In rat cerebellar granule neurons deprived of potassium, MKK7 (not MKK4) is the upstream
  activator of the JNK pathway [PMID:11849756 "These data suggest that MKK7 is responsible for
  activating the JNK pathway during LK-induced CGN apoptosis."].
- Inhibited by S-nitrosylation of Cys116 after IFN-gamma-induced NO production; rat alveolar
  macrophages were among the cells tested [PMID:11121042 "Substitution of serine for
  cysteine-116 in JNK1 abolished the inhibitory effect of IFN-gamma or SNAP on JNK1 activity in
  vivo or in vitro, respectively."].
- Activated in perfused rat heart by H2O2 and ischaemia/reperfusion [PMID:9516415 "H2O2
  activated both SAPKs/JNKs and p38-MAPK."]; by IL-1 beta in rat UMR-106 osteoblastic cells
  [PMID:9513050 "Both JNK1 and JNK2 were activated by IL-1 beta."]; by TNF-alpha, HGF and
  hyperosmotic glucose in primary rat hepatocytes [PMID:9487126].

## Substrates and direct functions (rat or rat-cell experiments)

- c-Jun Ser63 phosphorylation downstream of SEK/JNK1 in rat hepatocytes, required for agonist
  stimulated DNA synthesis [PMID:9487126 "These data demonstrate that multiple agonists
  stimulate DNA synthesis in primary cultures of hepatocytes via a Ras/Rac1/Cdc42/SEK/JNK/c-Jun
  pathway."].
- SCG10/stathmin-2 Ser62/Ser73 phosphorylation; JNK1 controls microtubule dynamics and
  axodendritic length in rat cortical neurons [PMID:16618812 "These data suggest that JNK1 is
  responsible for regulation of SCG10 depolymerizing activity and neurite elongation during
  brain development."]. Active JNK and SCG10 co-fractionate in vesicular (P2) membranes
  [PMID:16618812 "active JNK, SCG10, and S73-phosphorylated SCG10 concentrated in the P2
  fraction, containing predominantly endosomal and Golgi vesicles"].
- SCG10 phosphorylation by cytoplasmic JNK1 restrains exit from the multipolar stage and radial
  migration [PMID:21297631 "the phosphorylation of SCG10 by JNK1 is a fundamental mechanism that
  governs the transition from the multipolar stage and the rate of neuronal cell movement during
  cortical development."].
- Paxillin Ser178 phosphorylation, needed for rapid migration of rat NBT-II bladder carcinoma
  cells [PMID:12853963 "JNK1 phosphorylates serine 178 on paxillin, a focal adhesion adaptor,
  both in vitro and in intact cells."].
- Synaptotagmin-4 Ser135 phosphorylation (PC12 cells, rat hippocampal neurons), which releases
  Syt4 from KIF1A and captures dense core vesicles at synapses [PMID:29166604 "Phosphorylation
  of serine 135 of Syt4 by JNK steers DCV trafficking by destabilizing Syt4-Kif1A interaction"];
  in PC12 cells [PMID:18046461 "JNK associated with phosphorylated synaptotagmin-4 (Syt 4)"].
- AMPA receptor GluR2L Thr912 and GluR4 Thr855 phosphorylation; JNK1 co-precipitates with these
  subunits from rat brain [PMID:18188153 "JNK1 phosphorylated both GST-GluR2L and GST-GluR4
  extremely effectively in vitro"].

## Cell-survival and apoptosis phenotypes (context dependent)

- Pro-apoptotic: antisense JNK1 blocked reoxygenation-induced apoptosis of rat cardiac
  myocytes [PMID:11259632]; beta-amyloid-induced p53 stabilisation and apoptosis of cortical
  neurons [PMID:12534344]; tamoxifen-induced apoptosis of rat glioma cells [PMID:14997384].
- Anti-apoptotic: JNK1 shRNA increased palmitate/high-glucose-induced apoptosis of INS-1 beta
  cells [PMID:24475223 "These data suggest that JNK1 protects against palmitate and high"];
  SP600125 increased apoptosis during simulated ischaemia/reperfusion of neonatal
  cardiomyocytes [PMID:15309413 "JNK phosphorylation is protective in our cell model"].
- These opposing outcomes are cell-type and stimulus specific; they are downstream
  consequences of the kinase acting on different substrates, not distinct activities.

## Metabolic stress

- Palmitate activates JNK in rat H4IIEC3 hepatocytes via mitochondrial ROS, and the pan-JNK
  inhibitor SP600125 restores insulin-stimulated Akt/GSK-3 phosphorylation [PMID:19332540
  "These results suggest that JNK activation by palmitate contributed to palmitate-induced
  insulin resistance."]. The study did not distinguish JNK1 from JNK2 (pharmacological
  inhibition only), so it does not by itself attribute the effect to Mapk8.
- Oxidative stress in rat islets suppresses insulin gene expression through JNK, with reduced
  PDX-1 DNA binding [PMID:12011047].

## Localisation

- Cytoplasm (cortical neurons, predominantly cytoplasmic and on Golgi/endosomal membranes)
  and nucleus [file:rat/Mapk8/Mapk8-uniprot.txt "In the cortical neurons, predominantly
  cytoplasmic and associated with the Golgi apparatus and endosomal fraction"].
- Adult rat CNS: cytoplasm, dendrites and axons of neurons [PMID:9714150 "All four kinases
  were present in the cytoplasm, dendrites, and axons of neurons."].
- Phosphorylated JNK concentrated at synapses after neuronal activity [PMID:29166604].
