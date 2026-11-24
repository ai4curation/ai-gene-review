---
title: "guca1c / guca1d"
autolink_gene_symbols: false
---

# guca1c / guca1d

[Back to pairs](../README.md)

**Bottom line:** UNRESOLVED, leaning towards protein-level divergence on shared expression. The two GCAP3
co-orthologs (zGCAP3 = guca1c, zGCAP4 = guca1d) are both cone-specific and are co-expressed in every cone type,
with guca1c about ten times more abundant. Both are strong Ca2+-dependent activators of photoreceptor guanylate
cyclase, but in side-by-side assays guca1c is half-maximal near 30 nM free Ca2+ and guca1d near 400 nM. Which copy
kept the ancestral Ca2+ sensitivity is unknown. guca1d has never been knocked out, and guca1c knockdown has no
visual phenotype, so redundancy is suspected but untested.

**Sample record:** fate=UNRESOLVED; level=protein; evidence=experimental_both; identity=75.5%

| | guca1c | guca1d |
|---|---|---|
| Protein name in papers | zGCAP3 (GCAP3a in PMID:30257895) | zGCAP4 (GCAP3b) |
| UniProt | Q8UUX9 (TrEMBL, 188 aa) | Q6ZM98 (TrEMBL, 185 aa) |
| Human ortholog | GUCA1C (GCAP3) | GUCA1C (GCAP3) |
| Chromosome | 15 | 21 |
| ZFIN | ZDB-GENE-030829-1 (alias gcap3) | ZDB-GENE-040724-231 (alias gcap4) |
| Loss of function | morpholino; CRISPR knockout (NMD-type allele) | none |
| Review | [genes/DANRE/guca1c](../../../../genes/DANRE/guca1c/guca1c-ai-review.yaml) | [genes/DANRE/guca1d](../../../../genes/DANRE/guca1d/guca1d-ai-review.yaml) |

**Names.** Zebrafish has seven GCAP genes, and the literature uses protein numbers. From ZFIN aliases
([output.txt](../../../../genes/DANRE/guca1c/guca1c-bioinformatics/output.txt), section 0): gcap1 = guca1aa,
gcap2 = guca1b, gcap3 = guca1c, gcap4 = guca1d, gcap5 = guca1ab.1 (formerly guca1e), gcap7 = guca1g. zGCAP5 belongs
to the GCAP1 subfamily and zGCAP7 to GCAP2; only zGCAP3 and zGCAP4 are GCAP3 co-orthologs:
[PMID:30257895 "A third isoform, GCAP3 (encoded by GUCA1C), occurs in many species, and is expressed only in cones, at least in human and zebrafish [28]; in the latter species, both 3R duplicates (zGCAP3 and zGCAP4, here referred to as GCAP3a and GCAP3b) are cone-specific [24,28,29]."]
[PMID:30257895 "In zebrafish, an isoform that we identify here as one member of the pair of GCAP1 duplicates (zGCAP5, here referred to as GCAP1b) is cone-specific [23,24]."]

## 1. Evidence the pair comes from the TGD

**PANTHER.** The row in `panther_tgd_pairs.tsv` is:

| tgd_call | branch | class | family | human orthologs (a / b) | gar co-orthologs | medaka co-orthologs | medaka parallel dup |
|---|---|---|---|---|---|---|---|
| TGD_tree | Neopterygii\|Teleostei | 1:1 | PTHR23055 (CALCIUM BINDING PROTEINS) | GUCA1C(LDO) / GUCA1C(O) | 1 (same gar gene for both) | 2 | (blank) |

**Ensembl Compara** (`random_sample.tsv`): duplication at Osteoglossocephalai, one gar ortholog for both copies
(ENSLOCG00000009269, LG3), and a separate one-to-one medaka ortholog for each copy. Each zebrafish copy is 84-85%
identical to its own medaka ortholog and 78% to the other one
([RESULTS.md](../../../../genes/DANRE/guca1c/guca1c-bioinformatics/RESULTS.md)).

