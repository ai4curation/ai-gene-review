# RAC1 (human, P63000) curation notes

Deep research providers were unavailable in this environment; evidence below is from cached
publications and the UniProt record.

## Localization (benchmark-relevant)
- RAC1 is an **intracellular** protein: prenylated at Cys189 and attached to the **inner (cytoplasmic)
  leaflet** of the plasma membrane, with a soluble RhoGDI-bound cytosolic pool. UniProt:
  `SUBCELLULAR LOCATION: Cell membrane ...; Lipid-anchor; Cytoplasmic side` and
  "Note=Inner surface of plasma membrane possibly with attachment requiring prenylation of the
  C-terminal cysteine". It is NOT exposed on the cell surface.
- Functional sub-locations accepted: cytosol, cell cortex, lamellipodium, ruffle membrane,
  postsynapse/glutamatergic synapse, NADPH oxidase complex (recorded as `in_complex`).
- `cytoplasm` marked TOO_GENERAL (entailed by cytosol/plasma membrane/lamellipodium);
  `membrane` and `cytoskeleton` modified to the specific supported terms; pericentriolar material
  and kinocilium marked over-annotated.
- Nuclear pool retained as non-core: [PMID:12551911 "We show that the Rac1 PBR has significant NLS
  activity when it is fused to green fluorescent protein (GFP) or in the context of full-length
  Rac1."]

## Core activities
1. GTPase switch driving branched actin polymerization, lamellipodia/ruffles, spreading, polarity
   and migration. UniProt: "small GTPase which cycles between active GTP-bound and inactive
   GDP-bound states"; "In its active state, binds to a variety of effector proteins".
   [PMID:9312003 "remodels the actin cytoskeleton by inducing actin polymerization at the cell
   periphery"]; [PMID:19625648 neutrophil chemotaxis].
2. NADPH oxidase subunit: UniProt "Subunit of the phagocyte NADPH oxidase complex that mediates the
   transfer of electrons from cytosolic NADPH to O2 to produce the superoxide anion"
   [PMID:38355798]; Nox1 regulation [PMID:16636067].
3. Postsynaptic spine morphogenesis at glutamatergic synapses (UniProt, hippocampal neurons,
   ARHGEF6/7-dependent local activation).

## Review decisions
- 84 generic `GO:0005515` rows REMOVEd under the protein-binding policy; the informative binding
  terms (GTP-dependent protein binding, protein kinase binding, RhoGDI binding) were accepted.
- Pleiotropic organismal/tissue outputs (forebrain development, insulin secretion, ovarian follicle
  development, heart morphogenesis, neuron migration, cytokine regulation) kept as non-core.
- `GO:0046425 regulation of JAK-STAT` marked over-annotated.
- `GO:0035556 intracellular signal transduction` marked TOO_GENERAL beside Rac protein signal
  transduction.
