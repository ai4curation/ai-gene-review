---
title: "pax6a / pax6b"
autolink_gene_symbols: false
---

# pax6a / pax6b

[Back to pairs](../README.md)

**Bottom line:** PARTITION (subfunctionalization) at the expression level, on top of a
dose-sensitive shared core. The two proteins activate target genes equally well. Their
expression domains differ because each copy lost different cis-regulatory elements. As a
result, pancreatic and gut endocrine development belongs to pax6b alone, and habenular
neurogenesis to pax6a alone. In the eye the copies share the ancestral role and act additively
by dose. There is no evidence of a new (neofunctionalized) function in zebrafish.

| | pax6a | pax6b |
|---|---|---|
| UniProt | P26630 (Swiss-Prot) | A0A0R4IQL7 (TrEMBL) |
| Human ortholog | PAX6 | PAX6 |
| Former names | pax6.1, pax[zf-a] | pax6.2 |
| Chromosome | 25 | 7 |
| Review | [genes/DANRE/pax6a](../../../../genes/DANRE/pax6a/pax6a-ai-review.yaml) | [genes/DANRE/pax6b](../../../../genes/DANRE/pax6b/pax6b-ai-review.yaml) |

## 1. Evidence the pair comes from the TGD

**PANTHER.** The row in `panther_tgd_pairs.tsv` is:

| tgd_call | branch | class | family | human orthologs (a / b) | gar co-orthologs | medaka co-orthologs | medaka parallel dup |
|---|---|---|---|---|---|---|---|
| TGD_likely_parallel | Teleostei\|DANRE | 1:1 | PTHR45636 | PAX4(O);PAX6(LDO) / PAX4(O);PAX6(O) | 1 (same gar gene for both) | 2 | yes |

PANTHER puts the duplication on the zebrafish branch, but both copies share one gar
co-ortholog, and medaka also has two copies. The project page reads this pattern as a TGD pair
whose zebrafish and medaka copies do not group as ((zfA, medA), (zfB, medB)).

**Synteny and phylogeny (established).**

- Each copy keeps part of the ancestral neighbourhood, and the two parts are complementary:
  [PMID:18282108 "Zebrafish LG25 retains pax6a synteny with wt1a and with the majority of pax6 cis-regulatory elements, but rcn1 and elp4 coding exons have been lost."]
  [PMID:18282108 "On LG7 the pax6b locus and rcn1 and elp4 exons have been retained, but many of the pax6b control elements, as well as the wt1 homolog, have been lost."]
- The authors' conclusion on origin:
  [PMID:18282108 "Zebrafish pax6a and pax6b probably arose through large scale genome duplication, rather than regional duplication and translocation."]
- A gar-anchored synteny and phylogeny study places both teleost pax6 copies in the TGD:
  [PMID:24951566 "We detected conserved synteny between the genomic region containing the single Pax6 gene in the spotted gar and those containing pax6a and -6b genes in medaka, stickleback and zebrafish"]
  [PMID:24951566 "Thus, this one-to-two relationship between the spotted gar and teleost fish matches the pattern resulting from the TSGD."]
  [PMID:24951566 "By conducting rigorous molecular phylogenetic analyses and considering conserved synteny, we demonstrate that Pax4, -6, and -10 originated in the 2R-WGD, and that the two pax6 genes of teleost fishes (pax6a and pax6b) were duplicated in the TSGD."]

(Feiner et al. call the TGD "TSGD".)

**Disputed point (for acanthopterygians, not zebrafish).** Ravi et al. accepted a TGD origin
for the zebrafish pair:
[PMID:23359656 "In zebrafish two full-length Pax6 duplicates were known previously, originating from the fish-specific genome duplication (FSGD) and expressed in divergent patterns due to paralog-specific loss of cis-elements."]
They proposed an older (2R) origin for the medaka/stickleback/fugu duplicates:
[PMID:23359656 "We show that teleosts other than zebrafish also maintain duplicate full-length Pax6 loci, but differences in gene and regulatory domain structure suggest that these Pax6 paralogs originate from a more ancient duplication event and are hence renamed as Pax6.3."]
Feiner et al. rejected that and placed all teleost pax6a/pax6b pairs in the TGD
(PMID:24951566, quoted above).

