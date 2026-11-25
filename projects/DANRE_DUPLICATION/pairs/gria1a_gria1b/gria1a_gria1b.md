---
title: "gria1a / gria1b"
autolink_gene_symbols: false
---

# gria1a / gria1b

[Back to pairs](../README.md)

**Bottom line:** UNRESOLVED, with divergence at both levels but no functional test. Both GluA1 co-orthologs keep an
intact ligand-binding site and channel pore, and they are expressed in largely the same neuronal populations.
gria1a is the conserved copy, about 2-3 times more abundant in larvae, with some domains of its own (telencephalon,
spinal cord). gria1b has evolved significantly faster since the duplication, as has its medaka ortholog. Its
cytoplasmic tail lacks serines matching the mammalian regulatory phosphorylation sites. It has an otic vesicle
domain and non-neural RNA-seq signal. No experiment separates the copies, so partition, innovation in gria1b and
relaxed constraint on a backup copy all remain possible.

**Sample record:** fate=UNRESOLVED; level=both; evidence=expression_only; identity=82.5%

| | gria1a | gria1b |
|---|---|---|
| UniProt | Q71E65 (TrEMBL, 914 aa) | E7F1V8 (TrEMBL, 917 aa) |
| Human ortholog | GRIA1 (GluA1) | GRIA1 (GluA1) |
| Chromosome | 14 | 21 |
| ZFIN | ZDB-GENE-020125-1 | ZDB-GENE-020125-2 |
| Mutant alleles | CRISPR alleles from a screen that also mutated gria1b (details not in text) | as for gria1a |
| Review | [genes/DANRE/gria1a](../../../../genes/DANRE/gria1a/gria1a-ai-review.yaml) | [genes/DANRE/gria1b](../../../../genes/DANRE/gria1b/gria1b-ai-review.yaml) |

## 1. Evidence the pair comes from the TGD

**PANTHER.** The row in `panther_tgd_pairs.tsv` is:

| tgd_call | branch | class | family | human orthologs (a / b) | gar co-orthologs | medaka co-orthologs | medaka parallel dup |
|---|---|---|---|---|---|---|---|
| TGD_tree | Neopterygii\|Teleostei | 1:1 | PTHR18966 (IONOTROPIC GLUTAMATE RECEPTOR) | GRIA1(LDO) / GRIA1(O) | 1 (same gar gene for both) | 2 | (blank) |

**Ensembl Compara.** The duplication node is Osteoglossocephalai (as listed in `random_sample.tsv`), with one gar
ortholog for both copies. Medaka has a one-to-one ortholog of each copy, so both were kept in the two lineages
([RESULTS.md](../../../../genes/DANRE/gria1a/gria1a-bioinformatics/RESULTS.md)).

**Literature.** The survey of all zebrafish AMPA receptor genes treats the a/b pairs as duplicates:
[PMID:18224707 "Whereas mammals have four subunit genes, Gria1-4, zebrafish has retained a duplicated set of eight genes named gria1-4a and b."]
No gene tree or synteny study of the gria1 pair has been published.

**My check.** No teleost-level paralogue pair lies within 1.5 Mb of both copies. At the chromosome level, 6
teleost-level paralogue pairs link the gria1a region (chr14) to chr21, and 11 link the gria1b region (chr21) to
chr14 (for example npas4, fosl1, vegfb, nxf1). They sit several Mb from the gria1 genes, so local gene order has been
rearranged ([RESULTS.md](../../../../genes/DANRE/gria1a/gria1a-bioinformatics/RESULTS.md)).

**Status.** TGD origin is supported by the PANTHER tree call and by the Compara node with a single gar ortholog and
retention of both copies in medaka. Chromosome-level synteny is consistent with it; local synteny is not conserved.

## 2. Protein-level comparison

- **Identity.** 82.5% identity and 89.7% similarity over 920 columns
  ([annotation-comparison.md](annotation-comparison.md)). Against gar GRIA1: gria1a 88.3%, gria1b 81.7%. Against
  human GRIA1: 74.4% and 71.0%.
- **Channel core.** Both copies keep the six glutamate-binding residues annotated on human GRIA1, both palmitoylation
  cysteines, and an identical pore loop and M2-M3 gating segment (human 585-612). The ligand-binding extracellular
  segment (human 631-805) is 95.4% identical to human in gria1a and 90.3% in gria1b.