**Literature.** Lamb & Hunt call the pair the 3R (teleost genome duplication) duplicates of GCAP3 (quote above).
Morales-Camara et al. also place them on different chromosomes:
[PMID:32422965 "Two orthologous genes—guca1c and guca1d—have been identified in the zebrafish genome on chromosomes 15 and 21, respectively."]
The GCAP3 locus is unusual: in gar it seems to have moved, and no conserved neighbours were found across taxa:
[PMID:30257895 "We were not able to identify a consistent chromosomal relationship between GCAP3 and other gene families, when examined across taxa."]

**Synteny (my check).** Two neighbouring gene pairs are retained next to both copies: tgfb1a/tgfb1b and
lpar6a/lpar6b lie within 1.5 Mb of guca1c and guca1d respectively, in both scan directions
([output.txt](../../../../genes/DANRE/guca1c/guca1c-bioinformatics/output.txt), section 6). This is a small
duplicated block, weaker than for many ohnolog pairs.

**Status.** TGD origin supported by the PANTHER `TGD_tree` call, Compara at the teleost node with one gar and two
medaka orthologs, a published phylogenetic assignment as 3R duplicates, and a small duplicated block of two
neighbouring gene pairs. Synteny cannot add more because the GCAP3 neighbourhood is not stable across vertebrates.

## 2. Protein-level comparison

- **Identity.** 75.5% identity, 89.9% similarity over 188 columns ([annotation-comparison.md](annotation-comparison.md)).
  To gar GCAP3: guca1c 68.9%, guca1d 71.4%; to human GUCA1C: 40.7% and 42.6%. A relative-rate test with gar as
  outgroup finds no asymmetry (16 vs 12 unique changes; chi2 = 0.57).
- **Architecture.** Both keep the N-myristoylation glycine and intact Ca2+-binding loops in EF2-EF4 (positions 1, 3,
  5 and 12 of each loop), as in gar and medaka ([RESULTS.md](../../../../genes/DANRE/guca1c/guca1c-bioinformatics/RESULTS.md)).
- **Both activate the cyclase.** In one assay of all six zebrafish GCAPs:
  [PMID:21829700 "Isoforms 1-4 were strong, 5 and 7 were weak activators of membrane bound guanylate cyclase."]
  With native zebrafish retinal membranes, both gave highly significant Ca2+-dependent activation:
  [PMID:23940527 "Differences of activities in the presence of zGCAPs were highly significant: zGCAP3 (t = 9.53, ***P≤0.001); zGCAP4 (t = 10.26, ***P≤0.001)"]
- **They differ in Ca2+ sensitivity.**
  [PMID:21829700 "The IC50 values of zGCAPs could be separated in two groups; one group consisting of zGCAP1, 2, and 3 had IC50 values around 30 nM free [Ca2+], the second group of zGCAP4, 5 and 7 had IC50 values between 180 and 520 nM centered around 400 nM (Table 2 and Figure 3)."]
  [PMID:18777180 "zGCAP4 was a strong activator of membrane-bound guanylate cyclases from bovine and zebrafish retina, showing half-maximal activation at 520-570 nM free Ca(2+) concentration."]
  They also differ in Ca2+ binding: zGCAP3 has three high-affinity sites, the other zGCAPs two:
  [PMID:26061947 "In all zGCAPs at least two binding sites exhibited high affinities for Ca2+ with KD values in the submicromolar range (KD1 and KD2 in Table 2), for zGCAP3 also the third site (KD3) showed high affinity for Ca2+, whereas for other zGCAPs the affinity of KD3 was in the micromolar range."]
- **Ancestral state.** Not measured. Human GCAP3, assayed in a different system, is half-maximal at 0.52 uM:
  [PMID:35328663 "mGCAP3 displayed a half-maximal activation of GC1 (IC50) at 0.52 µM Ca2+, thus similar to the values reported in previous studies for hGCAP1 (0.26–0.59 µM [26,45]."]
  Because mammalian GCAP1 values in that system are also several-fold above the zebrafish GCAP1 value in the Koch
  lab assay, the numbers cannot be compared across labs, and gar GCAP3 has not been assayed.

**Does each copy keep the ancestral molecular function?** Both keep Ca2+-sensitive guanylate cyclase activation. They
differ roughly tenfold in the Ca2+ range over which they act. The residues responsible are not known; none of the
annotated Ca2+-binding positions differs between the copies.

