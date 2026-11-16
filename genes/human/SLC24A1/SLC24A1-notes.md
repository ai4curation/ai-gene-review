# SLC24A1 (O60721) review notes

Session 2026-11-16, vision-disorder alignment campaign (dismech: Congenital_Stationary_Night_Blindness,
recessive CSNB1D; module visual_phototransduction part with GO:0008273).

## Synthesis

- NCKX1, the rod outer-segment K+-dependent Na+/Ca2+ exchanger (SLC24 family, CaCA superfamily),
  exchanges 4 Na+ for 1 Ca2+ + 1 K+ [Reactome:R-HSA-425678 "all able to exchange one Ca2+ and one K+ for four Na+"].
- Human NCKX1 activity measured directly in HEK293 cells (reverse-mode Ca2+ influx, cation
  dependencies) [PMID:26631410, abstract only].
- Bovine immunohistochemistry: rod NCKX1 only in the outer-segment plasma membrane, not discs,
  inner segment or cones [PMID:10662833 full text]; human cDNA cloned from retina [PMID:9478004].
- Physiology (bovine ROS): extrudes Ca2+ entering through CNG channels in the dark and lowers
  cytosolic Ca2+ in light, the signal for light adaptation [PMID:10662833; PMID:7539424].
- Human genetics: homozygous frameshift p.F538CfsX23 segregates with recessive CSNB [PMID:20850105].
  That paper's IHC places SLC24A1 in inner segment and nuclear layers in human/mouse, which
  conflicts with the bovine outer-segment result; not used for location.
- GO:0008273 calcium, potassium:sodium antiporter activity is the right MF; I agree with the
  dismech module part.
- Wrong or over-propagated rows: calcium channel activity (IBA; an exchanger is not a channel);
  LTP/LTD (IBA from the NCKX2 Slc24a2 knockout hippocampal phenotype; NCKX1 is the rod
  exchanger); outer membrane GO:0019867 (NAS 2002, a bacterial/organelle term, the paper says
  "outer segments"); neuronal cell body (ISS from chicken in situ hybridization, transcript not protein).
- Physiological transport direction is Ca2+ export; the "import" row reflects the reverse-mode assay.