- **Rate asymmetry.** Against gar, 86 changes are unique to gria1b and 34 to gria1a (chi2 = 22.5, P < 0.05). The
  medaka ortholog of gria1b is also strongly diverged from gar (71.6% identity), while medaka gria1a is not (87.4%). The
  faster evolution of the b copy therefore began before the zebrafish-medaka split, soon after the duplication.
- **Cytoplasmic tail.** In mammals, two tail serines regulate the receptor:
  [PMID:20716669 "Ser831 is a substrate for both CaMKII- and PKC-dependent phosphorylation, whereas Ser845 is a substrate for PKA phosphorylation"]
  gria1a, gar and medaka gria1a keep both serines. gria1b has an isoleucine at the S831 position (medaka gria1b has a
  leucine) and no serine aligned to S845 (medaka gria1b keeps one). This holds in every Ensembl gria1b translation,
  so it is not an isoform artefact. The C-terminal PDZ-binding motif ends in -TGM or -SGM in all fish sequences,
  including gar, so the change from human -TGL predates the duplication. An early study had already noted
  incomplete motif conservation:
  [PMID:16887104 "Many but not all of the known mammalian protein-protein interaction motifs are preserved in the C-terminal domains (CTD) of zebrafish AMPARs."]
- **Biochemistry.** Neither zebrafish subunit has been expressed or recorded. The mammalian ortholog forms
  AMPA-selective channels:
  [PMID:2166337 "Functional expression of the cDNAs in cultured mammalian cells generated receptors displaying alpha-amino-3-hydroxy-5-methyl-4-isoxazole propionic acid (AMPA)-selective binding pharmacology (AMPA = quisqualate greater than glutamate greater than kainate) as well as cation channels gated by glutamate, AMPA, and kainate and blocked by 6,7-dinitroquinoxaline-2,3-dione (CNQX)."]

**Does each copy keep the ancestral molecular function?** Channel function: probably yes for both, since all
ligand-binding and pore residues are intact. Regulation: gria1b has lost at least the S831-type site in the teleost
b lineage, so its regulation may differ. This is an inference from sequence only.

## 3. Expression

- **In situ survey (24-72 hpf).** The authors conclude that each gria pair is differentially expressed:
  [PMID:18224707 "As a general rule, each pair of duplicated gria genes is differentially expressed, indicating subfunctionalization of AMPA receptor subunit expression in the teleost lineage."]
  The cached paper is abstract-only. ZFIN's curation of it gives 17 in situ terms shared by the two copies (olfactory
  bulb, habenula, hypothalamus, preoptic area, thalamus, ventral thalamus, tegmentum, optic tectum, medulla, retinal
  ganglion cell and inner nuclear layers, motor and sensory neurons, spinal interneurons, and the early neuronal
  clusters). Telencephalon (dorsal and ventral), dorsal thalamus, rhombomeres, spinal cord and retinal ganglion cells
  are recorded for gria1a only, and the otic vesicle for gria1b only
  ([RESULTS.md](../../../../genes/DANRE/gria1a/gria1a-bioinformatics/RESULTS.md)). ZFIN terms are coarse, and
  differences in level within a shared region would not show.
- **Maternal and early transcripts** of all AMPA receptor genes (RT-PCR):
  [PMID:16887104 "Transcripts of all AMPAR genes are detected at the time of fertilization, suggesting maternal transcriptions of zebrafish AMPAR genes."]
  In E-ERAD-475 both copies are near zero before segmentation.
- **Level.** In whole larvae (E-ERAD-475), gria1a is at 12-14 TPM and gria1b at 5-6 TPM.
- **Forebrain.** In a later screen, gria1a in situ signal was forebrain:
  [PMID:30929901 "gria1a: forebrain showed in situ and activity signal."]
- **Bgee RNA-seq.** Both copies have brain and retina calls. gria1b adds mature ovarian follicle (65.2), spleen (64.7)
  and gill (31.4), and a higher testis score (49.6 vs 22.4). Gar GRIA1 has calls in brain, eye, larva, ovary, bone and
  embryo. The ovary call is thus shared by gar and gria1b.

**Summary.** Both copies are broadly neural. gria1a carries the telencephalic and spinal cord domains in the in situ
data and dominates in larvae. gria1b adds an otic domain and non-neural calls, and the ovary call matches gar. This
pattern fits a partial, uneven partition, but it rests on coarse curated terms and thresholded RNA-seq calls.

## 4. Experimental evidence of function

