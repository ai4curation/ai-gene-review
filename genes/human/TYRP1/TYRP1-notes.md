# TYRP1 notes

Deep research providers unavailable in this environment (falcon/perplexity-lite failed); research done
from cached publications, PubMed and the UniProt record.

## Activity
- Crystal structure: binuclear **zinc** site, not copper [PMID:28661582 "We show that the active site contains
  two zinc ions, rather than copper ions as in tyrosinases, which makes it unlikely that human TYRP1 is a redox
  enzyme"]; purified lumenal domain lacks DHICA, tyrosine hydroxylase and L-DOPA oxidase activity, but activity
  appears after copper substitution [PMID:28661582 "exchanging the Zn2+/Cu2+ cofactors of TYRP1/TYR for Cu2+/Zn2+
  conferred"]. Hence tyrosinase activity rows REMOVEd; DHICA/catechol oxidase kept as non-core (disputed).
- The IDA "tyrosinase activity" row (PMID:21291857) comes from lysate tyrosinase assays in GIPC/APPL knockdown
  melanocytes, which report TYR protein levels, not a TYRP1 activity.
- Loss of function causes OCA3 [PMID:21996312].

## Trafficking and localization (surface benchmark)
- Melanosome membrane, single-pass type I, lumenal catalytic-like domain.
- Sorting: C-terminal Ser-Val-Val PDZ motif binds GIPC [PMID:11441007]; AP-1/KIF13A endosomal route [PMID:19841138].
- **Minor cell-surface pool in melanoma cells**: detected by flow cytometry with anti-TYRP1 antibodies
  [PMID:18334748 "native TYRP1 in melanoma cells as determined by flow cytometry analysis"] and used for CAR-T
  targeting [PMID:39308793]. Added as a NEW `GO:0009986 cell surface` annotation (non-core).
- Conclusion: primarily melanosome membrane (lumenal domain inside the organelle); a minor plasma-membrane pool
  presents the same domain extracellularly in melanoma.