**Status.** The TGD origin of the zebrafish pair is established by synteny and gar-anchored
phylogeny. Which medaka copy corresponds to which zebrafish copy is not established.
PANTHER's `TGD_likely_parallel` call and the cross-lineage differences below both fit
lineage-specific resolution after the TGD.

## 2. Protein-level comparison

- **Identity.** 92.7% identity and 95.1% similarity over 450 alignment columns
  ([annotation-comparison.md](annotation-comparison.md)). The UniProt canonical pax6a is the
  short isoform (437 aa). The pax6b entry (450 aa) includes the exon 5a insert, so part of
  the difference is an isoform difference. The earlier cDNA comparison reported:
  [PMID:9831649 "The coding sequences of the two genes show 82% identity whereas the deduced amino acid sequences are 95% identical with complete conservation of the paired- and homeodomains."]
- **Domains.** Both copies keep the paired domain, the homeodomain and the ability to make the
  exon 5a (Pax6(5a)) isoform. The 5a exon has been lost from the pax6b copy of
  acanthopterygian fish, but not from zebrafish:
  [PMID:23359656 "This indicates that the Pax6b genes of medaka, stickleback, fugu and Tetraodon do not have the ability to encode a Pax6(+5a) isoform, while both zebrafish Pax6a and Pax6b have retained this ability."]
- **Biochemistry (tested side by side).** In a head-to-head reporter assay the two proteins
  activate targets equally well:
  [PMID:18282108 "Activation by the two wild type co-orthologues through the P3 homeodomain target [45] (Figure 1D), or the CD19 paired domain target [46] (Figure 1E), was not significantly different, in contrast to the original observations by Nornes et al [43]."]
  An earlier assay had found pax6b more active:
  [PMID:9831649 "Both Pax6.1 and Pax6.2 can act as transcriptional activators with Pax6.2 being more efficient than Pax6.1."]
  Both copies keep the eye-inducing activity of Pax6:
  [PMID:9831649 "Both Pax6.1 and Pax6.2 are able to induce ectopic eyes in Drosophila, while Pax2 is not"]
- **Authors' conclusion:**
  [PMID:18282108 "The diverged functions of the pax6 co-orthologues are unlikely to be due to coding region changes [43], although there are ∼20 amino acid differences between them, and also between each zebrafish gene and their single human orthologue."]

**Does each copy keep the ancestral molecular function?** Yes. This is established by the
side-by-side reporter assay and the Drosophila eye induction. No direct cross-rescue
(protein swap) in zebrafish has been reported.

## 3. Expression

- **Summary of both copies:**
  [PMID:18282108 "pax6b is the “minor” co-orthologue, expressed in the developing eye (retina and early lens placode), and also in thin strips of dorsal diencephalon, at the midbrain-hindbrain boundary (MHB), and in the pancreas."]
  [PMID:18282108 "pax6a is expressed in the lens and retina, as well as more widely in the developing telencephalon, diencephalon, hind brain, and spinal cord, although not in developing pancreas [49]."]
- **Pancreas: pax6b only, in embryo and adult.** pax6a is not switched on even when pax6b is
  mutant:
  [PMID:18282108 "only pax6b is expressed in the pancreas isolated from 6 month old wild type and sri/sri fish, while eyes from the same individuals express both pax6a and pax6b"]
  [PMID:18282108 "We also showed that pax6a expression is not induced in the pancreas of the sunrise mutant."]
