---
title: "slc7a10a / slc7a10b"
autolink_gene_symbols: false
---

# slc7a10a / slc7a10b

[Back to pairs](../README.md)

**Bottom line:** UNRESOLVED, with an expression difference. Both copies keep every Asc-1 (SLC7A10) residue shown to
matter for substrate binding, gating and linking the 4F2hc heavy chain, so the proteins are probably equivalent
transporters. slc7a10a is broadly expressed and rises in larvae (brain, bone, heart, kidney, muscle and more).
slc7a10b is low, detected earlier in the embryo, and called mainly in brain, eye, bone and testis, which resembles the
gar pattern. The only functional data are for slc7a10b: loss-of-function fish gain more weight on overfeeding. The
other copy was not tested, and the ancestral tissue pattern is uncertain, so the fate cannot be called.

**Sample record:** fate=UNRESOLVED; level=expression; evidence=experimental_one; identity=77.8%

| | slc7a10a | slc7a10b |
|---|---|---|
| UniProt | G8JL19 (TrEMBL, 511 aa) | E7FE11 (TrEMBL, 517 aa) |
| Human ortholog | SLC7A10 (Asc-1) | SLC7A10 (Asc-1) |
| Chromosome | 7 | 25 |
| ZFIN | ZDB-GENE-080116-1 | ZDB-GENE-121105-2 |
| Ensembl | ENSDARG00000008100 | ENSDARG00000051730 |
| Mutant alleles | none published | loss-of-function line used for overfeeding (ZFIN genotype ZDB-GENO-211028-10; allele details not in the cached text) |
| Review | [genes/DANRE/slc7a10a](../../../../genes/DANRE/slc7a10a/slc7a10a-ai-review.yaml) | [genes/DANRE/slc7a10b](../../../../genes/DANRE/slc7a10b/slc7a10b-ai-review.yaml) |

This pair was drawn at random (batch 4, draw 18, seed 20260928) from the PANTHER `TGD_tree` 1:1 pairs and accepted
because Ensembl Compara dates the duplication to a teleost node (`random_sample.tsv`).

## 1. Evidence the pair comes from the TGD

**PANTHER.** The row in `panther_tgd_pairs.tsv` is:

| tgd_call | branch | class | family | human orthologs (a / b) | gar co-orthologs | medaka co-orthologs | medaka parallel dup |
|---|---|---|---|---|---|---|---|
| TGD_tree | Neopterygii\|Teleostei | 1:1 | PTHR11785 (AMINO ACID TRANSPORTER) | SLC7A10(O) / SLC7A10(LDO) | 1 (same gar gene for both) | 2 | (blank) |

**Ensembl Compara.** The duplication node is Osteoglossocephalai (`random_sample.tsv`), with one gar gene
(ENSLOCG00000001884) as a one-to-many orthologue of both. Herring, cavefish, pike, cod, medaka, stickleback, fugu and
tilapia each have one one-to-one orthologue of each copy (salmon has two of each, from the salmonid duplication);
the osteoglossomorph arowana has only an slc7a10a orthologue in Compara
([RESULTS.md](../../../../genes/DANRE/slc7a10a/slc7a10a-bioinformatics/RESULTS.md)).

**Synteny.** Weak. The copies lie on chromosomes 7 and 25. Within 1.5 Mb of each copy, only one teleost-level
paralogue pair (sall1a near slc7a10a, sall1b near slc7a10b) is shared, found in both directions
([output.txt](../../../../genes/DANRE/slc7a10a/slc7a10a-bioinformatics/output.txt), section 10). The flanking
regions have otherwise been rearranged, so local synteny gives little independent support.

**Status.** TGD origin is supported by the PANTHER `TGD_tree` call, the Compara teleost duplication node with a single
gar orthologue, and retention of both copies across the euteleost and otocephalan fishes in the panel. Double-conserved
synteny is not established (one shared paralogue pair). No published
phylogeny or synteny study of this pair was found.

## 2. Protein-level comparison

- **Identity.** 77.8% identity and 86.0% similarity over 523 columns
  ([annotation-comparison.md](annotation-comparison.md)). Against human SLC7A10: 69.0% (a) and 70.2% (b); both are
  closer to SLC7A10 than to its nearest paralog SLC7A8 (LAT2, about 61%). Against gar SLC7A10: 78.6% (a) and 80.2%
  (b). The zebrafish obesity study reported similar figures and chose slc7a10b on that basis:
  [PMID:36172277 "Moreover, Slc7a10b was chosen over Slc7a10a due to its slightly higher sequence identity (76% over 74%) with the human SLC7A10 (found using the T-coffee multiple sequence alignment tool (Notredame et al., 2000))."]
