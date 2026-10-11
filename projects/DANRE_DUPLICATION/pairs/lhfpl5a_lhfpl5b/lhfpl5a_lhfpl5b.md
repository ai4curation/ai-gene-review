---
title: "lhfpl5a / lhfpl5b"
autolink_gene_symbols: false
---

# lhfpl5a / lhfpl5b

[Back to pairs](../README.md)

**Bottom line:** PARTITION, at the level of expression, with the protein function conserved. The two copies of
the MET-channel accessory subunit LHFPL5 are expressed in separate hair-cell populations: lhfpl5a only in the inner
ear and lhfpl5b only in the lateral line. Each mutant loses transduction only where its gene is expressed.
Lhfpl5a protein restores lateral-line transduction in lhfpl5b mutants, so the proteins are interchangeable in the one
direction that has been tested. The ancestral (pre-duplication) expression has not been measured in gar.

**Sample record:** fate=PARTITION; level=expression; evidence=experimental_both; identity=76.5%

| | lhfpl5a | lhfpl5b |
|---|---|---|
| UniProt | F1Q837 (TrEMBL, 219 aa) | B0UYJ1 (TrEMBL, 221 aa) |
| Human ortholog | LHFPL5 (TMHS) | LHFPL5 (TMHS) |
| Chromosome | 11 | 8 |
| ZFIN | ZDB-GENE-110131-8 | ZDB-GENE-080220-51 |
| Mutant alleles | tm290d (astronaut; ENU, K80X) | vo35 (CRISPR, 5-bp deletion, S77FfsX48) |
| Review | [genes/DANRE/lhfpl5a](../../../../genes/DANRE/lhfpl5a/lhfpl5a-ai-review.yaml) | [genes/DANRE/lhfpl5b](../../../../genes/DANRE/lhfpl5b/lhfpl5b-ai-review.yaml) |

## 1. Evidence the pair comes from the TGD

**PANTHER.** The row in `panther_tgd_pairs.tsv` is:

| tgd_call | branch | class | family | human orthologs (a / b) | gar co-orthologs | medaka co-orthologs | medaka parallel dup |
|---|---|---|---|---|---|---|---|
| TGD_tree | Neopterygii\|Teleostei | 1:1 | PTHR12489 (LIPOMA HMGIC FUSION PARTNER-LIKE PROTEIN) | LHFPL5(LDO) / LHFPL5(O) | 1 (same gar gene for both) | 2 | (blank) |

PANTHER places the duplication after the split from gar and before the zebrafish-medaka split, with a single gar
co-ortholog for both copies and two medaka copies.

**Literature.** The paper that first described the pair built a gene tree with gar and 13 teleost orders:
[PMID:32009898 "Phylogenetic analysis of the Lhfpl5 protein sequences supports the idea that duplicate lhfpl5 genes originated from the teleost WGD event (Figure 1A)."]
[PMID:32009898 "In all 13 teleost orders surveyed, there are two lhfpl5 genes whose protein products cluster with either the lhfpl5a or lhfpl5b ohnolog groups."]
[PMID:32009898 "Based on available genomic data, there is no evidence that spotted gar fish have duplicated lhfpl5 genes."]
They also cite a synteny-based ohnolog catalogue:
[PMID:32009898 "In all four teleost species surveyed, Singh and Isambert show that lhfpl5a and lhfpl5b are true ohnologs that arose from the teleost-specific WGD under the strictest criteria used in their study."]

**My check.** Ensembl Compara places the duplication at the Osteoglossocephalai node and gives one gar
orthologue for both copies. The copies are on different chromosomes (11 and 8), and so are their one-to-one medaka
orthologues (5 and 7). The same gene families flank both copies: mapk14b, srpk1b and cpne5b next to lhfpl5a, and
mapk14a, srpk1a and cpne5a next to lhfpl5b. Where Compara gives orthologues for them, they sit next to gar lhfpl5
(LG3) and human LHFPL5 (6p21). This is double conserved synteny
([lhfpl5a-bioinformatics/RESULTS.md](../../../../genes/DANRE/lhfpl5a/lhfpl5a-bioinformatics/RESULTS.md)).

**Status.** TGD origin is well supported: a PANTHER `TGD_tree` call, a published gene tree with gar and retention in
all 13 teleost orders sampled, a synteny-based ohnolog call cited by the authors, and my own double-conserved-synteny
check.

## 2. Protein-level comparison

- **Identity.** 76.5% identity and 86.9% similarity over 221 columns
  ([annotation-comparison.md](annotation-comparison.md)). The published figure is:
  [PMID:32009898 "Zebrafish Lhfpl5a and Lhfpl5b are 76% identical and 86% similar to one another (Needleman-Wunsch alignment)."]
