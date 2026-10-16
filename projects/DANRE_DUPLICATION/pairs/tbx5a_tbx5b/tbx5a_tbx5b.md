---
title: "tbx5a / tbx5b"
autolink_gene_symbols: false
---

# tbx5a / tbx5b

[Back to pairs](../README.md)

**Bottom line:** MIXED. In the heart and pectoral fin, each copy is required and neither can stand in for
the other. So this is not backup: both copies are essential and non-redundant. The pectoral fin role is
split between them. tbx5a alone starts the fin bud; tbx5b is needed later, for timed outgrowth and
medio-lateral migration of fin-field cells. tbx5b has weak or no fin expression. Both copies are required
for cardiac looping. In the retina they act additively, but this is shown with morpholinos only.

Unlike pax6a/pax6b, the proteins have diverged a lot: 49% identity overall and 83% in the T-box. Injected
mRNA of one copy does not rescue loss of the other. That points to protein-level divergence, but this is
inferred: no coding-sequence swap or side-by-side biochemical assay has been done.

| | tbx5a | tbx5b |
|---|---|---|
| UniProt | Q9IAK8 (Swiss-Prot, 492 aa) | E3W6T6 (TrEMBL, 422 aa) |
| Human ortholog | TBX5 | TBX5 |
| Former names | heartstrings (hst), tbx5, tbx5.1 | (none; described in 2010) |
| ZFIN | ZDB-GENE-991124-7 | ZDB-GENE-060601-2 |
| Review | [genes/DANRE/tbx5a](../../../../genes/DANRE/tbx5a/tbx5a-ai-review.yaml) | [genes/DANRE/tbx5b](../../../../genes/DANRE/tbx5b/tbx5b-ai-review.yaml) |

## 1. Evidence the pair comes from the TGD

**PANTHER.** The row in `panther_tgd_pairs.tsv` (family PTHR11267, T-BOX PROTEIN-RELATED) is:

| tgd_call | branch | class | human orthologs (a / b) | gar co-orthologs | medaka co-orthologs | medaka parallel dup |
|---|---|---|---|---|---|---|
| TGD_likely_parallel | Teleostei\|DANRE | 1:1 | TBX5(LDO) / TBX5(O) | 1 (same gar gene for both) | 2 | yes |

PANTHER puts the duplication on the zebrafish branch. Both copies share one spotted gar co-ortholog, and
medaka also has two copies. The project page reads this pattern as a TGD pair whose zebrafish and medaka
copies do not group as ((zfA, medA), (zfB, medB)).

**Literature (phylogeny and presence across teleosts).**

- Albalat et al. found the second copy in every teleost genome available and proposed a TGD origin:
  [PMID:19925885 "This duplicate gene is present in all teleost genomes whose sequence is available, suggesting it resulted from the teleost-specific genome duplication event that took place during fish evolution."]
- Parrie et al. placed the duplication with a phylogeny:
  [PMID:23441045 "Our phylogenetic analyses confirm tbx5b as a paralog that likely arose in the teleost-specific whole genome duplication ∼270 MYA."]

**Status.** A TGD origin is supported by PANTHER (one gar co-ortholog, duplicated in medaka) and by
published gene trees, and it is accepted in the literature. I found no published gar-anchored synteny
analysis for tbx5a/tbx5b of the kind available for pax6. Double-conserved synteny is therefore **not
established** here. Which medaka copy corresponds to which zebrafish copy is also not established.

## 2. Protein-level comparison

- **Identity.** 49.2% identity and 58.7% similarity over 504 alignment columns
  ([annotation-comparison.md](annotation-comparison.md)). This is far lower than for pax6a/pax6b (93%).
  tbx5b is 70 residues shorter. The divergence lies mostly outside the T-box:
  [PMID:30532148 "There are high levels of conservation at the amino acid level in the Tbox domain between the two paralogues but there are low levels of conservation throughout the rest of the protein [10]."]
  [PMID:39079985 "The T-box domain of Tbx5b shares only 83% sequence identity with its Tbx5a counterpart, which is significantly lower than the typical 95–99% sequence identity observed between paralogous T-box genes within the same subfamily."]