- **Mechanism: the pancreatic enhancers diverged.**
  [PMID:18485195 "In constrast, regions A and C of the zebrafish pax6a gene are not active in the pancreas, this difference being attributable to sequence divergences within two cis-elements binding the pancreatic homeoprotein PDX1."]
  The pax6b promoter also drives enteroendocrine expression:
  [PMID:18485195 "We show that the pax6b P0 promoter targets expression to endocrine pancreatic cells and also to enteroendocrine cells, retinal neurons and the telencephalon of transgenic zebrafish."]
- **Brain: pax6a keeps more of the ancestral elements.** An ELP4-intron enhancer (E60A) is
  conserved and active only at the pax6a locus:
  [PMID:18282108 "For E60A only pax6a showed discernible conservation (Figures 5A and S8A), while pax6b (Figure S8B) has no homologous conserved sequence."]
  [PMID:18282108 "(G) No reporter expression is seen with the construct containing the E60A region from locus pax6b."]
  [PMID:18282108 "This may be the situation where several brain-specific elements, with spatiotemporal overlap in expression pattern, have been lost from pax6b."]
- **Shared domains.** Both copies are expressed in the lens epithelium, the retina and the
  diencephalon:
  [PMID:32555736 "In the WT, the lens epithelium located on the distal end expresses pax6a (E, black arrow) and pax6b (F, black arrow)."]
  [PMID:27387288 "The two zebrafish pax6 orthologues, pax6a and pax6b, are expressed in large, overlapping domains in the diencephalon [36,44] and have been implicated in aspects of diencephalon development [45]."]
  [PMID:24951566 "In adult zebrafish, pax6a, -6b, and -10a transcripts were detected in the brain, testis, and eye."]
- **The pre-duplication state.** A single-copy PAX6 acts in the eye, brain, olfactory system
  and pancreas in most vertebrates:
  [PMID:18282108 "duplicates pax6a and pax6b jointly fulfill these roles"]
  No gar pax6 expression data were found. The ancestral state is therefore inferred from
  tetrapods and from conserved non-coding elements, not measured in gar.
- **Other teleosts partitioned the elements differently.**
  [PMID:23359656 "Moreover, the conspicuous sub-partitioning of CNEs between the duplicate zebrafish Pax6a and Pax6b loci is not seen in the multiple gene loci of medaka, stickleback, Tetraodon and pufferfish"]

## 4. Experimental evidence of function

**pax6b**

- *sunrise* (L244P homeodomain missense, homozygous viable): small eye with lens and cornea
  defects.
  [PMID:18282108 "Sequencing of sri homozygotes and heterozygotes identified a leucine to proline missense mutation in a highly conserved residue of the pax6b homeodomain (Figures 1B, S1B, and S1C)."]
  [PMID:18282108 "The mild phenotype emphasizes role-sharing between the co-orthologues."]
  [PMID:25692557 "We also characterised homozygous pax6b mutants. Mutant embryos have a thick cornea, iris hypoplasia, a shallow anterior chamber and a small lens."]
- *sa0086* null allele (a premature stop codon, so the transcript may be degraded by NMD):
  loss of pancreatic endocrine cells.
  [PMID:20177065 "This pax6b mutant allele ( sa0086 ) harbors a C to A substitution changing codon 109 (Tyr) to a premature stop codon."]
  [PMID:20177065 "Pax6b-depleted embryos have almost no beta cells, a strongly reduced number of delta cells, and a significant increase of epsilon cells."]
  [PMID:32867764 "pax6b loss-of-function does not affect the total number of EECs and PECs but instead disrupts the balance between endocrine cell subtypes, leading to an increase of ghrelin- and motilin-like-expressing cells in both the intestine and pancreas at the expense of other endocrine cells such as beta and delta cells in the pancreas and pyyb-expressing cells in the intestine."]
- The eye needs the homeodomain; the pancreas does not. This is a within-copy difference
  between domains, not a difference between copies:
  [PMID:20177065 "we show that deletion of the Pax6b homeodomain in zebrafish embryos does not disturb pancreas development, whereas lens formation is strongly affected."]
