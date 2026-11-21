# lev-8 notes

## 2026-11-21

- Fetched `worm/lev-8` with UniProt Q93329, cached the WormBase hand-written MOD description, and checked PAINT: `just paint-losses worm lev-8` reported no IRD or IKR loss on the LEV-8 lineage.
- `just fetch-gene-pmids worm lev-8` found no PMID-cited seeded rows because the current GOA set contains only IBA and IEA rows. The review therefore reuses cached L-AChR literature from `unc-29`, `lev-1`, `unc-38` and `unc-63`, and adds PMID:15773900 for the LEV-8/ACR-13 cloning paper.
- Deep research was attempted with `just deep-research-falcon worm lev-8 --fallback perplexity-lite`, but both providers were unavailable in this environment. The review instead used cached primary papers, the WormBase MOD description, UniProt, the PTHR18945 family review, the draft L-AChR module, and the existing L-AChR subunit reviews.
- LEV-8 is the fifth C. elegans levamisole-sensitive acetylcholine receptor pore subunit. Native UNC-29 purifications recovered peptides from UNC-29, UNC-38, UNC-63, LEV-8 and LEV-1, and functional Xenopus oocyte reconstitution needed all five pore subunits plus RIC-3, UNC-50 and UNC-74.
- Unlike UNC-38 and UNC-63, LEV-8 is L-AChR-specific among the two characterized five-subunit receptors: the ACR-2R neuronal receptor uses ACR-12 as its LEV-8-like alpha subunit, and loss of `lev-8` does not suppress `acr-2(n2420gf)` convulsions.
- The broad InterPro2GO activity and transport rows were refined in parallel with `unc-29`, `lev-1`, `unc-38` and `unc-63`; calcium ion transport was kept as a real but secondary property because Boulin et al. measured modest calcium permeability for the recombinant L-AChR.
- The exact five-subunit order and the drug-binding contribution of LEV-8 remain open.
