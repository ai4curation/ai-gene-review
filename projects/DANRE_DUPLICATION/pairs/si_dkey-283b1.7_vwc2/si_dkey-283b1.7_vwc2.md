---
title: "si:dkey-283b1.7 / vwc2"
autolink_gene_symbols: false
---

# si:dkey-283b1.7 / vwc2

[Back to pairs](../README.md)

**Bottom line:** UNRESOLVED, and the pair's TGD origin is itself doubtful. vwc2 (brorin) is a
well-conserved VWC2 ortholog with a morpholino-defined role as a secreted BMP antagonist in forebrain
development. si:dkey-283b1.7 is an unstudied, fast-evolving brorin-family protein. Its cysteine-rich
core is intact, but it lacks the VWC2 N-terminal region and is only 32.6% identical to vwc2.
Public data show expression in retina and brain. Only PANTHER calls the two genes TGD ohnologs.
Ensembl Compara relates them only at the Bilateria level, and the si:dkey-283b1.7 region shows no
conserved synteny with the gar vwc2 region. No fate can be assigned.

**Sample record:** fate=UNRESOLVED; level=protein; evidence=experimental_one; identity=32.6%

| | si:dkey-283b1.7 | vwc2 |
|---|---|---|
| UniProt | E7F8B1 (TrEMBL, 242 aa, PE 4 predicted) | B0I1T8 (TrEMBL, 309 aa) |
| Human ortholog | VWC2 per PANTHER (O); ambiguous by sequence (VWC2 or VWC2L); none per Ensembl Compara | VWC2 (PANTHER LDO; Ensembl one-to-one) |
| Chromosome | 3 | 13 |
| ZFIN | ZDB-GENE-120215-126 | ZDB-GENE-090313-315 (synonym brorin) |
| Ensembl | ENSDARG00000053460 | ENSDARG00000076495 |
| GOA rows | 5 (IEA/IBA only) | 7 (2 IMP) |
| Review | [genes/DANRE/si_dkey-283b1.7](../../../../genes/DANRE/si_dkey-283b1.7/si_dkey-283b1.7-ai-review.yaml) | [genes/DANRE/vwc2](../../../../genes/DANRE/vwc2/vwc2-ai-review.yaml) |

Drawn at random (draw 2, seed 20260928) from the 778 clean 1:1 `TGD_tree` pairs
(`batch3_sample.tsv`). The brorin-like gene vwc2l (ZDB-GENE-081104-169), the VWC2L ortholog, is a
separate gene and not part of this pair.

## 1. Evidence the pair comes from the TGD

**PANTHER.** The row in `panther_tgd_pairs.tsv` is:

| tgd_call | branch | class | family | human orthologs (a / b) | gar co-orthologs | medaka co-orthologs | medaka parallel dup |
|---|---|---|---|---|---|---|---|
| TGD_tree | Neopterygii\|Teleostei | 1:1 | PTHR46252 (BRORIN FAMILY MEMBER) | VWC2(O) / VWC2(LDO) | 1 (same gar gene for both) | 2 | (blank) |

**Independent checks** ([RESULTS.md](../../../../genes/DANRE/si_dkey-283b1.7/si_dkey-283b1.7-bioinformatics/RESULTS.md)):

- **Ensembl Compara disagrees.** It gives si:dkey-283b1.7 no gar or human ortholog, only a one-to-one
  medaka ortholog (Clupeocephala). It relates si:dkey-283b1.7 to vwc2 and to vwc2l only as "other
  paralogs" at the Bilateria level. vwc2 itself has one-to-one orthologs in gar and human.
- **No double-conserved synteny.** Within +/- 1.5 Mb, the vwc2 region (chr 13) shares fignl1, ikzf1 and
  the SPMIP7 ortholog with the gar vwc2 region (LG11). This fits the published vwc2 synteny:
  [PMID:28448525 "Zebrafish brorin is closely linked to the ikzf1 and fingl1 genes on chromosome 13, while mouse Brorin is closely linked to the Ikzf1 and Fingl1 genes at A2 on chromosome 2 (Fig 1B)."]
  None of the 51 gar-orthologous genes near si:dkey-283b1.7 (chr 3) maps to the gar vwc2 region, and no gene
  has orthologs in both zebrafish windows.
- **Literature.** No paper mentions si:dkey-283b1.7. The vwc2 paper establishes vwc2 as the Brorin
  ortholog and does not mention a second copy.

