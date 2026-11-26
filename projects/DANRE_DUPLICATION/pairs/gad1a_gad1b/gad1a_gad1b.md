---
title: "gad1a / gad1b"
autolink_gene_symbols: false
---

# gad1a / gad1b

[Back to pairs](../README.md)

**Bottom line:** UNRESOLVED. The two GAD1 (GAD67) co-orthologs encode the same enzyme: every catalytic residue
checked is kept in both and neither copy evolves significantly faster. They differ strongly in expression level:
gad1b is the pan-GABAergic copy, about 20-fold more abundant than gad1a in whole larvae. gad1a is weakly expressed,
and it is not known where; published in situ data labelled gad1a may come from a gad1b-derived probe. Only gad1b
has been knocked out (null mutants show seizure-like brain activity). No gad1a or double mutant exists, so backup,
partition and slow loss of gad1a cannot be told apart.

**Sample record:** fate=UNRESOLVED; level=expression; evidence=experimental_one; identity=86.3%

| | gad1a | gad1b |
|---|---|---|
| UniProt | A0A8M1RDR2 (TrEMBL, 591 aa) | Q7ZUS3 (TrEMBL, 587 aa) |
| Human ortholog | GAD1 (GAD67) | GAD1 (GAD67) |
| Chromosome | 9 | 6 |
| ZFIN | ZDB-GENE-070912-472 | ZDB-GENE-030909-3 (formerly gad1, gad67) |
| Mutant alleles | none | gav2303 (CRISPR, 10-bp deletion in exon 4, reported null) |
| Review | [genes/DANRE/gad1a](../../../../genes/DANRE/gad1a/gad1a-ai-review.yaml) | [genes/DANRE/gad1b](../../../../genes/DANRE/gad1b/gad1b-ai-review.yaml) |

## 1. Evidence the pair comes from the TGD

**PANTHER.** The row in `panther_tgd_pairs.tsv` is:

| tgd_call | branch | class | family | human orthologs (a / b) | gar co-orthologs | medaka co-orthologs | medaka parallel dup |
|---|---|---|---|---|---|---|---|
| TGD_tree | Neopterygii\|Teleostei | 1:1 | PTHR45677 (GLUTAMATE DECARBOXYLASE-RELATED) | GAD1(LDO) / GAD1(O) | 1 (same gar gene for both) | 2 | (blank) |

PANTHER places the duplication after the gar split and before the zebrafish-medaka split.

**Ensembl Compara.** The duplication node is Clupeocephala (as listed in `random_sample.tsv`), and both copies have
the same one-to-many gar ortholog. Ensembl gives a one-to-one medaka ortholog for gad1a only, while PANTHER counts
two medaka co-orthologs, so retention of both copies in medaka is not settled
([RESULTS.md](../../../../genes/DANRE/gad1a/gad1a-bioinformatics/RESULTS.md)).

**Literature.** No phylogenetic or synteny study of the pair exists. Papers on the gene note that other fish also
have two copies:
[PMID:30200754 "Other fish species have two gad1 genes, designated as gad1a and gad1b, and a single gad2 gene."]
[PMID:30200754 "In zebrafish, gad1a is located on chromosome 9, gad1b on chromosome 6, and gad2 on chromosome 24 (VanLeuven,"]

**My check.** Two neighbouring gene pairs that Compara also dates to a teleost-level duplication flank both copies:
tlk1a and dync1i2a lie within 0.5 Mb of gad1a on chr9, and tlk1b and dync1i2b within 110 kb of gad1b on chr6. A
further 8 teleost-level paralogue pairs link the gad1a region to chr6, and 5 link the gad1b region to chr9
([RESULTS.md](../../../../genes/DANRE/gad1a/gad1a-bioinformatics/RESULTS.md)). This fits ohnologous chromosome
segments.

**Status.** TGD origin is supported by the PANTHER tree call, a Clupeocephala Compara node with a single gar
ortholog, and conserved flanking paralogues. It is not backed by a published gene tree.

## 2. Protein-level comparison

