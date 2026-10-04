---
title: "smad3a / smad3b"
autolink_gene_symbols: false
---

# smad3a / smad3b

[Back to pairs](../README.md)

**Bottom line:** BACKUP, provisional and low confidence. The two SMAD3 proteins are 94%
identical and keep every annotated functional residue except one (S418N in smad3b). They act
the same way, with different strengths, in every side-by-side assay: a Smad3 reporter,
constitutively active forms in the heart, and knockdown effects on neural differentiation.
Both are maternal and broadly expressed. The group that made the mutants says both copies had to
be knocked out to get an aortic phenotype. The double knockout enlarges the ventral aorta and still
survives to adulthood. The single-mutant data are not in any accessible text, so redundancy is
stated rather than shown. smad3a has one regulatory difference with no known consequence: its
expression is circadian and controlled by Clock1a.

**Sample record:** fate=BACKUP; level=both; evidence=experimental_both; identity=94.1%

| | smad3a | smad3b |
|---|---|---|
| UniProt | Q8AY15 (TrEMBL, 425 aa) | Q8AY16 (TrEMBL, 423 aa) |
| Human ortholog | SMAD3 | SMAD3 |
| Chromosome (Ensembl) | 7 | 18 |
| ZFIN | ZDB-GENE-000509-3 | ZDB-GENE-030128-4 |
| GOA rows | 31 (10 experimental, 3 TAS) | 19 (1 experimental) |
| Review | [genes/DANRE/smad3a](../../../../genes/DANRE/smad3a/smad3a-ai-review.yaml) | [genes/DANRE/smad3b](../../../../genes/DANRE/smad3b/smad3b-ai-review.yaml) |

Drawn at random (draw 6, seed 20260928) from the 778 clean 1:1 `TGD_tree` pairs
(`batch3_sample.tsv`).

## 1. Evidence the pair comes from the TGD

**PANTHER.** The row in `panther_tgd_pairs.tsv` is:

| tgd_call | branch | class | family | human orthologs (a / b) | gar co-orthologs | medaka co-orthologs | medaka parallel dup |
|---|---|---|---|---|---|---|---|
| TGD_tree | Neopterygii\|Teleostei | 1:1 | PTHR13703 (SMAD) | SMAD3(LDO) / SMAD3(O) | 1 (same gar gene for both) | 2 | (blank) |

**Literature.** A synteny and phylogeny study of teleost SMAD3 genes independently supports a
TGD origin:
[PMID:27703851 "confirmed that smad3a/3b most likely originated from the teleost-specific WGD"]
[PMID:27703851 "Teleost SMAD3 genes could be clearly divided into two well-conserved clusters, i.e., smad3a and smad3b, whereas spotted gar SMAD3 occupied a separate clade."]
[PMID:27703851 "According to the chromosomal synteny dot plot (Fig. 5), the human SMAD3 region showed double conserved synteny with green spotted puffer chromosomes Tni5 and Tni13."]

**Status.** TGD origin is established: the PANTHER tree places the duplication on the TGD
branch, and the published trees and double-conserved synteny agree. That paper also calls
smad3b "more likely" the ancestral gene, because its neighbourhood keeps more of the flanking gene
order. That is a statement about local synteny; after a whole-genome duplication neither copy is
older. I did not check which zebrafish copy matches which medaka copy.

## 2. Protein-level comparison

Source: [annotation-comparison.md](annotation-comparison.md) and
[smad3a-bioinformatics/RESULTS.md](../../../../genes/DANRE/smad3a/smad3a-bioinformatics/RESULTS.md).

- **Identity.** 94.1% between the paralogs (97.9% similarity). smad3a is 96.9% identical to
  human SMAD3 and 96.3% to gar SMAD3 (W5N932). smad3b is 93.0% and 93.9%.
- **Where the differences are.** Between the paralogs, 94.5% of MH1 positions, 98.5% of MH2
  positions and 84.2% of linker positions are identical. smad3b carries most of the change: its
  linker is 82.3% identical to human, against 92.7% for smad3a, and it has a 2-residue linker
  deletion. This fits the published trees:
  [PMID:27703851 "Moreover, the branch length of smad3b cluster was longer than smad3a"]
  [PMID:27703851 "Five candidate positive selected sites were identified, two of which were significantly positively selected (219L**, 221L**, posterior probability > 0.99) in smad3b."]
  These positively selected sites were found in flounder numbering. I did not map them to zebrafish.
