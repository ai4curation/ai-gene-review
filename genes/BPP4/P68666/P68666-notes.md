# Enterobacteria phage P4 `P68666` (Copy number control protein Cnr, `P68666`)

## Identity & Genomic Context
- **UniProt**: `P68666` (`Y106_BPP4`, historical annotation: `Uncharacterized 11.7 kDa protein`, 106 aa, ~11.7 kDa).
- **Locus**: `ORF106` (`cnr`), located immediately upstream of the `alpha` replication primase-helicase gene in the P4 replication operon ([PMID:3309336], [PMID:2183201], [PMID:11929357] / [PMID:11929537]).
- **Domains**: `IPR005528` / `PF03864` (Bacteriophage P4 Cnr / Peptidase S24/S26B-like winged-helix domain).

## Molecular Function & Biological Role
- First sequenced as a 106-codon open reading frame (`ORF106`) immediately upstream of the 777-codon `alpha` gene ([PMID:3309336], [PMID:2183201]), this protein was subsequently identified genetically and structurally as **Cnr** (copy number regulation), an essential negative regulator of P4 plasmid DNA replication that maintains plasmid copy number within a viable physiological window ([PMID:11929537]).
- Both Cnr and the C-terminal origin-binding domain of the P4 replication protein gpAlpha (`P4-OBD`) adopt winged-helix folds ([PMID:11929537]).
- Cnr directly interacts with `P4-OBD` of gpAlpha (forming a winged-helix heterodimer that competes with or modulates `P4-OBD` homodimerization) to regulate origin recognition (`ori` and `crr`) and control initiation of P4 DNA replication ([PMID:11929537]).

## Curation Summary
- `existing_annotations` in the GOA stub is empty.
- Added `NEW` annotations:
  - `GO:0006260` (`DNA replication`, `IMP`, [PMID:11929537]) for its direct role in regulating gpAlpha origin-binding activity and P4 DNA replication / plasmid copy number.
  - Populated `core_functions` with `directly_involved_in: GO:0006260` (`DNA replication`) supported by [PMID:11929537], leaving `molecular_function` unset because only the abstract of [PMID:11929537] is cached.
