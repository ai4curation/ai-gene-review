---
title: "prom1a / prom1b"
autolink_gene_symbols: false
---

# prom1a / prom1b

[Back to pairs](../README.md)

**Bottom line:** PARTITION at the level of expression, lopsided and only partly tested. prom1a keeps the broad,
maternal and multi-organ expression of the unduplicated gar gene; prom1b is zygotic, restricted to retina and brain,
and is the dominant prominin in photoreceptors. Only prom1b mutants lose outer-segment structure, so the ancestral
PROM1 photoreceptor role now rests on prom1b. In the adult brain and inner retina the two copies occupy
complementary domains. Both proteins keep the prominin architecture and no cross-rescue has been done, so a
protein-level contribution to the split cannot be excluded.

**Sample record:** fate=PARTITION; level=expression; evidence=experimental_both; identity=54.4%

| | prom1a | prom1b |
|---|---|---|
| UniProt | Q9W735 (Swiss-Prot, 826 aa) | A0A8M2BI60 (TrEMBL, RefSeq isoform X8, 867 aa) |
| Human ortholog | PROM1 (prominin-1, CD133) | PROM1 |
| Chromosome | 14 | 1 |
| ZFIN | ZDB-GENE-030131-1577 | ZDB-GENE-031003-1 |
| Mutant alleles | TALEN 4-bp deletion (frameshift; full text, see [prom1a-notes.md](../../../../genes/DANRE/prom1a/prom1a-notes.md)) | TALEN 4-bp deletion (frameshift; ZFIN genotype ZDB-GENO-200511-1) |
| Review | [genes/DANRE/prom1a](../../../../genes/DANRE/prom1a/prom1a-ai-review.yaml) | [genes/DANRE/prom1b](../../../../genes/DANRE/prom1b/prom1b-ai-review.yaml) |

## 1. Evidence the pair comes from the TGD

**PANTHER.** The row in `panther_tgd_pairs.tsv` is:

| tgd_call | branch | class | family | human orthologs (a / b) | gar co-orthologs | medaka co-orthologs | medaka parallel dup |
|---|---|---|---|---|---|---|---|
| TGD_tree | Neopterygii\|Teleostei | 1:1 | PTHR22730 (PROMININ PROM PROTEIN) | PROM1(LDO) / PROM1(O) | 1 (same gar gene for both) | 2 | (blank) |

The PANTHER row gives A0A8M9QBM3 as the prom1b UniProt entry; the review uses A0A8M2BI60, the entry that carries
the GOA rows.

**Ensembl Compara** (`random_sample.tsv`): duplication at Osteoglossocephalai, one gar ortholog for both copies
(ENSLOCG00000003057), and a separate one-to-one medaka ortholog for each copy
([RESULTS.md](../../../../genes/DANRE/prom1a/prom1a-bioinformatics/RESULTS.md)). prom2 is an older paralog.

**Synteny (my check).** Of the 61 protein-coding genes within 1.5 Mb of prom1a, 18 have a teleost-level zebrafish
paralogue, and 6 of these have their partner within 1.5 Mb of prom1b: anxa5a/b, fgfbp1a/b, fgfbp2a/b, tapt1a/b,
ldb2a/b and qdpra/qdprb.1 ([output.txt](../../../../genes/DANRE/prom1a/prom1a-bioinformatics/output.txt), section 6). The reverse scan
from prom1b finds the same six pairs, so the two copies sit in a duplicated block. I did not check the gar side.

**Literature.** The duplication is described but not dated:
[PMID:21407811 "In contrast to other vertebrates, the zebrafish prominin-1 gene is duplicated and consequently, both co-orthologues of mammalian prominin-1 are referred as to prominin-1a and b [27]."]

**Status.** TGD origin well supported: PANTHER `TGD_tree`, Compara at the teleost node with a single gar
ortholog and two medaka orthologs, and a duplicated block of six neighbouring gene pairs retained in both copies.

## 2. Protein-level comparison

- **Identity.** 54.4% identity, 72.2% similarity over 867 columns ([annotation-comparison.md](annotation-comparison.md));
  56.0% between the Ensembl canonical proteins. Each copy is about 60% identical to gar PROM1 and 39-41% to human PROM1.
- **Rates.** A relative-rate test with gar as outgroup finds no asymmetry (107 vs 118 unique changes; chi2 = 0.54).
- **Architecture.** Both keep the five transmembrane segments and the two large extracellular loops; the small
  cytoplasmic loops are the most conserved segments. Each keeps 15 of 22 human cysteines and three of the eight
  annotated human N-glycosylation sites (different subsets). The C-terminal tail aligns poorly in both zebrafish
  proteins; the fish genes have many splice variants:
  [PMID:21407811 "In fish, in addition to the prominin-1a splice variant s11, three new variants (designated as s18-20) were amplified from cDNA templates derived from either adult zebrafish retina or brain (for details see Table S3; GenBank entries: HQ386793-96)."]