## 3. Expression

- **Cone-specific, both copies.**
  [PMID:11860507 "These results suggest that zGCAP3 is expressed in all four types of cone photoreceptors, but not in rods."]
  [PMID:15486694 "The digoxigenin-labeled zGCAP4 antisense RNA probe hybridized specifically to the myoid region of double cones and long single cones protrude above the external limiting membrane."]
  [PMID:15486694 "Only minimal signal was observed in short single cones."]
- **Same onset.**
  [PMID:19168097 "Transcripts of three cone specific guanylate cyclase-activating proteins (zGCAP3, zGCAP4 and zGCAP7) were also detected at 3-4 dpf."]
- **Adult single-cell data (my reanalysis of GSE175929).** guca1c is in all cones of every type at 57-75 CP10K;
  guca1d in 80-98% of cones at 3.5-6.8 CP10K, lowest in UV cones. Rod signal of both is at the ambient level of the
  cone transducin gnat2 ([scrna_output.txt](../../../../genes/DANRE/guca1c/guca1c-bioinformatics/scrna_output.txt)).
  The published analysis of these data did not list the pair among cone-subtype partitioned genes; it named
  guca1e/guca1e.2 instead:
  [PMID:34462505 "Additionally, we found multiple pairs of paralogous genes that were differentially enriched between UV cones (grk7b, cngb3.2, and guca1e) and other cone types (grk7a, cngb3.1, and guca1e.2)."]
- **Protein.** zGCAP3 is abundant in cones:
  [PMID:23940527 "Although transcription and protein expression levels of zGC3 are similar to that of the cyclase regulator guanylate cyclase-activating protein 3 (zGCAP3), we surprisingly found that zGCAP3 is present in a 28-fold molar excess over zGC3 in zebrafish retinae."]
  No zGCAP4 antibody data exist.
- **Whole larva (E-ERAD-475).** Both are off before hatching; at 3-5 dpf guca1c is 3 TPM and guca1d 5-8 TPM, so the
  larval ratio differs from the adult one ([output.txt](../../../../genes/DANRE/guca1c/guca1c-bioinformatics/output.txt), section 4).
- **Pre-duplication state.** Spotted gar GCAP3 has a Bgee RNA-seq call in the eye (97.7) and only low calls
  elsewhere. Lamb & Hunt detected GCAP3 transcripts in both gar and bowfin:
  [PMID:30257895 "Interestingly, in both bowfin and Florida gar we found transcripts for all six jawed vertebrate isoforms, though GCAP3 and GCAP2-B were present at lower levels than the other four isoforms (GCAP1, GCAP1-L, GCAP2 and GCAP2-A)."]
  Human GCAP3 is cone-specific (PMID:11860507). The ancestral gene was therefore a cone gene, and both copies kept
  that; no gar data resolve cone subtypes.

Summary: fully overlapping cell-type expression, with a large difference in abundance and a modest UV-cone bias
against guca1d. No expression domain is copy-specific.

## 4. Experimental evidence of function

**guca1c**

- Morpholino knockdown abolished zGCAP3 but left larval optokinetic and optomotor responses normal:
  [PMID:23940527 "No significant differences in behavioral responses among wild type, morphants and control morphants were found, indicating that a loss of zGCAP3 has no consequences in primary visual processing in the larval retina despite its prominent expression pattern."]
  The authors attribute this to other GCAPs, naming zGCAP4:
  [PMID:23940527 "A good substitute for zGCAP3 might be zGCAP4, because its transcripts are also detected at 3.5 dpf [8] and it is a strong activator of membrane bound GCs with a similar apparent affinity for GCs [17], [20]."]
- CRISPR knockout (premature stop; mRNA below 40% of wild type), studied for a glaucoma link:
  [PMID:32422965 "One of the most interesting phenotypic findings in guca1c KO animals was the upregulation of GFAP in Müller cells, and the evidence of apoptosis in some ganglion, indicating the existence of gliosis and glaucoma-like alterations associated with GCAP3 LoF."]
  Cone physiology was not measured, and guca1d was not examined:
  [PMID:32422965 "Because there is no evidence of functional divergence among these genes, we prioritized guca1c LoF analysis in our study, although possible compensatory phenotypic effects by guca1d on a guca1c KO background cannot be disregarded."]

