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

- **PANTHER family:** PTHR43201 — ACYL-COA SYNTHETASE
- **Subfamily of interest:** PTHR43201:SF32 2-SUCCINYLBENZOATE--COA LIGASE
- **Representative member:** fcs (Q88HK0), PSEPK / PSEPK
- **GO term currently propagated at/near this node:** medium-chain fatty acid-CoA ligase activity (GO:0031956)

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
3. **Subfamily of interest.** Where does PTHR43201:SF32 2-SUCCINYLBENZOATE--COA LIGASE sit — does it carry the
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
**Generated:** 2026-06-24T04:36:47.789351

1. lux2019targetingadenylateformingenzymes pages 2-4
2. meganathan2009biosynthesisofmenaquinone pages 8-9
3. gulick2009conformationaldynamicsin pages 2-4
4. gulick2009conformationaldynamicsin pages 1-2
5. gulick2009conformationaldynamicsin pages 4-5
6. gulick2009conformationaldynamicsin pages 5-7
7. gulick2009conformationaldynamicsin pages 7-8
8. khurana2010genomescaleprediction pages 1-3
9. khurana2010genomescaleprediction pages 3-4
10. khurana2010genomescaleprediction pages 4-6
11. khurana2010genomescaleprediction pages 6-8
12. khurana2010genomescaleprediction pages 10-13
13. li2015structuralbasisfor pages 3-4
14. li2015structuralbasisfor pages 1-3
15. li2015structuralbasisfor pages 5-6
16. li2015structuralbasisfor pages 7-8
17. boersch2018menaquinonebiosynthesisinhibition pages 2-3
18. evans2019structurebaseddesignsynthesis pages 8-10
19. evans2019structurebaseddesignsynthesis pages 1-3
20. mohan2025biotransformationofferulic pages 5-10
21. mohan2025biotransformationofferulic pages 10-12
22. priyadarshan2018fattyacylampligases pages 1-2
23. gulick2009conformationaldynamicsin pages 12-14
24. khurana2010genomescaleprediction pages 13-14
25. evans2019structurebaseddesignsynthesis pages 17-22
26. evans2019structurebaseddesignsynthesis pages 3-5
27. boersch2018menaquinonebiosynthesisinhibition pages 1-2
28. li2015structuralbasisfor pages 10-11
29. mohan2025biotransformationofferulic pages 1-2
30. https://doi.org/10.1021/cb900156h,
31. https://doi.org/10.1038/s41429-019-0171-2,
32. https://doi.org/10.1186/1471-2105-11-57,
33. http://www.jlr.org
34. https://doi.org/10.1194/jlr.m700378-jlr200,
35. https://doi.org/10.1016/j.str.2015.08.012,
36. https://doi.org/10.1128/ecosalplus.3.6.3.3,
37. https://doi.org/10.1039/c7ra12950e,
38. https://doi.org/10.1021/acs.biochem.9b00003,
39. https://doi.org/10.1099/mic.0.000533,
40. https://doi.org/10.1007/s13399-025-06646-x,
41. https://doi.org/10.1007/s41745-018-0084-2,