- **Biochemistry and cross-rescue.** None. Prom1b-GFP localizes to the apical membrane of retinal neuroepithelia:
  [PMID:22492354 "We also generated a transgenic line in which GFP is fused with Prominin1b (Prom1b-GFP), a cholesterol-interacting pentaspan membrane protein that is enriched at the apical region of polarized cells, including retinal neuroepithelia ( Fig. 6B )"]

**Does each copy keep the ancestral molecular function?** Structurally, yes: no copy-specific loss of a conserved
landmark is visible. Prominins have no well-defined biochemical activity, and neither zebrafish protein has been
tested for one.

## 3. Expression

- **Embryo.** Whole-mount in situ hybridization found both overlapping and complementary domains:
  [PMID:20503380 "prominin1a and b show novel complementary and overlapping patterns of expression in proliferating zones in the developing sensory organs and central nervous system."]
- **Timing (E-ERAD-475).** prom1a is maternal (11-12 TPM from 2-cell to dome) and zygotic throughout; prom1b is
  absent before segmentation and rises to 26-49 TPM at 3-5 dpf, above prom1a
  ([RESULTS.md](../../../../genes/DANRE/prom1a/prom1a-bioinformatics/RESULTS.md)).
- **Adult brain.** Mostly complementary along the ventricular system:
  [PMID:23723983 "Distribution of the two molecules (prominin-1a and prominin-1b) along the rostro-caudal axis of the ventricle system of the zebrafish brain displays a fairly complementary pattern with only a low-degree of overlapping."]
  [PMID:23723983 "Note that major sites of expression of prominin-1a are mainly located in the prosencephalic (rostral) and dorsal mesencephalic (tectal) domain (A), whereas prominin-1b is predominantly found in the rhombencephalic brainstem (caudal) domain (B)."]
  [PMID:23723983 "The combined expression of prominin-1a and b mimics the distribution of musashi-1 in adult zebrafish brain."]
- **Adult retina.** Both in photoreceptors, split in the inner nuclear layer:
  [PMID:21407811 "Within the ONL of three month-old fish, both prominin-1 molecules were detected (Fig."]
  [PMID:21407811 "Of the two prominin-1 paralogues, expression of prominin-1b appeared to be more robust in line with gene expression profiling reported earlier on embryonic retina [33]."]
  [PMID:21407811 "Prominin-1a was strongly expressed along the vitreal side of the INL (Fig."]
  [PMID:21407811 "In contrast, prominin-1b was weakly, but reproducibly, detected at the scleral, but not the vitreal, side of the INL (Fig."]
- **Photoreceptor single-cell data (my reanalysis of GSE175929).** Both copies are in rods and all four cone types;
  prom1b is 3-4 times more abundant (rods 6.5 vs 1.7 CP10K) and both are rod-enriched
  ([scrna_output.txt](../../../../genes/DANRE/prom1a/prom1a-bioinformatics/scrna_output.txt)).
- **Other organs (Bgee, ZFIN).** prom1a has RNA-seq calls in ovary, testis, muscle, heart, intestine, gill, spleen,
  head kidney and skin, and ZFIN records in lens, olfactory epithelium, kidney and intestine. prom1b has calls only in
  retina, brain, larva, embryo and bone ([expression_output.txt](../../../../genes/DANRE/prom1a/prom1a-bioinformatics/expression_output.txt)).
- **Pre-duplication state.** Spotted gar PROM1 has Bgee RNA-seq calls in eye, ovary, brain, embryo, testis,
  mesonephros, skin, muscle, liver, intestine and heart ([output.txt](../../../../genes/DANRE/prom1a/prom1a-bioinformatics/output.txt),
  section 5). Human PROM1 is likewise expressed in stem cells, epithelia and photoreceptors:
  [PMID:32201384 "Human PROM1 (CD133) is detected in both somatic and cancer stem cells and is also expressed in terminally differentiated epithelial and photoreceptor cells."]
  So the ancestral gene was broad, as prom1a is; prom1b kept the retina and part of the brain.

Summary: prom1a retains most of the ancestral breadth including maternal and epithelial expression; prom1b is
limited to retina and brain but dominates photoreceptors and the hindbrain germinative zones. The copies overlap in
photoreceptors and partly in the embryonic nervous system.

## 4. Experimental evidence of function

**Alleles**

| Gene | Allele | Lesion | Type | Source |
|---|---|---|---|---|
| prom1a | TALEN | 4-bp deletion, frameshift (p.Asp46Glufs*15) | PTC; prom1a mRNA not significantly reduced at 2 mpf | full text of PMID:31362982, not cached ([prom1a-notes.md](../../../../genes/DANRE/prom1a/prom1a-notes.md)) |
| prom1b | TALEN | 4-bp deletion (p.Pro59Valfs*62) | PTC; prom1b mRNA reported lower at 7 dpf | full text of PMID:31362982, not cached ([prom1b-notes.md](../../../../genes/DANRE/prom1b/prom1b-notes.md)) |

**prom1b**

- Outer-segment morphogenesis fails; cones degenerate early, rods survive with abnormal outer segments:
  [PMID:31362982 "Loss of prom1b disrupted OS morphogenesis, with rods and cones exhibiting differences in impairment: cones degenerated at an early age, whereas rods remained viable but with an abnormal OS, even at 9 months postfertilization."]
