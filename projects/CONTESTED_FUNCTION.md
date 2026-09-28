---
title: "Contested Function Project"
maturity: IN_PROGRESS
tags: [PIPELINE, FLAGSHIP]
species: [SCHPO, SACEN, PSEAE, STRCO]
genes: [Epe1, eryCII, pqsB, actI-ORF2]
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
whose five electronic (IBA/IEA) demethylase, oxidoreductase, dioxygenase and metal-binding
rows are REMOVE in favour of histone-binding terms, and three
biosynthetic-cluster proteins without active sites (eryCII, pqsB, actI-ORF2). The two
PomBase experimental (IDA/EXP) H3K9 demethylase rows on Epe1 are also REMOVE in the
current review; PR #3229, not yet merged, proposes moving them, and the electronic
metal ion binding row, to UNDECIDED. Finding
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
1. The Epe1 JmjC Fe(II)-binding triad is H297-E299-Y370: the distal iron-ligating His is replaced by Tyr
2. The distal iron-ligating histidine is lost (His370 replaced by Tyr; UniProt caution)
3. Mass spectrometry assays show NO demethylation of H3K9me2/me3 peptides
4. The H297A Fe(II)-site mutant does not settle it: at endogenous levels it behaves like epe1Δ in erasing ectopic H3K9me (Audergon 2015), while overexpressed H297A still disrupts silencing, SAGA-dependently (Bao 2019)
5. C-terminus alone (without JmjC) disrupts heterochromatin

**Actual Function**: Non-enzymatic anti-silencing factor that:
- Binds HP1/Swi6 to recruit SAGA histone acetyltransferase complex
- Recruits Bdf2 bromodomain protein to heterochromatin boundaries
- Promotes nucleosome turnover
- Functions as chromatin reader, not eraser

**AI Review Action**: REMOVE the IBA/IEA enzymatic activity annotations and propose binding terms; the two PomBase experimental GO:0032454 rows (IDA/EXP, Audergon 2015) are REMOVE in the current review, and PR #3229 (not yet merged) proposes UNDECIDED for them, since they rest on in vivo genetic evidence.

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

## Slides

- [Slides](CONTESTED_FUNCTION/slides/CONTESTED_FUNCTION-slides.html) (Marp source: [CONTESTED_FUNCTION-slides.md](CONTESTED_FUNCTION/slides/CONTESTED_FUNCTION-slides.md)) — AI generated

Last updated: 2026-01-22

# NOTES

## 2026-01-22

**Project Creation**

Created project to document genes with contested molecular functions, starting with Epe1 from the GO Consortium 2025 presentation slides.

**Epe1 Summary**:
- Full review in `genes/SCHPO/Epe1/Epe1-ai-review.yaml`
- 7 enzymatic annotations marked REMOVE in the current review (5 electronic, 2 experimental):
  - `GO:0032452` histone demethylase activity (IBA)
  - `GO:0032454` histone H3K9 demethylase activity (IDA, EXP) - PR #3229 proposes UNDECIDED for these two
  - `GO:0140680` histone H3K36me/H3K36me2 demethylase activity (IEA)
  - `GO:0051213` dioxygenase activity (IEA)
  - `GO:0016491` oxidoreductase activity (IEA)
  - `GO:0046872` metal ion binding (IEA) - PR #3229 proposes UNDECIDED (H297/E299 retained, binding unmeasured)
- Key evidence: Mass spectrometry assays, degenerate active site residues, catalytic mutant retains function
- Proposed replacements: `GO:0042393` histone binding, `GO:0140030` modification-dependent protein binding
- 6 core functions documented with supporting evidence

This case demonstrates how AI review can integrate:
1. Domain-based predictions (suggests demethylase)
2. Phylogenetic inference (IBA from related proteins)
3. Direct biochemical evidence (no activity)
4. Genetic evidence (mutant analysis)
5. Literature synthesis (alternative mechanism)

The Epe1 review serves as a template for identifying and documenting other pseudo-enzymes.
