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

- **PANTHER family:** PTHR11571 — GLUTATHIONE S-TRANSFERASE
- **Subfamily of interest:** PTHR11571:SF150 GLUTATHIONE S-TRANSFERASE
- **Representative member:** OCTS1 (P27013), OCTVU / OCTVU
- **GO term currently propagated at/near this node:** glutathione transferase activity (GO:0004364)

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
3. **Subfamily of interest.** Where does PTHR11571:SF150 GLUTATHIONE S-TRANSFERASE sit — does it carry the
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
**Generated:** 2026-06-24T04:36:57.308099

1. sheehan2001structurefunctionand pages 2-3
2. sheehan2001structurefunctionand pages 9-10
3. chiou1995octopusscrystallinswith pages 4-5
4. tan2016structureofa pages 2-4
5. chiou1995octopusscrystallinswith pages 7-8
6. gavriouchkina2025asinglecellatlas pages 5-6
7. pearson2005phylogeniesofglutathione pages 6-9
8. chuang1999homologymodelingof pages 1-2
9. micic2024overlookedandmisunderstood pages 3-4
10. menon2015thebiologicalroles pages 55-58
11. sheehan2001structurefunctionand pages 7-9
12. sheehan2001structurefunctionand pages 4-6
13. vaish2020glutathionestransferasea pages 10-12
14. vaish2020glutathionestransferasea pages 1-2
15. perez2024sigmaclassglutathionetransferases pages 2-4
16. sheehan2001structurefunctionand pages 3-4
17. perez2024sigmaclassglutathionetransferases pages 4-5
18. perez2024sigmaclassglutathionetransferases pages 10-11
19. sheehan2001structurefunctionand pages 10-10
20. khoury2025aninvitro pages 1-2
21. khoury2025aninvitro pages 15-15
22. khoury2025aninvitro pages 13-15
23. khoury2025aninvitro pages 9-12
24. tan2016structureofa pages 5-6
25. chiou1995octopusscrystallinswith pages 5-5
26. chiou1995octopusscrystallinswith pages 1-2
27. tan2016structureofa pages 6-7
28. perez2024sigmaclassglutathionetransferases pages 5-7
29. https://doi.org/10.1042/0264-6021:3600001,
30. https://doi.org/10.1007/s13205-020-02312-3,
31. https://doi.org/10.1098/rstb.2023.0365,
32. https://doi.org/10.3390/tropicalmed9040085,
33. https://doi.org/10.1016/s0076-6879(05
34. https://doi.org/10.1016/s0006-3495(99
35. https://doi.org/10.1038/srep31176,
36. https://doi.org/10.25911/5d70ef0bed810,
37. https://doi.org/10.3390/biom15091213,
38. https://doi.org/10.1042/bj3090793,
39. https://doi.org/10.1038/s41559-025-02720-9,