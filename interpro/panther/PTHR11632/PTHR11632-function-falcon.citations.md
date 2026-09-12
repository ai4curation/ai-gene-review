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

- **PANTHER family:** PTHR11632 — SUCCINATE DEHYDROGENASE 2 FLAVOPROTEIN SUBUNIT
- **Subfamily of interest:** PTHR11632:SF51 SUCCINATE DEHYDROGENASE [UBIQUINONE] FLAVOPROTEIN SUBUNIT, MITOCHONDRIAL
- **Representative member:** Q72DT2 (Q72DT2), DESVH / DESVH
- **GO term currently propagated at/near this node:** succinate dehydrogenase activity (GO:0000104)

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
3. **Subfamily of interest.** Where does PTHR11632:SF51 SUCCINATE DEHYDROGENASE [UBIQUINONE] FLAVOPROTEIN SUBUNIT, MITOCHONDRIAL sit — does it carry the
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
**Generated:** 2026-06-24T04:30:04.231025

1. cheng2015redoxstateof pages 6-7
2. tran2011thefunctionof pages 34-39
3. maklashina2016bindingofthe pages 9-10
4. cheng2015redoxstateof pages 1-2
5. kim2013emergingconceptsin pages 2-3
6. zhang2025structuralbasisof pages 3-5
7. sharma2019maturationofthe pages 4-6
8. kim2012flavinylationandassembly pages 1-1
9. maklashina2006fumaratereductaseand pages 1-2
10. maklashina2006fumaratereductaseand pages 7-8
11. maklashina2006fumaratereductaseand pages 4-5
12. maklashina2006fumaratereductaseand pages 3-4
13. zaunmuller2006succinatedehydrogenasefunctioning pages 1-2
14. zaunmuller2006succinatedehydrogenasefunctioning pages 2-3
15. zaunmuller2006succinatedehydrogenasefunctioning pages 7-8
16. zaunmuller2006succinatedehydrogenasefunctioning pages 6-7
17. zaunmuller2006succinatedehydrogenasefunctioning pages 3-4
18. zaunmuller2006succinatedehydrogenasefunctioning pages 4-6
19. light2019extracellularelectrontransfer pages 2-3
20. light2019extracellularelectrontransfer pages 3-4
21. light2019extracellularelectrontransfer pages 4-5
22. light2019extracellularelectrontransfer pages 5-5
23. light2019extracellularelectrontransfer pages 1-1
24. cheng2015redoxstateof pages 7-9
25. maklashina2006fumaratereductaseand pages 6-7
26. light2019extracellularelectrontransfer pages 1-2
27. light2019extracellularelectrontransfer pages 6-6
28. UBIQUINONE
29. https://doi.org/10.1016/j.bbabio.2013.01.012,
30. https://doi.org/10.1021/bi501350j,
31. https://doi.org/10.1016/j.sbi.2019.01.027,
32. https://doi.org/10.1074/jbc.m112.405704,
33. https://doi.org/10.7939/r3jd33,
34. https://doi.org/10.1074/jbc.m512544200,
35. https://doi.org/10.1099/mic.0.28849-0,
36. https://doi.org/10.1073/pnas.1915678116,
37. https://doi.org/10.1074/jbc.m115.690396,
38. https://doi.org/10.1038/s41467-025-65828-3,