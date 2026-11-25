# NPC1L1 notes

Review created to support a two-part enterocyte sterol uptake/efflux module
(`modules/intestinal_sterol_absorption_and_efflux.yaml`) with ABCG5/ABCG8. Literature
work was done manually from cached publications (Falcon deep research was launched in
parallel; if it completes, its output is the separate `-deep-research-falcon.md` file).

## Key findings

- Required for intestinal cholesterol absorption; brush-border localization
  [PMID:14976318 "We show that Niemann-Pick C1 Like 1(NPC1L1) protein plays a critical role in the absorption of intestinal cholesterol."]
- Direct target of ezetimibe
  [PMID:15928087 "These results unequivocally establish NPC1L1 as the direct target of ezetimibe"]
- N-terminal domain binds cholesterol (not plant sterols)
  [PMID:21602275 "NPC1L1-NTD specifically binds cholesterol but not plant sterols"]
- Uptake by sterol-induced clathrin/AP2 endocytosis
  [PMID:18522832 "cholesterol is internalized into cells with NPC1L1 through clathrin/AP2-mediated endocytosis"]
- NUMB recognizes the YVNXXF motif and recruits clathrin
  [PMID:24336247 "Numb, a clathrin adaptor, specifically recognized this motif and recruited clathrin for internalization."]
- Return to PM on sterol depletion via myosin Vb-Rab11a-Rab11-FIP2
  [PMID:19542231 "Cellular cholesterol depletion induces the transport of NPC1L1 from the endocytic recycling compartment to the plasma membrane (PM)"]
- Homodimer; intramolecular channel for cholesterol and vitamin E
  [PMID:34407950 "the same intramolecular channel in hNPC1L1 mediates transport of VE and cholesterol"]
- Alpha-tocopherol uptake via NTD
  [PMID:28315682 "NPC1L1 recognizes α-tocopherol via its NTD and mediates α-tocopherol uptake through the same mechanism as cholesterol absorption"]

## Curation decisions

- Core MF: cholesterol binding (GO:0015485). GO:0015248 sterol transporter activity is
  obsolete, so the uptake role is expressed through GO:0030299 / GO:0030301.
- PMID:17140581 (ezetimibe pharmacogenetics) IMP rows for cholesterol biosynthesis and
  lipoprotein metabolism marked over-annotated (indirect systemic effects).
- Vitamin E metabolic process modified to vitamin transport.
- Bare protein-binding IPI rows removed as uninformative (interactions are real; NPC1L1 is cargo).