- Morphants: [PMID:18282108 "First, pax6b morpholino injections, using two different morpholinos, resulted in reduced eye size, a phenotype overlapping the sri phenotype, but somewhat more severe, as total eye size reduction (Figure 3A and 3B) rather than just small lens size [27] (Figure 1A) was observed."]
- Overexpression is harmful:
  [PMID:18282108 "we show that increased dosage of wild type pax6b leads to a deleterious phenotype"]

**pax6a**

- CRISPR allele (exons 8–12 deleted, with a premature stop codon). Single mutants look near
  normal:
  [PMID:32555736 "A pax6a mutant line was created by deleting exons 8–12, the C-terminal half encoding the homeobox and proline/serine/threonine-rich (PST) domains using CRISPR/Cas9 gene editing"]
  [PMID:32555736 "In contrast to the pax6b/sunrise allele used here, the pax6a mutant allele harbours a premature termination codon, lacking the homeobox DNA binding domain and the PST-rich transactivation domain."]
- Copy-specific habenula role (pax6a morphants compared with pax6b null mutants):
  [PMID:27387288 "Homozygous pax6bsa86 mutant embryos display cxcr4b and brn3a expression in the habenulae largely indistinguishable from that of wild type siblings (Fig 2A, 2B, 2E and 2F)."]
  [PMID:27387288 "Somewhat surprisingly, on the other hand, morpholino knock-down of pax6a alone abrogated the expression of both markers (Fig 2C and 2G); pax6a morphant/pax6bsa86 mutant embryos behaved the same as pax6a morphants alone with respect to these markers (Fig 2D and 2H)."]

**Both copies**

- Double mutants: the eye phenotype resembles the mammalian Pax6-null phenotype.
  [PMID:32555736 "In concordance with mouse homozygous pax6 mutant phenotypes, zebrafish pax6a-/-;pax6b-/- double homozygous mutants showed severe defects in distal eye structures, lacking the lens, iris, corneal endothelium and ganglion cell layer of the retina."]
- The effect depends on the number of functional copies (a dosage series):
  [PMID:32555736 "In double heterozygous mutants, pax6a+/-;pax6b+/-, the 2°NC entry into the distal eye compartment was affected in nearly half of the embryos (39%, Table 1), suggesting that this pax6 gene number provides a borderline dose of Pax6 protein."]
  [PMID:32555736 "Largely, AS phenotypes of pax6a/b single and double mutants supported an overall correlation between the degree of reduced pax6a/b gene copy number and the severity of ASD (Fig 6B–6I), as observed in mouse studies [11][33]."]
- Double morphants: [PMID:18282108 "Simultaneous injection of pax6a and pax6b morpholinos disrupts eye development leading to microphthalmia and general developmental delay (data not shown)."]
- Diencephalon and hindbrain (joint knockdown only):
  [PMID:24528677 "Similar to the loss of Pax6 in mice, blockage of the function of both zebrafish homologues pax6a and pax6b by morpholino oligomers led to an expansion of the MDO shh expression domain"]
  [PMID:17010333 "Additionally, stage-matched zebrafish embryos having decreased pax6a and/or pax6b activity display malformed rhombomere boundaries and an anteriorized hoxd4a expression border."]
- Adult retinal regeneration: the copies act at different steps.
  [PMID:20152834 "Loss of Pax6b expression did not affect Müller glial cell division, but blocked the subsequent first cell division of the neuronal progenitors."]
  [PMID:20152834 "In contrast, the paralogous Pax6a protein was required for later neuronal progenitor cell divisions, which maximized the number of neuronal progenitors."]

**Compensation.** No direct evidence either way.

- A complementation role for pax6a is proposed, not shown:
  [PMID:25692557 "However, in comparison to those in mammals, homozygous mutant embryos show milder eye defects and can be grown into adulthood with full fertility, suggesting functional complementation by the other co-orthologue pax6a [6]."]
