# 9 (P40820) Curation Notes — Escherichia phage P1

## Identity & Sequence Redundancy with `pacA` (`P28813`)
- **UniProt ID**: `P40820` (`9`, 142 aa fragment, `NON_TER 142`).
- **Critical finding**: Sequence alignment between `P40820` (`9`, 142 aa) and `P28813` (`pacA`, 397 aa) shows that `P40820` is the N-terminal 142-residue fragment of `PacA` (`141/142` identical residues; only residue 88 differs: `Q88` in `P40820` vs `E88` in `P28813`):
  - `P40820` (`1..142`): `MTWDDHKKNF ARDLANRIYN LSRRRVNGGT SGYAGLLAYC TAARQGYDVE AITARAAKLG VDPQLLKAIK VKPAAKSRDR AVAARRAQKA LAAYITKSVS LKEAWDFLGV DTRKSLRLLG RFLQSRILAD DDGERFEF`
  - `P28813` (`1..142`): `MTWDDHKKNF ARDLANRIYN LSRRRVNGGT SGYAGLLAYC TAARQGYDVE AITARAAKLG VDPQLLKAIK VKPAAKSRDR AVAARRAEKA LAAYITKSVS LKEAWDFLGV DTRKSLRLLG RFLQSRILAD DDGERFEF...`
- **Historical origin**:
  - In 1991, Lehnherr et al. (`PMID:1917870`, EMBL `X59560`) sequenced `gene 10` (`lpa`, encoding the late promoter activator gp10) and included the immediately downstream 5' end of classical P1 `gene 9` (codons 1–142), which lay just downstream of `lpa`.
  - In 1992, Skorupski et al. (`PMID:1538406`, EMBL `M82881`) sequenced the complete `pacA` and `pacB` genes and proved by marker rescue and sequencing of amber mutants (`am9.16`, `am31`, `am131`) that classical `gene 9` is `pacA` (397 aa, 44.8 kDa small terminase subunit).
  - UniProt created `P28813` (`PACA_BPP1`) from Skorupski et al. (`PMID:1538406`) and Łobocka et al. (`PMID:15489417`), but also retained `P40820` (`VP9_BPP1`) from the partial ORF in Lehnherr et al. (`PMID:1917870`) with the outdated comment `"Involved in the cutting of the viral packaging site (pac)"`.

## Curation Decisions
- `P40820` has no existing GOA annotations (`existing_annotations: []`).
- Because `P40820` represents the N-terminal 142-aa fragment of `pacA` (`P28813`, classical P1 `gene 9`), its biological identity is the small terminase subunit (`PacA` / `gp9`), which binds the methylated `pac` site (`GO:0003677` `DNA binding`) to initiate viral DNA genome packaging (`GO:0019073` `viral DNA genome packaging`) [PMID:1538406, PMID:15489417].
