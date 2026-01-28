# Contested Function Project

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
1. Epe1 JmjC domain has HVD instead of canonical HXD motif
2. Lacks conserved Fe(II)-binding histidine residues
3. Mass spectrometry assays show NO demethylation of H3K9me2/me3 peptides
4. H297A catalytic mutant retains full anti-silencing function
5. C-terminus alone (without JmjC) disrupts heterochromatin

**Actual Function**: Non-enzymatic anti-silencing factor that:
- Binds HP1/Swi6 to recruit SAGA histone acetyltransferase complex
- Recruits Bdf2 bromodomain protein to heterochromatin boundaries
- Promotes nucleosome turnover
- Functions as chromatin reader, not eraser

**AI Review Action**: REMOVE all enzymatic activity annotations; propose replacement with binding terms.

**Source**: Presented at Gene Ontology Consortium Meeting, October 2025, Cambridge UK. See [ai4curation/ai-gene-review](https://github.com/ai4curation/ai-gene-review).

## Genes for Review

### Priority 1: Documented Pseudo-enzymes
| Species | Gene | Domain | Contested Function | Status |
|---------|------|--------|-------------------|--------|
| pombe | Epe1 | JmjC | histone demethylase activity | COMPLETE |

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
- Bao et al. (2019) - Epe1 SAGA recruitment mechanism
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
- Full review in `genes/pombe/Epe1/Epe1-ai-review.yaml`
- 5 enzymatic annotations marked REMOVE:
  - `GO:0032452` histone demethylase activity (IBA)
  - `GO:0032454` histone H3K9 demethylase activity (IDA x2)
  - `GO:0140680` histone H3K36me/H3K36me2 demethylase activity (IEA)
  - `GO:0051213` dioxygenase activity (IEA)
  - `GO:0016491` oxidoreductase activity (IEA)
  - `GO:0046872` metal ion binding (IEA)
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
