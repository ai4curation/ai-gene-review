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

- **PANTHER family:** PTHR43775 — FATTY ACID SYNTHASE
- **Subfamily of interest:** PTHR43775:SF51 INACTIVE PHENOLPHTHIOCEROL SYNTHESIS POLYKETIDE SYNTHASE TYPE I PKS1-RELATED
- **Representative member:** eryAIII (A4F7P1), SACEN / SACEN
- **GO term currently propagated at/near this node:** fatty acid synthase activity (GO:0004312)

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
3. **Subfamily of interest.** Where does PTHR43775:SF51 INACTIVE PHENOLPHTHIOCEROL SYNTHESIS POLYKETIDE SYNTHASE TYPE I PKS1-RELATED sit — does it carry the
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
**Generated:** 2026-06-24T04:33:54.235685

1. cane2010programmingoferythromycin pages 1-3
2. kruh2008anovelinteraction pages 6-6
3. he2009cooperationbetweena pages 1-2
4. torres2020animalbiosynthesisof pages 1-3
5. bon2022solutionstructureof pages 1-2
6. piech2020computationalandin pages 23-28
7. tang2000formationoffunctional pages 1-3
8. lin2024thepolyketideto pages 1-2
9. katja2015unusualhalogenationand pages 13-16
10. piech2020computationalandin pages 18-23
11. jenkekodama2005evolutionaryimplicationsof pages 5-6
12. kruh2008anovelinteraction pages 5-6
13. ramos2020revisitingtheexpression pages 1-2
14. he2009cooperationbetweena pages 2-2
15. herbst2016mycocerosicacidsynthase pages 1-5
16. herbst2016mycocerosicacidsynthase pages 5-9
17. cane2010programmingoferythromycin pages 1-1
18. ramos2020revisitingtheexpression pages 2-3
19. herbst2016mycocerosicacidsynthase pages 9-12
20. jenkekodama2005evolutionaryimplicationsof pages 1-1
21. jenkekodama2005evolutionaryimplicationsof pages 4-5
22. KS5–AT5–KR5–ACP5
23. KS6–AT6–KR6–ACP6–TE
24. https://doi.org/10.1186/s12915-022-01337-9,
25. https://doi.org/10.1074/jbc.r110.144618,
26. https://doi.org/10.3929/ethz-a-010412088,
27. https://doi.org/10.15488/9866,
28. https://doi.org/10.1038/s41467-023-44497-0,
29. https://doi.org/10.1093/molbev/msi193,
30. https://doi.org/10.1016/s1074-5521(00
31. https://doi.org/10.1074/jbc.m802169200,
32. https://doi.org/10.1371/journal.pone.0229700,
33. https://doi.org/10.1021/ja904792q,
34. https://doi.org/10.1038/nature16993,
35. https://doi.org/10.1038/s41467-020-16376-5,