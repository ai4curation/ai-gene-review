# SLC41A1 (Q8IVJ1) — curation notes

Batch 28 (SLC41/MgtE family, PANTHER PTHR16228). De-novo review of 68 GOA rows.
No deep-research provider file; notes synthesized from the curated UniProt record
(experimental ECO:0000269 statements) and the GOA-cited primary literature.

## Core function
- **Na+/Mg2+ exchanger; predominant cellular Mg2+ efflux system at the plasma membrane.**
  [file:human/SLC41A1/SLC41A1-uniprot.txt "Na(+)/Mg(2+) ion exchanger that acts as a predominant Mg(2+)"]
  (CC:FUNCTION, ECO:0000269|PubMed:18367447, 22031603, 23661805, 23976986).
- Transport is driven by the inward Na+ electrochemical gradient set by the Na+/K+ pump
  [file:human/SLC41A1/SLC41A1-uniprot.txt "the inwardly directed electrochemical gradient for Na(+) ions"].
  So the physiological direction is Mg2+ extrusion coupled to Na+ entry (antiport).
- Magnesium:sodium antiporter activity (GO:0061768) is IMP-supported on the gene by three
  independent studies (PMID:22031603, 23661805, 23976986); Mg2+ transport / Mg2+ TM transport
  (GO:0015693 / GO:1903830) and the MF GO:0015095 are IDA (PMID:18367447).
- Sets intracellular Mg2+ homeostasis (GO:0010961, IMP PMID:22031603 knockdown).
- Generates circadian cellular Mg2+ fluxes feeding back on clock-controlled metabolism
  (UniProt CC:FUNCTION cites PubMed:27074515; not separately annotated in GOA).

## Localization
- Plasma membrane (CC:SUBCELLULAR LOCATION "Cell membrane", ECO:0000269|PubMed:18367447, 23976986);
  basolateral in polarized epithelia (CC "Basolateral cell membrane", ECO:0000269|PubMed:23661805).

## Annotation-landscape calls
- 31× bare `GO:0005515` protein binding (IPI, PMID:32296183, one high-throughput interactome):
  REMOVE per the protein-binding policy (uninformative).
- Generic transporter/cation/metal class terms (`GO:0022857`, `GO:0008324`, `GO:0006812`,
  `GO:0030001`) are TOO_GENERAL once the specific Mg transporter activity / Mg transport is
  asserted; they name a class, not the substrate.
- `GO:0035725` sodium ion TM transport (IEA from the antiporter activity) = the Na counter-ion
  flux; real but non-core (the physiological output is Mg2+ efflux). KEEP_AS_NON_CORE.
- `GO:0071286` cellular response to magnesium ion (IEA/IGI PMID:21696366/ISS): SLC41A1 is itself
  Mg-regulated; a real but non-core regulatory response.
- `GO:0032991` protein-containing complex (part_of, IDA PMID:18367447): vague complex membership;
  KEEP_AS_NON_CORE.
- `GO:0016323` basolateral plasma membrane (IDA PMID:23661805): a polarized-cell-specific
  localization; KEEP_AS_NON_CORE relative to the general PM.

## Family / propagation
- SLC41/MgtE family; PANTHER PTN001045280 seeds the IBA plasma-membrane location (WITH SLC41A1
  Q8IVJ1 / SLC41A2 Q96JW4 / SLC41A3 Q96GZ6). Location IBA is sound.
