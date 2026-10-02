---
title: "abi1a / abi1b"
autolink_gene_symbols: false
---

# abi1a / abi1b

[Back to pairs](../README.md)

**Bottom line:** UNRESOLVED, with a clear temporal expression split. The two ABI1 proteins
are conserved in every region known to carry function, and neither is evolving faster.
abi1b is the main maternal and cleavage-stage transcript, and abi1a takes over from
mid-gastrulation and is expressed across adult tissues, as the single gar ABI1 is. This fits an
expression PARTITION. But whether gar ABI1 is maternally loaded is unknown, and neither copy has
a loss-of-function test beyond one mosaic F0 knockdown of abi1a with no heart phenotype. So the
fate cannot be called.

**Sample record:** fate=UNRESOLVED; level=expression; evidence=expression_only; identity=79.2%

| | abi1a | abi1b |
|---|---|---|
| UniProt | A0A8M3AND6 (TrEMBL; RefSeq isoform X1, 522 aa) | A0A286YAJ7 (TrEMBL; RefSeq isoform X1, 507 aa) |
| Human ortholog | ABI1 | ABI1 |
| Chromosome | 24 | 2 |
| ZFIN | ZDB-GENE-040426-1701 | ZDB-GENE-060929-1182 |
| Ensembl | ENSDARG00000010155 | ENSDARG00000062991 |
| Review | [genes/DANRE/abi1a](../../../../genes/DANRE/abi1a/abi1a-ai-review.yaml) | [genes/DANRE/abi1b](../../../../genes/DANRE/abi1b/abi1b-ai-review.yaml) |

This pair was drawn at random (batch 3, draw 7, seed 20260928) from the 778 clean 1:1
`TGD_tree` pairs (`batch3_sample.tsv`).

## 1. Evidence the pair comes from the TGD

**PANTHER.** The row in `panther_tgd_pairs.tsv` is:

| tgd_call | branch | class | family | human orthologs (a / b) | gar co-orthologs | medaka co-orthologs | medaka parallel dup |
|---|---|---|---|---|---|---|---|
| TGD_tree | Neopterygii\|Teleostei | 1:1 | PTHR10460 (ABL INTERACTOR FAMILY MEMBER) | ABI1(LDO);ABI3(O) / ABI1(O);ABI3(O) | 1 (same gar gene for both) | 2 | (blank) |

PANTHER places the duplication after the split from gar and before the zebrafish-medaka split,
with one gar co-ortholog and two medaka copies. The ABI3 entries in the human-ortholog column are
PANTHER's broader orthology calls; by sequence both copies are ABI1 orthologs (81.6% and 77.5%
identical to human ABI1, about 36% to ABI3;
[RESULTS.md](../../../../genes/DANRE/abi1a/abi1a-bioinformatics/RESULTS.md)).

**Ensembl Compara** agrees: it places the abi1a/abi1b duplication at Clupeocephala (the
zebrafish-medaka ancestor) and gives each copy a different 1:1 medaka ortholog, with the gar gene
as a one-to-many ortholog of both (queried 2026-09-28; recorded in the gene notes).

**Synteny.** My own check found no conserved microsynteny
([RESULTS.md](../../../../genes/DANRE/abi1a/abi1a-bioinformatics/RESULTS.md), Synteny).
- abi1a is on chr24 and abi1b on chr2.
- None of the neighbours within 1.5 Mb of one copy has a teleost-level paralogue within 1.5 Mb of
  the other.
- The three teleost-level paralogue pairs from the abi1a neighbourhood all have their partner on
  chr2, but far from abi1b: kmt2ca/kmt2cb, agtr1b/agtr1a, and one unnamed pair.
- This chromosome-level signal is weak and was not tested against a background.

**Literature.** One paper mentions that zebrafish has two ABI1 copies, without an origin
analysis:
[PMID:32368696 "Zebrafish, unlike mouse or human, have 2 orthologs for ABI1 (abi1a and abi1b) with abi1b likely compensating to maintain normal cardiac development."]

**Status.** TGD origin is supported by two independent gene-tree methods. No published synteny
study covers the pair.

## 2. Protein-level comparison

All numbers are from [RESULTS.md](../../../../genes/DANRE/abi1a/abi1a-bioinformatics/RESULTS.md)
and [annotation-comparison.md](annotation-comparison.md).

