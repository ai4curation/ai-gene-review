---
title: "samsn1a / samsn1b"
autolink_gene_symbols: false
---

# samsn1a / samsn1b

[Back to pairs](../README.md)

**Bottom line:** UNRESOLVED, with expression differences but no functional data. These are the two copies of the
SH3-SAM immune adaptor SAMSN1 (HACS1). They have diverged a lot in sequence (37.8% identity), but both keep a
well-conserved SH3 domain. samsn1a is the zygotic copy, with in situ signal in blood, macrophages and lens; samsn1b has
a gastrula peak and in situ signal in the pineal organ and photoreceptors. Bulk RNA-seq detects both copies in
granulocytes, spleen and head kidney. The data fit a partial expression partition, but no study has tested either gene.

**Sample record:** fate=UNRESOLVED; level=expression; evidence=expression_only; identity=37.8%

| | samsn1a | samsn1b |
|---|---|---|
| UniProt | B3DH22 (TrEMBL, 621 aa) | A0A8M2BH30 (TrEMBL, 676 aa; RefSeq isoform X1) |
| Human ortholog | SAMSN1 (HACS1, SLy2, NASH1) | SAMSN1 |
| Chromosome | 15 | 10 |
| ZFIN | ZDB-GENE-030131-8639 | ZDB-GENE-041010-135 |
| Mutant alleles | none characterized | none characterized |
| Review | [genes/DANRE/samsn1a](../../../../genes/DANRE/samsn1a/samsn1a-ai-review.yaml) | [genes/DANRE/samsn1b](../../../../genes/DANRE/samsn1b/samsn1b-ai-review.yaml) |

## 1. Evidence the pair comes from the TGD

**PANTHER.** The row in `panther_tgd_pairs.tsv` is:

| tgd_call | branch | class | family | human orthologs (a / b) | gar co-orthologs | medaka co-orthologs | medaka parallel dup |
|---|---|---|---|---|---|---|---|
| TGD_tree | Neopterygii\|Teleostei | 1:1 | PTHR12301 (SAM-DOMAIN, SH3 AND NUCLEAR LOCALIZATION SIGNALS PROTEIN RELATED) | SAMSN1(LDO) / SAMSN1(O) | 1 (same gar gene for both) | 1 | (blank) |

PANTHER places the duplication after the split from gar and before the zebrafish-medaka split. Both copies share one
gar co-ortholog, and medaka keeps only one copy.

**Ensembl Compara** (random_sample.tsv, and my script) dates the samsn1a/samsn1b duplication to the Osteoglossocephalai
node. It gives one gar orthologue (ENSLOCG00000000927) for both copies. Medaka's single copy is a one-to-one orthologue of
samsn1a, and samsn1b has no medaka orthologue. So medaka seems to have lost the samsn1b copy
([RESULTS.md](../../../../genes/DANRE/samsn1a/samsn1a-bioinformatics/RESULTS.md)).

**Synteny.** samsn1a is on chr15 and samsn1b on chr10. My script looked at genes within 1.5 Mb of each copy. It found
six neighbour pairs whose members are teleost-level paralogues, one member next to each copy: gdpd5, serpinh1, nrip1,
msi2, omg and ksr1. The same six pairs are found whichever copy the search starts from. This is double-conserved
synteny ([RESULTS.md](../../../../genes/DANRE/samsn1a/samsn1a-bioinformatics/RESULTS.md)).

**Literature.** I found no paper that discusses the origin of this pair.

**Status.** A teleost-specific duplication is supported by two independent gene-tree methods (PANTHER and Compara).
It is also supported by double-conserved synteny with six flanking ohnolog pairs. TGD origin is well supported.

## 2. Protein-level comparison

- **Identity.** 37.8% identity and 51.7% similarity over 727 columns
  ([annotation-comparison.md](annotation-comparison.md)). Each copy is closer to gar SAMSN1 (43.3% / 46.4%) than to
  the other copy, and only 27-28% identical to human SAMSN1. The fish and gar proteins (621-690 aa) are much longer than
  human SAMSN1 (373 aa), so part of the low identity comes from extra, poorly conserved regions
  ([RESULTS.md](../../../../genes/DANRE/samsn1a/samsn1a-bioinformatics/RESULTS.md)).
