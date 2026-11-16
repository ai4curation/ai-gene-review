# GRM6 (mGluR6, O15303) review notes

Session 2026-11-16, DISMECH vision-alignment campaign (CSNB, Schubert-Bornschein complete form).

## Biology (with provenance)

- Class C GPCR (group III mGluR), 7TM with large Venus-flytrap glutamate-binding ectodomain;
  "G protein-coupled receptor for glutamate" [file:human/GRM6/GRM6-uniprot.txt].
- Expressed in retinal ON bipolar cells; mouse knockout loses ON responses
  [PMID:9215706 "mGluR6 is restrictedly expressed in the retinal ON bipolar cells and ablation of mouse mGluR6 by gene targeting results in a loss of ON responses to light stimulus"]
  [PMID:7889569 "The results demonstrate that mGluR6 is essential in synaptic transmission to the ON bipolar cell"] (mouse).
- Effector: Go, not adenylate cyclase, in ON bipolar cells
  [PMID:11124982 "establishes that the light response of the ON bipolar cell requires G(o)"] (mouse);
  [PMID:30027108 "The glutamate receptor, mGluR6, signals via the heterotrimeric G protein Go, which in turn gates a transduction channel by an unknown mechanism"];
  [PMID:30027108 "In the dark, tonic release of glutamate activates mGluR6, keeping the channel closed"].
  The channel is TRPM1 [PMID:19966281 "its activity is negatively regulated by Go in the mGluR6 cascade"] (mouse).
- Location: dendritic tips of ON bipolar cells, colocalising with TRPM1 [PMID:19966281]. Heterologous
  wild-type human mGluR6 reaches cell surface, passing ER and Golgi; CSNB missense mutants are retained
  in ER, dimerisation unaffected [PMID:17405131] (transfected cells; abstract only).
- Melanocytes (human): mGluR6 agonist L-AP4 increases TRPM1-dependent Ca2+ uptake; opposite polarity
  to retina because Galpha-o is absent [PMID:23452348]. Non-core for the retina.
- Mouse knockout behaviour: failure of light-onset suppression of wheel running (masking) is a
  consequence of lost ON pathway [PMID:10842024].

## Decisions summary

- Adenylate-cyclase-inhibiting MF/BP rows (IBA/IEA, group II/III family) generalised to
  GO:0098988 / GO:0007216: in the native cell the effector is TRPM1 via Go.
- Detection-of-light rows -> visual perception (the receptor detects glutamate, not light).
- Mouse "new growing cell tip" (GO:0035841, a fission-yeast cell-polarity term) IDA from PMID:19966281
  is a mis-chosen term for dendritic tips; projected here by Ensembl Compara. Recorded as source defect (MGI).
- ER and Golgi membrane rows: biosynthetic transit of overexpressed protein -> MARK_AS_OVER_ANNOTATED.