- Prph2 is mislocalized:
  [PMID:31362982 "Moreover, we found that Prom1b deletion causes mislocalization of Prph2 and disrupts its oligomerization."]

**prom1a**

- The same study made a prom1a mutant and concluded:
  [PMID:31362982 "The Prom1 orthologs in zebrafish include prom1a and prom1b, and our results showed that prom1b, rather than prom1a, plays an important role in zebrafish photoreceptors."]
  The full text (not cached) reports normal outer nuclear layer and outer-segment thickness in prom1a mutants up to
  11 months ([prom1a-notes.md](../../../../genes/DANRE/prom1a/prom1a-notes.md)). No phenotype outside the retina
  was reported.
- The conclusion was challenged in a letter (PMID:31704774; text not cached) that pointed to prom1a expression and
  splice variants in the retina; the authors replied (PMID:31704775).

**Both copies**

- No double mutant, no cross-rescue, and no measurement of prom1a in prom1b mutants (transcriptional adaptation
  untested). The prom1b allele is a frameshift, so paralog upregulation is possible in principle; since prom1b mutants
  still have a strong phenotype, any compensation by prom1a is at most partial.

## 5. Fate classification

**PARTITION, at the level of expression; lopsided. Confidence: moderate.**

**Established**

- The unduplicated gar gene is broadly expressed; prom1a keeps that breadth (maternal, gonads, epithelial organs);
  prom1b has lost it and is limited to retina and brain.
- In the adult brain and inner retina the two copies occupy mostly complementary domains.
- In photoreceptors both are expressed, prom1b 3-4 times more; only prom1b loss disrupts outer segments.

**Inferred, not shown**

- That the photoreceptor split is due to expression level rather than protein differences (no cross-rescue).
- That prom1a does something in the maternal embryo or adult epithelia: no phenotype outside the retina has been
  looked for.

**Why not the other fates**

- *Backup:* the prom1b single mutant has a strong phenotype, so prom1a does not back it up in photoreceptors.
- *Innovation:* no new function or new expression domain relative to gar/human PROM1 has been shown.
- *Dosage:* possible for photoreceptors (both expressed, prom1b more), but the non-overlapping brain, INL and organ
  domains are a partition, not a dosage share.

**What would change the call**

- Failure of Prom1a to rescue prom1b mutant photoreceptors when expressed at prom1b levels would add a protein-level
  component (MIXED).
- A worse phenotype in prom1a; prom1b double mutants would show residual redundancy in photoreceptors.

## 6. GO annotation consistency across the pair

Source: [annotation-comparison.md](annotation-comparison.md), after both reviews.

**Annotated to prom1a only, from propagation.** All localization rows (plasma membrane, apical membrane, microvillus,
cilium, prominosome, ER, ERGIC) and the process rows come from IBA, ISS and IEA on the Swiss-Prot entry. The ER and
ERGIC rows were marked as over-annotated (transit compartments). prom1b, a TrEMBL entry, receives almost none of the
PANTHER IBA rows, which is an artefact of entry status rather than biology; the family-level locations should apply
to both.

**Photoreceptor process: on the wrong copy.** The IBA row camera-type eye photoreceptor cell differentiation
(GO:0060219) sits on prom1a, which has no photoreceptor phenotype. I marked it as over-annotated with a
propagation_review (PROPAGATION_BAD, CONTEXT_OR_TISSUE_MISMATCH). The experimentally supported process, photoreceptor
cell outer segment organization (GO:0035845, IMP), is on prom1b and was accepted as core.

**Should be copy-specific:** photoreceptor outer segment organization (prom1b). **Should be shared:** apical plasma
membrane, microvillus, cilium (prom1b has only the apical membrane IDA row and the IEA microvillus membrane row).

## 7. Open questions

- Does Prom1a rescue prom1b mutant photoreceptors when expressed from the prom1b promoter?
- Do prom1a; prom1b double mutants have worse rod outer segments than prom1b mutants?
- What does maternal prom1a do, and do prom1a mutants have epithelial or brain phenotypes that were not examined?
- Is the same split (broad a-copy, photoreceptor b-copy) present in medaka, which keeps both copies?

## References

PMID:20503380, PMID:21407811, PMID:22492354, PMID:23723983, PMID:31362982, PMID:31704774, PMID:31704775,
PMID:32201384. Also `panther_tgd_pairs.tsv`, `random_sample.tsv`, [annotation-comparison.md](annotation-comparison.md),
[prom1a-bioinformatics/RESULTS.md](../../../../genes/DANRE/prom1a/prom1a-bioinformatics/RESULTS.md),
[output.txt](../../../../genes/DANRE/prom1a/prom1a-bioinformatics/output.txt),
[expression_output.txt](../../../../genes/DANRE/prom1a/prom1a-bioinformatics/expression_output.txt),
[scrna_output.txt](../../../../genes/DANRE/prom1a/prom1a-bioinformatics/scrna_output.txt).
