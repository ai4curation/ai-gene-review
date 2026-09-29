---
title: "Contested Function Project"
maturity: IN_PROGRESS
tags: [PIPELINE, FLAGSHIP]
species: [SCHPO, SACEN, PSEAE, STRCO]
genes: [Epe1, eryCII, pqsB, actI-ORF2]
manifest:
  slides:
    - href: CONTESTED_FUNCTION/slides/CONTESTED_FUNCTION-slides.html
  artifacts:
    - href: https://claude.ai/artifact/GW82WzsUznCSPvHxx9WdXV
      title: Project brief
---

# Contested Function Project

**Bottom line:** some proteins keep an enzyme family's domain but have lost the
activity, so homology-based IBA and IEA annotations, and occasionally an experimental
one, assign them a catalytic function that biochemistry contradicts. This project
collects such pseudo-enzyme cases and reviews them in depth, weighing domain homology
against assays, catalytic-site mutants and the protein's actual mechanism. We did this
because these cases need several evidence types synthesised at once, which makes them a
demanding test for AI-assisted curation, and because a wrong catalytic term on a
pseudo-enzyme keeps being re-propagated. Four reviews are complete: fission yeast Epe1,
whose four electronic (IBA/IEA) demethylase, oxidoreductase and dioxygenase rows are
REMOVE (none of the four has a replacement term; Epe1's binding functions are
captured by separate NEW rows, such as GO:0070087 chromo shadow domain binding),
and three
biosynthetic-cluster proteins without active sites (eryCII, pqsB, actI-ORF2). Epe1's
two PomBase experimental (IDA/EXP) H3K9 demethylase rows and its electronic metal ion
binding row are UNDECIDED: catalysis and metal binding are unmeasured or disputed, not
refuted. Finding
further candidates has not started; the [Top-Nots](TOP_NOTS.md) candidate list is the
natural source.

## Overview

This project tracks genes where GO annotations incorrectly describe the molecular function based on sequence homology or domain presence, but biochemical evidence demonstrates the protein has evolved away from that function. These are compelling cases for AI-assisted curation because they require synthesizing multiple evidence types:

1. **Sequence/domain homology** - suggests one function
2. **Biochemical assays** - demonstrate lack of activity
3. **Mutational analysis** - shows function retained without catalytic activity
4. **Alternative mechanisms** - protein functions through non-enzymatic means

Such genes are often annotated based on IBA (phylogenetic inference) or IEA (electronic annotation) from domains, but these annotations can be misleading when the protein is a **pseudo-enzyme** or has evolved a divergent function.

## Categories of Contested Functions

### 1. Pseudo-enzymes
Proteins with enzyme-like domains that lack catalytic activity due to:
- Degenerate active site residues
- Loss of cofactor binding
- Structural changes incompatible with catalysis

### 2. Moonlighting Functions
Proteins where the primary function differs from the one suggested by domain architecture.

### 3. Over-annotated Binding
Generic "protein binding" or "metal binding" annotations based on domains that don't reflect actual binding specificity or lack of binding.

## Featured Examples

### Epe1 (S. pombe) - Pseudo-demethylase

**The Problem**: Epe1 contains a JmjC domain typically associated with histone demethylase activity. Multiple annotations exist for:
- `GO:0032452` histone demethylase activity (IBA)
- `GO:0032454` histone H3K9 demethylase activity (IDA, EXP)
- `GO:0140680` histone H3K36me/H3K36me2 demethylase activity (IEA)
- `GO:0051213` dioxygenase activity (IEA)
- `GO:0016491` oxidoreductase activity (IEA)
- `GO:0046872` metal ion binding (IEA)

