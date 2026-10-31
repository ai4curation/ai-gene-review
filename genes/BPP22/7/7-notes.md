# Gene 7 (Q01074 / GP7_BPP22) - Internal virion protein gp7 / Ejection protein gp7

## Summary
- **UniProt ID**: `Q01074` (`GP7_BPP22`)
- **Gene symbol**: `7`
- **Length**: 229 AA (processed chain: residues 21-229, `gp7*`, after N-terminal propeptide 1-20 cleavage by host protease OpdA/PrlC)
- **Domains**: `IPR057916` / `PF25688` (`P22_gp7`)
- **Function**: Internal head ejection protein (`gp7` / `gp7*`) packaged at ~10-20 copies per procapsid via the scaffolding protein `gp8` [PMID:328927, PMID:26245366]. During procapsid maturation, the N-terminal 20 amino acids are proteolytically cleaved by host oligopeptidase A (`OpdA` / `PrlC`) to generate mature `gp7*` [PMID:1853558, PMID:1522065]. Upon virion attachment to host LPS and outer membrane protein OmpA and release of the `gp26` plug, `gp7*` is ejected prior to viral DNA [PMID:26245366] and assembles into the extracellular segment of the ~40 nm trans-envelope DNA-delivery channel that bridges the `gp10` tail hub to the host outer membrane [PMID:29590587, PMID:30886360, PMID:37952769]. Loss of `gp7` abolishes host `K+` release and viral DNA injection into the host cytoplasm without preventing ejection of `gp16` and `gp20` [PMID:328927, PMID:38236051].

## Key Literature Evidence
- **PMID:328927** (Israel 1977): Identified the four ejected ("E") proteins of P22 (`gp16`, `gp20`, `gp26`, `gp7`); showed that `7-` particles still eject `gp16` and `gp20`, whereas `16-` particles fail to eject `gp7`, and `7-` particles fail to deliver functional DNA.
- **PMID:1853558** (Eppler et al. 1991) and **PMID:1522065** (Conlin et al. 1992): Sequenced P22 gene `7` and demonstrated that 20 N-terminal residues are cleaved from `gp7` during phage development by *Salmonella* oligopeptidase A (`OpdA`), and that N-terminal mutations in `gp7` confer `opdA` independence.
- **PMID:26245366** (Jin et al. 2015): Demonstrated in vitro that in the presence of both LPS and OmpA, all three internal E proteins (`gp16`, `gp20`, `gp7`) are ejected prior to viral DNA release.
- **PMID:29590587** (tang/Parent et al. 2018): Cryo-EM reconstruction of post-ejection (`gp26-`) P22 virions revealed a hollow tube-like density extending from the distal tip of the `gp10` tail hub formed by remodeled ejection protein (`gp7`).
- **PMID:30886360** (Wang et al. 2019): Cryo-electron tomography of P22 infecting *Salmonella* mini-cells demonstrated that after `gp26` needle release, `gp7*` is ejected and assembles into an extracellular channel extending from the `gp10` baseplate to the host cell surface, continuous with the `gp20` periplasmic and `gp16` cytoplasmic-membrane channels (~40 nm trans-envelope conduit).
- **PMID:37952769** (Bravo et al. 2023): Cryo-EM localized reconstruction, genetic knockouts, and biochemical analyses characterized the organization of the P22 ejection proteins (`gp7`, `gp20`, `gp16`) and direct `gp7`-`gp20` interactions.
- **PMID:38236051** (Bhardwaj et al. 2024): Showed that all three E-proteins (`gp7`, `gp20`, `gp16`) are essential for host cytoplasmic membrane depolarization (`K+` release) and viral DNA injection.

## Existing GO Annotations Review
- `GO:0016020` (`membrane`, EXP, PMID:37952769, `located_in`) -> `MODIFY` to `GO:0033644` (`host cell membrane`), which is already annotated on `gp7` from the same reference.
- `GO:0033644` (`host cell membrane`, IDA, PMID:37952769, `located_in`) -> `ACCEPT`.
- `GO:0046718` (`symbiont entry into host cell`, IEA, GO_REF:0000043, `involved_in`) -> `MODIFY` to `GO:0099002` (`symbiont genome ejection through host cell envelope, short tail mechanism`).
- `GO:0099002` (`symbiont genome ejection through host cell envelope, short tail mechanism`, IDA, PMID:26245366 / IDA, PMID:29590587 / IMP, PMID:38236051) -> `ACCEPT`.
- Added `NEW` annotation: `GO:0005198` (`structural molecule activity`, IDA, PMID:30886360, `enables`), reflecting the assembly of ejected `gp7*` into the structural extracellular genome-delivery channel connecting the `gp10` tail hub to the host outer membrane.