- **Identity.** abi1a vs abi1b 79.2% identity and 84.5% similarity over 543 alignment columns. To human ABI1: abi1a 81.6%, abi1b 77.5%.
- **Domains.** Both have the ABI architecture: the N-terminal WAVE-binding region, a coiled coil,
  a proline-rich disordered middle and a C-terminal SH3 domain. Identity to human ABI1 by region:

  | Region (human numbering) | abi1a | abi1b | gar |
  |---|---|---|---|
  | WAVE-binding N-terminus (18-79) | 95.2% | 91.9% | 95.2% |
  | Coiled coil (45-107) | 100% | 100% | 100% |
  | Disordered middle (159-421) | 76.8% | 70.7% | 88.2% |
  | SH3 (446-505) | 90.0% | 91.7% | 91.7% |

  Tyrosines at human Y53, Y213 (the ABL phosphorylation site) and Y455 are kept in both.
- **What these regions do in mammals.** The N-terminus binds WAVE and builds the complex:
  [PMID:15048123 "Abi1 interacts directly with the WHD domain of WAVE2, increases WAVE2 actin polymerization activity and mediates the assembly of a WAVE2-Abi1-Nap1-PIR121 complex."]
  In the structure, the Abi N-terminal helices form a four-helix bundle with WAVE and HSPC300:
  [PMID:21107423 "A long four-helix bundle created by a helix from HSPC300 (residues 14-68), two helices from Abi2 (residues 1-39 and 43-112) and a helix from WAVE1 (residues 26-81) contacts Sra1 extensively and is aligned roughly parallel to the long axis of the dimer (Supplementary Figs."]
  The SH3 domain binds Abl:
  [PMID:7590237 "The protein exhibits sequence similarity to homeotic genes, contains several polyproline stretches, and includes a src homology 3 (SH3) domain at its very carboxyl terminus that is required for binding to Abl proteins."]
- **Differences.** Divergence is concentrated in the disordered middle. abi1b's predicted isoform
  has a 13-residue N-terminal extension that has not been checked against cDNA.
- **Rates.** With gar as outgroup, 17 changes are unique to abi1a and 28 to abi1b (chi2 = 2.69,
  not significant).
- **Biochemistry.** No zebrafish ABI protein has been tested biochemically or in cross-rescue.

**Does each copy keep the ancestral molecular function?** Probably yes. The inference rests on
sequence alone: the WAVE-complex and SH3 regions are conserved in both.

## 3. Expression

No published in situ or curated ZFIN expression exists for either copy. ZFIN's only record is an
abi1a high-throughput in situ annotated to an unspecified structure. The data below come from
public RNA-seq ([RESULTS.md](../../../../genes/DANRE/abi1a/abi1a-bioinformatics/RESULTS.md)).

- **Temporal split (E-ERAD-475, whole embryos, median TPM).**

  | Stage | abi1a | abi1b |
  |---|---|---|
  | 128-cell | 5 | 28 |
  | 1k-cell | 4 | 26 |
  | dome | 2 | 16 |
  | shield | 13 | 9 |
  | 75% epiboly | 26 | 6 |
  | 1-4 somites to 5 dpf | 22-36 | 3-7 |

  abi1b dominates the maternal and cleavage-stage pool. abi1a dominates from mid-gastrulation.
- **Tissues (Bgee "expressed" calls).** abi1a has RNA-seq calls in many adult tissues: gill,
  intestine, skin, spleen, liver, eye, kidney, muscle, testis, brain and retina. abi1b has calls
  only in early embryo, larva, brain, retina, ovarian follicle and bone. No tissue has an abi1b-only
  call. Bgee returns only positive calls, so a missing call is not proof of absence.
- **Pre-duplication state.** Gar ABI1 has 14 Bgee expressed calls (skin, eye, liver, kidney,
  testis, intestine, brain, bone, heart, embryo, ovary, gill, muscle, larva). Mammalian
  Abi1 is also broadly expressed:
  [PMID:7590237 "The gene is widely expressed in the mouse, with highest levels of mRNA found in the bone marrow, spleen, brain, and testes."]
  So broad adult expression is ancestral, and abi1a resembles the ancestor in breadth. Whether
  the ancestor was also maternally loaded is unknown: the gar data have no cleavage-stage samples.

## 4. Experimental evidence of function

**abi1a.** One test only: a mosaic F0 CRISPR knockdown in a congenital-heart-disease follow-up.
- [PMID:32368696 "Briefly, wild-type AB strain zebrafish embryos were injected at the 1- to 2-cell stage with zebrafish-optimized Cas9 protein and CRISPR RNAs targeting abi1, brk1, cyfip1 cul3a, nckap1, racgap1, or wasf2."]
- The result was no cardiac phenotype:
  [PMID:32368696 "Finally, loss of cyfip1 and abi1a, unlike the other WAVE2 complex genes, was not found to impact zebrafish heart development."]