- **Domains.** Both keep a T-box DNA-binding domain (tbx5a residues 62-237; tbx5b 57-237 in UniProt).
  UniProt flags tbx5b as lacking some conserved residues used to propagate the PROSITE T-box feature. What
  those substitutions do has not been tested. The tbx5a C-terminal region matters for regulation: the Pdlim7
  interaction that holds Tbx5 on cytoplasmic actin needs it
  [PMID:19895804 "Of importance, our new data provide the first evidence in eukaryotic cells for the importance of the C-terminus of Tbx5 for proper protein function since the truncated hst mutant protein cannot bind to Pdlim7 nor localize outside the nucleus."]
  Whether Tbx5b, with its divergent and shorter C-terminal region, binds Pdlim7 or Kctd10 is unknown.
- **Biochemistry.** Tbx5 binds DNA in EMSA (PMID:18347092; the text does not say which species' construct).
  No DNA-binding or transactivation assay of Tbx5b has been published, and no side-by-side comparison
  exists.
- **Cross-rescue (the key protein-level test).**
  [PMID:23441045 "simultaneous depletion of both tbx5 paralogs did not lead to more severe phenotypes, and injection of wild-type mRNA from one tbx5 paralog was not sufficient to cross-rescue phenotypes of the paralogous gene."]
  Each mRNA does rescue its own knockdown:
  [PMID:24759614 "Similarly, a full-length tbx5b form was able to rescue the jogging phenotype of tbx5b morphants when co-injected with our tbx5b MO (figure 3b; n = 117)."]
  A 2024 review reads this as protein-level subfunctionalization:
  [PMID:39079985 "(2013), who demonstrated, despite co-expression in developing heart and limb, Tbx5a and Tbx5b display distinct amino acid sequences that confer unique functions."]

**Does each copy keep the ancestral molecular function?**

- Both are almost certainly functional T-box transcription factors. Each is required in vivo. tbx5b mRNA
  rescues its own morphant, and a tbx5b allele truncated before the T-box phenocopies the morphant (section
  4).
- That the two proteins are **not equivalent** is suggested by the failure of reciprocal mRNA cross-rescue.
  This test is weak, though. Injected mRNA is expressed everywhere, is diluted by 1-2 dpf, and is not dosed
  to match. Only the abstract of the cross-rescue paper is cached. The review's "confer unique functions" is
  therefore an interpretation. Protein-level divergence is **inferred, not established**.

## 3. Expression

- **Shared domains: heart and dorsal retina.**
  [PMID:24759614 "We identified a novel tbx5 gene in zebrafish--tbx5b--that is co-expressed with its paralogue, tbx5a, in the developing eye and heart"]
- **Pectoral fin: tbx5a strongly, tbx5b weakly or not at all.**
  [PMID:19925885 "We show that tbx5b has lost the characteristic forelimb/pectoral fin expression of Tbx5 genes but has retained the eye and heart expression, partially overlapping with that of its paralogue, now referred to as tbx5a."]
  Parrie et al. reported low fin-bud expression:
  [PMID:24759614 "Although we had not previously observed tbx5b expression in developing pectoral fins [16], others have recently described it in the pectoral fin bud mesenchyme of 36 hpf embryos [17]."]
  Parrie et al.'s own summary is that expression is similar:
  [PMID:23441045 "Collectively, these data indicate that, despite similar spatio-temporal expression patterns, tbx5a and tbx5b have independent functions in heart and fin development."]
- **Timing, level and chamber.** tbx5b starts later, is expressed at lower levels, and becomes restricted to
  the ventricle:
  [PMID:30532148 "While tbx5a is detectable through in situ hybridization as early as 14 hpf in the LPM, tbx5b is not detectable until 17 hpf [9]."]
  [PMID:30532148 "Expression in the heart is similar for both paralogues until 36 hpf, when tbx5b expression is restricted to the ventricle, whereas tbx5a expression remains in both chambers of the heart [9]."]
  [PMID:29382818 "tbx5a expression levels during heart development are higher than those of tbx5b"]
- **The pre-duplication state.** Single-copy Tbx5 in jawed vertebrates is expressed in dorsal eye, heart and
  the pectoral fin/forelimb field:
  [PMID:27503876 "In skate and zebrafish embryos, Tbx5 was expressed in the dorsal portion of the eye, heart, and LPM (lateral plate mesoderm) of the pectoral fin field"]
  The fin enhancer CNS12 works when taken from gar, so the fin domain is ancestral:
  [PMID:27503876 "Analysis of stable lines revealed that all three CNS12sh drove GFP expression in the pectoral fin bud (four lines with gar sequence, two lines with zebrafish sequence, and nine lines with mouse sequence)"]
  That paper studied the tbx5a locus only. Whether a CNS12 copy survives at the tbx5b locus was not
  reported. So the loss or weakening of tbx5b fin expression is consistent with loss of this element, but
  that has not been tested.

**Summary.** tbx5a keeps the full ancestral pattern: eye, heart (both chambers) and fin. tbx5b keeps a
subset (eye, heart becoming ventricle-restricted) that starts later and is weaker. There is no tbx5b-only
domain. This is an asymmetric expression split, not a reciprocal one: tbx5a has no domain it lost to tbx5b.

## 4. Experimental evidence of function

**tbx5a**

- *heartstrings* (hst). ENU nonsense allele: premature termination codon (PTC) after the T-box. No fin buds,
  no looping, lethal.
  [PMID:12223419 "The heartstrings mutation causes premature termination at amino acid 316."]
  [PMID:12223419 "Homozygous mutant embryos never develop pectoral fin buds and do not express several markers of early fin differentiation."]
  [PMID:12223419 "However, the heart fails to loop and then progressively deteriorates, a process affecting the ventricle as well as the atrium."]
  The transcript is lost after 32 hpf, as expected from nonsense-mediated decay:
  [PMID:27503876 "The hst mutation is a premature stop codon in tbx5a exon8, and tbx5a is weakly expressed in the LPM of hst embryos until 32 hpf, but undetectable thereafter"]
- *oug* (hu6499). Truncated inside the T-box. Looping fails, but jogging is normal:
  [PMID:34372968 "Indeed, in oug approximately 75% of the gene product is lost, including a large portion of the DNA-binding T-box domain."]
  [PMID:34372968 "In such a screen we identified the oudegracht (oug) mutant in which cardiac jogging was unaffected while cardiac looping was compromised."]
- Gene trap (tpl58). Truncates the protein after 50 aa. Needed for adult heart regeneration:
  [PMID:29933372 "while all tbx5atpl58R/tpl58R fish failed to regenerate their hearts (n = 8)"]
- CRISPR F0 knockouts: [PMID:33416493 "100% (43/43) of the tbx5a F0 larvae did not develop pectoral fins (Figure 4A)."]
- Fin-field migration: [PMID:34756968 "In both tbx5a −/− mutants and Tbx5a knock-down embryos, AP convergence of the fin field cells fails to occur; however these same precursors exhibit a robust ML movement that is similar in migration dynamics to that of wt embryos."]

**tbx5b**

- CRISPR allele. A 4-bp insertion in intron 1 causes a splicing defect, a frameshift and a PTC. It is
  probably subject to NMD, but this was not tested. It phenocopies the morphants:
  [PMID:30532148 "This mutation would result in a splicing error such that the first intron is not spliced from the protein, leading to a frameshift starting at amino acid 53 and a premature stop codon after 16 incorrect amino acids (Fig 1C)."]
  [PMID:30532148 "Tbx5b-/- mutants fully phenocopy the reported Tbx5b morphants[10,13]."]
  [PMID:30532148 "The heart fails to loop and a fluid filled edema forms surrounding the heart (Fig 1E and 1F)."]
  [PMID:30532148 "By 6 days, both mutants and morphant embryos die, possibly as a result of the severe heart defects."]
- Morphants (several morpholinos) show heart looping defects and small, delayed fins:
  [PMID:23441045 "Using morpholino depletion studies, we find that tbx5b is required in the heart for embryonic survival, and influences the timing and morphogenesis of pectoral fin development."]
  [PMID:24759614 "Taken together, we show that pectoral fin development has a different requirement for each of the tbx5 paralogues: tbx5a function is required for the earliest steps of initiation of fin outgrowth, whereas tbx5b functions later to ensure properly timed and sustained fin outgrowth."]
  [PMID:34756968 "We show here that loss of Tbx5b function affects initial ML directed movements so that fin field cells fail to migrate laterally but continue to converge along the AP axis."]

**Both copies**

- The heart does not tolerate loss of either copy:
  [PMID:23441045 "Because tbx5a hypomorphic mutations are embryonic lethal, tbx5a and tbx5b functions in the heart must not be completely redundant."]
- Double knockdown raises penetrance but not severity (morpholinos only):
  [PMID:24759614 "Although, in agreement with a previous report [17], the severity of the phenotype was not enhanced by double knock-down, downregulation of both genes increased the penetrance of the phenotype (figure 1i)."]
- Fin: in double knockdown the two migration vectors are both lost:
  [PMID:34756968 "Furthermore, fin field cells in the double Tbx5a/Tbx5b knock-down zebrafish do not engage in directed migrations along either the ML or AP axis."]
- Retina and optic nerve: an additive effect, seen only in double morphants:
  [PMID:24759614 "suggesting that tbx5 paralogues act redundantly in the dorsal retina to ensure efnb2a expression in this territory."]
  [PMID:24759614 "Moreover, and in agreement with both tbx5 genes acting redundantly to ensure proper optic nerve formation, double-morphant embryos showed a significantly thinner optic nerve (figure 4n)."]
- Swim bladder formation needs neither copy (hst plus morphants):
  [PMID:30352852 "However, we find that although Tbx5 is required for lung formation, tbx5a / b is not required for SB formation in the zebrafish."]

**Heart jogging: a morpholino-versus-mutant conflict.** Morphants of either copy jog abnormally:
[PMID:24759614 "The cardiac phenotypes caused by tbx5a and/or tbx5b knock-down (namely cardiac jogging and looping orientation defects) demonstrate that tbx5 genes are required to direct both asymmetric events the zebrafish heart undergoes"]
The tbx5a mutants do not:
[PMID:24759614 "We have ourselves analysed heart tube jogging in hst mutants (n = 38) and all of them displayed a normal left-jog as visualized by myl7 expression in 26 hpf embryos (figure 3c,d)."]
Pi-Roig et al. explained this by calling hst hypomorphic. But the T-box-truncating oug allele also jogs
normally (quoted above). Three explanations remain open:

1. A morpholino artefact.
2. Transcriptional adaptation (genetic compensation) triggered by these PTC alleles.
3. A requirement specific to maternal or early transcripts.

Both mutant alleles and the tbx5b allele are PTC-type. No RNA-less allele exists for either copy. The
gene-trap paper raises allele-dependent compensation directly:
[PMID:29933372 "A particularly intriguing possibility would be that point mutant tbx5ahst but not gene trap mutant tbx5atpl58 may induce genetic compensation [40,41]."]
The transcriptomics study chose morpholinos over mutants partly to avoid paralog compensation:
[PMID:30532148 "The use of morpholinos also allows for the assaying of single gene effects without paralogous gene compensation[26]."]

**Compensation.** No study has measured tbx5b levels in tbx5a mutants, or the reverse. An early paper
proposed that tbx5b buffers tbx5a loss:
[PMID:20413782 "These milder cardiac phenotypes observed in zebrafish tbx5a mutants are likely due to functional redundancy between tbx5a and its newly identified paralogue tbx5b"]
The later loss-of-function data (each copy essential; no rescue in either direction) argue against simple
redundancy.

## 5. Fate classification

**MIXED: two essential, non-redundant copies. Expression split in the fin (asymmetric), with inferred
protein-level divergence. Confidence: moderate.**

**Established**

- Each copy is required, and neither compensates for loss of the other, in the heart (looping, survival) and
  the pectoral fin. Both single mutants are lethal with heart defects (hst, oug; tbx5b frameshift). This rules
  out BACKUP as the main fate.
- The fin role is divided. tbx5a is needed for bud initiation, fgf24 and antero-posterior convergence;
  tbx5b is needed for timed outgrowth and medio-lateral migration. This is shown with morphants and mutants
  of both copies (PMID:24759614, PMID:34756968, PMID:30532148).
- Expression is split asymmetrically. tbx5a keeps the full ancestral domain (fin, both heart chambers, dorsal
  retina). tbx5b keeps a later, weaker subset (heart becoming ventricle-restricted, retina) with weak or no
  fin expression.
- The proteins are much more diverged than most TGD transcription-factor pairs (49% overall, 83% T-box).

**Inferred (not established)**

- **Protein-level divergence.** This rests on the failure of reciprocal mRNA cross-rescue (abstract only;
  injected mRNA is a weak test) and on sequence divergence. Tbx5b biochemistry has not been measured.
- **Why tbx5b is needed in the fin despite little or no fin expression.** Possible reasons: low-level
  expression, a non-cell-autonomous effect from neighbouring tissue, or an early requirement in the LPM
  before the fin field forms. Unresolved.
- **The retinal role is additive (DOSAGE-like).** Morpholino-only.

**Not supported**

- *Pure backup/redundancy.* Contradicted by the lethal single-copy phenotypes and by the failure of
  cross-rescue.
- *Innovation (neofunctionalization).* Every tbx5b domain and role (heart, retina, fin outgrowth) is an
  ancestral Tbx5 territory. The divergent protein may have gained or lost interactions, but no new function
  has been shown.
- *Clean DDC subfunctionalization.* tbx5a has lost no domain to tbx5b. The expression split is one-sided, so
  on expression alone this looks like tbx5b degeneration. That tbx5b is still essential points to
  partitioning at another level (protein, dose or timing), not to reciprocal loss of cis elements.

**What would change the call**

- A coding-sequence swap at the endogenous loci. If tbx5b coding sequence at the tbx5a locus rescues fin
  initiation and looping, the divergence is regulatory: this becomes PARTITION (expression) plus DOSAGE. If it
  fails, protein-level partition or divergence is established.
- A gar tbx5 expression atlas (heart chamber restriction, fin timing), and a synteny/CNE analysis of the
  tbx5b locus (is CNS12 present?).
- RNA-less alleles for both copies, to settle the jogging question and test for transcriptional adaptation.

## 6. GO annotation consistency across the pair

Source: [annotation-comparison.md](annotation-comparison.md), after both reviews.

**Shared, and correctly so.**

- Molecular function (GO:0000981, GO:0000978, GO:0003700), nucleus, chromatin and regulation of transcription
  are accepted for both copies. The tbx5b MF rows rest on IBA and IEA only (no Tbx5b assay). I kept them,
  because each copy's mRNA rescues its own morphant, the T-box is conserved, and a truncating tbx5b allele
  phenocopies. Protein divergence argues for different targets or partners, not for loss of DNA-binding TF
  activity.
- Heart looping (GO:0001947), heart morphogenesis and heart development are accepted for both. Both copies are
  genetically required.
- Pectoral fin development (GO:0033339) is accepted for both.
- The IBA rows are handled the same way for both copies. "Cardiac left ventricle formation" (GO:0003218) is
  marked as over-annotated for **both**, with a propagation_review: the PAINT node is sound for amniotes, but
  teleosts have a single ventricle. This is a taxon issue, not a paralog issue.
- Epithelium development (ARBA) is over-annotated on both.
- The double-morphant retina and optic nerve rows (GO:0060042, GO:0021554) are non-core on both, as a shared,
  morpholino-only role.
- NOT swim bladder development is accepted on both.

**Asymmetric, and correctly so.**

- **Fin initiation terms are tbx5a-only.** Limb bud formation (GO:0060174), embryonic pectoral fin
  morphogenesis (GO:0035118) and pectoral fin morphogenesis are on tbx5a only. tbx5b is not needed to initiate
  the fin, so these should **not** be added to tbx5b. tbx5b keeps the general pectoral fin development term,
  which fits its later outgrowth role.
- **Heart jogging (GO:0003146).** UNDECIDED on tbx5a, because two tbx5a mutant alleles contradict the
  morphant data. Kept as non-core on tbx5b, where no mutant has been scored. This difference reflects the
  evidence available for each copy, not biology known to differ.

**Asymmetries caused by which copy was studied (not biology).**

- Most of the extra tbx5a rows come from 25 years of heartstrings and morphant studies:
  - AV canal and valve (GO:0036302, GO:0003190, GO:0003294);
  - proepicardium (GO:0003342);
  - chamber morphogenesis (GO:0003206);
  - regeneration (GO:0061026);
  - cBAF differentiation (GO:0055007);
  - heart tube morphogenesis;
  - the IDA/IPI rows with Pdlim7 and Kctd10.

  tbx5b has never been tested for these roles. Their absence from tbx5b is **absence of evidence**. Because
  the proteins have diverged and tbx5b is ventricle-restricted, they should not be propagated to tbx5b
  without data. I added no NEW terms to either copy.
- Localization. Cytoplasm and actin cytoskeleton (Pdlim7 sequestration) are shown only for Tbx5(a), and the
  C-terminal region that mediates this differs in Tbx5b. Cytoplasm is non-core on both (IEA on tbx5b). The
  actin row stays tbx5a-only.

**Other decisions of note (tbx5a).**

- Protein binding (IPI, Kctd10): REMOVE, as uninformative.
- GO:0061629 TF binding (IPI, Kctd10): UNDECIDED. The partner is not a DNA-binding TF, so the term probably
  belongs on kctd10.
- GO:0006351 DNA-templated transcription: MODIFY to GO:0006357.

**Should be copy-specific:** fin bud initiation and early fin morphogenesis (tbx5a).

**Should be shared:** T-box transcription factor activity; heart looping and heart development; pectoral fin
development (at the general level); dorsal retina patterning.

**Open (depends on untested tbx5b biology):** AV canal, proepicardium, regeneration and the regulatory
interactions (Pdlim7, Kctd10).

## 7. Open questions

- Would tbx5b coding sequence knocked into the tbx5a locus rescue fin initiation and looping, and the
  reverse? This is the decisive test between protein-level and regulatory partition.
- Do Tbx5a and Tbx5b bind the same sites (CUT&RUN or SELEX)? Does Tbx5b bind Pdlim7 and Kctd10?
- Is heart jogging tbx5-dependent? The morphant data conflict with the hst and oug mutants. RNA-less alleles
  are needed. Is tbx5b upregulated in hst or oug?
- Is tbx5b expressed in fin-field cells at all, and if not, how does it control their medio-lateral
  migration?
- Does the tbx5b locus keep the CNS12 fin enhancer? What does single-copy gar tbx5 look like in the heart
  (chamber restriction) and the fin?

## References

PMID:12066188, PMID:12223419, PMID:18347092, PMID:19895804, PMID:19925885, PMID:20413782, PMID:23441045,
PMID:24759614, PMID:27503876, PMID:29382818, PMID:29933372, PMID:30352852, PMID:30532148, PMID:33416493,
PMID:34372968, PMID:34756968, PMID:39079985. Also the files `panther_tgd_pairs.tsv` and
[annotation-comparison.md](annotation-comparison.md).