**Alleles.** The only loss-of-function data come from a large screen of schizophrenia-associated genes that mutated
both copies of every duplicated gene:
[PMID:30929901 "If the human gene of interest was duplicated in zebrafish, homozygous mutations were generated for both orthologs."]
gria1 mutants were among those with a forebrain (pallium) activity phenotype:
[PMID:30929901 "mutants with signals mainly in the pallium (label 2) were all unambiguously associated, including bcl11b, gria1, znf536, clcn3, and cacna1c."]
The main text does not say which copy, or whether only the double, produced it. The per-ortholog comparison is in a
supplementary heatmap that I could not read. Allele lesions are given on an external site and were not checked.

**gria1a / gria1b separately.** No morphant, rescue, cross-rescue, electrophysiology or compensation data.

## 5. Fate classification

**UNRESOLVED. Level: both (expression and protein). Evidence: expression and sequence; there is mutant data, but it
does not separate the copies.**

**Observed**

- Largely overlapping neural expression, with copy-specific domains in the curated in situ data: gria1a in
  telencephalon and spinal cord; gria1b in the otic vesicle.
- gria1a is more abundant in larvae.
- Asymmetric protein evolution: gria1b evolves faster in both zebrafish and medaka. It has lost the S831-equivalent
  serine in the teleost b lineage and the S845-equivalent serine in zebrafish, while the channel core is intact.

**Consistent with, but not shown**

- *MIXED (expression partition plus protein-level divergence of gria1b):* the most economical reading of the
  pattern, but no assay shows that gria1b receptors behave differently or that either copy is needed where it is
  uniquely expressed.
- *Relaxed constraint on a partly redundant gria1b:* faster evolution concentrated in the regulatory tail, with the
  channel core intact, would also be expected if gria1b were a lower-expressed backup under weaker selection.
- *Partition only:* possible if the tail changes are neutral.

**What would change the call**

- Paralog-specific in situ or single-cell data (larva and adult), with gar GRIA1 in situ as outgroup, to establish
  real copy-specific domains.
- Single and double mutants with brain activity maps and mEPSC recordings, plus paralog mRNA levels in each mutant.
- Recording from gria1a vs gria1b homomers and heteromers (with gria2) under CaMKII or PKA activation, to test
  whether the diverged tail changes regulation.

## 6. GO annotation consistency across the pair

Source: [annotation-comparison.md](annotation-comparison.md), after both reviews.

**Identical rows.** Both copies carry the same 15 GOA rows (8 IBA, 7 IEA), none experimental, and they were reviewed
identically. AMPA glutamate receptor activity, the transmitter-gated channel terms, AMPA receptor complex,
postsynaptic density membrane, postsynaptic and plasma membrane, and glutamatergic transmission were accepted on
both. Dendritic spine and modulation of chemical synaptic transmission were kept as non-core on both. They rest on
mammalian data, and for gria1b the plasticity role is less secure because of the tail changes (noted in the review
text).

**How propagation treats the pair.** The IBA rows come from three PANTHER nodes (PTN000437926, PTN000438081,
PTN001826301) that sit above the duplication. Both copies inherit them equally, which is right for the conserved
channel core. The one place where a copy-specific difference could matter, regulation of the receptor through the
C-terminal tail, has no GO row on either copy, so nothing needs to be made copy-specific now.

**Asymmetries that come from which copy was studied.** None: no zebrafish experimental annotation exists for
either copy.

**Should be copy-specific (if confirmed):** otic vesicle or inner-ear expression (gria1b) and telencephalic
expression (gria1a). These are expression data, not GO terms.
**Should be shared:** the receptor activity, complex membership and postsynaptic location, as now.

## 7. Open questions

- Which copy, or the double, gives the gria1 forebrain phenotype in the schizophrenia-gene screen?
- Do gria1a and gria1b co-assemble, and which subunit dominates in which neurons?
- Does the gria1b tail still carry functional CaMKII/PKC or PKA sites nearby, and does it change synaptic delivery?
- Is gria1b really expressed in the inner ear, ovary, spleen and gill, and are these domains present in gar?
- Why is local synteny lost around both copies (rearrangement near the gria1 loci)?

## References

PMID:2166337, PMID:16887104, PMID:18224707, PMID:20716669, PMID:30929901. Also `panther_tgd_pairs.tsv`,
`random_sample.tsv`, [annotation-comparison.md](annotation-comparison.md),
[gria1a-bioinformatics/RESULTS.md](../../../../genes/DANRE/gria1a/gria1a-bioinformatics/RESULTS.md) and
[output.txt](../../../../genes/DANRE/gria1a/gria1a-bioinformatics/output.txt).
