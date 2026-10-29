---
title: "olfm3a / olfm3b"
autolink_gene_symbols: false
---

# olfm3a / olfm3b

[Back to pairs](../README.md)

**Bottom line:** UNRESOLVED. The two OLFM3 (noelin-3) proteins are conserved: every domain,
cysteine, glycosylation sequon and calcium-site residue examined is kept, and neither copy
evolves faster. What differs is expression. olfm3a is the larval neural copy (brain, retina).
olfm3b is almost silent through larval stages, with weak adult calls in brain, intestine and
ovary. Gar OLFM3 is expressed in brain, eye and ovary, so the complementary retina and ovary calls
could reflect an expression partition. But these are thresholded RNA-seq calls, with no in situ
data and no mutants. The pattern is equally consistent with olfm3b drifting toward loss.

**Sample record:** fate=UNRESOLVED; level=expression; evidence=expression_only; identity=83.2%

| | olfm3a | olfm3b |
|---|---|---|
| UniProt | A8KB73 (TrEMBL; ZGC cDNA, 457 aa) | A0A8N7UT25 (TrEMBL; RefSeq isoform X1, 457 aa) |
| Human ortholog | OLFM3 | OLFM3 |
| Chromosome | 24 | 2 |
| ZFIN | ZDB-GENE-080219-11 | ZDB-GENE-070912-606 |
| Ensembl | ENSDARG00000071493 | ENSDARG00000039174 |
| Review | [genes/DANRE/olfm3a](../../../../genes/DANRE/olfm3a/olfm3a-ai-review.yaml) | [genes/DANRE/olfm3b](../../../../genes/DANRE/olfm3b/olfm3b-ai-review.yaml) |

This pair was drawn at random (batch 3, draw 10, seed 20260928) from the 778 clean 1:1
`TGD_tree` pairs (`batch3_sample.tsv`).

## 1. Evidence the pair comes from the TGD

**PANTHER.** The row in `panther_tgd_pairs.tsv` is:

| tgd_call | branch | class | family | human orthologs (a / b) | gar co-orthologs | medaka co-orthologs | medaka parallel dup |
|---|---|---|---|---|---|---|---|
| TGD_tree | Neopterygii\|Teleostei | 1:1 | PTHR23192 (OLFACTOMEDIN-RELATED) | OLFM3(O) / OLFM3(LDO) | 1 (same gar gene for both) | 2 | (blank) |

**Ensembl Compara disagrees.** Queried 2026-09-28 (recorded in the gene notes), it places the
olfm3a/olfm3b split at Gnathostomata. It gives olfm3b 1:1 orthologs in gar, human and medaka, and
gives olfm3a only a medaka ortholog. A gnathostome-level duplication would predict a second OLFM3
in tetrapods, which humans do not have. The human paralogs OLFM1 and OLFM2 are only 58-59%
identical to either zebrafish copy, while the two copies are 83% identical to each other. So
the Ensembl placement is most likely a gene-tree reconciliation artefact. Note also that the
Ensembl gar OLFM3 model is incomplete (375 aa;
[RESULTS.md](../../../../genes/DANRE/olfm3a/olfm3a-bioinformatics/RESULTS.md)).

**Synteny.** My own check supports duplicated segments
([RESULTS.md](../../../../genes/DANRE/olfm3a/olfm3a-bioinformatics/RESULTS.md), Synteny).
- olfm3a is on chr24 and olfm3b on chr2. Each lies about 130 kb from one member of the
  teleost-level paralogue pair abca4a/abca4b.
- Several other paralogue pairs link the two chromosomes: hs6st1, plppr4, agl, hccs and tlcd4a.
- This is independent of the gene tree and favours the PANTHER call over the Ensembl node. No
  background expectation was computed.

**Literature.** None on the pair.

**Status.** Supported by the strict PANTHER call, by pairwise identity, and by the shared abca4
neighbour on paralogous chromosomes. Contradicted by the Ensembl tree node, for reasons that are
plausibly technical. Treat TGD origin as probable, not certain.

## 2. Protein-level comparison

All numbers are from [RESULTS.md](../../../../genes/DANRE/olfm3a/olfm3a-bioinformatics/RESULTS.md).

