# mof (O02193) review notes

## Identity
- MYST-family histone acetyltransferase, KAT8 ortholog; named for male-specific lethality
  ("males absent on the first"). [PMID:9155031 "mof, a putative acetyl transferase gene related to the Tip60 and MOZ human genes and to the SAS genes of yeast, is required for dosage compensation in Drosophila"]

## Catalytic activity
- H4K16-specific HAT. [PMID:10882077 "is a histone acetyltransferase that acetylates chromatin specifically at histone H4 lysine 16"]
- C2HC zinc finger needed for nucleosome binding and HAT activity. [PMID:11258702 "We found that this domain is essential for HAT activity, in addition to the established catalytic domain."]
- Chromobarrel domain binds nucleic acids and potentiates activity. [PMID:22421046 "the MOF chromobarrel domain is essential for H4K16 acetylation throughout the Drosophila genome"]

## Complexes
- MSL dosage compensation complex with MSL1/2/3, MLE and roX RNAs; MOF binds roX2 via its chromodomain. [PMID:11014199 "MOF specifically binds through its chromodomain to roX2 RNA in vivo."]
- NSL complex at housekeeping promoters, both sexes. [PMID:20620954 "the nonspecific lethal (NSL) complex (NSL1, NSL2, NSL3, MCRS2, MBD-R2, and WDS) that associates with the histone acetyltransferase MOF in both Drosophila and mammals"]
- Partitioning between the two. [PMID:20620953 "MOF distributes dynamically between two complexes, the dosage compensation complex and a complex containing MBD-R2, a global facilitator of transcription."]
- Ubiquitylated by MSL2. [PMID:28510597 "We found earlier that MSL2 is an E3 ligase that ubiquitylates most MSL proteins, including MOF"]

## Processes
- Dosage compensation (core). Genome-wide binding: [PMID:18510926 "MOF is not only involved in the onset of dosage compensation, but also acts as a regulator of gene expression in the Drosophila genome."]
- Maternal H4K16ac primes ZGA. [PMID:32502394 "maternal H4K16ac provides an instructive function to the offspring, priming future gene activation."]
- Ionizing-radiation response (secondary). [PMID:22072291 "Drosophila mof mutations in males and females, as well as mof knockdown in SL-2 cells, reduce post-irradiation survival"]

## Curation decisions
- GO:0004402 / GO:0061733 rows MODIFY -> GO:0046972 (already annotated).
- NuA4 IBA (Tip60-clade donors) REMOVE; MOF is in MSL/NSL, not NuA4.
- GO:0016456 and GO:0072487 are siblings in GO, both ACCEPT (shared MSL complex convention across msl-1/2/3, mle, mof).
- Chromosome / nuclear chromosome ACCEPT for MOF only, because MOF binds X and autosomes; nucleus ACCEPT (aligned with the other MSL subunits after review of msl-2: free nuclear MSL pool, PMID:21551218).
- Protein binding IPI rows REMOVE.

## Deep research (falcon, added after initial review)
- `mof-deep-research-falcon.md` agrees with the review: H4K16 is the dominant physiological substrate; MOF acts in both MSL and NSL complexes ["MOF performs this reaction in two distinct chromatin-regulatory assemblies, MSL and NSL."]. It notes in-vitro secondary acetylation of other H4 lysines (2024 dissertation) that is not established in vivo, and a 2024 Genetics study questioning H3K36me3 as a general MSL-spreading signal (relevant to msl-3). No annotation decisions changed.

## PR 4481 review fixes
- Softened the GO:0016456/GO:0072487 relationship claim (neither is an ancestor of the other per QuickGO ancestor lists) and used GO:0072487 MSL complex consistently as in_complex in core functions.
