# EAF3 review notes

## Setup and literature search

Seeded with:

```bash
UV_FROZEN=1 just fetch-gene yeast EAF3
```

Automated deep research could not run in this environment. `just deep-research yeast
EAF3 --provider falcon` reported that `falcon` was unavailable; the only listed
provider was `claude_code`, and `just deep-research yeast EAF3 --provider
claude_code` failed because the Claude Code API key was invalid/not logged in.

I searched PubMed/web for `EAF3 Q12432`, `Saccharomyces EAF3 Rpd3S`, `Eaf3
TINTIN NuA4`, and `Rpd3S nucleosome Eaf3` to look for papers newer than the GOA
seed set. The useful additions were newer Rpd3S and NuA4/TINTIN mechanism papers:

- PMID:27535225, showing Eaf3/5/7 stimulates NuA4 binding to H3K36-methylated
  nucleosomes and RNA polymerase II.
- PMID:37666978, a 2023 cryo-EM analysis of Rpd3S-nucleosome engagement and DNA
  linker tightening.
- PMID:38065958, a 2023 cryo-EM structure of complete S. cerevisiae Rpd3S bound
  to nucleosome with two copies each of Rco1 and Eaf3.
- PMID:38598631, a 2024 structural analysis of apo and nucleosome-bound Rpd3S.
- PMID:39779918, a 2025 structural/mechanistic study of asymmetric Rco1-Eaf3
  dimers and Pol II CTD association.

## PTHR10880 / PAINT

Local PAINT cache:

- `interpro/panther/PTHR10880/PTHR10880-paint.tsv`
- `interpro/panther/PTHR10880/PTHR10880-entries.csv`

The yeast EAF3 protein Q12432 is in `PTHR10880:SF15`, the fungal/animal MRG15
subfamily named `MSL COMPLEX SUBUNIT 3` in PANTHER.

`PANTHER:PTN000853816` is a fungal IBD node for `GO:0032221 Rpd3S complex`,
seeded by yeast EAF3 and pombe alp13. This transfer is correct for budding yeast:
Eaf3 is a unique Rpd3S subunit in both 2005 discovery papers, and newer Rpd3S
cryo-EM structures place two copies of Eaf3 in the complete Rpd3S-nucleosome
complex.

`PANTHER:PTN000093963`, the eukaryotic MRG root node, carries three assertions
that reach yeast:

- `GO:0035267 NuA4 histone acetyltransferase complex`: correct for yeast Eaf3.
- `GO:0006357 regulation of transcription by RNA polymerase II`: broad but
  correct for the NuA4/Rpd3S/TINTIN family role.
- `GO:1990841 promoter-specific chromatin binding`: overpropagated. The only
  PAINT seeds for this term are Arabidopsis MRG genes. Yeast Eaf3 is supported
  as an H3K36me reader for coding-region Rpd3S and Pol II-coupled TINTIN
  mechanisms, not as a promoter-specific chromatin-binding activity.

## Care points

- The 15 IntAct `GO:0005515 protein binding` rows are all generic MF
  overannotations. The underlying interactions with Esa1, Eaf5, and Sin3 support
  NuA4, TINTIN, and Rpd3S membership rather than a specific independent Eaf3
  binding activity.
- `GO:0043487 regulation of RNA stability` appears to be an rDNA-vs-RNA
  miscitation in the abstract-only cache: PMID:31694990 discusses ribosomal DNA
  repeat stability and extrachromosomal rDNA circles in eaf3 mutants. Because the
  row is an SGD IMP annotation and the full text is not cached, the review leaves
  it `UNDECIDED`.
- `GO:0006281 DNA repair` is also `UNDECIDED`: PMID:16135807 is a NuA4/H4
  phosphorylation/DNA repair paper but the cached abstract does not mention Eaf3.