- **Rates.** slc7a10a has more lineage-specific changes than slc7a10b relative to gar (42 vs 25; chi2 4.31, P<0.05).
- **Functional residues.** The cryo-EM study of human Asc-1 tested pocket and gate residues by mutagenesis:
  [PMID:38589439 "Notably, E257A and R339A mutants also display almost no transport activity, indicating that the interaction between Glu257 and Arg339 is crucial for the transport cycle."]
  [PMID:38589439 "The F243A mutant exhibits nearly identical transport activity compared to the negative control, underscoring the pivotal role of Phe243."]
  and located the heavy-chain disulfide:
  [PMID:38589439 "The HAT-specific disulfide bond is found between Cys154 of Asc-1 and Cys211 of 4F2hc"]
  All ten positions (N52, Y131, I138, C154, F243, F250, Y253, E257, Y333, R339) are identical in slc7a10a, slc7a10b,
  gar, coelacanth and both medaka orthologues
  ([RESULTS.md](../../../../genes/DANRE/slc7a10a/slc7a10a-bioinformatics/RESULTS.md)).
- **Biochemistry.** Neither zebrafish protein has been expressed or assayed. Mammalian Asc-1 is a Na-independent
  exchanger of small neutral L- and D-amino acids:
  [PMID:10734121 "Asc-1 preferred small neutral amino acids such as Gly, L-Ala, L-Ser, L-Thr, and L-Cys, and alpha-aminoisobutyric acid as substrates."]
  [PMID:10734121 "Asc-1 also transported D-isomers of the small neutral amino acids, in particular D-Ser, a putative endogenous modulator of N-methyl-D-aspartate-type glutamate receptors, with high affinity."]

**Does each copy keep the ancestral molecular function?** Very likely both, by sequence; no protein-level divergence
is visible.

## 3. Expression

- **Development (E-ERAD-475, median TPM).** slc7a10b is detected from dome through segmentation (2-6 TPM) and stays at
  2-9 TPM; slc7a10a is near zero until hatching and rises to 19-29 TPM in larvae
  ([output.txt](../../../../genes/DANRE/slc7a10a/slc7a10a-bioinformatics/output.txt), section 7).
- **Adult and larval tissues (Bgee).** slc7a10a: 21 calls, highest in bone, brain, heart, mesonephros, larva and head
  kidney, plus muscle, testis, skin, swim bladder, granulocytes, intestine, gill, spleen, eye and liver. slc7a10b: 8
  calls (brain, testis, gastrula, blastula, head, larva, eye, bone), all lower than slc7a10a except blastula.
- **Other data.** An adult EST profile exists for slc7a10a only:
  [PMID:34338990 "slc7a10a (Chr 7)Developmental stage|adultAdult|heart > kidney > brain > eye---slc7a10b (Chr 25)----"]
  slc7a10b appears among transporters enriched in arachnoid cells of the zebrafish meninges:
  [PMID:35805100 "solute transporter Slc6a13 (GABA transporter), and many other SLC transporters (SLC1A2B, SLC1A3B, SLC3A2A SLC4A4, SLC6A1B, SLC6A9, SLC6A10, SLC7A10B, SLC27A1B) (Figure 6)."]
  ZFIN has no curated expression for either copy.
- **Pre-duplication state.** Gar SLC7A10 has Bgee calls in brain, eye, bone, ovary, larva, embryo, testis and skin,
  and none in heart, intestine, liver, mesonephros, muscle or gill, although Bgee samples all of these in gar
  ([bgee_gar_coverage.txt](../../../../genes/DANRE/agxta/agxta-bioinformatics/bgee_gar_coverage.txt)). This
  resembles slc7a10b. But mammalian Asc-1 is also expressed outside the nervous system
  [PMID:10734121 "Asc-1 mRNA was detected in the brain, lung, small intestine, and placenta."],
  so the broad slc7a10a pattern could be ancestral and missed in gar, or a teleost gain.

The copies differ clearly in level and breadth, but whether this is a partition of an ancestral pattern, a gain of
tissues by slc7a10a, or a decline of slc7a10b cannot be told from bulk data.

## 4. Experimental evidence of function

**slc7a10a.** None.

