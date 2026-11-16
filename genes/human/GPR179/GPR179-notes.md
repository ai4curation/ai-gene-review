# GPR179 (Q6PRD1) review notes

Session 2026-11-16, DISMECH vision-alignment campaign (complete CSNB).

## Biology (with provenance)

- Orphan class C GPCR (GPR158/179 group), 7TM with very large intracellular C-terminus; no known ligand.
- Required for depolarizing bipolar cell (DBC) transmission: nob5 mouse, zebrafish knockdown, human
  cCSNB (CSNB1E) [PMID:22325362]; localised to DBC dendritic terminals with GRM6 (mouse) [PMID:22325362]
  and to ON-BC dendrite tips in human retina [PMID:24084093].
- Anchors R7 RGS-Gbeta5 GAP complexes: "GPR158/179 recruited RGS complexes to the plasma membrane and
  augmented their ability to regulate GPCR signaling"; loss of GPR179 in nob5 prevents RGS targeting to
  the postsynaptic compartment [PMID:22689652] (heterologous cells; mouse retina).
- RGS7 binds a conserved site in GPR179; GPR179 binds R9AP; GPR179 needed for R9AP accumulation
  [PMID:26961947] (mouse).
- Complexes with mGluR6, TRPM1 and RGS proteins in mouse retina [PMID:24114537].
- Transsynaptic: binds HSPGs including pikachurin (EGFLAM), which with dystroglycan recruits the
  postsynaptic complex [PMID:30282023].

## GO-CAM gomodel:689e7a5d00000901 (human, UniProt curator, ISS from mouse MGI:2443409)

GPR179 activity = protein-membrane adaptor activity (GO:0043495), has input RGS7, part of protein
localization to plasma membrane (GO:0072659), occurs in dendrite terminus of ON-bipolar cell; the
pikachurin activity (molecular adaptor) is linked upstream of it. Agree with the MF and process: the
RGS-anchoring role is what the experimental data show; GPCR (G protein activation) activity is not shown.
The upstream causal link from pikachurin is reasonable as a localization dependency (PMID:30282023), but
is better read as positioning than as regulation of the adaptor activity itself.

## Decisions summary

- GPCR activity (InterPro IEA) MARK_AS_OVER_ANNOTATED: no G protein activation shown for an orphan whose
  established activity is RGS anchoring.
- GPCR signaling pathway -> G protein-coupled glutamate receptor signaling pathway (GAP anchoring shapes
  the mGluR6-Go signal); consistent with GRM6/TRPM1.
- Protein binding IPIs (HSPGs, pikachurin) -> heparan sulfate proteoglycan binding.
