---
title: "tusc2a / tusc2b"
autolink_gene_symbols: false
---

# tusc2a / tusc2b

[Back to pairs](../README.md)

**Bottom line:** UNRESOLVED. Neither copy of the small mitochondrial protein TUSC2 (FUS1) has ever been
studied in zebrafish. Both keep the two features known to matter: the myristoylated Gly2 and the
exact calcium-binding motif DEDGDLAHEFYEE. Neither is evolving faster. The copies differ in expression
level and timing: tusc2a is mainly a maternal transcript and a low-level adult copy with its highest
calls in gonads, while tusc2b is the main zygotic copy and is higher in most adult tissues. A gar
bridge shows double conserved synteny, so this is a genuine TGD pair. With no functional data, the
fate cannot be called.

**Sample record:** fate=UNRESOLVED; level=expression; evidence=expression_only; identity=80.2%

| | tusc2a | tusc2b |
|---|---|---|
| UniProt | Q08BH0 (TrEMBL, zgc:153746, 111 aa) | Q6DH03 (TrEMBL, zgc:92701, 111 aa) |
| Human ortholog | TUSC2 (FUS1) | TUSC2 (FUS1) |
| Chromosome | 6 | 22 |
| ZFIN | ZDB-GENE-061013-612 | ZDB-GENE-040718-99 |
| Ensembl | ENSDARG00000099817 | ENSDARG00000025340 |
| Review | [genes/DANRE/tusc2a](../../../../genes/DANRE/tusc2a/tusc2a-ai-review.yaml) | [genes/DANRE/tusc2b](../../../../genes/DANRE/tusc2b/tusc2b-ai-review.yaml) |

This pair was drawn at random (batch 4, draw 30, seed 20260928) from the PANTHER `TGD_tree` 1:1
pairs and accepted because Ensembl Compara places the duplication at a teleost node
(`random_sample.tsv`, compara_level Osteoglossocephalai).

## 1. Evidence the pair comes from the TGD

**PANTHER.** The row in `panther_tgd_pairs.tsv` is:

| tgd_call | branch | class | family | human orthologs (a / b) | gar co-orthologs | medaka co-orthologs | medaka parallel dup |
|---|---|---|---|---|---|---|---|
| TGD_tree | Neopterygii\|Teleostei | 1:1 | PTHR15453 (TUMOR SUPPRESSOR CANDIDATE 2) | TUSC2(LDO) / TUSC2(O) | 1 (same gar gene for both) | 2 | (blank) |

**Ensembl Compara** places the duplication at Osteoglossocephalai, gives gar ENSLOCG00000014230 as a
one-to-many orthologue of both copies, and gives each copy its own one-to-one medaka orthologue
(recorded in the tusc2a notes). Because the protein is only about 110 residues, the sequence
distances to the two medaka copies differ by just a few residues and do not by themselves resolve
the tree ([RESULTS.md](../../../../genes/DANRE/tusc2a/tusc2a-bioinformatics/RESULTS.md)).

**Synteny (my check).** Comparing the neighbourhoods of the two copies directly finds no shared
paralogous neighbours. The gar bridge does
([RESULTS.md](../../../../genes/DANRE/tusc2a/tusc2a-bioinformatics/RESULTS.md), Synteny;
[gar_bridge_output.txt](../../../../genes/DANRE/tusc2a/tusc2a-bioinformatics/gar_bridge_output.txt)):

- Gar TUSC2 is on LG5; 47 of its 52 protein-coding neighbours within 1 Mb have zebrafish
  orthologues.
- Near tusc2a (chr6): hyal1, hyal2a, cacna2d2a, mst1 and one more, within 3 Mb.
- Near tusc2b (chr22): bap1, rad54l2, cyb561d2, rassf1, hyal2b and abhd14a, all within about 70 kb
  of tusc2b.
- The gar hyal2 neighbour has one zebrafish orthologue beside each copy (hyal2a beside tusc2a,
  hyal2b beside tusc2b).

