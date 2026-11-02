# mpkC notes

## 2026-11-02 review

- Started from `just fetch-gene ASPFU mpkC`, which fetched UniProt Q4WUN7,
  18 GOA rows, and the GOA-cited publications.
- `ASPFU/mpkB` was initially considered as the next PTHR24055 family member,
  but the Af293 UniProt gene-exact query failed and the PANTHER member table
  only identified the CEA10 mpkB protein. I switched to the Af293 mpkC review.
- Cached the other UniProt-cited MpkC papers:
  PMID:25459537, PMID:27706915, PMID:30538182, PMID:31134001, and
  PMID:32743127. PMID:16372009 is only the genome-sequencing paper and was not
  used for functional interpretation.
- `just deep-research-falcon ASPFU mpkC --fallback perplexity-lite` could not
  run in this environment because the external `agentapi` binary was not
  available. I therefore did a manual PubMed / web scan around `Aspergillus
  fumigatus mpkC` and `SakA MpkC`: the newer items were broad HOG/MAPK or
  fungal-pathogen reviews plus errata, not newer primary data that would change
  the core GO interpretation.

## Functional synthesis

MpkC is a HOG1-subfamily MAP kinase in the A. fumigatus Af293 proteome. Reyes
et al. first showed that deleting `mpkC` specifically impaired growth on
minimal medium with sorbitol or mannitol as sole carbon sources, whereas the
mutant remained broadly wild type on minimal or complete media and on high
osmolarity in the original single-mutant assays. That row supports the AspGD
`GO:0015976 carbon utilization` IMP because MpkC kinase signaling is upstream
of the polyalcohol-utilization response rather than merely a downstream
phenotype [PMID:16998074].

The later A. fumigatus literature folded MpkC into the HOG stress-MAPK module.
The single `mpkC` mutant is modest relative to `sakA`, but SakA and MpkC have
redundant or cooperative roles in conidial stress tolerance, osmotic and
oxidative stress, cell-wall damage, and transient osmotic-stress transcription
[PMID:25459537; PMID:26878695; PMID:27706915]. MpkC::GFP is cytoplasmic and
translocates to the nucleus under osmotic and cell-wall stress, and later work
showed SakA::GFP physically associates with MpkC:3xHA under osmotic and
cell-wall stresses [PMID:26878695; PMID:27538790; PMID:31134001].

The HOG/stress IBAs are consistent with the IBA project: `PANTHER:PTN001172058`
is a fungal HOG/Sty1 stress-MAPK node seeded by fungal descendants, not a
pairwise similarity vote. The broad `PANTHER:PTN000622075` kinase and
compartment rows are likewise biologically defensible for MpkC, although the
Ser/Thr kinase row is less specific than `GO:0004707 MAP kinase activity`.

Several phenotypes should not be added as new GO process rows. The virulence,
biofilm-adhesion, paradoxical-growth, and PKA-dependent carbohydrate
mobilization observations are informative pathway outputs, but they do not by
themselves identify MpkC as a direct participant in a distinct GO process beyond
its stress-activated MAPK signaling role [PMID:26878695; PMID:30538182;
PMID:32743127].
