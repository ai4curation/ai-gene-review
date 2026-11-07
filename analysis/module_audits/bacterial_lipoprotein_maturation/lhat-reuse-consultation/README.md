# Exact approved LhaT review reuse

The reused target is BACSU/ypjA (LhaT), UniProt P54392, Bacillus subtilis168. Its review and notes are byte-identical to approved Ac-HepG PR6167, including the published commit bcfeede8a640e614c3bb569994192ea415aa4252 and approval commit recorded in reuse-provenance.yaml. The review blob is 19613a197820f0f0b19e5ee30ced859984f9f488 at both commits.

Normal `just fetch-gene BACSU ypjA` ran first in this worktree. Fresh UniProt and GOA were byte-identical to the approved source files and were left in place; no source overwrite or refresh occurred. PMID40626731 was already present and byte-identical. The review's complete evidence closure is its own UniProt record and that publication, plus a standard GO_REF vocabulary-mapping record. There are no module/family/source-analysis imports required for its quoted evidence. Historical notes refer to the prior project's research receipts: those remain provenance at the source commit, not new dependencies on the entire prior module. The genuine prior Falcon authentication failure was copied only into ignored audit cache with its hash recorded; no new provider report was generated.

One original localization payload remains in the same position with ACCEPT. The single historical NEW GO0008080 row remains active, with exactly its approved evidence and reasoning. There are zero newly authored annotations, deletions or retirements. Core GO0008080 and its N-terminal acetylation context remain unchanged.

## Independent primary boundary check

The full cached PMID40626731 Results was reread. Recombinant B.subtilis YpjA was supplied in E.coli membranes, while the coupled lipid-donor preparation used a C20 geranylgeranyl analogue and mixed acetylated carrier species. The +42Da lipopeptide product supports N-acetylation. This does not establish purified-LhaT kinetics, native C35 preference, donor regioselectivity, an exact directly mapped topology or a flippase. Acetyl-CoA serves upstream carrier loading, not the assigned direct LhaT donor. The approved donor-agnostic GO0008080 remains appropriate.

The same primary reports no modification by wild-type B.anthracis LhaT in its assay. That target result prevents universal substrate-specific activity transfer from membership alone; it does not prove every unassayed family member inactive. No detailed construct engineering is needed for the reused functional conclusion.

## Verified classification

The unchanged official UniProt P54392 record carries:

- PANTHER PTHR40042:SF1, DUF1405 DOMAIN-CONTAINING PROTEIN.
- PANTHER PTHR40042, HYPOTHETICAL MEMBRANE SPANNING PROTEIN.
- InterPro IPR009845, DUF1405.
- Pfam PF07187, DUF1405.

These identify this member's classification, not universal LhaT activity or an inferred PAINT loss node. Family review remains root-owned and was not imported or edited.

Reproduce preservation using `uv run python analysis/module_audits/bacterial_lipoprotein_maturation/lhat-reuse-consultation/check_preservation.py`. It verifies approved blob-derived hashes, the fresh original payload, historical proposal lifecycle, prior provider receipt and57 initial protected module sources. Focused validation, history and render receipts are recorded separately. No full validation, commit or push was performed.