The gar region is split between two zebrafish chromosomes, each with one tusc2 copy and a different
share of the ancestral neighbours. This is double conserved synteny.

**Literature.** No paper analyses the pair.

**Status.** TGD origin is well supported: PANTHER `TGD_tree`, a teleost-level Compara node and
double conserved synteny through gar.

## 2. Protein-level comparison

- **Identity.** 80.2% identity and 86.5% similarity over 111 columns
  ([annotation-comparison.md](annotation-comparison.md)). tusc2a is 70.3% and tusc2b 65.8%
  identical to human TUSC2; 81.2% and 77.7% to gar.
- **Functional features.** Both copies begin MGGSGSK, so the N-myristoyl glycine (Gly2 in human)
  is kept. Both carry the exact calcium-binding motif DEDGDLAHEFYEE at residue 55, as do human,
  gar and both medaka copies. The residue matching human phosphoserine Ser50 is Ser in both
  ([RESULTS.md](../../../../genes/DANRE/tusc2a/tusc2a-bioinformatics/RESULTS.md)).
- **Why these features matter.** Myristoylation is needed for the mitochondrial location:
  [PMID:35181743 "Also, myristoylation-deficient FUS1/TUSC2 loses its characteristic mitochondria/ER localization and its abilities to induce apoptosis and suppress tumor cell proliferation in vitro."]
  The acidic motif is the most conserved part of the family:
  [PMID:42314984 "Because TUSC2 is a small and otherwise weakly conserved protein, searches were guided by conservation of the acidic calcium-binding motif region, including the canonical DEDGDLAHEFYEE sequence and related D-x-D-x-D-containing variants, which represent the most evolutionarily conserved region of the protein family."]
- **Rate.** Against gar, 5 changes are unique to tusc2a and 9 to tusc2b (not significant).
- **No biochemical data** exist for either zebrafish protein.

**Does each copy keep the ancestral molecular function?** Probably yes, on sequence grounds: every
feature known to matter is intact in both. Note that the molecular activity of TUSC2 itself is not
settled; in mammals it is defined by its effect on mitochondrial calcium uptake:
[PMID:24328503 "Fus1 loss resulted in reduced rate of mitochondrial calcium uptake in calcium-loaded epithelial cells, splenocytes, and activated CD4(+) T cells."]

## 3. Expression

- **Development (E-ERAD-475, whole embryo).** tusc2a is the larger transcript in the zygote (26
  versus 10 TPM) but falls to 5-6 TPM in the blastula and 1-2 TPM at gastrulation, then recovers only
  to 14-18 TPM in larvae. tusc2b rises from 10 TPM in the zygote to 26-51 TPM from the blastula to day
  5. From the blastula on, tusc2b is the main copy (15- to 26-fold higher at gastrulation)
  ([RESULTS.md](../../../../genes/DANRE/tusc2a/tusc2a-bioinformatics/RESULTS.md)).
- **Adult tissues (Bgee).** tusc2a has no RNA-Seq call that tusc2b lacks; tusc2b alone has heart,
  ovary and tail. Of 25 entities called for both, tusc2b scores higher in 21. tusc2a's highest scores
  are testis (89.7) and mature ovarian follicle (87.3); tusc2b's are muscle, somite and liver.
- **ZFIN.** tusc2a has no curated expression. tusc2b has one whole-organism in situ row (zygote to
  pec-fin), with no restricted domain.
- **Pre-duplication state.** Gar TUSC2 has Bgee calls in 14 tissues, highest in eye, muscle and
  brain, so broad expression is ancestral. No gar developmental time course was available.

There is no tissue that belongs to one copy only. tusc2b looks like the broadly expressed,
gar-like copy; tusc2a is lower almost everywhere, with a maternal bias and relatively high gonad
expression.

## 4. Experimental evidence of function

