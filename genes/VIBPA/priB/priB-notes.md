# priB (Q87L73) - Replication restart protein PriB in *Vibrio parahaemolyticus*

## Gene Identity
- **UniProt**: Q87L73 (PRIB_VIBPA)
- **Gene**: priB (VP2739)
- **Organism**: *Vibrio parahaemolyticus* serotype O3:K6 (strain RIMD 2210633)
- **Taxon**: NCBITaxon:223926
- **Protein**: 100 AA, ~11 kDa
- **Family**: PriB family
- **Domains**: OB-fold (SSB-like), IPR000424 (Primosome_PriB/ssb), IPR023646 (Prisomal_replication_PriB)

## Summary of Function

PriB is a small homodimeric single-stranded DNA-binding protein that functions as an accessory factor in the PriA-dependent replication restart pathway. Its core role is to stabilize the PriA helicase at stalled or abandoned replication forks, facilitating recruitment of DnaT and subsequent reloading of the replicative helicase DnaB [PMID:15350383, PMID:16935876].

No direct experimental characterization exists for the *V. parahaemolyticus* PriB; all functional inference is from homology to well-characterized *E. coli* PriB and HAMAP rule MF_00720.

## Key Molecular Function

- **ssDNA binding**: PriB binds ssDNA via its OB-fold. Binding is cooperative and salt-sensitive [PMID:16935876 "PriB–ssDNA binding can be cooperative and salt-sensitive"]. Key residues in *E. coli* include Phe42, Trp47, and Lys82 (L45 loop) [PMID:15350383 "WT Kd = 34.6 nM"]. PriB uses a binding mode distinct from tetrameric SSB despite structural similarity.

- **Scaffolding/adapter function**: PriB stabilizes PriA on DNA and facilitates DnaT recruitment. It is not an enzyme - it functions through protein-protein and protein-DNA interactions [PMID:16935876, PMID:28096444].

## Biological Process

- PriB functions specifically in **replication restart** - the reloading of replicative helicase at stalled/collapsed replication forks, NOT in general replication initiation from the origin [PMID:28096444 "Replication restart in bacteria"].
- Assembly order: PriA binds fork first -> PriB stabilizes PriA -> DnaT recruited -> helicase loading [PMID:37185258 "fork binding triggers large PriA conformational changes including an ~85 degree pivot"].

## Cellular Component

- **Primosome complex** (GO:1990077): PriB is a bona fide component of the replication restart primosome [PMID:28096444].
- PriB is cytoplasmic/nucleoid-associated, functioning at chromosomal replication fork sites.

## Key Literature (from deep research)

1. Lopper et al. (2004) - Crystal structure of *E. coli* PriB OB-fold dimer, ssDNA binding Kd values [PMID:15350383]
2. Huang et al. (2006) - PriB-ssDNA complex structure, cooperative binding mode [PMID:16935876]
3. Michel & Sandler (2017) - Review of replication restart pathways, PriA/PriB/DnaT assembly [PMID:28096444]
4. Duckworth et al. (2023) - Cryo-EM of PriA/PriB/fork complex, switch mechanism for PriB recruitment [PMID:37185258]
5. Tominaga et al. (2024) - Vibrionaceae comparative genomics: priB frequently lost when viral helicase loaders acquired [PMID:38557186]
6. Bonde et al. (2024) - SSB interactome review, PriB interactions with SSB via L45 loop residues [PMID:38527903]
7. Makino et al. (2003) - *V. parahaemolyticus* genome sequence (source of VP2739/priB) [PMID:12620739]

## Annotation Considerations

- GO:0006260 (DNA replication) is overly broad for PriB - it specifically functions in replication restart, not general replication
- GO:0030894 (replisome) is likely incorrect for PriB - it is a component of the primosome, not the replisome proper. These are distinct complexes.
- GO:0006269 (DNA replication, synthesis of primer) listed in UniProt via KW mapping - this is also not quite right; PriB doesn't synthesize primers, it facilitates primosome assembly
- GO:1990077 (primosome complex) is the correct CC term
- GO:0003697 (ssDNA binding) is the correct core MF term

## Vibrionaceae Context

In Vibrionaceae comparative genomics, priB is frequently absent in genomes that have acquired virus-derived helicase loader genes (vdhL1/vdhL2), with strong statistical association (q-value < 10^-15). PriB is essential in *V. cholerae* C6706 (transposon-insertion sequencing evidence). The presence of priB in *V. parahaemolyticus* RIMD 2210633 suggests this strain uses the canonical PriA-PriB replication restart pathway [PMID:38557186].