**guca1d**

- No morphant, mutant or rescue data. Only biochemistry (section 2).

**Both copies**

- No double mutant, no electrophysiology, no measurement of guca1d in guca1c mutants. The knockout allele is of the
  NMD type that can trigger transcriptional adaptation.

## 5. Fate classification

**UNRESOLVED. Level of the observed difference: protein (Ca2+ sensitivity). Confidence in the difference: moderate
(one laboratory, same assay, repeated across three papers); confidence in any fate: low.**

**Established**

- Both copies are cone-specific and co-expressed in every cone type; no copy-specific expression domain.
- Both are strong Ca2+-dependent guanylate cyclase activators.
- They differ about tenfold in the Ca2+ concentration of half-maximal activation and in the affinity of the third
  Ca2+ site.
- Loss of guca1c alone does not impair larval visual behaviour.

**Not established**

- Which copy changed: the ancestral (gar) GCAP3 sensitivity is unknown, so the difference could be a split of an
  ancestral range (partition at the protein level), a gain in one copy (innovation), or neutral drift in a redundant
  pair.
- Whether the copies are redundant: guca1d was never knocked out, and the guca1c morphant result is compatible with
  compensation by guca1d or by other GCAPs.

**What would resolve it**

- Assaying gar or bowfin GCAP3 side by side with zGCAP3 and zGCAP4.
- guca1c, guca1d and double mutants with cone ERG recovery kinetics; a double-only phenotype would indicate backup,
  a single-mutant kinetic change matching its Ca2+ range would indicate protein-level specialization.
- The medaka orthologs, which also kept both copies, would test whether the sensitivity split is shared.

## 6. GO annotation consistency across the pair

Source: [annotation-comparison.md](annotation-comparison.md), after both reviews.

- **Shared, correctly.** Calcium ion binding (IBA, IDA, IEA, ISS) and calcium-sensitive guanylate cyclase activator
  activity (IBA, IDA) are on both copies with experimental support on each, and all were accepted. The PANTHER IBA
  node for GO:0008048 is seeded by the two zebrafish copies themselves.
- **Only on guca1c.** guanylate cyclase activator activity (GO:0030250, ISS), the parent of GO:0008048; redundant
  for guca1d, which has the child term by IDA.
- **Process.** Both carry only the deep-node IBA regulation of signal transduction (kept as non-core). Neither has a
  photoreceptor or phototransduction process row, and no in vivo physiology exists for either copy to support one.
- **What GO cannot express.** The difference between the copies is quantitative (Ca2+ range), and GO has no term that
  separates high- and low-sensitivity activators. The annotations are consistent across the pair and should stay
  shared.

## 7. Open questions

- What is the Ca2+ sensitivity of gar GCAP3 in the same assay?
- Do guca1c; guca1d double mutants slow cone photoresponse recovery, and do single mutants shift it in the direction
  predicted by their Ca2+ ranges?
- Why is guca1d relatively low in UV cones, and is that shared with medaka?
- Is the rod immunostaining for GCAP3 in the knockout study real, given that transcripts are cone-restricted?

## References

PMID:11860507, PMID:15486694, PMID:18777180, PMID:19168097, PMID:21829700, PMID:23940527, PMID:26061947,
PMID:30257895, PMID:32422965, PMID:34462505, PMID:35328663. Also `panther_tgd_pairs.tsv`, `random_sample.tsv`,
[annotation-comparison.md](annotation-comparison.md),
[guca1c-bioinformatics/RESULTS.md](../../../../genes/DANRE/guca1c/guca1c-bioinformatics/RESULTS.md),
[output.txt](../../../../genes/DANRE/guca1c/guca1c-bioinformatics/output.txt),
[scrna_output.txt](../../../../genes/DANRE/guca1c/guca1c-bioinformatics/scrna_output.txt),
[expression_output.txt](../../../../genes/DANRE/guca1c/guca1c-bioinformatics/expression_output.txt).
