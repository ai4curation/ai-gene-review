# id1 (INDETERMINATE1) — manual literature synthesis

No deep-research provider was available for this session; this summary was assembled by
hand from cached publications (`publications/PMID_*.md`) and PubMed metadata. Every
assertion carries its source.

## Identity

- UniProt O65215 (TrEMBL, unreviewed), *Zea mays*, 436 aa, GeneID 541693,
  Gramene Zm00001eb047750. PE 2 (transcript level).
- Domain architecture: the plant-specific ID domain (IDD) with C2H2 (Z1), C2H2 (Z3),
  C2HC (Z2) and C2HC (Z4) zinc fingers (InterPro IPR031140 IDD1-16; Pfam PF22995,
  PF22992, PF22996, PF12874).
- Founding member of the IDD family [PMID:16784536 "The maize INDETERMINATE1 gene, ID1,
  is a key regulator of the transition to flowering and the founding member of a
  transcription factor gene family that encodes a protein with a distinct arrangement of
  zinc finger motifs."]
- Grass orthologs: rice OsId1/Ehd2/RID1 (UniProt B1B534) and a sorghum ortholog form a
  group separate from other IDD genes; no clear Arabidopsis ortholog [PMID:16784536
  "Although no clear ID1 ortholog was identified in the Arabidopsis genome"].

## Molecular function

- Sequence-specific DNA binding via the ID domain, in vitro (SAAB selection + EMSA,
  GST fusions) [PMID:15020707 "ID1 binds selectively to an 11 bp consensus motif via the
  ID domain"]. Consensus 5'-TTTGTCG/CT/CT/aT/aT-3'. Z2 and Z3 required; Z1 and Z4 (incl.
  the canonical C2H2 Z1) dispensable; binding zinc-dependent (EDTA/phenanthroline
  abolish it; data not shown).
- Other IDD proteins (VEG7, VEG9) recognise the same motif, so target specificity of ID1
  likely does not come from the DNA-binding domain itself [PMID:15020707].
- Transcriptional activation has not been tested for maize ID1 in the cached literature;
  the rice ortholog activates transcription in yeast [PMID:18774969 "OsId1 is able to
  activate transcription in yeast."].

## Location

- Nuclear: immunolocalization with anti-ID1 antibody [PMID:17307745 "ID1 protein is
  detected in the nuclei of all cell types in immature leaves"] (abstract only cached).
- Expression confined to immature, non-photosynthetic leaf tissue; absent from mature
  blades and the shoot apical meristem [PMID:17307745].

## Biological role

- Loss of function causes extreme late flowering (more than twice the normal leaf
  number), aberrant flowers and frequently no ears [PMID:21730358 "Mutant id1 plants
  exhibit an extreme late flowering phenotype in which they produce more than twice as
  many leaves as normal maize"].
- Acts non-cell-autonomously from the leaf, regulating a transmissible floral signal
  [PMID:9604934 "id1 acts non-cell-autonomously to regulate the production of a
  transmissible signal in the leaf"].
- Acts in the autonomous (photoperiod-independent) pathway: expression and protein level
  are unaffected by light/dark or circadian cues [PMID:17307745 "ID1 expression is
  developmentally regulated and is unperturbed by external stimuli such as photoperiod
  supports the supposition that ID1 acts through the autonomous floral inductive pathway
  in maize"].
- Acts upstream of the florigen gene ZCN8; ZCN8 transcript is >15-fold reduced in id1
  leaves. Because id1 and ZCN8 expression domains do not overlap (immature vs mature
  leaf), ZCN8 is unlikely to be a direct target [PMID:21730358 "it is unlikely that ZCN8
  is a direct target of the ID1 transcriptional regulator"].
- id1 function associated with H3 hyperacetylation at ZCN7/ZCN8 [PMID:26084920] (abstract).
- Expression profiling of id1 vs WT immature leaves identifies 55 differentially expressed
  genes including the dhurrinase-like Zmdhr1-3 [PMID:17928372] (abstract), and carbohydrate
  partitioning differences in source leaves [PMID:22791826].
- In rice, OsId1 is required for flowering under both SD and LD [PMID:18774969 "RNAi
  mutants show a delay in flowering under both short-day (SD) and long-day (LD)
  conditions."].
- A 2026 preprint (PMID:42818387, bioRxiv, not cached) reports scATAC/snRNA-seq of id1
  leaves and candidate direct targets; not used as evidence here.

## Open questions

- Direct in vivo targets of ID1; whether it activates or represses them.
- Whether ID1 has a role in photoperiod-dependent tropical maize/teosinte (unknown per
  PMID:21730358).