- **Domains.** The SH3 domain is 82.3% (samsn1a) and 77.4% (samsn1b) identical to the human SH3 domain; the gar value
  is 83.9%. The SAM domain is 52-60% identical. Both copies keep the N-terminal 14-3-3 motif region (5 of 6 residues).
  In human SAMSN1 the SH3 domain is the part that binds the inhibitory receptor PIRB:
  [PMID:33188360 "Here, we describe the interaction between the HACS1 SH3 domain and a sequence near the third immunoreceptor tyrosine-based inhibition motif (ITIM3) of the paired immunoglobulin receptor B (PIRB)."]
- **Rates.** With gar as the outgroup, 96 changes are unique to samsn1a and 93 to samsn1b (chi2 = 0.05). Neither copy
  is evolving faster.
- **Biochemistry.** No zebrafish protein has been studied.

**Does each copy keep the ancestral molecular function?** Probably, because the SH3 domain is conserved in both copies.
However, the mammalian molecular function is itself only defined by binding partners
[PMID:15381729 "HACS1 associates with tyrosine-phosphorylated proteins after B cell activation and binds in vitro to the inhibitory molecule paired Ig-like receptor B."].
With such low overall identity, divergence in the disordered regions cannot be ruled out.

## 3. Expression

All numbers below are from my script
([RESULTS.md](../../../../genes/DANRE/samsn1a/samsn1a-bioinformatics/RESULTS.md);
[output.txt](../../../../genes/DANRE/samsn1a/samsn1a-bioinformatics/output.txt)).

- **Timing (E-ERAD-475 whole embryos).** Neither copy is maternal. samsn1b has a small gastrula peak (5 TPM); samsn1a
  is not expressed then. samsn1a comes on at late segmentation (about 1 TPM) and rises to 28 TPM by day 5. samsn1b is
  off from segmentation to hatching and returns at 10-17 TPM in larvae.
- **Curated in situ hybridization (ZFIN).** The two copies share no anatomy term:
  - samsn1a is in blood, macrophages and the solid lens vesicle at prim-5 (Covassin et al. 2006, ZDB-PUB-060927-11).
  - samsn1b is in the epiphysis (pineal) from 14-19 somites to high-pec, and in the retinal photoreceptor layer at
    day 5 (Thisse et al. 2004 direct submission).
- **Single-cell retina.** samsn1a marks bipolar cells:
  [PMID:37988404 "UMAP plots of vsx1 and samsn1a, known and novel markers of bipolar cells, respectively, showed high counts in cluster 15 (Figure 8E and F)."]
  [PMID:36047082 "samsn1a , vsx1 , neurod4 (BPs)"]
  So in the retina, the in situ and single-cell data put samsn1a in bipolar cells and samsn1b in photoreceptors.
- **Bulk RNA-seq (Bgee).**
  - samsn1a scores highest in granulocytes, spleen and head kidney (90-95).
  - samsn1b scores highest in retina (89) and granulocytes (88), and lower in spleen and head kidney (61-64).
  - Both have RNA-seq calls in 11 shared tissues, including all three hematopoietic entities.
- **Another teleost.** In channel catfish spleen, the samsn1a orthologue marks a myeloid cluster:
  [PMID:39325796 "Cluster 11 was defined by upregulated expression of myeloid-related genes such as dbn1 (drebrin 1), foxp4 (forkhead box P4), samsn1a (SAM domain, SH3 domain and nuclear localization signals 1), csf1rb (colony stimulating factor 1 receptor), mafba (MAF bZIP transcription factor B) and csf3r (colony stimulating factor 3 receptor)."]
- **Pre-duplication state.**
  - Mammalian SAMSN1 is a hematopoietic gene that is also expressed in brain:
    [PMID:11536050 "Polyclonal antibodies against HACS1 recognized a 49.5 kDa protein whose mRNA is expressed in human immune tissues, bone marrow, heart, lung, placenta and brain."]
  - Gar SAMSN1 has Bgee calls in eye (91.6), bone, gill, intestine, kidney, heart, liver and brain. Bgee returns no gar
    spleen or blood call, which may just reflect which gar samples exist.
  - Gar eye expression means retinal expression was probably present before the duplication. Whether the ancestral
    gene was in both bipolar cells and photoreceptors is unknown.

**Summary.** The copies differ in timing (gastrula peak for samsn1b, early blood and macrophage expression for samsn1a)
and in retinal cell type (bipolar cells vs photoreceptors). samsn1b also has pineal expression. The hematopoietic
domain is shared at the bulk level, with samsn1a dominant.

## 4. Experimental evidence of function

- **Zebrafish.** No mutant, morphant, rescue or overexpression data exist for either copy. The zebrafish literature has
  only marker-gene mentions.
