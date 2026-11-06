# ERG1 (YGR175C) notes

UniProt P32476; squalene epoxidase, EC 1.14.14.17; FAD (by similarity) [UniProt:P32476].

## Evidence journal
- Cloned from allylamine-resistant mutant; extract activity terbinafine-resistant [PMID:1743514 "The ERG tested in a cell-free extract from one of these transformants proved to be resistant to the Al derivative, terbinafine."].
- Microsomal enzyme needs NADPH, not added FAD [PMID:8358382 "S. cerevisiae squalene epoxidase required NADPH for enzyme reaction"].
- Dual ER/LD localisation; activity only in ER [PMID:9450962 "enzymatic activity of squalene epoxidase was only detectable in the endoplasmic reticulum but was absent from isolated lipid particles"].
- erg1 mutants lack the activity [PMID:200835 "These groupes lack the following enzymatic activities: squalene epoxidase (erg 1)"].
- Constitutive LD protein [PMID:24868093].

## Decisions
- All squalene monooxygenase rows ACCEPT; RCA cytosol -> MODIFY ER membrane (converter default); ARBA ergosterol metabolic -> MODIFY biosynthetic; membrane IEA -> ER membrane; triterpenoid BP and FAD binding KEEP_AS_NON_CORE.

## 2026-11-06 re-review

- `just deep-research-falcon yeast ERG1` failed because the Falcon provider is not available in this environment (`agentapi` missing; only `claude_code` listed). No provider-named deep-research file was created.
- A 2024 substrate-tunnel engineering paper on S. cerevisiae Erg1 further supports the existing squalene epoxidase/ergosterol-biosynthesis call but does not add a new GO function: "the catalytic activity of the squalene epoxidase from Saccharomyces cerevisiae was significantly improved by reshaping its substrate tunnel" [PMID:39454051].