**The Evidence Against**:
1. The Epe1 JmjC Fe(II)-binding triad is H297-E299-Y370: the distal iron-ligating His is replaced by Tyr (UniProt caution). The Tyr is nonetheless required, a result independent of Ayoub: Raiymbek 2020 (PMID:32195666) report "Replacing the non-conserved tyrosine residue in Epe1 with alanine (epe1 Y370A) leads to a similar loss of function phenotype. Hence, despite the lack of conservation, a natural tyrosine substitution within the JmjC domain of Epe1 is essential for its anti-silencing function in cells." Required is not catalytic (all three cofactor-site mutants weaken the Swi6 interaction), but Tyr370 is not a dispensable, decayed position
2. Mass spectrometry assays show NO demethylation of H3K9me2/me3 peptides
3. The H297A Fe(II)-site mutant does not settle it: at endogenous levels it behaves like epe1Δ in erasing ectopic H3K9me (Audergon 2015), while overexpressed H297A still disrupts silencing, SAGA-dependently (Bao 2019). Sorida 2019 shows the split within one experiment: under H297A, prevention of de novo H3K9me is retained (part of the anti-silencing activity does not need H297; a few pink colonies mean it is nearly but not fully retained, and the authors state that prevention acts "independently of both its JmjC-mediated demethylation and heterochromatin association ability"), but removal of established ectopic heterochromatin is lost (the other arm of the same experiment; see item 4 below)
4. C-terminus alone (without JmjC) disrupts heterochromatin, though only partly: Raiymbek call it "a hypomorphic allele that partially retains wild-type levels of Epe1 anti-silencing activity", expressed 4-5 fold below full-length Epe1

**Evidence for a catalytic contribution (not excluded)**:
1. The JmjC domain is required for Epe1 function: "the jmjC domain is essential for Epe1 activity" in complementation experiments (Ayoub et al. 2003, PMID:12773576), and Epe1's effect on Pol II accessibility "requires Epe1's JmjC domain" (Zofall and Grewal 2006, PMID:16762840)
2. A required domain is not required catalysis: Zofall and Grewal note the mechanism "might be distinct from other JmjC proteins that possess known demethylase activities", and Raiymbek et al. (PMID:32195666) show that the JmjC-containing half binds H3K9 methylation directly: "Next, we expressed and purified a C-terminal truncation mutant of Epe1, MBP-Epe1-ΔC from Sf9 insect cells, which includes amino acids 1–600 and includes the putative catalytic JmjC domain. We found that Epe1-ΔC can also directly bind to an H3K9me3 peptide and specifically interacts with H3K9 methylated histones (Figure 5—figure supplement 1A,B)." The fragment lacks residues 601-948 but keeps the minimal Swi6-binding site (434–600), and the assays contain no Swi6, so this is Swi6-independent H3K9me recognition by the JmjC-containing half, shown by data. The authors interpret it as the JmjC domain being "primarily responsible for H3K9 methylation recognition and binding"; the fragment extends beyond the JmjC domain (233–434), so that assignment is their inference
3. A single-residue mutant is recorded as loss of function, but it is not independent of item 1: UniProt records Y307A as loss of function (FT MUTAGEN 307, experimental evidence from PMID:12773576, its only mutagenesis record). UniProt has no BINDING feature at 307. Raiymbek et al. assign Y307 to the alpha-ketoglutarate site ("residues involved in Fe (II) or α-ketoglutarate binding (epe1 H297A and epe1 Y307A, respectively)"), and Sorida et al. describe Epe1Y307A as a JmjC mutant "which retains the metal-binding residues" (a background citation, [12], not resolvable from the cache). These agree: Y307 is a 2-oxoglutarate-site residue, not an Fe(II) ligand, so the Y307A record implicates the 2-oxoglutarate part of the cofactor pocket rather than just the fold. It still does not isolate catalysis: Raiymbek assert that the substitutions "disrupt co-factor binding" from the residues' assigned active-site roles, but the data shown are reporter phenotypes, Swi6 co-IP and localization, with no cofactor-binding or activity measurement on Y307A, and Y307A "fails to co-localize with mCherry-Swi6HP1" in vivo (Raiymbek), which conflicts with the reference Sorida cite for Swi6 interacting with Epe1Y307A, and not only in degree, since Raiymbek's co-IP legend states "The interaction between the two proteins is preserved in wild-type cells and is completely eliminated in all Epe1 JmjC mutants". The Y370A loss of function is the same colony readout, and the direct in vivo readout for all three residues is H3K9me: "In contrast, Epe1 mutants that exhibit a red or sectored phenotype upon +tetracycline addition retain high levels of H3K9 methylation at the ectopic site (Figure 1D)." Expression and stability are excluded for all three mutants ("We verified that the expression level of all Epe1 mutant proteins is equal relative to an actin loading control. Hence, neither overexpression artifacts nor changes in protein stability contribute to the maintenance-specific phenotype we observed in our genetic assays"); a local conformational change is not. This and the domain-essential statement in item 1 both come from Ayoub 2003 and may reflect the same experiment, so it is not an independent line of evidence; the same mutations also weaken Swi6 binding
4. An independent separation of function: Sorida et al. 2019 (PMID:31206516) found that H297A, a UniProt Fe ligand (rule-predicted, PRU00538), still suppressed red-white variegation (the de novo, N-terminal-dependent arm) but "entirely failed to remove already-established ectopic heterochromatin", which they attribute to the JmjC domain. This is the other arm of the experiment in item 3 of the evidence against. The removal arm has a dosage condition: it is read at single-copy expression, where Sorida et al. report that "re-introduction of single copy Epe1 did not erase ectopic heterochromatin when an H3K9me source existed nearby, while Epe1 overexpression completely erased it", and whether overexpressed H297A would remove established ectopic heterochromatin is not reported. It is a different paper, residue and assay, a folding defect would not predict the pattern (recombinant H297A also has the same denaturation temperature as wild type, Raiymbek 2020), and it reads out H3K9me (as Raiymbek's H297A/Y307A/Y370A data do, item 3, so Sorida's distinct contribution is the separation of function); it does not measure demethylation, and H297A also reduces Epe1's heterochromatin localization. Sorida et al. propose that mechanism themselves: "conformational changes in the JmjC domain induced by perturbations in Fe2+ binding result in a slight alteration of the interaction surface for Swi6 binding, while severely disrupting the structure of a region essential for heterochromatin association"
5. Wang et al. 2015 (PMID:25774602) interpret the sickness of epe1-H374A and epe1-Y307A mutants combined with mst2 loss as redundancy between the enzymatic activities of Mst2 and Epe1 (residue 374 of UniProt O94603 is Thr, so the mutated histidine cannot be identified from the cached text); for Y307A, reading it as enzymatically dead is consistent with a 2-oxoglutarate-site mutation but is an inference, not a measurement

