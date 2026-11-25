# SLC41A2 (Q96JW4) — curation notes

Batch 28 (SLC41/MgtE family, PANTHER PTHR16228). De-novo review of 54 GOA rows.
No deep-research provider file; notes synthesized from the curated UniProt record and the
GOA-cited primary literature.

## Core function
- **Plasma-membrane magnesium transporter.**
  [file:human/SLC41A2/SLC41A2-uniprot.txt "Acts as a plasma-membrane magnesium transporter"]
  (CC:FUNCTION, ECO:0000269|PubMed:16984228 — Goytain & Quamme 2006 heterologous characterization).
- Core MF GO:0015095 magnesium ion transmembrane transporter activity; core BP Mg2+ transport /
  Mg2+ TM transport (GO:0015693 IDA PMID:16984228; GO:1903830). Localizes to the plasma membrane
  (CC:SUBCELLULAR LOCATION "Cell membrane", ECO:0000269|PubMed:16984228).
- Not established as a Na+-coupled antiporter in human (unlike SLC41A1), so no antiporter MF
  term is asserted here.

## Divalent-cation breadth
- UniProt notes it "Can also mediate the transport of other divalent metal cations in an order of
  Ba(2+) > Ni(2+) > Co(2+) > Fe(2+) > Mn(2+)" — **By similarity** (ECO:0000250|UniProtKB:Q8BYR8,
  mouse ortholog), not human IDA. The GOA rows for nickel/cobalt/iron/manganese transport
  (`GO:0015675`, `GO:0006824`, `GO:0006826`, `GO:0006828`) are all IEA(ortholog)/ISS from that
  mouse record. These are in-vitro/by-similarity divalent permeation of unestablished physiological
  relevance; the physiological substrate is Mg2+. MARK_AS_OVER_ANNOTATED (measured/predicted
  activity is not automatically function; a Mg transporter conducting other divalents in
  overexpression is not evidence it transports them physiologically).

## Annotation-landscape calls
- 33× bare `GO:0005515` protein binding (IPI; 32 PMID:32296183 + 1 PMID:25416956): REMOVE per policy.
- Generic class terms (`GO:0022857`, `GO:0008324`, `GO:0006812`, `GO:0030001`) TOO_GENERAL once
  the Mg transporter activity / Mg transport is asserted.
- `GO:0015095` is IEA(ARBA)/TAS(Reactome) only (no IDA directly on the MF term), but the Mg
  transport is IDA (PMID:16984228) and the family assignment is firm, so the MF is ACCEPT as core;
  support cites the curated UniProt FUNCTION rather than the ARBA line.

## Family / propagation
- SLC41/MgtE family; PANTHER PTN001045280 seeds the IBA plasma-membrane location (WITH SLC41A1/A2/A3).
