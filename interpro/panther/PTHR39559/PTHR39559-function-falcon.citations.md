# Citations for Research Query

**Query:** # PANTHER Family Function Characterization (TreeGrafter granularity audit)

You are characterizing the function of a **protein family** for AI Gene Review.
This is the companion to a set of blinded gene-level function checks: the point
here is to establish, from primary literature and sequence/structure evidence,
**what function is actually conserved across the family** and **where function
diverges between subfamilies** — because automated phylogenetic annotation
(TreeGrafter/PANTHER) propagates a GO term from an ancestral node to every
descendant, and that is only safe when the family is functionally homogeneous.

## Family Under Review

- **PANTHER family:** PTHR39559 — ISOCITRATE DEHYDROGENASE KINASE/PHOSPHATASE (family)
- **Subfamily of interest:** PTHR39559:SF1 ISOCITRATE DEHYDROGENASE KINASE/PHOSPHATASE
- **Representative member:** aceK (Q88EA1), PSEPK / PSEPK
- **GO term currently propagated at/near this node:** phosphoprotein phosphatase activity (GO:0004721)

Note: do **not** assume the propagated term is the family's true conserved
function — that is exactly what you are testing.

## Research Objective

1. **Conserved core function.** What molecular function (and reaction/EC where
   relevant) is shared by *characterized* members across the whole family? Anchor
   this to the diagnostic fold, catalytic/binding residues, and obligate
   cofactors/partners — not to the family name.
2. **Functional divergence across subfamilies.** Enumerate the major
   functional subgroups within the family and how they differ (substrate
   specificity, lost catalysis / pseudo-enzymes, neofunctionalization, structural
   co-option). Is the family **homogeneous** (one MF safe to propagate) or
   **heterogeneous** (propagation will mis-annotate some branches)?
3. **Subfamily of interest.** Where does PTHR39559:SF1 ISOCITRATE DEHYDROGENASE KINASE/PHOSPHATASE sit — does it carry the
   conserved family function, a more specific specialized activity, or a diverged
   / non-enzymatic role? Name characterized exemplars of that subfamily.
4. **GO granularity verdict.** State the GO MF term appropriate at the **family**
   level versus at the **subfamily** level, and identify any subfamilies for
   which a family-level term would be an over-annotation. This is a lead for
   curators, not a final call.

Where decidable by computation, actually run it (domain/Pfam/InterPro
architecture, catalytic-residue conservation, orthology/paralogy splits) and keep
the result as provenance. Use resources you can access programmatically
(UniProt, InterPro, AlphaFold, sequence computation, public APIs). Prefer PMID
citations to primary literature; treat reviews/databases as orientation. If a
check is web-only or cannot be run, say so — an inconclusive result is acceptable;
never fabricate one.

## Required Output

### Family Function Summary

One paragraph: the conserved core molecular function and the fold/residues that
define it.

### Subfamily Divergence Table

One row per major functional subgroup: subgroup / representative member(s) (PMID)
· molecular function · substrate or specialization · catalytic residues intact?
· GO MF term that fits · notes (pseudo-enzyme, neofunctionalization, etc.).

### Homogeneous vs Heterogeneous Verdict

State plainly whether a single family-level GO MF term is safe to propagate
across this family, and if not, which branches it would mis-annotate.

### Granularity Leads for Curation

Family-level vs subfamily-level GO MF term recommendation, and the subfamilies
(if any) where the currently-propagated term is an over-annotation. Avoid
"protein binding" as a final recommendation.

### Evidence and Gaps

Key citations (PMID preferred), and explicit uncertainties that matter for
deciding the family-vs-subfamily granularity.

**Provider:** falcon
**Generated:** 2026-06-24T05:14:25.308972

1. zheng2012structuralandmechanistic pages 1-3
2. zheng2012structuralandmechanistic pages 3-4
3. crousilles2018threeenzymesand pages 1-3
4. zheng2012structuralandmechanistic pages 6-7
5. dolan2018theglyoxylateshunt pages 4-6
6. crousilles2018threeenzymesand pages 3-5
7. rangwala2022kinasesondouble pages 14-15
8. miller2000locationsofthe pages 1-2
9. zheng2012structuralandmechanistic pages 4-6
10. zheng2012structuralandmechanistic pages 7-9
11. zheng2012structuralandmechanistic pages 10-11
12. zheng2012structuralandmechanistic pages 11-13
13. chen2023twodifferentisocitrate pages 1-2
14. chen2023twodifferentisocitrate pages 9-10
15. crousilles2018threeenzymesand pages 5-7
16. dolan2018theglyoxylateshunt pages 11-12
17. dolan2018theglyoxylateshunt pages 10-11
18. Isocitrate dehydrogenase (NADP+)
19. https://doi.org/10.1098/rstb.2011.0426,
20. https://doi.org/10.3390/biom12050685,
21. https://doi.org/10.1101/318345,
22. https://doi.org/10.1074/jbc.275.2.833,
23. https://doi.org/10.1146/annurev-micro-090817-062257,
24. https://doi.org/10.3390/ijms241914985,