- **Functional residues.** Both copies keep the MH1 Zn-binding residues (C64, C109, C121,
  H126), K40 and K41, the linker phosphosites T8, T179, S204, S208 and S213, K378, S416 and the
  receptor-phosphorylated C-terminal SSVS (RCSSVS in both copies and in gar). The one annotated
  difference is **S418**, a CK1 phosphosite in human, which is **N in smad3b**. Its effect is
  untested.
- **Side-by-side functional comparisons.**
  - A Smad3 reporter responds to both proteins:
    [PMID:25286120 "Reporter fluorescence is activated in phospho-Smad3 positive cells and is responsive to both Smad3 isoforms, Smad3a and 3b."]
  - Constitutively active forms of both raise cardiomyocyte proliferation and Smad3 target genes,
    Smad3a more strongly:
    [PMID:29196619 "whereas both caSmad3a and caSmad3b expression resulted in a 70% (±18% s.e.m.) and 31% (±12% s.e.m.) increase in EdU incorporation, respectively"]
    [PMID:29196619 "an upregulation in Smad3 target gene expression in caSmad3a and caSmad3b hearts"]
  - On the myf5 promoter, overexpressed Smad3a is active and Smad3b is not:
    [PMID:21159776 "Using a luciferase assay to detect myf5 promoter activity when smad2 , smad3a , smad3b , or smad4 mRNAs were overexpressed, we found that excessive smad2 and smad3a showed enhanced myf5 promoter activity but not excessive smad3b or smad4 mRNA."]
    [PMID:21159776 "However, the proportion of defects that could be attributed to DN-Smad2 and DN-Smad3a was higher than the proportion of defects attributed to DN-Smad3b."]
  - Overexpressed Smad3b induces mesoderm and organizer genes:
    [PMID:12112463 "We show that zebrafish Smad3b, in contrast to the related zebrafish Smad2, can induce mesoderm independently of TGF-beta signaling."]
  - Dominant-negative forms of each copy block nodal-induced mesendoderm:
    [PMID:18025082 "We generated potent and specific dominant-negative forms of zebrafish Smad2, Smad3a, and Smad3b by mutating multiple amino acids."]
    [PMID:18025082 "Overexpression of these mutants abolished mesendoderm induction by ectopic Nodal signaling in zebrafish embryos."]

**Does each copy keep the ancestral molecular function?** Yes. Both are receptor-regulated SMAD
transcription factors that activate SMAD-responsive transcription. The quantitative differences
(myf5 promoter; about twofold in cardiomyocyte proliferation) come from overexpression at chosen
doses. They could reflect the diverged smad3b linker, or only differences in mRNA dose and
stability. No equal-protein comparison has been made.

## 3. Expression

- **Both maternal and broadly expressed early.**
  [PMID:28687631 "First, we showed that the smad3a gene is maternally expressed, and its transcripts are ubiquitously distributed during early embryonic development"]
  ZFIN has smad3b in situ rows at the 4-cell and sphere stages (from PMID:12112463; see
  `output.txt`).
- **Somitogenesis.** Both are broad. smad3a is stronger in new somites, and smad3b in eyes and tail:
  [PMID:21159776 "Although smad genes were expressed in most cells, we found that smad3a and smad4 expressions were stronger in the newly formed somites where myf5 was highly expressed."]
  [PMID:21159776 "smad3b expressed in the whole embryonic body but with stronger expression in eyes and tail ( supplemental Fig."]
- **Circadian regulation of smad3a only.**
  [PMID:29940038 "In contrast to Smad3a, another zebrafish paralog of Smad3, Smad3b, did not show any time- or light-dependent expression pattern"]
  [PMID:28687631 "Mechanistically, Clock1a activates the smad3a promoter via its E-box1 element (CAGATG)."]
- **Bgee and ZFIN** (RESULTS.md). 19 anatomical entities are shared. smad3a scores highest in
  presomitic and paraxial mesoderm, somite, caudal fin and retina. smad3b scores highest in heart,
  muscle, gill, eye and liver. The smad3b-only brain subregions all come from one in situ study
  of smad3b (PMID:12112463). smad3a has had no study at that resolution, so these domains are not
  evidence of a partition.
