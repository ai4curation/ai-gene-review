---
title: "mapre3a / mapre3b"
autolink_gene_symbols: false
---

# mapre3a / mapre3b

[Back to pairs](../README.md)

**Bottom line:** UNRESOLVED. The two EB3 (MAPRE3) co-orthologs encode equally conserved microtubule plus-end
tracking proteins, and there is no functional data for either. Their expression differs in timing and breadth:
mapre3b is maternal and broadly expressed, like the gar gene, and mapre3a is zygotic, starts late and is highest in
retina, brain and testis. That fits an expression partition or a declining mapre3a equally well.

**Sample record:** fate=UNRESOLVED; level=expression; evidence=expression_only; identity=83.0%

| | mapre3a | mapre3b |
|---|---|---|
| UniProt | A0A8M2B5B2 (TrEMBL, 273 aa; RefSeq XP_005158903.1) | A0A8M9Q0D6 (TrEMBL, 278 aa; RefSeq XP_021330664.2) |
| Human ortholog | MAPRE3 (EB3) | MAPRE3 (EB3) |
| Chromosome | 17 | 4 |
| ZFIN | ZDB-GENE-050913-88 | ZDB-GENE-040704-6 |
| Ensembl | ENSDARG00000020231 | ENSDARG00000102878 |
| Review | [genes/DANRE/mapre3a](../../../../genes/DANRE/mapre3a/mapre3a-ai-review.yaml) | [genes/DANRE/mapre3b](../../../../genes/DANRE/mapre3b/mapre3b-ai-review.yaml) |

## 1. Evidence the pair comes from the TGD

**PANTHER.** The row in `panther_tgd_pairs.tsv` is:

| tgd_call | branch | class | family | human orthologs (a / b) | gar co-orthologs | medaka co-orthologs | medaka parallel dup |
|---|---|---|---|---|---|---|---|
| TGD_tree | Neopterygii\|Teleostei | 1:1 | PTHR10623 (MICROTUBULE-ASSOCIATED PROTEIN RP/EB FAMILY MEMBER) | MAPRE3(LDO) / MAPRE3(O) | 1 (same gar gene for both) | 2 | (blank) |

**Ensembl Compara.** The duplication node is Clupeocephala (`random_sample.tsv`). Both copies share one gar
orthologue (ENSLOCG00000016310) and the human MAPRE3 gene, and each has its own one-to-one medaka orthologue
([RESULTS.md](../../../../genes/DANRE/mapre3a/mapre3a-bioinformatics/RESULTS.md)).

**Synteny.** The copies are on different chromosomes (mapre3a chr17, mapre3b chr4). One neighbouring gene is
duplicated alongside them: dpysl5a sits next to mapre3a and its teleost-level paralogue dpysl5b next to mapre3b.
No other neighbour within 1.5 Mb has its paralogue near the other copy, although two more teleost-level pairs link
the mapre3b region to chr17
([RESULTS.md](../../../../genes/DANRE/mapre3a/mapre3a-bioinformatics/RESULTS.md)). I did not check the gar
region directly.

**Literature.** I found no paper that discusses this pair or its origin.

**Status.** TGD origin is supported by two independent gene-tree methods (PANTHER and Compara) and by medaka
retaining both copies. The synteny signal is minimal (one conserved neighbour pair), consistent with, but not
strong independent support for, a whole-genome rather than a local duplication.

## 2. Protein-level comparison

- **Identity.** 83.0% identity and 89.0% similarity over 282 columns
  ([annotation-comparison.md](annotation-comparison.md)); 85.6% between the RefSeq NP isoforms. mapre3a and mapre3b
  are 77.9% and 76.6% identical to human MAPRE3 and 72.1% and 71.3% to gar MAPRE3.
- **Domains.** Both keep the calponin-homology (CH) domain (89.3% and 91.3% identical to human MAPRE3), the EB1
  C-terminal (EBH) domain (81.7% and 80.3%) and an acidic tail ending in an aromatic residue (mapre3a ...QDEY,
  mapre3b ...QEEY; human ...QDEY). Most differences between the copies are in the linker between the two domains.
  These are the parts that do the work in mammalian EBs:
  [PMID:19255245 "Furthermore, we demonstrated in vitro and in cells that the EB plus-end tracking behavior depends on the calponin homology domain but does not require dimer formation."]
  [PMID:19255245 "In contrast, dimerization is necessary for the EB anti-catastrophe activity in cells"]
  [PMID:19255245 "EBs terminate with a flexible acidic tail containing the C-terminal EEY/F sequence, which is important for self-inhibition and binding to various partners"]
- **Rate.** With gar as outgroup, 14 changes are unique to mapre3a and 17 to mapre3b (chi2 = 0.29, not
  significant).
- **Biochemistry and cross-rescue.** None for either zebrafish protein.

**Does each copy keep the ancestral molecular function?** Probably yes for both, on sequence grounds only: every
domain needed for plus-end tracking and catastrophe suppression in mammalian EB3 is conserved, and neither copy is
evolving faster.

## 3. Expression

All expression data come from my queries of public resources
([RESULTS.md](../../../../genes/DANRE/mapre3a/mapre3a-bioinformatics/RESULTS.md),
[output.txt](../../../../genes/DANRE/mapre3a/mapre3a-bioinformatics/output.txt)); no published in situ exists.

- **Development (E-ERAD-475, whole embryo).** mapre3b is maternal (4-5 TPM in zygote, 34 TPM at 1k-cell) and
  present at every stage, reaching 41 TPM at day 5. mapre3a is at 0 TPM until the 20-25-somite stage and rises to
  16 TPM by day 5.