- **Identity.** 86.3% identity and 93.9% similarity over 592 columns
  ([annotation-comparison.md](annotation-comparison.md)). Against human GAD1: gad1a 80.0%, gad1b 82.7%; against gar
  GAD1: 85.5% and 87.8% ([RESULTS.md](../../../../genes/DANRE/gad1a/gad1a-bioinformatics/RESULTS.md)).
- **Catalytic residues.** Both copies keep the PLP-binding lysine (human K405, in an identical
  RANSVTWNPHKMMGV motif), the annotated GABA-binding residues and the C-terminus. The only annotated human point
  feature that differs is phospho-S78 in the variable N-terminal region, a threonine in every gad1a translation.
- **Rate.** Against the gar ortholog, 37 changes are unique to gad1a and 23 to gad1b (chi2 = 3.27, not
  significant). gad1a is also further from human in the N-terminal region (58.9% identical over residues 1-95,
  vs 65.3% for gad1b and 80.0% for gar). In mammals this region differs between GAD1 and GAD2 and
  affects where the enzyme sits in the cell.
- **Biochemistry.** Neither zebrafish enzyme has been assayed, and no Gad1a antibody exists:
  [PMID:30200754 "Nevetheless, this cannot be directly tested at this time, because an antibody specific to Gad1a has yet to be identified."]
  Mammalian GAD1 is the constitutive GABA-synthesizing isoform:
  [PMID:17384644 "GAD67 is constitutively active and is responsible for basal GABA production."]

**Does each copy keep the ancestral molecular function?** Probably yes for both. The inference rests on conserved
catalytic residues, not on assays.

## 3. Expression

**Which probe is which?** Older papers call gad1b "GAD67", "gad67" or "gad1". I checked the first zebrafish GAD67
cDNA (Martin et al. 1998, GenBank AF017266) against both copies. Its translation is 99.6% identical to Gad1b and 90.9%
to Gad1a, so it is gad1b ([RESULTS.md](../../../../genes/DANRE/gad1a/gad1a-bioinformatics/RESULTS.md)). Another
lab also assigns the old probes to gad1b:
[PMID:26896392 "A mixture of two probes to gad1b (previously called gad67, probes used to be called gad67a and gad67b) and one probe to gad2 (previously called gad65) was used to label GABAergic cells [61, 62]."]
The one published in situ comparison of the two copies uses a "gad1a" probe that the authors trace to the same
Martin plasmid:
[PMID:35769333 "For two-color RNA ISH, a gad1a (previously gad67a) containing plasmid (Martin et al., 1998) was linearized"]
If that plasmid is the AF017266 clone, the "gad1a" signal is gad1b. The probe sequence is not given, so this cannot be
settled from the papers.

- **gad1b: pan-GABAergic.** In the embryo, expression coincides with GABA:
  [PMID:9634146 "Immunohistochemistry for gamma-aminobutyric acid (GABA) revealed that GABA is produced at all sites of GAD expression, including the novel cells in the caudal hindbrain."]
  It is used as the pan-GABAergic larval marker:
  [PMID:42466317 "At 5 dpf, as shown previously, gad1b expression occupies all regions of the larval brain (Figure 4A)."]
  ZFIN holds 247 curated gad1b expression records from 69 publications (forebrain, midbrain, hindbrain, spinal
  cord, retina).
- **gad1a: low and poorly mapped.** In the whole-embryo time course (E-ERAD-475), gad1b climbs to 84 TPM by day 5,
  while gad1a stays at 0.4-4 TPM, apart from one 5 TPM value at the 2-cell stage. Bgee has 8 RNA-seq calls for gad1a:
  brain, liver, early embryo, blastula, gastrula, larva, head and bone. The liver and early-embryo calls have no
  gad1b counterpart. ZFIN's gad1a brain records come from the Lueffe et al. papers, which carry the probe caveat
  ([RESULTS.md](../../../../genes/DANRE/gad1a/gad1a-bioinformatics/RESULTS.md)).
- **A cell type with gad1b only.** Single-cell RNA-seq of lateral-line efferent neurons:
  [PMID:41950195 "Efferent neurons showed robust expression of gad2 and gad1b (but not gad1a [Fig 4B]), encoding for enzymes required for the synthesis of GABA [35,36]."]
