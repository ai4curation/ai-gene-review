# Map2k3 (mouse MKK3/MEK3, UniProt O09110) - manual literature synthesis

No deep-research API was available; this synthesis was assembled manually from the
cached publications in `publications/` and the UniProt record. Each assertion carries
inline provenance.

## Identity and family

- Mouse Map2k3 encodes MKK3 (MEK3), a 347-aa member of the STE Ser/Thr kinase group,
  MAP kinase kinase subfamily [file:mouse/Map2k3/Map2k3-uniprot.txt "Belongs to the protein kinase superfamily. STE Ser/Thr protein kinase family. MAP kinase kinase subfamily."].
- Two splice isoforms are recorded (isoform 2, also called MKK3b, displayed; isoform 1).
  MKK3b was isolated from mouse in a yeast genetic screen [PMID:8900184 "Using a genetic screen in yeast, we isolated MKK3b, an alternatively spliced form of MKK3."].

## Molecular function: p38-directed MAP kinase kinase

- UniProt (by similarity to human P46734): "Catalyzes the concomitant phosphorylation of a
  threonine and a tyrosine residue in the MAP kinase p38" [file:mouse/Map2k3/Map2k3-uniprot.txt].
- Activation-loop Ser218/Thr222 dual phosphorylation by MAP3Ks activates it [file:mouse/Map2k3/Map2k3-uniprot.txt "Activated by dual phosphorylation on Ser-218 and Thr-222."].
- MKK3b is a specific p38 activator [PMID:8900184 "Like MKK3 and MAPKK6, MKK3b was shown to be a specific activator for p38 and was activated by osmotic shock when expressed in COS7 cells."].
- Specificity: "The MKK3 and MKK6 protein kinases are specific for p38 MAP kinase, whereas the MKK4 protein kinase can activate both p38 MAP kinase and JNK." [PMID:10097111].

## Upstream regulation

- ASK1 (Map3k5) phosphorylates MKK3; MPK38/Stk38 enhances ASK1 signalling by "increased interaction between ASK1 and its substrate MKK3" [PMID:18948261].
- In the ischaemic rat heart, MKK3 and MKK6 (not MKK4) are activated, with different kinetics [PMID:20550965 "Both of the known p38 activators MKK3 and MKK6 were activated by ischaemia but with different time courses"]; ASK1 preferentially couples to MKK6 there [PMID:20550965 "in ischaemic neonatal cardiac myocytes ASK1 expression preferentially activated MKK6 rather than MKK3"].
- Scaffold: JIP4 activates p38 "by a mechanism that requires the MAP kinase kinases MKK3 and MKK6" [PMID:15767678].
- Negative regulation: the PP2A regulatory subunit alpha-4 (Igbp1) targets PP2A to MEK3 and dephosphorylates Thr193 of the activation loop [PMID:17438131 "FLAG-alpha-4 coprecipitated hemagglutinin-MEK3 plus endogenous protein phosphatase 2A (PP2A) and selectively enhanced dephosphorylation of Thr193, but not Ser189, in the activation loop of MEK3."].

## Physiology from mouse genetics

- Mkk3-/- mice are viable; MEFs show a selective defect in TNF-induced p38 activation and IL-1/IL-6 expression [PMID:10097111 "Mkk3 gene disruption caused a selective defect in the response of fibroblasts to the proinflammatory cytokine tumor necrosis factor, including reduced p38 MAP kinase activation and cytokine expression."].
- Redundancy with MKK6 is proposed to explain the mild phenotype [PMID:10097111 "It is likely that a more profound defect in p38 MAP kinase signaling was not observed because the function of the MKK3 protein kinase is partially redundant to the MKK4 and MKK6 protein kinases."].
- Mkk3-/- macrophages and dendritic cells are defective in IL-12 production [PMID:10202148 "Mkk3(-/-) mice were viable and fertile; however, they were defective in interleukin-12 (IL-12) production by macrophages and dendritic cells."].
- Cardiac gain-of-function: activated MKK3bE in ventricular myocytes induced p38 activity, contractile depression and atrophy [PMID:11593045 "Targeted activation of p38 MAP kinase in ventricular myocytes was achieved in vivo by using a gene-switch transgenic strategy with activated mutants of upstream kinases MKK3bE and MKK6bE."]. This is an overexpression phenotype, not evidence for a normal role in contraction.

## Summary

MKK3 is a dedicated MAP2K of the p38 stress/cytokine MAPK cascade, partly redundant with
MKK6, with non-redundant roles in TNF-induced p38 activation and inflammatory cytokine
(IL-1, IL-6, IL-12) production.