- **Against outgroups.** Lhfpl5a is slightly closer than Lhfpl5b to gar and human LHFPL5 (my script:
  [RESULTS.md](../../../../genes/DANRE/lhfpl5a/lhfpl5a-bioinformatics/RESULTS.md); published:
  [PMID:32009898 "Compared to human LHFPL5, Lhfpl5a and Lhfpl5b are 70/65% identical and 86/81% similar respectively."]).
  This is a small difference and says nothing about function by itself.
- **Architecture.** Both keep the four transmembrane helices of the family:
  [PMID:32009898 "Alignment of the zebrafish Lhfpl5a and Lhfpl5b proteins with those from human, mouse and chicken reveals that both zebrafish ohnologs retain the same protein structure (Figure 1B)."]
- **Cross-rescue (one direction).** A hair-cell GFP-Lhfpl5a transgene restores lateral-line transduction in lhfpl5b
  mutants:
  [PMID:32009898 "The loss of MET channel activity in lhfpl5bvo35 neuromasts is rescued by expression of the GFP-lhfpl5a vo23Tg transgene (Figures 4I,J; n = 7/7 mutant individuals). This result indicates that Lhfpl5a and Lhfpl5b are functionally interchangeable in this context."]
  The same transgene restores swim-bladder inflation in lhfpl5b mutants:
  [PMID:37272538 "It has been shown that this lhfpl5a transgene rescues lateral line hair cell function in lhfpl5b−/− mutant fish (Erickson et al., 2020)."]
  The reverse (Lhfpl5b in lhfpl5a mutant ear) has not been done, and no GFP-Lhfpl5b localization exists.

**Does each copy keep the ancestral molecular function?** Yes for Lhfpl5a, which rescues both its own mutant and the
lhfpl5b mutant. For Lhfpl5b the evidence is its lateral-line requirement and its conserved structure; that it can
work in inner-ear hair cells is inferred, not shown.

## 3. Expression

- **Split between the ear and the lateral line (in situ hybridization, 1-5 dpf).**
  [PMID:32009898 "Here we show that the zebrafish lhfpl5 genes are expressed in discrete populations of hair cells: lhfpl5a expression is restricted to auditory and vestibular hair cells in the inner ear, while lhfpl5b expression is specific to hair cells of the lateral line organ."]
  [PMID:32009898 "This divergence in lhfpl5 ohnolog expression continues at 5 dpf, with lhfpl5a found exclusively in the sensory patches of the ear and lhfpl5b restricted to lateral line hair cells (Figures 2E–J)."]
- **Adults.** Adult inner-ear hair cells express lhfpl5a and not lhfpl5b:
  [PMID:39484049 "Zebrafish HCs expressed ush1c, tmie, pcdh15a/b, and lhfpl5a, but not the paralog lhfpl5b, while mouse HCs expressed the orthologs Ush1c, Tmie, Pcdh15, and Lhfpl5, respectively."]
- **Used as organ markers.** The single-cell atlas of the ear uses the two genes to tell ear and lateral-line hair
  cells apart:
  [PMID:36598134 "To distinguish between inner ear and lateral line hair cells, we queried expression of previously described markers for inner ear (gpx2, kifl, strc, and lhfpl5a) and lateral line (strc1, lhfpl5b, and s100t) (Erickson et al., 2019; Erickson and Nicolson, 2015)."]
- **Regulation.** lhfpl5a belongs to an ear hair-cell program that prdm1a represses in the lateral line:
  [PMID:40825768 "To validate the expression of genes upregulated in prdm1a mutants, we performed HCRs for pvalb9, ckbb, s100a1, tmc2a, strc, kncn, lhfpl5a, tbx2a, and tbx2b and found them to all be strongly expressed in the lateral line hair cells of prdm1a mutants, but not sibling hair cells (Fig. 2i–p, Supplementary Fig. 2e–h)."]
- **Public resources.** ZFIN curated expression has inner-ear terms only for lhfpl5a and neuromast terms only for
  lhfpl5b. Bgee adds bulk RNA-seq calls for lhfpl5b in many adult tissues and early embryos. These are not
  hair-cell resolved and I do not use them
  ([expression_output.txt](../../../../genes/DANRE/lhfpl5a/lhfpl5a-bioinformatics/expression_output.txt)).
- **Pre-duplication state.** Mouse LHFPL5 is expressed in cochlear and vestibular hair cells. Mammals have no lateral
  line, and I found no data on gar lhfpl5 expression. That the ancestor was expressed in both ear and lateral line is
  a reasonable inference (both organs use the same MET machinery), but it has not been measured.