- **The copies respond differently to mutations** (qPCR, paralog-specific primers):
  [PMID:35769333 "In grm8a–/– animals a significant reduction of gad1a transcript level was detected, whereas gad1b and gad2 were unchanged (Supplementary Figure 5A)."]
  [PMID:34650032 "Motivated by our qPCR results, showing a significant reduction in the amount of gad1b transcript in foxp2+/− and a tendency to higher gad1a and gad2 transcript levels in foxp2+/− and foxp2−/− (Fig."]
- **Claims of similar patterns are weak.**
  [PMID:34650032 "Since the expression pattern of both GAD1 paralogs, gad1a and gad1b, are highly similar (Supplementary Fig. 3A–L), we decided for gad1a as GABAergic marker due to technical reasons."]
  This rests on the probe discussed above. A 2026 paper states the same thing but cites a study that examined gad1b
  and gad2, not gad1a:
  [PMID:42466317 "Immunohistochemistry studies in several species have shown largely overlapping expression of gad1a and gad1b in the developing brain, including studies of the zebrafish brain at 4 dpf (Filippi et al., 2014)."]
- **Pre-duplication state.** Gar GAD1 has Bgee RNA-seq calls in brain (96.2), eye (96.0), larva, bone, ovary, muscle,
  embryo and testis. There is no gar data at cellular resolution. Mammalian GAD1 is neural, with minor non-neural
  sites.

**Summary.** gad1b carries the ancestral pan-GABAergic neural expression. gad1a is a low-level copy whose cellular
domains are unknown. Its liver, early-embryo and grm8a-sensitive expression hint at some regulatory divergence, but
none of this has been mapped with a verified probe.

## 4. Experimental evidence of function

**Alleles and knockdowns**

| Gene | Reagent | Lesion | Type | Source |
|---|---|---|---|---|
| gad1b | gav2303 | CRISPR 10-bp deletion, exon 4 | frameshift/PTC (reported functional null); mRNA decay not reported | PMID:30200754 |
| gad1b | translation-blocking MO (and photoactivatable version) | 25/25 match to gad1b, 19/25 to gad1a | knockdown | PMID:30200754 |
| gad1b | splice MO (intron 8 retention) | premature stop | knockdown | PMID:34650032 |
| gad1a | none | | | |

**gad1b**

- Null mutant with abnormal brain activity resembling PTZ-induced seizures:
  [PMID:30200754 "The gad1bgav2303/gav2303 allele used in these studies harbored a 10 bp deletion in exon 4 and was a functional null mutation."]
  [PMID:30200754 "The electrophysiological traces of the cMO morphants were comparable to those obtained from larvae null for gad1b and wild-type fish exposed to PTZ, which causes seizures in zebrafish."]
- The morphant has craniofacial defects that the mutant lacks:
  [PMID:30200754 "The craniofacial phenotype in gad1b morphants is surprising because genetic knockouts of gad1b do not cause craniofacial defects"]
  The authors suggest the MO may also hit gad1a, but consider it unlikely:
  [PMID:30200754 "MO used in our study has only 8 consecutive bases complementary to gad1a, so it seems unlikely that the gad1b translation blocking MO used here would also block translation of gad1a."]
- A splice morphant raises locomotor activity:
  [PMID:34650032 "Firstly, interference with gad1b, Gad or GABA-A-Rs results in an increased locomotor activity similar to what we find after foxp2 impairment, thus we demonstrate that GABAergic signalling influences locomotor activity in zebrafish."]
- The full mutant characterization was "submitted" in 2019. A 2024 preprint on reduced GABA levels in the tectum
  has no PMID and was not used.

**gad1a.** No mutant, morphant or assay.

**Both copies.** No double mutant, and no cross-rescue. Whether gad1a is upregulated in gad1b mutants
(transcriptional adaptation) has not been measured. The authors predict what a double mutant would show:
[PMID:30200754 "If this is the case, we hypothesize that zebrafish embryos null for gad1a and gad1b will exhibit the craniofacially defective phenotype."]

## 5. Fate classification

**UNRESOLVED. Level: expression (a large difference in expression level; the protein is conserved). Confidence in
the facts: moderate. The fate itself cannot be called.**

**Established**