- **Mammals (context).**
  - The mouse knockout is the experimental seed of the B-cell IBA that both copies carry:
    [PMID:19923443 "Purified splenic B cells from Hacs1(-/-) mice showed increased cell proliferation on BCR (B-cell receptor) stimulation."]
  - The mouse knockout mice were otherwise healthy:
    [PMID:19923443 "Hacs1(-/-) mice were viable and fertile and had normal bone marrow B-cell development and normal splenic T- and B-cell populations."]

## 5. Fate classification

**UNRESOLVED. Level: expression. Confidence: low.**

**Observed**

- The in situ domains do not overlap: samsn1a in blood, macrophages and lens; samsn1b in pineal and photoreceptors.
- The timing differs: samsn1b peaks at gastrula, samsn1a is zygotic from late segmentation.
- In the retina, single-cell and in situ data give different cell types: samsn1a in bipolar cells, samsn1b in
  photoreceptors.
- Both copies are detected in bulk hematopoietic tissues.
- Both copies keep a conserved SH3 domain, and neither is evolving faster than the other.
- Medaka appears to have kept only the samsn1a copy.

**Why UNRESOLVED and not PARTITION**

- The curated in situ data come from two different screens, at different stages, with different probes. The absence of
  a copy from the other screen's anatomy terms is not evidence that it is absent from that tissue.
- The bulk data show overlap in blood-forming tissues.
- The ancestral pattern at cell-type resolution (gar or bowfin) is unknown. So a pineal or photoreceptor domain for
  samsn1b could be ancestral (partition) or new (innovation).
- With 37.8% identity, protein-level divergence cannot be excluded without functional tests.

**What would resolve it**

- Paralog-specific HCR or single-cell data across blood, kidney marrow, retina and pineal, together with gar SAMSN1 in
  situ data.
- Single and double mutants, using RNA-less alleles to avoid transcriptional adaptation, scored for immune-cell
  activation and retinal or pineal phenotypes.
- Cross-rescue between the copies.

## 6. GO annotation consistency across the pair

Source: [annotation-comparison.md](annotation-comparison.md).

- **Shared, and consistent.** Both copies carry the same two IBA rows, and I accepted both on both copies:
  - negative regulation of B cell activation (GO:0050869, from node PTN002642349, seeded by mouse Hacs1);
  - regulation of intracellular signal transduction (GO:1902531, from the SLy/SASH1 family node, seeded by SASH1).

  Bulk RNA-seq places both copies in hematopoietic tissues, so the expression data give no reason to withhold the
  immune term from samsn1b. If paralog-resolved data later show samsn1b missing from lymphocytes, the samsn1b row
  would become a CONTEXT_OR_TISSUE_MISMATCH case.
- **Bookkeeping asymmetry.** samsn1b carries root ND rows for MF, BP and CC; samsn1a has none. Both reviews were
  accepted as accurate placeholders. The difference reflects record processing, not biology.
- **Not propagated to either copy.** Human SAMSN1 has IBA rows for nucleus, cytoplasm and phosphotyrosine residue
  binding from a different node (PTN008535977). Neither zebrafish copy receives them, which suggests that node does
  not include the fish genes. I did not add them as NEW, because neither zebrafish protein has been localized or
  assayed.
- **Copy-specific terms.** None are justified yet. Candidate copy-specific terms (for example pineal or photoreceptor
  roles for samsn1b) would need functional data.

## 7. Open questions

- Is samsn1b in lymphocytes or myeloid cells at the single-cell level, or only in granulocyte-rich bulk samples?
- Is the gar or bowfin SAMSN1 retinal expression in bipolar cells, photoreceptors or both? Is there pineal expression?
- Why did medaka lose one copy while zebrafish kept both? Is the zebrafish samsn1b domain (pineal, photoreceptors) the
  one that medaka lacks?
- Does the long N-terminal region found in fish and gar SAMSN1, but not in human, carry signalling motifs?

## References

PMID:11536050, PMID:15381729, PMID:19923443, PMID:33188360, PMID:36047082, PMID:37988404, PMID:39325796. Also
`panther_tgd_pairs.tsv`, `random_sample.tsv`, [annotation-comparison.md](annotation-comparison.md),
[samsn1a-bioinformatics/RESULTS.md](../../../../genes/DANRE/samsn1a/samsn1a-bioinformatics/RESULTS.md) and
[output.txt](../../../../genes/DANRE/samsn1a/samsn1a-bioinformatics/output.txt).