- **Adult heart.** smad3a is induced after ventricle ablation:
  [PMID:33816481 "Similarly, the gene expressions of TGF-β receptors alk5a, alk5b, and cofactor smad3a were also dramatically upregulated in the ablated hearts (Figures 1E–G′)."]
  smad3b was not reported in that experiment.
- **Another teleost.** In adult flounder both copies are expressed in every organ tested, at
  different levels:
  [PMID:27703851 "The smad3a and smad3b genes were expressed in all organs with different expression levels in specific organs."]
- **Pre-duplication state.** I found no gar SMAD3 expression data. Mammalian SMAD3 is broadly
  expressed, which fits the broad overlap seen here.

The picture is overlap with quantitative biases, plus one regulatory input (the clock) that only
smad3a has. No domain has been shown to express one copy and lack the other.

## 4. Experimental evidence of function

**Alleles and reagents**

| Gene | Reagent | Type | Source |
|---|---|---|---|
| smad3a + smad3b | CRISPR double knockout (smad3a/b DKO); also combined with smad6a/b | loss of function; allele details and mRNA-decay status not in the abstract | PMID:42584512 |
| smad3a, smad3b | morpholino knockdown of each | knockdown | PMID:25286120 |
| smad3a, smad3b | dominant-negative (P-to-H plus C-terminal S-to-A) | blocks Smad2/3 signalling generally | PMID:18025082, PMID:21159776 |
| smad3a, smad3b | constitutively active (phosphomimetic), myl7 promoter | gain of function | PMID:29196619 |
| smad3a | mRNA rescue of clock1a morphants | gain of function | PMID:28687631 |

**Loss of function**

- Each knockdown affects neural differentiation in the same direction:
  [PMID:25286120 "Similarly, smad3a and 3b knock-down alter neural differentiation showing that both paralogues play a positive role in neural differentiation."]
- The double knockout has an aortic phenotype and survives:
  [PMID:42584512 "We found an increased diameter of the ventral aorta in smad3a-/-;smad3b-/- double knockout (smad3a/b DKO) zebrafish larvae"]
  [PMID:42584512 "Smad3a/b DKO survive normally to adulthood"]
  [PMID:42584512 "Surprisingly, the smad3a-/-;smad3b-/-;smad6a-/-;smad6b-/- quadruple knockout (qKO) zebrafish model has normal survival and a milder vascular phenotype compared to the smad6a/b DKO."]
- The same group explains the double targeting by redundancy:
  [PMID:40066353 "To be able to study the function of SMAD3 and SMAD6 in zebrafish, both the smad3a and smad3b as well as the smad6a and smad6b ohnologs, which are the result of the whole genome duplication which occurred in the common ancestor of the teleost fish lineage (40), needed to be targeted due to their respective redundancy."]
  [PMID:40066353 "Since many of the zebrafish ohnologues have redundant functionality, they would need to both be targeted to elicit the desired phenotype in zebrafish, as we experienced for the smad3a/b and smad6a/b genes."]
  The single-mutant data behind this are not in the cached texts. PMID:42584512 is abstract-only
  and PMID:40066353 is a review.

**Gain of function and rescue**

- smad3a mRNA restores mesoderm and scl markers in clock1a morphants:
  [PMID:28687631 "These effects were largely compromised by co-injection of smad3a- mRNA."]
  smad3b was not tested in that assay.

**Dominant-negative data.** These block Smad2/3 signalling in general, so they do not separate
the copies. Many papers use dnSmad3b or caSmad3b as a generic TGF-beta/Smad2/3 tool
(PMID:19580801, PMID:31624259, PMID:39690179).

**Compensation.** No study reports whether either copy is upregulated in the other's mutant.

## 5. Fate classification

**BACKUP, at the level of both expression and protein. Confidence: low.**

**Established**

- TGD origin (section 1).
- Both proteins keep the SMAD3 molecular function, with the same effects in reporter,
  constitutively-active and knockdown assays (section 2, section 4).
- The two copies are broadly co-expressed and both are maternal (section 3).
- Losing both copies gives an aortic phenotype. The fish survive, as Smad3-null mice do.

**Inferred, not shown**

- That the single mutants lack the aortic phenotype, which is what "redundancy" means here.
  This is the authors' stated experience. The data are not in any accessible text.
- That the quantitative differences (myf5, cardiomyocyte proliferation) reflect protein
  divergence. They could come from dose.

**Why not the other fates**

- *Partition.* No domain or process has been shown to need one copy and not the other. The
  smad3a-only circadian regulation is a regulatory divergence. No phenotype has been tied to it.