None for either copy. Europe PMC searches for `"tusc2a"`, `"tusc2b"` and zebrafish TUSC2/FUS1 found
no zebrafish study (only one fish transcriptome that lists tusc2a). No mutant, morphant, rescue or
localization data exist. In mouse, loss of Tusc2 causes chronic inflammation and changes
mitochondrial parameters:
[PMID:22513871 "Untreated Fus1(-/-) mice had an ~eight-fold higher proportion of peritoneal granulocytes than Fus1(+/+) mice, pointing at ongoing chronic inflammation."]

## 5. Fate classification

**UNRESOLVED; the observed difference is at the level of expression. Confidence in any fate: low.**

**Established**

- TGD origin (double conserved synteny through gar).
- Both proteins keep the myristoylation site and the calcium-binding motif, and evolve at the same
  rate.
- tusc2b is the main zygotic copy and the higher copy in most adult tissues; tusc2a is the larger
  maternal transcript and is relatively high in testis and ovary.

**Not established**

- Whether the maternal bias of tusc2a is a partition of an ancestral maternal-plus-zygotic profile
  (no gar time course).
- Whether both proteins go to mitochondria and regulate calcium uptake.
- Whether losing either copy has any phenotype.

**Readings the data allow**

- *PARTITION (temporal):* tusc2a keeps the maternal phase and tusc2b the zygotic phase. This fits the
  time course, but adult expression overlaps almost completely.
- *DOSAGE or quantitative sharing:* both copies together give the TUSC2 dose, with tusc2b supplying
  most of it.
- *Decline of tusc2a:* a low, conserved copy on the way to loss would look similar, although its
  sequence is under the same constraint as tusc2b.

**What would change the call**

- A gar (or bowfin) developmental time course with maternal and zygotic stages.
- Maternal-zygotic tusc2a and zygotic tusc2b mutants, and a double mutant, scored for mitochondrial
  calcium uptake and membrane potential.
- Cross-rescue with each coding sequence.

## 6. GO annotation consistency across the pair

Source: [annotation-comparison.md](annotation-comparison.md), after both reviews.

The two copies have identical GOA sets (ND molecular function plus three IBA rows from mouse Tusc2),
and I reviewed them identically:

- mitochondrion and regulation of mitochondrial membrane potential: accepted on both; both keep the
  features that give TUSC2 its mitochondrial location.
- inflammatory response: marked as over-annotated on both. The mouse phenotype is a downstream
  consequence of mitochondrial dysfunction, and the protein does not carry out the inflammatory
  response. Recorded with a propagation_review (root cause TERM_SCOPING_PROBLEM, failure mode
  ROLE_CONFLATION).
- ND molecular function: accepted on both, since no activity has been measured for TUSC2 in any
  species; calcium binding is predicted from the motif.

**Should be copy-specific:** nothing on present evidence. **Should be shared:** all rows. IBA
propagation treats the pair as equivalent, which matches the protein evidence.

## 7. Open questions

- Do both zebrafish Tusc2 proteins localize to mitochondria and regulate mitochondrial calcium uptake?
- Is tusc2a's maternal bias ancestral or derived? What does gar TUSC2 expression look like in early
  embryos?
- Is the relatively high expression of tusc2a in gonads a real specialization (for example, in germ
  cells)?

## References

PMID:22513871, PMID:24328503, PMID:35181743, PMID:42314984. Also `panther_tgd_pairs.tsv`,
`random_sample.tsv`, [annotation-comparison.md](annotation-comparison.md),
[tusc2a-bioinformatics/RESULTS.md](../../../../genes/DANRE/tusc2a/tusc2a-bioinformatics/RESULTS.md),
[output.txt](../../../../genes/DANRE/tusc2a/tusc2a-bioinformatics/output.txt) and
[gar_bridge_output.txt](../../../../genes/DANRE/tusc2a/tusc2a-bioinformatics/gar_bridge_output.txt).