**Status.** The TGD origin of this pair rests on the PANTHER gene tree alone. Two lines of evidence fail
to support it, and one (Ensembl) contradicts it. The fast evolution of si:dkey-283b1.7 is the classic
setting for gene-tree artefacts in either direction (long-branch attraction; see the project background).
The pair is kept in the random sample as drawn, but it should be counted as "TGD not confirmed" when
estimating fate frequencies.

## 2. Protein-level comparison

Source: [RESULTS.md](../../../../genes/DANRE/si_dkey-283b1.7/si_dkey-283b1.7-bioinformatics/RESULTS.md) and
[annotation-comparison.md](annotation-comparison.md).

- **Identity.** 32.6% identity and 43.5% similarity over 340 alignment columns. That is the lowest identity
  in the project so far. It reflects different architecture as well as sequence divergence.
- **Architecture.** Both proteins have a signal peptide and the two VWFC (chordin-like) cysteine-rich
  domains. vwc2 keeps a VWC2-type N-terminal region, divergent in sequence as the authors note:
  [PMID:28448525 "While the 127-amino acid sequence of the amino-terminal region shares less similarity with that of mouse Brorin, the other regions of zebrafish Brorin and mouse Brorin are highly similar (~82% identity) (Fig 1A) [16]."]
  si:dkey-283b1.7 lacks that region almost entirely: 26 residues align to human VWC2 28-152, against 94 for
  vwc2. In length it resembles VWC2L (222-229 aa).
- **Core.** Both keep all 20 core cysteines of human VWC2. The vwc2 core is 83.6% identical to human VWC2
  and 89.3% to gar vwc2. The si:dkey-283b1.7 core is 54.9-59.8% identical to every vertebrate VWC2 and
  VWC2L, and 71.3% to its medaka ortholog. It is a fast-evolving lineage shared by zebrafish and medaka.
- **Biochemistry.** Only vwc2 has been tested. Injected brorin mRNA suppresses BMP signalling in the
  embryo:
  [PMID:28448525 "These results indicate that the overexpression of brorin leads to the inactivation of Bmp signaling."]
  [PMID:28448525 "These results indicate that Brorin inhibits Bmp signaling, but not canonical Wnt signaling."]
  The authors place the function in the core:
  [PMID:28448525 "Our results suggested that the functional region of Brorin was located in the core region containing the two cysteine-rich domains."]

**Does each copy keep the ancestral molecular function?** vwc2: yes, shown in vivo. si:dkey-283b1.7:
the core, which carries the activity, is intact in its cysteine framework but divergent in sequence.
Whether it antagonizes BMP is untested.

## 3. Expression

- **vwc2** is expressed predominantly in the developing nervous system, from 16 hpf:
  [PMID:28448525 "A low level of brorin expression was initially observed in the diencephalon primordium at 16 hpf (Fig 2B)."]
  [PMID:28448525 "At 36 hpf, brorin expression was detected in the ventral telencephalon, prethalamic/alar hypothalamic region, olfactory placode, hindbrain, and spinal cord (Fig 2H and 2I and data not shown)."]
  Bgee RNA-Seq also calls it in brain (the highest), head, larva, testis and bone.
- **si:dkey-283b1.7** has no in situ or published data. Bgee RNA-Seq calls it in retina (61.2), brain
  (58.2) and larva only.
- **Gar vwc2** (single copy) has RNA-Seq calls in eye (63.3), brain, mesonephros, liver and larva. Mouse
  Brorin is neural:
  [PMID:17400546 "Mouse Brorin was predominantly expressed in neural tissues in embryos and also predominantly expressed in the adult brain."]
- **Overlap.** Both zebrafish genes are called in brain and larva. Retina is called for si:dkey-283b1.7
  only, while gar vwc2 is expressed in the eye. That would fit an eye/retina domain retained by
  si:dkey-283b1.7, but a single present/absent call difference is too thin to call a partition, and
  Bgee lists present calls only.

## 4. Experimental evidence of function

**vwc2** (PMID:28448525; two non-overlapping splice-blocking morpholinos, mRNA rescue; no mutant):

- [PMID:28448525 "In brorin morphants, pSmad was increased in the dorsal region of the brain (MO1, n = 11/11 and MO2, n = 18/18)"]
- [PMID:28448525 "These results indicate that brorin is required for the development of the subpallial telencephalon."]
- [PMID:28448525 "We found that the co-injection of brorin RNA with brorin MO1 prevented the development of brain defects caused by brorin MO1 (n = 11/12) (Fig 3G)."]
- [PMID:28448525 "These results indicate that the knockdown of brorin affects axon guidance in the forebrain."]
- Both morpholinos match vwc2 perfectly and have 9-10 mismatches to si:dkey-283b1.7 (RESULTS.md), so they
  did not knock down the paralog.