**slc7a10b.** A loss-of-function line was overfed for two months:
[PMID:33408126 "Concordantly, loss of Slc7a10 function in zebrafish in vivo accelerates diet-induced body weight gain and adipocyte enlargement."]
[PMID:36172277 "Compared to wildtypes, the fish with impaired Slc7a10b function gained 38% more body weight and had on average 49% larger visceral adipocytes"]
The authors note that the line keeps slc7a10a:
[PMID:36172277 "Because two isoforms of Slc7a10 exist in zebrafish (Slc7a10a as well as Slc7a10b), this model should be considered a partial global knockout of Slc7a10."]
The primary paper is cached as abstract only, so the allele type (and whether it could trigger transcriptional
adaptation of slc7a10a) is not recorded here. No double mutant, slc7a10a mutant, rescue or cross-rescue has been
reported. Neither copy has been tested for the glycinergic (startle, motor) role that makes mouse Slc7a10 essential:
[PMID:25755256 "Asc-1 works as a glycine and L-serine transporter, and its transport activity is required for the subsequent conversion of L-serine into glycine in vivo."]

## 5. Fate classification

**UNRESOLVED. Protein conserved in both copies; clear difference in expression level and breadth.**

**Established**

- Both proteins keep all tested Asc-1 functional residues.
- slc7a10a is the broadly expressed, larval-rising copy; slc7a10b is low and narrow (brain, eye, bone, testis, early
  embryo).
- slc7a10b loss of function has a phenotype (diet-induced weight gain, adipocyte enlargement), so slc7a10a does not
  fully cover for it in that setting.

**Not established**

- Whether the ancestral (pre-TGD) expression was broad or neural. Gar Bgee calls favour neural/gonadal, mammalian
  data favour broad.
- Whether slc7a10a has a phenotype, and whether the two copies overlap in adipocytes or in the glycinergic CNS.
- Allele type and paralog compensation in the slc7a10b line.

**Why not a call**

- *PARTITION* would need slc7a10b-only domains that slc7a10a lacks; bulk data show none (slc7a10b-only Bgee call:
  gastrula).
- *INNOVATION* (expression gain by slc7a10a) would need the ancestral pattern to be neural-only; gar suggests it,
  mammals argue against it.
- *BACKUP/DOSAGE* would need evidence that the copies overlap and substitute for each other; the slc7a10b phenotype
  argues against full redundancy, but its adipose expression relative to slc7a10a is unknown.

**What data would decide it:** paralog-specific in situ or single-cell data in adult adipose tissue, CNS and heart;
gar or bowfin SLC7A10 in situ; slc7a10a and double mutants tested for adiposity and startle; qPCR of slc7a10a in the
slc7a10b mutant.

## 6. GO annotation consistency across the pair

Source: [annotation-comparison.md](annotation-comparison.md), after both reviews.

**Shared, and correctly so.** All ten IBA and IEA rows (plasma membrane; neutral L-amino acid and L-amino acid
transporter activity; D-alanine and D-serine transmembrane transport; the general transport terms) are identical on
both copies and were accepted on both. The IBA propagation treats the pair as equivalent, which fits the conserved
protein.

**Asymmetric because of which copy was studied.** Energy homeostasis (IMP) is on slc7a10b only, because only slc7a10b
was knocked out. It was kept as non-core: the phenotype is real but organism-level. Nothing indicates that slc7a10a
lacks this role.

**Should be copy-specific:** nothing yet. **Should be shared:** the transporter activity, plasma membrane location and
D-serine/D-alanine transport.

## 7. Open questions

- Which copy is expressed in zebrafish adipocytes, and in glycinergic astrocytes of the hindbrain and spinal cord?
- Do slc7a10a mutants or double mutants show adiposity or startle phenotypes?
- Is the broad slc7a10a expression ancestral? Gar or bowfin in situ data would settle this.
- Which slc3a2 paralog partners each copy?

## References

PMID:10734121, PMID:25755256, PMID:33408126, PMID:34338990, PMID:35805100, PMID:36172277, PMID:38589439. Also
`panther_tgd_pairs.tsv`, `random_sample.tsv`, [annotation-comparison.md](annotation-comparison.md),
[slc7a10a-bioinformatics/RESULTS.md](../../../../genes/DANRE/slc7a10a/slc7a10a-bioinformatics/RESULTS.md),
[output.txt](../../../../genes/DANRE/slc7a10a/slc7a10a-bioinformatics/output.txt) and
[bgee_gar_coverage.txt](../../../../genes/DANRE/agxta/agxta-bioinformatics/bgee_gar_coverage.txt).
