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

- **PANTHER family:** PTHR10681 — THIOREDOXIN PEROXIDASE
- **Subfamily of interest:** PTHR10681:SF121 ALKYL HYDROPEROXIDE REDUCTASE C
- **Representative member:** ahpC (Q88K52), PSEPK / PSEPK
- **GO term currently propagated at/near this node:** thioredoxin peroxidase activity (GO:0008379)

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
3. **Subfamily of interest.** Where does PTHR10681:SF121 ALKYL HYDROPEROXIDE REDUCTASE C sit — does it carry the
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
**Generated:** 2026-06-24T05:02:40.743812

1. perkins2015peroxiredoxinsguardiansagainst pages 2-3
2. groot2022thiolreductasesin pages 16-17
3. zhang2019molecularmechanismsof pages 4-5
4. vaskova2023glutathionerelatedenzymesand pages 10-11
5. xue2024unveilingthesignificance pages 1-3
6. lagal2024lossofperoxiredoxin pages 5-6
7. qausain2024unravelingtheperoxidase pages 1-3
8. zhang2019molecularmechanismsof pages 7-9
9. thapa2023theroleof pages 2-4
10. thapa2023theroleof pages 1-2
11. jia2023antioxidantandprooxidant pages 9-11
12. groot2022thiolreductasesin pages 30-31
13. jia2023antioxidantandprooxidant pages 3-4
14. zhang2019molecularmechanismsof pages 5-7
15. zhang2019molecularmechanismsof pages 1-2
16. https://doi.org/10.1016/j.tibs.2015.05.001,
17. https://doi.org/10.3390/molecules28031447,
18. https://doi.org/10.7759/cureus.66117,
19. https://doi.org/10.3390/antiox13040449,
20. https://doi.org/10.3389/fmicb.2019.01483,
21. https://doi.org/10.3390/biology12050666,
22. https://doi.org/10.3389/fmicb.2021.626874,
23. https://doi.org/10.3390/cells12010181,
24. https://doi.org/10.1042/bcj20240445,
25. https://doi.org/10.3390/antiox11030561,