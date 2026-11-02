# S. pombe erg2 Notes

## 2026-10-11

`just fetch-gene SCHPO erg2` seeded eight GOA rows for the reviewed UniProt
entry `P87113`: three PAINT/IBA rows, a duplicate Rhea C-8 sterol isomerase
IEA, an HDA endoplasmic-reticulum localization row from PomBase, a UniProt
ER-membrane IEA, a direct PomBase ergosterol-biosynthesis IMP row, and a
UniPathway sterol-biosynthesis IEA.

Automated deep research was not available in this environment:

```text
just deep-research-falcon SCHPO erg2 --fallback perplexity-lite
```

failed because neither `agentapi` nor provider API keys were configured. I
therefore did a manual literature and PAINT pass.

### PAINT

`interpro/panther/PTHR10868/PTHR10868-paint.tsv` has one fungal ERG2 ancestor,
`PTN001280219`, carrying `GO:0000247 C-8 sterol isomerase activity` and
`GO:0006696 ergosterol biosynthetic process`. The source list includes CGD and
SGD ERG2 entries for the activity row and PomBase plus SGD ERG2 entries for the
ergosterol-biosynthesis row, so the fission-yeast rows come from the fungal
sterol-isomerase node, not from animal Sigma-receptor descendants.

The ER row comes from the broader `PTN001328958` eukaryotic ERG2/SIGMAR1-family
node seeded by fungal ERG2 and animal SIGMAR1 entries. That node is appropriate
for the shared ER compartment. The animal signaling, postsynaptic, and
neuron-apoptosis rows in PTHR10868 sit on `PTN001593709` and `PTN008312250` and
do not propagate to `P87113`.

### Cached Publications

- PMID:18310029 is abstract-only locally. The abstract names Erg2p as the
  predicted C-8 sterol isomerase in the zymosterol-to-ergosterol series and
  reports that the tested late ergosterol-gene disruption mutants could not
  synthesize ergosterol. I retained the direct PomBase ergosterol-biosynthesis
  IMP row and used UniProt/Rhea plus PAINT for the exact molecular activity.
- PMID:16823372 is abstract-only locally. The abstract reports the
  proteome-scale S. pombe YFP localization assay but not the Erg2 image-table
  row. I retained the HDA row because PomBase and UniProt both use this paper
  for Erg2 ER/ER-membrane localization.
- PMID:21832151 is full text locally. The 2011 meiosis/endocytosis study uses
  erg2 deletion as a sterol-perturbation background and reports that erg2
  mutants have severe sporulation defects, but this supports no direct Erg2
  role beyond supplying normal ergosterol.
- PMID:37787768 is full text locally. The 2023 fission-yeast phenomics study
  includes erg2 deletion in a genome-scale stress- and drug-phenotype matrix,
  providing downstream phenotype context rather than a new direct Erg2
  activity or pathway annotation.
- PMID:36799444, a 2023 Lem2/Bqt4 interactome paper, was found in a web search
  for newer Erg2/SPAC20G8.07c literature and cached. Its abstract does not name
  Erg2 directly, and the reported inner-nuclear-membrane/lipid-enzyme
  interactions do not support any new Erg2 annotation.
- PMID:40424131 is full text locally. The 2025 pentadecanoic-acid lipotoxicity
  study reports that some ergosterol-biosynthesis mutants, including erg2, resist
  C15:0-induced giant ER sheet formation. This is a downstream lipid-composition
  phenotype, not a separate process executed by Erg2.

### Curation Decisions

The review has one core function: C-8 sterol isomerase activity at the ER
membrane, directly involved in ergosterol biosynthesis. The fungal
`PTN001280219` activity and pathway IBAs were accepted with `NO_FAILURE_CORE`
propagation reviews, as was the broader eukaryotic `PTN001328958`
ER-localization IBA. The Rhea C-8 sterol isomerase row, direct PomBase
ergosterol-biosynthesis row, PomBase HDA ER row, UniProt ER-membrane row, and
UniPathway sterol-biosynthesis row were all accepted.

The cached GO-CAM `gocams/66c7d41500002088` already models
`PomBase:SPAC20G8.07c` as a `GO:0000247` C-8 sterol isomerase activity that
occurs in the ER and is part of `GO:0006696` ergosterol biosynthetic process,
matching this gene review's sole core function.

No new GO rows are proposed. Drug tolerance, plasma-membrane protein
localization defects, and pentadecanoic-acid resistance are consequences of
altered sterol composition in erg2 mutant cells.

## 2026-10-14 (YeastPathways isoprenoid/ergosterol/ubiquinone module pass, #4545)

- Fetched accession verified P87113 (ERG2_SCHPO). C-8 sterol isomerase, ERG2 family (PTHR10868, sigma-1 receptor-related) [UniProt:P87113 "Belongs to the ERG2 family."].
- Reaction: [UniProt:P87113 "Reaction=fecosterol = episterol; Xref=Rhea:RHEA:33435,"].
- Deletion abolishes ergosterol [PMID:18310029 "Disruption mutants of these genes were unable to synthesize ergosterol"]; UniProt: multiple septa in some cells, cycloheximide/staurosporine sensitivity.
- ER membrane (single-pass) from ORFeome [PMID:16823372].
- Budding-yeast ERG2 review core: GO:0000247, ER membrane. Consistent.
- GO-CAM 66c7d41500002088: erg2 GO:0000247 in ER, -> erg31/erg32. Agrees (whereas SGD YeastPathways models type ERG2 only with GO:0003674).
- All 8 annotations accepted.
