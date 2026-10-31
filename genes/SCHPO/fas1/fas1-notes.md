# fas1 (SPAC926.09c, UniProt Q9UUG0) notes

Fetch: `just fetch-gene SCHPO fas1` fetched the correct accession (FAS1_SCHPO, Q9UUG0, 2073 aa).

## Subunit composition (checked against the naming-trap warning)
- S. pombe fas1 = FAS **beta** subunit, as in S. cerevisiae FAS1:
  [PMID:9693066 "We have cloned and sequenced the fission yeast (Schizosaccharomyces pombe) fas1+ gene, which encodes the fatty acid synthetase (FAS) beta subunit"],
  48.1% identity to budding-yeast beta. Alpha = fas2/lsd1 (Q10289). So the pombe/cerevisiae naming is congruent here.
- [PMID:9693066 "These results indicate that the FAS complex from S. pombe forms a heterododecameric alpha6beta6 structure"]; ~six FMN per complex.
- Domains [UniProt:Q9UUG0]: AT, MPT, DH (MaoC-like), ER; UniProt also names an "S-acyl fatty acid synthase thioesterase" (EC 3.1.2.14) - not a real chain-release thioesterase in fungal FAS.

## GO-CAM (gomodel:678073a900002931)
- fas1 enables GO:0019171, GO:0004318 (NADH!), GO:0004314, GO:0004313 in cytosol; complex node GO:0005835 enables GO:0004321.
- Oddity: an additional fas1 GO:0004313 activity (678073a900003740) is placed in the **mitochondrion** with no location evidence,
  causally upstream of the mitochondrial KS (SPBC887.13c). Probably a placeholder for the mitochondrial FAS II acetyl-loading step;
  fas1 has no evidence of mitochondrial function.
- GO-CAM uses the NADH enoyl-ACP reductase term; fungal FAS ER is FMN/NADPH-dependent (GO:0141148).

## Decisions (consistent with genes/yeast/FAS1)
- GO:0004312 rows -> MODIFY to GO:0004321; GO:0004318 rows -> MODIFY to GO:0141148 (yeast review REMOVED NADH rows; here MODIFY since the
  domain activity is right); GO:0016297 thioesterase IEA REMOVE.
- Core: contributes_to GO:0004321 in GO:0005835; partial MFs GO:0004314, GO:0004313, GO:0019171, GO:0141148; BP GO:0042759; cytosol.
