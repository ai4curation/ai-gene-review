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


## 2026-11-06 — PR6125 evidence/action follow-up

9: direct structural interaction evidence and bounded chaperone inhibition. Original machine rows and source bytes were frozen before edits. Published PMID and raw-source evidence remain separate from native target-specific experiments. Core location changes, where made, retain cytoplasm when finer cytosol resolution was not independently supported. Physiological uncertainty is not treated as automatic disproof of a directly measured molecular activity.

The exact prior PR-authored IC row is archived at dafA-source-analysis/authored-proposal-evidence-code-history.yaml. The direct structural/SEC-MALS physical interaction supports IPI for the tagged construct containing the exact full HB8 sequence; HB27 database source mapping and tag limitations remain explicit. The complete primary ATPase-suppression clause is retained. GO:0042030 covers ATP-hydrolysis inhibition but not the full client-pocket blockade mechanism; the broader chaperone-inhibitor proposal neither denies ATPase suppression nor invents a direct isolated ATPase-inhibition assay.
