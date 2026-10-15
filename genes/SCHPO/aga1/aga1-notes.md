# aga1 (SPBC1271.14, UniProt O94346) notes

## Identity
- ArgJ-family bifunctional protein, ortholog of S. cerevisiae ARG7 (PTHR23100:SF0, TIGR00120) [UniProt:O94346 "Belongs to the ArgJ family."]. UniProt has no gene name (ORFNames only); fetched with `-u O94346`.
- Precursor autoproteolytically split into alpha/beta chains (CHAIN 1..225, 226..445; ACT_SITE 226) [UniProt:O94346 "The alpha and beta chains are autoproteolytically processed from a"].

## Activity (inferred, not assayed in S. pombe)
- Ornithine acetyltransferase EC 2.3.1.35 [UniProt:O94346 "Reaction=N(2)-acetyl-L-ornithine + L-glutamate = N-acetyl-L-glutamate +"] and family-level EC 2.3.1.1 [UniProt:O94346 "Reaction=L-glutamate + acetyl-CoA = N-acetyl-L-glutamate + CoA + H(+);"]; both HAMAP-rule based.
- Anaplerotic NAGS in S. pombe is arg6 (module fungal_nags variant), so GO:0004042 kept as non-core (matches ARG7 review).

## Localisation / phenotype
- Mitochondrion in ORFeome screen (HDA PMID:16823372) [PMID:16823372 "we determined the localization of 4,431 proteins"].
- Arginine auxotrophy in the deletion-collection screen [PMID:32896087 "This screen identified 31 mutants that grew substantially better when supplemented with arginine"]; per-gene calls in Dataset EV1 (not cached) - deferred to curator.
- PomBase GO-CAM gomodel:6690711d00000916: aga1 enables GO:0004358 in mitochondrial matrix (ISS/TAS), downstream of arg1.

## Decisions
- Core: GO:0004358; BP GO:0006592 + GO:0006526; mitochondrial matrix. Consistent with ARG7 core.
- ARBA generic BPs MODIFY -> GO:0006526.