- **Identity.** olfm3a vs olfm3b 83.2% identity and 92.3% similarity over 457 alignment columns. To human OLFM3 isoform Q96PB7-3 (458 aa):
  83.8% (olfm3a) and 81.0% (olfm3b). Both zebrafish entries share the N-terminus of that isoform,
  not of the 478-aa canonical isoform. The two entries therefore represent the same splice form.
  Human OLFM3 has alternative promoters:
  [PMID:16115881 "There are two major splice variants of the Optimedin mRNA, Optimedin A and Optimedin B, transcribed from different promoters."]
- **Domains.** Identity to human OLFM3 by region: coiled coil 85.1% / 82.3%, olfactomedin domain
  86.6% / 85.0%.
  - All six human cysteines are kept in both copies; olfm3b has two extra.
  - The four N-glycosylation sequons sit at identical positions in the two copies.
  - Both keep the residues matching mouse Olfm1 E404 and D453, a calcium site that the Olfm1
    structure paper says is shared with Olfm2 and Olfm3:
    [PMID:25903135 "These residues are the same in Olfm1 paralogs Olfm2 and Olfm3, whereas Glu404 and Asp453 are both asparagine in Olfm4."]
- **What the domains do.** In mammals the N-terminal region mediates homodimerization and the
  olfactomedin domain binds myocilin:
  [PMID:12019210 "The C-terminal olfactomedin domains are essential for interaction between optimedin and myocilin, while the N-terminal domains of both proteins are involved in the formation of protein homodimers."]
  The noelins also form heteromers with one another:
  [PMID:21228389 "Results of the present interaction study show that Olfm1, OLFM2, and Olfm3 proteins form heterodimers in the CLs and CM."]
- **Rates.** With gar as outgroup, 21 changes are unique to olfm3a and 32 to olfm3b (chi2 = 2.28,
  not significant). The gar model is partial, so this test covers only 375 positions.
- **Biochemistry.** No zebrafish noelin has been tested.

**Does each copy keep the ancestral molecular function?** Probably yes, on sequence grounds. That
function is itself only partly defined: it covers oligomerization, binding myocilin and joining
AMPA-receptor complexes.

## 3. Expression

No published in situ and no curated ZFIN expression exists for either copy. The only zebrafish
paper naming either gene lists olfm3a among effector genes of larval brain glutamatergic neurons:
[PMID:34895465 "The first case was a glutamatergic pair cluster from different brain regions: tectal glutamatergic Cluster 1 and hindbrain glutamatergic Cluster 31 shared effector gene profiles including camk2n1a/stmn4/cbln2b/olfm3a/cd63, but differentially expressed TF profiles, atf5b/bhlhe41/lhx1a and ddit3/cebpb/lef1, respectively (Figure 3C)."]

Public RNA-seq ([RESULTS.md](../../../../genes/DANRE/olfm3a/olfm3a-bioinformatics/RESULTS.md)):

- **Time course (E-ERAD-475, whole embryos, median TPM).** olfm3a is 0 until prim-15, then rises:
  2 at prim-25, 3 at long-pec, and 9-11 in 3-5-day larvae. olfm3b is 0-1 at every stage.
- **Bgee calls.**
  - olfm3a: brain, retina, larva, bone.
  - olfm3b: brain, intestine, early embryo, blastula, ovary, tail, bone, all with low scores.
  - Only brain and bone have calls for both copies.
- **Pre-duplication state.** Gar OLFM3 is highest in brain, ovary and eye, then heart, kidney,
  larva, embryo, bone, testis and muscle. In mammals OLFM3 is a brain, retina and anterior-eye
  protein:
  [PMID:12019210 "In the human eye, optimedin is expressed in the retina and the trabecular meshwork."]
  In mouse hippocampus it is a minor, interneuron-biased noelin:
  [PMID:37591201 "While mRNA coding for Noe1, the most abundantly detected transcript, was present in all types of excitatory and inhibitory neurons (pyramidal cells in CA1/CA3, granule cells and mossy cells in the dentate gyrus (DG)) and, to a small extent, even in glial cells (Figures S4, S5), transcripts for Noe2, Noe3 and Brorin appeared low in abundance and were preferentially found in interneurons (Figure 2A, Gad1-high in Figure S4)."]