- The authors discuss redundancy only with vwc2l, not with si:dkey-283b1.7:
  [PMID:28448525 "However, brorin and brorin-like may in part function redundantly during forebrain development."]

**si:dkey-283b1.7:** no data of any kind (no mutant, morphant, overexpression or ZFIN phenotype).

**Compensation:** none studied. No vwc2 mutant exists, so transcriptional adaptation cannot yet be
tested.

## 5. Fate classification

**UNRESOLVED. Confidence that the fate is unknowable from current data: high.**

- Only one copy has any functional data, and those are morpholino data.
- The paralog relationship itself is uncertain (section 1). If si:dkey-283b1.7 is not the TGD partner of
  vwc2, the pair is not an ohnolog pair, and "fate" does not apply as defined.
- What is established is protein-level divergence in si:dkey-283b1.7: loss of the N-terminal region and a
  fast-evolving core. That is recorded as `level=protein`. It is a structural observation, not a fate.
  It fits relaxed constraint after duplication, or a lineage with a separate, unknown function.
- *INNOVATION* would need a function for si:dkey-283b1.7 absent from gar vwc2. There is none.
  *PARTITION* would need complementary expression domains; there is at most a retina hint. *BACKUP*
  and *DOSAGE* are implausible at 32.6% identity with different architectures, but they have not been
  tested.

**What would change the call:** a phylogeny that includes non-teleost ray-finned fish (bichir, sturgeon,
bowfin) to settle the origin of si:dkey-283b1.7; in situ hybridization of both genes (and vwc2l) in eye
and brain; overexpression of si:dkey-283b1.7 mRNA to test BMP antagonism; stable mutants of both genes.

## 6. GO annotation consistency across the pair

Source: [annotation-comparison.md](annotation-comparison.md), after both reviews.

**Shared, and acceptable.** Every IBA and IEA row is on both genes, and each was given the same action on
both: extracellular region (ACCEPT), negative regulation of BMP signaling pathway (ACCEPT), AMPA
glutamate receptor complex and synapse (KEEP_AS_NON_CORE). The PAINT node (PTN002921765) sits above
both VWC2 and VWC2L. si:dkey-283b1.7 inherits these terms whichever branch it belongs to, so the IBA does
not depend on the disputed orthology. For si:dkey-283b1.7 these are the only annotations, and they are
untested. BMP antagonism in particular is the family default and should be confirmed.

**Asymmetric, and correctly so.** The two IMPs are on vwc2 only, and the morpholinos are vwc2-specific.
forebrain development (PMID:28448525) was accepted. It should not be propagated to si:dkey-283b1.7.

**Probably mis-assigned.** nervous system development (IMP, PMID:19852960) on vwc2 comes from the
Brorin-like (vwc2l) paper. The abstract describes knockdown of Brorin-like:
[PMID:19852960 "The inhibition of Brorin-like functions in zebrafish resulted in the impairment of neural development."]
The same group later wrote that brorin's role had not been studied:
[PMID:28448525 "However, the role of Brorin in early neural development has not yet been elucidated."]
I marked it UNDECIDED rather than REMOVE because the full text is not available. It is worth a
question to ZFIN.

**Missing.** No NEW terms were added. The zebrafish vwc2 data are morpholino phenotypes downstream of BMP
antagonism, and the core process is already covered by the accepted IBA.

## 7. Open questions

- Where does si:dkey-283b1.7 come from: a fast-evolving TGD copy of VWC2 (PANTHER), or an older lineage
  lost in tetrapods and gar (Ensembl Compara)? Is there a brorin-family gene in bichir or sturgeon that
  groups with it?
- Is si:dkey-283b1.7 a secreted BMP antagonist?
- Is si:dkey-283b1.7 expressed in a retinal cell type, and is that where gar vwc2 is expressed?
- Does ZFIN's nervous system development IMP on vwc2 (PMID:19852960) rest on a vwc2 experiment?
- Do stable vwc2 mutants reproduce the morphant phenotypes, and do vwc2 and vwc2l (not si:dkey-283b1.7)
  compensate for each other?

## References

PMID:17400546, PMID:19852960, PMID:28448525, PMID:37591201. Also the files `panther_tgd_pairs.tsv`,
[annotation-comparison.md](annotation-comparison.md) and
[si_dkey-283b1.7-bioinformatics/RESULTS.md](../../../../genes/DANRE/si_dkey-283b1.7/si_dkey-283b1.7-bioinformatics/RESULTS.md).