- *Innovation.* Smad3b's induction of mesoderm and organizer genes is an overexpression
  property, and the authors contrast it with Smad2 and with mammalian Smad3 in explant assays.
  No loss-of-function evidence shows a new role for either copy.
- *Dosage.* No intermediate genotypes (for example smad3a-/-;smad3b+/-) are reported, so a dose
  effect cannot be judged.

**What would change the call**

- Single mutants with a phenotype that the other copy cannot rescue would mean PARTITION.
- Intermediate phenotypes in one-copy-plus-heterozygote genotypes would mean DOSAGE.
- An equal-dose cross-rescue showing Smad3b cannot replace Smad3a (for example at myf5) would add
  a protein-level component (MIXED).

## 6. GO annotation consistency across the pair

Source: [annotation-comparison.md](annotation-comparison.md), after both reviews.

**Shared, and correctly so.** Every IBA and IEA row is present on both copies and was reviewed
the same way:

- Accepted: DNA-binding transcription factor activity, cis-regulatory DNA binding, I-SMAD binding,
  heteromeric SMAD complex, nucleus and cytoplasm, TGF-beta, activin and SMAD signal transduction,
  and positive regulation of transcription.
- Kept as non-core: anatomical structure morphogenesis, cell differentiation and embryonic pattern
  specification.
- Marked as over-annotated on both: BMP signaling pathway and dorsal/ventral pattern formation.
  Both come from family-wide ARBA rules that suit BMP-pathway SMADs. SMAD3 is a
  TGF-beta/activin/nodal R-SMAD, and the zebrafish Smad3 reporter is blocked by ALK4/5 inhibitors.

Same-node IBA propagation is right for this pair: the proteins are conserved and behave alike.
The generic protein-binding IPI (Tob1a, PMID:16890162) sits on both copies and was removed from
both as uninformative.

**Asymmetric only because of which copy was studied.** The following are on smad3a only:

- nodal signaling pathway (TAS);
- endodermal and mesodermal cell fate specification (IMP);
- mesoderm development and primitive hemopoiesis (IGI with clock1a);
- sequence-specific DNA binding (IPI, ChIP at myf5);
- the TGF-beta receptor signaling IMP.

The Eaf1/2 rows (PMID:28887217) are abstract-only here. Two of them carry the eaf1 morpholino in
WITH, so I deferred to the curator and kept the cell-fate terms as non-core. None of these
reflects a smad3a-specific biology that smad3b lacks, except that the Clock1a link was shown for
smad3a alone.

**Should be shared:** the R-SMAD molecular function and complex, TGF-beta/activin/nodal
signalling, and mesendoderm induction. Nodal signaling pathway is missing from smad3b. The
dominant-negative data that would support it do not separate Smad2/3 family members, so I did not
add it as NEW. The activin receptor signaling IBA already covers the branch on both copies.

**Should be copy-specific:** nothing is established. If the Clock1a input to smad3a turns out to
matter, it would be a regulatory, not a GO molecular-function, difference.

## 7. Open questions

- What are the single-mutant phenotypes of smad3a and smad3b? Are the alleles PTC alleles with
  mRNA decay, which could trigger transcriptional adaptation of the paralog?
- Do smad3a-/-;smad3b+/- and smad3a+/-;smad3b-/- fish have intermediate aortic diameters (dosage)?
- Does the smad3b linker (S418N, positive-selection sites) change phosphoregulation or
  transcriptional strength at equal protein dose?
- Does the circadian expression of smad3a matter in any tissue? For example, could it be the
  pineal/clock output that smad3b cannot provide?
- Is gar SMAD3 expressed in the same tissues as the union of the two zebrafish copies?

## References

PMID:10767528, PMID:12112463, PMID:16890162, PMID:18025082, PMID:19580801, PMID:21159776,
PMID:25286120, PMID:27703851, PMID:28687631, PMID:28887217, PMID:29196619, PMID:29940038,
PMID:31624259, PMID:33816481, PMID:39690179, PMID:40066353, PMID:42584512. Also the files
`panther_tgd_pairs.tsv`, `batch3_sample.tsv`, [annotation-comparison.md](annotation-comparison.md)
and [smad3a-bioinformatics/RESULTS.md](../../../../genes/DANRE/smad3a/smad3a-bioinformatics/RESULTS.md).