- This is not a germline allele. The table reports 1/72 embryos with reversed looping, and no
  allele type or mRNA-decay data are given.

**abi1b.** No experiments. The claim that it compensates for abi1a is the authors' speculation
(quoted in section 1).

**Both copies.** No double mutants, no cross-rescue, and no expression data from mutants.

**Mammalian context, for what a loss might look like.** Mouse Abi1 knockouts die at mid-gestation
with heart and brain defects:
[PMID:21482783 "Thus, Abi1-signaling events are not required for gastrulation but are critical during brain and heart development."]
The mouse paralog Abi2 does not rescue this:
[PMID:21482783 "This finding suggests that the presence of Abi1 is critical for the integrity and stability of WAVE complex and that Abi2 levels are not sufficiently increased to compensate fully for the loss of Abi1 in KO cells and to restore the integrity and function of the WAVE complex."]
A normal heart after mosaic abi1a knockdown is therefore uninformative. Maternal abi1b, zygotic
abi1b, or incomplete mosaic loss could each explain it.

## 5. Fate classification

**UNRESOLVED. Expression diverges; the protein appears conserved. Confidence that there is a
real temporal split: moderate. Confidence in any fate: low.**

**Established**
- The proteins are conserved in WAVE-binding, coiled-coil and SH3 regions, and neither copy
  evolves significantly faster (sequence analysis only).
- The copies are expressed at different times: abi1b is maternal and early, abi1a zygotic and
  later (one RNA-seq time course).
- abi1a has broad adult tissue expression like gar ABI1; abi1b has few adult calls.

**Not established**
- The ancestral temporal profile. If gar ABI1 is both maternal and zygotic, this is a temporal
  PARTITION. If gar ABI1 is only zygotic, abi1b gained maternal loading (a regulatory innovation)
  and abi1a kept the ancestral pattern.
- Any function. Nothing shows that either copy is required, that they are redundant, or that
  Abi1b makes WAVE complexes in vivo.

**Why not the others.** PARTITION is the leading hypothesis but needs the gar or tetrapod
maternal state and a phenotype. BACKUP and DOSAGE need mutant data that do not exist; the
compensation claim is untested. INNOVATION has no protein-level support.

**What would change the call**
- Gar (or bichir) cleavage-stage RNA-seq showing whether ancestral ABI1 is maternally loaded.
- Maternal-zygotic abi1b and zygotic abi1a mutants, single and double, scored for gastrulation
  movements and for levels of the WAVE-complex protein.
- A cross-rescue of the mutant with the paralog's coding sequence.

## 6. GO annotation consistency across the pair

Source: [annotation-comparison.md](annotation-comparison.md).

- **Identical inputs.** Both copies carry the same 8 GOA rows: 5 IBA from the same PANTHER nodes
  and 3 SubCell IEA. There are no experimental rows, so no asymmetry comes from which copy was
  studied.
- **Identical actions.**
  - Accepted: SCAR complex, signaling adaptor activity, lamellipodium (IBA and IEA),
    actin-based cell projection and cytoskeleton.
  - Kept as non-core: neuron migration (seeded by mouse Abi2) and filopodium.
  - Shared IBA propagation is appropriate here: the protein is conserved and there is no
    copy-specific loss.
- **Missing from both.** The zygotic/maternal split is not reflected in GO, and should not be:
  GO does not annotate expression timing.
- **No NEW annotations** were added. The F0 knockdown gives no phenotype to annotate, and the
  mammalian roles in heart and brain development were not transferred.

## 7. Open questions

- Is gar or bichir ABI1 maternally loaded?
- Do maternal-zygotic abi1b mutants have gastrulation or cell-migration defects, and does abi1a
  rise when abi1b transcripts decay?
- Does the abi1b N-terminal extension exist in vivo?
- Do both proteins join WAVE complexes (with wasf2, nckap1, cyfip1) in tissues where both are
  expressed, such as brain and retina?

## References

PMID:7590237, PMID:15048123, PMID:21107423, PMID:21482783, PMID:32368696. Also the files
`panther_tgd_pairs.tsv`, `batch3_sample.tsv`, [annotation-comparison.md](annotation-comparison.md),
[RESULTS.md](../../../../genes/DANRE/abi1a/abi1a-bioinformatics/RESULTS.md) and
[output.txt](../../../../genes/DANRE/abi1a/abi1a-bioinformatics/output.txt).
