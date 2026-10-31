# MAP3K3 (MEKK3) curation notes

UniProt Q99759, 626 aa (isoform 1). N-terminal PB1 domain (PB1_MEKK2/3), N-terminal amphiphilic helix
that binds CCM2, C-terminal STE11-family Ser/Thr kinase domain. Paralog of MAP3K2/MEKK2.

## Molecular function

- MAP3K activating MEK5 (ERK5 pathway) [PMID:10593883 "we have identified MEKK3 as a molecule that physically interacts with MEK5"; "MEKK3 activity is required for growth factor mediated cellular activation of endogenous BMK1"].
- PB1-PB1 binding to MEK5 [PMID:12912994 "the PB1 domain mediates the association of MEKK2 and MEKK3 with MEK5"].
- Activates SEK1 (MKK4) and MEK1 directly, SAPK and ERK pathways, and NF-kB reporter
  [PMID:9006902 "We now demonstrate that MEKK3 activates SEK and MEK, the known kinases targeting SAPK and ERK, respectively."].
- Activation loop Ser526 autophosphorylation, needed for activity; 14-3-3 binding protects pSer526
  [PMID:16407301 "Ser526 of MEKK3 is an autophosphorylation site within the T-loop that is regulated by PP2A and 14-3-3 proteins"].
- Thr294 phosphorylation promotes 14-3-3 binding and restrains NF-kB activation [PMID:18308725].
- Directly phosphorylates IKK in TNF signalling [PMID:11429546 "MEKK3 interacts with RIP and directly phosphorylates IKK"].
- Hippo: MEKK2/3 phosphorylate LATS1/2 and YAP/TAZ; STRIPAK inhibits MEKK3 via CCM2/CCM3 [PMID:33571521].

## Biological process

- NF-kB: essential for TNF-induced IKK/NF-kB activation in MEKK3-deficient fibroblasts [PMID:11429546];
  essential transducer of MyD88-IRAK-TRAF6 in IL-1R/TLR4 signalling [PMID:14661019 "MEKK3 is crucial for IL-1- and LPS-induced activation of NF-kappaB and JNK-p38 but not ERK"].
  Reactome: p62 scaffolds MEKK3:TRAF6 (R-HSA-507719).
- Cardiovascular development: Map3k3-/- mice die ~E11 with vascular defects [PMID:10700190 "Map3k3-/- embryos died at approximately embryonic day (E) 11, displaying disruption of blood vessel development"].
  CCM complex restrains MEKK3 in endothelium/endocardium; gain of MEKK3-KLF2/4 signalling drives CCM
  [PMID:25625206 "MEKK3 is both necessary and sufficient for expression of these genes"], [PMID:27027284].
  These are necessity/genetic observations; the process terms (blood vessel development, heart development)
  are left to MGI (mouse Map3k3 has GO:0001568 IMP from PMID:10700190) and not proposed as NEW here.
- Somatic gain-of-function p.Ile441Met in sporadic CCM (CCM5), increases MEK5/ERK5 phosphorylation in
  HUVECs [PMID:33891857], [PMID:33729480].

## Localization

- Cytosolic signalling kinase; Reactome places the MEKK3:p62:TRAF6 complex in cytosol.

## Annotation issues

- 38 bare protein-binding IPIs: 14-3-3 isoforms (YWHAB/E/G/H/Q/Z) -> GO:0071889 14-3-3 protein binding
  (supported by targeted work: PMID:12392720, 16407301, 18308725); MAP2K5 -> GO:0019901 protein kinase
  binding; TRAF7 (RING E3) -> GO:0031625; CCM2 (scaffold/adaptor) -> GO:0097110 scaffold protein binding.
- GO:0043123 IEP (PMID:12761501): an overexpression reporter screen; better supported by
  PMID:11429546/14661019 loss-of-function data; ACCEPT.
- NEW: GO:0070375 ERK5 cascade (IDA/IMP-type evidence PMID:10593883, PMID:12912994). Term is sparsely
  used (7 annotations total in human/mouse/rat), so the absence is not a convention; MEKK3 performs the MEK5
  phosphorylation step.

## Final decisions (review completed)

- ERK5 cascade (GO:0070375) proposed as the MODIFY replacement for the ARBA intracellular signal transduction IEA
  rather than as a separate NEW (a NEW would duplicate the replacement). Comparator check: GO:0070375 is carried by
  MAP2K5 and MAPK7 (the other kinases of the same module); MAP3Ks routinely carry their cascade terms (e.g. JNK/p38
  cascades). MEKK3 performs the MEK5-phosphorylation step, so it passes the participation test.
- IDA intracellular signal transduction (PMID:15001576, TRAF7) -> MODIFY to MAPK cascade (AP1 output of MEKK3 runs
  through SEK/MEK [PMID:9006902]); kept consistent with the IEA row.
- 14-3-3 IPIs -> GO:0071889 (PMID:16407301, 18308725, 12392720, 9452471); MAP2K5 -> GO:0019901; TRAF7 (RING E3 per
  UniProt Q6Q0C0) -> GO:0031625; CCM2 (adaptor/scaffold) -> GO:0097110. Mirrors MAP3K2.
- IEP NF-kappaB (overexpression screen) ACCEPTED on the strength of loss-of-function data [PMID:11429546
  "MEKK3 plays a critical role in TNF-induced NF-kappaB activation"], [PMID:14661019].
- Blood vessel development not proposed as NEW for human (mouse Map3k3 carries it via IMP, acts_upstream); raised as a
  suggested question instead.