**Characterized mechanisms** (binding and recruitment; a catalytic contribution is not excluded, see above):
- Binds HP1/Swi6 (chromoshadow domain) at H3K9-methylated heterochromatin
- Associates with the SAGA histone acetyltransferase complex
- Recruits Bdf2 bromodomain protein to the heterochromatin boundaries flanking centromeres
- Required for normal heterochromatic nucleosome turnover (mechanism unresolved; the turnover itself is carried out by chaperones such as FACT)
- Binds H3K9-methylated histones in vitro (Raiymbek 2020); no eraser (demethylase) activity has been detected

**AI Review Action**: REMOVE the four IBA/IEA enzymatic activity annotations, none with a replacement term, and capture Epe1's binding functions as separate NEW rows (Swi6, SAGA, Bdf2, histones); the two PomBase experimental GO:0032454 rows (IDA/EXP, Audergon 2015) are UNDECIDED, since they rest on in vivo genetic evidence.

**Source**: Presented at Gene Ontology Consortium Meeting, October 2025, Cambridge UK. See [ai4curation/ai-gene-review](https://github.com/ai4curation/ai-gene-review).

## Genes for Review

### Priority 1: Documented Pseudo-enzymes
| Species | Gene | Domain | Contested Function | Status |
|---------|------|--------|-------------------|--------|
| pombe | Epe1 | JmjC | histone demethylase activity | COMPLETE |
| SACEN | eryCII | cytochrome P450 | monooxygenase activity (heme-less; GT activator) | COMPLETE |
| PSEAE | pqsB | FabH/KAS-III | acyltransferase activity (no active site; PqsBC partner) | COMPLETE |
| STRCO | actI-ORF2 | β-ketoacyl synthase | acyltransferase activity (chain-length factor, no active site) | COMPLETE |

> **Finding-level disputes.** Contested *claims within an otherwise sound paper* can now be
> recorded with the schema's `finding_review` (`finding_status: DISPUTED`/`OVERTURNED` +
> `superseded_by`), rather than condemning the whole reference. Example: in `genes/SACEN/eryCIII/`
> the 2004 claim that EryCIII is highly active on its own (PMID:15303858) is marked DISPUTED,
> superseded_by the 2012 structure study (PMID:22056329) showing EryCIII is inactive without EryCII.

