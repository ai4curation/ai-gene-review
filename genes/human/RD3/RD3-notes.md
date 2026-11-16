# RD3 (Q7Z3Z2) review notes

Session 2026-11-16, vision-disorder alignment campaign (dismech: RD3-Related_Retinopathy, LCA12).

## Synthesis

- RD3 is a small (195 aa) soluble four-helix-bundle protein with no catalytic activity
  [PMID:30559291 "consisting of a four-helix bundle with a long unstructured loop between helices 1 and 2"].
- It binds the retinal membrane guanylyl cyclases RetGC1 (GUCY2D) and RetGC2 (GUCY2F)
  (mouse retina co-IP and HEK293 co-expression) [PMID:21078983].
- Inhibitor: purified human recombinant RD3 is a high-affinity allosteric inhibitor of
  RetGC, suppressing basal and GCAP-stimulated activity [PMID:21928830 "We find that RD3 acts as a high-affinity allosteric inhibitor of RetGC, capable of both effectively competing with GCAPs and suppressing the catalytic activity of the cyclase."].
  GO MF: GO:0030251 guanylate cyclase inhibitor activity ("Binds to and stops, prevents or
  reduces the activity of guanylate cyclase"). RD3 regulates the enzyme; it is not the enzyme.
- Trafficking: RD3 mediates export of GC1 from the ER to Rab11 endosomal vesicles in COS-7 /
  HEK cells, and RetGC is undetectable in rd3 mouse photoreceptors [PMID:21078983];
  AAV8-Rd3 in rd3 mice moves cyclase from the ER to rod and cone outer segments
  [PMID:23740938 "RD3 plays an essential role in the exit of guanylate cyclase from the ER"].
  No GO MF expresses "escort/chaperone of a cargo for ER exit"; recorded as the process
  GO:1903546 protein localization to photoreceptor outer segment.
- Survival mechanism (mouse): rd3 degeneration is alleviated by deleting GCAPs, and added RD3
  does not change GMP phosphorylation [PMID:33539922]. This argues against the GUK1-activation
  model of PMID:29515371 (purified-protein assay, mouse retina co-localization) as the
  physiologically important activity. Kinase activator activity not asserted.
- Location: mouse immunostaining is intense in rod and cone outer segments, faint in inner
  segments [PMID:21078983]. Nuclear/perinuclear/cytoplasmic staining comes from heterologous
  COS-1 overexpression [PMID:17186464] and a custom antibody IHC of human non-retinal tissues
  [PMID:29030614]; kept as non-core.
- Retina development: rd3 mouse retina develops normally to P14 before degenerating
  [PMID:21078983 full text]; the IBA/ISS retina-development rows are better expressed as
  retina homeostasis.
- Binary interactome hits (HuRI, PMID:25416956, 31515488, 32296183) carry no functional information.

## Species

Biochemistry on human recombinant RD3 (bacterially expressed) with human RetGC1 in HEK293
membranes; in vivo work in mouse (rd3) and dog (rcd2); human genetics (LCA12).