- Both proteins keep the catalytic machinery. There is no sign of protein-level divergence beyond a more divergent
  N-terminal region in gad1a; the overall rate difference is not significant.
- gad1b is the dominant, pan-GABAergic copy. Its loss alone disturbs brain activity, so gad1a does not fully
  compensate.
- gad1a is expressed at a much lower level, and is absent from at least one gad1b-positive neuron type.

**Consistent with, but not shown**

- *Dosage-asymmetric backup or decay of gad1a:* a weakly expressed copy that keeps the enzyme but contributes
  little GABA.
- *Partition:* gad1a could keep a small ancestral domain that gad1b lost (the RNA-seq liver and early-embryo calls,
  or specific neurons). No such domain has been mapped with a verified probe, and the gar data have no cellular
  resolution.

**Why not the others**

- *Innovation:* no new protein feature and no new expression domain has been shown.
- *Backup (redundancy) as a positive call:* the gad1b single mutant already has a phenotype, and nothing has tested
  whether gad1a adds to it.

**What would change the call**

- A gad1a mutant, and a gad1a;gad1b double mutant with brain GABA measured. A worse double than gad1b alone would
  mean backup or dosage; a distinct gad1a-only phenotype would mean partition.
- HCR in situ or single-cell data with sequence-verified gad1a probes, plus gar GAD1 in situ, to map gad1a domains
  against the ancestral pattern.

## 6. GO annotation consistency across the pair

Source: [annotation-comparison.md](annotation-comparison.md), after both reviews.

**Shared, and correctly so.** Glutamate decarboxylase activity (IBA), carboxy-lyase and carbon-carbon lyase
activity, PLP binding, GABA biosynthetic process (IBA) and cytoplasm (IBA) are on both copies and were accepted on
both. They follow from the conserved enzyme.

**Presynaptic active zone (IBA)** is on both copies, seeded by rodent Gad1. It is kept as non-core on both. ZFIN has
Gad1b antibody staining at cerebellar presynaptic sites (Bae et al. 2009; not read beyond the abstract), and there
are no Gad1a localization data.

**Asymmetries that come from which copy was studied.**

- gad1b has the only experimental row: IEP for GABA biosynthetic process from Martin et al. 1998. The GAD67 cDNA of
  that paper is gad1b by sequence, so the row is on the right paralog. It was accepted.
- gad1b is the donor for the IBA GABA biosynthetic process row that both copies receive (ZFIN:ZDB-GENE-030909-3 in
  the WITH/FROM field). This is expected, not circular.
- gad1a has an extra IEA row for glutamate decarboxylase activity from the EC mapping of its UniProt name. gad1b's
  TrEMBL entry is named "GAD67" and has no EC number. This is a bookkeeping difference, not biology.

**Should be copy-specific:** nothing at present. The loss-of-function phenotypes of gad1b (seizure-like activity,
locomotion) are consequences of GABA deficiency and were not added as process terms to either copy.
**Should be shared:** the enzyme activity, GABA biosynthesis and cytoplasmic location, as now.

## 7. Open questions

- Is gad1a translated into active enzyme, and in which cells?
- Which "gad1a" probes in the literature are really gad1a? The Lueffe et al. probe needs to be sequenced.
- Does gad1a rise in gad1b mutants, and what does a double mutant look like?
- Are the RNA-seq signals of gad1a in liver and cleavage-stage embryos real, and does gar GAD1 show them?
- Did medaka keep both copies (Ensembl and PANTHER disagree)?

## References

PMID:9634146, PMID:17384644, PMID:26896392, PMID:30200754, PMID:34650032, PMID:35769333, PMID:41950195,
PMID:42466317. Also `panther_tgd_pairs.tsv`, `random_sample.tsv`, [annotation-comparison.md](annotation-comparison.md),
[gad1a-bioinformatics/RESULTS.md](../../../../genes/DANRE/gad1a/gad1a-bioinformatics/RESULTS.md),
[output.txt](../../../../genes/DANRE/gad1a/gad1a-bioinformatics/output.txt) and
[probe_identity_output.txt](../../../../genes/DANRE/gad1a/gad1a-bioinformatics/probe_identity_output.txt).
