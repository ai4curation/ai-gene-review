# Gene 16 (Q01146 / GP16_BPP22) - Internal virion protein gp16 / Ejection protein gp16

## Summary
- **UniProt ID**: `Q01146` (`GP16_BPP22`)
- **Gene symbol**: `16`
- **Length**: 609 AA (64.4 kDa)
- **Domains**: `IPR059961` / `PF26808` (`Phage_P22_gp16`)
- **Function**: Largest of the three internal virion ejection proteins (`gp16`, `gp20`, `gp7`) packaged at ~10-20 copies inside P22 procapsids via the scaffolding protein `gp8` [PMID:328927, PMID:1585633, PMID:26245366]. Required in the virion for ejection of `gp7` [PMID:328927]. Upon virion recognition of host LPS and outer membrane protein OmpA and displacement of the `gp26` plug, `gp16` is ejected prior to viral DNA [PMID:26245366], partitions into the host cytoplasmic (inner) membrane to form the inner-membrane conduit of the ~40 nm trans-envelope DNA-delivery channel [PMID:30886360], and triggers inner membrane depolarization (`K+` efflux) required for DNA translocation into the cytoplasm [PMID:38236051]. `gp16` (together with `gp20`) is directly targeted by the prophage P22 inner-membrane superinfection exclusion protein SieA; C-terminal substitutions in `gp16` (`G532W`, `P546S`) combined with `gp20` substitutions confer escape from SieA-mediated exclusion [PMID:38236051].

## Key Literature Evidence
- **PMID:328927** (Israel 1977): Showed that `gp16` is one of four ejected ("E") proteins (`gp16`, `gp20`, `gp26`, `gp7`); `16-` particles fail to eject `gp7` and are non-infectious, though `gp16` function can be supplied in *trans* by co-infecting helper phage.
- **PMID:1585633** (Umlauf & Dreiseikelmann 1992): Cloned, sequenced, and overexpressed P22 gene `16` (609 AA, 64,366 Da); purified `gp16` showed no sequence-specific or end-protective DNA-binding activity in vitro.
- **PMID:26245366** (Jin et al. 2015): Demonstrated that `gp16`, `gp20`, and `gp7` are all ejected ahead of viral DNA when triggered by both LPS and OmpA in vitro.
- **PMID:29590587** (Tang/Parent et al. 2018): Cryo-EM analysis of post-ejection (`gp26-`) P22 virions.
- **PMID:30886360** (Wang et al. 2019): Cryo-ET of P22 infecting *Salmonella* mini-cells demonstrated that ejected `gp16` assembles into the cytoplasmic-membrane channel segment of the continuous ~40 nm trans-envelope genome delivery conduit.
- **PMID:37952769** (Bravo et al. 2023): Cryo-EM localized reconstruction and knockout analysis of P22 ejection proteins (`gp7`, `gp20`, `gp16`).
- **PMID:38236051** (Bhardwaj et al. 2024): Showed that `gp16` is required for `K+` release and DNA injection, must functionally interact with cognate P22 `gp20` during DNA delivery, and is inhibited by the inner-membrane superinfection exclusion protein SieA (overcome by `gp16` `G532W` or `P546S` combined with `gp20` mutations).

## Existing GO Annotations Review
- `GO:0046718` (`symbiont entry into host cell`, IEA, GO_REF:0000043, `involved_in`) -> `MODIFY` to `GO:0099002` (`symbiont genome ejection through host cell envelope, short tail mechanism`).
- `GO:0099002` (`symbiont genome ejection through host cell envelope, short tail mechanism`, IDA, PMID:26245366 / IDA, PMID:29590587 / IEA, GO_REF:0000043 / IMP, PMID:38236051) -> `ACCEPT`.
- Added `NEW` annotations:
  - `GO:0005198` (`structural molecule activity`, IDA, PMID:30886360, `enables`) for forming the structural cytoplasmic-membrane channel segment of the ~40 nm trans-envelope DNA-delivery apparatus.
  - `GO:0033644` (`host cell membrane`, IDA, PMID:30886360, `located_in`) for partitioning into the host cytoplasmic membrane during infection.