**Reading.** olfm3a carries the ancestral larval neural and eye expression. olfm3b has calls in
ovary (ancestral) and intestine (no gar call) but not in retina. That is complementary, as a
partition would be. Two caveats weaken it. The olfm3b calls are weak, and a copy that has lost
most of its expression and is decaying toward pseudogenization would look the same.

## 4. Experimental evidence of function

- **olfm3a and olfm3b.** None: no mutants, morphants, rescue, or protein data.
- **Mammalian context.** The mouse Olfm3 single knockout is mild:
  [PMID:37591201 "The behavior of Noe3 KO mice appears normal and preliminary assessment of the brain sections found no defects."]
  The triple knockout of all three noelins is severe:
  [PMID:37591201 "Knock out of Noelins1-3 profoundly reduced AMPARs in synapses onto excitatory and inhibitory (inter)neurons, decreased their density and clustering in dendrites, and abolished activity-dependent synaptic plasticity."]
  So even a clean zebrafish olfm3a mutant might show little alone; the redundancy to test is with
  olfm1 and olfm2 as well as with the paralog.

## 5. Fate classification

**UNRESOLVED. The proteins are conserved. Expression differs, which suggests either an
asymmetric partition or decline of olfm3b. Confidence in any fate: low.**

**Established (sequence and public RNA-seq only)**
- Both copies keep all examined OLFM3 protein features.
- olfm3a is the predominant developmental copy, expressed in larval brain and retina.
- olfm3b is barely expressed before adulthood.

**Not established**
- Whether olfm3b has a real adult domain (intestine, ovary, particular brain nuclei), or is simply
  expressed at low levels.
- Any function of either copy.

**Why not the others.**
- PARTITION: would need in situ evidence of complementary domains, both present in gar.
- BACKUP or DOSAGE: would need mutants.
- INNOVATION: would need an olfm3b domain absent in gar and tetrapods. The intestine call is a
  candidate, but it is one weak RNA-seq call.

**What would change the call**
- Paralog-specific in situ in adult brain, retina, intestine and ovary. Complementary domains
  would support PARTITION; olfm3b detected nowhere reliably would point toward nonfunctionalization
  in progress.
- olfm3a and olfm3b mutants, alone and combined with other noelins, scored for AMPA-receptor
  clustering.

## 6. GO annotation consistency across the pair

Source: [annotation-comparison.md](annotation-comparison.md).

- **Shared rows.** Extracellular region (IBA and IEA), signal transduction (IBA) and synapse
  (IEA) are on both copies, from the same nodes and rules. There are no experimental rows.
- **Asymmetry from bookkeeping.** olfm3a alone has the two root-term ND rows, because its record
  was curated as having no data; olfm3b's record simply has no such rows. This is not biology.
- **Same actions.**
  - Extracellular region: accepted on both.
  - Signal transduction: marked over-annotated on both. It is seeded by myocilin and Olfm1, and
    no OLFM3 has evidence for it.
- **Deliberate difference: synapse.**
  - Accepted for olfm3a, which is expressed in larval glutamatergic neurons.
  - Kept as non-core for olfm3b, which is barely expressed in the developing nervous system.
  - This is a judgment on expression, not on the protein. It should be revisited if olfm3b turns
    out to have a real adult brain domain.
- **No NEW annotations.** Joining AMPA-receptor complexes is shown only for the noelins
  collectively in mouse, not for either zebrafish copy.

## 7. Open questions

- Is olfm3b expressed in any adult cell type at levels that suggest function, or is it decaying?
- Which medaka OLFM3 copy matches which zebrafish copy, and does medaka show the same
  asymmetry?
- Does the Ensembl gene tree change with a complete gar OLFM3 model?
- Do zebrafish noelins, including either olfm3 copy, co-purify with AMPA receptors?

## References

PMID:12019210, PMID:16115881, PMID:21228389, PMID:25903135, PMID:34895465, PMID:37591201. Also
the files `panther_tgd_pairs.tsv`, `batch3_sample.tsv`,
[annotation-comparison.md](annotation-comparison.md),
[RESULTS.md](../../../../genes/DANRE/olfm3a/olfm3a-bioinformatics/RESULTS.md) and
[output.txt](../../../../genes/DANRE/olfm3a/olfm3a-bioinformatics/output.txt).
