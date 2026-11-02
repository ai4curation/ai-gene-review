# RTL9 (SIRH10 / Retrotransposon Gag-like 9) — curation notes

RTL9 is a eutherian *sushi-ichi*/Ty3-gypsy-derived (Gag-like) domesticated gene.
Human review is by orthology to mouse functional studies (ISS); human–mouse
orthologs are strongly conserved across the functional Gag module.

## Function
- Unlike the secreted traps RTL5/RTL6, RTL9 is **intracellular and lysosomal**,
  acting within microglial lysosomes on phagocytosed fungal cell-wall material
  [PMID:37834332 "The RTL9 protein is localized in the microglial lysosomes where incorporated zymosan is digested."].
- Required, via its C-terminal retroviral Gag capsid-like region, for degradation
  of zymosan (a fungal PAMP)
  [PMID:37834332 "We have demonstrated that eutherian-specific RTL9 has functions in the innate antifungal immunity in the brain because Rtl9 KO mice lost zymosan degradation activity."].

## Curation decisions
- Because RTL9 acts intracellularly on the fungal material (not as an
  extracellular trap), the cellular-response framing GO:0071226 cellular response
  to molecule of fungal origin is retained, unlike RTL5/RTL6.
- Defense response to fungus is NOT proposed: only zymosan (a PAMP), not live
  fungal infection, was tested.
- The standalone GO:0045087 innate immune response proposal was dropped.