- pax6a is not upregulated in the pancreas of sunrise mutants (quoted in section 3). In the
  eye, in mutants: [PMID:32555736 "Also expression of pax6a and pax6b itself was not changed"]
  Neither result tests transcriptional adaptation to an NMD-triggering allele such as sa0086.
- Maternal transcripts are a stated caveat:
  [PMID:32555736 "Importantly, the phenotypic expression and, thus, the interpretation of the data with respect to subfunctionalization as well as gene dosage may also be hampered in addition by the presence of maternal pax6a/b mRNAs."]

## 5. Fate classification

**PARTITION (subfunctionalization), at the expression level. Confidence: high.**

**Established**

- The proteins are functionally equivalent in reporter assays (section 2).
- Pancreatic and enteroendocrine expression, and the loss-of-function phenotypes there, belong
  only to pax6b. pax6a lost its pancreatic enhancer function through divergence of PDX1 sites.
- Habenular neurogenesis requires pax6a and not pax6b.
- The ELP4-intronic brain/retina enhancer E60A survives only at the pax6a locus.
- These differences are the complementary loss of ancestral elements that the DDC model
  predicts, and the primary papers say so directly:
  [PMID:18282108 "we observed multiple examples of subfunctionalization, or job-sharing, between pax6a and pax6b."]
  [PMID:18485195 "This study also provides a striking example of how adaptative evolution of gene regulatory sequences upon gene duplication progressively leads to subfunctionalization of the paralogous gene pair."]

**Secondary: a dose-sensitive shared core in the eye (DOSAGE component)**

- In the lens, anterior segment and periocular neural crest, the copies act additively. Double
  heterozygotes already show defects (section 4).
- This is not redundancy in the backup sense. Each single mutant has an eye phenotype, and
  losing copies adds up. The authors speculated that dosage constraints shaped which elements
  were lost:
  [PMID:18282108 "It is interesting to speculate whether the coordinated loss of tissue-specific regulatory elements in duplicate pax6 loci is selected for because gene dosage needs to be maintained at the correct level."]
  That is a hypothesis, not a result.

**Not supported**

- *Innovation.* No zebrafish copy has a function absent from single-copy vertebrate PAX6.
  Pancreas, brain, habenula and eye are all ancestral PAX6 territories.
- *Pure backup.* Ruled out by the copy-specific phenotypes.

**Lineage contrast (evolutionary context).** The medaka pair appears to have resolved
differently. One copy picked up maternal and germline expression and lost its eye role:
[PMID:37094695 "Olpax6.2 knockout shows no obvious defect in eye development, while Olpax6.1 F0 mutant have severe defects in eye development."]
[PMID:37094695 "Thus, Olpax6.2 acquires maternal inheritance and germ cell expression, but functionally degenerates in the eye"]
The fate of TGD pax6 duplicates is therefore lineage-specific. The zebrafish outcome (partition)
should not be carried over to other teleosts. Which medaka copy is orthologous to which
zebrafish copy is not established (section 1).

**What would change the call**

- Evidence that pax6a or pax6b protein cannot substitute for the other when expressed from the
  other copy's locus would add a protein-level (innovation or partition) component.
- A gar expression atlas showing that single-copy pax6 is not expressed in, say, the habenula
  would reclassify that pax6a domain as a gain rather than a retained share.

## 6. GO annotation consistency across the pair

Source: [annotation-comparison.md](annotation-comparison.md), after both reviews.

**Shared, and correctly so.** Molecular function (GO:0000981, GO:0000978), nucleus, regulation
of transcription, brain, forebrain, retina and sensory organ development are accepted for both
copies. This follows from the protein-level equivalence and the shared eye, retina and brain
expression. The IBA terms treat the copies as equivalent here, and that is right.

**Asymmetric, and correctly so.**

- Pancreatic endocrine terms (GO:0003309, GO:0003310, GO:0003311, GO:0090104) and
  enteroendocrine cell differentiation (GO:0035883) belong to pax6b only.
