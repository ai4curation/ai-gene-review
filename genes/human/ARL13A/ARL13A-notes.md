# ARL13A notes

- ARL13A is the vertebrate paralog of ARL13B (PANTHER PTHR46090: ARL13A is SF1, ARL13B is SF3).
- **The affinage record is entirely about C. elegans ARL-13 / mammalian ARL13B**, the paralog; none of it is used.
- ARL13A-specific evidence:
  - Zebrafish Arl13a-mCherry localizes to about half of embryonic cilia and to microtubules; its expression diverges from arl13b; "arl13a and arl13b have evolved different roles" [PMID:30009987].
  - It lacks the catalytic glutamine [PMID:38606629].
  - The cheetah pseudogenization (premature stop codon) study lists ARL13A [PMID:39821281].
- **GOA calls:**
  - Ciliary location IBA/IEA rows → KEEP_AS_NON_CORE (supported by zebrafish).
  - Process IBAs (non-motile cilium assembly, receptor localization to non-motile cilium) → UNDECIDED (paralog transfer, untested), with propagation root cause UNRESOLVED.
  - GTP binding → ACCEPT; GTPase activity → UNDECIDED.
- WHOLLY_DARK gap.
- Review round (PR #4174):
  - Motile cilium (IBA) → MODIFY to GO:0005929 cilium (TERM_SCOPING_PROBLEM): nothing shows motility.
  - Ciliary membrane (IBA) → UNDECIDED: membrane association untested.
  - Non-motile cilium (IBA) and 9+0 cilium (IEA) → non-core, each with its own reasoning.
  - The gap boundary now says "not directly measured for ARL13A".
  - Overexpressed zebrafish Arl13a also marks spindle and midbody microtubules; noted in the description.