- **Tissues (Bgee).** mapre3b has 20 calls, most with high scores, including muscle, heart, gill, intestine, liver
  and spleen. mapre3a has 13, highest in retina, brain and testis, with lower scores elsewhere and no call in
  intestine, liver, gill, spleen or ovarian follicle. Both are called in brain and retina.
- **ZFIN.** Nothing curated for mapre3a; one high-throughput in situ record for mapre3b with anatomy
  "unspecified".
- **Pre-duplication state.** Gar MAPRE3 is called in 14 tissues, highest in brain and eye, and including muscle,
  liver, gill, intestine and ovary. The broad mapre3b profile resembles it; mapre3a looks like a narrower, mostly
  neural subset. Whether gar MAPRE3 is maternally loaded is not known from these data.
- **Tetrapod context.** Mammalian EB3 is brain-enriched:
  [PMID:10644998 "The full-length cDNA of this novel homologue of EB1, named EB3, encoded a protein of 282 amino acids with 54% identity to EB1, and it was expressed preferentially in brain tissue on Northern blots."]

**Shared vs copy-specific.** Brain and retina are shared. Maternal/early-embryo expression and most non-neural
adult tissues are mapre3b-only in these data. No domain was found that is mapre3a-only apart from marginal calls
(embryo, mesonephros).

## 4. Experimental evidence of function

- **mapre3a:** none. The only zebrafish paper naming it lists it among genes near CpGs that become hypermethylated
  after developmental glucocorticoid exposure:
  [PMID:38989456 "In addition, we found hypermethylated CpGs in genomic regions associated with hdGC-primed genes, auts2a, mapre3a, igfbp5a, and pde4cb, which overlapped with identified GC-primed DEGs in in vitro dexamethasone-treated human neurons13 (Table S8)."]
- **mapre3b:** none. It was one of the genes knocked down in a thrombocyte screen
  [PMID:39939668 "This study employed a comprehensive screening approach through a piggyback knockdown strategy targeting 394 protein-encoding genes expressed explicitly in young thrombocytes."]
  and is not among the eight hits. A negative screen result is not evidence of redundancy.
- **Both:** no mutants, morphants, double mutants or cross-rescue. Most zebrafish papers on "EB3" use tagged
  mammalian EB3 as a reporter of microtubule growth, which does not bear on these genes.

## 5. Fate classification

**UNRESOLVED; the observed difference is at the level of expression; the evidence is expression data only.
Confidence in any specific fate: low.**

**Established**

- Both proteins keep the full EB3 architecture, are about equally similar to human and gar MAPRE3, and evolve at
  the same rate.
- Expression differs in timing and breadth: mapre3b maternal, early and broad; mapre3a zygotic, late and highest in
  retina, brain and testis.

**Inferred, not shown**

- That the copies share molecular function (no assay or cross-rescue).
- That the expression difference is a partition. mapre3a has no clear domain of its own; its profile is a subset of
  mapre3b's and of gar's. That pattern fits a partition (with mapre3a keeping a neural role) but also a gradual
  decline of mapre3a (hypofunctionalization) with mapre3b doing most of the work.

**Why not the other fates**

- *Innovation:* no protein change and no new expression domain.
- *Backup or dosage:* the profiles are not the same (no maternal mapre3a; many tissues without mapre3a calls), and
  there are no functional data to show redundancy.
- *Partition:* possible, but needs cell-resolved expression showing a cell type where mapre3a dominates, and
  single-mutant phenotypes.

**What would change the call**

- Single-cell data showing mapre3a enriched in particular retinal or neuronal cell types where mapre3b is low would
  support PARTITION (expression).
- A neural phenotype in mapre3a single mutants (RNA-less alleles, to avoid transcriptional adaptation) would
  support PARTITION; no phenotype in either single mutant but a phenotype in the double would support BACKUP.
- Maternal gar MAPRE3 transcripts would make the late onset of mapre3a a loss rather than an ancestral feature.

## 6. GO annotation consistency across the pair

Source: [annotation-comparison.md](annotation-comparison.md), after both reviews.

- **Identical and correct.** The two copies carry exactly the same ten rows (eight IBA from the RP/EB family node
  PTN000065701, two IEA) and I made the same call on every row: microtubule plus-end binding, microtubule plus-end,
  cytoplasmic microtubule, microtubule binding, cytoskeleton, microtubule organizing center, regulation of
  microtubule polymerization or depolymerization and protein localization to microtubule accepted; spindle assembly
  and spindle midzone kept as non-core (fly/Dictyostelium and yeast donors, no vertebrate EB3 evidence).
- **No experimental rows** on either copy and none on the other UniProt accessions of either gene.
- **Propagation.** Same-node IBA propagation treats the copies as equivalent. That is right for the molecular
  function and location, which the sequence data support. It cannot capture the expression difference, but because
  all rows are cell-level (MF, CC, cellular processes), nothing here needs to be copy-specific.
- **Core functions** are the same on both copies: microtubule plus-end binding (GO:0051010) at the microtubule plus
  end, acting in regulation of microtubule polymerization or depolymerization.

## 7. Open questions

- Which cells express each copy in larval retina and brain (single-cell atlases, HCR)?
- Is gar MAPRE3 maternally deposited?
- Do mapre3a and mapre3b differ in comet behaviour when expressed in the same cells?
- Do single or double mutants have neuronal or retinal phenotypes?

## References

PMID:10644998, PMID:19255245, PMID:38989456, PMID:39939668. Also `panther_tgd_pairs.tsv`, `random_sample.tsv`,
[annotation-comparison.md](annotation-comparison.md),
[mapre3a-bioinformatics/RESULTS.md](../../../../genes/DANRE/mapre3a/mapre3a-bioinformatics/RESULTS.md) and
[output.txt](../../../../genes/DANRE/mapre3a/mapre3a-bioinformatics/output.txt).
