# Curation Notes: Escherichia phage Mu `Mup24` (`Q9T1X0`, Uncharacterized protein gp24)

## Summary of Function
- **Product**: Uncharacterized late protein gp24 (`Mup24`, 64 aa, 7.3 kDa).
- **Genomic Context**: Encoded in the `Plys`-driven late operon between the spanin genes (`Mup23`/`Mup23.1`) and the releasin gene (`Mup25`), activated by the viral late transcription activator C.
- **Sequence Features**: Soluble polypeptide lacking predicted transmembrane domains or signal peptides; contains four potential metal-binding residues (`Cys36`, `Cys39`, `His58`, `Cys60`). Chamblee et al. (`PMID:35471081`) noted that `gp22`, `gp23/gp23.1`, and `gp25` constitute the core lysis machinery, leaving `gp24` uncharacterized.

## Annotation Review Decisions
- **KEEP_AS_NON_CORE**:
  - `GO:0030430` (`host cell cytoplasm`, IEA): Plausible localization for a soluble cytoplasmic phage protein, retained as non-core with `core_functions: []` because the molecular function and biological process of gp24 are unknown.
