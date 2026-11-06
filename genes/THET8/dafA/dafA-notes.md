# THET8 dafA: manual annotation review

DafA is a small regulatory assembly protein of the Thermus DnaK-DnaJ2 chaperone system. It forms an inhibited complex by occupying the DnaK client-binding pocket and contacting the J domain in a way that prevents productive docking. The structurally characterized complex contains two copies each of DnaK, DnaJ2 and DafA. DafA regulates access to the folding machinery rather than supplying ATPase or nucleotide-exchange activity.

## Identity and evidence scope

See [identity-and-assay-scope.md](../dnaK/dnaK-source-analysis/identity-and-assay-scope.md) via the sibling dnaK source analysis; canonical reference: `file:genes/THET8/dnaK/dnaK-source-analysis/identity-and-assay-scope.md`. Native and heterologous observations are distinguished in the row reasons.

## Research and decisions

The normal Falcon research provider was attempted once and failed with HTTP 403 authentication failure; no provider report was fabricated. Manual primary-source review supports the annotations below. Original seeded annotation payloads and raw UniProt/GOA files are frozen in the ignored baseline.

- Inhibits productive DnaK-DnaJ2 client processing by occupying the client pocket and blocking J-domain docking.
  PMID:41092901: “DafA inhibits the Hsp70-Hsp40 machinery through two distinct mechanisms: it blocks access of protein clients to Hsp70 and it prevents the docking of the J domain onto Hsp70”
  PMID:41092901: “We have used SEC-MALS to show that the complex has a molecular mass of 210 kDa consisting of a 2:2:2 stoichiometry.”

Action counts: {"NEW": 1}.

Current evidence supports an inhibited 2:2:2 assembly. The older 3:3:3 inference is not silently combined with the new structural state. DafA is optional regulation of the productive cycle.
