# MYCTU dnaK: manual annotation review

DnaK is an Hsp70 chaperone that couples ATP binding and hydrolysis to binding and release of nonnative protein clients. DnaJ cochaperones assist client handling and GrpE promotes nucleotide exchange, enabling repeated folding cycles. The mycobacterial protein also occurs at the bacterial surface, in capsule preparations and in extracellular vesicles; these locations do not establish macrophage adhesin activity.

## Identity and evidence scope

See [identity-and-assay-scope.md](dnaK-source-analysis/identity-and-assay-scope.md) via the sibling dnaK source analysis; canonical reference: `file:genes/MYCTU/dnaK/dnaK-source-analysis/identity-and-assay-scope.md`. Native and heterologous observations are distinguished in the row reasons.

## Research and decisions

The normal Falcon research provider was attempted once and failed with HTTP 403 authentication failure; no provider report was fabricated. Manual primary-source review supports the annotations below. Original seeded annotation payloads and raw UniProt/GOA files are frozen in the ignored baseline.

- Couples nucleotide cycling to folding and refolding of nonnative protein clients with its J-protein and GrpE partners.
  PMID:27872278: “ClpB alone could not restore luciferase activity, but DnaK and cofactors gave a time-dependent increase in luciferase reactivation that was enhanced when ClpB was added to the reaction.”

Action counts: {"ACCEPT": 9, "KEEP_AS_NON_CORE": 7, "MODIFY": 2, "UNDECIDED": 9}.

Accessible full PMC19470749 supports the existing NOT adhesion row, not a new positive adhesin claim. Fibronectin/activation distinctions in PMID17849409 remain UNDECIDED where full assay access was unavailable. Broad proteomics/expression claims are not removed for lack of target detail.