- The IBA row for GO:0003309 was **removed from pax6a**. The PAINT node is sound for vertebrate
  Pax6, but pax6a is not expressed in the pancreas (PMID:18485195, PMID:18282108). This is the
  one place where IBA propagation treats the pair as equivalent and the biology does not.
- Habenula development (GO:0021986) was added to pax6a only (NEW, IMP PMID:27387288). The same
  paper shows that pax6b is not required for it.

**Asymmetries caused by which UniProt accession carries the annotations.** Most of the apparent
experimental gap between the copies is not biology. QuickGO shows that ZFIN's experimental pax6a
annotations sit on RefSeq-derived TrEMBL accessions (for example A0A8M3AP00), not on the
Swiss-Prot entry P26630 that this project reviews. These include IDA transcription factor
activity (PMID:18282108, PMID:9831649), IGI neural crest migration (PMID:32555736), IGI
epithalamus development (PMID:24528677), IMP A/P patterning and hindbrain (PMID:17010333) and
IMP habenula development (PMID:27387288). The pax6b entry reviewed here does carry its ZFIN
annotations. To restore the symmetry the genetic evidence supports, I added epithalamus
development and neural crest cell migration to pax6a as NEW. Both rest on evidence that
involves both copies.

The project-wide [accession audit](../../accession_audit.md) quantifies this. Nine ZFIN
experimental pax6a rows are on the RefSeq-derived entries (A0A8M9P6C7, whose sequence is
identical to P26630, and others) and are not in the pax6a review. Conversely, the IBA
annotations and UniProt's IMP rows from PMID:20152834 exist only on P26630. For pax6b, the same
three UniProt IMP rows from PMID:20152834 sit only on the legacy entry Q9YHZ8. No single
accession carries the full GOA set for either gene.

**Asymmetries from which copy a paper studied.**

- Eye, lens, cornea and lens-morphogenesis IMPs are on pax6b only, because the single-mutant
  studies used *sunrise* and sa0086. The biology is shared: double mutants lack the lens.
  pax6a keeps the general eye terms (camera-type eye morphogenesis, retina development), and I
  did not add pax6a lens terms from single-copy evidence.
- In the retinal-regeneration paper (PMID:20152834), UniProt annotated only pax6a:
  - the rod differentiation IMP was **removed**, because the paper shows rods are not
    Pax6-dependent;
  - the cone differentiation IMP was marked as over-annotated, because the pax6a effect was
    not significant;
  - the proliferation IMP was modified to GO:2000179 (positive regulation of neural precursor
    cell proliferation);
  - the matching GO:2000179 was added to pax6b as NEW.

**Should be copy-specific:** pancreatic and enteroendocrine differentiation (pax6b) and
habenula development (pax6a).

**Should be shared:** transcription factor activity; eye, retina, lens and anterior segment
development; neural crest guidance; epithalamus and hindbrain patterning.

## 7. Open questions

- Would a coding-sequence swap between the two loci rescue each single mutant? This is the
  missing test of protein equivalence in vivo.
- Does pax6a expression rise in pax6b sa0086 (PTC) eyes, as expected under transcriptional
  adaptation? No RNA-less allele has been compared.
- What does single-copy spotted gar pax6 express, in pancreas, habenula and brain? That would
  anchor the ancestral state directly.
- Should ZFIN pax6a annotations be mapped to Swiss-Prot P26630 in GOA? This is a data-pipeline
  question.

## References

PMID:9831649, PMID:17010333, PMID:18282108, PMID:18485195, PMID:20152834, PMID:20177065,
PMID:23359656, PMID:24528677, PMID:24951566, PMID:25692557, PMID:27387288, PMID:32555736,
PMID:32867764, PMID:37094695. Also the files `panther_tgd_pairs.tsv` and
[annotation-comparison.md](annotation-comparison.md).
