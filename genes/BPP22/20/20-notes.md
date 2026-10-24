# Gene 20 (Q01076 / GP20_BPP22) - Internal virion protein gp20 / Ejection protein gp20

## Summary
- **UniProt ID**: `Q01076` (`GP20_BPP22`)
- **Gene symbol**: `20`
- **Length**: 471 AA (50.1 kDa)
- **Domains**: `IPR031619` / `PF16928` (`Inj_translocase`, Phage injection translocase)
- **Function**: Internal virion ejection protein (`gp20`) packaged at ~10-20 copies inside P22 procapsids via the scaffolding protein `gp8` [PMID:328927, PMID:26245366]. Upon virion attachment to host LPS and outer membrane protein OmpA and release of the `gp26` plug, `gp20` is ejected ahead of the viral DNA [PMID:26245366], interacts with `gp7*` [PMID:37952769] and `gp16` [PMID:38236051], and assembles into the outer-membrane-periplasmic channel spanning the host periplasm to connect the `gp7*` extracellular channel to the `gp16` cytoplasmic-membrane pore within the ~40 nm trans-envelope DNA-delivery apparatus [PMID:30886360]. `gp20` is essential for host `K+` release and viral DNA injection [PMID:38236051], must co-evolve and interact specifically with cognate `gp16` (as shown by failure of hybrid P22/Sf6 swaps unless both `gp20` and `gp16` are from the same phage), and is co-targeted with `gp16` by the prophage inner-membrane superinfection exclusion protein SieA (substitutions `T338I`, `T341I`, `A348T`, or `G350D` in `gp20` combined with `gp16` mutations confer SieA escape) [PMID:38236051].

## Key Literature Evidence
- **PMID:328927** (Israel 1977): Identified `gp20` as one of the four ejected ("E") proteins of P22; `20-` particles eject their remaining E proteins (`gp16`, `gp7`, `gp26`) but are non-infectious.
- **PMID:26245366** (Jin et al. 2015): Demonstrated that in the presence of both LPS and OmpA, `gp20` is ejected from the capsid prior to viral DNA release.
- **PMID:29590587** (Tang/Parent et al. 2018): Cryo-EM reconstruction of P22 virions after genome release.
- **PMID:30886360** (Wang et al. 2019): Cryo-ET of P22 infecting *Salmonella* mini-cells demonstrated that ejected `gp20` assembles into the outer-membrane-periplasmic channel segment linking the extracellular `gp7*` channel to the cytoplasmic-membrane `gp16` channel.
- **PMID:37952769** (Bravo et al. 2023): Cryo-EM localized reconstruction, genetic knockouts, and biochemical analyses characterized the potential location of `gp20` inside the mature virion and its direct interaction with `gp7`.
- **PMID:38236051** (Bhardwaj et al. 2024): Demonstrated that `gp20` is required for `K+` efflux and DNA injection, interacts specifically with `gp16` during DNA delivery, and is inhibited together with `gp16` by prophage SieA.

## Existing GO Annotations Review
- `GO:0046718` (`symbiont entry into host cell`, IEA, GO_REF:0000043, `involved_in`) -> `MODIFY` to `GO:0099002` (`symbiont genome ejection through host cell envelope, short tail mechanism`).
- `GO:0098015` (`virus tail`, IEA, PMID:37952769, `located_in`) -> `ACCEPT` (note: per schema dynamic enum rules, `GO:0098015` is not placed in `core_functions.locations` or `in_complex`).
- `GO:0099002` (`symbiont genome ejection through host cell envelope, short tail mechanism`, IDA, PMID:26245366 / IDA, PMID:29590587 / IMP, PMID:38236051) -> `ACCEPT`.
- Added `NEW` annotation: `GO:0005198` (`structural molecule activity`, IDA, PMID:30886360, `enables`), reflecting assembly of ejected `gp20` into the structural outer-membrane-periplasmic channel of the ~40 nm trans-envelope genome delivery conduit.