The partition is clean and non-overlapping. The authors describe it as the first such case for hair-cell genes:
[PMID:32009898 "To our knowledge, this is the first description of duplicated genes whose expression patterns have cleanly partitioned between inner ear and lateral line hair cells."]

## 4. Experimental evidence of function

**Alleles**

| Gene | Allele | Lesion | Type | Source |
|---|---|---|---|---|
| lhfpl5a | tm290d (astronaut) | ENU point nonsense, K80X | PTC; mRNA decay not reported | PMID:32009898 |
| lhfpl5b | vo35 | CRISPR 5-bp deletion, S77FfsX48 | PTC (frameshift); mRNA decay not reported | PMID:32009898 |

[PMID:32009898 "This mutation disrupts the protein in the first extracellular loop and deletes the final three of four transmembrane helices in Lhfpl5b."]

**lhfpl5a**

- No transduction in any sensory patch of the ear; profoundly deaf; balance defects:
  [PMID:32009898 "These three tests confirmed that all sensory patches in the otic capsule are inactive in lhfpl5atm290d mutants."]
  [PMID:32009898 "Results confirm that lhfpl5atm290d mutants are profoundly deaf, displaying little to no response to acoustic stimuli (p < 0.001 compared to all other genotypes)."]
- Lateral line normal (FM 1-43 labeling and hair-cell number as wild type). This explains the original 1998 finding
  of normal lateral-line microphonics:
  [PMID:9491988 "Mutant astronaut and cosmonaut hair cells have relatively normal microphonics and thus appear to affect events downstream of mechanotransduction."]
- Rescued by GFP-Lhfpl5a:
  [PMID:32009898 "From these results we conclude that the hair bundle-localized GFP-Lhfpl5a protein is functional and can rescue the behavioral and MET channel defects in lhfpl5atm290d mutants."]
- Pcdh15a fails to reach the hair bundle:
  [PMID:28219986 "In contrast, EGFP-tagged Pcdh15a remained in the hair cell body of lhfpl5a mutants at all developmental stages, implying that Lhfpl5a is required for transport to the hair bundle."]

**lhfpl5b**

- Lateral line silenced; ear normal:
  [PMID:32009898 "CRISPR-Cas 9 knockout of lhfpl5b alone silences the lateral line organ but has no effect on otic hair cell function."]
  [PMID:32009898 "Thus, lhfpl5atm290d mutants exhibit defects in inner ear function, while the lhfpl5bvo35 mutation has no effect on these hair cells."]
- Fewer neuromast hair cells, as in other transduction mutants:
  [PMID:32009898 "This decrease in the number of neuromast hair cells is consistent with lhfpl5b mutants being deficient in mechanotransduction in this cell type."]
- Adult viable, and used since as a lateral-line-only mutant:
  [PMID:37272538 "A CRISPR-Cas9 knockout of LHFPL tetraspan subfamily member 5b (lhfpl5b) is the first genetic zebrafish mutant where the lateral line is non-functional from birth but hearing and balance are normal (Erickson et al., 2020)."]

**Both copies**

- Double mutants: the few neuromast hair cells that still take up dye in lhfpl5b mutants keep doing so, so lhfpl5a
  is not compensating in the lateral line:
  [PMID:32009898 "Occasional labeling persists in lhfpl5a/lhfpl5b double mutants, indicating that lhfpl5a is not partially compensating for the loss of lhfpl5b (Supplementary Figures 3A–D)."]
- Transcriptional adaptation (paralog upregulation) was not measured in either mutant. Both alleles carry premature
  stops, but since each single mutant already loses all function in its own organ, masking by the paralog is not an
  issue for the fate call.

## 5. Fate classification

**PARTITION, at the expression level; the protein function is conserved. Confidence: high for the partition; moderate
for protein equivalence (one-direction rescue).**

**Established**

- Non-overlapping expression: lhfpl5a in ear hair cells (larva and adult), lhfpl5b in lateral-line hair cells.
- Each single mutant loses transduction only in the organ where its copy is expressed; the other organ is normal.
- Lhfpl5a restores lateral-line function in lhfpl5b mutants, so the difference between the copies there is where
  they are expressed, not what the protein does. The authors conclude:
  [PMID:32009898 "As such, the subfunctionalization of the lhfpl5 ohnologs appears to be caused by the divergence in their expression patterns rather than functional differences in their protein products."]

**Inferred, not shown**

