# SLC34A2 / NaPi-IIb (human, O95436) curation notes

Deep research providers were unavailable; evidence from cached publications and UniProt.

## Localization (benchmark-relevant)
- Multi-pass **apical** plasma membrane transporter of polarized epithelia; the large glycosylated
  extracellular loop faces the lumen and is the face used by ADC antibodies.
  UniProt `SUBCELLULAR LOCATION: Apical cell membrane; Multi-pass membrane protein.
  Note=Localized at the brush border membranes of enterocytes.`
  [PMID:12488042 "The recently cloned NaPi-IIb cotransporter is an apical membrane protein that is
  involved in the absorption of phosphate in the intestine."]
- Generic `plasma membrane` and `membrane` rows MODIFYed to `GO:0016324 apical plasma membrane`;
  the antibody-imaging `nucleoplasm` and `cytosol` rows marked over-annotated; `vesicle` kept as
  non-core (regulated apical insertion pool).

## Function
- 3 Na+ : 1 phosphate electrogenic symport, UniProt `Reaction=3 Na(+)(out) + phosphate(out) = 3
  Na(+)(in) + phosphate(in)`; Km(Pi) ~106-113 uM, Km(Na) ~34-65 mM [PMID:12488042];
  oocyte functional characterization [PMID:10329428].
- Oestrogen upregulates expression and intestinal phosphate absorption [PMID:12893629] — kept as
  non-core regulatory context.
- Disease relevance (pulmonary alveolar microlithiasis; ROS1 fusion partner) noted in the
  description only.