### Priority 2: Suspected Pseudo-enzymes
(To be identified through literature and bioinformatics)

### Priority 3: Over-annotated Domains
(Genes with generic domain-based annotations that require refinement)

## Criteria for Inclusion

A gene belongs in this project if:

1. Has annotations for enzymatic activity based on domain homology
2. Biochemical evidence demonstrates lack of that specific activity
3. The protein has an alternative, non-catalytic function
4. The case illustrates broader curation principles

## Key References

- Raiymbek et al. (2020) - Epe1 biochemical characterization
- Bao et al. (2019) - Epe1 SAGA recruitment mechanism; overexpressed H297A (PMID:30573453)
- Audergon et al. (2015) - H297A/K314A phenocopy epe1Δ in ectopic H3K9me inheritance (PMID:25838386)
- Trewick et al. (2007) - Original observation of degenerate JmjC
- Wang et al. (2013) - Epe1/Bdf2 boundary formation

## Related Projects

- YEAST_EPIGENETICS_HISTONE_INHERITANCE.md - S. pombe heterochromatin genes

---

# STATUS

## Completed Reviews
- [x] pombe/Epe1 - Pseudo-demethylase, chromatin boundary factor

## Pending
- [ ] Identify additional pseudo-enzyme candidates
- [ ] Screen for over-annotated IBA/IEA annotations in reviewed genes

Last updated: 2026-01-22

# NOTES

## 2026-01-22

**Project Creation**

Created project to document genes with contested molecular functions, starting with Epe1 from the GO Consortium 2025 presentation slides.

**Epe1 Summary**:
- Full review in `genes/SCHPO/Epe1/Epe1-ai-review.yaml`
- 7 catalytic and metal annotations reviewed: 4 electronic rows REMOVE, 3 UNDECIDED:
  - `GO:0032452` histone demethylase activity (IBA)
  - `GO:0032454` histone H3K9 demethylase activity (IDA, EXP) - UNDECIDED (in vivo genetic evidence; catalysis disputed)
  - `GO:0140680` histone H3K36me/H3K36me2 demethylase activity (IEA)
  - `GO:0051213` dioxygenase activity (IEA)
  - `GO:0016491` oxidoreductase activity (IEA)
  - `GO:0046872` metal ion binding (IEA) - UNDECIDED (rule-predicted Fe ligands H297/E299 retained, binding unmeasured)
- Key evidence: Mass spectrometry assays, non-canonical Fe(II) triad, assay-dependent H297A phenotype
- Proposed replacements: `GO:0031625` ubiquitin protein ligase binding (for the Cdt2 protein-binding IPI MODIFY); none of the four REMOVE rows has a replacement, and the binding functions are separate NEW rows (`GO:0070087`, `GO:0062070`, `GO:0030674`, `GO:0042393`)
- 5 core functions documented with supporting evidence

This case demonstrates how AI review can integrate:
1. Domain-based predictions (suggests demethylase)
2. Phylogenetic inference (IBA from related proteins)
3. Direct biochemical evidence (no activity)
4. Genetic evidence (mutant analysis)
5. Literature synthesis (alternative mechanism)

The Epe1 review serves as a template for identifying and documenting other pseudo-enzymes.