- That the pre-duplication gene was expressed in both ear and lateral line (no gar or other non-teleost fish data).
  Without it, a gain of a lateral-line domain by one copy cannot be strictly excluded, although the lateral line and
  its MET machinery predate the teleosts.
- That Lhfpl5b can do Lhfpl5a's job in the ear (reciprocal rescue not done).
- That the same split holds in other teleosts; expression was examined only in zebrafish:
  [PMID:32009898 "It is possible that a similar mechanism is responsible for the retention of both genes in other teleost species as well, though the expression patterns of the lhfpl5 ohnologs have not been examined in other fish."]

**Why not the other fates**

- *Backup or dosage:* each copy is essential in its own organ and the other copy does not compensate.
- *Innovation:* no new protein function; the known Lhfpl5 roles (Pcdh15 trafficking, MET) are shared with mouse.
  Zebrafish-specific requirements for Cdh23 and Myo7aa in Lhfpl5a localization were found only for lhfpl5a and may
  reflect hair-cell type (vestibular hair cells keep a kinocilium) rather than a new function.

**What would change the call**

- Failure of Lhfpl5b to rescue lhfpl5a mutant ear hair cells would add a protein-level component (MIXED).
- Gar lhfpl5 expression limited to one organ would turn one copy's domain into an innovation.

## 6. GO annotation consistency across the pair

Source: [annotation-comparison.md](annotation-comparison.md), after both reviews.

**Shared, and correctly so.** plasma membrane (IBA), membrane (IEA) and detection of mechanical stimulus involved in
sensory perception (GO:0050974, IBA) are on both copies and were accepted on both. The IBA for GO:0050974 lists
lhfpl5a (ZFIN:ZDB-GENE-110131-8) among its sources; that is expected, not circular.

**Asymmetric, and correctly so.**

- Sensory perception of sound (GO:0007605, IBA) is accepted for lhfpl5a and marked as over-annotated for lhfpl5b.
  The PANTHER node is right for the protein, but lhfpl5b is not expressed in the ear and lhfpl5b mutants hear
  normally. This is the one row where same-node IBA propagation cannot see the expression partition. I recorded it
  with a propagation_review (root cause PROPAGATION_BAD, failure mode CONTEXT_OR_TISSUE_MISMATCH).
- The inner-ear IMP rows (stereocilium organization, Pcdh15a localization, the 1998 astronaut detection row) belong to
  lhfpl5a only, which matches its expression.

**Asymmetries that come from which copy was studied.**

- lhfpl5b has no experimental row for its defining process in GOA. Its only IMP row, neuromast hair cell
  morphogenesis, rests on a reduced hair-cell number that the authors attribute to lost transduction; I marked it as
  over-annotated. A NEW IMP row for GO:0050974 is blocked by the validator because the term already exists as an
  IBA, so the experimental evidence sits on the IBA review.
- The stereocilium-tip location (NEW, IDA) was added to lhfpl5a only, because GFP-Lhfpl5a is the only tagged protein
  that has been imaged. It probably also applies to Lhfpl5b.
- lhfpl5b carries a root-level ND molecular-function row, and lhfpl5a has no molecular function row at all. The ND row
  was removed. Both reviews record the same function in core_functions: a contribution to the MET channel complex
  (GO:0140135). The comparison table lists no core molecular functions because it reads only the
  `molecular_function` slot, and both reviews record the function as `contributes_to_molecular_function`.
- The lhfpl5a row "protein localization to cilium" was modified to protein localization to plasma membrane, because
  stereocilia are not cilia.

**Should be copy-specific:** hearing and balance (lhfpl5a); lateral-line transduction (lhfpl5b).
**Should be shared:** molecular function, stereocilium-tip location, MET complex membership.

## 7. Open questions

- Does Lhfpl5b rescue the lhfpl5a mutant ear? This is the missing half of the cross-rescue.
- Where is lhfpl5 expressed in gar or bowfin? That would test whether the partition split an ancestral ear +
  lateral line pattern.
- Is the partition the same in medaka and other teleosts, where both copies are kept?
- What produces the residual dye uptake in a few neuromast hair cells of double mutants (another LHFPL family
  member)?

## References

PMID:9491988, PMID:28219986, PMID:32009898, PMID:36598134, PMID:37272538, PMID:39484049, PMID:40825768. Also
`panther_tgd_pairs.tsv`, [annotation-comparison.md](annotation-comparison.md),
[lhfpl5a-bioinformatics/RESULTS.md](../../../../genes/DANRE/lhfpl5a/lhfpl5a-bioinformatics/RESULTS.md) and
[expression_output.txt](../../../../genes/DANRE/lhfpl5a/lhfpl5a-bioinformatics/expression_output.txt).
